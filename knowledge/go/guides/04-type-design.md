# Type Design

Patterns for designing Go types — structs, defined types, enums, and generic type parameters — so they are safe to copy, easy to evolve, and survive refactors. These patterns are grounded in authoritative sources: the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and *Effective Go*.

Target environment: **Go 1.22+**, **standard library first**, **`gofmt` + `go vet` + `staticcheck`** for formatting and linting. Generics (Go 1.18+) and `cmp.Ordered` (Go 1.21+) are assumed available.

Scope: type-shape decisions only. Interface-satisfaction mechanics and method-set rules live in `05-interfaces-methods.md`. Error-type design (sentinels, wrapping, `errors.Is`/`errors.As`) lives in `03-error-handling.md`. Synchronization primitives and their use live in `06-concurrency.md`; this chapter covers only the type-design constraints they impose (e.g., "don't copy a `sync.Mutex`").

---

## TD-01: Design Types So the Zero Value Is Useful

**Strength**: SHOULD

**Summary**: When designing a struct, arrange fields so that `var x T` is immediately usable without a constructor. If a type cannot have a useful zero, say so explicitly in its doc comment and force construction through a `New...` function.

```go
// Good — sync.Mutex, bytes.Buffer, strings.Builder, time.Time all work at zero.
var mu sync.Mutex
mu.Lock()

var buf bytes.Buffer
buf.WriteString("hello")

type Config struct {
    MaxConns int           // 0 means "use default"
    Timeout  time.Duration // 0 means "no timeout"
    Logger   *slog.Logger  // nil means "discard"
}
var cfg Config // immediately usable

// Bad — requires a constructor just to avoid nil-panics.
type Buffer struct {
    data []byte
}
func (b *Buffer) Write(p []byte) { b.data = append(b.data, p...) } // only safe if data was initialized

// Bad — unexported map that must be made by a constructor the caller must remember.
type Counter struct{ m map[string]int }
func (c *Counter) Inc(k string) { c.m[k]++ } // panic on var Counter{}
```

**Rationale**: A usable zero value removes an entire class of initialization bugs and makes the type cheaper to embed, declare at package scope, or construct inside composite literals. Google Decisions §Zero-value fields: "When possible, APIs should be designed so that the zero value of the struct is immediately useful." Google Best Practices §Declaring variables: prefer `var x T` when zero is the start state. Uber §Use Zero-value `sync.Mutex` is the canonical worked example: no `NewMutex` needed because the Go team designed the zero value to work (Google Decisions §Zero-value fields; Uber Style Guide §Zero-value Mutexes; Effective Go §The zero value).

**See also**: TD-17, TD-34, CI-11

---

## TD-02: Prefer Embedding Values Over Embedding Pointers

**Strength**: SHOULD

**Summary**: When you embed a type to promote its methods, embed by value unless you specifically need the shared-state semantics of a pointer. Value embedding keeps the zero value useful and avoids nil-dereference panics.

```go
// Good
type Server struct {
    log.Logger // value embedding — zero Logger is usable
}
var s Server
s.Print("starting") // works with zero value

// Acceptable — pointer embedding when nil must be meaningful (e.g., optional component).
type Client struct {
    *http.Client // nil means "use default transport"; caller must handle
}

// Bad — pointer embedding that destroys the useful zero value for no reason.
type Handler struct {
    *log.Logger // nil Logger panics on Print
}
var h Handler
h.Print("x") // panic
```

**Rationale**: Embedding a pointer means the outer type's zero value contains a nil inner pointer — every method call on the promoted field can panic. Embedding a value preserves TD-01 and makes copying the outer struct meaningful. Uber §Embedding in Structs explicitly recommends value embedding. Only reach for pointer embedding when sharing state is the point (Uber Style Guide §Embedding in Structs).

**See also**: TD-01, TD-03, TD-08

---

## TD-03: Avoid Embedding Types in Exported Structs

**Strength**: SHOULD-AVOID

**Summary**: Embedding a type in an exported struct leaks every current and future method of the embedded type into your public API. Prefer a named field so the dependency is explicit and your API surface is under your control.

```go
// Good
type AbstractList struct {
    list List // named field — only the AbstractList methods you define are promoted
}
func (l *AbstractList) Add(v any)    { l.list.Add(v) }
func (l *AbstractList) Remove(v any) { l.list.Remove(v) }

// Bad — every future method added to List silently becomes part of AbstractList's API.
type AbstractList struct {
    List // embedded — promotes Add, Remove, and every method added later
}
```

**Rationale**: Embedding inside an exported struct is an irreversible API commitment. If the embedded type is in another package (or evolves independently), adding a method there adds a method to your type — users may come to depend on it, locking you in. It also breaks encapsulation (callers can reach past your abstraction with `x.List.InternalThing()`). Uber §Avoid Embedding Types in Public Structs gives this exact guidance (Uber Style Guide §Avoid Embedding Types in Public Structs).

**See also**: TD-02, TD-04

---

## TD-04: Put Embedded Fields at the Top of the Struct

**Strength**: SHOULD

**Summary**: When you do embed a type, list the embedded fields before any named fields. Separate them with a blank line for readability.

```go
// Good
type Client struct {
    http.Client
    log.Logger

    Endpoint string
    Timeout  time.Duration
}

// Bad
type Client struct {
    Endpoint string
    http.Client
    Timeout  time.Duration
    log.Logger
}
```

**Rationale**: Readers scan the top of a struct to understand its inheritance-like surface (what methods are promoted). Mixing embedded and named fields hides that surface and makes code review harder. Uber §Embedding in Structs establishes this layout convention (Uber Style Guide §Embedding in Structs).

**See also**: TD-02, TD-30

---

## TD-05: Don't Embed Types That Must Not Be Copied

**Strength**: MUST-AVOID

**Summary**: Do not embed `sync.Mutex`, `sync.RWMutex`, `sync.WaitGroup`, `sync.Cond`, `sync.Once`, `atomic.*`, `bytes.Buffer`, `strings.Builder`, or `noCopy`-marked types in exported structs. Keep them as unexported named fields instead.

```go
// Good
type Counter struct {
    mu sync.Mutex // unexported, cannot be reached by callers
    n  int
}
func (c *Counter) Inc() { c.mu.Lock(); defer c.mu.Unlock(); c.n++ }

// Bad — Lock/Unlock leak into the public API; the struct invites copying.
type Counter struct {
    sync.Mutex
    N int
}
```

