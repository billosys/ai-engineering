---
concept: Provide References In The Code To The Specifications
slug: reference-specifications-in-code
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.2 Provide references in the code to the specifications"
extraction_confidence: high
aliases:
  - "reference specifications"
  - "cross-reference documents in code"
prerequisites: []
extends: []
related:
  - attribute-code
  - comment-each-function
contrasts_with: []
answers_questions:
  - "How should code reference the specifications it implements?"
---

# Quick Definition

Provide cross-references in the code to any documents relevant to understanding it — with exact document and page references.

# Core Definition

"Provide cross references in the code to any documents relevant to the understanding of the code" (Programming Rules, 8.2). For example, if the code implements a communication protocol or a hardware interface, give an exact reference — document and page number — to the documents used to write the code.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Code carries cross-references to relevant specification documents.
2. References are exact — document identifier and page number.
3. This applies especially to protocol and hardware-interface code.

# Construction / Recognition

## To Apply

1. In comments, cite the exact document and page that a piece of code implements.

## To Recognize a Violation

1. Protocol or hardware-interface code names no specification, or cites it only vaguely.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: code implementing protocols, hardware interfaces, or formal specifications.
- **Common applications**: a comment citing the protocol document and page a function implements.

# Examples

The source describes the rule (exact document and page references for protocol/hardware code); no code listing is given.

# Relationships

## Related

- **Attribute code** — both record where a module's content originates.
- **Comment each function** — function comments are a natural place for such references.

# Common Errors

- **Error**: Implementing a protocol with no reference to its specification.
  **Correction**: Cite the exact document and page in the code.

# Common Confusions

- **Confusion**: Thinking a general mention of "the spec" suffices.
  **Clarification**: The source asks for *exact* document and page references.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.2 "Provide references in the code to the specifications".

# Verification Notes

- Definition source: Direct adaptation of section 8.2.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
