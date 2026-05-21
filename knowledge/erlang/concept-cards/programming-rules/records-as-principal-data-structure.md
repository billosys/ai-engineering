---
concept: Use Records As The Principal Data Structure
slug: records-as-principal-data-structure
category: data-types
subcategory: erlang-specific-conventions
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.1 Use records as the principle data structure"
extraction_confidence: high
aliases:
  - "records as principal data structure"
  - "record"
  - "tagged tuple"
prerequisites: []
extends: []
related:
  - use-record-selectors-and-constructors
  - dont-leak-private-data-structures
  - document-data-structures
contrasts_with: []
answers_questions:
  - "What is a record in Erlang?"
  - "Where should a record definition be placed?"
---

# Quick Definition

Use records — tagged tuples — as the principal data structure, defining them in a `.hrl` header if shared, or at the top of the module if used by one module only.

# Core Definition

"Use records as the principle data structure. A record is a tagged tuple and was introduced in Erlang version 4.3" (Programming Rules, 6.1); it is similar to a struct in C or a record in Pascal. If a record is used in several modules, its definition is placed in a header file (`.hrl`) included by those modules; if used in only one module, it is defined at the beginning of that module's file. Records can ensure cross-module consistency of data structures and should be used by interface functions passing data between modules.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A record is a tagged tuple.
2. Records are the principal data structure for the system.
3. A shared record is defined in a `.hrl` header; a single-module record is defined at the top of that module.
4. Records ensure cross-module consistency and are used by interface functions.

# Construction / Recognition

## To Apply

1. Model structured data as a record.
2. Place a shared record in a `.hrl`; place a module-private one at the top of the module.

## To Recognize a Candidate

1. Structured data is being passed around as a bare untagged tuple.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: any structured data, especially data crossing module boundaries.
- **Common applications**: a `#person{}` record defining `name`, `age`, `phone`, `dict`.

# Examples

The source describes the record concept and placement rules; the concrete `#person{}` example appears in related sections (6.2, 8.7).

# Relationships

## Related

- **Use selectors and constructors** — the proper way to access record instances.
- **Don't allow private data structure to leak out of a module** — records help keep representations internal.
- **Document all the principle data structures in messages** — records are documented data structures.

# Common Errors

- **Error**: Passing structured data as bare tuples.
  **Correction**: Define a record; its tag and named fields make the structure explicit.

# Common Confusions

- **Confusion**: Thinking a record is a distinct runtime type.
  **Clarification**: A record *is* a tagged tuple — the record syntax is compile-time sugar over tuples.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.1 "Use records as the principle data structure".

# Verification Notes

- Definition source: Direct adaptation of section 6.1.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
