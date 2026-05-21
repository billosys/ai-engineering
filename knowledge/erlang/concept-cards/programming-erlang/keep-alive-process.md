---
# === CORE IDENTIFICATION ===
concept: Keep-Alive Process
slug: keep-alive-process

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: process-restart
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Programming for Fault Tolerance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "keep_alive/2"
  - "on_exit"
  - "process that never dies"
  - "restartable process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - monitor
  - spawn
extends: []
related:
  - let-it-crash
  - spawn-monitor
  - supervisor
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a process that restarts itself when it dies?"
  - "How do I perform an action when a process dies?"
  - "What is a race condition in process restart code?"
---

# Quick Definition

A keep-alive process is a registered process that is always alive — if it dies for any reason, an observing process detects the death (via a monitor) and immediately restarts it.

# Core Definition

A *keep-alive* process is a registered process that is always alive: if it dies for any reason, it is immediately restarted (Chapter 13, "Making a Process That Never Dies"). It is built from the utility `on_exit(Pid, Fun)`, which watches `Pid` and evaluates `Fun(Why)` if `Pid` exits with reason `Why`, using a monitor internally. The function `keep_alive(Name, Fun)` registers a process named `Name` that evaluates `spawn(Fun)`, and installs an `on_exit` handler that calls `keep_alive(Name, Fun)` again when the process dies — restarting it. The book notes a subtle *race condition*: the process can die in the gap between `register(...)` and the `on_exit` call, so the link inside `on_exit` is never created and restart fails; correct keep-alive code must be written so race conditions cannot happen.

# Prerequisites

- **Process** — A keep-alive process is a registered process being supervised.
- **Monitor** — `on_exit` uses a monitor to detect the watched process's death.
- **Spawn** — The process is (re)created with `spawn`.

# Key Properties

1. The kept-alive process is registered under a name so callers can always reach it.
2. An observer detects its death and restarts it immediately.
3. `on_exit(Pid, Fun)` runs `Fun(Why)` when `Pid` exits — the building block.
4. The restart handler is itself a recursive call to `keep_alive`.
5. There is a race condition between `register` and installing the handler — the process may die in the gap.

# Construction / Recognition

## To Construct a Keep-Alive Process:
1. Evaluate `register(Name, Pid = spawn(Fun))` to create and name the process.
2. Call `on_exit(Pid, fun(_Why) -> keep_alive(Name, Fun) end)` to reinstate it on death.
3. Be aware of the race between steps 1 and 2 and guard against it.

## To Recognize It:
1. Look for a registered process whose `on_exit`/monitor handler re-spawns it.
2. Look for recursive restart functions like `keep_alive/2`.

# Context & Application

- **Typical contexts**: Keeping a critical named service permanently available.
- **Common applications**: The book's `keep_alive(Name, Fun)`; restartable global processes.
- **Historical/stylistic notes**: This hand-rolled pattern is the conceptual precursor to OTP supervisors, which solve the restart problem robustly and configurably.

# Examples

**Example 1** (Chapter 13, "Making a Process That Never Dies"): `keep_alive(Name, Fun) -> register(Name, Pid = spawn(Fun)), on_exit(Pid, fun(_Why) -> keep_alive(Name, Fun) end).` This makes a registered process that is restarted whenever it dies.

**Example 2** (Chapter 13): The book highlights the race condition — if the process dies between `register(...)` and `on_exit(...)`, the link is not created and `on_exit` will not work as expected; this can happen if two programs evaluate `keep_alive` with the same `Name` at the same time.

# Relationships

## Builds Upon
- **Monitor** and **spawn** — the mechanisms `on_exit` and `keep_alive` are made of.

## Enables
- A precursor pattern that motivates OTP supervisors.

## Related
- **Let it crash** — restarting a crashed process is the natural complement of letting it crash.
- **spawn-monitor** — an atomic alternative for setting up the watch.

## Contrasts With
- **Supervisor** — OTP supervisors provide configurable, race-free restart strategies; the hand-rolled keep-alive process has a known race condition.

# Common Errors

- **Error**: Using separate `register` and `on_exit` calls, leaving a race window.
  **Correction**: Restructure so the watch is established before the process can die, or use an atomic primitive / OTP supervisor.
- **Error**: Two callers running `keep_alive` with the same `Name` simultaneously.
  **Correction**: Serialize creation of named processes to avoid the registration race.

# Common Confusions

- **Confusion**: A keep-alive process can never be lost.
  **Clarification**: The naive implementation has a race condition; it is not robust without extra care.
- **Confusion**: `keep_alive` is the same as an OTP supervisor.
  **Clarification**: It is a minimal hand-rolled illustration; supervisors add restart strategies, intensity limits, and race-free behavior.

# Source Reference

Chapter 13: Errors in Concurrent Programs, section "Programming for Fault Tolerance," subsections "Performing an Action When a Process Dies" (the `on_exit` function) and "Making a Process That Never Dies" (the `keep_alive` function and the race-condition discussion).

# Verification Notes

- Definition source: Direct adaptation of the `keep_alive` and `on_exit` code and surrounding discussion.
- Confidence rationale: HIGH — the keep-alive pattern, its code, and its race condition are explicitly presented.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `process`/`monitor`/`spawn`/`supervisor` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
