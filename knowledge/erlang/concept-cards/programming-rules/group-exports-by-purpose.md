---
concept: Group Exports By Purpose
slug: group-exports-by-purpose
category: api-design
subcategory: erlang-specific-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.7 Exporting functions"
extraction_confidence: high
aliases:
  - "exporting functions"
  - "export groupings"
  - "why a function is exported"
prerequisites: []
extends: []
related:
  - export-few-functions
  - comment-conventions
contrasts_with: []
answers_questions:
  - "How should I organize a module's -export declarations?"
  - "Why distinguish the reasons a function is exported?"
---

# Quick Definition

Distinguish *why* each function is exported, and use separate, commented `-export` groupings for user-interface, intermodule, and within-module-only functions.

# Core Definition

"Make a distinction of why a function is exported" (Programming Rules, 6.7). A function may be exported because it is a user interface to the module, because it is an interface function for other modules, or because it is called from `apply`/`spawn` etc. but only from within its own module. Use different `-export` groupings and comment them accordingly.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each export has an identifiable reason: user interface, intermodule interface, or within-module use (`apply`/`spawn`).
2. Exports are split into multiple `-export` declarations by reason.
3. Each grouping carries a comment naming its purpose.

# Construction / Recognition

## To Apply

1. Sort exported functions by why they are exported.
2. Write a separate, commented `-export([...])` for each group.

## To Recognize a Violation

1. All exports are lumped into one undifferentiated `-export` list.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: every module's `-export` section.
- **Common applications**: `%% user interface`, `%% intermodule exports`, and `%% exports for use within module only` groupings.

# Examples

**Example** (from source): three commented groups — `%% user interface` (`help/0`, `start/0`, ...), `%% intermodule exports` (`make_pid/1`, ...), and `%% exports for use within module only` (`init/1`, `info_log_impl/1`).

# Relationships

## Related

- **Export as few functions as possible** — companion rule on shaping the export surface.
- **Comments** — the groupings depend on the comment conventions to label them.

# Common Errors

- **Error**: One flat `-export` list mixing public API with `spawn`-only functions.
  **Correction**: Split into commented groups by export reason.

# Common Confusions

- **Confusion**: Thinking all exported functions are equally "public".
  **Clarification**: Some are exported only so `apply`/`spawn` can reach them from within the module — the grouping makes that intent explicit.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.7 "Exporting functions".

# Verification Notes

- Definition source: Direct adaptation of section 6.7.
- Confidence rationale: HIGH — the rule is stated explicitly with a code example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
