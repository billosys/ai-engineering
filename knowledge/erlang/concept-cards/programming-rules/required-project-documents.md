---
concept: Required Project Documents
slug: required-project-documents
category: documentation
subcategory: required-documents
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Required Documents"
chapter_number: 10
pdf_page: null
section: "10 Required Documents"
extraction_confidence: high
aliases:
  - "required documents"
  - "system level documents"
  - "module descriptions"
  - "message descriptions"
prerequisites: []
extends: []
related:
  - comment-each-function
  - document-message-data-structures
  - document-all-errors
  - registered-processes
contrasts_with: []
answers_questions:
  - "What system-level documents are required for an Erlang project?"
---

# Quick Definition

The system-level documents a project must maintain: Module Descriptions, Message Descriptions, a Process document, and Error Messages.

# Core Definition

Section 10 of the Programming Rules describes the system-level documents necessary for designing and maintaining an Erlang system: **Module Descriptions** — one chapter per module, describing each module and all its exported functions (argument meanings and data structures, return value meaning and structure, purpose, and possible causes of failure and exit signals from `exit/1`); **Message Descriptions** — the format of all inter-process messages except those internal to a single module; **Process** — descriptions of all registered servers and their interfaces and purpose, plus the dynamic processes and their interfaces; **Error Messages** — descriptions of error messages.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Module Descriptions: one chapter per module, covering each exported function's arguments, return value, purpose, and failure modes.
2. Message Descriptions: the format of all inter-process messages not internal to one module.
3. Process: descriptions of all registered servers and the dynamic processes, with their interfaces and purposes.
4. Error Messages: descriptions of the system's error messages.

# Construction / Recognition

## To Apply

1. Maintain the four documents as the project's system-level documentation.

## To Recognize a Violation

1. A project lacks one or more of the four required documents.

# Context & Application

The document's required-documents specification (section 10).

- **Typical contexts**: system design and maintenance documentation.
- **Common applications**: a documentation set with Module, Message, Process, and Error sections.

# Examples

The source lists the four documents and their contents; for each it notes "Format of document to be defined later", so the contents — not a fixed format — are the specification.

# Relationships

## Related

- **Comment each function** — Module Descriptions document the same per-function facts at system level.
- **Document all the principle data structures in messages** — produces the Message Descriptions document.
- **Document all the errors** — produces the Error Messages document.
- **Registered processes** — the Process document describes the registered servers.

# Common Errors

- **Error**: Relying only on in-code comments with no system-level documents.
  **Correction**: Maintain the four required documents alongside the code.

# Common Confusions

- **Confusion**: Expecting a fixed template for each document.
  **Clarification**: The source leaves each document's format "to be defined later" — it specifies the required *content*, not a layout.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 10 "Required Documents" (subsections 10.1-10.4).

# Verification Notes

- Definition source: Direct adaptation of section 10 and its four subsections.
- Confidence rationale: HIGH — the documents and their required contents are listed explicitly.
- Uncertainties: The source defers each document's format ("to be defined later").
- Cross-reference status: all referenced slugs are cards in this extraction.
