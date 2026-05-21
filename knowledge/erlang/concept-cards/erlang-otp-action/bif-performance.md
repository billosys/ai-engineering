---
# === CORE IDENTIFICATION ===
concept: Performance of BIFs and Operators
slug: bif-performance

# === CLASSIFICATION ===
category: performance
subcategory: caveats
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.2. Performance of built-in functions and operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "BIF performance"
  - "operator performance"
  - "length/1 cost"
  - "++ and -- operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - list-performance
extends: []
related:
  - atom-performance
  - function-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the performance pitfalls of common BIFs and operators?"
  - "Why is length/1 not a constant-time operation?"
  - "Why prefer tuple_size/byte_size over size/1?"
---

# Quick Definition

Erlang's BIFs and operators are implemented in C and generally fast, but several — `++`, `--`, `length/1`, `list_to_atom/1`, `size/1` — carry performance or clarity pitfalls worth knowing.

# Core Definition

Erlang's operators and BIFs are implemented directly in C as part of the runtime system, which makes them efficient in general; but a few carry caveats. `++` (an alias for `lists:append/2`) must not be used to grow lists on the right side. `--` (an alias for `lists:subtract/2`) runs in quadratic time, going over the left list once per right-side element; for unordered data, sorting and using `ordsets:subtract/2` is far better. `list_to_atom/1` adds entries to the never-collected atom table — prefer `list_to_existing_atom/1`. `length(List)` traverses the whole list to count elements, so it is not constant time. `size/1` works on tuples and binaries, always in constant time, but is ambiguously overloaded; modern code should use `tuple_size/1`, `byte_size/1`, or `bit_size/1` (Chapter 14, Section 14.3.2).

# Prerequisites

- **List cell storage and performance** — Several of these caveats (`++`, `--`, `length/1`) follow from how lists are stored.

# Key Properties

1. BIFs and operators are written in C and generally efficient.
2. `++` is `lists:append/2`; never use it to grow a list on the right side repeatedly.
3. `--` is `lists:subtract/2`; it removes only the first occurrence per right-side element and runs in quadratic time.
4. For unordered subtraction, sort first and use `ordsets:subtract/2`.
5. `list_to_atom/1` populates the never-collected atom table; `list_to_existing_atom/1` is often safer.
6. `length(List)` traverses the list — it is O(n), not O(1).
7. `size/1` is constant time but overloaded over tuples and binaries; `tuple_size/1`, `byte_size/1`, and `bit_size/1` are clearer and help the compiler and Dialyzer.
8. `byte_size/1` on a bitstring rounds up to the smallest whole number of bytes.

# Construction / Recognition

## To Identify/Recognize (and fix):
1. Repeated right-side `++` → restructure to prepend on the left, then reverse.
2. `--` on long lists → sort and use `ordsets:subtract/2`.
3. `length/1` in a hot path assumed O(1) → use pattern matching where possible.
4. `size/1` → replace with `tuple_size/1` or `byte_size/1`/`bit_size/1` to clarify intent.

# Context & Application

- **Typical contexts**: Spotting and removing accidental quadratic or linear costs.
- **Common applications**: The book singles out `++`, `--`, `list_to_atom`, `length`, and `size` as common pitfalls.
- **Historical/stylistic notes**: `size/1`'s overloading is called "unfortunate" because it hides whether a tuple or binary is expected.

# Examples

**Example 1** (Section 14.3.2): `[1,2,3,2,1] -- [2,1,2]` yields `[3,1]` — only the first `1` is removed, both `2`s are removed, order is preserved.

**Example 2** (Section 14.3.2): `length(List)` is compared to C's `strlen` — it must traverse the data to count.

# Relationships

## Related
- **Atom table and atom performance** — Explains the `list_to_atom/1` caveat.
- **Function performance** — Both sections cover common Erlang efficiency caveats.

# Common Errors

- **Error**: Calling `length/1` repeatedly in a loop, assuming it is constant time.
  **Correction**: It is O(n); use pattern matching to check for empty/nonempty lists instead.

- **Error**: Using `--` to subtract from long lists.
  **Correction**: It is quadratic; sort and use `ordsets:subtract/2` when order does not matter.

# Common Confusions

- **Confusion**: Thinking `size/1` means the same thing for tuples and binaries.
  **Clarification**: It counts elements for tuples but bytes for binaries; use the specific `tuple_size`/`byte_size`/`bit_size`.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.2 "Performance of built-in functions and operators."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.2.
- Confidence rationale: HIGH — each caveat is explicitly discussed.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
