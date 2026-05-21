---
# === CORE IDENTIFICATION ===
concept: Process
slug: process

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-model
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang process"
  - "lightweight process"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - spawn
  - message-passing
  - mailbox
  - process-identifier
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process in Erlang?"
  - "How are Erlang processes different from operating-system processes?"
  - "Why are Erlang processes considered cheap?"
---

# Quick Definition

An Erlang process is a small, self-contained virtual machine that evaluates Erlang functions concurrently. Processes share no memory and interact only through message passing.

# Core Definition

"Erlang concurrency is based on processes. These are small, self-contained virtual machines that can evaluate Erlang functions" (Armstrong, "Concurrent Programming," chapter introduction). Crucially, "In Erlang, processes belong to the programming language and not the operating system" — so they behave identically on every operating system, making concurrent code portable. Each process has its own private memory and an associated mailbox. "The only way for processes to interact is through message passing"; processes "share no memory and are completely independent."

# Prerequisites

This is a foundational concept — processes are the basis of all concurrent programming in Erlang and depend on no prior concurrency concept.

# Key Properties

1. A process is a small, self-contained virtual machine evaluating Erlang functions.
2. Processes belong to the language, not the OS — behavior is identical across operating systems.
3. Each process has its own private memory (its state) and an associated mailbox.
4. Processes share no memory and are completely independent.
5. The only interaction mechanism is message passing.
6. Creating and destroying processes — and sending messages — is very fast.
7. A system can have very large numbers of processes; the default `erlang:system_info(process_limit)` was 262,144, raisable with the `+P` flag.

# Construction / Recognition

## To Construct/Create:
1. Call `spawn/1` or `spawn/3` with the function the process should evaluate.
2. The new process runs in parallel with its creator and gets a fresh mailbox.
3. It terminates when its function returns (or it crashes).

## To Identify/Recognize:
1. A process is referred to by its Pid (process identifier), printed like `<0.36.0>`.
2. `erlang:system_info(process_limit)` reports how many processes the node allows.

# Context & Application

- **Typical contexts**: Every concurrent Erlang program; client/server designs, servers, workers.
- **Common applications**: Modeling independent real-world entities; running many tasks in parallel; tail-recursive server loops.
- **Historical/stylistic notes**: "Processes Are Cheap" — spawning 20,000 processes took about 3.0 µs of CPU time each on Armstrong's machine; "creating processes simplifies programming instead of complicating it."

# Examples

**Example 1** ("The Concurrency Primitives"): `Pid = spawn(area_server0, loop, [])` creates a process evaluating `area_server0:loop()`, returning a Pid printed as `<0.36.0>`.

**Example 2** ("Processes Are Cheap"): `processes:max(20000)` spawns 20,000 processes and reports a spawn time of 3.0 (3.4) microseconds each.

**Example 3** ("Processes Are Cheap"): `erlang:system_info(process_limit)` returns `262144` by default; starting with `erl +P 3000000` raises the limit (rounded up to the next power of two).

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Spawn** — `spawn` is the primitive that creates processes.
- **Message passing** — Processes interact by exchanging messages.
- **Mailbox** — Each process has a mailbox created with it.

## Related
- **Process identifier** — A process is addressed by its Pid.

## Contrasts With
- None — the source contrasts Erlang processes informally with OS processes rather than with a single named concept.

# Common Errors

- **Error**: Spawning more processes than physical memory can hold.
  **Correction**: Find how many processes fit in physical memory before swapping, and keep the program within that.

- **Error**: Exceeding `process_limit` and getting "Too many processes" / "a system limit has been reached."
  **Correction**: Raise the limit with `erl +P N`, or reduce the number of live processes.

# Common Confusions

- **Confusion**: Equating Erlang processes with operating-system processes or threads.
  **Clarification**: Erlang processes are language-level, far lighter, and behave identically on all operating systems.

- **Confusion**: Thinking processes can share data directly.
  **Clarification**: Processes share no memory; all interaction is by message passing.

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives" and "Processes Are Cheap." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes from the chapter introduction and "Processes Are Cheap."
- Confidence rationale: HIGH — the process concept is defined explicitly with measurements.
- Uncertainties: None.
- Cross-reference status: Canonical slug `process`; cross-refs verified.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
