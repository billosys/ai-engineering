# Testing in Go

Go's `testing` package is small, opinionated, and sufficient. This chapter collects the idioms for writing Go tests that the *Uber Go Style Guide*, the *Google Go Style Guide* (Style Guide, Decisions, Best Practices), and the Go team itself all converge on: table-driven tests, subtests, `t.Helper`, `t.Cleanup`, parallel execution, `cmp.Diff` for structural comparison, stdlib-first with no assertion libraries, and tests designed so failures diagnose themselves.

Target environment: **Go 1.22+** (loop-variable fix is assumed), **standard library `testing`** is the only testing framework, **`github.com/google/go-cmp`** for deep comparison, `go test` for running, `-race` for concurrent code.

---

## TE-01: Put Tests in `_test.go` Files and Use the `testing` Package

**Strength**: MUST

**Summary**: Test code lives in files named `*_test.go` in the same directory as the code under test. These files are compiled only by `go test` and are invisible to normal builds. The standard `testing` package is the only testing framework you should use.

```go
// Good — foo_test.go next to foo.go
package foo

import "testing"

func TestFoo(t *testing.T) {
    if got, want := Foo(2), 4; got != want {
        t.Errorf("Foo(2) = %d, want %d", got, want)
    }
}
```

**Rationale**: `go test` discovers `*_test.go` files automatically, compiles them against the package (or a `_test` sibling), and runs every `TestXxx`, `BenchmarkXxx`, `ExampleXxx`, and `FuzzXxx` function. Google Decisions §Use package `testing`: "The Go standard library provides the `testing` package. This is the only testing framework permitted for Go code in the Google codebase. In particular, assertion libraries and third-party testing frameworks are not allowed." The `testing` package provides everything needed — top-level tests, benchmarks, runnable examples, subtests, logging, failures and fatal failures (Google Decisions §Use package `testing`).

**See also**: TE-02, TE-03

---

## TE-02: Test Function Names Are `TestXxx(t *testing.T)`

**Strength**: MUST

**Summary**: A test function must be named `TestXxx` where `Xxx` starts with an uppercase letter, and it takes exactly one argument of type `*testing.T`. Benchmarks are `BenchmarkXxx(b *testing.B)`, examples are `ExampleXxx()`, fuzz targets are `FuzzXxx(f *testing.F)`.

```go
// Good
func TestParse(t *testing.T)                  { /* ... */ }
func BenchmarkParse(b *testing.B)             { /* ... */ }
func ExampleParse()                           { /* ... */ }
func FuzzParse(f *testing.F)                  { /* ... */ }

// Underscores are allowed in test function names (exception to MixedCaps)
func Test_parseWithSymbols_roundtrip(t *testing.T) { /* ... */ }

// Bad — not discovered by go test
func testParse(t *testing.T)     { /* ... */ } // lowercase "test"
func TestParse(t *testing.T, x int) { /* extra param — won't compile */ }
```

**Rationale**: `go test` discovers functions by prefix and signature; anything that doesn't match is silently ignored. Underscores are specifically allowed in test, benchmark, and example names as an exception to the general MixedCaps rule. Google Decisions §Underscores: "Test, Benchmark and Example function names within `*_test.go` files may include underscores." This means `Test_feature_behavior` style names are acceptable when they improve readability (Google Decisions §Underscores; Google Decisions §Use package `testing`).

**See also**: TE-03

---

## TE-03: Use `t.Errorf` for Independent Failures, `t.Fatalf` Only When Continuing Is Pointless

**Strength**: SHOULD

**Summary**: Prefer `t.Error`/`t.Errorf` so every independent problem is reported in one run. Use `t.Fatal`/`t.Fatalf` only when subsequent assertions cannot meaningfully continue — usually because a precondition failed (setup, decode, open).

```go
// Good — every comparison runs; all failures reported
gotMean, gotVariance, err := MyDistribution(input)
if err != nil {
    t.Fatalf("MyDistribution(%v) returned unexpected error: %v", input, err)
}
if diff := cmp.Diff(wantMean, gotMean); diff != "" {
    t.Errorf("MyDistribution(%v) mean mismatch (-want +got):\n%s", input, diff)
}
if diff := cmp.Diff(wantVariance, gotVariance); diff != "" {
    t.Errorf("MyDistribution(%v) variance mismatch (-want +got):\n%s", input, diff)
}

// Good — Fatal because decoding unexpected bytes is pointless
gotEncoded := Encode(input)
if gotEncoded != wantEncoded {
    t.Fatalf("Encode(%q) = %q, want %q", input, gotEncoded, wantEncoded)
}
gotDecoded, err := Decode(gotEncoded)
if err != nil {
    t.Fatalf("Decode(%q) returned unexpected error: %v", gotEncoded, err)
}
if gotDecoded != input {
    t.Errorf("Decode(%q) = %q, want %q", gotEncoded, gotDecoded, input)
}

// Bad — Fatal on the first inequality hides the rest
if gotMean != wantMean {
    t.Fatalf("mean wrong")     // variance check never runs
}
if gotVariance != wantVariance {
    t.Fatalf("variance wrong")
}
```

**Rationale**: Tests should keep going so developers see every failure in a single run, not a sequence of "fix, rerun, next failure". Google Decisions §Keep going: "Tests should keep going for as long as possible, even after a failure, in order to print out all of the failed checks in a single run... Prefer calling `t.Error` over `t.Fatal` for reporting a mismatch." `t.Fatal` is appropriate when later checks would be meaningless or misleading, for example decoding output that is already known to be wrong (Google Decisions §Keep going; Google Best Practices §`t.Error` vs. `t.Fatal`).

**See also**: TE-04, TE-14

---

## TE-04: Write Test Failures That Identify the Function, the Input, and "got vs want"

**Strength**: SHOULD

**Summary**: A failure message should stand alone. The conventional form is `YourFunc(%v) = %v, want %v`. That gives the reader the name of the tested function, the inputs that produced the failure, the actual output, and the expected output, without requiring them to open the test source.

```go
// Good
if got := Compare(a, b); got != want {
    t.Errorf("Compare(%q, %q) = %v, want %v", a, b, got, want)
}

// Good — multiple inputs
if got, want := postLength(post), 60; got != want {
    t.Errorf("postLength(%v) = %v, want %v", post, got, want)
}

// Bad — "actual/expected" and no function or input
if got != want {
    t.Errorf("actual: %v, expected: %v", got, want)
}

// Bad — indexed failure requires counting the table
for i, tc := range tests {
    if strings.ToUpper(tc.input) != tc.want {
        t.Errorf("Failed on case #%d", i)
    }
}
```

**Rationale**: Diagnosing a failure without rereading the test saves enormous amounts of developer time across a large codebase. Google Decisions §Useful test failures covers this as four sub-rules — Identify the function, Identify the input, Got before want, Level of detail — and insists that every failure message include the function name and inputs: "In most tests, failure messages should include the name of the function that failed, even though it seems obvious from the name of the test function. Specifically, your failure message should be `YourFunc(%v) = %v, want %v` instead of just `got %v, want %v`." Test outputs should print the actual value before the expected value, using the words "got" and "want" (Google Decisions §Identify the function; §Identify the input; §Got before want).

**See also**: TE-17

---

## TE-05: Table-Driven Tests Are the Canonical Go Pattern

**Strength**: SHOULD

**Summary**: When many cases exercise the same logic with different inputs and outputs, collect them in a slice of structs and loop. Uber's convention: the slice is named `tests`, each case is `tt`, input fields are prefixed `give`, expected fields are prefixed `want`. Google's convention uses `test` and often `want`/`wantErr`. Either is acceptable; pick one per package and stay consistent.

```go
// Good — Uber style (give/want, tt iteration variable)
func TestSplitHostPort(t *testing.T) {
    tests := []struct {
        give     string
        wantHost string
        wantPort string
    }{
        {give: "192.0.2.0:8000", wantHost: "192.0.2.0", wantPort: "8000"},
        {give: "192.0.2.0:http", wantHost: "192.0.2.0", wantPort: "http"},
        {give: ":8000",          wantHost: "",          wantPort: "8000"},
        {give: "1:8",             wantHost: "1",          wantPort: "8"},
    }

    for _, tt := range tests {
        t.Run(tt.give, func(t *testing.T) {
            host, port, err := net.SplitHostPort(tt.give)
            if err != nil {
                t.Fatalf("SplitHostPort(%q) unexpected error: %v", tt.give, err)
            }
            if host != tt.wantHost {
                t.Errorf("SplitHostPort(%q) host = %q, want %q", tt.give, host, tt.wantHost)
            }
            if port != tt.wantPort {
                t.Errorf("SplitHostPort(%q) port = %q, want %q", tt.give, port, tt.wantPort)
            }
        })
    }
}

// Good — Google minimal style (no subtest names when inputs are short)
func TestCompare(t *testing.T) {
    compareTests := []struct {
        a, b string
        want int
    }{
        {"", "", 0},
        {"a", "", 1},
        {"abc", "abc", 0},
        {"ab", "abc", -1},
    }
    for _, test := range compareTests {
        got := Compare(test.a, test.b)
        if got != test.want {
            t.Errorf("Compare(%q, %q) = %v, want %v", test.a, test.b, got, test.want)
        }
    }
}
```

**Rationale**: Table-driven tests reduce duplicate logic, make it trivial to add cases, and focus the reader on the axis of variation (inputs and outputs). Uber §Test Tables: "If a system under test needs to be tested against multiple conditions where certain parts of the inputs and outputs change, a table-driven test should be used to reduce redundancy and improve readability... We follow the convention that the slice of structs is referred to as `tests` and each test case `tt`. Further, we encourage explicating the input and output values for each test case with `give` and `want` prefixes." Google Decisions §Table-driven tests agrees: "Use table-driven tests when many different test cases can be tested using similar testing logic" (Uber §Test Tables; Google Decisions §Table-driven tests).

**See also**: TE-06, TE-07, TE-08

---

## TE-06: Use `t.Run` for Subtests — Name Them for the Command Line

**Strength**: SHOULD

**Summary**: Wrap each table case in `t.Run(name, func(t *testing.T) { ... })`. The subtest name becomes part of the output and the `-run` filter, so choose short, descriptive names — "function identifier" style, not prose. Avoid spaces (replaced with underscores) and slashes (interpreted as subtest path separators).

```go
// Good — concise, filterable names
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        // ...
    })
}

// Good — input-based name when it's short and safe
t.Run(tt.give, func(t *testing.T) { /* ... */ })

// Bad — prose is awkward at the command line
t.Run("check that there is no mention of scratched records", ...)

// Bad — slashes are special; this subtest is hard to target
t.Run("AM/PM confusion", ...)
```