**Rationale**: Embedding a mutex promotes `Lock`/`Unlock` onto the outer type, so callers can lock your internal state and your invariants are gone. Worse, these types must not be copied (they contain state that `go vet copylocks` tracks). If the outer struct is copied, the copy has a second, independent mutex protecting nothing. Uber §Zero-value Mutexes recommends unexported `mu` (Uber Style Guide §Zero-value Mutexes; `go vet` §copylocks).

**See also**: TD-02, TD-03, TD-08

---

## TD-06: Unexported Fields by Default; Export Only When the Caller Must Set Them

**Strength**: SHOULD

**Summary**: Default to unexported field names. Export a field only when callers are expected to read or write it directly through struct literals or method-free access (e.g., DTOs, plain config structs).

```go
// Good — internal invariants protected by unexported fields.
type Counter struct {
    mu sync.Mutex
    n  int
}
func (c *Counter) Value() int { c.mu.Lock(); defer c.mu.Unlock(); return c.n }

// Good — plain config type intended for struct-literal initialization.
type HTTPConfig struct {
    Addr         string
    ReadTimeout  time.Duration
    WriteTimeout time.Duration
}

// Bad — exports internal mutable state; any caller can break invariants.
type Counter struct {
    Mu sync.Mutex
    N  int
}
```

**Rationale**: An exported field is part of the API contract — renaming, removing, or changing its invariants is a breaking change. Start unexported; export deliberately when the caller's access is part of the design. Google Decisions §Getters and §Receiver type, plus Uber §Zero-value Mutexes, all assume unexported fields by default.

**See also**: TD-05, TD-18

---

## TD-07: Copy Slices and Maps at API Boundaries

**Strength**: SHOULD

**Summary**: When a method accepts a slice or map and stores it, or returns a slice or map backed by internal state, copy at the boundary. Slices and maps are references; sharing them creates spooky action at a distance.

```go
// Good — store a defensive copy.
type Trip struct {
    trips []Trip
}
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = make([]Trip, len(trips))
    copy(d.trips, trips)
}

// Good — return a copy so callers can't mutate internal state.
func (d *Driver) Trips() []Trip {
    out := make([]Trip, len(d.trips))
    copy(out, d.trips)
    return out
}

// Bad — caller can mutate the slice after handing it in.
func (d *Driver) SetTrips(trips []Trip) { d.trips = trips }
trips := []Trip{t1}
driver.SetTrips(trips)
trips[0] = t2 // silently mutates driver.trips[0]
```

**Rationale**: A slice header is `{ptr, len, cap}`; two headers can point to the same backing array. If you store a caller's slice as-is, the caller still has a reference and can mutate your state. Same for maps. Uber §Copy Slices and Maps at Boundaries documents both directions — receiving and returning (Uber Style Guide §Copy Slices and Maps at Boundaries).

**See also**: TD-17, CI-11

---

## TD-08: Uncopyable State Forces Pointer-Only Types

**Strength**: MUST

**Summary**: If a type contains a `sync.Mutex`, `sync.WaitGroup`, `atomic.Int64`, `bytes.Buffer`, or any other field that must not be copied, ensure all methods use pointer receivers and all APIs accept/return `*T`, not `T`. Document the constraint.

```go
// Good
type Counter struct {
    mu sync.Mutex
    n  int
}
// All methods use pointer receivers.
func (c *Counter) Inc()     { c.mu.Lock(); defer c.mu.Unlock(); c.n++ }
func (c *Counter) Value() int { c.mu.Lock(); defer c.mu.Unlock(); return c.n }

func NewCounter() *Counter { return &Counter{} } // return pointer

// Bad — value receiver copies the mutex on every call; each copy has its own lock.
func (c Counter) Inc() { c.mu.Lock(); defer c.mu.Unlock(); c.n++ }
```

**Rationale**: Copying a `sync.Mutex` produces two independent mutexes that protect nothing. `go vet`'s copylocks analyzer flags these copies, but the type's own design decides whether copies are possible at all. Google Decisions §Copying: "values of a type should not be copied if that could cause an issue." Uber §Zero-value Mutexes and §Copy Slices and Maps at Boundaries both orbit this invariant (Google Decisions §Copying; Uber Style Guide §Zero-value Mutexes).

**See also**: TD-05, TD-07, TD-09

---

## TD-09: Choose Pointer vs. Value Receivers Based on Type Shape

**Strength**: SHOULD

**Summary**: As a type-design choice, pick one receiver kind and apply it to all methods of the type. Use pointer receivers when the type contains uncopyable state, is large, or methods must mutate it. Use value receivers for small, immutable value types.

```go
// Good — large struct with mutation and uncopyable field: pointer receivers.
type Server struct {
    mu       sync.Mutex
    handlers map[string]Handler
}
func (s *Server) Handle(path string, h Handler) { /* mutates s */ }
func (s *Server) Lookup(path string) Handler    { /* reads s */ }

// Good — small immutable value type: value receivers.
type Point struct{ X, Y float64 }
func (p Point) Add(q Point) Point { return Point{p.X + q.X, p.Y + q.Y} }
func (p Point) String() string    { return fmt.Sprintf("(%g,%g)", p.X, p.Y) }

// Bad — mixing receiver kinds on the same type.
type Counter struct{ n int }
func (c *Counter) Inc()     { c.n++ }  // pointer
func (c Counter) Value() int { return c.n } // value — inconsistent
```

**Rationale**: The receiver choice is really a type-design decision, not a per-method one: it's a claim about what a value of the type *is* (an immutable snapshot vs. a handle to mutable state). Mixing kinds produces a method set that's confusing and forbids certain interface satisfactions. Google Decisions §Receiver type lists the factors (uncopyable fields, mutation, size, consistency) and is explicit that consistency across a type's methods matters more than per-method optimization (Google Decisions §Receiver type; Uber Style Guide §Receivers and Interfaces). Method-set rules for interface satisfaction are covered in `05-interfaces-methods.md`.

**See also**: TD-05, TD-08, TD-35

---

## TD-10: Define a New Type for Domain Identifiers and Bounded Strings

**Strength**: SHOULD

**Summary**: When a `string`, `int`, or `[]byte` has a specific domain meaning (user ID, order ID, SKU, postal code), define a named type for it. This prevents silent mix-ups at call sites and gives you a place to hang validation.

```go
// Good
type UserID string
type OrderID string
type ZIP string

func GetUser(id UserID) (*User, error) { /* ... */ }
func GetOrder(id OrderID) (*Order, error) { /* ... */ }

var u UserID = "u_123"
var o OrderID = "o_456"
GetUser(o) // compile error — can't pass OrderID where UserID is wanted

// Bad — strings everywhere, swap at the call site is a silent bug.
func GetUser(id string) (*User, error) { /* ... */ }
func GetOrder(id string) (*Order, error) { /* ... */ }
userID := "u_123"
orderID := "o_456"
GetUser(orderID) // compiles, wrong data
```

