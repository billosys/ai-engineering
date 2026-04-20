---
# === CORE IDENTIFICATION ===
concept: Function Grouping and Ordering
slug: function-grouping-and-ordering

# === CLASSIFICATION ===
category: style
subcategory: code-organization
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Function Grouping and Ordering"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "function ordering"
  - "method grouping by receiver"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - reduce-nesting
  - function-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "In what order should I arrange functions in a Go file?"
  - "Where should exported functions appear relative to unexported ones?"
  - "How should methods be grouped in a Go file?"
---

# Quick Definition

Sort functions in rough call order, group by receiver, and place exported functions first -- after type, const, and var definitions.

# Core Definition

Functions in a Go file should be sorted in rough call order and grouped by receiver. Exported functions should appear first in the file, after `struct`, `const`, and `var` definitions. A `newXYZ()`/`NewXYZ()` constructor may appear immediately after the type is defined, but before the rest of the methods on the receiver. Plain utility functions (not attached to a receiver) should appear towards the end of the file (Uber Go Style Guide, "Function Grouping and Ordering").

# Prerequisites

- **Go exported/unexported identifiers** -- Understanding visibility via capitalization to know which functions are "exported"
- **Go methods and receivers** -- Understanding receiver functions to apply grouping by receiver

# Key Properties

1. Functions are sorted in rough call order (callers before callees where practical)
2. Functions are grouped by receiver type
3. Exported functions appear first in the file
4. Type definitions, `const`, and `var` blocks precede functions
5. Constructors (`newXYZ`/`NewXYZ`) appear right after the type definition
6. Plain utility functions (no receiver) go towards the end of the file

# Construction / Recognition

## To Apply:
1. Place `struct`, `const`, and `var` definitions at the top of the file
2. Define the type, then immediately its constructor (`NewXYZ` or `newXYZ`)
3. Group all methods by their receiver type
4. Within each group, place exported methods before unexported methods
5. Arrange functions in rough call order
6. Place standalone utility functions at the end of the file

## To Recognize:
1. Look for type definitions appearing after methods -- this violates the guideline
2. Look for utility functions interspersed among methods -- they should be at the end
3. Look for constructors separated from their type definition -- they should be adjacent

# Context & Application

This guideline makes Go files scannable by establishing a predictable layout. A reader can find the type definition at the top, its constructor immediately after, exported methods next, and utility functions at the bottom. This top-down reading experience mirrors how most developers approach unfamiliar code.

# Examples

**Example 1 -- Bad** (Style, "Function Grouping and Ordering"):

```go
func (s *something) Cost() {
  return calcCost(s.weights)
}

type something struct{ ... }

func calcCost(n []int) int {...}

func (s *something) Stop() {...}

func newSomething() *something {
    return &something{}
}
```

**Example 2 -- Good** (Style, "Function Grouping and Ordering"):

```go
type something struct{ ... }

func newSomething() *something {
    return &something{}
}

func (s *something) Cost() {
  return calcCost(s.weights)
}

func (s *something) Stop() {...}

func calcCost(n []int) int {...}
```

# Relationships

## Related
- **reduce-nesting** -- Complements function ordering by improving readability within each function
- **function-names** -- Naming conventions pair with ordering conventions

# Common Errors

- **Error**: Placing the constructor function far from its type definition
  **Correction**: Place `NewXYZ()` or `newXYZ()` immediately after the type definition

- **Error**: Scattering methods of the same receiver across the file with unrelated functions in between
  **Correction**: Group all methods for a given receiver type together

- **Error**: Placing unexported utility functions before exported methods
  **Correction**: Exported functions first; utility functions at the end

# Common Confusions

- **Confusion**: Thinking "call order" means strict topological sorting
  **Clarification**: The guideline says "rough call order" -- it is a heuristic for readability, not a strict rule. Group by receiver takes priority.

- **Confusion**: Wondering where package-level `init()` functions should go
  **Clarification**: The guideline does not address `init()` explicitly, but convention places it near the top after package-level declarations

# Source Reference

Chapter 4: Style, Section "Function Grouping and Ordering".

# Verification Notes

- Definition source: Directly from the "Function Grouping and Ordering" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides explicit ordering rules with a bad/good example
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
