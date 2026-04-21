---
name: go-guidelines
description: |
  Comprehensive Go best practices, idioms, and anti-patterns grounded in the
  Uber Go Style Guide, the Google Go Style Guide (Style Guide, Decisions,
  Best Practices), Effective Go, and the official Go spec.
  Use when: writing new Go code, refactoring existing Go, reviewing Go for
  issues, designing package APIs, handling errors with `errors.Is`/`%w`,
  propagating `context.Context`, wiring concurrency (channels, goroutines,
  `sync`), writing table-driven tests with `testing`, profiling with
  `testing.B` and `pprof`, organizing modules and packages, writing
  `godoc`-visible doc comments, or building Gio desktop UIs.
---

# Go Coding Guidelines Skill

## Overview

This skill gives you the condensed wisdom of the Go community's two most authoritative style guides — Uber and Google — reconciled with *Effective Go*, the Go spec, and a corpus of AI-audited anti-patterns. The guides are split by topic into twelve chapters. Each entry is a numbered pattern with a strength indicator (MUST / SHOULD / CONSIDER / …), a summary, paired Good/Bad Go snippets, a rationale, and cross-references. Every chapter ends with a Quick Reference Table summarising all of its patterns.

The target environment is **Go 1.22+** (some patterns reference 1.24 and 1.25 features — `b.Loop`, `synctest`, `os.Root`, `weak.Pointer`, `AddCleanup`, `T.Context`, `T.Chdir`, `slices.Sorted`, `maps.Keys`, `WithoutCancel`). The default toolchain is **`gofmt` + `goimports` + `go vet` + `staticcheck`**, the default test runner is **`go test`**, and the default dependency philosophy is **standard library first**.

## When to Use This Skill

Activate this skill when the task involves:

- Writing new Go code
- Refactoring existing Go code
- Reviewing Go code for issues, bugs, or style drift
- Designing package APIs, exported types, interface boundaries
- Handling errors with `fmt.Errorf("%w", …)`, `errors.Is`, `errors.As`, sentinel values
- Propagating `context.Context` through call chains, timeouts, cancellation
- Writing goroutines, channels, `sync.Mutex`/`sync.WaitGroup`, pipelines, fan-in/fan-out
- Writing tests: table-driven tests, subtests, fuzzing, benchmarks, `t.Helper()`, `t.Cleanup()`
- Profiling performance, escape analysis, allocation, inlining
- Organising modules, packages, and internal package boundaries
- Writing `godoc`-visible doc comments and package-level documentation
- Building **Gio desktop UIs** (window construction, widget state, macOS Cocoa threading, event routing)
- Triaging generated Go for security, concurrency, and idiomatic-style regressions

## Document Locations

All guideline documents are in `knowledge/go/guides/`:

**Core chapters (12):**

- `01-core-idioms.md` — Declarations, naming, `gofmt`, control flow, shared idioms
- `02-api-design.md` — Package boundaries, exported surfaces, functional options, constructors
- `03-error-handling.md` — `error` contract, wrapping, sentinels, `errors.Is`/`As`, panics
- `04-type-design.md` — Struct layout, zero values, validated types, generics constraints
- `05-interfaces-methods.md` — Small interfaces, accept-interfaces/return-concrete, typed-nil, method sets
- `06-concurrency.md` — Goroutines, channels, `context`, `sync`, lifecycle, cancellation
- `07-testing.md` — `testing`, table-driven, subtests, fuzz, `synctest`, `b.Loop`, `T.Context`/`T.Chdir`
- `08-performance.md` — Profiling, allocation, escape analysis, `sync.Pool`, slices, maps, inlining
- `09-anti-patterns.md` — What NOT to do: 56 concrete traps, each with fix
- `10-project-structure.md` — Modules, packages, `internal/`, layout, `go.mod` discipline
- `11-documentation.md` — Doc comments, `godoc`, package docs, READMEs, examples
- `12-gio-ui.md` — Gio (`gioui.org`) window, widgets, theme, macOS threading, event routing

**Supporting material:**

