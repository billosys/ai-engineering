---
# === CORE IDENTIFICATION ===
concept: t.Error vs t.Fatal
slug: t-error-vs-t-fatal

# === CLASSIFICATION ===
category: testing
subcategory: test-failures
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "t.Error vs. t.Fatal"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "test error vs fatal"
  - "when to use t.Fatal"
  - "test failure modes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - keep-going
extends: []
related:
  - test-helper-error-handling
  - t-fatal-from-goroutines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use t.Error vs t.Fatal in Go tests?"
  - "Is it safe to use t.Fatal in subtests?"
  - "How should I handle table-driven test failures?"
---

# Quick Definition

Use `t.Error` for continuable failures (the test should keep checking more things). Use `t.Fatal` for setup failures and conditions that make continuing impossible. In table-driven tests without subtests, use `t.Error` + `continue`; with subtests (`t.Run`), `t.Fatal` is fine as it only ends the current subtest.

# Core Definition

Tests should generally not abort at the first problem (following the keep-going principle). However, `t.Fatal` is appropriate when test setup fails and the rest of the test cannot run, or when a failure in a table-driven test's setup makes it impossible to continue with that entry. In table-driven tests without `t.Run` subtests, use `t.Error` followed by `continue` to move to the next entry. In subtests (inside `t.Run`), use `t.Fatal` since it only ends the current subtest, allowing the test to progress to the next one. For whole-test-function setup that precedes a table-driven loop, `t.Fatal` is appropriate for failures that prevent any entries from running.

# Prerequisites

- **keep-going** -- The Decisions chapter guidance that tests should not abort at first failure

# Key Properties

1. `t.Error`: marks the test as failed but continues execution
2. `t.Fatal`: marks the test as failed and stops the current test/subtest immediately
3. Use `t.Fatal` for setup failures (preconditions that make continuing pointless)
4. In table-driven tests without subtests: `t.Error` + `continue` for per-entry failures
5. In subtests (`t.Run`): `t.Fatal` is safe -- only ends the current subtest
6. Not always safe to call `t.Fatal` from goroutines (see t-fatal-from-goroutines)

# Construction / Recognition

## To Apply:
1. For assertion failures where more checks could be valuable: use `t.Error`/`t.Errorf`
2. For setup failures that make proceeding impossible: use `t.Fatal`/`t.Fatalf`
3. In table tests without `t.Run`: `t.Errorf(...)` then `continue`
4. In table tests with `t.Run`: `t.Fatal` within the subtest is fine

## To Recognize:
1. `t.Error` used for validation failures, `t.Fatal` for setup failures
2. Table-driven tests using subtests with `t.Fatal` per entry
3. No `t.Fatal` calls from separate goroutines

# Context & Application

The distinction mirrors the difference between "this assertion failed but we can check more things" vs "this precondition failed and nothing else will be meaningful." The keep-going approach provides more diagnostic information in a single test run, which is especially valuable in CI environments.

# Examples

**Example 1 -- Table-driven test with subtests**:

In a table-driven test using `t.Run`, `t.Fatal` within the subtest is safe because it only stops the current subtest, not the entire test function.

**Example 2 -- Setup failure**:

```go
func TestFoo(t *testing.T) {
    engine, err := Start()
    if err != nil {
        t.Fatalf("Engine failed to start: %v", err) // Can't continue without engine
    }
    // ... test using engine
}
```

# Relationships

## Related
- **test-helper-error-handling** -- How test helpers should use t.Fatal
- **t-fatal-from-goroutines** -- Restriction on calling t.Fatal from goroutines

## Contrasts With
(none)

# Common Errors

- **Error**: Using `t.Fatal` for every assertion in a test
  **Correction**: Use `t.Error` for continuable assertions; reserve `t.Fatal` for setup failures

- **Error**: Using `t.Error` (without `continue`) in a table-driven test loop without subtests
  **Correction**: After `t.Error`, add `continue` to skip to the next entry, or use `t.Run` subtests

# Common Confusions

- **Confusion**: Thinking `t.Fatal` in a subtest stops the entire test function
  **Clarification**: In `t.Run`, `t.Fatal` only stops the current subtest

- **Confusion**: Thinking `t.Parallel` makes `t.Fatal` unsafe
  **Clarification**: `t.Parallel` does not make `t.Fatal` unsafe; goroutines do

# Source Reference

Chapter 4: Best Practices, Section "Tests" > "t.Error vs. t.Fatal".

# Verification Notes

- Definition source: Directly from "t.Error vs. t.Fatal" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with specific scenarios
- Uncertainties: None
- Cross-reference status: References decisions#keep-going
