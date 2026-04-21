# Go Anti-Patterns

A curated gallery of patterns to avoid in Go code — the traps that trip up newcomers arriving from Java, C++, Python, or JavaScript, plus a handful of home-grown mistakes that even seasoned Go programmers commit under deadline pressure. Each entry pairs the anti-pattern with its idiomatic replacement and a citation from an authoritative source: the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and *Effective Go*.

This chapter is structured as a negative mirror of the rest of the series. Where chapter 01 (`01-core-idioms.md`) says "do this," chapter 09 says "don't do that." The two chapters are meant to be read together: every `AP-NN` here has a positive counterpart in the other guides, listed under `## Related Guidelines` at the end.

Target environment: **Go 1.22+**, **standard library first**, **`gofmt` + `go vet` + `staticcheck`** for formatting and linting. Go 1.22 fixed the loop-variable capture gotcha; `any` (Go 1.18) has replaced `interface{}`; `slices`, `maps`, and `cmp` live in the standard library.

---

## AP-01: Using `init()` for Side-Effectful Program Setup

**Strength**: SHOULD-AVOID

**Summary**: `init()` runs implicitly at import time with no return value and no way to fail gracefully. Reading files, parsing flags, opening connections, or mutating globals from `init()` makes programs non-deterministic, hard to test, and difficult to debug.

```go
// Bad — I/O and env lookups at import time
var config Config

func init() {
    cwd, _ := os.Getwd()                                     // env dependency
    raw, _ := os.ReadFile(path.Join(cwd, "config.yaml"))    // I/O
    yaml.Unmarshal(raw, &config)                            // ignored error
}

// Good — explicit, returns errors, testable
func loadConfig(path string) (Config, error) {
    raw, err := os.ReadFile(path)
    if err != nil {
        return Config{}, fmt.Errorf("read %q: %w", path, err)
    }
    var cfg Config
    if err := yaml.Unmarshal(raw, &cfg); err != nil {
        return Config{}, fmt.Errorf("parse %q: %w", path, err)
    }
    return cfg, nil
}

func main() {
    cfg, err := loadConfig("config.yaml")
    if err != nil {
        log.Fatal(err)
    }
    // ...
}
```

**Rationale**: Uber §Avoid `init()` requires that any `init()` "be completely deterministic, regardless of program environment or invocation... avoid depending on the ordering or side-effects of other `init()` functions... avoid accessing or manipulating global or environment state... avoid I/O." Functions that violate these rules "likely belong as a helper to be called as part of `main()`." `init()` has no way to return an error, so failures become panics or silently swallowed errors. Tests cannot substitute a different config, because `init()` has already run by the time `TestMain` is entered (Uber Style Guide §Avoid `init()`; Google Best Practices §Program initialization).

**See also**: AP-02, AP-13, AP-14

---

## AP-02: Spawning Goroutines from `init()`

**Strength**: MUST-AVOID

**Summary**: An `init()` that launches a background goroutine binds that goroutine's lifetime to the process and gives the user no way to stop it. Any program that imports the package pays the cost whether it needs the feature or not.

```go
// Bad — background work starts just because the package was imported
func init() {
    go pollMetrics()
}

func pollMetrics() {
    for {
        emit()
        time.Sleep(10 * time.Second)
    }
}

// Good — expose an object; caller controls the lifetime
type Poller struct {
    stop chan struct{}
    done chan struct{}
}

func NewPoller() *Poller {
    p := &Poller{stop: make(chan struct{}), done: make(chan struct{})}
    go p.run()
    return p
}

func (p *Poller) run() {
    defer close(p.done)
    t := time.NewTicker(10 * time.Second)
    defer t.Stop()
    for {
        select {
        case <-t.C:
            emit()
        case <-p.stop:
            return
        }
    }
}

func (p *Poller) Shutdown() {
    close(p.stop)
    <-p.done
}
```

