---
# === CORE IDENTIFICATION ===
concept: Module
slug: module

# === CLASSIFICATION ===
category: core-idioms
subcategory: code-organization
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Modules Are Where We Store Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-module attribute"
  - module declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
extends: []
related:
  - function
  - export-attribute
  - compiling-modules
  - comment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a module in Erlang?"
  - "How do I write, compile, and run a module?"
---

# Quick Definition

A module is the basic unit of code in Erlang: a file with an `.erl` extension containing a `-module` declaration and a set of functions. It must be compiled before its code can run.

# Core Definition

"Modules are the basic units of code in Erlang. Modules are contained in files with `erl` extensions and must be compiled before the code in the modules can be run. Compiled modules have the extension `beam`" (Chapter 4, "Modules Are Where We Store Code"). "Modules contain functions, and the functions can be run sequentially or in parallel" (Chapter 4 opening). Every module begins with a *module declaration*: "The name of the module in the declaration must be the same as the base name of the file where the module is stored" (Chapter 4, "Modules Are Where We Store Code"). The module name "is technically an atom" and "must start with a small letter" (Chapter 1). To call a function in a module you qualify it with the module name: `geometry:area({rectangle, 10, 5})`. Armstrong's analogy: "Modules in Erlang are like classes in an object-oriented programming language ... and processes are like objects."

# Prerequisites

- **Atom** — A module name is technically an atom and follows atom naming rules (lowercase initial letter).

# Key Properties

1. A module is the basic unit of code; it contains functions.
2. Source files have the `.erl` extension; compiled object files have `.beam`.
3. A module must be compiled before its code can run.
4. The first line is a module declaration, `-module(name).`.
5. The module name must equal the base name of its file and must start with a lowercase letter.
6. A function is called from outside with the qualified form `module:function(...)`.
7. One module can be the code for thousands of processes.

# Construction / Recognition

## To Create a Module:
1. Create a file named `name.erl`.
2. Make its first line `-module(name).` with the name matching the filename.
3. Add an `-export` declaration listing the public functions.
4. Define the functions.
5. Compile it to produce `name.beam`.

## To Recognize It:
1. A `.erl` file whose first line is a `-module(...)` declaration.

# Context & Application

- **Typical contexts**: Every Erlang program — code lives in modules.
- **Common applications**: One module per kind of process or per area of functionality (`geometry`, `shop`, `afile_server`).
- **Historical/stylistic notes**: Modules play the role of classes; processes play the role of objects.

# Examples

**Example 1** (Chapter 4, "Modules Are Where We Store Code"): The `geometry` module — stored in `geometry.erl`, starting with `-module(geometry).` — contains the `area/1` function.

**Example 2** (Chapter 1, "Modeling Concurrency"): `-module(person).` is the first line of `person.erl`; the module name must match the filename and start with a lowercase letter.

# Relationships

## Builds Upon
- **Atom** — The module name is an atom.

## Enables
- **Function** — Functions are defined inside modules.
- **Export attribute** — Declares which of a module's functions are public.
- **Compiling modules** — A module is the thing that gets compiled.

## Related
- **Function** — The contents of a module.
- **Compiling modules** — Turns the module into runnable `.beam` code.
- **Comment** — Module-level commentary documents a module.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Giving the module a name different from its filename.
  **Correction**: The module name must equal the base name of the `.erl` file.

- **Error**: Choosing a module name that collides with a system module.
  **Correction**: Rename the module and delete any stale `.beam`; collisions cause a "sticky directory" error.

# Common Confusions

- **Confusion**: Thinking the module name can start with an uppercase letter.
  **Clarification**: The module name is an atom and must start with a lowercase letter.

- **Confusion**: Believing one module corresponds to one running process.
  **Clarification**: A module is just code; thousands of processes can run the same module, as instances run the same class.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "Modules Are Where We Store Code"; Chapter 1: Introducing Concurrency, "Modeling Concurrency." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Modules Are Where We Store Code," and Chapter 1.
- Confidence rationale: HIGH — modules are explicitly defined with naming and compilation rules.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
