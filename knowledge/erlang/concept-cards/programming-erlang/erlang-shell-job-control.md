---
# === CORE IDENTIFICATION ===
concept: Erlang Shell Job Control
slug: erlang-shell-job-control

# === CLASSIFICATION ===
category: production-ops
subcategory: shell
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Compiling and Running Your Program"
chapter_number: 10
pdf_page: null
section: "The Shell Isn't Responding"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "shell JCL"
  - "Job Control Language mode"
  - "Ctrl+G shell mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-shell
extends:
  - erlang-shell
related:
  - running-erlang-programs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do I do when the Erlang shell stops responding?"
  - "How do I interrupt a hung shell command?"
  - "How do I start a second shell or connect to a remote node?"
---

# Quick Definition

Erlang shell job control (shell JCL) is the mode entered by pressing Ctrl+G. It lets you interrupt or kill a hung shell job, start additional shells, switch between them, or connect to a remote node.

# Core Definition

"If the shell is not responding to commands ... you can interrupt the current shell by pressing Ctrl+G" (Armstrong, "Compiling and Running Your Program," "The Shell Isn't Responding"). Ctrl+G enters "shell JCL" (Job Control Language) mode, signaled by the `User switch command` prompt `-->`. From this mode, `h` shows help; `j` lists all jobs; `i [nn]` interrupts a job; `k [nn]` kills a job; `c [nn]` connects to a job; `s` starts a new local shell; `r [node]` starts a remote shell; and `q` quits Erlang. Commands with an optional `[nn]` argument act on the default shell (marked with a star) unless a number is given.

# Prerequisites

- **The Erlang shell** — Job control manages shell sessions; you must know the shell first.

# Key Properties

1. Entered by pressing Ctrl+G; prompt becomes `-->` (`User switch command`).
2. `h` (or `?`) — show help.
3. `j` — list all jobs; the default shell is marked with `*`.
4. `i [nn]` — interrupt a job; `k [nn]` — kill a job.
5. `c [nn]` — connect to a job; `s` — start a new local shell.
6. `r [node]` — start a remote shell on another node; `q` — quit Erlang.
7. Multiple shells can coexist; you swap between them via Ctrl+G.

# Construction / Recognition

## To Construct/Create:
1. When the shell hangs, press Ctrl+G to enter JCL mode.
2. Type `j` to list jobs and identify the stuck one.
3. Use `i` to interrupt or `k` to kill it, `s` to start a fresh shell, then `c N` to connect to it.

## To Identify/Recognize:
1. The `User switch command` line and `-->` prompt indicate JCL mode.
2. A job list with one entry starred (`1*`) shows the default shell.

# Context & Application

- **Typical contexts**: Recovering from a hung command (e.g. a `receive` waiting for a message that never comes), or an unterminated quote/expression.
- **Common applications**: Killing a runaway job, opening a second shell, attaching a shell to a remote node.
- **Historical/stylistic notes**: A hung shell may also be caused by forgetting the closing `dot-carriage-return` at the end of a command.

# Examples

**Example 1** ("The Shell Isn't Responding"): `receive foo -> true end.` makes the shell wait forever (no one sends `foo`); pressing Ctrl+G enters JCL mode.

**Example 2** ("The Shell Isn't Responding"): Typing `h` lists the JCL commands (`c`, `i`, `k`, `j`, `s`, `r`, `q`, `?`/`h`).

**Example 3** ("The Shell Isn't Responding"): `s` starts a new shell, `j` shows two shells (2 now default), `c 2` connects to shell 2, then `init:stop()` stops the system.

# Relationships

## Builds Upon
- **The Erlang shell** — JCL mode controls and switches between shell jobs.

## Enables
- (No downstream concept depends on this in the chapter.)

## Related
- **Running Erlang programs** — JCL `r` can start a remote shell to run programs on another node.

## Contrasts With
- None.

# Common Errors

- **Error**: Killing the whole Erlang runtime when only a hung job needs interrupting.
  **Correction**: Use Ctrl+G then `i`/`k` on the specific job, or start a fresh shell with `s`.

- **Error**: Assuming `[nn]`-argument commands always need a number.
  **Correction**: Without a number they act on the default (starred) shell.

# Common Confusions

- **Confusion**: Thinking Ctrl+G stops the running program.
  **Clarification**: Ctrl+G switches to JCL mode for *managing* jobs; you then choose to interrupt or kill.

- **Confusion**: Believing only one shell can exist.
  **Clarification**: `s` starts additional shells; `j`/`c` list and switch between them.

# Source Reference

Chapter 10: "Compiling and Running Your Program," section "When Things Go Wrong," subsection "The Shell Isn't Responding." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the Ctrl+G / JCL walkthrough in "The Shell Isn't Responding."
- Confidence rationale: HIGH — the JCL commands and workflow are shown explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; new card (no prior file).
