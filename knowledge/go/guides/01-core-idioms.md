# Core Go Idioms

Essential Go idioms for writing clean, idiomatic code that matches community conventions. These patterns represent fundamental best practices grounded in authoritative sources: the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and *Effective Go*.

Target environment: **Go 1.22+**, **standard library first**, **`gofmt` + `go vet` + `staticcheck`** for formatting and linting.

---

## CI-01: Use `:=` for Initialization, `var` for Zero-Value Declarations

**Strength**: SHOULD

**Summary**: Use short variable declaration (`:=`) when you are assigning a non-zero initial value. Use `var` when declaring a variable whose initial value is its zero value (so the reader sees the type explicitly).

```go
// Good
var count int            // zero value — reader sees int clearly
var users []User         // nil slice, ready to append
sum := computeSum(xs)    // non-zero init — := is concise and clear
name := "Alice"

// Bad
var sum int = computeSum(xs)  // redundant — := is shorter
count := 0                    // when the value is just the zero value, var is clearer
var name string = "Alice"     // redundant type annotation
```

**Rationale**: `:=` emphasizes the initial value and infers the type. `var` emphasizes the type and the zero-value start. Mixing them signals intent. Google Best Practices §Variable declarations: "use the `var` keyword when declaring a variable with no initial value... the short variable declaration should only be used when a variable is being set to some non-zero value." Uber §Local Variable Declarations makes the same point (Google Best Practices §Variable declarations; Uber Style Guide §Local Variable Declarations).

**See also**: CI-02, CI-03

---

## CI-02: Use Top-Level `var` Without Redundant Type

**Strength**: SHOULD

**Summary**: At package scope, omit the type in `var` declarations when it can be inferred from the initializer. Otherwise, the type is duplicated.

```go
// Good
var defaultTimeout = 30 * time.Second
var validName = regexp.MustCompile(`^[a-z]+$`)
var errNotFound = errors.New("not found")

// Bad
var defaultTimeout time.Duration = 30 * time.Second
var validName *regexp.Regexp = regexp.MustCompile(`^[a-z]+$`)
var errNotFound error = errors.New("not found")
```

**Rationale**: The type is already visible in the initializer, so annotating it is redundant. Specify the type only when the initializer's inferred type is not what you want (e.g., `var x int64 = 1`). Uber §Top-level Variable Declarations: "Unless you are initializing the variable to some value different from the type implied by the expression, omit the type from the declaration" (Uber Style Guide §Top-level Variable Declarations).

---

## CI-03: Group Similar Declarations

**Strength**: SHOULD

**Summary**: Group related `var`, `const`, `import`, or `type` declarations into a single parenthesized block. Keep unrelated declarations separate.

```go
// Good
const (
    maxRetries  = 3
    defaultPort = 8080
    apiVersion  = "v1"
)

var (
    errInvalidInput = errors.New("invalid input")
    errNotFound     = errors.New("not found")
    errTimeout      = errors.New("timeout")
)

// Bad
const maxRetries = 3
const defaultPort = 8080
const apiVersion = "v1"

var errInvalidInput = errors.New("invalid input")
var errNotFound = errors.New("not found")
var errTimeout = errors.New("timeout")
```

**Rationale**: Grouping signals relation: these things belong together. It also aligns cleanly under `gofmt`. Uber §Group Similar Declarations: "Go supports grouping similar declarations... Do not group unrelated declarations" (Uber Style Guide §Group Similar Declarations).

---

## CI-04: Group Imports: Standard Library, Then Everything Else

**Strength**: SHOULD

**Summary**: Split imports into two groups separated by a blank line: standard library first, then third-party and local. `goimports` does this automatically.

```go
// Good
import (
    "context"
    "fmt"
    "os"

    "github.com/pkg/errors"
    "go.uber.org/zap"

    "example.com/myproject/internal/config"
)

// Bad — mixed together
import (
    "context"
    "example.com/myproject/internal/config"
    "fmt"
    "github.com/pkg/errors"
    "go.uber.org/zap"
    "os"
)
```

**Rationale**: Grouping separates standard-library dependencies (always available) from external dependencies (pinned by `go.mod`) from local packages. It matches the convention `goimports` enforces. Google §Imports and Uber §Import Group Ordering both specify two groups, stdlib first (Google Decisions §Imports; Uber Style Guide §Import Group Ordering).

---

## CI-05: Package Names Are Short, Lowercase, Single Words

**Strength**: MUST

**Summary**: Package names are lowercase, short, and a single word. No `snake_case`, no `camelCase`, no plural forms, no meaningless names like `util` or `common`.

```go
// Good
package user
package httputil
package tabwriter

// Bad
package Users         // capitalized
package user_service  // underscores
package userService   // camelCase
package util          // meaningless catch-all
package common        // meaningless catch-all
```

**Rationale**: The package name appears at every call site (`pkg.Thing`), so it should be short and descriptive. Google Decisions §Package names: "Good Go package names are short and clear... Avoid meaningless package names like `util`, `utility`, `common`, `helper`." Uber §Package Names enforces the same rules (Google Decisions §Package names; Uber Style Guide §Package Names; Effective Go §Package names).

**See also**: CI-06

---

## CI-06: Avoid Weasel Packages: `util`, `common`, `helpers`, `misc`

**Strength**: SHOULD-AVOID

**Summary**: Do not create packages whose name tells you nothing about their purpose. Name packages by what they provide, not how they are used.

```go
// Bad
package util       // what does it do?
package helpers    // help with what?
package common     // common to what?
package misc       // literally "miscellaneous"

// Good — name by purpose
package stringutil  // operates on strings
package timeconv    // converts times
package httpauth    // HTTP auth helpers
```

**Rationale**: "Util" packages accrete unrelated functions whose only commonality is that someone thought they might be reused. They create import cycles, obscure ownership, and hide the true home of each function. Google Best Practices §Util packages: "If it is meaningful, prefer naming a utility package after the domain of its contents instead of `util`." Uber echoes this (Google Best Practices §Util packages; Uber Style Guide §Package Names).

**See also**: CI-05

---

## CI-07: Use MixedCaps, Not `snake_case`

**Strength**: MUST

**Summary**: Multi-word identifiers use `MixedCaps` (exported) or `mixedCaps` (unexported). Never use underscores to separate words.

```go
// Good
var maxRetries = 3
type UserService struct{}
func ProcessOrder(o Order) error

// Bad
var max_retries = 3
type User_Service struct{}
func Process_Order(o Order) error
```