**Rationale**: Subtests let developers run a single case (`go test -run TestParse/empty_input`), provide per-case output scoping, and allow per-case `t.Parallel()` and `t.Cleanup`. Google Decisions §Subtest names: "Name your subtest such that it is readable in test output and useful on the command line for users of test filtering... Think of subtest names more like a function identifier than a prose description. The test runner replaces spaces with underscores, and escapes non-printing characters. To ensure accurate correlation between test logs and source code, it is recommended to avoid using these characters in subtest names." Slashes have special meaning: `-run=TestTime/New_York` will not match `t.Run("America/New_York", ...)` without double slashes (Google Decisions §Subtests; §Subtest names).

**See also**: TE-05, TE-08

---

## TE-07: Name the Row; Don't Use the Index

**Strength**: SHOULD

**Summary**: Every table case should carry a `name` (or similar descriptive) field used both for `t.Run` and in failure messages. Never identify a failing case by its table index.

```go
// Good
tests := []struct {
    name        string
    srcLang     string
    dstLang     string
    srcText     string
    wantDstText string
}{
    {
        name:        "hu=en_bug-1234",
        srcLang:     "hu",
        dstLang:     "en",
        srcText:     "cigarettát és egy öngyújtót kérek",
        wantDstText: "cigarettes and a lighter please",
    },
    // ...
}
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        got := Translate(tt.srcLang, tt.dstLang, tt.srcText)
        if got != tt.wantDstText {
            t.Errorf("Translate(%q, %q, %q) = %q, want %q",
                tt.srcLang, tt.dstLang, tt.srcText, got, tt.wantDstText)
        }
    })
}

// Bad — nobody wants to count rows to find case #7
for i, tc := range tests {
    if got := strings.ToUpper(tc.input); got != tc.want {
        t.Errorf("Failed on case #%d", i)
    }
}
```

**Rationale**: Index-based failure messages force the reader to count entries — which is error-prone and annoying. Named cases also make `-run TestX/case_name` usable. Google Decisions §Identifying the row: "Do not use the index of the test in the test table as a substitute for naming your tests or printing the inputs. Nobody wants to go through your test table and count the entries in order to figure out which test case is failing" (Google Decisions §Identifying the row).

---

## TE-08: Use Field Names in Test-Case Struct Literals

**Strength**: SHOULD

**Summary**: Initialize table cases with `Field: value` syntax. Positional literals become unreadable once the struct has more than a few fields or adjacent fields of the same type, and they break silently when fields are reordered.

```go
// Good
tests := []struct {
    slice     []string
    separator string
    skipEmpty bool
    want      string
}{
    {
        slice:     []string{"a", "b", ""},
        separator: ",",
        want:      "a,b,",
    },
    {
        slice:     []string{"a", "b", ""},
        separator: ",",
        skipEmpty: true,
        want:      "a,b",
    },
}

// Bad — which field is true? which is the separator?
tests := []struct {
    slice     []string
    separator string
    skipEmpty bool
    want      string
}{
    {[]string{"a", "b", ""}, ",", false, "a,b,"},
    {[]string{"a", "b", ""}, ",", true,  "a,b"},
}
```

**Rationale**: Named fields survive refactors, document each case, and let zero-value fields be omitted. Google Best Practices §Use field names in struct literals: "In table-driven tests, prefer to specify field names when initializing test case struct literals. This is helpful when the test cases cover a large amount of vertical space (e.g. more than 20-30 lines), when there are adjacent fields with the same type, and also when you wish to omit fields which have the zero value" (Google Best Practices §Use field names in struct literals).

**See also**: TE-05

---

## TE-09: Avoid Complex Conditional Logic Inside a Table Loop

**Strength**: SHOULD

**Summary**: When cases diverge in setup, mocks, or validation — `shouldCallX`, `shouldErr`, `setupMocks func(*FooMock)`, branching on an enum — split them into separate test functions instead of stuffing flags into the table. A simple `wantErr bool` branch is acceptable, but more than that is a smell.

```go
// Bad — multi-branch table with conditional mock setup
tests := []struct {
    give          string
    want          string
    wantErr       error
    shouldCallX   bool
    shouldCallY   bool
    giveXResponse string
    giveXErr      error
    giveYResponse string
    giveYErr      error
}{ /* ... */ }

for _, tt := range tests {
    t.Run(tt.give, func(t *testing.T) {
        ctrl := gomock.NewController(t)
        xMock := xmock.NewMockX(ctrl)
        if tt.shouldCallX {
            xMock.EXPECT().Call().Return(tt.giveXResponse, tt.giveXErr)
        }
        // ... etc ...
        if tt.wantErr != nil {
            require.EqualError(t, err, tt.wantErr)
            return
        }
        // ...
    })
}

// Good — two focused tests, no branches
func TestShouldCallX(t *testing.T) {
    ctrl := gomock.NewController(t)
    xMock := xmock.NewMockX(ctrl)
    xMock.EXPECT().Call().Return("XResponse", nil)
    yMock := ymock.NewMockY(ctrl)

    got, err := DoComplexThing("inputX", xMock, yMock)
    if err != nil {
        t.Fatalf("DoComplexThing(%q) unexpected error: %v", "inputX", err)
    }
    if got != "want" {
        t.Errorf("DoComplexThing(%q) = %q, want %q", "inputX", got, "want")
    }
}

func TestShouldCallYAndFail(t *testing.T) {
    // ... similarly focused ...
}

// Acceptable — single wantErr branch, short body
tests := []struct {
    dividend, divisor int
    want              int
    wantErr           bool
}{
    {dividend: 4, divisor: 2, want: 2},
    {dividend: 1, divisor: 0, wantErr: true},
}
for _, test := range tests {
    got, err := Divide(test.dividend, test.divisor)
    if (err != nil) != test.wantErr {
        t.Errorf("Divide(%d, %d) error = %v, want error presence = %t",
            test.dividend, test.divisor, err, test.wantErr)
    }
    if err != nil {
        continue
    }
    if got != test.want {
        t.Errorf("Divide(%d, %d) = %d, want %d", test.dividend, test.divisor, got, test.want)
    }
}
```

**Rationale**: Table tests shine when the axis of variation is input/output only. Once the body branches on per-row flags, readers have to simulate each case mentally and maintainers fear breaking an invisible interaction. Uber §Avoid Unnecessary Complexity in Table Tests: "Table tests should NOT be used whenever there needs to be complex or conditional logic inside subtests (i.e. complex logic inside the for loop)... Some ideals to aim for are: Focus on the narrowest unit of behavior; Minimize 'test depth'... Ensure that all table fields are used in all tests; Ensure that all test logic runs for all table cases." Google Decisions §Table-driven tests: "More complicated logic in your test code... can be difficult to understand when each entry in a table has specialized logic based on the inputs. If test cases have different logic but identical setup, a sequence of subtests within a single test function might be more readable" (Uber §Avoid Unnecessary Complexity in Table Tests; Google Decisions §Table-driven tests).

**See also**: TE-05

---

## TE-10: Parallel Tests — Call `t.Parallel()` Once Per Test and Subtest

**Strength**: SHOULD

**Summary**: Mark independent tests with `t.Parallel()` so `go test` runs them concurrently. In a table-driven test, call it inside `t.Run` so each subtest parallelizes. Go 1.22 fixed the loop-variable capture bug — earlier code required a local copy (`tt := tt`); on 1.22+, that is no longer necessary, but assigning `tt` still makes intent explicit.

```go
// Good — Go 1.22+, no rebinding needed
tests := []struct {
    name string
    give string
    // ...
}{ /* ... */ }

for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        t.Parallel()
        got := Process(tt.give)
        // ...
    })
}

// Still-valid, explicit form — rebinds tt to scope of each iteration
for _, tt := range tests {
    tt := tt  // local copy; required on Go < 1.22
    t.Run(tt.name, func(t *testing.T) {
        t.Parallel()
        // ...
    })
}

// Bad on Go < 1.22 — all parallel subtests see the last tt
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        t.Parallel()
        // tt captured by reference — same value across all iterations
        _ = tt
    })
}
```

**Rationale**: Without `t.Parallel()`, every subtest runs serially. With it, the Go runtime schedules them up to `-parallel` at a time. Before Go 1.22, the loop variable `tt` was a single variable shared across iterations — a parallel subtest reading it after the loop moved on would observe the wrong value. The 1.22 loop-variable semantics change made each iteration bind a fresh `tt`. Uber §Parallel Tests: "Parallel tests, like some specialized loops (for example, those that spawn goroutines or capture references as part of the loop body), must take care to explicitly assign loop variables within the loop's scope to ensure that they hold the expected values... we must declare a `tt` variable scoped to the loop iteration because of the use of `t.Parallel()` below. If we do not do that, most or all tests will receive an unexpected value for `tt`, or a value that changes as they're running" (Uber §Parallel Tests).

**See also**: TE-05, TE-13

---

## TE-11: Use `t.Helper` in Test Helpers (but Not in Assertion Libraries)

**Strength**: SHOULD

**Summary**: A "test helper" performs setup or cleanup and may call `t.Fatal` on environment failures. Mark it with `t.Helper()` so failure line numbers point to the caller, not inside the helper. Place the `*testing.T` after any `context.Context` parameter and before the rest.

```go
// Good
func readFile(t *testing.T, filename string) string {
    t.Helper()
    contents, err := os.ReadFile(filename)
    if err != nil {
        t.Fatal(err)
    }
    return string(contents)
}

func TestSomeFunction(t *testing.T) {
    golden := readFile(t, "testdata/golden-result.txt")
    // ... tests against golden ...
}

// Good — setup helper with Fatal on precondition failure
func mustAddGameAssets(t *testing.T, dir string) {
    t.Helper()
    if err := os.WriteFile(path.Join(dir, "pak0.pak"), pak0, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak0 asset: %v", err)
    }
    if err := os.WriteFile(path.Join(dir, "pak1.pak"), pak1, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak1 asset: %v", err)
    }
}

// Bad — no t.Helper; failure blames the helper's line, not the test's
func readFile(t *testing.T, filename string) string {
    contents, err := os.ReadFile(filename)
    if err != nil {
        t.Fatal(err)
    }
    return string(contents)
}
```

Test output comparison with and without `t.Helper`:

```text
=== RUN   TestBad
    paint_test.go:15: Could not paint the house under test: ...    // line inside helper
=== RUN   TestGood
    paint_test.go:32: Could not paint the house under test: ...    // line in TestGood
```

