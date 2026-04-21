# Go API Design

How to shape the exported surface of a Go package: function signatures, constructors, options, interfaces returned versus accepted, and the documentation contract callers rely on. These patterns are grounded in the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and *Effective Go*.

Target environment: **Go 1.22+**, **standard library first**, **`gofmt` + `go vet` + `staticcheck`** for formatting and linting.

This chapter assumes the fundamentals from `01-core-idioms.md`. It focuses on **the shape of the API** — what a caller sees, types, and calls. Implementation concerns (error handling, concurrency, type internals) are covered in later chapters.

---

## API-01: `context.Context` Is the First Parameter

**Strength**: MUST

**Summary**: Any function that may block, perform I/O, or cross an API boundary takes `ctx context.Context` as its first argument. Never store a `Context` inside a struct; pass it explicitly through every call.

```go
// Good
func (s *Server) Fetch(ctx context.Context, id string) (*Doc, error) { /* ... */ }
func Query(ctx context.Context, db *sql.DB, q string) (Rows, error) { /* ... */ }

// Bad — context hidden in a field
type Server struct {
    ctx context.Context // never do this
}
func (s *Server) Fetch(id string) (*Doc, error) { /* ... */ }

// Bad — context in the middle or at the end of the arg list
func Fetch(id string, ctx context.Context) (*Doc, error)
func Fetch(db *sql.DB, id string, ctx context.Context) (*Doc, error)
```

**Rationale**: Context carries deadlines, cancellation, and request-scoped values. Making it the first parameter is a universal Go convention, so callers always know where to pass one and reviewers can scan for missing cancellation wiring. Storing a `Context` in a struct ties its lifetime to the struct's lifetime instead of the call's — cancellation stops working. Google Decisions §Contexts: "A Context should be the first parameter of a function, typically named `ctx`. [...] Do not add a Context member to a struct type." (Google Decisions §Contexts; Effective Go §Context).

**See also**: API-02, API-35

---

## API-02: Do Not Define Custom `Context` Types

**Strength**: MUST-AVOID

**Summary**: Accept the standard `context.Context`. Do not create a wrapper type in your package's public API that substitutes for it.

```go
// Good
func Handle(ctx context.Context, req Request) (Response, error)

// Bad — forces every caller to adapt
type MyContext struct {
    context.Context
    UserID string
}
func Handle(ctx *MyContext, req Request) (Response, error)
```

**Rationale**: A custom context type leaks into every caller's signature and prevents use with libraries that speak plain `context.Context`. Put request-scoped values in the request struct, not in a custom context. Google Decisions §Custom contexts: "Do not create custom Context types or use interfaces other than `context.Context` in function signatures." If callers need extra data, add it to the function arguments or the request type (Google Decisions §Custom contexts).

**See also**: API-01, API-04

---

## API-03: Prefer Synchronous Functions over Callbacks and Channels

**Strength**: SHOULD

**Summary**: Return results directly. Let callers decide when concurrency is needed. Do not expose callbacks or channels as the primary API shape when a synchronous call will do.

```go
// Good — synchronous, composable
func Fetch(ctx context.Context, id string) (*Doc, error)

// Caller adds concurrency if they need it:
go func() { doc, err := Fetch(ctx, id); ... }()

// Bad — bakes goroutines into the API
func Fetch(ctx context.Context, id string, out chan<- *Doc, errs chan<- error)
func Fetch(ctx context.Context, id string, cb func(*Doc, error))
```

**Rationale**: Synchronous functions are easier to test, reason about, and compose. Google Decisions §Synchronous functions: "Prefer synchronous functions over asynchronous functions. [...] Callers that need concurrency can easily add it by calling the function from a separate goroutine. But it is difficult — sometimes impossible — for callers to remove unwanted concurrency from an asynchronous API." Channels and callbacks also complicate lifecycle: who closes, who drains, who cancels (Google Decisions §Synchronous functions).

**See also**: API-27, API-35

---

## API-04: Order Arguments by Dependency, Not by Convenience

**Strength**: SHOULD

**Summary**: Argument order follows a consistent pattern: `context.Context`, then required inputs (the "subject" first), then optional configuration. Related values that form a unit should be grouped into a struct.

```go
// Good
func Send(ctx context.Context, to Address, msg Message, opts ...Option) error
func Copy(ctx context.Context, dst io.Writer, src io.Reader) (int64, error) // matches io.Copy

// Bad — context buried, required and optional mixed
func Send(to Address, retries int, ctx context.Context, msg Message, logger *zap.Logger) error
```

**Rationale**: Consistent ordering lets readers skim a signature and match it against familiar shapes (`io.Copy(dst, src)`, `strings.Replace(s, old, new, n)`). Mixing optional and required arguments obscures the call site. Google Best Practices §Function argument lists: "Avoid long lists of arguments of the same type [...] Consider using a varargs parameter, a slice parameter, or a parameter with a named struct type to improve readability." When the list gets long, see API-05 (Google Best Practices §Function argument lists).

**See also**: API-05, API-06

---

## API-05: Use a Parameter Struct for Long or Ambiguous Argument Lists

**Strength**: SHOULD

**Summary**: When a function has more than three or four arguments — or two arguments of the same type that could be swapped by mistake — accept a named struct instead of a flat list.

```go
// Good
type PrintOpts struct {
    Duplex     bool
    Color      bool
    PageRange  string
}
func Print(ctx context.Context, doc *Document, opts PrintOpts) error

// Bad — easy to transpose the three bools
func Print(ctx context.Context, doc *Document, duplex, color, landscape bool, pages string) error
```

**Rationale**: A parameter struct gives each field a name at the call site (`PrintOpts{Duplex: true, Color: true}`), is extensible without breaking callers (just add a field with a safe zero value), and prevents transposition bugs when multiple arguments share a type. Google Best Practices §Function argument lists: a named struct is "often the right choice when the function takes more than a handful of arguments, or when several parameters have the same type." Uber's functional-options section makes the same three-argument threshold explicit (Google Best Practices §Function argument lists; Uber Style Guide §Functional Options).

**See also**: API-04, API-06, API-39

---

## API-06: Use Functional Options for Open-Ended Constructor Configuration

**Strength**: SHOULD

**Summary**: For constructors or public APIs whose configuration is likely to grow, accept `opts ...Option` where `Option` is an unexported-method interface. Callers pass only what they want; defaults fill in the rest.

```go
// Good
type Option interface{ apply(*options) }

type options struct {
    cache  bool
    logger *zap.Logger
}

type cacheOption bool
func (c cacheOption) apply(o *options) { o.cache = bool(c) }
func WithCache(c bool) Option { return cacheOption(c) }

type loggerOption struct{ log *zap.Logger }
func (l loggerOption) apply(o *options) { o.logger = l.log }
func WithLogger(log *zap.Logger) Option { return loggerOption{log: log} }

func Open(addr string, opts ...Option) (*Conn, error) {
    o := options{logger: zap.NewNop()}
    for _, opt := range opts {
        opt.apply(&o)
    }
    // ...
}

// Caller
db.Open(addr)
db.Open(addr, db.WithCache(true), db.WithLogger(log))

// Bad — every caller must pass every value
func Open(addr string, cache bool, logger *zap.Logger) (*Conn, error)
// Callers: db.Open(addr, false, zap.NewNop())  — meaningless literals
```

