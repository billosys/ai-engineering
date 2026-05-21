---
# === CORE IDENTIFICATION ===
concept: Term
slug: term

# === CLASSIFICATION ===
category: data-types
subcategory: type-system-foundations
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Pattern Matching Again"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Erlang term
  - data structure

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - atom
  - integer
  - float
  - tuple
  - list
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a term in Erlang?"
---

# Quick Definition

A term is any Erlang data structure — an integer, float, atom, tuple, list, string, or any combination of them. "Term" is the umbrella word for any value in the language.

# Core Definition

"A *term* is just an Erlang data structure" (Chapter 3, "Pattern Matching Again"). The word covers every value Erlang manipulates: the primitive types (integers, floats, atoms) and the compound types (tuples, lists, and structures nested from them). In pattern matching, a pattern is matched against a term: the source's pattern-matching table is headed "Pattern", "=", and "Term", and shows patterns such as `{X,Y,Z}` matched against terms such as `{222,def,"cat"}`. Because Erlang has no type declarations, any term can be built, passed, sent as a message, and matched against a pattern of the same shape.

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is the general category to which all Erlang values belong.

# Key Properties

1. A term is any Erlang data structure — any value.
2. Primitive terms include integers, floats, and atoms.
3. Compound terms include tuples and lists (and structures nested from them).
4. Strings are terms (they are lists of integers).
5. A pattern is matched against a term during pattern matching.
6. Terms can be built freely — Erlang has no type declarations.
7. Any term can be sent as a message between processes.

# Construction / Recognition

## To Create a Term:
1. Write any literal value (integer, float, atom, string) or compound structure (tuple, list).
2. There is no declaration step — terms are created when written.

## To Recognize It:
1. Anything that is an Erlang value is a term.

# Context & Application

- **Typical contexts**: The vocabulary used to talk generically about Erlang data — in pattern matching, message passing, and BIF descriptions.
- **Common applications**: "Term comparisons" and "convert a list to a term" — the word appears throughout the language documentation.
- **Historical/stylistic notes**: Because every value is a term and Erlang has no type declarations, data structures are created ad hoc and shaped to the problem.

# Examples

**Example 1** (Chapter 3, "Pattern Matching Again"): In the pattern-matching table, `{222,def,"cat"}` is the *term* matched against the pattern `{X,Y,Z}`.

**Example 2** (Chapter 3, "Pattern Matching Again"): `{{abc,12},42,{abc,12}}` is a term — a tuple nesting other tuples — matched against the pattern `{X,Y,X}`.

# Relationships

## Builds Upon
- This is a foundational, umbrella concept and does not build upon another card in this source.

## Enables
- **Pattern matching** — Patterns are matched against terms.

## Related
- **Atom**, **integer**, **float** — Primitive terms.
- **Tuple**, **list** — Compound terms.
- **Pattern matching** — Operates on terms.

## Contrasts With
- No directly contrasting concept; "term" is the universal category.

# Common Errors

- **Error**: Treating "term" as a specific type to declare or check.
  **Correction**: "Term" is the umbrella name for *any* Erlang value, not a particular type.

# Common Confusions

- **Confusion**: Thinking "term" means only simple values like atoms and integers.
  **Clarification**: A term is any data structure, including arbitrarily nested tuples and lists.

- **Confusion**: Believing terms must be declared with a type.
  **Clarification**: Erlang has no type declarations; terms are created freely as written.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Pattern Matching Again." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation from Chapter 3, "Pattern Matching Again" — "A term is just an Erlang data structure."
- Confidence rationale: HIGH — the term is explicitly defined, though briefly.
- Uncertainties: None; the definition is short but unambiguous.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
