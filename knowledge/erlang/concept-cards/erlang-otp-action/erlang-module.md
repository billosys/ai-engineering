---
# === CORE IDENTIFICATION ===
concept: Erlang Module
slug: erlang-module

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3 Modules and functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - module
  - module declaration
  - export declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
  - erlang-function
extends: []
related:
  - compiling-modules
  - remote-call
  - function-arity
  - erlang-comment
contrasts_with:
  - compiled-module-vs-shell

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang module?"
  - "What must the first declaration in a module be?"
  - "What does the export declaration do?"
---

# Quick Definition

A module is the container for Erlang program code. Each module has a unique name (an atom), a module declaration, and an export declaration listing the functions visible from outside.

# Core Definition

"To give your code some structure in life and a place to call home, Erlang has *modules*, which are containers for program code. Each module has a unique name, which is specified as an atom" (Chapter 2, section 2.3). A module is written in a source file named after the module with the `.erl` suffix. The first item in a module, apart from comments, must be the *module declaration* `-module(Name).` — *declarations* begin with a hyphen and end with a period. The module name must match the file name. The *export declaration* `-export([...]).` tells the compiler which functions (each given as `name/arity`) are visible from outside; functions not listed stay internal to the module. Erlang's standard library is itself a large collection of predefined modules, such as `lists`.

# Prerequisites

- **Atom** — a module name is an atom.
- **Erlang function** — modules contain function definitions.

# Key Properties

1. A module is a container for program code with a unique atom name.
2. It lives in a source file named `<module>.erl`.
3. The first non-comment item must be `-module(Name).`.
4. Declarations begin with a hyphen and end with a period.
5. The module name must match the file name (apart from `.erl`).
6. `-export([name/arity, ...]).` lists the functions visible from outside.
7. Unexported functions are internal to the module.

# Construction / Recognition

## To Construct/Create:
1. Create a source file `my_module.erl`.
2. Write `-module(my_module).` as the first declaration.
3. Add `-export([...]).` listing functions as `name/arity`.
4. Write the function definitions.

# Context & Application

- **Typical contexts**: All real Erlang programs (as opposed to shell snippets).
- **Common applications**: Grouping related functions; defining a public API via the export list.
- **Historical/stylistic notes**: The standard library `erlang` module is central to the whole system; `lists`, `io`, `dict`, `array` are other common modules.

# Examples

**Example 1** (Listing 2.1, `my_module.erl`): A module with a comment, `-module(my_module).`, `-export([pie/0]).`, and the function `pie() -> 3.14.`.

**Example 2** (section 2.3.4): The export list entry `pie/0` states both the name and arity (0) needed to identify the function.

# Relationships

## Builds Upon
- **Atom** — the module name is an atom.
- **Erlang function** — modules house functions.

## Enables
- **Remote call** — calling a module's exported functions from elsewhere.
- **Compiling modules** — modules are compiled to `.beam` files.

## Related
- **Function arity** — export entries and function identity include arity.
- **Erlang comment** — modules contain `%`-introduced comments.

## Contrasts With
- **Compiled module vs. shell** — declarations like `-module` and `-export` are only valid in a module, not in the shell.

# Common Errors

- **Error**: Naming the source file differently from the module.
  **Correction**: The file name must match the module name (plus `.erl`).

- **Error**: Forgetting to add a function to the export list, then failing to call it.
  **Correction**: Only exported functions are callable from outside; add `name/arity` to `-export`.

# Common Confusions

- **Confusion**: Believing module declarations can be used in the shell.
  **Clarification**: There is no module context in the shell; `-module` and `-export` are only valid inside a module source file.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3 "Modules and functions" and section 2.3.4 "Creating modules." See Listing 2.1.

# Verification Notes

- Definition source: Direct adaptation from sections 2.3 and 2.3.4.
- Confidence rationale: HIGH — modules, module declarations, and export declarations are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `compiling-modules`, `compiled-module-vs-shell`, `erlang-comment` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
