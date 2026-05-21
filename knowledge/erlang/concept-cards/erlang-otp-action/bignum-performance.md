---
# === CORE IDENTIFICATION ===
concept: Bignums and Arbitrary-Precision Integers
slug: bignum-performance

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
section: "14.3.1. Bignums"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "bignum"
  - "large integer"
  - "arbitrary-precision integer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - small-integer-performance
  - boxed-representation
extends: []
related:
  - data-type-sizes
contrasts_with:
  - small-integer-performance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bignum?"
  - "When does an Erlang integer become a bignum?"
  - "Why is bignum arithmetic slower than small-integer arithmetic?"
---

# Quick Definition

A bignum is the boxed, multi-word representation an Erlang integer automatically takes when it grows too large to fit in a single machine word; arithmetic on bignums is slower than on small integers.

# Core Definition

In Erlang you can use integers of any size. When they get too large to fit in a single word, the runtime system automatically changes their representation to bignums, which can be of any size up to available memory. Bignums use a boxed representation, which is why they need at least three words. The only visible difference to the programmer is that arithmetic on large integers becomes slower than on small integers. This can be noticeable in a tight loop doing a lot of arithmetic when the input causes many operations on large numbers (Chapter 14, Section 14.3.1).

# Prerequisites

- **Small integers and tagged representation** — A bignum is what an integer becomes once it overflows the immediate range.
- **Boxed representation** — Bignums are boxed, hence their multi-word cost.

# Key Properties

1. A bignum represents an integer too large for a single tagged word.
2. The conversion from small integer to bignum is automatic and invisible.
3. Bignums can be arbitrarily large, up to available memory.
4. They use boxed representation and need 3 or more words.
5. Arithmetic on bignums is slower than on small integers.
6. The slowdown is noticeable in tight arithmetic loops fed large-number input.

# Construction / Recognition

## To Identify/Recognize:
1. Any integer outside the small-integer immediate range is stored as a bignum.

## To Construct/Create (avoiding the cost):
1. If a tight loop is slow on large numbers, rewrite the calculation a different way.
2. Or factor out a large part of the numbers so most operations stay on small integers.

# Context & Application

- **Typical contexts**: Cryptography, hashing, factorials, and other large-number arithmetic.
- **Common applications**: The book suggests restructuring tight arithmetic loops to keep most operations on small integers.
- **Historical/stylistic notes**: Arbitrary-precision integers are a language feature; the cost is purely a performance consideration.

# Examples

**Example 1** (Section 14.3.1): The book notes a tight arithmetic loop can be sped up by rewriting it or factoring out large parts of the numbers so most operations involve only small integers.

# Relationships

## Related
- **Memory sizes of Erlang data types** — Bignums are the "3 words or more" entry in Table 14.1.

## Contrasts With
- **Small integers and tagged representation** — Small integers are immediate, single-word, and fast; bignums are boxed and slower.

# Common Errors

- **Error**: Doing heavy arithmetic on large numbers in a tight loop without considering bignum cost.
  **Correction**: Restructure the computation to keep operations on small integers where possible.

# Common Confusions

- **Confusion**: Thinking you must explicitly request bignums.
  **Clarification**: The runtime switches representation automatically when an integer grows too large.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Bignums."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — bignums are explicitly defined.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
