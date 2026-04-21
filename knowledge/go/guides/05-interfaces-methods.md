# Interfaces and Methods

Guidelines for defining and using Go interfaces, and for writing methods on Go types. Go interfaces are satisfied *structurally* (implicitly), which makes them a tool for decoupling rather than declaration — the consequence is that interfaces in Go are designed, named, and placed very differently than in nominally-typed languages. These patterns are grounded in authoritative sources: the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and *Effective Go*.

Target environment: **Go 1.22+**, **standard library first**, **`gofmt` + `go vet` + `staticcheck`** for formatting and linting.

---

## IM-01: Accept Interfaces, Return Concrete Types

**Strength**: SHOULD

**Summary**: Functions should take interfaces as parameters and return concrete types. An interface parameter lets callers pass any satisfying value; a concrete return value gives callers access to every field and method of the result, not just a pre-chosen subset.

```go
// Good — accept an interface, return a concrete type
func NewUploader(r io.Reader) (*Uploader, error) {
    // ...
}

type Uploader struct { /* ... */ }

func (u *Uploader) Upload(ctx context.Context) error { /* ... */ }
func (u *Uploader) Progress() float64                { /* ... */ }

// Bad — returning an interface hides Progress() from callers
func NewUploader(r io.Reader) (Uploader, error) { /* ... */ }

type Uploader interface {
    Upload(context.Context) error
}
```

