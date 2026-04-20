---
# === CORE IDENTIFICATION ===
concept: Unnecessary Else
slug: unnecessary-else

# === CLASSIFICATION ===
category: style
subcategory: control-flow
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Unnecessary Else"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "eliminate else"
  - "default value pattern"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends:
  - reduce-nesting
related:
  - reduce-nesting
  - top-level-variable-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When can I eliminate an else branch in Go?"
  - "How does reduce-nesting relate to unnecessary-else elimination?"
  - "How do I simplify if/else blocks that set a variable?"
---

# Quick Definition

When a variable is set in both branches of an if/else, eliminate the else by setting the default value first, then overriding it conditionally.

# Core Definition

If a variable is set in both branches of an `if`/`else`, the `else` can be eliminated by initializing the variable to the value from the `else` branch (the default), then using a single `if` to conditionally override it. This reduces nesting and makes the default value immediately visible (Uber Go Style Guide, "Unnecessary Else").

# Prerequisites

- **Go variable declarations** -- Understanding `:=` short variable declarations and `var` declarations
- **reduce-nesting** -- Unnecessary else elimination is a specific application of the reduce-nesting principle

# Key Properties

1. Applies when a variable is assigned in both the `if` and `else` branches
2. The `else` value becomes the default initialization
3. The `if` block becomes the conditional override
4. Reduces one level of indentation
5. Makes the default value immediately visible at the declaration

# Construction / Recognition

## To Apply:
1. Identify an if/else where the same variable is set in both branches
2. Initialize the variable with the value from the `else` branch (the default)
3. Use a single `if` to set the override value
4. Remove the `else` block entirely

## To Recognize:
1. Look for `var x T; if cond { x = A } else { x = B }` -- the else is unnecessary
2. Look for if/else blocks where both branches only assign to the same variable

# Context & Application

This guideline is a specific case of the broader "reduce nesting" principle. It targets a common pattern where developers write symmetric if/else blocks to set a variable's value. The refactored form -- default value plus conditional override -- is both shorter and clearer, as it makes the default case immediately obvious. This pattern appears frequently in configuration, option handling, and conditional initialization code.

# Examples

**Example 1 -- Bad** (Style, "Unnecessary Else"):

Variable set in both branches:

```go
var a int
if b {
  a = 100
} else {
  a = 10
}
```

**Example 2 -- Good** (Style, "Unnecessary Else"):

Default value set first, conditionally overridden:

```go
a := 10
if b {
  a = 100
}
```

# Relationships

## Extends
- **reduce-nesting** -- Unnecessary else elimination is a specific technique for reducing nesting

## Related
- **reduce-nesting** -- Both guidelines aim to flatten control flow and reduce indentation
- **top-level-variable-declarations** -- Both address how variables should be declared and initialized

# Common Errors

- **Error**: Writing symmetric if/else blocks to set a variable's value
  **Correction**: Set the default value first, then conditionally override it

- **Error**: Using `var x T` followed by an if/else to set the value, when a short declaration would suffice
  **Correction**: Use `x := defaultValue` then `if cond { x = overrideValue }`

# Common Confusions

- **Confusion**: Thinking this only applies when both branches are single assignments
  **Clarification**: The principle applies whenever both branches primarily serve to set the same variable, even if there is other logic involved. However, if the branches have significantly different side effects, the if/else may be appropriate.

- **Confusion**: Applying this when the "default" value requires computation
  **Clarification**: If the default value is expensive to compute and the condition often takes the other branch, the if/else form may be more efficient. Apply judgment.

# Source Reference

Chapter 4: Style, Section "Unnecessary Else".

# Verification Notes

- Definition source: Directly from the "Unnecessary Else" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides an explicit bad/good example with a clear rule
- Uncertainties: None
- Cross-reference status: Related to reduce-nesting as both address control flow simplification
