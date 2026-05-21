---
# === CORE IDENTIFICATION ===
concept: The Erlang Shell
slug: erlang-shell

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
section: "Tweaking the Environment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang shell"
  - "Eshell"
  - "erl"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiling-modules
  - running-erlang-programs
  - erlang-shell-job-control
  - erlang-startup-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang shell?"
  - "How do I compile and run code in the shell?"
  - "How do I add my own shell commands?"
---

# Quick Definition

The Erlang shell (`erl`, "Eshell") is the interactive read-eval-print environment for evaluating Erlang expressions, compiling modules with `c/1`, and running functions during development.

# Core Definition

The Erlang shell is the interactive environment started by the `erl` command — it greets the user with an `Eshell` banner and a numbered prompt. It is "fine for small examples" of compiling and running programs (Armstrong, "Compiling and Running Your Program," chapter introduction): `c(Module)` compiles a module and `Module:Func(...)` runs an exported function. The shell has built-in commands listed by `help()` — for example `b()` (show bindings), `f()` (forget bindings), `e(N)` (repeat expression `N`), `h()` (history) — all defined in the module `shell_default`. Users can add their own shell commands by creating a `user_default` module; any function in it can be called without a module name once the module is on the load path.

# Prerequisites

This is a foundational concept within this chapter — it has no prerequisites among the chapter's other concepts.

# Key Properties

1. Started with the `erl` command; shows the `Eshell` banner and numbered prompts.
2. Reads, evaluates, and prints Erlang expressions interactively.
3. `c(Module)` compiles a module from within the shell.
4. Built-in commands (`b()`, `f()`, `e(N)`, `h()`, etc.) are listed by `help()` and defined in `shell_default`.
5. A user-defined `user_default` module adds custom commands callable without a module prefix.
6. Pressing Ctrl+G enters job-control mode for managing shell sessions.
7. The `.erlang` file is read and evaluated before the shell starts.

# Construction / Recognition

## To Construct/Create:
1. Run `erl` to start the shell.
2. Compile with `c(Module)`, then call `Module:Func(Args)`.
3. To extend it, write and compile a `user_default` module on the load path.

## To Identify/Recognize:
1. The `Eshell V...` banner and `1>` prompt identify the shell.
2. `help()` lists the available built-in shell commands.

# Context & Application

- **Typical contexts**: Interactive development; trying out expressions; compiling and running small programs.
- **Common applications**: The compile-and-run-in-the-shell method of running a program; inspecting and managing the runtime.
- **Historical/stylistic notes**: For larger programs the book moves beyond the shell to makefiles and command-line invocation; the shell remains the day-to-day development tool.

# Examples

**Example 1** ("Compile and Run in the Erlang Shell"): `1> c(hello).` returns `{ok,hello}`; `2> hello:start().` prints `Hello world`.

**Example 2** ("Tweaking the Environment"): `help()` prints the built-in shell commands such as `b()`, `e(N)`, `f()`, and `h()`.

**Example 3** ("Tweaking the Environment"): A `user_default` module with `hello() -> "Hello Joe how are you?".` lets `hello().` be typed directly in the shell.

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Compiling modules** — `c/1` compiles from the shell.
- **Running Erlang programs** — The shell is the interactive run method.

## Related
- **Erlang shell job control** — Ctrl+G mode for managing shell jobs.
- **Erlang startup file** — `.erlang` runs before the shell starts.

## Contrasts With
- None.

# Common Errors

- **Error**: Calling a function from a module that was never compiled in the shell.
  **Correction**: Run `c(Module)` first; an uncompiled module yields an `undef` error.

- **Error**: Expecting a hung shell to recover on its own.
  **Correction**: Use Ctrl+G job-control mode to interrupt, kill, or start a fresh shell.

# Common Confusions

- **Confusion**: Thinking the shell is only a toy and unrelated to real programs.
  **Clarification**: It is the primary development environment; the same `c/1`-compiled modules run identically when launched from the command line.

- **Confusion**: Believing custom commands need a special API.
  **Clarification**: Just create a `user_default` module; its functions become bare shell commands.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Compile and Run in the Erlang Shell" and "Tweaking the Environment." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the shell usage and `user_default` discussion in the named sections.
- Confidence rationale: HIGH — the shell, its commands, and customization are described explicitly.
- Uncertainties: None.
- Cross-reference status: Cross-refs verified against KB slugs.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
