---
# === CORE IDENTIFICATION ===
concept: BEAM File
slug: beam-file

# === CLASSIFICATION ===
category: tooling
subcategory: build-and-load
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.5 Compiling and loading modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - .beam file
  - object file
  - compiled module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiling-modules
extends: []
related:
  - beam
  - erlc
  - compiled-module-vs-shell
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a .beam file?"
  - "Why can't you edit a .beam file by hand?"
  - "How does a .beam file differ from a source file?"
---

# Quick Definition

A `.beam` file is the compiled object file of an Erlang module: a compact, ready-to-deploy byte-code representation the runtime can load and execute.

# Core Definition

Compiling a module produces "a corresponding file with the extension `.beam` instead of `.erl`, which contains instructions in a form that the Erlang system can load and execute. This is a more compact and efficient representation of the program than the source code, and it contains everything the system needs to load and run the module" (Chapter 2, section 2.3.5). A source file might require additional files via include declarations; all such files are read at compile time, so the single `.beam` file is "a more definite form for a module," although it cannot be easily read by a human and cannot be edited by hand — you edit the source and recompile. A `.beam` file is also called an *object file*. All the code in a `.beam` file was compiled together at the same time, in the same context (section 2.3.7).

# Prerequisites

- **Compiling and loading modules** — a `.beam` file is the product of compilation.

# Key Properties

1. A `.beam` file is the compiled object file of a module.
2. It is a compact, efficient byte-code representation of the program.
3. It contains everything the system needs to load and run the module.
4. It cannot be easily read by a human and cannot be edited by hand.
5. All code in a `.beam` file was compiled together, in the same context.
6. It is also called an *object file*.

# Construction / Recognition

## To Construct/Create:
1. Compile the module's `.erl` source (via `c(...)` or `erlc`).
2. The compiler writes `<module>.beam`.
3. The runtime loads and executes the `.beam` file.

# Context & Application

- **Typical contexts**: Deploying and running compiled Erlang code.
- **Common applications**: The deployable artifact of every Erlang module.
- **Historical/stylistic notes**: `.beam` files are conventionally kept in an `ebin` subdirectory.

# Examples

**Example 1** (section 2.3.5): After `c(my_module)`, listing the directory with `ls()` shows a new `my_module.beam` alongside the source `my_module.erl`.

**Example 2** (section 2.3.7): A `.beam` file is "an efficient, ready-to-deploy representation of a module"; all its code was compiled together at the same time.

# Relationships

## Builds Upon
- **Compiling and loading modules** — the `.beam` file is the compilation output.

## Enables
- Loading and execution of a module by the runtime.

## Related
- **BEAM** — the emulator that loads and runs `.beam` files.
- **erlc** — the standalone compiler that produces `.beam` files.
- **Compiled module vs. shell** — `.beam` code differs from interpreted shell code.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Editing a `.beam` file directly to change a module.
  **Correction**: `.beam` files cannot be edited by hand; edit the `.erl` source and recompile.

# Common Confusions

- **Confusion**: Thinking a `.beam` file still needs the source's include files at load time.
  **Clarification**: All include files are read at compile time; the single `.beam` file is self-contained for loading and running.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.5 "Compiling and loading modules" and section 2.3.7 "Compiled modules versus evaluation in the shell."

# Verification Notes

- Definition source: Direct adaptation from sections 2.3.5 and 2.3.7.
- Confidence rationale: HIGH — the `.beam` object file is explicitly described.
- Uncertainties: None.
- Cross-reference status: `erlc` and `compiled-module-vs-shell` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
