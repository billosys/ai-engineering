---
# === CORE IDENTIFICATION ===
concept: Multicore Efficiency Rules
slug: multicore-efficiency-rules

# === CLASSIFICATION ===
category: performance
subcategory: parallelism
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Multicore CPUs"
chapter_number: 26
pdf_page: null
section: "How to Make Programs Run Efficiently on a Multicore CPU"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rules for running efficiently on a multicore
  - multicore performance rules

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - spawn
extends: []
related:
  - sequential-bottleneck
  - small-messages-big-computations
  - pmap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I do to make an Erlang program run efficiently on a multicore CPU?"
  - "Why might a sequential Erlang program not get faster on more cores?"
---

# Quick Definition

The multicore efficiency rules are the four things an Erlang program must do — use lots of processes, avoid side effects, avoid sequential bottlenecks, and write small-messages/big-computations code — to run efficiently on a multicore CPU.

# Core Definition

"If you want your application to run faster on a multicore CPU, you'll have to make sure that it has lots of processes, that the processes don't interfere with each other, and that you have no sequential bottlenecks in your program." The chapter states the rules explicitly: "To run efficiently, we have to do the following: Use lots of processes; Avoid side effects; Avoid sequential bottlenecks; Write 'small messages, big computations' code" ("How to Make Programs Run Efficiently on a Multicore CPU"). A monolithic sequential program that never calls `spawn` "might not go any faster."

# Prerequisites

- **Process** — The first rule is to use *lots* of processes; the concept of a process underpins all four rules.
- **Spawn** — Processes are created with `spawn`; a program with no `spawn` calls cannot parallelize.

# Key Properties

1. Rule 1 — **Use lots of processes**: keep all CPUs busy; "lots" means lots relative to the number of CPUs. Many processes statistically avoid one process hogging a CPU.
2. Rule 2 — **Avoid side effects**: side effects prevent concurrency; "variables that do not vary" are the key to faster multicore execution. In particular, do not write to shared `public` ETS/DETS tables.
3. Rule 3 — **Avoid sequential bottlenecks**: points where concurrent processes contend for a sequential resource (I/O, a registered process).
4. Rule 4 — **Write "small messages, big computations" code**: minimize data copied between processes relative to the work each does.
5. Processes should do similar amounts of work; one process doing most of the work is a bad design.
6. An Erlang program "might run n times faster on an n-core processor — without any changes" if it already follows the rules.

# Construction / Recognition

## To Construct/Create:
1. Decompose the problem into many independent processes (many relative to the core count).
2. Keep computations free of shared mutable state — avoid shared `public` ETS/DETS tables.
3. Identify and eliminate or redesign sequential bottlenecks; avoid unnecessary registered processes.
4. Structure work so messages are small and the computation per message is large.

## To Identify/Recognize:
1. A program that scales near-linearly with cores already follows the rules.
2. A program with one big sequential clump, no `spawn`, or heavy shared-table writes violates them.

# Context & Application

- **Typical contexts**: Tuning Erlang programs to exploit multicore and many-core CPUs.
- **Common applications**: "Intrinsically parallel" applications (e.g., a messaging system with tens of thousands of connections) get lots of processes for free.
- **Historical/stylistic notes**: "When work in Erlang started in 1985, we had no idea that parallel computers would be commonplace... When multicore CPUs arrived, we found that a lot of our programs just ran faster."

# Examples

**Example 1** ("How to Make Programs Run Efficiently..." sidebar): A 32-core CPU running 4 hyperthreads each gives ~128 threads; "a hundred times faster is within striking distance" if the rules are followed.

**Example 2** ("Use Lots of Processes"): A messaging system managing tens of thousands of simultaneous connections is "intrinsically parallel" — the concurrency comes free from the connections, and per-connection code need not worry about concurrency.

# Relationships

## Builds Upon
- This card aggregates the chapter's guidance; it builds on the process and spawn primitives.

## Enables
- **pmap** — A concrete technique for satisfying "use lots of processes."
- **mapreduce** — Another parallel abstraction built to follow these rules.

## Related
- **Sequential bottleneck** — Rule 3 is about eliminating these.
- **Small messages, big computations** — Rule 4, stated as its own card.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Writing one monolithic sequential program and expecting more cores to speed it up.
  **Correction**: Decompose into many independent processes; a program that never calls `spawn` will not scale.

- **Error**: Designing a few processes where one does most of the work.
  **Correction**: Use many processes that each do similar amounts of work.

# Common Confusions

- **Confusion**: Believing any Erlang program automatically runs faster on more cores.
  **Clarification**: Only programs that already use many independent, side-effect-free processes with no sequential bottlenecks scale; a monolithic program will not.

# Source Reference

Chapter 26: Programming Multicore CPUs, Sections "Good News for Erlang Programmers" and "How to Make Programs Run Efficiently on a Multicore CPU" (subsections "Use Lots of Processes," "Avoid Side Effects," "Avoid Sequential Bottlenecks").

# Verification Notes

- Definition source: Direct quote of the four-rule list from "How to Make Programs Run Efficiently on a Multicore CPU."
- Confidence rationale: HIGH — the source enumerates the rules explicitly and devotes a subsection to each.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
