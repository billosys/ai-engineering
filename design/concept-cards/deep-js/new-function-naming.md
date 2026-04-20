---
# === CORE IDENTIFICATION ===
concept: "new Function() Naming"
slug: new-function-naming

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.10 Other programming constructs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - function-naming-rules
  - bound-function-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Functions created via `new Function()` have a `.name` of `'anonymous'`, a historical requirement for web compatibility.

# Core Definition

From "Deep JavaScript" (Ch 21.2.10): "`new Function()` produces functions whose `.name` is `'anonymous'`." A WebKit bug describes why this is necessary for web compatibility.

# Prerequisites

- **Function .name property** — `new Function()` naming is a special case

# Key Properties

1. Name is always `'anonymous'`
2. Required for web compatibility
3. Unlike other anonymous functions, does not infer from context

# Construction / Recognition

## To Construct/Create:
1. `new Function('return 1')`

## To Identify/Recognize:
1. `.name === 'anonymous'`

# Context & Application

This is a rare edge case. `new Function()` is uncommon in modern code but understanding its naming is useful for debugging.

# Examples

**Example 1** (Ch 21):
```js
assert.equal(new Function().name, 'anonymous');
```

# Relationships

## Builds Upon
- **Function .name property** — A special naming case

## Related
- **Bound function naming** — Another special naming pattern

# Common Confusions

- **Confusion**: `new Function()` produces a function with an empty name
  **Clarification**: It produces `'anonymous'`, not `''`

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.10, lines 11437+.

# Verification Notes

- Definition source: direct from source with assertion
- Confidence rationale: Explicitly stated
- Cross-reference status: verified (references WebKit bug)
