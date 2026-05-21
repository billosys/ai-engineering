---
# === CORE IDENTIFICATION ===
concept: Scheduler
slug: scheduler

# === CLASSIFICATION ===
category: performance
subcategory: runtime-system
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.4.1 The scheduler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process scheduler
  - ERTS scheduler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
  - erlang-process
extends: []
related:
  - symmetric-multiprocessing
  - io-and-scheduling
  - parallelism
  - garbage-collector
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang scheduler?"
  - "How does the scheduler map processes to CPUs?"
  - "What is the n:m mapping between processes and OS threads?"
---

# Quick Definition

The scheduler is the ERTS subsystem that runs Erlang's processes, sharing the available CPU resources among ready-to-run processes and waking sleeping processes on a new message or timeout.

# Core Definition

The process scheduler in ERTS "handles the running of Erlang's processes, allowing all the ready-to-run processes to share the available CPU resources, and waking up sleeping processes when they get a new message or a timeout happens" (Chapter 1, section 1.4). Originally there was one scheduler making lightweight processes run concurrently on a single CPU. With SMP support (release 11, May 2006), ERTS can run multiple process schedulers internally, each using a separate OS thread. This gives an *n:m* mapping between Erlang processes and OS threads: each scheduler handles a pool of processes, at most *m* processes run in parallel (one per scheduler thread), and processes can be moved between pools to balance work. Processes can even be tied to schedulers according to CPU topology to exploit cache architecture (section 1.4.1).

# Prerequisites

- **Erlang runtime system** — the scheduler is an ERTS subsystem.
- **Erlang process** — the scheduler runs processes.

# Key Properties

1. The scheduler runs Erlang processes and shares CPU resources among ready-to-run ones.
2. It wakes sleeping processes on a new message or a timeout.
3. With SMP, ERTS uses multiple schedulers, each on its own OS thread.
4. There is an n:m mapping between Erlang processes and OS threads.
5. At most m processes run in parallel — one per scheduler thread.
6. Processes can be moved between scheduler pools to balance the workload.

# Construction / Recognition

## To Identify/Recognize:
1. ERTS starts a pool of schedulers, by default one per available core.
2. Each scheduler owns a pool of processes and time-shares among them.
3. Work is rebalanced across schedulers automatically.

# Context & Application

- **Typical contexts**: Every running Erlang system.
- **Common applications**: Spreading concurrent work over CPUs without programmer effort — "a single core or 128 cores, it works the same, only faster."
- **Historical/stylistic notes**: Before SMP, using multiple cores required running multiple ERTS instances on one machine.

# Examples

**Example 1** (section 1.4.1): Each scheduler handles a pool of processes; processes within a pool share their time as when there was one scheduler, and at most m run in parallel.

**Example 2** (section 1.4.1): In the latest releases it is possible to tie processes to schedulers depending on the machine's CPU topology, to make better use of the cache architecture.

# Relationships

## Builds Upon
- **Erlang runtime system** — the scheduler lives inside ERTS.

## Enables
- **Parallelism** — multiple schedulers run processes in parallel.
- **I/O and scheduling** — the scheduler integrates the event-based I/O subsystem.

## Related
- **Symmetric multiprocessing** — SMP support introduced multiple schedulers.
- **Garbage collector** — the scheduler knows when a process last ran, helping skip GC.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Relying on timing effects observed with a single scheduler on a laptop.
  **Correction**: Multi-scheduler servers have less deterministic timing; test on representative hardware.

# Common Confusions

- **Confusion**: Believing each Erlang process gets its own OS thread.
  **Clarification**: Many processes share each scheduler; the mapping of processes to OS threads is n:m.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4 (overview) and section 1.4.1 "The scheduler." See Figure 1.1.

# Verification Notes

- Definition source: Direct adaptation from sections 1.4 and 1.4.1.
- Confidence rationale: HIGH — the scheduler and the n:m mapping are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
