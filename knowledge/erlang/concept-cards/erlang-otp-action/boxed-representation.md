---
# === CORE IDENTIFICATION ===
concept: Boxed Representation
slug: boxed-representation

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
section: "14.3.1. Floats and boxed representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "boxed value"
  - "boxed term"
  - "tagged pointer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
extends: []
related:
  - small-integer-performance
  - bignum-performance
  - list-performance
contrasts_with:
  - small-integer-performance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a boxed representation in the BEAM?"
  - "Why do floats use a boxed representation?"
  - "What gets copied when you pass a boxed value to a function?"
---

# Quick Definition

A boxed representation stores a value that does not fit in one machine word as data on the process heap, referenced by a single tagged pointer word that is what actually gets passed around.

# Core Definition

Values that do not fit in a single machine word use a boxed representation. There is one word containing a tag and a pointer to a location on the process's heap memory where the rest of the data is stored; this tagged-pointer word is all that is copied when the value is passed as an argument or stored in a data structure. The data on the heap begins with another word describing the kind of data and its size, followed by the actual payload. Erlang's 64-bit floats use boxing because they cannot fit in a single word (the BEAM also needs bits for the tag); bignums and tuples are likewise boxed (Chapter 14, Section 14.3.1).

# Prerequisites

- **Memory sizes of Erlang data types** — Boxing explains the multi-word costs in Table 14.1.

# Key Properties

1. Used for values too large to fit in one tagged machine word.
2. A single tagged-pointer word references the boxed data on the process heap.
3. Only the tagged pointer is copied when the value is passed or stored elsewhere.
4. The heap data begins with a header word giving the data's kind and size.
5. Floats (64-bit precision), bignums, and tuples all use boxed representation.
6. A list cell is special: it needs no header word, only two heap words.

# Construction / Recognition

## To Identify/Recognize:
1. If a type's Table 14.1 size is more than one word, it is boxed (e.g. float, bignum, tuple).
2. Small integers and atoms are *not* boxed — they are immediate single-word values.

# Context & Application

- **Typical contexts**: Understanding why passing large terms is still cheap, and why updates copy.
- **Common applications**: Explains why a float passed as an argument copies only one pointer word, not its 64-bit payload.
- **Historical/stylistic notes**: List cells are deliberately exempt from the header word, making lists efficient.

# Examples

**Example 1** (Section 14.3.1, Figure 14.3): A float is stored boxed — a tagged pointer plus a heap header word plus the 64-bit data (two words on 32-bit, one on 64-bit).

**Example 2** (Section 14.3.1): Bignums use boxing too, which is why they need at least three words.

# Relationships

## Related
- **Bignum performance** — Bignums are boxed, hence their 3+ word cost.
- **List performance** — List cells are a boxing special case with no header word.

## Contrasts With
- **Small-integer performance** — Small integers are immediate (unboxed) single-word values.

# Common Errors

- **Error**: Assuming passing a large boxed term copies all its data.
  **Correction**: Only the one-word tagged pointer is copied between functions or into structures.

# Common Confusions

- **Confusion**: Thinking all Erlang terms are boxed.
  **Clarification**: Small integers, atoms, and local pids are immediate single-word values; only larger terms are boxed.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Floats and boxed representations," Figure 14.3.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — boxing is explicitly defined and illustrated.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
