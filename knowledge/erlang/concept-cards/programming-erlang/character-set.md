---
# === CORE IDENTIFICATION ===
concept: Character Set
slug: character-set

# === CLASSIFICATION ===
category: core-idioms
subcategory: syntax
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Character Set"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - source encoding
  - UTF-8 source
  - character encoding

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - escape-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What character set does Erlang source code use?"
  - "Does Erlang have a character data type?"
  - "How are strings represented in Erlang?"
---

# Quick Definition

Since Erlang R16B, source files are assumed to be UTF-8 encoded; Erlang has no character data type, and strings are lists of integers.

# Core Definition

"Since Erlang version R16B, Erlang source code files are assumed to be encoded in the UTF-8 character set. Prior to this, the ISO-8859-1 (Latin-1) character set was used. This means all UTF-8 printable characters can be used in source code files without using any escape sequences" ("The Rest of Sequential Erlang", *Character Set*). "Internally Erlang has no character data type. Strings don't really exist but instead are represented by lists of integers. Unicode strings can be represented by lists of integers without any problems."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Erlang source files are UTF-8 encoded as of R16B (previously ISO-8859-1 / Latin-1).
2. All UTF-8 printable characters may appear directly in source — no escape sequences needed.
3. Erlang has no character data type.
4. Strings do not exist as a distinct type — they are lists of integers.
5. Unicode strings are representable as lists of integers without difficulty.

# Construction / Recognition

## To Construct/Create:
1. Write UTF-8 text directly in source files; no special declaration is needed for printable characters.

## To Identify/Recognize:
1. Any Erlang "string" is in fact a list of integer character codes.

# Context & Application

- **Typical contexts**: writing source files and handling text data.
- **Common applications**: representing Unicode text as ordinary integer lists.
- **Historical/stylistic notes**: the move from Latin-1 to UTF-8 source encoding happened at R16B.

# Examples

**Example 1** (*Character Set*): because Erlang has no character type, a "string" such as `"hello"` is a list of integers — the ASCII codes of its characters; Unicode strings are likewise lists of integers.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Escape sequences** — Escape sequences enter characters into strings as integer codes.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting a dedicated character type to manipulate text.
  **Correction**: There is no character type; operate on strings as lists of integer codes.

# Common Confusions

- **Confusion**: Believing Erlang strings are a primitive type.
  **Clarification**: Strings "don't really exist" — they are lists of integers.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Character Set".

# Verification Notes

- Definition source: Direct quotation from *Character Set*.
- Confidence rationale: HIGH — the source explicitly states the source encoding and the list-of-integers representation.
- Uncertainties: None.
- Cross-reference status: Slug `escape-sequences` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
