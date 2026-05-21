---
concept: No Implicit Functions With Mixer
slug: explicit-mixer-functions
category: tooling
subcategory: tools
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Tools"
chapter_number: null
pdf_page: null
section: "No implicit functions with mixer"
extraction_confidence: high
aliases:
  - "mixer library"
  - "explicit mixin functions"
prerequisites: []
extends: []
related:
  - dont-use-import
contrasts_with: []
answers_questions:
  - "How should I use the mixer library to include functions from another module?"
---

# Quick Definition

When using the `mixer` library, don't implicitly include all of a module's functions — explicitly list every mixed-in function.

# Core Definition

"Don't implicitly include all functions from a module when using the mixer library. Explicitly list all mixed-in functions" (Inaka, "No implicit functions with mixer"). A `-mixin` declaration names each function (with arity) it brings in, rather than pulling in everything a module exports.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `mixer` mix-ins enumerate each included function by name and arity.
2. Implicitly including all of a module's functions is disallowed.
3. An explicit list shows exactly which functions a module gains.
4. It is a PR-rejection rule under Tools.

# Construction / Recognition

## To Apply

1. In a `-mixin` declaration, list every function: `[a_function/3, another_function/2, ...]`.

## To Recognize a Violation

1. A `-mixer([Module])` form pulls in all of `Module`'s functions implicitly.

# Context & Application

A PR-blocking convention under Tools; applies to projects using the `mixer` library.

- **Typical contexts**: modules composing behavior from other modules via `mixer`.
- **Common applications**: an explicit `-mixin([{good, [a_function/3, another_function/2, yet_another_one/2]}])`.

# Examples

**Example 1** — bad: `-mixer([bad])` — implicitly mixes in every function of module `bad`.

**Example 2** — good: `-mixin([{good, [a_function/3, another_function/2, yet_another_one/2]}])` — each function listed explicitly.

# Relationships

## Related

- **Don't import** — both reject implicitly pulling functions into a module's namespace.

# Common Errors

- **Error**: Using `-mixer([Module])` to grab everything a module exports.
  **Correction**: Use `-mixin` with an explicit per-function list.

# Common Confusions

- **Confusion**: Thinking implicit inclusion is a convenient shortcut.
  **Clarification**: It adds an unnecessary layer of indirection, forcing readers to jump between files to learn what a module contains.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Tools", guideline "No implicit functions with mixer".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: `dont-use-import` is a planned card in this extraction.
