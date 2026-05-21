---
concept: List
slug: list
category: data-types
subcategory: compound-types
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Lists"
extraction_confidence: high
aliases:
  - "proper list"
  - "improper list"
  - "string"
prerequisites:
  - variable
extends: []
related:
  - cons-and-list-operations
  - list-comprehension
  - tuple
contrasts_with:
  - tuple
  - binary-string
answers_questions:
  - "What distinguishes a list from a tuple?"
  - "What are the basic data types in Erlang?"
---

# List

## Quick Definition

A list is the most-used Erlang data structure: a variable-length, ordered collection written `[Element1, ..., ElementN]` that can hold values of any type. Strings are just lists of numbers.

## Core Definition

Lists are the bread and butter of Erlang and can contain anything — numbers, atoms, tuples, other lists. The basic notation is `[Element1, Element2, ..., ElementN]`, and types may be mixed freely. Erlang has no real string type: strings are lists of integers, and Erlang prints a list of numbers as a string only when every element could represent a printable character. A *proper list* ends with an empty list as its last cell; an *improper list* (e.g., `[1|2]`) does not and fails with standard functions (Hébert, ch. 1, "Lists").

## Prerequisites

- **Variable** — List elements are commonly bound and unpacked through variables

## Key Properties

1. Variable-length, ordered, written with square brackets.
2. May mix any data types, including nested lists and tuples.
3. Strings are lists of integers; `"abc"` equals `[97,98,99]`.
4. `++` concatenates lists; `--` removes elements; both are right-associative.
5. A proper list ends with `[]`; an improper list does not and breaks `length()` etc.
6. Accessing or adding the head is fast and efficient.

## Construction / Recognition

To recognize how a list is built, all of these are equivalent: `[a,b,c,d]`, `[a,b,c,d|[]]`, `[a,b|[c,d]]`, `[a|[b|[c|[d|[]]]]]`.

## Context & Application

Lists are used to solve all kinds of problems and are the most-used data structure in Erlang. Because Erlang has no built-in string type, text manipulation is weaker than in Perl or Python, though binary strings provide a more efficient alternative for storage.

## Examples

**Example** (ch. 1): `[1, 2, 3, {numbers,[4,5,6]}, 5.34, atom].` mixes integers, a tuple, a float, and an atom.

**Example** (ch. 1): `[97, 98, 99].` is printed as `"abc"` because each integer is a printable character.

## Relationships

### Prerequisites

- **Variable** — List elements bind to variables

### Related

- **Cons and list operations** — The `[H|T]` cons form builds and decomposes lists
- **List comprehension** — A concise way to build and modify lists

### Contrasts With

- **Tuple** — A list has variable length; a tuple has a fixed length
- **Binary string** — Binary strings store text more efficiently than lists of integers

## Common Errors

- **Error**: Using an improper list like `[1|2]` with standard functions
  **Correction**: Build proper lists ending in `[]`; `[1|[2]]` is proper

## Common Confusions

- **Confusion**: Expecting a dedicated string type
  **Clarification**: Strings are lists of integers; there is no separate string type

## Source Reference

Chapter 1: "Starting Out," section "Lists."

## Verification Notes

- Definition: Adapted from the "Lists" section, including the proper/improper list note
- Confidence: HIGH — explicit section
- Uncertainties: None
