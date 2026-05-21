---
concept: Do Not Comment Out Old Code - Remove It
slug: remove-old-code
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.11 Do not comment out old code - remove it"
extraction_confidence: high
aliases:
  - "remove old code"
  - "don't comment out code"
  - "no dead code"
prerequisites: []
extends: []
related:
  - file-header-revision-history
  - use-source-code-control
contrasts_with: []
answers_questions:
  - "What should I do with old code I no longer need?"
---

# Quick Definition

Don't comment out old code — remove it, and note the removal in the revision history.

# Core Definition

"Do not comment out old code - remove it" (Programming Rules, 8.11). Add a comment in the revision history to that effect. The source control system keeps track of the old code, so commenting it out in place is unnecessary.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Obsolete code is deleted, not commented out.
2. The removal is noted in the revision history.
3. The source control system preserves the old code, making in-place retention unnecessary.

# Construction / Recognition

## To Apply

1. Delete code you no longer need.
2. Record the removal in the file's revision history.

## To Recognize a Violation

1. Blocks of old code sit commented out in the source.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: editing existing modules.
- **Common applications**: deleting a superseded function and noting it in the revision history.

# Examples

The source states the rule directly and points to the revision history and source control system; no code listing is given.

# Relationships

## Related

- **File headers, revision history** — where the removal is recorded.
- **Use a source code control system** — the system that preserves the deleted code.

# Common Errors

- **Error**: Commenting out old code "in case it's needed later".
  **Correction**: Delete it; the source control system retains the history.

# Common Confusions

- **Confusion**: Thinking commented-out code is a safety net.
  **Clarification**: It is clutter — version control already preserves the old code safely.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.11 "Do not comment out old code - remove it".

# Verification Notes

- Definition source: Direct adaptation of section 8.11.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