**Rationale**: Functional options keep the common case short and let the API grow without breaking callers. Uber §Functional Options: "Use this pattern for optional arguments in constructors and other public APIs that you foresee needing to expand, especially if you already have three or more arguments." Implementing the pattern with an `Option` interface (not a closure) allows options to be compared, logged, and mocked in tests (Uber Style Guide §Functional Options; Google Best Practices §Option structure).

**See also**: API-05, API-07

---

## API-07: Option Struct vs Functional Options — Pick the Lighter Weight That Works

**Strength**: CONSIDER

**Summary**: An option struct (`type Options struct { ... }`) is simpler; use it when configuration fields are independent, have safe zero values, and you do not need validation or runtime composition. Switch to functional options when you need defaults distinct from zero, validation at construction, or options that interact.

```go
// Good — option struct fits when zeros are fine
type ClientOptions struct {
    Timeout  time.Duration
    MaxConns int
}
func NewClient(addr string, o ClientOptions) *Client {
    if o.Timeout == 0 { o.Timeout = 30 * time.Second }
    if o.MaxConns == 0 { o.MaxConns = 10 }
    // ...
}

// Good — functional options fit when defaults or validation matter
func NewClient(addr string, opts ...Option) (*Client, error)
// WithTimeout can return an error-returning Option, enforce non-negative, etc.
```

**Rationale**: Functional options add machinery. Google Best Practices §Option structure: "An option struct is a struct type that collects some or all arguments of a function or method, that is then passed as the last argument to the function or method." §Variadic options: "We recommend using variadic options when the benefits are clear over passing a simple options struct." Choose by weighing call-site clarity vs implementation cost — most configs can start as an option struct (Google Best Practices §Option structure; Google Best Practices §Variadic options).

**See also**: API-05, API-06

---

## API-08: Constructors Are Named `New` or `NewX`

**Strength**: MUST

**Summary**: A package's primary constructor is `New` (when the package name disambiguates) or `NewX` where `X` is the type. A constructor that takes a source value for conversion is `NewXFromY`.

```go
// Good
package http
func NewRequest(method, url string, body io.Reader) (*Request, error)  // http.NewRequest

package user
func New(name, email string) *User                // called as user.New(...)

package config
func NewFromFile(path string) (*Config, error)    // source-based constructor

// Bad
func CreateUser(name, email string) *User         // "Create" is not idiomatic in Go
func MakeRequest(method, url string) *Request     // "Make" is reserved in spirit for make()
func BuildConfig(path string) (*Config, error)    // introduces a new verb
```

**Rationale**: Go's standard library is consistent: `bytes.NewBuffer`, `bufio.NewReader`, `http.NewRequest`, `sync.NewCond`. Callers learn one pattern and search for `New*` to find constructors. Uber §Function Names: "Follow Go community conventions of using MixedCaps for function names." Google Best Practices §Function and method names reinforces reading the call site: `config.NewFromFile(path)` reads as natural English (Uber Style Guide §Function Names; Google Best Practices §Function and method names).

**See also**: API-09, API-17

---

## API-09: Constructors Return `(*T, error)` or `*T` — Never Panic

**Strength**: MUST

**Summary**: If construction can fail (I/O, validation, parsing, external dependency), return `(*T, error)`. If it cannot fail, return `*T`. Constructors must not panic on invalid user input; reserve panics for programmer errors and `Must*` variants (see API-10).

```go
// Good
func NewServer(addr string) (*Server, error) {
    if addr == "" {
        return nil, errors.New("server: addr is required")
    }
    // ...
}

func NewCounter() *Counter { return &Counter{} }  // infallible

// Bad — panic on bad user input
func NewServer(addr string) *Server {
    if addr == "" {
        panic("addr is required")
    }
    // ...
}
```

**Rationale**: Libraries should not panic on caller mistakes; they should return errors so the caller can decide what to do. CI-32 in Chapter 1 covers the general "don't panic in libraries" rule; here it applies specifically to constructors because they are the most common place for user input to enter. Uber §Don't Panic: "Code running in production must avoid panics. Panics are a major source of cascading failures" (Uber Style Guide §Don't Panic; see CI-32).

**See also**: API-10, CI-32

---

## API-10: `Must*` Constructors Only for Package-Initialization Patterns

**Strength**: SHOULD

**Summary**: A `Must*` constructor that panics on error is acceptable only when the caller will use it at package initialization or in tests with a compile-time-known valid input. It must be a peer to the fallible constructor, not a replacement.

```go
// Good — both shapes exist
var re = regexp.MustCompile(`^[a-z]+$`)        // package var, input is a constant
func MustCompile(expr string) *Regexp          // panics on bad input

func Compile(expr string) (*Regexp, error)     // returns err on bad input (for runtime input)

// Bad — only offering Must*, forcing panics into request paths
func MustConnect(addr string) *Conn  // every runtime caller must recover
```

**Rationale**: `Must*` is shorthand for "the input is known valid at compile time; stop the program if I'm wrong." It is a peer to the normal constructor, not a substitute. Effective Go and Google Decisions §Panics both emphasize that libraries should return errors, with panic reserved for truly unrecoverable situations. Match `regexp.MustCompile` / `regexp.Compile` and `template.Must` / `template.New` as prior art (Google Decisions §Panics; CI-33).

**See also**: API-09, CI-32, CI-33

---

## API-11: Accept Interfaces, Return Concrete Types

**Strength**: SHOULD

**Summary**: Function parameters should be interfaces when behavior — not identity — is what matters. Return concrete types so callers see the real shape and can access type-specific methods.

```go
// Good
func Copy(dst io.Writer, src io.Reader) (int64, error)   // accepts interfaces
func NewBuffer(buf []byte) *bytes.Buffer                 // returns concrete *bytes.Buffer

// Bad
func Copy(dst *os.File, src *os.File) (int64, error)     // locks callers to *os.File
func NewBuffer(buf []byte) io.ReadWriter                 // hides Buffer-specific methods
```

**Rationale**: Accepting interfaces widens the set of callers that can use your function; returning concrete types widens the set of methods those callers can use. Go's `io` package is the canonical example: `io.Copy` accepts any `Reader`/`Writer`, but `bytes.NewBuffer` returns `*bytes.Buffer` so callers can call `Buffer.Bytes()`. Google Best Practices §Interfaces: "Go interfaces generally belong in the package that consumes values of the interface type, not a package that implements the interface type. The implementing package should return concrete (usually pointer or struct) types" (Google Best Practices §Interfaces; Effective Go §Interfaces).

