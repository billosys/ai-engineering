---
# === CORE IDENTIFICATION ===
concept: Examples in Documentation
slug: examples-in-documentation

# === CLASSIFICATION ===
category: commentary
subcategory: documentation
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "runnable examples"
  - "example test functions"
  - "Godoc examples"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - package-comments
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where should Go example code live?"
  - "How do runnable examples show up in Godoc?"
  - "Can I put examples in comments instead of test files?"
---

# Quick Definition

Provide runnable examples in test files (`_test.go`) to demonstrate package usage. These examples appear in Godoc. When a runnable example is not feasible, example code can be provided within comments.

# Core Definition

Packages should clearly document their intended usage by providing runnable examples. Runnable examples belong in test files (not production source files) and automatically appear in Godoc documentation. Go's testing framework supports `Example` functions that serve as both documentation and verified tests. If providing a runnable example is not feasible, example code can be included within code comments, following standard formatting conventions (indented to render as code in Godoc) (Google Go Style Guide, "Style Decisions", "Examples").

# Prerequisites

- **doc-comments** -- Understanding doc comment conventions that examples supplement
- **Go testing package** -- Knowledge of how `Example` functions work in Go test files

# Key Properties

1. Runnable examples belong in `_test.go` files
2. Examples show up automatically in Godoc
3. Examples serve as both documentation and tests (they are verified by `go test`)
4. If runnable examples are not feasible, use indented code in comments
5. Comment-based examples should follow standard formatting conventions

# Construction / Recognition

## To Apply:
1. Create `Example` functions in test files (e.g., `ExampleFoo`, `ExampleFoo_method`)
2. Include `// Output:` comments to make examples verifiable
3. Place examples in `example_test.go` or alongside related tests
4. For non-runnable examples, indent code within comments for Godoc rendering

## To Recognize:
1. Look for packages lacking `Example` functions in test files
2. Look for complex APIs without usage demonstrations
3. Look for example code in production source files -- it should be in test files

# Context & Application

Go's example system is uniquely powerful: examples are compiled and run as tests, ensuring they stay up to date with the API. Unlike documentation in many languages that can drift from reality, Go examples fail the build if the API changes in an incompatible way. This makes them the gold standard for Go package documentation. The `time.Duration` example in the standard library is a canonical reference for this pattern.

# Examples

**Example 1 -- Good: runnable example in test file** (Decisions, "Examples"):

```go
// In example_test.go:
func ExampleDuration() {
    t1 := time.Date(2022, time.January, 1, 0, 0, 0, 0, time.UTC)
    t2 := time.Date(2022, time.March, 1, 0, 0, 0, 0, time.UTC)
    fmt.Println(t2.Sub(t1))
    // Output:
    // 1416h0m0s
}
```

**Example 2 -- Acceptable: example code in comments when runnable example is not feasible**:

```go
// Process transforms input data according to the configured rules.
//
// Example usage:
//
//     p := NewProcessor(config)
//     result, err := p.Process(input)
//     if err != nil {
//         log.Fatal(err)
//     }
func (p *Processor) Process(input []byte) ([]byte, error) {
```

# Relationships

## Related
- **doc-comments** -- Examples supplement doc comments with concrete usage demonstrations
- **package-comments** -- Package-level examples demonstrate overall package usage

# Common Errors

- **Error**: Placing example code in production source files
  **Correction**: Runnable examples must be in `_test.go` files

- **Error**: Writing examples without `// Output:` comments
  **Correction**: Include output comments to make examples verifiable by `go test`

# Common Confusions

- **Confusion**: Thinking examples are only documentation and not tests
  **Clarification**: Go `Example` functions are compiled and run by `go test`, verifying their correctness

- **Confusion**: Believing every function needs a runnable example
  **Clarification**: Focus on key entry points and complex APIs; simple getters and setters rarely need examples

# Source Reference

Chapter 3: Style Decisions, Section "Examples".

# Verification Notes

- Definition source: Directly from the "Examples" section of Google Go Style Decisions
- Confidence rationale: HIGH -- clear guidance with references to Go blog and standard library examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
