---
# === CORE IDENTIFICATION ===
concept: Erlang Compilation
slug: erlang-compilation

# === CLASSIFICATION ===
category: core-idioms
subcategory: code-loading
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Compilation and Code Loading"
chapter_number: null
pdf_page: null
section: "Compilation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compiling Erlang"
  - "erlc"
  - "compile module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - beam-object-code
  - code-server
  - compile-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compile an Erlang module?"
  - "What tools are available for compiling Erlang code?"
  - "What is erlc?"
---

# Quick Definition
Erlang programs must be compiled to object code before execution. The compiler produces `.beam` files (or in-memory binaries) and can be accessed through the `compile` module, the Erlang shell (`c/1`), or the `erlc` command-line tool.

# Core Definition
The Erlang Reference Manual states: "Erlang programs must be _compiled_ to object code. The compiler can generate a new file that contains the object code. The current abstract machine, which runs the object code, is called BEAM and therefore the object files get the suffix `.beam`. The compiler can also generate a binary which can be loaded directly." The compiler is accessed through: `compile:file(Module)` or `compile:file(Module, Options)`. "The Erlang shell understands the command `c(Module)`, which both compiles and loads `Module`." The `erlc` program is also available from the OS shell. (Compilation and Code Loading, "Compilation" section).

# Prerequisites
- **erlang-module** -- Compilation operates on modules

# Key Properties
1. The compiler produces `.beam` files or in-memory binaries
2. Three primary interfaces: `compile:file/1,2`, shell `c/1`, and `erlc` from the OS
3. The shell's `c(Module)` compiles and loads the module in one step
4. `erlc` accepts flags for macros (`-D`), include paths (`-I`), and other options
5. The `erl` executable can also compile with `-compile` or `-make` flags
6. The `make` module provides Make-like build functionality

# Construction / Recognition
## To Construct/Create:
1. From the Erlang shell: `c(my_module).`
2. Programmatically: `compile:file(my_module).` or `compile:file(my_module, [debug_info]).`
3. From the OS shell: `erlc my_module.erl` or `erlc -Ddebug my_module.erl`
4. Batch from OS: `erl -compile Module1 Module2`

## To Identify/Recognize:
1. The presence of `.beam` files alongside `.erl` source files
2. Compiler invocations through any of the above interfaces

# Context & Application
Compilation is the mandatory first step before Erlang code can be executed. The BEAM virtual machine cannot execute source code directly. Understanding the compilation workflow is essential for development, deployment, and debugging. The ability to compile and load from the shell (`c/1`) is a key part of Erlang's interactive development experience.

# Examples
**Example 1** (Compilation section):
```erlang
compile:file(Module)
compile:file(Module, Options)
```

**Example 2** (Compilation section, from OS prompt):
```text
% erl -compile Module1...ModuleN
% erl -make
```

**Example 3** (Compilation section, using erlc):
```text
% erlc <flags> File1.erl...FileN.erl
```

# Relationships
## Builds Upon
- **erlang-module** -- Modules are the unit of compilation

## Enables
- **beam-object-code** -- Compilation produces BEAM object code
- **code-server** -- Compiled code is loaded by the code server

## Related
- **compile-attribute** -- In-source compiler options

## Contrasts With
None.

# Common Errors
- **Error**: Trying to run an `.erl` file directly
  **Correction**: Erlang source files must be compiled to `.beam` before execution (or use `c(Module)` in the shell to compile and load)

- **Error**: Compiling a module whose `-module` name does not match the file name
  **Correction**: Ensure the module declaration matches the file name for code loading to work

# Common Confusions
- **Confusion**: Thinking `c(Module)` only compiles
  **Clarification**: `c(Module)` both compiles and loads the module into the running system

# Source Reference
"Compilation and Code Loading" chapter, "Compilation" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit description of compilation tools and methods
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