- `knowledge/go/sources/md/` — The authoritative upstream style guides (Google, Uber) in markdown form
- `knowledge/go/concept-cards/` — Single-pattern reference cards distilled from the upstream guides
- `knowledge/go/workbench/` — Provenance records for how each pattern was accepted into the guides

Guides are the normative artefact. Sources and concept cards are there when you need deeper rationale, original wording, or edge-case examples.

## Document Selection Guide

Load documents based on the task. Anti-patterns (chapter 09) is the cheap safety net — load it first on any Go task.

| Task | Load These Documents |
|------|---------------------|
| **Any Go code** | `09-anti-patterns.md` (always load first) |
| **New code from scratch** | `01-core-idioms.md`, `09-anti-patterns.md`, `10-project-structure.md` |
| **Implementing a new feature** | `01-core-idioms.md`, `03-error-handling.md`, `05-interfaces-methods.md` |
| **API design** | `02-api-design.md`, `05-interfaces-methods.md`, `04-type-design.md` |
| **Error handling** | `03-error-handling.md`, `09-anti-patterns.md` |
| **Type design / struct layout** | `04-type-design.md`, `02-api-design.md`, `08-performance.md` |
| **Interfaces & methods** | `05-interfaces-methods.md`, `02-api-design.md` |
| **Concurrency, goroutines, channels** | `06-concurrency.md`, `09-anti-patterns.md`, `03-error-handling.md` |
| **Context propagation** | `06-concurrency.md` (CC-08…CC-12), `02-api-design.md` |
| **Writing tests** | `07-testing.md`, `03-error-handling.md` |
| **Benchmarks / profiling** | `07-testing.md` (TE-36, TE-41), `08-performance.md` |
| **Performance optimisation** | `08-performance.md`, `07-testing.md`, `09-anti-patterns.md` |
| **Refactoring** | `09-anti-patterns.md`, then topic-specific |
| **Code review / quality audit** | `09-anti-patterns.md` (scan PREFIX-NN list), topic-specific |
| **Module / repository layout** | `10-project-structure.md`, `02-api-design.md` |
| **Documentation** | `11-documentation.md`, `02-api-design.md` |
| **Security / crypto / SQL / JWT** | `09-anti-patterns.md` (AP-46…AP-56) |
| **Gio desktop UI** | `12-gio-ui.md`, then `06-concurrency.md` for goroutine/window lifecycle |

## Workflow

### For Writing New Code

1. **Load anti-patterns first**: Read `09-anti-patterns.md` — know what NOT to do before writing a line.
2. **Load core idioms**: Read `01-core-idioms.md` for declarations, naming, control flow, `gofmt` discipline.
3. **Load topic-specific docs**: Based on what you're building (error handling, concurrency, interfaces, …).
4. **Structure the package**: One package per directory, clear boundary, `doc.go` or package comment on `package foo`.
5. **Write code**: Small interfaces, `context.Context` as first param on blocking calls, `%w` on every wrap, `defer` for unwind discipline.
6. **Self-review**: Walk the anti-patterns table one last time. Run `gofmt`, `go vet`, `staticcheck`.

### For Building a Gio UI

1. **Load the Gio chapter**: Read `12-gio-ui.md` — Gio's API is small but its event model is surprising. GI-04 in particular prevents a silent macOS deadlock.
2. **Load concurrency**: Read `06-concurrency.md` — the Gio event loop must run on the main goroutine; all blocking work goes to goroutines that communicate via channels or `app.Window.Invalidate()`.
3. **Construct the window**: `new(app.Window)` + `win.Option(...)` (GI-01), never `app.NewWindow(...)`.
4. **Persist widget state as struct fields** (GI-02), allocate the theme once (GI-03), and on macOS call `app.Main()` from `main()` directly (GI-04).
5. **Mind the event model**: Keyboard `key.Event`/`key.EditEvent` have different delivery rules (GI-09); `pointer.InputOp` merges; `PassOp` controls overlay propagation (GI-08).

### For Error Handling