**Rationale**: `t.Helper()` tells the test runner "failures here should be attributed to my caller." That keeps the file:line in every failure message pointing to the test the reader is looking for. It is specifically **not** for building assertion libraries — those have other problems (see TE-15). Google Decisions §Test helpers: "If you pass a `*testing.T`, call `t.Helper` to attribute failures in the test helper to the line where the helper is called. This parameter should come after a context parameter, if present, and before any remaining parameters... `t.Helper` should not be used to implement [assertion] libraries." Google Best Practices §Error handling in test helpers: "Correctly using `(*testing.T).Helper` attributes the location of the failure much better when the helper functions grow, the helper functions call other helpers, the amount of helper usage in the test functions grow" (Google Decisions §Test helpers; Google Best Practices §Error handling in test helpers).

**See also**: TE-12, TE-15

---

## TE-12: `Must`-Style Test Helpers for Value-Context Setup

**Strength**: SHOULD

**Summary**: Helpers that return a value and are expected to succeed can use the `MustXxx` / `mustXxx` naming convention and call `t.Fatal` on error. They are handy for inline use in struct fields of table-driven tests, where a function returning `(T, error)` cannot be assigned directly.

```go
// Good
func mustMarshalAny(t *testing.T, m proto.Message) *anypb.Any {
    t.Helper()
    any, err := anypb.New(m)
    if err != nil {
        t.Fatalf("mustMarshalAny: %v", err)
    }
    return any
}

func TestCreateObject(t *testing.T) {
    tests := []struct {
        desc string
        data *anypb.Any
    }{
        {
            desc: "my test case",
            data: mustMarshalAny(t, mypb.Object{}),  // value-context usage
        },
        // ...
    }
    // ...
}

// Bad — using MustXxx on user input in production code
func Version(o *servicepb.Object) (*version.Version, error) {
    v := version.MustParse(o.GetVersionString())  // panics on bad input
    return dealiasVersion(v)
}
```

**Rationale**: Constructing test fixtures inline keeps tables readable. Wrapping `(T, error)` constructors in a `must` helper avoids cluttering every row with an `if err != nil`. Google Decisions §Must functions: "The same convention may be used in test helpers that only stop the current test (using `t.Fatal`). Such helpers are often convenient in creating test values, for example in struct fields of table driven tests, as functions that return errors cannot be directly assigned to a struct field... Where `Must` functions are used in a test, they should generally be marked as a test helper and call `t.Fatal` on error" (Google Decisions §Must functions).

**See also**: TE-11

---

## TE-13: Never Call `t.Fatal` from a Separate Goroutine

**Strength**: MUST

**Summary**: `t.FailNow`, `t.Fatal`, `t.Fatalf`, `t.SkipNow` must only be called from the test's own goroutine. From goroutines launched by the test, use `t.Error`/`t.Errorf` and `return`. This is stated in `testing` package documentation and is not relaxed by `t.Parallel()`.

```go
// Good
func TestRevEngine(t *testing.T) {
    engine, err := Start()
    if err != nil {
        t.Fatalf("Engine failed to start: %v", err)  // test goroutine — OK
    }

    var wg sync.WaitGroup
    for i := 0; i < 11; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            if err := engine.Vroom(); err != nil {
                t.Errorf("No vroom left on engine: %v", err)  // Error, not Fatal
                return
            }
            if rpm := engine.Tachometer(); rpm > 1e6 {
                t.Errorf("Inconceivable engine rate: %d", rpm)
            }
        }()
    }
    wg.Wait()

    if seen := engine.NumVrooms(); seen != 11 {
        t.Errorf("engine.NumVrooms() = %d, want 11", seen)
    }
}

// Bad
go func() {
    if err := engine.Vroom(); err != nil {
        t.Fatalf("no vroom: %v", err)  // wrong goroutine — undefined behavior
    }
}()
```

**Rationale**: `t.FailNow` works by calling `runtime.Goexit`, which only unwinds the goroutine that calls it. From another goroutine, it does not stop the test, and the `testing` package documents it as incorrect. Google Best Practices §Don't call `t.Fatal` from separate goroutines: "As documented in package testing, it is incorrect to call `t.FailNow`, `t.Fatal`, etc. from any goroutine but the one running the Test function (or the subtest). If your test starts new goroutines, they must not call these functions from inside these goroutines... Adding `t.Parallel` to a test or subtest does not make it unsafe to call `t.Fatal`." Test helpers called from the main test goroutine can still use `t.Fatal`; what matters is the calling goroutine, not the calling function (Google Best Practices §Don't call `t.Fatal` from separate goroutines).

**See also**: TE-11

---

## TE-14: Run with `-race` to Catch Data Races

**Strength**: SHOULD

**Summary**: Run concurrent-code tests under `go test -race`. The race detector instruments memory accesses and reports concurrent unsynchronized reads/writes. Because `t.Parallel` already encourages concurrent test execution, `-race` pairs naturally with parallel tests.

```go
// Typical CI invocation
$ go test -race ./...

// Good — a concurrent test whose race the detector will catch
func TestCounter(t *testing.T) {
    var c Counter
    var wg sync.WaitGroup
    for i := 0; i < 100; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            c.Inc()  // detector flags this if Inc has no mutex
        }()
    }
    wg.Wait()
    if got, want := c.Value(), 100; got != want {
        t.Errorf("Counter = %d, want %d", got, want)
    }
}
```

**Rationale**: Go's concurrency primitives give the compiler no static view of data races; the race detector is the only reliable way to find them. It has overhead but is essentially free in test runs. Running tests under `-race` is a convention the Go team and Google both assume. Combined with `t.Parallel` from TE-10, `-race` turns the test suite into a cheap data-race regression check. This aligns with Uber §Don't fire-and-forget goroutines — any goroutine launched in a test must have a bounded lifetime, and `-race` plus `sync.WaitGroup` is how tests prove concurrent code is correct (Uber §Don't fire-and-forget goroutines; Google Best Practices §Don't call `t.Fatal` from separate goroutines).

**See also**: TE-10, TE-13

---

## TE-15: Do Not Write or Use Assertion Libraries

**Strength**: SHOULD-AVOID

**Summary**: Don't build helpers that take `*testing.T`, perform a comparison, and call `t.Errorf`/`t.Fatalf` themselves. Prefer plain Go — `if got != want { t.Errorf(...) }` — or comparison helpers that return a value (`cmp.Diff`, `cmp.Equal`). This is the Go community's preferred style and matches the standard library.

```go
// Bad — an assertion library
package assert

func IsNotNil(t *testing.T, name string, val any) {
    if val == nil {
        t.Fatalf("Data %s = nil, want not nil", name)
    }
}
func StringEq(t *testing.T, name, got, want string) {
    if got != want {
        t.Fatalf("Data %s = %q, want %q", name, got, want)
    }
}

// Bad — caller site
var obj BlogPost
assert.IsNotNil(t, "obj", obj)
assert.StringEq(t, "obj.Type", obj.Type, "blogPost")
assert.IntEq(t, "obj.Comments", obj.Comments, 2)

// Good — stdlib Go with cmp for deep comparison
var got BlogPost
want := BlogPost{Comments: 2, Body: "Hello, world!"}
if !cmp.Equal(got, want) {
    t.Errorf("Blog post = %v, want = %v", got, want)
}

// Good — domain helper returns a value, not a testing.T-consumer
func postLength(p BlogPost) int { return len(p.Body) }

func TestBlogPost_VeritableRant(t *testing.T) {
    post := BlogPost{Body: "I am Gunnery Sergeant Hartman..."}
    if got, want := postLength(post), 60; got != want {
        t.Errorf("postLength(%v) = %v, want %v", post, got, want)
    }
}
```

**Rationale**: Assertion libraries either stop the test early (if `assert` calls `t.Fatalf`) or omit useful context about what else is true. They fragment the ecosystem: which library, which output style, which helper. Google Decisions §Assertion libraries: "Do not create 'assertion libraries' as helpers for testing... Complex assertion functions often do not provide useful failure messages and context that exists within the test function. Too many assertion functions and libraries lead to a fragmented developer experience... Instead of creating a domain-specific language for testing, use Go itself." Google Best Practices §Leave testing to the `Test` function draws the line explicitly: test helpers do setup and cleanup; assertion helpers check correctness and fail the test — the latter are "not considered idiomatic" in Go (Google Decisions §Assertion libraries; Google Best Practices §Leave testing to the `Test` function).

**Note**: Third-party assertion libraries (testify/require, testify/assert) are widely used in the Go ecosystem. Some Uber examples show `require.NoError(t, err)` and `assert.Equal(...)` — this reflects Uber's internal preference. The Google style guide disallows them in its codebase. The stdlib-only approach is the default in this guide because it matches the Go team's own posture and keeps test code readable without extra dependencies.

**See also**: TE-16, TE-18

---

## TE-16: Use `cmp.Diff` for Structural Comparisons

**Strength**: SHOULD

**Summary**: For structs, slices, maps, or any multi-field value, compare with `github.com/google/go-cmp/cmp`. Use `cmp.Equal(got, want)` for a boolean check and `cmp.Diff(want, got)` for a human-readable diff to print on failure. Do not hand-code field-by-field comparisons. Do not use `reflect.DeepEqual`.

```go
import "github.com/google/go-cmp/cmp"

// Good — boolean check with context-rich error
want := &Doc{
    Type:     "blogPost",
    Comments: 2,
    Body:     "This is the post body.",
    Authors:  []string{"isaac", "albert", "emmy"},
}
if !cmp.Equal(got, want) {
    t.Errorf("AddPost() = %+v, want %+v", got, want)
}

// Good — diff for larger values
if diff := cmp.Diff(want, got); diff != "" {
    t.Errorf("AddPost() returned unexpected diff (-want +got):\n%s", diff)
}

// Good — protobufs need an option
if diff := cmp.Diff(want, got, protocmp.Transform()); diff != "" {
    t.Errorf("Foo() returned unexpected difference in protobuf messages (-want +got):\n%s", diff)
}

// Bad — reflect.DeepEqual is sensitive to unexported fields and gives no diff
if !reflect.DeepEqual(got, want) {
    t.Errorf("got %v, want %v", got, want)
}

// Bad — hand-coded field-by-field compare
if got.Type != want.Type { t.Errorf("Type mismatch") }
if got.Comments != want.Comments { t.Errorf("Comments mismatch") }
// ...
```

**Rationale**: `cmp` handles nested types, gives a readable diff, and is user-configurable via `cmp.Option`/`cmpopts`. Though not part of the standard library, it is maintained by the Go team and is the community standard. Google Decisions §Equality comparison and diffs: "Use `cmp.Equal` for equality comparison and `cmp.Diff` to obtain a human-readable diff between objects... Although the `cmp` package is not part of the Go standard library, it is maintained by the Go team and should produce stable equality results over time... Prefer using `cmp` for new code, and it is worth considering updating older code to use `cmp` where and when it is practical to do so." §Print diffs: "To compute diffs for such values, `cmp.Diff` is preferred, particularly for new tests and new code." `reflect.DeepEqual` "should not be used for checking equality, as it is sensitive to changes in unexported fields and other implementation details" (Google Decisions §Equality comparison and diffs; §Print diffs; §Full structure comparisons).

