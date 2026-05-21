---
# === CORE IDENTIFICATION ===
concept: Erlang Debugger
slug: erlang-debugger

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
section: "5.3 Debugger"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - debugger
  - "source-level debugger"
  - "graphical debugger"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - erlang-process
extends: []
related:
  - appmon
  - pman
  - tv-table-viewer
  - erlang-toolbar
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang debugger?"
  - "How do you make a module available for debugging?"
  - "How do you set a breakpoint in the Erlang debugger?"
---

# Quick Definition

The Erlang Debugger is a graphical source-level debugger. Modules must be *interpreted* before they can be debugged, and processes attach to the debugger when they hit a breakpoint.

# Core Definition

The Erlang Debugger is a graphical source-level debugger, started with `debugger:start()` (Ch. 5, Section 5.3). Its architecture is process-oriented: the main monitor window has a large area listing processes currently attached to the debugger and a small area listing interpreted modules. A module is not available for debugging until you tell the debugger to *interpret* it; this needs both the `.erl` source file and a `.beam` file compiled with the `debug_info` flag (passed to `erlc` as `+debug_info`). Selecting Module > Interpret picks a source file. Double-clicking a line of an interpreted module sets or removes a breakpoint (shown as a red circle). When a process hits a breakpoint it appears in the monitor window; double-clicking it opens an attach window for single-stepping, continuing, viewing variables, and managing breakpoints. The book notes you will likely use the debugger less than in other languages, because logs and crash reports often suffice.

# Prerequisites

- **Erlang module** — Modules must be interpreted to be debugged.
- **Process** — The debugger's architecture is process-oriented; processes attach to it.

# Key Properties

1. Started with `debugger:start()`.
2. A module must be *interpreted* before it can be debugged.
3. Interpreting needs the `.erl` source and a `.beam` compiled with `debug_info`.
4. `debug_info` is passed to `erlc` as `+debug_info` (compiler flags use `+`, not `-`).
5. Double-clicking a source line sets or removes a breakpoint.
6. Attaching to a stopped process allows single-stepping and variable inspection.

# Construction / Recognition

## To Use the Debugger:
1. Recompile the code with `erlc +debug_info -o ebin src/*.erl`.
2. Call `debugger:start()`.
3. Use Module > Interpret to select a source file.
4. Double-click a line to set a breakpoint.
5. Run the code; double-click the stopped process to attach and step.

# Context & Application

The debugger is for cases where you must step through code — e.g. developing a tricky algorithm or protocol — though crash reports and logs are often a better tool for concurrent/timing bugs.

- **Typical contexts**: Stepping through a tricky algorithm; inspecting variables at a breakpoint.
- **Common applications**: Setting a breakpoint in `tr_server`'s `do_rpc/2` and stepping through an RPC.

# Examples

**Example 1** (Ch. 5): After interpreting `tr_server`, double-clicking the line that calls `split_out_mfa(RawData)` sets a breakpoint; performing a remote call over telnet halts `tr_server` there.

# Relationships

## Related
- **appmon** / **pman** / **tv-table-viewer** — Other introspection tools.
- **erlang-toolbar** — Can launch the Debugger.

## Contrasts With
- This card has no direct contrast within the source's treatment.

# Common Errors

- **Error**: Trying to interpret a module compiled without `debug_info`.
  **Correction**: Recompile with `+debug_info` so the `.beam` contains debugging information.

- **Error**: Using `-debug_info` with `erlc`.
  **Correction**: Compiler flags are prefixed with `+`; use `+debug_info`.

# Common Confusions

- **Confusion**: Expecting the debugger to look like Eclipse or DDD.
  **Clarification**: Its architecture is process-oriented — the main window lists attached processes and interpreted modules.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.3 "Debugger."

# Verification Notes

- Definition source: Direct adaptation of Section 5.3.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slugs `erlang-module`, `process` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