**Rationale**: `gofmt` does not rewrite names, but Go's convention — enforced by `revive`, `staticcheck`, and community reviewers — is unambiguous. Google Style Guide §MixedCaps: "Go source code uses `MixedCaps` or `mixedCaps` (camel case) rather than underscores when writing multi-word names." The only exception is test function names of the form `Test_feature_behavior` (Google Style Guide §MixedCaps; Google Decisions §Underscores; Effective Go §Mixed caps).

**See also**: CI-08

---

## CI-08: Keep Initialisms Consistent in Case

**Strength**: SHOULD

**Summary**: Treat initialisms (URL, ID, API, DB, HTTP) as single words. Use all-uppercase when exported, all-lowercase when unexported. Never mix cases within one initialism.

```go
// Good
var userID int
var apiURL string
func ServeHTTP(w http.ResponseWriter, r *http.Request)
type JSONEncoder struct{}

// Bad
var userId int          // mixed — Id is not consistent
var apiUrl string       // Url is not consistent
func ServeHttp(...)     // Http is not consistent
type JsonEncoder struct // Json is not consistent
```

**Rationale**: Treating initialisms as single words keeps names scannable and visually grouped. Google Decisions §Initialisms: "Words in names that are initialisms or acronyms (e.g., `URL` and `NATO`) should have the same case. `URL` should appear as `URL` or `url` (as in `urlPony`, or `URLPony`), never as `Url`." The standard library follows this consistently (Google Decisions §Initialisms; Uber Style Guide §Guidelines).

---

## CI-09: Receiver Names Are Short and Consistent

**Strength**: SHOULD

**Summary**: Receiver names are 1–2 letters, usually derived from the type name. Use the same receiver name for every method on a given type.

```go
// Good — consistent 'u' across User methods
func (u *User) Name() string      { return u.name }
func (u *User) Email() string     { return u.email }
func (u *User) SetRole(r Role)    { u.role = r }

// Bad — changing receiver names across methods
func (u *User) Name() string      { return u.name }
func (self *User) Email() string  { return self.email }  // inconsistent
func (user *User) SetRole(r Role) { user.role = r }      // verbose

// Bad — no meaningful receiver
func (this *User) Name() string   { return this.name }   // 'this' is not Go
```

**Rationale**: Short receivers reduce visual noise; consistency lets readers navigate a file without re-learning names. Never use `self`, `this`, or `me` — those come from other languages. Google Decisions §Receiver names: "Receiver variable names must be short (usually one or two letters in length)... A given type's references should use a consistent receiver name." Uber agrees (Google Decisions §Receiver names; Uber Style Guide §Guidelines).

---

## CI-10: No `Get` Prefix on Getter Methods

**Strength**: SHOULD-AVOID

**Summary**: A getter is named after the field it exposes, not `GetField`. The `Get` prefix is JavaBean-style noise.

```go
// Good
type User struct {
    name string
}
func (u *User) Name() string  { return u.name }
func (u *User) SetName(n string) { u.name = n }

// Bad
func (u *User) GetName() string { return u.name }
```

**Rationale**: A method returning a value is already identifiable as a getter by its signature; the `Get` prefix adds nothing. Setters do take `Set` because `SetX(value)` distinguishes them from `X()`. Effective Go §Getters: "It's neither idiomatic nor necessary to put `Get` into the getter's name." Google Decisions §Getters: same rule (Effective Go §Getters; Google Decisions §Getters).

---

## CI-11: Use Zero Values — Don't Initialize What You Don't Need To

**Strength**: SHOULD

**Summary**: Many Go types are usable in their zero state. A `sync.Mutex`, a `bytes.Buffer`, a nil slice, a nil map read — all work without explicit initialization. Only initialize when you need a non-zero value.

```go
// Good — zero-value mutex and buffer
type Server struct {
    mu    sync.Mutex         // ready to use
    buf   bytes.Buffer       // ready to use
    conns []net.Conn         // nil slice — append works
}

var s Server
s.mu.Lock()
s.buf.WriteString("hello")
s.conns = append(s.conns, c)  // works on nil slice

// Bad — unnecessary initialization
type Server struct {
    mu    *sync.Mutex
    buf   *bytes.Buffer
    conns []net.Conn
}

s := Server{
    mu:    &sync.Mutex{},
    buf:   &bytes.Buffer{},
    conns: []net.Conn{},  // empty, non-nil — usually not what you want
}
```

**Rationale**: Go is carefully designed so that the zero value is useful for the most important standard types. Making these pointers or pre-initializing them adds noise, allocations, and nil-pointer risk. Uber §Zero-value Mutexes are Valid: "The zero-value `sync.Mutex` and `sync.RWMutex` are valid, so you almost never need a pointer to a mutex." Effective Go §The zero value: "Since the zero value is useful and the storage allocation propagates through the data structures, it is a good idea to design your types so that the zero value is useful" (Uber §Zero-value Mutexes; Effective Go §The zero value).

**See also**: CI-12, CI-13

---

## CI-12: `nil` Slices Are Valid — Don't Distinguish Them from Empty Slices

**Strength**: SHOULD

**Summary**: `nil` slices behave like empty slices for `len`, `cap`, `range`, and `append`. Return `nil`, don't return `[]T{}` to signal "no elements."

```go
// Good
func activeUsers() []User {
    var result []User          // nil slice
    for _, u := range allUsers {
        if u.active {
            result = append(result, u)  // append works on nil
        }
    }
    return result  // nil if no matches — that's fine
}

// Check length, not nilness
if len(users) == 0 { /* ... */ }

// Bad — returning empty literal just to avoid nil
func activeUsers() []User {
    result := []User{}  // allocates a header; nil would do
    // ...
    return result
}

// Bad — nil check conflates two equivalent states
if users == nil { /* ... */ }  // use len(users) == 0 instead
```

**Rationale**: From a caller's perspective, an empty slice and a nil slice are indistinguishable through the slice API. Uber §nil is a valid slice: "nil is a valid slice of length 0. This means that... you should return a nil slice instead [of an empty slice]... To check if a slice is empty, always use `len(s) == 0`. Do not check for nil." Google Decisions §Nil slices agrees (Uber Style Guide §nil is a valid slice; Google Decisions §Nil slices).

**Exception**: JSON marshalling distinguishes them (`nil` → `null`, `[]T{}` → `[]`). When exact wire format matters, initialize explicitly.

**See also**: CI-11

---

## CI-13: Initialize Maps with `make`, Not `map` Literals (Unless Populating)

**Strength**: SHOULD

**Summary**: Use `make(map[K]V)` for an empty map you will populate. Use a map literal only when you are inserting entries at construction time.

```go
// Good — empty map to be filled
counts := make(map[string]int)
for _, event := range events {
    counts[event.kind]++
}

// Good — literal with known contents
statusText := map[int]string{
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
}

// Good — literal with known capacity hint
counts := make(map[string]int, len(events))

// Bad
counts := map[string]int{}   // map literal for an empty map — use make
```

