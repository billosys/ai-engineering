---
# === CORE IDENTIFICATION ===
concept: Intentional Programming
slug: intentional-programming

# === CLASSIFICATION ===
category: api-design
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Idioms"
chapter_number: 24
pdf_page: null
section: "Intentional Programming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - intention-revealing functions

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - adapter-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a function's intent obvious from its name?"
  - "How do I write maintainable Erlang APIs?"
---

# Quick Definition

Intentional programming is a style in which the programmer's intent is obvious from the names of the functions called, rather than having to be inferred by analyzing the surrounding code.

# Core Definition

"Intentional programming is a name given to a style of programming where we can easily see what was intended by the programmer. The intention of the programmer should be obvious from the names of the functions involved and not be inferred by analyzing the structure of the code" ("Intentional Programming"). An overloaded, ambiguous function forces a reader to study the calling context to guess intent; intention-revealing functions name each distinct purpose explicitly so "no guesswork or program analysis is involved."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Function names should make purpose obvious without code analysis.
2. A single overloaded function used for several purposes hides intent.
3. Splitting an overloaded operation into purpose-specific functions makes intent explicit.
4. Code written with intention-revealing functions is easier to understand and maintain.
5. Distinct semantics (e.g., "key must exist" vs. "key may exist") deserve distinct, named functions.

# Construction / Recognition

## To Construct/Create:
1. Identify a function being used for several distinct purposes.
2. Define one named function per purpose, each with semantics that match its name.
3. Replace ambiguous calls with the purpose-specific function.

## To Identify/Recognize:
1. Code where you must read the surrounding `case` or pattern matches to know why a function was called signals a missed intentional-programming opportunity.
2. APIs with separate names for separate intents (`fetch`, `search`, `is_key`) embody the idiom.

# Context & Application

- **Typical contexts**: Library API design and any code intended to be read and maintained by others.
- **Common applications**: Replacing a generic `lookup` with `fetch`, `search`, and `is_key`.
- **Historical/stylistic notes**: The chapter uses the early `dict` library's evolution to illustrate the principle.

# Examples

**Example 1** ("Intentional Programming"): The early `dict` exported `lookup(Key, Dict) -> {ok, Value} | not_found`, which was used in three different ways — data retrieval (`{ok, Value} = lookup(...)`), searching (matching both `{ok, Val}` and `not_found`), and presence testing (matching `{ok, _}` and `not_found`). The reader has to analyze the code to discover which intent applies.

**Example 2** ("Intentional Programming"): `dict` later exported three intention-revealing functions:

```erlang
dict:fetch(Key, Dict)  = Val | EXIT
dict:search(Key, Dict) = {found, Val} | not_found
dict:is_key(Key, Dict) = Boolean
```

`fetch` is for when the key *must* be present (its absence is an error); `search` is for when the key *might* be present; `is_key` tests presence. "These precisely express the intention of the programmer."

# Relationships

## Builds Upon
- This is a foundational style principle; it builds on no other card.

## Enables
- Clearer, more maintainable APIs throughout a codebase.

## Related
- **Adapter pattern** — Both concern designing interfaces that communicate intent.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Overloading one function (e.g., `lookup`) for retrieval, searching, and presence testing.
  **Correction**: Provide a separate, well-named function for each intent.

- **Error**: Using a function whose error behavior does not match the call site's expectation (e.g., `lookup` producing `{badmatch, not_found}`).
  **Correction**: Choose the function whose semantics match — `fetch` when absence is an error, `search` when it is not.

# Common Confusions

- **Confusion**: Believing intentional programming is about comments.
  **Clarification**: It is about function *names and semantics*; the intent should be visible without comments or code analysis.

# Source Reference

Chapter 24: Programming Idioms, Section "Intentional Programming." See the `dict` `lookup` vs. `fetch`/`search`/`is_key` discussion.

# Verification Notes

- Definition source: Direct quote and adaptation from "Intentional Programming."
- Confidence rationale: HIGH — the source explicitly names and defines the style with a detailed worked example.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
