---
concept: Maintain Existing Style
slug: maintain-existing-style
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Maintain existing style"
extraction_confidence: high
aliases:
  - "consistent style"
  - "respect the local style"
  - "when in Rome"
prerequisites: []
extends: []
related:
  - honor-dry
contrasts_with: []
answers_questions:
  - "What does \"maintain existing style\" mean when editing Erlang modules?"
  - "Should I reformat a module to my own style when editing it?"
---

# Quick Definition

When editing a module written by someone else, stick to the style it was already written in; when a project has an overall style, follow that for new modules too.

# Core Definition

"When editing a module written by someone else, stick to the style in which it was written. If a project has an overall style, stick to that when writing new modules as well" (Inaka, "Maintain existing style"). The guideline subordinates personal stylistic preference to local consistency: the unit of consistency is the module first, then the project.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Consistency within a single module outranks any individual developer's preferred style.
2. A project-wide style, where one exists, governs new modules.
3. It is a PR-rejection rule (a "Convention & Rule"), not merely advice.
4. It applies to layout decisions such as list-element alignment and comma placement.

# Construction / Recognition

## To Apply

1. Before editing, read the surrounding code and identify its formatting conventions.
2. Match new code to those conventions even if they differ from your own habits.
3. For a brand-new module, adopt the project's overall style if one is discernible.

## To Recognize a Violation

1. New lines in a function use a different indentation or comma style than adjacent existing lines.
2. A single module contains two competing layout styles.

# Context & Application

This is a PR-blocking convention. It applies whenever code is modified rather than written from scratch.

- **Typical contexts**: maintenance edits, bug fixes, and feature additions to existing modules.
- **Common applications**: matching list/comma alignment, indentation width, and clause spacing already present in a file.

# Examples

**Example 1** — bad: new list elements are appended in a different layout than the existing entries, producing a module with two comma/alignment styles.

**Example 2** — good: new elements `{elem3, 3}`, `{elem4, 4}`, `{elem5, 5}` each follow the existing leading-comma, one-element-per-line layout already used for `{elem1, 1}` and `{elem2, 2}`.

# Relationships

## Related

- **Honor DRY** — both are "Convention & Rule" entries reviewers may cite to reject a PR.

# Common Errors

- **Error**: Reformatting an existing module to your personal style as part of an unrelated change.
  **Correction**: Keep style edits out of feature/bugfix PRs; match the file you found.

# Common Confusions

- **Confusion**: Believing the "best" style should always win.
  **Clarification**: The guideline's rationale is explicit — a uniformly "ugly to you" module beats one that is "half ugly to you, half ugly to somebody else."

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Maintain existing style".

# Verification Notes

- Definition source: Direct quote from the guideline's blockquote.
- Confidence rationale: HIGH — the source states the rule explicitly with an example and reasoning.
- Uncertainties: None.
- Cross-reference status: `honor-dry` is a planned card in this same extraction.
