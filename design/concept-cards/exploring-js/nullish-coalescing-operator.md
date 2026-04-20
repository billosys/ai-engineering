---
# === CORE IDENTIFICATION ===
concept: Nullish Coalescing Operator
slug: nullish-coalescing-operator

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "The nullish coalescing operator (??) for default values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "??"
  - "default value operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - undefined-value
  - null-value
extends: []
related:
  - nullish-coalescing-assignment-operator
  - logical-or-operator
contrasts_with:
  - logical-or-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes `null` from `undefined`?"
---

# Quick Definition

The nullish coalescing operator (`??`) returns its right-hand operand when the left-hand operand is `undefined` or `null`, and the left-hand operand otherwise. Introduced in ES2020.

# Core Definition

The expression `value ?? defaultValue` evaluates to `defaultValue` if `value` is `undefined` or `null`, and to `value` otherwise. Unlike `||`, it does not trigger for other falsy values like `false`, `0`, or `''`. The operator is short-circuiting: the right-hand side is only evaluated if needed (Ch. 16, Section 16.4).

# Prerequisites

- **undefined-value** -- understanding what constitutes a nullish value
- **null-value** -- understanding what constitutes a nullish value

# Key Properties

1. Returns right-hand side only for `undefined` or `null` (not other falsy values) (ES2020)
2. Short-circuiting: right-hand side not evaluated if left is non-nullish
3. Distinguishes between "nullish" (`undefined`/`null`) and "falsy" (`false`, `0`, `''`, etc.)

# Construction / Recognition

```js
undefined ?? 'default' // 'default'
null ?? 'default'      // 'default'
false ?? 'default'     // false  (not nullish)
0 ?? 'default'         // 0      (not nullish)
'' ?? 'default'        // ''     (not nullish)
```

# Context & Application

Use `??` when you want to provide defaults specifically for missing values (`undefined`/`null`) without treating other falsy values as missing. This is the modern replacement for the `||` default-value pattern.

# Examples

From the source text:

```js
function countMatches(regex, str) {
  const matchResult = str.match(regex); // null or Array
  return (matchResult ?? []).length;
}
assert.equal(countMatches(/a/g, 'ababa'), 3);
assert.equal(countMatches(/x/g, 'ababa'), 0);

function getTitle(fileDesc) {
  return fileDesc.title ?? '(Untitled)';
}
```

# Relationships

## Builds Upon
- **undefined-value** — triggers the default
- **null-value** — triggers the default

## Enables
- **nullish-coalescing-assignment-operator** — `??=` combines `??` with assignment

## Related
- **logical-or-operator** — `||` is the legacy approach to defaults

## Contrasts With
- **logical-or-operator** — `||` returns default for all falsy values, not just nullish ones

# Common Errors

- **Error**: Expecting `0 ?? 'default'` to return `'default'`
  **Correction**: `0` is not nullish (only `undefined` and `null` are). Use `||` if you want to treat all falsy values as triggers.

# Common Confusions

- **Confusion**: Treating `??` and `||` as interchangeable
  **Clarification**: `??` only triggers for `undefined`/`null`; `||` triggers for any falsy value including `false`, `0`, `0n`, and `''`.

# Source Reference

Chapter 16: The non-values undefined and null, Section 16.4, lines 190-347.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comprehensive comparison to `||`
- Cross-reference status: verified
