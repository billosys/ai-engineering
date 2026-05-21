---
# === CORE IDENTIFICATION ===
concept: spawn_monitor
slug: spawn-monitor

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-creation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Error Handling Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "spawn_monitor/1"
  - "spawn_monitor/3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - spawn
  - monitor
extends:
  - spawn
related:
  - spawn-link
  - keep-alive-process
contrasts_with:
  - spawn-link

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I spawn a process and monitor it atomically?"
  - "How do I get a reference to a monitored process?"
  - "What distinguishes spawn_monitor from spawn_link?"
---

# Quick Definition

`spawn_monitor` creates a new process and atomically sets up a monitor on it, returning `{Pid, Ref}` — the new process's identifier and a reference to the monitor.

# Core Definition

`spawn_monitor(Fun)` and `spawn_monitor(Mod, Func, Args)` are like `spawn_link`, but they create a *monitor* rather than a *link* (Chapter 13, "Error Handling Primitives"). The call returns `{Pid, Ref}`, where `Pid` is the process identifier of the newly created process and `Ref` is a reference to the monitor. If the process dies with reason `Why`, the message `{'DOWN', Ref, process, Pid, Why}` is sent to the parent process. Because it creates a monitor, the parent does not need to be a system process to be informed of the child's death.

# Prerequisites

- **Process** — `spawn_monitor` creates a process.
- **Spawn** — `spawn_monitor` is `spawn` plus an atomic monitor.
- **Monitor** — The monitor semantics (unidirectional, `'DOWN'` message) must be understood.

# Key Properties

1. Creates a new process and atomically monitors it.
2. Returns `{Pid, Ref}` rather than just `Pid`.
3. The monitor is unidirectional — only the parent is informed.
4. A child death sends `{'DOWN', Ref, process, Pid, Why}` to the parent.
5. The parent need not call `process_flag(trap_exit, true)`.

# Construction / Recognition

## To Use spawn_monitor:
1. Call `{Pid, Ref} = spawn_monitor(fun() -> ... end)` or with `Mod, Func, Args`.
2. Add a `receive` clause matching `{'DOWN', Ref, process, Pid, Why}`.

## To Recognize It:
1. Look for `{Pid, Ref} = spawn_monitor(...)` bindings.
2. Look for a paired `'DOWN'` message handler.

# Context & Application

- **Typical contexts**: Asymmetric supervision where a parent watches a child but should not die with it.
- **Common applications**: Restart-on-death utilities; the chapter mentions `spawn_monitor` alongside `spawn` and `register` as primitives to combine carefully.
- **Historical/stylistic notes**: Combining `spawn`, `spawn_monitor`, and `register` requires care to avoid race conditions.

# Examples

**Example 1** (Chapter 13, "Error Handling Primitives"): The spec states that if the process dies with reason `Why`, the message `{'DOWN', Ref, process, Pid, Why}` is sent to the parent process.

**Example 2** (Chapter 13, "Making a Process That Never Dies"): The chapter warns that when combining the primitives `spawn`, `spawn_monitor`, and `register`, you must think carefully about race conditions.

# Relationships

## Builds Upon
- **Spawn** — `spawn_monitor` extends `spawn` with an atomic monitor.

## Enables
- **Keep-alive process** — restart-on-death utilities can be built with `spawn_monitor`.

## Related
- **Monitor** — `spawn_monitor` produces the monitor that delivers `'DOWN'` messages.

## Contrasts With
- **spawn-link** — `spawn_link` creates a bidirectional link and returns `Pid`; `spawn_monitor` creates a unidirectional monitor and returns `{Pid, Ref}`.

# Common Errors

- **Error**: Pattern-matching the result as a bare `Pid`.
  **Correction**: `spawn_monitor` returns the tuple `{Pid, Ref}`; bind both.
- **Error**: Setting `trap_exit` expecting an `{'EXIT', ...}` message.
  **Correction**: `spawn_monitor` delivers a `'DOWN'` message; match that instead.

# Common Confusions

- **Confusion**: `spawn_monitor` links parent and child.
  **Clarification**: It creates a monitor, which is unidirectional; the parent is not killed by the child's death.
- **Confusion**: `spawn_monitor` and `spawn_link` return the same thing.
  **Clarification**: `spawn_monitor` returns `{Pid, Ref}`; `spawn_link` returns just `Pid`.

# Source Reference

Chapter 13: Errors in Concurrent Programs, section "Error Handling Primitives" (the `spawn_monitor/1` and `spawn_monitor/3` specs); cautionary note in "Making a Process That Never Dies."

# Verification Notes

- Definition source: Direct adaptation of the `spawn_monitor` BIF specs.
- Confidence rationale: HIGH — `spawn_monitor` is explicitly specified with its return value and `'DOWN'` message.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `spawn`/`monitor` and planned `spawn-link`/`keep-alive-process` cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
