---
concept: Cons and List Operations
slug: cons-and-list-operations
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
  - "cons operator"
  - "head and tail"
  - "[H|T]"
  - "list constructor"
prerequisites:
  - list
  - pattern-matching
extends:
  - list
related:
  - recursion
contrasts_with: []
answers_questions:
  - "What distinguishes a list from a tuple?"
---

# Cons and List Operations

## Quick Definition

The cons operator `|` separates a list's head (its first element) from its tail (the rest). The `[Head|Tail]` form both constructs lists and decomposes them via pattern matching.

## Core Definition

The first element of a list is the *head*, and the rest is the *tail*; the BIFs `hd/1` and `tl/1` return them. The `|` symbol is the *cons* operator (constructor): any list can be built from cons operators and values alone, e.g., `[3 | [2 | [1 | []]]]`. The pattern `[Head|Tail]` separates the head from the tail by pattern matching, and `[NewHead|List]` prepends a new head. Lists are therefore defined recursively as a head preceding a tail (Hébert, ch. 1, "Lists").

## Prerequisites

- **List** — Cons operations build and decompose lists
- **Pattern matching** — `[H|T]` decomposition is a form of pattern matching

## Key Properties

1. `hd(List)` returns the head; `tl(List)` returns the tail.
2. `|` is the cons operator, used both to build and to decompose lists.
3. `[X | List]` prepends `X` as a new head.
4. `[Head|Tail] = List` binds `Head` to the first element and `Tail` to the rest.
5. Lists are defined recursively: a head followed by a tail that is itself a list.
6. Accessing or prepending the head is fast and efficient.

## Construction / Recognition

To prepend an element: write `[NewElement | ExistingList]`.

To decompose a list:

1. Place `[Head|Tail]` on the left of `=`.
2. Erlang binds `Head` to the first element and `Tail` to the remaining list.

## Context & Application

Virtually all list-processing in Erlang operates on the head first, then recurses on the tail. This head/tail recursion underpins recursive functions and list comprehensions.

## Examples

**Example** (ch. 1): `hd([1,2,3,4]).` returns `1`; `tl([1,2,3,4]).` returns `[2,3,4]`.

**Example** (ch. 1): `NewList = [1|List].` where `List = [2,3,4]` produces `[1,2,3,4]`.

## Relationships

### Prerequisites

- **List** — The structure being built/decomposed
- **Pattern matching** — `[H|T]` is a matching pattern

### Builds Upon

- **List** — Cons is the constructor for lists

### Related

- **Recursion** — Recursive list functions repeatedly split head from tail

## Common Errors

- **Error**: Writing `[1 | 2]` and expecting a usable list
  **Correction**: The tail must itself be a list; use `[1 | [2]]`

## Common Confusions

- **Confusion**: Thinking `hd` and `tl` belong to a `lists` module
  **Clarification**: They are BIFs in the `erlang` module, automatically imported

## Source Reference

Chapter 1: "Starting Out," section "Lists."

## Verification Notes

- Definition: Adapted from the head/tail and cons discussion
- Confidence: HIGH — explicit treatment with examples
- Uncertainties: None
