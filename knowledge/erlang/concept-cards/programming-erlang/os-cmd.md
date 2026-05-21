---
# === CORE IDENTIFICATION ===
concept: os:cmd
slug: os-cmd

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Calling a Shell Script from Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "os:cmd/1"
  - "calling a shell command"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - port
  - port-program
contrasts_with:
  - port-program

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call a shell command from Erlang?"
  - "How do I capture the output of an OS command?"
  - "What is the simplest way to run an external program from Erlang?"
---

# Quick Definition

`os:cmd(Str)` runs the operating-system command in the string `Str` and returns its captured output as a string.

# Core Definition

To call a shell script (or any OS command) from Erlang, you can use the library function `os:cmd(Str)`; this runs the command in the string `Str` and captures the result (Chapter 15, "Calling a Shell Script from Erlang"). It is the second of the three interfacing approaches in the chapter — "running an OS command from within Erlang and capturing the result." The returned string typically needs parsing to extract the information of interest.

# Prerequisites

This is a foundational interfacing function with no prerequisites within this source.

# Key Properties

1. `os:cmd(Str)` takes a string containing an OS command.
2. It runs the command and captures its standard output.
3. It returns the output as a string.
4. The returned string usually needs further parsing.
5. It is the simplest of the chapter's three interfacing approaches.

# Construction / Recognition

## To Use os:cmd:
1. Build the command as a string, e.g. `"ifconfig"`.
2. Call `os:cmd(Str)`.
3. Parse the returned string for the information you need.

## To Recognize It:
1. Look for `os:cmd/1` calls with shell-command strings.
2. Look for subsequent string-parsing of the result.

# Context & Application

- **Typical contexts**: Quick, one-off invocation of external OS commands.
- **Common applications**: Querying system information (network config, CPU type); running shell scripts.
- **Historical/stylistic notes**: Unlike a port, `os:cmd` does not give you an ongoing process-like channel — it runs the command and returns its output once.

# Examples

**Example 1** (Chapter 15, "Calling a Shell Script from Erlang"): `os:cmd("ifconfig")` returns a string beginning `"lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384\n\t..."`.

**Example 2** (Chapter 15, Exercise 3): The chapter suggests writing a function that returns the CPU type by using `os:cmd` to call an appropriate OS command.

# Relationships

## Builds Upon
- A standalone library function; builds on no other concept in this source.

## Enables
- Quick access to external command output from Erlang.

## Related
- **Port** / **port program** — the more powerful, ongoing interfacing mechanism.

## Contrasts With
- **Port program** — a port program is a persistent, message-driven external process under Erlang's control; `os:cmd` is a one-shot run-and-capture call.

# Common Errors

- **Error**: Expecting structured data from `os:cmd`.
  **Correction**: It returns a raw string; parse it to extract what you need.
- **Error**: Using `os:cmd` for a long-running interactive external program.
  **Correction**: Use a port for ongoing, bidirectional communication.

# Common Confusions

- **Confusion**: `os:cmd` gives a process-like channel to the command.
  **Clarification**: It runs the command and returns its output once; there is no ongoing channel.
- **Confusion**: `os:cmd` is unsafe like a linked-in driver.
  **Clarification**: The command runs as a separate OS process, so it cannot crash the Erlang VM.

# Source Reference

Chapter 15: Interfacing Techniques, section "Calling a Shell Script from Erlang" (the `os:cmd/1` function and `ifconfig` example); Exercise 3.

# Verification Notes

- Definition source: Direct adaptation of "Calling a Shell Script from Erlang."
- Confidence rationale: HIGH — `os:cmd` is explicitly described with an example.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards (`port`, `port-program`).
- Re-extraction notes: Fresh extraction; no pre-existing card.
