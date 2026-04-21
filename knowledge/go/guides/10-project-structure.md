# Go Project Structure

Conventions for organizing Go modules, packages, files, tests, and build configuration. This chapter covers the *structural skeleton* — the decisions that shape a repository before application code is written: module layout, package boundaries, import paths, dependency discipline, and the build environment. Grounded in the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), *Effective Go*, and the official Go modules reference.

Target environment: **Go 1.22+**, **Go modules** (no GOPATH), **`gofmt` + `goimports` + `go vet` + `staticcheck`**, **`go test` with the standard `testing` package**.

This chapter is deliberately pragmatic: Go's tooling (the `go` command, the compiler, `go mod`) imposes most of the structural rules. The remaining decisions are small. Where Uber and Google differ from looser "Go Standard Project Layout" community conventions, this guide follows Uber and Google — they are authoritative; `github.com/golang-standards/project-layout` is not.

---

## PS-01: One Package Per Directory

**Strength**: MUST

**Summary**: Every directory in a module contains the source files of exactly one package. The Go compiler enforces this — files in the same directory must all declare the same `package` name (the sole exception being `_test` packages, which live alongside).

```
// Good — one package per directory
myproject/
├── go.mod
├── config/
│   ├── config.go           // package config
│   └── config_test.go      // package config (or config_test)
├── server/
│   ├── server.go           // package server
│   ├── handler.go          // package server
│   └── server_test.go      // package server
└── storage/
    ├── storage.go          // package storage
    └── storage_test.go     // package storage
```

```
// Bad — trying to put two packages in one directory
myproject/
└── util/
    ├── strings.go          // package stringutil
    └── times.go            // package timeutil   ← compile error
```

**Rationale**: The directory is the unit of compilation; the package is the unit of import. Conflating them would break `go build`. The directory path (relative to the module root) also becomes the import path, so splitting concerns across directories is the only way to create separate importable units. Google Best Practices §Package size: "A good reason to give each package its own directory is if you expect to open source your project in the future." The Go specification treats the directory as the package's compilation unit.

**See also**: PS-02, PS-04

---

## PS-02: The Directory Name Should Match the Package Name

**Strength**: SHOULD

**Summary**: The last element of a directory path and the `package` declared inside it should be the same. Mismatches force every importer to rename, which is noise.

```go
// Good — directory is config, package is config
// file: internal/config/config.go
package config

// Importers use the matching name:
import "example.com/myproject/internal/config"
// ... config.Load(...)
```

```go
// Bad — directory is configuration, package is cfg
// file: internal/configuration/cfg.go
package cfg

// Importers must rename or accept a mismatch:
import cfg "example.com/myproject/internal/configuration"
```

**Rationale**: When the directory name and package name diverge, readers of `import` statements have to mentally map one to the other, and import aliasing becomes obligatory. Uber §Import Aliasing: "Import aliasing must be used if the package name does not match the last element of the import path." Avoiding the mismatch removes the need for the alias entirely. Google Decisions §Import renaming: "good package names should not require renaming."

**Exception**: When the directory holds generated code whose import path is fixed (e.g., a proto-generated `_go_proto` directory), the package name may differ. Use an alias consistently.

**See also**: PS-05, PS-12

---

## PS-03: Binaries Live Under `cmd/<binary-name>/main.go`

**Strength**: SHOULD

**Summary**: For a module that produces one or more executables, place each binary's entry point in `cmd/<name>/main.go`. The directory name becomes the binary name (`go build ./cmd/server` produces `server`).

```
// Good — clear binary layout
myservice/
├── go.mod
├── internal/
│   ├── server/
│   │   └── server.go
│   └── config/
│       └── config.go
├── cmd/
│   ├── server/
│   │   └── main.go          // go build ./cmd/server -> ./server
│   └── migrate/
│       └── main.go          // go build ./cmd/migrate -> ./migrate
└── README.md
```

```go
// cmd/server/main.go — thin wrapper
package main

import (
    "context"
    "fmt"
    "os"

    "example.com/myservice/internal/config"
    "example.com/myservice/internal/server"
)

func main() {
    cfg, err := config.Load(os.Args[1:])
    if err != nil {
        fmt.Fprintln(os.Stderr, "config:", err)
        os.Exit(2)
    }
    if err := server.Run(context.Background(), cfg); err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
}
```

**Rationale**: `cmd/<name>` is a community-standard layout (not explicitly mandated by Uber or Google, but universally observed in open source Go codebases and in Google-internal `main` packages). It lets one module ship multiple binaries without polluting the root, keeps each binary's `main` thin, and makes `go install ./cmd/...` build them all. Keeping `main` thin also lets the bulk of the logic be tested at package level rather than end-to-end.

**See also**: PS-04, PS-20, PS-21

---

## PS-04: Use `internal/` for the Language-Enforced Privacy Boundary

**Strength**: SHOULD

**Summary**: Packages under a directory named `internal/` are importable only by code rooted at the parent directory. This is a *language* rule enforced by the Go compiler, not a convention.

```
// Good — internal/ enforces privacy
example.com/myproject/
├── go.mod
├── cmd/
│   └── server/
│       └── main.go                 // may import internal/...
├── internal/
│   ├── server/
│   │   └── server.go               // internal/server — not importable outside myproject
│   └── storage/
│       └── storage.go              // internal/storage — same
└── api/
    └── api.go                      // part of the public API
```

```go
// In some other module:
import "example.com/myproject/internal/server"
// ← compile error: use of internal package not allowed
```

**Rationale**: Before `internal/`, Go packages had only two visibility states: importable and nonexistent. `internal/` adds a third: importable within a module (or subtree), private elsewhere. This is the right tool for code that needs to be shared across packages in your module but is *not* part of your public API surface. Uber and Google both publish libraries using `internal/` heavily; the Go standard library itself uses it (`net/http/internal`, `crypto/internal`, etc.).

**Placement**: `internal/` may appear at any level — the privacy boundary is "the parent of `internal/`." Placing it at the module root hides a package from all external consumers; placing it deeper (`pkg/foo/internal/...`) hides it only from code outside `pkg/foo/`.

**See also**: PS-06, PS-07

---

## PS-05: Prefer Short, Lowercase, Single-Word Package Names

**Strength**: MUST