**See also**: API-12, API-13

---

## API-12: Define Interfaces Where They Are Consumed, Not Where They Are Implemented

**Strength**: SHOULD

**Summary**: The interface declaration lives in the package that calls its methods. Implementations in other packages satisfy it structurally without importing it.

```go
// Good — package pdf consumes; package storage implements
package pdf

type BlobStore interface {         // defined where it is used
    Read(key string) ([]byte, error)
}

func Render(ctx context.Context, store BlobStore, key string) (*Doc, error) { /* ... */ }

package storage
type S3 struct{ /* ... */ }
func (s *S3) Read(key string) ([]byte, error) { /* ... */ } // implicitly satisfies pdf.BlobStore

// Bad — interface defined in the implementer, forces all users to import storage
package storage
type BlobStore interface { Read(key string) ([]byte, error) }
type S3 struct{}
func (s *S3) Read(key string) ([]byte, error) { /* ... */ }
```

**Rationale**: Consumer-defined interfaces keep the interface surface minimal (exactly what the consumer needs) and avoid forcing every implementation package to be imported by every user. Google Best Practices §Interfaces: "Go interfaces generally belong in the package that consumes values of the interface type, not a package that implements the interface type." This is the inverse of Java-style "interface in the implementer" and is the root cause of many Go interface-design mistakes (Google Best Practices §Interfaces; Google Best Practices §Avoid unnecessary interfaces).

**See also**: API-11, API-13, API-14

---

## API-13: Keep Interfaces Small — One Method Is Often Enough

**Strength**: SHOULD

**Summary**: The smallest useful interface is the best useful interface. If callers only need one method, accept a one-method interface. Compose larger interfaces from smaller ones.

```go
// Good — single method, broadly satisfied
type Flusher interface{ Flush() error }
func Shutdown(f Flusher) error { return f.Flush() }

// Good — composition
type ReadCloser interface {
    io.Reader
    io.Closer
}

// Bad — demands more than the function needs
type FileLike interface {
    Read(p []byte) (int, error)
    Write(p []byte) (int, error)
    Close() error
    Stat() (os.FileInfo, error)
    Sync() error
}
func Shutdown(f FileLike) error { return f.Close() }  // only Close() is used
```

**Rationale**: Small interfaces are satisfied by more types, are easier to mock in tests, and are easier to evolve. The Go proverb "the bigger the interface, the weaker the abstraction" is reflected in the standard library's `io.Reader`, `io.Writer`, `io.Closer`, `fmt.Stringer` — each one method. Google Best Practices §Designing effective interfaces: "The smaller the interface, the easier it is to provide an implementation." (Google Best Practices §Designing effective interfaces; Effective Go §Interfaces).

**See also**: API-11, API-12, API-14

---

## API-14: Don't Add Interfaces Until a Second Implementation Exists

**Strength**: SHOULD-AVOID

**Summary**: Resist the urge to create an interface for every type "for future flexibility." Wait until there is a real second implementation (production alternative, fake for testing, remote vs local). Until then, export the concrete type.

```go
// Good — one implementation, return the concrete type
package cache
type Cache struct { /* ... */ }
func New() *Cache { /* ... */ }
func (c *Cache) Get(key string) ([]byte, bool) { /* ... */ }

// Bad — speculative interface with one implementation
package cache
type Cache interface {
    Get(key string) ([]byte, bool)
    Set(key string, val []byte)
}
type memCache struct{ /* ... */ }
func New() Cache { return &memCache{} }  // hides the type from callers
```

**Rationale**: A one-implementation interface is dead weight: it adds a layer of indirection, hides documentation and field accessors, and makes the API harder to evolve (adding a method breaks all implementations). Google Best Practices §Avoid unnecessary interfaces: "Do not export interfaces if you do not have a real need for them. [...] If unsure, use a concrete type." The correct time to introduce an interface is when you need to substitute implementations — then introduce it in the consumer, per API-12 (Google Best Practices §Avoid unnecessary interfaces).

**See also**: API-11, API-12, API-13

---

## API-15: Prefer `io.Reader`/`io.Writer` over `[]byte` and `string` at Boundaries

**Strength**: SHOULD

**Summary**: When accepting bulk data, accept `io.Reader` (or `io.Writer` for output). Reserve `[]byte` and `string` for small, bounded values that truly belong in memory as a whole.

```go
// Good — streams, no memory cliff
func Parse(r io.Reader) (*Doc, error)
func Render(w io.Writer, doc *Doc) error

// Bad — forces the whole document into memory and copies it
func Parse(data []byte) (*Doc, error)
func Render(doc *Doc) ([]byte, error)
```

**Rationale**: Streaming interfaces let callers pipe from files, network connections, or generated content without materializing the whole blob. They also work with `io.LimitReader`, `io.TeeReader`, and `bufio` layers. When the input really is bounded and small (a name, a key, a short config), `string` is fine. For larger payloads, prefer `io.Reader`. The standard library chose this shape for `json.NewDecoder`, `encoding/csv`, `image.Decode`, etc. (Effective Go §Interfaces; Google Best Practices §Interfaces).

**See also**: API-11, API-13

---

## API-16: Zero Values Should Be Useful

**Strength**: SHOULD

**Summary**: Design types so `var x T` produces a usable value. A caller should be able to declare a value without calling a constructor unless invariants demand it.

```go
// Good — zero value works
var b bytes.Buffer            // ready to WriteString, Read, etc.
var wg sync.WaitGroup         // ready to Add, Done, Wait
var mu sync.Mutex             // ready to Lock, Unlock
type Config struct {
    Timeout time.Duration     // 0 = default
    Retries int               // 0 = no retry
}
var c Config                  // usable

// Bad — requires New before any use
type Buffer struct {
    buf []byte
    initialized bool          // every method has to check this
}
func (b *Buffer) Write(p []byte) (int, error) {
    if !b.initialized { return 0, errors.New("call NewBuffer first") }
    // ...
}
```

**Rationale**: Useful zero values eliminate an entire class of caller mistakes ("did I call New?") and make types composable (embedding, slices of structs). CI-11 in Chapter 1 introduced the idea; here we apply it to API surface: if your type *requires* initialization, provide a constructor and return it from every source — but strive to design the type so the constructor is unnecessary. Effective Go §The zero value: "The sync.Mutex does not have an explicit constructor or Init method. Instead, the zero value for a `sync.Mutex` is defined to be an unlocked mutex." (Effective Go §The zero value; Uber Style Guide §Zero-value Mutexes are Valid; CI-11).

**See also**: API-17, CI-11

---

## API-17: Require a Constructor When Invariants Cannot Be Encoded in the Zero Value

**Strength**: SHOULD

