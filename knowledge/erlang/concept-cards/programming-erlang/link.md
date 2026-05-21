---
# === CORE IDENTIFICATION ===
concept: Link
slug: link

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
section: "Creating Links"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "process link"
  - "link/1"
  - "link set"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - spawn-link
  - exit-signal
  - trapping-exits
  - error-handling-philosophy
contrasts_with:
  - monitor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do links relate to process supervision?"
  - "What distinguishes a link from a monitor?"
  - "How do I make a group of processes that all die together?"
---

# Quick Definition

A link is a symmetric, bidirectional connection between two processes: if either linked process terminates, an error signal is sent to the other. Links are the foundation for groups of processes that all die together.

# Core Definition

Processes can be *linked*. If two processes `A` and `B` are linked and `A` terminates for any reason, an error signal will be sent to `B` — and the same the other way around (Chapter 13, "Error Handling Semantics"). The *link set* of a process `P` is the set of processes that are linked to `P`. Links are created with the BIF `link(Pid)`, which creates a link between the calling process and `Pid`. Links are symmetric: if process `A` evaluates `link(B)`, the net effect is the same as if `B` had evaluated `link(A)`. If `Pid` does not exist, `link/1` raises an exit `noproc` exception; if the link already exists, the call is ignored. Links are removed with `unlink(Pid)`.

# Prerequisites

- **Process** — A link connects two processes; you must understand processes and their PIDs first.

# Key Properties

1. Links are bidirectional (symmetric): death of either process informs the other.
2. `link(Pid)` connects the calling process and `Pid`; `unlink(Pid)` removes the link.
3. Linking is idempotent — relinking an already-linked pair is ignored.
4. `link/1` to a nonexistent process raises an `exit` exception with reason `noproc`.
5. When a process dies, error signals propagate along its link set; non-system processes receiving an abnormal signal also die, propagating further.
6. Links work transparently across machine boundaries.

# Construction / Recognition

## To Create a Link:
1. From the calling process, evaluate `link(Pid)` where `Pid` is the process to connect to.
2. Alternatively, use `spawn_link/1,3` to spawn and link atomically.

## To Recognize Linked Behavior:
1. Observe that when one process crashes, a connected process also dies (unless it traps exits).
2. The entire set of transitively linked processes dies together.

# Context & Application

- **Typical contexts**: Building groups of processes that should all live or die together; the basis for OTP supervision.
- **Common applications**: Worker pools where one failure should tear down the whole group; firewalls of processes that trap exits.
- **Historical/stylistic notes**: `spawn` and `link` were once separate primitives; `spawn_link` was added as an atomic operation to close a race where the spawned process died before `link` was called (Chapter 13 sidebar "Why Spawning and Linking Must Be an Atomic Operation").

# Examples

**Example 1** (Chapter 13, "Creating Links"): If `P1` calls `link(P3)`, a link is created between `P1` and `P3`. After `P1` calls `link(P3)`, `P3` calls `link(P10)`, and so on, `P1` has a link set of one element (`P3`) while `P3` has two (`P1` and `P10`).

**Example 2** (Chapter 13, "Groups of Processes That All Die Together"): When `P9` dies, error signals reach `P4` and `P10`; they die because they are not system processes, and the signals propagate until the entire group of linked processes dies.

# Relationships

## Builds Upon
- **Process** — links connect processes.

## Enables
- **Spawn-link** — the atomic spawn-and-link primitive.
- **Trapping exits** — trapping converts the link's error signal into a message.

## Related
- **Exit signal** — what propagates along links.
- **Error handling philosophy** — links are the observation mechanism behind remote error handling.

## Contrasts With
- **Monitor** — monitors are unidirectional and send a "down" message instead of an exit signal; the monitoring process need not be a system process.

# Common Errors

- **Error**: Using separate `spawn` then `link` calls, allowing the child to die in the gap before linking.
  **Correction**: Use `spawn_link` so spawning and linking are atomic.
- **Error**: Linking to a process that has already exited and not anticipating the `noproc` exception.
  **Correction**: Handle or expect the exit `noproc` exception from `link/1`.

# Common Confusions

- **Confusion**: Links are one-directional.
  **Clarification**: Links are symmetric; either process's death informs the other. Monitors are the one-directional variant.
- **Confusion**: A linked process always dies when its partner dies.
  **Clarification**: A process that has called `process_flag(trap_exit, true)` becomes a system process and receives an `{'EXIT', Pid, Why}` message instead of dying.

# Source Reference

Chapter 13: Errors in Concurrent Programs, sections "Error Handling Semantics," "Creating Links," "Groups of Processes That All Die Together," and "Error Handling Primitives" (the `link/1` and `unlink/1` BIFs).

# Verification Notes

- Definition source: Direct adaptation of the "Links" and "Link sets" definitions and the `link/1`/`unlink/1` BIF specs.
- Confidence rationale: HIGH — links are explicitly defined with semantics and BIF signatures.
- Uncertainties: None.
- Cross-reference status: This is the canonical `link` card. Other slugs match planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