1. **Load `03-error-handling.md`** plus **AP-01…AP-08** in `09-anti-patterns.md`.
2. **Return, don't panic**: Errors are values. `panic` is for programmer invariants, not expected failure modes.
3. **Wrap with `%w`** whenever you add context. Compare with `errors.Is` (sentinels) or `errors.As` (typed).
4. **Sentinel errors are `var Err… = errors.New(…)`** at package level, documented.
5. **Never discard errors** — `_ = foo()` is a bright-line anti-pattern except at documented boundaries.

### For Concurrency

1. **Load `06-concurrency.md`** plus the CC-\* rows of the anti-patterns chapter.
2. **Every goroutine must have a clear lifecycle**: a way to start, a way to signal stop, and a way to wait for completion.
3. **`context.Context` is the first parameter** on every blocking call. Never store it in a struct field except in well-justified cases (CC-11).
4. **`defer cancel()`** immediately after `ctx, cancel := context.WithCancel(...)`.
5. **Channel discipline**: the *sender* closes, the *receiver* does not. `nil` channel blocks forever — useful for disabling a `select` case.

### For Testing

1. **Load `07-testing.md`**.
2. **Table-driven by default**: `tests := []struct{ name string; …; want … }{…}`; iterate with `t.Run(tc.name, …)`.
3. **`t.Helper()`** on every assertion helper so failures point at the caller, not the helper.
4. **`t.Cleanup()`** for teardown that should run even if the test failed. **`t.Context()`** (1.24+) for a context scoped to the test.
5. **Benchmarks use `b.Loop()`** (1.24+) — `for b.Loop()` is safer than `for i := 0; i < b.N; i++` because the toolchain prevents compiler dead-code elimination.
6. **`synctest`** (1.25+) for deterministic time-based testing.

### For Refactoring

1. **Load `09-anti-patterns.md`** first.
2. **Scan the code for each PREFIX-NN** you recognise (note the ID for commit messages).
3. **Load the affirmative chapter** for anything you want to replace.
4. **Refactor one pattern at a time**, run `go test ./...` after each.
5. **Reference pattern IDs in commit messages** (e.g. `refactor(errors): replace string-check with errors.Is (AP-04)`).

### For Code Review

1. **Load `09-anti-patterns.md`** and walk AP-01…AP-56.
2. **Load topic chapters** based on what the PR touches (concurrency? errors? APIs?).
3. **Check for context propagation, error wrapping, goroutine lifecycle, receiver consistency, typed-nil returns, sentinel comparisons, and `defer` placement** — these are the recurring regressions.
4. **Report findings by pattern ID** for unambiguous follow-up.

## Critical Rules (Always Apply)

These rules should be followed in ALL Go code without needing to load documents:

### Formatting and Tooling

```go
// All Go code is gofmt-clean. Always.
// `goimports` manages imports. `go vet` + `staticcheck` are non-negotiable.
// If your editor does not run gofmt on save, fix your editor.
```

### Error Handling

```go
// Bad — error dropped
result, _ := parseConfig(path)

// Bad — string-based error identity
if err.Error() == "not found" { /* … */ }

// Bad — loses chain
if err != nil {
    return fmt.Errorf("parse: %v", err)
}

// Good — wrap with %w, compare with errors.Is/As
if err != nil {
    return fmt.Errorf("parse %s: %w", path, err)
}
if errors.Is(err, fs.ErrNotExist) { /* … */ }

var pathErr *fs.PathError
if errors.As(err, &pathErr) { /* … */ }
```

### Context

```go
// Bad — ctx stored in struct, ctx not first param, context.TODO() in production
type Server struct { ctx context.Context } // almost always wrong
func Fetch(url string, ctx context.Context) (…) // ctx is the first param

// Good
func (s *Server) Fetch(ctx context.Context, url string) (…, error) {
    req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    // …
}
```

### Interfaces

```go
// Bad — big interface, returned to the caller
type UserService interface { /* 20 methods */ }
func NewUserService() UserService { … } // returning an interface forces typed-nil bugs

// Good — accept interfaces, return concrete types
type UserReader interface { ReadUser(ctx context.Context, id string) (User, error) }
func NewPostgresUsers(pool *pgxpool.Pool) *PostgresUsers { … } // concrete return
```