**Note**: `cmp` is designed for testing and may panic on certain comparisons to steer authors toward more explicit options — don't use it in production code.

**See also**: TE-17, TE-20

---

## TE-17: Annotate Diff Direction in the Failure Message

**Strength**: SHOULD

**Summary**: `cmp.Diff` takes `(want, got)` by convention and annotates its output with `-` (want) and `+` (got). Print a legend so the reader isn't guessing which side is which.

```go
// Good — (want, got) → "-want +got"
if diff := cmp.Diff(want, got); diff != "" {
    t.Errorf("MyFunc(%v) returned unexpected diff (-want +got):\n%s", input, diff)
}

// Also OK, but be consistent and re-label
if diff := cmp.Diff(got, want); diff != "" {
    t.Errorf("MyFunc(%v) returned unexpected diff (-got +want):\n%s", input, diff)
}

// Bad — reader has to guess
if diff := cmp.Diff(want, got); diff != "" {
    t.Errorf("MyFunc: %s", diff)
}
```

**Rationale**: `cmp.Diff`'s output has `-`/`+` markers that correspond to the first and second argument. Without a legend, readers have to remember (or look up) which side is "want". Google Decisions §Print diffs: "Add some text to your failure message explaining the direction of the diff... `diff (-want +got)` is good when you're using the `cmp`, `pretty`, and `diff` packages (if you pass `(want, got)` to the function), because the `-` and `+` that you add to your format string will match the `-` and `+` that actually appear at the beginning of the diff lines. If you pass `(got, want)` to your function, the correct key would be `(-got +want)` instead." The style guide explicitly marks argument order as a non-decision: pick one and be locally consistent (Google Decisions §Print diffs; §Non-decisions).

**See also**: TE-16

---

## TE-18: Test Error Semantics, Not Error Strings

**Strength**: SHOULD

**Summary**: When a test needs to check an error, check whether one occurred (`err != nil`), whether it matches a sentinel (`errors.Is`), or whether it can be unwrapped to a known type (`errors.As`). Do not compare error messages as strings. For table cases, a `wantErr bool` is sufficient when the error's identity doesn't matter; use `cmpopts.EquateErrors` only when you are actually comparing to a sentinel or `cmpopts.AnyError`.

```go
// Good — "did it fail?" check
err := f(input)
if gotErr := err != nil; gotErr != tt.wantErr {
    t.Errorf("f(%q) = %v, want error presence = %v", input, err, tt.wantErr)
}

// Good — identity check against a sentinel
if !errors.Is(err, io.EOF) {
    t.Errorf("Read() error = %v, want errors.Is(io.EOF)", err)
}

// Good — type check
var pathErr *os.PathError
if !errors.As(err, &pathErr) {
    t.Errorf("Open() error = %v, want *os.PathError", err)
}

// Bad — brittle string match turns the test into a change detector
if err.Error() != "open foo.txt: no such file or directory" {
    t.Errorf("wrong error: %v", err)
}
```

**Rationale**: Error messages are for humans and they change. Asserting on their exact text makes refactoring error wording break tests. Go's error API (`errors.Is`, `errors.As`, typed errors) exists precisely to separate semantic identity from display. Google Decisions §Test error semantics: "When a unit test performs string comparisons or uses a vanilla `cmp` to check that particular kinds of errors are returned for particular inputs, you may find that your tests are brittle if any of those error messages are reworded... don't use string comparison to check what type of error your function returns. However, it is permissible to use string comparisons to check that error messages coming from the package under test satisfy certain properties, for example, that it includes the parameter name... If you would like to test that the error semantically matches some other error, then consider using `errors.Is` or `cmp` with `cmpopts.EquateErrors`." If all `wantErr` values are just nil vs non-nil, use a `bool`; introducing `cmpopts.EquateErrors` there is unnecessary mechanism (Google Decisions §Test error semantics).

**See also**: TE-15, TE-16

---

## TE-19: Compare Multi-Return Values Individually

**Strength**: SHOULD

**Summary**: If a function returns several values, don't wrap them in a struct just to compare. Check each value separately so each mismatch produces its own focused failure.

```go
// Good
val, multi, tail, err := strconv.UnquoteChar(`\"Fran & Freddie's Diner\"`, '"')
if err != nil {
    t.Fatalf("UnquoteChar returned unexpected error: %v", err)
}
if val != '"' {
    t.Errorf("UnquoteChar val = %q, want %q", val, '"')
}
if multi {
    t.Errorf("UnquoteChar multi = %v, want false", multi)
}
if tail != `Fran & Freddie's Diner"` {
    t.Errorf("UnquoteChar tail = %q, want %q", tail, `Fran & Freddie's Diner"`)
}

// Bad — constructing a throwaway struct just to call cmp.Diff
type result struct { val rune; multi bool; tail string }
got := result{val, multi, tail}
want := result{'"', false, `Fran & Freddie's Diner"`}
if !cmp.Equal(got, want) {
    t.Errorf("UnquoteChar got %+v, want %+v", got, want)
}
```

**Rationale**: Individual comparisons produce localized failures — you learn exactly which return value is wrong without parsing a diff. Google Decisions §Full structure comparisons: "If your function returns multiple return values, you don't need to wrap those in a struct before comparing them. Just compare the return values individually and print them" (Google Decisions §Full structure comparisons).

**See also**: TE-03, TE-16

---

## TE-20: Compare Semantic Equivalence, Not Unstable Serialized Output

**Strength**: SHOULD

**Summary**: Don't compare serialized forms (JSON bytes, printed strings, error-message text) when you care about the underlying meaning. Compare parsed structures instead. The serializer's exact output is not part of the contract.

```go
// Good — parse the output and compare structure
var got map[string]any
if err := json.Unmarshal(data, &got); err != nil {
    t.Fatalf("unmarshal: %v", err)
}
want := map[string]any{"name": "alice", "age": float64(30)}
if diff := cmp.Diff(want, got); diff != "" {
    t.Errorf("Marshal mismatch (-want +got):\n%s", diff)
}

// Bad — string-matches the serialized bytes
if string(data) != `{"name":"alice","age":30}` {
    t.Errorf("unexpected JSON: %s", data)
    // breaks if json package reorders keys, changes spacing, etc.
}
```

**Rationale**: The Go `encoding/json` package has changed its exact byte output in the past and will again. Testing that serializers produce specific bytes ties your tests to another package's implementation details. Google Decisions §Compare stable results: "Avoid comparing results that may depend on output stability of a package that you do not own. Instead, the test should compare on semantically relevant information that is stable and resistant to changes in dependencies. For functionality that returns a formatted string or serialized bytes, it is generally not safe to assume that the output is stable. For example, `json.Marshal` can change (and has changed in the past) the specific bytes that it emits" (Google Decisions §Compare stable results).

---

## TE-21: Choose Between `package foo` and `package foo_test`

**Strength**: CONSIDER

**Summary**: Internal tests (white-box) live in `package foo` and can touch unexported identifiers. External tests (black-box) live in `package foo_test` in the same directory and import `foo` like a user would. `_test` is the one permitted exception to the "no underscores in package names" rule.

```go
// Good — internal test, foo_test.go
package foo

import "testing"

func TestInternalHelper(t *testing.T) {
    if got := internalHelper(); got != expected {
        t.Errorf(...)
    }
}

// Good — external test in the same directory, also foo_test.go (or api_test.go)
package foo_test

import (
    "testing"

    "example.com/foo"
)

func TestPublicAPI(t *testing.T) {
    c := foo.New()
    // ...
}

// Good — integration test with an external name
package gmailintegration_test

import "testing"
```

**Rationale**: Internal tests exercise implementation details and keep coverage honest for unexported functions. External tests exercise the public API exactly as callers will; they also prevent cyclic imports when the test needs packages that themselves import `foo`. Google Decisions §Tests in the same package: "A test in the same package can access unexported identifiers in the package. This may enable better test coverage and more concise tests." §Tests in a different package: "It is not always appropriate or even possible to define a test in the same package as the code being tested. In these cases, use a package name with the `_test` suffix. This is an exception to the 'no underscores' rule." Use `_test` when an integration test has no natural home library or when same-package tests create circular dependencies (Google Decisions §Test package; §Underscores).

**Tip**: Both files can coexist in the same directory — `foo_test.go` with `package foo` for internal tests and `foo_api_test.go` with `package foo_test` for public-surface tests.

---

## TE-22: Name Test Double Types by Behavior, Not by "Stub" Alone

**Strength**: CONSIDER

**Summary**: Test doubles (stubs, fakes, mocks, spies) for package `foo` conventionally live in `package footest`. When there is one kind of double for one type, a bare name like `Stub` or `Spy` is fine — the caller's `footest.Stub` is already unambiguous. When you have multiple behaviors or multiple target types, name doubles by what they do.

```go
// Good — one double in the footest package
package creditcardtest

import (
    "path/to/creditcard"
    "path/to/money"
)

// Stub stubs creditcard.Service and provides no behavior of its own.
type Stub struct{}

func (Stub) Charge(*creditcard.Card, money.Money) error { return nil }

// Caller:
var spyCC creditcardtest.Spy  // unambiguous at call site

// Good — name by behavior when multiple stubs exist
type AlwaysCharges struct{}
func (AlwaysCharges) Charge(*creditcard.Card, money.Money) error { return nil }

type AlwaysDeclines struct{}
func (AlwaysDeclines) Charge(*creditcard.Card, money.Money) error {
    return creditcard.ErrDeclined
}

// Good — qualify type names when multiple production types get doubles
type StubService struct{}
func (StubService) Charge(*creditcard.Card, money.Money) error { return nil }

type StubStoredValue struct{}
func (StubStoredValue) Credit(*creditcard.Card, money.Money) error { return nil }

