---
concept: Reduce Intermodule Dependencies
slug: reduce-intermodule-dependencies
category: api-design
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.2 Try to reduce intermodule dependencies"
extraction_confidence: high
aliases:
  - "intermodule dependencies"
  - "module coupling"
  - "acyclic dependency graph"
prerequisites: []
extends: []
related:
  - export-few-functions
  - common-code-into-libraries
  - dont-use-import
contrasts_with: []
answers_questions:
  - "Why should intermodule dependencies be minimized?"
  - "Should a module's dependency graph be a tree or a cyclic graph?"
---

# Quick Definition

Minimize the number of different modules a given module calls, and keep the inter-module calling graph a tree rather than a cyclic graph.

# Core Definition

"A module which calls functions in many different modules will be more difficult to maintain than a module which only calls functions in a few different modules" (Programming Rules, 3.2), because every change to a module interface forces a check of every caller. The rule adds that inter-module calling dependencies should form a tree, not a cyclic graph.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Fewer distinct modules called means fewer places to check on an interface change.
2. Reducing interdependencies simplifies maintenance.
3. The inter-module call graph should be a tree (acyclic), not cyclic.

# Construction / Recognition

## To Apply

1. Limit the set of modules any given module calls into.
2. Arrange dependencies so they flow in one direction (a tree).

## To Recognize a Violation

1. A module calls into many unrelated modules.
2. Modules call each other cyclically.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: overall system module structure.
- **Common applications**: layering modules so calls flow downward only.

# Examples

The source illustrates this with a diagram contrasting an acceptable tree-shaped dependency graph against an unacceptable cyclic one (no code example).

# Relationships

## Related

- **Export as few functions as possible** — a small interface limits how modules can couple.
- **Put commonly used code into libraries** — shared libraries reduce ad-hoc cross-calls.
- **Don't use import** — `exref`/`xref` is recommended for finding module dependencies.

# Common Errors

- **Error**: Letting modules call each other in a cycle.
  **Correction**: Restructure so the dependency graph is a tree.

# Common Confusions

- **Confusion**: Thinking dependency count is harmless if each call works.
  **Clarification**: Each dependency is a maintenance edge — every interface change must be checked across all of them.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.2 "Try to reduce intermodule dependencies".

# Verification Notes

- Definition source: Direct adaptation of section 3.2.
- Confidence rationale: HIGH — the rule is stated explicitly with reasoning and a diagram.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