**Rationale**: Go's assignability is structural for untyped constants but nominal for named types, so `type UserID string` is a different type from `string` and from `OrderID`. The compiler catches argument swaps that a plain-string API would silently accept. Google Decisions §Constant names and Effective Go §New types both use this pattern. Note this is distinct from a type alias (see TD-11).

**See also**: TD-11, TD-20

---

## TD-11: Use a Defined Type for New Semantics; Use a Type Alias Only for Gradual Migration

**Strength**: MUST

**Summary**: `type A B` creates a new, distinct type with its own method set. `type A = B` creates an alias — a second name for the exact same type. Use defined types (`type A B`) for new semantics. Reserve aliases for renaming or relocating existing types across package boundaries.

```go
// Good — defined type: UserID is its own type, can have methods, compiler distinguishes it.
type UserID string
func (u UserID) Redacted() string { return "u_***" }

// Good — alias used during a package rename/move.
// Old package still compiles while callers migrate.
package old
type Client = new.Client // alias, identical type

// Bad — alias used where a new semantic type was intended.
type UserID = string // UserID is literally string; no type safety
func GetUser(id UserID) {} // same as GetUser(id string); swaps silently compile
```

**Rationale**: The two forms look similar but do different things: aliases are for *identity* (this is the same type under another name), defined types are for *distinction* (this is a new type with new semantics). Google Decisions §Type aliases: "type aliases are useful to help with refactors... Do not use type aliases when you intend to create a new type." Uber does not have aliases in its permitted style except for re-export compatibility (Google Decisions §Type aliases).

**See also**: TD-10, TD-13

---

## TD-12: Start `iota` Enums at One When Zero Would Be an Invalid State

**Strength**: SHOULD

**Summary**: When a zero value of the enum type would represent an invalid or unset state, start `iota` at 1 so that the zero value signals "unset." Use a `_` or explicit `Unknown` for zero if it has a meaningful distinct name.

```go
// Good — zero value signals "not set," useful for detecting uninitialized fields.
type Operation int
const (
    Add Operation = iota + 1
    Subtract
    Multiply
    Divide
)

// Good — explicit "Unknown" sentinel at zero.
type LogLevel int
const (
    LogLevelUnknown LogLevel = iota
    LogLevelDebug
    LogLevelInfo
    LogLevelWarn
    LogLevelError
)

// Bad — a zero Operation means "Add" silently, so missed initialization looks like Add.
type Operation int
const (
    Add Operation = iota
    Subtract
    Multiply
    Divide
)
```

**Rationale**: Without `+ 1` (or an explicit `Unknown`), the zero value silently aliases the first real case, so forgetting to set the field looks like "Add" (or whatever the first case is). Uber §Start Enums at One is explicit: "The standard way of introducing enumerations in Go is to declare a custom type and a const group with iota. ... In most cases, you want the default value to start at a reasonable value" (Uber Style Guide §Start Enums at One).

**See also**: TD-13, TD-33

---

## TD-13: Give Enums a `String()` Method

**Strength**: SHOULD

**Summary**: For any named integer enum, implement `fmt.Stringer` so that `%v` in logs and errors shows a readable name instead of a number. Prefer `go generate` with `golang.org/x/tools/cmd/stringer` for generated implementations.

```go
// Good — hand-written or stringer-generated.
type LogLevel int
const (
    LogLevelDebug LogLevel = iota
    LogLevelInfo
    LogLevelWarn
    LogLevelError
)

//go:generate stringer -type=LogLevel
func (l LogLevel) String() string {
    switch l {
    case LogLevelDebug: return "debug"
    case LogLevelInfo:  return "info"
    case LogLevelWarn:  return "warn"
    case LogLevelError: return "error"
    default:            return fmt.Sprintf("LogLevel(%d)", int(l))
    }
}

// Bad — logs show "level=2" and readers have to go look up what 2 means.
fmt.Printf("level=%v\n", LogLevelWarn)
```

**Rationale**: Integer enums are opaque in output. A `String()` method makes `fmt` and `log` render something humans can read without changing any call site. The `default` arm preserves debuggability when new constants are added but `String` isn't updated. Google Decisions §Constant names and Uber §Start Enums at One both assume this pairing.

**See also**: TD-12, TD-32

---

## TD-14: Prefer a Named Type Over a `bool` Parameter When Meaning Is Non-Obvious

**Strength**: SHOULD

**Summary**: `true`/`false` at a call site loses the parameter's meaning. If a boolean argument isn't self-explanatory, introduce a small enum type or use an options struct.

```go
// Good — call sites self-document.
type Mode int
const (
    ModeRead Mode = iota + 1
    ModeWrite
    ModeAppend
)
func Open(path string, m Mode) (*File, error) { /* ... */ }
Open("log.txt", ModeAppend)

// Bad — reader has to check the signature to know what 'true' means.
func Open(path string, append bool) (*File, error) { /* ... */ }
Open("log.txt", true)  // append? overwrite? truncate?
Open("log.txt", false) // ???

// Acceptable — inline comment on a naked literal when the call stays local.
Open("log.txt", true /* append */)
```

**Rationale**: Naked `true`/`false` at call sites is a common source of mistakes, especially when the signature is not on screen. A named type or options struct forces the caller to write the intent, and the compiler will catch confusion between two different bools. Uber §Avoid Naked Parameters and Google Decisions §Literal formatting both prescribe this pattern (Uber Style Guide §Avoid Naked Parameters; Google Decisions §Literal formatting).

**See also**: TD-10, TD-22

---

## TD-15: Return `error`, Not a Concrete `*MyError` Type

**Strength**: SHOULD

**Summary**: Public functions and methods should declare a return type of `error`, not `*MyError`. Returning a concrete pointer type turns `nil` comparisons into a minefield (a nil `*MyError` stored in an `error` is a non-nil interface).

```go
// Good
func Parse(b []byte) (*Node, error) { /* ... */ }

// Bad — caller may do `if err != nil` on the interface result but compare the concrete pointer.
func Parse(b []byte) (*Node, *ParseError) { /* ... */ }

// The classic bug this prevents:
func do() error {
    var e *MyError = nil
    return e // returns a non-nil error whose dynamic value is a nil *MyError
}
if do() != nil { /* triggers — bug */ }
```

**Rationale**: An interface value is nil only if both its type and value are nil. Returning a concrete pointer type invites callers (and the function itself) to return typed-nils that compare non-nil as `error`. Return `error`, construct with `&MyError{...}` or `fmt.Errorf`, and let callers use `errors.As` to recover the concrete type when needed. Full error-type design (sentinels, wrapping, custom error types) is covered in `03-error-handling.md`; this entry is only about the function-signature choice. Google Decisions §In-band errors and §Handle errors, Uber §Errors all agree on this signature.