**Rationale**: `make` signals "empty, ready to grow"; a literal signals "these are the entries". Keeping the signals distinct makes reading easier. Uber §Initializing Maps: "Prefer `make(..)` for empty maps, and maps populated programmatically. This makes map initialization visually distinct from declaration." `make` also accepts a size hint (Uber Style Guide §Initializing Maps).

---

## CI-14: Use Field Names in Struct Literals

**Strength**: SHOULD

**Summary**: Initialize structs with explicit `Field: value` syntax. Positional struct literals are only acceptable for tiny, stable types (e.g., `image.Point{1, 2}`).

```go
// Good
u := User{
    Name:  "Alice",
    Email: "alice@example.com",
    Role:  RoleAdmin,
}

// Bad — positional; breaks silently when fields are added or reordered
u := User{"Alice", "alice@example.com", RoleAdmin}
```

**Rationale**: Named fields survive refactors. If a new field is added to `User`, positional initializers become compile errors or, worse, silently misinterpret existing values. `go vet` warns on unnamed struct literals outside the same package. Google Decisions §Field names: "For struct types from other packages, provide the field names in a struct literal." Uber §Use Field Names to Initialize Structs expands this to every struct with more than a few fields (Google Decisions §Field names; Uber Style Guide §Use Field Names to Initialize Structs).

**See also**: CI-15

---

## CI-15: Omit Zero-Value Fields in Struct Literals

**Strength**: SHOULD

**Summary**: When initializing a struct, omit fields whose desired value is the zero value. Listing them adds noise.

```go
// Good
u := User{
    Name: "Alice",
}
// Role and Active left at zero values

// Bad — zero-value clutter
u := User{
    Name:   "Alice",
    Email:  "",
    Role:   RoleNone,
    Age:    0,
    Active: false,
}
```

**Rationale**: Readers focus on the fields that matter. Explicit zero values distract and make it look like those values were chosen deliberately rather than defaulted. Uber §Omit Unnecessary Zero Value Fields in Structs: "Explicitly listing fields that have zero values adds noise" (Uber Style Guide §Omit Unnecessary Zero Value Fields in Structs).

**Exception**: When the struct has few fields and the zero values are semantically important (e.g., a config with `Debug: false` explicitly stating the default), listing them can be acceptable for documentation.

---

## CI-16: Use `&T{}` for Pointers, Not `new(T)`

**Strength**: SHOULD

**Summary**: Prefer `&T{}` over `new(T)` when constructing a pointer to a struct. `new` is generally reserved for pointers to basic types.

```go
// Good
u := &User{Name: "Alice"}
p := &Point{X: 1, Y: 2}

// Bad
u := new(User)
u.Name = "Alice"      // two statements instead of one

// Acceptable
n := new(int)         // *int zero — fine; &int{} is not valid syntax
```

**Rationale**: `&T{...}` is more flexible because it allows field initialization in the same expression. `new(T)` always produces a zero-valued pointer that must be mutated later. Uber §Initializing Struct References: "Use `&T{}` instead of `new(T)` when initializing struct references so that it is consistent with the struct initialization" (Uber Style Guide §Initializing Struct References; Google Decisions §Composite literals).

---

## CI-17: Use `var x T` for a Zero-Value Struct

**Strength**: SHOULD

**Summary**: To declare an empty (zero-value) struct, use `var x T`. Reserve `x := T{}` for cases where you are initializing fields (even if none end up set).

```go
// Good
var user User    // zero value, declared intent is "start empty"

// Good — explicit empty struct literal for initialization intent
user := User{}   // less common, but acceptable when fields may follow

// Bad — using := just for the zero value
user := User{}   // when you want zero, var User is clearer
```

**Rationale**: `var` signals "start at zero"; `T{}` signals "I'm choosing these field values (even though the list is empty)." Keeping the signals distinct is the same principle as CI-01. Uber §Initializing Structs: "Declare empty structs with `var`" (Uber Style Guide §Initializing Structs).

**See also**: CI-01, CI-15

---

## CI-18: Use `iota` for Enumerated Constants, Start at 1 for Explicit Values

**Strength**: SHOULD

**Summary**: Use `iota` for related constants. Skip `0` (by starting at `iota + 1`) when the zero value would be ambiguous or misleading — unless there is a meaningful "unknown" zero case.

```go
// Good — zero value means "unknown/unset", which is a real state
type LogLevel int
const (
    LogLevelUnknown LogLevel = iota
    LogLevelDebug
    LogLevelInfo
    LogLevelWarn
    LogLevelError
)

// Good — no meaningful zero state; start at 1
type Operation int
const (
    OpAdd Operation = iota + 1
    OpSubtract
    OpMultiply
    OpDivide
)

// Bad — zero would silently mean "Add" even for an uninitialized var
type Operation int
const (
    OpAdd Operation = iota
    OpSubtract
    OpMultiply
    OpDivide
)
```

**Rationale**: The zero value of an `int`-based enum is the first constant. If that constant is a valid operational state (e.g., `OpAdd`), a forgotten initialization silently behaves as that state. Starting at 1 forces callers to set a value explicitly, or to handle the zero as "unknown." Uber §Start Enums at One: "The standard way of introducing enumerations in Go is to declare a custom type and a const group with `iota`. Since variables have a zero value... you should usually start your enums on a non-zero value" (Uber Style Guide §Start Enums at One).

---

## CI-19: Use the Comma-Ok Idiom for Type Assertions and Map Lookups

**Strength**: MUST

**Summary**: When a type assertion may fail, or when a map key may be missing, use the two-return form (`value, ok := ...`). The single-return form of a type assertion panics on failure.

```go
// Good — type assertion
if s, ok := x.(string); ok {
    fmt.Println("got string:", s)
} else {
    return fmt.Errorf("expected string, got %T", x)
}

// Good — map lookup
if v, ok := cache[key]; ok {
    return v
}
return compute(key)

// Bad — single-return type assertion panics if x is not a string
s := x.(string)

// Bad — can't distinguish "missing key" from "zero value"
v := cache[key]
if v == 0 {
    // is 0 the stored value, or was the key missing?
}
```

**Rationale**: The single-return type assertion panics on failure, which is rarely what you want. For maps, the zero value cannot be distinguished from an absent key without the `ok` return. Uber §Handle Type Assertion Failures: "The single return value form of a type assertion will panic on an incorrect type. Therefore, always use the 'comma ok' idiom" (Uber Style Guide §Handle Type Assertion Failures).

---

## CI-20: Handle Errors — Don't Ignore Them with `_`

