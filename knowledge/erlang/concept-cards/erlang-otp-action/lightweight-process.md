---
# === CORE IDENTIFICATION ===
concept: Lightweight Process
slug: lightweight-process

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - green process
  - cheap concurrency

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends:
  - erlang-process
related:
  - process-spawning
  - scheduler
  - erlang-runtime-system
contrasts_with:
  - os-thread

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why are Erlang processes called lightweight?"
  - "How do Erlang processes differ from OS threads?"
  - "How many processes can Erlang run?"
---

# Quick Definition

An Erlang process is lightweight: implemented by the runtime system rather than the OS, it starts with only a few hundred bytes of stack and a system can spawn hundreds of thousands of them.

# Core Definition

"Erlang processes are *not* operating system threads. They're much more lightweight, implemented by the Erlang runtime system, and Erlang is easily capable of spawning hundreds of thousands of processes on a single system running on commodity hardware" (Chapter 1, section 1.1.4). A typical OS thread reserves megabytes of address space for its stack (so a 32-bit machine can never have more than a few thousand threads) and crashes if it overruns. Erlang processes, by contrast, start with only a couple of hundred bytes of stack each, and grow or shrink automatically as required. Each process shares no memory with others and cannot be corrupted by another process dying.

# Prerequisites

- **Erlang process** — "lightweight" describes a property of the process.

# Key Properties

1. Implemented by the Erlang runtime system, not the operating system.
2. Each process starts with only a couple of hundred bytes of stack.
3. Stacks grow and shrink automatically as required.
4. A single system can spawn hundreds of thousands of processes on commodity hardware.
5. Each is fully isolated — no shared memory, no corruption from another's failure.

# Construction / Recognition

## To Identify/Recognize:
1. Note that the process is created with `spawn`, not an OS thread API.
2. Note the tiny initial stack and automatic growth.
3. Note that process counts in the hundreds of thousands are normal.

# Context & Application

- **Typical contexts**: Designing systems with one process per concurrent activity.
- **Common applications**: Massively concurrent servers; short-lived per-task processes.
- **Historical/stylistic notes**: Cheap concurrency is what makes Erlang's "spawn freely" design idiom practical.

# Examples

**Example 1** (section 1.1.4): A modern OS thread reserves megabytes of address space for its stack, limiting a 32-bit machine to a few thousand simultaneous threads.

**Example 2** (section 1.1.4): Erlang processes start with only a couple of hundred bytes of stack each and grow or shrink automatically.

# Relationships

## Builds Upon
- **Erlang process** — lightweight is a defining quality of the process.

## Enables
- **Process spawning** — cheapness makes liberal spawning practical.

## Related
- **Scheduler** — the runtime schedules many lightweight processes.
- **Erlang runtime system** — implements the lightweight process.

## Contrasts With
- **OS thread** — heavy, megabyte stacks, limited count, crashes on stack overrun.

# Common Errors

- **Error**: Treating processes as a scarce resource as with OS threads.
  **Correction**: Erlang processes are cheap; create one per concurrent activity without hesitation.

# Common Confusions

- **Confusion**: Believing an Erlang process maps to an OS thread.
  **Clarification**: Processes are implemented inside the runtime; many processes are multiplexed onto a few scheduler threads.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "Creating a process: spawning" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.4.
- Confidence rationale: HIGH — the lightweight property is explicitly described and contrasted with OS threads.
- Uncertainties: None.
- Cross-reference status: `os-thread` is referenced as a contrast concept; it is a planned card within this source.
- Re-extraction notes: Fresh extraction; no prior card.
