---
# === CORE IDENTIFICATION ===
concept: List
slug: list

# === CLASSIFICATION ===
category: data-types
subcategory: compound-types
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Lists"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cons cell
  - head and tail
  - "[H|T]"
  - improper list

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - pattern-matching
  - the-match-operator
  - term
  - recursion
contrasts_with:
  - tuple

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a list?"
  - "What distinguishes a list from a tuple?"
---

# Quick Definition

A list stores an arbitrary number of things, written with square brackets and commas. It has a head (first element) and a tail (the rest); `[H|T]` constructs or deconstructs a list.

# Core Definition

"Lists are used to store arbitrary numbers of things. We create a list by enclosing the list elements in square brackets and separating them with commas" (Chapter 3, "Lists"). "The individual elements of a list can be of any type." The first element is the *head*; "if you imagine removing the head from the list, what's left is called the *tail*" — for `[1,2,3,4,5]` the head is `1` and the tail is `[2,3,4,5]` (Chapter 3, "Terminology"). "If `T` is a list, then `[H|T]` is also a list with head `H` and tail `T`. The vertical bar (`|`) separates the head of a list from its tail. `[ ]` is the empty list" (Chapter 3, "Defining Lists"). When `[...|T]` is used and `T` is a list, the result is a "properly formed" list; if `T` is not a list, the result is an "improper list" that most library functions will not handle. "Accessing the head of a list is a very efficient operation."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A list stores an arbitrary number of elements; the count is not fixed.
2. It is written `[E1, E2, ...]` — square brackets, comma-separated.
3. Elements can be of any type, even mixed types.
4. It has a *head* (first element) and a *tail* (the remaining list).
5. `[H|T]` constructs a list (in an expression) or deconstructs one (in a pattern).
6. `[]` is the empty list.
7. A list whose tail is a list is "properly formed"; otherwise it is "improper."
8. Accessing the head is very efficient.

# Construction / Recognition

## To Create a List:
1. Enclose elements in `[ ]`, comma-separated, e.g. `[1,2,3]`.
2. Or prepend elements with `[E1,E2,...|T]` where `T` is an existing list.

## To Extract Head and Tail:
1. Match the nonempty list against `[X|Y]`; `X` binds to the head, `Y` to the tail.
2. Match `[A,B,C|T]` to take several leading elements at once.

## To Recognize It:
1. Data enclosed in square brackets.

# Context & Application

- **Typical contexts**: Collections of unknown or variable length — shopping lists, drawings, sequences.
- **Common applications**: List processing functions extract the head, act on it, and recurse on the tail.
- **Historical/stylistic notes**: For LISP programmers, `[H|T]` "is a CONS cell with CAR `H` and CDR `T`."

# Examples

**Example 1** (Chapter 3, "Lists"): `[1+7,hello,2-2,{cost, apple, 30-20},3]` evaluates to `[8,hello,0,{cost,apple,10},3]` — a list mixing integers, an atom, and a tuple.

**Example 2** (Chapter 3, "Extracting Elements from a List"): `[Buy1|ThingsToBuy2] = ThingsToBuy1` binds `Buy1` to the head `{oranges,4}` and `ThingsToBuy2` to the tail.

# Relationships

## Builds Upon
- This is a foundational data type and does not build upon another card in this source.

## Enables
- **Recursion** — List processing is the canonical use of recursion: act on the head, recurse on the tail.

## Related
- **Pattern matching** / **the match operator** — `[H|T]` patterns extract list elements.
- **Recursion** — Most list functions are recursive over head and tail.
- **Term** — A list is one kind of compound term.

## Contrasts With
- **Tuple** — A list holds an *arbitrary* number of elements; a tuple holds a *fixed* number. Use a tuple for a fixed group of fields, a list for a variable-length collection.

# Common Errors

- **Error**: Building a list with `[H|T]` where `T` is not a list.
  **Correction**: Ensure `T` is a list so the result is "properly formed"; improper lists break most library functions.

- **Error**: Matching `[H|T]` against an empty list.
  **Correction**: `[H|T]` only matches a *nonempty* list; handle `[]` with a separate pattern.

# Common Confusions

- **Confusion**: Thinking the tail of a list is its last element.
  **Clarification**: The tail is everything *after* the head — itself a list — not the final element.

- **Confusion**: Believing a list and a tuple are interchangeable.
  **Clarification**: Lists vary in length and use `[ ]`; tuples are fixed-size and use `{ }`.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Lists," "Terminology," "Defining Lists," and "Extracting Elements from a List." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Lists" and "Defining Lists."
- Confidence rationale: HIGH — lists, head/tail, and `[H|T]` are explicitly defined with examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