**Strength**: MUST

**Summary**: Check every returned error. Explicitly discarding an error with `_` is acceptable only when the error is provably uninteresting (rare) and always with a comment explaining why.

```go
// Good
data, err := os.ReadFile(path)
if err != nil {
    return fmt.Errorf("read %q: %w", path, err)
}

// Acceptable with comment
_ = conn.Close()  // best-effort close; already logging above

// Bad — silently discards
data, _ := os.ReadFile(path)
json.Unmarshal(data, &v)  // also ignored
```

**Rationale**: Silent `_` on an error is the Go equivalent of an empty `catch` block — and because Go has no exceptions, the error is the only signal. `errcheck` and `staticcheck` both flag this. Google Decisions §Returning errors and Uber §Guidelines both insist on explicit handling (Google Decisions §Returning errors; Uber Style Guide §Guidelines).

**Note**: Detailed error-handling patterns (wrapping, `errors.Is`, custom types) are covered in chapter 03.

---

## CI-21: Indent the Error Path; Keep the Happy Path Left-Aligned

**Strength**: SHOULD

**Summary**: Handle errors by returning early. The main logic stays at the lowest indentation level; the error handling is indented.

```go
// Good
func load(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("read %q: %w", path, err)
    }

    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return nil, fmt.Errorf("parse %q: %w", path, err)
    }

    return &cfg, nil
}

// Bad — happy path indented inside err == nil branches
func load(path string) (*Config, error) {
    if data, err := os.ReadFile(path); err == nil {
        var cfg Config
        if err := json.Unmarshal(data, &cfg); err == nil {
            return &cfg, nil
        } else {
            return nil, err
        }
    } else {
        return nil, err
    }
}
```

**Rationale**: Reading top-to-bottom, the main flow stays on the left margin; errors return early. This makes both paths easy to scan. Google Decisions §Indent error flow: "Go code is written with the success path aligned to the left, and the failure paths increasingly to the right. Each condition check contributes to this alignment pattern" (Google Decisions §Indent error flow; Effective Go §If; Uber Style Guide §Reduce Nesting).

**See also**: CI-22

---

## CI-22: Reduce Nesting — Omit Unnecessary `else`

**Strength**: SHOULD

**Summary**: When an `if` branch ends with `return`, `break`, `continue`, or `panic`, the following code does not need to be in an `else` block.

```go
// Good
if err != nil {
    return err
}
doWork()  // not indented, no else

// Good
for _, item := range items {
    if !item.valid {
        continue
    }
    process(item)  // not inside an else
}

// Bad — unnecessary else
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
```

**Rationale**: Each nesting level costs cognitive load. Terminating early and letting the next statement flow naturally reads better. `gofmt` does not fix this, but `revive`, `staticcheck`, and `go vet` flag it. Uber §Unnecessary Else: "If a variable is set in both branches of an if, it can be replaced with a single if" (Uber Style Guide §Unnecessary Else; Google Decisions §Indent error flow).

**See also**: CI-21

---

## CI-23: Reduce the Scope of Variables

**Strength**: SHOULD

**Summary**: Declare variables in the narrowest scope that holds them. Move the declaration into the block where the variable is used when possible.

```go
// Good — data scope limited to the err check
if data, err := os.ReadFile(path); err == nil {
    return parse(data)
}

// Good
for i := 0; i < n; i++ {
    // i is only visible here
}

// Bad — data outlives its use
data, err := os.ReadFile(path)
if err == nil {
    return parse(data)
}
// data is still in scope here for no reason
```

**Rationale**: Narrow scope limits how far a reader must scan to understand a variable's lifetime. `if` and `for` both allow declaration in the initializer clause — use that. Uber §Reduce Scope of Variables: "Where possible, reduce the scope of variables and constants. Do not reduce the scope if it conflicts with [Reduce Nesting]" (Uber Style Guide §Reduce Scope of Variables).

---

## CI-24: Avoid Shadowing Built-Ins and Package Names

**Strength**: SHOULD-AVOID

**Summary**: Do not name variables `len`, `cap`, `make`, `new`, `copy`, `delete`, `error`, `string`, etc. Do not shadow imported package names.

```go
// Bad
var len int                          // shadows builtin len
error := errors.New("bad")           // shadows builtin error type
for string := range strs { /*...*/ } // shadows builtin string

// Bad — shadows the imported package
import "fmt"
fmt := "plain text"  // now fmt.Println is unavailable

// Good
var length int
err := errors.New("bad")
for s := range strs { /* ... */ }
```

**Rationale**: Shadowing silently disables the built-in or package for the rest of the scope. The error often only surfaces when someone later tries to use the shadowed name. `go vet -shadow` and `predeclared` (staticcheck) catch most cases. Uber §Avoid Using Built-In Names: "The Go language specification describes several built-in... identifiers that should not be used as names within Go programs" (Uber Style Guide §Avoid Using Built-In Names).

---

## CI-25: Use `any` Instead of `interface{}`

**Strength**: SHOULD

**Summary**: Since Go 1.18, `any` is a built-in alias for `interface{}`. Prefer `any` everywhere.

```go
// Good
func log(format string, args ...any) { /* ... */ }
var cache map[string]any

// Bad
func log(format string, args ...interface{}) { /* ... */ }
var cache map[string]interface{}
```

**Rationale**: `any` is shorter, easier to read, and matches modern Go. The tooling and standard library use it uniformly since 1.18. Google Decisions §Use any: "`interface{}` [is] equivalent to and interchangeable with `any`... In general, use `any`" (Google Decisions §Use any).

---

## CI-26: Use `%q` to Quote Strings in Diagnostics

**Strength**: SHOULD

**Summary**: In error messages and logs that include user-provided strings, use `%q` to quote the value. It delimits the string clearly, reveals whitespace, and escapes unprintable characters.

```go
// Good
return fmt.Errorf("unknown field %q in %q", field, source)
// → unknown field "  x" in "config.json"

// Bad
return fmt.Errorf("unknown field %s in %s", field, source)
// → unknown field   x in config.json   (where does one end?)
```

**Rationale**: `%q` produces Go-syntax-quoted output that is unambiguous even when the value contains spaces, newlines, or non-ASCII characters. This prevents operator confusion when debugging. Google Decisions §Use %q: "Go's format verb `%q` wraps its output in double quotes. Prefer this to manually adding quotes around strings" (Google Decisions §Use %q).

---

## CI-27: Use Raw String Literals for Strings with Backslashes or Quotes

**Strength**: SHOULD

**Summary**: Use backtick-delimited raw strings when the content contains backslashes, quotes, or spans multiple lines. Raw strings have no escape interpretation.

