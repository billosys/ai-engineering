---
concept: Place
slug: place
category: memory-model
subcategory: memory-layout
tier: foundational
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Move semantics"
extraction_confidence: high
aliases:
  - "lvalue"
  - "memory place"
  - "memory location"
prerequisites: []
extends: []
related:
  - move-semantics
  - address-sensitivity
  - pinning
contrasts_with: []
answers_questions:
  - "What is a place in Rust's memory model?"
  - "What must I understand before learning about Pin?"
---

# Quick Definition

A place is a chunk of memory with an address where a value can live. References point at places (not values), which is why dereferencing and assigning through a reference works.

# Core Definition

"A place is a chunk of memory (with an address) where a value can live. A reference doesn't really point at a value, it points at a place. That is why `*ref = ...` makes sense: the dereference gives you the place, not a copy of the value. Places are well-known to language implementers but usually implicit in programming languages (they are implicit in Rust). Programmers usually have a good intuition for places, but may not think of them explicitly." (Async Reference, Ch. 2: Pinning, "Move semantics" section)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A place is a chunk of memory with an address
2. A place is where a value can live at runtime
3. References point at places, not at values directly
4. Variables and field accesses evaluate to places
5. Anything that can appear on the left-hand side of an assignment must be a place at runtime (hence the compiler-jargon synonym "lvalue")
6. In Rust, mutability is a property of places
7. Being "frozen" (borrowed) is a property of places
8. Places are implicit in Rust — the language has no explicit `place` keyword or type

# Construction / Recognition

## To Recognize a Place

1. Check if the expression can appear on the left-hand side of an assignment — if so, it denotes a place
2. Variables are places: `a` in `let a = 5;` names a place
3. Field accesses are places: `obj.field` denotes a place
4. Dereferenced references are places: `*ref` gives you the place the reference points to

# Context & Application

The concept of places is foundational for understanding move semantics and pinning in Rust. When data is moved (e.g., `let b = a;`), data transfers from one place to another. Pinning is fundamentally about guaranteeing that an object will remain at its place (its memory address will not change). Without understanding places, the motivation for `Pin` and address sensitivity cannot be properly grasped.

**Typical contexts:**

- Discussing move semantics (data moves from one place to another)
- Understanding why borrowed references prevent moves (references point at places)
- Understanding pinning (pinning guarantees a value stays at its place)

# Examples

**Example 1** (Ch. 2, "Move semantics" section): `*ref = ...` — dereferencing a reference gives you the place, not a copy of the value, which is why assignment through a reference works.

**Example 2** (Ch. 2, "Move semantics" section): `let b = a;` — data is moved from the place identified by `a` to the place identified by `b`. After the assignment, the data exists at `b` but no longer exists at `a`.

**Example 3** (Ch. 2, "Move semantics" section): `let r = &a;` — `r` points at the place `a`, not at the value stored there. This is why the existence of `r` prevents `a` from being moved.

# Relationships

## Builds Upon

- No prerequisites — this is a foundational memory-model concept.

## Enables

- **move-semantics** — Moves are defined in terms of data transferring between places
- **pinning** — Pinning guarantees a value stays at its place
- **address-sensitivity** — Address sensitivity means a type's correctness depends on its place's address

## Related

- **address-sensitivity** — Whether a type depends on its place's address not changing

## Contrasts With

- (none)

# Common Errors

- **Error**: Assuming a reference points at a value and not understanding why `*ref = new_val` modifies the original.
  **Correction**: A reference points at a place. Dereferencing gives the place, and assigning to a place replaces the value stored there.

# Common Confusions

- **Confusion**: Thinking that places and values are the same thing.
  **Clarification**: A place is a location in memory (with an address); a value is the data stored at that location. The same place can hold different values over time, and the same value can be moved between different places.

- **Confusion**: Thinking places are an explicit part of Rust syntax.
  **Clarification**: Places are implicit in Rust. The concept is well-known to language implementers but is not surfaced as a keyword or type in Rust's surface syntax.

# Source Reference

Chapter 2: Pinning, section "Move semantics," paragraphs 1-3.

# Verification Notes

- Definition source: Direct quotation from Ch. 2, "Move semantics" section, paragraph 1
- Key Properties 1-4: Directly stated in source
- Key Properties 5-8: Synthesized from surrounding discussion in same section
- Confidence: HIGH — the source explicitly introduces and defines the concept of places
- Cross-reference status: Slugs `move-semantics`, `pinning`, `address-sensitivity` are planned cards in this extraction batch
- Uncertainties: None
