---
# === CORE IDENTIFICATION ===
concept: Benefits of Concurrency
slug: benefits-of-concurrency

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: rationale
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing Concurrency"
chapter_number: 1
pdf_page: null
section: "Benefits of Concurrency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - why concurrency
  - reasons for concurrent programming

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - concurrency-oriented-programming
  - concurrency-vs-parallelism
  - modeling-concurrency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why write concurrent programs?"
  - "What are the benefits of concurrency?"
  - "Why model real-world applications with concurrent programs?"
---

# Quick Definition

Concurrent programming brings four benefits: performance, scalability, fault tolerance, and clarity. These are the reasons Erlang programs are written as sets of communicating processes.

# Core Definition

"Concurrent programming can be used to improve performance, to create scalable and fault-tolerant systems, and to write clear and understandable programs for controlling real-world applications" (Chapter 1, "Benefits of Concurrency"). The chapter enumerates four benefits:

- **Performance** — On a parallel computer, independent tasks can run at the same time; "if you have a suitable problem and a computer with sixty-four cores, your program might go sixty-four times faster ... but only if you write a concurrent program." Erlang programs written for sequential machines years ago "now just run faster when we run them on modern multicores."
- **Scalability** — "Concurrent programs are made from small independent processes," so the system scales by adding more processes and CPUs; the Erlang VM "automatically distributes the execution of processes over the available CPUs."
- **Fault tolerance** — Built on "independence and hardware redundancy." Erlang programs are "made up of many small independent processes. Errors in one process cannot accidentally crash another process." Process independence and remote failure detection "are built into the Erlang VM."
- **Clarity** — "In the real world things happen in parallel"; mapping that real-world parallelism onto Erlang concurrency "results in clear and easily understood code."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Performance: a concurrent program can exploit multiple cores; a sequential one cannot.
2. Scalability: more processes and CPUs scale the system; the VM distributes processes automatically.
3. Fault tolerance: independent processes mean one process's error cannot crash another.
4. Clarity: concurrency lets code mirror real-world parallel structure.
5. Erlang has no problem parallelizing legacy code, unlike sequential languages.
6. Both process independence and remote failure detection are built into the Erlang VM.

# Construction / Recognition

## To Realize These Benefits:

1. Write the program as a concurrent program (sets of communicating processes), not sequential code.
2. For performance/scalability, decompose work into many small independent processes.
3. For fault tolerance, keep processes independent so failures are isolated.
4. For clarity, map each real-world concurrent entity onto a process.

# Context & Application

- **Typical contexts**: Justifying why a system should be built concurrently in Erlang.
- **Common applications**: Multicore performance scaling, fault-tolerant telecom and web systems, real-world control programs.
- **Historical/stylistic notes**: Erlang was designed for fault-tolerant telecommunications systems, "but the same technology can be applied equally well to building fault-tolerant scalable web systems or cloud services."

# Examples

**Example 1** (Chapter 1, "Benefits of Concurrency" — Performance): Task A takes ten seconds and task B fifteen; on one CPU together they take twenty-five seconds, but on two independent CPUs only fifteen — achievable only with a concurrent program.

**Example 2** (Chapter 1, "Benefits of Concurrency" — Fault tolerance): "Errors in one process cannot accidentally crash another process"; to survive a whole-computer failure, the VM detects failures in remote computers.

# Relationships

## Builds Upon

- This is a foundational rationale and does not build upon another card in this source.

## Enables

- **Concurrency-oriented programming** — These benefits motivate structuring programs as communicating processes.

## Related

- **Concurrency vs. parallelism** — Performance benefits depend on parallel hardware.
- **Modeling concurrency** — Clarity comes from modeling real-world entities as processes.

## Contrasts With

- No directly contrasting concept in this chapter.

# Common Errors

- **Error**: Expecting a sequential program to gain the performance benefit on a multicore machine.
  **Correction**: Only a concurrent program can exploit extra cores.

- **Error**: Putting unrelated work in one process and expecting fault isolation.
  **Correction**: Fault tolerance depends on processes being small and independent so a crash stays contained.

# Common Confusions

- **Confusion**: Believing concurrency's only benefit is speed.
  **Clarification**: The book lists four benefits — performance, scalability, fault tolerance, and clarity.

- **Confusion**: Thinking fault tolerance is automatic regardless of design.
  **Clarification**: It rests on process independence and hardware redundancy; the design must keep processes independent.

# Source Reference

"Programming Erlang, Second Edition," Chapter 1: Introducing Concurrency, section "Benefits of Concurrency." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 1, "Benefits of Concurrency."
- Confidence rationale: HIGH — the four benefits are explicitly enumerated and described.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
