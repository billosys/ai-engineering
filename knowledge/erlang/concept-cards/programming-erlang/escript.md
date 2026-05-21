---
# === CORE IDENTIFICATION ===
concept: escript
slug: escript

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
section: "Run As an Escript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang script"
  - "escript"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - running-erlang-programs
  - compiling-modules
contrasts_with:
  - compiling-modules

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an escript?"
  - "How do I run an Erlang program without compiling it?"
  - "How does an escript access command-line arguments?"
---

# Quick Definition

An escript is an Erlang program run directly as a script — no separate compilation step. The file defines a `main(Args)` function and is made executable so the OS can run it.

# Core Definition

"Using an escript, you can run your programs directly as scripts — there's no need to compile them first" (Armstrong, "Compiling and Running Your Program," "Run As an Escript"). An escript file begins with the line `#!/usr/bin/env escript` and "must contain a function `main(Args)`." When the script is called from an operating-system shell, "`Args` will contain a list of the command-line arguments." On a Unix system the file's mode must be set to executable (`chmod u+x File`), which need be done only once.

# Prerequisites

This is a foundational concept within this chapter — it has no prerequisites among the chapter's other concepts.

# Key Properties

1. First line is the shebang `#!/usr/bin/env escript`.
2. Must define a function `main(Args)`.
3. `Args` is a list of command-line arguments.
4. Requires no compilation — the source runs directly.
5. The file must be made executable once (`chmod u+x`).
6. In a `main(Args)` escript, arguments arrive in a form that may be passed straight to functions like `list_to_integer/1`.

# Construction / Recognition

## To Construct/Create:
1. Create a file whose first line is `#!/usr/bin/env escript`.
2. Define `main(Args) -> ...` to do the work.
3. Make the file executable: `chmod u+x File`.
4. Run it directly: `./File arg1 arg2`.

## To Identify/Recognize:
1. A file starting with `#!/usr/bin/env escript` is an escript.
2. The presence of a `main/1` function (and absence of a `-module` declaration) is characteristic.

# Context & Application

- **Typical contexts**: Quick command-line utilities; programs that should run without a build step.
- **Common applications**: Small tools and scripts; programs that take command-line arguments.
- **Historical/stylistic notes**: The book contrasts escripts with the compile-then-run workflow as the third of three ways to run a program.

# Examples

**Example 1** ("Run As an Escript"): The `hello` escript — `#!/usr/bin/env escript` then `main(Args) -> io:format("Hello ~p~n",[Args]).` — run as `./hello joe` prints `Hello ["joe"]`.

**Example 2** ("Programs with Command-Line Arguments"): The `factorial` escript defines `main([A]) -> I = list_to_integer(A), F = fac(I), io:format("factorial ~w = ~w~n",[I, F]).` and is run with `./factorial 25`.

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Running Erlang programs** — escript is one of the three ways the chapter presents for running a program.

## Related
- **Compiling modules** — escript is the no-compile alternative to the compiled workflow.

## Contrasts With
- **Compiling modules** — A compiled program produces a `.beam` and runs via `erl -s`; an escript runs source directly through `main/1`.

# Common Errors

- **Error**: Forgetting to make the escript file executable.
  **Correction**: Run `chmod u+x File` once before invoking the script.

- **Error**: Omitting or misnaming the `main/1` function.
  **Correction**: An escript must define exactly `main(Args)` as its entry point.

# Common Confusions

- **Confusion**: Thinking an escript must be compiled like a module.
  **Clarification**: An escript runs directly; no `erlc` step is involved.

- **Confusion**: Expecting escript `Args` and compiled `-s Mod main` arguments to have identical representations.
  **Clarification**: In the `hello` escript example arguments arrive as a list (e.g. `["joe"]`); details depend on how the program is launched.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Run As an Escript" and "Programs with Command-Line Arguments." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the escript discussion and the `hello`/`factorial` examples.
- Confidence rationale: HIGH — escript is defined explicitly with examples.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
