---
concept: Tuple
slug: tuple
category: data-types
subcategory: compound-types
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Tuples"
extraction_confidence: high
aliases:
  - "tagged tuple"
prerequisites:
  - atom
  - variable
extends: []
related:
  - pattern-matching
contrasts_with:
  - list
answers_questions:
  - "What is a tuple?"
  - "What distinguishes a list from a tuple?"
---

# Tuple

## Quick Definition

A tuple is a way to group together a fixed number of terms into a single value. It is written as `{Element1, Element2, ..., ElementN}`.

## Core Definition

A tuple groups a set number of terms, written in the form `{Element1, Element2, ..., ElementN}`. Any element can be of any type, including another tuple. A tuple containing an atom followed by one element is called a *tagged tuple*; the atom qualifies the data, making the kind of data being passed explicit and easier to debug. Pattern matching unpacks tuple values, but only if the tuple lengths match (Hébert, ch. 1, "Tuples").

## Prerequisites

- **Atom** — Tagged tuples use an atom as their first element to label the data
- **Variable** — Tuple values are typically unpacked into variables via pattern matching

## Key Properties

1. Holds a fixed (set) number of terms.
2. Written with curly brackets: `{X, Y}`.
3. Elements may be of any type, including nested tuples.
4. A tagged tuple has an atom as its first element to qualify the data.
5. Pattern matching to unpack a tuple succeeds only when the lengths are equal.

## Construction / Recognition

To unpack a tuple:

1. Place a tuple pattern of matching length on the left of `=`.
2. Use variables for elements you want, and `_` for elements you do not care about.
3. Erlang binds the variables to the corresponding elements.

## Context & Application

Tuples let you carry related values as a single unit (e.g., a Cartesian point `{X,Y}`). Tagged tuples such as `{celsius, 23.213}` attach a unit/meaning to a value, so mismatched data raises an exception early — acting as a debugging aid.

## Examples

**Example** (ch. 1): `Point = {4,5}.` then `{X,Y} = Point.` binds `X` to `4` and `Y` to `5`.

**Example** (ch. 1): `{kelvin, T} = {celsius, 23.213}.` raises a no-match exception because the atom tags differ.

## Relationships

### Prerequisites

- **Atom** — Used as the tag in tagged tuples
- **Variable** — Tuple elements are unpacked into variables

### Related

- **Pattern matching** — Tuples are unpacked by matching tuple patterns

### Contrasts With

- **List** — A tuple has a fixed length and is unpacked positionally; a list has variable length and is processed head/tail

## Common Errors

- **Error**: Matching a tuple pattern against a tuple of a different length
  **Correction**: Tuple lengths must match exactly; use a pattern of the right size

## Common Confusions

- **Confusion**: Using a tuple where the number of elements varies
  **Clarification**: Tuples hold a fixed number of terms; use a list for variable-length collections

## Source Reference

Chapter 1: "Starting Out," section "Tuples."

## Verification Notes

- Definition: Adapted from the "Tuples" section with point and temperature examples
- Confidence: HIGH — explicit section
- Uncertainties: None
