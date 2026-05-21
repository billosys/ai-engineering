---
# === CORE IDENTIFICATION ===
concept: Process Isolation
slug: process-isolation

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: isolation
tier: foundational

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
  - state encapsulation
  - process separation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends:
  - erlang-process
related:
  - garbage-collector
  - fault-tolerance
  - message-passing
  - let-it-crash
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is process isolation in Erlang?"
  - "Why can't one Erlang process corrupt another?"
  - "How does process isolation help garbage collection?"
---

# Quick Definition

Process isolation is the property that each Erlang process has its own private memory, so no process can read or corrupt another's internal state. It underpins both fault tolerance and efficient garbage collection.

# Core Definition

Process isolation means each Erlang process has its own areas of memory, allocated when the process is created and de-allocated when the process dies (Chapter 1, section 1.4.3). Because processes share no internal data, "no matter how bad the code is that a process is running, it can't corrupt the internal state of your other processes" (section 1.1.2). Isolation is what makes "let it crash" safe: a process encapsulates all its state and can die without corrupting the rest of the system. It also makes garbage collection efficient — each process can be paused individually for GC while others keep running, each process's memory is usually small and fast to traverse, and the scheduler can skip processes that have not run since their last collection.

# Prerequisites

- **Erlang process** — isolation is a property of how processes are constructed.

# Key Properties

1. Each process owns private memory not shared with any other process.
2. A process's memory is allocated at creation and de-allocated at death.
3. A buggy or crashing process cannot corrupt another process's state.
4. Each process can be garbage collected independently while others keep running.
5. Short-lived processes can spawn, work, and die without ever triggering GC.

# Construction / Recognition

## To Identify/Recognize:
1. Each process has separate memory regions managed by ERTS.
2. Communication crosses isolation boundaries only via copied messages.
3. Process death cleanly reclaims all of that process's resources.

# Context & Application

- **Typical contexts**: Designing fault-tolerant systems where failures must be contained.
- **Common applications**: Supervision trees rely on isolation so a crashed worker cannot poison its supervisor or siblings.
- **Historical/stylistic notes**: Isolation is one of the pillars enabling Erlang's fault tolerance and low-pause garbage collection.

# Examples

**Example 1** (section 1.1.1): The isolation between processes is compared to the isolation between a web browser and a word processor on a desktop.

**Example 2** (section 1.4.3): A process can be spawned, do its job, and die without triggering any garbage collection at all, acting as a short-lived, automatically allocated and de-allocated memory region.

# Relationships

## Builds Upon
- **Erlang process** — isolation is intrinsic to the process model.

## Enables
- **Fault tolerance** — contained failures cannot spread through shared state.
- **Garbage collector** — per-process memory enables independent, low-pause GC.
- **Let it crash** — crashing safely depends on isolation.

## Related
- **Message passing** — copying messages is the only way data crosses isolation boundaries.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a crash in one process can leave shared global state corrupted.
  **Correction**: Processes share no internal state; only the crashing process's memory is affected.

# Common Confusions

- **Confusion**: Thinking isolation is only about fault tolerance.
  **Clarification**: Isolation also makes garbage collection fast by keeping per-process heaps small and independently collectable.

# Source Reference

Chapter 1: The Erlang/OTP platform, sections 1.1.2 "Erlang's process model" and 1.4.3 "Process isolation and the garbage collector."

# Verification Notes

- Definition source: Synthesized from sections 1.1.2 and 1.4.3.
- Confidence rationale: HIGH — both the isolation property and its GC consequences are explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
