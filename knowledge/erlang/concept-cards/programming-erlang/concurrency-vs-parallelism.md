---
# === CORE IDENTIFICATION ===
concept: Concurrency vs. Parallelism
slug: concurrency-vs-parallelism

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: terminology
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing Concurrency"
chapter_number: 1
pdf_page: null
section: "Concurrent Programs and Parallel Computers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - concurrent vs parallel
  - parallel computer

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - concurrency-oriented-programming
  - process
contrasts_with:
  - modeling-concurrency

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between concurrency and parallelism?"
  - "What distinguishes a concurrent program from a parallel computer?"
---

# Quick Definition

Concurrency is a property of software — a program structured as communicating processes; parallelism is a property of hardware — a computer with more than one CPU or core. A concurrent program can run on a single core; it only runs *in parallel* on a parallel computer.

# Core Definition

Armstrong draws a precise distinction (Chapter 1, "Concurrent Programs and Parallel Computers"):

- "A *concurrent program* is a program written in a concurrent programming language. We write concurrent programs for reasons of performance, scalability, or fault tolerance."
- "A *concurrent programming language* is a language that has explicit language constructs for writing concurrent programs."
- "A *parallel computer* is a computer that has several processing units (CPUs or cores) that run at the same time."

The summary: "Concurrency has to do with software structure; parallelism has to do with hardware." On a single-core computer you can never run a *parallel* program, but you can run a *concurrent* program — "the computer time-shares between the different tasks, maintaining the illusion that the different tasks run in parallel" (Chapter 1, opening).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is part of the vocabulary Armstrong establishes before any Erlang programming.

# Key Properties

1. Concurrency is a software-structure property; parallelism is a hardware property.
2. A concurrent program can run on a single-core machine via time-sharing.
3. A parallel program *requires* a parallel computer (multiple CPUs/cores).
4. A concurrent program *may* run in parallel when placed on a parallel computer.
5. Whether a concurrent program actually runs in parallel is sometimes outside the programmer's control (the OS may disable cores; a cloud may migrate computations).
6. We write concurrent programs for performance, scalability, or fault tolerance.

# Construction / Recognition

## To Distinguish the Two:
1. Ask whether the property concerns how the *program* is written (concurrency) or how the *hardware* is built (parallelism).
2. If the term describes language constructs or process structure, it is concurrency.
3. If the term describes CPUs/cores running simultaneously, it is parallelism.

## To Recognize Genuine Parallel Execution:
1. Confirm the hardware has more than one core/CPU.
2. Note that even then, actual parallel execution is not guaranteed.

# Context & Application

- **Typical contexts**: Reasoning about why an Erlang program might or might not speed up on a given machine.
- **Common applications**: Multicore computers, networked clusters, cloud deployments.
- **Historical/stylistic notes**: Armstrong is "pedantic" here on purpose, because in everyday language "concurrent," "simultaneous," and "parallel" mean almost the same thing, but precise programming discussion requires the distinction.

# Examples

**Example 1** (Chapter 1, opening): "If we have only a single-core computer, then we can never run a parallel program on it ... We can, however, run concurrent programs on a single-core computer."

**Example 2** (Chapter 1, "Benefits of Concurrency"): Task A takes ten seconds and task B fifteen seconds. On one CPU, A and B together take twenty-five seconds; on two independent CPUs they take only fifteen — but achieving that speedup requires writing a concurrent program.

# Relationships

## Builds Upon
- This is foundational terminology and does not build upon another card in this source.

## Enables
- **Concurrency-oriented programming** — Understanding the distinction underpins the COP philosophy.

## Related
- **Concurrency-oriented programming** — COP produces concurrent programs whose parallelism depends on the hardware.
- **Process** — The unit of concurrency in Erlang.

## Contrasts With
- **Modeling concurrency** — Modeling is about structuring software (concurrency); this card additionally separates that from the hardware notion of parallelism.

# Common Errors

- **Error**: Expecting a sequential program to speed up just by running it on a multicore machine.
  **Correction**: Only a *concurrent* program can exploit extra cores; legacy sequential code does not.

- **Error**: Assuming a concurrent program always runs in parallel.
  **Correction**: Parallel execution depends on hardware and runtime decisions outside the programmer's control.

# Common Confusions

- **Confusion**: Treating "concurrent" and "parallel" as synonyms.
  **Clarification**: Concurrency is a property of how the program is written; parallelism is a property of the computer it runs on.

- **Confusion**: Believing single-core machines cannot run concurrent programs.
  **Clarification**: They can — the OS or VM time-shares between tasks, giving the illusion of simultaneity.

# Source Reference

"Programming Erlang, Second Edition," Chapter 1: Introducing Concurrency, sections "Concurrent Programs and Parallel Computers" and "Sequential vs. Concurrent Programming Languages." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 1, "Concurrent Programs and Parallel Computers."
- Confidence rationale: HIGH — the source gives explicit bulleted definitions.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
