---
# === CORE IDENTIFICATION ===
concept: Pid
slug: pid

# === CLASSIFICATION ===
category: data-types
subcategory: identifiers
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.7 Pids, ports, and references"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process identifier
  - process id

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
  - erlang-process
extends:
  - erlang-term
related:
  - process-spawning
  - send-operator
  - port-identifier
  - reference
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a pid?"
  - "How is a pid displayed?"
  - "How do you get the pid of the current process?"
---

# Quick Definition

A pid is a process identifier — a unique, opaque value identifying an Erlang process. It is the address used to send a process messages.

# Core Definition

"Every process has a unique identifier, usually referred to as a *pid*. Pids are a special data type in Erlang and should be thought of as opaque objects" (Chapter 2, section 2.2.7). When the shell prints a pid it shows three integers in angle brackets, as in `<0.35.0>`; this form is only for debugging — you cannot enter it to create a pid. Pids are expected to be unique for the lifetime of the system, though the same identifier may be reused after some hundred million processes have come and gone. The function `self()` always gives the pid of the process currently running (the one that called it).

# Prerequisites

- **Erlang term** — a pid is a kind of term.
- **Erlang process** — a pid identifies a process.

# Key Properties

1. A pid uniquely identifies an Erlang process.
2. Pids are a special, opaque data type.
3. The shell prints a pid as three integers in angle brackets, e.g. `<0.35.0>`.
4. You cannot construct a pid from its printed syntax.
5. Pids are expected to be unique for the system's lifetime; identifiers may eventually be reused.
6. `self()` returns the pid of the calling process.

# Construction / Recognition

## To Identify/Recognize:
1. A pid is produced by `spawn` (the new process's id) or `self()` (the caller's id).
2. The shell renders it as `<A.B.C>`.
3. It is opaque — treat it as a handle, not as numbers.

# Context & Application

- **Typical contexts**: Addressing processes for message sending; storing references to processes.
- **Common applications**: Passing `self()` to a spawned child so it can reply; linking and monitoring.
- **Historical/stylistic notes**: Even the Erlang shell is a process with its own pid — try `self()` in the shell.

# Examples

**Example 1** (section 2.2.7): The shell prints pids in the form `<0.35.0>` — three integers enclosed in angle brackets, shown for debugging only.

**Example 2** (section 2.2.7): Calling `self()` in the shell returns the shell's own pid, demonstrating that the shell is itself a process.

# Relationships

## Builds Upon
- **Erlang term** — a pid is a term.
- **Erlang process** — a pid is a process's identity.

## Enables
- **Send operator** — a pid is the destination of `Destination ! Message`.

## Related
- **Process spawning** — `spawn` returns a fresh pid.
- **Port identifier** and **reference** — closely related identifier data types.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to type `<0.35.0>` into the shell to construct a pid.
  **Correction**: The printed form is debug-only; you cannot create a pid from it. Obtain pids from `spawn` or `self()`.

# Common Confusions

- **Confusion**: Reading the three integers of a pid as meaningful numbers.
  **Clarification**: A pid is opaque; the printed integers are only for debugging comparison.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.7 "Pids, ports, and references," "Pids (process identifiers)" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.2.7.
- Confidence rationale: HIGH — pids are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `port-identifier` and `reference` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
