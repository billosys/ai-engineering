---
# === CORE IDENTIFICATION ===
concept: Atom
slug: atom

# === CLASSIFICATION ===
category: data-types
subcategory: atoms
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.3 Atoms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - symbol
  - label

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - tuple
  - tagged-tuple
  - comparing-terms
contrasts_with:
  - string
  - variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an atom in Erlang?"
  - "How are atoms written?"
  - "Why should you avoid dynamically generating atoms?"
---

# Quick Definition

An atom is a constant identified only by its characters; two atoms are equal exactly when they have the same character representation. Atoms act as labels, like enum constants.

# Core Definition

"In Erlang, an *atom* is a special kind of string constant that is identified only by the characters in the string, so that two atoms are always considered to be exactly the same if they have the same character representation" (Chapter 2, section 2.2.3). Internally, atoms are stored in a table and referred to by index, so comparing atoms at runtime is comparing two small integers, and each use of an atom takes only one word of memory. Atoms play a role like `enum` constants in Java or C — they are labels — but need no declaration. Normally an atom starts with a lowercase letter and may then contain letters, digits, underscores, and `@`; anything else must be single-quoted. Atoms are limited to 255 characters, and there is a system-wide upper limit of just over a million atoms (1,048,576).

# Prerequisites

- **Erlang term** — an atom is one kind of term.

# Key Properties

1. An atom is identified solely by its characters.
2. Two atoms are equal exactly when their characters match.
3. Atoms are stored in a table; equality compares table indices (small integers).
4. Each atom use takes only one word of memory.
5. An unquoted atom starts with a lowercase letter; otherwise single quotes are needed.
6. Atoms are limited to 255 characters; the system allows just over a million distinct atoms.
7. Atoms are never removed from the table until the system restarts.

# Construction / Recognition

## To Construct/Create:
1. Write a name starting with a lowercase letter (`ok`, `error`, `trap_exit`).
2. Or single-quote any other character sequence (`'Blanks and Capitals'`).
3. No declaration is needed — invent atoms as you go.

# Context & Application

- **Typical contexts**: Labels, status codes, configuration keys, tuple tags.
- **Common applications**: `true`/`false` for Booleans, `ok` for "no interesting value," `undefined` as a placeholder.
- **Historical/stylistic notes**: In Lisp these are called *symbols*. Atoms are more readable and user-friendly than numeric constants.

# Examples

**Example 1** (section 2.2.3): `ok`, `error`, `foo`, `undefined`, `trap_exit` are atoms starting with a lowercase letter.

**Example 2** (section 2.2.3): `'$%#*!'`, `'Blanks and Capitals can be quoted'`, and `'Anything inside single-quotes\n is an atom'` are atoms requiring single quotes.

# Relationships

## Builds Upon
- **Erlang term** — an atom is a term.

## Enables
- **Tagged tuple** — an atom is used as the first element to label a tuple.

## Related
- **Comparing terms** — all atoms come before all tuples and lists in the term ordering.

## Contrasts With
- **String** — a string is a list of character codes; an atom is a single interned label.
- **Variable** — a lowercase-starting name is an atom; an uppercase-starting name is a variable.

# Common Errors

- **Error**: Dynamically generating unique atoms (`'x_4711'`, `'x_4712'`, ...) in a long-running system.
  **Correction**: Atoms are never garbage collected and the table has a ~1M limit; avoid dynamic atom generation.

- **Error**: Using camelCase for atoms.
  **Correction**: Atoms are written in lowercase/snake_case; camelCase atoms are legal but discouraged ("it looks awful").

# Common Confusions

- **Confusion**: Treating atoms as ordinary strings.
  **Clarification**: Atoms are special labels, identified by characters but stored as interned table entries; they are not string data.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.3 "Atoms."

# Verification Notes

- Definition source: Direct adaptation from section 2.2.3.
- Confidence rationale: HIGH — atoms are explicitly defined with their limits and usage.
- Uncertainties: None.
- Cross-reference status: `tagged-tuple` and `variable` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
