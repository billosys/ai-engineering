---
# === CORE IDENTIFICATION ===
concept: BEAM Object Code Format
slug: beam-object-code

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
  - ".beam file"
  - "BEAM file"
  - "BEAM bytecode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-compilation
extends: []
related:
  - code-server
  - erlang-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a .beam file?"
  - "What format does compiled Erlang code use?"
  - "What is the BEAM abstract machine?"
---

# Quick Definition
BEAM is Erlang's abstract machine (virtual machine), and `.beam` files contain the compiled object code that it executes. The compiler can also produce BEAM code as an in-memory binary for direct loading.

# Core Definition
The Erlang Reference Manual states: "The compiler can generate a new file that contains the object code. The current abstract machine, which runs the object code, is called BEAM and therefore the object files get the suffix `.beam`. The compiler can also generate a binary which can be loaded directly." (Compilation and Code Loading, "Compilation" section).

# Prerequisites
- **erlang-compilation** -- BEAM files are the output of compilation

# Key Properties
1. `.beam` is the file extension for compiled Erlang object code
2. BEAM stands for Bogdan/Bjorn's Erlang Abstract Machine
3. The BEAM is the virtual machine that executes the object code
4. Object code can also be generated as an in-memory binary (not written to a file)
5. `.beam` files can be inspected using the `beam_lib` module
6. The code server loads `.beam` files at runtime

# Construction / Recognition
## To Construct/Create:
1. Compile an Erlang module: `erlc my_module.erl` produces `my_module.beam`
2. Or: `compile:file(my_module)` produces `my_module.beam`
3. For in-memory binary: `compile:file(my_module, [binary])` returns `{ok, Module, Binary}`

## To Identify/Recognize:
1. Files with the `.beam` extension
2. Contain compiled Erlang bytecode, not human-readable source

# Context & Application
The BEAM format is central to Erlang's deployment and operation model. All Erlang code must exist as BEAM object code to be executed. The BEAM virtual machine provides the runtime environment for Erlang's concurrency, fault tolerance, and hot code loading features. Understanding BEAM files is important for deployment (shipping `.beam` files rather than source), release building, and using tools like `beam_lib` for introspection.

# Examples
**Example 1** (compilation producing a .beam file):
```text
% erlc hello.erl
% ls hello.beam
hello.beam
```

**Example 2** (inspecting a .beam file):
```erlang
1> beam_lib:version("hello.beam").
{ok, {hello, [...]}}
```

# Relationships
## Builds Upon
- **erlang-compilation** -- BEAM files are produced by compilation

## Enables
- **code-server** -- The code server loads and manages BEAM code
- **code-replacement** -- BEAM code can be replaced at runtime

## Related
- **erlang-module** -- Each module compiles to one `.beam` file

## Contrasts With
None.

# Common Errors
- **Error**: Deploying `.erl` source files instead of `.beam` files
  **Correction**: The BEAM VM executes `.beam` files; deploy compiled object code

- **Error**: Editing `.beam` files directly
  **Correction**: `.beam` files are binary; edit the `.erl` source and recompile

# Common Confusions
- **Confusion**: Thinking BEAM is an interpreter
  **Clarification**: BEAM is a virtual machine that executes compiled bytecode, not an interpreter of source code

# Source Reference
"Compilation and Code Loading" chapter, "Compilation" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit naming and description of BEAM and .beam files
- Uncertainties: The acronym expansion "Bogdan/Bjorn's Erlang Abstract Machine" is common knowledge but not stated in this section
- Cross-reference status: All slugs correspond to planned or existing cards