```go
// Good
var path = `C:\Users\alice\go`
var re = regexp.MustCompile(`^\d{4}-\d{2}-\d{2}$`)
var query = `
    SELECT id, name
    FROM users
    WHERE active = true
`

// Bad
var path = "C:\\Users\\alice\\go"
var re = regexp.MustCompile("^\\d{4}-\\d{2}-\\d{2}$")
```

**Rationale**: Raw strings eliminate escape-sequence errors, especially in regex and Windows paths. They also allow natural multi-line text without `\n`. Uber §Use Raw String Literals to Avoid Escaping: "Go supports raw string literals, which can span multiple lines and include quotes. Use these to avoid hand-escaped strings which are harder to read" (Uber Style Guide §Use Raw String Literals to Avoid Escaping).

---

## CI-28: Avoid `init()` — Use Explicit Initialization

**Strength**: SHOULD-AVOID

**Summary**: `init()` runs at package import time, before `main`, with no way for callers to control, defer, or fail gracefully. Prefer explicit constructors or `sync.OnceFunc`.

```go
// Good — explicit, testable, fails gracefully
func NewClient(ctx context.Context, cfg Config) (*Client, error) {
    conn, err := dial(ctx, cfg.Addr)
    if err != nil {
        return nil, fmt.Errorf("dial: %w", err)
    }
    return &Client{conn: conn}, nil
}

// Bad — hidden side effect at import time
var defaultClient *Client

func init() {
    conn, err := dial(context.Background(), os.Getenv("ADDR"))
    if err != nil {
        panic(err)  // package consumers have no recourse
    }
    defaultClient = &Client{conn: conn}
}
```

**Rationale**: `init` functions run in undefined order relative to other `init`s, cannot accept arguments or return errors, and complicate testing. Side effects at import time are surprising. Uber §Avoid `init()`: "Avoid `init()` where possible. When `init()` is unavoidable or desirable, code should attempt to..." (be deterministic, avoid globals, avoid I/O) (Uber Style Guide §Avoid init()).

**Exception**: Registering drivers via blank imports (`_ "github.com/lib/pq"`) legitimately uses `init`. This is a deliberate language pattern.

---

## CI-29: Avoid Mutable Global State

**Strength**: SHOULD-AVOID

**Summary**: Avoid package-level variables that are written at runtime. They complicate testing, obscure data flow, and introduce hidden concurrency requirements.

```go
// Good — state lives in a struct with an explicit constructor
type Tracker struct {
    mu     sync.Mutex
    counts map[string]int
}

func NewTracker() *Tracker {
    return &Tracker{counts: make(map[string]int)}
}

func (t *Tracker) Inc(key string) {
    t.mu.Lock()
    defer t.mu.Unlock()
    t.counts[key]++
}

// Bad — package-level mutable state
var counts = map[string]int{}

func Inc(key string) {
    counts[key]++  // not thread-safe, not testable in isolation
}
```

**Rationale**: Global mutable state is implicit: callers of `Inc` cannot tell from the signature that it reads and writes shared state. Two tests cannot run in parallel. Swapping implementations for a test requires package-level patching. Uber §Avoid Mutable Globals: "Avoid mutating global variables, instead opting for dependency injection. This applies to function pointers as well as other kinds of values" (Uber Style Guide §Avoid Mutable Globals).

---

## CI-30: Prefix Unexported Package-Level Globals with `_`

**Strength**: CONSIDER

**Summary**: When you must have unexported package-level `var`s (e.g., compiled regexps, default configs), prefixing with `_` signals "package-global, not a local."

```go
// Good
var (
    _defaultTimeout = 30 * time.Second
    _validName      = regexp.MustCompile(`^[a-z]+$`)
)

func normalize(s string) string {
    if !_validName.MatchString(s) {
        return ""
    }
    return strings.ToLower(s)
}

// Acceptable without _ when the package does not adopt this convention
```

**Rationale**: The `_` prefix immediately distinguishes a package-level binding from a local — at a glance in the function body. This convention is specific to Uber. Uber §Prefix Unexported Globals with _: "Prefix unexported top-level `var`s and `const`s with `_` to make it clear... they are global symbols" (Uber Style Guide §Prefix Unexported Globals with _).

**Note**: Sentinel errors are traditionally `errFoo` (no underscore). Use the `_` convention for other globals.

---

## CI-31: Exit from `main` Only

**Strength**: SHOULD

**Summary**: Call `os.Exit` and `log.Fatal` only from `main` (or from tests via `t.Fatal`). Library code should return errors, not terminate the process.

```go
// Good — library returns errors
func LoadConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, err
    }
    // ...
}

// Good — main decides to exit
func main() {
    cfg, err := LoadConfig("config.json")
    if err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
    run(cfg)
}

// Bad — library terminates the program
func LoadConfig(path string) *Config {
    data, err := os.ReadFile(path)
    if err != nil {
        log.Fatal(err)  // caller has no way to recover
    }
    // ...
}
```

