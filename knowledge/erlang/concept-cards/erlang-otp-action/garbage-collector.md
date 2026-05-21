---
# === CORE IDENTIFICATION ===
concept: Garbage Collector
slug: garbage-collector

# === CLASSIFICATION ===
category: performance
subcategory: memory-management
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.4.3 Process isolation and the garbage collector"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - GC
  - garbage collection
  - generational copying collector

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-isolation
  - erlang-runtime-system
extends: []
related:
  - scheduler
  - erlang-process
  - process-termination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang manage memory?"
  - "Why don't Erlang programs suffer long GC pauses?"
  - "What kind of garbage collector does Erlang use?"
---

# Quick Definition

The garbage collector is the ERTS subsystem that automatically reclaims unused memory. Erlang uses a per-process generational copying collector, which keeps GC pauses small.

# Core Definition

"Erlang manages memory automatically... There is no explicit de-allocation. Instead, a so-called *garbage collector* is used to regularly find and recycle unused memory" (Chapter 1, section 1.4.3). Erlang currently uses "a straightforward generational copying garbage collector." Erlang programs do not tend to suffer GC pauses, mostly because of process isolation: each process has its own memory, allocated when it is created and de-allocated when it dies. As a result (1) each process can be paused individually for GC while others keep running; (2) per-process memory is usually small and quick to traverse; and (3) the scheduler knows when a process last ran, so a process that has done no work since its last collection can be skipped. A short-lived process may even spawn, work, and die without triggering any GC at all.

# Prerequisites

- **Process isolation** — per-process memory is what makes GC low-pause.
- **Erlang runtime system** — the GC is an ERTS subsystem.

# Key Properties

1. Memory management is automatic; there is no explicit de-allocation.
2. Erlang uses a generational copying garbage collector.
3. Each process is garbage collected individually while others keep running.
4. Per-process heaps are usually small, so traversal is fast.
5. The scheduler lets the GC skip processes that have not run since their last collection.
6. A short-lived process can complete without ever triggering GC.

# Construction / Recognition

## To Identify/Recognize:
1. No `free`/`delete`-style calls appear in Erlang code.
2. GC runs per process, not stop-the-world across the whole system.
3. Pauses stay small because each process heap is small and independently collected.

# Context & Application

- **Typical contexts**: Every running Erlang system, especially soft real-time systems.
- **Common applications**: Maintaining soft real-time responsiveness while recycling memory.
- **Historical/stylistic notes**: GC algorithms are a large research field; the book stresses that Erlang's relatively simple implementation works well precisely because of process isolation.

# Examples

**Example 1** (section 1.4.3): In some cases a process can be spawned, do its job, and die again without triggering any garbage collection at all — acting as a short-lived memory region automatically allocated and de-allocated with no overhead.

**Example 2** (section 1.4.3): Because the scheduler knows when a process last ran, a process that has done no work since its last collection can be skipped by the GC.

# Relationships

## Builds Upon
- **Process isolation** — per-process heaps make low-pause GC possible.
- **Erlang runtime system** — the GC is part of ERTS.

## Enables
- Soft real-time responsiveness despite automatic memory management.

## Related
- **Scheduler** — informs the GC about when a process last ran.
- **Process termination** — a process's memory is de-allocated when it dies.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting global stop-the-world GC pauses as in some other languages.
  **Correction**: Erlang collects each process's small heap independently, keeping pauses small.

# Common Confusions

- **Confusion**: Thinking the simple collector implies poor performance.
  **Clarification**: Process isolation makes even a straightforward generational copying collector perform well, with small pauses.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4.3 "Process isolation and the garbage collector."

# Verification Notes

- Definition source: Direct adaptation from section 1.4.3.
- Confidence rationale: HIGH — the garbage collector and its per-process character are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
