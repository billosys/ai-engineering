---
# === CORE IDENTIFICATION ===
concept: Small Messages, Big Computations
slug: small-messages-big-computations

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
section: "Small Messages, Big Computations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - granularity of concurrency
  - small messages big computations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
  - pmap
extends:
  - multicore-efficiency-rules
related:
  - smp-erlang
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why do some parallel Erlang programs scale better than others?"
  - "How does message size affect parallel speedup?"
---

# Quick Definition

"Small messages, big computations" is the multicore principle that parallel work scales best when each process receives a small message but performs a large computation on it.

# Core Definition

The fourth multicore efficiency rule is to "write 'small messages, big computations' code." The chapter measures this empirically by comparing `map` and `pmap` on two workloads: sorting (sending a 1,000-element list per process — a large message, a quick computation) and computing `fib(27)` (sending a tiny request, doing a large recursive computation). "Since there is little copying of data between processes in computing `fib(27)` and a relatively large amount of work involved, we would expect the second problem to perform better." The result: "CPU-bound computations with little message passing have linear speed-up, whereas lighter-weight computations with more message passing scale less well" ("Small Messages, Big Computations").

# Prerequisites

- **Message-passing** — The principle is about the ratio of message size to computation; understanding message copying is required.
- **pmap** — The principle is demonstrated by comparing `pmap` against `map` on two workloads.

# Key Properties

1. Each process should receive a small message and do a large computation on it.
2. Data copied between processes costs time; large messages reduce parallel speedup.
3. CPU-bound work with little message passing achieves near-linear speedup.
4. Lightweight work with heavy message passing scales poorly.
5. It is the fourth of the four multicore efficiency rules.

# Construction / Recognition

## To Construct/Create:
1. Structure parallel tasks so each process is dispatched a small request.
2. Ensure the computation each process performs is large relative to the message it received.
3. Avoid shipping large data structures between processes when a small descriptor would suffice.

## To Identify/Recognize:
1. A parallel program that scales near-linearly is doing big computations on small messages.
2. A program that scales poorly is likely copying large messages relative to the work done.

# Context & Application

- **Typical contexts**: Designing parallel computations for multicore and distributed Erlang.
- **Common applications**: Choosing whether to parallelize a workload — `fib(27)` over a list parallelizes well; sorting many large lists parallelizes less well.
- **Historical/stylistic notes**: "Ericsson is building commercial products that run almost twice as fast on dual-core processors." The chapter cautions not to read too much into the specific figures, as SMP Erlang changes daily.

# Examples

**Example 1** ("Small Messages, Big Computations" — `ptests.erl` test 1): Mapping `lists:sort/1` over 100 lists of 1,000 random integers each. `pmap` must send a large list to each process; the sort itself is quick. This is a large-message, small-computation workload that scales less well.

**Example 2** ("Small Messages, Big Computations" — `ptests.erl` test 2): Computing `fib(27)` 100 times via `lists:duplicate(100, 27)`. Each process receives the tiny request `27` but does a large recursive computation. This small-message, big-computation workload shows linear speedup.

# Relationships

## Builds Upon
- **Multicore efficiency rules** — This is the fourth rule, stated and measured in detail.

## Enables
- Informed decisions about which workloads to parallelize.

## Related
- **SMP Erlang** — The measurements use SMP Erlang run with varying numbers of schedulers.
- **pmap** — The abstraction used to demonstrate the principle.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Parallelizing a workload that ships large data structures between processes for cheap computation.
  **Correction**: Parallelize only when the computation per message is large relative to the data copied.

- **Error**: Assuming `pmap` always beats `map`.
  **Correction**: The sort benchmark shows large-message workloads scale poorly; measure before parallelizing.

# Common Confusions

- **Confusion**: Thinking parallel speedup depends only on the number of processes.
  **Clarification**: Speedup also depends on the ratio of message size to computation — message copying is a real cost.

# Source Reference

Chapter 26: Programming Multicore CPUs, Section "Small Messages, Big Computations." See the `ptests.erl` `test/1` listings and the `speed.png` figure.

# Verification Notes

- Definition source: Direct adaptation from "Small Messages, Big Computations" and the four-rule list.
- Confidence rationale: HIGH — the source names the principle as a rule and backs it with two measured benchmarks.
- Uncertainties: The specific speedup figures are version-dependent (the chapter says so explicitly).
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