**Rationale**: A library that calls `os.Exit` or `log.Fatal` bypasses deferred cleanup (flushing buffers, closing connections, releasing locks) and makes the library unusable from contexts where termination is wrong (long-running servers, test harnesses). Uber §Exit in Main: "Go programs use `os.Exit` or `log.Fatal*` to exit immediately... Only one of your `main()` functions should call these" (Uber Style Guide §Exit in Main; Google Decisions §Don't panic).

---

## CI-32: Don't Panic in Library Code

**Strength**: MUST-AVOID

**Summary**: Return errors; do not panic. Panic is reserved for truly unrecoverable programmer errors (e.g., violation of internal invariants) and for `main`-level fatal checks that wrap initialization.

```go
// Good
func ParseConfig(b []byte) (*Config, error) {
    var c Config
    if err := json.Unmarshal(b, &c); err != nil {
        return nil, fmt.Errorf("parse config: %w", err)
    }
    return &c, nil
}

// Bad
func ParseConfig(b []byte) *Config {
    var c Config
    if err := json.Unmarshal(b, &c); err != nil {
        panic(err)
    }
    return &c
}
```

**Rationale**: Panics cross goroutine boundaries only via `recover` and terminate the program by default. In library code, they deprive callers of the ability to respond. Google Decisions §Don't panic: "Don't use `panic` for normal error handling. Instead, use `error` and multiple return values." Uber §Don't Panic agrees (Google Decisions §Don't panic; Uber Style Guide §Don't Panic).

**Note**: Package-initialization helpers like `regexp.MustCompile` and `template.Must` panic by design — see CI-33.

**See also**: CI-33

---

## CI-33: Use `Must` Functions Only at Package Initialization

**Strength**: SHOULD

**Summary**: Functions named `MustX` panic on failure and are intended for use as package-level initializers where failure implies a program-wide bug. Never use them in request-path code.

```go
// Good — package-level init
var validEmail = regexp.MustCompile(`^[^@]+@[^@]+$`)

var greetingTmpl = template.Must(template.New("greet").Parse(`Hello, {{.Name}}`))

// Bad — request-path use
func validateEmail(pattern, email string) bool {
    re := regexp.MustCompile(pattern)   // user-supplied pattern can panic the server
    return re.MatchString(email)
}

// Good — recover and return an error in the request path
func validateEmail(pattern, email string) (bool, error) {
    re, err := regexp.Compile(pattern)
    if err != nil {
        return false, err
    }
    return re.MatchString(email), nil
}
```

**Rationale**: `MustX` is appropriate when the input is a constant under the programmer's control — a regex literal, a template literal — so panicking indicates a bug, not a runtime condition. At runtime, use the non-`Must` variant and handle the error. Google Decisions §Must functions: "Must functions... panic if they fail... Such functions are safe to call during program startup, but are generally not good to use as part of the normal program flow" (Google Decisions §Must functions).

**See also**: CI-32

---

## CI-34: Use `defer` for Cleanup, and Put It Near the Acquire

**Strength**: SHOULD

**Summary**: Use `defer` for cleanup (close files, unlock mutexes, release resources). Place the `defer` immediately after the acquire, not at the end of the function.

```go
// Good
f, err := os.Open(path)
if err != nil {
    return err
}
defer f.Close()  // right after open, before anything that can fail

// do work

// Bad — defer buried deep
func process(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    data, err := io.ReadAll(f)
    if err != nil {
        f.Close()  // manual close on error path — easy to miss
        return err
    }
    defer f.Close()  // only reached on the happy path
    return parse(data)
}
```

**Rationale**: `defer` guarantees cleanup even when functions return early from errors or panics. Putting the `defer` right after the acquire makes the invariant visually obvious: this resource is paired with its cleanup. The small overhead of `defer` is negligible except in extremely hot loops. Uber §Defer to Clean Up: "Use defer to clean up resources such as files and locks" (Uber Style Guide §Defer to Clean Up; Effective Go §Defer).

---

## CI-35: Specify Channel Direction in Function Signatures

**Strength**: SHOULD

**Summary**: When a function only sends or only receives on a channel, reflect that in the parameter type (`chan<- T` for send-only, `<-chan T` for receive-only).

```go
// Good — direction in signature documents and restricts use
func producer(out chan<- Job) {
    for i := 0; i < 10; i++ {
        out <- Job{ID: i}
    }
    close(out)
}

func consumer(in <-chan Job) {
    for j := range in {
        process(j)
    }
}

// Bad — bidirectional channel forces reader to check the body
func producer(out chan Job) { /* ... */ }
func consumer(in chan Job)  { /* ... */ }
```

**Rationale**: Directional channel types are self-documenting and let the compiler prevent misuse (the producer can't accidentally receive, and vice versa). Google Decisions §Channel direction: "Specify a channel direction where possible" (Google Decisions §Channel direction; Uber Style Guide §Guidelines).

---

## CI-36: Channel Sizes Are Zero (Unbuffered) or One — Rarely More

**Strength**: CONSIDER

**Summary**: Unbuffered channels (size 0) provide synchronization. A buffer of 1 is useful for signaling without blocking. Larger buffers require careful justification.

```go
// Good — unbuffered: send blocks until receive
done := make(chan struct{})
go func() {
    work()
    close(done)
}()
<-done

// Good — size 1: non-blocking signal
errCh := make(chan error, 1)
go func() { errCh <- doWork() }()

// Suspicious — why 100? Is the producer faster than the consumer by exactly that factor?
jobs := make(chan Job, 100)
```

**Rationale**: Buffered channels with arbitrary sizes (`10`, `100`, `1000`) often indicate the programmer is hoping to avoid blocking rather than designing synchronization. A buffer that's too small still blocks; a buffer that's too large just delays the problem. Uber §Channel Size is One or None: "Channels should usually have a size of one or be unbuffered. By default, channels are unbuffered and have a size of zero. Any other size must be subject to a high level of scrutiny" (Uber Style Guide §Channel Size is One or None).

---

## CI-37: Use `time.Time`, `time.Duration`, and `context` Deadlines

**Strength**: SHOULD

**Summary**: Use the `time` package types for time values and durations. Never use `int` or `int64` for "seconds" or "milliseconds." Pass deadlines via `context.Context`.

```go
// Good
func Fetch(ctx context.Context, url string, timeout time.Duration) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, timeout)
    defer cancel()
    // ...
}

Fetch(ctx, url, 30*time.Second)

// Bad
func Fetch(url string, timeoutSeconds int) ([]byte, error) { /* ... */ }

Fetch(url, 30)           // 30 what? seconds? ms? minutes?
Fetch(url, 30*1000)      // hope you guessed the unit right
```

**Rationale**: `time.Duration` is unit-safe — the compiler ensures `30 * time.Second` and `500 * time.Millisecond` are correct. Integer seconds lose this safety and every call site must agree on the unit. For deadlines and cancellation, `context.Context` is the standard mechanism. Uber §Use time to handle time: "Time is complicated... Represent instants of time as `time.Time` and durations as `time.Duration`" (Uber Style Guide §Use time to handle time).

---

## CI-38: Use Field Tags in Structs Marshaled to JSON/YAML/...

**Strength**: SHOULD

**Summary**: Add struct tags (`json:"name"`, `yaml:"name"`) whenever a struct is marshaled to an external format. Do not rely on field name inference.

```go
// Good
type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email,omitempty"`
}

// Bad — JSON keys default to field names; rename breaks callers silently
type User struct {
    ID    int
    Name  string
    Email string
}
```

**Rationale**: Without tags, refactoring field names silently changes the wire format. Tags make the external contract explicit. Uber §Use Field Tags in Marshaled Structs: "Any struct field that is marshaled into JSON, YAML, or other formats that support tag-based field naming should be annotated with the relevant tag" (Uber Style Guide §Use Field Tags in Marshaled Structs).

---

## CI-39: Hoist Format Strings in `Printf`-Style Wrappers

**Strength**: SHOULD

**Summary**: When you pass a format string to a `Printf`-style function through a variable, declare the variable as `const` so `go vet` can analyze the format/argument relationship.

```go
// Good
const errFmt = "failed to process %s: %w"
return fmt.Errorf(errFmt, name, err)

// Good — literal at call site is fine; vet can still check it
return fmt.Errorf("failed to process %s: %w", name, err)

// Bad — format string built at runtime defeats vet
msg := "failed to process " + "%s" + ": %w"
return fmt.Errorf(msg, name, err)
```

**Rationale**: `go vet` statically checks format strings against their arguments. If the format string is dynamic, vet cannot verify it, and mismatches (wrong verb, wrong count) reach production. Uber §Format Strings outside Printf: "If you declare format strings for Printf-style functions outside a string literal, make them const values" (Uber Style Guide §Format Strings outside Printf).

---

## CI-40: Name Unused Parameters `_` or Document Naked Literals

**Strength**: CONSIDER

**Summary**: When a function must match a signature but doesn't use every parameter, name unused ones `_`. At call sites, annotate naked boolean or numeric literals with a parameter-name comment.

```go
// Good — handler signature requires both; we only use r
func healthz(_ http.ResponseWriter, r *http.Request) {
    log.Printf("healthz from %s", r.RemoteAddr)
}

// Good — label naked booleans at the call site
printInfo("foo", true /* isLocal */)

// Bad — what does true mean here?
printInfo("foo", true)
```

**Rationale**: `_` tells readers (and linters) that a parameter is unused intentionally. For call-site literals, a short comment gives a scan-time hint without requiring a jump to the definition. Uber §Avoid Using Naked Parameters: "Naked parameters in function calls can hurt readability. Add C-style comments (`/* ... */`) for parameter names when their meaning is not obvious" (Uber Style Guide §Avoid Using Naked Parameters).

---

## CI-41: Prefer Conventional Boolean Expressions — No Yoda Conditions

**Strength**: SHOULD

**Summary**: Write conditions in natural order: `if x == 5`, not `if 5 == x`. Go disallows assignment inside `if`, so the C-era motivation for reversed comparisons doesn't exist.

```go
// Good
if x == 5 { /* ... */ }
if name == "alice" { /* ... */ }

// Bad — Yoda style; reads awkwardly, no benefit in Go
if 5 == x { /* ... */ }
if "alice" == name { /* ... */ }
```

**Rationale**: Yoda comparisons exist to guard against `if (x = 5)` assignment bugs in C. Go forbids assignments in conditions, so the style offers no protection and harms readability. Google Decisions §Conditionals and loops: "Go has no requirement (and lint checks should not be added) that the constant come first in a comparison, sometimes known as the 'Yoda condition'" (Google Decisions §Conditionals and loops).

---

## CI-42: Doc Comments Are Full Sentences Starting with the Identifier Name

**Strength**: SHOULD

**Summary**: Every exported identifier needs a doc comment that starts with the identifier's name and is a full English sentence.

```go
// Good
// NewClient returns a Client configured for the given address.
// It returns an error if addr is empty or unreachable.
func NewClient(addr string) (*Client, error) { /* ... */ }

// Good
// MaxRetries is the default number of retry attempts.
const MaxRetries = 3

// Bad — no leading name, not a sentence
// creates a new client
func NewClient(addr string) (*Client, error) { /* ... */ }

// Bad — starts with "This function"
// This function returns a new client.
func NewClient(addr string) (*Client, error) { /* ... */ }
```

**Rationale**: `godoc` and `go doc` render these comments as documentation. Starting with the name makes the output ("NewClient returns...") read naturally and makes `grep` for "`NewClient `" match the doc. Google Decisions §Doc comments: "Every exported (capitalized) name should have a doc comment... The comment should begin with the name of the thing being described and end in a period" (Google Decisions §Doc comments; Effective Go §Commentary).

---

## CI-43: Type Switch Over Repeated Type Assertions

**Strength**: CONSIDER

**Summary**: When dispatching on an interface's dynamic type across several cases, use a single type switch rather than a chain of `v.(T)` assertions.

```go
// Good — single dispatch
switch v := v.(type) {
case string: return v
case int:    return strconv.Itoa(v)
}

// Bad — evaluates interface multiple times
if s, ok := v.(string); ok { return s }
if i, ok := v.(int); ok { return strconv.Itoa(i) }
```

**Rationale**: A type switch resolves the dynamic type exactly once and dispatches directly to the matching case. A chain of comma-ok assertions forces the runtime down the slower type-check path once per branch, which adds up inside hot loops. Prefer the switch when three or more types are under consideration (paraphrased from cc-skills-golang/skills/golang-performance/references/cpu.md).

---

## CI-44: Modern slog Logging over Legacy log.Printf

**Strength**: SHOULD

**Summary**: Reach for `log/slog` (Go 1.21+) with structured key-value pairs instead of printf-style `log.Printf`, and wire a `slog.LevelVar` so the level can change at runtime.

```go
// Good — structured logging with slog
logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
slog.SetDefault(logger)
slog.Info("user logged in", "user_id", userID, "ip", ip)

// Good — dynamic level control at runtime
var programLevel = new(slog.LevelVar)
logger = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
    Level: programLevel,
}))
slog.SetDefault(logger)

