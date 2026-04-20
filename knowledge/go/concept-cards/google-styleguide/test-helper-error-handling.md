---
# === CORE IDENTIFICATION ===
concept: Test Helper Error Handling
slug: test-helper-error-handling

# === CLASSIFICATION ===
category: testing
subcategory: test-helpers
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Error handling in test helpers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "test setup helpers"
  - "must helpers in tests"
  - "t.Helper usage"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - t-error-vs-t-fatal
extends:
  - mark-test-helpers
related:
  - t-fatal-from-goroutines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should test helpers handle errors?"
  - "Why should test helpers call t.Helper()?"
  - "Should test helpers return errors or call t.Fatal?"
---

# Quick Definition

Test helpers that perform setup should call `t.Fatal` on failure (not return errors) and always call `t.Helper()` so failure reports point to the caller. Include descriptive failure messages explaining what went wrong. Use `t.Cleanup` for teardown.

# Core Definition

Test helpers (functions that perform setup and cleanup) should call `t.Fatal` when they fail, because a setup failure means the test cannot continue. This is preferred over returning errors, which clutters the calling test with error-handling boilerplate. Helpers must call `t.Helper()` so that when a failure occurs, the reported file and line number points to the caller of the helper, not the helper itself. Failure messages should describe what went wrong (e.g., "Setup failed: could not write pak0 asset: ...") because as the number of error-producing steps in the helper increases, clear messages become critical. Use `t.Cleanup` to register cleanup functions. If a helper does not interact with the testing framework (cannot cause failure), it does not need `t` as a parameter.

# Prerequisites

- **t-error-vs-t-fatal** -- Understanding when to use t.Error vs t.Fatal

# Key Properties

1. Test helpers call `t.Fatal` on failure (not return errors)
2. Always call `t.Helper()` at the top of the helper
3. Include descriptive failure messages with context
4. `t.Helper()` makes failure reports point to the calling test, not the helper
5. Use `t.Cleanup` for registering teardown functions
6. If a helper cannot cause test failure, omit `t` from its parameters

# Construction / Recognition

## To Apply:
1. Start every test helper with `t.Helper()`
2. Call `t.Fatalf` with a descriptive message on failure
3. Prefix helper names with `must` to signal they fatal on error
4. Register cleanup with `t.Cleanup`
5. Remove `t` parameter if the helper never interacts with the testing framework

## To Recognize:
1. Functions starting with `t.Helper()`
2. `must`-prefixed helper names that call `t.Fatal`
3. Failure messages that describe context, not just the raw error

# Context & Application

The `t.Helper()` mechanism is critical for debugging. Without it, failures report the line inside the helper function, which is unhelpful when the same helper is called from many tests. With `t.Helper()`, failures report the line in the test function that called the helper, making it immediately clear which test case triggered the failure. Go 1.14 introduced `t.Cleanup` as a complement, allowing helpers to register cleanup actions.

# Examples

**Example 1 -- Good: test helper with t.Fatal**:

```go
// Good:
func mustAddGameAssets(t *testing.T, dir string) {
    t.Helper()
    if err := os.WriteFile(path.Join(dir, "pak0.pak"), pak0, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak0 asset: %v", err)
    }
    if err := os.WriteFile(path.Join(dir, "pak1.pak"), pak1, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak1 asset: %v", err)
    }
}
```

**Example 2 -- Bad: returning errors from helper**:

```go
// Bad:
func addGameAssets(t *testing.T, dir string) error {
    t.Helper()
    if err := os.WriteFile(path.Join(d, "pak0.pak"), pak0, 0644); err != nil {
        return err
    }
    // ... caller must handle this error, adding boilerplate
}
```

**Example 3 -- t.Helper() effect on failure reporting**:

Without `t.Helper()`, failure reports point to the helper: `paint_test.go:15`. With `t.Helper()`, they point to the test: `paint_test.go:32`.

# Relationships

## Related
- **t-fatal-from-goroutines** -- Restriction on calling t.Fatal from goroutines
- **mark-test-helpers** -- Decisions chapter guidance on marking test helpers

## Contrasts With
(none)

# Common Errors

- **Error**: Forgetting to call `t.Helper()` in a test helper
  **Correction**: Always call `t.Helper()` first; failure reports will point to the wrong location otherwise

- **Error**: Providing bare error messages without context
  **Correction**: Include what the helper was trying to do: "Setup failed: could not write pak0 asset: ..."

# Common Confusions

- **Confusion**: Thinking test helpers and assertion helpers are the same
  **Clarification**: Test helpers do setup/cleanup (t.Fatal on failure); assertion helpers check correctness (not idiomatic in Go)

- **Confusion**: Thinking every function called from a test should use t.Helper
  **Clarification**: Only functions that call testing methods (t.Fatal, t.Error, etc.) need t.Helper

# Source Reference

Chapter 4: Best Practices, Section "Tests" > "Error handling in test helpers".

# Verification Notes

- Definition source: Directly from "Error handling in test helpers" section
- Confidence rationale: HIGH -- extensive guidance with before/after examples and output
- Uncertainties: None
- Cross-reference status: References decisions#mark-test-helpers, GoTip #4
