---
# === CORE IDENTIFICATION ===
concept: Constant Names
slug: constant-names

# === CLASSIFICATION ===
category: naming
subcategory: constants
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Constant names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "constant naming conventions"
  - "Go constant style"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mixed-caps
extends: []
related:
  - variable-names
  - initialisms
contrasts_with:
  - prefix-unexported-globals-with-underscore

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should constants be named in Go?"
  - "Should Go constants use ALL_CAPS?"
  - "Should constant names reflect their value or their role?"
---

# Quick Definition

Constant names must use MixedCaps like all other names in Go; never ALL_CAPS or kPrefix. Name constants by their role, not their value.

# Core Definition

In Go, constant names follow the same MixedCaps convention as all other identifiers. Exported constants start with uppercase, unexported constants start with lowercase. This applies even when it breaks conventions from other languages like C or Java. Constant names should explain what the value denotes (its role), not be a derivative of the value itself. If a constant has no role apart from its value, defining it as a constant is unnecessary (Google Go Style Guide, "Style Decisions", "Constant names").

# Prerequisites

- **mixed-caps** -- Understanding Go's MixedCaps naming convention is essential since constants follow the same rule
- **Go exported vs unexported identifiers** -- Uppercase initial letter means exported; lowercase means unexported

# Key Properties

1. Constants use MixedCaps, never ALL_CAPS with underscores
2. No `K` or `k` prefix (unlike some C++ conventions)
3. Exported constants start with uppercase; unexported with lowercase
4. Name should describe the role, not the value
5. A constant with no role beyond its value is unnecessary

# Construction / Recognition

## To Apply:
1. Use MixedCaps for all constant names
2. Choose a name that describes what the constant represents, not what it equals
3. Do not use ALL_CAPS or kPrefix conventions from other languages
4. If you cannot name the constant by its role, question whether the constant is needed

## To Recognize:
1. Look for ALL_CAPS constant names -- these violate Go style
2. Look for `k` or `K` prefixed constants -- these violate Go style
3. Look for constants whose names merely restate their value (e.g., `Twelve = 12`)

# Context & Application

This convention reflects Go's philosophy of uniform naming. Unlike C/C++ or Java where ALL_CAPS signals immutability, Go relies on the type system and language semantics. Using MixedCaps keeps constants visually consistent with other identifiers and avoids the need for a separate mental model for naming.

# Examples

**Example 1 -- Good: role-based MixedCaps constant names** (Decisions, "Constant names"):

```go
// Good:
const MaxPacketSize = 512

const (
    ExecuteBit = 1 << iota
    WriteBit
    ReadBit
)
```

**Example 2 -- Bad: ALL_CAPS and kPrefix** (Decisions, "Constant names"):

```go
// Bad:
const MAX_PACKET_SIZE = 512
const kMaxBufferSize = 1024
const KMaxUsersPergroup = 500
```

**Example 3 -- Bad: name derived from value, not role** (Decisions, "Constant names"):

```go
// Bad:
const Twelve = 12

const (
    UserNameColumn = "username"
    GroupColumn    = "group"
)
```

# Relationships

## Related
- **variable-names** -- Similar principles about naming by role rather than type
- **initialisms** -- Affects how initialisms appear within constant names
- **mixed-caps** -- The foundational naming convention that constants follow

## Contrasts With
- **prefix-unexported-globals-with-underscore** (Uber style) -- Uber uses underscore prefix for unexported globals, which Google style does not adopt for constants

# Common Errors

- **Error**: Using ALL_CAPS for constants out of habit from C/Java
  **Correction**: Use MixedCaps; Go does not distinguish constants visually from other identifiers

- **Error**: Adding a `k` prefix to constant names
  **Correction**: Drop the prefix; use standard MixedCaps naming

# Common Confusions

- **Confusion**: Thinking constants need special naming to distinguish them from variables
  **Clarification**: Go intentionally does not visually distinguish constants. The `const` keyword in the declaration is sufficient.

- **Confusion**: Believing column name or config key constants should mirror the string value
  **Clarification**: Name the constant by its role in your program, not by the literal value it holds

# Source Reference

Chapter 3: Style Decisions, Section "Constant names".

# Verification Notes

- Definition source: Directly from the "Constant names" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with good/bad examples provided
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
