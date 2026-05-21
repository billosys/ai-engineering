---
# === CORE IDENTIFICATION ===
concept: Small Integers and Tagged Representation
slug: small-integer-performance

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
section: "14.3.1. Small integers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "small integer"
  - "immediate integer"
  - "tagged integer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
extends: []
related:
  - bignum-performance
  - atom-performance
contrasts_with:
  - bignum-performance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are small integers represented in the BEAM?"
  - "What range of integers fits in a single word?"
  - "Why are small integers efficient?"
---

# Quick Definition

A small integer fits in one machine word, with a few bits used as a tag; on a 32-bit machine only 28 bits remain for the value, so integers outside roughly ±134 million become bignums.

# Core Definition

Small integers require only a single word of memory, but the BEAM needs a few bits of that word as a tag, to separate it from other kinds of values. On a 32-bit machine only 28 bits can be used for the value (including the sign bit), so integers between -134,217,728 and +134,217,727 fit in one word; larger integers are stored as bignums. Because the value is held directly in the tagged word (an *immediate* representation), small integers are very efficient (Chapter 14, Section 14.3.1, Figure 14.2).

# Prerequisites

- **Memory sizes of Erlang data types** — Small integers are the 1-word "immediate" entry in Table 14.1.

# Key Properties

1. A small integer occupies exactly one machine word.
2. A few bits of that word are a type tag.
3. On a 32-bit machine, 28 bits remain for the value, including the sign bit.
4. The fitting range on 32-bit is -134,217,728 to +134,217,727.
5. Integers larger than the immediate range automatically become bignums.
6. Because the value is stored directly (immediate, not boxed), small integers are fast.

# Construction / Recognition

## To Identify/Recognize:
1. An integer literal within the ±134-million 32-bit range is a small integer.
2. Anything outside it is a bignum.

# Context & Application

- **Typical contexts**: Loop counters, indices, character codes — heavily used numeric values.
- **Common applications**: Character codes in a string are small integers held directly in list-cell head words.
- **Historical/stylistic notes**: The transition from small integer to bignum is invisible to the programmer apart from a speed change.

# Examples

**Example 1** (Section 14.3.1, Figure 14.2): On a 32-bit machine, only 28 of the 32 bits store the value; integers needing more bits are stored as bignums.

# Relationships

## Related
- **Atom performance** — Atoms are similar: one immediate word, fast comparison.

## Contrasts With
- **Bignum performance** — Bignums are boxed, multi-word, and slower to operate on.

# Common Errors

- **Error**: Assuming all integers cost the same.
  **Correction**: Once a value exceeds the immediate range it becomes a slower, boxed bignum.

# Common Confusions

- **Confusion**: Thinking a 32-bit word gives 32 bits of integer range.
  **Clarification**: A few bits are the tag; only 28 bits hold the value on a 32-bit machine.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Small integers," Figure 14.2.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — the representation and range are explicit.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
