---
# === CORE IDENTIFICATION ===
concept: Module Declaration
slug: module-declaration

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Pre-Defined Module Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-module attribute"
  - "module attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - export-attribute
  - compile-attribute
  - module-version
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare a module in Erlang?"
  - "What is the -module attribute?"
  - "What is the only mandatory module attribute?"
---

# Quick Definition
The module declaration (`-module(Module).`) defines the name of an Erlang module. It is the only mandatory attribute and must be specified first.

# Core Definition
The Erlang Reference Manual states: "`-module(Module).` -- Module declaration, defining the name of the module. The name `Module`, an atom, is to be the same as the file name minus the extension `.erl`. Otherwise code loading does not work as intended." It further notes: "This attribute is to be specified first and is the only mandatory attribute." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- The module declaration is an attribute of a module

# Key Properties
1. Syntax: `-module(Module).` where `Module` is an atom
2. It is the only mandatory module attribute
3. Must be specified first among all module attributes
4. The module name must match the source file name minus the `.erl` extension
5. If the name does not match the file name, code loading will not work correctly

# Construction / Recognition
## To Construct/Create:
1. For a file named `my_module.erl`, write: `-module(my_module).`
2. Place it as the very first attribute in the file (before any other attributes or function declarations)

## To Identify/Recognize:
1. The `-module(...)` attribute at the top of an `.erl` file
2. Contains a single atom argument

# Context & Application
The module declaration is the starting point of every Erlang source file. It establishes the module's identity for the code server, the compiler, and all external references. The strict requirement that the module name match the file name ensures that the code server can locate and load modules by name.

# Examples
**Example 1** (Module Syntax section):
```erlang
-module(m).          % module attribute
-export([fact/1]).   % module attribute

fact(N) when N>0 ->
    N * fact(N-1);
fact(0) ->
    1.
```

# Relationships
## Builds Upon
- **erlang-module** -- Module declaration is the defining attribute of a module

## Enables
- **export-attribute** -- After declaring a module, functions can be exported
- **erlang-compilation** -- The compiler uses the module name to produce the `.beam` file
- **code-server** -- The code server uses the module name to locate and manage code

## Related
- **compile-attribute** -- Another pre-defined module attribute
- **module-version** -- Version attribute supplements the module declaration

## Contrasts With
None.

# Common Errors
- **Error**: Module name does not match the file name
  **Correction**: If the file is `foo.erl`, the declaration must be `-module(foo).`

- **Error**: Placing the module declaration after other attributes
  **Correction**: `-module(...)` must be the first attribute in the file

# Common Confusions
- **Confusion**: Thinking the module declaration is optional
  **Clarification**: It is the only mandatory module attribute; a file without it is not a valid Erlang module

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition with clear mandatory status
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
