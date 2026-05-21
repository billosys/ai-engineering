---
# === CORE IDENTIFICATION ===
concept: String
slug: string

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
section: "Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - string literal
  - dollar syntax
  - "$char"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - list
  - integer
related:
  - term
contrasts_with:
  - atom

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a string in Erlang?"
  - "How are strings represented in Erlang?"
---

# Quick Definition

Strictly speaking, Erlang has no string type. A string is represented either as a list of integer Unicode codepoints or as a binary; a double-quoted string literal is just shorthand for that list of integers.

# Core Definition

"Strictly speaking, there are no strings in Erlang. To represent a string in Erlang, we can choose between representing the string as a list of integers or as a binary. ... When a string is represented as a list of integers, each element in the list represents a Unicode codepoint" (Chapter 3, "Strings"). "A string literal is just a sequence of characters enclosed in double quotation marks (`"`)." So `"Hello"` "is just shorthand for the list of integer character codes that represent the individual characters in that string." When the shell prints a list, "it prints it as a string literal if all the integers in the list represent printable characters; otherwise, it prints it in list notation." The "dollar syntax" gives the integer for a character: "`$a` is actually the integer that represents the character a." In Erlang strings must use double quotes; single quotes delimit atoms.

# Prerequisites

- **List** — A string is (by default) a list, so the list type must be understood first.
- **Integer** — The elements of a string-as-list are integer Unicode codepoints.

# Key Properties

1. Erlang has no distinct string type.
2. A string is represented as a list of integer Unicode codepoints, or as a binary.
3. A double-quoted literal (`"Hello"`) is shorthand for a list of character-code integers.
4. The shell prints a list as a string literal only if every integer is a printable character.
5. `$c` "dollar syntax" yields the integer codepoint of character `c` (e.g., `$s` is `115`).
6. Strings must use double quotes; single quotes denote atoms.
7. Special characters can be entered with escapes such as `\x{221e}` for a hex codepoint.

# Construction / Recognition

## To Create a String:
1. Write characters in double quotes, e.g. `"Hello"`.
2. Equivalently, write the list of integer codepoints directly, e.g. `[97,98,99]` for `"abc"`.
3. Use `$c` to obtain a single character's codepoint.

## To Recognize It:
1. Text in double quotes is a string literal.
2. A list of integers that the shell prints back as quoted text is being treated as a string.

# Context & Application

- **Typical contexts**: Text data, filenames, messages.
- **Common applications**: Passed as arguments (`spawn(person, init, ["Joe"])`), printed with `io:format`.
- **Historical/stylistic notes**: Because a string *is* a list, all list operations and `[H|T]` patterns work on strings — e.g., `[H|T] = "cat"` binds `H` to `99` and `T` to `"at"`.

# Examples

**Example 1** (Chapter 3, "Strings"): `[83,117,114,112,114,105,115,101]` is printed by the shell as `"Surprise"` because all the integers are printable characters.

**Example 2** (Chapter 3, "Strings"): `I = $s` binds `I` to `115`; then `[I-32,$u,$r,$p,$r,$i,$s,$e]` produces `"Surprise"`, showing dollar syntax for character codes.

# Relationships

## Builds Upon
- **List** — A string is, by default, a list of integers.
- **Integer** — Each element of that list is an integer codepoint.

## Enables
- All list and pattern-matching operations apply to strings since a string is a list.

## Related
- **Term** — A string is a term (specifically a list term).

## Contrasts With
- **Atom** — A string uses double quotes and is a list of integers; an atom uses single quotes (or no quotes) and is a single constant. They are not interchangeable.

# Common Errors

- **Error**: Using single quotes for a string.
  **Correction**: Strings require double quotes; single quotes create an atom.

- **Error**: Expecting `[1,2,3]` to print as text.
  **Correction**: The shell prints a list as a string only when all integers are printable characters; `1`, `2`, `3` are not, so it prints as a list.

# Common Confusions

- **Confusion**: Believing Erlang has a dedicated string type.
  **Clarification**: It does not — a string is a list of integer codepoints (or a binary).

- **Confusion**: Thinking a list printed as `"abc"` is somehow different from a list of integers.
  **Clarification**: It is the same list; the shell merely *displays* it as text because the integers are printable.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Strings." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Strings."
- Confidence rationale: HIGH — the source explicitly states "there are no strings in Erlang" and explains the list-of-integers representation.
- Uncertainties: Binary representation of strings is only cross-referenced here; the Binaries chapter is out of scope.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
