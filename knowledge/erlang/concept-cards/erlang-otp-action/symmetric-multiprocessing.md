---
# === CORE IDENTIFICATION ===
concept: Symmetric Multiprocessing
slug: symmetric-multiprocessing

# === CLASSIFICATION ===
category: performance
subcategory: runtime-system
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.4.1 The scheduler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - SMP
  - SMP support

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scheduler
extends:
  - scheduler
related:
  - parallelism
  - erlang-runtime-system
  - os-thread
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is SMP support in Erlang?"
  - "When was SMP support added to Erlang/OTP?"
  - "How did Erlang use multiple cores before SMP?"
---

# Quick Definition

Symmetric multiprocessing (SMP) is the ERTS capability, added in 2006, to use multiple process schedulers — each on its own OS thread — so that one Erlang runtime can run processes across multiple CPUs.

# Core Definition

"Starting in May 2006 with release 11 of Erlang/OTP, support for symmetric multiprocessing (SMP) was added. This was a major effort, allowing the Erlang runtime system to use, not one, but multiple process schedulers internally, each using a separate operating system thread" (Chapter 1, section 1.4.1). Before SMP, ERTS had only one thread for the main body of work; to use a multicore system you had to run multiple ERTS instances on the same machine. SMP gives an n:m mapping between Erlang processes and OS threads and lets a single Erlang runtime exploit all available cores.

# Prerequisites

- **Scheduler** — SMP is about running multiple schedulers.

# Key Properties

1. SMP support was added in May 2006 with release 11 of Erlang/OTP.
2. It allows ERTS to use multiple process schedulers internally.
3. Each scheduler uses a separate operating system thread.
4. It produces an n:m mapping between Erlang processes and OS threads.
5. Before SMP, multicore use required running multiple ERTS instances per machine.

# Construction / Recognition

## To Identify/Recognize:
1. The shell banner shows an `[smp:N]` tag indicating N schedulers.
2. One Erlang node uses several cores via multiple scheduler threads.

# Context & Application

- **Typical contexts**: Running Erlang on multicore servers and laptops.
- **Common applications**: Transparent parallel execution of concurrent Erlang processes.
- **Historical/stylistic notes**: SMP was a major engineering effort; its effect can be seen in Figure 1.1's multiprocessor diagram.

# Examples

**Example 1** (section 1.4.1): Before SMP, "if you wanted to use a multicore system, you had to run multiple ERTS instances on the same machine."

**Example 2** (Chapter 2, section 2.1.1): The shell banner "Erlang (BEAM) emulator version 5.6.5 [smp:2]" shows SMP running with two schedulers.

# Relationships

## Builds Upon
- **Scheduler** — SMP multiplies the number of schedulers.

## Enables
- **Parallelism** — multiple scheduler threads run Erlang processes in parallel.

## Related
- **Erlang runtime system** — SMP is an ERTS capability.
- **OS thread** — each scheduler runs on its own OS thread.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Running multiple ERTS instances on one machine to use multiple cores.
  **Correction**: Since SMP support, a single ERTS instance uses all cores via multiple schedulers.

# Common Confusions

- **Confusion**: Believing Erlang always had multicore support.
  **Clarification**: SMP support was added in 2006 (release 11); earlier ERTS had a single work thread.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4.1 "The scheduler." See Figure 1.1.

# Verification Notes

- Definition source: Direct adaptation from section 1.4.1.
- Confidence rationale: HIGH — SMP support and its 2006 introduction are explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
