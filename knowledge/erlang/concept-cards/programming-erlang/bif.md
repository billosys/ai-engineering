---
# === CORE IDENTIFICATION ===
concept: BIF
slug: bif

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: built-in-functions
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "BIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - built-in function
  - autoimported function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - module
extends: []
related:
  - guard
  - tuple
  - list
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a BIF?"
  - "How do I convert a list to a tuple or get the current time?"
---

# Quick Definition

A BIF is a built-in function — a function that is part of the Erlang language itself. BIFs do things that are impossible or inefficient to write in plain Erlang, such as converting a list to a tuple or reading the system clock.

# Core Definition

"A *BIF* is a *built-in function*; BIFs are functions that are defined as part of the Erlang language. Some BIFs are implemented in Erlang, but most are implemented as primitive operations in the Erlang virtual machine" (Chapter 4, "BIFs"). "BIFs provide interfaces to the operating system or perform operations that are impossible or very inefficient to program in Erlang. For example, it's impossible to turn a list into a tuple or to find the current time and date. To perform such an operation, we call a BIF." `list_to_tuple/1` converts a list to a tuple; `time/0` returns the current time of day. "All BIFs behave as if they belong to the module `erlang`, though the most common BIFs (such as `list_to_tuple`) are *autoimported*, so we can call `list_to_tuple(...)` instead of `erlang:list_to_tuple(...)`."

# Prerequisites

- **Function** — A BIF is a kind of function; it is called like any function.
- **Module** — BIFs behave as if they belong to the `erlang` module.

# Key Properties

1. A BIF is a function defined as part of the Erlang language.
2. Most BIFs are implemented as primitive operations in the Erlang VM; some in Erlang.
3. BIFs do things impossible or inefficient in plain Erlang (OS interfaces, list-to-tuple, time/date).
4. All BIFs behave as if they belong to the `erlang` module.
5. Common BIFs are *autoimported* and can be called unqualified (`list_to_tuple(...)`).
6. A full list of BIFs is in the `erlang` manual page.

# Construction / Recognition

## To Use a BIF:
1. Call common (autoimported) BIFs by name, e.g. `list_to_tuple([...])`, `time()`.
2. Call others with the `erlang:` prefix, e.g. `erlang:halt()`.

## To Recognize It:
1. A function that is part of the language rather than user-defined — found in the `erlang` manual page.

# Context & Application

- **Typical contexts**: Operations that touch the runtime or OS — type conversion, time/date, process info.
- **Common applications**: `list_to_tuple/1`, `time/0`, `tuple_to_list/1`, `element/2`, `length/1`, `self/0`.
- **Historical/stylistic notes**: Many BIFs (`abs`, `length`, `element`, `self`, `tuple_size`, ...) are also usable inside guards as guard BIFs.

# Examples

**Example 1** (Chapter 4, "BIFs"): `list_to_tuple([12,cat,"hello"])` returns the tuple `{12,cat,"hello"}` — an operation impossible to write in plain Erlang.

**Example 2** (Chapter 4, "BIFs"): `time()` returns the current time of day as a tuple such as `{20,0,3}` (hours, minutes, seconds).

# Relationships

## Builds Upon
- **Function** — A BIF is a function.
- **Module** — BIFs behave as members of the `erlang` module.

## Enables
- Operations on tuples and lists (e.g., `list_to_tuple`, `tuple_to_list`) and access to runtime/OS facilities.

## Related
- **Guard** — A subset of BIFs (guard BIFs) may be used inside guards.
- **Tuple** / **list** — BIFs commonly convert between and operate on these.

## Contrasts With
- No directly contrasting concept; BIFs are simply distinguished from user-defined functions.

# Common Errors

- **Error**: Trying to write a function that turns a list into a tuple in pure Erlang.
  **Correction**: This is impossible in plain Erlang; use the BIF `list_to_tuple/1`.

- **Error**: Assuming every BIF can be called without the `erlang:` prefix.
  **Correction**: Only the common, autoimported BIFs can be called unqualified; others need `erlang:`.

# Common Confusions

- **Confusion**: Thinking BIFs are ordinary library functions.
  **Clarification**: BIFs are part of the language, mostly implemented as VM primitives, not ordinary Erlang code.

- **Confusion**: Believing all BIFs are documented in the book.
  **Clarification**: The book introduces only the BIFs needed for each section; the complete list is in the `erlang` manual page.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "BIFs." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "BIFs."
- Confidence rationale: HIGH — "built-in function" is explicitly defined with examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