**Summary**: If a type has required fields, computed defaults, or resources that must be allocated (channels, maps, open files), provide a constructor and make the raw zero value unusable or explicitly documented as "empty."

```go
// Good — channel must be made; constructor is mandatory
type Pool struct {
    jobs chan Job
    workers int
}
func NewPool(workers int) *Pool {
    return &Pool{
        jobs:    make(chan Job),
        workers: workers,
    }
}

// Bad — zero value looks usable but deadlocks
type Pool struct {
    jobs chan Job  // nil chan blocks forever
    workers int
}
```

**Rationale**: Some types cannot have a useful zero value: channels and maps must be `make`'d, required dependencies have no sensible default, invariants must be checked. When that's the case, provide `New*` and make it clear in the doc comment that direct construction is not supported. This pairs with API-16: prefer a zero value, but when you can't, force the constructor (Effective Go §Allocation with new; Effective Go §Allocation with make).

**See also**: API-08, API-16

---

## API-18: No `Get` Prefix on Getters

**Strength**: SHOULD-AVOID

**Summary**: Go getters drop the `Get` prefix. The field `owner` is read by a method named `Owner()`, not `GetOwner()`. `Set` is fine for setters because it disambiguates from the field name.

```go
// Good
func (u *User) Name() string        { return u.name }
func (u *User) SetName(n string)    { u.name = n }

// Bad
func (u *User) GetName() string     { return u.name }
func (u *User) RetrieveName() string
```

**Rationale**: Go reads methods as nouns that describe what they return. `user.Name()` reads like a field access; `user.GetName()` reads like imported Java. The standard library and all major style guides agree. CI-10 introduced this; here it is re-stated as an API-design rule because getters are part of the exported surface. Google Decisions §Getters: "Function and method names should not use a `Get` or `get` prefix, unless the underlying concept uses the word 'get' (e.g. an HTTP GET)." (Google Decisions §Getters; Effective Go §Getters; CI-10).

**See also**: CI-10

---

## API-19: Name Exported Functions by Role, Not by Implementation

**Strength**: SHOULD

**Summary**: Exported function names describe what the function produces or does from the caller's perspective. Avoid leaking implementation details (`UseHashMap`, `BinarySearch`) unless the algorithm is the contract.

```go
// Good — name describes what the caller gets
func Lookup(key string) (*Record, bool)
func Encode(w io.Writer, v any) error

// Bad — leaks implementation
func LookupByHashMap(key string) (*Record, bool)
func EncodeWithReflection(w io.Writer, v any) error
```

**Rationale**: Implementation-flavored names create a maintenance trap: if you swap the data structure or algorithm, every caller sees a lie. Keep the call site stable by naming the behavior. When the algorithm is part of the promised semantics (e.g., `sort.SearchInts` is binary search by contract), naming it is fine. Uber §Function Names and Google Best Practices §Function and method names both emphasize role-based naming (Uber Style Guide §Function Names; Google Best Practices §Function and method names).

---

## API-20: Avoid Repeating the Package Name in Exported Identifiers

**Strength**: SHOULD-AVOID

**Summary**: The caller already writes `pkg.X`. Do not add `pkg` to the name of `X`.

```go
// Good
package user
func New(name string) *User
type User struct{ /* ... */ }
// Called as: user.New("Alice"), *user.User

// Bad
package user
func NewUser(name string) *User       // called as user.NewUser — stutters
type UserRecord struct{ /* ... */ }   // called as user.UserRecord — stutters

// Good — stutter is fine when the external name is the common form
package http
type Request struct{}                 // http.Request, not http.HTTPRequest
```

**Rationale**: The compiler forces callers to qualify with the package name. Repeating it makes every call site verbose. Google Best Practices §Avoid repetition: "Avoid including names in identifiers that are redundant given the context, such as the package name, a receiver type, or a variable type." The standard library is strict: `bytes.Buffer`, not `bytes.BytesBuffer`; `http.Request`, not `http.HTTPRequest` (Google Best Practices §Avoid repetition; Google Decisions §Package names; Effective Go §Package names).

**See also**: CI-05, CI-06

---

## API-21: Use Named Return Values Sparingly — for Documentation or Naked Deferred Writes

**Strength**: CONSIDER

**Summary**: Name return values when the name documents the meaning (e.g., `(n int, err error)` for bytes read) or when a `defer` needs to modify the returned error. Avoid named returns in other cases, and avoid naked `return` statements in long functions.

```go
// Good — names carry meaning
func (r *Reader) Read(p []byte) (n int, err error)

// Good — defer modifies the error
func Save(path string) (err error) {
    f, err := os.Create(path)
    if err != nil { return err }
    defer func() {
        if cerr := f.Close(); err == nil {
            err = cerr
        }
    }()
    // ...
    return nil
}

// Bad — naked return in a long function
func compute(x int) (result int, err error) {
    // ... 40 lines ...
    return   // what does `return` return here?
}
```

**Rationale**: Named returns are implicitly zero-initialized at function entry, which helps `defer` patterns that wrap the final error. But in long functions, naked `return` hides what is being returned. Google Decisions §Named result parameters: "Do not name result parameters just to avoid declaring a var inside the function. [...] They often help readers, however, when the parameters serve as documentation or when a `defer` closure needs to close over the return values." Uber §Naked Returns says the same (Google Decisions §Named result parameters; Uber Style Guide §Naked Returns).

**See also**: API-22

---

## API-22: Second Return Is `bool` (ok) or `error` — Never In-Band Sentinels

**Strength**: MUST

**Summary**: When a function can fail or "not find" something, return a second value: `(T, bool)` for lookup-style functions that cannot error, `(T, error)` for anything else. Do not encode failure in the first return (e.g., -1, "", nil with no second return).

```go
// Good
func Lookup(key string) (value string, ok bool)          // comma-ok
func Parse(s string) (v Value, err error)                // comma-err

// Bad — in-band sentinels force callers to know the magic value
func Lookup(key string) string        { return "" }      // what if "" is valid?
func IndexOf(s string, sub string) int { return -1 }     // -1 is a sentinel
```

**Rationale**: In-band sentinels make callers write `if x != -1` or `if v != ""`, which is easy to forget and can collide with valid values. Returning a second value makes the failure explicit and compiles-out the ambiguity. Google Decisions §In-band errors: "In C and similar languages, it's common for functions to return values like -1, null, or the empty string to signal errors or missing results. This is known as in-band error handling. [...] Go's support for multiple return values provides a better solution." (Google Decisions §In-band errors; CI-19).

**See also**: API-23, CI-19, CI-20

---

## API-23: `error` Return Is Last

**Strength**: MUST

**Summary**: When a function returns an error along with other values, `error` is the final return. Callers rely on this position for `if err != nil` patterns and error-checking linters.

```go
// Good
func Open(name string) (*File, error)
func Read(p []byte) (n int, err error)

// Bad
func Open(name string) (error, *File)
func Read(p []byte) (err error, n int)
```