// Bad — redundantly verbose
type StubCreditCardService struct{}  // "StubService" or "Stub" is already clear
```

**Rationale**: Callers read `creditcardtest.Stub`, not `Stub` in isolation — so the package path already carries the context. Repeating it in the type name is noise. When the behavioral variants multiply, name them after the behavior (`AlwaysDeclines`) so tests read as English. Google Best Practices §Test double and helper packages: "A safe choice is to append the word `test` to the original package name ('creditcard' + 'test')... If you anticipate only test doubles for one type (like `Service`), you can take a concise approach to naming the doubles... When one kind of stub is not enough (for example, you also need one that always fails), we recommend naming the stubs according to the behavior they emulate" (Google Best Practices §Test double and helper packages).

**See also**: TE-23, TE-24

---

## TE-23: Prefer Fakes over Mocks; Accept Interfaces at the Boundary

**Strength**: CONSIDER

**Summary**: A **fake** is a lightweight in-memory implementation of an interface (e.g., a fake database that stores entries in a map). A **mock** records expected calls and fails the test if they are wrong. Fakes exercise more of the real interaction surface and give more stable tests. To use either, the production code must accept an interface it depends on — "accept interfaces, return concrete types".

```go
// Good — production type depends on an interface
type CreditCard interface {
    Charge(*creditcard.Card, money.Money) error
}

type Processor struct {
    CC CreditCard
}

func (p *Processor) Process(c *creditcard.Card, amount money.Money) error {
    if c.Expired() {
        return ErrBadInstrument
    }
    return p.CC.Charge(c, amount)
}

// Good — test uses a fake/spy from creditcardtest
func TestProcessor(t *testing.T) {
    var spyCC creditcardtest.Spy
    proc := &Processor{CC: spyCC}

    if err := proc.Process(card, amount); err != nil {
        t.Errorf("proc.Process(card, amount) = %v, want nil", err)
    }

    charges := []creditcardtest.Charge{{Card: card, Amount: amount}}
    if got, want := spyCC.Charges, charges; !cmp.Equal(got, want) {
        t.Errorf("spyCC.Charges = %v, want %v", got, want)
    }
}

// Good — fake codex as a fast, in-memory implementation
func TestDecodeWithFake(t *testing.T) {
    codex := newFakeCodex()  // in-memory; fast; deterministic
    // ... table-driven tests against codex ...
}
```

**Rationale**: Mocks that prescribe call sequences tie the test to the current implementation; fakes test behavior at a higher level and survive refactors. And the only reason a test can swap either one in is that the production code was written to accept an interface — making "accept an interface" a direct consequence of testability. Google Best Practices §Test double and helper packages shows fakes-and-spies patterns throughout. Google Decisions §Data-driven test cases: "A fakeCodex is a fast approximation of a real Codex" — fakes are a first-class testing tool (Google Best Practices §Test double and helper packages; Google Decisions §Data-driven test cases).

**See also**: TE-22, TE-24

---

## TE-24: Use Prefixed Names for Local Test-Double Variables

**Strength**: CONSIDER

**Summary**: When a test-double variable sits next to production types of related names, prefix the local variable (`spyCC`, `stubFoo`) so the reader can tell which is which at a glance.

```go
// Good — "spyCC" is clearly distinct from the CreditCard production interface
func TestProcessor(t *testing.T) {
    var spyCC creditcardtest.Spy
    proc := &Processor{CC: spyCC}
    // ...
}

// Bad — "cc" matches the field name and the production interface's shorthand
func TestProcessor(t *testing.T) {
    var cc creditcardtest.Spy
    proc := &Processor{CC: cc}   // cc here is a test double, but it looks production
    // ...
}
```

**Rationale**: In a test body that also mentions real types of similar name, prefixing the double disambiguates at a glance without requiring navigation. Google Best Practices §Local variables in tests: "In the tests, a test double called a 'spy' for `CreditCard` is juxtaposed against production types, so prefixing the name may improve clarity... This is clearer than when the name is not prefixed" (Google Best Practices §Local variables in tests).

**See also**: TE-22, TE-23

---

## TE-25: Use Real Transports with Fake Servers for Integration Tests

**Strength**: CONSIDER

**Summary**: When a system under test communicates over HTTP/RPC, use the real client library configured to talk to a test double of the *server*. Don't hand-implement the client.

```go
// Good — real OperationsClient, test OperationsServer
func TestSUT(t *testing.T) {
    fakeServer := startTestOperationsServer(t)  // implements the RPC interface
    t.Cleanup(fakeServer.Stop)

    client := longrunning.NewOperationsClient(fakeServer.Conn())

    sut := NewSystemUnderTest(client)
    // ... exercise sut, observe interactions on fakeServer ...
}

// Bad — hand-roll a client implementation that pretends to be the real one
type fakeOperationsClient struct{}
func (fakeOperationsClient) GetOperation(...) (...) { /* re-implement the RPC semantics */ }
```

**Rationale**: Client libraries contain serialization, retries, deadlines, and authentication that are hard to replicate. Using a real client with a fake server keeps as much of the production code path under test as possible. Google Best Practices §Use real transports: "Prefer using the real underlying transport to connect to the test version of the backend... This is recommended over hand-implementing the client, due to the complexity of imitating client behavior correctly. By using the production client with a test-specific server, you ensure your test is using as much of the real code as possible" (Google Best Practices §Use real transports).

**Tip**: Where possible, use a testing library provided by the authors of the service under test.

---

## TE-26: Keep Setup Scoped to the Tests That Need It

**Strength**: SHOULD

**Summary**: Don't put expensive or failure-prone setup in `init()` or at package scope just because multiple tests use it. Prefer a test helper function (e.g., `mustLoadDataset`) called explicitly from the tests that need it. Tests that don't need the dataset stay cheap and hermetic.

```go
// Good — only tests that use the dataset pay for loading it
func mustLoadDataset(t *testing.T) []byte {
    t.Helper()
    data, err := os.ReadFile("testdata/dataset")
    if err != nil {
        t.Fatalf("Could not load dataset: %v", err)
    }
    return data
}

func TestParseData(t *testing.T) {
    data := mustLoadDataset(t)
    // ...
}

func TestListContents(t *testing.T) {
    data := mustLoadDataset(t)
    // ...
}

func TestRegression682831(t *testing.T) {
    // This test doesn't touch the dataset and shouldn't be slowed by it.
    if got, want := guessOS("zpc79.example.com"), "grhat"; got != want {
        t.Errorf(`guessOS("zpc79.example.com") = %q, want %q`, got, want)
    }
}

// Bad — init() forces every test in the package to load the dataset
var dataset []byte

func init() {
    dataset = mustLoadDataset()  // slow; fails go test -run TestRegression682831 too
}
```

**Rationale**: Tests that don't need a fixture shouldn't be slowed or broken by it. `go test -run TestRegression682831` should work even when the dataset file is unavailable. Google Best Practices §Keep setup code scoped to specific tests: "Where possible, setup of resources and dependencies should be as closely scoped to specific test cases as possible... A user may wish to run a function in isolation of the others and should not be penalized by these factors" (Google Best Practices §Keep setup code scoped to specific tests).

**See also**: TE-27, TE-28

---

## TE-27: Amortize Expensive Setup with `sync.Once`, Not `init`

**Strength**: CONSIDER

**Summary**: If loading a fixture is expensive, only some tests need it, and it requires no teardown, cache it in a package-level `sync.Once`-guarded struct. Each test calls the helper; first call does the work, rest reuse the result.

```go
// Good
var dataset struct {
    once sync.Once
    data []byte
    err  error
}

func mustLoadDataset(t *testing.T) []byte {
    t.Helper()
    dataset.once.Do(func() {
        data, err := os.ReadFile("testdata/dataset")
        dataset.data = data
        dataset.err = err
    })
    if err := dataset.err; err != nil {
        t.Fatalf("Could not load dataset: %v", err)
    }
    return dataset.data
}

func TestParseData(t *testing.T)    { data := mustLoadDataset(t); _ = data }
func TestListContents(t *testing.T) { data := mustLoadDataset(t); _ = data }
func TestRegression682831(t *testing.T) {
    // doesn't call mustLoadDataset; loading is skipped when this is the only test run
}
```

**Rationale**: `sync.Once` keeps the cost per package at most once, yet runs only if a test actually asks for the fixture. This is better than `init` (which always runs) and better than re-loading from every test (which is slow). Google Best Practices §Amortizing common test setup: "Using a `sync.Once` may be appropriate, though not required, if all of the following are true about the common setup: It is expensive. It only applies to some tests. It does not require teardown" (Google Best Practices §Amortizing common test setup).

**See also**: TE-26, TE-28

---

## TE-28: Use `TestMain` Only for Package-Wide Setup That Requires Teardown

**Strength**: CONSIDER

**Summary**: `func TestMain(m *testing.M)` is the last resort. Use it when every test in the package needs the same expensive resource and that resource must be torn down cleanly (e.g., a shared database). Structure it so the teardown runs even on failures.

```go
// Good
var db *sql.DB

func TestInsert(t *testing.T) { /* uses db */ }
func TestSelect(t *testing.T) { /* uses db */ }

func runMain(ctx context.Context, m *testing.M) (code int, err error) {
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()

    d, err := setupDatabase(ctx)
    if err != nil {
        return 0, err
    }
    defer d.Close()        // runs before return
    db = d

    return m.Run(), nil
}

func TestMain(m *testing.M) {
    code, err := runMain(context.Background(), m)
    if err != nil {
        log.Fatal(err)     // to stderr
    }
    // defers above do NOT run past os.Exit; that's why setup lives in runMain
    os.Exit(code)
}
```

**Rationale**: `os.Exit` skips deferreds, so naive `TestMain` bodies leak resources. Factoring the real work into `runMain` lets defers run before the exit call. But a custom `TestMain` should be a last resort: it runs for every test in the package, so a single test run like `-run TestRegression682831` also pays its cost. Google Best Practices §When to use a custom `TestMain` entrypoint: "If all tests in the package require common setup and the setup requires teardown, you can use a custom testmain entrypoint... Using a custom `TestMain` should not be your first choice due the amount of care that should be taken for correct use. Consider first whether the solution in the amortizing common test setup section or an ordinary test helper is sufficient" (Google Best Practices §When to use a custom `TestMain` entrypoint).

**Tip**: Aim for hermetic test cases — each should reset any global state it mutated, especially when an external database is involved.

**See also**: TE-26, TE-27

---

## TE-29: Write Runnable Examples for Godoc

**Strength**: SHOULD

**Summary**: An `ExampleXxx` function in a `*_test.go` file shows up in godoc attached to the documentation of `Xxx`. Add an `// Output:` comment to make `go test` verify the example's stdout matches, keeping the documentation provably correct.

```go
// Good — example for the Config.WriteTo method, verified by go test
func ExampleConfig_WriteTo() {
    cfg := &Config{
        Name: "example",
    }
    if err := cfg.WriteTo(os.Stdout); err != nil {
        log.Fatal(err)
    }
    // Output:
    // {
    //   "name": "example"
    // }
}

// Good — package-level example
func Example() {
    result := strings.ToUpper("hello")
    fmt.Println(result)
    // Output: HELLO
}

// Good — example without verified output (still renders in godoc, not executed)
func ExampleFetch() {
    resp, err := Fetch(context.Background(), "https://example.com")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Close()
    // ...
}
```

