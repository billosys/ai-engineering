---
# === CORE IDENTIFICATION ===
concept: String
slug: string

# === CLASSIFICATION ===
category: data-types
subcategory: lists
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.6 Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - character list
  - double-quoted string

# === TYPED RELATIONSHIPS ===
prerequisites:
  - list
  - number
extends:
  - list
related:
  - binary
  - erlang-shell
  - pattern-matching
contrasts_with:
  - binary
  - atom

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a string in Erlang?"
  - "How are strings represented?"
  - "Why does the shell sometimes print a list as a string?"
---

# Quick Definition

A string in Erlang is not a separate type — it is simply a list of character codes. A double-quoted string is an alternative way of writing such a list.

# Core Definition

"A double-quoted string in Erlang is merely an alternative way of writing a list of character codes" (Chapter 2, section 2.2.6). For example, `"abcd"` is exactly equivalent to `[97,98,99,100]`, and also to `[$a, $b, $c, $d]` using the `$`-prefix character-code notation. Because strings are lists, every list-processing technique applies to strings. A drawback is that it can be hard to tell whether a list was intended as a string. The Erlang shell tries to maintain the illusion that strings differ from plain lists by checking whether a list contains only printable characters: if so it prints it as a double-quoted string, otherwise as a list of integers.

# Prerequisites

- **List** — a string *is* a list.
- **Number** — the elements of a string are integer character codes.

# Key Properties

1. A string is a list of character (integer) codes — not a distinct type.
2. `"abcd"` equals `[97,98,99,100]` equals `[$a,$b,$c,$d]`.
3. All list operations apply to strings.
4. The empty string `""` equals the empty list `[]`.
5. The shell prints all-printable lists as double-quoted strings, others as integer lists.

# Construction / Recognition

## To Construct/Create:
1. Write characters within double quotes: `"Hello!"`.
2. Or write the equivalent list of character codes directly.
3. Use `$c` notation for individual character codes.

# Context & Application

- **Typical contexts**: Text data, string buffers, text-based protocols.
- **Common applications**: String processing using list functions; matching string prefixes with `++`.
- **Historical/stylistic notes**: The list nature is reflected in library names like `atom_to_list(A)`. For long-term storage of large constant string data, binaries may be preferable.

# Examples

**Example 1** (section 2.2.6): `"abcd"`, `"Hello!"`, `" \t\r\n"`, and `""` are exactly equivalent to `[97,98,99,100]`, `[72,101,108,108,111,33]`, `[32,9,13,10]`, and `[]`.

**Example 2** (section 2.2.6): To force the shell to print the raw integer representation of a list, prepend a zero — `[0 | v(1)]` will not be shown as a string.

# Relationships

## Builds Upon
- **List** — a string is a list of character codes.

## Enables
- String processing via ordinary list-processing techniques.

## Related
- **Binary** — strings can be embedded in binary syntax; binaries store large string data more compactly.
- **Erlang shell** — the shell heuristically prints printable lists as strings.

## Contrasts With
- **Binary** — a string is a linked list of code points; a binary is a contiguous byte sequence.
- **Atom** — an atom is a single interned label; a string is a list of characters.

# Common Errors

- **Error**: Assuming a list of numbers is meant as integers when the shell prints it as a string.
  **Correction**: The shell prints any all-printable list as a string; prepend `0` to see the raw list.

# Common Confusions

- **Confusion**: Believing Erlang has a dedicated string type.
  **Clarification**: A string is just a list of character codes; there is no separate string type.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.6 "Strings," including the "Strings and the shell" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.2.6.
- Confidence rationale: HIGH — the list-of-character-codes definition is explicit.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
