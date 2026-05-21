---
concept: Erlang Shell
slug: erlang-shell
category: tooling
subcategory: development-environment
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Using the Erlang Shell"
extraction_confidence: high
aliases:
  - "Eshell"
  - "erl"
  - "Erlang emulator"
  - "REPL"
prerequisites: []
extends: []
related:
  - compiling-erlang-code
  - variable
contrasts_with: []
answers_questions:
  - "How do I create and compile a module?"
---

# Erlang Shell

## Quick Definition

The Erlang shell (Eshell) is an interactive emulator where you can type and immediately evaluate Erlang expressions. It is started with the `erl` command and is the primary tool for testing code live.

## Core Definition

The Erlang shell is an interactive environment, started by typing `erl` (or `werl.exe` on Windows), in which Erlang code can be entered and run in the emulator. The shell is not a single instance but "a bundle of shell instances, each running different jobs," manageable like operating-system processes via the job-control menu (Ctrl-G) (Hébert, ch. 1, "Using the Erlang Shell").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Started with `erl` on Linux/macOS; `werl.exe` is preferred on Windows for line-editing support.
2. Has a built-in line editor based on a subset of Emacs (Ctrl-A start of line, Ctrl-E end of line).
3. Tab completion expands module names and lists module functions.
4. A sequence of expressions must be terminated with a period followed by whitespace; otherwise it will not execute.
5. Expressions separated by commas all execute, but only the last result is shown.
6. Ctrl-G opens the job-control menu (connect, interrupt, kill, list, start shell jobs).
7. `q().` (shorthand for `init:stop()`) quits Erlang; `help().` lists shell commands.

## Construction / Recognition

To recover a frozen shell:

1. Press Ctrl-G to reach the job-control menu.
2. Type `i` and press Enter to interrupt the current shell job.
3. Type `c` and press Enter to connect back to it.

## Context & Application

The shell is where most code is tested before being saved into modules. Industrial Erlang shells may run for years uninterrupted, which is why shell-only helpers like `f(Variable)` exist for clearing variables during testing without affecting compiled programs.

## Examples

**Example** (ch. 1): `2 + 15.` entered at the shell prompt returns `17`.

**Example** (ch. 1): Pressing Tab after typing `li` expands to `lists:`, and pressing Tab again lists all functions in the `lists` module.

## Relationships

### Related

- **Compiling Erlang code** — The shell's `c()` function compiles modules for use in the emulator
- **Variable** — Shell-only functions `f(Variable)` and `f()` clear bound variables during testing

## Common Errors

- **Error**: Forgetting the terminating period followed by whitespace, so an expression never executes
  **Correction**: End each shell expression with `.` followed by a line break or space

## Common Confusions

- **Confusion**: Thinking the shell is a single process like in other languages
  **Clarification**: The shell is a bundle of job instances managed via Ctrl-G, similar to OS processes

## Source Reference

Chapter 1: "Starting Out," sections "Using the Erlang Shell," "Entering Shell Commands," and "Exiting the Shell."

## Verification Notes

- Definition: Direct adaptation from the chapter's opening sections
- Confidence: HIGH — the source dedicates an explicit section to the shell with worked examples
- Uncertainties: None