**Rationale**: Uber §No goroutines in `init()` states that "`init()` functions should not spawn goroutines... If a package has need of a background goroutine, it must expose an object that is responsible for managing a goroutine's lifetime. The object must provide a method (`Close`, `Stop`, `Shutdown`, etc) that signals the background goroutine to stop, and waits for it to exit." Fire-and-forget goroutines in `init()` prevent clean shutdown, mask leaks during testing, and make the package coupling implicit (Uber Style Guide §No goroutines in init(); Uber Style Guide §Don't fire-and-forget goroutines).

**See also**: AP-01, AP-14, AP-15

---

## AP-03: Panicking in Library Code for Recoverable Conditions

**Strength**: MUST-AVOID

**Summary**: A library panic is an unrecoverable error signal that escapes to callers through `recover`. Using `panic` for invalid arguments, missing files, or network failures forces every caller to either wrap every call in `defer recover()` or accept that the program will crash.

```go
// Bad — panic on a recoverable error
func run(args []string) {
    if len(args) == 0 {
        panic("an argument is required")
    }
    // ...
}

// Good — return the error; caller decides
func run(args []string) error {
    if len(args) == 0 {
        return errors.New("an argument is required")
    }
    // ...
    return nil
}

func main() {
    if err := run(os.Args[1:]); err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
}
```

**Rationale**: Uber §Don't Panic: "Code running in production must avoid panics. Panics are a major source of cascading failures. If an error occurs, the function must return an error and allow the caller to decide how to handle it." Google Decisions §Don't panic: "Do not use `panic` for normal error handling. Instead, use `error` and multiple return values." Panics propagate across goroutines, bypass deferred cleanup in unrelated code paths, and force recovery boilerplate on every consumer (Uber Style Guide §Don't Panic; Google Decisions §Don't panic; Google Best Practices §When to panic).

**See also**: AP-04, AP-05, AP-07

---

## AP-04: Using panic/recover as Exception-Style Control Flow

**Strength**: MUST-AVOID

**Summary**: Go has no exceptions. Using `panic` to unwind several frames and `recover` to catch the unwinding is not idiomatic; it hides control flow, defeats `go vet` and `errcheck`, and subverts the caller's error-handling expectations.

```go
// Bad — exception-style
func Find(tree *Node, key string) *Node {
    defer func() {
        if r := recover(); r != nil {
            // swallow "not found" as a normal result
        }
    }()
    return mustFind(tree, key) // panics if not present
}

// Good — return a sentinel or a (value, ok) pair
var ErrNotFound = errors.New("not found")

func Find(tree *Node, key string) (*Node, error) {
    n := find(tree, key)
    if n == nil {
        return nil, ErrNotFound
    }
    return n, nil
}
```

**Rationale**: Google Best Practices §Program checks and panics warns against using `recover` to avoid crashes: "resist the temptation to recover panics to avoid crashes, as doing so can result in propagating a corrupted state. The further you are from the panic, the less you know about the state of the program, which could be holding locks or other resources." The one acceptable pattern — a parser that panics internally and converts to an error at the package boundary — requires that "these panics are never allowed to escape across package boundaries" (Google Best Practices §When to panic; Google Best Practices §Program checks and panics; Uber Style Guide §Don't Panic).

**See also**: AP-03, AP-05

---

## AP-05: Calling `Must`-Style Functions in a Request Path

**Strength**: MUST-AVOID

**Summary**: `Must`-prefixed helpers (`regexp.MustCompile`, `template.Must`) convert errors into panics. They are safe to call once at package initialization with constant inputs, and dangerous in a request path where inputs are user-controlled.

```go
// Bad — user input flows into a Must function, so bad input crashes the server
func Version(o *servicepb.Object) (*version.Version, error) {
    v := version.MustParse(o.GetVersionString()) // panics on malformed input
    return dealiasVersion(v)
}

// Good — for user input, use the normal error-returning variant
func Version(o *servicepb.Object) (*version.Version, error) {
    v, err := version.Parse(o.GetVersionString())
    if err != nil {
        return nil, fmt.Errorf("parse version: %w", err)
    }
    return dealiasVersion(v)
}

// Good — Must is fine when the input is a compile-time constant
var defaultVersion = version.MustParse("1.2.3")
```

**Rationale**: Google Decisions §Must functions: "In general, they should only be called early on program startup, not on things like user input where normal Go error handling is preferred... These helpers should not be called in places where it's difficult to ensure an error would be caught or in a context where an error should be checked (e.g., in many request handlers)." A `Must` call with runtime input turns a validation failure into a server-wide crash (Google Decisions §Must functions; Uber Style Guide §Don't Panic).

**See also**: AP-03, AP-06

---

## AP-06: Calling `os.Exit` or `log.Fatal` Outside `main`

**Strength**: SHOULD-AVOID

**Summary**: `os.Exit` and `log.Fatal*` terminate the program without running deferred functions. When a helper deep in a call chain calls them, the program loses the chance to clean up (close files, flush buffers, release locks) and tests become hard to write.

```go
// Bad — log.Fatal inside a helper
func readFile(path string) string {
    f, err := os.Open(path)
    if err != nil {
        log.Fatal(err) // terminates the whole process
    }
    defer f.Close() // never runs if log.Fatal above fires
    b, _ := io.ReadAll(f)
    return string(b)
}

// Good — return errors; let main decide
func readFile(path string) (string, error) {
    f, err := os.Open(path)
    if err != nil {
        return "", fmt.Errorf("open %q: %w", path, err)
    }
    defer f.Close()

    b, err := io.ReadAll(f)
    if err != nil {
        return "", fmt.Errorf("read %q: %w", path, err)
    }
    return string(b), nil
}

func main() {
    body, err := readFile(path)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(body)
}
```

**Rationale**: Uber §Exit in Main: "Call one of `os.Exit` or `log.Fatal*` **only in `main()`**. All other functions should return errors to signal failure." Early exits make deferred cleanup unreachable and make any non-`main` package impossible to reuse as a library. A helper that exits on failure cannot be called from a test without terminating the test process (Uber Style Guide §Exit in Main).

**See also**: AP-03, AP-05

---

## AP-07: Mutable Package-Level Globals

**Strength**: SHOULD-AVOID

**Summary**: A mutable top-level variable — a registry, a default instance, a client singleton, a callback list — is shared by every consumer of the package. Tests pollute each other, concurrent clients fight for ownership, and migration to per-instance state becomes a multi-quarter refactor.

```go
// Bad — every caller in the process shares one registry
package sidecar

var registry = make(map[string]*Plugin)

func Register(name string, p *Plugin) error { /* mutates registry */ }

// Good — callers create and own their registry
package sidecar

type Registry struct { plugins map[string]*Plugin }

func New() *Registry { return &Registry{plugins: make(map[string]*Plugin)} }

func (r *Registry) Register(name string, p *Plugin) error { /* ... */ }

// In main:
sidecars := sidecar.New()
_ = sidecars.Register("cloudlogger", cloudlogger.New())
```

**Rationale**: Google Best Practices §Global state: "Libraries should not force their clients to use APIs that rely on global state. They are advised not to expose APIs or export package level variables that control behavior for all clients as parts of their API." Global state creates order-dependent tests, prevents parallelism, and collapses under multi-tenant or multi-config workloads. Uber §Avoid Mutable Globals gives the same guidance: "Avoid mutating global variables, instead opting for dependency injection" (Google Best Practices §Global state; Uber Style Guide §Avoid Mutable Globals).

**See also**: AP-01, AP-08, AP-09

---

## AP-08: Monkey-Patching Function Pointers to Inject in Tests

**Strength**: SHOULD-AVOID

**Summary**: Assigning package-level function variables (`var timeNow = time.Now`) so tests can replace them is a form of mutable global. Parallel tests collide, unrelated tests accidentally see replaced state, and the production-vs-test code paths diverge.

```go
// Bad — test rewrites a package-level function variable
// sign.go
var _timeNow = time.Now

func sign(msg string) string {
    return signWithTime(msg, _timeNow())
}

// sign_test.go
func TestSign(t *testing.T) {
    old := _timeNow
    _timeNow = func() time.Time { return fixed }
    defer func() { _timeNow = old }()
    // test
}

// Good — inject the dependency as a field
type signer struct{ now func() time.Time }

func newSigner() *signer { return &signer{now: time.Now} }

func (s *signer) Sign(msg string) string {
    return signWithTime(msg, s.now())
}

// sign_test.go
func TestSigner(t *testing.T) {
    s := newSigner()
    s.now = func() time.Time { return fixed }
    // test; isolated to this signer
}
```

**Rationale**: Uber §Avoid Mutable Globals presents this exact refactor as the motivating example: "Avoid mutating global variables, instead opting for dependency injection. This applies to function pointers as well as other kinds of values." A per-instance field scopes the override to one test; a package variable leaks across the whole test binary (Uber Style Guide §Avoid Mutable Globals; Google Best Practices §Global state).

**See also**: AP-07, AP-09

---

## AP-09: Using `init()` to Register Callbacks or Plugins

**Strength**: SHOULD-AVOID

**Summary**: Side-effectful registration at import time (`init()` adding an entry to a global registry) is a form of mutable global state that is especially hard to reason about: whether the registration happened depends on whether some package, somewhere, was imported.

```go
// Bad — import order determines behavior
package health

var unhealthyFuncs []func()

func OnUnhealthy(f func()) { unhealthyFuncs = append(unhealthyFuncs, f) }

// other_pkg/init.go
func init() { health.OnUnhealthy(alertOps) } // implicit coupling

// Good — explicit wiring in main
type Monitor struct{ cbs []func() }

func (m *Monitor) OnUnhealthy(f func()) { m.cbs = append(m.cbs, f) }

func main() {
    m := &Monitor{}
    m.OnUnhealthy(alertOps)
    run(m)
}
```

**Rationale**: Google Best Practices §Major forms of package state APIs lists "Registries for callbacks and similar behaviors" as a problematic form: "A client could call `Register` in `func init`, before flags are parsed, or after `main`. The stage at which a function is called affects error handling... Aborting is not appropriate for general-purpose library functions that can be used at any stage." Import-time registration makes ordering invisible, testing order-dependent, and replacement impossible (Google Best Practices §Major forms of package state APIs; Uber Style Guide §Avoid `init()`).

**See also**: AP-01, AP-07

---

## AP-10: Ignoring Errors with `_`

**Strength**: MUST-AVOID

**Summary**: Discarding an error return with `_ :=` is equivalent to an empty `catch` block. The function signaled that something could fail; you chose to pretend it didn't. Downstream code proceeds with invalid state and the bug surfaces far from the cause.

```go
// Bad
data, _ := os.ReadFile(path)
var v Config
_ = json.Unmarshal(data, &v)   // data may be empty or invalid
use(v)

// Good
data, err := os.ReadFile(path)
if err != nil {
    return fmt.Errorf("read %q: %w", path, err)
}
var v Config
if err := json.Unmarshal(data, &v); err != nil {
    return fmt.Errorf("parse %q: %w", path, err)
}
use(v)

// Acceptable with a comment explaining why
var buf *bytes.Buffer
n, _ := buf.Write(p) // never returns a non-nil error, per the docs
```

**Rationale**: Google Decisions §Handle errors: "It is not usually appropriate to discard errors using `_` variables... In the rare circumstance where it is appropriate to ignore or discard an error... an accompanying comment should explain why this is safe." `errcheck` and `staticcheck` flag blanket discards; a comment is the difference between silent data loss and an informed choice (Google Decisions §Handle errors; Effective Go §Errors).

**See also**: AP-11, AP-12, AP-21

---

## AP-11: Prefixing Error Messages with "failed to"

**Strength**: SHOULD-AVOID

**Summary**: Error wrapping should add information, not redundant framing. Starting every wrapped error with "failed to" yields cascading error chains like `failed to x: failed to y: failed to z: the error` — all noise, no signal.

```go
// Bad
s, err := store.New()
if err != nil {
    return fmt.Errorf("failed to create new store: %w", err)
}
// Resulting chain: "failed to process request: failed to create new store: failed to open: no space left on device"

// Good
s, err := store.New()
if err != nil {
    return fmt.Errorf("new store: %w", err)
}
// Resulting chain: "process request: new store: open: no space left on device"
```

**Rationale**: Uber §Error Wrapping: "When adding context to returned errors, keep the context succinct by avoiding phrases like 'failed to', which state the obvious and pile up as the error percolates up through the stack... However once the error is sent to another system, it should be clear the message is an error (e.g. an `err` tag or 'Failed' prefix in logs)." The error type already signals failure; every wrap should narrow the location, not repeat the conclusion (Uber Style Guide §Error Wrapping; Google Best Practices §Adding information to errors).

**See also**: AP-10, AP-12

---

## AP-12: Wrapping Errors Without Adding Any Information

**Strength**: SHOULD-AVOID

**Summary**: `fmt.Errorf("%w", err)` or `fmt.Errorf("error: %w", err)` creates a new error that wraps the original without contributing context. Either return the original directly, or add a useful frame.

```go
// Bad — pointless wrap
if err != nil {
    return fmt.Errorf("%w", err)
}

// Bad — wrap with no new information
if err != nil {
    return fmt.Errorf("failed: %v", err)
}

// Good — return as-is if you have nothing to add
if err != nil {
    return err
}

// Good — add something the caller doesn't know
if err := os.Open(path); err != nil {
    return fmt.Errorf("launch codes unavailable: %w", err)
}
```

**Rationale**: Google Best Practices §Adding information to errors: "Don't add an annotation if its sole purpose is to indicate a failure without adding new information. The presence of an error sufficiently conveys the failure to the caller... `return fmt.Errorf('failed: %v', err) // just return err instead`." Also, avoid redundancy: "When adding information to errors, avoid redundant information that the underlying error already provides" — the `os` package already includes the path in its errors (Google Best Practices §Adding information to errors).

**See also**: AP-10, AP-11

---

## AP-13: String-Matching Error Messages to Branch on Them

**Strength**: MUST-AVOID

**Summary**: Parsing an error's `.Error()` text to decide how to handle it is fragile. The message format is not part of the API contract; a single log tweak upstream silently breaks every caller.

```go
// Bad — branching on the error message
err := process(an)
if regexp.MatchString(`duplicate`, err.Error()) {
    // ...
}
if strings.Contains(err.Error(), "marsupial") {
    // ...
}

// Good — sentinel values with errors.Is
var (
    ErrDuplicate = errors.New("duplicate")
    ErrMarsupial = errors.New("marsupials are not supported")
)

err := process(an)
switch {
case errors.Is(err, ErrDuplicate):
    // ...
case errors.Is(err, ErrMarsupial):
    // ...
}

// Good — typed errors with errors.As
var pe *os.PathError
if errors.As(err, &pe) {
    log.Printf("path %q: %v", pe.Path, pe.Err)
}
```

**Rationale**: Google Best Practices §Error structure: "If callers need to interrogate the error (e.g., distinguish different error conditions), give the error value structure so that this can be done programmatically rather than having the caller perform string matching." An error's message is for humans; matching it couples two packages through a string. `errors.Is` and `errors.As` make the contract explicit and refactor-safe (Google Best Practices §Error structure; Uber Style Guide §Error Types).

**See also**: AP-10, AP-14

---

## AP-14: Using In-Band Error Values (`-1`, `""`, `nil`)

**Strength**: SHOULD-AVOID

**Summary**: Returning a magic value to signal "not found" or "error" is a C-era technique. Go's multiple return values let the signal and the datum travel on separate channels, so the caller cannot accidentally treat a signal as data.

```go
// Bad — -1 might also be a valid key's value
// Lookup returns the value for key or -1 if there is no mapping.
func Lookup(key string) int

// Using it is easy to mis-compose:
return Parse(Lookup(missingKey)) // Parse sees -1, fails, wrong error attributed

// Good — explicit second return
// Lookup returns the value for key; ok is false if there is no mapping.
func Lookup(key string) (value string, ok bool)

v, ok := Lookup(key)
if !ok {
    return fmt.Errorf("no value for %q", key)
}
return Parse(v)
```

**Rationale**: Google Decisions §In-band errors: "Failing to check for an in-band error value can lead to bugs and can attribute errors to the wrong function... a function should return an additional value to indicate whether its other return values are valid. This return value may be an error or a boolean." The two-return form prevents `Parse(Lookup(k))`, because the compiler sees the arity mismatch (Google Decisions §In-band errors; Effective Go §Multiple return values).

**See also**: AP-10, AP-13

---

## AP-15: Fire-and-Forget Goroutines with No Stop Signal

**Strength**: MUST-AVOID

**Summary**: `go f()` without a plan for how `f` will stop is a leak waiting to happen. Goroutines are cheap but not free; one leaked per request accumulates into an unresponsive process in production.

```go
// Bad — no way to stop this goroutine
go func() {
    for {
        flush()
        time.Sleep(delay)
    }
}()

// Good — context-aware ticker
func (w *Worker) Run(ctx context.Context) {
    t := time.NewTicker(delay)
    defer t.Stop()
    for {
        select {
        case <-t.C:
            flush()
        case <-ctx.Done():
            return
        }
    }
}

// Good — explicit stop/done channels
var (
    stop = make(chan struct{})
    done = make(chan struct{})
)
go func() {
    defer close(done)
    t := time.NewTicker(delay)
    defer t.Stop()
    for {
        select {
        case <-t.C:
            flush()
        case <-stop:
            return
        }
    }
}()

// Shut down and wait:
close(stop)
<-done
```

**Rationale**: Uber §Don't fire-and-forget goroutines: "every goroutine: must have a predictable time at which it will stop running; or there must be a way to signal to the goroutine that it should stop. In both cases, there must be a way for code to block and wait for the goroutine to finish." Google Decisions §Goroutine lifetimes: "When you spawn goroutines, make it clear when or whether they exit. Goroutines can leak by blocking on channel sends or receives. The garbage collector will not terminate a goroutine blocked on a channel even if no other goroutine has a reference to the channel." Use `goleak` to catch leaks in tests (Uber Style Guide §Don't fire-and-forget goroutines; Google Decisions §Goroutine lifetimes).

**See also**: AP-02, AP-16, AP-17

---

## AP-16: Using `time.Sleep` for Synchronization

**Strength**: MUST-AVOID

**Summary**: Sleeping to wait for an event is a guess. The event may happen sooner (you waste time), may happen later (you hit a race), or may not happen at all (you deadlock). Use channels, `sync.WaitGroup`, or `context` to express the actual condition.

```go
// Bad — hoping the goroutine finishes in 100ms
go doWork()
time.Sleep(100 * time.Millisecond) // race

// Bad — busy-waiting on a flag
go func() { ready = true }()
for !ready {
    time.Sleep(10 * time.Millisecond)
}

// Good — WaitGroup
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    doWork()
}()
wg.Wait()

// Good — done channel
done := make(chan struct{})
go func() {
    defer close(done)
    doWork()
}()
<-done

// Good — periodic work with a ticker, not sleep
t := time.NewTicker(interval)
defer t.Stop()
for {
    select {
    case <-t.C:
        poll()
    case <-ctx.Done():
        return
    }
}
```

**Rationale**: Uber §Don't fire-and-forget goroutines and Google Decisions §Goroutine lifetimes both require an explicit synchronization mechanism ("Use a `sync.WaitGroup` to wait for multiple goroutines to complete... Add another `chan struct{}` that the goroutine closes when it's done"). The "Bad" example in Uber's guide is literally `time.Sleep(delay)` inside a for-loop; the "Good" fix uses a `time.Ticker` inside a `select` with a stop channel. Sleeping is neither test-deterministic nor resource-aware (Uber Style Guide §Don't fire-and-forget goroutines; Google Decisions §Goroutine lifetimes).

**See also**: AP-15, AP-17, AP-33

---

## AP-17: Busy-Waiting on a Condition

**Strength**: SHOULD-AVOID

**Summary**: A `for` loop that repeatedly polls a variable — with or without a short sleep — burns CPU and introduces races unless every access is properly synchronized. Use channels or `sync.Cond` to block on the event instead.

```go
// Bad — spins the CPU
for !done {
}

// Bad — hides the race and still wastes cycles
for !done {
    runtime.Gosched()
}

// Good — block on a channel
<-done

// Good — sync.Cond when the condition is complex
var (
    mu   sync.Mutex
    cond = sync.NewCond(&mu)
    q    []Job
)

// producer
mu.Lock()
q = append(q, j)
cond.Signal()
mu.Unlock()

// consumer
mu.Lock()
for len(q) == 0 {
    cond.Wait()
}
j := q[0]
q = q[1:]
mu.Unlock()
```

**Rationale**: Google Decisions §Goroutine lifetimes refers to "condition variables" and channel-based blocking as the expected synchronization primitives. Busy-waiting on a shared variable without synchronization is a classic data race (flagged by `-race`), and even with atomics the constant polling is pure overhead. The point of goroutines and channels is that a blocked goroutine costs almost nothing — take the blocking (Google Decisions §Goroutine lifetimes; Effective Go §Concurrency).

**See also**: AP-15, AP-16

---

## AP-18: Creating Buffered Channels with Arbitrary Sizes

**Strength**: SHOULD-AVOID

**Summary**: Picking a buffer size like 64 or 100 because "it'll probably be enough" is engineering by coincidence. An unbuffered channel enforces synchronization; a buffer of 1 covers the narrow case where sender and receiver naturally move at the same rate. Anything else needs a reason.

```go
// Bad — magic buffer size
c := make(chan int, 64) // why 64?

// Bad — extremely large buffer used as a queue
c := make(chan int, 10000)

// Good — unbuffered, when the sender needs a confirmation
c := make(chan int)

// Good — buffer of 1, when you explicitly want a non-blocking single-value drop
result := make(chan *Result, 1)
go func() { result <- compute() }()
select {
case r := <-result:
    use(r)
case <-ctx.Done():
    return ctx.Err()
}
```

**Rationale**: Uber §Channel Size is One or None: "Channels should usually have a size of one or be unbuffered... Any other size must be subject to a high level of scrutiny. Consider how the size is determined, what prevents the channel from filling up under load and blocking writers, and what happens when this occurs." A buffered channel with an arbitrary size creates backpressure problems that are invisible until traffic grows (Uber Style Guide §Channel Size is One or None).

**See also**: AP-15, AP-17

---

## AP-19: Embedding `sync.Mutex` into Public Struct Fields

**Strength**: SHOULD-AVOID

**Summary**: Embedding `sync.Mutex` promotes `Lock` and `Unlock` onto the struct's public API. Callers can — and will — lock your struct from outside, breaking your internal invariants. Make the mutex an unexported field and expose methods instead.

```go
// Bad — SMap.Lock and SMap.Unlock are callable by outsiders
type SMap struct {
    sync.Mutex
    data map[string]string
}

func (m *SMap) Get(k string) string {
    m.Lock()
    defer m.Unlock()
    return m.data[k]
}

// Anyone can do:
//   s.Lock(); inspect(s.data); s.Unlock()   // reaches past the API

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
```

**Rationale**: Uber §Zero-value Mutexes are Valid: "Do not embed the mutex on the struct, even if the struct is not exported... The `Mutex` field, and the `Lock` and `Unlock` methods are unintentionally part of the exported API of `SMap`... The mutex and its methods are implementation details of `SMap` hidden from its callers." A non-embedded, unexported mutex keeps the synchronization strategy private (Uber Style Guide §Zero-value Mutexes are Valid).

**See also**: AP-20, AP-22

---

## AP-20: Copying a `sync.Mutex` by Value

**Strength**: MUST-AVOID

**Summary**: A `sync.Mutex` is not safe to copy after use. A value receiver, a struct assignment, or passing a struct-containing-mutex by value silently creates a second mutex that doesn't protect the original. `go vet` will flag many of these cases.

```go
// Bad — value receiver copies the mutex each call
type Counter struct {
    mu sync.Mutex
    n  int
}

func (c Counter) Inc() {     // value receiver
    c.mu.Lock()              // locks a copy; useless
    c.n++                    // mutates a copy, lost on return
    c.mu.Unlock()
}

// Bad — struct copy
a := Counter{}
b := a // copies the mutex state

// Good — pointer receiver; callers share the one mutex
type Counter struct {
    mu sync.Mutex
    n  int
}

func (c *Counter) Inc() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.n++
}
```

**Rationale**: Google Decisions §Copying: "synchronization objects such as `sync.Mutex` must not be copied... In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`. Invoking a method that takes a value receiver can hide the copy. When you author an API, you should generally take and return pointer types if your structs contain fields that should not be copied." `go vet` reports copied locks; treat it as an error (Google Decisions §Copying; Uber Style Guide §Zero-value Mutexes are Valid).

**See also**: AP-19, AP-22

---

## AP-21: Using the Single-Return Form of a Type Assertion

**Strength**: MUST-AVOID

**Summary**: `x.(T)` panics at runtime if `x` does not hold a `T`. Unless you've just performed a check that proves `x`'s dynamic type, always use the comma-ok form.

```go
// Bad — panics if x is not a string
s := x.(string)

// Bad — panics if err is not *os.PathError
pe := err.(*os.PathError)

// Good — comma-ok
s, ok := x.(string)
if !ok {
    return fmt.Errorf("expected string, got %T", x)
}

// Good — errors.As for error trees
var pe *os.PathError
if errors.As(err, &pe) {
    log.Printf("path=%s", pe.Path)
}

// Good — type switch for multiple possibilities
switch v := x.(type) {
case string:
    handleStr(v)
case int:
    handleInt(v)
default:
    return fmt.Errorf("unexpected %T", x)
}
```

**Rationale**: Uber §Handle Type Assertion Failures: "The single return value form of a type assertion will panic on an incorrect type. Therefore, always use the 'comma ok' idiom." A panicking assertion deep in request processing becomes an unrecovered 500. The comma-ok form is one extra variable and one extra line; use it (Uber Style Guide §Handle Type Assertion Failures).

**See also**: AP-03, AP-04

---

## AP-22: Using `new(T)` for a Mutex or Other Zero-Valued Struct

**Strength**: SHOULD-AVOID

**Summary**: `new(sync.Mutex)` returns a pointer to a zero-valued mutex, which is already valid as a plain value. The extra indirection buys nothing and makes every field access a pointer deref.

```go
// Bad
mu := new(sync.Mutex)
mu.Lock()

type Server struct {
    mu *sync.Mutex // pointer for no reason
}

// Good — zero value is valid
var mu sync.Mutex
mu.Lock()

type Server struct {
    mu sync.Mutex
}
```

**Rationale**: Uber §Zero-value Mutexes are Valid: "The zero-value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex." The same principle applies to `bytes.Buffer`, `strings.Builder`, and most other value-useful types: reach for a pointer only when you need shared state across copies or when the type documents that a pointer is required (Uber Style Guide §Zero-value Mutexes are Valid; Effective Go §Allocation with new).

**See also**: AP-19, AP-20

---

## AP-23: Starting `iota` Enums at Zero When Zero Is a Valid State

**Strength**: SHOULD-AVOID

**Summary**: Go zero-initializes variables. If your first enum constant equals zero and represents a legitimate operational state, then "forgot to initialize" and "intentionally set to the first state" are indistinguishable. Reserve zero for "unset" and start real states at 1.

```go
// Bad — a zero-valued Operation silently means Add
type Operation int

const (
    Add Operation = iota // 0 — also the zero value
    Subtract
    Multiply
)

var op Operation // op == Add without anyone setting it

// Good — start at 1; zero means "unknown/unset"
type Operation int

const (
    Add Operation = iota + 1
    Subtract
    Multiply
)

// Or: reserve an explicit Unknown
const (
    OpUnknown Operation = iota
    OpAdd
    OpSubtract
    OpMultiply
)
```

**Rationale**: Uber §Start Enums at One: "The standard way of introducing enumerations in Go is to declare a custom type and a `const` group with `iota`. Since variables have a 0 default value, you should usually start your enums on a non-zero value." There are legitimate cases where the zero value is the desired default (e.g., `LogToStdout`), but they should be an explicit design choice, not an accident (Uber Style Guide §Start Enums at One).

**See also**: AP-24

---

## AP-24: Using Untyped Strings as Enums

**Strength**: SHOULD-AVOID

**Summary**: `status string` with documented values `"active"`, `"inactive"`, `"pending"` is a promise the compiler cannot enforce. Define a named type and `const` block so that typos are compile errors.

```go
// Bad — any string sneaks through
type User struct {
    Status string // "active", "inactive", "pending"
}

u := User{Status: "activee"} // compiles; typo hits production

// Good — named type + iota
type UserStatus int

const (
    StatusUnknown UserStatus = iota
    StatusActive
    StatusInactive
    StatusPending
)

func (s UserStatus) String() string {
    switch s {
    case StatusActive:
        return "active"
    case StatusInactive:
        return "inactive"
    case StatusPending:
        return "pending"
    default:
        return "unknown"
    }
}

type User struct {
    Status UserStatus
}

u := User{Status: StatusActive} // typo caught at compile time
```

**Rationale**: Uber §Start Enums at One and the broader Go community convention introduce enums as a custom type plus a `const` group with `iota`, not as a set of string literals. A typed enum gives you exhaustiveness via `switch`, zero-cost substitution for `fmt.Stringer`, and compile-time rejection of invalid values (Uber Style Guide §Start Enums at One; Effective Go §Constants).

**See also**: AP-23

---

## AP-25: Writing Java-Style Getter/Setter Wrappers

**Strength**: SHOULD-AVOID

**Summary**: Go is not Java. If a field has no invariant, expose it directly. If it has an invariant, expose the minimum methods needed to enforce it — and don't name them `GetX`.

```go
// Bad — pass-through getter and setter on a plain field
type User struct {
    name string
}

func (u *User) GetName() string     { return u.name }
func (u *User) SetName(s string)    { u.name = s }

// Good — if there's no invariant, export the field
type User struct {
    Name string
}

// Good — if there is an invariant, enforce it without the Get prefix
type User struct {
    name string
}

func (u *User) Name() string { return u.name }

func (u *User) Rename(s string) error {
    if s == "" {
        return errors.New("empty name")
    }
    u.name = s
    return nil
}
```

**Rationale**: Google Decisions §Getters: "Function and method names should not use a `Get` or `get` prefix, unless the underlying concept uses the word 'get' (e.g. an HTTP GET). Prefer starting the name with the noun directly, for example use `Counts` over `GetCounts`." Uber §Function Names and Effective Go §Getters both reject the prefix. Auto-generating pass-through getters and setters on every field is a Java-ism; Go callers access fields directly unless the type needs mediation (Google Decisions §Getters; Effective Go §Getters).

**See also**: AP-26, AP-30

---

## AP-26: Type Names That Stutter the Package Name

**Strength**: SHOULD-AVOID

**Summary**: The package name is always visible at the call site. A type named `http.HTTPServer` or `user.UserID` reads as `http.HTTPServer` — the "HTTP" and "user" appear twice. Name types by what they *are*, not by what package they *live in*.

```go
// Bad
// package user
type UserID string
type UserService struct{}
func (s *UserService) GetUser(id UserID) *User

// Bad
// package http
type HTTPServer struct{}

// Bad — DBConnection in package sqldb
// package sqldb
type DBConnection struct{}

// Good — qualified at the call site reads well
// package user
type ID string
type Service struct{}
func (s *Service) Get(id ID) *User
// call site: user.Service, user.ID, s.Get(...)

// package http
type Server struct{}
// call site: http.Server

// package sqldb
type Connection struct{}
// call site: sqldb.Connection
```

**Rationale**: Google Decisions §Repetition: "When naming exported symbols, the name of the package is always visible outside your package, so redundant information between the two should be reduced or eliminated." Examples listed include `widget.NewWidget` → `widget.New` and "`DBConnection` in package `sqldb`" → "`Connection` in package `sqldb`." Every repetition lengthens call sites without adding information (Google Decisions §Repetition; Google Best Practices §Avoid repetition; Effective Go §Package names).

**See also**: AP-25, AP-27, AP-30

---

## AP-27: Generic Suffixes — `Manager`, `Service`, `Helper`, `Processor`

**Strength**: SHOULD-AVOID

**Summary**: `UserManager`, `OrderService`, `AuthHelper`, `PaymentProcessor` all tell the reader you couldn't decide what the type does. Name by behavior: `UserRepository`, `OrderValidator`, `PaymentGateway`. Or, more often, realize you just need a handful of plain functions.

```go
// Bad — a "manager" that manages something unspecified
type UserManager struct{}
func (m *UserManager) GetUser(id int) *User
func (m *UserManager) DeleteUser(id int) error

// Bad — "Helper" is a confession, not a name
type StringHelper struct{}
func (h *StringHelper) ReverseString(s string) string

// Good — name describes behavior
type UserRepository struct{ db *sql.DB }
func (r *UserRepository) Find(id int) (*User, error)
func (r *UserRepository) Delete(id int) error

// Good — package-level functions don't need a holder type
package strutil
func Reverse(s string) string { /* ... */ }
```

**Rationale**: Google Decisions §Interfaces: "Focus on the required behavior rather than just abstract named patterns like 'service' or 'repository' and the like." Google Best Practices §Avoid unnecessary interfaces: "Don't confuse the concept with the keyword: Just because you are designing a 'service' or a 'repository' or similar pattern doesn't mean you need a named interface type (e.g., `type Service interface`). Focus on the behavior and its concrete implementation first." Generic suffixes are the Java/C#-style architectural nouns that Go's concrete, behavior-first design rejects (Google Decisions §Interfaces; Google Best Practices §Avoid unnecessary interfaces).

**See also**: AP-26, AP-28, AP-30

---

## AP-28: Weasel Packages — `util`, `common`, `helpers`, `misc`, `shared`

**Strength**: SHOULD-AVOID

**Summary**: A package named `util` tells callers nothing. It becomes a dumping ground, encourages circular imports, and makes call sites like `util.Do(...)` unreadable. Split by purpose: `stringutil`, `httputil`, `timex`.

```go
// Bad — generic catch-all
package util
func Reverse(s string) string
func DoubleInt(i int) int
func ParseYAML(b []byte, v any) error

// Bad at the call site
util.Reverse(name)
util.ParseYAML(data, &cfg) // what kind of util is this?

// Good — split by purpose
package strutil
func Reverse(s string) string

package yamlutil
func Parse(b []byte, v any) error

// At the call site
strutil.Reverse(name)
yamlutil.Parse(data, &cfg)
```

**Rationale**: Google Best Practices §Util packages: "Naming a package just `util`, `helper`, `common` or similar is usually a poor choice... Uninformative names make the code harder to read, and if used too broadly they are liable to cause needless import conflicts." Uber §Package Names: package names must not be "'common', 'util', 'shared', or 'lib'. These are bad, uninformative names." A descriptive short name — `spannertest`, `elliptic`, `httputil` — tells the reader something at the call site (Google Best Practices §Util packages; Uber Style Guide §Package Names).

**See also**: AP-26, AP-27

---

## AP-29: Returning an Interface When a Concrete Type Would Do

**Strength**: SHOULD-AVOID

**Summary**: Returning a concrete type lets callers use the full API; they can still pass the value to any function that expects a compatible interface. Returning a pre-selected interface strips methods callers might want and forces everyone to use that abstraction.

```go
// Bad — Reader strips every method of *bytes.Buffer except Read
func NewBuffer() io.Reader {
    return &bytes.Buffer{}
}

// Good — return the concrete; callers pick the interface they need
func NewBuffer() *bytes.Buffer {
    return &bytes.Buffer{}
}

// Callers who only need io.Reader can still do:
var r io.Reader = NewBuffer()

// Exceptions (acceptable): error, rate-limited wrappers that must hide internals,
// factories in command/strategy patterns, generated RPC clients.
func Open(name string) (*File, error) { /* ... */ }   // concrete *File
```

**Rationale**: Google Decisions §Interfaces: "Functions should take interfaces as arguments but return concrete types... Returning concrete types allows the caller to have access to every public method and field of that specific implementation, not just the subset of methods defined in a pre-chosen interface. The caller can still pass that concrete result into any other function that expects an interface. Sometimes returning an interface is acceptable for encapsulation (e.g., `error` interface), and certain constructs like command, chaining, factory, and strategy patterns" (Google Decisions §Interfaces; Google Best Practices §Designing effective interfaces).

**See also**: AP-30, AP-31

---

## AP-30: Defining an Interface the Producer Doesn't Use

**Strength**: SHOULD-AVOID

**Summary**: In Go, interfaces belong in the package that consumes them, not in the package that implements them. If your package exports a `UserService` interface alongside the only implementation `userService`, you've created a maintenance burden for no benefit.

```go
// Bad — interface exported by the producer for no reason
package user

type Service interface {
    Find(id int) (*User, error)
    Delete(id int) error
}

type service struct{}
func (s *service) Find(id int) (*User, error) { /* ... */ }
func (s *service) Delete(id int) error         { /* ... */ }
func New() Service { return &service{} }

// Good — producer returns concrete; consumer defines its own interface if needed
package user

type Service struct{}
func (s *Service) Find(id int) (*User, error) { /* ... */ }
func (s *Service) Delete(id int) error         { /* ... */ }
func New() *Service { return &Service{} }

// In the consumer:
package admin

type userLookup interface {  // only the methods admin actually uses
    Find(id int) (*User, error)
}

func HandleAdminRequest(u userLookup, id int) { /* ... */ }
```

**Rationale**: Google Best Practices §Interface ownership and visibility: "The consumer defines the interface: In Go, interfaces generally belong in the package that uses them, not the package that implements them. The consumer should define only the methods they actually use, adhering to the idea that 'the bigger the interface, the weaker the abstraction.'" Google Decisions §Interfaces: "Avoid creating interfaces until a real need exists... Do not wrap RPC clients in new manual interfaces just for the sake of abstraction or testing." Exported producer interfaces couple every consumer to a shape the producer chose (Google Decisions §Interfaces; Google Best Practices §Avoid unnecessary interfaces; Google Best Practices §Interface ownership and visibility).

**See also**: AP-29, AP-31

---

## AP-31: Using `interface{}` / `any` as a Bag of Anything

**Strength**: SHOULD-AVOID

**Summary**: `any` (or `interface{}` pre-1.18) throws away every type guarantee. Any non-trivial use requires runtime type assertions, so bugs that a compiler could catch become runtime panics. Generics, a concrete type, or a small sum-type-like interface are almost always better.

```go
// Bad — a cache that stores anything and returns anything
type Cache struct{ m map[string]any }
func (c *Cache) Get(k string) any        { return c.m[k] }
func (c *Cache) Put(k string, v any)     { c.m[k] = v }

// Usage requires a type assertion at every call:
u := c.Get("user").(*User) // panics if the stored value isn't *User

// Good — a generic cache keeps types through
type Cache[V any] struct{ m map[string]V }
func (c *Cache[V]) Get(k string) (V, bool) { v, ok := c.m[k]; return v, ok }
func (c *Cache[V]) Put(k string, v V)       { c.m[k] = v }

var userCache Cache[*User]
u, ok := userCache.Get("alice") // no assertion, no panic

// Good — sum-type interface when there are known variants
type Event interface{ isEvent() }

type Login struct{ UserID int }
func (Login) isEvent() {}

type Logout struct{ UserID int }
func (Logout) isEvent() {}

func handle(e Event) {
    switch e := e.(type) {
    case Login:  handleLogin(e)
    case Logout: handleLogout(e)
    }
}
```

**Rationale**: Google Decisions §Use any: prefer `any` over `interface{}` for the same semantics, but this is a spelling decision — the underlying advice is to avoid the empty interface when a real type is known. Google Decisions §Generics: "Do not use generics just because you are implementing an algorithm or data structure that does not care about the type of its member elements... instead of relying on the `any` type and excessive type switching, consider generics." An `any`-heavy API is Python-in-Go: the compile-time benefits evaporate (Google Decisions §Use any; Google Decisions §Generics; Google Best Practices §Avoid unnecessary interfaces).

**See also**: AP-21, AP-29

---

## AP-32: Reaching for `reflect` When Generics or Type Switch Would Do

**Strength**: SHOULD-AVOID

**Summary**: `reflect` bypasses the type system and is a notorious source of bugs, performance cliffs, and surprising behavior. Since Go 1.18, generics cover most of `reflect`'s classic use cases (containers, helpers that work for many types); a type switch handles a small closed set of variants.

```go
// Bad — reflect for a sum over a slice of ints or floats
func SumReflect(v any) float64 {
    rv := reflect.ValueOf(v)
    if rv.Kind() != reflect.Slice {
        panic("want slice")
    }
    var total float64
    for i := 0; i < rv.Len(); i++ {
        el := rv.Index(i)
        switch el.Kind() {
        case reflect.Int, reflect.Int32, reflect.Int64:
            total += float64(el.Int())
        case reflect.Float32, reflect.Float64:
            total += el.Float()
        }
    }
    return total
}

// Good — generics express the constraint at compile time
type Number interface{ ~int | ~int32 | ~int64 | ~float32 | ~float64 }

func Sum[T Number](xs []T) T {
    var total T
    for _, x := range xs {
        total += x
    }
    return total
}

// Good — type switch when there are a few concrete cases
func Describe(v any) string {
    switch v := v.(type) {
    case int:    return fmt.Sprintf("int=%d", v)
    case string: return fmt.Sprintf("string=%q", v)
    default:     return fmt.Sprintf("other=%T", v)
    }
}
```

**Rationale**: Google Decisions §Generics: "In many applications, a conventional approach using existing language features (slices, maps, interfaces, and so on) works just as well without the added complexity, so be wary of premature use... instead of relying on the `any` type and excessive type switching, consider generics." Google Best Practices §When to panic notes that `reflect` itself panics on misuse, because "the standard library panics on API misuse" — using `reflect` inherits that fragility. Generics preserve types; `reflect` discards them (Google Decisions §Generics; Google Best Practices §When to panic).

**See also**: AP-31

---

## AP-33: Capturing the Loop Variable in a Goroutine (Pre-1.22 Pattern)

**Strength**: MUST-AVOID

**Summary**: Before Go 1.22, `for i, v := range xs` reused the same `i` and `v` across iterations. A goroutine that closed over `v` saw whichever value the loop happened to be on. Go 1.22 fixed this by making loop variables fresh per iteration — but code targeting older modules, or style habits carried forward, still produce the buggy shape.

```go
// Bad (pre-1.22) — all goroutines see the same v
for _, v := range items {
    go func() {
        process(v) // captures the shared v
    }()
}

// Bad (defensive, still appears) — shadowing inside the loop body
for _, v := range items {
    v := v
    go func() {
        process(v)
    }()
}

// Good (Go 1.22+) — each iteration gets its own v; shadowing is unnecessary
for _, v := range items {
    go func() {
        process(v)
    }()
}

// Even better — pass the value explicitly, self-documenting regardless of Go version
for _, v := range items {
    go func(v Item) {
        process(v)
    }(v)
}
```

**Rationale**: This is the single most common concurrency bug in Go before 1.22. The `go.dev/blog` announcement and the release notes for Go 1.22 describe the semantics change. For code that targets 1.22+ (declared by `go 1.22` in `go.mod`), the bug is gone; for older targets, pass the loop variable as a parameter or shadow it. Either way, be aware that reading a closure over a ranged variable in older code bases is an immediate red flag. Compiler and `go vet` both help (`loopclosure` check) (Go 1.22 release notes; Go Wiki §CommonMistakes).

**See also**: AP-15, AP-34

---

## AP-34: Shadowing `ctx` Inside an `if` (Losing the Cancellable Context)

**Strength**: MUST-AVOID

**Summary**: A `:=` inside a new block creates a fresh variable scoped to that block. Writing `ctx, cancel := context.WithTimeout(ctx, d)` inside an `if` replaces only the inner `ctx`; code after the `if` keeps using the outer, uncancelled context.

```go
// Bad — ctx after the if is the caller's original context
func (s *Server) inner(ctx context.Context, req *Request) {
    if *shortenDeadlines {
        ctx, cancel := context.WithTimeout(ctx, 3*time.Second) // shadow!
        defer cancel()
        log.Info(ctx, "capped")
    }
    // BUG: ctx here is the ORIGINAL context, unchanged.
    doWork(ctx, req)
}

// Good — use = so the outer ctx is reassigned (with a pre-declared cancel)
func (s *Server) inner(ctx context.Context, req *Request) {
    if *shortenDeadlines {
        var cancel func()
        ctx, cancel = context.WithTimeout(ctx, 3*time.Second)
        defer cancel()
        log.Info(ctx, "capped")
    }
    doWork(ctx, req) // now uses the capped ctx if the flag was set
}

// Good — or unconditionally cap at the top of the function
func (s *Server) inner(ctx context.Context, req *Request) {
    ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
    defer cancel()
    doWork(ctx, req)
}
```

**Rationale**: Google Best Practices §Shadowing presents this exact bug: "Attempt to conditionally cap the deadline... BUG: 'ctx' here again means the context that the caller provided. The above buggy code compiled because both ctx and cancel were used inside the if statement." The fix is to declare `cancel` outside and use `=` to reassign, or to restructure so the context replacement is unconditional (Google Best Practices §Shadowing).

**See also**: AP-35, AP-33

---

## AP-35: Shadowing Built-Ins and Standard Library Package Names

**Strength**: SHOULD-AVOID

**Summary**: Variables named `error`, `string`, `len`, or `url` shadow Go's predeclared identifiers or common package names, either silently or within their scope. Code becomes harder to grep, harder to read, and prone to latent bugs.

```go
// Bad — shadows the builtin error
var error string

// Bad — shadows the predeclared len
len := len(users)

// Bad — shadows net/url; can't use url.Parse below
func LongFunction() {
    url := "https://example.com/"
    // Oops, now we can't use net/url in code below.
}

// Bad — field and type name clash is grep-hostile
type Foo struct {
    error error
    string string
}

// Good — use different names
var errMessage string

numUsers := len(users)

func LongFunction() {
    endpoint := "https://example.com/"
    u, err := url.Parse(endpoint) // url package is accessible
    // ...
}

type Foo struct {
    err error
    str string
}
```

**Rationale**: Uber §Avoid Using Built-In Names: "Depending on context, reusing these identifiers as names will either shadow the original within the current lexical scope (and any nested scopes) or make affected code confusing. In the best case, the compiler will complain; in the worst case, such code may introduce latent, hard-to-grep bugs." Google Best Practices §Shadowing: "It is not a good idea to use variables with the same name as standard packages other than very small scopes, because that renders free functions and values from that package inaccessible." `go vet`'s shadow checker flags many cases (Uber Style Guide §Avoid Using Built-In Names; Google Best Practices §Shadowing).

**See also**: AP-34, AP-36

---

## AP-36: Deep Nesting That Obscures the Happy Path

**Strength**: SHOULD-AVOID

**Summary**: Go's idiom is to handle errors by returning early and keeping the success path left-aligned. Code that nests `if err == nil { ... }` branches three or four deep is harder to read and almost always hides an early-return refactor.

```go
// Bad — three levels deep to read the happy path
func load(path string) (*Config, error) {
    if data, err := os.ReadFile(path); err == nil {
        var cfg Config
        if err := json.Unmarshal(data, &cfg); err == nil {
            if err := cfg.Validate(); err == nil {
                return &cfg, nil
            } else {
                return nil, err
            }
        } else {
            return nil, err
        }
    } else {
        return nil, err
    }
}

// Good — each error returns early; happy path runs straight down
func load(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("read %q: %w", path, err)
    }

    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return nil, fmt.Errorf("parse %q: %w", path, err)
    }

    if err := cfg.Validate(); err != nil {
        return nil, fmt.Errorf("validate %q: %w", path, err)
    }

    return &cfg, nil
}
```

**Rationale**: Google Decisions §Indent error flow: "Go code is written with the success path aligned to the left, and the failure paths increasingly to the right." Uber §Reduce Nesting: "Code should reduce nesting where possible by handling error cases/special conditions first and returning early or continuing the loop. Reduce the amount of code that is nested multiple levels." Deep nesting is the single most common readability problem reviewers flag in Go (Google Decisions §Indent error flow; Uber Style Guide §Reduce Nesting).

**See also**: AP-37, AP-21

---

## AP-37: Unnecessary `else` After a Terminating `if`

**Strength**: SHOULD-AVOID

**Summary**: If the `if` branch ends in `return`, `break`, `continue`, or `panic`, the `else` is redundant. Drop it and let the next statement flow at the outer level.

```go
// Bad
if err != nil {
    return err
} else {
    doWork()
}

// Bad
for _, item := range items {
    if item.valid {
        process(item)
    } else {
        continue
    }
}

// Bad — both branches assign; collapse to one default + overwrite
var a int
if b {
    a = 100
} else {
    a = 10
}

// Good
if err != nil {
    return err
}
doWork()

// Good
for _, item := range items {
    if !item.valid {
        continue
    }
    process(item)
}

// Good
a := 10
if b {
    a = 100
}
```

**Rationale**: Uber §Unnecessary Else: "If a variable is set in both branches of an if, it can be replaced with a single if." Google Decisions §Indent error flow also calls out the equivalent pattern: "Code that runs if the terminal condition is not met should appear after the `if` block, and should not be indented in an `else` clause." Unnecessary `else` is extra indentation, extra braces, and an extra level of cognitive load for the reader (Uber Style Guide §Unnecessary Else; Google Decisions §Indent error flow).

**See also**: AP-36

---

## AP-38: Calling `fmt.Sprint(x)` to Convert a Primitive to a String

**Strength**: SHOULD-AVOID

**Summary**: `strconv` is purpose-built for primitive-to-string conversion and is several times faster than `fmt`. Reach for `fmt` only when you need formatting (width, precision, verbs).

```go
// Bad — slow and allocation-heavy
s := fmt.Sprint(rand.Int())
s := fmt.Sprintf("%d", n)

// Good
s := strconv.Itoa(rand.Int())
s := strconv.FormatInt(n, 10)
s := strconv.FormatBool(b)
s := strconv.FormatFloat(f, 'g', -1, 64)
```

**Rationale**: Uber §Prefer strconv over fmt: "When converting primitives to/from strings, `strconv` is faster than `fmt`." The Uber benchmark shows `strconv.Itoa` at 64 ns/op / 1 alloc vs. `fmt.Sprint` at 143 ns/op / 2 allocs. On a hot path — parsing logs, building keys, formatting many rows — the difference adds up (Uber Style Guide §Prefer strconv over fmt).

**See also**: AP-39, AP-40

---

## AP-39: Repeated `[]byte("literal")` Conversions in a Hot Loop

**Strength**: SHOULD-AVOID

**Summary**: Each `[]byte("Hello world")` inside a loop allocates a new byte slice. Hoist the conversion out once.

```go
// Bad
for i := 0; i < b.N; i++ {
    w.Write([]byte("Hello world"))
}

// Good
data := []byte("Hello world")
for i := 0; i < b.N; i++ {
    w.Write(data)
}
```

**Rationale**: Uber §Avoid repeated string-to-byte conversions: "Do not create byte slices from a fixed string repeatedly. Instead, perform the conversion once and capture the result." Uber's benchmark shows the per-iteration cost drops from ~22 ns/op to ~3 ns/op — roughly 7× — simply by hoisting the conversion (Uber Style Guide §Avoid repeated string-to-byte conversions).

**See also**: AP-38, AP-40

---

## AP-40: `append` to a Slice Without a Capacity Hint

**Strength**: SHOULD-AVOID

**Summary**: `make([]T, 0)` and then appending `N` times re-allocates the backing array roughly `log2(N)` times, copying the existing data each time. If you know the final length, pass it as the capacity.

```go
// Bad — 0 capacity, many grows
data := make([]int, 0)
for k := 0; k < size; k++ {
    data = append(data, k)
}

// Good — preallocate
data := make([]int, 0, size)
for k := 0; k < size; k++ {
    data = append(data, k)
}

// Maps too — hint is a sizing suggestion, not exact
m := make(map[string]int, len(entries))
for _, e := range entries {
    m[e.key] = e.value
}
```

**Rationale**: Uber §Prefer Specifying Container Capacity: "Specify container capacity where possible in order to allocate memory for the container up front. This minimizes subsequent allocations (by copying and resizing of the container) as elements are added." The benchmark difference for slice preallocation is order-of-magnitude (2.48s vs 0.21s in the Uber numbers). Map capacity hints are softer — they size the hashmap's bucket count — but still reduce rehashing (Uber Style Guide §Specifying Slice Capacity; Uber Style Guide §Specifying Map Capacity Hints; Google Decisions §Size hints).

**See also**: AP-38, AP-39

---

## AP-41: Writing a Test That Uses `panic` on Setup Failure

**Strength**: SHOULD-AVOID

**Summary**: When a test's setup fails, use `t.Fatal` (or `t.Fatalf`) rather than `panic`. `t.Fatal` marks the test failed and lets other tests continue; `panic` terminates the whole test binary in whichever state it's in.

```go
// Bad
func TestFoo(t *testing.T) {
    f, err := os.CreateTemp("", "test")
    if err != nil {
        panic("failed to set up test")
    }
    defer os.Remove(f.Name())
    // ...
}

// Good
func TestFoo(t *testing.T) {
    f, err := os.CreateTemp("", "test")
    if err != nil {
        t.Fatalf("create temp: %v", err)
    }
    t.Cleanup(func() { os.Remove(f.Name()) })
    // ...
}
```

**Rationale**: Uber §Don't Panic explicitly addresses the testing case: "Even in tests, prefer `t.Fatal` or `t.FailNow` over panics to ensure that the test is marked as failed." A panic in a test can skip other tests in the package, confuse test frameworks, and hide parallel-test interactions (Uber Style Guide §Don't Panic).

**See also**: AP-03, AP-04

---

## AP-42: Missing Struct Tags on Marshaled Types

**Strength**: SHOULD-AVOID

**Summary**: If a struct crosses a serialization boundary (JSON, YAML, protobuf, config file), declare its wire-format names with tags. Without tags, every field rename becomes a silent breaking change to your consumers.

```go
// Bad — the JSON field names are whatever Go exports
type Stock struct {
    Price int
    Name  string
}
// JSON: {"Price": 137, "Name": "UBER"}
// Rename Price -> Cost and every client breaks with no compile error.

// Good — explicit JSON contract
type Stock struct {
    Price int    `json:"price"`
    Name  string `json:"name,omitempty"`
}
// JSON: {"price": 137, "name": "UBER"}
```

**Rationale**: Uber §Use field tags in marshaled structs: "When declaring a struct type that is marshaled to JSON, YAML, or other formats that support tag-based field naming, annotate it with the relevant tags. Rationale: The serialized form of the structure is a contract between different systems. Changes to the structure of the serialized form -- including field names -- break this contract. Specifying field names inside tags makes the contract explicit, and it guards against accidentally breaking the contract by refactoring or renaming fields" (Uber Style Guide §Use field tags in marshaled structs).

**See also**: AP-26

---

## AP-43: Dynamic `Printf`-Style Format Strings

**Strength**: SHOULD-AVOID

**Summary**: `go vet` statically checks the format string in `fmt.Printf`-style calls against their arguments. If the format string is built at runtime (concatenation, `Sprintf`ing a format), vet cannot verify it and mismatched verbs slip through to production.

```go
// Bad — format string assembled at runtime
msg := "failed to " + action + ": %w"
return fmt.Errorf(msg, err)

// Bad — putting a format string in a non-const var
var errTmpl = "user %s not found at %d"
return fmt.Errorf(errTmpl, name, id) // vet can't check against callers

// Good — literal at the call site
return fmt.Errorf("failed to %s: %w", action, err)

// Good — if you need a shared template, use const
const errUserNotFound = "user %s not found at %d"
return fmt.Errorf(errUserNotFound, name, id)
```

**Rationale**: Uber §Format Strings outside Printf: "If you declare format strings for Printf-style functions outside a string literal, make them const values. This helps `go vet` perform static analysis of the format string." Vet's format-string check is one of Go's most useful static diagnostics; don't defeat it by computing format strings (Uber Style Guide §Format Strings outside Printf).

**See also**: AP-38

---

## AP-44: Logging an Error and Then Returning It

**Strength**: SHOULD-AVOID

**Summary**: Each error should be handled once. If you log and return, the caller is likely to log or propagate too, and the same error appears multiple times in logs — noise with little diagnostic value. Either handle the error (log and recover) or propagate it (wrap and return).

```go
// Bad — logs at every layer, then returns
u, err := getUser(id)
if err != nil {
    log.Printf("could not get user %q: %v", id, err)
    return err
}

// Good — wrap and return; let the outermost handler log
u, err := getUser(id)
if err != nil {
    return fmt.Errorf("get user %q: %w", id, err)
}

// Good — handle and degrade
if err := emitMetrics(); err != nil {
    // Metrics failure must not break the request; log once and move on.
    log.Printf("emit metrics: %v", err)
}
```

**Rationale**: Uber §Handle Errors Once: "Regardless of how the caller handles the error, it should typically handle each error only once. The caller should not, for example, log the error and then return it, because *its* callers may handle the error as well... **Bad**: Log the error and return it. Callers further up the stack will likely take a similar action with the error. Doing so makes a lot of noise in the application logs for little value." Pick one layer — usually the boundary, like an HTTP handler — to log (Uber Style Guide §Handle Errors Once).

**See also**: AP-11, AP-12

---

## AP-45: Writing Go in Java / C++ / Python Style

**Strength**: SHOULD-AVOID

**Summary**: Go has its own idioms. Patterns that are obviously correct in other languages — deep inheritance via embedding, `AbstractXxxFactory` types, mutation-heavy classes with getters/setters, `try`/`except` flow, monkey-patching — produce Go code that reads poorly, tests poorly, and fights the tooling.

```go
// Bad — Java-style architecture: interface hierarchy, factory, abstract base
type IUserService interface {
    IUser
    IAuditable
    Validate() error
}
type AbstractUserService struct{ /* protected fields */ }
func NewUserServiceFactory() UserServiceFactory { /* ... */ }

// Bad — Python-style: pass around maps instead of structs
func handle(opts map[string]any) {
    name := opts["name"].(string)   // any-cast soup
    retries, _ := opts["retries"].(int)
    // ...
}

// Bad — C++-style: new-everything, pointer to every primitive
mu := new(sync.Mutex)
count := new(int)
*count = 0

// Good — Go-style: small concrete type, small interface at the consumer
type User struct {
    ID   int64
    Name string
}

type UserStore struct{ db *sql.DB }
func (s *UserStore) Find(ctx context.Context, id int64) (*User, error) { /* ... */ }

// An HTTP handler defines only what it uses:
type userFinder interface {
    Find(ctx context.Context, id int64) (*User, error)
}
func ShowUser(finder userFinder) http.HandlerFunc { /* ... */ }

// Good — Go-style: struct with typed options, not a map
type HandleOptions struct {
    Name    string
    Retries int
}
func handle(opts HandleOptions) { /* ... */ }

// Good — Go-style: zero values are ready
var mu sync.Mutex
var count int // zero by default
```

**Rationale**: Every section of the Uber and Google guides is, in aggregate, a rebuttal of non-Go idioms. Google Decisions §Interfaces: "Focus on the required behavior rather than just abstract named patterns like 'service' or 'repository' and the like." Google Decisions §Generics: "In many applications, a conventional approach using existing language features (slices, maps, interfaces, and so on) works just as well without the added complexity, so be wary of premature use." Uber §Zero-value Mutexes and Uber §Package Names and Google §Getters all push toward a concrete, behavior-first, tooling-friendly style. When a Go reviewer says "this looks Java-ish," they usually mean: too many interfaces, too many layers, getters and setters where fields would do, factories that don't need to exist, and architecture-by-noun instead of behavior-by-function (Google Decisions §Interfaces; Google Best Practices §Avoid unnecessary interfaces; Uber Style Guide §Package Names; Uber Style Guide §Zero-value Mutexes are Valid).

**See also**: AP-25, AP-26, AP-27, AP-28, AP-30, AP-31

---

## AP-46: Never Build SQL by String Concatenation — Use Placeholders

**Strength**: MUST-NOT

**Summary**: Pass user input through placeholders; never concatenate into the SQL string.

```go
// Bad — SQL injection vulnerability
query := fmt.Sprintf("SELECT * FROM users WHERE email = '%s'", email)

// Good — parameterized
err := db.GetContext(ctx, &user,
    "SELECT id, name, email FROM users WHERE email = $1", email)
```

**Rationale**: Placeholders let the driver bind values safely and keep user-controlled data out of the SQL grammar. Any concatenation path — `fmt.Sprintf`, `+`, `strings.Builder` — eventually leaks an attacker-controlled string into a parsed query, opening the door to injection. Parameterized queries are the only defense that scales across drivers, dialects, and input types (source: `cc-skills-golang/skills/golang-security/references/injection.md`).

---

## AP-47: Always defer rows.Close() on sql.Rows

**Strength**: MUST

**Summary**: `sql.Rows` holds a pooled connection until closed — defer `rows.Close()` immediately after a successful `QueryContext`.

```go
// Bad — connection leak
rows, err := db.Query("SELECT id FROM users")
if err != nil { return err }
for rows.Next() { /* ... */ }
// rows never closed

// Good
rows, err := db.QueryContext(ctx, "SELECT id FROM users")
if err != nil { return err }
defer rows.Close()
for rows.Next() { /* ... */ }
if err := rows.Err(); err != nil { return err }
```

**Rationale**: The `*sql.Rows` value owns a connection from the pool until closed, and GC will not reclaim it fast enough under load. Forgetting `rows.Close()` causes the pool to exhaust, new queries to block, and the service to appear deadlocked. `defer rows.Close()` on the line immediately after the error check is the only safe pattern (source: `cc-skills-golang/skills/golang-database/SKILL.md`).

---

## AP-48: AES-ECB Mode Reveals Plaintext Patterns — Use GCM

**Strength**: MUST-NOT

**Summary**: Raw `block.Encrypt` is ECB mode, which reveals plaintext patterns. Wrap the block cipher in GCM for authenticated encryption.

```go
// Bad — ECB mode reveals patterns in structured data
block, _ := aes.NewCipher(key)
// using block.Encrypt directly == ECB mode

// Good — GCM provides authenticated encryption
aead, _ := cipher.NewGCM(block)
nonce := make([]byte, aead.NonceSize())
rand.Read(nonce)
ciphertext := aead.Seal(nonce, nonce, plaintext, nil)
```

**Rationale**: ECB encrypts each block independently, so identical plaintext blocks produce identical ciphertext blocks — structure leaks even without a key. GCM is randomized and authenticated, covering confidentiality and integrity in a single primitive. Calling `block.Encrypt` directly is almost never what you want; reach for `cipher.NewGCM` instead (source: `cc-skills-golang/skills/golang-security/references/cryptography.md`).

---

## AP-49: Never Reuse an AES-GCM Nonce

**Strength**: MUST-NOT

**Summary**: Generate a fresh random nonce per encryption — reusing a nonce with AES-GCM destroys confidentiality and authentication.

```go
// Bad — static or reused nonce
nonce := []byte("fixed_nonce!")

// Good — random nonce per encryption
nonce := make([]byte, 12) // 96-bit for GCM
rand.Read(nonce)
```

**Rationale**: GCM's security relies on the `(key, nonce)` pair being unique; reusing a nonce with the same key fully breaks the authenticator and leaks the XOR of plaintexts. The correct pattern is a 96-bit nonce (`make([]byte, 12)`) freshly read from `crypto/rand.Read` for every encryption operation. Never hardcode, derive, or counter nonces without a cryptographer signing off (source: `cc-skills-golang/skills/golang-security/references/cryptography.md`).

---

## AP-50: InsecureSkipVerify: true is Not an Acceptable Default

**Strength**: MUST-NOT

**Summary**: Disabling TLS certificate verification opens the client to man-in-the-middle attacks; pin a minimum TLS version and curve set instead.

```go
// Bad — disables certificate verification
transport := &http.Transport{
    TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
}

// Good — verified TLS with safe defaults
func secureConfig() *tls.Config {
    return &tls.Config{
        MinVersion:       tls.VersionTLS12,
        CurvePreferences: []tls.CurveID{tls.X25519, tls.CurveP256},
    }
}
```

**Rationale**: `InsecureSkipVerify: true` accepts any certificate, including attacker-presented ones — it is the TLS equivalent of turning off authentication entirely. Production code should instead pin `MinVersion: tls.VersionTLS12` (or later) and a safe curve list, and use a proper CA bundle or certificate pinning. If a self-signed cert is needed for tests, scope the relaxed config to the test binary only (source: `cc-skills-golang/skills/golang-security/references/cryptography.md`).

---

## AP-51: math/rand is Predictable — Use crypto/rand for Secrets

**Strength**: MUST

**Summary**: `math/rand` is deterministic from its seed; anything security-relevant (tokens, nonces, keys) must use `crypto/rand`.

```go
// Bad — predictable output
import "math/rand"
bytes := make([]byte, 16)
rand.Read(bytes)

// Good — cryptographically secure
import "crypto/rand"
_, err := rand.Read(bytes)
```

**Rationale**: `math/rand` produces a repeatable sequence an attacker can predict after observing a handful of outputs; it is only suitable for non-security uses like shuffling or jitter. `crypto/rand.Read` pulls from the OS CSPRNG and is the correct source for tokens, session IDs, GCM nonces, and key material. Import-path discipline — reach for `crypto/rand` whenever the output will be trusted — is the easiest way to avoid the trap (source: `cc-skills-golang/skills/golang-security/references/cryptography.md`).

---

## AP-52: filepath.Join Does Not Confine Paths — Use os.Root or Prefix-Check

**Strength**: MUST

**Summary**: `filepath.Join` cleans `..` but doesn't confine the result to the base; verify the cleaned path starts with the base, or use `os.Root` (Go 1.24+).

```go
// Bad — user escapes the base directory
base := "/srv/files"
userInput := "../../etc/passwd"
path := filepath.Join(base, userInput) // "/etc/passwd"

// Good — verify the result stays within the base
func safePath(base, userInput string) (string, error) {
    path := filepath.Join(base, userInput)
    if !strings.HasPrefix(filepath.Clean(path),
        filepath.Clean(base)+string(os.PathSeparator)) {
        return "", fmt.Errorf("path traversal attempt: %s", userInput)
    }
    return path, nil
}

// Good (Go 1.24+) — OS-level confinement
root, err := os.OpenRoot(base)
if err != nil { return err }
defer root.Close()
f, err := root.Open(userInput) // cannot escape root directory
```

**Rationale**: `filepath.Join` resolves `..` but happily returns paths above the base, so joining user input with a trusted prefix does nothing to prevent traversal. The two safe options are an explicit prefix check after `filepath.Clean`, or — on Go 1.24+ — `os.OpenRoot` which enforces confinement at the OS layer so no manual validation is needed. Prefer `os.Root` for new code; the prefix check is the backport-friendly fallback (source: `cc-skills-golang/skills/golang-security/references/filesystem.md` + `claude-skills (saisudhir14)/skills/go-security/SKILL.md`).

---

## AP-53: Pin the JWT Signing Algorithm

**Strength**: MUST

**Summary**: JWT validation must assert the signing algorithm — otherwise an attacker can switch RS256 to HS256 and sign with the public key.

```go
// Bad — parse without algorithm check; library trusts token's "alg" header
token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
    return publicKey, nil
})

// Good — pin the signing method before trusting the token
token, err := jwt.ParseWithClaims(tokenString, &jwt.RegisteredClaims{},
    func(token *jwt.Token) (interface{}, error) {
        // Pin signing algorithm — prevents algorithm confusion
        if _, ok := token.Method.(*jwt.SigningMethodRSA); !ok {
            return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
        }
        return publicKey, nil
    },
    jwt.WithIssuer("your-issuer"),
    jwt.WithAudience("your-audience"),
    jwt.WithExpirationRequired(),
)
```

**Rationale**: Without an algorithm check, a JWT library may accept whatever `alg` the token itself advertises — classic algorithm-confusion lets an attacker flip RS256 to HS256 and sign with the RSA public key as if it were an HMAC secret. Pinning the method type inside the key function closes the hole, and adding `WithIssuer`, `WithAudience`, and `WithExpirationRequired` tightens validation further. Never trust `token.Header["alg"]` to pick a verification key (source: `cc-skills-golang/skills/golang-security/references/architecture.md`).

---

## AP-54: Server-Side Identity, Never a Client-Supplied Header

**Strength**: MUST-NOT

**Summary**: Headers like `X-Is-Admin` or `X-User-ID` can be forged by any HTTP client; identity must be derived from a server-validated token.

```go
// Bad — trusting client-provided identity
func badHandler(w http.ResponseWriter, r *http.Request) {
    if r.Header.Get("X-Is-Admin") == "true" {
        adminPanel(w, r)
    }
}

// Good — server-side identity verification
func goodHandler(w http.ResponseWriter, r *http.Request) {
    claims := r.Context().Value(userClaimsKey).(*jwt.RegisteredClaims)
    if !hasRole(claims.Subject, "admin") {
        http.Error(w, "Forbidden", http.StatusForbidden)
        return
    }
    adminPanel(w, r)
}
```

**Rationale**: Anyone can set arbitrary request headers with `curl -H`, so `X-Is-Admin` or `X-User-ID` convey no authority whatsoever. Authorization must come from a cryptographically verified identity — a JWT validated by middleware, mTLS peer certificates, or a signed session cookie — attached to `r.Context()` so handlers read a trusted value. If a reverse proxy injects identity headers, the backend must also verify a shared secret or mTLS binding; otherwise any direct connection bypasses it (source: `cc-skills-golang/skills/golang-security/references/architecture.md`).

---

## AP-55: strings.Trim Takes a Cutset, Not a Prefix

**Strength**: MUST

**Summary**: `strings.Trim` takes a *set of characters*, not a substring — use `TrimPrefix`/`TrimSuffix` to remove literal prefixes or suffixes.

```go
// Bad — strips any chars in {a,p,l,i,c,t,o,n,/} from both ends
s := strings.Trim("application/json", "application/")
// Result: "js"

// Good — removes the literal prefix
s := strings.TrimPrefix("application/json", "application/")
// Result: "json"
```

**Rationale**: The second argument to `strings.Trim` is a cutset — each character is trimmed independently from both ends, not matched as a substring. Developers routinely mistake it for a prefix/suffix operation and ship subtly wrong code that passes happy-path tests. Reach for `strings.TrimPrefix` or `strings.TrimSuffix` whenever the intent is to remove a literal string (source: `cc-skills-golang/skills/golang-troubleshooting/references/common-go-bugs.md`).

---

## AP-56: Bounds-Check Integer Conversions of External Input

**Strength**: MUST

**Summary**: Go integer conversions silently truncate; bounds-check before converting from external input.

```go
// Bad — silent truncation
var big int64 = 256
small := int8(big)    // 0 — overflowed
n32 := int32(math.MaxInt64) // -1 — wrapped

// Good — check bounds before converting
func safeIntToInt32(n int64) (int32, error) {
    if n < math.MinInt32 || n > math.MaxInt32 {
        return 0, fmt.Errorf("value %d overflows int32", n)
    }
    return int32(n), nil
}
```

**Rationale**: Numeric conversions in Go do not panic on overflow — they silently wrap or truncate, so a length field from a decoded protocol message can land in a 32-bit slot as a negative number and bypass size checks. Any value originating from user input, file formats, or the network must be range-checked before narrowing the type. Wrap the check in a helper so the conversion is never written inline (source: `cc-skills-golang/skills/golang-troubleshooting/references/common-go-bugs.md`).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Anti-Pattern | Strength | Key Insight |
|----|--------------|----------|-------------|
| 01 | `init()` for program setup | SHOULD-AVOID | `init()` can't return errors; move to explicit helpers |
| 02 | Goroutines in `init()` | MUST-AVOID | Every import launches work with no off-switch |
| 03 | Panicking in libraries | MUST-AVOID | Return errors; let the caller decide |
| 04 | panic/recover as control flow | MUST-AVOID | Go has no exceptions; use error returns |
| 05 | `Must` functions in request path | MUST-AVOID | `Must` is for constant inputs at startup |
| 06 | `os.Exit` / `log.Fatal` outside `main` | SHOULD-AVOID | Helpers return errors, not kill the process |
| 07 | Mutable package globals | SHOULD-AVOID | Order-dependent tests; no multi-tenancy |
| 08 | Monkey-patching for tests | SHOULD-AVOID | Use dependency injection, not variable swap |
| 09 | `init()`-based registration | SHOULD-AVOID | Import-time side effects are invisible |
| 10 | Ignoring errors with `_` | MUST-AVOID | Every discard needs a comment or error check |
| 11 | "failed to" error prefix | SHOULD-AVOID | Wrapping adds context, not the word "failed" |
| 12 | No-op error wrapping | SHOULD-AVOID | Either add info or return the original |
| 13 | String-matching errors | MUST-AVOID | Sentinel values + `errors.Is`/`errors.As` |
| 14 | In-band error sentinels | SHOULD-AVOID | Multiple return values, not magic `-1` |
| 15 | Fire-and-forget goroutines | MUST-AVOID | Every goroutine needs a stop mechanism |
| 16 | `time.Sleep` for sync | MUST-AVOID | Use channels, `WaitGroup`, or `context` |
| 17 | Busy-waiting | SHOULD-AVOID | Block on a channel or `sync.Cond` |
| 18 | Arbitrary channel buffer size | SHOULD-AVOID | 0 or 1 unless you have a reason |
| 19 | Embedded public `sync.Mutex` | SHOULD-AVOID | Promotes Lock/Unlock onto the API |
| 20 | Copying a `sync.Mutex` | MUST-AVOID | Value receivers silently duplicate locks |
| 21 | Single-return type assertion | MUST-AVOID | Always use comma-ok |
| 22 | `new(sync.Mutex)` | SHOULD-AVOID | Zero value is valid |
| 23 | `iota` enums starting at 0 | SHOULD-AVOID | Reserve 0 for unset |
| 24 | Stringly-typed enums | SHOULD-AVOID | Named type + `iota` |
| 25 | Getter/setter wrappers | SHOULD-AVOID | Export the field or enforce an invariant |
| 26 | Stuttering names (`http.HTTPServer`) | SHOULD-AVOID | Package prefix is already present |
| 27 | `Manager`/`Service`/`Helper` names | SHOULD-AVOID | Name by behavior, not role |
| 28 | `util`/`common`/`helpers` packages | SHOULD-AVOID | Split by purpose |
| 29 | Returning interfaces by default | SHOULD-AVOID | Return concrete; caller picks the abstraction |
| 30 | Producer-defined interfaces | SHOULD-AVOID | Consumer defines what it uses |
| 31 | `any`/`interface{}` as escape hatch | SHOULD-AVOID | Generics or concrete types |
| 32 | `reflect` for polymorphism | SHOULD-AVOID | Generics or type switch |
| 33 | Loop-variable capture | MUST-AVOID | Pre-1.22 bug; fixed in 1.22 |
| 34 | Shadowing `ctx` in `if` | MUST-AVOID | Outer `ctx` keeps the old deadline |
| 35 | Shadowing built-ins / packages | SHOULD-AVOID | Don't name a variable `error` or `url` |
| 36 | Deep nesting of error branches | SHOULD-AVOID | Return early; keep happy path left |
| 37 | Unnecessary `else` | SHOULD-AVOID | `if` with return/continue needs no else |
| 38 | `fmt.Sprint` for primitives | SHOULD-AVOID | `strconv` is faster in hot paths |
| 39 | Repeated `[]byte("literal")` | SHOULD-AVOID | Hoist conversion out of the loop |
| 40 | No slice/map capacity hint | SHOULD-AVOID | `make([]T, 0, n)` when size is known |
| 41 | `panic` in test setup | SHOULD-AVOID | `t.Fatal` marks the test failed |
| 42 | Missing struct tags | SHOULD-AVOID | Pin the wire-format contract |
| 43 | Dynamic `Printf` format strings | SHOULD-AVOID | `go vet` can't check; use `const` |
| 44 | Log + return the same error | SHOULD-AVOID | Handle each error once |
| 45 | Java/C++/Python style in Go | SHOULD-AVOID | Follow Go idioms, not transplanted ones |
| 46 | Placeholders, never string-concat SQL | MUST-NOT | SQL injection by definition |
| 47 | Always `defer rows.Close()` | MUST | Connection leak otherwise |
| 48 | AES-GCM, never ECB | MUST-NOT | ECB leaks plaintext patterns |
| 49 | Fresh nonce per AES-GCM encryption | MUST-NOT | Reuse breaks auth + confidentiality |
| 50 | Never `InsecureSkipVerify: true` | MUST-NOT | MITM wide open |
| 51 | `crypto/rand` for secrets | MUST | `math/rand` is predictable |
| 52 | `os.Root` or prefix-check for paths | MUST | `filepath.Join` doesn't confine |
| 53 | Pin JWT signing algorithm | MUST | Prevents alg-confusion attack |
| 54 | Server-side identity, never `X-Is-Admin` | MUST-NOT | Headers are forgeable |
| 55 | `TrimPrefix` not `Trim` for affixes | MUST | `Trim` cutset bites |
| 56 | Bounds-check int conversions | MUST | Silent truncation |

---

## Related Guidelines

Each anti-pattern here maps to one or more positive-framing entries in the rest of the series. Read both sides: the anti-pattern to recognize the trap, the positive entry to see the idiomatic alternative.

### Core Idioms (`01-core-idioms.md`)

- **AP-01** (init misuse) → **CI-28** (Avoid `init()`)
- **AP-02** (goroutines in init) → **CI-28**, **CI-31** (Exit from `main` only)
- **AP-03** (panic in libs) → **CI-32** (Don't panic in library code)
- **AP-04** (panic/recover control flow) → **CI-32**
- **AP-05** (Must in request path) → **CI-33** (`Must` only at package init)
- **AP-06** (os.Exit outside main) → **CI-31** (Exit from `main` only)
- **AP-07** (mutable globals) → **CI-29** (Avoid mutable global state)
- **AP-08** (monkey-patching) → **CI-29**
- **AP-09** (init registration) → **CI-28**, **CI-29**
- **AP-10** (ignoring errors) → **CI-20** (Handle errors — don't ignore with `_`)
- **AP-18** (arbitrary buffer sizes) → **CI-36** (Channel size 0 or 1)
- **AP-21** (single-return assertion) → **CI-19** (Comma-ok idiom)
- **AP-22** (`new(Mutex)`) → **CI-16** (`&T{}` over `new(T)`), **CI-17** (`var x T` for zero)
- **AP-23** (enum at 0) → **CI-18** (iota enums; skip zero often)
- **AP-25** (getter/setter) → **CI-10** (No `Get` prefix on getter methods)
- **AP-26** (stuttering names) → **CI-05**, **CI-06**, **CI-08** (package names, initialisms)
- **AP-27** (Manager/Service/Helper) → **CI-05**, **CI-06** (package and type naming)
- **AP-28** (util packages) → **CI-06** (Avoid `util`/`common`/`helpers`)
- **AP-31** (`interface{}` overuse) → **CI-25** (`any` over `interface{}`)
- **AP-34** (ctx shadowing) → **CI-24** (Avoid shadowing built-ins and package names)
- **AP-35** (shadowing) → **CI-24**
- **AP-36** (deep nesting) → **CI-21** (Indent errors; left-align success)
- **AP-37** (unnecessary else) → **CI-22** (Reduce nesting — omit unnecessary `else`)
- **AP-42** (missing struct tags) → **CI-38** (Field tags for marshaling)
- **AP-43** (dynamic format strings) → **CI-39** (Format strings as `const`)

### API Design (`02-api-design.md`)

- **AP-14** (in-band errors) — API-design chapter covers explicit multiple-return APIs
- **AP-25** (getter/setter wrappers) — covered in API-design entries on zero values and constructors
- **AP-27** (Manager/Service/Helper) — covered in API-design entries on package and type naming

### Error Handling (`03-error-handling.md`)

- **AP-10** (ignoring errors) — chapter 03 extends the basic rule from CI-20 with wrapping, sentinel, and typed errors
- **AP-11** ("failed to" prefix) — chapter 03 §Error wrapping
- **AP-12** (no-op wrapping) — chapter 03 §Error wrapping
- **AP-13** (string-matching errors) — chapter 03 §Sentinel errors, `errors.Is`, `errors.As`
- **AP-44** (log + return) — chapter 03 §Handle each error once

### Type Design (`04-type-design.md`)

- **AP-20** (copying Mutex) — chapter 04 §Types that cannot be copied, §Receiver types
- **AP-22** (`new(T)` overuse) → **CI-16**, **CI-17** — chapter 04 explains when zero values are designed to be useful
- **AP-23** (iota 0 enums) — chapter 04 §Enumerated types
- **AP-24** (stringly-typed enums) — chapter 04 §Named types over primitives

### Interfaces & Methods (`05-interfaces-methods.md`)

- **AP-19** (embedded public Mutex) — chapter 05 §Embedding; Uber §Avoid Embedding Types in Public Structs
- **AP-29** (return interfaces) — chapter 05 §Accept interfaces, return concrete types
- **AP-30** (producer-defined interfaces) — chapter 05 §Interface ownership; consumer defines
- **AP-31** (`any` overuse) → **CI-25** — chapter 05 §Prefer small, specific interfaces
- **AP-32** (reflect) — chapter 05 §When generics; §When type switches

### Concurrency (`06-concurrency.md`)

- **AP-02** (goroutines in init) — chapter 06 §Goroutine lifetimes
- **AP-15** (fire-and-forget) — chapter 06 §Goroutine lifetimes, §`sync.WaitGroup`
- **AP-16** (`time.Sleep` sync) — chapter 06 §Channels and signaling; §Tickers vs sleeps
- **AP-17** (busy-wait) — chapter 06 §`sync.Cond` and channel blocking
- **AP-18** (buffer sizes) → **CI-36** — chapter 06 §Channel direction and size
- **AP-19** (embedded Mutex) — chapter 06 §Synchronization primitives
- **AP-20** (copying Mutex) — chapter 06 §Copying mutexes; `go vet -copylocks`
- **AP-33** (loop-var capture) — chapter 06 §Goroutine-safe loops; Go 1.22 semantics
- **AP-34** (ctx shadowing) — chapter 06 §Context propagation

### Testing (`07-testing.md`)

- **AP-08** (monkey-patching) — chapter 07 §Dependency injection in tests
- **AP-41** (panic in test setup) — chapter 07 §`t.Fatal` vs `t.Error` vs `panic`

### Performance (`08-performance.md`)

- **AP-38** (`fmt.Sprint` for primitives) — chapter 08 §`strconv` on hot paths
- **AP-39** (repeated `[]byte`) — chapter 08 §Avoiding repeated conversions
- **AP-40** (no capacity hint) — chapter 08 §`make` with capacity

### Project Structure (`10-project-structure.md`)

- **AP-28** (util packages) — chapter 10 §Package naming and organization
- **AP-07** (mutable globals) — chapter 10 §Dependency wiring from `main`

### Documentation (`11-documentation.md`)

- **AP-45** (Java/C++/Python style) — chapter 11 §Write for Go readers; doc conventions

---

## External References

- [*Effective Go*](https://go.dev/doc/effective_go) — the Go team's foundational idiom guide; the origin of "Don't communicate by sharing memory; share memory by communicating"
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — community-standard style reference, with hot-path performance benchmarks for most of the guidance
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Style Guide, Decisions, and Best Practices (three separate documents at increasing depth)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — the Go team's canonical review checklist; compact form of many of the same rules
- [Go Proverbs](https://go-proverbs.github.io/) — Rob Pike's distilled wisdom, including "The bigger the interface, the weaker the abstraction," "A little copying is better than a little dependency," and "Don't panic"
- Dave Cheney, [*Don't just check errors, handle them gracefully*](https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully)
- Dave Cheney, [*Never start a goroutine without knowing how it will stop*](https://dave.cheney.net/2016/12/22/never-start-a-goroutine-without-knowing-how-it-will-stop)
- Damien Neil and Jonathan Amsterdam, [*Working with Errors in Go 1.13*](https://go.dev/blog/go1.13-errors) — `errors.Is`, `errors.As`, and the `%w` verb
- [Go 1.22 release notes](https://go.dev/doc/go1.22) — loop-variable scope change (fixes AP-33)
- [`go vet`](https://pkg.go.dev/cmd/vet) — catches AP-20 (copylocks), AP-33 (loopclosure), AP-34 (shadow), AP-43 (printf)
- [`staticcheck`](https://staticcheck.dev/) — catches AP-10, AP-22, AP-37, and many more
- [`errcheck`](https://github.com/kisielk/errcheck) — catches AP-10 (ignored errors)
- [`go.uber.org/goleak`](https://pkg.go.dev/go.uber.org/goleak) — catches AP-02, AP-15 in tests