func enableDebug() {
    programLevel.Set(slog.LevelDebug) // flip without restarting
}

// Bad — printf-style, unstructured
log.Printf("user %s logged in from %s", userID, ip)
```

**Rationale**: Structured attributes are machine-parseable, grep-friendly, and survive round-trips through log aggregators, whereas interpolated strings have to be re-parsed downstream. A shared `slog.LevelVar` lets an admin endpoint or signal handler raise verbosity in production without a redeploy. `log/slog` is standard library in Go 1.21+, so there is no dependency cost for adopting it (paraphrased from golang-skills (cxuu)/skills/go-logging/references/LOGGING-PATTERNS.md).

---

## CI-45: Deterministic Map Iteration via Sorted Keys

**Strength**: SHOULD

**Summary**: When iteration order matters (tests, diffable output, deterministic hashes), collect keys with `slices.Sorted(maps.Keys(m))` instead of ranging over the map directly.

```go
// Good — sort keys if order matters
m := map[string]int{"z": 1, "a": 2, "m": 3}
keys := slices.Sorted(maps.Keys(m))
var results []int
for _, k := range keys {
    results = append(results, m[k]) // consistent order
}

// Bad — assumes iteration order
m := map[string]int{"z": 1, "a": 2, "m": 3}
var results []int
for k, v := range m {
    _ = k
    results = append(results, v) // order varies between runs
}
```

**Rationale**: Go deliberately randomizes map iteration to prevent callers from depending on any particular order. The Go 1.22+ combination of `maps.Keys` (returning an iterator) and `slices.Sorted` (collecting an iterator into a sorted slice) expresses "iterate in sorted order" in one line with no manual `sort.Strings` step. Reach for it whenever your output is compared, hashed, or read by humans (paraphrased from claude-skills (saisudhir14)/references/gotchas.md).

---

## CI-46: Per-Iteration Cleanup via Anonymous Function in Loops

**Strength**: SHOULD

**Summary**: `defer` runs at function return, not at loop-iteration end. Wrap the loop body in an immediately-invoked anonymous function when a resource must be released on each pass.

```go
// Good — anonymous function closes per iteration
for _, name := range files {
    func() {
        f, err := os.Open(name)
        if err != nil {
            return
        }
        defer f.Close() // runs at end of each iteration
        process(f)
    }()
}

