---
concept: Document All The Principal Data Structures In Messages
slug: document-message-data-structures
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.4 Document all the principle data structures in messages"
extraction_confidence: high
aliases:
  - "document message data structures"
  - "message descriptions"
prerequisites: []
extends: []
related:
  - tag-messages
  - records-as-principal-data-structure
  - required-project-documents
contrasts_with: []
answers_questions:
  - "How should the data structures used in messages be documented?"
---

# Quick Definition

Use tagged tuples as the principal data structure in inter-part messages, and give every such data structure an English description in a Message Descriptions document.

# Core Definition

"Use tagged tuples as the principle data structure when sending messages between different parts of the system" (Programming Rules, 8.4). The record features of Erlang can be used to ensure cross-module consistency of these data structures. An English description of all these data structures should be documented — in the "Message Descriptions" document.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Inter-part messages use tagged tuples as their principal data structure.
2. Records help keep these message data structures consistent across modules.
3. Every message data structure has an English description.
4. The descriptions live in the Message Descriptions document.

# Construction / Recognition

## To Apply

1. Model message payloads as tagged tuples (often records).
2. Describe each in English in the Message Descriptions document.

## To Recognize a Violation

1. A message data structure has no English description in the documentation.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: messages exchanged between different parts of the system.
- **Common applications**: a Message Descriptions document covering every inter-part message.

# Examples

The source states the rule and points to the Message Descriptions document; no code listing is given.

# Relationships

## Related

- **Tag messages** — the tagged-tuple structure this rule documents.
- **Use records as the principle data structure** — records carry the message data structures.
- **Required documents** — the Message Descriptions document is a required project document.

# Common Errors

- **Error**: Defining message structures only in code, with no English description.
  **Correction**: Document each in the Message Descriptions document.

# Common Confusions

- **Confusion**: Thinking the message tuple in code is self-documenting.
  **Clarification**: The source requires a separate English description of each message data structure.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.4 "Document all the principle data structures in messages".

# Verification Notes

- Definition source: Direct adaptation of section 8.4.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
