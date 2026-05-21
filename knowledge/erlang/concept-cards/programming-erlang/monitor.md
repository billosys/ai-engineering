---
# === CORE IDENTIFICATION ===
concept: Monitor
slug: monitor

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-supervision
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Monitors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "process monitor"
  - "erlang:monitor/2"
  - "DOWN message"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - spawn-monitor
  - exit-signal
  - keep-alive-process
contrasts_with:
  - link

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a link from a monitor?"
  - "How do I perform an action when a process dies?"
  - "How do servers observe the behavior of clients?"
---

# Quick Definition

A monitor is a unidirectional observation relationship: if `A` monitors `B` and `B` dies, `A` receives a `'DOWN'` message — but not the other way around. The monitoring process need not become a system process.

# Core Definition

Monitors are similar to links but with significant differences. Monitors are *unidirectional*: if `A` monitors `B` and `B` dies, `A` is sent an exit (`'DOWN'`) message, but not the other way around. When a monitored process dies, a "down" message — not an exit signal — is sent to the monitoring process; this means the monitoring process does not have to become a system process in order to handle errors (Chapter 13, "Monitors"). A monitor is set up with `erlang:monitor(process, Item)`, where `Item` is a PID or registered name, and it returns a reference `Ref`. The message has the form `{'DOWN', Ref, process, Pid, Why}`. A monitor is removed with `demonitor(Ref)`.

# Prerequisites

- **Process** — A monitor observes a process; you must understand processes and PIDs first.

# Key Properties

1. Monitors are unidirectional — only the monitoring process is informed.
2. `erlang:monitor(process, Item)` returns a reference `Ref` identifying the monitor.
3. A dying monitored process sends `{'DOWN', Ref, process, Pid, Why}` to the monitor.
4. The monitoring process does NOT need to be a system process (no `trap_exit` required).
5. `demonitor(Ref)` removes a monitor.
6. Monitors are used for asymmetric error handling; links for symmetric error handling.

# Construction / Recognition

## To Set Up a Monitor:
1. From the observing process, evaluate `Ref = erlang:monitor(process, Pid)`.
2. Receive the `{'DOWN', Ref, process, Pid, Why}` message to react to the death.
3. Call `demonitor(Ref)` to stop monitoring.

## To Recognize Monitor Use:
1. Look for `receive` clauses matching `{'DOWN', Ref, process, Pid, Why}`.
2. Look for a process that is informed of another's death without itself dying.

# Context & Application

- **Typical contexts**: Asymmetric error handling — when one process needs to know about another's death but not vice versa.
- **Common applications**: Servers monitoring the behavior of clients; the `on_exit` utility that runs a function when a watched process dies.
- **Historical/stylistic notes**: Monitors avoid the need to set `process_flag(trap_exit, true)`, making one-way observation simpler than links.

# Examples

**Example 1** (Chapter 13, "Performing an Action When a Process Dies"): `on_exit(Pid, Fun)` spawns a process that does `Ref = monitor(process, Pid)`, then `receive {'DOWN', Ref, process, Pid, Why} -> Fun(Why) end`. When the watched process dies, `Fun(Why)` is invoked.

**Example 2** (Chapter 13, "Monitors"): The book notes monitors are "typically used by servers to monitor the behavior of clients."

# Relationships

## Builds Upon
- **Process** — monitors observe processes.

## Enables
- **Spawn-monitor** — the atomic spawn-and-monitor primitive.
- **Keep-alive process** — built on `on_exit`, which uses a monitor.

## Related
- **Exit signal** — the monitored process's exit reason `Why` is carried in the `'DOWN'` message.

## Contrasts With
- **Link** — links are bidirectional and send exit signals (which can kill non-system processes); monitors are unidirectional and send a `'DOWN'` message that does not kill the monitor.

# Common Errors

- **Error**: Expecting the monitored process to also be informed when the monitor dies.
  **Correction**: Monitors are one-way; use a link (or a second monitor) for bidirectional notification.
- **Error**: Setting `trap_exit` before using a monitor, believing it is required.
  **Correction**: Monitors deliver an ordinary message; no `trap_exit` is needed.

# Common Confusions

- **Confusion**: A monitor sends an exit signal.
  **Clarification**: A monitor sends a `'DOWN'` *message*, which an ordinary `receive` handles; it never kills the monitoring process.
- **Confusion**: A monitor and a link are interchangeable.
  **Clarification**: Choose a monitor for asymmetric observation and a link for symmetric "die together" semantics.

# Source Reference

Chapter 13: Errors in Concurrent Programs, sections "Error Handling Semantics" (the "Monitors" definition), "Monitors," and "Error Handling Primitives" (the `erlang:monitor/2` and `demonitor/1` BIFs); example in "Performing an Action When a Process Dies."

# Verification Notes

- Definition source: Direct adaptation of the "Monitors" section and the `erlang:monitor/2`/`demonitor/1` BIF specs.
- Confidence rationale: HIGH — monitors are explicitly defined and contrasted with links.
- Uncertainties: None.
- Cross-reference status: This is the canonical `monitor` card. Other slugs match planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
