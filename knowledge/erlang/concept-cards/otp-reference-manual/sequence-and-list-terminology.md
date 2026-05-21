---
# === CORE IDENTIFICATION ===
concept: Sequence and List Terminology
slug: sequence-and-list-terminology

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-conventions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Introduction"
chapter_number: null
pdf_page: null
section: "Document Conventions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-reference-manual-overview
  - function-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does 'sequence' mean in the Erlang Reference Manual?"
  - "What does 'list' mean in the Erlang Reference Manual documentation conventions?"
  - "What is the difference between a sequence and a list in the Erlang manual?"
---

# Quick Definition

In the Erlang Reference Manual's terminology, a _sequence_ means one or more items (at least one required), while a _list_ means any number of items including zero.

# Core Definition

The Erlang Reference Manual establishes two key documentation terms: "A _sequence_ is one or more items. For example, a clause body consists of a sequence of expressions. This means that there must be at least one expression." and "A _list_ is any number of items. For example, an argument list can consist of zero, one, or more arguments." (Erlang Reference Manual, Introduction, "Document Conventions").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A _sequence_ requires at least one item -- it cannot be empty
2. A _list_ can contain zero, one, or more items -- it can be empty
3. These are documentation conventions, not data type definitions
4. Example of sequence usage: clause bodies are sequences of expressions (must have at least one)
5. Example of list usage: argument lists can have zero or more arguments

# Construction / Recognition

## To Identify/Recognize:
1. When the manual says "sequence of X", it means there must be at least one X
2. When the manual says "list of X" or "X list", it means there can be zero or more X items
3. These terms appear throughout the reference manual in syntax descriptions

# Context & Application

These conventions are critical for correctly reading the Erlang Reference Manual's syntax descriptions. When the manual states that a function body is a "sequence of expressions," this means you cannot have an empty function body. When it says "argument list," the function may take zero arguments.

# Examples

**Example 1** (Introduction, Document Conventions): "a clause body consists of a sequence of expressions. This means that there must be at least one expression."

**Example 2** (Introduction, Document Conventions): "an argument list can consist of zero, one, or more arguments."

# Relationships

## Enables
- **function-declaration** -- Function clauses use these conventions: clause body is a sequence, argument list is a list

## Related
- **erlang-reference-manual-overview** -- These conventions are part of the manual's introduction

# Common Errors

- **Error**: Writing an empty clause body expecting it to be valid
  **Correction**: A clause body is a _sequence_ and must contain at least one expression

# Common Confusions

- **Confusion**: Confusing the documentation term "list" with the Erlang data type `list`
  **Clarification**: The term "list" in the Document Conventions section refers to a documentation convention (zero or more items), not the Erlang data type

# Source Reference

Introduction chapter of the Erlang Reference Manual, section "Document Conventions."

# Verification Notes

- Definition source: Direct quotes from the Document Conventions section
- Confidence rationale: HIGH -- explicit definitions with examples provided in source
- Uncertainties: None
- Cross-reference status: Verified against planned extraction slugs