**See also**: TD-16, TD-35

---

## TD-16: Use Multiple Return Values, Not In-Band Sentinels

**Strength**: MUST

**Summary**: When a function can fail or return "no result," return an extra `error` or `bool`, not a sentinel value within the primary return. This forces the caller to check explicitly and keeps the success value unambiguous.

```go
// Good
func Lookup(key string) (string, bool) { /* ... */ }
v, ok := Lookup("k")
if !ok { /* handle */ }

func Parse(b []byte) (int, error) { /* ... */ }
n, err := Parse(b)
if err != nil { /* handle */ }

// Bad — caller may forget to check for -1 / "" / nil-but-valid.
func Lookup(key string) string {
    if _, ok := m[key]; !ok { return "" } // is "" a real value or "not found"?
    return m[key]
}
func Parse(b []byte) int {
    if !valid(b) { return -1 } // is -1 a real parse result?
    return real(b)
}
```

**Rationale**: Sentinel return values conflate "no result" with a legitimate primary value, and callers routinely forget to check them. Multiple returns with `error` or a second `bool` are a Go idiom that keeps the success value honest — and the language makes the check ergonomic. Google Decisions §In-band errors: "Functions that take or return data where a particular value has special meaning should avoid 'in-band' signaling." Effective Go §Multiple return values is the canonical source (Google Decisions §In-band errors; Effective Go §Multiple return values).

**See also**: TD-15

---

## TD-17: Treat `nil` Slices as Empty; Design for the Zero-Length Case

**Strength**: SHOULD

**Summary**: In signatures and comparisons, treat `nil` slices the same as empty slices. Use `len(s) == 0`, not `s == nil`. Return `nil` (not `[]T{}`) when you have no elements; callers can `range` and `append` over nil safely.

```go
// Good
func Filter(items []Item, pred func(Item) bool) []Item {
    var out []Item // nil — fine
    for _, it := range items {
        if pred(it) { out = append(out, it) }
    }
    return out
}
if len(items) == 0 { /* empty check */ }

// Bad — forces callers to handle both nil and empty slice separately.
func Filter(items []Item, pred func(Item) bool) []Item {
    out := []Item{} // allocates for the nothing case
    // ...
    return out
}
if items == nil || len(items) == 0 { /* double check */ }
```

**Rationale**: In Go, `range`, `append`, `len`, and `cap` all work on nil slices. Returning `nil` is cheaper (no allocation) and equally correct. Distinguishing `nil` from `[]T{}` is almost always a bug attractor — unless you are doing JSON marshaling where `nil` renders as `null` and `[]T{}` renders as `[]` (and that difference matters to the schema). Uber §nil is a valid slice and Google Decisions §Nil slices both formalize this (Uber Style Guide §nil is a valid slice; Google Decisions §Nil slices).

**See also**: TD-07, TD-18, CI-12

---

## TD-18: Use Struct Tags to Lock the Wire Format

**Strength**: MUST

**Summary**: For any struct that is marshaled (JSON, YAML, Protobuf, SQL column mapping, URL values, env vars), specify struct tags explicitly for every field. Do not rely on the default "field-name-matches-wire-name" behavior.

```go
// Good
type User struct {
    ID        string    `json:"id"`
    Email     string    `json:"email"`
    CreatedAt time.Time `json:"created_at"`
    Admin     bool      `json:"admin,omitempty"`
}

// Bad — rely on Go's default; renaming ID to UserID silently breaks the wire contract.
type User struct {
    ID        string
    Email     string
    CreatedAt time.Time
    Admin     bool
}
```

**Rationale**: The default JSON encoding uses the Go field name as the key, so the wire format is coupled to Go-level names. A field rename, which looks safe locally, becomes a silent breaking change at the network boundary. Explicit tags decouple the two and make the wire contract visible at the struct definition. Uber §Use Field Tags in Marshaled Structs is explicit: "Any struct field that is marshaled into JSON, YAML, or other formats that support tag-based field naming should be annotated with the relevant tag" (Uber Style Guide §Use Field Tags in Marshaled Structs).

**See also**: TD-19, TD-06

---

## TD-19: Keep Struct Tag Ordering Consistent

**Strength**: SHOULD

**Summary**: When a field carries multiple tags (e.g., `json`, `yaml`, `db`, `validate`), order them consistently across every field in the file (and ideally across the codebase). Pick an order and stick to it.

```go
// Good — consistent json, yaml, db order for every field.
type User struct {
    ID        string    `json:"id" yaml:"id" db:"id"`
    Email     string    `json:"email" yaml:"email" db:"email"`
    CreatedAt time.Time `json:"created_at" yaml:"created_at" db:"created_at"`
}

// Bad — order shuffles per field, diffs churn, readers can't scan.
type User struct {
    ID        string    `db:"id" json:"id" yaml:"id"`
    Email     string    `json:"email" db:"email" yaml:"email"`
    CreatedAt time.Time `yaml:"created_at" json:"created_at" db:"created_at"`
}
```

**Rationale**: Consistency is the point — a reader reviewing a struct should not have to re-parse each tag line. It also lets `gofmt` align tags cleanly. No official rule mandates a specific order, but Uber and Google both emphasize local consistency (Uber Style Guide §Use Field Tags in Marshaled Structs).

**See also**: TD-18

---

## TD-20: Define Types for Physical Units

**Strength**: SHOULD

**Summary**: When a value has a physical unit (bytes, milliseconds, meters, a currency amount), define a named type that encodes the unit, with constants for common magnitudes. This prevents unit-confusion bugs (seconds vs. milliseconds, bytes vs. bits).

```go
// Good — Bytes type with magnitude constants.
type Bytes int64
const (
    KB Bytes = 1 << 10
    MB Bytes = 1 << 20
    GB Bytes = 1 << 30
)
func (b Bytes) String() string { /* "1.5 MB" */ }

func SetBufferSize(n Bytes) { /* ... */ }
SetBufferSize(4 * MB)

// Bad — raw int64 everywhere, caller units implicit.
func SetBufferSize(n int64) { /* is this bytes? KB? */ }
SetBufferSize(4_000_000) // or 4*1024*1024? nobody knows
```

**Rationale**: `time.Duration` is the canonical example in the standard library: `5 * time.Second` is self-documenting and impossible to confuse with `5 * time.Millisecond`. The same technique applies to any domain with magnitudes. Uber §Use "time" to handle time makes the general argument (Uber Style Guide §Use "time" to handle time).