### Concurrency

```go
// Bad — unbounded goroutine, no cancellation, no waiting
go doWork(x)

// Bad — WaitGroup.Add inside the goroutine races
for _, x := range xs {
    go func(x int) { wg.Add(1); defer wg.Done(); … }(x)
}

// Good — bounded lifetime: start, signal, wait
ctx, cancel := context.WithCancel(parent)
defer cancel()
var wg sync.WaitGroup
for _, x := range xs {
    wg.Add(1)
    go func(x int) {
        defer wg.Done()
        doWork(ctx, x)
    }(x)
}
wg.Wait()
```

### Zero Values

```go
// Good — zero value is useful. A caller should not need a constructor
// just to get a valid empty thing.
var buf bytes.Buffer     // ready to use
var mu  sync.Mutex       // ready to use
var tbl map[string]int   // NOT ready — nil map panics on write. Use make(…).
```

### Defer Discipline

```go
// Good — always pair the resource acquisition with a defer
f, err := os.Open(path)
if err != nil { return err }
defer f.Close() // for read-only files, err from Close is usually safe to drop

ctx, cancel := context.WithTimeout(parent, 5*time.Second)
defer cancel()

mu.Lock()
defer mu.Unlock()
```

### Testing

```go
// Good — table-driven with subtests, t.Helper() on assertions
func TestParse(t *testing.T) {
    tests := []struct {
        name    string
        input   string
        want    Config
        wantErr error
    }{
        {"empty", "", Config{}, nil},
        {"invalid", "garbage", Config{}, ErrMalformed},
    }
    for _, tc := range tests {
        t.Run(tc.name, func(t *testing.T) {
            got, err := Parse(tc.input)
            if !errors.Is(err, tc.wantErr) {
                t.Fatalf("err = %v, want %v", err, tc.wantErr)
            }
            if diff := cmp.Diff(tc.want, got); diff != "" {
                t.Errorf("Parse() mismatch (-want +got):\n%s", diff)
            }
        })
    }
}
```

### Gio UI

```go
// Bad — app.NewWindow does not exist
win := app.NewWindow(app.Title("x"))

// Good — Gio window is a zero-value struct + Option()
win := new(app.Window)
win.Option(app.Title("x"), app.Size(unit.Dp(800), unit.Dp(600)))

// macOS: app.Main() MUST run on the main goroutine.
// Do NOT wrap it in `go func() { app.Main() }()` — it silently deadlocks.
func main() {
    go runWindow() // your event logic in a goroutine
    app.Main()     // blocks the main goroutine; returns only on exit
}
```

## Pattern ID Reference

Each chapter uses a prefix for pattern IDs. Cross-references throughout the guides use these prefixes.

| Prefix | Chapter |
|--------|---------|
| `CI-NN`  | `01-core-idioms.md` |
| `API-NN` | `02-api-design.md` |
| `EH-NN`  | `03-error-handling.md` |
| `TD-NN`  | `04-type-design.md` |
| `IM-NN`  | `05-interfaces-methods.md` |
| `CC-NN`  | `06-concurrency.md` |
| `TE-NN`  | `07-testing.md` |
| `PF-NN`  | `08-performance.md` |
| `AP-NN`  | `09-anti-patterns.md` |
| `PS-NN`  | `10-project-structure.md` |
| `DC-NN`  | `11-documentation.md` |
| `GI-NN`  | `12-gio-ui.md` |

## Strength Indicators

The guides use a graded strength scale. MUST/MUST-NOT are non-negotiable; SHOULD/SHOULD-NOT are firm conventions; CONSIDER/CONSIDER-AVOID depend on context. The `-AVOID` variants are used in the anti-patterns chapter, where the entry's title is itself the thing to avoid.

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness, safety, or interop | Always follow |
| **MUST-NOT** | Forbidden (breaks correctness, safety, or interop) | Never do this |
| **MUST-AVOID** | Anti-pattern; listed thing is forbidden | Never write this |
| **SHOULD** | Strong project/community convention | Follow unless specific reason not to |
| **SHOULD-NOT** | Strong convention against | Avoid unless specific justification |
| **SHOULD-AVOID** | Anti-pattern; listed thing is strongly discouraged | Don't write this |
| **CONSIDER** | Context-dependent recommendation | Evaluate case by case |
| **CONSIDER-AVOID** | Context-dependent discouragement | Evaluate case by case |