**Rationale**: Examples live next to the code and rot when the package changes, which is why `// Output:` is so valuable — it makes examples executable documentation. Google Decisions §Examples: "Packages should clearly document their intended usage. Try to provide a runnable example; examples show up in Godoc. Runnable examples belong in the test file, not the production source file." Google Best Practices §Godoc formatting includes an example of `ExampleConfig_WriteTo` with an `// Output:` block. Google Decisions §Use package `testing`: runnable examples are one of the six things the `testing` package provides (Google Decisions §Examples; Google Best Practices §Godoc formatting).

**Note**: Internal (`package foo`) examples won't have the package prefix a real user would need. For correct usage-as-documentation, put examples in `package foo_test`.

---

## TE-30: Support Fuzz Testing for Functions with Input-Dependent Behavior

**Strength**: CONSIDER

**Summary**: Go 1.18+ supports fuzz testing via `FuzzXxx(f *testing.F)`. Seed with `f.Add(...)`, then pass a property-checking function to `f.Fuzz(...)`. Fuzz targets run as ordinary tests (with only the seed corpus) unless invoked with `go test -fuzz`.

```go
// Good — fuzz target with seeds and a reference implementation
func FuzzFencepost(f *testing.F) {
    f.Add(tomsDiner, 1*meter)
    f.Add(school, 3*meter)

    f.Fuzz(func(t *testing.T, geo Place, padding Length) {
        got := Fencepost(geo, padding)
        // Simple reference implementation: slow, but easy to reason about;
        // useful for random input checks.
        reference := slowFencepost(geo, padding)
        if !cmp.Equal(got, reference, polygonCmp()) {
            t.Errorf("Fencepost returned wrong placement")
        }
    })
}

// Run discovery seeds only (default):
//   go test
// Run the fuzzer for 30 seconds:
//   go test -fuzz=FuzzFencepost -fuzztime=30s
```

**Rationale**: Fuzz testing is excellent for finding edge cases in parsers, encoders, and any function whose behavior has many input-dependent branches. Pairing a fuzz target with a slow reference implementation is a classic property-based testing idiom. Google Best Practices §Leave testing to the `Test` function shows the pattern: "`FuzzFencepost` — Fuzz test for the same. In the fuzz test, inputs and outputs can be large so don't bother with printing a diff. `cmp.Equal` is enough" (Google Best Practices §Leave testing to the `Test` function). Google Decisions §Test helpers notes that helper advice applies to "benchmark and fuzz helpers" as well (Google Decisions §Test helpers).

---

## TE-31: Keep Validation Helpers Agnostic: Return a Value, Not Call `t.Error`

**Strength**: SHOULD

**Summary**: When you need a reusable comparison for a domain-specific type (e.g., approximate equality, custom ignore rules), return a value — typically a `cmp.Option`, a `bool`, or an `error` — rather than a function that takes `*testing.T` and fails the test internally. The caller decides how to report the failure.

```go
// Good — a cmp.Option that equates geometry up to small float error
func polygonCmp() cmp.Option {
    return cmp.Options{
        cmp.Transformer("polygon", func(p *s2.Polygon) []*s2.Loop { return p.Loops() }),
        cmp.Transformer("loop", func(l *s2.Loop) []s2.Point { return l.Vertices() }),
        cmpopts.EquateApprox(0.00000001, 0),
        cmpopts.EquateEmpty(),
    }
}

func TestFenceposts(t *testing.T) {
    got := Fencepost(tomsDiner, 1*meter)
    if diff := cmp.Diff(want, got, polygonCmp()); diff != "" {
        t.Errorf("Fencepost(tomsDiner, 1m) returned unexpected diff (-want+got):\n%v", diff)
    }
}

// Good — validation returns error; caller formats the failure
func ExercisePlayer(b *chess.Board, p chess.Player) error {
    for color, army := range b.Armies {
        if army.King == nil {
            return &MissingPieceError{Color: color, Piece: chess.King}
        }
    }
    return nil
}

// Bad — validation internally calls t.Fatal; caller loses control of the message
func ExercisePlayer(t *testing.T, b *chess.Board, p chess.Player) {
    if army.King == nil {
        t.Fatalf("king missing")   // hard to use in other contexts; cost of change is high
    }
}
```

**Rationale**: A helper that returns a value is usable in more contexts — normal tests, fuzz tests, acceptance tests. It also composes: the same `cmp.Option` can be passed to `cmp.Diff`, `cmp.Equal`, and fuzz checks. Google Best Practices §Leave testing to the `Test` function: "The `polygonCmp` function is agnostic about how it's called; it doesn't take a concrete input type nor does it police what to do in case two objects don't match. Therefore, more callers can make use of it... If there are multiple callers who need the same validation function but table tests are not suitable... arrange the validation function so that it returns a value (typically an `error`) rather than taking a `testing.T` parameter and using it to fail the test" (Google Best Practices §Leave testing to the `Test` function).

**See also**: TE-15, TE-16

---

## TE-32: Keep Tests Hermetic — Reset Global State You Mutate

**Strength**: SHOULD

**Summary**: A test must leave no side effects visible to another test: no leftover entries in a shared table, no changed environment variables, no process-global singletons pointing somewhere new. If a test mutates shared state, it must restore it on exit — usually with `t.Cleanup(func() { ... })`.

```go
// Good — clean up inside the test itself
func TestWithTmpConfig(t *testing.T) {
    orig := os.Getenv("APP_CONFIG")
    os.Setenv("APP_CONFIG", "/tmp/testcfg.yaml")
    t.Cleanup(func() {
        os.Setenv("APP_CONFIG", orig)
    })
    // ... test body ...
}

// Better — use t.Setenv; it restores automatically and is incompatible with t.Parallel
func TestWithTmpConfig(t *testing.T) {
    t.Setenv("APP_CONFIG", "/tmp/testcfg.yaml")
    // APP_CONFIG is restored when the test ends.
}

// Good — database test tears down rows it created
func TestInsert(t *testing.T) {
    id := insertRow(t, db, "alice")
    t.Cleanup(func() { deleteRow(t, db, id) })
    // ...
}

// Bad — mutates a package-level var and never restores it
var apiBase = "https://prod.example.com"

func TestFoo(t *testing.T) {
    apiBase = "http://localhost:8080"   // every subsequent test sees this
    // ...
}
```

**Rationale**: When a test leaks state, failures stop being reproducible in isolation — a later test's failure depends on which earlier tests ran. Hermetic tests pass under `go test -run TestOne` regardless of what else is in the package. Google Best Practices §When to use a custom `TestMain` entrypoint: "Ideally a test case is hermetic between invocations of itself and between other test cases. At the very least, ensure that individual test cases reset any global state they have modified if they have done so (for instance, if the tests are working with an external database)." This also aligns with Uber §Avoid Mutable Globals — packages that avoid mutable globals in production are trivially hermetic in tests (Google Best Practices §When to use a custom `TestMain` entrypoint; Uber §Avoid Mutable Globals).

**See also**: TE-28, TE-33

---

## TE-33: Use `t.Cleanup` for Per-Test Teardown

**Strength**: SHOULD

**Summary**: `t.Cleanup(fn)` registers `fn` to run when the test (or subtest) ends, regardless of how it ends. It composes across helpers — a helper can register its own cleanups without the test function having to orchestrate them. Prefer it to manual `defer` at the test level when cleanup is set up inside a helper.

```go
// Good — helper encapsulates its own cleanup
func openTempDB(t *testing.T) *sql.DB {
    t.Helper()
    db, err := sql.Open("sqlite3", ":memory:")
    if err != nil {
        t.Fatalf("open db: %v", err)
    }
    t.Cleanup(func() { db.Close() })   // test doesn't need to know
    return db
}

func TestInsert(t *testing.T) {
    db := openTempDB(t)
    // ... no explicit Close needed ...
}

// Good — chess.ExerciseGame registers cleanup for an allocated resource
func ExerciseGame(t *testing.T, cfg *Config, p chess.Player) error {
    t.Helper()

    if cfg.Simulation == Modem {
        conn, err := modempool.Allocate()
        if err != nil {
            t.Fatalf("No modem for the opponent could be provisioned: %v", err)
        }
        t.Cleanup(func() { modempool.Return(conn) })
    }
    // Run acceptance test.
}

// Bad — defer in the helper runs when the helper returns, not when the test ends
func openTempDB(t *testing.T) *sql.DB {
    db, _ := sql.Open("sqlite3", ":memory:")
    defer db.Close()  // closes immediately; db is useless to the caller
    return db
}
```

**Rationale**: `t.Cleanup` lets helpers own their own lifecycle, which keeps test bodies focused on what is being tested. It runs in LIFO order, integrates with `t.Parallel`, and runs after subtests finish. Google Best Practices §Error handling in test helpers: "Go 1.14 introduced a `t.Cleanup` function that can be used to register cleanup functions that run when your test completes. The function also works with test helpers" (Google Best Practices §Error handling in test helpers; §Writing an acceptance test).

**See also**: TE-11, TE-32

---

## TE-34: Use `t.TempDir` for Per-Test Temporary Directories

**Strength**: SHOULD

**Summary**: `t.TempDir()` returns a fresh directory unique to the test, automatically cleaned up when the test ends. It replaces patterns like `os.MkdirTemp` + `defer os.RemoveAll(...)`.

```go
// Good
func TestWriteConfig(t *testing.T) {
    dir := t.TempDir()
    path := filepath.Join(dir, "cfg.yaml")
    if err := WriteConfig(path, cfg); err != nil {
        t.Fatalf("WriteConfig(%q): %v", path, err)
    }
    // read it back, verify, etc. No cleanup needed.
}

// Bad — verbose and easy to forget the RemoveAll
func TestWriteConfig(t *testing.T) {
    dir, err := os.MkdirTemp("", "cfg")
    if err != nil {
        t.Fatalf("MkdirTemp: %v", err)
    }
    defer os.RemoveAll(dir)
    // ...
}
```

**Rationale**: `t.TempDir` removes a whole class of cleanup bugs and keeps tests concise. The `testing` package integrates its cleanup with `t.Cleanup`, so it works correctly with subtests and parallel tests. Google Best Practices writes fixture files to a test-local directory throughout (e.g., `os.WriteFile(path.Join(dir, "pak0.pak"), ...)` inside `mustAddGameAssets(t, dir)`), which is idiomatic when paired with `dir := t.TempDir()` (Google Best Practices §Error handling in test helpers; `testing.T.TempDir`).

**See also**: TE-33

---

## TE-35: Store Fixture Data Under `testdata/`

