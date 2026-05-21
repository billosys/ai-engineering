---
concept: Attribute Code
slug: attribute-code
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.1 Attribute code"
extraction_confidence: high
aliases:
  - "attribute code"
  - "code attribution"
  - "don't steal code"
prerequisites: []
extends: []
related:
  - file-header-revision-history
  - reference-specifications-in-code
contrasts_with: []
answers_questions:
  - "How should the origin of code be attributed in a module?"
---

# Quick Definition

Correctly attribute all code in the module header — say where every contributing idea came from, and never present borrowed code as your own.

# Core Definition

"You must always correctly attribute all code in the module header. Say where all ideas contributing to the module came from" (Programming Rules, 8.1). If your code was derived from other code, say where you got it and who wrote it. "Never steal code — stealing code is taking code from some other module editing it and forgetting to say who wrote the original." Useful attribute examples include `-revision(...)`, `-created(...)`, `-created_by(...)`, `-modified(...)`, `-modified_by(...)`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. All code is attributed in the module header.
2. The origin of every contributing idea is stated.
3. Derived code names its source and the original author.
4. Module attributes such as `-created_by`, `-modified_by` record authorship.

# Construction / Recognition

## To Apply

1. In the module header, record where ideas and derived code came from.
2. Use attributes like `-created_by('eklas@erlang')` and `-modified_by(...)`.

## To Recognize a Violation

1. Borrowed or derived code carries no statement of its origin or original author.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: module headers.
- **Common applications**: `-revision`, `-created`, `-created_by`, `-modified`, `-modified_by` attributes.

# Examples

**Example** (from source): attributes `-revision('Revision: 1.14 ')`, `-created('Date: 1995/01/01 11:21:11 ')`, `-created_by('eklas@erlang')`, `-modified(...)`, `-modified_by('mbj@erlang')`.

# Relationships

## Related

- **File headers, revision history** — revision history is the running record of authorship.
- **Provide references in the code to the specifications** — both make a module's provenance explicit.

# Common Errors

- **Error**: Copying code from another module and dropping the original author's credit.
  **Correction**: Attribute it — name the source and who wrote it.

# Common Confusions

- **Confusion**: Thinking attribution is a courtesy.
  **Clarification**: The source frames it as a requirement — unattributed borrowed code is "stealing code".

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.1 "Attribute code".

# Verification Notes

- Definition source: Direct adaptation of section 8.1.
- Confidence rationale: HIGH — the rule is stated explicitly with attribute examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
