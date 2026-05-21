---
# === CORE IDENTIFICATION ===
concept: Anonymous Variable
slug: anonymous-variable

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "underscore variable"
  - "don't care variable"
  - "wildcard variable"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables
  - pattern-matching
extends:
  - variables
related:
  - underscore-prefixed-variables
contrasts_with:
  - underscore-prefixed-variables

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the anonymous variable in Erlang?"
  - "How do I ignore a value in a pattern?"
  - "What does underscore mean in Erlang?"
---

# Quick Definition

The anonymous variable, denoted by a standalone underscore (`_`), is used in patterns when a variable is required but its value can be ignored. Each occurrence of `_` is independent and does not bind to any value.

# Core Definition

The Erlang Reference Manual states: "The _anonymous variable_ is denoted by underscore (`_`) and can be used when a variable is required but its value can be ignored." Unlike regular variables, each occurrence of `_` is independent -- multiple `_` in the same pattern do not need to match the same value (Erlang Reference Manual, "Expressions", "Variables").

# Prerequisites

- **variables** -- The anonymous variable is a special kind of variable
- **pattern-matching** -- The anonymous variable is used in patterns

# Key Properties

1. Denoted by a single underscore: `_`
2. Used when a value must be present but is not needed
3. Each occurrence is independent -- multiple `_` can match different values
4. Never binds to a value (cannot be referenced later)
5. Does not generate compiler warnings for unused values

# Construction / Recognition

## To Construct/Create:
1. Write `_` wherever a variable is required but the value is irrelevant

## To Identify/Recognize:
1. A standalone underscore `_` in a pattern position
2. Contrasted with `_Name` which is a regular variable with a name starting with underscore

# Context & Application

The anonymous variable is essential for writing clean pattern-matching code. It communicates intent ("I know there's a value here but I don't care about it") and avoids cluttering the namespace with unused variable names. It is heavily used in function clause heads, case expressions, and receive patterns.

# Examples

**Example 1** (Variables section): Using `_` to ignore the tail of a list:
```erlang
[H|_] = [1,2,3]
```

**Example 2** (Variables section): Multiple `_` in a tuple pattern match independently:
```erlang
{_,_} = {1,2}   %% succeeds -- each _ matches independently
```

# Relationships

## Builds Upon
- **variables** -- The anonymous variable is a special variable
- **pattern-matching** -- Used exclusively in pattern positions

## Related
- **underscore-prefixed-variables** -- Variables starting with `_` but having a name (e.g., `_X`) are NOT anonymous

## Contrasts With
- **underscore-prefixed-variables** -- `_` is anonymous (never binds); `_Name` is a named variable that binds but suppresses warnings

# Common Errors

- **Error**: Trying to reference the value of `_` after a match
  **Correction**: The anonymous variable does not bind; use a named variable (even `_Name`) if you need the value later

# Common Confusions

- **Confusion**: Thinking `_Name` (e.g., `_Height`) is anonymous like `_`
  **Clarification**: Variables starting with underscore followed by a name are regular variables that bind normally; they simply suppress unused-variable warnings. Only the bare `_` is truly anonymous.

# Source Reference

"Expressions" chapter, section "Variables", paragraphs on the anonymous variable and the `[H|_]` example.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: HIGH -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
