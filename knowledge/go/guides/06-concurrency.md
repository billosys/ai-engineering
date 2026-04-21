# Concurrency

Concurrency patterns for goroutines, channels, `sync` primitives, and `context.Context`. Grounded in the *Uber Go Style Guide* (§Guidelines, §Style, §Patterns), the *Google Go Style Guide* (Decisions: Goroutine lifetimes, Synchronous functions, Contexts, Copying, Channel direction; Best Practices: Concurrency documentation, Global state, Program checks), and the concurrency lore that those guides cite (Cheney's *"Never start a goroutine without knowing how it will stop"* and Mills' *"Rethinking Classical Concurrency Patterns"*).

Target environment: **Go 1.22+**, **standard library first**, **`go test -race`** in CI, **`go vet`** + **`staticcheck`** for static analysis.

Concurrency-safe naming, error wrapping, and race-detector test patterns live in adjacent chapters; this one is about the mechanics and design of concurrent code.

---

## CC-01: Never Start a Goroutine Without Knowing How It Will Stop

**Strength**: MUST

**Summary**: Every goroutine must have a predictable exit point: either it runs to completion on its own, or there is a mechanism (channel close, context cancellation, `Stop`/`Shutdown` call) that tells it to stop. Fire-and-forget goroutines leak.

```go
// Bad — no way to stop this goroutine; it runs until the process exits
go func() {
    for {
        flush()
        time.Sleep(delay)
    }
}()

// Good — explicit stop signal and explicit exit notification
var (
    stop = make(chan struct{}) // tells the goroutine to stop
    done = make(chan struct{}) // tells us that the goroutine exited
)
go func() {
    defer close(done)

    ticker := time.NewTicker(delay)
    defer ticker.Stop()
    for {
        select {
        case <-ticker.C:
            flush()
        case <-stop:
            return
        }
    }
}()

// Elsewhere:
close(stop)  // signal
<-done       // wait for exit
```

**Rationale**: Goroutines cost memory for their stack and CPU to be scheduled, and a goroutine blocked on a channel send/receive is never garbage-collected — even if no other goroutine holds the channel. Leaked goroutines accumulate, hold references that block GC, and make programs hard to shut down cleanly. Uber §Don't fire-and-forget goroutines: "every goroutine: must have a predictable time at which it will stop running; or there must be a way to signal to the goroutine that it should stop. In both cases, there must be a way for code to block and wait for the goroutine to finish." Google Decisions §Goroutine lifetimes: "When you spawn goroutines, make it clear when or whether they exit... Goroutines can leak by blocking on channel sends or receives" (Uber §Don't fire-and-forget goroutines; Google Decisions §Goroutine lifetimes; Cheney, *"Never start a goroutine without knowing how it will stop"*).

**See also**: CC-02, CC-03, CC-07

---

## CC-02: Wait for Goroutines to Exit

**Strength**: MUST

**Summary**: For every goroutine your code starts, there must be a way for the caller (or the surrounding function) to block until it finishes. Use `sync.WaitGroup` for N goroutines; use a `chan struct{}` closed on exit for a single goroutine.

```go
// Good — WaitGroup for multiple goroutines
var wg sync.WaitGroup
for _, item := range items {
    wg.Add(1)
    go func(it Item) {
        defer wg.Done()
        process(it)
    }(item)
}
wg.Wait() // blocks until all goroutines have called Done

// Good — done channel for a single goroutine
done := make(chan struct{})
go func() {
    defer close(done)
    doWork()
}()
<-done // blocks until doWork returns

// Bad — function returns while spawned goroutines may still be running
func Run() {
    for _, item := range items {
        go process(item) // no join — goroutines outlive Run
    }
}
```

**Rationale**: Without a join, the surrounding function returns while its goroutines are still alive. They may write to freed resources, log after the program is shutting down, or fail tests non-deterministically. Google Decisions §Goroutine lifetimes: "`wg.Wait()` // Prevent spawned goroutines from outliving this function." Uber §Wait for goroutines to exit describes the same pattern (Uber §Wait for goroutines to exit; Google Decisions §Goroutine lifetimes).

**See also**: CC-01, CC-04

---

## CC-03: Tie Goroutine Lifetime to `context.Context` Cancellation

**Strength**: SHOULD

**Summary**: Pass `context.Context` into long-running goroutines and make them exit when `ctx.Done()` fires. This is the idiomatic stop signal for Go concurrency.

```go
// Good — context cancellation stops the worker
func (w *Worker) Run(ctx context.Context) error {
    var wg sync.WaitGroup
    for item := range w.q {
        wg.Add(1)
        go func(it Item) {
            defer wg.Done()
            process(ctx, it) // process must itself honor ctx
        }(item)
    }
    wg.Wait()
    return ctx.Err() // usually nil or context.Canceled
}

// Good — select on ctx.Done() to interrupt a loop
func poll(ctx context.Context, ticker *time.Ticker) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        case <-ticker.C:
            if err := scrape(ctx); err != nil {
                return err
            }
        }
    }
}

// Bad — no cancellation path
func poll(ticker *time.Ticker) {
    for range ticker.C {
        scrape() // runs forever; caller cannot stop it
    }
}
```

**Rationale**: Context cancellation propagates through the call tree automatically, which means a single `cancel()` at the root shuts down every descendant that honors its context. Google Decisions §Goroutine lifetimes: "Code that follows best practices around context usage often helps make this clear. It is conventionally managed with a `context.Context`." This composes with CC-02: `wg.Wait()` after cancellation ensures a clean exit (Google Decisions §Goroutine lifetimes; Google Best Practices §Documentation conventions: Contexts).

**See also**: CC-01, CC-13, CC-14

---

## CC-04: Use `sync.WaitGroup` Correctly — Add Before Go, Done via Defer

**Strength**: MUST

**Summary**: Call `wg.Add(1)` before `go func() { ... }()`, not inside the goroutine. Call `wg.Done()` via `defer` as the first statement of the goroutine, so panics and early returns still decrement the counter.

```go
// Good
for _, item := range items {
    wg.Add(1)                     // Add before go
    go func(it Item) {
        defer wg.Done()           // Done guaranteed even on panic/return
        process(it)
    }(item)
}
wg.Wait()

// Bad — race: wg.Wait may run before Add in the goroutine executes
for _, item := range items {
    go func(it Item) {
        wg.Add(1)                 // too late
        defer wg.Done()
        process(it)
    }(item)
}

// Bad — early return skips Done(), wg.Wait() hangs forever
go func() {
    wg.Add(1)
    if !precheck() {
        return  // leaked counter
    }
    defer wg.Done()
    process()
}()
```

**Rationale**: `wg.Add` from inside the goroutine races with `wg.Wait` on the main path — `Wait` can observe a counter of 0 before the goroutine runs and return prematurely. Calling `Add` before `go` removes the race. Using `defer wg.Done()` at the top of the goroutine function makes `Done` unconditional, which is the only correct discipline under panics and early returns (Uber §Wait for goroutines to exit).

**See also**: CC-02, CC-05

---

## CC-05: Use `errgroup` for Goroutines That Can Fail

**Strength**: SHOULD

**Summary**: When a group of goroutines can each return an error and you want to cancel the group on the first failure, use `golang.org/x/sync/errgroup` instead of hand-rolling `sync.WaitGroup` + error channel + cancel.

```go
import "golang.org/x/sync/errgroup"

// Good — errgroup cancels the derived context on first error
func fetchAll(ctx context.Context, urls []string) ([]Result, error) {
    g, ctx := errgroup.WithContext(ctx)
    results := make([]Result, len(urls))
    for i, u := range urls {
        i, u := i, u
        g.Go(func() error {
            r, err := fetch(ctx, u)
            if err != nil {
                return err
            }
            results[i] = r
            return nil
        })
    }
    if err := g.Wait(); err != nil {
        return nil, err
    }
    return results, nil
}

// Bad — manual error coordination is error-prone
func fetchAll(urls []string) ([]Result, error) {
    var wg sync.WaitGroup
    errCh := make(chan error, len(urls))
    for _, u := range urls {
        wg.Add(1)
        go func(u string) {
            defer wg.Done()
            if _, err := fetch(u); err != nil {
                errCh <- err
            }
        }(u)
    }
    wg.Wait()
    close(errCh)
    for err := range errCh {
        return nil, err // first error, if any — but what about the rest?
    }
    return nil, nil
}
```

**Rationale**: Orchestrating a group of fallible goroutines correctly is surprisingly subtle: you need a buffered error channel, a cancel function to stop sibling work, and a way to drain the channel. `errgroup.Group` packages all of this. Google Best Practices §Handle errors: "Package `errgroup` provides a convenient abstraction for a group of operations that can all fail or be canceled as a group" (Google Best Practices §Handle errors; `golang.org/x/sync/errgroup` documentation).

**See also**: CC-02, CC-03

---

## CC-06: Never Spawn Goroutines in `init()`

**Strength**: MUST-AVOID

**Summary**: `init()` runs at import time, before `main` has any say. A goroutine started there has no lifetime owner, no stop mechanism, and no error path. If you need a background worker, expose a constructor that starts it and a `Close`/`Stop`/`Shutdown` that stops it.

```go
// Bad — invisible background goroutine for every importer of this package
func init() {
    go doWork()
}

// Good — caller chooses whether to spawn the worker, and can stop it
type Worker struct {
    stop chan struct{}
    done chan struct{}
}

func NewWorker() *Worker {
    w := &Worker{
        stop: make(chan struct{}),
        done: make(chan struct{}),
    }
    go w.run()
    return w
}

func (w *Worker) run() {
    defer close(w.done)
    for {
        select {
        case <-w.stop:
            return
        // ...
        }
    }
}

func (w *Worker) Shutdown() {
    close(w.stop)
    <-w.done
}
```

**Rationale**: `init` runs at import time in undefined order and with no access to configuration, context, or error returns. A goroutine that starts there becomes a background process of every binary that imports the package — tests can't disable it, and the goroutine has no stop channel. Uber §No goroutines in init(): "If a package has need of a background goroutine, it must expose an object that is responsible for managing a goroutine's lifetime. The object must provide a method (`Close`, `Stop`, `Shutdown`, etc.) that signals the background goroutine to stop, and waits for it to exit" (Uber §No goroutines in init(); see also CI-28).

