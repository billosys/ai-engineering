# Error Handling

Idioms for producing, propagating, classifying, and inspecting Go errors. Go's `error` is an interface value, not an exception — every failure travels as an ordinary return value, and how it is constructed, wrapped, and examined decides how useful it will be in logs and in recovery logic. These rules are grounded in the *Uber Go Style Guide* (§Errors, §Don't Panic) and the *Google Go Style Guide* (Decisions §Errors, Best Practices §Error handling, §When to panic, §Must functions).

Target environment: **Go 1.20+** (for `errors.Join` and `%w` with multiple wrappees), **standard library `errors` and `fmt` packages**, **`errcheck` + `go vet` + `staticcheck`**.

This chapter extends **CI-20** (don't ignore errors) and **CI-21** (indent the error path) from chapter 01. It does not cover `errgroup` and goroutine error fan-out (see chapter 06) or asserting on errors in tests (see chapter 07).

---

## EH-01: Use `error` as the Failure Signal — Not Booleans, Not Sentinels In-Band

**Strength**: MUST

**Summary**: Declare failure with an `error` return. `nil` means success; a non-nil error means the other return values are unspecified unless documented otherwise. Do not smuggle failure into in-band values like `-1`, `""`, or `nil` pointers.

```go
// Good
func Lookup(key string) (string, error) {
    v, ok := cache[key]
    if !ok {
        return "", fmt.Errorf("lookup %q: not found", key)
    }
    return v, nil
}

// Good — when the only failure is "missing", a bool is fine
func Lookup(key string) (value string, ok bool)

// Bad — in-band sentinel in a normal-looking return
// Lookup returns the value for key or -1 if there is no mapping for key.
func Lookup(key string) int
```

**Rationale**: Go's multi-return makes error signaling explicit. In-band sentinels (`-1`, empty string) let callers accidentally chain `Parse(Lookup(k))` and attribute the failure to the wrong function. Google Decisions §Returning errors: "Use `error` to signal that a function can fail. By convention, `error` is the last result parameter." Google Decisions §In-band errors: "a function should return an additional value to indicate whether its other return values are valid" (Google Decisions §Returning errors; §In-band errors).

**See also**: EH-02, CI-20

---

## EH-02: Return the `error` Interface, Not a Concrete Pointer Type

**Strength**: MUST

**Summary**: Exported functions that can fail return the `error` interface. Do not return `*MyError` directly — a typed nil pointer wrapped in an interface is a non-nil error value, and that trap has bitten every Go programmer at least once.

```go
// Good
func Chdir(dir string) error { /* ... */ }

// Good — document the concrete dynamic type for callers who want errors.As
// If there is an error, it will be of type *PathError.
func Chdir(dir string) error { /* ... */ }

// Bad — typed-nil hazard
func Bad() *os.PathError { /* ... */ }

// Why this hurts:
func caller() {
    var perr *os.PathError // nil
    err := error(perr)     // non-nil interface wrapping a nil pointer
    if err != nil {        // TRUE — surprise
        // treats a successful call as a failure
    }
}
```

**Rationale**: An `error` value is nil only when both its dynamic type and dynamic value are nil. Returning a concrete pointer type forces all success paths to explicitly return a literal `nil` and creates a subtle trap for callers who compare against `nil`. Google Decisions §Returning errors: "Exported functions that return errors should return them using the `error` type. Concrete error types are susceptible to subtle bugs: a concrete `nil` pointer can get wrapped into an interface and thus become a non-nil value." Google Documentation Conventions §Errors notes that the docstring should still name the concrete type (`"If there is an error, it will be of type *PathError"`) so callers can use `errors.As` (Google Decisions §Returning errors; Best Practices §Errors/Documentation Conventions).

**See also**: EH-14, EH-18

---

## EH-03: Pick the Error Construction That Matches the Contract

**Strength**: SHOULD

**Summary**: Four cases, four constructors — decide whether callers need to match the error (`errors.Is`/`errors.As`) and whether the message is static or dynamic.

| Callers match? | Message  | Construct with                                           |
|----------------|----------|----------------------------------------------------------|
| No             | static   | `errors.New("...")` inline                               |
| No             | dynamic  | `fmt.Errorf("... %v", ...)`                              |
| Yes            | static   | top-level `var ErrX = errors.New("...")`                 |
| Yes            | dynamic  | custom `error` type (struct implementing `Error() string`) |

```go
// Static, no matching — inline errors.New
func validate(n int) error {
    if n < 0 {
        return errors.New("negative value")
    }
    return nil
}

// Dynamic, no matching — fmt.Errorf
func Open(file string) error {
    return fmt.Errorf("file %q not found", file)
}

// Static, matching — exported sentinel
var ErrCouldNotOpen = errors.New("could not open")

func Open() error { return ErrCouldNotOpen }

// Dynamic, matching — custom type
type NotFoundError struct{ File string }

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("file %q not found", e.File)
}

func Open(file string) error { return &NotFoundError{File: file} }
```

**Rationale**: Sentinels and custom types become part of the public API: exporting them is a commitment. Picking the weakest constructor that meets the contract keeps that surface area small. Uber §Error Types: "There are few options for declaring errors. Consider the following before picking the option best suited for your use case." (Uber §Error Types).

**See also**: EH-04, EH-05, EH-07

---

## EH-04: Use `errors.New` for Static Messages, `fmt.Errorf` for Dynamic

**Strength**: SHOULD

**Summary**: `errors.New` is the cheapest and clearest constructor for a fixed string. Reach for `fmt.Errorf` only when you need to interpolate values or wrap another error.

```go
// Good
return errors.New("empty input")
return fmt.Errorf("parse header at offset %d: %w", off, err)

// Bad — fmt.Errorf with no formatting directives
return fmt.Errorf("empty input")       // errors.New is enough

// Bad — errors.New with a format string that never gets formatted
return errors.New(fmt.Sprintf("offset %d", off))  // just use fmt.Errorf
```

**Rationale**: `fmt.Errorf` allocates a formatter and a string builder even when there are no verbs; `errors.New` stores the string directly. More importantly, the choice signals intent: `errors.New` says "this message is a constant," `fmt.Errorf` says "this message carries runtime data." Uber §Error Types enumerates the same split (Uber §Error Types).

---

## EH-05: Declare Sentinel Errors as Package-Level `var` — Not `const`

**Strength**: MUST

**Summary**: Sentinel errors live at package scope as `var`. `const` cannot hold an `error` value because `error` is an interface. Group them in a `var (...)` block.

```go
// Good
var (
    // ErrBrokenLink is returned when a link target is missing.
    ErrBrokenLink = errors.New("link is broken")

    // ErrCouldNotOpen is returned when the underlying resource cannot be opened.
    ErrCouldNotOpen = errors.New("could not open")
)

// Bad — doesn't compile; const can only hold a basic value
const ErrBrokenLink = errors.New("link is broken")

// Bad — one declaration per line when they're clearly related
var ErrBrokenLink = errors.New("link is broken")
var ErrCouldNotOpen = errors.New("could not open")
```

**Rationale**: Grouping makes the "these are the errors this package exposes" surface obvious at a glance. Uber §Error Naming shows the grouped-`var` pattern (Uber §Error Naming; Uber §Group Similar Declarations; referenced from CI-03).

**See also**: EH-06, CI-03

---

## EH-06: Name Sentinels `Err*` (Exported) or `err*` (Unexported)

**Strength**: MUST

**Summary**: Sentinel error values use the prefix `Err` when exported and `err` when unexported. This overrides the `_` prefix convention for package-level globals (CI-30).

```go
// Good
var (
    ErrNotFound   = errors.New("not found")   // exported — part of the API
    ErrBadRequest = errors.New("bad request")

    errTimeout  = errors.New("timeout")       // unexported — internal use
    errShutdown = errors.New("shutdown")
)

// Bad — unclear this is an error
var NotFoundError = errors.New("not found")   // suffix looks like a type

// Bad — underscore prefix conflicts with Err/err convention
var _errTimeout = errors.New("timeout")
```

**Rationale**: The `Err` prefix is a strong community convention — readers scanning a package see at a glance which identifiers are error sentinels. Uber §Error Naming: "For error values stored as global variables, use the prefix `Err` or `err` depending on whether they're exported. This guidance supersedes the Prefix Unexported Globals with `_`" (Uber §Error Naming).

**See also**: EH-07, CI-30

---

## EH-07: Name Custom Error Types with the `Error` Suffix

**Strength**: SHOULD

**Summary**: A custom struct implementing `error` uses the suffix `Error`: exported types get `NotFoundError`, unexported ones get `resolveError`.

```go
// Good — exported type for callers matching with errors.As
type NotFoundError struct {
    File string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("file %q not found", e.File)
}

// Good — unexported type for internal matching
type resolveError struct {
    Path string
}

func (e *resolveError) Error() string {
    return fmt.Sprintf("resolve %q", e.Path)
}

// Bad — prefix-named types blur with sentinel values
type ErrNotFound struct{ File string }   // Err prefix is for vars
```

**Rationale**: The two prefixes/suffixes together make error classification self-documenting: `Err*` means "a concrete value you can compare with `==` or `errors.Is`," `*Error` means "a type you can extract with `errors.As`." Uber §Error Naming: "For custom error types, use the suffix `Error` instead" (Uber §Error Naming).

**See also**: EH-06, EH-17

---

## EH-08: Use Pointer Receivers for Error Types That Carry Fields

**Strength**: SHOULD

**Summary**: Implement `Error() string` on `*T`, not `T`, when the type carries data. Return `&T{...}`, not `T{...}`. Document the pointer-ness so callers know what to pass to `errors.As`.

```go
// Good — pointer receiver, pointer construction, documented
type NotFoundError struct {
    File string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("file %q not found", e.File)
}

// Open reports missing files with *NotFoundError.
func Open(file string) error {
    return &NotFoundError{File: file}
}

// Caller
var nf *NotFoundError
if errors.As(err, &nf) {
    log.Printf("missing: %s", nf.File)
}

// Bad — value receiver forces a copy into each call and complicates errors.As
func (e NotFoundError) Error() string { /* ... */ }
```

**Rationale**: Pointer receivers avoid copying the error each time `Error()` is called (which happens often, e.g., in logging middleware). They also make `errors.As` unambiguous: callers pass `&var` where `var` is `*NotFoundError`. Google Best Practices §Errors: "When a function returns a specific error type, correctly note whether the error is a pointer receiver or not... Documenting whether the values returned are pointer receivers enables callers to correctly compare the errors using `errors.Is`, `errors.As`, and `package cmp`" (Google Best Practices §Errors/Documentation Conventions).

**See also**: EH-02, EH-18

---

## EH-09: Error Strings Start Lowercase and End Without Punctuation

**Strength**: MUST

**Summary**: The string passed to `errors.New` or `fmt.Errorf` should be a lowercase phrase, with no trailing period, question mark, or exclamation. Exceptions: proper nouns, acronyms, and identifiers that legitimately start with a capital.

```go
// Good
return errors.New("connection refused")
return fmt.Errorf("parse %q: %w", path, err)
return errors.New("HTTP 500")          // proper acronym

// Bad
return errors.New("Connection refused.")   // capitalized + trailing period
return errors.New("Something bad happened!")
```

**Rationale**: Error strings are almost always embedded in other messages (`"load: parse: connection refused"`). A capital letter mid-sentence and trailing punctuation look wrong once the error has been wrapped a few times. The top-level, human-facing presentation (log line, test failure, UI banner) is where capitalization happens — not at the error site. Google Decisions §Error strings: "Error strings should not be capitalized (unless beginning with an exported name, a proper noun or an acronym) and should not end with punctuation. This is because error strings usually appear within other context before being printed to the user" (Google Decisions §Error strings).

**See also**: EH-10

---

## EH-10: Don't Say "Failed to" — The `error` Return Already Means Failure

**Strength**: SHOULD

**Summary**: Skip phrases like "failed to", "error while", and "could not" in wrap messages. The presence of an error already signals failure; repeating it at every layer pollutes the final message.

```go
// Good — terse, stacks cleanly
return fmt.Errorf("new store: %w", err)
return fmt.Errorf("load config %q: %w", path, err)

// Bad — "failed to" at every layer
return fmt.Errorf("failed to create new store: %w", err)
// Final message after three layers of wrapping:
//   failed to x: failed to y: failed to create new store: the error
```

**Rationale**: Wrapped errors print left-to-right from outermost to innermost. A four-layer call stack that each says "failed to" produces `"failed to x: failed to y: failed to create new store: the error"`. Drop the verb and the result is `"x: y: new store: the error"` — same information, quarter the noise. Uber §Error Wrapping: "When adding context to returned errors, keep the context succinct by avoiding phrases like 'failed to', which state the obvious and pile up as the error percolates up through the stack" (Uber §Error Wrapping). Google Best Practices §Adding information to errors: "Don't add an annotation if its sole purpose is to indicate a failure without adding new information" (Google Best Practices §Adding information to errors).

---

## EH-11: Don't Duplicate Information the Wrapped Error Already Contains

**Strength**: SHOULD

**Summary**: Before adding context to a wrapped error, check what the underlying error already reports. `os` errors already include the file path; `net` errors include addresses; repeating that data bloats the message.

```go
// Good — adds meaning the os.Open error doesn't carry
if err := os.Open("settings.txt"); err != nil {
    return fmt.Errorf("launch codes unavailable: %w", err)
}
// → launch codes unavailable: open settings.txt: no such file or directory

// Bad — duplicates the filename os.Open already reports
if err := os.Open("settings.txt"); err != nil {
    return fmt.Errorf("could not open settings.txt: %w", err)
}
// → could not open settings.txt: open settings.txt: no such file or directory
```

**Rationale**: Each layer of wrapping should add *new* context: the operation this function was trying to perform, the domain object in play, the retry number. Repeating the filename that `*os.PathError` already formats adds clutter without insight. Google Best Practices §Adding information to errors: "When adding information to errors, avoid redundant information that the underlying error already provides" (Google Best Practices §Adding information to errors).

**See also**: EH-10

---

## EH-12: Wrap with `%w` When Callers Should Be Able to Inspect the Cause

**Strength**: SHOULD

**Summary**: In `fmt.Errorf`, use `%w` to embed an error so that `errors.Is` and `errors.As` can walk the chain. Use `%v` when you intentionally want to hide the cause.

```go
// Good — caller can errors.Is(err, fs.ErrNotExist)
func (s *Server) loadBlob(id string) error {
    b, err := s.fs.Open(id)
    if err != nil {
        return fmt.Errorf("load blob %q: %w", id, err)
    }
    _ = b
    return nil
}

// Good — hiding internals at an RPC boundary
func (*FortuneTeller) Suggest(ctx context.Context, _ *pb.Req) (*pb.Resp, error) {
    fortunes, err := db.Load(ctx)
    if err != nil {
        // Callers outside our domain shouldn't inspect db errors directly.
        return nil, fmt.Errorf("couldn't find fortune database: %v", err)
    }
    _ = fortunes
    return nil, nil
}

// Bad — %s throws away error value and prevents unwrapping
return fmt.Errorf("load blob %q: %s", id, err)
```

**Rationale**: `%w` is the only verb that preserves the error chain for programmatic inspection. `%v` and `%s` interpolate the error's string and drop the value. A good default is `%w` inside a module; `%v` at the public boundary where you do not want to commit to exposing implementation errors. Google Best Practices §Adding information to errors: "`%w` (wrap) for programmatic inspection and error chaining... This is the primary use case within helpers of your application." Uber §Error Wrapping: "Use `%w` if the caller should have access to the underlying error. This is a good default for most wrapped errors... Use `%v` to obfuscate the underlying error" (Google Best Practices §Adding information to errors; Uber §Error Wrapping).

**See also**: EH-13, EH-15, EH-16

---

## EH-13: Place `%w` at the End of the Format String

**Strength**: SHOULD

**Summary**: Put `%w` after the context, not before it. The resulting message reads outermost-to-innermost, matching the chain direction that `errors.Unwrap` walks.

```go
// Good — "[...]: %w" prints outer-to-inner
err1 := errors.New("err1")
err2 := fmt.Errorf("err2: %w", err1)
err3 := fmt.Errorf("err3: %w", err2)
fmt.Println(err3)
// err3: err2: err1

// Bad — "%w: [...]" prints inner-to-outer, confusing the reader
err2 := fmt.Errorf("%w: err2", err1)
err3 := fmt.Errorf("%w: err3", err2)
fmt.Println(err3)
// err1: err2: err3   (reads like a chain going the wrong direction)

// Bad — %w in the middle produces scrambled order
err2 := fmt.Errorf("err2-a %w err2-b", err1)
err3 := fmt.Errorf("err3-a %w err3-b", err2)
// err3-a err2-a err1 err2-b err3-b
```

**Rationale**: Wherever `%w` sits, the new error still wraps the argument — but the printed string reflects the literal format order. Putting `%w` last matches the natural reading direction (outer context first, inner cause last) and mirrors how `errors.Unwrap` traverses. Google Best Practices §Placement of %w: "in order for error text to mirror error chain structure, prefer placing the `%w` verb at the end with the form `[...]: %w`" (Google Best Practices §Placement of %w in errors).

**See also**: EH-14

---

## EH-14: Put `%w` at the Start When Wrapping a Sentinel Category

**Strength**: SHOULD

**Summary**: The one exception to EH-13: when the wrapped error is itself a categorical sentinel (e.g., `ErrParse`, `ErrInternal`), leading with `%w` makes the category obvious on the first token.

```go
// Good — sentinel leads, specifics follow
package parser

var ErrParse = errors.New("parse error")

var ErrInvalidHeader = fmt.Errorf("%w: invalid header", ErrParse)

func parseHeader(b []byte) error {
    if err := checkMagic(b); err != nil {
        return fmt.Errorf("%w: invalid magic: %v", ErrInvalidHeader, err)
    }
    return nil
}
// Prints: parse error: invalid header: invalid magic: ...

// Bad — category buried at the end
return fmt.Errorf("invalid magic: %v: %w", err, ErrInvalidHeader)
// Prints: invalid magic: <inner>: parse error: invalid header
```

**Rationale**: Operators and log analysts frequently scan just the start of an error message to categorize. Putting the sentinel first immediately communicates "this is a parse error" or "this is an internal error" without reading through mechanical detail. Google Best Practices §Sentinel error placement: "when wrapping sentinel errors... placing the `%w` verb at the beginning of the error string can improve readability by immediately identifying the category of the error" (Google Best Practices §Sentinel error placement).

**See also**: EH-13

---

## EH-15: Match Sentinel Errors with `errors.Is`, Not `==`

**Strength**: SHOULD

**Summary**: Once you wrap an error with `%w`, a plain `==` comparison no longer matches the sentinel — the wrapper is a different value. Use `errors.Is(err, target)` to walk the chain.

```go
// Good
if errors.Is(err, ErrUserNotFound) {
    tz = time.UTC // recover with a default
} else if err != nil {
    return fmt.Errorf("get user %q: %w", id, err)
}

// Acceptable — only if you know no wrapping has happened
switch err := process(an); err {
case ErrDuplicate:
    return fmt.Errorf("feed %q: %v", an, err)
case ErrMarsupial:
    // ...
}

// Bad — after wrapping, == returns false even when the chain contains the target
if err == ErrUserNotFound { /* never true */ }
```

**Rationale**: `errors.Is` walks the `Unwrap() error` chain so it works through any number of `%w` wrappers. `==` only compares the immediate interface value. Once any layer wraps the sentinel, `==` stops working. Google Best Practices §Error structure: "If `process` returns wrapped errors (discussed below), you can use `errors.Is`." Uber §Error Types: "declaring a top-level error variable... to handle it with `errors.Is`" (Google Best Practices §Error structure; Uber §Error Types).

**See also**: EH-12, EH-16

---

## EH-16: Extract Custom Error Types with `errors.As`

**Strength**: SHOULD

**Summary**: When a caller needs the data inside a custom error (e.g., the file name, the syntax position), use `errors.As` to assign the first matching error in the chain into a typed variable.

```go
// Good
var notFound *NotFoundError
if errors.As(err, &notFound) {
    log.Printf("missing file: %s", notFound.File)
    // fall through to recovery
}

// Good — distinguish multiple types
switch {
case errors.Is(err, ErrUserNotFound):
    return defaultUser, nil
case errors.As(err, new(*ValidationError)):
    return nil, err  // let the HTTP layer translate to 400
default:
    return nil, fmt.Errorf("handle request: %w", err)
}

// Bad — manual type assertion bypasses unwrap
if nf, ok := err.(*NotFoundError); ok { /* misses wrapped errors */ }
```

**Rationale**: Like `errors.Is`, `errors.As` walks the unwrap chain. A direct type assertion (`err.(*NotFoundError)`) only sees the outermost error and will fail the moment any caller wraps with `%w`. Pass a pointer to a variable of the target pointer type — `errors.As` populates it. Uber §Error Types: "if errors.As(err, &notFound) { // handle the error }" (Uber §Error Types; Google Best Practices §Error structure).

**See also**: EH-15

---

## EH-17: Don't Match Errors by String Substring

**Strength**: MUST-AVOID

**Summary**: Never branch on `strings.Contains(err.Error(), "not found")` or the equivalent regex. It ties your control flow to the human-readable message, which is allowed to change at any time.

```go
// Good
if errors.Is(err, ErrNotFound) {
    return defaultValue, nil
}

// Bad — breaks the moment the upstream message is rephrased
if strings.Contains(err.Error(), "not found") {
    return defaultValue, nil
}
if regexp.MustCompile(`duplicate`).MatchString(err.Error()) { /* ... */ }
```

**Rationale**: Error strings are part of the *human* contract, not the *machine* contract. Google Best Practices §Error structure: "Do not attempt to distinguish errors based on their string form." If the dependency doesn't expose a structured error, the right response is to ask the upstream to add one, not to pattern-match a message (Google Best Practices §Error structure).

**See also**: EH-15, EH-16

---

## EH-18: Document the Errors a Function Can Return

**Strength**: SHOULD

**Summary**: If a function returns specific sentinel errors or a specific concrete error type, say so in the doc comment. Without that, callers cannot write sound `errors.Is` or `errors.As` checks.

```go
// Good
// Read reads up to len(b) bytes from the File and stores them in b. It returns
// the number of bytes read and any error encountered.
//
// At end of file, Read returns 0, io.EOF.
func (*File) Read(b []byte) (n int, err error) { /* ... */ }

// Good — naming the concrete type makes errors.As usable
// Chdir changes the current working directory to the named directory.
//
// If there is an error, it will be of type *PathError.
func Chdir(dir string) error { /* ... */ }

// Bad — caller has no idea what to match against
// Chdir changes the current working directory.
func Chdir(dir string) error { /* ... */ }
```

**Rationale**: The error's dynamic type and the set of sentinels returned are part of the function's contract. Callers who must distinguish "not found" from "permission denied" cannot do so without documentation. Google Best Practices §Errors: "Document significant error sentinel values or error types that your functions return to callers so that callers can anticipate what types of conditions they can handle in their code" (Google Best Practices §Errors/Documentation Conventions).

---

## EH-19: Handle Each Error Exactly Once

**Strength**: MUST

**Summary**: When you receive an error, pick one response: handle it, log it and recover, translate and return, or wrap and return. Do not both log and return — the caller will do something with it too, and the log line just adds noise.

```go
// Bad — duplicates the log at every layer
u, err := getUser(id)
if err != nil {
    log.Printf("Could not get user %q: %v", id, err)
    return err
}

// Good — wrap and return; one handler logs at the top
u, err := getUser(id)
if err != nil {
    return fmt.Errorf("get user %q: %w", id, err)
}

// Good — match-and-recover for a known case, wrap-and-return otherwise
tz, err := getUserTimeZone(id)
if err != nil {
    if errors.Is(err, ErrUserNotFound) {
        tz = time.UTC
    } else {
        return fmt.Errorf("get user tz %q: %w", id, err)
    }
}

// Good — log-and-drop when the call is purely advisory
if err := emitMetrics(); err != nil {
    // Failure to write metrics must not break the operation.
    log.Printf("emit metrics: %v", err)
}
```

**Rationale**: Logging an error and returning it means the same failure shows up in logs N times, once per stack frame. Callers who see an error have enough context to decide whether to log, ignore, or translate — they don't need your log line too. Uber §Handle Errors Once: "Regardless of how the caller handles the error, it should typically handle each error only once. The caller should not, for example, log the error and then return it, because *its* callers may handle the error as well" (Uber §Handle Errors Once). Google Best Practices §Logging errors: "If you return an error, it's usually better not to log it yourself but rather let the caller handle it... giving the caller control helps avoid logspam" (Google Best Practices §Logging errors).

**See also**: EH-20, EH-21

---

## EH-20: Translate Errors at Package Boundaries

**Strength**: SHOULD

**Summary**: At a public API surface, decide what errors callers may see. Wrap internal errors into a domain error — either by wrapping a sentinel with `%w` or by translating into a canonical code (e.g., gRPC `status`). Don't leak implementation errors across boundaries you don't want to commit to.

```go
// Good — translate internal fs error into a domain error
func (s *Store) Load(ctx context.Context, id string) (*Blob, error) {
    b, err := s.fs.Open(s.keyFor(id))
    if err != nil {
        if errors.Is(err, fs.ErrNotExist) {
            return nil, fmt.Errorf("%w: %s", ErrBlobNotFound, id)
        }
        return nil, fmt.Errorf("open blob %q: %w", id, err)
    }
    _ = b
    return nil, nil
}

// Good — at an RPC boundary, translate to canonical code and hide internals
func (*Server) Suggest(ctx context.Context, _ *pb.Req) (*pb.Resp, error) {
    result, err := compute()
    if err != nil {
        // %v, not %w — callers outside our domain don't inspect the internal error.
        return nil, status.Errorf(codes.Internal, "couldn't compute suggestion: %v", err)
    }
    _ = result
    return nil, nil
}

// Bad — leaks fs.ErrNotExist up through four packages' worth of public API
return s.fs.Open(s.keyFor(id))
```

**Rationale**: Once an error is part of your public API, either explicitly via `errors.Is`/`errors.As` or implicitly via its string form, you are stuck with it. At the boundary where your package meets the outside world, translate into errors that match your contract. Google Best Practices §Adding information to errors: "At points where your system interacts with external systems like RPC, IPC, or storage, it's often better to translate domain-specific errors into a standardized error space" (Google Best Practices §Adding information to errors; Uber §Error Wrapping).

**See also**: EH-12

---

## EH-21: Add Context That Narrows the Failure — Not the Whole World

**Strength**: SHOULD

**Summary**: The wrap message should name *this* function's operation, not repeat what happened below or speculate about what's happening above. One wrap per layer, one verb per layer.

```go
// Good — each layer adds its own operation
func loadAndValidate(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("read %q: %w", path, err)
    }
    cfg, err := parse(data)
    if err != nil {
        return nil, fmt.Errorf("parse %q: %w", path, err)
    }
    if err := validate(cfg); err != nil {
        return nil, fmt.Errorf("validate %q: %w", path, err)
    }
    return cfg, nil
}

// Bad — vague blanket context doesn't help diagnose which step failed
return nil, fmt.Errorf("load failed: %w", err)

// Bad — speculating about the caller's use case
return nil, fmt.Errorf("could not start web server because config is bad: %w", err)
```

**Rationale**: Good wrap chains read like a stack trace in English: the outer verb narrows to the inner verb, down to the root cause. Context that's too vague ("load failed") adds a layer without information; context that's too specific about the caller ("web server config is bad") is both wrong (this function doesn't know about web servers) and misleading (other callers may not be serving HTTP). Google Best Practices §Adding information to errors (Google Best Practices §Adding information to errors).

---

## EH-22: Returning the Error Unchanged Is Fine When There's Nothing to Add

**Strength**: SHOULD

**Summary**: If your function is a thin pass-through and has no additional context, return the error as-is. Don't wrap for the sake of wrapping.

```go
// Good — no new context to add
func (s *store) Get(id string) (*Blob, error) {
    return s.backend.Get(id)
}

// Good — wrap only where you're adding information
func (s *store) GetByAlias(alias string) (*Blob, error) {
    id, err := s.resolveAlias(alias)
    if err != nil {
        return nil, fmt.Errorf("resolve alias %q: %w", alias, err)
    }
    return s.backend.Get(id) // no wrap needed; backend error already has ID
}

// Bad — wrap with no added meaning
if err != nil {
    return fmt.Errorf("failed: %w", err)  // same information, more noise
}
```

**Rationale**: Wrapping always adds a layer to the message. If the layer has nothing to say, it's pure noise. Uber §Error Wrapping: "Return the original error as-is if there is no additional context to add. This maintains the original error type and message. This is well suited for cases when the underlying error message has sufficient information to track down where it came from" (Uber §Error Wrapping). Google Best Practices §Adding information to errors: "Don't add an annotation if its sole purpose is to indicate a failure without adding new information" (Google Best Practices §Adding information to errors).

---

## EH-23: Don't Use `panic` for Normal Error Handling

**Strength**: MUST-AVOID

**Summary**: Production code returns errors. `panic` is for truly unrecoverable conditions (violated invariants, corrupted state), not for validating inputs or reporting missing files.

```go
// Good
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

// Bad
func run(args []string) {
    if len(args) == 0 {
        panic("an argument is required") // caller can't react
    }
}
```

**Rationale**: A panic in library code propagates up the goroutine stack, bypasses `defer` cleanup that doesn't explicitly `recover`, and terminates the program unless every caller wraps the call in a `defer func() { recover() }()`. For a condition the caller can reasonably handle, `error` is the right mechanism. Uber §Don't Panic: "Code running in production must avoid panics. Panics are a major source of cascading failures. If an error occurs, the function must return an error and allow the caller to decide how to handle it." Google Decisions §Don't panic: "Do not use `panic` for normal error handling. Instead, use `error` and multiple return values" (Uber §Don't Panic; Google Decisions §Don't panic).

**See also**: EH-24, EH-25, CI-32

---

## EH-24: `panic` Is Reserved for Programmer Errors and Impossible States

**Strength**: SHOULD

**Summary**: The narrow cases where `panic` is the right tool: invariant violations that indicate a bug, API misuse that would silently corrupt data, and unreachable-branch guards after `log.Fatal`.

```go
// Good — true invariant check; reaching this line means the code has a bug
func (q *queue) popLocked() *item {
    if len(q.items) == 0 {
        panic("queue: popLocked called on empty queue") // internal invariant
    }
    x := q.items[0]
    q.items = q.items[1:]
    return x
}

// Good — appeasing the compiler after a known-terminal call
func answer(i int) string {
    switch i {
    case 42:
        return "yup"
    default:
        log.Fatalf("unexpected value %d", i)
        panic("unreachable")
    }
}

// Good — misuse of the reflect API
func mustTypeOf(v any) reflect.Type {
    t := reflect.TypeOf(v)
    if t == nil {
        panic("mustTypeOf: nil interface value") // caller passed invalid input
    }
    return t
}
```

**Rationale**: Panics are for the situations where continuing would be dangerous: an invariant has already been violated, so any further computation is operating on corrupted state. For *expected* failures like a missing file or a malformed request, panic is wrong — those are errors the caller should handle. Google Best Practices §When to panic: "The standard library panics on API misuse... These panics act as invariant checks" (Google Best Practices §When to panic).

**See also**: EH-23, EH-25

---

## EH-25: Don't `recover` Except at a Package Boundary That You Control

**Strength**: MUST-AVOID

**Summary**: Blanket `recover` hides bugs and keeps corrupted programs running. The one legitimate use is the "parsers that panic internally and recover at the public function" pattern, confined to a single package.

```go
// Good — panic used as an internal unwind, never escaping the package
type syntaxError struct{ msg string }

func parseInt(s string) int {
    n, err := strconv.Atoi(s)
    if err != nil {
        panic(&syntaxError{"not a valid integer"})
    }
    return n
}

func Parse(in string) (_ *Node, err error) {
    defer func() {
        if p := recover(); p != nil {
            sErr, ok := p.(*syntaxError)
            if !ok {
                panic(p) // not ours — re-panic so real crashes surface
            }
            err = fmt.Errorf("syntax error: %v", sErr.msg)
        }
    }()
    return doParse(in), nil
}

// Bad — swallow every panic in an HTTP handler "for safety"
func handler(w http.ResponseWriter, r *http.Request) {
    defer func() {
        if p := recover(); p != nil {
            log.Printf("recovered: %v", p) // program is now in an unknown state
        }
    }()
    process(w, r)
}
```

**Rationale**: By the time control reaches `recover`, the panicking goroutine may be holding locks, leaking file descriptors, or sitting on partially-written state. Recovering and continuing runs the next request with that corruption. The parser pattern is safe only because the `panic`/`recover` pair is confined to one package, the recovered type is checked, and unknown panics are re-panicked. Google Best Practices §Program checks and panics: "resist the temptation to recover panics to avoid crashes, as doing so can result in propagating a corrupted state." Google Best Practices §When to panic: "these **panics are never allowed to escape across package boundaries**" (Google Best Practices §Program checks and panics; §When to panic).

**See also**: EH-23, EH-24

---

## EH-26: Exit from `main` with `os.Exit` (or `log.Fatal`) — Not from Libraries

**Strength**: MUST

**Summary**: Program-fatal errors at startup (bad flags, missing config) should propagate up to `main`, which prints and exits. Libraries must return errors, not terminate.

```go
// Good — library returns, main exits
func loadConfig(path string) (*Config, error) { /* ... */ }

func main() {
    cfg, err := loadConfig(*flagPath)
    if err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
    run(cfg)
}

// Acceptable — package-init `must` helper where inputs are constants (see EH-27)
var tmpl = template.Must(template.New("t").Parse(`Hello {{.Name}}`))

// Bad — library terminates the program
func loadConfig(path string) *Config {
    data, err := os.ReadFile(path)
    if err != nil {
        log.Fatal(err) // bypasses caller's deferred cleanup
    }
    // ...
}
```

**Rationale**: `log.Fatal` and `os.Exit` skip deferred functions — no open file gets flushed, no mutex gets unlocked, no transaction gets rolled back. That's tolerable in `main` (the process is about to die anyway) but disastrous in library code. Google Best Practices §Program initialization: "Program initialization errors... should be propagated upward to `main`, which should call `log.Exit` with an error that explains how to fix the error. In these cases, `log.Fatal` should not generally be used, because a stack trace that points at the check is not likely to be as useful as a human-generated, actionable message" (Google Best Practices §Program initialization; §Program checks and panics; CI-31).

**See also**: CI-31, EH-23

---

## EH-27: Use `MustXxx` Only at Package Initialization Time

**Strength**: SHOULD

**Summary**: A `Must`-prefixed helper panics on failure. This is appropriate when the input is a compile-time constant (a regex literal, a template literal) so failure indicates a programming bug. It is never appropriate in a request path.

```go
// Good — constants: if these panic, ship a bug fix
var (
    validName    = regexp.MustCompile(`^[a-z]+$`)
    greetingTmpl = template.Must(template.New("g").Parse(`Hello, {{.Name}}`))
    version      = semver.MustParse("1.2.3")
)

// Good — defining your own Must for a package-level helper
func MustParse(s string) *Version {
    v, err := Parse(s)
    if err != nil {
        panic(fmt.Sprintf("MustParse(%q): %v", s, err))
    }
    return v
}

// Bad — user-supplied input to a Must helper inside a request handler
func handle(w http.ResponseWriter, r *http.Request) {
    re := regexp.MustCompile(r.URL.Query().Get("pattern")) // attacker panics server
    _ = re
}

// Bad — wrapping a Must to dodge proper error handling
func version(o *servicepb.Object) (*version.Version, error) {
    v := semver.MustParse(o.GetVersionString()) // caller has a real error to return
    return dealiasVersion(v)
}
```

**Rationale**: `Must*` is a shortcut that trades runtime error handling for a compile-time guarantee — it's safe only when the inputs are fixed. At startup, failure means the binary was built wrong; in a request handler, failure means an attacker can take down the process by sending a bad query string. Uber §Don't Panic: "An exception to this is program initialization: bad things at program startup that should abort the program may cause panic." Google Decisions §Must functions: "In general, they should only be called early on program startup, not on things like user input where normal Go error handling is preferred" (Uber §Don't Panic; Google Decisions §Must functions; CI-33).

**See also**: EH-23, EH-26, CI-33

---

## EH-28: Use `t.Fatal` in Tests, Not `panic`

**Strength**: SHOULD

**Summary**: When a test cannot continue, stop with `t.Fatal`/`t.Fatalf`. A panic marks the test as "passed" in some runners and bypasses cleanup; `t.Fatal` marks it failed and runs registered cleanups.

```go
// Good
func TestFoo(t *testing.T) {
    f, err := os.CreateTemp("", "test")
    if err != nil {
        t.Fatalf("CreateTemp: %v", err)
    }
    defer os.Remove(f.Name())
    // ...
}

// Good — in a test helper, t.Helper() + t.Fatal
func mustAddGameAssets(t *testing.T, dir string) {
    t.Helper()
    if err := os.WriteFile(filepath.Join(dir, "pak0.pak"), pak0, 0o644); err != nil {
        t.Fatalf("Setup: could not write pak0 asset: %v", err)
    }
}

// Bad
func TestFoo(t *testing.T) {
    f, err := os.CreateTemp("", "test")
    if err != nil {
        panic("failed to set up test")
    }
    // ...
}
```

**Rationale**: `t.Fatal` is integrated with the testing package's lifecycle — it records the failure, runs `t.Cleanup` hooks, and allows other test functions (and subtests) to continue. A panic from a test goroutine may terminate the process before other tests run. Uber §Don't Panic: "Even in tests, prefer `t.Fatal` or `t.FailNow` over panics to ensure that the test is marked as failed." Google Best Practices §Error handling in test helpers (Uber §Don't Panic; Google Best Practices §Error handling in test helpers; chapter 07 covers testing patterns in depth).

---

## EH-29: Discard Errors Only with a Comment Justifying Why It's Safe

**Strength**: MUST

**Summary**: The blank-identifier discard (`_ = f()`) is reserved for calls documented to never fail in the current context. Always pair the discard with a comment that names the reason.

```go
// Good — bytes.Buffer.Write's contract says the error is always nil
var b bytes.Buffer
n, _ := b.Write(p) // bytes.Buffer.Write never returns a non-nil error

// Good — best-effort close; outer error is already being returned
f, err := os.Open(path)
if err != nil {
    return err
}
defer func() { _ = f.Close() }() // ignore; we're only reading

// Bad — silent discard, no explanation
data, _ := os.ReadFile(path)
json.Unmarshal(data, &v)  // also silently ignored
```

**Rationale**: `_ = expr()` is the Go equivalent of an empty `catch {}`. It's occasionally right (you really do know the error is nil, or you really are doing a best-effort cleanup) but the reader can't tell which case applies without a comment. Google Decisions §Handle errors: "In the rare circumstance where it is appropriate to ignore or discard an error... an accompanying comment should explain why this is safe." `errcheck` flags the missing check; the comment is what makes the discard defensible in review (Google Decisions §Handle errors; CI-20).

**See also**: CI-20

---

## EH-30: Put the `defer` Cleanup Right After the Acquire — Handle Its Errors Too

**Strength**: SHOULD

**Summary**: Every acquire (open, lock, begin-transaction) should be immediately followed by the `defer` that releases it. When the cleanup can fail and the function already returns an error, capture the cleanup error into a named return.

```go
// Good — simple cleanup, error ignored with comment
f, err := os.Open(path)
if err != nil {
    return err
}
defer f.Close() // read-only; close errors are not interesting

// Good — cleanup error matters; propagate it via named return
func writeFile(path string, data []byte) (err error) {
    f, err := os.Create(path)
    if err != nil {
        return err
    }
    defer func() {
        if cerr := f.Close(); cerr != nil && err == nil {
            err = fmt.Errorf("close %q: %w", path, cerr)
        }
    }()
    if _, err := f.Write(data); err != nil {
        return fmt.Errorf("write %q: %w", path, err)
    }
    return nil
}

// Bad — defer placed at the bottom of the function, only reached on happy path
func process(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    data, err := io.ReadAll(f)
    if err != nil {
        f.Close() // manual close on error path — easy to forget
        return err
    }
    defer f.Close() // too late: errors between Open and here skip it
    return parse(data)
}
```

**Rationale**: The `defer` immediately after the acquire pairs the two visually: readers see "acquire/release" as one unit. For writes in particular, the `Close` can itself report an error (a flush fault, a disk full) that the caller needs to know about — using a named return lets the deferred function fold that into the primary error. CI-34 covers the "put defer near the acquire" rule; this entry extends it to the error-return interaction (CI-34; Uber §Defer to Clean Up).

**See also**: CI-34

---

## EH-31: Call `context.Context`-Returning Functions with Their Cancellation Error

**Strength**: SHOULD

**Summary**: A function that accepts a `context.Context` returns `ctx.Err()` when the context is cancelled. Callers should check for `context.Canceled` and `context.DeadlineExceeded` using `errors.Is` — those are sentinel errors in the standard library.

```go
// Good
func (w *Worker) Run(ctx context.Context) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err() // context.Canceled or context.DeadlineExceeded
        case job := <-w.jobs:
            if err := w.process(ctx, job); err != nil {
                if errors.Is(err, context.Canceled) {
                    return err
                }
                log.Printf("process %s: %v", job.ID, err)
            }
        }
    }
}

// Good — caller distinguishes cancellation from other failures
if err := w.Run(ctx); err != nil {
    switch {
    case errors.Is(err, context.Canceled):
        // clean shutdown
    case errors.Is(err, context.DeadlineExceeded):
        log.Printf("worker timed out")
    default:
        log.Printf("worker failed: %v", err)
    }
}
```

**Rationale**: The context package standardizes cancellation via two sentinel errors (`context.Canceled`, `context.DeadlineExceeded`). Returning `ctx.Err()` is the conventional way for a context-aware function to report that it stopped because of cancellation. Google Best Practices §Documentation Conventions §Contexts: "It is implied that the cancellation of a context argument interrupts the function it is provided to. If the function can return an error, conventionally it is `ctx.Err()`." Concurrency patterns are covered in chapter 06; this rule is limited to the error side (Google Best Practices §Documentation Conventions §Contexts).

---

## EH-32: Aggregate Multiple Errors with `errors.Join` (Go 1.20+)

**Strength**: CONSIDER

**Summary**: When several independent operations may each fail and you want to surface all their errors — not just the first — collect them with `errors.Join`. `errors.Is` and `errors.As` walk joined errors just like they walk wrapped ones.

```go
// Good — close multiple resources, surface every failure
func (s *Server) Shutdown() error {
    var errs []error
    if err := s.listener.Close(); err != nil {
        errs = append(errs, fmt.Errorf("close listener: %w", err))
    }
    if err := s.db.Close(); err != nil {
        errs = append(errs, fmt.Errorf("close db: %w", err))
    }
    if err := s.cache.Close(); err != nil {
        errs = append(errs, fmt.Errorf("close cache: %w", err))
    }
    return errors.Join(errs...) // nil if errs is empty
}

// Good — caller can still test for specific sentinels
err := s.Shutdown()
if errors.Is(err, net.ErrClosed) {
    // one of the closers reported net.ErrClosed
}

// Bad — return only the first; silently lose the rest
for _, c := range closers {
    if err := c.Close(); err != nil {
        return err // other closers not even called
    }
}
```

**Rationale**: For genuinely independent operations (closing N resources, validating N fields, fanning out to N backends), stopping at the first failure hides the others. `errors.Join` was added in Go 1.20 precisely for this: it returns a single error whose `Unwrap() []error` exposes every joined cause. Google Best Practices §Error handling notes the related `errgroup` utility for "a group of operations that can all fail or be canceled as a group" — `errors.Join` is the synchronous sibling for cases where you don't need cancellation. Goroutine fan-out with `errgroup` is covered in chapter 06 (Google Best Practices §Error handling).

**See also**: EH-21

---

## EH-33: Don't Wrap `io.EOF` Unless You Mean to

**Strength**: SHOULD

**Summary**: `io.EOF` is a signal, not an error in the usual sense — it marks the normal end of a stream. Callers compare against it directly. If you wrap it, the comparison breaks unless every caller uses `errors.Is`.

```go
// Good — propagate io.EOF unchanged
func (s *scanner) next() (token, error) {
    t, err := s.read()
    if err == io.EOF {
        return token{}, io.EOF
    }
    if err != nil {
        return token{}, fmt.Errorf("scan: %w", err)
    }
    return t, nil
}

// Acceptable — wrap only if the caller is expected to use errors.Is
return token{}, fmt.Errorf("scan at offset %d: %w", s.pos, io.EOF)
// caller: errors.Is(err, io.EOF)

// Bad — wraps EOF with a string format that hides it from ==
return token{}, fmt.Errorf("scan at offset %d: %v", s.pos, io.EOF) // caller's `err == io.EOF` now fails
```

**Rationale**: A lot of existing code compares `err == io.EOF` directly because the standard library's `Read` contract was documented that way before `errors.Is` existed. Wrapping EOF silently breaks those callers. If you do wrap it, use `%w` (so `errors.Is` still works) and document the wrap. Otherwise, return `io.EOF` unchanged. (Google Best Practices §Errors — documentation conventions example: `"At end of file, Read returns 0, io.EOF"` is the classic contract.)

**See also**: EH-15, EH-18

---

## EH-34: Don't Panic on nil Maps, Slices, or Channels — Check First

**Strength**: MUST

**Summary**: Writing to a nil map panics. Sending on a nil channel blocks forever. Several "obvious" runtime panics are preventable with a nil check or `make`. Treat them as bugs, not as errors you can recover from.

```go
// Good — initialize before use
m := make(map[string]int)
m["x"] = 1

// Good — guard
var cache map[string]int
if cache == nil {
    cache = make(map[string]int)
}
cache["x"] = 1

// Bad — panics: "assignment to entry in nil map"
var m map[string]int
m["x"] = 1
```

**Rationale**: These are programmer errors caught by the runtime. They're listed here because a panic caught by `recover` can mask them — and because the tempting fix ("recover and log") keeps a broken program running. The right fix is to make the code not reach that state. Uber §Initializing Maps (referenced from CI-13) shows the construction patterns. Google Best Practices §When to panic classifies nil dereferences and out-of-bounds access as "analogous to... core language bugs... not expected to appear in production code" (Uber §Initializing Maps; Google Best Practices §When to panic).

**See also**: EH-23, EH-24, CI-13

---

## EH-35: Test Error Semantics, Not Error Strings

**Strength**: SHOULD

**Summary**: In tests, assert that the *type* or *sentinel* matches (`errors.Is`, `errors.As`), not that the message contains a particular substring. String-based tests break whenever the message is rephrased.

```go
// Good
got := f(input)
if !errors.Is(got, ErrNotFound) {
    t.Errorf("f(%q) = %v, want ErrNotFound", input, got)
}

// Good — only the presence of an error matters
if gotErr := err != nil; gotErr != tc.wantErr {
    t.Errorf("f(%q) = %v, want error presence = %v", tc.input, err, tc.wantErr)
}

// Bad — coupled to human-readable wording
if !strings.Contains(err.Error(), "not found") {
    t.Errorf("expected 'not found' in err, got %q", err)
}
```

**Rationale**: Error strings are for humans; error values are for code. Tests that match on strings are "change detector tests" — they fail whenever you touch the message, even for an improvement. Google Decisions §Test error semantics: "Tests should seek to only test semantic information that can be reliably observed, rather than display information that is intended for human debugging... don't use string comparison to check what type of error your function returns." Chapter 07 expands on testing patterns (Google Decisions §Test error semantics).

**See also**: EH-17

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `error` is the failure signal | MUST | No in-band `-1`/`""` sentinels |
| 02 | Return `error`, not `*MyError` | MUST | Avoid the typed-nil interface trap |
| 03 | Pick the right constructor | SHOULD | Match × dynamic → four cases |
| 04 | `errors.New` vs `fmt.Errorf` | SHOULD | Static text vs interpolation |
| 05 | Sentinels are `var`, not `const` | MUST | Group in one `var (...)` block |
| 06 | `Err` / `err` prefix for sentinels | MUST | Overrides `_` prefix convention |
| 07 | `Error` suffix for custom types | SHOULD | Type vs value distinction |
| 08 | Pointer receiver on error types | SHOULD | Avoids copy, aligns `errors.As` |
| 09 | Lowercase, no trailing punctuation | MUST | Strings are embedded, not terminal |
| 10 | Skip "failed to" / "error while" | SHOULD | `error` already means failure |
| 11 | Don't duplicate wrapped info | SHOULD | Add only *new* context |
| 12 | `%w` exposes the chain | SHOULD | `%v` hides; `%s` drops the value |
| 13 | `%w` at the end of the format | SHOULD | Prints outer-to-inner naturally |
| 14 | `%w` at the start for sentinels | SHOULD | Category visible first |
| 15 | `errors.Is` for sentinel matching | SHOULD | `==` breaks through wrappers |
| 16 | `errors.As` for custom-type extraction | SHOULD | Walks the unwrap chain |
| 17 | No substring matching on messages | MUST-AVOID | Couples to human text |
| 18 | Document returned errors | SHOULD | Sentinels and types are contract |
| 19 | Handle each error once | MUST | Log or return, not both |
| 20 | Translate at package boundaries | SHOULD | Canonical codes or domain sentinels |
| 21 | Context narrows the failure | SHOULD | One verb per layer |
| 22 | Return unchanged when nothing to add | SHOULD | No-op wraps are noise |
| 23 | Don't panic for normal errors | MUST-AVOID | Callers lose the ability to react |
| 24 | `panic` for invariants and bugs | SHOULD | Corrupt state, unreachable branches |
| 25 | `recover` only at package boundaries | MUST-AVOID | Blanket recover hides bugs |
| 26 | Exit from `main`, not libraries | MUST | `log.Fatal` skips `defer` |
| 27 | `MustXxx` only at init time | SHOULD | Never on user input |
| 28 | `t.Fatal`, not `panic`, in tests | SHOULD | Integrates with test lifecycle |
| 29 | `_` discard needs a comment | MUST | Explain why the error is safe |
| 30 | `defer` near acquire; capture close err | SHOULD | Named return for write paths |
| 31 | Return `ctx.Err()` on cancellation | SHOULD | `context.Canceled` is the sentinel |
| 32 | `errors.Join` for independent failures | CONSIDER | Go 1.20+; every error survives |
| 33 | Don't wrap `io.EOF` without meaning | SHOULD | `==` compares break silently |
| 34 | Nil map/slice/channel panics are bugs | MUST | Initialize or guard; don't recover |
| 35 | Test error semantics, not strings | SHOULD | `errors.Is` / presence boolean |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for CI-20 (don't ignore errors with `_`), CI-21 (indent the error path), CI-31 (exit from main only), CI-32 (don't panic in library code), CI-33 (`Must` functions at init), CI-34 (`defer` near acquire). This chapter extends those rules with the specifics of wrapping, classification, and inspection.
- **API Design**: See `02-api-design.md` for `error` as the last return, multi-return value ordering, and how an error return interacts with named results.
- **Type Design**: See `04-type-design.md` for struct design patterns that apply to custom error types (EH-07, EH-08).
- **Concurrency**: See `06-concurrency.md` for `errgroup`, goroutine-local error handling, and fan-out patterns — the multi-error story that `errors.Join` (EH-32) covers synchronously.
- **Testing**: See `07-testing.md` for table-driven error tests, `cmpopts.EquateErrors`, and test-helper `Must` patterns (EH-28, EH-35).
- **Anti-Patterns**: See `09-anti-patterns.md` for recurring violations — panic-in-library, string-match-on-errors, log-and-return, typed-nil returns.

---

## External References

- [Package `errors`](https://pkg.go.dev/errors) — `New`, `Is`, `As`, `Join`, `Unwrap`
- [Package `fmt`](https://pkg.go.dev/fmt) — `Errorf` and the `%w` verb
- [The Go Blog — Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors) — the wrapping model
- [The Go Blog — Errors are values](https://go.dev/blog/errors-are-values) — Rob Pike on why the language has no exceptions
- [Dave Cheney — Don't just check errors, handle them gracefully](https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully) — canonical essay on error-handling discipline
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) §Errors, §Don't Panic
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions §Errors, §Don't panic, §Must functions; Best Practices §Error handling, §When to panic
- [Effective Go §Errors](https://go.dev/doc/effective_go#errors)
- [Go FAQ — Why is my nil error value not equal to nil?](https://go.dev/doc/faq#nil_error) — the typed-nil trap behind EH-02