**Rationale**: Returning a concrete `*Uploader` lets the caller call `Progress()` without a type assertion. A caller who only wants the `Upload` method can still assign the returned pointer to a local interface variable. Returning an interface makes that decision for every caller, forever. Google Decisions §Interfaces: "Functions should take interfaces as arguments but return concrete types... Returning concrete types allows the caller to have access to every public method and field of that specific implementation, not just the subset of methods defined in a pre-chosen interface." Google Best Practices §Designing effective interfaces repeats the rule (Google Decisions §Interfaces; Google Best Practices §Interfaces; GoTip #49).

**Exceptions**: Return an interface when it is the product (e.g., `error`, `io.Reader`), when the function is a factory or strategy selecting among several concrete implementations at runtime, or when returning a concrete type would create an import cycle. See IM-07.

**See also**: IM-02, IM-07

---

## IM-02: Define Interfaces in the Consumer Package, Not the Producer

**Strength**: SHOULD

**Summary**: The package that *uses* an interface owns the interface definition. The package that implements it should just export concrete types. This keeps each interface minimal — it lists only the methods the consumer actually calls.

```go
// Good — consumer package defines the interface it needs
package report

// Storer is the subset of the storage API that report needs.
// Defined here, in the consumer, not in the storage package.
type Storer interface {
    Put(ctx context.Context, key string, data []byte) error
}

func Generate(ctx context.Context, s Storer, users []User) error {
    // uses only s.Put
}

// The producer package exports the concrete type.
package storage

type Client struct { /* ... */ }

func (c *Client) Put(ctx context.Context, key string, data []byte) error { /* ... */ }
func (c *Client) Get(ctx context.Context, key string) ([]byte, error)    { /* ... */ }
func (c *Client) Delete(ctx context.Context, key string) error           { /* ... */ }

// Bad — producer pre-defines a large interface that every consumer must accept
package storage

type Client interface {
    Put(ctx context.Context, key string, data []byte) error
    Get(ctx context.Context, key string) ([]byte, error)
    Delete(ctx context.Context, key string) error
    List(ctx context.Context, prefix string) ([]string, error)
    // ...fifteen more methods
}
```

**Rationale**: Because Go satisfies interfaces structurally, the consumer can declare exactly the methods it uses without the producer's cooperation. This has three benefits: (1) the interface documents *what the consumer depends on* rather than the producer's full API; (2) consumers can be tested with a stub that implements only those methods; (3) the producer remains free to add methods to the concrete type without forcing every consumer to update. Google Decisions §Interfaces: "The consumer of the interface should define it (not the package implementing the interface), ensuring it includes only the methods they actually use." Google Best Practices §Interface ownership and visibility: "In Go, interfaces generally belong in the package that uses them, not the package that implements them" (Google Decisions §Interfaces; Google Best Practices §Interface ownership and visibility; GoTip #78).

**See also**: IM-03, IM-06

---

## IM-03: Keep Interfaces Small — One or a Few Methods

**Strength**: SHOULD

**Summary**: The smallest useful interface is best. Single-method interfaces are the Go idiom: `io.Reader`, `io.Writer`, `io.Closer`, `fmt.Stringer`, `error`. A large interface is harder to implement, harder to mock, and harder to compose.

```go
// Good — single responsibility, minimal surface
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Good — a specialized consumer defines just what it needs
type lineCounter interface {
    Read(p []byte) (int, error)  // not even the full io.Reader
}

// Bad — a "god interface" that pre-combines unrelated concerns
type Storage interface {
    Read(key string) ([]byte, error)
    Write(key string, data []byte) error
    Delete(key string) error
    Lock(key string) error
    Unlock(key string) error
    Metrics() Metrics
    Healthcheck(ctx context.Context) error
    Migrate(ctx context.Context, schema Schema) error
}
```

**Rationale**: "The bigger the interface, the weaker the abstraction" (Rob Pike). A small interface makes fewer demands on implementers, so more types satisfy it by accident — which is exactly the point of structural typing. Small interfaces also compose cleanly (see IM-05). Google Decisions §Interfaces: "Design interfaces to be small for easier implementation and composition." Google Best Practices §Designing effective interfaces: "Keep interfaces small: The larger the interface, the harder it is to implement and to write code that takes advantage of it" (Google Decisions §Interfaces; Google Best Practices §Designing effective interfaces; GoTip #78: Minimal Viable Interfaces).

**See also**: IM-04, IM-05

---

## IM-04: Name Single-Method Interfaces with the `-er` Suffix

**Strength**: SHOULD

**Summary**: By convention, an interface with one method is named after the method plus the agent suffix `-er`. `Read` → `Reader`, `Write` → `Writer`, `Close` → `Closer`, `String` → `Stringer`. If the base method name does not form a grammatical English word with `-er`, adjust it minimally.

```go
// Good — idiomatic single-method interfaces
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Closer interface {
    Close() error
}

type Stringer interface {
    String() string
}

// A method named Serve naturally becomes Server
type Server interface {
    Serve(l net.Listener) error
}

// Good — compound when -er alone is awkward
type Walker interface {  // for Walk
    Walk(fn func(path string) error) error
}

// Bad — nominal "interface name" style from other languages
type IReader interface {
    Read(p []byte) (n int, err error)
}
type ReaderInterface interface { /* ... */ }
type AbstractReader interface { /* ... */ }
```

**Rationale**: The `-er` convention is pervasive in the standard library and reads naturally in prose: "the function takes a `Reader`." Hungarian-style `I` prefixes (`IReader`) or the `Interface` suffix (`ReaderInterface`) clash with Go's conventions. Effective Go §Interface names: "By convention, one-method interfaces are named by the method name plus an `-er` suffix or similar modification to construct an agent noun: `Reader`, `Writer`, `Formatter`, `CloseNotifier` etc." (Effective Go §Interface names).

**Exception**: Multi-method interfaces describe a role or protocol and are named after the role (`http.Handler`, `sort.Interface`, `hash.Hash`), not with `-er`.

**See also**: IM-03

---

## IM-05: Compose Larger Interfaces by Embedding Smaller Ones

**Strength**: SHOULD

**Summary**: Build larger interfaces by embedding smaller ones, not by listing all methods again. `io.ReadWriter` is literally `{ Reader; Writer }`.

```go
// Good — composition by embedding
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

type Closer interface {
    Close() error
}

type ReadWriter interface {
    Reader
    Writer
}

type ReadWriteCloser interface {
    Reader
    Writer
    Closer
}

// Bad — restating methods defeats the composition
type ReadWriter interface {
    Read(p []byte) (n int, err error)
    Write(p []byte) (n int, err error)
}
```

**Rationale**: Embedding makes the relationship between interfaces explicit: `ReadWriter` is declaratively `Reader + Writer`, not accidentally so. Callers that already have a `Reader` can see at a glance that it is a component of a `ReadWriter`. When the embedded interface changes, the embedding interface updates automatically. Effective Go §Embedding describes this pattern with the canonical `io.ReadWriter` example. Google Decisions §Interfaces: "Small interfaces are easier to compose into larger ones if needed" (Effective Go §Embedding; Google Decisions §Interfaces; Google Best Practices §Designing effective interfaces).

**Note**: Interface embedding is a *type* relationship, unrelated to struct embedding (see IM-29 for that).

**See also**: IM-03, IM-29

---

## IM-06: Don't Create Interfaces Until a Real Need Exists

**Strength**: SHOULD-AVOID

**Summary**: Avoid speculative interfaces. Introduce an interface only when you have at least one of: multiple real implementations, a package-boundary decoupling need, or a large concrete API you want to narrow for a specific consumer.

```go
// Bad — speculative "abstraction" with one implementation
type UserService interface {
    GetUser(id string) (*User, error)
    CreateUser(u *User) error
}

type userService struct{ db *sql.DB }
func (s *userService) GetUser(id string) (*User, error) { /* ... */ }
func (s *userService) CreateUser(u *User) error         { /* ... */ }

func NewUserService(db *sql.DB) UserService { /* ... */ }

// Good — just the concrete type until a second implementation appears
type UserService struct{ db *sql.DB }

func NewUserService(db *sql.DB) *UserService { /* ... */ }

func (s *UserService) GetUser(id string) (*User, error) { /* ... */ }
func (s *UserService) CreateUser(u *User) error         { /* ... */ }
```

**Rationale**: An interface added before there is a reason for one is almost always a one-to-one mirror of a single concrete type — it doubles the API surface, adds an indirection, and rarely survives contact with a real second implementation. When a second implementation does appear, you can introduce the interface *in the consumer* (see IM-02) without changing the existing producer. Google Decisions §Interfaces: "Avoid creating interfaces until a real need exists. Focus on the required behavior rather than just abstract named patterns like 'service' or 'repository' and the like." Google Best Practices §Avoid unnecessary interfaces: "The most common mistake is creating an interface before a real need exists" (Google Decisions §Interfaces; Google Best Practices §Avoid unnecessary interfaces).

**When interfaces are warranted**: (1) two or more concrete types must be handled by the same logic; (2) breaking a circular import; (3) narrowing a large concrete API for a specific caller. Otherwise, prefer the concrete type.

**See also**: IM-02, IM-07

---

## IM-07: Valid Reasons to Return an Interface

**Strength**: CONSIDER

**Summary**: Despite IM-01, there are specific cases where returning an interface is the right choice: encapsulation of an implementation with internal-only methods; factory/strategy functions that can produce several concrete types; and returning a type whose concrete form would create an import cycle.

```go
// Good — encapsulation. ThrottledReader has an internal Refill method
// that should not be exposed to normal consumers.
type ThrottledReader struct {
    source  io.Reader
    limit   int
    balance int
}

func (t *ThrottledReader) Read(p []byte) (int, error) { /* ... */ }

// Refill is called only by an internal coordinator.
func (t *ThrottledReader) Refill(amount int) { /* ... */ }

// New returns an io.Reader, not *ThrottledReader: callers cannot call Refill.
func New(r io.Reader, bytesPerSec int) io.Reader {
    return &ThrottledReader{source: r, limit: bytesPerSec}
}

// Good — factory chooses among concrete types at runtime
func NewWriter(format string) io.Writer {
    switch format {
    case "json":
        return &jsonWriter{}
    case "xml":
        return &xmlWriter{}
    default:
        return &textWriter{}
    }
}

// Good — error is always returned as the interface, never the concrete type
func Fetch(url string) ([]byte, error) {
    // ...
    return nil, &NetworkError{URL: url, Cause: err}  // returns error, not *NetworkError
}
```

**Rationale**: These are the three cases the Google style guide explicitly sanctions. The `error` interface is the canonical example of encapsulation. Factories naturally return the interface because the concrete type is chosen at runtime. Circular-import avoidance is sometimes necessary but is often a signal of mis-sized packages (see IM-06). Google Best Practices §Designing effective interfaces: "Returning an interface is the idiomatic choice... Encapsulation... Certain patterns [command, chaining, factory, strategy]... Avoiding circular dependencies." Google Decisions §Interfaces: "Sometimes returning an interface is acceptable for encapsulation (e.g., `error` interface), and certain constructs like command, chaining, factory, and strategy patterns" (Google Best Practices §Designing effective interfaces; Google Decisions §Interfaces).

**See also**: IM-01, IM-06

---

## IM-08: Keep Internal Interfaces Unexported

**Strength**: SHOULD

**Summary**: If an interface is only used within the package, keep it unexported. Exporting an interface makes it part of your API and commits you to maintaining it.

```go
// Good — unexported interface used only by this package's logic
package cache

type loader interface {
    Load(ctx context.Context, key string) ([]byte, error)
}

type Cache struct {
    l loader
}

func New(l loader) *Cache { return &Cache{l: l} }

// Bad — Loader exported even though no other package asks for it
type Loader interface {
    Load(ctx context.Context, key string) ([]byte, error)
}
```

**Rationale**: Exporting an identifier is a promise to external callers. Every exported interface expands your public API, adds cognitive load for readers of the package's doc, and locks in the method signatures. If the interface is purely an internal decoupling tool, nothing outside the package needs to name it. Google Decisions §Interfaces: "Keep interface types unexported if they are only used internally within a package." Google Best Practices §Interface ownership and visibility: "Do not export interface types unnecessarily" (Google Decisions §Interfaces; Google Best Practices §Interface ownership and visibility).

---

## IM-09: Export an Interface When It Is the Product (Protocol, Plugin Contract)

**Strength**: CONSIDER

**Summary**: Export an interface from the producer when the interface *is* the contract — when many implementations will conform to it, or it acts as a published protocol. `io.Writer`, `hash.Hash`, and protobuf service interfaces are canonical examples.

```go
// Good — hash.Hash is a protocol; many implementations exist
package hash

type Hash interface {
    io.Writer
    Sum(b []byte) []byte
    Reset()
    Size() int
    BlockSize() int
}

// Good — plugin contract published from a neutral package
package logplugin

type Logger interface {
    Log(level Level, msg string, attrs ...Attr)
}

// Implementations live in dozens of external packages that all import logplugin.
```

**Rationale**: When an interface defines a boundary that many independent implementations target, centralizing it avoids *interface bloat* — the situation where every consumer redefines a slightly different version of the same contract. In such cases the interface should typically live in a small, dependency-light package so that consumers don't pull in the entire world to reference it. Google Best Practices §Interface ownership and visibility: "When a package's primary purpose is to provide a common protocol that many different implementations must follow, the producer defines the interface... In large codebases, maintenance becomes difficult if numerous packages utilize the same `AuthService` while each defining an identical `type Authorizer interface`" (Google Best Practices §Interface ownership and visibility).

**See also**: IM-02, IM-08

---

## IM-10: Don't Pass a Pointer to an Interface

**Strength**: MUST-AVOID

**Summary**: `*io.Reader` is almost always wrong. An interface value already contains two words (type and data); the data word holds a pointer if the concrete type is a pointer. If a method needs to mutate the underlying concrete value, store a pointer *in* the interface value instead.

```go
// Good — pass the interface by value; the data it wraps may be a pointer
func Copy(dst io.Writer, src io.Reader) (int64, error) { /* ... */ }

var buf bytes.Buffer
io.Copy(os.Stdout, &buf)  // &buf is a *bytes.Buffer stored inside the io.Reader

// Bad — pointer to interface
func Copy(dst *io.Writer, src *io.Reader) (int64, error) { /* ... */ }

// Bad — accidentally taking a pointer to an interface variable
func handle(w io.Writer) {
    doSomething(&w)  // almost never right
}
```

**Rationale**: An interface value has two fields: a type descriptor and a data pointer. Taking `*interface` adds a useless indirection because the interface value is already effectively a handle. To let an interface method mutate the underlying value, you put a pointer type inside the interface (e.g., `var w io.Writer = &buf`). Uber §Pointers to Interfaces: "You almost never need a pointer to an interface. You should be passing interfaces as values—the underlying data can still be a pointer... If you want interface methods to modify the underlying data, you must use a pointer [type as the concrete value]." Google Decisions §Pass values: "Do not pass pointers as function arguments just to save a few bytes... Common instances of this include passing a pointer to a string (`*string`) or a pointer to an interface value (`*io.Reader`)" (Uber Style Guide §Pointers to Interfaces; Google Decisions §Pass values).

---

## IM-11: Pointer Receivers for Mutation; Value Receivers for Read-Only

**Strength**: MUST

**Summary**: If the method modifies the receiver, or the receiver contains a field that must not be copied (a `sync.Mutex`, a `bytes.Buffer`), the receiver must be a pointer. If the method is read-only and the type is cheap to copy, a value receiver is acceptable.

```go
// Good — mutation needs pointer receiver
type Counter struct{ n int }

func (c *Counter) Inc()      { c.n++ }      // mutates
func (c *Counter) Value() int { return c.n } // read-only but see IM-12 for consistency

// Good — type contains a sync.Mutex that must not be copied
type SafeMap struct {
    mu sync.Mutex
    m  map[string]int
}

func (s *SafeMap) Put(k string, v int) { /* must be *SafeMap */ }
func (s *SafeMap) Get(k string) int    { /* must be *SafeMap */ }

// Good — small value type, read-only, no fields to protect
type Point struct{ X, Y float64 }

func (p Point) Distance(q Point) float64 {
    return math.Hypot(p.X-q.X, p.Y-q.Y)
}

// Bad — value receiver silently drops the mutation
type Counter struct{ n int }

func (c Counter) Inc() { c.n++ }  // operates on a copy, original unchanged
```

**Rationale**: A value receiver gets a copy of the receiver. Mutating that copy is a silent no-op on the original. Copying a struct that contains a mutex duplicates the locked state incorrectly. Google Decisions §Receiver type: "If the method needs to mutate the receiver, the receiver must be a pointer... If the receiver is a struct containing fields that cannot safely be copied, use a pointer receiver. Common examples are `sync.Mutex` and other synchronization types." Google Decisions §Copying: "In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`." Uber §Receivers and Interfaces has the same rule (Google Decisions §Receiver type; Google Decisions §Copying; Uber Style Guide §Receivers and Interfaces).

**See also**: IM-12, IM-13, IM-14

---

## IM-12: Be Consistent — All Methods on a Type Use the Same Receiver Kind

**Strength**: SHOULD

**Summary**: Choose pointer receivers or value receivers per type and apply consistently to every method on that type. Mixing creates confusing method sets and awkward call sites.

```go
// Good — every method on User uses *User
type User struct { name string }

func (u *User) Name() string     { return u.name }
func (u *User) SetName(n string) { u.name = n }
func (u *User) Valid() bool      { return u.name != "" }

// Good — every method on Point uses a value receiver
type Point struct{ X, Y float64 }

func (p Point) Add(q Point) Point      { return Point{p.X + q.X, p.Y + q.Y} }
func (p Point) Scale(k float64) Point  { return Point{p.X * k, p.Y * k} }
func (p Point) Magnitude() float64     { return math.Hypot(p.X, p.Y) }

// Bad — mixed kinds on the same type
type User struct{ name string }

func (u User) Name() string      { return u.name }  // value
func (u *User) SetName(n string) { u.name = n }     // pointer — the method set of User now differs from *User
```

**Rationale**: A type with mixed receivers has two distinct method sets. `T` has only the value-receiver methods; `*T` has both. That means `T` may satisfy one interface while `*T` satisfies another, and callers must remember which variables are pointers. Google Decisions §Receiver type: "As a general guideline, prefer to make the methods for a type either all pointer methods or all value methods." When in doubt, use a pointer (Google Decisions §Receiver type; Effective Go §Pointers vs. Values).

**See also**: IM-11, IM-14

---

## IM-13: Value Receivers for Small Types, Maps, Channels, Slices Without Reslicing

**Strength**: SHOULD

**Summary**: Specific types conventionally use value receivers even when they have methods: small POD structs (like `time.Time`), map types, channel types, function types, and slice types that do not reslice or grow.

```go
// Good — small immutable value type
type Duration int64

func (d Duration) Seconds() float64 { return float64(d) / 1e9 }
func (d Duration) String() string   { /* ... */ }

// Good — map type
type Header map[string][]string

func (h Header) Add(key, value string) { h[key] = append(h[key], value) }
func (h Header) Get(key string) string { /* ... */ }

// Good — slice method that reads, does not grow
type Buffer []byte

func (b Buffer) Len() int { return len(b) }

// Good — slice method that mutates *length* or reallocates needs pointer
type Queue []Item

func (q *Queue) Push(x Item) { *q = append(*q, x) }

// Bad — pointer receiver on a map type is unnecessary; the map is already a reference
type Header map[string][]string
func (h *Header) Add(key, value string) { (*h)[key] = append((*h)[key], value) }
```

**Rationale**: Maps, channels, and slices are already reference-like — they carry internal pointers — so a value receiver on the header is cheap and callers don't need a pointer to mutate the underlying data. Small fixed-size value types (`time.Time`, small `struct`s with no mutexes or buffers) are copied without cost and feel more natural as values. Reslicing (`append` that may reallocate, or `*q = ...`) *does* need a pointer, because you are overwriting the slice header itself. Google Decisions §Receiver type: "If the receiver is a slice and the method doesn't reslice or reallocate the slice, use a value... If the receiver is a map, function, or channel, use a value rather than a pointer... If the receiver is a 'small' array or struct that is naturally a value type with no mutable fields and no pointers, a value receiver is usually the right choice" (Google Decisions §Receiver type).

**See also**: IM-11, IM-12

---

## IM-14: When in Doubt, Use a Pointer Receiver

**Strength**: CONSIDER

**Summary**: Correctness wins over optimization. If you cannot clearly justify a value receiver (small, no mutex, no buffer, immutable, no future growth), default to a pointer receiver. A pointer receiver also leaves room for the type to grow fields that can't be copied.

```go
// Good — Config may grow; start with pointer receivers
type Config struct {
    APIKey string
    Timeout time.Duration
}

func (c *Config) Validate() error { /* ... */ }
func (c *Config) String() string   { /* ... */ }

// Later someone adds a sync.Once — no API break because methods already use pointer
type Config struct {
    APIKey  string
    Timeout time.Duration

    once sync.Once  // OK: receivers were already *Config
    cli  *http.Client
}
```

**Rationale**: Once a type has shipped with value receivers, changing to pointer receivers is a breaking change for any caller that stored a value in a variable whose interface was satisfied by the value receiver. Starting with pointer receivers avoids that cliff. Google Decisions §Receiver type: "When in doubt, use a pointer receiver... pick pointers for large types or as future-proofing if you don't have a good sense of how the code will grow" (Google Decisions §Receiver type).

**Note**: Don't use pointer receivers for performance alone. The compiler can already pass values via pointers on the stack when profitable. Measure before optimizing.

**See also**: IM-11, IM-12

---

## IM-15: Method Sets — What's Callable on `T` vs `*T`

**Strength**: MUST (understand)

**Summary**: The method set of `T` contains only the methods declared with a value receiver. The method set of `*T` contains every method — both value- and pointer-receiver ones. This determines which interfaces each satisfies.

```go
type S struct{ data string }

func (s S) Read() string        { return s.data }  // value receiver
func (s *S) Write(str string)   { s.data = str }   // pointer receiver

// Method set of S:  {Read}
// Method set of *S: {Read, Write}

type Reader interface { Read() string }
type Writer interface { Write(string) }

var _ Reader = S{}     // OK: S has Read
var _ Reader = &S{}    // OK: *S has Read too
var _ Writer = &S{}    // OK: *S has Write
// var _ Writer = S{}  // COMPILE ERROR: S does not have Write

// Gotcha: map values are not addressable
sVals := map[int]S{1: {"a"}}
sVals[1].Read()         // OK: Read has a value receiver
// sVals[1].Write("x")  // COMPILE ERROR: cannot take address of map element
```

**Rationale**: Go's call-site conversion rules automatically let you call a pointer-receiver method `m()` on an addressable value `v` (it rewrites to `(&v).m()`), but a value like `sVals[1]`, a return value, or an interface's contents is *not* addressable, so the auto-addressing does not apply. Knowing this prevents both "why doesn't this type satisfy the interface?" and "why can't I call this method on a map element?" Uber §Receivers and Interfaces: "Methods with value receivers can be called on pointers as well as values. Methods with pointer receivers can only be called on pointers or addressable values... Similarly, an interface can be satisfied by a pointer, even if the method has a value receiver" (Uber Style Guide §Receivers and Interfaces; Effective Go §Pointers vs. Values).

**See also**: IM-11, IM-12

---

## IM-16: Verify Interface Compliance at Compile Time with `var _ I = (*T)(nil)`

**Strength**: SHOULD

**Summary**: When a type is expected to implement an interface as part of its contract, add a compile-time assertion: `var _ I = (*T)(nil)`. This fails to compile the moment the type stops satisfying the interface.

```go
// Good — compile-time proof that *Handler implements http.Handler
type Handler struct {
    log *zap.Logger
}

var _ http.Handler = (*Handler)(nil)

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    // ...
}

// Good — when methods are on the value type, assert against the zero value
type LogHandler struct{}

var _ http.Handler = LogHandler{}

func (h LogHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) { /* ... */ }

// Good — for a collection of related types implementing the same interface
var (
    _ Storage = (*MemoryStore)(nil)
    _ Storage = (*DiskStore)(nil)
    _ Storage = (*RemoteStore)(nil)
)

// Bad — no compile-time check; a renamed or removed method breaks callers silently
type Handler struct{}

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) { /* ... */ }
```

**Rationale**: Without the assertion, the only check that `*Handler` satisfies `http.Handler` happens at a call site (or at a `var h http.Handler = &Handler{}` binding). If no such site exists in the same package, a refactor that breaks the interface goes undetected until a downstream caller tries to compile. The assertion centralizes the check next to the type's declaration. The right-hand side uses the *zero value* of the asserted type — `nil` for pointer/slice/map types, `{}` for struct types. Uber §Verify Interface Compliance: "Verify interface compliance at compile time where appropriate. This includes: exported types required to implement specific interfaces, exported or unexported types that are part of a collection implementing the same interface, and other cases where violating an interface would break users... The statement `var _ http.Handler = (*Handler)(nil)` will fail to compile if `*Handler` ever stops matching the `http.Handler` interface" (Uber Style Guide §Verify Interface Compliance).

**When not to add it**: For a type whose interface satisfaction is obvious, local, and checked at a call site anyway, the assertion is noise.

---

## IM-17: `nil` Interfaces vs Interfaces Holding a `nil` Concrete Value

**Strength**: MUST (understand)

**Summary**: An interface is nil only when both its type word and its data word are nil. An interface holding a *typed* nil pointer is NOT nil, and `err != nil` will be true even though the underlying pointer is nil — this is the classic "returning a typed nil error" bug.

```go
// The classic bug
type MyError struct{ msg string }
func (e *MyError) Error() string { return e.msg }

func doWork() error {
    var e *MyError  // typed nil
    // ... nothing sets e ...
    return e  // returns error whose type is *MyError, data is nil
}

err := doWork()
if err != nil {
    // TRUE! err's type slot holds *MyError; only the data slot is nil.
    fmt.Println(err.Error())  // PANIC: nil pointer dereference
}

// Good — return a truly nil interface
func doWork() error {
    var e *MyError
    if somethingWrong {
        e = &MyError{msg: "bad"}
    }
    if e != nil {
        return e
    }
    return nil  // untyped nil; interface is fully nil
}

// Good — construct the concrete value only when you need to return it
func doWork() error {
    if somethingWrong {
        return &MyError{msg: "bad"}
    }
    return nil
}
```

**Rationale**: An interface value is two words (type descriptor, data pointer). `iface == nil` compares both. `return someTypedNilPointer` fills the type word even when the data word is zero, so the resulting interface is non-nil — the caller's `if err != nil` check then passes, and any subsequent method call on the typed-nil dereferences a nil pointer and panics. The idiomatic fix is mechanical: when the return type is an interface, return the untyped `nil` literal, never a zero-valued typed variable. Branch on the concrete value and `return nil` when there is no error. Uber §Pointers to Interfaces describes the two-word model; this gotcha is a direct consequence of it. See also Effective Go and the Go FAQ ("Why is my nil error value not equal to nil?"). (Uber Style Guide §Pointers to Interfaces; Go FAQ §Why is my nil error value not equal to nil?; also corroborated by `cc-skills-golang/skills/golang-safety/references/nil-safety.md` + `skills/golang-troubleshooting/references/common-go-bugs.md` and `claude-skills/references/gotchas.md`).

**See also**: IM-10, IM-28

---

## IM-18: Use `any`, Not `interface{}`; Avoid Both at API Boundaries When You Can

**Strength**: SHOULD

**Summary**: Since Go 1.18, `any` is the built-in alias for `interface{}`. Prefer `any`. And prefer a concrete type or small interface over `any` at public boundaries — `any` erases all type information and forces callers (and readers) to reason about what's inside.

```go
// Good — use any for truly generic containers
func log(format string, args ...any) { /* ... */ }

// Good — generics for homogeneous "any type but one type per call"
func Map[T, U any](xs []T, f func(T) U) []U { /* ... */ }

// Bad — any as a cop-out at a real boundary
func Process(input any) (any, error) { /* ... */ }
// callers must know the expected shape with no help from the signature

// Good — the actual contract
func Process(req *Request) (*Response, error) { /* ... */ }
```

**Rationale**: `any` at an API boundary is usually a smell: it means the function either (1) accepts too many things and will need runtime type switching, or (2) has not yet been designed. Before accepting `any`, consider whether a small interface captures what you actually need (`fmt.Stringer`? `io.Reader`?) or whether the real parameter list should just be a generic type parameter. Google Decisions §Use any: "`interface{}` [is] equivalent to and interchangeable with `any`... In general, use `any`." Google Decisions §Generics: "instead of relying on the `any` type and excessive type switching, consider generics" (Google Decisions §Use any; Google Decisions §Generics; see also IM-19, IM-20).

**See also**: IM-19, IM-20

---

## IM-19: Use Type Assertions with the Comma-Ok Form

**Strength**: MUST

**Summary**: When narrowing an interface to a concrete type, always use the two-return form `v, ok := x.(T)`. The single-return form `x.(T)` panics on mismatch.

```go
// Good
if s, ok := val.(fmt.Stringer); ok {
    fmt.Println(s.String())
} else {
    fmt.Printf("not a Stringer: %T\n", val)
}

// Good — when you want the type-assertion failure to be a typed error
val, ok := req.Body.(io.Closer)
if !ok {
    return fmt.Errorf("request body %T is not io.Closer", req.Body)
}
defer val.Close()

// Bad — panics if val is not a Stringer
s := val.(fmt.Stringer)
```

**Rationale**: Panics from type assertions are rarely what you want in library code — they cannot be distinguished from unrecoverable programmer errors and they cross goroutine boundaries. The comma-ok form turns the test into a normal branch. Uber §Handle Type Assertion Failures: "The single return value form of a type assertion will panic on an incorrect type. Therefore, always use the 'comma ok' idiom." See also CI-19 in chapter 01 (Uber Style Guide §Handle Type Assertion Failures).

**See also**: IM-20, chapter 01 CI-19

---

## IM-20: Use a Type Switch When Branching on Multiple Concrete Types

**Strength**: SHOULD

**Summary**: When you need to handle several concrete types behind an interface, prefer a `switch x := v.(type)` statement over a chain of comma-ok assertions. It reads naturally, binds a typed name in each branch, and ensures exhaustive visual coverage.

```go
// Good
func describe(v any) string {
    switch x := v.(type) {
    case nil:
        return "nil"
    case string:
        return fmt.Sprintf("string: %q", x)
    case int, int64:
        return fmt.Sprintf("integer: %v", x)
    case fmt.Stringer:
        return fmt.Sprintf("stringer: %s", x.String())
    default:
        return fmt.Sprintf("other: %T", x)
    }
}

// Bad — chained assertions, each re-testing the interface
func describe(v any) string {
    if s, ok := v.(string); ok {
        return fmt.Sprintf("string: %q", s)
    }
    if i, ok := v.(int); ok {
        return fmt.Sprintf("integer: %v", i)
    }
    if i, ok := v.(int64); ok {
        return fmt.Sprintf("integer: %v", i)
    }
    if st, ok := v.(fmt.Stringer); ok {
        return fmt.Sprintf("stringer: %s", st.String())
    }
    return fmt.Sprintf("other: %T", v)
}
```

**Rationale**: A type switch is evaluated once and dispatches in the compiler's preferred order. It also gives a meaningful typed name in each case (the identifier `x` is `string` in the string case, `fmt.Stringer` in the stringer case). For branching on concrete types, this is the direct tool. Effective Go §Type switch describes this pattern; it shows up throughout the standard library (Effective Go §Type switch; Google Decisions §Generics warns against "excessive type switching" — use generics if the switching gets out of hand).

**See also**: IM-19, IM-18

---

## IM-21: Prefer Compile-Time Interface Checks Over Runtime Type Assertions

**Strength**: SHOULD

**Summary**: If you know at compile time what a value is, do not prove it at runtime with a type assertion. Use the interface directly, accept the concrete type in the parameter, or use the compile-time assertion pattern (IM-16).

```go
// Good — the parameter type forces the caller to supply a Closer
func shutdown(c io.Closer) error { return c.Close() }

// Good — compile-time check that *Server is an io.Closer
var _ io.Closer = (*Server)(nil)

// Bad — runtime assertion where no polymorphism exists
func shutdown(s *Server) error {
    c, ok := any(s).(io.Closer)  // pointless: *Server is known at compile time
    if !ok {
        return errors.New("not closable")
    }
    return c.Close()
}

// Good — runtime assertion is warranted when the value genuinely may or may not
// satisfy an interface (optional behavior pattern)
func closeIfPossible(v any) {
    if c, ok := v.(io.Closer); ok {
        _ = c.Close()
    }
}
```

**Rationale**: Runtime assertions cost readability (a reader must check what types the branch covers) and sometimes performance (a small but real `itab` lookup). Use them for *optional* behavior ("if this value happens to be a Closer, also close it") — not to smuggle static types through an `any`. Google Best Practices §Avoid unnecessary interfaces and Google Decisions §Interfaces both warn against introducing polymorphism that doesn't exist (Google Best Practices §Avoid unnecessary interfaces; Google Decisions §Interfaces).

**See also**: IM-16, IM-19

---

## IM-22: Document Every Interface as If It Were a User Manual

**Strength**: SHOULD

**Summary**: An interface is a contract; a reader implementing it or consuming it needs to know the expected behavior, thread-safety, error conventions, and edge cases. Put that information in doc comments — on the interface, on each method for multi-method interfaces, and even on unexported interfaces.

```go
// Good
// Storer persists opaque blobs of data under string keys.
//
// Implementations must be safe for concurrent use by multiple goroutines.
// Get returns (nil, ErrNotFound) for missing keys.
// Put overwrites any existing value for the key.
type Storer interface {
    // Get returns the value stored under key, or ErrNotFound if no such key exists.
    // The returned slice must not be modified by the caller.
    Get(ctx context.Context, key string) ([]byte, error)

    // Put stores data under key, overwriting any previous value.
    // It returns an error only for transport or disk failures.
    Put(ctx context.Context, key string, data []byte) error
}

// Bad — no documentation on an interface's contract
type Storer interface {
    Get(ctx context.Context, key string) ([]byte, error)
    Put(ctx context.Context, key string, data []byte) error
}
```

**Rationale**: Interface doc is especially important because, unlike a concrete type, an IDE cannot jump from the call site to an implementation's doc — it can only show the interface's doc. Google Best Practices §Designing effective interfaces: "Treat every interface as the 'user manual' for your abstraction... Whether an interface has ten methods or a single `Write` of `io.Writer`, if a programmer is expected to interact with that type, the API must be documented thoroughly... Unexported interfaces: consider documenting them anyway. They are often the glue that holds complex internal logic together" (Google Best Practices §Designing effective interfaces).

**See also**: IM-03, chapter 01 CI-42

---

## IM-23: Receiver Names Are Short Abbreviations of the Type — Never `this` or `self`

**Strength**: SHOULD

**Summary**: Use one or two letters derived from the type name. Use the same receiver across every method on the type. Never `this`, `self`, `me`, or the whole type name.

```go
// Good
type ResearchInfo struct{ /* ... */ }

func (ri *ResearchInfo) Title() string   { /* ... */ }
func (ri *ResearchInfo) Summary() string { /* ... */ }
func (ri *ResearchInfo) Update() error   { /* ... */ }

// Good — single letter for short type names
type Tray struct{}

func (t Tray) Load() { /* ... */ }

// Bad
func (this *ReportWriter) Write(p []byte) (int, error) { /* ... */ }
func (self *Scanner) Scan() bool                        { /* ... */ }
func (reportWriter *ReportWriter) Flush() error         { /* ... */ }
func (tray Tray) Load()                                 { /* ... */ }  // prefer `t Tray`
```

**Rationale**: Receivers appear on every method; keeping them short and consistent reduces visual noise and lets readers navigate a type's methods without context-switching. `this`/`self` are not Go — they are a trap imported from other languages. When a receiver is unused, omit the name entirely. Google Decisions §Receiver names: "Receiver variable names must be short (usually one or two letters in length), abbreviations for the type itself, applied consistently to every receiver for that type, not an underscore; omit the name if it is unused." Uber §Guidelines agrees (Google Decisions §Receiver names; Uber Style Guide §Guidelines).

**See also**: chapter 01 CI-09

---

## IM-24: No `Get` Prefix on Methods; Verb-Like Names for Action Methods

**Strength**: SHOULD-AVOID

**Summary**: A method that returns a value is named after the noun it returns: `Name()`, `Size()`, `Count()`. Methods that *do* something take verb-like names: `Write`, `Connect`, `Close`. Use `Get` only when the underlying concept is literally "get" (e.g., HTTP GET).

```go
// Good
type Config struct{ /* ... */ }

func (c *Config) JobName(key string) (value string, ok bool) { /* ... */ }
func (c *Config) WriteDetail(w io.Writer) (int64, error)     { /* ... */ }

// Good — the type name itself communicates "get"
func (c *HTTPClient) Get(url string) (*Response, error) { /* ... */ }

// Bad
func (c *Config) GetJobName(key string) (string, bool)       { /* ... */ }
func (c *Config) GetWriteDetail(w io.Writer) (int64, error)  { /* ... */ }
```

**Rationale**: A method returning a value is self-evidently a getter from its signature; the `Get` prefix is JavaBean-style noise. For methods that compute expensively or block, use a word like `Compute`, `Fetch`, or `Load` to signal that. Google Decisions §Getters: "Function and method names should not use a `Get` or `get` prefix, unless the underlying concept uses the word 'get'... Prefer starting the name with the noun directly, for example use `Counts` over `GetCounts`." Google Best Practices §Naming conventions distinguishes noun-like names (returning something) from verb-like names (doing something) (Google Decisions §Getters; Google Best Practices §Naming conventions; Effective Go §Getters).

**See also**: chapter 01 CI-10

---

## IM-25: Implement `fmt.Stringer` for Types with a Natural Human Form

**Strength**: CONSIDER

**Summary**: Implement `String() string` when a type has a clear textual representation that callers would want from `%v`, `%s`, or `fmt.Println`. Beware of infinite recursion when the implementation itself uses `%v` on the receiver.

```go
// Good — natural string form of an enum
type Status int

const (
    StatusUnknown Status = iota
    StatusActive
    StatusPaused
    StatusStopped
)

func (s Status) String() string {
    switch s {
    case StatusActive:
        return "active"
    case StatusPaused:
        return "paused"
    case StatusStopped:
        return "stopped"
    default:
        return "unknown"
    }
}

// Good — Stringer on a struct
type Point struct{ X, Y int }

func (p Point) String() string {
    return fmt.Sprintf("(%d,%d)", p.X, p.Y)
}

// Bad — infinite recursion: %v of Point calls String, which calls %v of Point, ...
func (p Point) String() string {
    return fmt.Sprintf("%v", p)
}

// Bad — breaks with a typed alias
type MyPoint Point
func (m MyPoint) String() string {
    return fmt.Sprintf("%v", m)  // also recurses
}

// Good — use the underlying representation explicitly
type Point struct{ X, Y int }
func (p Point) String() string {
    return fmt.Sprintf("(%d,%d)", p.X, p.Y)  // formats fields, not p itself
}
```

**Rationale**: `fmt` inspects the `Stringer` interface when formatting with `%v`, `%s`, or via `Println`. Implementing it lets logs, error messages, and debug output render the type correctly. The recursion trap is real: if `String()` uses `%v` on the full receiver, `fmt` calls `String()` again. Format fields individually, or convert to the underlying type: `fmt.Sprintf("(%d,%d)", p.X, p.Y)`. Effective Go §Printing describes the `Stringer` hookup. See also Go FAQ on `%v` recursion (Effective Go §Printing).

**See also**: IM-23, IM-27

---

## IM-26: Implement `error` with a Pointer Receiver on `*FooError`

**Strength**: SHOULD

**Summary**: Custom error types conventionally implement `Error() string` on a pointer receiver, and are named with the suffix `Error`. Callers use `errors.As(err, &target)` to extract them. Return them by pointer.

```go
// Good
type NotFoundError struct {
    File string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("file %q not found", e.File)
}

func Open(file string) error {
    return &NotFoundError{File: file}
}

// caller
var nf *NotFoundError
if errors.As(err, &nf) {
    fmt.Println("missing:", nf.File)
}

// Bad — value receiver makes errors.As awkward and loses identity on comparison
type NotFoundError struct{ File string }
func (e NotFoundError) Error() string { /* ... */ }

// Bad — name without Error suffix doesn't signal "this is an error type"
type FileMissing struct{ File string }
```

**Rationale**: Error values are typically returned and compared many times on the path up the stack. A pointer receiver means every `errors.As` target is a `*FooError`, and two different constructions of the same error have distinct identities if that matters. Uber §Error Naming: "For custom error types, use the suffix `Error`." Uber §Error Types demonstrates the `*NotFoundError` pattern and `errors.As` usage (Uber Style Guide §Error Types; Uber Style Guide §Error Naming).

**Note**: Detailed error-handling patterns — wrapping, sentinels, `errors.Is`/`errors.As` — are covered in chapter 03. This entry covers only the method/interface mechanics.

**See also**: IM-11, chapter 03

---

## IM-27: Implement Marshaler and Unmarshaler in Pairs; Match Pointer-Receiver Discipline

**Strength**: SHOULD

**Summary**: When a type implements `MarshalJSON`, it should usually also implement `UnmarshalJSON` (and similarly for text, binary, YAML, protobuf). The unmarshaler must use a pointer receiver because it mutates. Keeping both on the same receiver kind is clearest.

```go
// Good — symmetric pair, pointer receivers on both
type Hex []byte

func (h Hex) MarshalText() ([]byte, error) {
    out := make([]byte, hex.EncodedLen(len(h)))
    hex.Encode(out, h)
    return out, nil
}

func (h *Hex) UnmarshalText(text []byte) error {
    buf := make([]byte, hex.DecodedLen(len(text)))
    if _, err := hex.Decode(buf, text); err != nil {
        return fmt.Errorf("decode hex: %w", err)
    }
    *h = buf
    return nil
}

// Bad — Unmarshaler with a value receiver never writes the result back
func (h Hex) UnmarshalText(text []byte) error {
    // ... decodes, but the caller never sees the result
    h = decoded  // assignment to the local copy; lost when the method returns
    return nil
}

// Bad — MarshalJSON without UnmarshalJSON means a JSON round-trip loses information
type Money struct{ amount, scale int }

func (m Money) MarshalJSON() ([]byte, error) { /* writes "12.34" */ }
// no UnmarshalJSON — encoding/json will populate fields positionally, incorrectly
```

**Rationale**: Un-paired marshalers silently fail round-trips. Forgetting the pointer receiver on the unmarshaler is a common bug: the method appears to work (returns nil) but nothing is written. Type-name suffix rules apply: `Marshal` is the primary form, `MarshalText`/`MarshalJSON`/`MarshalBinary` disambiguate the encoding. Google Best Practices §Naming conventions: "If there is a clear 'primary' version, the type can be omitted from the name for that version: `func (c *Config) Marshal() ([]byte, error)`, `func (c *Config) MarshalText() (string, error)`" (Google Best Practices §Naming conventions; standard library `encoding` contracts).

**See also**: IM-11

---

## IM-28: Avoid In-Band Error Signals from Methods — Return `(value, ok)` or `(value, error)`

**Strength**: SHOULD

**Summary**: Do not signal failure by returning a magic value (`-1`, `""`, `nil`) from a method. Return an extra `bool` (comma-ok) or `error`.

```go
// Good — comma-ok for an informational miss
func (c *Config) JobName(key string) (value string, ok bool) {
    v, ok := c.m[key]
    return v, ok
}

// Good — error for a failure that can have a reason
func (c *Cache) Get(ctx context.Context, key string) ([]byte, error) {
    // ...
    if !found {
        return nil, ErrNotFound
    }
    return data, nil
}

// Bad — -1 is magic; callers must remember to check
func (c *Cache) Get(key string) int {
    v, ok := c.m[key]
    if !ok {
        return -1
    }
    return v
}

// Bad — empty string as "missing"; hides the case where the stored value is actually ""
func (c *Config) JobName(key string) string {
    return c.m[key]
}
```

**Rationale**: In-band errors are easy to forget to check; worse, `Parse(Lookup(missingKey))` silently propagates the sentinel into an unrelated failure mode. Returning an extra value forces the caller to bind both — if they forget, the compiler complains. Google Decisions §In-band errors: "A function should return an additional value to indicate whether its other return values are valid. This return value may be an error or a boolean when no explanation is needed, and should be the final return value... Go code in the Google codebase should return additional values for errors" (Google Decisions §In-band errors).

**See also**: IM-19, chapter 01 CI-19

---

## IM-29: Embed Structs and Interfaces Only for Tangible Benefit — Not for "Inheritance"

**Strength**: SHOULD-AVOID

**Summary**: Struct embedding promotes the embedded type's fields and methods onto the outer type. Use it only when those methods genuinely belong on the outer type — not as a shortcut for code reuse. Never embed in *public* structs unless you are committed to the embedded type's API forever.

```go
// Good — targeted embedding with a clear wrapper purpose
type countingWriteCloser struct {
    io.WriteCloser
    count int
}

func (w *countingWriteCloser) Write(bs []byte) (int, error) {
    w.count += len(bs)
    return w.WriteCloser.Write(bs)
}

// Good — embedding preserves a useful zero value
type Book struct {
    bytes.Buffer  // zero-valued Buffer is usable
    // other fields
}

// Bad — embedding just to "inherit" methods leaks the embedded API
type ConcreteList struct {
    *AbstractList  // Add, Remove are now part of ConcreteList's public API forever
}

// Better — delegate explicitly
type ConcreteList struct {
    list *AbstractList
}
func (l *ConcreteList) Add(e Entity)    { l.list.Add(e) }
func (l *ConcreteList) Remove(e Entity) { l.list.Remove(e) }

// Bad — embedding a type whose zero value is nil produces a trap
type Book struct {
    io.ReadWriter  // interface zero value is nil
    // other fields
}

var b Book
b.Read(nil)  // panic: nil pointer
```

**Rationale**: Embedding is a *convenience* that trades away API evolution flexibility. Once a public struct embeds a type, every exported method and field on the embedded type becomes part of the outer type's API: removing the embedded type, replacing it, or even bumping the embedded type's API is a breaking change. Embedding an interface is even more fragile — adding a method to the interface breaks every struct that embeds it. Uber §Avoid Embedding Types in Public Structs: "These embedded types leak implementation details, inhibit type evolution, and obscure documentation... Adding methods to an embedded interface is a breaking change. Removing methods from an embedded struct is a breaking change. Removing the embedded type is a breaking change. Replacing the embedded type, even with an alternative that satisfies the same interface, is a breaking change." Uber §Embedding in Structs lists the full set of things embedding should not do (purely cosmetic, affect zero values, expose unrelated methods, etc.) (Uber Style Guide §Embedding in Structs; Uber Style Guide §Avoid Embedding Types in Public Structs).

**See also**: IM-05, IM-30, chapter 04

---

## IM-30: Don't Embed `sync.Mutex` — Make It a Named, Unexported Field

**Strength**: MUST-AVOID

**Summary**: Embedding `sync.Mutex` (or `sync.RWMutex`) accidentally makes `Lock`/`Unlock` part of the surrounding type's public API. Callers outside the package can then lock your internal mutex. Make the mutex a named, unexported field.

```go
// Good
type SMap struct {
    mu sync.Mutex

    data map[string]string
}

func (m *SMap) Get(k string) string {
    m.mu.Lock()
    defer m.mu.Unlock()
    return m.data[k]
}

// Bad — Lock/Unlock become part of SMap's exported API
type SMap struct {
    sync.Mutex

    data map[string]string
}

// external caller
var s SMap
s.Lock()  // should not be possible!
```

**Rationale**: Mutex methods are an implementation detail of the type that owns the mutex. Exposing them lets outside callers deadlock the type, hold the lock indefinitely, or introduce subtle concurrency bugs. A named, unexported field keeps the lock private. Uber §Zero-value Mutexes are Valid: "The zero-value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex. If you use a struct by pointer, then the mutex should be a non-pointer field on it. Do not embed the mutex on the struct, even if the struct is not exported... The mutex and its methods are implementation details of `SMap` hidden from its callers." Uber §Embedding in Structs lists mutexes as an explicit exception to any embedding rule (Uber Style Guide §Zero-value Mutexes are Valid; Uber Style Guide §Embedding in Structs).

**See also**: IM-29

---

## IM-31: Prefer Generics Over `any` + Type Switches for Homogeneous Polymorphism

**Strength**: CONSIDER

**Summary**: When the same logic applies to "any type from this set" and the set is small or natural, use a type parameter instead of `any` with runtime type switching. When only one implementation exists in practice, don't introduce a type parameter at all — just write it for that type.

```go
// Good — a single generic function over any numeric slice
func Sum[T ~int | ~int64 | ~float64](xs []T) T {
    var s T
    for _, x := range xs {
        s += x
    }
    return s
}

// Bad — any + type switch implements the same thing slower and unsafely
func Sum(xs any) any {
    switch v := xs.(type) {
    case []int:
        var s int
        for _, x := range v { s += x }
        return s
    case []int64:
        // ...
    case []float64:
        // ...
    default:
        panic("unsupported")
    }
}

// Good — if only int is needed, start concrete
func Sum(xs []int) int {
    var s int
    for _, x := range xs { s += x }
    return s
}
```

**Rationale**: Generics give compile-time type safety and eliminate the runtime type-switch branching that `any`-based code needs. But they also add abstraction cost — if only one concrete type is used in practice, the generic version is harder to read. Google Decisions §Generics: "Do not use generics just because you are implementing an algorithm or data structure that does not care about the type of its member elements. If there is only one type being instantiated in practice, start by making your code work on that type without using generics at all. Adding polymorphism later will be straightforward compared to removing abstraction... Otherwise, instead of relying on the `any` type and excessive type switching, consider generics." Also: "If you have several types that share a useful unifying interface, consider modeling the solution using that interface. Generics may not be needed" (Google Decisions §Generics).

**See also**: IM-18, IM-20, chapter 04

---

## IM-32: Don't Build Test-Only Interfaces When the Real API Is Testable

**Strength**: SHOULD-AVOID

**Summary**: Do not wrap a concrete type in a manual interface solely so that tests can mock it. Prefer testing against the real implementation (including real transports for RPC clients). Introduce an interface only when production code has a reason for one.

```go
// Bad — an interface invented for testing, with one production implementation
type userStore interface {
    Get(id string) (*User, error)
    Put(u *User) error
}

type realUserStore struct{ db *sql.DB }
func (s *realUserStore) Get(id string) (*User, error) { /* ... */ }
func (s *realUserStore) Put(u *User) error            { /* ... */ }

type fakeUserStore struct{ users map[string]*User }
func (f *fakeUserStore) Get(id string) (*User, error) { /* ... */ }
func (f *fakeUserStore) Put(u *User) error            { /* ... */ }

// Good — test the concrete type against a real (in-process) backend
func TestService(t *testing.T) {
    db := sqltest.Open(t)  // real sqlite or test container
    svc := NewService(NewUserStore(db))
    // exercise the real code path
}

// Good — if substitution is genuinely needed, let the consumer define the interface
package report

type userLookup interface {
    User(id string) (*User, error)  // only the method report uses
}

func Generate(ctx context.Context, lookup userLookup) error { /* ... */ }
```

**Rationale**: Test-only interfaces double the API surface, drag the reader through three entities (interface, real type, fake), and often make production code harder to navigate. They also encourage *mocking* behavior that diverges from reality. Google Decisions §Interfaces: "Do not wrap RPC clients in new manual interfaces just for the sake of abstraction or testing... Do not define back doors or export test double implementations of an interface solely for testing. Prefer testing via the public API of the real implementation instead." Google Best Practices §Avoid unnecessary interfaces: "Every exported type increases the cognitive load for the reader. When you export a test double alongside the real implementation, you force the reader to understand three entities (the interface, the real implementation, and the test double) instead of one" (Google Decisions §Interfaces; Google Best Practices §Avoid unnecessary interfaces; Google Best Practices §Use real transports).

**See also**: IM-02, IM-06

---

## IM-33: Method Values and Method Expressions — When Each Is Warranted

**Strength**: CONSIDER

**Summary**: `obj.Method` is a *method value*: a bound function with the receiver captured. `Type.Method` (or `(*Type).Method`) is a *method expression*: an unbound function that takes the receiver as its first argument. Use method values when you need a callback that remembers a specific receiver; use method expressions rarely, and only when the receiver varies per call.

```go
// Good — method value as a callback; server is captured
func (s *Server) Handle() { /* ... */ }

srv := &Server{}
registerCallback(srv.Handle)  // callback always targets srv

// Good — method value for deferred cleanup
f, err := os.Open(path)
if err != nil { return err }
defer f.Close           // method value; f captured; no need for a closure
// Note: `defer f.Close` and `defer f.Close()` behave the same here.

// Good — method expression when applying the same method to varying receivers
func stringifyAll(pts []Point) []string {
    toStr := Point.String  // method expression: func(Point) string
    out := make([]string, len(pts))
    for i, p := range pts {
        out[i] = toStr(p)
    }
    return out
}

// Usually unnecessary
sort.Slice(users, func(i, j int) bool {
    return (*User).less(&users[i], &users[j])  // method expression
})
// Clearer:
sort.Slice(users, func(i, j int) bool {
    return users[i].less(&users[j])
})
```

**Rationale**: Method values let you treat a method like a first-class function without writing a closure. Method expressions are rarely the clearest option — a short closure or direct call is usually more readable. Reserve method expressions for the uncommon case where you genuinely want a callable that accepts the receiver as a parameter. Effective Go does not formalize these patterns; the Go spec defines them, and idiomatic Go leans heavily on method values via `defer obj.Close` and similar (Go Spec §Method values and §Method expressions).

---

## IM-34: Segregated Role Interfaces over a Fat CRUD Interface

**Strength**: SHOULD

**Summary**: Rather than declaring one `Repository` interface with every CRUD/search/count method, declare a single-method role interface per operation (`Creator`, `Reader`, `Updater`, `Deleter`, `Lister`) and compose only the ones a given consumer actually needs (`ReadWriter`, `FullRepository`). This is the concrete, copy-pasteable realization of "keep interfaces small" in the repository-layer context that Go codebases routinely need.

```go
// Bad: Fat interface
type BadRepository interface {
    Create(item Item) error
    Read(id string) (Item, error)
    Update(item Item) error
    Delete(id string) error
    List() ([]Item, error)
    Search(query string) ([]Item, error)
    Count() (int, error)
}

// Good: Segregated interfaces
type Creator interface {
    Create(item Item) error
}

type Reader interface {
    Read(id string) (Item, error)
}

type Updater interface {
    Update(item Item) error
}

type Deleter interface {
    Delete(id string) error
}

type Lister interface {
    List() ([]Item, error)
}

// Compose only what you need
type ReadWriter interface {
    Reader
    Creator
}

type FullRepository interface {
    Creator
    Reader
    Updater
    Deleter
    Lister
}
```

**Rationale**: A consumer that only needs to read should depend on `Reader`, not on a seven-method `BadRepository` whose `Update`, `Delete`, `Search`, and `Count` it never uses. Segregated interfaces make mocks trivial (one method each), let callers compose the exact capability set they need, and avoid forcing every implementation to stub out methods that are irrelevant to it. This extends IM-03 (keep interfaces small) and IM-05 (compose by embedding) into a named pattern for the common CRUD case. Source: `jeffallan-claude-skills/skills/golang-pro/references/interfaces.md` (via `jeffallan-claude-skills/skills-accepted.md` §Interface Segregation).

**See also**: IM-03, IM-05, IM-02

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Accept interfaces, return concrete | SHOULD | Don't pre-choose the caller's subset |
| 02 | Interface lives with the consumer | SHOULD | Lists only what the consumer uses |
| 03 | Keep interfaces small | SHOULD | "The bigger the interface, the weaker the abstraction" |
| 04 | `-er` suffix for single-method interfaces | SHOULD | `Reader`, `Writer`, `Stringer`; no `I`/`Interface` |
| 05 | Compose by embedding smaller interfaces | SHOULD | `ReadWriter = Reader + Writer` |
| 06 | Don't create interfaces until needed | SHOULD-AVOID | Two implementations, cycles, or narrowing |
| 07 | Valid reasons to return an interface | CONSIDER | Encapsulation, factory, cycle-breaking |
| 08 | Keep internal interfaces unexported | SHOULD | Exporting is an API commitment |
| 09 | Export interfaces that are the product | CONSIDER | Protocols, plugins, generated RPC |
| 10 | Never pass `*Interface` | MUST-AVOID | The interface value is already a handle |
| 11 | Pointer receivers for mutation / uncopyables | MUST | Or the mutation is lost |
| 12 | Consistent receiver kind per type | SHOULD | One method set, not two |
| 13 | Value receivers for small/reference types | SHOULD | Maps, chans, funcs, slices w/o reslice |
| 14 | When in doubt, pointer receiver | CONSIDER | Leaves room to grow uncopyable fields |
| 15 | Understand `T` vs `*T` method sets | MUST | `*T` has both; `T` has only value-receiver |
| 16 | `var _ I = (*T)(nil)` compile-time check | SHOULD | Fails fast when interface drifts |
| 17 | `nil` interface vs typed nil inside | MUST | Don't return a typed nil pointer as error |
| 18 | `any` over `interface{}`; avoid at boundaries | SHOULD | Prefer concrete types or generics |
| 19 | Comma-ok type assertions | MUST | Single-return form panics |
| 20 | Type switch for multi-type branching | SHOULD | Clearer than chained assertions |
| 21 | Compile-time over runtime interface checks | SHOULD | Runtime assertions are for optional behavior |
| 22 | Document every interface as a user manual | SHOULD | Including unexported ones |
| 23 | Receiver names: short, consistent, no `this`/`self` | SHOULD | One or two letters derived from type |
| 24 | No `Get` prefix on methods | SHOULD-AVOID | `Name()`, not `GetName()` |
| 25 | Implement `Stringer` carefully; no `%v` on self | CONSIDER | Avoid infinite recursion |
| 26 | `*FooError` with pointer receiver | SHOULD | Suffix `Error`, `errors.As` with `*T` target |
| 27 | Pair Marshal/Unmarshal; unmarshaler on pointer | SHOULD | Un-paired marshalers break round-trips |
| 28 | No in-band errors; return `(v, ok)` or `(v, error)` | SHOULD | Callers can't forget to check |
| 29 | Embed only for tangible benefit | SHOULD-AVOID | Never embed in public structs casually |
| 30 | Don't embed `sync.Mutex` | MUST-AVOID | Leaks Lock/Unlock into public API |
| 31 | Generics over `any` + type switch | CONSIDER | Type-safe and faster; skip if one type |
| 32 | Avoid test-only interfaces for production types | SHOULD-AVOID | Test the real implementation |
| 33 | Method values for callbacks; expressions rarely | CONSIDER | `defer f.Close`; `Type.Method` is uncommon |
| 34 | Segregated role interfaces | SHOULD | Per-op `Creator`/`Reader` compose |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for receiver-name basics (CI-09), no-Get (CI-10), comma-ok (CI-19), and `any` vs `interface{}` (CI-25) — this chapter extends all of those.
- **API Design**: See `02-api-design.md` for constructor patterns and the top-level decision of when to return a concrete type vs an interface at a package boundary (extends IM-01, IM-07).
- **Error Handling**: See `03-error-handling.md` for error wrapping, sentinels, `errors.Is`/`errors.As`, and full custom error-type patterns (extends IM-26).
- **Type Design**: See `04-type-design.md` for struct embedding beyond the interface context, type aliases, and generics design (extends IM-29, IM-31).
- **Concurrency**: See `06-concurrency.md` for goroutine-safe interface design, `context.Context` placement on interface methods, and mutex-holding types (extends IM-30).
- **Testing**: See `07-testing.md` for testing strategies that avoid over-interfacing (extends IM-32).
- **Anti-Patterns**: See `09-anti-patterns.md` for the common over-abstraction smells that amplify IM-06, IM-10, IM-29, IM-32.

---

## External References

- [*Effective Go* — Interfaces](https://go.dev/doc/effective_go#interfaces) — the foundational Go interface discussion
- [*Effective Go* — Pointers vs. Values](https://go.dev/doc/effective_go#pointers_vs_values) — receiver-choice guidance
- [*Effective Go* — Embedding](https://go.dev/doc/effective_go#embedding) — struct and interface embedding
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — §Pointers to Interfaces, §Verify Interface Compliance, §Receivers and Interfaces, §Zero-value Mutexes, §Embedding in Structs, §Avoid Embedding Types in Public Structs
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions §Interfaces, §Receiver names, §Receiver type, §Pass values, §Generics, §In-band errors; Best Practices §Interfaces
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — the Go team's canonical review checklist
- [Go Proverbs](https://go-proverbs.github.io/) — "The bigger the interface, the weaker the abstraction"; "Accept interfaces, return structs"
- [GoTip #49: Accept Interfaces, Return Concrete Types](https://google.github.io/styleguide/go/index.html#gotip)
- [GoTip #78: Minimal Viable Interfaces](https://google.github.io/styleguide/go/index.html#gotip)
- [Go FAQ — Why is my nil error value not equal to nil?](https://go.dev/doc/faq#nil_error) — the classic typed-nil gotcha
- [`go vet`](https://pkg.go.dev/cmd/vet), [`staticcheck`](https://staticcheck.dev/) — catch unused receivers, missing `Error()` methods, and common interface-related bugs
