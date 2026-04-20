---
# === CORE IDENTIFICATION ===
concept: Reduce Nesting
slug: reduce-nesting

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
section: "Reduce Nesting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "early return"
  - "guard clause pattern"
  - "reduce indentation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - unnecessary-else
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I reduce nesting in Go code?"
  - "How does reduce-nesting relate to unnecessary-else elimination?"
  - "When should I use early returns in Go?"
---

# Quick Definition

Handle error cases and special conditions first, then return early or continue the loop, keeping the happy path at the lowest indentation level.

# Core Definition

Code should reduce nesting where possible by handling error cases and special conditions first and returning early or continuing the loop. The goal is to reduce the amount of code nested multiple levels. Instead of wrapping the happy path inside conditional blocks, invert the condition, handle the exceptional case, and let the main logic flow at the top level of indentation (Uber Go Style Guide, "Reduce Nesting").

# Prerequisites

- **Go control flow** -- Understanding `if`, `return`, `continue`, and `break` statements

# Key Properties

1. Handle error/special cases first with early returns or `continue`
2. Keep the happy path at the lowest indentation level
3. Invert conditions to eliminate else branches
4. Reduces cognitive load by limiting nesting depth
5. Complements the "unnecessary else" guideline -- both aim to flatten control flow

# Construction / Recognition

## To Apply:
1. Identify deeply nested code blocks
2. Look for error checks buried inside success paths
3. Invert the condition: check for the error case first
4. Return early or `continue` on the error/special case
5. Let the main logic flow without additional indentation

## To Recognize:
1. Look for `if/else` chains where the happy path is inside the `if` and error handling is in the `else`
2. Look for multiple levels of nesting (3+ indentation levels)
3. Look for `else` blocks that only return an error -- the condition should be inverted

# Context & Application

This guideline is one of the most impactful style rules for Go readability. Deeply nested code requires readers to track multiple conditions simultaneously. By handling edge cases first and returning early, the reader can quickly dismiss error paths and focus on the main logic. This pattern is sometimes called the "guard clause" pattern. It works hand-in-hand with the "unnecessary else" guideline -- both reduce indentation and simplify control flow.

# Examples

**Example 1 -- Bad** (Style, "Reduce Nesting"):

Deeply nested with the happy path buried inside conditionals:

```go
for _, v := range data {
  if v.F1 == 1 {
    v = process(v)
    if err := v.Call(); err == nil {
      v.Send()
    } else {
      return err
    }
  } else {
    log.Printf("Invalid v: %v", v)
  }
}
```

**Example 2 -- Good** (Style, "Reduce Nesting"):

Error cases handled first, happy path at lowest indentation:

```go
for _, v := range data {
  if v.F1 != 1 {
    log.Printf("Invalid v: %v", v)
    continue
  }

  v = process(v)
  if err := v.Call(); err != nil {
    return err
  }
  v.Send()
}
```

# Relationships

## Related
- **unnecessary-else** -- A specific case of reducing nesting: when a variable is set in both branches of an if/else, eliminate the else

## Contrasts With
- Deep nesting style where error handling is pushed to else branches

# Common Errors

- **Error**: Wrapping the entire function body inside an `if err == nil` block
  **Correction**: Check `if err != nil { return err }` first, then continue with the main logic

- **Error**: Using `else` to handle the error case after a long success block
  **Correction**: Invert the condition, handle the error case first, and `return` or `continue`

# Common Confusions

- **Confusion**: Thinking early returns are bad practice (a habit from single-return-point languages)
  **Clarification**: Go idiom strongly favors early returns. Multiple return points are standard and expected in Go.

- **Confusion**: Applying reduce-nesting when it conflicts with variable scoping
  **Clarification**: The Uber guide notes that reducing variable scope should not conflict with reducing nesting. If scoping a variable to an `if` block would require nesting the success path, keep the variable in the outer scope.

# Source Reference

Chapter 4: Style, Section "Reduce Nesting".

# Verification Notes

- Definition source: Directly from the "Reduce Nesting" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides explicit guidance with a bad/good example
- Uncertainties: None
- Cross-reference status: Related to unnecessary-else as noted in the source's "Reduce Scope of Variables" section
