---
# === CORE IDENTIFICATION ===
concept: t.Fatal from Goroutines
slug: t-fatal-from-goroutines

# === CLASSIFICATION ===
category: testing
subcategory: concurrency-in-tests
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Don't call t.Fatal from separate goroutines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "t.Fatal goroutine restriction"
  - "testing from goroutines"
  - "t.FailNow goroutine"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - t-error-vs-t-fatal
extends: []
related:
  - test-helper-error-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't I call t.Fatal from a goroutine?"
  - "How do I report test failures from goroutines?"
  - "Does t.Parallel make t.Fatal unsafe?"
---

# Quick Definition

Never call `t.Fatal`, `t.Fatalf`, or `t.FailNow` from any goroutine other than the one running the Test function (or subtest). Use `t.Error`/`t.Errorf` and return instead. `t.Parallel` does not make `t.Fatal` unsafe.

# Core Definition

As documented in the `testing` package, it is incorrect to call `t.FailNow`, `t.Fatal`, or `t.Fatalf` from any goroutine other than the one running the Test function or subtest. If a test starts new goroutines, these goroutines must not call fatal functions. Use `t.Error` and return instead within goroutines. Test helpers generally do not signal failure from new goroutines, so they can safely use `t.Fatal`. When in doubt, use `t.Error` and return. Adding `t.Parallel` to a test or subtest does not make `t.Fatal` unsafe -- the restriction is specifically about separate goroutines created with the `go` keyword. When all testing API calls are in the test function itself, incorrect usage is easy to spot because the `go` keyword is visible.

# Prerequisites

- **t-error-vs-t-fatal** -- Understanding when to use t.Error vs t.Fatal

# Key Properties

1. `t.Fatal`/`t.FailNow` must only be called from the test's goroutine
2. Goroutines spawned by the test must use `t.Error` + return instead
3. `t.Parallel` does not make `t.Fatal` unsafe
4. Test helpers are generally safe because they run in the test's goroutine
5. The `go` keyword is the signal -- if you see it, avoid `t.Fatal` in that function

# Construction / Recognition

## To Apply:
1. In goroutines spawned by `go func()`: use `t.Errorf` + `return`, never `t.Fatalf`
2. Use `sync.WaitGroup` or channels to wait for goroutines to complete
3. Check results after goroutines finish, in the test's main goroutine

## To Recognize:
1. No `t.Fatal` calls inside `go func()` blocks
2. `t.Error` + `return` pattern inside goroutines
3. Results checked in the main test goroutine after synchronization

# Context & Application

This restriction exists because `t.Fatal` calls `runtime.Goexit()` to stop the current goroutine. When called from a non-test goroutine, it stops that goroutine (not the test), leading to undefined behavior. The test may hang, produce confusing output, or silently miss failures. Passing `testing.T` to helper functions is fine as long as those helpers run in the test's goroutine.

# Examples

**Example 1 -- Correct: t.Error in goroutines**:

```go
// Good:
func TestRevEngine(t *testing.T) {
    engine, err := Start()
    if err != nil {
        t.Fatalf("Engine failed to start: %v", err)
    }

    num := 11
    var wg sync.WaitGroup
    wg.Add(num)
    for i := 0; i < num; i++ {
        go func() {
            defer wg.Done()
            if err := engine.Vroom(); err != nil {
                // This cannot be t.Fatalf.
                t.Errorf("No vroom left on engine: %v", err)
                return
            }
            if rpm := engine.Tachometer(); rpm > 1e6 {
                t.Errorf("Inconceivable engine rate: %d", rpm)
            }
        }()
    }
    wg.Wait()

    if seen := engine.NumVrooms(); seen != num {
        t.Errorf("engine.NumVrooms() = %d, want %d", seen, num)
    }
}
```

# Relationships

## Related
- **test-helper-error-handling** -- Helpers are generally safe since they run in the test goroutine
- **t-error-vs-t-fatal** -- When to use each in the main test goroutine

## Contrasts With
(none)

# Common Errors

- **Error**: Calling `t.Fatal` inside a `go func()` block
  **Correction**: Use `t.Error` + `return`; check results after `wg.Wait()`

- **Error**: Thinking the restriction applies to `t.Parallel` tests
  **Correction**: `t.Parallel` does not make `t.Fatal` unsafe; only `go func()` goroutines do

# Common Confusions

- **Confusion**: Thinking passing `*testing.T` to a helper makes it unsafe
  **Clarification**: Helpers called from the test's goroutine can safely use `t.Fatal`

- **Confusion**: Thinking `t.Error` from a goroutine will stop the goroutine
  **Clarification**: `t.Error` marks failure but continues execution; use `return` explicitly to stop

# Source Reference

Chapter 4: Best Practices, Section "Tests" > "Don't call t.Fatal from separate goroutines".

# Verification Notes

- Definition source: Directly from the goroutine restriction section of Best Practices
- Confidence rationale: HIGH -- explicit rule from the testing package documentation
- Uncertainties: None
- Cross-reference status: References testing package documentation