**Rationale**: Every Go caller expects `err` last: `x, err := f()` is the universal shape. Swapping the order confuses readers, breaks `errcheck` heuristics, and forces mental translation at every call site. Effective Go §Multiple return values: "Go's multi-value returns [...] In Go, `Write` returns a count and an error: 'Yes, you wrote some bytes but not all of them because you filled the device'." By convention the error is last (Effective Go §Multiple return values; Google Decisions §Error handling).

**See also**: API-22, ch03 (Error Handling)

---

## API-24: Prefer Composition to Embedding in Exported Types

**Strength**: SHOULD-AVOID

**Summary**: Do not embed a type in a struct if you want to reuse its methods. Embedding lifts every method — including ones you don't mean to expose — into the outer type's API, and changes to the embedded type silently change yours.

```go
// Good — explicit composition, narrow surface
type Server struct {
    log *zap.Logger  // named field; only what we use
}
func (s *Server) Info(msg string) { s.log.Info(msg) }

// Bad — embedding leaks the full logger API into Server
type Server struct {
    *zap.Logger       // every Logger method is now a Server method
}
// Callers can now call server.With(...), server.Sync(), server.Core()
// If zap adds a method tomorrow, Server's API changes
```

**Rationale**: Embedding is a promotion mechanism, not an inheritance one. It is correct when you genuinely want to expose the embedded type's API as part of yours (e.g., a wrapper around `*sql.DB`), but in most cases it is a leak. Uber §Avoid Embedding Types in Public Structs: "Embedded types leak implementation details, inhibit type evolution, and obscure documentation." Use named fields and forward only the methods you mean to expose (Uber Style Guide §Avoid Embedding Types in Public Structs).

**See also**: API-25

---

## API-25: Do Not Embed `sync.Mutex` (or Other Syncers) in Exported Types

**Strength**: SHOULD-AVOID

**Summary**: When a struct contains a `sync.Mutex`, `sync.RWMutex`, `sync.WaitGroup`, or `sync.Cond`, make it an unexported field. Embedding exposes `Lock`/`Unlock` to callers and makes the locking protocol part of your public API.

```go
// Good — lock is an internal detail
type Cache struct {
    mu    sync.Mutex
    items map[string][]byte
}
func (c *Cache) Get(k string) []byte {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.items[k]
}

// Bad — embedding exposes Lock/Unlock
type Cache struct {
    sync.Mutex                          // callers can now cache.Lock()
    items map[string][]byte
}
```

**Rationale**: Locking is an implementation detail; exposing `Lock`/`Unlock` invites callers to hold the lock around unrelated work, breaks your concurrency guarantees, and freezes the locking strategy as part of your API contract. Uber §Zero-value Mutexes are Valid: "The zero value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex." Combined with §Avoid Embedding Types, this means: use an unexported `mu` field (Uber Style Guide §Zero-value Mutexes are Valid; Uber Style Guide §Avoid Embedding Types in Public Structs).

**See also**: API-24

---

## API-26: Verify Interface Compliance with a Compile-Time Assertion

**Strength**: SHOULD

**Summary**: When a type is *intended* to satisfy an interface, assert it at compile time with `var _ I = (*T)(nil)`. This catches drift the moment someone removes or renames a method.

```go
// Good — compile breaks if *Handler stops satisfying http.Handler
var _ http.Handler = (*Handler)(nil)

type Handler struct{}
func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) { /* ... */ }
```

**Rationale**: Go's structural satisfaction means a removed or renamed method only shows up at the consumer's call site — which may be in a different repository. A one-line assertion catches the regression at compile time in the implementing package. Uber §Verify Interface Compliance: "Verify interface compliance at compile time where appropriate. This includes types passed to APIs that expect specific interfaces, concrete types implementing interfaces that make up part of a returned API, or other cases where breaking interface compliance would be a compilation error." (Uber Style Guide §Verify Interface Compliance).

**See also**: API-11, API-12

---

## API-27: Channel Direction Is Part of the Function Signature

**Strength**: SHOULD

**Summary**: When a function takes or returns a channel, express whether it sends, receives, or both in the type. `chan<- T` for send-only, `<-chan T` for receive-only, `chan T` only when both directions are genuinely used.

```go
// Good
func Produce(ctx context.Context, out chan<- Job) error       // function only sends
func Consume(ctx context.Context, in <-chan Job) error        // function only receives
func (q *Queue) Jobs() <-chan Job                             // callers can only receive

// Bad — caller has no idea who may close or send
func Produce(ctx context.Context, c chan Job) error
func (q *Queue) Jobs() chan Job
```

**Rationale**: The direction encodes the protocol: a `chan<- T` cannot be closed by the caller, a `<-chan T` cannot be sent to. That narrows the contract to exactly what the caller may do and makes review trivial: "can this function close?" becomes a type question. CI-35 covered channel direction generally; here it is specifically about exported function signatures as part of the API surface (Uber Style Guide §Channel Size is One or None; CI-35).

**See also**: API-35, CI-35

---

## API-28: Pass Small Values, Pointer for Large or Mutating

**Strength**: SHOULD

**Summary**: Pass structs by value when they are small, non-mutated, and want value semantics (copies, safe to share). Use pointers for large structs, mutation, or types embedding `sync.Mutex`/`sync.WaitGroup`.

```go
// Good — small, immutable-feeling
func Distance(p, q Point) float64    // Point{X, Y float64}; 16 bytes

// Good — large or mutating
func (s *Server) Start() error       // Server owns state
func Parse(cfg *Config) error        // Config is large; don't copy per call

// Bad — pointer to a tiny value pointlessly
func Distance(p, q *Point) float64

// Bad — value receiver on something with a mutex
func (s Server) Start() error        // copies the mutex — race!
```

**Rationale**: Value passing is simpler to reason about: no aliasing, no nil checks. But large copies cost CPU and memory, mutating callers need a shared reference, and `sync` types must never be copied. Google Decisions §Pass values: "Pass small values; use pointers for larger values, for mutation, or when the type contains a Mutex." Uber §Receiver and Interface: "Use a value receiver unless the method [...] needs to mutate the receiver or the struct is large" (Google Decisions §Pass values; Google Decisions §Receiver type; Uber Style Guide §Receivers and Interfaces).

**See also**: API-29

---

## API-29: Receiver Type Is Consistent Across a Type's Methods

**Strength**: SHOULD

**Summary**: Within a single type, use the same receiver kind (value or pointer) on every method. Do not mix `func (s Server)` and `func (s *Server)` — pick one.

```go
// Good — all methods use *Server
func (s *Server) Start() error
func (s *Server) Stop() error
func (s *Server) Addr() string

// Bad — mixed receivers
func (s *Server) Start() error
func (s Server) Addr() string    // copy of Server; won't see mutations
```

