---
# === CORE IDENTIFICATION ===
concept: List Cell Storage and Performance
slug: list-performance

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
section: "14.3.1. Lists"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "list cell"
  - "cons cell"
  - "list performance"
  - "string memory usage"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
  - boxed-representation
extends: []
related:
  - tuple-performance
  - binary-performance
  - referential-transparency
contrasts_with:
  - tuple-performance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a list cell stored in memory?"
  - "Why does a list cell need no header word?"
  - "How much memory does a string use?"
---

# Quick Definition

A list cell is two heap words — element and pointer-to-rest — with no header word, because a special tag on the referencing word marks it as a list cell.

# Core Definition

List cells are a bit like two-element tuples, but with an important implementation difference: the first word (the tag and pointer to the heap) carries a special tag meaning "list cell." Because list cells always have exactly two elements, no additional type or size information is needed; so whereas a two-element tuple has a header word on the heap, a list cell needs none — it consists of exactly two heap words and nothing more. This makes Erlang's lists efficient as a general data structure. For a string, where each element is a small integer character code, the head word of each cell holds the whole element, so a string uses exactly two words per character (Chapter 14, Section 14.3.1).

# Prerequisites

- **Memory sizes of Erlang data types** — A list is "1 word + 2 words per element."
- **Boxed representation** — A list cell is a special case of boxing with no header word.

# Key Properties

1. A list cell is like a two-element tuple: an element and a pointer to the rest.
2. The referencing word has a special tag meaning "list cell."
3. Because cells always have two elements, no header word is needed.
4. A list cell is exactly two heap words — fewer than a two-element tuple.
5. This makes lists efficient as a general-purpose data structure.
6. A string uses exactly two words per character (the head word holds the small-integer code).
7. Storing text as character-code lists uses far more memory than binaries — converting can shrink it 8x (16x on 64-bit).

# Construction / Recognition

## To Identify/Recognize:
1. Each `[H|T]` cell is two heap words; the list value itself is a tagged pointer.
2. Estimate a list's footprint as 1 word plus 2 words per element.

# Context & Application

- **Typical contexts**: Choosing list vs. binary representation for sequences and text.
- **Common applications**: Short temporary strings as lists are fine; large stored text should be binaries.
- **Historical/stylistic notes**: The no-header-word design is the reason adding to the left of a list is so cheap.

# Examples

**Example 1** (Section 14.3.1): A list cell needs only two heap words, whereas a two-element tuple also needs a header word.

**Example 2** (Section 14.3.1 sidebar): A relatively short temporary string (under ~10,000 characters) as a list is generally fine; storing large text as character lists wastes memory versus binaries.

# Relationships

## Related
- **Binary performance** — Binaries are the compact alternative for large text.
- **Referential transparency** — List cells are the elegant solution to growing lists transparently.

## Contrasts With
- **Tuple read/update trade-off** — A two-element tuple needs a header word; a list cell does not.

# Common Errors

- **Error**: Storing large amounts of text as lists of character codes.
  **Correction**: Use binaries for stored text — two words per character is wasteful at scale.

# Common Confusions

- **Confusion**: Thinking a list cell costs the same as a two-element tuple.
  **Clarification**: A list cell saves the header word — two heap words instead of three.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Lists," including the "Memory usage for strings" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — list-cell storage is explicitly described.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
