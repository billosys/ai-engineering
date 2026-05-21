---
# === CORE IDENTIFICATION ===
concept: List
slug: list

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "List"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - proper list

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - tuple
  - string
contrasts_with:
  - tuple

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a proper list from an improper list?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
  - "What is an Erlang term?"
---

# Quick Definition
A list is a compound data type with a variable number of terms, written as `[Term1,...,TermN]`. Lists are constructed from a head (first element) and a tail (the rest), and are one of Erlang's most fundamental data structures.

# Core Definition
The Erlang Reference Manual defines a list as "a compound data type with a variable number of terms," written as `[Term1,...,TermN]`. Formally, "a list is either the empty list `[]` or consists of a _head_ (first element) and a _tail_ (remainder of the list). The _tail_ is also a list." The head-tail structure is expressed as `[H|T]`, and the shorthand `[Term1,...,TermN]` is equivalent to `[Term1|[...|[TermN|[]]]]`. A list where the tail is a list is called a "proper list." It is allowed to have a tail that is not a list (e.g., `[a|b]`), but "this type of list is of little practical use" (Data Types, "List" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Compound data type with a variable number of terms
2. Written as `[Term1,...,TermN]`
3. Either the empty list `[]` or a head-tail pair `[H|T]`
4. The tail of a proper list is itself a list
5. `[a,b,c]` is equivalent to `[a|[b|[c|[]]]]`
6. Improper lists (tail is not a list, e.g., `[a|b]`) are allowed but rarely useful
7. The number of elements is the length, obtained via `length/1`
8. Elements can be of any type (heterogeneous)

# Construction / Recognition
## To Construct/Create:
1. Use literal syntax: `[a, 2, {c, 4}]`
2. Use cons operator: `[d | T]` prepends `d` to list `T`
3. Use list comprehensions: `[X * 2 || X <- [1,2,3]]`
4. Convert from tuple: `tuple_to_list({a,b,c})`

## To Identify/Recognize:
1. Use `is_list/1` BIF to test if a term is a list (tests for the empty list or a cons cell)
2. Use `length/1` to get the number of elements
3. Pattern match with `[H|T]` to decompose into head and tail

# Context & Application
Lists are the primary sequential data structure in Erlang, used for:
- Processing collections of items with recursion
- Strings (which are lists of integer code points)
- Arguments to functions and return values
- Pattern matching on sequential data

Lists support efficient prepend (O(1)) but expensive random access (O(n)). The `lists` module in STDLIB provides a comprehensive collection of list-processing functions.

# Examples
**Example 1** (Data Types, "List" section): Building and decomposing lists:
```erlang
1> L1 = [a,2,{c,4}].
[a,2,{c,4}]
2> [H|T] = L1.
[a,2,{c,4}]
3> H.
a
4> T.
[2,{c,4}]
5> L2 = [d|T].
[d,2,{c,4}]
6> length(L1).
3
7> length([]).
0
```

**Example 2** (Data Types, "List" section): The formal structure of a list:
`[]` is a list, thus
`[c|[]]` is a list, thus
`[b|[c|[]]]` is a list, thus
`[a|[b|[c|[]]]]` is a list, or in short `[a,b,c]`

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
- **string** -- Erlang strings are lists of integer code points

## Related
- **erlang-term** -- Lists are a kind of term; list elements are terms
- **tuple** -- Both are compound types; tuples are fixed-size, lists are variable-size

## Contrasts With
- **tuple** -- Tuples have fixed size with O(1) element access; lists have variable length with O(1) head access and O(n) random access

# Common Errors
- **Error**: Expecting `[a|b]` to be a proper list
  **Correction**: `[a|b]` is an improper list because `b` is not a list. Proper lists always terminate with `[]`.

- **Error**: Using `length/1` to check if a list is empty (O(n) traversal)
  **Correction**: Pattern match against `[]` or use `L =:= []` for O(1) emptiness check

# Common Confusions
- **Confusion**: Confusing proper lists with improper lists
  **Clarification**: A proper list has `[]` as the ultimate tail. An improper list like `[a|b]` has a non-list tail. Most list functions (e.g., `length/1`, `lists:map/2`) require proper lists and will crash on improper lists.

- **Confusion**: Expecting lists to provide O(1) random access like arrays
  **Clarification**: Lists are linked structures. Accessing the Nth element requires traversing N-1 elements.

# Source Reference
Data Types chapter, "List" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