**Rationale**: Mixed receivers cause subtle bugs: a value receiver method called on a `*Server` is fine, but assignments inside it vanish; a value receiver on a type with a `sync.Mutex` silently copies the lock. Consistency also matters for interface satisfaction: only `*T` satisfies an interface if any method has a pointer receiver. Google Decisions §Receiver type: "Use pointer receivers for types whose methods must mutate the receiver. [...] Once you decide, be consistent." (Google Decisions §Receiver type; Uber Style Guide §Receivers and Interfaces).

**See also**: API-28

---

## API-30: Use `time.Time` and `time.Duration` in Signatures, Not Numbers

**Strength**: MUST

**Summary**: Any API that exposes a point in time or a span of time uses `time.Time` and `time.Duration`. Never `int64` seconds, `int` milliseconds, or untyped constants.

```go
// Good
func Schedule(at time.Time, every time.Duration) (*Job, error)
func (c *Client) SetTimeout(d time.Duration)

// Bad
func Schedule(at int64, everyMillis int) (*Job, error)        // unit?
func (c *Client) SetTimeout(seconds int)                      // caller guesses
```

**Rationale**: `time.Duration` carries its unit in its type (`10 * time.Second`), so call sites are self-documenting. `time.Time` is timezone- and monotonic-clock-aware. Numeric durations force callers to remember the unit and make unit errors silent. CI-37 covered this as a general idiom; it is re-stated here because signatures are the place the rule matters most (Uber Style Guide §Use time.Duration; Uber Style Guide §Use time.Time; CI-37).

**See also**: CI-37

---

## API-31: Printf-Style Functions End in `f`; `vet` Depends On It

**Strength**: MUST

**Summary**: If a function takes a format string and variadic arguments, name it ending in `f` (`Printf`, `Errorf`, `Sprintf`, `Logf`). `go vet` uses the suffix to enable format-string checking.

```go
// Good
func (l *Logger) Infof(format string, args ...any)
func (l *Logger) Debugf(format string, args ...any)

// Bad — vet will not check the format string
func (l *Logger) Info(format string, args ...any)   // Info(...) should not take a format
```

**Rationale**: `go vet`'s printf analyzer turns on automatically for functions whose name ends in `f` and whose last parameter is `...any` (or `...interface{}`). Name a format-taking function without the `f` and vet silently stops checking your format strings, so mismatched `%d`/`%s` and missing arguments slip through. Uber §Naming Printf-style Functions: "When you declare a Printf-style function, make sure that `go vet` can detect it and check the format string." (Uber Style Guide §Naming Printf-style Functions).

**See also**: CI-39

---

## API-32: `internal/` Marks Hard Package Boundaries

**Strength**: SHOULD

**Summary**: Put packages under `internal/` when they are implementation details that must not be imported from outside your module (or subtree). The compiler enforces the boundary.

```
// Good — only example.com/app and its subpackages can import this
example.com/app/internal/auth
example.com/app/internal/storage

// Usable publicly
example.com/app/pkg/client
```

**Rationale**: `internal/` is a built-in Go mechanism: any package under `.../internal/...` is importable only by packages rooted at the parent of `internal/`. This lets you ship a public API (top-level packages) and keep the rest private without relying on naming conventions alone. It is the strongest tool Go offers for API-surface control. Effective Go discusses it as part of package organization; most large Go codebases rely on it to keep refactors safe (Effective Go §Names; Go spec §Import declarations).

**See also**: API-33

---

## API-33: One Package, One Concept

**Strength**: SHOULD

**Summary**: Each package should have a single clear responsibility that is obvious from its name. A package is not a directory for "things that live together"; it is a named unit of behavior.

```go
// Good
package user       // all things "user"
package http       // HTTP protocol
package jwt        // JWT tokens

// Bad
package models     // the anti-pattern: everything that is "a model"
package types      // same
package util       // same (see CI-06)
```

**Rationale**: When a package has one concept, `godoc` reads as a coherent document and the dependency graph stays acyclic. When it is a grab bag, every new file pulls in new dependencies and the package becomes hard to import without bringing everything. Google Best Practices §Package size: "Each Go package should have a clear purpose." Google Best Practices §Util packages: avoid `util` / `common`. CI-06 covers the naming aspect; this rule covers the cohesion aspect (Google Best Practices §Package size; Google Best Practices §Util packages; CI-05, CI-06).

**See also**: CI-05, CI-06, API-32

---

## API-34: Document Parameters, Return Values, and Errors in the Doc Comment

**Strength**: SHOULD

**Summary**: Exported function doc comments describe not just what the function does but what its parameters and return values mean, under what conditions it returns an error, and any special sentinel values.

```go
// Good
// Fetch retrieves the document with the given id.
//
// If id is empty, Fetch returns ErrInvalidID. If the document
// does not exist, Fetch returns a wrapped ErrNotFound. The
// returned Doc is safe to use until ctx is canceled.
func Fetch(ctx context.Context, id string) (*Doc, error)

// Bad
// Fetch fetches the document.
func Fetch(ctx context.Context, id string) (*Doc, error)
```

**Rationale**: The doc comment is the API contract. Callers should be able to understand how to invoke the function, what they get back, and what errors to handle — without reading the implementation. Google Best Practices §Documentation conventions: "The doc comment for any exported symbol should begin with the symbol's name. [...] Document how to use the parameters, what is returned, and any errors that may be returned." (Google Best Practices §Documentation conventions; CI-42).

**See also**: API-35, API-36, CI-42

---

## API-35: Document Concurrency Expectations

**Strength**: SHOULD

**Summary**: If a type is safe for concurrent use, say so in the doc comment. If it is not, say that too. If some methods are safe and others are not, say which.

```go
// Good
// Cache is an in-memory key-value store.
//
// All methods are safe for concurrent use by multiple goroutines.
type Cache struct { /* ... */ }

// Good
// Builder constructs a Query.
//
// Builder is not safe for concurrent use. Create one per goroutine.
type Builder struct { /* ... */ }

// Bad — caller must read the implementation
type Cache struct { /* ... */ }
```

**Rationale**: Concurrency safety is not inferable from the type alone. Leaving it implicit invites both over-locking (defensive callers) and data races (optimistic callers). Google Best Practices §Documentation conventions — Concurrency: "If a type or function is safe for concurrent use, its documentation should say so. If concurrent use is unsafe, say that as well." (Google Best Practices §Documentation conventions; Effective Go §Concurrency).

**See also**: API-34

---

## API-36: Document Resource Ownership and Cleanup

**Strength**: SHOULD

**Summary**: When a function returns a resource that must be closed or released, say so in the doc comment. When a function takes a resource it will close, say so as well. Ownership should never be guesswork.

```go
// Good
// Open returns a file opened for reading. The caller must Close the file
// when done.
func Open(path string) (*File, error)

// Good
// WriteTo writes the contents of r to w and returns the number of bytes written.
// WriteTo does not close r or w.
func WriteTo(w io.Writer, r io.Reader) (int64, error)

// Bad — who closes r?
func WriteTo(w io.Writer, r io.Reader) (int64, error)
```

