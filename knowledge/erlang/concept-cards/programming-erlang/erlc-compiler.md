---
# === CORE IDENTIFICATION ===
concept: erlc Compiler
slug: erlc-compiler

# === CLASSIFICATION ===
category: tooling
subcategory: build
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Compiling and Running Your Program"
chapter_number: 10
pdf_page: null
section: "Compile and Run from the Command Prompt"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erlc"
  - "command-line compiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiling-modules
extends:
  - compiling-modules
related:
  - erlang-makefile
  - running-erlang-programs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is erlc?"
  - "How do I compile an Erlang module from the OS command line?"
  - "How do makefiles invoke the Erlang compiler?"
---

# Quick Definition

`erlc` is the Erlang command-line compiler. It compiles `.erl` source files to `.beam` object code directly from the OS prompt, without starting an Erlang runtime.

# Core Definition

"Compiling a program can be done directly from the command prompt. This is the easiest way to do things if you just want to compile some code but not run it" (Armstrong, "Compiling and Running Your Program," "Compile and Run from the Command Prompt"). The command `erlc hello.erl` "compiles the file `hello.erl`, producing an object code file called `hello.beam`." `erlc` is invoked from a properly configured OS shell and is the compiler that makefiles use to build Erlang modules.

# Prerequisites

- **Compiling modules** — `erlc` is one way to perform module compilation; the general concept of compiling `.erl` to `.beam` comes first.

# Key Properties

1. A standalone OS command, not a shell function.
2. `erlc Module.erl` compiles to `Module.beam` without launching a runtime.
3. The `-W` flag controls warnings (e.g. `erlc -W $<` in makefile rules).
4. Used as the compile step in makefile `.erl.beam:` suffix rules.
5. Availability depends on a correctly configured OS shell (system-specific setup).

# Construction / Recognition

## To Construct/Create:
1. Open a shell where `erlc` is on the PATH.
2. Run `erlc Module.erl` (optionally with flags such as `-W`).
3. Confirm `Module.beam` was produced.

## To Identify/Recognize:
1. `erlc` invocations appear at the OS prompt or inside makefile rules.
2. A `.erl.beam:` makefile rule whose body is `erlc -W $<` is the standard erlc compile rule.

# Context & Application

- **Typical contexts**: Batch compilation; build automation via `make`; compiling without entering the shell.
- **Common applications**: Compiling a module before launching it with `erl -noshell -s Mod ...`; makefile-driven builds.
- **Historical/stylistic notes**: The book notes that exact shell setup for `erl`/`erlc` is system-specific and documented on the Erlang website.

# Examples

**Example 1** ("Compile and Run from the Command Prompt"): `erlc hello.erl` followed by `erl -noshell -s hello start -s init stop` compiles then runs the program.

**Example 2** ("Programs with Command-Line Arguments"): `erlc fac1.erl` then `erl -noshell -s fac1 main 25` compiles and runs the factorial program.

**Example 3** ("A Makefile Template"): The suffix rule `.erl.beam:` with body `erlc -W $<` uses `erlc` to build each module listed in `MODS`.

# Relationships

## Builds Upon
- **Compiling modules** — `erlc` is the command-line realization of module compilation.

## Enables
- **Erlang makefile** — Makefile rules call `erlc` to compile each module.

## Related
- **Running Erlang programs** — `erlc` produces the `.beam` files that `erl -s` then runs.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting `erlc` to also run the program.
  **Correction**: `erlc` only compiles; use `erl -s ...` (or an escript) to run.

- **Error**: Running `erlc` in a shell where it is not on the PATH.
  **Correction**: Configure the OS shell so `erl`/`erlc` are directly executable (system-specific).

# Common Confusions

- **Confusion**: Confusing `erlc` (compiler) with `erl` (runtime/shell).
  **Clarification**: `erlc` compiles `.erl` to `.beam`; `erl` starts the runtime that loads and executes `.beam` files.

- **Confusion**: Thinking `erlc` and the shell's `c/1` are unrelated.
  **Clarification**: Both perform module compilation; `erlc` runs at the OS prompt, `c/1` runs inside the shell.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Compile and Run from the Command Prompt" and "A Makefile Template." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `erlc` usage in the named sections.
- Confidence rationale: HIGH — `erlc` and its behavior are shown explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
