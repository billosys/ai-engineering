---
# === CORE IDENTIFICATION ===
concept: Logical Assignment Operators
slug: logical-assignment-operators

# === CLASSIFICATION ===
category: types-values
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Logical assignment operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "||="
  - "&&="
  - "??="

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assignment-operators
  - logical-and-operator
  - logical-or-operator
  - nullish-coalescing-operator
extends:
  - assignment-operators
related:
  - short-circuiting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Logical assignment operators (`||=`, `&&=`, `??=`) combine logical operators with assignment, but unlike other compound operators, they short-circuit and only assign if the condition is met. Introduced in ES2021.

# Core Definition

Logical assignment operators differ from other compound operators: `a ||= b` is equivalent to `a || (a = b)` (assigns if falsy), `a &&= b` is `a && (a = b)` (assigns if truthy), `a ??= b` is `a ?? (a = b)` (assigns if nullish). They short-circuit: the right-hand side is only evaluated and the assignment only performed when the condition triggers (Ch. 15, Section 15.4.2.1).

# Prerequisites

- **assignment-operators** -- these are a specialized form
- **logical-and-operator** -- `&&=` uses `&&` semantics
- **logical-or-operator** -- `||=` uses `||` semantics
- **nullish-coalescing-operator** -- `??=` uses `??` semantics

# Key Properties

1. `a ||= b`: assigns if `a` is falsy (ES2021)
2. `a &&= b`: assigns if `a` is truthy (ES2021)
3. `a ??= b`: assigns if `a` is nullish (ES2021)
4. Short-circuiting: right side not evaluated if condition not met
5. NOT equivalent to `a = a op b` (which always assigns)

# Construction / Recognition

```js
// ||= assigns when falsy
let a = '';
a ||= 'default'; // a is now 'default'

// &&= assigns when truthy
let b = 'exists';
b &&= 'updated'; // b is now 'updated'

// ??= assigns when nullish
let c = 0;
c ??= 'default'; // c stays 0 (not nullish)
```

# Context & Application

Logical assignment operators provide concise patterns for default values, conditional updates, and property initialization.

# Examples

From the source text:

| Operator | Equivalent to | Only assigns if `a` is |
|----------|--------------|----------------------|
| `a \|\|= b` | `a \|\| (a = b)` | Falsy |
| `a &&= b` | `a && (a = b)` | Truthy |
| `a ??= b` | `a ?? (a = b)` | Nullish |

# Relationships

## Builds Upon
- **assignment-operators** — extends compound assignment concept
- **logical-and-operator** — `&&=` semantics
- **logical-or-operator** — `||=` semantics
- **nullish-coalescing-operator** — `??=` semantics

## Enables
- Concise conditional assignment patterns

## Related
- **short-circuiting** — all three operators short-circuit

## Contrasts With
- None

# Common Errors

- **Error**: Thinking `a ||= b` is the same as `a = a || b`
  **Correction**: The latter always performs an assignment; the former only assigns if `a` is falsy.

# Common Confusions

- **Confusion**: Not knowing when to use `||=` vs `??=`
  **Clarification**: Use `??=` when only `undefined`/`null` should trigger the default. Use `||=` when all falsy values should trigger.

# Source Reference

Chapter 15: Operators, Section 15.4.2.1, lines 289-382.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit equivalence table in source
- Cross-reference status: verified against Ch. 16 (??=)
