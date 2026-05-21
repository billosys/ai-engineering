---
# === CORE IDENTIFICATION ===
concept: Referential Transparency
slug: referential-transparency

# === CLASSIFICATION ===
category: core-idioms
subcategory: semantics
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Appendix B"
chapter_number: null
pdf_page: null
section: "B.1-B.3. Lists and referential transparency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "referential transparency"
  - "immutability"
  - "no mutation behind your back"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - single-assignment
  - list
  - list-performance
  - tuple-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is referential transparency?"
  - "What are the advantages of referential transparency?"
  - "Why does referential transparency mean you cannot add to the end of a list?"
---

# Quick Definition

Referential transparency is Erlang's guarantee that once you hold a value and name it, that value never changes behind your back, even if a reference to it is passed elsewhere.

# Core Definition

Referential transparency boils down to this: if you get hold of a value (a *term*) and give it a name (say *X*), you are guaranteed that X remains unchanged no matter what, even if you pass a reference to X to another part of the program. Values kept in variables, or parts of those values, are never changed behind your back. This goes hand in hand with Erlang's single-assignment variables. In Erlang you are never allowed to modify the value of something if it could cause someone else's data to change behind their back; this property holds for *all* data in Erlang (Appendix B, Sections B.1-B.2).

# Prerequisites

This is a foundational semantic concept with no prerequisites within this source.

# Key Properties

1. A named value is guaranteed never to change, even when a reference to it is shared.
2. It applies to all data in Erlang, not just some types.
3. It goes hand in hand with single-assignment variables.
4. It makes programming far less error-prone, especially in large multi-programmer projects.
5. Code that works in one process needs no rewrite when split across processes — there are no covert mutable channels.
6. It lets the runtime do creative things with memory management and multithreading, knowing there are no writes to existing structures.
7. For lists, it forbids appending to the end of an existing list but permits cheap prepending on the left.

# Construction / Recognition

## To Identify/Recognize:
1. If passing a value to another function could never let it observe a later change to that value, the language is referentially transparent.
2. A right-side append to an existing list would violate it — others holding the list would see a new last element appear.

# Context & Application

- **Typical contexts**: Reasoning about Erlang's data model, concurrency, and list design.
- **Common applications**: Justifies why list cells allow cheap left-side growth and why tuples/records copy on update.
- **Historical/stylistic notes**: The book draws an analogy to Java strings being constant for the same reason.

# Examples

**Example 1** (Section B.3): You cannot add an element to the end of an existing list, because anyone holding a reference would discover an extra last element materialized from nowhere.

**Example 2** (Section B.3): Adding to the left is fine — a new cell points to the first cell of the original list, leaving the original undisturbed.

# Relationships

## Related
- **Single-assignment variables** — Referential transparency goes hand in hand with single assignment.
- **Erlang list** — List cells are the elegant solution to growing lists in a referentially transparent system.
- **List cell storage and performance** — Left-side prepend is cheap because the original list is never disturbed.
- **Tuple read/update trade-off** — Tuple copy-on-update follows from referential transparency.

# Common Errors

- **Error**: Trying to append to the end of a list you received as an argument.
  **Correction**: Build the list by prepending on the left (and reverse if needed); right-side growth is not allowed.

# Common Confusions

- **Confusion**: Thinking referential transparency is only a theoretical nicety.
  **Clarification**: It has concrete consequences for stability, scalability, readability, debuggability, and development speed.

# Source Reference

Appendix B: Lists and referential transparency, Sections B.1 "A definition of referential transparency," B.2 "Advantages of referential transparency," and B.3 "What it has to do with lists."

# Verification Notes

- Definition source: Direct adaptation of Appendix B, Sections B.1-B.3.
- Confidence rationale: HIGH — referential transparency is explicitly defined.
- Uncertainties: None.
- Cross-reference status: References Agent 1-owned slugs `single-assignment` and `erlang-list` by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