## Example Usage

### Task: "Write an HTTP handler that fetches a user by ID with a timeout"

1. Load: `09-anti-patterns.md`, `01-core-idioms.md`, `06-concurrency.md`, `03-error-handling.md`.
2. Apply:
   - **CC-10** Pass `ctx` as the first parameter; derive a timeout with `context.WithTimeout`; `defer cancel()`.
   - **IM-17** Return concrete types; return untyped `nil` (never a typed nil) on the error path.
   - **EH-01 / EH-36** Wrap errors with `%w`; define sentinel `ErrUserNotFound` at package level.
   - **AP-02** Use `errors.Is(err, ErrUserNotFound)`, not `strings.Contains(err.Error(), "not found")`.
   - **AP-16** Don't write `panic(err)` in a handler; return `http.Error(w, …, http.StatusInternalServerError)`.
   - **DC-01** Doc-comment the handler with a full sentence starting with the function name.

### Task: "Review a concurrent pipeline for correctness"

1. Load: `09-anti-patterns.md`, `06-concurrency.md`, `03-error-handling.md`.
2. Check:
   - **CC-38…CC-51** Channel direction, `WaitGroup.Add` before goroutine start, `defer wg.Done`, `defer cancel`, graceful shutdown, bounded goroutine semaphore.
   - **CC-08…CC-12** Context propagation, no `context.Context` stored in struct, `WithoutCancel` where detachment is intentional.
   - **AP-09…AP-15** No goroutine leak, no `time.After` inside loops, no unbuffered-channel deadlock, no `close()` by the receiver.
   - **TE-40** Is this testable under `synctest`?

### Task: "Design a public API for a config loader"

1. Load: `02-api-design.md`, `05-interfaces-methods.md`, `04-type-design.md`, `11-documentation.md`.
2. Apply:
   - **API-41** Functional options (`Option func(*Config)`) over huge parameter lists.
   - **API-42** Dependency injection over package-level globals.
   - **IM-01 / IM-17** Small interfaces at the consumer boundary; return concrete types from constructors.
   - **TD-37** Validated types — return errors from `NewLoader` when inputs are malformed.
   - **DC-01 / DC-02** Every exported name has a godoc comment starting with the identifier's name.

### Task: "Performance review of a hot loop that allocates too much"

1. Load: `08-performance.md`, `07-testing.md`, `09-anti-patterns.md`.
2. Apply:
   - **PF-36** Reuse slice backing arrays via `s = s[:0]`.
   - **PF-37** Direct indexing beats range-with-copy for large structs.
   - **PF-40** Beware interface boxing on hot paths (alloc per call).
   - **PF-47** Multi-accumulator tricks for ILP.
   - **TE-41** Re-run benchmarks with `b.Loop()` to prevent compiler dead-code elimination.
   - **TE-36** Use `testing.AllocsPerRun` and `-benchmem` to verify allocations actually dropped.

### Task: "Add tests for a time-sensitive scheduler"

1. Load: `07-testing.md`, `06-concurrency.md`.
2. Apply:
   - **TE-40** Use `testing/synctest` (Go 1.25+) so virtual time is deterministic.
   - **TE-42** `t.Context()` for the test-scoped context; `t.Chdir()` for test-scoped working directory.
   - **TE-43** Write tests in a companion `_test` package to exercise the public API.
   - **CC-23** Recover per-goroutine and surface the panic through the test's error channel.

### Task: "Build a Gio UI with a keyboard shortcut handler"

