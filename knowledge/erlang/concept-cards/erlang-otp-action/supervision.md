---
# === CORE IDENTIFICATION ===
concept: Supervision
slug: supervision

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.2 Supervision and trapping of exit signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - supervisor
  - system process
  - worker process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - trapping-exit-signals
  - process-link
extends: []
related:
  - supervision-tree
  - let-it-crash
  - fault-tolerance
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is supervision in Erlang?"
  - "What is a supervisor?"
  - "What is the difference between a system process and a worker process?"
---

# Quick Definition

Supervision is the OTP approach to fault tolerance in which a special process — a supervisor — traps exit signals from a group of worker processes and restarts them when they fail.

# Core Definition

A signal-trapping *system process* "acts as a bulwark that prevents exit signals from propagating further, it insulates the processes it's linked to from each other and can also be entrusted with reporting failures and even restarting the failed subsystems... We call such processes *supervisors*" (Chapter 1, section 1.2.2). Supervisors typically run different code from ordinary *worker processes*, which do not trap signals. OTP lets a supervisor start its processes "in a prescribed manner and order," and be told how to restart processes relative to one another, how many restart attempts to make within a time period before giving up, and more — "all you need to do is to provide some parameters and hooks." The point of letting an entire subsystem terminate and restart is that it returns the system to a state known to function properly — like a fine-grained "reboot."

# Prerequisites

- **Trapping exit signals** — a supervisor must trap exit signals to detect failures.
- **Process link** — supervisors are linked to the processes they watch.

# Key Properties

1. A supervisor is a system process that traps exit signals.
2. It insulates the processes it is linked to and stops signal propagation.
3. It reports failures and restarts failed subsystems.
4. Workers are ordinary processes that do not trap signals.
5. OTP supplies the supervisor methodology and battle-hardened libraries; the developer provides parameters and hooks.
6. Restarting a subsystem returns it to a known-good base state — a granular "reboot."

# Construction / Recognition

## To Construct/Create:
1. Designate a system process that traps exit signals.
2. Link it to the worker processes it supervises.
3. Specify start order, restart strategy, and restart-intensity limits.
4. On a worker crash, the supervisor restarts the prescribed group.

# Context & Application

- **Typical contexts**: OTP applications structured for fault tolerance.
- **Common applications**: Restarting crashed subsystems automatically; controlling and monitoring running systems.
- **Historical/stylistic notes**: This chapter gives only an introductory treatment; the full `supervisor` behaviour is covered in later chapters.

# Examples

**Example 1** (Figure 1.3): A crash in one worker process is propagated to the other linked processes until it reaches the supervisor, which restarts the group; another group under the same supervisor is unaffected.

**Example 2** (section 1.2.2): The book compares a subsystem restart to rebooting a computer — but more granular, so only a part of the system is "rebooted," and the smaller the better.

# Relationships

## Builds Upon
- **Trapping exit signals** — supervisors are signal-trapping system processes.

## Enables
- **Supervision tree** — supervisors are layered into a tree.

## Related
- **Let it crash** — supervision provides the recovery half of let-it-crash.
- **Fault tolerance** — supervision is a main OTP fault-tolerance mechanism.
- **Supervisor** — the concrete OTP `supervisor` behaviour (covered in a later chapter).

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Implementing supervisors from scratch.
  **Correction**: OTP provides a methodology and battle-hardened libraries; supply parameters and hooks instead.

# Common Confusions

- **Confusion**: Believing workers and supervisors run the same kind of code.
  **Clarification**: Supervisors are system processes that trap signals; workers are ordinary processes that do not.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.2.2 "Supervision and trapping of exit signals." See Figure 1.3.

# Verification Notes

- Definition source: Direct adaptation from section 1.2.2.
- Confidence rationale: HIGH — supervisors, system processes, and workers are explicitly defined here (introductory treatment).
- Uncertainties: Detailed `supervisor` behaviour belongs to a later chapter and is owned by another agent.
- Cross-reference status: `supervisor` is a planned slug owned by another agent.
- Re-extraction notes: Fresh extraction; no prior card.
