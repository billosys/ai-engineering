---
concept: Document All The Errors
slug: document-all-errors
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.3 Document all the errors"
extraction_confidence: high
aliases:
  - "document errors"
  - "error message documentation"
prerequisites: []
extends: []
related:
  - required-project-documents
  - separate-error-handling-from-normal-code
contrasts_with: []
answers_questions:
  - "How should detected errors be documented?"
---

# Quick Definition

List all errors detected by the system, each with an English description, in a separate Error Messages document.

# Core Definition

"All errors should be listed together with an English description of what they mean in a separate document" (Programming Rules, 8.3) — the "Error Messages" document. By errors the source means errors detected by the system. Where you detect a logical error, call the error logger — `error_logger:error_msg(Format, {Descriptor, Arg1, Arg2, ...})` — and make sure the `{Descriptor, Arg1, ...}` line is added to the error message documents.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. All system-detected errors are listed in a separate Error Messages document.
2. Each error has an English description of what it means.
3. When code detects a logical error, it calls `error_logger:error_msg/2`.
4. Every logged error descriptor is added to the error message documents.

# Construction / Recognition

## To Apply

1. On detecting a logical error, call `error_logger:error_msg(Format, {Descriptor, ...})`.
2. Add the descriptor and an English description to the Error Messages document.

## To Recognize a Violation

1. A detected error is logged but never described in the error documentation.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: error-detection points throughout the system.
- **Common applications**: an `error_logger:error_msg/2` call paired with an Error Messages entry.

# Examples

**Example** (from source): `error_logger:error_msg(Format, {Descriptor, Arg1, Arg2, ....})` — and the matching `{Descriptor, Arg1,...}` line is added to the error documents.

# Relationships

## Related

- **Required documents** — the Error Messages document is one of the required project documents.
- **Separate error handling and normal case code** — documented errors support later diagnosis.

# Common Errors

- **Error**: Logging an error without adding it to the error documentation.
  **Correction**: Every detected error descriptor goes into the Error Messages document.

# Common Confusions

- **Confusion**: Thinking "errors" here means runtime crashes generally.
  **Clarification**: The source means errors *detected by the system* — the ones you deliberately log.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.3 "Document all the errors".

# Verification Notes

- Definition source: Direct adaptation of section 8.3.
- Confidence rationale: HIGH — the rule is stated explicitly with an example call.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
