---
# === CORE IDENTIFICATION ===
concept: Error Structure
slug: error-structure

# === CLASSIFICATION ===
category: error-handling
subcategory: error-design
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Error structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sentinel errors"
  - "structured errors"
  - "error matching"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - adding-information-to-errors
  - placement-of-w-in-errors
  - handle-errors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use sentinel errors vs custom error types?"
  - "How should callers distinguish between different error conditions?"
  - "Why should I avoid string-matching errors?"
---

# Quick Definition

Give errors structure when callers need to distinguish error conditions programmatically. Use sentinel values for simple cases, `errors.Is`/`errors.As` for wrapped errors, and custom struct types for errors carrying extra data. Never match errors by their string representation.

# Core Definition

If callers need to interrogate errors to distinguish different conditions, the error should have structure that supports programmatic inspection rather than string matching. The simplest structured errors are unparameterized global sentinel values (e.g., `var ErrDuplicate = errors.New("duplicate")`). Callers compare with `==` for unwrapped sentinels or `errors.Is` for potentially wrapped errors. For errors carrying extra information (like file paths), use custom struct types with exported fields (e.g., `os.PathError`). For richer error categorization, consider using gRPC status codes with canonical codes. Never use `regexp.MatchString` or similar string matching to distinguish errors.

# Prerequisites

(none)

# Key Properties

1. Sentinel values: unparameterized global `errors.New` values for simple error categories
2. Use `==` comparison for unwrapped sentinels; `errors.Is` for potentially wrapped errors
3. Custom error types (structs implementing `error`) carry structured data callers can access
4. Never match errors by their string representation
5. Status codes (e.g., gRPC canonical codes) provide another structured error approach

# Construction / Recognition

## To Apply:
1. Define sentinel errors as package-level `var` with `errors.New`
2. Define custom error types as structs with exported fields when callers need extra data
3. Use `errors.Is` for sentinel comparison (handles wrapping)
4. Use `errors.As` to extract custom error types from wrapped chains
5. Document which errors a function returns

## To Recognize:
1. Package-level `var Err... = errors.New(...)` declarations
2. Callers using `errors.Is`/`errors.As` instead of string matching
3. Custom error structs with accessible fields

# Context & Application

This guidance applies to both production code and tests. Structured errors enable callers to handle different failure modes programmatically. The `os` package exemplifies this with `os.PathError` containing the operation, path, and underlying error. When choosing between sentinel values and custom types, consider whether the caller needs additional data beyond the error category. Status codes are useful at system boundaries (e.g., gRPC services) where errors need canonical categorization.

# Examples

**Example 1 -- Sentinel error values**:

```go
var (
    ErrDuplicate = errors.New("duplicate")
    ErrMarsupial = errors.New("marsupials are not supported")
)

func process(animal Animal) error {
    switch {
    case seen[animal]:
        return ErrDuplicate
    case marsupial(animal):
        return ErrMarsupial
    }
    seen[animal] = true
    return nil
}
```

**Example 2 -- Matching with errors.Is**:

```go
// Good:
func handlePet(...) {
    switch err := process(an); {
    case errors.Is(err, ErrDuplicate):
        return fmt.Errorf("feed %q: %v", an, err)
    case errors.Is(err, ErrMarsupial):
        alternate = an.BackupAnimal()
        return handlePet(..., alternate, ...)
    }
}
```

**Example 3 -- Bad: string matching**:

```go
// Bad:
func handlePet(...) {
    err := process(an)
    if regexp.MatchString(`duplicate`, err.Error()) {...}
    if regexp.MatchString(`marsupial`, err.Error()) {...}
}
```

# Relationships

## Related
- **adding-information-to-errors** -- How to annotate errors with context
- **placement-of-w-in-errors** -- Where to place %w when wrapping errors
- **handle-errors** -- General error handling guidance from Decisions chapter

## Contrasts With
(none)

# Common Errors

- **Error**: Using string matching to distinguish error conditions
  **Correction**: Use sentinel values with `errors.Is` or custom types with `errors.As`

- **Error**: Creating parameterized errors where a sentinel would suffice
  **Correction**: Use simple sentinels when no additional data is needed

# Common Confusions

- **Confusion**: Using `==` comparison when errors might be wrapped
  **Clarification**: Use `errors.Is` which traverses the wrapping chain; `==` only works for direct comparison

- **Confusion**: Thinking `errors.Unwrap` is the right way to inspect errors
  **Clarification**: Prefer `errors.Is` and `errors.As` as they handle multi-errors; `errors.Unwrap` is generally not recommended

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "Error structure".

# Verification Notes

- Definition source: Directly from the "Error structure" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with clear examples
- Uncertainties: None
- Cross-reference status: References GoTip #13, GoTip #48, GoTip #89
