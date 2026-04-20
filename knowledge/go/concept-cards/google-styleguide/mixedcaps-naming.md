---
# === CORE IDENTIFICATION ===
concept: MixedCaps Naming
slug: mixedcaps-naming

# === CLASSIFICATION ===
category: naming
subcategory: capitalization
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Core guidelines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "MixedCaps"
  - "camelCase in Go"
  - "Go naming capitalization"
  - "no underscores in names"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - underscores-in-go-names
  - naming-principles
  - gofmt-formatting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should Go names use underscores or camelCase?"
  - "How do I name constants in Go?"
  - "How does Go handle multi-word names?"
---

# Quick Definition

Go source code uses `MixedCaps` or `mixedCaps` (camel case) for all multi-word names, never underscores (snake case). This applies even when it breaks conventions from other languages, such as `MaxLength` instead of `MAX_LENGTH` for constants.

# Core Definition

Go uses `MixedCaps` (exported) or `mixedCaps` (unexported) -- also known as camel case -- rather than underscores (snake case) when writing multi-word names. This is a core guideline and applies to all identifiers: variables, functions, methods, types, constants, and packages. This applies even when it breaks conventions in other languages. For example, a constant is `MaxLength` (not `MAX_LENGTH`) if exported and `maxLength` (not `max_length`) if unexported. Local variables are considered unexported for the purpose of choosing initial capitalization.

# Prerequisites

- **Go export rules** -- Understanding that uppercase initial letter means exported, lowercase means unexported

# Key Properties

1. Use `MixedCaps` for exported names (uppercase first letter)
2. Use `mixedCaps` for unexported names (lowercase first letter)
3. Never use underscores in multi-word Go names
4. Applies to all identifiers: variables, functions, types, constants, methods
5. Overrides conventions from other languages (e.g., `MAX_LENGTH` becomes `MaxLength`)
6. Local variables are treated as unexported (lowercase first letter)

# Construction / Recognition

## To Apply:
1. For exported identifiers, capitalize the first letter of each word: `MaxLength`, `UserName`
2. For unexported identifiers, lowercase the first word, capitalize subsequent words: `maxLength`, `userName`
3. Never use underscores between words
4. For constants, use MixedCaps (not ALL_CAPS): `MaxPacketSize` not `MAX_PACKET_SIZE`

## To Recognize:
1. Names with underscores (e.g., `max_length`, `MAX_LENGTH`) violate this guideline
2. Constants in ALL_CAPS style indicate code from another language's convention

# Context & Application

This is one of the "core guidelines" that all Go code is expected to follow. It reflects Go's design philosophy of having a single, uniform naming convention rather than multiple conventions for different identifier types. The fact that constants use MixedCaps (not ALL_CAPS) is a common stumbling point for developers coming from C, Java, or Python.

# Examples

**Example 1 -- Exported vs unexported (from source)**:

```go
// Good:
const MaxLength = 512   // exported constant
const maxLength = 512   // unexported constant

// Bad:
const MAX_LENGTH = 512  // wrong: snake case
const max_length = 512  // wrong: snake case
```

**Example 2 -- Local variables**:

```go
// Good:
userName := "alice"     // local variable, treated as unexported
userCount := 42

// Bad:
user_name := "alice"    // wrong: underscores
user_count := 42        // wrong: underscores
```

# Relationships

## Related
- **underscores-in-go-names** -- Details the three narrow exceptions where underscores are permitted
- **naming-principles** -- MixedCaps is the mechanical foundation for Go naming
- **gofmt-formatting** -- Another core guideline alongside MixedCaps

# Common Errors

- **Error**: Using ALL_CAPS for constants (e.g., `MAX_BUFFER_SIZE`)
  **Correction**: Use `MaxBufferSize` (exported) or `maxBufferSize` (unexported)

- **Error**: Using snake_case for variable names coming from Python or Ruby
  **Correction**: Use `mixedCaps` for all local variables

# Common Confusions

- **Confusion**: Thinking Go constants should use ALL_CAPS like C or Java
  **Clarification**: Go uses MixedCaps for everything, including constants. `MaxLength` not `MAX_LENGTH`.

- **Confusion**: Believing underscores are acceptable in test helper names
  **Clarification**: Only test *function* names (Test_Foo, TestFoo_Bar) may use underscores. Regular identifiers within test code still use MixedCaps.

# Source Reference

Chapter 2: Guide, Section "Core guidelines" > "MixedCaps".

# Verification Notes

- Definition source: Directly from the "MixedCaps" section of Core guidelines
- Confidence rationale: HIGH -- explicit rule with clear examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
