---
# === CORE IDENTIFICATION ===
concept: Creation-Time Naming
slug: creation-time-naming

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
section: "21.3.1 The name of a function is always assigned at creation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "name assignment at creation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
  - function-naming-rules
extends: []
related:
  - anonymous-function-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

A function's `.name` is set at creation time and is never updated by later assignments, even if the function is stored in a named variable after creation.

# Core Definition

From "Deep JavaScript" (Ch 21.3.1): "A function only gets a name if one of the previously mentioned patterns is used during its creation. Using one of the patterns later doesn't change anything." The text notes: "Missing function names could conceivably be updated later, but doing so would impact performance negatively."

# Prerequisites

- **Function .name property** — Understanding what `.name` is
- **Function naming rules** — Understanding which patterns set `.name`

# Key Properties

1. Name is assigned once, at creation time
2. Later assignments to variables do not update the name
3. Performance is the reason for not updating names retroactively
4. Functions returned from factories remain unnamed (`.name === ''`)

# Construction / Recognition

## To Construct/Create:
1. This is a constraint, not a constructible pattern

## To Identify/Recognize:
1. A function with `.name === ''` stored in a named variable

# Context & Application

This explains why some functions appear unnamed in stack traces even when stored in named variables: the naming context must be present at creation time.

# Examples

**Example 1** (Ch 21):
```js
function functionFactory() {
  return function () {}; // name set to '' here (line A)
}
const func = functionFactory(); // (line B)
assert.equal(func.name, ''); // still anonymous
```

# Relationships

## Builds Upon
- **Function naming rules** — This is a constraint on when naming occurs

## Related
- **Anonymous function expression** — Factory-returned functions remain truly anonymous

# Common Errors

- **Error**: Expecting a factory-returned function to get a name from its variable
  **Correction**: The name was already set to `''` at creation time in the factory

# Common Confusions

- **Confusion**: Assigning to a `const` always names the function
  **Clarification**: Only if the function is created in the assignment expression; a pre-existing anonymous function keeps its empty name

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.3.1, lines 11437+.

# Verification Notes

- Definition source: direct from source with example
- Confidence rationale: Explicitly explained with rationale
- Cross-reference status: verified