**See also**: CC-01, CC-02

---

## CC-07: Prefer Synchronous APIs; Let Callers Add Concurrency

**Strength**: SHOULD

**Summary**: Design library functions to return results synchronously. If the caller needs concurrency, they can wrap your function in `go`. The reverse — removing concurrency from a function that spawned its own goroutines — is difficult or impossible.

```go
// Good — synchronous; caller decides concurrency
func Fetch(ctx context.Context, url string) ([]byte, error) {
    // ... blocks until done, returns directly
}

// Caller's choice:
data, err := Fetch(ctx, url)            // sequential
// or
g, ctx := errgroup.WithContext(ctx)     // concurrent
for _, u := range urls { /* g.Go(...) */ }

// Bad — function spawns its own goroutine with no way to wait
func Fetch(url string, out chan<- []byte) {
    go func() {
        data, _ := doFetch(url)
        out <- data
    }()
}
// Caller can't join, can't cancel, can't get the error directly
```

**Rationale**: Synchronous functions keep goroutine lifetimes inside a single call frame, which makes them easy to reason about and easy to test (pass inputs, check outputs — no polling, no synchronization). Google Decisions §Synchronous functions: "Synchronous functions return their results directly and finish any callbacks or channel operations before returning. Prefer synchronous functions over asynchronous functions... it is quite difficult (sometimes impossible) to remove unnecessary concurrency at the caller side" (Google Decisions §Synchronous functions; Mills, *"Rethinking Classical Concurrency Patterns"*).

**See also**: CC-01, CC-05

---

## CC-08: `context.Context` Is the First Parameter

**Strength**: MUST

**Summary**: When a function accepts a `context.Context`, it is the first parameter and is conventionally named `ctx`.

```go
// Good
func F(ctx context.Context, req *Request) (*Response, error)
func (s *Server) Handle(ctx context.Context, req *Request) (*Response, error)

// Bad — context as second or later parameter
func F(req *Request, ctx context.Context) (*Response, error)

// Bad — non-"ctx" names
func F(c context.Context, req *Request) (*Response, error)
```

**Rationale**: This is a near-universal convention. `go vet` and `golint`/`revive` flag the wrong position. Consistency lets readers scan call sites for "is a context being threaded here?" by looking at the first argument. Google Decisions §Contexts: "When passed to a function or method, `context.Context` is always the first parameter." Exceptions are limited to HTTP handlers (`req.Context()`), streaming RPC methods, and test functions (`testing.TB.Context()`) (Google Decisions §Contexts).

**See also**: CC-09, CC-10

---

## CC-09: Do Not Store `context.Context` in a Struct

**Strength**: SHOULD

**Summary**: Pass `ctx` explicitly to each method that needs one. Do not add a `ctx` field to a struct.

```go
// Good — each call takes a fresh context
type Client struct {
    conn *Conn
}

func (c *Client) Fetch(ctx context.Context, url string) ([]byte, error) { /* ... */ }
func (c *Client) Post(ctx context.Context, url string, b []byte) error  { /* ... */ }

// Bad — stale/shared context baked into the struct
type Client struct {
    ctx  context.Context // whose context is this? when does it expire?
    conn *Conn
}

func (c *Client) Fetch(url string) ([]byte, error) {
    req, _ := http.NewRequestWithContext(c.ctx, "GET", url, nil)
    // If c.ctx was cancelled five minutes ago, every call fails forever.
}
```

**Rationale**: Contexts are request-scoped: their deadlines and cancellation belong to a single logical operation, not to an object's lifetime. Storing a context in a struct silently couples every method call to one logical operation, usually the first one that constructed the struct. Google Decisions §Contexts: "Do not add a context member to a struct type. Instead, add a context parameter to each method on the type that needs to pass it along. The one exception is for methods whose signature must match an interface in the standard library or in a third party library outside Google's control" (Google Decisions §Contexts; Go blog, *Contexts and structs*).

**See also**: CC-08

---

## CC-10: Never Define Custom Context Types

**Strength**: MUST

**Summary**: Do not create your own `Context` interface or concrete type to replace `context.Context` in function signatures. Always use the standard `context.Context`.

```go
// Bad — custom context undermines interop with every other package
type AppContext interface {
    context.Context
    User() User
    Tracer() Tracer
}

func Process(ctx AppContext, req *Request) error { /* ... */ }

// Good — use context.Value for request-scoped data; keep the type standard
type userKey struct{}

func WithUser(ctx context.Context, u User) context.Context {
    return context.WithValue(ctx, userKey{}, u)
}

func UserFrom(ctx context.Context) (User, bool) {
    u, ok := ctx.Value(userKey{}).(User)
    return u, ok
}

func Process(ctx context.Context, req *Request) error {
    u, _ := UserFrom(ctx)
    // ...
}
```

**Rationale**: Custom contexts don't compose. Every function call that crosses a package boundary would need to translate between `p.Context` and `q.Context`, which is impractical at scale and impossible for automated refactorings that thread contexts through code. Google Decisions §Custom contexts: "Do not create custom context types or use interfaces other than `context.Context` in function signatures. There are no exceptions to this rule... it undermines the ability of the Go team to make Go programs work properly in production" (Google Decisions §Custom contexts).

**See also**: CC-08, CC-11

---

## CC-11: Use `context.Background()` Only at Entry Points

**Strength**: SHOULD

**Summary**: `context.Background()` is the root context. It should be created only in entry points — `main`, `init`-like setup, server frameworks that fabricate per-request contexts, and tests (where `testing.TB.Context()` is preferred since Go 1.24). Library code in the middle of a call chain should accept a context from its caller.

```go
// Good — entry point creates the root
func main() {
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()
    if err := run(ctx); err != nil {
        log.Fatal(err)
    }
}

// Good — library takes ctx from the caller
func LoadUser(ctx context.Context, id int) (*User, error) { /* ... */ }

// Bad — library silently starts a fresh context, discarding caller's deadline
func LoadUser(id int) (*User, error) {
    ctx := context.Background() // ignores caller's cancellation
    return db.Query(ctx, "...", id)
}
```

**Rationale**: If a library function fabricates its own `context.Background()`, it opts out of the caller's deadline, cancellation, and request-scoped values — which defeats the point of contexts. Google Decisions §Contexts: "It is very rare for code in the middle of a callchain to require creating a base context of its own using `context.Background()`. Always prefer taking a context from your caller, unless it's the wrong context... Unless you are implementing a server framework, you shouldn't create contexts with `context.Background()` in library code" (Google Decisions §Contexts).

**See also**: CC-08, CC-12

---

## CC-12: `context.TODO()` Is for Placeholder Contexts, Not Production Paths

**Strength**: CONSIDER

**Summary**: Use `context.TODO()` only when you are midway through adding context propagation to a codebase and genuinely do not yet know which context to plumb in. It is a signal to future readers (and `staticcheck`) that this location needs attention.

```go
// Good — during a refactor, before the caller threads ctx
func loadConfig() (*Config, error) {
    return loadConfigCtx(context.TODO())
}

// Good — the real caller now threads ctx
func run(ctx context.Context) error {
    cfg, err := loadConfigCtx(ctx)
    // ...
}

// Bad — context.TODO left in a finished code path
func Handle(req *Request) (*Response, error) {
    return backend.Fetch(context.TODO(), req) // silently ignores request cancellation
}
```

**Rationale**: `context.Background()` and `context.TODO()` are indistinguishable at runtime, but they carry different meaning for readers. `TODO` says "I know a real context belongs here; I haven't wired it up yet." Leaving it in production code is a latent bug — the request's deadline or cancellation is not being honored. The `go` team's guidance is to prefer `context.TODO()` over `context.Background()` whenever the location *should* have a real context but currently doesn't (Go `context` package documentation; Google Decisions §Contexts).

**See also**: CC-11

---

## CC-13: Prefer `context.WithTimeout` / `WithCancel`; Always `defer cancel()`

**Strength**: MUST

**Summary**: When you derive a cancellable or timed-out context, the returned `cancel` function must be called — always — or the parent-child relationship leaks. `defer cancel()` immediately after the derivation is the safe pattern.

```go
// Good
ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
defer cancel()

resp, err := httpClient.Do(req.WithContext(ctx))
// ...

// Good — cancel on shadowed variable (stomping); still requires defer
func (s *Server) innerHandler(ctx context.Context, req *Request) *Response {
    // Unconditionally cap the deadline for this portion of request handling.
    ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
    defer cancel()
    // ctx here is the capped context
    return s.do(ctx, req)
}

// Bad — cancel never called; resources leak until parent is cancelled
ctx, _ := context.WithTimeout(ctx, 3*time.Second)
resp, err := httpClient.Do(req.WithContext(ctx))

// Bad — conditional shadowing means the outer ctx is used after the if,
// but the inner cancel is deferred only within the block and nothing
// caps the outer path's deadline.
if shortenDeadlines {
    ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
    defer cancel()
    log.Print(ctx)
}
// BUG: "ctx" here is the caller's original context.
```

