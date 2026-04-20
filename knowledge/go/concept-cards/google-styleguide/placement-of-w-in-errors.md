---
# === CORE IDENTIFICATION ===
concept: Placement of %w in Errors
slug: placement-of-w-in-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-wrapping
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Placement of %w in errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error wrapping placement"
  - "error chain ordering"
  - "sentinel error placement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adding-information-to-errors
extends: []
related:
  - error-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where should %w appear in an error format string?"
  - "How does %w placement affect error chain printing order?"
  - "When should a sentinel error be placed at the beginning of the error string?"
---

# Quick Definition

Place `%w` at the end of the error string so that printed error text mirrors the error chain structure (newest to oldest). The exception is sentinel errors, which should be placed at the beginning of the string to immediately identify the error category.

# Core Definition

When wrapping errors with `fmt.Errorf`, prefer placing `%w` at the end of the format string with the pattern `[context]: %w`. This ensures that the printed error text reads newest-to-oldest, matching the logical error chain structure. Placing `%w` at the beginning reverses the print order (oldest-to-newest) which is confusing. Placing `%w` in the middle produces output that is neither oldest-to-newest nor newest-to-oldest. The exception is sentinel errors -- errors that serve as primary categorization of a failure (e.g., "parse error", "not found"). For sentinels, placing `%w` at the beginning immediately identifies the error category, improving readability: `fmt.Errorf("%w: specific detail: %v", ErrParse, err)`.

# Prerequisites

- **adding-information-to-errors** -- Understanding when and why to wrap with %w

# Key Properties

1. Default: place `%w` at the end -- `fmt.Errorf("context: %w", err)`
2. Error text then reads newest-to-oldest, matching the chain structure
3. Placing `%w` at the beginning reverses print order -- confusing for general errors
4. Exception: sentinel errors should be placed at the beginning for immediate category identification
5. Wrapped errors form a chain traversable via `Unwrap()`, `errors.Is`, and `errors.As`

# Construction / Recognition

## To Apply:
1. For general wrapping: `fmt.Errorf("couldn't do X: %w", err)` -- `%w` at end
2. For sentinel wrapping: `fmt.Errorf("%w: specific detail: %v", ErrCategory, err)` -- sentinel first
3. Verify by printing: does the error text read logically?

## To Recognize:
1. Error format strings with `%w` at the end (standard pattern)
2. Sentinel errors at the beginning of format strings for categorization

# Context & Application

The error chain always goes newest-to-oldest regardless of `%w` placement. However, the printed representation depends on where `%w` appears. Consistent placement at the end ensures error messages are predictable and readable. The sentinel exception exists because identifying the error category (e.g., "parse error") immediately gives the reader the most important information first, with details following.

# Examples

**Example 1 -- Good: %w at end (newest-to-oldest printing)**:

```go
err1 := fmt.Errorf("err1")
err2 := fmt.Errorf("err2: %w", err1)
err3 := fmt.Errorf("err3: %w", err2)
fmt.Println(err3) // err3: err2: err1
```

**Example 2 -- Bad: %w at beginning (reversed printing)**:

```go
err1 := fmt.Errorf("err1")
err2 := fmt.Errorf("%w: err2", err1)
err3 := fmt.Errorf("%w: err3", err2)
fmt.Println(err3) // err1: err2: err3
```

**Example 3 -- Good: sentinel error at beginning**:

```go
// Good:
var ErrParse = fmt.Errorf("parse error")
var ErrParseInvalidHeader = fmt.Errorf("%w: invalid header", ErrParse)

func parseHeader() error {
    err := checkHeader()
    return fmt.Errorf("%w: invalid character in header: %v", ErrParseInvalidHeader, err)
}
```

# Relationships

## Related
- **error-structure** -- Defines sentinel errors and custom types used in wrapping
- **adding-information-to-errors** -- When to use %w vs %v

## Contrasts With
(none)

# Common Errors

- **Error**: Placing `%w` in the middle of a format string
  **Correction**: Place at the end for general wrapping, or at the beginning only for sentinel categorization

- **Error**: Placing a sentinel error at the end where it gets buried in details
  **Correction**: Place sentinel `%w` at the beginning for immediate category identification

# Common Confusions

- **Confusion**: Thinking `%w` placement affects the error chain structure
  **Clarification**: The chain is always newest-to-oldest; placement only affects the printed string representation

- **Confusion**: Always putting `%w` at the end, even for sentinel categorization
  **Clarification**: Sentinels are the exception -- place them at the beginning to lead with the error category

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "Placement of %w in errors".

# Verification Notes

- Definition source: Directly from "Placement of %w in errors" including sentinel placement subsection
- Confidence rationale: HIGH -- explicit guidance with mermaid diagrams and multiple examples
- Uncertainties: None
- Cross-reference status: References GoTip #48, GoTip #106
