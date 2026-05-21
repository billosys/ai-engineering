---
# === CORE IDENTIFICATION ===
concept: List
slug: list

# === CLASSIFICATION ===
category: data-types
subcategory: lists
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.5 Lists"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cons cell
  - list cell
  - nil
  - proper list
  - improper list

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - string
  - tuple
  - pattern-matching
contrasts_with:
  - tuple

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a list in Erlang?"
  - "How is a list structured in memory?"
  - "What is the difference between a proper and an improper list?"
  - "Why should you add to the left of a list?"
---

# Quick Definition

A list is a variable-length sequence of terms, built from the empty list and cons cells (head + tail pointer) forming a singly linked list. It is Erlang's workhorse data type.

# Core Definition

"*Lists* are truly the workhorse of Erlang's data types" (Chapter 2, section 2.2.5). They are written within square brackets and hold an arbitrary number of items. Lists are "created from the *empty list* (nil) and so-called *list cells* which add one element at a time on top of an existing list, building a singly linked list in memory" (section 2.2.10). Each list cell uses two words of memory: the *head* (the value or a pointer to it) and the *tail* (a pointer to the rest of the list). The `|` (vertical bar) constructs a new cell: `[1 | []]` yields `[1]`, and `[5,4,3 | [2,1]]` yields `[5,4,3,2,1]`. The `++` operator appends lists; its cost depends on the length of the *left* list. A *proper list* ends with an empty list as its innermost tail; an *improper list* has a non-list tail and is generally a programming error.

# Prerequisites

- **Erlang term** — a list is a term and holds terms.

# Key Properties

1. A list is a variable-length sequence written within square brackets.
2. It is built from the empty list `[]` (nil) and list cells (cons cells).
3. Each cell holds a head (value) and a tail (rest of the list); a cell uses two words of memory.
4. `[H | T]` constructs a cell; the `|` separates head(s) from the tail.
5. `++` appends lists; its time cost depends on the length of the left-hand list.
6. A proper list ends in `[]`; an improper list ends in a non-list term.
7. The `++` operator never modifies its right-hand list.

# Construction / Recognition

## To Construct/Create:
1. Write elements in square brackets: `[1, 2, 3]`.
2. Or cons onto an existing list: `[New | OldList]`.
3. Append two lists with `++`: `[1,2] ++ [3,4]`.
4. Prefer adding to the left; reverse at the end if necessary.

# Context & Application

- **Typical contexts**: Temporary data, collections being processed, accumulating results, string buffers.
- **Common applications**: Most data processing is traversing a list of items; lists are the main intermediate data structure.
- **Historical/stylistic notes**: List cells are called *cons cells* by people with a Lisp/functional background; adding a cell is *consing*. For long-term storage of large constant data, binaries may be preferable.

# Examples

**Example 1** (section 2.2.5): `[]`, `[1, 2, 3]`, `[one, two, three]`, `[[1,2,3],[4,5,6]]`, and a list of tagged tuples are all valid lists.

**Example 2** (section 2.2.10): `[1, 2, [3,4]]` is a three-element list whose last element is a list, while `[1, 2 | [3,4]]` is a four-element list — the `|` versus `,` distinction.

# Relationships

## Builds Upon
- **Erlang term** — a list holds terms and is a term.

## Enables
- **String** — strings are lists of character codes.
- **Recursion** — list traversal is naturally recursive.

## Related
- **Pattern matching** — `[H | T]` patterns decompose lists.

## Contrasts With
- **Tuple** — tuples are fixed-length with constant-time element access; lists are variable-length linked structures.

# Common Errors

- **Error**: Repeatedly appending with `++` to the end of a growing list.
  **Correction**: `++` cost grows with the left list's length; add to the left and reverse once at the end.

- **Error**: Writing a comma where a `|` was intended (or vice versa).
  **Correction**: `[1,2,[3,4]]` is a 3-element list; `[1,2|[3,4]]` is a 4-element list — choose deliberately.

- **Error**: Building an improper list by consing onto a non-list, e.g. `[1 | oops]`.
  **Correction**: Treat improper lists as programming errors; functions expecting proper lists will crash on them.

# Common Confusions

- **Confusion**: Thinking `++` modifies one of its arguments.
  **Clarification**: The right-hand list is never modified; the left-hand list is copied to build the result.

# Source Reference

Chapter 2: Erlang language essentials, sections 2.2.5 "Lists" and 2.2.10 "Understanding lists." See Figures 2.1 and 2.2.

# Verification Notes

- Definition source: Direct adaptation from sections 2.2.5 and 2.2.10.
- Confidence rationale: HIGH — lists, list cells, and proper/improper lists are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `recursion` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card. Merged the 2.2.5 introduction and the 2.2.10 "Understanding lists" structural treatment into one card, since both describe the same concept (the list) progressively.