**Rationale**: `context.WithTimeout` and `context.WithCancel` register the derived context as a child of the parent; failing to call `cancel` leaves that registration alive until the parent itself is cancelled. For short-lived operations this is a minor leak; for long-lived parents (an RPC server's root context), it accumulates forever. `go vet`'s `lostcancel` analyzer catches many of these. Google Best Practices (on stomping vs shadowing): note that `ctx, cancel := ...` inside an `if` shadows the outer `ctx`, which is a different bug — use `ctx, cancel = ...` with a pre-declared `cancel` if you need conditional derivation (Google Best Practices §Shadowing; `go vet` lostcancel).

**See also**: CC-11, CC-12

---

## CC-14: Document Non-Obvious Context Semantics

**Strength**: SHOULD

**Summary**: Callers assume that cancelling a context passed to a function interrupts that function and that the function returns `ctx.Err()` on cancellation. When behavior differs — different error, asynchronous cancellation, required context values — say so in the doc comment.

```go
// Good — default assumption, no need to restate
// Run executes the worker's run loop.
func (Worker) Run(ctx context.Context) error

// Good — non-default: returns nil, not ctx.Err(), on cancellation
// Run executes the worker's run loop.
//
// If the context is cancelled, Run returns a nil error.
func (Worker) Run(ctx context.Context) error

// Good — non-default: separate Stop() for synchronous shutdown
// Run processes work until the context is cancelled or Stop is called.
// Context cancellation is handled asynchronously internally: Run may
// return before all work has stopped. Use Stop for graceful shutdown.
func (Worker) Run(ctx context.Context) error
func (Worker) Stop()

// Bad — restating the default adds no information
// Run executes the worker's run loop.
//
// The method will process work until the context is cancelled and
// accordingly returns an error.
func (Worker) Run(ctx context.Context) error
```

**Rationale**: Assuming the default lets the common case stay terse; documenting non-default semantics explicitly prevents callers from guessing. Google Best Practices §Documentation conventions: Contexts: "It is implied that the cancellation of a context argument interrupts the function... This fact does not need to be restated. Where context behavior is different or non-obvious, it should be expressly documented" (Google Best Practices §Documentation conventions: Contexts).

**See also**: CC-03, CC-24

---

## CC-15: Zero-Value `sync.Mutex` Is Valid — Don't Use a Pointer

**Strength**: SHOULD

**Summary**: `sync.Mutex` and `sync.RWMutex` are usable in their zero state. Declare them as values, not pointers.

```go
// Good
type Cache struct {
    mu    sync.Mutex
    items map[string]Item
}

var c Cache
c.mu.Lock() // works; no init needed

// Bad — unnecessary heap allocation and nil-pointer hazard
type Cache struct {
    mu    *sync.Mutex
    items map[string]Item
}

c := &Cache{mu: &sync.Mutex{}} // if you forget, c.mu.Lock() panics

// Bad — new(sync.Mutex) for a local mutex
mu := new(sync.Mutex)
mu.Lock()
```

**Rationale**: Go is designed so the zero value of the standard synchronization primitives is usable. Pointing to them adds no behavior, costs an allocation, and introduces a nil-pointer failure mode that the value form doesn't have. Uber §Zero-value Mutexes are Valid: "The zero-value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex" (Uber §Zero-value Mutexes are Valid; see also CI-11).

**See also**: CC-16, CC-17

---

## CC-16: Unexported Mutex Field, Not Embedded

**Strength**: SHOULD

**Summary**: When a struct has a mutex, put it in an unexported field named `mu`. Do not embed `sync.Mutex` or `sync.RWMutex` — embedding exports `Lock`/`Unlock` to every caller of your type.

```go
// Good — mutex is an implementation detail
type SMap struct {
    mu   sync.Mutex
    data map[string]string
}

func (m *SMap) Get(k string) string {
    m.mu.Lock()
    defer m.mu.Unlock()
    return m.data[k]
}

// Bad — Lock() and Unlock() are now part of SMap's public API
type SMap struct {
    sync.Mutex
    data map[string]string
}

// External callers can now do m.Lock() and hold the mutex arbitrarily long.
// You've lost control over the locking discipline.
```

**Rationale**: Embedding promotes the embedded type's methods, so `sync.Mutex` embedded in `SMap` makes `SMap.Lock()` and `SMap.Unlock()` callable by anyone. That breaks encapsulation — external code can take the lock and hold it across any operation, preventing the type's own methods from enforcing invariants. Uber §Zero-value Mutexes are Valid: "If you use a struct by pointer, then the mutex should be a non-pointer field on it. Do not embed the mutex on the struct, even if the struct is not exported." Uber §Embedding in Structs lists mutexes as an explicit exception: embedding is not appropriate here because it leaks implementation details (Uber §Zero-value Mutexes are Valid; Uber §Embedding in Structs).

**See also**: CC-15, CC-17

---

## CC-17: Do Not Copy Types Containing a Mutex

**Strength**: MUST

**Summary**: `sync.Mutex`, `sync.RWMutex`, `sync.WaitGroup`, `sync.Once`, `sync.Cond`, `sync.Pool`, and `sync.Map` must not be copied after first use. Types that embed them must also not be copied. Return and pass pointers; prefer pointer receivers on methods that use the mutex.

```go
// Good — pointer receiver; Counter is addressed, never copied
type Counter struct {
    mu   sync.Mutex
    data map[string]int64
}

func (c *Counter) Inc(k string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[k]++
}

func NewCounter() *Counter { return &Counter{data: make(map[string]int64)} }

// Bad — value receiver silently copies Counter (and its Mutex)
func (c Counter) Inc(k string) {  // COPY
    c.mu.Lock()                   // locks the copy's mutex, not the caller's
    defer c.mu.Unlock()
    c.data[k]++                   // but map is a reference, so writes go through
}

// Bad — explicit copy
b1 := bytes.Buffer{}
b2 := b1  // Buffer has internal state that aliases after a copy

// Bad — copying a mutex by passing by value
func update(c Counter) { c.Inc("x") }
```

**Rationale**: `sync.Mutex` and friends track their own state, including which goroutine holds them. A copy desynchronizes that state from the original: two different mutexes now guard what was supposed to be one logical lock. `go vet`'s `copylocks` analyzer catches many such cases. Google Decisions §Copying: "synchronization objects such as `sync.Mutex` must not be copied... In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`... This guidance also applies to copying `sync.Mutex`." Google Best Practices: "If you need a lock or other field that must not be copied in your struct, you can make it a value type to take advantage of zero value initialization. It does mean that the containing type must now be passed via a pointer and not a value" (Google Decisions §Copying; Google Best Practices §Declaring variables with zero values).

**See also**: CC-15, CC-16

---

## CC-18: Lock the Smallest Section That Preserves the Invariant

**Strength**: SHOULD

**Summary**: Hold a mutex for as short a window as correctness allows. Use `defer mu.Unlock()` for simple methods; for longer operations, copy out what you need under the lock and do the slow part unlocked.

```go
// Good — short critical section, defer unlock
func (s *Stats) Inc(k string) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.counters[k]++
}

// Good — copy under lock, compute unlocked
func (s *Stats) Report() string {
    s.mu.Lock()
    snapshot := make(map[string]int, len(s.counters))
    for k, v := range s.counters {
        snapshot[k] = v
    }
    s.mu.Unlock()

    // Formatting is expensive but doesn't need the lock
    return formatReport(snapshot)
}

// Bad — manual Unlock at every return; easy to miss
func (p *Pool) Take() (*Item, error) {
    p.mu.Lock()
    if len(p.free) == 0 {
        p.mu.Unlock()
        return nil, errEmpty
    }
    item := p.free[0]
    p.free = p.free[1:]
    p.mu.Unlock()
    return item, nil
}

// Bad — I/O under a lock stalls every other caller
func (c *Cache) Fetch(k string) ([]byte, error) {
    c.mu.Lock()
    defer c.mu.Unlock()
    return http.Get(c.upstream + k) // network call under lock!
}
```

**Rationale**: `defer mu.Unlock()` is almost always correct and avoids the easy-to-miss unlock-on-return bug. When the critical section contains slow work (I/O, expensive formatting), snapshot the shared state under the lock and finish the work without it. Uber §Defer to Clean Up: "Defer has an extremely small overhead and should be avoided only if you can prove that your function execution time is in the order of nanoseconds. The readability win of using defers is worth the miniscule cost" (Uber §Defer to Clean Up; see also CI-34).

**See also**: CC-15, CC-19

---

## CC-19: Copy Slices and Maps at Concurrency Boundaries

**Strength**: SHOULD

**Summary**: Slices and maps contain pointers to backing storage. If a method receives one from a caller or returns one to a caller, copy it at the boundary — otherwise the caller can mutate the internal state of your type, bypassing your mutex.

```go
// Bad — storing the caller's slice; caller can mutate later and race
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = trips
}

trips := loadTrips()
d.SetTrips(trips)
trips[0] = Trip{}  // also mutates d.trips; no lock held

// Good — copy on entry
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = make([]Trip, len(trips))
    copy(d.trips, trips)
}

// Bad — returning internal map; caller reads without holding the mutex
type Stats struct {
    mu       sync.Mutex
    counters map[string]int
}

func (s *Stats) Snapshot() map[string]int {
    s.mu.Lock()
    defer s.mu.Unlock()
    return s.counters // caller now has a reference to the protected map
}

// Good — copy on exit
func (s *Stats) Snapshot() map[string]int {
    s.mu.Lock()
    defer s.mu.Unlock()
    out := make(map[string]int, len(s.counters))
    for k, v := range s.counters {
        out[k] = v
    }
    return out
}
```

**Rationale**: A mutex only protects the slice/map *header* while the method holds the lock. Once the caller has a reference to the backing array or hash table, they can read and write without synchronization, producing races that the mutex was supposed to prevent. Uber §Copy Slices and Maps at Boundaries: "snapshot is no longer protected by the mutex, so any access to the snapshot is subject to data races" (Uber §Copy Slices and Maps at Boundaries).

**See also**: CC-18, CC-28

---

## CC-20: `sync.RWMutex` When Reads Dominate Heavily

**Strength**: CONSIDER

**Summary**: `sync.RWMutex` allows many readers or one writer. Use it only when reads vastly outnumber writes and profile confirms contention on a plain `Mutex`. Otherwise, `sync.Mutex` is simpler and usually faster.

```go
// Good — read-heavy configuration map
type Config struct {
    mu   sync.RWMutex
    data map[string]string
}

func (c *Config) Get(k string) string {
    c.mu.RLock()
    defer c.mu.RUnlock()
    return c.data[k]
}

func (c *Config) Set(k, v string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[k] = v
}

// Bad — using RWMutex "just in case"; adds bookkeeping without benefit
type Counter struct {
    mu  sync.RWMutex // reads and writes are both mutations here
    val int
}
```

**Rationale**: `RWMutex` has higher per-operation overhead than `Mutex` and can starve writers under heavy read load. Use it as a targeted optimization when profiling shows a plain mutex is the bottleneck and the workload is overwhelmingly read-biased. For contention-tuning details, see chapter 08 (Performance).

**See also**: CC-15, CC-18

---

## CC-21: `sync.Once` for Lazy Initialization

**Strength**: SHOULD

**Summary**: Use `sync.Once` when a value needs to be computed on first use and then reused. It guarantees the initializer runs exactly once, even under concurrent callers, and all later callers observe the fully initialized value.

```go
// Good — lazy, thread-safe singleton initialization
var (
    cfgOnce sync.Once
    cfg     *Config
    cfgErr  error
)

func getConfig() (*Config, error) {
    cfgOnce.Do(func() {
        cfg, cfgErr = loadConfig()
    })
    return cfg, cfgErr
}

// Good — amortize expensive test setup
var dataset struct {
    once sync.Once
    data []byte
    err  error
}

func mustLoadDataset(t *testing.T) []byte {
    t.Helper()
    dataset.once.Do(func() {
        dataset.data, dataset.err = os.ReadFile("testdata/dataset")
    })
    if dataset.err != nil {
        t.Fatalf("load: %v", dataset.err)
    }
    return dataset.data
}

// Bad — manual double-checked locking with a mutex; easy to get wrong
```

**Rationale**: `sync.Once.Do` has built-in memory-ordering guarantees: calls that observe `Do` has returned are guaranteed to see the effects of the initializer. Hand-rolled lazy initialization needs explicit memory ordering or a mutex on every access. Google Best Practices §Amortizing common test setup: "Using a `sync.Once` may be appropriate, though not required, if all of the following are true about the common setup: It is expensive. It only applies to some tests. It does not require teardown." Caveat: `sync.Once` cannot respect context cancellation — "the second of two racing calls to the setup function would need to wait for the first call to finish before returning. This period of waiting cannot be easily made to respect the context's cancellation" (Google Best Practices §Amortizing common test setup).

**See also**: CC-22

---

## CC-22: `sync.Pool` Is for Reusable Buffers, Not Cached Objects

**Strength**: CONSIDER

**Summary**: `sync.Pool` holds transient, interchangeable objects (buffers, scratch slices) to reduce allocation pressure. It is not a cache: the runtime may drop any entry at any time, and items must be reset before reuse.

```go
// Good — buffer pool for log formatting
var bufPool = sync.Pool{
    New: func() any { return new(bytes.Buffer) },
}

func formatEntry(e Entry) string {
    buf := bufPool.Get().(*bytes.Buffer)
    buf.Reset() // MUST reset — pool may return a used buffer
    defer bufPool.Put(buf)

    fmt.Fprintf(buf, "%s %s", e.Time, e.Msg)
    return buf.String()
}

// Bad — using Pool as a session cache
var userPool = sync.Pool{
    New: func() any { return &User{} },
}
// Entries get silently dropped; you cannot rely on finding your User again.
```

**Rationale**: The runtime drains `sync.Pool` between GC cycles. Items are only a performance hint, never a persistent store. Use a real cache (or an LRU) if you need durability. Performance tradeoffs (when `sync.Pool` pays off) are covered in chapter 08.

**See also**: CC-21

---

## CC-23: Atomics for Counters and Flags; Mutex for Compound State

**Strength**: SHOULD

**Summary**: `sync/atomic` (including the typed `atomic.Int64`, `atomic.Bool`, `atomic.Pointer[T]` since Go 1.19) is for single-word operations on a single field. Use a mutex as soon as you need to coordinate two fields or implement a read-modify-write that depends on multiple values.

```go
// Good — typed atomic, no mixing of atomic and non-atomic accesses
type Runner struct {
    running atomic.Bool
}

func (r *Runner) Start() {
    if r.running.Swap(true) {
        return // already running
    }
    // start the runner
}

func (r *Runner) IsRunning() bool {
    return r.running.Load()
}

// Bad — raw sync/atomic with easy-to-forget "non-atomic read" bugs
type Runner struct {
    running int32 // "atomic"
}

func (r *Runner) Start() {
    if atomic.SwapInt32(&r.running, 1) == 1 {
        return
    }
}

func (r *Runner) IsRunning() bool {
    return r.running == 1 // RACE: non-atomic read of a field that is atomically written
}

// Bad — atomics cannot coordinate two fields
type Account struct {
    balance atomic.Int64
    txns    atomic.Int64
}
// balance and txns can desynchronize: reading both does not yield a
// consistent snapshot. Use a mutex instead.
```

**Rationale**: Raw `sync/atomic` operates on untyped `int32`/`int64` values, so nothing prevents a non-atomic read of the same variable — a silent data race. Typed `atomic.Bool`/`atomic.Int64`/`atomic.Pointer[T]` hide the underlying word and force every access through the atomic API. Uber §Use go.uber.org/atomic made this point before Go 1.19; the stdlib now provides the same type safety. Atomics still cannot coordinate multiple fields — that requires a mutex or `atomic.Pointer` to a whole snapshot struct (Uber §Use go.uber.org/atomic; Go 1.19 release notes on typed atomics).

**See also**: CC-15, CC-27

---

## CC-24: Document Concurrency Safety — Or Its Absence

**Strength**: SHOULD

**Summary**: Readers assume read-only operations are safe for concurrent use and that mutating operations are not. When the actual behavior deviates from this default, say so in the doc comment.

```go
// Good — default assumption, no remark needed
// Len returns the number of bytes of the unread portion of the buffer.
func (*Buffer) Len() int

// Good — default assumption, no remark needed
// Grow grows the buffer's capacity.
func (*Buffer) Grow(n int)

// Good — unexpected: a "read-only looking" operation mutates internal state
// Lookup returns the data associated with the key from the cache.
//
// This operation is not safe for concurrent use.
func (*Cache) Lookup(key string) (data []byte, ok bool)

// Good — API provides synchronization internally
// NewFortuneTellerClient returns an *rpc.Client for the FortuneTeller service.
// It is safe for simultaneous use by multiple goroutines.
func NewFortuneTellerClient(cc *rpc.ClientConn) *FortuneTellerClient

// Good — interface contract that implementers must honor
// Watcher methods are safe for simultaneous use by multiple goroutines.
type Watcher interface {
    Watch(changed chan<- bool) (unwatch func())
    Health() error
}
```

**Rationale**: Concurrency safety is part of the API contract. An LRU cache's "Lookup" is a reasonable-sounding read, but it mutates recency internally — callers need to know. Conversely, a concurrency-safe type (a client built on an internally synchronized RPC stub, for example) should say so, because the contract affects how callers share the value. Google Best Practices §Documentation conventions: Concurrency: "Go users assume that conceptually read-only operations are safe for concurrent use and do not require extra synchronization... Mutating operations, however, are not assumed to be safe for concurrent use" (Google Best Practices §Documentation conventions: Concurrency).

**See also**: CC-14, CC-25

---

## CC-25: Channels Communicate; Mutexes Guard

**Strength**: CONSIDER

**Summary**: Channels are for passing ownership of a value between goroutines (produce/consume, request/response). Mutexes are for protecting a shared data structure. Use the one that matches the problem; do not mechanically substitute.

```go
// Good — producer owns jobs, hands them off via a channel
func produce(out chan<- Job) {
    defer close(out)
    for _, j := range source() {
        out <- j
    }
}

func consume(in <-chan Job) {
    for j := range in {
        process(j)
    }
}

// Good — shared counter is a data structure; use a mutex
type Counter struct {
    mu sync.Mutex
    n  int
}

func (c *Counter) Inc() { c.mu.Lock(); c.n++; c.mu.Unlock() }

// Bad — channel as a shared counter; correct but awkward
type Counter struct {
    reqs chan func(*int)
    n    int
}

func (c *Counter) Inc() {
    done := make(chan struct{})
    c.reqs <- func(n *int) { *n++; close(done) }
    <-done
}
```

**Rationale**: The Go proverb — "Don't communicate by sharing memory; share memory by communicating" — is a design heuristic, not a command to eliminate mutexes. Pipelines and worker pools fit channels naturally; a counter, cache, or registry fits a mutex. The rough test: if the goroutines are producing and consuming distinct values, use channels; if they're reading and writing a shared data structure, use a mutex. Mills' *"Rethinking Classical Concurrency Patterns"* (linked from both Google Decisions §Goroutine lifetimes and §Synchronous functions) gives practical guidance for the mismatch (Google Decisions §Goroutine lifetimes; Mills, *"Rethinking Classical Concurrency Patterns"*).

**See also**: CC-26, CC-28

---

## CC-26: Channel Size Is Zero (Unbuffered) or One

**Strength**: CONSIDER

**Summary**: Unbuffered channels provide synchronization. A buffer of 1 allows a sender to deliver without blocking when no receiver has arrived yet. Larger buffer sizes should be justified by measurement, not chosen by round numbers.

```go
// Good — unbuffered: send blocks until receive; used for synchronization
done := make(chan struct{})
go func() { work(); close(done) }()
<-done

// Good — buffer of 1: non-blocking first send, typical for result/error
errCh := make(chan error, 1)
go func() { errCh <- doWork() }()

// Suspicious — why 64? what happens when the buffer fills?
c := make(chan int, 64)
```

**Rationale**: Large buffers often paper over a design problem: "the consumer is too slow, so let's give the producer some slack." A too-small buffer still blocks; a too-large buffer just delays the blocking. If the buffer's purpose is "smooth out bursts," measure the burst size and justify the number; if it's "avoid blocking," you probably need a different design. Uber §Channel Size is One or None: "Channels should usually have a size of one or be unbuffered... Any other size must be subject to a high level of scrutiny. Consider how the size is determined, what prevents the channel from filling up under load and blocking writers, and what happens when this occurs" (Uber §Channel Size is One or None; see also CI-36).

**See also**: CC-27, CC-28

---

## CC-27: Specify Channel Direction in Function Signatures

**Strength**: SHOULD

**Summary**: When a function only sends on a channel, declare the parameter as `chan<- T`; when it only receives, declare `<-chan T`. A bidirectional `chan T` in a signature is either a convenience you didn't need or a bug waiting to happen.

```go
// Good — sum only reads
func sum(values <-chan int) int {
    var out int
    for v := range values {
        out += v
    }
    return out
}

// Good — producer only writes
func produce(out chan<- Job) {
    defer close(out)
    for _, j := range source() {
        out <- j
    }
}

// Bad — bidirectional parameter hides intent and allows the "second close" bug
func sum(values chan int) int {
    var out int
    for v := range values {
        out += v
    }
    // values must already be closed for this code to be reachable,
    // which means a second close triggers a panic.
    close(values)
    return out
}
```

**Rationale**: Direction in the signature documents ownership ("who closes?") and lets the compiler enforce it. Closing a receive-only channel is a compile error, not a runtime panic. Google Best Practices §Channel direction: "When the direction is specified, the compiler catches simple errors like this. It also helps to convey a measure of ownership to the type" (Google Best Practices §Channel direction; see also CI-35).

**See also**: CC-28, CC-29

---

## CC-28: The Sender Closes — and Only the Sender

**Strength**: MUST

**Summary**: Close a channel from the sending side, never from the receiving side, never more than once. Closing a closed channel panics. Sending on a closed channel panics. Receiving on a closed channel returns the zero value and `ok=false`.

```go
// Good — sender owns the channel and closes on exit
func produce(out chan<- Job) {
    defer close(out)
    for _, j := range source() {
        out <- j
    }
}

// Good — fan-in: a coordinating goroutine closes after all senders are done
func merge(a, b <-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    forward := func(c <-chan int) {
        defer wg.Done()
        for v := range c {
            out <- v
        }
    }
    wg.Add(2)
    go forward(a)
    go forward(b)
    go func() {
        wg.Wait()
        close(out) // last-writer-wins closing discipline
    }()
    return out
}

// Bad — receiver closes; any still-living sender will panic
func consume(ch chan int) {
    for v := range ch {
        process(v)
    }
    close(ch) // race: if a sender is still running, this panics
}

// Bad — double close
close(ch)
close(ch) // panic: close of closed channel

// Bad — send on a closed channel
ch := make(chan int)
close(ch)
ch <- 1 // panic: send on closed channel
```

**Rationale**: Closing is a signal the sender gives when it has nothing more to send. If a receiver closes, the sender cannot tell the channel is closed without first trying to send (and panicking). With multiple senders, use a `sync.WaitGroup` or counter and close only after all senders have finished — this is the "last-writer-closes" discipline. Google Decisions §Goroutine lifetimes: "Sending on a channel that has been closed causes a panic." Uber's general channel guidance and the stdlib channel documentation agree (Google Decisions §Goroutine lifetimes; Go spec §Close).

**See also**: CC-26, CC-27, CC-29

---

## CC-29: `range` over a Channel Until It Closes

**Strength**: SHOULD

**Summary**: `for v := range ch` receives values until the channel is closed and drained. Use it as the canonical consumer loop. Avoid hand-rolled `for` + `ok`-check unless you genuinely need the `ok` signal.

```go
// Good
for v := range in {
    process(v)
}

// Good — when you need to distinguish "closed" from "zero value"
for {
    v, ok := <-in
    if !ok {
        return // channel closed and drained
    }
    process(v)
}

// Bad — hand-rolled loop that ignores closure
for {
    v := <-in // returns zero value forever after close; infinite loop
    process(v)
}
```

**Rationale**: `range` terminates cleanly on close; the hand-rolled `<-in` does not. The `v, ok := <-ch` form is necessary only when zero-valued data elements are meaningful and you must distinguish them from "channel closed". Go spec §For statements with range clause covers the semantics.

**See also**: CC-27, CC-28, CC-30

---

## CC-30: `select` with `default` for Non-Blocking Operations

**Strength**: SHOULD

**Summary**: A bare receive or send on a channel blocks. A `select` with a `default` case makes it non-blocking. Use this for "try-send" / "try-receive" patterns, not as a substitute for synchronization.

```go
// Good — try-send: drop when the channel is full
func (l *Logger) Emit(e Event) {
    select {
    case l.events <- e:
    default:
        l.dropped.Add(1) // or log a warning
    }
}

// Good — try-receive: peek without blocking
select {
case msg := <-in:
    process(msg)
default:
    // no message ready right now; do other work
}

// Bad — busy loop: spins the CPU at 100%
for {
    select {
    case v := <-in:
        process(v)
    default: // nothing ready; loop immediately
    }
}
```

**Rationale**: `select { default: }` makes the choice "take one if ready, otherwise skip" explicit. Without `default`, `select` blocks until one case is ready — which is usually what you want. Never write `select { default: }` inside a tight `for` loop without a timer or sleep; you will burn a CPU core for nothing.

**See also**: CC-29, CC-31

---

## CC-31: `select` with a Timeout or `ctx.Done()`

**Strength**: SHOULD

**Summary**: Combine a channel receive with either `ctx.Done()` or `time.After` inside a `select` to bound how long the receiver will wait. Prefer `ctx.Done()` — it composes with your caller's deadline; `time.After` creates an untracked timer that leaks until it fires.

```go
// Good — bounded wait via context
func receive(ctx context.Context, in <-chan Msg) (Msg, error) {
    select {
    case m := <-in:
        return m, nil
    case <-ctx.Done():
        return Msg{}, ctx.Err()
    }
}

// Good — local timeout when no context is threaded yet
func receive(in <-chan Msg, timeout time.Duration) (Msg, error) {
    t := time.NewTimer(timeout)
    defer t.Stop() // release the timer early on fast path

    select {
    case m := <-in:
        return m, nil
    case <-t.C:
        return Msg{}, errTimeout
    }
}

// Bad — time.After leaks a timer for the full duration on every call
func receive(in <-chan Msg) (Msg, error) {
    select {
    case m := <-in:
        return m, nil
    case <-time.After(5 * time.Second): // timer created each call; not stopped
        return Msg{}, errTimeout
    }
}
```

**Rationale**: `time.After(d)` returns a channel backed by a timer that lives for the full duration `d`, even if the surrounding `select` is resolved early. In a tight loop, that's a memory leak proportional to the call rate. `time.NewTimer` with `defer t.Stop()` lets you release the timer on the fast path. When a `ctx` is already in scope, using `<-ctx.Done()` is even better — you inherit the caller's deadline.

**See also**: CC-03, CC-30

---

## CC-32: Pipelines — Each Stage Is a Goroutine, Channels Are the Edges

**Strength**: CONSIDER

**Summary**: A pipeline is a series of stages, each a goroutine that receives from an input channel, does work, and sends to an output channel. Each stage owns its output: it closes the output when its input closes and in-flight work is done.

```go
// Generator stage
func gen(ctx context.Context, nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for _, n := range nums {
            select {
            case out <- n:
            case <-ctx.Done():
                return
            }
        }
    }()
    return out
}

// Transform stage
func square(ctx context.Context, in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for n := range in {
            select {
            case out <- n * n:
            case <-ctx.Done():
                return
            }
        }
    }()
    return out
}

// Composition
func run(ctx context.Context) {
    for v := range square(ctx, gen(ctx, 1, 2, 3, 4)) {
        fmt.Println(v)
    }
}
```

**Rationale**: The pattern — "stage owns output, closes on input-close, honors context for early exit" — is the structured-concurrency idiom for Go channels. It avoids goroutine leaks because every stage exits when its input is closed or its context is cancelled. Mills' *"Rethinking Classical Concurrency Patterns"* develops these patterns at length (Google Decisions §Goroutine lifetimes; Mills, *"Rethinking Classical Concurrency Patterns"*).

**See also**: CC-03, CC-27, CC-28, CC-33

---

## CC-33: Fan-Out / Fan-In with a Bounded Worker Pool

**Strength**: CONSIDER

**Summary**: To parallelize N independent units of work across K workers, fan out from one producer channel to K consumer goroutines, then fan in their results into a single channel. Bound K — do not spawn one goroutine per input.

```go
func process(ctx context.Context, inputs []Input) ([]Result, error) {
    const workers = 8

    in := make(chan Input)
    out := make(chan Result)

    g, ctx := errgroup.WithContext(ctx)

    // Producer
    g.Go(func() error {
        defer close(in)
        for _, x := range inputs {
            select {
            case in <- x:
            case <-ctx.Done():
                return ctx.Err()
            }
        }
        return nil
    })

    // Workers (fan-out)
    var wg sync.WaitGroup
    for i := 0; i < workers; i++ {
        wg.Add(1)
        g.Go(func() error {
            defer wg.Done()
            for x := range in {
                r, err := doWork(ctx, x)
                if err != nil {
                    return err
                }
                select {
                case out <- r:
                case <-ctx.Done():
                    return ctx.Err()
                }
            }
            return nil
        })
    }

    // Closer: when all workers are done, close the output
    go func() { wg.Wait(); close(out) }()

    // Fan-in: collect results
    var results []Result
    for r := range out {
        results = append(results, r)
    }
    return results, g.Wait()
}
```

**Rationale**: A bounded worker pool caps concurrency — unlike `go doWork()` per input, which creates arbitrarily many goroutines and can exhaust memory, file descriptors, or downstream capacity. `errgroup.WithContext` provides first-error cancellation; the `sync.WaitGroup` + closer goroutine implements the "last-writer-closes" discipline on the output channel. See Mills' talk for alternative structures (Google Best Practices §Handle errors; Mills, *"Rethinking Classical Concurrency Patterns"*).

**See also**: CC-05, CC-26, CC-28, CC-32

---

## CC-34: Avoid Mutable Package-Level State; Inject Instead

**Strength**: SHOULD-AVOID

**Summary**: Package-level `var`s that are written at runtime are implicit shared state. They force every caller to reason about concurrency and make tests non-parallelizable. Put state in a struct with a constructor, and inject it.

```go
// Bad — hidden shared state, implicit concurrency contract
package sidecar

var registry = make(map[string]*Plugin)

func Register(name string, p *Plugin) error {
    registry[name] = p // not thread-safe; no synchronization documented
    return nil
}

// Good — instance-scoped state with explicit mutex
package sidecar

type Registry struct {
    mu      sync.Mutex
    plugins map[string]*Plugin
}

func New() *Registry {
    return &Registry{plugins: make(map[string]*Plugin)}
}

func (r *Registry) Register(name string, p *Plugin) error {
    r.mu.Lock()
    defer r.mu.Unlock()
    r.plugins[name] = p
    return nil
}

// Caller wires it explicitly:
func main() {
    reg := sidecar.New()
    app.Run(ctx, &app.Config{Registry: reg})
}
```

**Rationale**: Global state creates implicit concurrency contracts that no one can see from a function signature. It also serializes tests (they can't run in parallel if they share package state). Uber §Avoid Mutable Globals: "Avoid mutating global variables, instead opting for dependency injection." Google Best Practices §Global state: "This creates an order-dependent test case, which breaks running with test filters, and prevents tests from running in parallel or being sharded" (Uber §Avoid Mutable Globals; Google Best Practices §Global state; see also CI-29).

**See also**: CC-06, CC-15

---

## CC-35: `t.Fatal` Only from the Test Goroutine

**Strength**: MUST

**Summary**: `t.FailNow`, `t.Fatal`, and `t.Fatalf` must be called only from the goroutine running the test function. From child goroutines, use `t.Error` / `t.Errorf` and return.

```go
// Good — error from worker goroutines, fatal only from the test goroutine
func TestEngine(t *testing.T) {
    engine, err := Start()
    if err != nil {
        t.Fatalf("Start: %v", err) // OK: test goroutine
    }

    var wg sync.WaitGroup
    wg.Add(N)
    for i := 0; i < N; i++ {
        go func() {
            defer wg.Done()
            if err := engine.Vroom(); err != nil {
                t.Errorf("Vroom: %v", err) // NOT t.Fatalf
                return
            }
        }()
    }
    wg.Wait()

    if seen := engine.NumVrooms(); seen != N {
        t.Errorf("NumVrooms = %d, want %d", seen, N) // OK: test goroutine
    }
}

// Bad — t.Fatal from worker goroutine
go func() {
    if err := engine.Vroom(); err != nil {
        t.Fatalf("Vroom: %v", err) // illegal: doesn't stop the test cleanly
    }
}()
```

**Rationale**: `t.FailNow` calls `runtime.Goexit` on the goroutine that invokes it — which works when that goroutine *is* the test, but stops only the worker goroutine otherwise. The test function itself keeps running, possibly accessing already-cleaned-up state. Google Best Practices §Don't call t.Fatal from separate goroutines: "it is incorrect to call `t.FailNow`, `t.Fatal`, etc. from any goroutine but the one running the Test function (or the subtest). If your test starts new goroutines, they must not call these functions from inside these goroutines" (Google Best Practices §Don't call t.Fatal from separate goroutines; `testing.T` documentation).

**See also**: CC-02

---

## CC-36: Run the Race Detector in CI

**Strength**: SHOULD

**Summary**: Enable `go test -race` for the full test suite in continuous integration. The race detector finds data races — concurrent accesses to the same memory where at least one is a write, without synchronization — that testing alone cannot reliably surface.

```bash
# In CI
go test -race ./...
```

```go
// A race the detector will catch
type Stats struct {
    counters map[string]int // no mutex
}

func (s *Stats) Inc(k string) { s.counters[k]++ }

// From parallel test or production traffic:
//   WARNING: DATA RACE
//   Write at 0x... by goroutine N
//   Previous write at 0x... by goroutine M
```

**Rationale**: Data races are undefined behavior in Go. Concurrency-safety guidelines are necessary but not sufficient — the race detector provides empirical confirmation. Run it in CI because races are often non-deterministic and may not surface under ordinary test loads. (Detailed race-test patterns — parallel tests, `t.Parallel`, goroutine leak detection — live in chapter 07.)

**See also**: CC-15, CC-19, CC-23

---

## CC-37: Make the Happens-Before Relationship Explicit

**Strength**: CONSIDER

**Summary**: The Go memory model defines which reads are guaranteed to observe which writes. A read is guaranteed to see a write only if the two are ordered by a *happens-before* relationship — most commonly established by channel operations, mutex Lock/Unlock, `sync.Once.Do`, or `WaitGroup.Wait`. Rely on these primitives, not on timing or "it seemed to work".

```go
// Good — channel send happens-before matching receive; close happens-before receive
var result int
ch := make(chan struct{})
go func() {
    result = compute()
    close(ch) // close happens-before receive
}()
<-ch
fmt.Println(result) // safe: result write happens-before this read

// Good — sync.Once.Do happens-before subsequent Do returns
var (
    once sync.Once
    cfg  *Config
)
getConfig := func() *Config {
    once.Do(func() { cfg = loadConfig() })
    return cfg // safe: load happens-before every subsequent read
}

// Bad — no happens-before relationship between the two goroutines
var ready bool
var data Data

go func() {
    data = load()
    ready = true // write
}()

for !ready {} // read with no synchronization — race, may loop forever
_ = data
```

**Rationale**: Without a happens-before ordering, a reader may observe the older of two writes, observe a partially-initialized value, or loop forever because the compiler caches the check in a register. The standard synchronization primitives (channels, mutexes, `sync.Once`, atomics with appropriate ordering) provide the guarantees; naive reads and writes of shared variables do not. This is a quick practical framing — the full Go memory model spec is the authoritative reference (Go spec §The Go memory model).

**See also**: CC-21, CC-23, CC-36

---

## CC-38: Nil the Channel After Close to Disable a select Case

**Strength**: SHOULD

**Summary**: After a channel is closed, reads from it return the zero value immediately, so a `select` case over that channel fires continuously and pegs a CPU. Set the channel variable to `nil` once you observe the closed signal — a nil channel blocks forever in `select`, cleanly disabling the case.

```go
// Bad — after ch is closed, this loops at 100% CPU
for {
    select {
    case v := <-ch:
        process(v)   // keeps firing with zero values
    case <-done:
        return
    }
}

// Good — nil the channel after it closes
for {
    select {
    case v, ok := <-ch:
        if !ok {
            ch = nil // nil channel blocks forever, disables this case
            continue
        }
        process(v)
    case <-done:
        return
    }
}
```

**Rationale**: A closed channel is *always* ready to receive (it yields the zero value with `ok=false`), so in a `select` its case is selectable on every iteration and starves the other cases. Assigning `nil` takes the case out of the random selection set without changing the loop structure, letting the `select` continue servicing remaining channels until `done` fires (cc-skills-golang/skills/golang-troubleshooting/references/common-go-bugs.md).

**See also**: CC-28, CC-29, CC-30

---

## CC-39: Reuse a time.Timer Instead of time.After in select Loops

**Strength**: SHOULD

**Summary**: `time.After` inside a `select` loop allocates a fresh timer on every iteration; each one stays referenced by the runtime until it fires, producing a slow leak under load. Create a single `time.Timer` outside the loop and `Reset` it on each branch so only one timer ever exists.

```go
// Bad — leaks a timer on every iteration until it fires
for {
    select {
    case msg := <-ch:
        handle(msg)
    case <-time.After(5 * time.Second):
        handleTimeout()
    }
}

// Good — reuse the timer
timer := time.NewTimer(5 * time.Second)
defer timer.Stop()
for {
    select {
    case msg := <-ch:
        if !timer.Stop() { <-timer.C }
        timer.Reset(5 * time.Second)
        handle(msg)
    case <-timer.C:
        handleTimeout()
        timer.Reset(5 * time.Second)
    }
}
```

**Rationale**: `time.After` is fine for one-shot uses but in a hot `select` loop every call creates a timer that cannot be garbage collected until its deadline elapses — memory grows proportionally to iteration rate times timeout. Reusing a single `time.Timer` with `Reset` keeps the timer count at one regardless of loop speed; the `!timer.Stop()` drain pattern avoids a stale value sitting on `timer.C` (cc-skills-golang/skills/golang-concurrency/references/channels-and-select.md).

**See also**: CC-31

---

## CC-40: Use Directional Channel Types in Function Signatures

**Strength**: SHOULD

**Summary**: Declare channel parameters as `chan<- T` (send-only) or `<-chan T` (receive-only) to document the function's role and let the compiler reject misuse such as a consumer accidentally closing or sending on its input.

```go
// Bad — caller could accidentally close or send on a receive-only channel
func consume(ch chan int) { ... }

// Good — compiler enforces correct usage
func produce(ch chan<- int) { ... } // send-only
func consume(ch <-chan int) { ... } // receive-only
```

**Rationale**: A bidirectional `chan T` in a parameter is an API that allows every operation, including `close`, which is almost always wrong for a consumer and gets the ownership rule in CC-28 violated. Directional types push the constraint into the type system so the compiler, not code review, catches the mistake (cc-skills-golang/skills/golang-concurrency/references/channels-and-select.md).

**See also**: CC-27, CC-28

---

## CC-41: wg.Add Before Launching the Goroutine, Not Inside It

**Strength**: MUST

**Summary**: Call `wg.Add(1)` on the goroutine that *launches* the worker, before the `go` statement. Calling `Add` from inside the new goroutine races with `wg.Wait` — the waiter may observe a zero counter and return before any worker has had a chance to increment it.

```go
// Bad — Add inside the goroutine
var wg sync.WaitGroup
for i := 0; i < n; i++ {
    go func() {
        wg.Add(1) // may run after wg.Wait() returns
        defer wg.Done()
        doWork()
    }()
}
wg.Wait()

// Good
for i := 0; i < n; i++ {
    wg.Add(1) // called BEFORE launching the goroutine
    go func() {
        defer wg.Done()
        doWork()
    }()
}
wg.Wait()
```

**Rationale**: `WaitGroup.Wait` returns when the counter reaches zero; if every `Add` happens asynchronously from within the goroutine, the first call to `Wait` can legally see zero and proceed, even though the goroutines have not yet started. The bug is timing-dependent and typically only surfaces under load or on slower machines. Always pair `Add` with the `go` statement that launches the work (cc-skills-golang/skills/golang-troubleshooting/references/common-go-bugs.md).

**See also**: CC-04, CC-02

---

## CC-42: Every Goroutine Needs Its Own defer recover

**Strength**: MUST

**Summary**: `recover` only catches panics in the *same* goroutine that defers it. A parent's `recover` cannot save a child goroutine that panics — the unhandled panic crashes the whole process. Every goroutine that can panic must install its own `defer func() { recover() }()`.

```go
// Bad — parent recover() cannot catch child panic
func main() {
    defer func() { recover() }() // never catches child panic
    go func() { panic("crash!") }() // crashes the program
    time.Sleep(time.Second)
}

// Good — each goroutine recovers its own panics
go func() {
    defer func() {
        if r := recover(); r != nil {
            log.Printf("goroutine recovered: %v", r)
        }
    }()
    doWork(ctx)
}()
```

**Rationale**: Panic propagation is per-goroutine: the runtime walks only the panicking goroutine's defer stack, so a protective `recover` elsewhere is invisible. For long-running services this means a single buggy handler can take down every other in-flight request. Wrap goroutine entry points with a recovery helper and log the stack so the bug is still visible (cc-skills-golang/skills/golang-concurrency/references/channels-and-select.md).

**See also**: CC-01, CC-02

---

## CC-43: Always defer cancel() on Derived Contexts

**Strength**: MUST

**Summary**: Every `context.WithCancel`, `WithTimeout`, or `WithDeadline` returns a `cancel` function whose call releases the associated timer and tracker goroutine. Discarding it — typically with `_` — leaks those resources even when the deadline expires naturally.

```go
// Bad — cancel is discarded, resources leak
func fetch(ctx context.Context) error {
    ctx, _ = context.WithTimeout(ctx, 5*time.Second)
    return doWork(ctx)
}

// Good — defer cancel immediately
func fetch(ctx context.Context) error {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    return doWork(ctx)
}
```

**Rationale**: Derived contexts allocate bookkeeping (a timer for deadlines, a child registered on the parent's cancel tree) that is only reclaimed when `cancel` runs. Relying on the deadline alone still leaks the parent-tree entry, and `go vet` now flags the pattern. Adopt the reflex of writing `defer cancel()` on the line immediately after `WithTimeout`/`WithCancel`/`WithDeadline` (cc-skills-golang/skills/golang-context/references/cancellation.md).

**See also**: CC-13

---

## CC-44: Thread Context Through with *Context Method Variants

**Strength**: SHOULD

**Summary**: When you have a `ctx`, use the context-aware downstream API: `http.NewRequestWithContext`, `db.QueryContext`, `db.ExecContext`, and so on. Context-less variants ignore cancellation, so a client disconnect or upstream timeout does not free the in-flight work.

```go
// Bad — downstream call ignores the request context
func (c *PaymentClient) Charge(ctx context.Context, amount int) error {
    req, _ := http.NewRequest("POST", c.url+"/charge", body)
    return c.client.Do(req)
}

// Good — all downstream operations respect the context
func (c *PaymentClient) Charge(ctx context.Context, amount int) error {
    req, err := http.NewRequestWithContext(ctx, "POST", c.url+"/charge", body)
    if err != nil { return fmt.Errorf("creating request: %w", err) }
    return c.client.Do(req)
}
```

**Rationale**: Propagating the context is the mechanism by which cancellation and deadlines reach the socket or database driver. A call made with `http.NewRequest` (no context) will run to completion even after the caller has disconnected, holding a connection open and burning downstream capacity. The `*Context` variants thread the signal the whole way down (cc-skills-golang/skills/golang-context/references/http-services.md).

**See also**: CC-03, CC-08, CC-13

---

## CC-45: Use an Unexported Named Type for Context Keys

**Strength**: MUST

**Summary**: `context.Value` lookups are keyed by Go equality on the key. Two packages using the same `string` literal will collide. Declare an unexported named type in your package and use typed constants as keys so the type itself is unique.

```go
// Bad — string keys collide across packages
ctx = context.WithValue(ctx, "trace_id", traceID)

// Good — unexported key type prevents collisions
type contextKey string
const traceIDKey contextKey = "trace_id"

func WithTraceID(ctx context.Context, traceID string) context.Context {
    return context.WithValue(ctx, traceIDKey, traceID)
}
```

**Rationale**: Go equality on interface values compares both dynamic type and value; an unexported type cannot be named from outside the package, so no foreign caller can construct a colliding key even with the same underlying string. This is both a correctness fix (packages can't clobber each other) and a mild encapsulation win — consumers must go through your accessor functions (cc-skills-golang/skills/golang-context/references/values-tracing.md).

**See also**: CC-10

---

## CC-46: Detach Cancellation with context.WithoutCancel for Fire-and-Forget

**Strength**: CONSIDER

**Summary**: Background work spawned from a request handler — audit logs, analytics events — usually shouldn't die when the client disconnects, but also shouldn't lose the trace IDs and user info carried on the request context. `context.WithoutCancel` (Go 1.21+) keeps the values while detaching cancellation.

```go
// Bad — background audit log dies if the client disconnects
go h.auditService.LogOrderCreated(ctx, order)

// Good — detach cancellation, keep trace values
auditCtx := context.WithoutCancel(ctx)
go h.auditService.LogOrderCreated(auditCtx, order)
```

**Rationale**: If you forward `ctx` directly the background goroutine is cancelled the moment the handler returns — a surprise that loses audit entries under normal traffic. Switching to `context.Background()` fixes the cancellation but drops `trace_id`, `user_id`, and any other request-scoped values, hurting observability. `WithoutCancel` is the precise tool: same value chain, no cancellation propagation. Pair with a bounded background pool (CC-50) so detached work can't spawn unboundedly (cc-skills-golang/skills/golang-context/references/cancellation.md).

**See also**: CC-43, CC-50

---

## CC-47: Graceful Shutdown via signal.NotifyContext

**Strength**: SHOULD

**Summary**: Wire `signal.NotifyContext` to SIGINT/SIGTERM at program start, block `main` on `<-ctx.Done()`, then call `srv.Shutdown` with its own bounded timeout context so in-flight requests drain before the process exits.

```go
// Bad: no graceful shutdown
func main() {
    srv := &http.Server{Addr: ":8080"}
    go srv.ListenAndServe()
    // Server runs forever; no way to drain connections
}

// Good: graceful shutdown
func main() {
    ctx, stop := signal.NotifyContext(context.Background(),
        syscall.SIGINT, syscall.SIGTERM)
    defer stop()
    
    srv := &http.Server{Addr: ":8080", Handler: handler}
    
    go func() {
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            slog.Error("server error", "err", err)
            stop()
        }
    }()
    
    slog.Info("server started", "addr", ":8080")
    <-ctx.Done()
    slog.Info("shutting down")
    
    shutdownCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    
    if err := srv.Shutdown(shutdownCtx); err != nil {
        slog.Error("shutdown error", "err", err)
    }
}
```

**Rationale**: Without this pattern the orchestrator's SIGTERM becomes an abrupt kill: open connections are reset, requests fail with truncated bodies, and post-commit side effects may be half-applied. `signal.NotifyContext` gives you a single context whose cancellation means "start shutdown"; a separate timeout context bounds the drain so a stuck handler can't keep the process alive forever. The server's `ListenAndServe` returns `http.ErrServerClosed` on a clean shutdown, which is not an error condition (claude-skills (saisudhir14)/references/patterns.md).

**See also**: CC-01, CC-03, CC-13

---

## CC-48: Channels of Channels for Non-Blocking Reply Routing

**Strength**: CONSIDER

**Summary**: When a server goroutine multiplexes many concurrent requests, embed a reply channel inside the request struct. Each client owns the path its answer returns on, so the server can reply without a shared response queue, mutex, or map of correlation IDs.

```go
// Bad: Requires mutex-based request/response queuing
type Request struct {
    args []int
    // caller has no direct path for reply
}

type result struct {
    err error
    val int
}

var responses = make(chan result)

// Good: Channels of channels for natural request/response multiplexing
type Request struct {
    args       []int
    f          func([]int) int
    resultChan chan int
}

request := &Request{[]int{3, 4, 5}, sum, make(chan int)}
clientRequests <- request
fmt.Printf("answer: %d\n", <-request.resultChan)

func handle(queue chan *Request) {
    for req := range queue {
        req.resultChan <- req.f(req.args)
    }
}
```

**Rationale**: A single shared response channel forces callers to demultiplex by inspecting IDs, reintroducing the mutex you were trying to avoid. Putting the reply channel on the request makes the response path implicit in the message, which also generalises cleanly to rate limiting and worker pools — the reply channel is just another field. Pattern comes from Effective Go but is rarely shown with an explicit contrast (golang-skills (cxuu)/skills/go-concurrency/references/ADVANCED-PATTERNS.md).

**See also**: CC-25, CC-33

---

## CC-49: Partition CPU-Bound Work with runtime.NumCPU and WaitGroup

**Strength**: CONSIDER

**Summary**: For CPU-bound work on independent data (vector operations, matrix transforms, batch encoding), split the range into `runtime.NumCPU()` chunks and process them concurrently with a `WaitGroup`. Use `runtime.GOMAXPROCS(0)` instead if you want to honour operator tuning rather than hardware.

```go
// Bad: Sequential processing doesn't use available cores
func (v Vector) DoAll(u Vector) {
    for i := 0; i < len(v); i++ {
        v[i] += u.Op(v[i])
    }
}

// Good: Parallel processing leverages all CPU cores
func (v Vector) DoAll(u Vector) {
    numCPU := runtime.NumCPU()
    var wg sync.WaitGroup
    wg.Add(numCPU)
    for i := 0; i < numCPU; i++ {
        go func(i int) {
            defer wg.Done()
            v.DoSome(i*len(v)/numCPU, (i+1)*len(v)/numCPU, u)
        }(i)
    }
    wg.Wait()
}
```

**Rationale**: Go's scheduler won't parallelise a single tight loop — only the program can, by splitting the work. One goroutine per core is the sweet spot for CPU-bound tasks: more goroutines add scheduling overhead without adding parallelism, and fewer leaves cores idle. Prefer `runtime.GOMAXPROCS(0)` when you run in cgroups or containers where the operator has capped parallelism below the hardware core count. The pattern is inappropriate for IO-bound work, where the concurrency level should come from target latency, not CPU count (golang-skills (cxuu)/skills/go-concurrency/references/ADVANCED-PATTERNS.md).

**See also**: CC-33, CC-50

---

## CC-50: Bound Concurrency with a Buffered-Channel Semaphore

**Strength**: MUST

**Summary**: Never launch one goroutine per input item unbounded. A buffered channel of capacity `maxWorkers` used as a semaphore — send before `go`, receive on exit — caps how many workers run at once and prevents memory and downstream-resource exhaustion.

```go
// Bad: Spawns len(items) goroutines at once — can exhaust memory
var wg sync.WaitGroup
for _, item := range items {
    wg.Add(1)
    go func(it Item) {
        defer wg.Done()
        process(it)
    }(item)
}
wg.Wait()

// Good: Semaphore limits concurrency to maxWorkers
var wg sync.WaitGroup
sem := make(chan struct{}, maxWorkers)
for _, item := range items {
    wg.Add(1)
    sem <- struct{}{}
    go func(it Item) {
        defer wg.Done()
        defer func() { <-sem }()
        process(it)
    }(item)
}
wg.Wait()
```

**Rationale**: Unbounded goroutine spawning is the canonical way to take down a Go service: one request with a big slice can allocate gigabytes of goroutine stacks, open more DB connections than the pool permits, or saturate an upstream service. A buffered channel is the smallest semaphore primitive in the language — the send blocks when `maxWorkers` tokens are held, providing natural backpressure without any extra coordination (golang-skills (cxuu)/skills/go-concurrency/references/ADVANCED-PATTERNS.md).

**See also**: CC-33, CC-46

---

## CC-51: Always defer wg.Done() in the Goroutine

**Strength**: MUST

**Summary**: Place `defer wg.Done()` as the first line of every goroutine you launch against a `WaitGroup`. Any path that returns without calling `Done` — an early return, a panic, a forgotten branch — leaves the counter positive and `wg.Wait` deadlocks forever.

```go
// Bad: Missing wg.Done() — deadlocks
var wg sync.WaitGroup
wg.Add(1)
go func() {
    doWork()
    // forgot to call wg.Done()
}()
wg.Wait() // blocks forever

// Good: Always defer wg.Done()
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    doWork()
}()
wg.Wait()
```

**Rationale**: `WaitGroup.Wait` only returns when the internal counter hits zero, so a single missed `Done` means permanent blocking — which in production looks like a hung shutdown or a leaked request handler. `defer` makes correctness structural: it runs on every exit path, including panics, which is also why it composes cleanly with goroutine-local `recover` (see CC-42) (golang-skills (cxuu)/skills/go-concurrency/references/ADVANCED-PATTERNS.md).

**See also**: CC-04, CC-41, CC-42

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Know how the goroutine stops | MUST | Every goroutine needs a predictable exit |
| 02 | Wait for goroutines to exit | MUST | `WaitGroup` for N, `chan struct{}` for 1 |
| 03 | Tie lifetime to `ctx.Done()` | SHOULD | Context cancellation is the stop signal |
| 04 | `WaitGroup`: Add before go, defer Done | MUST | Avoid the classic race and leaked counter |
| 05 | Use `errgroup` for fallible groups | SHOULD | First-error cancellation + join |
| 06 | No goroutines in `init()` | MUST-AVOID | Expose a constructor + `Shutdown` |
| 07 | Prefer synchronous APIs | SHOULD | Callers can add concurrency; not the reverse |
| 08 | `ctx` is the first parameter | MUST | Named `ctx`, always position 1 |
| 09 | Don't store `ctx` in a struct | SHOULD | Per-call, not per-object |
| 10 | No custom `Context` types | MUST | Use `ctx.Value` for request-scoped data |
| 11 | `Background()` only at entry points | SHOULD | Library code takes `ctx` from the caller |
| 12 | `TODO()` marks unfinished wiring | CONSIDER | Not for production code paths |
| 13 | `WithTimeout`/`WithCancel` + `defer cancel()` | MUST | Always free the derived context |
| 14 | Document non-default ctx semantics | SHOULD | Default is assumed; deviations must be said |
| 15 | Zero-value `sync.Mutex` is valid | SHOULD | No pointer; no `new(sync.Mutex)` |
| 16 | Unexported mutex field, not embedded | SHOULD | `mu sync.Mutex`, not `sync.Mutex` |
| 17 | Don't copy types with a mutex | MUST | Pointer receivers; `go vet` copylocks |
| 18 | Short critical sections | SHOULD | `defer Unlock`; copy out for slow work |
| 19 | Copy slices/maps at boundaries | SHOULD | Prevents callers from bypassing the lock |
| 20 | `RWMutex` only when profile justifies | CONSIDER | `Mutex` is simpler and often faster |
| 21 | `sync.Once` for lazy init | SHOULD | Memory-ordering guarantees built in |
| 22 | `sync.Pool` is for buffers, not cache | CONSIDER | Runtime may drop entries any time |
| 23 | Atomics for counters, mutex for compound | SHOULD | Typed atomics since Go 1.19 |
| 24 | Document concurrency safety | SHOULD | Say so when behavior deviates from default |
| 25 | Channels communicate, mutexes guard | CONSIDER | Match the mechanism to the problem |
| 26 | Channel size 0 or 1 | CONSIDER | Larger buffers need measured justification |
| 27 | Channel direction in signatures | SHOULD | `chan<- T`, `<-chan T` — compiler enforces |
| 28 | The sender closes — only once | MUST | Receivers never close; use WaitGroup for N |
| 29 | `range` over channels | SHOULD | Idiomatic consumer loop |
| 30 | `select { default: }` for non-blocking | SHOULD | Not inside a tight loop without a sleep |
| 31 | `select` + `ctx.Done()` > `time.After` | SHOULD | Avoid untracked timer leaks |
| 32 | Pipeline: stage per goroutine | CONSIDER | Each stage owns and closes its output |
| 33 | Fan-out / fan-in with bounded pool | CONSIDER | Cap workers; `errgroup` + WaitGroup closer |
| 34 | Avoid mutable package-level state | SHOULD-AVOID | Structs + constructors + injection |
| 35 | `t.Fatal` only from the test goroutine | MUST | `t.Error` / `t.Errorf` from workers |
| 36 | `go test -race` in CI | SHOULD | Empirical check for data races |
| 37 | Happens-before through sync primitives | CONSIDER | Channels, mutex, Once, WaitGroup — not timing |
| 38 | `ch = nil` to disable closed case | SHOULD | Avoids 100% CPU busy loop |
| 39 | `time.Timer` reuse over `time.After` | SHOULD | `time.After` leaks timers |
| 40 | Directional channels in signatures | SHOULD | `chan<- T`, `<-chan T` |
| 41 | `wg.Add` before goroutine launch | MUST | Inside-goroutine races `Wait` |
| 42 | Per-goroutine `defer recover` | MUST | Parent can't catch child panics |
| 43 | Always `defer cancel()` | MUST | Derived contexts leak timers |
| 44 | `*Context` method variants | SHOULD | Propagates cancellation |
| 45 | Unexported context key type | MUST | Prevents package collisions |
| 46 | `context.WithoutCancel` for detached work | CONSIDER | Keeps values, drops cancel |
| 47 | `signal.NotifyContext` for shutdown | SHOULD | Clean drain on SIGINT/SIGTERM |
| 48 | Channels of channels | CONSIDER | Per-caller reply path |
| 49 | Partition CPU work by `NumCPU` | CONSIDER | Parallel map over range |
| 50 | Bounded-semaphore concurrency | MUST | Unbounded spawns exhaust memory |
| 51 | Always `defer wg.Done()` | MUST | Survives panics; avoids deadlock |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for channel direction in signatures (CI-35), channel size philosophy (CI-36), `time.Duration` (CI-37), and `defer` for cleanup (CI-34) — this chapter extends them into concurrency design
- **API Design**: See `02-api-design.md` for constructor shapes that pair with worker lifecycles (extends CC-06, CC-34)
- **Error Handling**: See `03-error-handling.md` for wrapping and sentinel errors — this chapter uses those patterns inside `errgroup` (CC-05) and `ctx.Err()` handling (CC-03, CC-14)
- **Type Design**: See `04-type-design.md` for pointer vs. value receivers; CC-17 applies the "pointer receiver if the value can't be copied" rule to mutex-holding types
- **Interfaces & Methods**: See `05-interfaces-methods.md` for concurrency safety documented on interfaces (extends CC-24)
- **Testing**: See `07-testing.md` for `t.Parallel`, race-detector test configurations, and goroutine-leak tests that exercise the patterns here
- **Performance**: See `08-performance.md` for contention profiling, `sync.Pool` as an allocation optimization (extends CC-22), and `RWMutex` tuning (extends CC-20)
- **Anti-Patterns**: See `09-anti-patterns.md` for the concurrency failure modes that CC-01, CC-17, CC-28, CC-34 prevent

---

## External References

- [The Go Memory Model](https://go.dev/ref/mem) — authoritative spec for happens-before and synchronization
- [*Effective Go* — Concurrency](https://go.dev/doc/effective_go#concurrency) — channels, goroutines, `select`
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — §Zero-value Mutexes, §Channel Size is One or None, §Don't fire-and-forget goroutines, §Use go.uber.org/atomic
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions §Goroutine lifetimes, §Contexts, §Custom contexts, §Copying, §Synchronous functions; Best Practices §Documentation conventions: Concurrency, §Channel direction, §Global state
- [Dave Cheney — *Never start a goroutine without knowing how it will stop*](https://dave.cheney.net/2016/12/22/never-start-a-goroutine-without-knowing-how-it-will-stop)
- [Bryan Mills — *Rethinking Classical Concurrency Patterns*](https://drive.google.com/file/d/1nPdvhB0PutEJzdCq5ms6UI58dp50fcAN/view) ([video](https://www.youtube.com/watch?v=5zXAHh5tJqQ))
- [Go Blog — *Contexts and structs*](https://go.dev/blog/context-and-structs)
- [`golang.org/x/sync/errgroup`](https://pkg.go.dev/golang.org/x/sync/errgroup) — coordinated cancellation for groups of fallible goroutines
- [`sync` package](https://pkg.go.dev/sync), [`sync/atomic` package](https://pkg.go.dev/sync/atomic), [`context` package](https://pkg.go.dev/context) — primitives used throughout this chapter
- [`go test -race`](https://go.dev/doc/articles/race_detector), [`go vet` copylocks / lostcancel](https://pkg.go.dev/cmd/vet) — the tooling that enforces most of these rules
