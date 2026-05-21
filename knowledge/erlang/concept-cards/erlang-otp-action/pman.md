---
# === CORE IDENTIFICATION ===
concept: Pman
slug: pman

# === CLASSIFICATION ===
category: production-ops
subcategory: introspection-tools
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Using the main graphical introspection tools"
chapter_number: 5
pdf_page: null
section: "5.2 Pman"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - pman
  - "process manager"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - appmon
  - erlang-debugger
  - tv-table-viewer
  - erlang-toolbar
contrasts_with:
  - appmon

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Pman?"
  - "How do you view all processes in a running Erlang system?"
  - "What is a reduction in the Pman process list?"
---

# Quick Definition

Pman (process manager) is the Erlang graphical tool with a process-oriented world view: it lists all processes in the system, shows information about each, and can trace and kill them.

# Core Definition

Pman, short for *process manager*, takes a process-oriented view of the Erlang world (Ch. 5, Section 5.2). It lets you view all the processes running in your system and perform various actions on them. It is started with `pman:start()`. The main window lists processes with information about whether they are registered, how many messages are in their mailboxes, their estimated memory size in machine words, and the number of *reductions* each has performed — reductions being an approximate measure of CPU time used. A "Hide System Processes" check box shortens the list to the processes you care about. Double-clicking a process opens a Trace window. Pman has no knowledge of applications — its world view is focused only on processes.

# Prerequisites

- **Process** — Pman's entire world view is processes.

# Key Properties

1. Started with `pman:start()`.
2. Process-centric world view; knows nothing about applications.
3. Lists every process with registered name, mailbox length, memory (in words), and reductions.
4. Reductions are an approximate measure of CPU time used.
5. "Hide System Processes" trims the list to user processes.
6. Double-clicking a process opens a tracing window.

# Construction / Recognition

## To Use Pman:
1. Call `pman:start()` in the Erlang shell.
2. Select "Hide System Processes" to focus on your application's processes.
3. Use the View menu to show/hide specific processes.
4. Double-click a process (or Trace > Trace Selected Process) to trace it.

# Context & Application

Pman is for when you care about individual processes — their mailboxes, memory, and behaviour — independent of which application they belong to.

- **Typical contexts**: Inspecting and tracing individual processes; spotting mailbox growth.
- **Common applications**: Tracing `tr_server` and `tr_sup` while interacting with the RPC server over telnet.

# Examples

**Example 1** (Ch. 5): After `application:start(tcp_rpc)` and `pman:start()`, hiding system processes leaves mainly `tr_sup` and `tr_server` in the list.

**Example 2** (Ch. 5): The `tr_sup` process's Current Function shows `gen_server:loop/6` — framework code — because supervisors are built on `gen_server`.

# Relationships

## Related
- **appmon** — A complementary tool with an application-centric view.
- **erlang-debugger** / **tv-table-viewer** — Other introspection tools.
- **erlang-toolbar** — Can launch Pman.

## Contrasts With
- **appmon** — Pman has a process-only world view; Appmon has an application/supervision view.

# Common Errors

- **Error**: Double-clicking (tracing) a system process involved in displaying trace output.
  **Correction**: Tracing such a process can flood the system and crash it; never randomly trace system processes in production.

# Common Confusions

- **Confusion**: Expecting a process's Current Function to be your own code.
  **Clarification**: For behaviour processes it is often framework code (e.g. `gen_server:loop/6`); the registered name is more useful for identification.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.2 "Pman."

# Verification Notes

- Definition source: Direct adaptation of Section 5.2.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
