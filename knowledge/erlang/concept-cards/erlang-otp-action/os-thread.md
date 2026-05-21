---
# === CORE IDENTIFICATION ===
concept: Operating System Thread
slug: os-thread

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-model
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.4 Programming with processes in Erlang"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - thread
  - OS thread

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - scheduler
  - symmetric-multiprocessing
contrasts_with:
  - lightweight-process
  - erlang-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an operating system thread?"
  - "How do OS threads differ from Erlang processes?"
  - "Why can't a 32-bit machine run many OS threads?"
---

# Quick Definition

An operating system thread is a concurrent activity provided by the OS that shares the same memory space as other threads and reserves a large stack. Erlang uses OS threads only to run its schedulers, not for user-level concurrency.

# Core Definition

The book describes OS threads as a point of contrast with Erlang processes. "Threads in many other programming languages and operating systems are concurrent activities that share the same memory space (and have countless opportunities to step on each other's toes)" (Chapter 1, section 1.1.2). A typical thread in a modern operating system "reserves some megabytes of address space for its stack (which means a 32-bit machine can never have more than a few thousand simultaneous threads), and it still crashes if it uses more stack space than expected" (section 1.1.4). ERTS runs as a single OS process and uses a small number of OS threads internally — one per scheduler — to run its many lightweight Erlang processes.

# Prerequisites

This is a foundational concept with no prerequisites within this source. (It is a contrast/background concept rather than a built concept of Erlang.)

# Key Properties

1. OS threads share the same memory space within a process.
2. Each thread reserves megabytes of address space for its stack.
3. A 32-bit machine can support only a few thousand simultaneous threads.
4. A thread crashes if it overruns its allotted stack space.
5. ERTS uses OS threads internally — one per scheduler — to host Erlang processes.

# Construction / Recognition

## To Identify/Recognize:
1. Look for concurrent activities that share a memory space.
2. Note large per-thread stack reservations and low practical thread counts.
3. In Erlang, OS threads appear only as scheduler threads inside ERTS.

# Context & Application

- **Typical contexts**: Concurrency in C, C++, Java, and similar imperative languages.
- **Common applications**: In Erlang, OS threads carry the schedulers; the I/O system also ran in a separate thread.
- **Historical/stylistic notes**: Originally ERTS used a single main thread; SMP support (release 11, May 2006) introduced multiple scheduler threads.

# Examples

**Example 1** (section 1.1.4): A modern OS thread reserves megabytes of address space for its stack, capping a 32-bit machine at a few thousand threads.

**Example 2** (section 1.4.1): As threads became available in operating systems, ERTS was changed to run things like the I/O system in a different thread, and later to use multiple scheduler threads.

# Relationships

## Builds Upon
- This is a background concept, not built from other Erlang concepts.

## Enables
- **Scheduler** — each Erlang scheduler runs on its own OS thread.
- **Symmetric multiprocessing** — multiple scheduler threads enable SMP.

## Related
- **Scheduler** — there is an n:m mapping of Erlang processes to OS threads.

## Contrasts With
- **Lightweight process** — Erlang processes are tiny and isolated; OS threads are heavy and share memory.
- **Erlang process** — the unit of user-level concurrency in Erlang is the process, not the OS thread.

# Common Errors

- **Error**: Trying to map each unit of Erlang concurrency to an OS thread.
  **Correction**: Many Erlang processes are multiplexed onto a few scheduler OS threads.

# Common Confusions

- **Confusion**: Believing Erlang has no relationship with OS threads at all.
  **Clarification**: ERTS uses OS threads for its schedulers and I/O; it just does not expose them as the unit of user concurrency.

# Source Reference

Chapter 1: The Erlang/OTP platform, sections 1.1.2, 1.1.4 "Programming with processes in Erlang," and 1.4.1 "The scheduler."

# Verification Notes

- Definition source: Synthesized from contrasting discussion in sections 1.1.2, 1.1.4, and 1.4.1.
- Confidence rationale: MEDIUM — the source describes OS threads only as a contrast, never defining them as a first-class topic.
- Uncertainties: None significant.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
