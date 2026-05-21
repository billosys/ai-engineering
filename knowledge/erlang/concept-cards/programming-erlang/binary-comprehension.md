---
# === CORE IDENTIFICATION ===
concept: Binary Comprehension
slug: binary-comprehension

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: comprehensions
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Binaries and the Bit Syntax"
chapter_number: 7
pdf_page: null
section: "Bitstrings: Processing Bit-Level Data"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - bit comprehension
  - bitstring comprehension

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
  - bit-syntax
extends: []
related:
  - bitstring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary comprehension?"
  - "How do I extract the bits of a byte?"
---

# Quick Definition

A binary (bit) comprehension is to binaries what a list comprehension is to lists: it iterates over a binary or bitstring and produces a list or a binary.

# Core Definition

The book introduces the construct while extracting the individual bits of a byte: "Bit comprehensions are to binaries what list comprehensions are to lists. List comprehensions iterate over lists and return lists. Bit comprehensions iterate over binaries and produce lists or binaries" ("Binaries and the Bit Syntax", *Bitstrings: Processing Bit-Level Data*). A generator uses the `<=` operator with a bit syntax pattern, e.g. `<<X:1>> <= B` iterates over `B` one bit at a time. The result form can be a list (`[ X || ... ]`) or a binary (`<< <<X>> || ... >>`). The full syntax is not given in the book; it refers the reader to the Erlang Reference Manual.

# Prerequisites

- **Binary** — Bit comprehensions iterate over binaries.
- **Bit syntax** — The generator pattern and the result expression both use bit syntax.

# Key Properties

1. Analogous to list comprehensions but operating over binaries/bitstrings.
2. The generator uses `<=` with a bit syntax pattern, e.g. `<<X:1>> <= B`.
3. The result can be a list, written `[ Expr || Generator ]`.
4. The result can be a binary, written `<< Expr || Generator >>`.
5. The generator pattern controls how many bits are consumed per step.

# Construction / Recognition

## To Construct/Create:
1. To produce a list of bits: `[ X || <<X:1>> <= B ]`.
2. To produce a binary of bits: `<< <<X>> || <<X:1>> <= B >>`.

## To Identify/Recognize:
1. A comprehension whose generator uses `<=` (not `<-`) is a bit comprehension.

# Context & Application

- **Typical contexts**: bit-level processing — splitting data into individual bits or repacking it.
- **Common applications**: extracting the eight bits of a byte into a list or a binary.
- **Historical/stylistic notes**: more examples appear in the paper "Bit-Level Binaries and Generalized Comprehensions in Erlang."

# Examples

**Example 1** (*Bitstrings: Processing Bit-Level Data*): extracting the bits of a byte:

```erlang
1> B = <<16#5f>>.
<<"_">>
2> [ X || <<X:1>> <= B].
[0,1,0,1,1,1,1,1]
3> << <<X>> || <<X:1>> <= B >>.
<<0,1,0,1,1,1,1,1>>
```

Line 2 produces a list of the byte's bits; line 3 produces a binary from the same bits.

# Relationships

## Builds Upon
- This builds on binaries and the bit syntax.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Bitstring** — Bit comprehensions iterate over bitstrings as well as binaries.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Using `<-` instead of `<=` in a bit comprehension generator.
  **Correction**: List generators use `<-`; binary/bit generators use `<=`.

# Common Confusions

- **Confusion**: Thinking a bit comprehension can only produce a list.
  **Clarification**: Wrapping the body in `<< ... >>` produces a binary instead of a list.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", section "Bitstrings: Processing Bit-Level Data".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Bitstrings: Processing Bit-Level Data*.
- Confidence rationale: MEDIUM — the source explains the idea and gives a worked example but explicitly does not describe the full syntax (it defers to the Reference Manual).
- Uncertainties: Full grammar of bit comprehensions (filters, multiple generators) is not in the source.
- Cross-reference status: Slug `binary` exists; `bit-syntax`, `bitstring` extracted in scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
