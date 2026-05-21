---
concept: Module Names
slug: module-names
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.7 Module names"
extraction_confidence: high
aliases:
  - "module names"
  - "module name prefix"
  - "simulated hierarchical modules"
prerequisites: []
extends: []
related:
  - function-names
  - registered-processes
contrasts_with: []
answers_questions:
  - "How can I simulate a hierarchical module structure in Erlang?"
---

# Quick Definition

Erlang has a flat module namespace; simulate a hierarchical structure by giving sets of related modules a common name prefix.

# Core Definition

"Erlang has a flat module structure (i.e. there are not modules within modules)" (Programming Rules, 7.7). To simulate the effect of a hierarchical module structure, give sets of related modules the same module prefix. For example, an ISDN handler implemented across five related modules would name them `isdn_init`, `isdn_partb`, `isdn_...`, etc.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Erlang's module namespace is flat — no modules within modules.
2. A hierarchy is simulated by a shared name prefix on related modules.
3. The prefix groups a set of modules that belong together.

# Construction / Recognition

## To Apply

1. Choose a common prefix for a set of related modules.
2. Name each module `<prefix>_<role>` (e.g. `isdn_init`).

## To Recognize a Candidate

1. A set of related modules lacks any naming relationship.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: subsystems implemented as several related modules.
- **Common applications**: an ISDN handler's `isdn_init`, `isdn_partb`, etc.

# Examples

**Example** (from source): an ISDN handler implemented in five modules named `isdn_init`, `isdn_partb`, `isdn_...`.

# Relationships

## Related

- **Function names** — companion naming rule.
- **Registered processes** — a registered process takes its module's name, so module naming flows through.

# Common Errors

- **Error**: Naming related modules with no shared prefix.
  **Correction**: Give the related set a common prefix to simulate hierarchy.

# Common Confusions

- **Confusion**: Expecting nested modules.
  **Clarification**: Erlang's module space is flat; a shared prefix is the only "hierarchy" available.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.7 "Module names".

# Verification Notes

- Definition source: Direct adaptation of section 7.7.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
