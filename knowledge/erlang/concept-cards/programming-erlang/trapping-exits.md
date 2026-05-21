---
# === CORE IDENTIFICATION ===
concept: Trapping Exits
slug: trapping-exits

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: error-propagation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Setting Up a Firewall"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "process_flag(trap_exit, true)"
  - "system process"
  - "trap_exit"
  - "process firewall"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - link
  - exit-signal
extends: []
related:
  - monitor
  - error-handling-philosophy
  - supervisor
contrasts_with:
  - monitor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a process trap exit signals?"
  - "What is a system process in Erlang?"
  - "How do I stop errors from propagating through a system?"
---

# Quick Definition

Trapping exits is turning a normal process into a *system process* by evaluating `process_flag(trap_exit, true)`, so that incoming exit signals are converted into ordinary `{'EXIT', Pid, Why}` messages instead of killing the process.

# Core Definition

There are two types of processes: *normal processes* and *system processes*. `spawn` creates a normal process; a normal process becomes a system process by evaluating the BIF `process_flag(trap_exit, true)` (Chapter 13, "Error Handling Semantics"). A system process is a process that can receive and process error signals. When a system process receives an exit signal, the signal is converted into a message of the form `{'EXIT', Pid, Why}` and placed in its mailbox, rather than (for an abnormal reason) terminating the process. A process that traps exits acts as a *firewall*, stopping the propagation of errors through the system: linked processes downstream of it die, but the system process and processes beyond it survive. The kill signal (`exit(Pid, kill)`) is the one exception — it is untrappable even by a system process.

# Prerequisites

- **Process** — Trapping exits changes a process from normal to system type.
- **Link** — Exit signals arrive via links; trapping only matters for a linked process.
- **Exit signal** — Trapping converts these signals into messages; understand them first.

# Key Properties

1. `process_flag(trap_exit, true)` turns the current process into a system process.
2. A system process converts incoming exit signals into `{'EXIT', Pid, Why}` messages.
3. A trapping process does not die when a linked process exits abnormally — it receives a message instead.
4. A trapping process acts as a firewall, halting error propagation.
5. The kill signal (`exit(Pid, kill)`) bypasses trapping and always terminates the process.

# Construction / Recognition

## To Trap Exits:
1. In the process you want to make a system process, evaluate `process_flag(trap_exit, true)`.
2. Link to (or be linked from) the processes whose exits you want to observe.
3. Add a `receive` clause matching `{'EXIT', Pid, Why}` to handle the converted signal.

## To Recognize a Trapping Process:
1. Look for a call to `process_flag(trap_exit, true)` near the start of the process.
2. Look for `receive` clauses handling `{'EXIT', Pid, Why}` messages.

# Context & Application

- **Typical contexts**: Supervisor-style processes that must survive the death of their workers; processes that interface to ports.
- **Common applications**: Stopping error propagation at a chosen boundary (a firewall); the basis on which OTP supervisors are built.
- **Historical/stylistic notes**: The book draws the firewall as a double-circled node in its process diagrams.

# Examples

**Example 1** (Chapter 13, "Setting Up a Firewall"): `P3` evaluates `process_flag(trap_exit, true)` and becomes a system process. After `P9` crashes, the propagation of errors stops at `P3`, so `P1` and `P3` do not die — `P3` functions as a firewall.

**Example 2** (Chapter 15, the `example1` port driver): The port server process calls `process_flag(trap_exit, true)` so that if the external program crashes it receives `{'EXIT', Port, Reason}` and can exit cleanly with `{port_terminated, Reason}` instead of crashing silently.

# Relationships

## Builds Upon
- **Exit signal** — trapping changes how a process reacts to exit signals.
- **Link** — trapping is only meaningful for processes linked to others.

## Enables
- **Supervisor** — OTP supervisors are trapping processes that restart dead workers.

## Related
- **Error handling philosophy** — a trapping process is the "other process" that fixes errors.

## Contrasts With
- **Monitor** — a monitor delivers a `'DOWN'` message without requiring `trap_exit`; trapping exits is the link-based way to receive death notifications as messages.

# Common Errors

- **Error**: Expecting a trapping process to survive an `exit(Pid, kill)`.
  **Correction**: The kill signal is untrappable; nothing converts it to a message.
- **Error**: Forgetting to set `trap_exit` before linking, then being surprised the process dies.
  **Correction**: Evaluate `process_flag(trap_exit, true)` before establishing links you want to observe.

# Common Confusions

- **Confusion**: A system process never terminates from exit signals.
  **Clarification**: It does not terminate from *trappable* signals, but the kill signal still terminates it.
- **Confusion**: Trapping exits is the same as monitoring.
  **Clarification**: Trapping works through bidirectional links and the `{'EXIT', ...}` message; monitoring is unidirectional and uses `'DOWN'` messages without `trap_exit`.

# Source Reference

Chapter 13: Errors in Concurrent Programs, section "Error Handling Semantics" (the "Processes" and "Receipt of an error signal" definitions), section "Setting Up a Firewall," and "Error Handling Primitives" (the `process_flag(trap_exit, true)` BIF). Also Chapter 15, "The Erlang Program" (`example1` port server).

# Verification Notes

- Definition source: Direct adaptation of the system-process definition and the "Setting Up a Firewall" section.
- Confidence rationale: HIGH — `process_flag(trap_exit, true)` and the firewall behavior are explicitly defined.
- Uncertainties: None.
- Cross-reference status: This is the canonical `trapping-exits` card. Other slugs match planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
