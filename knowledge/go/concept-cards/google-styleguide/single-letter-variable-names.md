---
# === CORE IDENTIFICATION ===
concept: Single-Letter Variable Names
slug: single-letter-variable-names

# === CLASSIFICATION ===
category: naming
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Single-letter variable names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "short variable names"
  - "single-char identifiers"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-names
extends: []
related:
  - receiver-names
  - repetition-in-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is it OK to use single-letter variable names in Go?"
  - "What are the conventional single-letter names for common types in Go?"
  - "Should loop variables use single letters?"
---

# Quick Definition

Single-letter variable names are appropriate for method receivers, loop variables, and familiar type conventions (e.g., `r` for `io.Reader`, `w` for `io.Writer`). Use them only when the full word would be repetitive and the meaning is obvious.

# Core Definition

Single-letter variable names minimize repetition but can make code opaque if overused. Their use should be limited to cases where the full word is obvious and would be repetitive. Method receivers prefer one or two-letter names. Familiar conventions exist for common types: `r` for `io.Reader` or `*http.Request`, `w` for `io.Writer` or `http.ResponseWriter`. Single-letter identifiers are acceptable as integer loop variables (`i` for indices, `x` and `y` for coordinates). Short abbreviations are acceptable as loop identifiers when scope is short, such as `n` in `for _, n := range nodes` (Google Go Style Guide, "Style Decisions", "Single-letter variable names").

# Prerequisites

- **variable-names** -- Understanding the scope-proportional naming principle that governs when single letters are appropriate

# Key Properties

1. Preferred for method receivers: one or two letters abbreviating the type
2. Conventional for common types: `r` for Reader, `w` for Writer
3. Acceptable for loop indices: `i`, `j`, `k`
4. Acceptable for coordinates: `x`, `y`
5. Short abbreviations OK in short-scoped loops: `n` for node
6. Avoid when the meaning is not immediately obvious

# Construction / Recognition

## To Apply:
1. For method receivers, use one or two letters abbreviating the type name
2. For loop indices, use `i`, `j`, `k`
3. For well-known interfaces, use the conventional letter (`r`, `w`)
4. For range variables in short loops, use a short abbreviation
5. If the single letter would be ambiguous, use a longer name

## To Recognize:
1. Look for single-letter variables in large scopes -- they may need longer names
2. Look for non-conventional single letters -- they may confuse readers
3. Look for verbose names in tiny scopes -- a single letter may be clearer

# Context & Application

Go's culture favors brevity where meaning is clear. The convention of `r` for Reader and `w` for Writer is so pervasive that using longer names like `reader` or `writer` would actually feel unusual and noisy to experienced Go developers. This convention works because these types are used frequently and the association is well-established across the ecosystem.

# Examples

**Example 1 -- Good: conventional single-letter names** (Decisions, "Single-letter variable names"):

```go
// Method receiver
func (s *Scanner) Scan() bool { ... }

// Common type conventions
func Copy(w io.Writer, r io.Reader) (int64, error) { ... }

// Loop indices
for i := 0; i < len(items); i++ { ... }
```

**Example 2 -- Good: short abbreviation in range loop** (Decisions, "Single-letter variable names"):

```go
for _, n := range nodes {
    process(n)
}
```

**Example 3 -- Bad: single letter in large scope where meaning is unclear**:

```go
// Bad: 'c' is ambiguous in a large function with many variables
func processData(data []byte) {
    c := initConfig()
    // ... 30 more lines ...
    c.Apply() // what is c again?
}
```

# Relationships

## Related
- **receiver-names** -- Receivers are the primary use case for one/two-letter names
- **variable-names** -- Single-letter names are the short end of the scope-proportional naming spectrum
- **repetition-in-naming** -- Single-letter names help reduce repetition in tight scopes

# Common Errors

- **Error**: Using single-letter names in large scopes where the meaning is not obvious
  **Correction**: Use a descriptive name proportional to the scope size

- **Error**: Using non-standard single letters for well-known types (e.g., `x` for an `io.Reader`)
  **Correction**: Use the conventional letter: `r` for Reader, `w` for Writer

# Common Confusions

- **Confusion**: Thinking single-letter variable names are always bad style
  **Clarification**: In Go, they are idiomatic and preferred in the right contexts (receivers, loops, familiar types)

- **Confusion**: Using `self` or `this` for method receivers
  **Clarification**: Go convention is a short abbreviation of the type, not `self` or `this`

# Source Reference

Chapter 3: Style Decisions, Section "Single-letter variable names".

# Verification Notes

- Definition source: Directly from the "Single-letter variable names" subsection of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit conventions listed with specific examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
