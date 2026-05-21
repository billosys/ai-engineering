---
concept: Don't Allow Private Data Structures To Leak Out Of A Module
slug: dont-leak-private-data-structures
category: api-design
subcategory: sw-engineering-principles
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.11 Don't allow private data structure to \"leak\" out of a module"
extraction_confidence: high
aliases:
  - "data structure leakage"
  - "abstract data type"
  - "information hiding"
prerequisites: []
extends: []
related:
  - export-few-functions
  - use-record-selectors-and-constructors
  - records-as-principal-data-structure
contrasts_with: []
answers_questions:
  - "What does it mean for a private data structure to \"leak\" out of a module?"
  - "How do I keep a module's internal representation hidden?"
---

# Quick Definition

Don't let a module's internal data representation leak to its callers — provide constructors and accessor functions so the representation can change freely.

# Core Definition

A module's internal representation should be hidden behind functions. In the source's `queue` example, exposing the queue as a list forces callers to know it is a list (`NewQ = []`, `length(Queue)`) — which both burdens the caller and freezes the implementation. Adding `new/0` and `len/1` "abstracts out" the details, making the queue an abstract data type. "The practice of abstracting out internal details of the implementation allows us to change the implementation without changing the code of the modules which call the functions" (Programming Rules, 3.11).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Callers never construct or inspect the module's internal representation directly.
2. The module supplies constructors (e.g. `new/0`) and accessors (e.g. `len/1`).
3. With the representation hidden, the implementation can change without touching callers.
4. The result is an abstract data type.

# Construction / Recognition

## To Apply

1. Provide a constructor function instead of letting callers build the representation.
2. Provide accessor functions for every property callers need (length, etc.).

## To Recognize a Violation

1. Caller code builds the structure directly (`NewQ = []`) or inspects it (`length(Queue)`).

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: modules implementing data structures (queues, dictionaries, etc.).
- **Common applications**: a `queue` module exposing `new/0`, `add/2`, `fetch/1`, `len/1`.

# Examples

**Example** (from source): the leaky `queue` requires `NewQ = []` and `length(Queue)`; the abstracted version adds `new/0` and `len/1`, and a faster `{X,Y}` two-list representation can then be swapped in with no caller changes.

# Relationships

## Related

- **Export as few functions as possible** — a small interface is what hides the representation.
- **Use selectors and constructors** — the record-level mechanism for the same hiding.
- **Use records as the principle data structure** — records help keep representations internal.

# Common Errors

- **Error**: Letting callers build or inspect a module's data with raw list/tuple operations.
  **Correction**: Add constructor and accessor functions; keep the representation private.

# Common Confusions

- **Confusion**: Thinking direct access is harmless if it works today.
  **Clarification**: It freezes the representation — any future implementation change breaks every caller that reached in.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.11 "Don't allow private data structure to 'leak' out of a module".

# Verification Notes

- Definition source: Direct adaptation of section 3.11.
- Confidence rationale: HIGH — the rule is stated explicitly with an extended `queue` example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
