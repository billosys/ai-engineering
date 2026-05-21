---
concept: Compiling Erlang Code
slug: compiling-erlang-code
category: tooling
subcategory: compiler
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Compiling Code"
extraction_confidence: high
aliases:
  - "erlc"
  - "BEAM"
  - "bytecode compilation"
prerequisites:
  - module
extends: []
related:
  - compiler-options
  - erlang-shell
contrasts_with: []
answers_questions:
  - "How do I create and compile a module?"
---

# Compiling Erlang Code

## Quick Definition

Erlang source code is compiled to bytecode for the BEAM virtual machine, producing a `.beam` file. Compilation can be done from the command line or from inside the shell.

## Core Definition

Erlang code is compiled to bytecode so it can be used by the VM. The compiler can be called from the command line with `erlc flags file.erl`, from code with `compile:file(Filename)`, or from the shell with `c(Module)` (often used during development). A successful compilation produces a `.beam` file next to the `.erl` source — the compiled module. The `.beam` extension stands for Bogdan/Björn's Erlang Abstract Machine, the VM itself (Hébert, ch. 2, "Compiling Code").

## Prerequisites

- **Module** — Compilation operates on a module's `.erl` source file

## Key Properties

1. Source compiles to bytecode for the BEAM VM.
2. `erlc flags file.erl` compiles from the command line.
3. `compile:file(Filename)` compiles from code; `c(Module)` compiles from the shell.
4. A successful compile produces a `Module.beam` file in the working directory.
5. The shell looks for files only in its start directory and the standard library; `cd/1` changes that.
6. `c(Module)` returns `{ok, Module}` on success.

## Construction / Recognition

To compile a module in the shell:

1. Use `cd("/path/to/module/")` to move to the file's directory.
2. Call `c(modulename)`.
3. On success it returns `{ok, modulename}` and writes `modulename.beam`.

## Context & Application

Shell compilation with `c()` is the common workflow during development. Native-code compilation via the `hipe` module is available on some platforms for roughly 20% speedups, used as a last resort for CPU-intensive code.

## Examples

**Example** (ch. 2): `c(useless).` returns `{ok,useless}` and produces `useless.beam`.

**Example** (ch. 2): If the module fails to compile, the shell shows a message like `useless.erl:Line: Some Error Message`.

## Relationships

### Prerequisites

- **Module** — A module's source is the compilation input

### Related

- **Compiler options** — Flags control how compilation is done
- **Erlang shell** — `c()` compiles from within the shell

## Common Errors

- **Error**: Compiling from the wrong directory so the shell cannot find the file
  **Correction**: Use `cd/1` to move to the file's directory first

## Common Confusions

- **Confusion**: Thinking `.beam` is platform-specific native code
  **Clarification**: `.beam` is portable bytecode; only `hipe`-compiled native code is non-portable

## Source Reference

Chapter 2: "Modules," section "Compiling Code."

## Verification Notes

- Definition: Adapted from the "Compiling Code" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
