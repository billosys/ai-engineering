---
# === CORE IDENTIFICATION ===
concept: Switch Statement
slug: switch-statement

# === CLASSIFICATION ===
category: control-flow
subcategory: conditionals
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.4 `switch` statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "switch-case"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - if-statement
extends: []
related:
  - break-statement
contrasts_with:
  - if-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I branch on multiple values of a single expression?"
---

# Quick Definition

The `switch` statement evaluates an expression and jumps to the first `case` clause whose expression matches (via strict equality), or to the `default` clause if no match is found.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, `switch` evaluates its switch expression, then uses strict equality (`===`) to compare against each case expression. Execution falls through from one case to the next unless explicitly terminated by `break` or `return`. All case clauses share a single variable scope.

# Prerequisites

- If statement (simpler conditional)
- Break statement

# Key Properties

1. Introduced in ES3.
2. Uses strict equality for comparisons (not truthiness).
3. Fall-through: execution continues to the next case unless `break` or `return` is used.
4. All cases share the same variable scope -- wrap cases in `{}` to create separate scopes.
5. Empty case clauses can group multiple values for the same behavior.

# Construction / Recognition

```js
switch (expr) {
  case value1:
    // ...
    break;
  case value2:
    // ...
    break;
  default:
    // ...
}
```

# Context & Application

Best used when branching on discrete values of a single expression. Use `default` for error checking. Prefer `if-else` chains for complex or non-equality conditions.

# Examples

From the source text (Ch. 25, section 25.4.1):

```js
function dayOfTheWeek(num) {
  switch (num) {
    case 1: return 'Monday';
    case 2: return 'Tuesday';
    case 3: return 'Wednesday';
    case 4: return 'Thursday';
    case 5: return 'Friday';
    case 6: return 'Saturday';
    case 7: return 'Sunday';
  }
}
```

# Relationships

## Builds Upon
- **If Statement** -- `switch` is an alternative branching mechanism

## Enables
- **Pattern Matching** -- common dispatch pattern

## Contrasts With
- **If Statement** -- `if` supports arbitrary conditions; `switch` tests one expression against discrete values

# Common Errors

- **Error**: Forgetting `break` or `return`, causing unintended fall-through.
  **Correction**: Always end each case with `break`, `return`, or `throw` unless fall-through is intentional.

- **Error**: Declaring the same variable name in multiple case clauses.
  **Correction**: Wrap each case in curly braces `{}` to create separate block scopes, since all cases share one variable scope.

# Common Confusions

- **Confusion**: Assuming `switch` uses loose equality.
  **Clarification**: `switch` uses strict equality (`===`) to compare the switch expression with case expressions.

# Source Reference

Chapter 25: Control flow statements, Section 25.4, lines 277-533.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition and examples in source text
- Cross-reference status: verified
