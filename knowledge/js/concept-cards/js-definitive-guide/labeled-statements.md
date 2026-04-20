---
# === CORE IDENTIFICATION ===
concept: Labeled Statements
slug: labeled-statements

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 130
section: "5.5.1 Labeled Statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "statement labels"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compound-and-empty-statements
extends: []
related:
  - break-continue-statements
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Any statement can be labeled by preceding it with an identifier and a colon. Labels are used with `break` and `continue` to target specific enclosing loops or statements.

# Core Definition

"Any statement may be *labeled* by preceding it with an identifier and a colon: `identifier: statement`. By labeling a statement, you give it a name that you can use to refer to it elsewhere in your program." Labels are useful only with `break` and `continue`. (Ch. 5, §5.5.1)

# Prerequisites

- **compound-and-empty-statements** — Labels are applied to statements, typically loops or blocks.

# Key Properties

1. Syntax: `identifier: statement`.
2. The label namespace is separate from variable and function namespaces.
3. Labels are scoped to the statement they label (and its substatements).
4. Two statements may share a label if neither is nested within the other.
5. Labels are useful primarily on loops and block statements.

# Construction / Recognition

```js
mainloop: while(token !== null) {
    // ...
    continue mainloop;
}
```

# Context & Application

Labeled statements are used in nested loops when `break` or `continue` needs to target an outer loop rather than the innermost one.

# Examples

From the source text (§5.5.1, p. 130):

```js
mainloop: while(token !== null) {
    // Code omitted...
    continue mainloop;  // Jump to the next iteration of the named loop
    // More code omitted...
}
```

# Relationships

## Builds Upon
- **compound-and-empty-statements** — Labels apply to any statement

## Enables
- **break-continue-statements** — Labels are used exclusively with `break` and `continue`

## Related
- **for-loop** — Loops are the primary statements that benefit from labels

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Attempting to use a label to jump to an arbitrary location in code (like `goto`).
  **Correction**: Labels in JavaScript can only be used with `break` and `continue`, not as general jump targets.

# Common Confusions

- **Confusion**: Confusing label syntax with object literal property syntax.
  **Clarification**: `identifier: statement` at the statement level is a label; `identifier: value` inside `{}` is a property. Context determines interpretation.

# Source Reference

Chapter 5: Statements, Section 5.5.1, page 130.

# Verification Notes

- Definition source: Direct quote from §5.5.1
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
