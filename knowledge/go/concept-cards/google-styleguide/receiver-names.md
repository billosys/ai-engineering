---
# === CORE IDENTIFICATION ===
concept: Receiver Names
slug: receiver-names

# === CLASSIFICATION ===
category: naming
subcategory: methods
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Decisions"
chapter_number: 3
pdf_page: null
section: "Naming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "method receiver naming"
  - "receiver variable names"
  - "Go receiver conventions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - naming-principles
extends: []
related:
  - mixedcaps-naming
  - google-package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should method receivers be named in Go?"
  - "Should I use 'self' or 'this' for receiver names in Go?"
  - "Must receiver names be consistent across all methods of a type?"
  - "Can I use an underscore for an unused receiver?"
---

# Quick Definition

Receiver variable names must be short (one or two letters), an abbreviation of the type itself, and applied consistently to every receiver for that type. Never use `this` or `self`. Do not use an underscore for unused receivers; omit the name instead.

# Core Definition

Method receiver variable names must follow four rules: (1) short, usually one or two letters in length; (2) abbreviations for the type itself; (3) applied consistently to every receiver for that type; (4) not an underscore -- if the receiver is unused, omit the name entirely. Names like `this` or `self` from other languages are explicitly rejected in favor of short abbreviations (e.g., `t` for `Tray`, `ri` for `ResearchInfo`, `w` for `ReportWriter`, `s` for `Scanner`).

# Prerequisites

- **naming-principles** -- General naming philosophy (short names, context-awareness)

# Key Properties

1. Short: usually one or two letters
2. Abbreviation of the type name
3. Consistent across all methods of the same type
4. Never use an underscore for unused receivers; omit the name instead
5. Never use `this` or `self`

# Construction / Recognition

## To Apply:
1. Take the first letter(s) of the type name as the receiver name
2. For single-word types, use the first letter: `Tray` -> `t`, `Scanner` -> `s`
3. For multi-word types, use initials: `ResearchInfo` -> `ri`, `ReportWriter` -> `w` or `rw`
4. Use the same name in every method on that type
5. If the receiver is unused, omit the name: `func (Tray) Method()` not `func (_ Tray) Method()`

## To Recognize:
1. Receivers named `this` or `self` -- violation
2. Long receiver names like `tray` or `scanner` -- should be shortened
3. Inconsistent receiver names across methods of the same type -- violation
4. Underscore receiver names (`_`) -- should omit the name entirely

# Context & Application

Go's convention of short receiver names reflects the language's preference for brevity in small scopes. Since method bodies are typically short and the receiver is used frequently within them, a one- or two-letter name provides sufficient clarity without noise. The prohibition on `this` and `self` reinforces that Go methods are not fundamentally different from functions -- the receiver is just another parameter. Consistency across all methods of a type is important so that readers can quickly identify the receiver when reading any method.

# Examples

**Example 1 -- Correct receiver names (from source)**:

| Long Name                   | Better Name               |
|-----------------------------|---------------------------|
| `func (tray Tray)`          | `func (t Tray)`           |
| `func (info *ResearchInfo)` | `func (ri *ResearchInfo)` |
| `func (this *ReportWriter)` | `func (w *ReportWriter)`  |
| `func (self *Scanner)`      | `func (s *Scanner)`       |

**Example 2 -- Unused receiver**:

```go
// Good: omit the name when unused
func (Tray) String() string { return "tray" }

// Bad: do not use underscore
func (_ Tray) String() string { return "tray" }
```

# Relationships

## Related
- **mixedcaps-naming** -- Receiver names follow MixedCaps but are so short they are usually just lowercase letters
- **google-package-names** -- Another naming convention with specific rules

# Common Errors

- **Error**: Using `this` or `self` as receiver names
  **Correction**: Use a one- or two-letter abbreviation of the type name

- **Error**: Using different receiver names across methods of the same type
  **Correction**: Pick one name and use it consistently in all methods

- **Error**: Using `_` for an unused receiver
  **Correction**: Omit the receiver name entirely: `func (MyType) Method()`

# Common Confusions

- **Confusion**: Thinking longer receiver names are more readable
  **Clarification**: Receivers appear frequently in short method bodies. Short names reduce noise without sacrificing clarity.

- **Confusion**: Applying Java/Python conventions (`this`/`self`) to Go
  **Clarification**: Go receivers are just parameters. Use a short type abbreviation, not `this` or `self`.

# Source Reference

Chapter 3: Decisions, Section "Naming" > "Receiver names".

# Verification Notes

- Definition source: Directly from the "Receiver names" section of Style Decisions with table of examples
- Confidence rationale: HIGH -- explicit rules with a concrete correction table
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
