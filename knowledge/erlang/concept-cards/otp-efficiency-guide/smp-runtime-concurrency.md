---
concept: SMP Runtime Concurrency
slug: smp-runtime-concurrency
category: system-configuration
subcategory: null
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "SMP Run-Time System"
extraction_confidence: high
aliases:
  - "SMP run-time system"
  - "multi-core Erlang"
  - "scheduler threads"
prerequisites:
  - erlang-process-creation
  - tail-recursive-main-loop
extends: []
related:
  - driver-concurrency
  - receive-optimization
contrasts_with: []
answers_questions:
  - "How does the Erlang runtime exploit multi-core hardware?"
  - "Why do some benchmarks not benefit from SMP?"
  - "What is required for an Erlang application to gain performance from multiple cores?"
---

# Quick Definition

The Erlang runtime system runs several scheduler threads (typically one per CPU core) to execute Erlang processes in parallel, but an application must have more than one runnable process most of the time to gain performance from a multi-core computer.

# Core Definition

The Erlang run-time system takes advantage of a multi-core or multi-CPU computer by running several Erlang scheduler threads (typically, the same number of threads as the number of cores). To gain performance from a multi-core computer, your application _must have more than one runnable Erlang process_ most of the time. Otherwise, the Erlang emulator can still only run one Erlang process at a time (Ericsson/OTP Team, "Processes" chapter, "SMP Run-Time System" section).

# Prerequisites

- **erlang-process-creation** -- Understanding lightweight processes is fundamental to understanding how scheduler threads execute them
- **tail-recursive-main-loop** -- Process loops are the units of work scheduled across cores

# Key Properties

1. The BEAM runs several Erlang scheduler threads, typically matching the number of CPU cores
2. Each scheduler thread can run one Erlang process at a time
3. True parallelism requires multiple runnable processes simultaneously
4. A single active process (with others blocked in `receive`) cannot benefit from multiple cores
5. Benchmarks that appear concurrent can be entirely sequential in practice

# Construction / Recognition

## To Verify SMP Is Active

When starting the Erlang emulator, the boot banner shows SMP information:
```
Erlang/OTP 27 [erts-14.2.3] [64-bit] [smp:8:8] ...
```

The `[smp:8:8]` indicates 8 scheduler threads with 8 online.

## To Benefit from SMP

1. Design the application with multiple concurrent activities (processes)
2. Ensure multiple processes are runnable (not all blocked in `receive`) at the same time
3. Avoid bottleneck designs where a single process serializes all work
4. Use process pools or parallel computation patterns to spread work across schedulers

# Context & Application

SMP support is fundamental to scaling Erlang applications on modern hardware. However, the presence of multiple cores does not automatically improve performance -- the application architecture must support genuine concurrency.

**Typical contexts:**

- Scaling server applications across multi-core machines
- Evaluating benchmark results (many benchmarks are misleadingly sequential)
- Architectural decisions about process granularity and work distribution

**Common pitfall -- sequential benchmarks:** The source specifically warns that benchmarks which appear to be concurrent are often sequential. The EStone benchmark is entirely sequential. The most common implementation of the "ring benchmark" usually has only one active process at a time, with the others waiting in `receive`.

# Examples

**Example 1** (Processes chapter, "SMP Run-Time System" section): The source describes the fundamental requirement:

> To gain performance from a multi-core computer, your application _must have more than one runnable Erlang process_ most of the time. Otherwise, the Erlang emulator can still only run one Erlang process at a time.

**Example 2** (Processes chapter): Misleading benchmarks:

> Benchmarks that appear to be concurrent are often sequential. For example, the EStone benchmark is entirely sequential. So is the most common implementation of the "ring benchmark"; usually one process is active, while the others wait in a `receive` statement.

# Relationships

## Related

- **driver-concurrency** -- Drivers have their own locking mechanisms that interact with SMP scheduling
- **receive-optimization** -- Processes blocked in `receive` are not runnable and do not contribute to parallelism

## Builds Upon

- **erlang-process-creation** -- Lightweight processes are the units of work distributed across scheduler threads

# Common Errors

- **Error**: Designing a system with a single bottleneck process that serializes all work
  **Correction**: Distribute work across multiple processes to take advantage of multiple scheduler threads

- **Error**: Using benchmarks like EStone or simple ring benchmarks to measure SMP performance
  **Correction**: These benchmarks are sequential despite appearing concurrent. Use benchmarks with genuinely parallel workloads

# Common Confusions

- **Confusion**: Believing that adding more CPU cores automatically speeds up any Erlang application
  **Clarification**: Only applications with multiple simultaneously runnable processes benefit from additional cores. A system where only one process is active at a time will not see improvement

- **Confusion**: Thinking the "ring benchmark" measures parallel performance
  **Clarification**: In a ring benchmark, typically only one process is active while all others wait in `receive`. This is sequential despite having many processes

- **Confusion**: Equating "many processes" with "parallel execution"
  **Clarification**: Having many processes does not guarantee parallelism. What matters is how many processes are _runnable_ (not waiting) at the same time

# Source Reference

"Processes" chapter, "SMP Run-Time System" section. Brief section covering scheduler threads, the requirement for multiple runnable processes, and warnings about misleadingly sequential benchmarks (EStone, ring benchmark).

# Verification Notes

- Definition: Directly from source text in the "SMP Run-Time System" section
- The scheduler thread count (matching cores) is explicit in the source
- The requirement for multiple runnable processes is stated emphatically with italics in the source
- The EStone and ring benchmark examples are directly from source
- Confidence: HIGH -- explicit, clear statements in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