**See also**: TD-10, TD-21

---

## TD-21: Use `time.Time` and `time.Duration` for Instants and Spans

**Strength**: MUST

**Summary**: Represent instants in time as `time.Time`, not `int64` Unix seconds. Represent durations as `time.Duration`, not `int` seconds or milliseconds. At the wire boundary, convert explicitly.

```go
// Good
type Event struct {
    At       time.Time     `json:"at"`
    Duration time.Duration `json:"duration_ms"` // documented unit in JSON
}
func RetryAfter(d time.Duration) { time.Sleep(d) }
RetryAfter(500 * time.Millisecond)

// Custom marshaling to emit "duration_ms" as milliseconds if desired.
func (e Event) MarshalJSON() ([]byte, error) { /* encode Duration as ms */ }

// Bad — int64 seconds in struct, ambiguous and lossy.
type Event struct {
    At       int64 `json:"at"`
    Duration int   `json:"duration_ms"` // is this ms? seconds? who knows
}
func RetryAfter(ms int) {} // seconds or millis? re-check at every call
RetryAfter(500)
```

**Rationale**: `time.Time` and `time.Duration` are typed, unit-safe, and have rich standard-library support (formatting, arithmetic, parsing, comparison). Using raw integers is a known source of "wrong by 1000x" bugs. Uber §Use "time" to handle time is prescriptive about this across package boundaries (Uber Style Guide §Use "time" to handle time).

**See also**: TD-20, TD-18

---

## TD-22: Use an Options Struct for Three-Plus Parameters with Defaults

**Strength**: SHOULD

**Summary**: When a constructor takes several parameters — especially with defaults or optional fields — take a single `Options` struct value by pointer or by value. Callers fill only the fields that matter.

```go
// Good
type ServerOptions struct {
    Addr         string
    ReadTimeout  time.Duration
    WriteTimeout time.Duration
    MaxConns     int
    Logger       *slog.Logger
}

func NewServer(opts ServerOptions) *Server {
    if opts.ReadTimeout == 0 {
        opts.ReadTimeout = 30 * time.Second
    }
    // ...
}

srv := NewServer(ServerOptions{
    Addr:        ":8080",
    ReadTimeout: 10 * time.Second,
})

// Bad — positional parameters with zeroes-for-defaults.
func NewServer(addr string, readT, writeT time.Duration, max int, log *slog.Logger) *Server {}
NewServer(":8080", 10*time.Second, 0, 0, nil) // what do 0, 0, nil mean?
```

**Rationale**: Struct literals are field-named, which makes call sites self-documenting and robust to parameter-order changes. Adding a new option only requires adding a field — existing callers compile unchanged. Google Best Practices §Option structure is the canonical source; Uber recommends struct-based configuration for the same reasons (Google Best Practices §Option structure).

**See also**: TD-23, CI-14

---

## TD-23: Prefer Functional Options for Libraries with Evolving, Orthogonal Settings

**Strength**: CONSIDER

**Summary**: When a constructor needs a growing set of orthogonal, optional settings — especially in libraries — consider the functional options pattern: accept `...Option` where `Option` is an interface with an unexported method that records state on an internal `options` struct.

```go
// Good
package db

type options struct {
    cache  bool
    logger *slog.Logger
}

type Option interface{ apply(*options) }

type cacheOpt bool
func (c cacheOpt) apply(o *options) { o.cache = bool(c) }
func WithCache(b bool) Option       { return cacheOpt(b) }

type loggerOpt struct{ log *slog.Logger }
func (l loggerOpt) apply(o *options) { o.logger = l.log }
func WithLogger(l *slog.Logger) Option { return loggerOpt{l} }

func Open(addr string, opts ...Option) (*Conn, error) {
    o := options{cache: true, logger: slog.Default()}
    for _, opt := range opts { opt.apply(&o) }
    // ...
}

db.Open(addr)
db.Open(addr, db.WithLogger(log), db.WithCache(false))

// Bad for libraries — rigid, can't add settings without breaking callers.
func Open(addr string, cache bool, logger *slog.Logger) (*Conn, error) {}
```

**Rationale**: Options expressed as values of an interface type can be compared, logged, reused, and tested more easily than closures. For a library, new options can ship without breaking older callers. Prefer this pattern when the list of settings is expected to grow or when optionality is orthogonal; an options struct (TD-22) remains simpler for closed-set internal APIs. Uber §Functional Options gives the full pattern with the interface variant; Google Best Practices §Variadic options covers the same design (Uber Style Guide §Functional Options; Google Best Practices §Variadic options).

**See also**: TD-22, TD-34

---

## TD-24: Define Interfaces at the Point of Use, Not at the Point of Implementation

**Strength**: SHOULD

**Summary**: When you need an interface to abstract over a dependency, define it in the package that *consumes* it, not in the package that implements it. Concrete packages export concrete types; consumers name their own narrow interface.

```go
// Good — consumer defines the interface it needs.
package report

type UserStore interface {
    GetUser(ctx context.Context, id string) (User, error)
}

func Generate(ctx context.Context, s UserStore, id string) (*Report, error) {
    u, err := s.GetUser(ctx, id)
    // ...
}

// And elsewhere — users package exports the concrete type; no interface there.
package users
type Store struct{ db *sql.DB }
func (s *Store) GetUser(ctx context.Context, id string) (User, error) { /* ... */ }

// report.Generate accepts *users.Store via structural satisfaction.

// Bad — producer package defines a big interface "just in case" someone needs it.
package users
type Store interface {
    GetUser(...) (...)
    CreateUser(...) error
    DeleteUser(...) error
    ListUsers(...) (...)
    // ... 12 more methods
}
```

**Rationale**: Consumer-defined interfaces stay narrow (often one or two methods) and describe exactly what the consumer needs. Producer-defined interfaces tend to bloat, couple consumers to unrelated methods, and make testing harder. Google Best Practices §Interface ownership and §Avoid unnecessary interfaces, and Effective Go §Interfaces all converge on this rule. Full interface-design mechanics are in `05-interfaces-methods.md` (Google Best Practices §Interface ownership).

**See also**: TD-25, TD-35

---

## TD-25: Assert Interface Compliance at Compile Time When You Own the Relationship

**Strength**: SHOULD

**Summary**: When a concrete type must satisfy an interface (typically one defined in another package — e.g., `io.Reader`, `http.Handler`, `sort.Interface`), add a compile-time assertion near the type definition: `var _ Iface = (*T)(nil)`.

```go
// Good — near the type definition.
type Handler struct{ /* ... */ }

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) { /* ... */ }

var _ http.Handler = (*Handler)(nil) // compile-time check

// Bad — rely on a use site far away to catch the mismatch.
// A refactor that drops a method breaks only at the call site, which may be in a test or another package.
```

