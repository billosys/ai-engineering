---
# === CORE IDENTIFICATION ===
concept: SMP Erlang
slug: smp-erlang

# === CLASSIFICATION ===
category: performance
subcategory: runtime
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Multicore CPUs"
chapter_number: 26
pdf_page: null
section: "Running SMP Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - symmetric multiprocessing Erlang
  - SMP virtual machine
  - Erlang schedulers

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - multicore-efficiency-rules
  - small-messages-big-computations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run Erlang on a multicore CPU?"
  - "What is an Erlang scheduler and how do I control how many run?"
---

# Quick Definition

SMP Erlang is the Erlang virtual machine built to run on symmetric multiprocessing hardware, executing processes across multiple schedulers — one complete VM per CPU.

# Core Definition

"A symmetric multiprocessing (SMP) machine has two or more identical CPUs that are connected to a single shared memory." SMP Erlang is the build of the runtime that exploits such hardware. It is controlled by two command-line flags: `-smp` starts SMP Erlang, and `+S N` runs Erlang with `N` schedulers, where "each Erlang scheduler is a complete virtual machine that knows about all the other virtual machines." If `+S` is omitted, the scheduler count defaults to the number of logical processors ("Running SMP Erlang").

# Prerequisites

This is a foundational runtime concept with no prerequisites within this source.

# Key Properties

1. SMP Erlang runs on hardware with two or more identical CPUs sharing memory.
2. `-smp` is the flag that starts SMP Erlang.
3. `+S N` sets the number of schedulers; each scheduler is a complete VM aware of the others.
4. With `+S` omitted, the scheduler count defaults to the number of logical processors.
5. SMP Erlang has been built by default since Erlang R11B-0.
6. The scheduler count can deliberately differ from the physical CPU count — for benchmarking, for emulating a multicore on a unicore, or because more schedulers than CPUs can sometimes improve throughput.

# Construction / Recognition

## To Construct/Create:
1. Start the runtime with `erl -smp` to use the SMP virtual machine.
2. Optionally pass `+S N` to fix the number of schedulers at `N`.
3. To benchmark scaling, vary `N` (e.g., a script looping `+S 1` through `+S 32`).

## To Identify/Recognize:
1. A runtime started with `-smp` and/or `+S` flags is running SMP Erlang.
2. Performance tests that loop over scheduler counts indicate SMP measurement.

# Context & Application

- **Typical contexts**: Running and benchmarking Erlang programs on multicore hardware.
- **Common applications**: A `runtests` shell script starts Erlang with 1–32 schedulers (`erl -boot start_clean -noshell -smp +S $i`) and collects timings to measure parallel speedup.
- **Historical/stylistic notes**: SMP Erlang "is undergoing daily changes, so what is true today may not be true tomorrow"; on non-default platforms `--enable-smp-support` could be passed to `configure`. In modern OTP, SMP is mandatory and the separate non-SMP VM is gone.

# Examples

**Example 1** ("Running SMP Erlang"): The two scheduler flags:

```
$ erl -smp +S N
```

`-smp` starts SMP Erlang; `+S N` runs Erlang with `N` schedulers.

**Example 2** ("Running SMP Erlang" — `runtests` script): A benchmark loop starts Erlang once per scheduler count from 1 to 32 and appends each timing to a `results` file:

```
erl -boot start_clean -noshell -smp +S $i -s ptests tests $i >> results
```

# Relationships

## Builds Upon
- This is a foundational runtime card; it builds on no other concept card.

## Enables
- Multicore execution and the parallel-speedup measurements in the chapter.

## Related
- **Multicore efficiency rules** — SMP Erlang is the runtime on which the rules deliver speedup.
- **Small messages, big computations** — The SMP benchmarks vary scheduler count to measure scaling.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Assuming the scheduler count must equal the physical CPU count.
  **Correction**: `+S N` can be set lower (to emulate fewer cores) or higher (sometimes improving throughput); it defaults to the logical processor count.

- **Error**: Reading too much into a single SMP benchmark result.
  **Correction**: SMP Erlang changes frequently; treat measured speedups as snapshots, and vary `+S` to see the trend.

# Common Confusions

- **Confusion**: Thinking an Erlang scheduler is just an OS thread queue.
  **Clarification**: Each scheduler is "a complete virtual machine that knows about all the other virtual machines."

# Source Reference

Chapter 26: Programming Multicore CPUs, Section "Small Messages, Big Computations," subsection "Running SMP Erlang." See the `runtests` script listing.

# Verification Notes

- Definition source: Direct quote and adaptation from "Running SMP Erlang."
- Confidence rationale: HIGH — the source defines SMP, the schedulers, and the two control flags explicitly.
- Uncertainties: The book's `-smp`/`--enable-smp-support` mechanics are dated; modern OTP always runs SMP.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
