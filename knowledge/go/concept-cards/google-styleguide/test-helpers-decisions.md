---
# === CORE IDENTIFICATION ===
concept: Test Helpers
slug: test-helpers-decisions

# === CLASSIFICATION ===
category: testing
subcategory: test-utilities
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Test helpers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "t.Helper"
  - "test setup functions"
  - "mark test helpers"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - assertion-libraries
  - table-driven-tests-decisions
  - contexts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a test helper in Go?"
  - "When should I call t.Helper()?"
  - "Should test helpers use t.Fatal or t.Error?"
  - "How are test helpers different from assertion libraries?"
  - "Where should the *testing.T parameter go in a test helper?"
---

# Quick Definition

Test helpers perform setup or cleanup tasks. Mark them with `t.Helper()` so failures are attributed to the calling line. Place `*testing.T` after `context.Context` but before other parameters. Use `t.Fatal` in helpers for environment failures. Do not use this pattern to build assertion libraries.

# Core Definition

A test helper is a function that performs setup or cleanup, where all failures represent environment problems (not code-under-test bugs) -- for example, when a test database cannot be started. If a helper accepts `*testing.T`, call `t.Helper()` at the start so that failure locations are attributed to the line that called the helper rather than the line inside the helper. The `*testing.T` parameter should come after a `context.Context` parameter (if present) and before remaining parameters. Use `t.Fatal` in setup helpers when failure makes subsequent test steps meaningless. Do not use `t.Helper()` to build assertion libraries -- helpers and assertions serve different purposes.

# Prerequisites

- **Go testing package** -- Familiarity with `*testing.T`, `t.Helper()`, `t.Fatal`
- **assertion-libraries** -- Understanding the distinction between helpers and assertion libraries

# Key Properties

1. **Call t.Helper()**: First line of any helper that accepts `*testing.T`
2. **Environment failures**: Helpers report failures of the test environment, not the code under test
3. **Parameter order**: `ctx context.Context, t *testing.T, remaining...`
4. **Fatal in helpers**: Setup helpers that must succeed should use `t.Fatal`
5. **Not assertion libraries**: `t.Helper()` should not be used to build assertion DSLs
6. **Same goroutine**: Helpers calling `t.Helper()` must be called from the same goroutine as the test
7. **Applies to benchmarks and fuzz**: The guidance extends to benchmark and fuzz helpers too

# Construction / Recognition

## To Apply:
1. Define a function that performs setup or cleanup
2. Accept `*testing.T` (after `context.Context` if present)
3. Call `t.Helper()` as the first line
4. Use `t.Fatal` for setup failures that would make further testing pointless
5. Return useful data (file contents, handles, etc.) to the caller

## To Recognize:
1. Helper functions missing `t.Helper()` -- failures will point to the wrong line
2. Helpers that perform validation/assertion rather than setup/cleanup
3. Helpers with `*testing.T` as the first parameter when a context is also needed

# Context & Application

Test helpers make tests concise by extracting repeated setup logic. The `t.Helper()` call is essential for debugging: without it, a failure in `readFile` at line 42 of the helper would be reported as such, even though the real question is "which test called readFile?" With `t.Helper()`, the failure points to the test function that invoked the helper.

# Examples

**Example 1 -- File reading helper**:

```go
func TestSomeFunction(t *testing.T) {
    golden := readFile(t, "testdata/golden-result.txt")
    // ... tests against golden ...
}

func readFile(t *testing.T, filename string) string {
    t.Helper()
    contents, err := runfiles.ReadFile(filename)
    if err != nil {
        t.Fatal(err)
    }
    return string(contents)
}
```

**Example 2 -- Helper with context**:

```go
func readTestFile(ctx context.Context, t *testing.T, path string) string {
    t.Helper()
    // ...
}
```

# Relationships

## Related
- **assertion-libraries** -- Test helpers differ from assertion libraries; helpers do setup, not validation
- **table-driven-tests-decisions** -- Helpers simplify setup in table-driven tests
- **contexts** -- Context comes before `*testing.T` in helper parameter lists

# Common Errors

- **Error**: Forgetting to call `t.Helper()` in a test helper
  **Correction**: Always call `t.Helper()` as the first line so failure attribution is correct.

- **Error**: Using test helpers to build assertion-style validation
  **Correction**: Helpers should perform setup/cleanup. Validation belongs in the test function itself.

# Common Confusions

- **Confusion**: Thinking `t.Helper()` changes the behavior of `t.Fatal` or `t.Error`
  **Clarification**: It only changes how the failure location is reported -- it attributes the failure to the caller rather than the helper.

- **Confusion**: Thinking the `*testing.T` parameter should always be first
  **Clarification**: If a context is present, `context.Context` comes first, then `*testing.T`.

# Source Reference

Chapter 3: Style Decisions, Section "Test helpers" under "Test structure".

# Verification Notes

- Definition source: Directly from the "Test helpers" section
- Confidence rationale: HIGH -- explicit guidance with clear examples
- Uncertainties: None
- Cross-reference status: References best practices on test functions for helper vs assertion distinction
