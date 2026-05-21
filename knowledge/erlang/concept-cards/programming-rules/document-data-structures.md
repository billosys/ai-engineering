---
concept: Document Data Structures
slug: document-data-structures
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.7 Data structures"
extraction_confidence: high
aliases:
  - "document data structures"
  - "record documentation"
prerequisites: []
extends: []
related:
  - records-as-principal-data-structure
  - comment-each-function
contrasts_with: []
answers_questions:
  - "How should a record's definition be documented?"
---

# Quick Definition

Document each record definition together with a plain-text description of its fields, their types, and their default values.

# Core Definition

"The record should be defined together with a plain text description" (Programming Rules, 8.7). The source's example documents a `person` record: a boxed comment names the data type and describes each field — `name` (a string, default `undefined`), `age` (an integer, default `undefined`), `phone` (a list of integers, default `[]`), `dict` (a `{Key, Value}` list, default `[]`) — placed directly above the `-record(person, ...)` definition.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A record definition is accompanied by a plain-text description.
2. The description names the data type.
3. Each field's meaning, type, and default value are described.

# Construction / Recognition

## To Apply

1. Above each `-record` definition, write a boxed comment naming the type and describing every field.

## To Recognize a Violation

1. A `-record` definition has no accompanying field-by-field description.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: every record definition.
- **Common applications**: a `%% Data Type: person` comment block above `-record(person, ...)`.

# Examples

**Example** (from source): a `%% Data Type: person` comment listing `name`, `age`, `phone`, `dict` with types and defaults, above `-record(person, {name, age, phone = [], dict = []})`.

# Relationships

## Related

- **Use records as the principle data structure** — these are the records being documented.
- **Comment each function** — both demand documenting data structures and their meanings.

# Common Errors

- **Error**: Defining a record with no description of its fields.
  **Correction**: Add a plain-text comment describing each field's meaning, type, and default.

# Common Confusions

- **Confusion**: Thinking field names alone document a record.
  **Clarification**: The source asks for meaning, type, and default for each field — not just names.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.7 "Data structures".

# Verification Notes

- Definition source: Direct adaptation of section 8.7.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
