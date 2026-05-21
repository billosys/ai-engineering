---
concept: Function Export
slug: function-export
category: tooling
subcategory: code-organization
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Creating Modules"
extraction_confidence: high
aliases:
  - "-export"
  - "-import"
  - "arity"
  - "module interface"
prerequisites:
  - module
  - module-attribute
extends:
  - module-attribute
related:
  - compiler-options
contrasts_with: []
answers_questions:
  - "How do I create and compile a module?"
---

# Function Export

## Quick Definition

The `-export` attribute lists which functions of a module can be called from outside it, identified by name and arity. Exported functions form the module's interface.

## Core Definition

The `-export` attribute defines which functions of a module can be called by the outside world. It takes a list of functions with their respective arity, written `-export([Function1/Arity, ..., FunctionN/Arity])`. The *arity* of a function is the integer count of its arguments; functions sharing a name are distinct if and only if they have different arity (e.g., `add/2` vs. `add/3`). Exported functions represent the module's interface and should reveal only the bare minimum necessary. The `-import(Module, [Function/Arity, ...])` attribute imports foreign functions so they can be called unqualified, but its use is generally discouraged for readability (Hébert, ch. 2, "Creating Modules").

## Prerequisites

- **Module** — Exports apply to functions within a module
- **Module attribute** — `-export` and `-import` are module attributes

## Key Properties

1. `-export([Name/Arity, ...])` lists publicly callable functions.
2. Arity is the number of arguments; it is part of a function's identity.
3. `add/2` and `add/3` are different functions.
4. Non-exported functions cannot be called from other modules.
5. `-import(Module, [F/A,...])` lets foreign functions be called unqualified, but is discouraged.
6. An unexported function called externally raises an "undefined function" error.

## Construction / Recognition

To export a function:

1. Determine the function's arity (its argument count).
2. Add `Name/Arity` to the `-export` list attribute.

## Context & Application

A well-designed interface exports only what is necessary, so internal implementation details can change without breaking dependent code. `-import` is usually avoided because it obscures where a function comes from; including the module name aids `grep`-based navigation.

## Examples

**Example** (ch. 2): `-export([add/2, hello/0, greet_and_add_two/1]).` exports the three functions of the `useless` module.

**Example** (ch. 2): Calling `useless:not_a_real_function().` raises `undefined function useless:not_a_real_function/0`.

## Relationships

### Prerequisites

- **Module** — Functions exist in modules
- **Module attribute** — `-export` is an attribute

### Builds Upon

- **Module attribute** — `-export` is a specific module attribute

### Related

- **Compiler options** — `-export_all` overrides `-export` to export everything

## Common Errors

- **Error**: Forgetting to add a new function to `-export`
  **Correction**: Add `Name/Arity` to the export list whenever a function must be callable externally

## Common Confusions

- **Confusion**: Thinking `add/2` and `add/3` are the same function
  **Clarification**: Different arity means different functions

## Source Reference

Chapter 2: "Modules," section "Creating Modules."

## Verification Notes

- Definition: Adapted from the `-export`/`-import` discussion
- Confidence: HIGH — explicit treatment
- Uncertainties: None
