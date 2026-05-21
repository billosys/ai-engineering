---
# === CORE IDENTIFICATION ===
concept: Erlang Makefile
slug: erlang-makefile

# === CLASSIFICATION ===
category: tooling
subcategory: build
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Compiling and Running Your Program"
chapter_number: 10
pdf_page: null
section: "Automating Compilation with Makefiles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "makefile"
  - "make for Erlang"
  - "build automation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlc-compiler
extends: []
related:
  - compiling-modules
  - running-erlang-programs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I automate compiling Erlang code?"
  - "What does an Erlang makefile look like?"
  - "What is a makefile target?"
---

# Quick Definition

An Erlang makefile automates compiling (and running) Erlang modules with the `make` utility. It lists the modules to build, defines suffix rules that call `erlc`, and provides named targets such as `all`, `compile`, and `clean`.

# Core Definition

`make` is "the utility for automating my work — I use it for compiling and distributing my Erlang code" (Armstrong, "Compiling and Running Your Program," "Automating Compilation with Makefiles"). An Erlang makefile defines suffix rules (e.g. `.erl.beam:` whose body is `erlc -W $<`), a `MODS` variable listing the modules to compile, and a set of **targets** — "a target is an alphanumeric string starting in the first column and terminated by a colon (`:`)." The command `make [Target]` runs a target; if `Target` is omitted, "the first target in the file is assumed." Any module in `MODS` is compiled with `erlc Mod.erl`.

# Prerequisites

- **erlc Compiler** — Makefile rules call `erlc` to compile each module; you must know the command-line compiler.

# Key Properties

1. Driven by the `make` utility; run with `make [Target]`.
2. Suffix rules (e.g. `.erl.beam:`) tell `make` how to turn `.erl` into `.beam`.
3. The `MODS` variable lists every module to compile.
4. Targets are colon-terminated names starting in column 1 (e.g. `all`, `compile`, `clean`).
5. With no argument, `make` runs the first target in the file.
6. A `clean` target typically removes `*.beam` and `erl_crash.dump`.
7. Indented command lines must begin with a tab character — spaces break `make`.

# Construction / Recognition

## To Construct/Create:
1. Start from the book's makefile template and delete irrelevant lines.
2. Set `.SUFFIXES: .erl .beam` and a `.erl.beam:` rule with `erlc -W $<`.
3. List your modules in `MODS`.
4. Define `all`, `compile`, and `clean` targets.
5. Run `make` (or `make Target`).

## To Identify/Recognize:
1. A `MODS = ...` line and a `.erl.beam:` suffix rule identify an Erlang makefile.
2. Colon-terminated names in column 1 are the targets.

# Context & Application

- **Typical contexts**: Larger projects; recurring compile/test cycles; resuming a project months later.
- **Common applications**: Building all modules, running an application from `make`, cleaning object code, recursing into subdirectories.
- **Historical/stylistic notes**: Armstrong prefers minimal makefiles — start from the template and remove clutter, ending with a short, readable file.

# Examples

**Example 1** ("A Makefile Template"): The suffix rule `.erl.beam:` with body `erlc -W $<` compiles each `.erl` to `.beam`.

**Example 2** ("A Makefile Template"): `MODS = module1 module2 module3` lists the modules; `compile: ${MODS:%=%.beam}` builds them all.

**Example 3** ("Specializing the Makefile Template"): A simplified makefile keeps only `.SUFFIXES`, the `.erl.beam:` rule, `MODS`, `all`, and `clean` (which runs `rm -rf *.beam erl_crash.dump`).

# Relationships

## Builds Upon
- **erlc Compiler** — Makefile rules invoke `erlc` to do the compilation.

## Enables
- (No downstream concept depends on this in the chapter.)

## Related
- **Compiling modules** — A makefile automates the compile step.
- **Running Erlang programs** — A target can also launch an application via `erl -s`.

## Contrasts With
- None.

# Common Errors

- **Error**: Indenting makefile command lines with spaces instead of a tab.
  **Correction**: Each indented command line (except continuations) must start with a tab; spaces confuse `make`.

- **Error**: Listing a module in `MODS` with no corresponding `.erl` file (or a misspelled name).
  **Correction**: `make` fails with "No rule to make target `glurk.beam'"; fix the `MODS` entry or add the file.

# Common Confusions

- **Confusion**: Thinking `make` with no argument runs every target.
  **Clarification**: It runs only the first target in the file (often `all`).

- **Confusion**: Believing makefiles are an Erlang-specific tool.
  **Clarification**: `make` is a general OS build tool; the makefile just contains Erlang-specific rules.

# Source Reference

Chapter 10: "Compiling and Running Your Program," section "Automating Compilation with Makefiles" (subsections "A Makefile Template" and "Specializing the Makefile Template"). EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the makefile discussion and the template.
- Confidence rationale: HIGH — the makefile structure, targets, and rules are described explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
