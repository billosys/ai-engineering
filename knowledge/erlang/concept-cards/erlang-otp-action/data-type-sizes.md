---
# === CORE IDENTIFICATION ===
concept: Memory Sizes of Erlang Data Types
slug: data-type-sizes

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
section: "14.3.1. Performance aspects of the primitive data types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "data type sizes"
  - "machine words"
  - "term sizes"

# === TYPED RELATIONSHIPS ===
prerequisites:
extends: []
related:
  - boxed-representation
  - small-integer-performance
  - tuple-performance
  - list-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How much memory do Erlang data types use?"
  - "What is a machine word in the BEAM?"
  - "How big is a tuple or list in memory?"
---

# Quick Definition

In the BEAM, the sizes of Erlang data types are counted in machine words — 4 bytes on a 32-bit machine, 8 on a 64-bit machine — and each type has a characteristic word cost.

# Core Definition

Sizes of data types in Erlang are counted in machine words, because of the way the BEAM emulator works. On a 32-bit machine a word is 4 bytes; on a 64-bit machine it is 8 bytes. Table 14.1 lists the primitive sizes: a small integer is 1 word; a large integer (bignum) is 3 or more words; a float is 4 words on 32-bit, 3 on 64-bit; an atom is 1 word (the name string is stored once per node); a binary or bitstring is 3-6 words plus the data size divided by word size; a local pid/port/reference is 1 word (5 for a remote one); a fun is 9-13 words plus 1 word per captured variable; a tuple is 2 words plus 1 word per element; a list is 1 word plus 2 words per element (Chapter 14, Section 14.3.1, Table 14.1).

# Prerequisites

- **Erlang data types** — The card quantifies the memory cost of the language's primitive types.

# Key Properties

1. All sizes are counted in machine words: 4 bytes (32-bit) or 8 bytes (64-bit).
2. Small integer: 1 word; bignum: 3+ words.
3. Float: 4 words (32-bit), 3 words (64-bit).
4. Atom: 1 word per occurrence; the name string is stored once per node.
5. Binary/bitstring: 3-6 words + (data size / word size).
6. Pid/port/reference: 1 word local, 5 words remote.
7. Fun: 9-13 words + 1 word per captured variable.
8. Tuple: 2 words + 1 word per element. List: 1 word + 2 words per element.

# Construction / Recognition

## To Identify/Recognize:
1. To estimate a term's footprint, sum the per-type word costs from Table 14.1.
2. Multiply word counts by 4 or 8 bytes depending on the architecture.

# Context & Application

- **Typical contexts**: Estimating memory use and choosing data representations.
- **Common applications**: The book uses these figures to explain why updating a record copies a whole tuple, and why strings cost two words per character.
- **Historical/stylistic notes**: For this discussion funs behave like tuples with metadata, and pids behave like integers.

# Examples

**Example 1** (Section 14.3.1): A tuple of 10 fields (a record) needs 12 words; updating it writes all 12.

**Example 2** (Section 14.3.1 sidebar): A string uses exactly two words per character, because each list cell's head word holds the small-integer character code.

# Relationships

## Related
- **Boxed representation** — Floats, bignums, and tuples use boxing, which the sizes reflect.
- **Small-integer performance** — Small integers fit in one tagged word.
- **Tuple performance** — Tuple update cost follows from the 2+N word size.
- **List performance** — List storage follows from the 1+2N word size.

# Common Errors

- **Error**: Assuming a 64-bit build is always more memory-efficient.
  **Correction**: Words are larger on 64-bit; per-word data types take twice the bytes.

# Common Confusions

- **Confusion**: Thinking each use of an atom stores its name.
  **Clarification**: Each occurrence is 1 word; the name string is stored once per node in the atom table.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Performance aspects of the primitive data types," Table 14.1.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1 and Table 14.1.
- Confidence rationale: HIGH — the sizes are explicitly tabulated.
- Uncertainties: Exact figures are implementation-specific to the book's era of BEAM.
- Cross-reference status: References Agent 1-owned slug `erlang-data-types` by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
