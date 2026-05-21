---
# === CORE IDENTIFICATION ===
concept: Tagged Tuple
slug: tagged-tuple

# === CLASSIFICATION ===
category: data-types
subcategory: tuples
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.4 Tuples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - labeled tuple

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tuple
  - atom
extends:
  - tuple
related:
  - pattern-matching
  - function-clause-selection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tagged tuple?"
  - "Why label tuples with an atom?"
---

# Quick Definition

A tagged tuple is a tuple whose first element is an atom that labels what kind of data the tuple contains, such as `{size, 42}` or `{rectangle, 200, 100}`.

# Core Definition

"A standard convention in Erlang is to label tuples to indicate what type of data they contain, by using an atom as the first element, as in `{size, 42}`, or `{position, 5, 2}`. These are called *tagged tuples*" (Chapter 2, section 2.2.4). The tag makes the tuple's purpose explicit and, combined with pattern matching, lets code select and decompose data based on the tag — for example, function clauses that match `{circle, Radius}`, `{square, Side}`, or `{rectangle, Height, Width}` (section 2.5.4).

# Prerequisites

- **Tuple** — a tagged tuple is a kind of tuple.
- **Atom** — the tag is an atom.

# Key Properties

1. A tagged tuple's first element is an atom — the tag.
2. The tag indicates what kind of data the tuple contains.
3. It is a convention, not a language-enforced rule.
4. The tag enables clause selection and decomposition via pattern matching.

# Construction / Recognition

## To Construct/Create:
1. Choose an atom that names the data kind.
2. Make it the first element of the tuple, followed by the data.
3. Example: `{rectangle, Height, Width}`.

# Context & Application

- **Typical contexts**: Representing variant/record-like data; messages between processes.
- **Common applications**: Distinguishing shapes, status results (`{ok, Value}` / `{error, Reason}`), tagged messages.
- **Historical/stylistic notes**: Tagged tuples are the basis for the record syntax and for OTP message conventions.

# Examples

**Example 1** (section 2.2.4): `{size, 42}` and `{position, 5, 2}` are tagged tuples — atoms `size` and `position` label the data.

**Example 2** (section 2.5.4): The `area` function pattern-matches tagged tuples `{circle, Radius}`, `{square, Side}`, and `{rectangle, Height, Width}` to select the right clause.

# Relationships

## Builds Upon
- **Tuple** — a tagged tuple is a tuple with an atom-tagged first element.
- **Atom** — the tag is an atom.

## Enables
- **Function clause selection** — clauses can match on the tag.

## Related
- **Pattern matching** — patterns match the tag and bind the remaining elements.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Omitting the tag and relying only on tuple size to distinguish data kinds.
  **Correction**: Use an atom tag so the data's purpose is explicit and pattern-matchable.

# Common Confusions

- **Confusion**: Believing the tag is enforced by the language.
  **Clarification**: Tagged tuples are a convention; any tuple can have any first element.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.4 "Tuples." See also section 2.5.4 for tag-based clause selection.

# Verification Notes

- Definition source: Direct adaptation from section 2.2.4.
- Confidence rationale: HIGH — tagged tuples are explicitly named and defined.
- Uncertainties: None.
- Cross-reference status: `function-clause-selection` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
