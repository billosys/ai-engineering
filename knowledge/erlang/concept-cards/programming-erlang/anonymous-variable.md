---
# === CORE IDENTIFICATION ===
concept: Anonymous Variable
slug: anonymous-variable

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: patterns
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Extracting Values from Tuples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - underscore
  - "_"
  - don't-care variable

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - single-assignment-variable
  - tuple
  - list
contrasts_with:
  - single-assignment-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the underscore variable in Erlang?"
  - "How do I ignore values I don't care about in a pattern?"
---

# Quick Definition

The anonymous variable, written `_`, is a placeholder in a pattern for a value you do not care about. It matches anything, never binds, and may appear several times in one pattern without the occurrences having to be equal.

# Core Definition

"We wrote `_` as a placeholder for variables that we're not interested in. The symbol `_` is called an *anonymous variable*. Unlike regular variables, several occurrences of `_` in the same pattern don't have to bind to the same value" (Chapter 3, "Extracting Values from Tuples"). It is used inside patterns wherever a position must be matched but its value discarded — for example `{_,{_,Who,_},_} = Person` extracts only the field captured by `Who` and ignores everything else.

# Prerequisites

- **Pattern matching** — The anonymous variable only has meaning inside a pattern; you must understand pattern matching first.

# Key Properties

1. Written as a single underscore, `_`.
2. Matches any value.
3. Never binds — its matched value is discarded and cannot be referred to.
4. Multiple occurrences of `_` in one pattern need not match the same value.
5. Used wherever a pattern position must be filled but the value is unwanted.

# Construction / Recognition

## To Use the Anonymous Variable:
1. In a pattern, write `_` at every position whose value you do not need.
2. Place named variables only where you want to capture values.

## To Recognize It:
1. A bare `_` appearing inside a pattern (tuple, list, function head, `case`, or `receive`).

# Context & Application

- **Typical contexts**: Extracting one field from a large nested structure; function clauses that ignore an argument.
- **Common applications**: `{_,{_,Who,_},_} = Person` to pull out one name; `map(_, []) -> []` to ignore the function argument when the list is empty.
- **Historical/stylistic notes**: Using `_` documents intent — it signals to a reader that a value is deliberately unused.

# Examples

**Example 1** (Chapter 3, "Extracting Values from Tuples"): `{_,{_,Who,_},_} = Person` matched against `{person,{name,joe,armstrong},{footsize,42}}` binds only `Who` to `joe`, discarding all other positions.

**Example 2** (Chapter 4, "Simple List Processing"): `map(_, []) -> [];` — the first clause of `map/2` uses `_` because mapping any function over an empty list ignores the function entirely.

# Relationships

## Builds Upon
- **Pattern matching** — The anonymous variable is a pattern element.

## Enables
- Cleaner patterns that capture only the values that matter.

## Related
- **Single-assignment variable** — `_` is a special, non-binding variable.
- **Tuple** / **list** — Common structures in which `_` discards unwanted positions.

## Contrasts With
- **Single-assignment variable** — A named variable binds once and a repeated name must match the same value; `_` never binds and repeated `_` occurrences are independent.

# Common Errors

- **Error**: Trying to use the value matched by `_` later in the code.
  **Correction**: `_` does not bind; if you need the value, use a named variable.

- **Error**: Assuming two `_` in one pattern must be equal.
  **Correction**: Each `_` is independent; they need not match the same value.

# Common Confusions

- **Confusion**: Thinking `_` is just a normal variable named underscore.
  **Clarification**: `_` is the *anonymous* variable — it never binds and its occurrences are unrelated.

- **Confusion**: Believing `_Name` (underscore-prefixed names) behaves like `_`.
  **Clarification**: Chapter 3 introduces only the bare `_`; a name beginning with `_` is still a regular (binding) variable, conventionally marking deliberate non-use.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Extracting Values from Tuples." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation from Chapter 3, "Extracting Values from Tuples."
- Confidence rationale: HIGH — the anonymous variable is explicitly named and its key rule stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
