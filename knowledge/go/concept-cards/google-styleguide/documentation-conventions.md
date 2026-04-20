---
# === CORE IDENTIFICATION ===
concept: Documentation Conventions
slug: documentation-conventions

# === CLASSIFICATION ===
category: commentary
subcategory: documentation
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Documentation conventions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "godoc conventions"
  - "API documentation"
  - "documenting Go code"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends:
  - commentary
related:
  - godoc-formatting
  - signal-boosting
  - error-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What should I document in function parameters and configuration?"
  - "How should I document context behavior?"
  - "How should I document concurrency safety?"
  - "How should I document cleanup requirements?"
  - "How should I document error return values?"
---

# Quick Definition

Document Go code for godoc readability: focus on non-obvious parameters, document context behavior only when it deviates from convention, state concurrency safety when ambiguous, specify cleanup requirements, and document significant error types and sentinel values.

# Core Definition

Go code documented in familiar style is easier to read and less likely to be misused. Runnable examples in godoc are an excellent way to explain API usage. For parameters and configuration, document only the error-prone or non-obvious fields -- restating the obvious (e.g., "format is the format") adds no value. For contexts, the standard behavior (cancellation interrupts the function, returns `ctx.Err()`) is implied and should not be restated; only document non-standard context behavior. For concurrency, read-only operations are assumed safe for concurrent use; document concurrency safety only when it is ambiguous (e.g., LRU cache lookup that mutates internal state), when the API provides synchronization, or when the API consumes interfaces with concurrency requirements. Always document cleanup requirements (e.g., "Call Stop to release resources"). Document significant error sentinel values and custom error types so callers know what conditions to handle programmatically. Preview documentation using the Go documentation server.

# Prerequisites

- **clarity-principle** -- Understanding that documentation serves the reader

# Key Properties

1. Document non-obvious parameters, not obvious ones
2. Context cancellation behavior is implied -- only document deviations
3. Read-only operations are assumed concurrent-safe -- document exceptions
4. Mutating operations are assumed NOT concurrent-safe -- document if they are
5. Always document cleanup requirements
6. Document significant error types with pointer receiver details
7. Preview docs with the Go documentation server

# Construction / Recognition

## To Apply:
1. Ask: would a reader guess this from the signature? If yes, skip the doc
2. For context: only document if behavior differs from standard cancellation
3. For concurrency: document if the operation looks read-only but mutates, or if it provides synchronization
4. For cleanup: always specify what the caller must do and how
5. For errors: document sentinel values and whether error types are pointer receivers

## To Recognize:
1. Documentation that adds value beyond what the signature already conveys
2. Context docs only present when behavior is non-standard
3. Cleanup requirements clearly stated

# Context & Application

This is an extensive section covering parameters, contexts, concurrency, cleanup, and errors. The guidance reflects Go's philosophy of convention over documentation -- when behavior follows convention, documenting it is noise. When behavior deviates, documentation is critical. Package-level documentation should describe overall error conventions when they apply to most functions in the package (like `package os` documenting that errors are often `*PathError`).

# Examples

**Example 1 -- Bad: restating the obvious**:

```go
// Bad:
// Sprintf formats according to a format specifier and returns the resulting string.
// format is the format, and data is the interpolation data.
func Sprintf(format string, data ...any) string
```

**Example 2 -- Good: documenting non-obvious behavior**:

```go
// Good:
// Sprintf formats according to a format specifier and returns the resulting string.
// The provided data is used to interpolate the format string. If the data does not
// match the expected format verbs, the function will inline warnings about formatting
// errors into the output string.
func Sprintf(format string, data ...any) string
```

**Example 3 -- Documenting concurrency when ambiguous**:

```go
// Good:
// Lookup returns the data associated with the key from the cache.
// This operation is not safe for concurrent use.
func (*Cache) Lookup(key string) (data []byte, ok bool)
```

**Example 4 -- Documenting cleanup**:

```go
// Good:
// NewTicker returns a new Ticker containing a channel that will send the
// current time on the channel after each tick.
// Call Stop to release the Ticker's associated resources when done.
func NewTicker(d Duration) *Ticker
```

**Example 5 -- Documenting error types**:

```go
// Good:
// Chdir changes the current working directory to the named directory.
// If there is an error, it will be of type *PathError.
func Chdir(dir string) error {
```

# Relationships

## Related
- **godoc-formatting** -- Formatting syntax for godoc rendering
- **signal-boosting** -- Highlighting unusual patterns in comments
- **commentary** -- General commentary guidance from the Decisions chapter

## Contrasts With
(none)

# Common Errors

- **Error**: Documenting that context cancellation stops the function (it's implied)
  **Correction**: Only document context behavior when it deviates from convention

- **Error**: Stating that a read-only method is safe for concurrent use (it's assumed)
  **Correction**: Only document concurrency when behavior is ambiguous or surprising

# Common Confusions

- **Confusion**: Thinking every parameter needs documentation
  **Clarification**: Only document error-prone, non-obvious, or surprising parameters

- **Confusion**: Not documenting cleanup because "the API is obvious"
  **Clarification**: Always document cleanup requirements -- callers may not realize resources need releasing

# Source Reference

Chapter 4: Best Practices, Section "Documentation" > "Conventions" (including Parameters, Contexts, Concurrency, Cleanup, and Errors subsections).

# Verification Notes

- Definition source: Synthesized from all subsections of Documentation > Conventions
- Confidence rationale: HIGH -- explicit guidance across five subsections
- Uncertainties: None
- Cross-reference status: References decisions#commentary, decisions#examples, decisions#package-comments
