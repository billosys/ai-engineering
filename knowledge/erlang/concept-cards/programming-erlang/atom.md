---
# === CORE IDENTIFICATION ===
concept: Atom
slug: atom

# === CLASSIFICATION ===
category: data-types
subcategory: primitive-types
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Atoms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - symbolic constant
  - quoted atom

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - tuple
  - term
contrasts_with:
  - single-assignment-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an atom?"
  - "What is the difference between an atom and a variable?"
---

# Quick Definition

An atom is a constant whose value is just itself — a global symbolic constant. Atoms start with a lowercase letter (or are single-quoted) and are used to represent fixed, named values.

# Core Definition

"In Erlang, atoms are used to represent constant values" (Chapter 3, "Atoms"). They serve the role of enumerated types in C or Java and of symbols in Scheme or Ruby. "Atoms start with lowercase letters, followed by a sequence of alphanumeric characters or the underscore (`_`) or at (`@`) sign, for example, `red`, `december`, `cat`, `meters`, `joe@somehost`, and `a_long_name`." Atoms "can also be quoted with a single quotation mark," which allows atoms starting with uppercase letters or containing non-alphanumeric characters, e.g. `'Monday'`, `'+'`, `'an atom with spaces'`. "In Erlang, atoms are global, and this is achieved without the use of macro definitions or include files." "The value of an atom is just the atom" — entering an atom in the shell prints that atom.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An atom's value is itself.
2. Unquoted atoms start with a lowercase letter, then alphanumerics, `_`, or `@`.
3. Single-quoted atoms may start with uppercase letters or contain spaces and symbols (`'+'`, `'Monday'`).
4. Atoms are global — no include files or macros are needed to share them.
5. `'a'` and `a` denote exactly the same atom.
6. Atoms are interesting only because they are distinct and comparable for equality.
7. Single quotes delimit atoms; double quotes delimit strings — they are not interchangeable.

# Construction / Recognition

## To Write an Atom:
1. For ordinary atoms, write a lowercase initial letter followed by alphanumerics, `_`, or `@`.
2. To start with an uppercase letter or include symbols/spaces, enclose the name in single quotes.

## To Recognize an Atom:
1. A bare lowercase-initial name (e.g., `monday`) is an atom.
2. A single-quoted name (e.g., `'Tuesday'`) is an atom.

# Context & Application

- **Typical contexts**: Status values (`ok`, `error`), tags on tuples, enumerations like days of the week.
- **Common applications**: Tagging tuples — `{point, 10, 45}` uses the atom `point` to say what the tuple is.
- **Historical/stylistic notes**: Atoms replace C's `#define` symbolic constants; the actual "value" is unimportant — only distinctness and equality matter.

# Examples

**Example 1** (Chapter 3, "Atoms"): To represent days of the week, "we'd represent the days using the atoms `monday`, `tuesday`, ...."

**Example 2** (Chapter 3, "Atoms"): `1> hello.` entered in the shell prints `hello` — the value of an atom is just the atom itself.

# Relationships

## Builds Upon
- This is a foundational data type and does not build upon another card in this source.

## Enables
- **Tuple** — Atoms are conventionally used as the first (tag) element of a tuple.

## Related
- **Tuple** — Atoms tag tuples to describe what they represent.
- **Term** — Atoms are one of the primitive kinds of term.

## Contrasts With
- **Single-assignment variable** — An atom starts lowercase and is a constant; a variable starts uppercase and is bound once. Writing `x = 123` (lowercase) is almost certainly a mistake.

# Common Errors

- **Error**: Writing `x = 123` intending a variable.
  **Correction**: `x` is an atom; matching it against `123` fails. Use an uppercase initial letter for a variable.

- **Error**: Using double quotes to write an atom with spaces.
  **Correction**: Atoms use single quotes (`'an atom with spaces'`); double quotes make a string.

# Common Confusions

- **Confusion**: Thinking an atom's value is some hidden number.
  **Clarification**: An atom's value is the atom itself; only its distinctness from other atoms matters.

- **Confusion**: Believing single and double quotes are interchangeable.
  **Clarification**: Single quotes delimit atoms; double quotes delimit string literals — Erlang treats them differently.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Atoms." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Atoms."
- Confidence rationale: HIGH — atoms are explicitly defined with syntax rules and examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
