---
# === CORE IDENTIFICATION ===
concept: Modeling Concurrency
slug: modeling-concurrency

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: design-philosophy
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing Concurrency"
chapter_number: 1
pdf_page: null
section: "Modeling Concurrency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process modeling

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends:
  - concurrency-oriented-programming
related:
  - process
  - message-passing
  - spawn
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I identify the processes needed to solve a problem?"
  - "What must I know before writing concurrent programs?"
---

# Quick Definition

Modeling concurrency is the act of identifying the set of processes that will solve a problem. It is the concurrency equivalent of choosing the objects in an object-oriented design.

# Core Definition

"To write a concurrent program in Erlang, you must identify a set of processes that will solve your problem. We call this act of identifying the processes *modeling concurrency*" (Chapter 1, "Concurrent Programs and Parallel Computers"). The programming model "is based on observation of the real world": you create one module (process type) for each type of concurrent thing in the problem, and one process per real-world instance of that thing. The messages in the program "reflect the observed messages" between the real-world entities (Chapter 1, "Sending Messages"). Armstrong stresses that "choosing the correct processes can be difficult" and that "the difference between a good and bad process model can make or break a design."

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is presented in Chapter 1 before the reader has written any Erlang code.

# Key Properties

1. It is the first step in writing any concurrent Erlang program.
2. It is analogous to identifying objects in object-oriented design.
3. The number of process types equals the number of types of concurrent entity in the problem.
4. The number of processes of each type equals the number of real-world instances.
5. The messages in the model mirror the messages observed between real-world entities.
6. It is recognized as a hard design problem — a good or bad model can make or break the design.

# Construction / Recognition

## To Model Concurrency:
1. Observe the real-world problem and list the kinds of concurrent things in it.
2. Create one module for each kind of thing (e.g., `person`, `dog`, `rabbit`).
3. Add a top-level module (e.g., `world`) whose job is to start everything.
4. Spawn one process per real-world instance (four people => four `person` processes).
5. Define the messages each entity sends, mirroring real-world communication.

## To Recognize a Good Model:
1. Each process corresponds to one identifiable real-world concurrent entity.
2. Message types map cleanly onto observed real-world interactions.

# Context & Application

- **Typical contexts**: The opening design step of every concurrent Erlang program.
- **Common applications**: Simulations, control systems, multiuser systems — anything where real-world parallelism must be mapped to software.
- **Historical/stylistic notes**: Armstrong deliberately parallels object-oriented design: "Choosing the objects that are needed to solve a problem is recognized as being a hard problem ... The same is true in modeling concurrency."

# Examples

**Example 1** (Chapter 1, "Modeling Concurrency"): A scene with four people walking, two dogs, and many rabbits is modeled with four modules — `person`, `dog`, `rabbit`, and `world` — because there are three types of concurrent things plus a top-level starter.

**Example 2** (Chapter 1, "Sending Messages"): "We created two dog processes because there are two dogs, and we created four people processes because there were four people." One process per real-world instance.

# Relationships

## Builds Upon
- **Concurrency-oriented programming** — Modeling concurrency is the concrete first step of the COP philosophy.

## Enables
- **Spawn** — Once the model is chosen, `spawn` creates the processes it specifies.
- **Process** — The model determines which processes will exist.

## Related
- **Process** — The entities a model is composed of.
- **Message passing** — The model also specifies the messages between processes.
- **Spawn** — The primitive that brings the modeled processes to life.

## Contrasts With
- No directly contrasting concept in this source.

# Common Errors

- **Error**: Creating one process per *type* of thing but forgetting to spawn one per instance.
  **Correction**: Spawn as many processes as there are real-world instances (four people => four processes).

- **Error**: Skipping modeling and writing the program as a single monolithic process.
  **Correction**: Identify the concurrent entities first; that set of processes *is* the design.

# Common Confusions

- **Confusion**: Believing that more processes always means a better model.
  **Clarification**: A good model maps processes onto genuine real-world concurrent entities; arbitrary process counts do not improve the design.

- **Confusion**: Thinking modeling concurrency is automatic or obvious.
  **Clarification**: Armstrong explicitly calls it a hard problem — "choosing the correct processes can be difficult."

# Source Reference

"Programming Erlang, Second Edition," Chapter 1: Introducing Concurrency, sections "Modeling Concurrency" and "Concurrent Programs and Parallel Computers." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation from Chapter 1, "Concurrent Programs and Parallel Computers."
- Confidence rationale: HIGH — Armstrong explicitly names and defines "modeling concurrency."
- Uncertainties: None.
- Cross-reference status: Verified — `concurrency-oriented-programming`, `process`, `message-passing`, `spawn` are planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
