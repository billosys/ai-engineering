---
# === CORE IDENTIFICATION ===
concept: Erlang Shell
slug: erlang-shell

# === CLASSIFICATION ===
category: tooling
subcategory: interactive-environment
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.1 The Erlang shell"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - eshell
  - erl
  - werl
  - REPL

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - shell-expression
  - shell-functions
  - compiling-modules
  - single-assignment
contrasts_with:
  - compiled-module-vs-shell
  - erlang-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang shell?"
  - "How do you start the Erlang shell?"
  - "What can you do in the Erlang shell?"
---

# Quick Definition

The Erlang shell is the interactive environment for entering and evaluating expressions, doing incremental development and debugging, and controlling a running Erlang system.

# Core Definition

"Interaction with an Erlang system happens mainly through the *shell*. The shell is your command central. It's where you can try out short snippets to see how they work; it's where you do incremental development and interactive debugging; and it can also be used to control a running system in production" (Chapter 2, section 2.1). Erlang "is more like an operating system within your operating system" — designed for running continuously rather than start-stop execution. The shell is started by running the `erl` command on UNIX-like systems, or by running `werl` on Windows (which avoids problems of running `erl` interactively under the Windows console). It can also be started with the `-noshell` flag for batch jobs or daemons.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The shell is the main way to interact with an Erlang system.
2. It is used for trying snippets, incremental development, interactive debugging, and production control.
3. It is started with `erl` (UNIX-like systems) or `werl` (Windows).
4. The `-noshell` flag runs Erlang without an interactive console.
5. The prompt is numbered (`1>`, `2>`, ...) and increments per evaluated expression.

# Construction / Recognition

## To Construct/Create:
1. On UNIX-like systems, run `erl` in a console window.
2. On Windows, click the Erlang icon, which runs `werl`.
3. The shell prints a banner and the `1>` prompt.

# Context & Application

- **Typical contexts**: Learning Erlang, developing code, debugging, operating production systems.
- **Common applications**: Compiling and loading modules, inspecting a running system, killing runaway jobs.
- **Historical/stylistic notes**: An Erlang system is designed to run continuously; optimally the only reasons to restart it are hardware failure or an OS upgrade.

# Examples

**Example 1** (section 2.1.1): Starting the shell shows a banner like `Erlang (BEAM) emulator version 5.6.5 [smp:2]` followed by `Eshell V5.6.5 (abort with ^G)` and the `1>` prompt.

**Example 2** (section 2.1.1): `erl -noshell` runs the Erlang system without a console, used for running Erlang as a batch job or daemon.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **Shell expression** — the shell evaluates expressions.
- **Shell functions** — special functions available only in the shell.
- **Compiling modules** — `c(...)` compiles and loads modules from the shell.

## Related
- **Single assignment** — shell variables follow single-assignment rules with shell-specific scoping.

## Contrasts With
- **Compiled module vs. shell** — shell code is interpreted, not compiled; declarations are not allowed in the shell.
- **Erlang module** — real programs live in modules, not in the shell.

# Common Errors

- **Error**: Running `erl` interactively under the normal Windows `cmd.exe` console.
  **Correction**: On Windows, use `werl` for interactive work; `erl` is for scripts.

# Common Confusions

- **Confusion**: Treating the Erlang shell like a start-stop interpreter run.
  **Clarification**: Erlang is designed to run continuously; the shell is a persistent interactive environment, "an operating system within your operating system."

# Source Reference

Chapter 2: Erlang language essentials, section 2.1 "The Erlang shell," including 2.1.1 "Starting the shell."

# Verification Notes

- Definition source: Direct adaptation from sections 2.1 and 2.1.1.
- Confidence rationale: HIGH — the shell is explicitly described.
- Uncertainties: None.
- Cross-reference status: `shell-expression`, `shell-functions`, `compiling-modules`, `compiled-module-vs-shell`, `erlang-module` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
