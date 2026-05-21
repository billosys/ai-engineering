---
# === CORE IDENTIFICATION ===
concept: Compiling Modules
slug: compiling-modules

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
section: "Different Ways to Run Your Program"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "compiling code"
  - "c/1"
  - "module compilation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlc-compiler
  - running-erlang-programs
  - erlang-shell
  - escript
contrasts_with:
  - escript

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compile an Erlang module?"
  - "How do I write, compile, and run a module?"
  - "What is a .beam file?"
---

# Quick Definition

Compiling a module turns an `.erl` source file into a `.beam` object-code file that the runtime can load and run. It can be done in the shell with `c(Module)` or from the OS prompt with `erlc`.

# Core Definition

"Erlang programs are stored in modules. Once you have written your program, you have to compile it before you can run it" (Armstrong, "Compiling and Running Your Program," "Different Ways to Run Your Program"). Compilation produces an object-code file with the `.beam` extension — for example, `erlc hello.erl` "compiles the file `hello.erl`, producing an object code file called `hello.beam`." Inside the shell, `c(Module)` compiles `Module.erl` and returns `{ok, Module}`. The alternative to compiling is to run the program directly as an escript.

# Prerequisites

This is a foundational concept within this chapter — it has no prerequisites among the chapter's other concepts.

# Key Properties

1. Source files have the `.erl` extension; compiled object code has the `.beam` extension.
2. In the shell, `c(Module)` compiles `Module.erl`; success yields `{ok, Module}`.
3. From the OS prompt, `erlc Module.erl` compiles without starting a runtime.
4. A module must be compiled before it can be run with `erl -s Mod ...`.
5. `-compile(export_all).` makes the compiler export every function (useful during development).
6. The compiler produces better code when it knows exactly which functions are exported.

# Construction / Recognition

## To Construct/Create:
1. Write the module in an `.erl` file with a `-module` and `-export` declaration.
2. Compile it: `c(Module)` in the shell or `erlc Module.erl` at the OS prompt.
3. Confirm a `Module.beam` file was produced.

## To Identify/Recognize:
1. `{ok, Module}` from `c/1` indicates a successful compile.
2. A `.beam` file alongside the `.erl` file confirms compilation occurred.

# Context & Application

- **Typical contexts**: Every development cycle; preparing a module so it can be loaded and run.
- **Common applications**: Interactive shell development (`c/1`); batch/build compilation (`erlc`); makefile-driven builds.
- **Historical/stylistic notes**: `-compile(export_all)` eases development but should be commented out for production — it also makes Dialyzer analysis harder.

# Examples

**Example 1** ("Compile and Run in the Erlang Shell"): `1> c(hello).` returns `{ok,hello}`, then `2> hello:start().` prints `Hello world`.

**Example 2** ("Compile and Run from the Command Prompt"): `erlc hello.erl` compiles `hello.erl` to `hello.beam`.

**Example 3** ("Exporting Functions During Development"): `-compile(export_all).` exports every function in the module, convenient while developing.

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Running Erlang programs** — A module must be compiled before it can be run.

## Related
- **erlc Compiler** — `erlc` is the command-line compiler.
- **The Erlang shell** — `c/1` compiles from within the shell.

## Contrasts With
- **escript** — An escript runs Erlang source directly, with no compilation step.

# Common Errors

- **Error**: Running `erl -s Mod ...` for a module that was never compiled.
  **Correction**: The `-s Mod` option requires `Mod` to have been compiled first.

- **Error**: Shipping production code with `-compile(export_all).` still enabled.
  **Correction**: Comment it out and add explicit `-export` declarations; this also helps Dialyzer and the optimizer.

# Common Confusions

- **Confusion**: Thinking `.beam` is human-readable source.
  **Clarification**: `.beam` is compiled object code for the BEAM virtual machine; `.erl` is the source.

- **Confusion**: Believing compilation is always required to run Erlang code.
  **Clarification**: escripts run source directly without a separate compile step.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Different Ways to Run Your Program," "Compile and Run in the Erlang Shell," and "Compile and Run from the Command Prompt." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the compilation discussion and the `hello` examples.
- Confidence rationale: HIGH — the source defines compilation and shows it explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