**Strength**: SHOULD

**Summary**: The Go toolchain ignores directories named `testdata`: files inside are not compiled and not subject to package-name or vet rules. Put golden files, sample inputs, and other test fixtures there, and reference them from tests via relative paths.

```go
// Directory layout:
//   parser.go
//   parser_test.go
//   testdata/
//     valid/
//       simple.yaml
//       nested.yaml
//     invalid/
//       syntax-error.yaml
//     golden/
//       simple.json        // expected output of Parse(simple.yaml) marshaled

// Good — helper loads from testdata/
func readFile(t *testing.T, filename string) string {
    t.Helper()
    contents, err := os.ReadFile(filename)
    if err != nil {
        t.Fatal(err)
    }
    return string(contents)
}

func TestParse(t *testing.T) {
    golden := readFile(t, "testdata/golden-result.txt")
    got := Parse(readFile(t, "testdata/input.txt"))
    if diff := cmp.Diff(golden, got); diff != "" {
        t.Errorf("Parse mismatch (-want +got):\n%s", diff)
    }
}
```

**Rationale**: `testdata/` is the idiomatic home for files a test needs. `go build` ignores it, and `go test` runs from the package directory so relative paths are stable. This is the pattern Google's own examples use: `os.ReadFile("path/to/your/project/testdata/dataset")` and `"testdata/golden-result.txt"` appear throughout Google Best Practices §Keep setup code scoped to specific tests and §Test helpers (Google Best Practices §Keep setup code scoped to specific tests; Google Decisions §Test helpers).

**See also**: TE-36

---

## TE-36: Golden File Pattern: Compare to File, Regenerate Behind a Flag

**Strength**: CONSIDER

**Summary**: When a test's expected output is too large to inline, store it in `testdata/` as a "golden file". Compare the actual output to the file contents. Expose a `-update` flag that rewrites the file when the test is run with `-update`, so maintainers can regenerate goldens after an intentional change.

```go
var update = flag.Bool("update", false, "update golden files")

func TestFormat(t *testing.T) {
    got := Format(input)

    goldenPath := filepath.Join("testdata", "format.golden")
    if *update {
        if err := os.WriteFile(goldenPath, []byte(got), 0644); err != nil {
            t.Fatalf("update golden: %v", err)
        }
    }
    wantBytes, err := os.ReadFile(goldenPath)
    if err != nil {
        t.Fatalf("read golden: %v", err)
    }
    if diff := cmp.Diff(string(wantBytes), got); diff != "" {
        t.Errorf("Format mismatch (-want +got):\n%s", diff)
    }
}

// Regenerate after an intentional change:
//   go test -run TestFormat -update
```

**Rationale**: Goldens are strictly better than inline multi-line strings once output exceeds a few dozen lines: the diff in `git` shows exactly how the output changed, and a dedicated file is easier to read than an escaped Go string literal. The `-update` flag is the standard way to accept a new golden — it's what the Go toolchain itself uses. Combining goldens with `cmp.Diff` gives tight, human-readable failure messages. Google's examples use golden files (`testdata/golden-result.txt`) and explicitly contrast them with inline expected strings (Google Decisions §Test helpers; §Print diffs).

**See also**: TE-16, TE-35

---

## TE-37: Split Integration Tests from Unit Tests with Build Tags or `testing.Short`

**Strength**: CONSIDER

**Summary**: Unit tests should run in seconds without network or database dependencies. For tests that need external resources, either gate them with `testing.Short` (`if testing.Short() { t.Skip(...) }`) or put them behind a build tag (`//go:build integration`). CI can then run `go test -short ./...` in fast pipelines and `go test -tags=integration ./...` in slower ones.

```go
// Good — build-tag gate; file compiled only with the tag set
//go:build integration

package db_test

import "testing"

func TestAgainstRealDatabase(t *testing.T) {
    db := connectToRealDB(t)
    // ...
}

// Good — runtime gate; compiled always, skipped with -short
func TestAgainstRealDatabase(t *testing.T) {
    if testing.Short() {
        t.Skip("skipping integration test under -short")
    }
    db := connectToRealDB(t)
    // ...
}

// Good — package name for integration tests can carry the suffix
package linked_list_service_test

// Good — standalone directory for integration tests
package gmailintegration_test
```

**Rationale**: Fast feedback is a property of the test suite, not of any single test. Isolating the slow/flaky minority of tests — network, database, browser — preserves the "seconds to green" feeling of the rest. `testing.Short()` is the standard runtime gate (a pure stdlib facility); build tags are the standard compile-time gate. Google Decisions §Package names explicitly mentions that integration test packages may carry the `_test` suffix and may even use underscores: "Using underscores and the `_test` suffix for packages that specify functional or integration tests. For example, a linked list service integration test could be named `linked_list_service_test`" (Google Decisions §Package names; §Tests in a different package).

---

## TE-38: Benchmark Functions: `BenchmarkXxx(b *testing.B)`, Loop `b.N` Times

**Strength**: SHOULD

**Summary**: A benchmark is a function `BenchmarkXxx(b *testing.B)` that runs the measured workload `b.N` times. Go's test runner calibrates `b.N` to achieve stable timing. Use `b.ResetTimer()` to discard setup from the measured time and `b.ReportAllocs()` to include allocation counts in the output.

```go
// Good
func BenchmarkFormat(b *testing.B) {
    input := buildLargeInput()   // setup; don't measure it
    b.ReportAllocs()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        _ = Format(input)
    }
}

// Good — subtest-style sub-benchmarks
func BenchmarkCodec(b *testing.B) {
    for _, size := range []int{16, 256, 4096} {
        b.Run(fmt.Sprintf("size=%d", size), func(b *testing.B) {
            data := make([]byte, size)
            b.ResetTimer()
            for i := 0; i < b.N; i++ {
                _ = Encode(data)
            }
        })
    }
}

// Run:
//   go test -bench=. -benchmem
```

Typical output:

```text
BenchmarkFmtSprint-4       143 ns/op    2 allocs/op
BenchmarkStrconv-4          64.2 ns/op    1 allocs/op
```

**Rationale**: `b.N` lets the runtime decide how many iterations are needed for a stable measurement — don't loop a fixed count. `b.ResetTimer` excludes setup; `b.ReportAllocs` surfaces allocator behavior, which often explains performance differences more than raw ns/op does. Uber §Performance shows this pattern repeatedly when comparing alternatives (`BenchmarkBad`/`BenchmarkGood`) to justify claims like "prefer strconv over fmt" (Uber §Prefer strconv over fmt; §Avoid repeated string-to-byte conversions; §Prefer Specifying Container Capacity).

**See also**: TE-39

---

## TE-39: Benchmarks Back Performance Claims with Before/After Numbers

**Strength**: SHOULD

**Summary**: Performance claims need benchmark evidence. Write a `BenchmarkBad`/`BenchmarkGood` pair to demonstrate the improvement, and include allocations (`-benchmem`) when they're relevant to the change.

```go
// Good — demonstrate a specific optimization
func BenchmarkBad(b *testing.B) {
    for i := 0; i < b.N; i++ {
        w.Write([]byte("Hello world"))        // byte conversion each call
    }
}

func BenchmarkGood(b *testing.B) {
    data := []byte("Hello world")             // hoist out of the loop
    for i := 0; i < b.N; i++ {
        w.Write(data)
    }
}
```

Output demonstrating the improvement:

```text
BenchmarkBad-4    50000000   22.2 ns/op
BenchmarkGood-4  500000000    3.25 ns/op
```

**Rationale**: Without benchmarks, "optimizations" often have no effect or the wrong sign. Benchmarks paired with before/after numbers turn performance review from argument into measurement. Uber §Performance uses benchmark output in exactly this form throughout (Uber §Prefer strconv over fmt; §Avoid repeated string-to-byte conversions).

**Note**: Detailed performance patterns are in chapter 08. This entry establishes only the testing mechanics.

**See also**: TE-38

---

## TE-40: Deterministic Concurrency Tests with `testing/synctest`

**Strength**: SHOULD (Go 1.25+)

**Summary**: For concurrent code that depends on timing, run the test inside a `synctest.Test(t, func(t *testing.T) { ... })` bubble. Inside the bubble, time is synthetic and advances only when every goroutine in the bubble is blocked, so `time.Sleep` and `context.WithTimeout` become deterministic and instant.

```go
// Bad: flaky timing-dependent test
func TestTimeout(t *testing.T) {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    time.Sleep(4 * time.Second) // real time, test is slow and flaky
    if ctx.Err() != nil {
        t.Fatal("unexpected timeout")
    }
}

// Good: deterministic with synthetic time
func TestTimeout(t *testing.T) {
    synctest.Test(t, func(t *testing.T) {
        ctx, cancel := context.WithTimeout(t.Context(), 5*time.Second)
        defer cancel()

        time.Sleep(4 * time.Second) // instant in synthetic time
        if ctx.Err() != nil {
            t.Fatal("unexpected timeout")
        }
    })
}
```

**Rationale**: `testing/synctest` removes the two things that make concurrent tests flaky: wall-clock timing and scheduling non-determinism. Real `time.Sleep` calls execute instantly because the fake clock only moves when all bubbled goroutines are blocked, and tests no longer race with real-world CPU contention. Use it whenever a test would otherwise need `time.Sleep` or a generous timeout to "let things happen" (claude-skills (saisudhir14)/skills/go-testing/SKILL.md).

---

## TE-41: Benchmark with `b.Loop()` Instead of Manual `b.N` Loops

**Strength**: SHOULD (Go 1.24+)

**Summary**: Prefer `for b.Loop()` over `for i := 0; i < b.N; i++` in new benchmarks. `b.Loop()` runs setup exactly once (no `b.ResetTimer()` needed) and guarantees the compiler cannot optimize away the loop body.

```go
// Bad: error-prone, setup included in timing
func BenchmarkOld(b *testing.B) {
    input := setupInput() // counted in benchmark time!
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        process(input) // compiler might optimize away
    }
}

// Good: clean and correct (Go 1.24+)
func BenchmarkNew(b *testing.B) {
    input := setupInput() // setup runs once, excluded from timing
    for b.Loop() {
        process(input) // compiler cannot optimize away
    }
}
```

**Rationale**: `b.Loop()` encodes the two easy-to-forget rules of `b.N` benchmarks — exclude setup from timing, and keep the compiler from deleting work whose result is unused — directly in the loop form. Setup before `for b.Loop()` runs once and is not measured, and the runtime keeps arguments live so dead-code elimination cannot invalidate the benchmark. Use the `b.N` form from TE-38 only when maintaining older code (claude-skills (saisudhir14)/skills/go-testing/SKILL.md).

