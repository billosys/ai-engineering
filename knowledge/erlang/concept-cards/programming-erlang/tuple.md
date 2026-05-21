---
# === CORE IDENTIFICATION ===
concept: Tuple
slug: tuple

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
section: "Tuples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - tagged tuple

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
related:
  - pattern-matching
  - the-match-operator
  - term
  - record
contrasts_with:
  - list

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tuple?"
  - "What distinguishes a list from a tuple?"
---

# Quick Definition

A tuple groups a fixed number of items into a single entity, written with curly brackets and commas, e.g. `{joe, 1.82}`. Tuples are like anonymous C structs; values are extracted by pattern matching.

# Core Definition

"Suppose we want to group a fixed number of items into a single entity. For this we'd use a *tuple*. We can create a tuple by enclosing the values we want to represent in curly brackets and separating them with commas" (Chapter 3, "Tuples"). "Tuples are similar to structs in C, with the difference that they are anonymous" — the fields have no names. To make a tuple's purpose clear, "it's common to use an atom as the first element of the tuple, which describes what the tuple represents" — so `{point, 10, 45}` is preferred over `{10, 45}`. "This way of tagging a tuple is not a language requirement but is a recommended style of programming." Tuples can be nested, are created automatically when declared, and are reclaimed by the garbage collector. Values are extracted with the pattern matching operator: "the tuples on both sides of the equal sign must have the same number of elements, and the corresponding elements on both sides must bind to the same value."

# Prerequisites

- **Atom** — Tuples are conventionally tagged with an atom as their first element to describe what they represent.

# Key Properties

1. A tuple groups a *fixed* number of items.
2. It is written `{Item1, Item2, ...}` — curly brackets, comma-separated.
3. Its fields are anonymous (unnamed), unlike a C struct's fields.
4. By convention the first element is an atom tag describing the tuple.
5. Tuples can contain values of any type and can be nested.
6. They are created automatically and garbage-collected when no longer used.
7. Values are extracted by pattern matching; both sides of `=` must have the same shape.

# Construction / Recognition

## To Create a Tuple:
1. Enclose the elements in `{ }`, separated by commas.
2. Conventionally make the first element an atom tag, e.g. `{point, 10, 45}`.

## To Extract Values:
1. Write a pattern of the same shape with unbound variables, e.g. `{point, X, Y} = Point`.
2. The variables are bound to the corresponding elements.

## To Recognize It:
1. Data enclosed in curly brackets.

# Context & Application

- **Typical contexts**: Representing a record-like group with a fixed field count — points, people, messages.
- **Common applications**: Inter-process messages (`{From, Message}`), status results (`{ok, Value}`, `{error, enoent}`).
- **Historical/stylistic notes**: When the number of fields grows large, records (next chapter) give names to a tuple's elements.

# Examples

**Example 1** (Chapter 3, "Tuples"): `{person, {name, joe}, {height, 1.82}, {footsize, 42}, {eyecolour, brown}}` — a nested tuple where atoms both tag fields and serve as values.

**Example 2** (Chapter 3, "Extracting Values from Tuples"): `{point, X, Y} = Point` matched against `{point, 10, 45}` binds `X` to `10` and `Y` to `45`.

# Relationships

## Builds Upon
- **Atom** — The conventional tuple tag is an atom.

## Enables
- **Record** — Records (later chapter) are tuples whose elements are given names.

## Related
- **Pattern matching** / **the match operator** — How values are put into and taken out of tuples.
- **Term** — A tuple is one kind of compound term.

## Contrasts With
- **List** — A tuple holds a *fixed* number of items; a list holds an *arbitrary* number. The source: "Each of the individual elements in the drawing list are fixed-size tuples ... but the drawing itself can contain an arbitrary number of things and so is represented by a list."

# Common Errors

- **Error**: Matching a tuple pattern against a tuple of a different size.
  **Correction**: Both sides must have the same number of elements, or the match fails.

- **Error**: Leaving a tuple untagged (`{10, 45}`) so its meaning is unclear.
  **Correction**: Tag it with a descriptive atom (`{point, 10, 45}`) — recommended style.

# Common Confusions

- **Confusion**: Thinking a tuple can grow or shrink like a list.
  **Clarification**: A tuple groups a *fixed* number of items; use a list for an arbitrary number.

- **Confusion**: Expecting tuple fields to have names like a struct's.
  **Clarification**: Tuple fields are anonymous; to give them names, use a record.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Tuples," "Creating Tuples," and "Extracting Values from Tuples." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Tuples."
- Confidence rationale: HIGH — tuples are explicitly defined with syntax and worked examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards. Canonical slug `record` referenced for the later-chapter concept.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `tuple` used.
