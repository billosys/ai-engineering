---
concept: No God Modules
slug: no-god-modules
category: api-design
subcategory: source-code-layout
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "No God modules"
extraction_confidence: high
aliases:
  - "god module"
  - "god object"
  - "single responsibility"
prerequisites: []
extends: []
related:
  - group-functions-logically
  - move-code-to-independent-applications
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "What is a God module, and why is it an anti-pattern?"
  - "What distinguishes a \"God module\" from a well-scoped module?"
---

# Quick Definition

Do not design systems around god modules — modules with a huge number of functions or that deal with many unrelated things.

# Core Definition

"Don't design your system using **god** modules (modules that have a huge number of functions and/or deal with very unrelated things)" (Inaka, "No God modules"). A god module, like a god object, does too much or knows too much; it typically arises through feature accretion until a focused module becomes a 6000-line, 500-function monolith.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A god module has an excessive function count and/or unrelated responsibilities.
2. God modules form gradually by accretion, one related-but-different function at a time.
3. The remedy is one module, one responsibility, done well.
4. It is a PR-rejection rule under Source Code Layout.

# Construction / Recognition

## To Apply

1. Give each module a single, nameable responsibility.
2. When a module accumulates unrelated function families, split it along those families.

## To Recognize a Violation

1. A single module exports operations for multiple unrelated entities (e.g., users *and* posts *and* comments).
2. Function count grows without bound.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: data-access layers, "utils" modules, controller modules.
- **Common applications**: splitting an all-in-one `db` module into per-entity modules.

# Examples

**Example 1** — bad: a `god` module exporting `create_user`, `update_user`, `delete_user`, `create_post`, `update_post`, `delete_post`, `create_comment`, etc. — every DB operation for every entity in one module.

# Relationships

## Related

- **Group functions logically** — both keep a module navigable and comprehensible.
- **Move stuff to independent applications** — extends the same decomposition idea to the application level.
- **Keep functions small** — the function-level analogue of the module-level rule.

# Common Errors

- **Error**: Adding "just one more" function to an already broad module.
  **Correction**: Notice accretion early and split before the module becomes a god module.

# Common Confusions

- **Confusion**: Believing many functions alone makes a god module.
  **Clarification**: The defining trait is *unrelated* responsibilities and/or unbounded size — a focused module with many cohesive functions is fine.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "No God modules".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning paragraph.
- Confidence rationale: HIGH — explicit rule with an extended example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
