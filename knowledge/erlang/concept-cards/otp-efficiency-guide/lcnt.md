---
# === CORE IDENTIFICATION ===
concept: lcnt
slug: lcnt

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Profiling"
chapter_number: null
pdf_page: null
section: "lcnt"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "lock counting"
  - "lock contention profiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
  - large-system-profiling
extends: []
related:
  - fprof
  - dbg-profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "What must I understand before profiling a large system?"
  - "How do I find lock contention in a parallel Erlang system?"
---

# Quick Definition

`lcnt` is an Erlang/OTP tool used to find contention points in the Erlang Run-Time System's internal locking mechanisms. It is useful for identifying bottlenecks in parallel interactions between processes, ports, ETS tables, and other concurrent entities.

# Core Definition

The Erlang Efficiency Guide describes lcnt in two places. The introductory listing states: "`lcnt` is used to find contention points in the Erlang Run-Time System's internal locking mechanisms. It is useful when looking for bottlenecks in interaction between processes, ports, ETS tables, and other entities that can be run in parallel."

The dedicated subsection adds: "`lcnt` is used to profile interactions between entities that run in parallel. For example if you have a process that all other processes in the system need to interact with (maybe it has some global configuration), then `lcnt` can be used to figure out if the interaction with that process is a problem." It further notes: "In the Erlang Run-Time System entities are only run in parallel when there are multiple schedulers. Therefore `lcnt` will show more contention points (and thus be more useful) on systems using many schedulers on many cores."

# Prerequisites

- **Profiling Strategy** -- Understanding the overall profiling approach and when lock contention is the suspected issue.
- **Large-System Profiling** -- lcnt is most relevant in large, multi-scheduler systems.

# Key Properties

1. Profiles interactions between entities that run in parallel.
2. Finds contention points in internal locking mechanisms.
3. Useful for bottlenecks involving processes, ports, ETS tables, and other parallel entities.
4. Shows more contention points on systems with many schedulers on many cores.
5. Only meaningful when multiple schedulers are active (entities are only parallel with multiple schedulers).
6. Profiles at the Erlang Run-Time System level (internal locks), not at the application level.

# Construction / Recognition

## To Use lcnt:
1. Ensure the system is running with multiple schedulers.
2. Start lcnt profiling (see `m:lcnt` manual page in Tools).
3. Run the workload that exhibits contention.
4. Stop profiling and analyze lock contention data.
5. Identify which locks have the highest contention.

## To Recognize When lcnt Is Appropriate:
1. Performance degrades as the number of schedulers/cores increases.
2. A shared resource (process, ETS table) is accessed by many concurrent processes.
3. You suspect lock contention rather than algorithmic or I/O bottlenecks.
4. The system uses many schedulers on many cores.

# Context & Application

Lock contention is a class of performance bottleneck unique to parallel and concurrent systems. In Erlang, the run-time system uses internal locks to coordinate access to shared resources. When multiple schedulers on multiple cores compete for the same lock, throughput can degrade despite having more computational resources available.

The source gives a practical example: "if you have a process that all other processes in the system need to interact with (maybe it has some global configuration), then `lcnt` can be used to figure out if the interaction with that process is a problem." This scenario -- a single shared resource accessed by many concurrent processes -- is the canonical use case for lcnt.

# Examples

**Example 1** (profiling.md, "lcnt"): The source describes a scenario where a process with global configuration is accessed by all other processes in the system. `lcnt` can determine whether this interaction pattern creates a lock contention problem.

**Example 2** (profiling.md, "lcnt"): The source notes that `lcnt` is more useful on systems using many schedulers on many cores, because entities are only run in parallel when multiple schedulers exist.

# Relationships

## Builds Upon
- **profiling-strategy** -- lcnt addresses a specific class of performance bottleneck
- **large-system-profiling** -- lock contention is primarily a concern in large, multi-core systems

## Enables
- Identification and resolution of parallel interaction bottlenecks

## Related
- **fprof** -- fprof can show time spent but cannot identify lock contention specifically
- **dbg-profiling** -- dbg can time specific interactions but does not profile locks

## Contrasts With
- No direct contrasts in source, though lcnt is fundamentally different from time-based profilers (fprof, eprof, cprof) as it measures lock contention rather than function execution.

# Common Errors

- **Error**: Running lcnt on a single-scheduler system and expecting useful results.
  **Correction**: Entities only run in parallel with multiple schedulers; lcnt needs multiple schedulers on multiple cores to show meaningful contention.

- **Error**: Using lcnt to profile application-level logic.
  **Correction**: lcnt profiles the Erlang Run-Time System's internal locking mechanisms, not application-level code. Use fprof/eprof/tprof for application-level profiling.

# Common Confusions

- **Confusion**: Thinking lcnt measures the same thing as fprof but for locks.
  **Clarification**: fprof measures function execution time; lcnt measures contention on internal runtime locks. They address fundamentally different performance concerns.

- **Confusion**: Believing lock contention is always the cause of poor multi-core scaling.
  **Clarification**: Poor scaling can also result from sequential bottlenecks, memory allocation patterns, or cache effects. lcnt specifically tests the lock contention hypothesis.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "lcnt" subsection under "Tools," plus the introductory tool listing in "Never Guess About Performance Bottlenecks." See `m:lcnt` manual page in Tools for full usage details.

# Verification Notes

- Definition: Directly quoted from both the introductory listing and the dedicated subsection.
- Key Properties: All derived from source text.
- Confidence: HIGH -- explicitly described with use case example in official documentation.
- Cross-references: Related tool slugs correspond to cards in this extraction.
- Uncertainties: None.
