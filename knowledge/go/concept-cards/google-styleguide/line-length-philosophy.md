---
# === CORE IDENTIFICATION ===
concept: Line Length Philosophy
slug: line-length-philosophy

# === CLASSIFICATION ===
category: language
subcategory: formatting
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
  - "Go line length"
  - "no fixed line length"
  - "line wrapping in Go"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - gofmt-formatting
  - clarity-principle
  - simplicity-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is there a maximum line length in Go?"
  - "When should I split a long line in Go?"
  - "Should I break long URLs across multiple lines?"
---

# Quick Definition

There is no fixed line length for Go source code. If a line feels too long, prefer refactoring over splitting. Do not split lines before indentation changes (e.g., function declarations, conditionals) or to break long strings like URLs across multiple shorter lines.

# Core Definition

Go has no fixed line length limit. When a line feels too long, the preferred response is to refactor the code (e.g., extract a variable or function) rather than mechanically splitting the line. If the line is already as short as it can practically be, it should be allowed to remain long. Two specific prohibitions: do not split a line before an indentation change (such as a function declaration or conditional), and do not split a long string (such as a URL) across multiple shorter lines.

# Prerequisites

- **gofmt-formatting** -- Understanding that gofmt handles mechanical formatting but not line length

# Key Properties

1. No fixed line length for Go source code
2. Prefer refactoring over line splitting when a line feels too long
3. Allow lines to remain long if they are already as short as practical
4. Do not split before an indentation change (function declaration, conditional)
5. Do not split long strings (URLs) into multiple shorter lines

# Construction / Recognition

## To Apply:
1. If a line feels too long, first try to refactor: extract variables, extract functions, simplify expressions
2. If the line cannot be shortened through refactoring, leave it long
3. Never break a line just before a function declaration or conditional block
4. Never wrap a URL or long string literal across lines

## To Recognize:
1. Lines artificially broken mid-expression without refactoring the underlying complexity
2. URLs or long string literals split across multiple lines
3. Function signatures split onto multiple lines when the signature itself could be simplified

# Context & Application

This philosophy reflects Go's preference for simplicity and refactoring over mechanical rules. A fixed line length limit encourages developers to wrap lines without addressing the root cause of length -- overly complex expressions, too many parameters, or deeply nested logic. Go's approach pushes developers toward actual simplification. Long lines that remain long after refactoring attempts are acceptable because forcing a split would harm readability more than the length does.

# Examples

**Example 1 -- Refactor instead of splitting**:

Instead of wrapping a long function call across multiple lines, consider whether the arguments can be simplified by extracting variables or whether the function itself is doing too much.

**Example 2 -- Do not split URLs**:

```go
// Good:
// See https://google.github.io/styleguide/go/decisions#indentation-confusion

// Bad:
// See https://google.github.io/styleguide/go/
//     decisions#indentation-confusion
```

# Relationships

## Related
- **gofmt-formatting** -- Gofmt handles formatting but does not enforce line length
- **clarity-principle** -- Refactoring for shorter lines improves clarity
- **simplicity-principle** -- The preference for refactoring aligns with simplicity

# Common Errors

- **Error**: Setting a linter to enforce an 80- or 100-character line limit
  **Correction**: Go has no fixed line length. Use judgment, not a mechanical limit.

- **Error**: Splitting a function declaration across lines when it could be simplified
  **Correction**: Refactor (shorter parameter names, fewer parameters, extract types) before resorting to line splitting

# Common Confusions

- **Confusion**: Thinking Go allows infinitely long lines without concern
  **Clarification**: Lines should be as short as practical. The point is to prefer refactoring over splitting, not to ignore length entirely.

- **Confusion**: Applying line length rules from other languages (80 chars, 120 chars) to Go
  **Clarification**: Go explicitly has no fixed line length. The style guide considers line length restrictions an invalid local style consideration.

# Source Reference

Chapter 2: Guide, Section "Core guidelines" > "Line length".

# Verification Notes

- Definition source: Directly from the "Line length" section of Core guidelines
- Confidence rationale: HIGH -- explicit statement with specific rules
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
