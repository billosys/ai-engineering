---
concept: Use Record Selectors And Constructors
slug: use-record-selectors-and-constructors
category: data-types
subcategory: erlang-specific-conventions
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.2 Use selectors and constructors"
extraction_confidence: high
aliases:
  - "record selectors and constructors"
  - "don't match records as tuples"
prerequisites:
  - records-as-principal-data-structure
extends: []
related:
  - dont-leak-private-data-structures
contrasts_with: []
answers_questions:
  - "How should I access the fields of a record?"
  - "Why shouldn't I match a record as a raw tuple?"
---

# Quick Definition

Manage record instances with the record feature's selectors and constructors — never with matching that assumes the record is a plain tuple.

# Core Definition

"Use selectors and constructors provided by the record feature for managing instances of records. Don't use matching that explicitly assumes that the record is a tuple" (Programming Rules, 6.2). Access a field with record matching (`#person{name = Name1} = P`) or the selector syntax (`P#person.name`); do not destructure the record as a positional tuple.

# Prerequisites

- **Use records as the principle data structure** — selectors and constructors presuppose that data is modeled as records.

# Key Properties

1. Record fields are read via record matching or the `Var#record.field` selector.
2. Record instances are built with the `#record{...}` constructor syntax.
3. Matching a record as a positional tuple (`{person, Name, _, _, _}`) is forbidden.
4. Positional tuple matching breaks whenever the record definition changes.

# Construction / Recognition

## To Apply

1. Build instances with `#person{name = "Joe", age = 29}`.
2. Read fields with `#person{name = Name1} = P` or `Name2 = P#person.name`.

## To Recognize a Violation

1. A record is destructured as a raw tuple, e.g. `{person, Name, _Age, _Phone, _Misc} = P`.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: any code reading or building records.
- **Common applications**: field access via record selector syntax.

# Examples

**Example** (from source): the good `demo/0` uses `#person{name = Name1} = P` and `Name2 = P#person.name`; the bad version writes `{person, Name, _Age, _Phone, _Misc} = P` — "Don't do this".

# Relationships

## Builds Upon

- **Use records as the principle data structure** — this rule governs how those records are accessed.

## Related

- **Don't allow private data structure to leak out of a module** — selector/constructor use keeps the tuple shape from leaking.

# Common Errors

- **Error**: Matching a record positionally as a tuple.
  **Correction**: Use record matching or the `#record.field` selector.

# Common Confusions

- **Confusion**: Thinking positional matching is fine since a record is a tuple.
  **Clarification**: It couples code to field order and count — any record change silently breaks it.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.2 "Use selectors and constructors".

# Verification Notes

- Definition source: Direct adaptation of section 6.2.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