**Rationale**: The zero-cost assertion `var _ Iface = (*T)(nil)` gives you a compile error at the type's own file the moment a method is removed or its signature drifts. Without it, the first signal is often a test failure far from the edit site. Uber §Verify Interface Compliance formalizes the exact spelling (Uber Style Guide §Verify Interface Compliance).

**See also**: TD-24, TD-35

---

## TD-26: Use Generics Only When They Clarify or Consolidate

**Strength**: CONSIDER

**Summary**: Reach for type parameters when you're writing the same logic for multiple unrelated types (container utilities, numeric helpers) or when `any` would force callers to assert. Don't use generics to parameterize a type that always has one concrete instantiation.

```go
// Good — one generic, many types.
func Map[T, U any](xs []T, f func(T) U) []U {
    out := make([]U, len(xs))
    for i, x := range xs { out[i] = f(x) }
    return out
}

// Good — constraint guarantees arithmetic.
func Sum[T cmp.Ordered](xs []T) T { /* ... */ }

// Bad — generic for generic's sake; only ever used with User.
type Repo[T any] struct{ /* ... */ }
var userRepo Repo[User]

// Bad — generics used where an interface is more natural.
func Process[T Processor](p T) { p.Run() } // a plain `p Processor` parameter is simpler
```

**Rationale**: Generics help when the alternative is repeating near-identical code across types or using `any` plus assertions. They *don't* help when there's only one instantiation, when an interface would suffice, or when type inference fails and callers must type-annotate every call. Google Decisions §Generics: "generics should be used judiciously... if you find yourself writing very similar code with only the types changing, consider generics; if an interface would work just as well, prefer the interface" (Google Decisions §Generics).

**See also**: TD-27, TD-28

---

## TD-27: Choose the Narrowest Type Constraint That Compiles

**Strength**: SHOULD

**Summary**: When introducing a type parameter, use the most specific constraint the body requires: `comparable` for equality, `cmp.Ordered` for `<`/`>`, a custom interface for methods, `any` only when nothing is required.

```go
// Good
func Contains[T comparable](xs []T, needle T) bool { /* ... */ }
func Max[T cmp.Ordered](a, b T) T { if a < b { return b }; return a }

type Stringer interface{ String() string }
func Join[T Stringer](xs []T, sep string) string { /* ... */ }

// Bad — any is too broad; body would need reflection or assertions.
func Contains[T any](xs []T, needle T) bool {
    for _, x := range xs {
        if x == needle { /* compile error: == not supported on any */ }
    }
    return false
}
```

**Rationale**: A narrower constraint lets the body use operations (==, <, a method) directly and documents what the caller must bring. `any` opts out of the type system inside the function; reserve it for truly type-agnostic helpers. Google Decisions §Generics §Type parameters as a design tool makes the narrowness argument (Google Decisions §Generics).

**See also**: TD-26

---

## TD-28: Start Concrete; Generify Only After Duplication Appears

**Strength**: SHOULD

**Summary**: Write the first version of a function or type with concrete types. Convert to generics when you have two or three nearly identical copies and the duplication is visibly expensive, not because the generic version is theoretically more elegant.

```go
// Good — start here.
func SumInts(xs []int) int { /* ... */ }
func SumFloats(xs []float64) float64 { /* ... */ }

// Later, once two copies exist and the third is coming, generify:
func Sum[T cmp.Ordered](xs []T) T { /* ... */ }
// Delete SumInts / SumFloats or keep them as thin wrappers.

// Bad — speculative generic with only one real user.
func Sum[T cmp.Ordered](xs []T) T { /* ... */ }
// ...only Sum[int] is ever called.
```

**Rationale**: Generic signatures are harder to read, type-infer, and document. If the concrete version stays the only instance, the extra machinery is pure cost. Google Decisions §Generics explicitly recommends deferring the generic form until duplication is real (Google Decisions §Generics).

**See also**: TD-26, TD-27

---

## TD-29: Name Nested Struct Types When They're Reused or Documented

**Strength**: SHOULD

**Summary**: Inline anonymous struct types are fine for one-off literals (test tables, quick DTOs used in a single place). Once a type is referenced from more than one place, needs a doc comment, needs methods, or needs marshaling, give it a name.

```go
// Good — anonymous struct for a one-shot table.
tests := []struct {
    give string
    want int
}{
    {give: "a", want: 1},
    {give: "b", want: 2},
}

// Good — named type once the shape is reused or documented.
// Address is the user's mailing address.
type Address struct {
    Line1 string `json:"line1"`
    City  string `json:"city"`
    Zip   string `json:"zip"`
}
type User struct {
    Name    string  `json:"name"`
    Home    Address `json:"home"`
    Work    Address `json:"work"`
}

// Bad — duplicated anonymous struct in two fields; any change must be done twice.
type User struct {
    Home struct {
        Line1 string `json:"line1"`
        City  string `json:"city"`
        Zip   string `json:"zip"`
    } `json:"home"`
    Work struct {
        Line1 string `json:"line1"`
        City  string `json:"city"`
        Zip   string `json:"zip"`
    } `json:"work"`
}
```

**Rationale**: Anonymous structs can't have methods, can't be documented, and can't be referenced by type from other files. Once any of those is desirable, a named type is strictly better. Uber §Test Tables uses anonymous structs specifically because the scope is one loop; Google Best Practices §Major forms of package state APIs encourages named types for anything public (Uber Style Guide §Test Tables).

**See also**: TD-30

---

## TD-30: Group Struct Fields by Role, with Blank Lines Between Groups

**Strength**: SHOULD

**Summary**: In a struct with many fields, separate logically distinct groups (identity, configuration, state, metrics) with a single blank line. Keep mutex or lock declarations directly above the fields they guard.

```go
// Good
type Server struct {
    // Identity
    ID   string
    Name string

    // Configuration
    Addr         string
    ReadTimeout  time.Duration
    WriteTimeout time.Duration

    // State (mu guards the fields below)
    mu        sync.Mutex
    handlers  map[string]Handler
    listening bool

    // Metrics
    requestCount atomic.Int64
}

// Bad — everything in one wall of fields; the mutex contract is invisible.
type Server struct {
    ID           string
    Addr         string
    mu           sync.Mutex
    handlers     map[string]Handler
    Name         string
    ReadTimeout  time.Duration
    listening    bool
    WriteTimeout time.Duration
    requestCount atomic.Int64
}
```

