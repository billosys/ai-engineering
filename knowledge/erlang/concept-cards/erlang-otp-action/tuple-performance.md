---
# === CORE IDENTIFICATION ===
concept: Tuple Read/Update Trade-off
slug: tuple-performance

# === CLASSIFICATION ===
category: performance
subcategory: memory
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.1. Tuples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "tuple performance"
  - "tuple update cost"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
extends: []
related:
  - list-performance
  - referential-transparency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does updating a tuple or record require copying?"
  - "What is the read/update trade-off for tuples?"
  - "How can nesting tuples change the trade-off?"
---

# Quick Definition

Tuples give fast element reads but, being read-only, require copying the whole tuple to update one field — so they trade fast reads against costly updates.

# Core Definition

Tuples are read-only data structures, and updates require copying. Because records are really tuples, updating a field in a record means creating a new tuple: updating a 10-field record writes 12 words of data. On the other hand, picking out fields in a tuple or record is as fast as it can be. This gives a trade-off between fast reads and fast updates. For data that does not change, a huge tuple works as a quick-access array, but updating it is inefficient. By nesting tuples into a tree, accesses go through several indirections and become slower, but updates become less costly — which is how the standard `array` module works (Chapter 14, Section 14.3.1).

# Prerequisites

- **Memory sizes of Erlang data types** — A tuple is "2 words + 1 word per element"; this card explains the update cost that size implies.

# Key Properties

1. Tuples are read-only; any update creates a new tuple.
2. Updating one field copies the whole tuple (e.g. 12 words for a 10-field record).
3. Reading a field from a tuple or record is as fast as possible.
4. A large flat tuple is a fast-access array for unchanging data, but slow to update.
5. Nesting tuples into a tree makes reads slower (more indirections) but updates cheaper.
6. The standard `array` module is built on nested tuples for exactly this trade-off.

# Construction / Recognition

## To Identify/Recognize:
1. If data is read often and rarely changed → a flat tuple gives fast reads.
2. If data is updated often → a nested tuple tree (e.g. the `array` module) reduces per-update copying.

# Context & Application

- **Typical contexts**: Choosing between flat and nested tuple structures for collections.
- **Common applications**: The `array` module uses nested tuples to balance read and update cost.
- **Historical/stylistic notes**: The copy-on-update behaviour is a direct consequence of referential transparency.

# Examples

**Example 1** (Section 14.3.1): Updating a record with 10 fields writes 12 words, because the whole underlying tuple is recreated.

**Example 2** (Section 14.3.1): A huge flat tuple works as a quick-access array but is inefficient to update; nesting tuples trades read speed for cheaper updates.

# Relationships

## Related
- **List performance** — Lists have the opposite profile: cheap head prepend, costly indexed access.
- **Referential transparency** — Tuple immutability and copy-on-update follow from it.

# Common Errors

- **Error**: Using a large flat tuple as a frequently updated array.
  **Correction**: Each update copies the whole tuple; use a nested-tuple structure like the `array` module instead.

# Common Confusions

- **Confusion**: Thinking a tuple field can be updated in place.
  **Clarification**: Tuples are read-only; "updating" a field builds a fresh copy of the tuple.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Tuples."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — the trade-off is explicitly described.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
