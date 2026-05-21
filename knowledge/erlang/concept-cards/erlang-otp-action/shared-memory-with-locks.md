---
# === CORE IDENTIFICATION ===
concept: Shared Memory with Locks
slug: shared-memory-with-locks

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-communication
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.3 Four process communication paradigms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - shared memory
  - locking
  - mutexes

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-communication-paradigms
extends:
  - process-communication-paradigms
related:
  - software-transactional-memory
contrasts_with:
  - message-passing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared memory with locks?"
  - "What are the drawbacks of locking?"
  - "Why does Erlang avoid shared memory with locks?"
---

# Quick Definition

Shared memory with locks is the mainstream process-communication paradigm in which processes read and write common memory cells, using locks to grant exclusive access for atomic operations.

# Core Definition

In this paradigm, one or more regular memory cells can be read or written by two or more processes in parallel (Chapter 1, section 1.1.3). To perform an *atomic* sequence of operations, a process must block all others from accessing the cells until it finishes; this is done with a *lock* — "a construct that makes it possible to restrict access to a single process at a time." Implementing locks needs memory-system support, typically special hardware instructions. Higher-level constructs (semaphores, monitors, mutexes) are built on basic locks. The book calls shared memory "the GOTO of our time": the current mainstream technique, used for a long time, with numerous ways to shoot yourself in the foot.

# Prerequisites

- **Process communication paradigms** — this is one of the four surveyed approaches.

# Key Properties

1. Multiple processes read/write common memory cells in parallel.
2. Atomic operation sequences require a lock to exclude other processes.
3. Locks need memory-system support, often hardware instructions.
4. Semaphores, monitors, and mutexes are higher-level constructs built on locks.
5. Correctness depends on complete cooperation: every process must request and release locks correctly.

# Construction / Recognition

## To Identify/Recognize:
1. Look for memory shared directly between concurrent processes.
2. Look for lock/unlock (or mutex/semaphore) operations guarding that memory.
3. Recognize the risk of deadlock as the number of cooperating processes grows.

# Context & Application

- **Typical contexts**: Most current mainstream and scripting languages; operating-system kernels.
- **Common applications**: Low-level synchronization where the book concedes it has a niche that probably cannot be replaced.
- **Historical/stylistic notes**: Its ubiquity is attributed to being easy to implement and non-intrusive on existing programming models; the book argues this widespread use has hurt our ability to reason about concurrency.

# Examples

**Example 1** (section 1.1.3): The book lists drawbacks — locks require overhead even when collisions are unlikely; they are points of contention; they may be left locked by failed processes; problems with locks are extraordinarily hard to debug.

**Example 2** (section 1.1.3): As the number of cooperating processes grows, a complex, unforeseeable deadlock becomes a real possibility — in many cases a certainty.

# Relationships

## Builds Upon
- **Process communication paradigms** — one of the four members.

## Enables
- Higher-level synchronization constructs (semaphores, monitors, mutexes).

## Related
- **Software transactional memory** — considered at its core a variant of shared memory with locks.

## Contrasts With
- **Message passing** — Erlang's paradigm, which avoids shared mutable state and locks entirely.

# Common Errors

- **Error**: Forgetting to release a lock, or failing while holding it.
  **Correction**: Locks left in a locked state by failed processes can cause havoc; the slightest cooperation failure breaks the scheme.

# Common Confusions

- **Confusion**: Believing higher-level constructs (mutexes, monitors) are a different paradigm.
  **Clarification**: They are built directly on basic locks and belong to the same shared-memory paradigm.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.3 "Four process communication paradigms," "Shared memory with locks" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.3.
- Confidence rationale: HIGH — explicitly defined and discussed with enumerated drawbacks.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
