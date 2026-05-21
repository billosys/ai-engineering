---
concept: Separate Responsibilities In sumo_db
slug: separate-sumo-db-responsibilities
category: api-design
subcategory: suggestions
tier: advanced
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Separate responsibilities in sumo_db"
extraction_confidence: high
aliases:
  - "sumo_db"
  - "model and repo modules"
prerequisites:
  - no-god-modules
extends: []
related:
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "How should I structure modules when using sumo_db?"
---

# Quick Definition

When using `sumo_db`, give each entity two modules: a model module describing the entity and managing in-memory instances, and a `MODEL_repo` module holding the business-logic operations.

# Core Definition

"When using sumo_db you should separate the responsibilities clearly, creating for each entity: one module (usually called MODELs) to describe the entity and allow administrating instances of the model in memory; one module (usually called MODEL_repo) to handle the various operations that require business logic relating to the entity" (Inaka, "Separate responsibilities in sumo_db").

# Prerequisites

- **No God modules** — this rule is the single-responsibility principle applied to the `sumo_db` entity pattern.

# Key Properties

1. Each entity gets a model module (description + in-memory instance administration).
2. Each entity gets a `MODEL_repo` module (business-logic operations).
3. Splitting the two raises understandability, especially for external callers.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule; it is `sumo_db`-specific.

# Construction / Recognition

## To Apply

1. For each `sumo_db` entity, create a `MODEL` module for the entity description and in-memory instances.
2. Create a separate `MODEL_repo` module for business-logic operations on the entity.

## To Recognize a Candidate

1. A single module mixes a `sumo_db` entity's description with its business-logic operations.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR. It is specific to projects using the `sumo_db` library.

- **Typical contexts**: persistence layers built on `sumo_db`.
- **Common applications**: the source cites `fiar`'s `src/models` directory as an example.

# Examples

**Example 1** (from source): the `fiar` project's `src/models` directory demonstrates the model / `MODEL_repo` split.

# Relationships

## Builds Upon

- **No God modules** — this is single-responsibility applied to the `sumo_db` entity pattern.

## Related

- **Keep functions small** — both yield smaller, more focused modules and functions.

# Common Errors

- **Error**: Putting an entity's description and its business logic in one module.
  **Correction**: Split into `MODEL` and `MODEL_repo` modules.

# Common Confusions

- **Confusion**: Thinking this is a general modeling rule.
  **Clarification**: It is specific to the `sumo_db` library's entity pattern.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Separate responsibilities in sumo_db".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a real-world example link.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
