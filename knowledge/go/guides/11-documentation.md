# Documentation

Conventions for writing `godoc`-visible comments, package documentation, READMEs, and the internal commentary that supports maintainers. These patterns are grounded in the *Go Doc Comments* specification (the canonical reference since Go 1.19), *Effective Go §Commentary*, the *Google Go Style Guide* (Decisions §Commentary, Best Practices §Documentation), and the *Uber Go Style Guide*. The core principle: documentation is read in two places — on [pkg.go.dev](https://pkg.go.dev) by users of your API, and inside the source file by maintainers. Write for both audiences and respect godoc's minimal rendering.

Target environment: **Go 1.22+**, doc rendering via `go doc` and [pkg.go.dev](https://pkg.go.dev), `gofmt` + `go vet` + `staticcheck` for mechanical checks. This chapter extends CI-42 (Doc Comments Are Full Sentences) with the full treatment.

---

## DC-01: Every Top-Level Exported Name Has a Doc Comment

**Strength**: MUST

**Summary**: Every exported `func`, `type`, `const`, `var`, and method must have a doc comment. Unexported identifiers should have one too when their behavior is non-obvious.

```go
// Good
// Client is a connection to the remote service.
type Client struct{ /* ... */ }

// NewClient returns a Client configured for addr.
func NewClient(addr string) (*Client, error) { /* ... */ }

// DefaultTimeout is the timeout applied when no deadline is set on ctx.
const DefaultTimeout = 30 * time.Second

// ErrNotFound is returned when the requested resource does not exist.
var ErrNotFound = errors.New("not found")

// Bad — exported name without a doc comment
type Client struct{ /* ... */ }

func NewClient(addr string) (*Client, error) { /* ... */ }
```

**Rationale**: Doc comments appear in Godoc, surfaces via IDEs, and are surfaced by `go doc`. Missing comments on exported names are the most common lint finding and produce generated doc pages that are simply lists of signatures with no explanation. Google Decisions §Doc comments: "All top-level exported names must have doc comments, as should unexported type or function declarations with unobvious behavior or meaning" (Google Decisions §Doc comments; Effective Go §Commentary; Go Doc Comments spec).

**See also**: CI-42, DC-02

---

## DC-02: Start the Comment with the Identifier Name

**Strength**: SHOULD

**Summary**: The first word of a doc comment is the name of the thing being documented. An article (`A`, `An`, `The`) may precede it.

```go
// Good — begins with the identifier
// Client is a connection to the remote service.
type Client struct{ /* ... */ }

// A Request represents a request to run a command.
type Request struct{ /* ... */ }

// Encode writes the JSON encoding of req to w.
func Encode(w io.Writer, req *Request) error { /* ... */ }

// Bad — does not begin with the identifier
// This type represents a client connection.
type Client struct{ /* ... */ }

// Creates a new client.
func NewClient(addr string) *Client { /* ... */ }

// The following function encodes JSON.
func Encode(w io.Writer, req *Request) error { /* ... */ }
```

**Rationale**: Starting with the name makes the rendered doc line read naturally (`"NewClient returns..."`) and lets `grep NewClient` find both the declaration and the comment. `go doc`'s output is a tabular list of signatures and summary lines — the leading name keeps signal aligned with the column that contains it. Go Doc Comments spec: "every exported name should have a doc comment... Each [doc comment] begins with the name of the item it describes." Uber and Google both require this (Go Doc Comments spec; Google Decisions §Doc comments; Effective Go §Commentary).

**See also**: CI-42, DC-01

---

## DC-03: Doc Comments Are Full, Punctuated Sentences

**Strength**: SHOULD

**Summary**: Documentation comments on declarations are complete English sentences — capitalized, punctuated, subject-verb-object. End-of-line comments on struct fields may be sentence fragments.

```go
// Good — complete sentence, punctuated
// Compile parses a regular expression and returns, if successful, a Regexp
// object that can be used to match against text.
func Compile(expr string) (*Regexp, error) { /* ... */ }

// Good — struct field fragments are allowed
type Server struct {
    // BaseDir points to the base directory under which Shakespeare's works
    // are stored.
    BaseDir string

    WelcomeMessage  string // displayed when user logs in
    ProtocolVersion string // checked against incoming requests
    PageLength      int    // lines per page when printing (optional; default: 20)
}

// Bad — sentence fragment on a declaration
// compiles an expression
func Compile(expr string) (*Regexp, error) { /* ... */ }

// Bad — no period
// Compile parses a regular expression
func Compile(expr string) (*Regexp, error) { /* ... */ }
```

**Rationale**: Godoc renders doc comments directly; ending with a period and writing full sentences produces grammatical output. Short end-of-line field comments are a common exception because the field name acts as the subject (`WelcomeMessage` — "displayed when user logs in" reads as "WelcomeMessage is displayed when user logs in"). Google Decisions §Comment sentences: "Documentation comments should always be complete sentences, and as such should always be capitalized and punctuated. Simple end-of-line comments (especially for struct fields) can be simple phrases that assume the field name is the subject" (Google Decisions §Comment sentences; Go Doc Comments spec).

**See also**: DC-02

---

## DC-04: Package Comments Precede the `package` Clause

**Strength**: MUST

**Summary**: Each package has exactly one package comment. It sits directly above the `package` clause with no blank line separating them. Start it with `Package <name>`.

```go
// Good
// Package math provides basic constants and mathematical functions.
//
// This package does not guarantee bit-identical results across
// architectures.
package math
```

```go
// Bad — blank line breaks the association
// Package math provides basic constants and mathematical functions.

package math

// Bad — does not start with "Package <name>"
// Provides basic math helpers.
package math
```

**Rationale**: Godoc uses the contiguous comment block directly above `package` as the package-level documentation. A blank line cuts the association; tools then attribute the comment to nothing. Starting with `Package math` makes the rendered overview read naturally. Google Decisions §Package comments: "Package comments must appear immediately above the package clause with no blank line between the comment and the package name... There must be a single package comment per package" (Google Decisions §Package comments; Go Doc Comments spec).

**See also**: DC-05, DC-06

---

## DC-05: Use `doc.go` for Long Package Documentation

**Strength**: CONSIDER

**Summary**: When the package comment grows long, or when no single source file is an obvious "primary" file, move the package comment into its own `doc.go` file containing only the comment and the `package` clause.

```go
// Good — doc.go
// Package auth provides authentication and session management.
//
// # Overview
//
// This package is split into three areas:
//
//   - Login and logout via the LoginFlow type.
//   - Session creation and validation via Session.
//   - Password hashing via HashPassword/VerifyPassword.
//
// All password operations use bcrypt with the cost factor from
// config.PasswordCost (default: 12).
//
// # Thread safety
//
// All exported functions in this package are safe for concurrent use.
package auth
```

**Rationale**: Placing a 100-line package comment at the top of `auth.go` pushes the actual code below the fold. A dedicated `doc.go` keeps the prose separate from implementation and gives editors a natural place to land when browsing. Google Best Practices §Package size: "Packages with long package documentation may choose to dedicate one file called `doc.go` that has the package documentation, a package declaration, and nothing else." Not required, but idiomatic for non-trivial packages (Google Best Practices §Package size; Google Decisions §Package comments).

**See also**: DC-04

---

## DC-06: Binary (`package main`) Comments Describe the Command

**Strength**: SHOULD

**Summary**: A `main` package's doc comment describes the binary, not a library. Start with the binary name as the first word, or prefix with `Binary`, `Command`, or `The`.

```go
// Good
// The seed_generator command generates a Finch seed file from a set of
// JSON study configs.
//
//     seed_generator *.json | base64 > finch-seed.base64
package main
```

```go
// Also good — all of these forms are acceptable
// Binary seed_generator ...
// Command seed_generator ...
// Program seed_generator ...
// Seed_generator ...
// The seed_generator command ...
package main
```

```go
// Bad — uses "Package main", which is meaningless to readers
// Package main is the seed generator.
package main
```

**Rationale**: "Package main" is syntactically required but semantically useless in documentation — there are many `main` packages. Describing the binary by name matches how it will be invoked and how it appears in documentation indexes. Google Decisions §Package comments: "Comments for `main` packages have a slightly different form, where the name of the `go_binary` rule in the BUILD file takes the place of the package name" (Google Decisions §Package comments; Go Doc Comments spec).

**See also**: DC-04

---

## DC-07: Comment Every Struct Field That Isn't Self-Explanatory

**Strength**: SHOULD

**Summary**: Fields in an exported struct should have a comment when their purpose or constraints aren't obvious from the name and type. End-of-line comments are acceptable for short notes; sentence-long notes go above the field.

```go
// Good
// Options configure the group management service.
type Options struct {
    // General setup:
    Name  string
    Group *FooGroup

    // Dependencies:
    DB *sql.DB

    // Customization:
    LargeGroupThreshold int // optional; default: 10
    MinimumMembers      int // optional; default: 2
}

// Good — long field comment above the field
type Server struct {
    // BaseDir points to the base directory under which Shakespeare's
    // works are stored. The directory structure is expected to be:
    //
    //   {BaseDir}/manifest.json
    //   {BaseDir}/{name}/{name}-part{number}.txt
    BaseDir string

    // short fields: end-of-line comments
    Addr string // host:port to bind
    TLS  bool   // enable HTTPS
}
```

**Rationale**: Struct field documentation appears in Godoc alongside the field. Without it, callers must infer meaning from the name, which fails for fields like `Tolerance`, `Threshold`, or `Mode`. Comment only what adds information — `// Name string: the name` is noise. Google Decisions §Doc comments: "A documentation comment applies to the following symbol, or the group of fields if it appears in a struct." Google Best Practices §Parameters and configuration: "Document the error-prone or non-obvious fields and parameters by saying why they are interesting" (Google Decisions §Doc comments; Google Best Practices §Parameters).

---

## DC-08: Document Unexported Code When Behavior Is Non-Obvious

**Strength**: SHOULD

**Summary**: Unexported functions, types, and methods with subtle invariants, tricky concurrency, or non-obvious semantics deserve doc comments. Follow the same "starts with the identifier name" rule, so it remains correct if the identifier is later exported.

```go
// Good
// recomputeIndex rebuilds s.index from s.items. The caller must hold s.mu.
func (s *store) recomputeIndex() { /* ... */ }

// normalizeHost lowercases host and strips a trailing dot, preserving
// ports and IPv6 brackets.
func normalizeHost(host string) string { /* ... */ }

// Good — unexported type whose zero value has a precondition
// bucket tracks per-key hit counts. The zero value is not usable;
// use newBucket.
type bucket struct { /* ... */ }

// Bad — silent invariant
func (s *store) recomputeIndex() {
    // caller must hold s.mu (this should be in the doc)
    ...
}
```

**Rationale**: Internal docs pay maintainers, not users. When an unexported function has a lock invariant, a side effect, or a surprising edge case, a one-line comment prevents the next maintainer from breaking it. Google Best Practices on doc comments: "If you have doc comments for unexported code, follow the same custom as if it were exported (namely, starting the comment with the unexported name). This makes it easy to export it later by simply replacing the unexported name with the newly-exported one across both comments and code." Google Decisions §Doc comments also mandates this for unexported names "with unobvious behavior or meaning" (Google Decisions §Doc comments; Google Best Practices §Doc comments).

---

## DC-09: Comments Explain *Why*, Not *What*

**Strength**: MUST

**Summary**: Internal comments inside function bodies should explain intent, context, or non-obvious choices. They should not restate what the code does — that's the code's job.

```go
// Good — comment explains why
// The upstream API rate-limits at 100 req/min and returns 429 without a
// Retry-After header; back off exponentially starting at 250ms.
for attempt := 0; attempt < maxRetries; attempt++ {
    if err := call(); err == nil {
        return nil
    }
    time.Sleep(backoff(attempt))
}

// Good — calls attention to a subtle invariant
// Must copy s before sorting: caller retains the original slice.
sorted := append([]int(nil), s...)
sort.Ints(sorted)

// Bad — narrates the code
// Increment the counter by one
counter++

// Bad — restates what the call does
// Get the user from the database
u, err := db.GetUser(id)
```

**Rationale**: Code that restates itself is noise; it doubles maintenance (the comment must be updated with every change) and obscures the genuinely informative comments nearby. Google Style Guide §Clarity: "It is often better for comments to explain why something is done, not what the code is doing." Google Style Guide §Simplicity: "Has comments that explain why, not what, the code is doing" (Google Style Guide §Clarity; Google Style Guide §Simplicity).

**See also**: DC-10

---

## DC-10: Delete Commented-Out Code — That's What Version Control Is For

**Strength**: MUST

**Summary**: Don't leave commented-out code in the tree. If it's not running, remove it. Version control preserves every line ever written.

```go
// Bad — commented-out code
func processOrder(o Order) error {
    // oldValidation(o)  // kept in case we need it
    // if o.Amount < 0 {
    //     return errors.New("negative")
    // }
    return validate(o)
}

// Good — remove it; git history is there if you need it
func processOrder(o Order) error {
    return validate(o)
}
```

**Rationale**: Commented-out code confuses readers: is it a work-in-progress, a deliberately-disabled feature, or dead weight? The answer is almost always "dead weight." Removing it eliminates the ambiguity. `git log -S` retrieves any line that ever existed. There is no corresponding Go-team or Google document that prohibits this explicitly, but every Go review guide (and most general coding guides) treat it as a bright line.

---

## DC-11: `TODO(owner)`: Mark Incomplete Work with an Owner

**Strength**: SHOULD

**Summary**: A `TODO` comment identifies the person (username or team) responsible, optionally a bug number, and what needs to happen.

```go
// Good
// TODO(alice): Replace with context.AfterFunc when Go 1.21 is min version.
signal.Notify(sigCh, os.Interrupt)

// TODO(auth-team, b/42): The token refresh path assumes single-tenant;
// extend for multi-tenant once the session struct carries tenant IDs.

// Acceptable — no owner, but still informative
// TODO: clamp to [0, MaxInt] once https://example.com/issues/17 ships.

// Bad — untraceable, no context
// TODO: fix this
// TODO
// FIXME
```

**Rationale**: A bare `TODO` becomes invisible debt. Naming an owner lets the next reader ask who to talk to, and a bug number gives the TODO a lifecycle. The `TODO(owner)` convention originates in Go's own codebase and is matched by Google's style (in Google C++/Python/Go guides). No hard Go-spec rule requires the owner annotation, but community norms and the Go standard library use it uniformly. `go vet` does not check these; code reviews do.

**See also**: DC-12

---

## DC-12: `BUG(author)`: Mark Known Bugs for `go doc`

**Strength**: CONSIDER

**Summary**: A top-level comment beginning with `BUG(author):` is surfaced by `go doc` as a known issue on the package's documentation page. Use it for publicly-observable defects that users should know about.

```go
// Good — surfaced on the package's godoc page under "Bugs"
// BUG(rsc): The rule Title uses for word boundaries does not handle
// Unicode punctuation properly.

// Package strings implements simple functions to manipulate UTF-8 encoded
// strings.
package strings
```

**Rationale**: The `BUG(name):` prefix at file scope is the Go-spec convention for known bugs; `go doc` scans for it and publishes it in the package documentation. This makes user-visible issues discoverable without a separate issue tracker. Use sparingly — most bugs should be fixed, not documented. See the Go Doc Comments spec for the BUG prefix and [standard library examples](https://pkg.go.dev/strings#pkg-note-bug).

**See also**: DC-11

---

## DC-13: `Deprecated:` Lines Mark Retirement

**Strength**: SHOULD

**Summary**: Mark a function, method, type, or constant as deprecated by starting a paragraph in its doc comment with `Deprecated:`. Follow with the recommended replacement.

```go
// Good
// Parse parses the input and returns a document.
//
// Deprecated: Use ParseContext instead, which supports cancellation.
func Parse(input []byte) (*Document, error) { /* ... */ }

// Good — deprecated const with pointer to replacement
// MaxSize is the maximum message size in bytes.
//
// Deprecated: Use MaxBytes; this constant will be removed in v2.
const MaxSize = 1 << 20
```

**Rationale**: The `Deprecated:` paragraph prefix is recognized by `go doc`, [pkg.go.dev](https://pkg.go.dev), IDEs (gopls highlights deprecated identifiers), and `staticcheck`'s `SA1019` check. Writing `// DEPRECATED:` or `// Note: deprecated` does not trigger tooling — only the exact form `Deprecated: ` at the start of a paragraph does. Go Doc Comments spec ([Deprecation](https://go.dev/doc/comment#deprecation)): "Deprecated: followed by a space and then a description of the deprecation" starts a new paragraph.

---

## DC-14: Indent Code Blocks in Doc Comments

**Strength**: MUST

**Summary**: Godoc formats any line indented more than the surrounding text as preformatted code. Use a leading two-space indent (four total with the `// `) for code snippets, commands, and tabular data.

```go
// Good
// Update runs the function in an atomic transaction.
//
// This is typically used with an anonymous TransactionFunc:
//
//     if err := db.Update(func(s *State) { s.Foo = bar }); err != nil {
//         // ...
//     }
func Update(fn TransactionFunc) error { /* ... */ }

// Good — command-line example in package doc
// The seed_generator command reads JSON configs and emits a seed.
//
//     seed_generator *.json > finch-seed.txt
package main

// Bad — unindented code block renders as wrapped prose
// Update runs the function in an atomic transaction. Use it like this:
// if err := db.Update(...); err != nil { return err }
```

**Rationale**: Godoc has no fenced code blocks (`\`\`\``) — indentation is the only mechanism. Unindented code runs into the surrounding paragraph and loses line breaks. Google Best Practices §Godoc formatting: "Indenting lines by an additional two spaces formats them verbatim." Go Doc Comments spec: "A span of indented lines is a preformatted code block." Treat this as a hard rule (Go Doc Comments spec; Google Best Practices §Godoc formatting; Google Decisions §Commentary).

**See also**: DC-15, DC-19

---

## DC-15: Lists in Doc Comments (Go 1.19+)

**Strength**: SHOULD

**Summary**: Since Go 1.19, godoc recognizes bulleted and numbered lists if each item starts at the same indent level with `-`, `*`, or `N.`. Separate the list from surrounding prose by a blank line.

```go
// Good — Go 1.19+ renders this as a bulleted list
// Parse accepts the following source types:
//
//   - A string. The string is parsed as UTF-8.
//   - An io.Reader. Its contents are read in full.
//   - A byte slice.
//
// The returned Document reflects the parsed structure.
func Parse(src any) (*Document, error) { /* ... */ }

// Good — numbered list for ordered steps
// Run performs the migration in three phases:
//
//  1. Validate the current schema.
//  2. Write the new schema.
//  3. Migrate rows in batches.
func Run(ctx context.Context) error { /* ... */ }

// Bad — list items run together into prose
// Parse accepts the following source types: - A string. - An io.Reader.
// - A byte slice.
```

**Rationale**: Before Go 1.19, godoc had no list recognition and the indentation trick from DC-14 was the only way to get tabular output. The Go 1.19 update to godoc (see the [Go Doc Comments spec](https://go.dev/doc/comment#lists)) added formal list support: items at the same indent, separated from prose by a blank line. Use `-` or `*` for bullets, `N.` for numbered lists. Google Decisions §Commentary notes: "Godoc uses very little special formatting; lists and code snippets should usually be indented to avoid linewrapping" — the 1.19 rules formalize this.

**See also**: DC-14

---

## DC-16: Link to Other Packages with `[PackageName]`

**Strength**: SHOULD

**Summary**: Since Go 1.19, godoc recognizes bracket references — `[Name]`, `[pkg.Name]`, or `[pkg.Type.Method]` — and renders them as hyperlinks on [pkg.go.dev](https://pkg.go.dev). Use them to cross-reference related identifiers.

```go
// Good — rendered as links by godoc and pkg.go.dev
// NewClient returns a [Client] configured for addr. The client uses
// [http.DefaultTransport] unless Transport is set.
//
// See [Client.Do] for the request lifecycle.
func NewClient(addr string) (*Client, error) { /* ... */ }

// Good — link to a symbol in a different package
// Context wraps a [context.Context] with request-scoped values.
type Context struct { /* ... */ }

// Good — link to a method on another type
// After the call, callers should invoke [Response.Body.Close].
func (c *Client) Do(req *Request) (*Response, error) { /* ... */ }

// Bad — bare package.Type references don't link automatically before 1.19,
// and after 1.19 they still won't link without brackets
// Do calls http.DefaultTransport.RoundTrip.
```

**Rationale**: Hyperlinks make documentation navigable without copy-pasting identifiers into search boxes. The bracket syntax is parsed by godoc starting in Go 1.19; earlier tools render the brackets literally (a small cost) but most users are on modern tooling. See the Go Doc Comments spec ([Links](https://go.dev/doc/comment#links)) for the full grammar, including custom link text via `[text]: URL`. Google §Commentary points to the Go Doc Comments spec as authoritative.

**See also**: DC-15

---

## DC-17: Headings Use the Go 1.19 `#` Syntax

**Strength**: CONSIDER

**Summary**: Since Go 1.19, godoc recognizes lines starting with `#` (in column 1 of the comment) as headings. Earlier, headings were signaled by a standalone capitalized line. Prefer the `#` form for new code.

```go
// Good — Go 1.19+ heading form
// Package auth provides authentication primitives.
//
// # Overview
//
// The package exposes three main types: LoginFlow, Session, Token.
//
// # Thread safety
//
// All exported functions are safe for concurrent use.
package auth
```

```go
// Older style (still recognized) — capitalized line with no punctuation,
// preceded and followed by blank lines
// Package auth provides authentication primitives.
//
// Overview
//
// The package exposes three main types: LoginFlow, Session, Token.
package auth
```

**Rationale**: The `# Heading` form is unambiguous — godoc can tell it's a heading without heuristics — and is the recommended form going forward. The older "capitalized-line-between-blanks" form (documented in Google Best Practices §Godoc formatting: "A single line that begins with a capital letter, contains no punctuation except parentheses and commas, and is followed by another paragraph, is formatted as a header") still works, but collides easily with normal prose (any short sentence-like line can accidentally become a heading). Go Doc Comments spec ([Headings](https://go.dev/doc/comment#headings)).

---

## DC-18: No Markdown — Respect the Godoc Renderer

**Strength**: MUST

**Summary**: Godoc is not Markdown. `**bold**`, `*italic*`, ` `code` `, `[text](url)`, and fenced code blocks (` ``` `) render literally. Use godoc's mechanisms: indent for code, blank lines for paragraphs, `[Name]` for links.

```go
// Good — godoc-native formatting
// Compile parses a regular expression. Patterns use Go's RE2 syntax; see
// [regexp/syntax] for the specification.
//
// Example:
//
//     re := regexp.MustCompile(`^hello`)
//     re.MatchString("hello world") // true

// Bad — Markdown syntax renders literally
// Compile parses a regular expression. Patterns use **Go's RE2 syntax**.
//
// See the [syntax reference](https://pkg.go.dev/regexp/syntax).
//
// ```go
// re := regexp.MustCompile(`^hello`)
// ```
```

**Rationale**: Godoc's rendering model is deliberately minimal: paragraphs, indented code, lists (1.19+), headings (1.19+), and `[Name]` links. It ignores Markdown. Writing Markdown produces pages with stray asterisks and unformatted code fences. Google Decisions §Commentary: "Godoc uses very little special formatting; lists and code snippets should usually be indented to avoid linewrapping. Apart from indentation, decoration should generally be avoided." The Go Doc Comments spec is the canonical reference (Google Decisions §Commentary; Go Doc Comments spec).

**See also**: DC-14, DC-15, DC-16

---

## DC-19: Separate Paragraphs with a Blank Comment Line

**Strength**: SHOULD

**Summary**: Within a doc comment, use a blank line (a `//` line with nothing after it) to separate paragraphs. Godoc joins contiguous non-blank lines into one paragraph.

```go
// Good
// LoadConfig reads a configuration out of the named file.
//
// The file format is YAML; see the Config type for field meanings.
// Unknown keys are ignored.
//
// LoadConfig does not watch the file for changes. Re-invoke to reload.
func LoadConfig(path string) (*Config, error) { /* ... */ }

// Bad — all one paragraph
// LoadConfig reads a configuration out of the named file. The file format
// is YAML; see the Config type for field meanings. Unknown keys are
// ignored. LoadConfig does not watch the file for changes. Re-invoke to
// reload.
```

**Rationale**: A blank comment line is godoc's paragraph separator. Without it, distinct ideas run together into a wall of text. Google Best Practices §Godoc formatting: "A blank line is required to separate paragraphs."

---

## DC-20: Comment Line Length — No Hard Limit, but Wrap for Readability

**Strength**: CONSIDER

**Summary**: There is no fixed line length for Go comments. Wrap at roughly 80–100 columns for readability in source; don't wrap URLs or other long tokens that would be worse if broken.

```go
// Good — wrapped comment, unwrapped URL
// This is a comment paragraph. The length of individual lines doesn't
// matter in Godoc; but the choice of wrapping makes it easy to read on
// narrow screens.
//
// Don't worry too much about the long URL:
// https://supercalifragilisticexpialidocious.example.com:8080/Animalia/Chordata/Mammalia/Rodentia/Geomyoidea/Geomyidae/

// Bad — one very long line of prose
// This is a comment paragraph. While some code editors and viewers will wrap the paragraph for the reader, others will display a very long line that will overflow most windows and require users to scroll horizontally. In addition, even on a screen capable of displaying the entire line, it is easier to read a narrower paragraph than very wide one.
```

**Rationale**: Godoc re-flows paragraphs on render, so the exact column width doesn't affect the published doc. But source files are also read directly, in tools that don't re-wrap (diffs, code review). Wrapping around 80–100 columns makes the source readable without forcing odd breaks. Google Decisions §Comment line length: "There is no fixed line length for comments in Go. Long comment lines should be wrapped to ensure that source is readable... 80 or 100 columns are common choices. However, this is not a hard cut-off."

---

## DC-21: Document Error Conventions — Sentinel Values and Typed Errors

**Strength**: SHOULD

**Summary**: When a function returns specific errors (sentinels, typed errors, or a particular concrete type wrapped in the `error` interface), document them so callers can match with `errors.Is`/`errors.As`.

```go
// Good — document the sentinel and the condition
// Read reads up to len(b) bytes from the File. It returns the number of
// bytes read and any error encountered.
//
// At end of file, Read returns 0, [io.EOF].
func (f *File) Read(b []byte) (n int, err error) { /* ... */ }

// Good — document the concrete error type
// Chdir changes the current working directory to dir.
//
// If there is an error, it will be of type [*PathError].
func Chdir(dir string) error { /* ... */ }

// Good — package-level overview of error conventions
// Package os provides a platform-independent interface to operating system
// functionality.
//
// Often, more information is available within the error. For example, if
// a call that takes a file name fails, such as Open or Stat, the error
// will include the failing file name when printed and will be of type
// [*PathError], which may be unpacked for more information.
package os
```

**Rationale**: Without documentation, callers don't know which errors to match. `errors.Is(err, io.EOF)` only works if the reader knows `io.EOF` is the sentinel. Documenting pointer vs. non-pointer receivers on error types matters because `errors.As` requires the right target type. Google Best Practices §Errors: "Document significant error sentinel values or error types that your functions return to callers so that callers can anticipate what types of conditions they can handle in their code." Error-handling mechanics are covered in chapter 03 (Google Best Practices §Errors).

**See also**: CI-20, CI-21

---

## DC-22: Document Cleanup Requirements

**Strength**: SHOULD

**Summary**: If a function returns a resource that the caller must release (close, cancel, stop), say so in the doc — and point to the specific method to call.

```go
// Good — cleanup spelled out
// NewTicker returns a new Ticker containing a channel that will send the
// current time on the channel after each tick.
//
// Call Stop to release the Ticker's associated resources when done.
func NewTicker(d Duration) *Ticker { /* ... */ }

// Good — cleanup requirement with a small snippet
// Get issues a GET to the specified URL.
//
// When err is nil, resp always contains a non-nil resp.Body. The caller
// should close resp.Body when done reading from it.
//
//     resp, err := http.Get("http://example.com/")
//     if err != nil {
//         // handle error
//     }
//     defer resp.Body.Close()
//     body, err := io.ReadAll(resp.Body)
func (c *Client) Get(url string) (resp *Response, err error) { /* ... */ }

// Bad — caller must guess that Stop is required
// NewTicker returns a new Ticker. It ticks every d.
func NewTicker(d Duration) *Ticker { /* ... */ }
```

**Rationale**: Resource leaks from undocumented cleanup are endemic in long-running Go services. A one-line "Call Stop when done" turns a silent invariant into an obvious contract. Google Best Practices §Documentation conventions — Cleanup: "Document any explicit cleanup requirements that the API has. Otherwise, callers won't use the API correctly, leading to resource leaks and other possible bugs."

**See also**: CI-34

---

## DC-23: Concurrency Safety — Document the Contract

**Strength**: SHOULD

**Summary**: Go users assume read-only operations are safe for concurrent use and that mutating operations are not. Document only deviations from those defaults, or when the category isn't obvious.

```go
// Good — no unnecessary annotation; reading is assumed safe
// Len returns the number of bytes of the unread portion of the buffer.
func (b *Buffer) Len() int { /* ... */ }

// Good — no unnecessary annotation; mutating is assumed unsafe
// Grow grows the buffer's capacity.
func (b *Buffer) Grow(n int) { /* ... */ }

// Good — ambiguous case (Lookup on an LRU mutates internal state)
// Lookup returns the data associated with the key from the cache.
//
// This operation is not safe for concurrent use.
func (c *Cache) Lookup(key string) (data []byte, ok bool) { /* ... */ }

// Good — the type synchronizes internally, so document it at the type
// A Watcher reports the health of some entity.
//
// Watcher methods are safe for simultaneous use by multiple goroutines.
type Watcher interface{ /* ... */ }
```

**Rationale**: Excess concurrency annotations are clutter; missing annotations on surprising APIs are bugs. Google Best Practices §Documentation — Concurrency: "Go users assume that conceptually read-only operations are safe for concurrent use and do not require extra synchronization... Mutating operations, however, are not assumed to be safe for concurrent use." Document only when the default assumption is wrong, when a mutating-looking method is actually safe, or when the safety is part of a type-wide contract.

---

## DC-24: Context Semantics — Only Document the Surprising

**Strength**: SHOULD

**Summary**: By default, a `context.Context` cancellation interrupts the function and returns `ctx.Err()`. Don't restate this. Do document when the context has special requirements (no deadline, particular values attached) or when cancellation behavior is non-standard.

```go
// Good — standard behavior; don't restate
// Run executes the worker's run loop.
func (Worker) Run(ctx context.Context) error { /* ... */ }

// Good — non-standard: returns nil on cancellation
// Run executes the worker's run loop.
//
// If the context is cancelled, Run returns a nil error.
func (Worker) Run(ctx context.Context) error { /* ... */ }

// Good — context has preconditions
// NewReceiver starts receiving messages sent to the specified queue.
// The context should not have a deadline.
func NewReceiver(ctx context.Context) *Receiver { /* ... */ }

// Bad — restates the default
// Run executes the worker's run loop. The method will process work until
// the context is cancelled and accordingly returns an error.
func (Worker) Run(ctx context.Context) error { /* ... */ }
```

**Rationale**: "Cancels when ctx is cancelled" is the default assumption for every context-accepting function; writing it wastes the reader's attention. What matters is what's different: non-standard error on cancel, alternate cancellation mechanisms, or value-attached expectations. Google Best Practices §Documentation — Contexts: "It is implied that the cancellation of a context argument interrupts the function it is provided to... This fact does not need to be restated" (Google Best Practices §Contexts).

---

## DC-25: Testable Examples — `ExampleX` Functions

**Strength**: SHOULD

**Summary**: Add runnable examples in `*_test.go` files as functions named `ExampleX`, `ExampleX_variant`, or `Example` (package-level). Examples appear in godoc and are executed by `go test`.

```go
// Good — in example_test.go, appears attached to Duration in godoc
func ExampleDuration_String() {
    fmt.Println(5 * time.Second)
    // Output: 5s
}

// Good — variant example for the same function
func ExampleSplit_separator() {
    fmt.Printf("%q\n", strings.Split("a,b,c", ","))
    // Output: ["a" "b" "c"]
}

// Good — package-level example
func Example() {
    cfg, err := auth.LoadConfig("auth.yaml")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(cfg.Issuer)
    // Output: https://auth.example.com
}
```

**Rationale**: Testable examples double as documentation and tests. The `// Output:` line is compared against stdout; stale examples become failing tests. They appear inline in godoc attached to the documented symbol. Google Decisions §Examples: "Packages should clearly document their intended usage. Try to provide a runnable example; examples show up in Godoc. Runnable examples belong in the test file, not the production source file." Full testing patterns are covered in chapter 07 (Google Decisions §Examples; Effective Go §Testable examples).

**See also**: CI-42

---

## DC-26: README Is the Project's Front Door

**Strength**: SHOULD

**Summary**: A Go module's `README.md` should introduce the project, show installation, include a minimal usage example, link to godoc, and note licensing. Keep it short and actionable; move long prose to `doc.go` so godoc has it.

```markdown
# mypkg

A short description in one or two sentences.

[![Go Reference](https://pkg.go.dev/badge/example.com/mypkg.svg)](https://pkg.go.dev/example.com/mypkg)
[![Go Report Card](https://goreportcard.com/badge/example.com/mypkg)](https://goreportcard.com/report/example.com/mypkg)

## Install

    go get example.com/mypkg

## Usage

    package main

    import (
        "fmt"
        "example.com/mypkg"
    )

    func main() {
        c, err := mypkg.NewClient("addr")
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(c.Ping())
    }

See the [godoc](https://pkg.go.dev/example.com/mypkg) for the full API.

## License

MIT — see LICENSE.
```

**Rationale**: A README and `godoc` have different jobs: the README sells and orients; godoc is the reference. Duplicate them and they diverge. Keep the README focused on the first five minutes of using the package: what it is, how to install, a snippet, a link to the reference. The `pkg.go.dev` badge is standard; the Go Report Card badge is common but optional. Project-level organization (where READMEs live in `cmd/` vs. the module root) is covered in chapter 10.

**See also**: DC-05, DC-27

---

## DC-27: API Stability Is Communicated in the Doc

**Strength**: SHOULD

**Summary**: If a package, type, or function is experimental, internal-only, or unstable, say so in the doc comment. Tag pre-release API surfaces with explicit wording — tooling does not infer stability from the module version alone.

```go
// Good
// Package internal/experiment contains preview features. The API is not
// covered by the project's compatibility guarantee and may change or be
// removed without notice.
package experiment

// Good — per-symbol unstable marker
// BatchRetry sends items in parallel with retries.
//
// This function is experimental and may change in a future minor release.
// Use at your own risk; pin a specific module version if stability matters.
func BatchRetry(ctx context.Context, items []Item) ([]Result, error) { /* ... */ }

// Good — Go 1 compatibility promise; use the package comment
// Package foo is part of the v2 API. The v1 API remains in
// example.com/foo and is frozen.
package foo
```

**Rationale**: Go modules follow SemVer (`v0` is pre-stable, `v1+` is stable, `v2+` uses a path suffix like `/v2`), but the tag alone doesn't tell users which individual functions are stable. An explicit note in the doc prevents users from building critical systems on APIs that will change. There is no Go-team mandate for stability annotations, but the convention is pervasive in the standard library (`internal/` packages, the `x/exp` module, `vendor/`).

---

## DC-28: Don't Over-Document the Obvious

**Strength**: SHOULD

**Summary**: Not every parameter needs prose. A doc that only restates names and types ("format is the format, and data is the interpolation data") adds nothing. Document the surprising and leave the rest.

```go
// Good — documents the non-obvious behavior
// Sprintf formats according to a format specifier and returns the
// resulting string.
//
// If the data does not match the expected format verbs or the amount of
// data does not satisfy the format specification, Sprintf inlines
// warnings about formatting errors into the output string.
func Sprintf(format string, data ...any) string { /* ... */ }

// Bad — restates the signature
// Sprintf formats according to a format specifier and returns the
// resulting string.
//
// format is the format, and data is the interpolation data.
func Sprintf(format string, data ...any) string { /* ... */ }
```

**Rationale**: Doc comments that parrot the signature add maintenance cost with zero information gain. Google Best Practices §Parameters: "Not every parameter must be enumerated in the documentation... Document the error-prone or non-obvious fields and parameters by saying why they are interesting." The same principle applies to return values — document semantics (`returns io.EOF at end`, `returns a nil slice for empty results`), not types.

**See also**: DC-07, DC-09

---

## DC-29: Comment Exported-but-Unclear Types and Generic Type Parameters

**Strength**: SHOULD

**Summary**: When a type name doesn't fully convey its purpose (single-letter generic parameters, exported wrappers around anonymous types, tag-style types), add prose that explains the meaning and constraints.

```go
// Good — generic type parameter documented
// OrderedMap is a map that preserves insertion order.
//
// K is the key type; it must be comparable. V is the value type and has
// no constraint beyond being a Go type.
type OrderedMap[K comparable, V any] struct { /* ... */ }

// Good — a type alias that needs explanation
// Duration is a length of time in nanoseconds. Values outside the range
// of int64 nanoseconds (~292 years) are not representable.
type Duration int64

// Good — exported marker type
// FullyQualifiedName is a domain name ending in a dot, matching the
// convention used by DNS wire format. Use [ParseFQDN] to construct.
type FullyQualifiedName string

// Bad — single-letter type with no doc
type OrderedMap[K comparable, V any] struct { /* ... */ }
```

**Rationale**: Generic type parameters are constrained by syntax (`comparable`, `any`, interface constraints), but constraints don't convey intent. A single sentence distinguishes a map that cares about ordering from one that cares about keys being hashable. For alias types (`type Duration int64`), the underlying type gives no hint — the doc carries the meaning. The Go Doc Comments spec doesn't single out generics, but the same "first word is the name" rule applies.

---

## DC-30: Comments on Stuttering Names Should Not Stutter

**Strength**: CONSIDER

**Summary**: If the package name stutters into the exported name (`bytes.Buffer` — good; `user.UserService` — bad), don't amplify the problem in the doc comment. Start with the bare name as the reader will refer to it.

```go
// Good — in package user
// Service manages user accounts. Use [NewService] to construct.
type Service struct { /* ... */ }

// In a call site, this reads as user.Service — no stutter.

// Bad — stuttering name amplified by stuttering comment
// UserService manages user accounts. Use [NewUserService] to construct
// a new UserService.
type UserService struct { /* ... */ }
```

**Rationale**: Godoc renders the package-qualified name (`user.Service`) in headers; the doc comment shouldn't repeat the package name. This is a corollary of CI-05 (short, purpose-named packages) and the "start with the identifier" rule — the identifier is `Service`, not `user.Service`. See Google Decisions §Repetitive names (referenced throughout) for the broader rule on stuttering (Google Decisions §Repetitive names; Effective Go §Names).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Doc comment on every exported name | MUST | `go doc` surfaces these; missing comments = blank docs |
| 02 | Start comment with the identifier name | SHOULD | `"NewClient returns..."` reads naturally |
| 03 | Full, punctuated sentences | SHOULD | Field end-of-line comments may be fragments |
| 04 | Package comment precedes `package` | MUST | No blank line; starts with `Package <name>` |
| 05 | `doc.go` for long package docs | CONSIDER | Separate prose from implementation |
| 06 | Binary packages describe the command | SHOULD | `"The xyz command ..."`, not `"Package main ..."` |
| 07 | Comment non-obvious struct fields | SHOULD | End-of-line for short; above for long |
| 08 | Document unexported non-obvious code | SHOULD | Same rule: start with the identifier name |
| 09 | Comments explain *why*, not *what* | MUST | Internal comments surface intent, not narration |
| 10 | Delete commented-out code | MUST | Version control preserves history |
| 11 | `TODO(owner)` marks incomplete work | SHOULD | Owner + ticket, not bare `TODO` |
| 12 | `BUG(author):` prefix for known bugs | CONSIDER | Surfaced by `go doc`; use sparingly |
| 13 | `Deprecated:` paragraph marker | SHOULD | Recognized by tooling; exact form matters |
| 14 | Indent code blocks in doc comments | MUST | Godoc's only code-block mechanism |
| 15 | Lists with `-`/`*`/`N.` (Go 1.19+) | SHOULD | Separated from prose by a blank line |
| 16 | `[PackageName]` links (Go 1.19+) | SHOULD | Bracketed identifiers become hyperlinks |
| 17 | Headings with `#` (Go 1.19+) | CONSIDER | Prefer over the older capitalized-line form |
| 18 | No Markdown — respect godoc | MUST | No `**bold**`, no fences, no `[text](url)` |
| 19 | Blank `//` separates paragraphs | SHOULD | Otherwise runs together as one paragraph |
| 20 | No hard line-length limit | CONSIDER | Wrap at 80–100 for source readability |
| 21 | Document error conventions | SHOULD | Sentinels, typed errors, pointer vs value |
| 22 | Document cleanup requirements | SHOULD | Call `Stop`, `Close`, `cancel()` |
| 23 | Concurrency contract when non-default | SHOULD | Reads assumed safe, writes not |
| 24 | Context semantics when non-standard | SHOULD | Don't restate the default behavior |
| 25 | Testable examples (`ExampleX`) | SHOULD | Double as docs and tests |
| 26 | README is the project front door | SHOULD | Install, usage, godoc link, license |
| 27 | Mark unstable API explicitly | SHOULD | SemVer doesn't cover per-symbol stability |
| 28 | Don't over-document the obvious | SHOULD | Document the surprising, skip the signature |
| 29 | Clarify generics and marker types | SHOULD | Type constraints don't convey intent |
| 30 | Non-stuttering comments | CONSIDER | `Service` in package `user`, not `UserService` |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` — CI-42 (Doc Comments Are Full Sentences) is the starting point this chapter extends. CI-05 (package names) underlies DC-04 and DC-30.
- **API Design**: See `02-api-design.md` for constructor naming and option patterns; those names are what doc comments document.
- **Error Handling**: See `03-error-handling.md` for error wrapping and sentinel values (extends DC-21).
- **Testing**: See `07-testing.md` for the full treatment of testable examples and `go test` integration (DC-25 is the documentation-facing slice).
- **Project Structure**: See `10-project-structure.md` for where `README.md`, `doc.go`, and `cmd/` READMEs live (extends DC-05, DC-26).
- **Anti-Patterns**: See `09-anti-patterns.md` for patterns that produce stale or misleading comments (extends DC-09, DC-10).

---

## External References

- [Go Doc Comments](https://go.dev/doc/comment) — the canonical specification for godoc syntax, introduced alongside the Go 1.19 formatting changes (links, lists, headings). This is the authoritative source for DC-14 through DC-18.
- [*Effective Go* — Commentary](https://go.dev/doc/effective_go#commentary) — the foundational Go-team guide to doc comments.
- [`go doc` reference](https://pkg.go.dev/cmd/go#hdr-Show_documentation_for_package_or_symbol) — command-line documentation tool that reads the comments this chapter describes.
- [*pkgsite* (pkg.go.dev source)](https://pkg.go.dev/golang.org/x/pkgsite/cmd/pkgsite) — the documentation server; use `pkgsite` locally to preview docs before publishing.
- [The Go Blog — Godoc: documenting Go code](https://blog.golang.org/godoc-documenting-go-code) — historical context on the conventions.
- [*Google Go Style Guide* — Decisions §Commentary and Best Practices §Documentation](https://google.github.io/styleguide/go/) — the most detailed enterprise-style codification.
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — reinforces the naming and structural conventions that make comments consistent across a codebase.
- [`staticcheck` SA1019](https://staticcheck.dev/docs/checks#SA1019) — the deprecation check that reads `Deprecated:` markers.
