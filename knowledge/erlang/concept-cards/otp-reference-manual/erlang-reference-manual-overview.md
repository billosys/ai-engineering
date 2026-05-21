---
# === CORE IDENTIFICATION ===
concept: Erlang Reference Manual Overview
slug: erlang-reference-manual-overview

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-introduction
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Introduction"
chapter_number: null
pdf_page: null
section: "Purpose"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang language reference"
  - "Erlang ref manual"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - reserved-words
  - erlang-character-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang Reference Manual?"
  - "What terminology conventions does the Erlang reference use?"
---

# Quick Definition

The Erlang Reference Manual describes the Erlang programming language through text and examples rather than formal specification. It focuses on the language itself, not its implementation.

# Core Definition

The Erlang Reference Manual is the official language reference for Erlang/OTP. As stated in the introduction: "The focus of the Erlang reference manual is on the language itself, not the implementation of it. The language constructs are described in text and with examples rather than formally specified." It is not intended as a tutorial, and assumes familiarity with general programming concepts (Erlang Reference Manual, Introduction).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Describes Erlang language constructs through text and examples, not formal specification
2. Focuses on the language, not the implementation
3. Not intended as a tutorial
4. Uses specific terminology: a _sequence_ means one or more items; a _list_ means any number of items (including zero)
5. Implementation details are documented separately in System Principles, Efficiency Guide, and ERTS User's Guide

# Construction / Recognition

## To Identify/Recognize:
1. This is a meta-document describing the structure and purpose of the reference manual itself
2. Look for sections labeled "Introduction" or "Purpose" in the Erlang/OTP documentation

# Context & Application

The reference manual is the authoritative source for Erlang language semantics. It is distinct from tutorials and implementation guides. The terminology conventions (sequence vs. list) are used consistently throughout all chapters.

# Examples

**Example 1** (Introduction, Document Conventions): "A _sequence_ is one or more items. For example, a clause body consists of a sequence of expressions. This means that there must be at least one expression."

**Example 2** (Introduction, Document Conventions): "A _list_ is any number of items. For example, an argument list can consist of zero, one, or more arguments."

# Relationships

## Enables
- **reserved-words** -- The reference manual defines the complete set of reserved words
- **erlang-character-set** -- Defines character set rules for the language

## Related
- **function-declaration** -- Described in the Functions chapter
- **pattern-matching** -- Described in the Pattern Matching chapter

# Common Errors

- **Error**: Confusing "sequence" with "list" when reading the manual
  **Correction**: A sequence requires at least one item; a list can be empty

# Common Confusions

- **Confusion**: Treating the reference manual as a tutorial
  **Clarification**: The manual assumes programming experience and describes language constructs for reference, not for learning from scratch

# Source Reference

Introduction chapter of the Erlang Reference Manual. Sections: Purpose, Prerequisites, Document Conventions, Complete List of BIFs, Reserved Words.

# Verification Notes

- Definition source: Direct from the Introduction section
- Confidence rationale: HIGH -- explicit statement of purpose and conventions in source
- Uncertainties: None
- Cross-reference status: Related slugs are planned for extraction
