---
concept: Must Functions
slug: must-functions
category: error-handling
subcategory: initialization-patterns
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Must functions"
extraction_confidence: high
aliases:
  - MustXYZ pattern
  - must helpers
prerequisites:
  - dont-panic-decisions
  - returning-errors
related:
  - handle-errors-decisions
contrasts_with: []
answers_questions:
  - "What is the MustXYZ naming convention in Go?"
  - "When should Must functions be used?"
  - "How should Must functions be used in tests?"
---

# Quick Definition

Setup helpers that stop the program on failure use the naming convention `MustXYZ`. They should only be called during program startup or package initialization. In tests, the equivalent pattern uses `t.Fatal` instead of `panic` and should be marked as a test helper.

# Core Definition

> "Setup helper functions that stop the program on failure follow the naming convention `MustXYZ` (or `mustXYZ`). In general, they should only be called early on program startup, not on things like user input where normal Go error handling is preferred." -- Google Go Style Guide, "Must functions"

> "The same convention may be used in test helpers that only stop the current test (using `t.Fatal`). Such helpers are often convenient in creating test values, for example in struct fields of table driven tests, as functions that return errors cannot be directly assigned to a struct field." -- Google Go Style Guide, "Must functions"

# Prerequisites

- Understanding of Go's `panic` mechanism
- Knowledge of package initialization and `init` functions
- Familiarity with Go testing framework (`t.Fatal`, `t.Helper`)

# Key Properties

1. **`MustXYZ` naming**: Signals that the function panics on failure.
2. **Startup only**: Call Must functions only during program startup or package initialization, not on user input.
3. **Package-level constants**: Enables initializing package-level variables without `init` functions (e.g., `var DefaultVersion = MustParse("1.2.3")`).
4. **Test helpers use `t.Fatal`**: In tests, Must-style helpers call `t.Fatal` instead of `panic` and should be marked with `t.Helper()`.
5. **"Value" context**: Must helpers are useful where you need a value directly (e.g., struct field in table-driven test).

# Construction / Recognition

**Good -- MustParse for package-level variable:**

```go
func MustParse(version string) *Version {
    v, err := Parse(version)
    if err != nil {
        panic(fmt.Sprintf("MustParse(%q) = _, %v", version, err))
    }
    return v
}

// Package level "constant". If we wanted to use `Parse`, we would have had to
// set the value in `init`.
var DefaultVersion = MustParse("1.2.3")
```

**Good -- test helper using t.Fatal:**

```go
func mustMarshalAny(t *testing.T, m proto.Message) *anypb.Any {
    t.Helper()
    any, err := anypb.New(m)
    if err != nil {
        t.Fatalf("mustMarshalAny(t, m) = %v; want %v", err, nil)
    }
    return any
}

func TestCreateObject(t *testing.T) {
    tests := []struct{
        desc string
        data *anypb.Any
    }{
        {
            desc: "my test case",
            data: mustMarshalAny(t, mypb.Object{}),
        },
        // ...
    }
    // ...
}
```

**Bad -- using Must in normal error-handling context:**

```go
func Version(o *servicepb.Object) (*version.Version, error) {
    // Return error instead of using Must functions.
    v := version.MustParse(o.GetVersionString())
    return dealiasVersion(v)
}
```

# Context & Application

The Must pattern exists because package-level variable initialization cannot return errors. Standard library examples include `template.Must` and `regexp.MustCompile`. The key constraint is that Must functions should only be called with constant or known-good inputs -- if the input could be invalid at runtime, use the error-returning version. In tests, Must helpers assigned to `t.Fatal` enable clean table-driven test definitions where values must be computed but errors are not part of the test case.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **dont-panic-decisions**: Must functions are the controlled exception to the no-panic rule.
- **handle-errors-decisions**: Normal functions should return errors rather than panicking.

# Common Errors

1. Using Must functions on user input or runtime-variable data.
2. Using `panic` in test helpers instead of `t.Fatal`.
3. Forgetting `t.Helper()` in test Must helpers, producing confusing failure locations.
4. Calling Must functions in request handlers or non-initialization code.

# Common Confusions

- **Must in tests vs. production**: In production, Must panics. In tests, the equivalent calls `t.Fatal`, which only stops the current test, not the entire test suite.
- **When ordinary error handling suffices**: If you can refactor to use error returns, do so. Must is a last resort for initialization contexts.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Must functions" section.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