**Summary**: Package names are lowercase, short, and a single word with no underscores or `MixedCaps`. The name is typed at every call site (`pkg.Thing`), so brevity matters.

```go
// Good
package user
package httputil
package tabwriter
package oauth2
package k8s
```

```go
// Bad
package Users            // capitalized
package user_service     // underscores
package userService      // camelCase
package management_api   // both
```

**Rationale**: Go's cross-file naming convention relies on qualified identifiers being readable. `tabwriter.NewWriter` reads cleanly; `TabWriter.NewWriter` or `tab_writer.NewWriter` does not. Google Decisions §Package names: "package names must be concise and use only lowercase letters and numbers... Multi-word package names should remain unbroken and in all lowercase." Uber §Package Names: "All lower-case. No capitals or underscores. Not plural. For example, `net/url`, not `net/urls`." Core-idioms CI-05 introduced this rule; this chapter expands on directory correspondence (see PS-02) and on package-size considerations (see PS-13).

**Exception**: Test-only package names may contain underscores (`foo_test`, `gmailintegration_test`) — see PS-15.

**See also**: PS-02, PS-15

---

## PS-06: Do Not Use `pkg/` as a Top-Level Directory

**Strength**: SHOULD-AVOID

**Summary**: Do not place your public library code under a directory called `pkg/` at the module root. The `pkg/` prefix is an anti-pattern that adds a meaningless segment to every import path and conveys no information.

```
// Bad — pkg/ prefix adds noise without meaning
example.com/myproject/
├── cmd/
│   └── server/main.go
└── pkg/
    ├── server/            // imported as example.com/myproject/pkg/server
    ├── storage/
    └── config/
```

```
// Good — package directories sit at the module root
example.com/myproject/
├── cmd/
│   └── server/main.go
├── server/                // imported as example.com/myproject/server
├── storage/
└── config/
```

**Rationale**: `pkg/` is not part of the official Go project layout. It originated in the `github.com/golang-standards/project-layout` repository, which the Go team has explicitly disclaimed as a community document rather than an official standard. The directory adds one redundant path segment — every import becomes `example.com/myproject/pkg/thing` instead of `example.com/myproject/thing`. Neither Uber's nor Google's style guide prescribes `pkg/`, and no Go standard-library subtree uses it.

The `internal/` directory (PS-04) is a real, language-enforced construct. `pkg/` is not. If you need to distinguish "library" code from "binary" code, `internal/` (for private-within-module) and the module root (for public) already do that.

**Note**: This is a community convention, not a Uber- or Google-specified rule. It is widespread in the Go ecosystem and consistent with the absence of `pkg/` in `std`, Kubernetes' `staging/src/`, `etcd`, and Uber's own open-source Go repositories.

**See also**: PS-04, PS-07

---

## PS-07: Library Versus Application Layouts Differ

**Strength**: SHOULD

**Summary**: A module whose primary artifact is a library (imported by others) should be flat. A module whose primary artifact is a binary should use `cmd/` and `internal/`. Do not mix the layouts.

```
// Good — library layout (flat, public API at root)
example.com/mylib/
├── go.mod
├── mylib.go                // package mylib
├── encode.go               // package mylib
├── decode.go               // package mylib
├── encode_test.go
└── internal/
    └── parser/             // library-internal helper
        └── parser.go
```

```
// Good — application layout (cmd/ for binary, internal/ for logic)
example.com/myservice/
├── go.mod
├── cmd/
│   └── myservice/main.go
├── internal/
│   ├── server/
│   └── storage/
└── README.md
```

**Rationale**: Libraries are consumed by `import "example.com/mylib"`; keeping the public types at the module root makes that import short and meaningful. Applications are consumed as binaries; `cmd/<name>` makes the entry points discoverable and `internal/` prevents the application's implementation from becoming an accidental public API. The standard library itself demonstrates the library layout (packages sit directly under `src/`), while open-source Go services demonstrate the application layout.

**Mixed modules** (library + CLI) exist — e.g., `gopls`, `hugo`, `kubectl`. The convention there is: put the library at the root, the binary under `cmd/<name>`. The library remains importable; the binary exists alongside.

**See also**: PS-03, PS-04

---

## PS-08: Avoid `util`, `common`, `helpers`, `shared`, `lib`

**Strength**: SHOULD-AVOID

**Summary**: Packages named for *how* they are used (utility, helper, common) rather than *what* they do (httputil, strconv, timeconv) accrete unrelated code, obscure ownership, and produce import conflicts.

```go
// Bad
package util        // util for what?
package common      // common to what?
package helpers     // help with what?
package shared      // shared between what?
package lib         // literally "library"

// Good — name by content domain
package stringutil  // operates on strings
package httputil    // helpers for HTTP
package timeconv    // time conversion
package retry       // retry logic
```

**Rationale**: Uber §Package Names: "Not 'common', 'util', 'shared', or 'lib'. These are bad, uninformative names." Google Decisions §Package names: "Avoid uninformative package names like `util`, `utility`, `common`, `helper`, `model`, `testhelper`, and so on that would tempt users of the package to rename it when importing." Google Best Practices §Util packages adds: "it can be used as *part* of the name though" — so `httputil` and `stringutil` are fine, since the name still conveys what the package operates on.

Such packages also tend to attract dependencies — every other package in the codebase ends up importing `util`, making it impossible to break apart later. Core-idioms CI-06 introduced this rule; this chapter emphasizes the structural consequences.

**See also**: PS-05, PS-09

---

## PS-09: Do Not Repeat the Package Name in Its Symbols

**Strength**: SHOULD

**Summary**: Exported symbols are qualified by their package at the call site (`pkg.Name`), so including the package name in the symbol produces repetition (`pkg.PkgName`). Name symbols for what they mean within the package.

```go
// Bad
package yamlconfig

func ParseYAMLConfig(input string) (*Config, error)
// Call site: yamlconfig.ParseYAMLConfig(s)  ← "YAMLConfig" twice

// Good
package yamlconfig

func Parse(input string) (*Config, error)
// Call site: yamlconfig.Parse(s)
```

```go
// Bad
package creditcard

type CreditCardService struct{}
// Call site: creditcard.CreditCardService  ← "creditcard" twice

// Good
package creditcard

type Service struct{}
// Call site: creditcard.Service
```

