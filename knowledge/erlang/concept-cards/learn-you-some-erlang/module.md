---
concept: Module
slug: module
category: tooling
subcategory: code-organization
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "What Are Modules?"
extraction_confidence: high
aliases:
  - ".erl file"
prerequisites:
  - atom
extends: []
related:
  - module-attribute
  - function-export
  - compiling-erlang-code
  - circular-dependency
contrasts_with: []
answers_questions:
  - "What is a module?"
  - "How do I create and compile a module?"
---

# Module

## Quick Definition

A module is a group of functions collected in a single file under a single name. All Erlang functions must be defined in modules.

## Core Definition

A module is a bunch of functions grouped together in a single file, under a single name. All functions in Erlang must be defined in modules. Functions in a module are called from other modules using the form `Module:Function(Arguments)`. The BIFs of the `erlang` module are automatically imported and can be called without the module prefix. A module file declares two kinds of things: functions and attributes (metadata). The module name set by the `-module` attribute must match the filename (`.erl` extension), or the module will not compile (Hébert, ch. 2, "What Are Modules?" and "Creating Modules").

## Prerequisites

- **Atom** — The module name in the `-module` attribute is an atom

## Key Properties

1. A module is one file containing a group of functions.
2. All Erlang functions live in modules.
3. Functions are called as `Module:Function(Args)` from outside.
4. The `-module(Name)` attribute names the module and must be the first statement.
5. The module name must match the filename (with `.erl` extension).
6. Comments are single-line, beginning with `%` (conventionally `%%%`, `%%`, or `%`).
7. Erlang has no `return` keyword; the last expression's value is returned.

## Construction / Recognition

To create a module:

1. Open a text editor and write `-module(Name).` as the first line.
2. Save the file as `Name.erl`.
3. Add `-export` attributes and function definitions.
4. Compile the file.

## Context & Application

Modules group functions that deal with similar things — `lists` for list operations, `io`/`file` for input/output. The `erlang` module is an exception (it holds unrelated BIFs); programmers should aim for clean, logical separations rather than `erlang`-like grab-bag modules.

## Examples

**Example** (ch. 2): A minimal valid module is just the single line `-module(useless).`.

**Example** (ch. 2): The `useless` module defines `add/2`, `hello/0`, and `greet_and_add_two/1`, with intra-module calls needing no module prefix.

## Relationships

### Prerequisites

- **Atom** — The module name is an atom

### Related

- **Module attribute** — Modules declare metadata via attributes
- **Function export** — `-export` defines the module's public interface
- **Compiling Erlang code** — A module file must be compiled to bytecode
- **Circular dependency** — Module design should avoid mutual calls between modules

## Common Errors

- **Error**: Module name in `-module` not matching the filename
  **Correction**: Name the file `ModuleName.erl` to match the `-module` attribute

## Common Confusions

- **Confusion**: Expecting a `return` keyword
  **Clarification**: The last expression evaluated is returned automatically

## Source Reference

Chapter 2: "Modules," sections "What Are Modules?" and "Creating Modules."

## Verification Notes

- Definition: Adapted from the opening sections of chapter 2
- Confidence: HIGH — explicit definition
- Uncertainties: None