**Rationale**: Grouping signals the designer's mental model of the struct — which fields are inputs, which are state, which are internal. Putting the guarding mutex directly above its fields (and optionally a comment like `// mu guards the fields below`) documents a locking discipline that's otherwise invisible. Uber §Zero-value Mutexes recommends this layout for mutex-guarded state.

**See also**: TD-05, TD-30, TD-31

---

## TD-31: Reorder Fields for Alignment Only When the Cost Is Measured

**Strength**: CONSIDER

**Summary**: Go struct field layout affects size via alignment padding. For most structs, leave fields ordered by role (TD-30). For hot, frequently-allocated structs — caches, graph nodes, per-request structs — measure size with `fieldalignment` and reorder largest-to-smallest if it pays.

```go
// Default — grouped by role, even if not maximally packed.
type Packet struct {
    Kind  uint8  // 1 byte + 7 padding
    Len   int64  // 8 bytes
    Flags uint8  // 1 byte + 7 trailing padding
} // 24 bytes

// Only do this after measurement suggests the padding matters.
type Packet struct {
    Len   int64 // 8 bytes
    Kind  uint8 // 1 byte
    Flags uint8 // 1 byte + 6 trailing padding
} // 16 bytes
```

**Rationale**: Alignment-optimal ordering sacrifices readability for memory. The vast majority of structs aren't allocated at a rate where the savings matter. Use `go vet -vettool=$(which fieldalignment)` or `betteralign` to identify the few structs where it's worth the trade. Google's guidance emphasizes measuring before reordering; premature layout optimization is an anti-pattern.

**See also**: TD-30

---

## TD-32: Name Types for the Role They Play, Not Their Implementation

**Strength**: SHOULD

**Summary**: Types should be named for what they represent in the domain, not for how they're built. Prefer `UserStore`, `OrderProcessor`, `RetryPolicy` over `UserMap`, `OrderStruct`, `RetryConfigObj`.

```go
// Good
type UserStore interface { /* ... */ }
type MemoryUserStore struct{ /* ... */ }  // implementation prefix is fine
type RetryPolicy struct{ /* ... */ }

// Bad
type UserMap map[string]User          // leaks implementation (what if it becomes a DB?)
type OrderStruct struct{ /* ... */ }  // "Struct" is noise
type RetryConfigObj struct{ /* ... */ }
```

**Rationale**: A type name is part of the API. Naming by implementation (`Map`, `Struct`, `Obj`) forces a rename when the implementation changes. Role-based names outlast implementations. Google Decisions §Naming and §Interface types use this rule throughout (Google Decisions §Naming).

**See also**: TD-10, TD-33

---

## TD-33: Name Constants for Their Role, Not as ALL_CAPS

**Strength**: MUST

**Summary**: Go constants follow the same `MixedCaps` rule as other identifiers. `MaxConns`, `DefaultTimeout`, `APIVersion` — not `MAX_CONNS`, `DEFAULT_TIMEOUT`, `API_VERSION`. Unexported constants use camelCase: `maxConns`.

```go
// Good
const (
    MaxRetries     = 5
    DefaultTimeout = 30 * time.Second
    APIVersion     = "v1"
)

const maxBuffer = 4096 // unexported

// Bad
const (
    MAX_RETRIES     = 5
    DEFAULT_TIMEOUT = 30 * time.Second
    kMaxBuffer      = 4096 // k-prefix is C++; Go uses MixedCaps
)
```

**Rationale**: Go's case-based visibility rule replaces ALL_CAPS as a visibility signal: the first letter's case tells you exported vs. unexported, so additional uppercasing conveys nothing. Google Decisions §Constant names: "Constants in Go are named using MixedCaps like other names, even if they are unchanging values with no complex internal structure" (Google Decisions §Constant names; Uber Style Guide §Naming).

**See also**: TD-12, TD-32

---

## TD-34: Write a Constructor Only When Construction Is Nontrivial

**Strength**: SHOULD

**Summary**: If a type's zero value is usable (TD-01) or a struct literal is adequate, don't invent a `NewT` constructor. Constructors are for types that need validation, resource acquisition, or default population.

```go
// Good — no constructor needed; struct literal is self-documenting.
cfg := Config{MaxConns: 10, Timeout: 30 * time.Second}

// Good — constructor earns its keep: validation and defaults.
func NewClient(addr string, opts ClientOptions) (*Client, error) {
    if addr == "" { return nil, errors.New("addr required") }
    if opts.Timeout == 0 { opts.Timeout = 30 * time.Second }
    return &Client{addr: addr, opts: opts}, nil
}

// Bad — trivial "constructor" that only forwards fields.
func NewConfig(maxConns int, timeout time.Duration) Config {
    return Config{MaxConns: maxConns, Timeout: timeout}
}
```

**Rationale**: A `NewT` that only copies its arguments adds a call site without adding safety — it's pure ceremony. Reserve constructors for the cases that actually protect invariants (required inputs, allocated resources, defaults). Google Best Practices §Providing a default instance and Uber §Initializing Structs both assume struct literals for the trivial case (Google Best Practices §Providing a default instance).

**See also**: TD-01, TD-22, TD-35

---

## TD-35: Constructors Return Concrete Types, Not Interfaces

**Strength**: SHOULD

**Summary**: When a constructor returns a newly built value, return the concrete type (`*Client`, `Server`), not an interface. Callers who need an interface can assign to one; callers who need concrete methods can still reach them.

```go
// Good
func NewClient(addr string) (*Client, error) { /* ... */ }

c, err := NewClient(":8080")
// c has access to every *Client method and also satisfies any interface it implements.

// Bad — return io.ReadCloser when *File has more methods the caller might need.
func Open(path string) (io.ReadCloser, error) { return os.Open(path) }
```

**Rationale**: Returning an interface narrows callers' access unnecessarily. "Accept interfaces, return concrete types" is the canonical Go phrasing: your function signature takes the smallest interface it needs for the input, but hands back the concrete result so the caller can use its full behavior (including type assertions, fields, and un-abstracted methods). Full interface-placement guidance lives in `05-interfaces-methods.md`. Effective Go §Interfaces and Google Best Practices §Avoid unnecessary interfaces both codify this (Google Best Practices §Avoid unnecessary interfaces).

**See also**: TD-24, TD-34

---

## TD-36: Name Return Parameters Only When They Clarify, Not for Naked Returns

**Strength**: SHOULD-AVOID

**Summary**: Use named result parameters when the names document the role of each return value (especially when two returns have the same type). Don't use named returns to enable naked `return` statements — explicit returns are clearer.

