---
# === CORE IDENTIFICATION ===
concept: Concurrency-Oriented Programming
slug: concurrency-oriented-programming

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: concurrency-model
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Real-World Concurrency"
chapter_number: 11
pdf_page: null
section: "Real-World Concurrency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "COP"
  - "concurrency-oriented programming"
  - "concurrent programming model"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - process
  - message-passing
  - link
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is concurrency-oriented programming?"
  - "Why model real-world applications with concurrent processes?"
  - "What must I know before writing concurrent programs?"
---

# Quick Definition

Concurrency-oriented programming is Erlang's model in which a program is many independent processes, each with private memory, that interact only by sending messages — just as people in a room communicate by talking.

# Core Definition

Armstrong names the model "concurrency-oriented programming" and summarizes it through three observations (Armstrong, "Real-World Concurrency"): (1) "Erlang programs are made of lots of processes. These processes can send messages to each other." (2) "These messages may or may not be received and understood. If you want to know whether a message was received and understood, you must send the process a message and wait for a reply." (3) "Pairs of processes can be linked. If one of the processes in a linked pair dies, the other process in the pair will be sent a message containing the reason why the first process died." The model rests on the fact that "the world is parallel" — real-world entities act independently, so programs that mirror the world should have a concurrent structure.

# Prerequisites

This is a foundational concept — Armstrong's "Real-World Concurrency" chapter deliberately steps back from programming to motivate the model before any concurrency primitives are introduced.

# Key Properties

1. A program is composed of many — dozens to hundreds of thousands of — small, independent processes.
2. Processes share no memory; each has its own private memory (state).
3. The only way to change another process's memory is to send it a message.
4. Message delivery is not acknowledged; to confirm receipt you must ask and await a reply.
5. With no shared memory there are no locks and no keys — and so none to lose.
6. Processes can be linked; when a linked process dies, its partner is told why.
7. The model maps directly onto how people interact: talking is messaging, having children is `spawn`, dying is a process exit.

# Construction / Recognition

## To Construct/Create:
1. Decompose the problem into independent real-world-like entities.
2. Make each entity a process with its own private state.
3. Have entities interact solely by sending messages.
4. Link processes that must clean up after one another's failures.

## To Identify/Recognize:
1. A design built from many isolated processes communicating by messages — with no shared state and no locks — follows the model.
2. The use of links for failure notification is characteristic.

# Context & Application

- **Typical contexts**: Modeling real-world systems whose components naturally act in parallel.
- **Common applications**: Scaling by adding processes ("get more people"); managing groups by broadcasting messages.
- **Historical/stylistic notes**: Armstrong argues most real-world applications are wrongly written in sequential languages; a concurrent language makes them "a lot easier." The next chapters introduce the three primitives `spawn`, `send`, and `receive`, and (Chapter 13) links and exits.

# Examples

**Example 1** ("Real-World Concurrency"): The Sue/Bill telephone-number dialogue — Sue tells Bill a number, then asks "Did you hear me?"; Bill echoes it back — illustrates that confirmation requires an explicit reply message.

**Example 2** ("Real-World Concurrency"): A room of people all chattering models an Erlang program of many processes; shouting instructions at the room models broadcasting.

**Example 3** ("Real-World Concurrency"): Jane and John, each assigned to clean up if the other dies, illustrate linked processes and error detection.

# Relationships

## Builds Upon
- This is foundational; it motivates, rather than builds upon, the concurrency primitives.

## Enables
- **Process** — The model is realized as Erlang processes.
- **Message passing** — Inter-process communication in the model.
- **Link** — Failure notification between paired processes.

## Related
- **Process**, **Message passing**, **Link** — the concrete mechanisms that implement the model.

## Contrasts With
- None — the chapter contrasts the model informally with shared-memory/lock-based programming, not with a single named concept.

# Common Errors

- **Error**: Assuming a sent message was received and acted upon.
  **Correction**: Delivery is unacknowledged; send a query and wait for a reply to confirm.

- **Error**: Reaching for shared mutable state to coordinate processes.
  **Correction**: Processes share no memory; coordinate by message passing instead.

# Common Confusions

- **Confusion**: Thinking concurrency-oriented programming is hard, like thread programming with locks.
  **Clarification**: With no shared memory there are no locks, race conditions, or memory corruption — Armstrong stresses "programming with processes is easy."

- **Confusion**: Believing the model is only about performance.
  **Clarification**: Its primary motivation is that it mirrors how the real world (and people) actually work, making programs easier to understand, manage, and scale.

# Source Reference

Chapter 11: "Real-World Concurrency" (the whole chapter; opening of Part 3, "Concurrent and Distributed Programs"). EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the chapter's named "concurrency-oriented programming" model and its three summary points.
- Confidence rationale: HIGH — the chapter names and explains the model explicitly.
- Uncertainties: None.
- Cross-reference status: Canonical slugs `process`, `message-passing`, `link` used; verified against the KB.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