// Bad — defer delays cleanup until all files processed
for _, name := range files {
    f, err := os.Open(name)
    if err != nil {
        continue
    }
    defer f.Close() // doesn't run until loop exits!
    process(f)      // may process many files with handles open
}
```

**Rationale**: A naked `defer` inside a loop accumulates on the function's defer stack, so file handles, locks, or transactions pile up until the enclosing function returns — a common source of "too many open files" and lock-contention bugs. Wrapping the body in `func() { ... }()` gives each iteration its own function scope, so the `defer` fires promptly. The cost is a single extra closure call per iteration, which is negligible next to the I/O being guarded (paraphrased from claude-skills (saisudhir14)/references/gotchas.md).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `:=` for init, `var` for zero | SHOULD | Signal intent: initialized vs starting-at-zero |
| 02 | Top-level `var` without type | SHOULD | Type is redundant with initializer |
| 03 | Group similar declarations | SHOULD | One parenthesized block per concern |
| 04 | Imports: stdlib, then rest | SHOULD | Two groups separated by blank line |
| 05 | Short, lowercase package names | MUST | Single word, no underscores, no camelCase |
| 06 | Avoid `util`/`common`/`helpers` | SHOULD-AVOID | Name by purpose, not by role |
| 07 | MixedCaps, not `snake_case` | MUST | Underscores are not Go |
| 08 | Consistent initialism case | SHOULD | `URL` or `url`, never `Url` |
| 09 | Short, consistent receiver names | SHOULD | 1-2 letters, same across methods |
| 10 | No `Get` prefix on getters | SHOULD-AVOID | `User.Name()` not `User.GetName()` |
| 11 | Use zero values | SHOULD | Design types so zero is useful |
| 12 | `nil` slices are valid | SHOULD | Use `len(s) == 0`, not `s == nil` |
| 13 | `make` for empty maps | SHOULD | Literals only for initial entries |
| 14 | Named struct fields | SHOULD | Survives refactors |
| 15 | Omit zero-value fields | SHOULD | Focus on fields that matter |
| 16 | `&T{}` over `new(T)` | SHOULD | Allows field init in one step |
| 17 | `var x T` for zero struct | SHOULD | `var` signals "start at zero" |
| 18 | `iota` enums; skip zero often | SHOULD | Avoid silent default state |
| 19 | Comma-ok idiom | MUST | Single-form assertion panics |
| 20 | Don't ignore errors | MUST | `_` only with comment |
| 21 | Indent errors; left-align success | SHOULD | Happy path on the left margin |
| 22 | No unnecessary `else` | SHOULD | Return, break, continue, panic |
| 23 | Narrow variable scope | SHOULD | Declare in the `if`/`for` initializer |
| 24 | Don't shadow built-ins | SHOULD-AVOID | `len`, `error`, `string`, etc. |
| 25 | `any` over `interface{}` | SHOULD | Since Go 1.18 |
| 26 | `%q` in diagnostics | SHOULD | Delimits and escapes cleanly |
| 27 | Raw string literals | SHOULD | No hand-escaping backslashes |
| 28 | Avoid `init()` | SHOULD-AVOID | Hidden side effects at import |
| 29 | Avoid mutable globals | SHOULD-AVOID | Use dependency injection |
| 30 | `_` prefix for package globals | CONSIDER | Uber convention, optional |
| 31 | Exit from `main` only | SHOULD | Libraries return errors |
| 32 | Don't panic in libraries | MUST-AVOID | Return errors instead |
| 33 | `Must` only at init | SHOULD | Never in request path |
| 34 | `defer` near acquire | SHOULD | Guaranteed cleanup |
| 35 | Channel direction in signatures | SHOULD | `chan<- T`, `<-chan T` |
| 36 | Channel size 0 or 1 | CONSIDER | Arbitrary buffers are suspect |
| 37 | `time.Time`/`time.Duration` | SHOULD | Unit-safe, typed |
| 38 | Struct tags for marshaling | SHOULD | Lock the wire format |
| 39 | Format strings as `const` | SHOULD | Preserve vet analysis |
| 40 | Name unused params `_` | CONSIDER | Or comment naked literals |
| 41 | No Yoda conditions | SHOULD | Go forbids assignment in `if` |
| 42 | Doc comments: full sentences | SHOULD | Start with the identifier name |
| 43 | Type switch over repeated `.(T)` | CONSIDER | One dispatch vs N assertions |
| 44 | `slog` over legacy `log.Printf` | SHOULD | Structured, dynamic levels |
| 45 | Sort keys for stable map iteration | SHOULD | Iteration order is randomized |
| 46 | Anon-func wrapper for per-iter defer | SHOULD | `defer` runs at function return |

---

## Related Guidelines

- **API Design**: See `02-api-design.md` for constructor patterns, functional options, and parameter structs (extends CI-16, CI-17)
- **Error Handling**: See `03-error-handling.md` for wrapping, sentinel errors, `errors.Is`/`errors.As`, and custom error types (extends CI-20, CI-21)
- **Type Design**: See `04-type-design.md` for struct embedding, type aliases, and type definitions (extends CI-11, CI-14)
- **Interfaces & Methods**: See `05-interfaces-methods.md` for interface-satisfaction patterns and accept-interfaces-return-concrete (extends CI-09, CI-10)
- **Concurrency**: See `06-concurrency.md` for goroutine lifetimes, `sync` primitives, and `context` propagation (extends CI-34, CI-35, CI-36, CI-37)
- **Testing**: See `07-testing.md` for table-driven tests and parallel test patterns
- **Anti-Patterns**: See `09-anti-patterns.md` for patterns that amplify CI-22, CI-24, CI-28, CI-29, CI-32

---

## External References

- [*Effective Go*](https://go.dev/doc/effective_go) — the Go team's foundational idiom guide
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — community-standard style reference
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Style Guide, Decisions, Best Practices
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — the Go team's canonical review checklist
- [Go Proverbs](https://go-proverbs.github.io/) — Rob Pike's distilled wisdom
- [`gofmt`](https://pkg.go.dev/cmd/gofmt), [`go vet`](https://pkg.go.dev/cmd/vet), [`staticcheck`](https://staticcheck.dev/) — enforce most of these idioms automatically