```go
// Good — names clarify which is which.
func Divide(a, b float64) (quotient, remainder float64, err error) {
    if b == 0 { return 0, 0, errors.New("div by zero") }
    return a / b, math.Mod(a, b), nil
}

// Good — no names needed; return types are obvious.
func GetUser(id string) (*User, error) { /* ... */ }

// Bad — named returns used for naked returns, hiding what each value is.
func Divide(a, b float64) (quotient, remainder float64, err error) {
    if b == 0 {
        err = errors.New("div by zero")
        return // reader must track state through the function
    }
    quotient = a / b
    remainder = math.Mod(a, b)
    return
}
```

**Rationale**: Named returns give you two features: (a) a zero-initialized variable of the return type in scope, and (b) the option to use naked `return`. (a) is useful for documentation and deferred cleanup (`defer func(){ err = ... }()`); (b) is almost always a readability loss in anything larger than a few lines. Google Decisions §Named result parameters: "use named result parameters only when the name makes the function clearer; don't use them just to enable naked returns" (Google Decisions §Named result parameters).

**See also**: TD-15, TD-16

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Design zero value useful | SHOULD | `var x T` should just work |
| 02 | Embed values, not pointers | SHOULD | Pointer embedding nukes the zero value |
| 03 | Avoid embedding in exported structs | SHOULD-AVOID | Leaks every future method |
| 04 | Embedded fields at top | SHOULD | Make promoted surface visible |
| 05 | Don't embed uncopyable types | MUST-AVOID | Mutex, WaitGroup, Buffer, atomic.* |
| 06 | Unexported fields by default | SHOULD | Export deliberately |
| 07 | Copy slices/maps at boundaries | SHOULD | Prevent aliasing bugs |
| 08 | Uncopyable state → pointer-only | MUST | All methods on `*T`, construct with `&T{}` |
| 09 | Pointer vs value receivers by shape | SHOULD | Pick once per type, stay consistent |
| 10 | Defined types for domain IDs | SHOULD | `type UserID string` prevents swaps |
| 11 | `type A B` ≠ `type A = B` | MUST | Defined types for semantics, aliases for migration |
| 12 | Start enums at 1 (or Unknown at 0) | SHOULD | Zero means "unset" |
| 13 | Enums implement `Stringer` | SHOULD | Readable logs, use `stringer` tool |
| 14 | Named type over `bool` parameter | SHOULD | Call sites self-document |
| 15 | Return `error`, not `*MyError` | SHOULD | Avoid typed-nil interface bug |
| 16 | Multiple returns, not sentinels | MUST | `(T, error)` or `(T, bool)` |
| 17 | `nil` slices are empty slices | SHOULD | `len(s) == 0`, return nil |
| 18 | Struct tags for wire format | MUST | Decouple Go name from JSON/DB name |
| 19 | Consistent struct tag order | SHOULD | Same order across every field |
| 20 | Types for physical units | SHOULD | Prevent unit confusion |
| 21 | `time.Time`/`time.Duration` | MUST | Never raw int64 seconds |
| 22 | Options struct for 3+ params | SHOULD | Field-named call sites |
| 23 | Functional options for libraries | CONSIDER | Evolving optional settings |
| 24 | Consumer defines interface | SHOULD | Small, purpose-built |
| 25 | Compile-time interface assertion | SHOULD | `var _ Iface = (*T)(nil)` |
| 26 | Generics when they consolidate | CONSIDER | Not for a single instantiation |
| 27 | Narrowest constraint that compiles | SHOULD | `comparable`, `cmp.Ordered`, method set |
| 28 | Start concrete, generify later | SHOULD | Wait for real duplication |
| 29 | Name nested structs when reused | SHOULD | Anonymous only for one-shot |
| 30 | Group fields by role | SHOULD | Mutex above the fields it guards |
| 31 | Align fields only when measured | CONSIDER | `fieldalignment` when it pays |
| 32 | Name types for role | SHOULD | `UserStore`, not `UserMap` |
| 33 | Constants in MixedCaps | MUST | No `ALL_CAPS`, no `k`-prefix |
| 34 | Constructor only if nontrivial | SHOULD | Struct literals for the trivial case |
| 35 | Constructors return concrete | SHOULD | Accept interfaces, return concrete |
| 36 | Named returns for clarity only | SHOULD-AVOID | Don't enable naked returns |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for zero-value usage, nil slices, struct-literal initialization, and MixedCaps naming that this chapter builds on (CI-11, CI-12, CI-14, CI-17, CI-18)
- **API Design**: See `02-api-design.md` for the broader API context around constructors (TD-34), options (TD-22, TD-23), and return-type choices (TD-35)
- **Error Handling**: See `03-error-handling.md` for full error-type design — sentinel errors, wrapping, custom error types, `errors.Is`/`errors.As` — beyond the signature rule in TD-15
- **Interfaces & Methods**: See `05-interfaces-methods.md` for method-set rules, interface-satisfaction mechanics, and accept-interfaces/return-concrete (extends TD-09, TD-24, TD-25, TD-35)
- **Concurrency**: See `06-concurrency.md` for `sync` primitive usage, goroutine lifetimes, and `context` propagation; this chapter only covers the type-design constraints they impose (TD-05, TD-08)
- **Testing**: See `07-testing.md` for table-driven tests that use anonymous structs deliberately (TD-29)
- **Anti-Patterns**: See `09-anti-patterns.md` for patterns that amplify TD-03, TD-05, TD-15, TD-18

---

## External References

- [*Effective Go*](https://go.dev/doc/effective_go) — the Go team's foundational guide (§The zero value, §New types, §Interfaces, §Multiple return values)
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — §Verify Interface Compliance, §Zero-value Mutexes, §Copy Slices and Maps at Boundaries, §Start Enums at One, §Use "time" to handle time, §Avoid Embedding Types in Public Structs, §Use Field Tags in Marshaled Structs, §Functional Options
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions §Receiver type, §Copying, §Zero-value fields, §Nil slices, §Constant names, §Type aliases, §Generics, §In-band errors, §Named result parameters; Best Practices §Option structure, §Variadic options, §Avoid unnecessary interfaces, §Interface ownership, §Providing a default instance
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — receiver types, interfaces, errors
- [Go Proverbs](https://go-proverbs.github.io/) — "The bigger the interface, the weaker the abstraction"; "Don't communicate by sharing memory, share memory by communicating"
- [`fieldalignment`](https://pkg.go.dev/golang.org/x/tools/go/analysis/passes/fieldalignment) — analyzer for struct layout (TD-31)
- [`stringer`](https://pkg.go.dev/golang.org/x/tools/cmd/stringer) — generate `String()` for enum types (TD-13)
- [`go vet -copylocks`](https://pkg.go.dev/cmd/vet) — detect copied mutexes (TD-05, TD-08)
