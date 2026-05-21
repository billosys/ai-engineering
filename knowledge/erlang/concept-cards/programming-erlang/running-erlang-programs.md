---
# === CORE IDENTIFICATION ===
concept: Running Erlang Programs
slug: running-erlang-programs

# === CLASSIFICATION ===
category: tooling
subcategory: environment
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
  - "running a program"
  - "erl runtime"
  - "starting Erlang programs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiling-modules
extends: []
related:
  - erlc-compiler
  - escript
  - erlang-shell
  - erlang-makefile
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the ways to run an Erlang program?"
  - "How do I run a program with command-line arguments?"
  - "How do I run an Erlang program without an interactive shell?"
---

# Quick Definition

There are three ways to run an Erlang program: compile and run in the shell, compile and run from the OS command prompt, or run it directly as an escript. The right choice depends on the occasion.

# Core Definition

"There are actually three different ways to run your programs" (Armstrong, "Compiling and Running Your Program," chapter introduction). They are: (1) compile with `c(Module)` in the shell, then call an exported function; (2) compile with `erlc`, then run from the OS prompt with `erl -noshell -s Mod Func ... -s init stop`; and (3) run directly as an escript with no compilation. The `erl` program starts the Erlang runtime system. Key startup options include `-noshell` (start without the interactive shell and banner), `-s Mod Func [Args]` (run `Mod:Func` via apply — the module must be compiled), and `-s init stop` (stop the system after the previous command finishes).

# Prerequisites

- **Compiling modules** — Two of the three ways require the module to be compiled to `.beam` first.

# Key Properties

1. Three ways: shell (`c/1` + call), command prompt (`erlc` + `erl -s`), escript.
2. `erl` starts the Erlang runtime; `erlc` only compiles.
3. `-noshell` suppresses the interactive shell and banner.
4. `-s Mod Func Args` runs `Mod:Func` via an apply; `Mod` must be compiled.
5. Multiple `-s ...` commands run in sequence; each completes before the next begins.
6. `-s init stop` cleanly stops the system after preceding commands.
7. Command-line arguments require the program to be written to receive them (e.g. a `main/1` function).

# Construction / Recognition

## To Construct/Create:
1. Choose the method: shell for interactive development; command prompt or shell script for repeatable runs; escript for quick scripts.
2. For methods 1 and 2, compile the module first.
3. For method 2, invoke `erl -noshell -s Mod Func ... -s init stop`, optionally setting the path with `-pa Dir`.
4. For method 3, write a `main/1` function and run the escript directly.

## To Identify/Recognize:
1. `erl -noshell -s ...` in a shell script signals the command-prompt method.
2. A `#!/usr/bin/env escript` shebang signals the escript method.

# Context & Application

- **Typical contexts**: Development (shell), automated/repeatable runs (command prompt, makefiles), quick utilities (escript).
- **Common applications**: Wrapping `erl -noshell ...` in a shell script that sets the path with `-pa Directory` and launches the program.
- **Historical/stylistic notes**: The `-eval` argument is "very handy for quick scripting" — e.g. `erl -eval '...' -noshell -s init stop`.

# Examples

**Example 1** ("Compile and Run in the Erlang Shell"): `c(hello).` then `hello:start().` prints `Hello world`.

**Example 2** ("Compile and Run from the Command Prompt"): `erl -noshell -s hello start -s init stop` runs `hello:start()` then stops the system.

**Example 3** ("Programs with Command-Line Arguments"): `erl -noshell -s fac1 main 25` runs `fac1:main` with argument `25`, printing `factorial 25 = 15511210043330985984000000`.

## Worked Example

A shell script that runs `hello` ("Compile and Run from the Command Prompt"):

```sh
#!/bin/sh
erl -noshell -pa /home/joe/2012/book/JAERLANG/Book/code \
    -s hello start -s init stop
```

`chmod u+x hello.sh` once, then `./hello.sh` prints `Hello world`.

# Relationships

## Builds Upon
- **Compiling modules** — Shell and command-prompt runs require compiled `.beam` files.

## Enables
- (No downstream concept strictly depends on this in the chapter.)

## Related
- **erlc Compiler** — Produces the `.beam` files the command-prompt method runs.
- **escript** — The third, no-compile way to run a program.
- **The Erlang shell** — The interactive run method.
- **Erlang makefile** — Automates compile-and-run.

## Contrasts With
- None.

# Common Errors

- **Error**: Using `-s Mod ...` for a module that has not been compiled.
  **Correction**: The `-s Mod` option requires `Mod` to be compiled; compile it first.

- **Error**: Forgetting `-s init stop`, leaving the runtime alive after a batch run.
  **Correction**: Append `-s init stop` so the system stops once the program finishes.

# Common Confusions

- **Confusion**: Thinking the entry function must be named `main`.
  **Clarification**: For `-s Mod Func`, the function can have any name; only the function name and the command-line name must agree. (`main` is required specifically for escripts.)

- **Confusion**: Believing `-noshell` changes program behavior.
  **Clarification**: `-noshell` only suppresses the interactive shell and banner; the program runs the same.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Different Ways to Run Your Program," "Compile and Run from the Command Prompt," and "Programs with Command-Line Arguments." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the three-ways discussion and the `hello`/`fac1` examples.
- Confidence rationale: HIGH — the three methods and `erl` options are described explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