**Rationale**: Package names are part of every qualified identifier. Repeating the package name in the symbol is like saying "`user.UserName`" or "`http.HTTPClient`" — the package already qualifies it. Google Best Practices §Avoid repetition: "For functions, do not repeat the name of the package." Google Decisions §Repetition gives the canonical examples; `bytes.Buffer`, `ring.New`, `strings.Reader` all use short, contextual names precisely because the package qualifies them.

**Exception**: When two packages export the same symbol name and callers import both, adding a disambiguator is acceptable — but prefer renaming one import (see PS-11).

**See also**: PS-05, PS-11

---

## PS-10: Group Imports — Standard Library First, Then Everything Else

**Strength**: SHOULD

**Summary**: Use two import groups separated by a blank line: standard library first, then third-party and local. Google's style permits additional groups for generated-proto and side-effect imports. `goimports` produces this layout automatically.

```go
// Good — Uber-style: two groups
import (
    "context"
    "fmt"
    "os"

    "github.com/pkg/errors"
    "go.uber.org/zap"
    "example.com/myproject/internal/config"
)
```

```go
// Good — Google-style: up to four groups
import (
    // 1. Standard library
    "context"
    "fmt"

    // 2. Other (project and vendored) packages
    "github.com/dsnet/compress/flate"
    "google.golang.org/protobuf/proto"

    // 3. Protocol Buffer imports
    foopb "myproj/foo/proto/proto"

    // 4. Side-effect imports
    _ "myproj/rpc/protocols/dial"
)
```

```go
// Bad — one mashed-together group
import (
    "context"
    "example.com/myproject/internal/config"
    "fmt"
    "github.com/pkg/errors"
    "os"
)
```

**Rationale**: Grouping separates dependencies by lifetime and origin: standard-library is always available, third-party is pinned by `go.mod`, side-effect imports have ordering implications, proto imports have distinct rename rules. Uber §Import Group Ordering: "There should be two import groups: Standard library, Everything else." Google Decisions §Import grouping lists the four groups. Both agree on the minimum: stdlib first, separated by a blank line. Core-idioms CI-04 introduced this rule at an idiom level; this chapter explains the structural rationale.

**See also**: PS-11

---

## PS-11: Use Import Aliases Only When the Package Name Does Not Match, or to Avoid Conflicts

**Strength**: SHOULD

**Summary**: Alias an import only when (a) the package name differs from the last path element (forced rename) or (b) two imports collide. Otherwise, use the natural name.

```go
// Good — package name doesn't match path
import (
    "net/http"

    client "example.com/client-go"         // package is "client", path ends in "client-go"
    trace "example.com/trace/v2"           // "v2" is not the package name
)

// Good — collision between two trace packages
import (
    "runtime/trace"                         // keep the stdlib name

    nettrace "golang.net/x/trace"           // alias the less-common one
)

// Bad — gratuitous alias
import (
    runtimetrace "runtime/trace"            // no conflict; no need to rename
)
```

**Rationale**: Aliases add a level of indirection between what's imported and how it's referenced. Overuse obscures code. Uber §Import Aliasing: "In all other scenarios, import aliases should be avoided unless there is a direct conflict between imports." Google Decisions §Import renaming lists four legitimate cases: collision, generated proto, uninformative upstream name (`v1`, `util`), and local-variable shadowing. None of them include cosmetic or preference-based aliases.

When an alias is needed, the aliased name follows the package-name rules (PS-05): lowercase, no underscores.

**See also**: PS-02, PS-05, PS-10

---

## PS-12: Do Not Use `import .`

**Strength**: MUST-AVOID

**Summary**: The `import .` form brings exported identifiers into scope without qualification. It makes code harder to read and tool-hostile.

```go
// Bad
package foo_test

import (
    "bar/testutil"
    . "foo"
)

var myThing = Bar()          // where does Bar come from? No qualifier.
```

```go
// Good
package foo_test

import (
    "bar/testutil"
    "foo"
)

var myThing = foo.Bar()      // clear origin
```

**Rationale**: Qualified identifiers (`pkg.Name`) are one of Go's readability anchors. `import .` defeats it and also creates resolution ambiguity for tools and readers. Google Decisions §Import "dot": "Do **not** use this feature in the Google codebase; it makes it harder to tell where the functionality is coming from." This rule has no known legitimate use case in Go.

**See also**: PS-10

---

## PS-13: Right-Size Packages — Neither One Big Package Nor Many Tiny Ones

**Strength**: SHOULD

**Summary**: A package should be large enough that its types interact meaningfully and small enough that its public API fits on one page in `godoc`. Do not put your entire project in one package; do not create one-type-per-package.

```
// Good — packages map to cohesive domains
myproject/
├── storage/               // one package, several related types
│   ├── store.go           // Store type
│   ├── transaction.go     // Transaction type (tightly coupled to Store)
│   └── index.go           // internal Index helper
└── auth/                  // separate domain, separate package
    ├── auth.go
    └── session.go
```

```
// Bad — one package per type
myproject/
├── store/store.go
├── transaction/transaction.go     // forced to export internals to work with Store
├── index/index.go                 // same
└── session/session.go
```

**Rationale**: Packages are Go's encapsulation boundary. Types within the same package can access each other's unexported fields; types in different packages cannot. Over-splitting forces what should be internal details to be exported, bloating the public API. Under-splitting creates packages that do too many unrelated things and attract every other package as an importer. Google Best Practices §Package size: "If *client code* is likely to need two values of different type to interact with each other, it may be convenient for the user to have them in the same package... if you have a few related types whose *implementation* is tightly coupled, placing them in the same package lets you achieve this coupling without polluting the public API." Canonical examples: `net/http` is large (`Client`, `Server`, `Cookie`, `Request`, `Response` all together); `expvar` is small (one file, one concept).

**Heuristic**: If a hypothetical user would have to import both `A` and `B` to use either in any meaningful way, they probably belong in one package.

**See also**: PS-01, PS-14

---

## PS-14: Split Large Packages Across Files by Type or Concern

**Strength**: SHOULD

**Summary**: Within one package, split source across multiple files grouped by the type or concern they implement. There is no "one type, one file" rule, but maintainability suffers from both thousand-line megafiles and directories of tiny files.

