---
# === CORE IDENTIFICATION ===
concept: Tuple
slug: tuple

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
section: "Tuple"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - atom
  - list
  - map
  - record-definition
contrasts_with:
  - list
  - map

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tuple?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
  - "What is an Erlang term?"
---

# Quick Definition
A tuple is a compound data type with a fixed number of terms, written as `{Term1,...,TermN}`. Each term is called an element, and the number of elements is the size of the tuple.

# Core Definition
The Erlang Reference Manual defines a tuple as "a compound data type with a fixed number of terms," written as `{Term1,...,TermN}`. Each term in the tuple is called an element, and the number of elements is the size of the tuple. Tuples support several BIFs: `element/2` for positional access, `setelement/3` for creating a modified copy, `tuple_size/1` for the number of elements, and `is_tuple/1` for type testing (Data Types, "Tuple" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Compound data type with a fixed number of elements
2. Written as `{Term1,...,TermN}`
3. Elements are accessed by position (1-based indexing)
4. The empty tuple `{}` has size 0
5. Elements can be any term, including other tuples (nesting)
6. Tuple size is fixed at creation; adding/removing elements creates a new tuple
7. Conventionally, the first element is an atom tag identifying the tuple's purpose

# Construction / Recognition
## To Construct/Create:
1. Use literal syntax: `{adam, 24, {july, 29}}`
2. Use `setelement/3` to create a modified copy: `setelement(2, P, 25)`
3. Convert from list: `list_to_tuple([a,b,c])`

## To Identify/Recognize:
1. Use `is_tuple/1` BIF
2. Use `tuple_size/1` to get the number of elements
3. Use `element(N, Tuple)` to access the Nth element (1-based)

# Context & Application
Tuples are one of the core data structures in Erlang, used for:
- Tagged values: `{ok, Value}`, `{error, Reason}`
- Fixed-size records before maps were introduced
- Return values from functions (multiple return via tuple)
- The underlying representation of tuple-based records

Tuples are chosen over lists when the number of elements is known and fixed. Access by position is O(1), while lists require O(n) traversal.

# Examples
**Example 1** (Data Types, "Tuple" section):
```erlang
1> P = {adam,24,{july,29}}.
{adam,24,{july,29}}
2> element(1,P).
adam
3> element(3,P).
{july,29}
4> P2 = setelement(2,P,25).
{adam,25,{july,29}}
5> tuple_size(P).
3
6> tuple_size({}).
0
7> is_tuple({a,b,c}).
true
```

**Example 2** (Data Types, "Type Conversions" section):
```erlang
10> tuple_to_list({a,b,c}).
[a,b,c]
11> list_to_tuple([a,b,c]).
{a,b,c}
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
- **record-definition** -- Tuple-based records are syntactic sugar over tuples
- **tuple-based-record-internal-representation** -- Records are internally represented as tuples

## Related
- **erlang-term** -- Tuples are a kind of term
- **atom** -- Atoms are typically used as tuple tags
- **list** -- Lists are variable-length; tuples are fixed-length
- **map** -- Maps are key-value stores; tuples are positional

## Contrasts With
- **list** -- Lists have variable length and efficient head access; tuples have fixed size and efficient positional access
- **map** -- Maps use key-based access; tuples use positional (index-based) access

# Common Errors
- **Error**: Using 0-based indexing with `element/2`
  **Correction**: Erlang tuples use 1-based indexing. `element(1, {a,b,c})` returns `a`.

- **Error**: Trying to modify a tuple in place
  **Correction**: Tuples are immutable. `setelement/3` returns a new tuple with the modification.

# Common Confusions
- **Confusion**: Confusing tuples with lists
  **Clarification**: Tuples use `{}`, have fixed size, and provide O(1) element access. Lists use `[]`, have variable length, and provide O(1) head access but O(n) random access.

# Source Reference
Data Types chapter, "Tuple" section and "Type Conversions" section.

# Verification Notes
- Definition source: Direct quote from source ("a compound data type with a fixed number of terms")
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