**Rationale**: Go has no destructors, so the caller has to know who owns `Close`. Documenting it prevents leaks and double-closes. Google Best Practices §Documentation conventions — Cleanup: "If the caller is responsible for cleaning up (for example, by calling Close), the documentation should say so." The standard library's `os.Open` and `http.Response.Body` are the canonical examples (Google Best Practices §Documentation conventions).

**See also**: API-34, API-35

---

## API-37: Mark Deprecated Symbols with `// Deprecated:`

**Strength**: SHOULD

**Summary**: When you can't remove an exported symbol yet but want callers to migrate, add a doc comment paragraph beginning `Deprecated: ` and point to the replacement. Tools (IDE warnings, `staticcheck`) will surface the deprecation.

```go
// Good
// OldFetch retrieves the document with the given id.
//
// Deprecated: use Fetch instead. OldFetch will be removed in v2.
func OldFetch(id string) (*Doc, error) { return Fetch(context.Background(), id) }

// Bad — no standard marker
// DO NOT USE — prefer Fetch.
func OldFetch(id string) (*Doc, error)
```

**Rationale**: The `Deprecated:` marker is a Go-wide convention: `go doc` prints it prominently, IDEs strike through call sites, and `staticcheck` (SA1019) warns callers. Any other wording is ignored. Google Decisions §Deprecation and Google Best Practices both specify the exact format: a blank line above, `Deprecated: ` followed by a migration hint (Google Decisions §Deprecation; Google Best Practices §Documentation conventions).

---

## API-38: Avoid Bare `bool` Parameters — Use an Enum or Named Option

**Strength**: SHOULD-AVOID

**Summary**: A function with two or more `bool` parameters forces callers to pass `true, false, true` at the call site — unreadable and easy to transpose. Replace with a named enum type or an option.

```go
// Good — typed enum
type Mode int
const (
    ModeRead Mode = iota
    ModeWrite
    ModeAppend
)
func Open(path string, mode Mode) (*File, error)
// Call site: Open("/a", ModeWrite)

// Good — single bool with a descriptive name stays okay
func Trim(s string, removeTabs bool) string

// Bad — call site is unreadable
func Open(path string, write, append, truncate bool) (*File, error)
// Call site: Open("/a", true, false, true) — what do those mean?
```

**Rationale**: Booleans at call sites carry no meaning; an enum type names the choice and enables exhaustive-switch analysis. When there are multiple booleans, the odds of transposition grow. Google Best Practices §Function argument lists: "Avoid passing multiple parameters of the same type, particularly bool [...] Consider using a named type." (Google Best Practices §Function argument lists; CI-18).

**See also**: API-05, API-06, CI-18

---

## API-39: Exported Struct Fields Require Doc Comments and Stable Meanings

**Strength**: SHOULD

**Summary**: Every exported struct field has a doc comment describing what it means, its units (if applicable), and whether zero is a valid/default value. Once documented, the meaning is part of the API and cannot change silently.

```go
// Good
// Config configures a Client.
type Config struct {
    // Addr is the host:port of the server. Required.
    Addr string

    // Timeout is the maximum duration for a single request.
    // Zero means no timeout.
    Timeout time.Duration

    // MaxRetries is the number of retry attempts on transient errors.
    // Zero disables retries.
    MaxRetries int
}

// Bad — fields' meanings are implicit
type Config struct {
    Addr       string
    Timeout    time.Duration
    MaxRetries int
}
```

**Rationale**: Exported fields are part of the API; callers set them by name and rely on their documented behavior. Undocumented fields force readers into the source, and changing their interpretation later is a silent breaking change. Google Best Practices §Documentation conventions: "Every exported top-level type, function, method, constant, and variable should have a doc comment." Uber §Struct fields reinforces documenting units and defaults (Google Best Practices §Documentation conventions; CI-42).

**See also**: API-34, API-40, CI-42

---

## API-40: Name Fields in Struct Literals at API Boundaries

**Strength**: MUST

**Summary**: When constructing a value of a type defined in another package (or one whose fields may change), use named fields. Positional struct literals are forbidden by `go vet` for most external types and are brittle for your own.

```go
// Good
req := http.Request{
    Method: http.MethodGet,
    URL:    u,
    Body:   body,
}

cfg := Config{
    Addr:    "localhost:8080",
    Timeout: 5 * time.Second,
}

// Bad — positional, breaks when fields are added or reordered
req := http.Request{http.MethodGet, u, proto, protoMajor, /* ... */}
```

**Rationale**: Named fields survive refactors: add a field, reorder for readability, or deprecate one without breaking callers. Positional literals tie every call site to the exact current field order. `go vet`'s `composites` analyzer flags positional literals from imported packages by default. CI-14 introduced this at the language level; here it is re-stated as an API-consumer rule — when you accept a struct, your callers will write literals for it, and named fields protect them (CI-14; Uber Style Guide §Use Field Tags in Marshaled Structs; Go `vet` §composites).

**See also**: API-39, CI-14

---

## API-41: Functional Options over Positional Parameters or Struct-Field Defaults

**Strength**: SHOULD

**Summary**: For constructors with more than a couple of optional parameters, expose an `Option` type plus `With*` helpers and accept `opts ...Option`. Avoid long positional signatures or large config structs full of zero-value fields.

```go
// Good: functional options
type Option func(*Server)

func WithTimeout(d time.Duration) Option {
    return func(s *Server) { s.timeout = d }
}

func WithLogger(l *slog.Logger) Option {
    return func(s *Server) { s.logger = l }
}

func NewServer(addr string, opts ...Option) *Server {
    s := &Server{
        addr:    addr,
        timeout: 30 * time.Second,
        logger:  slog.Default(),
    }
    for _, opt := range opts {
        opt(s)
    }
    return s
}

// Usage is clean and extensible
srv := NewServer("localhost:8080",
    WithTimeout(60*time.Second),
    WithLogger(logger),
)

// Bad: positional parameters or large struct with zero values
func NewServer(addr string, timeout time.Duration, logger *slog.Logger, tls *tls.Config) *Server {
    // Adding new options requires new parameters or breaks existing calls
}
```

**Rationale**: Options keep the required arguments obvious at the call site while letting optional behavior grow without breaking existing callers. Defaults live next to the constructor rather than at every call site, and each `With*` helper gets its own doc comment describing units and semantics. Adding a new option is a non-breaking change (claude-skills (saisudhir14)/references/patterns.md).

**See also**: API-05, API-06, API-07

---

## API-42: Dependency Injection over Package-Level Globals

**Strength**: SHOULD

**Summary**: Pass collaborators such as databases, caches, and loggers as explicit constructor arguments on a struct. Do not reach for package-level `var` state initialized in `init()`.