```
// Good — package http in the standard library
net/http/
├── client.go        // client support
├── server.go        // server support
├── cookie.go        // cookie management
├── request.go       // Request type
├── response.go      // Response type
└── ...

// Good — small focused package
encoding/csv/
├── reader.go        // CSV reading
└── writer.go        // CSV writing
```

```
// Bad — every function in its own file
myproject/auth/
├── login.go             // one function
├── logout.go            // one function
├── validate.go          // one function
├── hash.go              // one function
└── ... (30 more)

// Bad — one 4000-line file with everything
myproject/auth/
└── auth.go          // login, logout, validation, hashing, session, middleware...
```

**Rationale**: The standard library's own structure is the canonical reference: `net/http`, `encoding/csv`, and `os` all split by concern. Google Best Practices §Package size: "As a rule of thumb, files should be focused enough that a maintainer can tell which file contains something, and the files should be small enough that it will be easy to find once there." Splitting also helps version control — concurrent work on different concerns avoids merge conflicts.

**See also**: PS-13, PS-17

---

## PS-15: Tests Live Next to Source in `_test.go` Files

**Strength**: MUST

**Summary**: Go's testing tool picks up files named `*_test.go` from the same directory as the code under test. Do not place tests in a separate directory tree. For external (black-box) tests that exercise only the public API, use a `package foo_test` declaration in the same directory.

```
// Good — tests next to source
storage/
├── storage.go           // package storage
├── storage_test.go      // package storage       — same-package (white-box) tests
├── storage_ext_test.go  // package storage_test  — external (black-box) tests
└── index.go
```

```go
// storage_test.go — same-package tests, can access unexported
package storage

func TestInternalIndex(t *testing.T) {
    s := &Store{idx: newIndex()}  // idx is unexported — OK, same package
    // ...
}

// storage_ext_test.go — external tests, public API only
package storage_test

import (
    "testing"

    "example.com/myproject/storage"
)

func TestPublicAPI(t *testing.T) {
    s, err := storage.New(...)  // must use exported surface
    // ...
}
```

```
// Bad — tests in a separate directory
myproject/
├── storage/
│   └── storage.go
└── tests/
    └── storage_test.go    // won't be run by `go test ./storage/...`
```

**Rationale**: The `testing` tool is designed around the `_test.go` convention: same-package tests verify internals; `_test` suffix tests verify the public API from a consumer's perspective. Splitting them into a `tests/` directory breaks tool support (`go test ./...` would find them, but `go test -cover ./storage/...` would not attribute coverage correctly). Google Decisions §Test package: "tests may be defined in the same package as the code being tested... Place the tests in a `foo_test.go` file [with] `package foo`." Same section on `_test` packages: "use a package name with the `_test` suffix. This is an exception to the 'no underscores' rule." Detailed test organization patterns are in chapter 07.

**See also**: PS-16, chapter 07 (testing)

---

## PS-16: Put Shared Test Helpers in a `<pkg>test` Package

**Strength**: SHOULD

**Summary**: When multiple packages need the same test fixtures, doubles, or helpers, put them in a companion package whose name is the original package name plus `test` — e.g., `creditcard` → `creditcardtest`. Mark it as test-only in your build system if possible.

```
// Good — companion test-helper package
myproject/
├── creditcard/
│   ├── creditcard.go               // package creditcard
│   └── creditcard_test.go
└── creditcardtest/
    └── creditcardtest.go           // package creditcardtest — stubs, fakes
```

```go
// creditcardtest/creditcardtest.go
package creditcardtest

import (
    "example.com/myproject/creditcard"
    "example.com/myproject/money"
)

// Stub stubs creditcard.Service and provides no behavior of its own.
type Stub struct{}

func (Stub) Charge(*creditcard.Card, money.Money) error { return nil }

// AlwaysDeclines stubs creditcard.Service and simulates declined charges.
type AlwaysDeclines struct{}

func (AlwaysDeclines) Charge(*creditcard.Card, money.Money) error {
    return creditcard.ErrDeclined
}
```

**Rationale**: Same-package `_test.go` tests can't export helpers to consumers of the real package. A companion `<pkg>test` package exports fixtures for other packages to use in *their* tests, while remaining conceptually separate from production code. Google Best Practices §Test double and helper packages: "A safe choice is to append the word `test` to the original package name ('creditcard' + 'test')... `creditcardtest.Stub` is strictly preferable to... `StubCreditCardService`."