1. Load: `12-gio-ui.md`, `06-concurrency.md`.
2. Apply:
   - **GI-01** `new(app.Window)` + `win.Option(...)`.
   - **GI-02** Widget state as struct fields — not per-frame locals.
   - **GI-03** Allocate the theme once; reuse across frames.
   - **GI-04** On macOS, run `app.Main()` on the main goroutine; move your loop into `go runWindow()`.
   - **GI-05** Consume the `Tab` key explicitly if you want it routed to your handler.
   - **GI-09** Use `key.Event` for shortcuts; `key.EditEvent` is text-input only.

### Task: "Triage SQL injection / JWT / crypto issues in a codebase"

1. Load: `09-anti-patterns.md` (AP-46…AP-56).
2. Check:
   - **AP-46** Parameterised queries only; never `fmt.Sprintf` into SQL.
   - **AP-47** `defer rows.Close()` on every `*sql.Rows`.
   - **AP-48 / AP-49** AES-GCM (not ECB); fresh nonce per encryption.
   - **AP-50** Never set `InsecureSkipVerify: true` in production.
   - **AP-51** `crypto/rand`, never `math/rand`, for secrets and tokens.
   - **AP-53 / AP-54** Pin JWT algorithm, verify server-side identity, never trust client claims.
   - **AP-56** Checked integer conversions (`math/big` or range-check) when crossing size boundaries.

## Integration Notes

- **Code blocks use `go` syntax** with the `// Good` / `// Bad` comment convention (mirrors the `✅` / `❌` idiom used elsewhere, but in Go-native form).
- **Pattern IDs are `PREFIX-NN`** (e.g. `AP-17`, `CC-42`). Numbers are stable within a chapter; fold-merges preserve the lower number.
- **Cross-references in-guide** use `See also: CC-08, EH-17` style at the end of an entry.
- **Each chapter ends with a Quick Reference Table** summarising every pattern in that chapter — use it as a compressed index before loading the full guide.
- **Strength labels are uppercase** (`MUST`, `SHOULD`, `MUST-AVOID`). Consistent casing lets you `grep` for everything at a given severity.
- **`knowledge/go/sources/md/`** holds the upstream source material (Google's four-doc set plus Uber's six sections). When a pattern cites an upstream source the citation uses the upstream doc's own section anchor.
- **`knowledge/go/concept-cards/`** holds single-pattern cards — useful when you want the distilled reference without pulling in an entire chapter.
- **`knowledge/go/workbench/skills-accepted.md`** records which patterns were accepted from which workbench repos, with merge decisions and distribution across chapters.

## Quick Reference for Common Tasks

| I want to… | Read this |
|------------|-----------|
| Write any Go code | Start with `09-anti-patterns.md`, then `01-core-idioms.md` |
| Design an API / exported surface | `02-api-design.md` |
| Handle errors | `03-error-handling.md` (and `09-anti-patterns.md` AP-01…AP-08) |
| Lay out types and structs | `04-type-design.md` |
| Define interfaces, method sets, receivers | `05-interfaces-methods.md` |
| Write goroutines, channels, context | `06-concurrency.md` |
| Pass context through a call chain | `06-concurrency.md` (CC-08…CC-12) |
| Write table-driven tests | `07-testing.md` (TE-01…TE-15) |
| Write benchmarks | `07-testing.md` (TE-36, TE-41) + `08-performance.md` |
| Profile and optimise performance | `08-performance.md` |
| Review for anti-patterns | `09-anti-patterns.md` (walk all 56) |
| Lay out a module / repository | `10-project-structure.md` |
| Write `godoc` comments | `11-documentation.md` |
| Build a Gio desktop UI | `12-gio-ui.md` |
| Secure SQL, crypto, JWT, TLS | `09-anti-patterns.md` (AP-46…AP-56) |
| Triage a typed-nil return bug | `05-interfaces-methods.md` (IM-17) |
| Recover from a panic in a goroutine | `06-concurrency.md` (CC-42) |
| Understand zero-value usefulness | `04-type-design.md` (TD-01…TD-05) |
| Use `%w`, `errors.Is`, `errors.As` | `03-error-handling.md` (EH-01, EH-04, EH-07) |
| Test time-sensitive code deterministically | `07-testing.md` (TE-40 `synctest`) |