```go
// Good: dependency injection
type Server struct {
    db     *sql.DB
    cache  Cache
    logger *slog.Logger
}

func NewServer(db *sql.DB, cache Cache, logger *slog.Logger) *Server {
    return &Server{db: db, cache: cache, logger: logger}
}

func (s *Server) GetUser(ctx context.Context, id string) (*User, error) {
    // Dependencies are explicit; easy to mock in tests
    return s.db.QueryRowContext(ctx, "SELECT * FROM users WHERE id=$1", id).Scan()
}

// Bad: mutable globals
var db *sql.DB

func init() {
    db, _ = sql.Open("postgres", os.Getenv("DSN"))
}

func GetUser(id string) (*User, error) {
    // GetUser implicitly depends on global db; hard to test
    return db.QueryRow("SELECT * FROM users WHERE id=$1", id).Scan()
}
```

**Rationale**: Explicit dependencies make the API's requirements legible and let tests substitute fakes or mocks without global teardown. `init()`-populated globals swallow errors, create hidden ordering constraints between packages, and prevent running two configurations side by side in the same process (claude-skills (saisudhir14)/references/patterns.md).

**See also**: API-08, API-11, API-12

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `context.Context` is first parameter | MUST | `ctx` first, never in a struct |
| 02 | No custom Context types | MUST-AVOID | Use plain `context.Context` |
| 03 | Prefer synchronous functions | SHOULD | Caller adds goroutines if needed |
| 04 | Argument order: ctx, required, optional | SHOULD | Consistent shape across the package |
| 05 | Parameter struct for long arg lists | SHOULD | >3 args or ambiguous same-type args |
| 06 | Functional options for extensible APIs | SHOULD | `opts ...Option` with interface |
| 07 | Option struct vs variadic options | CONSIDER | Use the lighter-weight that fits |
| 08 | Constructors named `New`/`NewX` | MUST | `NewXFromY` for conversions |
| 09 | Constructors return `(*T, error)` or `*T` | MUST | Never panic on user input |
| 10 | `Must*` only at init/test time | SHOULD | Peer to fallible constructor |
| 11 | Accept interfaces, return concrete | SHOULD | Wide inputs, rich outputs |
| 12 | Interfaces live with the consumer | SHOULD | Implementer stays decoupled |
| 13 | Small interfaces (one method often) | SHOULD | Compose for larger needs |
| 14 | No speculative interfaces | SHOULD-AVOID | Wait for second implementation |
| 15 | `io.Reader`/`io.Writer` over `[]byte` | SHOULD | Stream at boundaries |
| 16 | Zero values should be useful | SHOULD | Design around `var x T` working |
| 17 | Constructor required for invariants | SHOULD | When zero value would break |
| 18 | No `Get` prefix on getters | SHOULD-AVOID | `Name()` not `GetName()` |
| 19 | Name by role, not implementation | SHOULD | Keeps call site stable |
| 20 | No package name in identifiers | SHOULD-AVOID | `user.New`, not `user.NewUser` |
| 21 | Named returns sparingly | CONSIDER | For docs or deferred error wrap |
| 22 | Second return is `bool` or `error` | MUST | No in-band sentinels |
| 23 | `error` return is last | MUST | `(T, error)`, never `(error, T)` |
| 24 | Avoid embedding in public structs | SHOULD-AVOID | Use named fields |
| 25 | Don't embed `sync.Mutex` | SHOULD-AVOID | Keep locking private |
| 26 | Compile-time interface assertion | SHOULD | `var _ I = (*T)(nil)` |
| 27 | Channel direction in signatures | SHOULD | `chan<- T`, `<-chan T` |
| 28 | Pass small values, pointer for large | SHOULD | Mutation or size ⇒ pointer |
| 29 | Consistent receiver kind per type | SHOULD | All value or all pointer |
| 30 | `time.Time`/`time.Duration` in signatures | MUST | Unit-safe, typed |
| 31 | Printf functions end in `f` | MUST | `vet` requires it |
| 32 | `internal/` for hard boundaries | SHOULD | Compiler-enforced privacy |
| 33 | One package, one concept | SHOULD | Cohesion beats coincidence |
| 34 | Document params, returns, errors | SHOULD | The doc is the contract |
| 35 | Document concurrency expectations | SHOULD | Safe or not — say which |
| 36 | Document resource ownership | SHOULD | Who closes wins |
| 37 | `// Deprecated:` marker for migration | SHOULD | Tooling-recognized format |
| 38 | Avoid bare `bool` parameters | SHOULD-AVOID | Named enum at call sites |
| 39 | Doc comments on exported fields | SHOULD | Units, defaults, requiredness |
| 40 | Named fields in struct literals | MUST | Survives reorderings |
| 41 | Functional options | SHOULD | Extensible without breaking signatures |
| 42 | Dependency injection, not globals | SHOULD | Explicit deps, testable |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for foundations that underpin API design (CI-10 getters, CI-11 zero values, CI-14 named struct fields, CI-18 iota enums, CI-35 channel direction, CI-37 `time.Time`/`time.Duration`, CI-39 format-string constants, CI-42 doc comments)
- **Error Handling**: See `03-error-handling.md` for error types, wrapping, sentinels, and `errors.Is`/`errors.As` — extends API-22, API-23, API-34
- **Type Design**: See `04-type-design.md` for struct composition, type aliases vs definitions, and zero-value construction — extends API-16, API-17, API-24
- **Interfaces & Methods**: See `05-interfaces-methods.md` for interface-satisfaction patterns, method sets, and embedding rules — extends API-11, API-12, API-13, API-26, API-29
- **Concurrency**: See `06-concurrency.md` for goroutine lifetimes, channels, context propagation, and `sync` primitives — extends API-01, API-03, API-25, API-27, API-35
- **Testing**: See `07-testing.md` for mocking strategies that benefit from consumer-defined interfaces (API-12, API-14)
- **Anti-Patterns**: See `09-anti-patterns.md` for API-surface smells that amplify API-02, API-14, API-20, API-24

---

## External References

- [*Effective Go*](https://go.dev/doc/effective_go) — the Go team's foundational guide, including the sections on Interfaces, Getters, and Package names
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — Functional Options, Receivers and Interfaces, Verify Interface Compliance, Avoid Embedding Types in Public Structs, Naming Printf-style Functions
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions (Contexts, Receiver type, Pass values, Named result parameters, In-band errors, Getters, Interfaces, Synchronous functions) and Best Practices (Option structure, Variadic options, Function argument lists, Documentation conventions, Avoid unnecessary interfaces, Designing effective interfaces, Util packages, Package size)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — canonical review checklist; many API rules here trace back to it
- [`go vet` `printf` analyzer](https://pkg.go.dev/cmd/vet#hdr-Printf_family) — enforces API-31
- [`internal/` packages](https://go.dev/doc/go1.4#internalpackages) — compiler-enforced API boundary (API-32)
