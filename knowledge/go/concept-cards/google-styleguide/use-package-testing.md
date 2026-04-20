---
# === CORE IDENTIFICATION ===
concept: Use Package testing
slug: use-package-testing

# === CLASSIFICATION ===
category: testing
subcategory: test-framework
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Use package testing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "standard testing package"
  - "no third-party test frameworks"
  - "Go testing framework policy"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - assertion-libraries
  - test-package
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What testing framework should I use in Go?"
  - "Can I use third-party testing frameworks in Go at Google?"
  - "What capabilities does the standard testing package provide?"
  - "Why does Go not have a built-in assertion framework?"
---

# Quick Definition

Use the standard `testing` package exclusively. Third-party testing frameworks and assertion libraries are not permitted. The `testing` package provides a minimal but complete set of functionality designed to work cohesively with Go's language features.

# Core Definition

The Go standard library `testing` package is the only permitted testing framework in the Google codebase. Assertion libraries and third-party testing frameworks are explicitly not allowed. The `testing` package provides top-level tests, benchmarks, runnable examples, subtests, logging, and both non-fatal (`t.Error`) and fatal (`t.Fatal`) failure modes. These features are designed to work cohesively with core Go language features like composite literals and if-with-initializer syntax, enabling clear, readable, and maintainable tests without the need for a testing DSL.

# Prerequisites

- **Go testing package** -- Basic familiarity with the `testing` package API
- **Go language features** -- Composite literals, if-with-initializer syntax

# Key Properties

1. **Only permitted framework**: The standard `testing` package is the only allowed testing framework
2. **No third-party frameworks**: Third-party test frameworks (testify, gocheck, etc.) are not permitted
3. **No assertion libraries**: Assertion libraries are explicitly excluded
4. **Complete feature set**: Provides tests, benchmarks, examples, subtests, logging, and failure modes
5. **Language integration**: Designed to leverage composite literals and if-with-initializer syntax
6. **Go FAQ alignment**: The Go FAQ explicitly addresses why a testing framework is not included

# Construction / Recognition

## To Apply:
1. Import only `testing` for test infrastructure
2. Use `t.Errorf`, `t.Fatalf`, `t.Log`, `t.Run` for test logic
3. Use composite literals to construct expected values
4. Use if-with-initializer for concise comparison and error checking

## To Recognize:
1. Imports of `github.com/stretchr/testify`, `gopkg.in/check.v1`, or similar
2. Usage of `assert.Equal`, `require.NoError`, or other assertion patterns
3. Custom test runner frameworks

# Context & Application

Go's testing philosophy favors simplicity and directness over abstraction. The `testing` package keeps tests as plain Go code, making them accessible to all Go developers without learning a testing DSL. This also makes large-scale changes and automated refactoring simpler, since there is one consistent testing pattern across the entire codebase.

# Examples

**Example 1 -- Standard testing package capabilities**:

```go
func TestFoo(t *testing.T) {
    // Top-level test with subtests
    t.Run("case1", func(t *testing.T) {
        // Composite literal for expected value
        want := Result{Value: 42, OK: true}
        // If-with-initializer for concise checking
        if got := Foo("input"); !cmp.Equal(got, want) {
            t.Errorf("Foo(%q) = %v, want %v", "input", got, want)
        }
    })
}
```

# Relationships

## Related
- **assertion-libraries** -- Assertion libraries are the specific anti-pattern this rule addresses
- **test-package** -- Test package organization works with the standard testing package

# Common Errors

- **Error**: Importing third-party testing frameworks for "convenience"
  **Correction**: Use the standard `testing` package. The apparent convenience comes at the cost of fragmentation and maintenance burden.

# Common Confusions

- **Confusion**: Thinking the `testing` package is too limited for real-world tests
  **Clarification**: Combined with `cmp`, `fmt`, and Go's language features, the `testing` package covers all standard testing needs. The apparent simplicity is intentional.

- **Confusion**: Thinking `cmp` is a third-party testing framework
  **Clarification**: `cmp` is a comparison library maintained by the Go team, designed to complement the `testing` package. It is not a test framework.

# Source Reference

Chapter 3: Style Decisions, Section "Use package testing" under "Test structure".

# Verification Notes

- Definition source: Directly from the "Use package testing" section
- Confidence rationale: HIGH -- the guidance is explicit and unambiguous
- Uncertainties: None
- Cross-reference status: References Go FAQ section on testing frameworks; related to assertion-libraries card