**See also**: TE-38, TE-39

---

## TE-42: Prefer `T.Context()` and `T.Chdir()` over Manual Setup/Teardown

**Strength**: SHOULD (Go 1.24+)

**Summary**: Use `t.Context()` for any context a test needs to cancel, and `t.Chdir()` when a test must run in a different working directory. Both hook into the test's lifecycle automatically — no manual `cancel()`, no save/restore of the previous working directory.

```go
// Bad: no test-scoped context
func TestWithTimeout(t *testing.T) {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    // Context doesn't know it's in a test; may outlive test
}

// Good: test-scoped (Go 1.24+)
func TestWithTimeout(t *testing.T) {
    ctx := t.Context() // canceled after test, before cleanup
    result, err := doWork(ctx)
    // ...
}

// Bad: global side effect
func TestReadConfig(t *testing.T) {
    oldDir, _ := os.Getwd()
    os.Chdir("testdata")
    // forgetting to restore causes test pollution
    os.Chdir(oldDir)
}

// Good: automatic restore (Go 1.24+)
func TestReadConfig(t *testing.T) {
    t.Chdir("testdata")
    data, _ := os.ReadFile("config.json")
    // directory automatically restored after test
}
```

**Rationale**: `t.Context()` is canceled after the test body returns but before `t.Cleanup` functions run, which is exactly what test-scoped work needs — no bespoke `context.WithTimeout` + `defer cancel()` pair. `t.Chdir` records the old working directory and restores it via `Cleanup`, so a panic or early return cannot leave the process in the wrong directory and poison later tests. Both APIs make the hermeticity rule in TE-32 a one-liner (claude-skills (saisudhir14)/skills/go-testing/SKILL.md).

**See also**: TE-32, TE-33

---

## TE-43: Expose Acceptance Tests in a Companion `*test` Package

**Strength**: CONSIDER

**Summary**: If you own an interface that others implement, ship a companion `xxxtest` package whose exported `Verify(impl) error` exercises the contract. External implementers then get a one-line acceptance test. Return `error`, not `t.Fatal`, so the caller chooses how to report failures.

```go
// Bad: No standard way for external implementations to validate correctness
// External package has no way to verify they implement your interface correctly

// Good: Export validation in a companion *test package
package storagetest

func Verify(b storage.Backend) error {
    if err := verifyRoundTrip(b); err != nil {
        return fmt.Errorf("round-trip: %w", err)
    }
    if err := verifyNotFound(b); err != nil {
        return fmt.Errorf("not-found: %w", err)
    }
    return nil
}

// External implementer uses it
func TestMyBackend(t *testing.T) {
    b := mybackend.New(t)
    if err := storagetest.Verify(b); err != nil {
        t.Errorf("MyBackend failed acceptance: %v", err)
    }
}
```

**Rationale**: The contract of an interface is a property of *every* implementation, so the tests belong next to the interface, not copy-pasted into each implementer. Returning `error` (rather than taking `*testing.T` and calling `t.Fatal`) keeps the helper usable from benchmarks, from integration harnesses, and from implementations that want to keep going after a single failure — the caller still decides between `t.Errorf`, `t.Fatal`, or logging. This is the same shape as the stdlib's `testing/fstest.TestFS` (golang-skills (cxuu)/skills/go-testing/references/VALIDATION-APIS.md).

**See also**: TE-31

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Tests in `*_test.go`; stdlib `testing` only | MUST | No third-party framework in the default path |
| 02 | `TestXxx(t *testing.T)` naming | MUST | Also `BenchmarkXxx`, `ExampleXxx`, `FuzzXxx` |
| 03 | `t.Errorf` usually, `t.Fatalf` only when hopeless | SHOULD | Report every failure per run |
| 04 | Failures identify function, input, got vs want | SHOULD | `YourFunc(%v) = %v, want %v` |
| 05 | Table-driven tests are the canonical pattern | SHOULD | `tests`/`tt`/`give`/`want` (Uber) or `tests`/`test`/`want` (Google) |
| 06 | `t.Run` for subtests; function-identifier names | SHOULD | Avoid spaces, slashes, prose |
| 07 | Name the row, not the index | SHOULD | `name` field, printed in failures |
| 08 | Named fields in test-case struct literals | SHOULD | Survives refactors, allows zero-value omission |
| 09 | No conditional logic inside the table loop | SHOULD | `wantErr bool` OK; mock-setup branches split into separate tests |
| 10 | `t.Parallel` per test/subtest | SHOULD | Loop-var fix auto since 1.22 |
| 11 | `t.Helper` in setup/cleanup helpers | SHOULD | Correct failure line numbers |
| 12 | `MustXxx` helpers for value-context setup | SHOULD | Use `t.Fatal` + `t.Helper` |
| 13 | Never call `t.Fatal` from a secondary goroutine | MUST | Use `t.Error` + `return` instead |
| 14 | Run with `-race` | SHOULD | Catches concurrent unsynchronized access |
| 15 | No assertion libraries | SHOULD-AVOID | Plain Go `if got != want { t.Errorf }` |
| 16 | `cmp.Diff` / `cmp.Equal` for structural compare | SHOULD | Not `reflect.DeepEqual` |
| 17 | Label diff direction in messages | SHOULD | `(-want +got)` matches `cmp.Diff(want, got)` |
| 18 | Test error semantics, not error strings | SHOULD | `errors.Is`/`errors.As`; `wantErr bool` |
| 19 | Compare multi-returns individually | SHOULD | No throwaway struct for comparison |
| 20 | Compare semantic values, not serialized bytes | SHOULD | JSON byte output is unstable |
| 21 | `package foo` vs `package foo_test` | CONSIDER | Internal for unexported; external for public API / cycles |
| 22 | Test doubles named by behavior | CONSIDER | `Stub`/`AlwaysDeclines`/`StubService` |
| 23 | Prefer fakes over mocks; accept interfaces | CONSIDER | Fakes exercise more real surface |
| 24 | Prefixed names for local double variables | CONSIDER | `spyCC`, `stubFoo` |
| 25 | Real transports, fake servers | CONSIDER | Don't hand-implement clients |
| 26 | Setup scoped to tests that need it | SHOULD | No `init()`-loaded fixtures |
| 27 | `sync.Once` for expensive cache-once setup | CONSIDER | When teardown not needed |
| 28 | `TestMain` only with teardown | CONSIDER | Factor into `runMain` so defers run |
| 29 | `ExampleXxx` with `// Output:` | SHOULD | Verified documentation |
| 30 | `FuzzXxx` for input-dependent behavior | CONSIDER | Seed with `f.Add`, check with `f.Fuzz` |
| 31 | Validation helpers return a value | SHOULD | `cmp.Option`, `error`, `bool` |
| 32 | Hermetic tests; restore global state | SHOULD | Use `t.Setenv` for env vars |
| 33 | `t.Cleanup` for teardown | SHOULD | Composes with helpers |
| 34 | `t.TempDir` for scratch directories | SHOULD | Auto-cleanup |
| 35 | Fixtures under `testdata/` | SHOULD | Ignored by `go build` |
| 36 | Golden files with `-update` flag | CONSIDER | Large expected outputs |
| 37 | Integration tests: build tags or `testing.Short` | CONSIDER | Keep unit tests fast |
| 38 | `BenchmarkXxx(b *testing.B)`, loop `b.N` | SHOULD | `b.ResetTimer`, `b.ReportAllocs` |
| 39 | Benchmarks back performance claims | SHOULD | Before/after numbers, not argument |
| 40 | `testing/synctest` for timing tests | SHOULD | Synthetic time, deterministic |
| 41 | `b.Loop()` over manual `b.N` | SHOULD | Setup excluded, compiler can't DCE |
| 42 | `T.Context()` / `T.Chdir()` | SHOULD | Self-cleaning scoped helpers |
| 43 | `*test`-package acceptance helpers | CONSIDER | Return `error`, not `t.Fatal` |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for naming, `%q` in diagnostics (CI-26), and the `MixedCaps` rule's exception for test names (CI-07); also CI-33 on `Must` functions
- **API Design**: See `02-api-design.md` for constructor/option patterns — TE-23's "accept an interface" is the testing-side consequence of those API decisions
- **Error Handling**: See `03-error-handling.md` for wrapping, sentinels, `errors.Is`/`errors.As`; TE-18 is how tests assert on those wrapped errors
- **Type Design**: See `04-type-design.md` for struct design that is easy to compare with `cmp.Diff`
- **Interfaces & Methods**: See `05-interfaces-methods.md` for "accept interfaces, return concrete" — the pattern that makes TE-22/TE-23 possible
- **Concurrency**: See `06-concurrency.md` for goroutine lifetimes; TE-13 and TE-14 are the testing-side constraints
- **Performance**: See `08-performance.md` for the patterns benchmarks in TE-38/TE-39 justify
- **Anti-Patterns**: See `09-anti-patterns.md` for testing smells — global state mutation, flaky tests, order-dependent suites

---

## External References

- [`go test`](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — command-line reference for the test runner
- [`testing` package](https://pkg.go.dev/testing) — canonical docs for `T`, `B`, `F`, `M`, `Helper`, `Cleanup`, `TempDir`, `Setenv`, `Parallel`, `Short`
- [`testing/fstest`](https://pkg.go.dev/testing/fstest) — acceptance-test helpers for `io/fs` implementations
- [`github.com/google/go-cmp/cmp`](https://pkg.go.dev/github.com/google/go-cmp/cmp) — structural comparison; `Diff`, `Equal`, `Option`
- [`cmp/cmpopts`](https://pkg.go.dev/github.com/google/go-cmp/cmp/cmpopts) — common `cmp.Option`s: `EquateEmpty`, `EquateErrors`, `EquateApprox`, `IgnoreFields`, `IgnoreInterfaces`
- [Go blog — Using subtests and sub-benchmarks](https://go.dev/blog/subtests)
- [Go blog — Testable examples](https://go.dev/blog/examples)
- [Go blog — Fuzzing is beta ready](https://go.dev/blog/fuzz-beta) — introduction to `testing.F`
- [*Uber Go Style Guide* — Patterns §Test Tables](https://github.com/uber-go/guide/blob/master/style.md#test-tables)
- [*Google Go Style Guide* — Decisions §Test structure](https://google.github.io/styleguide/go/decisions#test-structure) and [§Useful test failures](https://google.github.io/styleguide/go/decisions#useful-test-failures)
- [*Google Go Style Guide* — Best Practices §Tests](https://google.github.io/styleguide/go/best-practices#tests)
- [Go 1.22 release notes — loop variable semantics](https://go.dev/doc/go1.22#language) — the fix that made `tt := tt` unnecessary
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) — the Go team's canonical checklist
