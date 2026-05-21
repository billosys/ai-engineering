---
concept: Records Go First
slug: records-before-functions
category: data-types
subcategory: records
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Records go first"
extraction_confidence: high
aliases:
  - "records first"
  - "record placement"
prerequisites: []
extends: []
related:
  - types-at-top-of-module
  - group-functions-logically
  - lowercase-record-names
contrasts_with: []
answers_questions:
  - "Where should record definitions go in an Erlang module?"
---

# Quick Definition

Records used within a module must be defined before any function bodies.

# Core Definition

"Records that are used within a module should be defined before any function bodies" (Inaka, "Records go first"). All `-record` definitions appear above the first function, grouped near the top of the module.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Record definitions precede every function body.
2. Records define data types used by multiple functions, so they are module-level, not function-local.
3. Placement mirrors documentation, where `edoc` lists types at the top.
4. It is a PR-rejection rule under Records.

# Construction / Recognition

## To Apply

1. Place all `-record` definitions above the first function.

## To Recognize a Violation

1. A `-record` definition appears below a function body.

# Context & Application

A PR-blocking convention under Records.

- **Typical contexts**: modules defining one or more records.
- **Common applications**: a record block placed below `-export` and the type block.

# Examples

**Example 1** — good: `-record(good, {...})` appears before `good/0`.

**Example 2** — bad: `-record(bad, {...})` appears below `good/0`, just before `bad/0`.

# Relationships

## Related

- **Get your types together** — the same top-down placement rule for types.
- **Group functions logically** — the same module-organization principle for functions.
- **Record names** — companion record rule.

# Common Errors

- **Error**: Defining a record right above the single function that uses it.
  **Correction**: Move it into the module's record block at the top.

# Common Confusions

- **Confusion**: Thinking a record "belongs to" its first-using function.
  **Clarification**: Records define data shared across functions; their placement is module-level.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Records", guideline "Records go first".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
