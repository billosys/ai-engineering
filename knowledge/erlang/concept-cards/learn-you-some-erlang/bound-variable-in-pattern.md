---
concept: Bound Variable in a Pattern
slug: bound-variable-in-pattern
category: functions-pattern-matching
subcategory: pattern-matching
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "Variables in a Bind"
extraction_confidence: high
aliases:
  - "repeated variable"
  - "non-linear pattern"
prerequisites:
  - pattern-matching
  - variable
extends:
  - pattern-matching
related:
  - function-clause
contrasts_with: []
answers_questions:
  - "What is pattern matching?"
---

# Bound Variable in a Pattern

## Quick Definition

When the same variable name appears more than once in a pattern, its first occurrence binds a value and later occurrences must match that bound value — letting a function test that two arguments are identical.

## Core Definition

The concept of free and bound variables holds true inside function heads. When a variable appears in a pattern, its first occurrence is treated as unbound and takes on the matched value; if the same variable name appears again, Erlang sees it as already bound and compares the new value against it. If the values differ, the pattern match fails and Erlang moves to the next clause. This lets a function such as `same(X,X)` test whether its two arguments are equal (Hébert, ch. 3, "Variables in a Bind").

## Prerequisites

- **Pattern matching** — This is a refinement of how patterns match
- **Variable** — Relies on the bound/unbound distinction

## Key Properties

1. A variable's first occurrence in a pattern binds it.
2. A repeated occurrence of the same name must match the already-bound value.
3. A mismatch causes the clause to fail, moving to the next clause.
4. This works for any data type, not just lists or single values.
5. The `=` operator may also be used in a function head to match a structure and its parts.

## Construction / Recognition

To test argument equality with a repeated variable:

1. Use the same variable name in two argument positions of a clause head, e.g., `same(X,X)`.
2. Provide a fallback clause `same(_,_)` for the non-equal case.

## Context & Application

Repeated variables in patterns provide a concise, declarative equality test inside function heads, avoiding an explicit comparison in the body.

## Examples

**Example** (ch. 3): `same(X,X) -> true; same(_,_) -> false.` returns `true` only when both arguments are identical.

**Example** (ch. 3): `insert(Key, Val, {node, {Key, _, Smaller, Larger}})` (ch. 5) reuses `Key` to match a node whose key equals the new key.

## Relationships

### Prerequisites

- **Pattern matching** — The mechanism being refined
- **Variable** — Bound/unbound variable behavior

### Builds Upon

- **Pattern matching** — Repeated variables extend basic matching

### Related

- **Function clause** — Repeated variables appear in clause heads

## Common Errors

- **Error**: Expecting a repeated variable to rebind to a new value
  **Correction**: A repeated variable compares; it does not rebind

## Common Confusions

- **Confusion**: Thinking each occurrence of a variable in a pattern is independent
  **Clarification**: The first binds; subsequent ones must match the bound value

## Source Reference

Chapter 3: "Syntax in Functions," section "Variables in a Bind."

## Verification Notes

- Definition: Adapted from the `same/2` discussion
- Confidence: HIGH — explicit treatment with example
- Uncertainties: None
