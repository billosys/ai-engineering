---
# === CORE IDENTIFICATION ===
concept: Erlang Process
slug: erlang-process

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
section: "1.1.2 Erlang's process model"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process
  - Erlang process model
  - actor

# === TYPED RELATIONSHIPS ===
prerequisites:
  - concurrency
extends: []
related:
  - process-spawning
  - message-passing
  - process-mailbox
  - pid
  - process-isolation
  - process-termination
contrasts_with:
  - os-thread

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang process?"
  - "What is the unit of concurrency in Erlang?"
  - "Why do processes encapsulate state?"
---

# Quick Definition

An Erlang process is the unit of concurrency: a lightweight, isolated agent running its own program code, with its own working memory and mailbox, sharing nothing with other processes.

# Core Definition

In Erlang, the unit of concurrency is the *process*. A process "represents an ongoing activity; it's an agent that is running a piece of program code, concurrent to other processes running their own code, at their own pace" (Chapter 1, section 1.1.2). Processes are likened to people: separate individuals who share nothing and are guaranteed not to disturb one another through their own internal state changes. Each process has its own working memory and its own mailbox for incoming messages. Whereas threads in many languages share memory, Erlang's processes can safely assume nobody else is changing their data — "we say that processes encapsulate state." Because processes cannot directly change each other's internal state, even buggy code in one process cannot corrupt another.

# Prerequisites

- **Concurrency** — the process is the concrete representation of a separate, concurrent task.

# Key Properties

1. The process is Erlang's unit of concurrency.
2. Each process has its own working memory and its own mailbox.
3. Processes share no internal data — they encapsulate their state.
4. Processes cannot corrupt one another's internal state, no matter how bad the code.
5. Because processes share no data, they communicate only by copying (message passing).
6. When a process finishes, its memory, mailbox, and resources are recycled automatically.

# Construction / Recognition

## To Construct/Create:
1. Identify a concurrent activity in the problem.
2. Spawn a process to run the code for that activity (see `process-spawning`).
3. The new process runs independently, at its own pace, with its own state.

# Context & Application

- **Typical contexts**: Modeling every independent activity in an Erlang system as its own process.
- **Common applications**: One process per web request, per connection, per session, per concurrent task.
- **Historical/stylistic notes**: Erlang's process model is an implementation of the actor model — independent agents communicating only by messages.

# Examples

**Example 1** (section 1.1.2, "Processes: an example"): A web server handles each incoming request in a separate process; the process's state is the request URL, who to reply to, and progress so far. When the request finishes, the process disappears and recycles its memory; if a bug crashes one request, only that process dies.

**Example 2** (section 1.1.1): Process isolation is compared to the isolation between a web browser and a word processor on a desktop — a crash in one cannot corrupt the other.

# Relationships

## Builds Upon
- **Concurrency** — a process is a concrete, separate concurrent task.

## Enables
- **Process spawning** — processes are created by spawning.
- **Message passing** — processes interact only through messages.
- **Process isolation** — each process has private memory.

## Related
- **Process mailbox** — each process owns a mailbox.
- **Pid** — each process is identified by a pid.

## Contrasts With
- **OS thread** — OS threads share memory and reserve megabytes of stack; Erlang processes share nothing and start with a few hundred bytes of stack.

# Common Errors

- **Error**: Sharing data between processes by reference and expecting in-place updates.
  **Correction**: Processes share nothing; communicate by sending message copies.

- **Error**: Forgetting to send a process's result before it terminates.
  **Correction**: A process that produces data for another must send it explicitly as a message before it dies.

# Common Confusions

- **Confusion**: Thinking Erlang processes are operating system threads.
  **Clarification**: They are implemented by the Erlang runtime system and are far more lightweight.

- **Confusion**: Believing processes can corrupt each other if code is buggy.
  **Clarification**: State encapsulation guarantees a process can only damage itself.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1 "Concurrent programming with processes," section 1.1.2 "Erlang's process model." See also the "Processes: an example" sidebar.

# Verification Notes

- Definition source: Direct adaptation of the process definition in section 1.1.2.
- Confidence rationale: HIGH — the book explicitly defines the process and the state-encapsulation property.
- Uncertainties: The "actor model" alias is well-established but the term itself is not used in this chapter.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
