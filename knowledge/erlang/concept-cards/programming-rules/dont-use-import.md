---
concept: Don't Use Import
slug: dont-use-import
category: core-idioms
subcategory: erlang-specific-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.6 Don't use import"
extraction_confidence: high
aliases:
  - "no -import"
  - "import directive"
prerequisites: []
extends: []
related:
  - reduce-intermodule-dependencies
  - group-exports-by-purpose
contrasts_with: []
answers_questions:
  - "Why shouldn't I use the -import directive?"
  - "How should I find module dependencies instead?"
---

# Quick Definition

Don't use the `-import` directive — it makes code harder to read because you cannot see which module a function comes from.

# Core Definition

"Don't use `-import`, using it makes the code harder to read since you cannot directly see in what module a function is defined" (Programming Rules, 6.6). To find module dependencies, use `exref` (the Cross Reference Tool) instead.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The `-import` directive is not used.
2. Functions from other modules are called fully qualified, so their origin is visible.
3. `exref` (the Cross Reference Tool) is used to discover module dependencies.

# Construction / Recognition

## To Apply

1. Call external functions as `module:function(...)`.
2. Use `exref` to analyze inter-module dependencies.

## To Recognize a Violation

1. The module contains an `-import(...)` directive.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: any module calling functions from other modules.
- **Common applications**: fully qualified calls plus `exref`-based dependency analysis.

# Examples

The source states the rule directly and recommends `exref`; no code listing is given.

# Relationships

## Related

- **Try to reduce intermodule dependencies** — `exref` is the recommended tool for both.
- **Exporting functions** — both concern keeping module boundaries visible and explicit.

# Common Errors

- **Error**: Importing functions to shorten call sites.
  **Correction**: Keep fully qualified calls; the module prefix shows where each function lives.

# Common Confusions

- **Confusion**: Thinking `-import` aids readability.
  **Clarification**: It hides each function's defining module, making code harder to read and debug.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.6 "Don't use import".

# Verification Notes

- Definition source: Direct adaptation of section 6.6.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
