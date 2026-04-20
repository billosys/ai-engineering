---
# === CORE IDENTIFICATION ===
concept: Top-level Variable Declarations
slug: top-level-variable-declarations

# === CLASSIFICATION ===
category: style
subcategory: declarations
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Top-level Variable Declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package-level var declarations"
  - "top-level var keyword"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - prefix-unexported-globals-with-underscore
  - unnecessary-else
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes := from var for variable declarations?"
  - "When should I specify the type in a top-level var declaration?"
  - "Should I use := or var at the package level?"
---

# Quick Definition

Use the `var` keyword for top-level (package-level) variable declarations. Omit the type when it is obvious from the right-hand side expression.

# Core Definition

At the top level (package scope), use the standard `var` keyword to declare variables. Do not specify the type unless it differs from the type of the expression on the right-hand side. When the return type of the initializing function already makes the type clear, omitting the explicit type annotation reduces noise. However, specify the type explicitly when the desired type differs from the expression's type, such as when you want an interface type but the function returns a concrete type (Uber Go Style Guide, "Top-level Variable Declarations").

# Prerequisites

- **Go variable declaration syntax** -- Understanding `var`, `:=`, and type inference
- **Go type system** -- Understanding when a concrete type satisfies an interface type

# Key Properties

1. Use `var` (not `:=`) at the package level -- `:=` is not allowed at package scope anyway
2. Omit the type when it matches the expression's type: `var _s = F()` instead of `var _s string = F()`
3. Specify the type when you want a different type than the expression returns: `var _e error = F()` when `F()` returns `myError`
4. Type omission reduces redundancy when the right-hand side makes the type obvious

# Construction / Recognition

## To Apply:
1. Always use `var` for package-level declarations (not `:=`)
2. If the right-hand side's type is obvious (e.g., a function with a clear return type), omit the explicit type
3. If you need a different type (e.g., an interface instead of a concrete type), specify it explicitly

## To Recognize:
1. Look for `var _s string = F()` where `F()` already returns `string` -- the type is redundant
2. Look for `:=` at the package level -- this is a compile error in Go, but indicates unfamiliarity with the convention

# Context & Application

This guideline addresses a common source of noise in Go code. When a function's return type is clear from its signature, repeating the type in the variable declaration adds no information. However, when the desired variable type differs from the expression type -- commonly when storing a concrete type in an interface variable -- the explicit type annotation is essential both for correctness and documentation. This convention pairs with the underscore prefix convention for unexported globals.

# Examples

**Example 1 -- Bad: redundant type** (Style, "Top-level Variable Declarations"):

```go
var _s string = F()

func F() string { return "A" }
```

**Example 2 -- Good: type omitted** (Style, "Top-level Variable Declarations"):

```go
var _s = F()
// Since F already states that it returns a string, we don't need to specify
// the type again.

func F() string { return "A" }
```

**Example 3 -- Good: type specified when different** (Style, "Top-level Variable Declarations"):

```go
type myError struct{}

func (myError) Error() string { return "error" }

func F() myError { return myError{} }

var _e error = F()
// F returns an object of type myError but we want error.
```

# Relationships

## Related
- **prefix-unexported-globals-with-underscore** -- Unexported top-level variables should use the `_` prefix, as shown in the examples
- **unnecessary-else** -- Both guidelines address how variables should be initialized cleanly

# Common Errors

- **Error**: Specifying the type when it matches the expression: `var _count int = getCount()`
  **Correction**: Omit the redundant type: `var _count = getCount()`

- **Error**: Omitting the type when you want an interface type but the expression returns a concrete type
  **Correction**: Specify the type explicitly: `var _w io.Writer = newFileWriter()`

# Common Confusions

- **Confusion**: Thinking `:=` can be used at the package level
  **Clarification**: The `:=` short variable declaration is only available inside functions. At the package level, you must use `var`.

- **Confusion**: Always specifying the type for "clarity"
  **Clarification**: When the type is obvious from the right-hand side (e.g., `F()` returns `string`), the explicit type is noise, not clarity. Omit it.

# Source Reference

Chapter 4: Style, Section "Top-level Variable Declarations".

# Verification Notes

- Definition source: Directly from the "Top-level Variable Declarations" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides explicit rules with bad/good examples and a special case
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
