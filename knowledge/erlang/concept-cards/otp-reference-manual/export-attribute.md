---
# === CORE IDENTIFICATION ===
concept: Export Attribute
slug: export-attribute

# === CLASSIFICATION ===
category: api-design
subcategory: module-interface
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
  - "-export"
  - "export declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - function-arity
extends: []
related:
  - import-attribute
  - module-declaration
  - module-info
contrasts_with:
  - import-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make an Erlang function visible outside its module?"
  - "What is the -export attribute?"
  - "How do I specify the public interface of an Erlang module?"
---

# Quick Definition
The `-export(Functions)` attribute specifies which functions defined within a module are visible from outside the module. `Functions` is a list of `Name/Arity` pairs.

# Core Definition
The Erlang Reference Manual states: "`-export(Functions).` -- Exported functions. Specifies which of the functions, defined within the module, are visible from outside the module. `Functions` is a list `[Name1/Arity1, ..., NameN/ArityN]`, where each `NameI` is an atom and `ArityI` an integer." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- Exports are an attribute of a module
- **function-arity** -- Export lists use `Name/Arity` notation

# Key Properties
1. Syntax: `-export([Name1/Arity1, ..., NameN/ArityN]).`
2. Functions not listed in an export attribute are local to the module
3. Multiple `-export` attributes can appear in the same module
4. Only exported functions can be called using fully qualified calls (`Module:Function(Args)`)
5. Local (unexported) functions can only be called from within the same module
6. The export list defines the module's public API

# Construction / Recognition
## To Construct/Create:
1. Write `-export([` followed by a list of `Name/Arity` pairs separated by commas, then `]).`
2. Example: `-export([start/0, stop/1, process/2]).`

## To Identify/Recognize:
1. The `-export(...)` attribute containing a list of `Name/Arity` pairs
2. Functions listed here are callable as `Module:Function(Args)` from other modules

# Context & Application
The export attribute is fundamental to Erlang's encapsulation model. By default, all functions in a module are private (local). Only functions explicitly listed in an `-export` attribute become part of the module's public interface. This supports the design principle of exposing a minimal API while keeping implementation details private. Exported functions are also essential for hot code loading -- a process must make a fully qualified call to an exported function to switch to new code.

# Examples
**Example 1** (Module Syntax section):
```erlang
-module(m).
-export([fact/1]).   % only fact/1 is visible outside

fact(N) when N>0 ->
    N * fact(N-1);
fact(0) ->
    1.
```

**Example 2** (multiple exports):
```erlang
-module(server).
-export([start/0, stop/0]).
-export([call/2, cast/2]).
```

# Relationships
## Builds Upon
- **erlang-module** -- Exports are an attribute of a module
- **function-arity** -- The export list uses Name/Arity notation

## Enables
- **module-info** -- `module_info(exports)` returns the list of exported functions
- **code-replacement** -- Fully qualified calls to exported functions trigger code switching

## Related
- **import-attribute** -- Import is the complement: allowing calls to external functions without module prefix

## Contrasts With
- **import-attribute** -- Export makes local functions visible externally; import makes external functions callable locally without prefix

# Common Errors
- **Error**: Trying to call a function that is not exported from another module
  **Correction**: Add the function to the module's `-export` list

- **Error**: Listing a function with the wrong arity in the export list
  **Correction**: The `Name/Arity` in the export list must exactly match the function's definition

# Common Confusions
- **Confusion**: Thinking all functions are automatically exported
  **Clarification**: In Erlang, functions are private by default. Only functions explicitly listed in `-export` are accessible from other modules.

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