This is distinct from `package foo_test` (external tests of `foo`, which live in `foo/`'s directory) — `<pkg>test` is its own package in its own directory, intended to be imported by other tests.

**See also**: PS-15, chapter 07

---

## PS-17: Package Documentation Goes in a Package Comment, Often in `doc.go`

**Strength**: SHOULD

**Summary**: Every package should have a single package-level doc comment starting with `Package <name>`. For short comments, attach it to the primary source file. For long comments, put it in a dedicated `doc.go` file containing only the comment and the `package` clause.

```go
// Good — short package doc on the primary file
// Package config loads and validates service configuration
// from environment variables and command-line flags.
package config

// ... rest of the file
```

```go
// Good — long package doc in doc.go
// file: storage/doc.go
// Package storage implements a transactional key-value store
// backed by Badger, with support for multi-version concurrency
// and point-in-time snapshots.
//
// # Overview
//
// A Store is created with New(...) and must be closed with Close.
// All reads and writes occur within transactions.
//
// # Transactions
//
// Transactions are created with Store.Begin. A transaction sees
// a consistent snapshot of the store from the moment it began...
package storage
```

```go
// Bad — no package comment
package config

func Load(...) { /* ... */ }
```

**Rationale**: `godoc` and `pkg.go.dev` render the package comment as the package's landing page. A package without a doc comment is effectively undocumented. Google Decisions §Package comments: "Package comments must appear immediately above the package clause with no blank line between the comment and the package name." Google Best Practices §Package size: "Packages with long package documentation may choose to dedicate one file called `doc.go` that has the package documentation, a package declaration, and nothing else, but this is not required." The `doc.go` convention is widely observed in the standard library (e.g., `database/sql/doc.go`, `crypto/doc.go`). Detailed commentary conventions are in chapter 11.

**See also**: PS-14, chapter 11 (documentation)

---

## PS-18: Module Path Matches the Directory Tree

**Strength**: MUST

**Summary**: The module path declared in `go.mod` is the prefix of every package import path in the module. A package located at `<module-root>/a/b/c` is imported as `<module-path>/a/b/c`. The module path is fixed; the directory structure under it mirrors import paths exactly.

```go
// go.mod
module example.com/myproject

go 1.22
```

```
// Directory structure
myproject/
├── go.mod
├── server/               // package server
│   └── server.go
└── internal/
    └── storage/          // package storage
        └── storage.go
```

```go
// Imports must match the directory layout
import (
    "example.com/myproject/server"
    "example.com/myproject/internal/storage"
)
```

**Rationale**: The `go` command resolves import paths by matching the module path prefix and then walking the rest of the path as directories. There is no configurable mapping. The module path also appears in every published version (`example.com/myproject v1.3.0`) and must be globally unique — typically rooted at a VCS URL you control (`github.com/user/repo`, `example.com/product`). Once the module path is chosen, changing it is a breaking change for every importer.

**Version suffix**: For v2+, the module path includes a `/v2` suffix (e.g., `example.com/myproject/v2`). This lets v1 and v2 coexist as different modules. See the Go modules reference.

**See also**: PS-19

---

## PS-19: `go.mod` and `go.sum` Are Source-Controlled and Discipline-Managed

**Strength**: MUST

**Summary**: `go.mod` declares the module's dependencies; `go.sum` pins cryptographic hashes of those dependencies. Both files are committed to version control. They are updated by `go get`, `go mod tidy`, and `go mod edit` — not by hand — and changes to them are reviewed like any other source change.

```
// go.mod — human-readable, hand-editable, but prefer the go tool
module example.com/myservice

go 1.22

require (
    github.com/stretchr/testify v1.9.0
    go.uber.org/zap v1.27.0
)

require (
    // Indirect dependencies — pinned transitively
    github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
    github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
)
```

**Update discipline**:

- **Add a dependency**: `go get example.com/foo@v1.2.3`
- **Update to latest minor/patch**: `go get -u example.com/foo`
- **Remove unused + tidy**: `go mod tidy`
- **Verify integrity**: `go mod verify`

**Rationale**: `go.mod` is the single source of truth for what the module depends on. `go.sum` ensures that every build pulls the same bytes for every dependency (build reproducibility). Deleting `go.sum` or skipping `go mod tidy` in review creates supply-chain risk and merge noise. Committing both files lets `go build` work for fresh checkouts without running any separate dependency-install step.

**Owner**: Typically one or two maintainers per repo review dependency bumps. Automated tools (Dependabot, Renovate) that open PRs bumping `go.mod` are the norm at Uber, Google, and most serious Go shops.

**See also**: PS-20, PS-23

---

## PS-20: Fewer Dependencies Is Better

**Strength**: SHOULD

**Summary**: Every direct dependency is a commitment: to track its releases, audit its security posture, and reconcile its transitive dependencies with yours. Before adding a dependency, prefer the standard library or a small, focused in-module helper.

```go
// Good — use standard library where it suffices
import "encoding/json"

data, err := json.Marshal(v)
```

```go
// Bad — pulling in a large dependency for something stdlib does
import "github.com/some-org/mega-json-lib"
```

```go
// Good — tiny in-module helper
// internal/stringutil/stringutil.go
package stringutil

func Truncate(s string, n int) string {
    if len(s) <= n {
        return s
    }
    return s[:n]
}
```

```go
// Bad — 15MB dependency for one helper
import "github.com/big-util-collection/stringhelper"
```

**Rationale**: The Go standard library is comprehensive and high-quality. Adding a dependency to avoid writing 20 lines of glue code often pulls in several hundred transitive dependencies, slows builds, expands the attack surface, and creates version-conflict risk. Go's build tool does not support dependency deduplication across major versions, so transitive version pins can force unwanted upgrades. Neither Uber nor Google explicitly codifies this as a style rule, but both organizations (and the Go team) are well-known for preferring stdlib over third-party. This is a community convention, widely observed.

**Rules of thumb**:

- Do not take a dependency on a one-function library.
- Prefer maintained libraries with stable APIs and active releases.
- Review the transitive dependency graph before adding — `go mod graph`.

**See also**: PS-19, PS-22

---

## PS-21: Use Semantic Import Versioning for v2+

**Strength**: MUST

**Summary**: Go enforces semantic import versioning: modules at major version v2 and above must include the major version in their import path (`example.com/foo/v2`). v0 and v1 share the unversioned path.

```go
// Good — v2+ uses /v2 suffix
// go.mod
module example.com/foo/v2

go 1.22

// Importers:
import "example.com/foo/v2"
```

```go
// Good — v0 and v1 share the unversioned path
// go.mod
module example.com/foo

go 1.22

// Importers:
import "example.com/foo"
```

```
// Bad — v2 without the suffix
module example.com/foo      // but publishing v2.0.0 — breaks consumers
```

**Rationale**: Semantic import versioning lets v1 and v2 of the same module coexist in a single build. Without the `/v2` suffix, the build system cannot distinguish them, and Go refuses to let you depend on both. The rule is baked into the `go` command: publishing `v2.0.0` of a module whose path does not include `/v2` will fail validation. See the Go modules reference for details on major-version suffixes.

**For v0 modules**: No API compatibility is implied. Breaking changes are allowed. This is the conventional phase for "early development."

**For v1+ modules**: Follow Semver strictly. Breaking changes require a major-version bump (`/v2`). API design concerns are covered in chapter 02.

**See also**: PS-18, PS-19

---

## PS-22: Vendor Only When You Have a Reason

**Strength**: CONSIDER

**Summary**: `go mod vendor` copies all dependencies into a `vendor/` directory at the module root. Do this only when you have a specific reason: air-gapped builds, regulatory requirements, or ensuring bit-for-bit reproducibility beyond what `go.sum` provides. The default (no vendor directory, dependencies fetched from module proxy) is preferred.

```
// Vendored layout (only when needed)
myproject/
├── go.mod
├── go.sum
├── vendor/
│   ├── modules.txt
│   └── github.com/
│       └── ...            // full copy of every dependency
└── ...
```

**When to vendor**:

- Builds must succeed without network access (air-gapped CI, offline deployment).
- Regulatory or licensing audit requires a snapshot of every line of dependency code.
- You need to patch a dependency temporarily and want the patch to live in the repo.

**When not to vendor**:

- Default case. `go.sum` + the module proxy give you reproducibility without the directory bloat.
- Small projects where the vendor directory doubles or triples the repo size.
- Rapid-development projects where dependency updates are frequent.

**Rationale**: Before Go modules, vendoring was the standard way to pin dependencies. With modules and `go.sum`, it's optional. `go build` honors `vendor/` if present (defaults to `-mod=vendor`), but most CI today uses `-mod=readonly` against the module proxy. Neither Uber's nor Google's open-source style guides mandate vendoring; Google-internal code uses a different mechanism (monorepo vendoring via Bazel). This is community convention, not Uber/Google-specified.

**See also**: PS-19

---

## PS-23: Use `replace` Directives Sparingly, and Never in Published Modules

**Strength**: SHOULD

**Summary**: The `replace` directive in `go.mod` substitutes one module path for another, typically to point to a local directory or fork. It is ignored when the module is imported as a dependency — it only affects the module where it's declared. Use it for local development and private forks; never rely on it for published library releases.

```
// Good — local development of two modules side by side
// myservice/go.mod
module example.com/myservice

go 1.22

require example.com/mylib v1.0.0

replace example.com/mylib => ../mylib      // local path for dev
```

```
// Good — emergency fork
replace github.com/broken/lib v1.2.3 => github.com/myorg/lib-fork v1.2.3-patched
```

```
// Bad — relying on replace in a library
// mylib/go.mod (published as v1.0.0)
module example.com/mylib

replace github.com/foo/bar => github.com/myfork/bar v1.0.0   // consumers won't see this
```

**Rationale**: `replace` is consulted only for the main module (the one being built). Published libraries' `replace` directives are ignored by importers. A library that depends on a `replace` to resolve its own dependencies is unusable — consumers will pick up the unreplaced version. For development ergonomics (editing two modules in parallel), prefer `go.work` (see PS-26).

**See also**: PS-19, PS-26

---

## PS-24: Generated Code Lives Alongside Hand-Written Code, in the Same Package

**Strength**: SHOULD

**Summary**: When a tool generates Go source (protobuf, mock implementations, enum-to-string code, `stringer`), the generated file lives in the package that consumes it. Use `go generate` directives and a conventional filename (often ending in `_gen.go` or `.pb.go`).

```
// Good — generated code in the same package as its consumers
rpc/
├── service.go              // hand-written
├── service.pb.go           // generated from service.proto
├── service_grpc.pb.go      // generated gRPC stubs
└── mock/                   // generated mocks — separate package
    └── mock_service.go
```

```go
// service.go — directive triggers generation
package rpc

//go:generate protoc --go_out=. --go-grpc_out=. service.proto
//go:generate mockgen -destination=mock/mock_service.go -package=mock . Service

type Service interface {
    DoWork(ctx context.Context, req *Request) (*Response, error)
}
```

**Conventions**:

- Name generated files to signal origin: `*.pb.go`, `*_gen.go`, `*_string.go`, `zz_generated_*.go` (Kubernetes convention).
- Put a "DO NOT EDIT" header at the top — `goimports` and `gofmt` honor it; humans are warned.
- Commit generated code to the repository so consumers don't need the generator installed (library OOBE principle, carried over from Rust).
- Run `go generate ./...` in CI to verify the checked-in generated code is up to date.

**Rationale**: Generated code is source. Treating it as "not real code" (gitignored, regenerated at build time) creates the exact problems Rust's "Libraries Work Out of the Box" rule avoids: consumers need the generator toolchain, CI builds depend on external tools, and regression bugs slip in silently. Neither Uber's nor Google's public style guide codifies `go generate` structurally, but both organizations commit generated proto code extensively (see Kubernetes, gRPC-Go). This is community convention, grounded in the behavior of `go generate` and the Go standard library's own practices (e.g., `golang.org/x/tools/cmd/stringer`).

**See also**: PS-13, PS-19

---

## PS-25: Examples Belong in `_test.go` (Testable) or `examples/` (Runnable)

**Strength**: SHOULD

**Summary**: Go supports two kinds of examples:

1. **Testable examples** in `_test.go` files — functions named `ExampleXxx` with an `// Output:` comment. These run as tests (`go test`), appear in `godoc`, and ensure the example stays correct.
2. **Runnable examples** under an `examples/` directory at the module root — full programs that demonstrate library use. These are standalone `main` packages.

```go
// Good — testable example in _test.go
// file: bytes/example_test.go
package bytes_test

import (
    "bytes"
    "fmt"
)

func ExampleBuffer() {
    var b bytes.Buffer
    b.Write([]byte("Hello, "))
    fmt.Fprintf(&b, "world!")
    fmt.Println(b.String())
    // Output: Hello, world!
}
```

```
// Good — runnable example directory
mylib/
├── mylib.go
└── examples/
    ├── basic/
    │   └── main.go          // package main — a full, runnable demo
    └── advanced/
        └── main.go
```

**Rationale**: Testable examples are enforced by the compiler and `go test` — they cannot drift. `pkg.go.dev` surfaces them prominently. Runnable examples in `examples/` are for demonstrations too complex for a single function (multi-file setup, config files, CLI demos). Neither `testdata/` nor `examples/` is magic to the `go` tool — `testdata/` is ignored by `go test` by convention, and `examples/` is just a directory.

Both approaches are referenced in Google Decisions §Examples and the Go blog's "Testable Examples in Go."

**See also**: PS-15, chapter 11

---

## PS-26: Use `go.work` for Multi-Module Development

**Strength**: CONSIDER

**Summary**: When a single repository contains multiple modules — or when you're editing multiple related modules across repositories — a `go.work` file (Go 1.18+) lets you treat them as a unit during development without needing `replace` directives.

```
// Good — monorepo with multiple modules
my-platform/
├── go.work
├── services/
│   ├── api/
│   │   ├── go.mod              // module example.com/platform/api
│   │   └── ...
│   └── worker/
│       ├── go.mod              // module example.com/platform/worker
│       └── ...
└── libs/
    ├── logger/
    │   ├── go.mod              // module example.com/platform/logger
    │   └── ...
    └── config/
        ├── go.mod              // module example.com/platform/config
        └── ...
```

```
// go.work
go 1.22

use (
    ./services/api
    ./services/worker
    ./libs/logger
    ./libs/config
)
```

**When to use `go.work`**:

- A monorepo with multiple Go modules that reference each other.
- Local development where you need to edit a library alongside its consumer without publishing a new version.

**When not to use `go.work`**:

- Single-module repositories. Just don't create a `go.work`.
- CI builds: `go.work` is typically gitignored; CI builds each module against its published dependencies.

**Convention**: Commit `go.work` if every contributor uses it (monorepo); gitignore it if it's a per-developer convenience (cross-repo editing).

**Rationale**: Before `go.work`, multi-module development required fragile `replace` directives (see PS-23). Workspaces solve this without affecting published module metadata. Neither Uber nor Google publicly specifies workspace conventions; this is community convention anchored in the Go modules reference.

**See also**: PS-23

---

## PS-27: CI for Go Looks Like `fmt + vet + test + build`

**Strength**: SHOULD

**Summary**: A conventional Go CI pipeline runs, at minimum: `gofmt` (or `goimports`) check, `go vet`, `go test -race`, `go build`. Optionally: `staticcheck`, `govulncheck`, a lint pass (`revive`, `golangci-lint`), test coverage, race-detector runs.

```yaml
# .github/workflows/go.yml — illustrative minimum
name: Go CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'

      - name: Verify formatting
        run: |
          test -z "$(gofmt -l .)"

      - name: Verify tidy
        run: |
          go mod tidy
          git diff --exit-code go.mod go.sum

      - name: Vet
        run: go vet ./...

      - name: Staticcheck
        uses: dominikh/staticcheck-action@v1

      - name: Test
        run: go test -race -coverprofile=cover.out ./...

      - name: Build
        run: go build ./...
```

**Rationale**: Go's toolchain ships most of what a CI pipeline needs — `gofmt`, `go vet`, `go test`, `go build`. Adding `staticcheck` and `govulncheck` catches most real bugs and known vulnerabilities. Running `go mod tidy` in CI and checking for a clean diff prevents dependency-file drift. The `-race` flag on `go test` catches data races that would otherwise surface in production. Neither Uber nor Google publishes a canonical YAML pipeline, but these checks are universal across Go open-source projects. This is community convention; the specific tools are Go-team-sanctioned.

**See also**: PS-19, PS-29

---

## PS-28: Build Task Runners Are Conventional but Optional

**Strength**: CONSIDER

**Summary**: Many Go repos use a `Makefile`, a `Taskfile.yml`, or `mage` to orchestrate common developer commands (`make test`, `make lint`, `make docker`). None is required — `go build`, `go test`, and `go generate` already cover most needs. Choose one tool per repo, keep it thin, and document targets.

```makefile
# Makefile — minimal and Go-idiomatic
.PHONY: build test lint tidy

build:
	go build ./...

test:
	go test -race ./...

lint:
	go vet ./...
	staticcheck ./...

tidy:
	go mod tidy
	git diff --exit-code go.mod go.sum

generate:
	go generate ./...
```

**Rationale**: A task runner is a README for humans and CI. It encodes the project's conventions — which flags to pass, what order to run things in, what to check before pushing. For small projects, a Makefile (or nothing at all) suffices; `mage` offers Go-based task definitions for larger projects; `Taskfile` offers cross-platform support. Neither Uber nor Google prescribes a specific tool — this is community convention, varying by team.

**Keep it thin**: Do not reimplement what `go` already does. A Makefile target of `go test ./...` is fine; a Makefile that tries to replace `go.mod` resolution is not.

**See also**: PS-27

---

## PS-29: Lint Configuration Lives at the Module Root

**Strength**: SHOULD

**Summary**: When using `staticcheck`, `revive`, `golangci-lint`, or similar tools, put their configuration (`.staticcheck.conf`, `revive.toml`, `.golangci.yml`) at the module root. One configuration per module, applied to the whole module.

```
// Good — single configuration at module root
myproject/
├── go.mod
├── .golangci.yml           // applies to all packages
├── staticcheck.conf        // applies to all packages
└── ...
```

```
# staticcheck.conf
checks = ["all", "-ST1000", "-ST1003"]    # enable all, disable a few
```

**Rationale**: Linter configuration is module-wide by nature — the rules should apply uniformly so that coverage is comparable across packages and CI signals are consistent. Per-package configurations create drift and confusion. Linter-specific exceptions should use inline directives (`//nolint:specific-check`) with a reason comment, not per-directory config files.

This is community convention, not explicitly Uber- or Google-specified.

**See also**: PS-27

---

## PS-30: Keep the Module Root Clean

**Strength**: SHOULD

**Summary**: The module root should hold configuration, documentation, and entry points — not application source files. Source belongs in packages (directories) organized by concern.

```
// Good — clean module root
myservice/
├── go.mod
├── go.sum
├── README.md
├── LICENSE
├── Makefile
├── .golangci.yml
├── .github/
│   └── workflows/go.yml
├── cmd/
│   └── myservice/main.go
└── internal/
    └── ...
```

```
// Bad — source files scattered at the root
myservice/
├── go.mod
├── server.go              // stray source
├── config.go              // stray source
├── handler.go             // stray source
├── server_test.go
├── util.go
└── README.md              // where does everything go?
```

**Rationale**: A developer cloning the repo should immediately see its shape: config, docs, and entry-point directories. A flat root with dozens of `.go` files is as disorienting as a deeply-nested layout. There is a legitimate exception: a *single-package library* whose entire public API fits in a few files may legitimately have those files at the root (see PS-07). The distinction is: a library's `.go` files at the root *are* the library; an application's `.go` files at the root are clutter.

This is community convention, consistent with the standard library's organization and both Uber's and Google's open-source Go repos.

**See also**: PS-03, PS-07, PS-14

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | One package per directory | MUST | Compiler-enforced; directory = compilation unit |
| 02 | Directory name matches package name | SHOULD | Avoids forced import aliases |
| 03 | Binaries in `cmd/<name>/main.go` | SHOULD | `main` stays thin, ships multiple binaries |
| 04 | `internal/` for private packages | SHOULD | Language-enforced privacy across module |
| 05 | Short, lowercase, single-word packages | MUST | No underscores, no camelCase, no plurals |
| 06 | No `pkg/` top-level directory | SHOULD-AVOID | Adds noise; not standard-library convention |
| 07 | Library vs. application layouts differ | SHOULD | Library: flat at root. App: `cmd/` + `internal/` |
| 08 | Avoid `util`/`common`/`helpers` | SHOULD-AVOID | Name by domain, not by role |
| 09 | Don't repeat package name in symbols | SHOULD | `pkg.Parse`, not `pkg.ParsePkg` |
| 10 | Group imports: stdlib first | SHOULD | Blank-line-separated groups |
| 11 | Alias imports only when needed | SHOULD | Mismatch, collision, uninformative — nothing else |
| 12 | No `import .` | MUST-AVOID | Defeats qualified identifiers |
| 13 | Right-size packages | SHOULD | Cohesive, godoc-sized, internally coupled |
| 14 | Split large packages across files | SHOULD | By concern; neither megafile nor tiny-file |
| 15 | Tests in `_test.go` next to source | MUST | White-box same-package, black-box `_test` pkg |
| 16 | Shared helpers in `<pkg>test` | SHOULD | Companion package, test-only |
| 17 | Package docs in comment, `doc.go` if long | SHOULD | "Package x ..." — renders in godoc |
| 18 | Module path = directory tree | MUST | No remapping; import paths follow layout |
| 19 | `go.mod` and `go.sum` in VCS | MUST | Edited via `go` tool; reviewed in PRs |
| 20 | Fewer dependencies is better | SHOULD | Prefer stdlib; audit before adding |
| 21 | Semver import versioning for v2+ | MUST | Path ends in `/v2`, `/v3`, etc. |
| 22 | Vendor only when needed | CONSIDER | Default: no vendor; use for air-gapped/audit |
| 23 | `replace` only for local dev | SHOULD | Never in published libraries |
| 24 | Generated code in consumer package | SHOULD | `go generate` directives; commit output |
| 25 | Examples: `_test.go` or `examples/` | SHOULD | Testable examples preferred |
| 26 | `go.work` for multi-module dev | CONSIDER | Monorepo or cross-repo editing |
| 27 | CI: `fmt + vet + test + build` | SHOULD | Add staticcheck, govulncheck, `-race` |
| 28 | Task runner optional | CONSIDER | Makefile/Taskfile/mage — pick one, keep thin |
| 29 | Lint config at module root | SHOULD | One config per module, applied uniformly |
| 30 | Keep module root clean | SHOULD | Config, docs, entry points — not scattered source |

### Layout Templates

**Library module** (imported by others):

```
example.com/mylib/
├── go.mod
├── go.sum
├── README.md
├── doc.go                  // package-level documentation
├── mylib.go                // package mylib — primary API
├── encode.go               // package mylib
├── decode.go               // package mylib
├── mylib_test.go
└── internal/
    └── parser/
        └── parser.go       // package parser (library-internal)
```

**Application module** (produces one or more binaries):

```
example.com/myservice/
├── go.mod
├── go.sum
├── README.md
├── Makefile
├── .golangci.yml
├── .github/
│   └── workflows/go.yml
├── cmd/
│   ├── myservice/
│   │   └── main.go         // package main — thin entry
│   └── migrate/
│       └── main.go
└── internal/
    ├── server/
    │   ├── server.go
    │   └── handler.go
    ├── storage/
    │   ├── storage.go
    │   └── index.go
    └── config/
        ├── config.go
        └── doc.go
```

**Multi-module workspace** (monorepo with `go.work`):

```
my-platform/
├── go.work                 // use (...) listing each module
├── services/
│   ├── api/
│   │   ├── go.mod          // module example.com/platform/api
│   │   └── ...
│   └── worker/
│       ├── go.mod          // module example.com/platform/worker
│       └── ...
└── libs/
    ├── logger/
    │   ├── go.mod          // module example.com/platform/logger
    │   └── ...
    └── config/
        ├── go.mod          // module example.com/platform/config
        └── ...
```

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for package-name rules at the idiom level (CI-05, CI-06), import grouping (CI-04), and MixedCaps (CI-07), all extended structurally here.
- **API Design**: See `02-api-design.md` for what to export vs. hide in `internal/` (extends PS-04, PS-07).
- **Error Handling**: See `03-error-handling.md` for sentinel-error placement and package-scoped error types.
- **Testing**: See `07-testing.md` for test-file organization, table-driven tests, and fixtures (extends PS-15, PS-16).
- **Documentation**: See `11-documentation.md` for package comments, doc.go style, and godoc formatting (extends PS-17).
- **Anti-Patterns**: See `09-anti-patterns.md` for `init()` abuse, stray global state, and other structural smells that amplify PS-08, PS-13.

---

## External References

- [*Effective Go* — Package names](https://go.dev/doc/effective_go#package-names) — foundational naming guidance
- [*Effective Go* — Commentary](https://go.dev/doc/effective_go#commentary) — doc comment and `doc.go` conventions
- [Go Modules Reference](https://go.dev/ref/mod) — authoritative specification of `go.mod`, `go.sum`, replace, vendor, and version suffixes
- [Go Workspaces Tutorial](https://go.dev/doc/tutorial/workspaces) — `go.work` usage
- [Go Blog: Package names](https://go.dev/blog/package-names) — canonical package-naming post
- [Go Blog: Organizing Go Code](https://go.dev/blog/organizing-go-code) — structural advice from the Go team
- [Go Blog: Testable Examples](https://go.dev/blog/examples) — `ExampleXxx` functions
- [*Uber Go Style Guide*](https://github.com/uber-go/guide) — §Package Names, §Import Group Ordering, §Import Aliasing
- [*Google Go Style Guide*](https://google.github.io/styleguide/go/) — Decisions §Package names, §Import grouping, §Package comments, §Test package; Best Practices §Package size, §Util packages, §Test double and helper packages
- [Go Code Review Comments — Package names](https://go.dev/wiki/CodeReviewComments#package-names) — the Go team's canonical reviewer checklist
- [`golang-standards/project-layout`](https://github.com/golang-standards/project-layout) — a widely-cited community repository; **note**: the Go team does not endorse it, and its `pkg/` convention is explicitly an anti-pattern in this guide (see PS-06)
- [`go vet`](https://pkg.go.dev/cmd/vet), [`staticcheck`](https://staticcheck.dev/), [`govulncheck`](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — the baseline static-analysis tools referenced in PS-27
