---
concept: Export As Few Functions As Possible
slug: export-few-functions
category: api-design
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.1 Export as few functions as possible from a module"
extraction_confidence: high
aliases:
  - "minimize exports"
  - "small module interface"
prerequisites: []
extends: []
related:
  - reduce-intermodule-dependencies
  - group-exports-by-purpose
  - dont-leak-private-data-structures
contrasts_with: []
answers_questions:
  - "Why should a module export as few functions as possible?"
  - "How does the size of a module's export list affect its complexity?"
---

# Quick Definition

Keep a module's export list small — the fewer functions a module exports, the simpler it is to understand and the freer its author is to change its internals.

# Core Definition

A module may contain many functions, but only those in its export list are callable from outside. "Seen from the outside the complexity of a module depends upon the number of functions which are exported" (Programming Rules, 3.1). Modules with a low exported/non-exported ratio are desirable: a user need only understand the exported functions, and the maintainer can freely change the internal structure as long as the external interface is unchanged.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Only functions in the `-export` list are callable from other modules.
2. A module's external complexity is proportional to its number of exported functions.
3. A low exported/non-exported ratio is the goal.
4. A small interface lets the maintainer refactor internals without affecting callers.

# Construction / Recognition

## To Apply

1. Export only the functions that genuinely form the module's external interface.
2. Keep helper functions unexported.

## To Recognize a Violation

1. A module exports dozens of functions, many of which are internal helpers.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: every module's `-export` declaration.
- **Common applications**: exporting one or two entry points and keeping the rest private.

# Examples

The source states the principle without a code example: a module exporting one or two functions is "usually easier to understand than a module which exports dozens of functions."

# Relationships

## Related

- **Try to reduce intermodule dependencies** — a small interface is easier to depend on.
- **Exporting functions** — when you must export, group exports by purpose.
- **Don't allow private data structure to leak out of a module** — both protect encapsulation.

# Common Errors

- **Error**: Exporting internal helper functions for convenience.
  **Correction**: Export only the true interface; keep helpers private.

# Common Confusions

- **Confusion**: Thinking more exports make a module more useful.
  **Clarification**: More exports raise external complexity and freeze more of the implementation as a contract.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.1 "Export as few functions as possible from a module".

# Verification Notes

- Definition source: Direct adaptation of section 3.1.
- Confidence rationale: HIGH — the rule is stated explicitly with reasoning.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
