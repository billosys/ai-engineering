---
# === CORE IDENTIFICATION ===
concept: Parallelism
slug: parallelism

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: concurrency-model
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.1 Understanding concurrency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - in parallel
  - true parallel fashion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - concurrency
extends:
  - concurrency
related:
  - erlang-process
  - scheduler
  - symmetric-multiprocessing
contrasts_with:
  - concurrency

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is parallelism?"
  - "How does Erlang turn concurrency into parallelism?"
  - "What is the difference between parallelism and concurrency?"
---

# Quick Definition

Parallelism is the actual simultaneous execution of multiple tasks on separate CPUs, cores, or hyperthreads. Erlang automatically runs concurrent tasks in parallel when the hardware allows it.

# Core Definition

Parallelism is when concurrent tasks are physically executed at the same time on separate hardware resources (Chapter 1, section 1.1.1). The book distinguishes it from concurrency: concurrent tasks *could* happen at the same time, while parallelism is when they *do*. One of the nice things Erlang does is help with the physical execution of tasks — if extra CPUs, cores, or hyperthreads are available, Erlang uses them to run more concurrent tasks in parallel; if not, Erlang uses whatever CPU power exists to do them all a bit at a time. Programs automatically adapt to different hardware, running more efficiently with more CPUs as long as there are concurrent activities lined up.

# Prerequisites

- **Concurrency** — there must be concurrent (non-ordered) tasks before any of them can be run in parallel.

# Key Properties

1. Parallelism requires multiple physical execution resources (CPUs/cores/hyperthreads).
2. Erlang exploits parallelism transparently; the programmer does not write parallel-specific code.
3. A program runs the same on 1 core or 128 cores — only faster with more.
4. The benefit of parallel hardware is realized only if the program is split into concurrent tasks.

# Construction / Recognition

## To Identify/Recognize:
1. Determine whether the program has concurrent tasks available to run.
2. Observe whether the runtime has multiple schedulers/CPUs to assign them to.
3. If both hold, the runtime distributes the workload across CPUs automatically.

# Context & Application

- **Typical contexts**: Running Erlang systems on modern multicore hardware.
- **Common applications**: Scaling throughput by adding cores without code changes.
- **Historical/stylistic notes**: SMP support was added in May 2006 with release 11 of Erlang/OTP, enabling true parallel execution of Erlang processes.

# Examples

**Example 1** (section 1.1.1): Sorting two packs of cards "in true parallel fashion" if you have extra arms and eyes — performing both at once rather than interleaving them.

**Example 2** (Figure 1.1): Erlang processes running on uniprocessor versus multiprocessor hardware; the runtime distributes the workload over the available CPU resources.

# Relationships

## Builds Upon
- **Concurrency** — parallelism is the realized execution of concurrent tasks.

## Enables
- **Symmetric multiprocessing** — SMP support lets the runtime run processes in parallel.

## Related
- **Scheduler** — the schedulers distribute processes across CPUs.

## Contrasts With
- **Concurrency** — concurrency is potential simultaneity (a property of the problem); parallelism is actual simultaneity (a property of execution).

# Common Errors

- **Error**: Relying on timing effects observed on a single-core laptop.
  **Correction**: Multicore servers have less deterministic timing; test on representative hardware.

# Common Confusions

- **Confusion**: Believing you must explicitly program for parallel hardware in Erlang.
  **Clarification**: The runtime distributes concurrent work over CPUs automatically; you write ordinary concurrent code.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.1 "Understanding concurrency." See also Figure 1.1 and section 1.4.1 "The scheduler."

# Verification Notes

- Definition source: Synthesized from section 1.1.1 discussion contrasting concurrency and parallelism.
- Confidence rationale: HIGH — the distinction is explicitly drawn in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
