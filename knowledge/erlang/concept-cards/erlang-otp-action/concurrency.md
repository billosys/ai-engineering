---
# === CORE IDENTIFICATION ===
concept: Concurrency
slug: concurrency

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
  - concurrent programming
  - concurrent tasks

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-process
  - parallelism
  - functional-programming
contrasts_with:
  - parallelism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is concurrency?"
  - "How does concurrency differ from parallelism?"
  - "Why was Erlang designed for concurrency?"
---

# Quick Definition

Concurrency is the property of tasks that have nothing forcing them to happen in a specific order, so they could be executed in any order or simultaneously. Erlang was designed for concurrency from the ground up.

# Core Definition

The book offers a semiformal definition: "Those things that don't have anything that forces them to happen in a specific order are said to be concurrent" (Chapter 1, section 1.1.1). The key point is that concurrent tasks *could* happen at the same time, leaving the system free to schedule them at its convenience. Tasks that *must* be done simultaneously aren't really separate tasks; tasks that are separate but must be done in a fixed order (such as breaking the egg before making the omelet) are non-concurrent. Everything else is concurrent. Erlang was designed for concurrency — having multiple tasks running simultaneously — as a central concern, using the process concept to give a clean separation between tasks.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Concurrent tasks have no required ordering between them.
2. Concurrency does not require simultaneous execution — only the *possibility* of it.
3. Concurrency is a property of the problem; parallelism is a property of the execution.
4. Identifying concurrency means finding the real dependencies in a problem and eliminating unnecessary ones.
5. Separating non-dependent parts of a program makes code more readable and lets the programmer focus on real problems.

# Construction / Recognition

## To Identify/Recognize:
1. Ask which activities can happen independently of one another.
2. Check whether any ordering is genuinely required between two tasks.
3. If no ordering is forced, the tasks are concurrent and can be modeled separately.
4. For apparently sequential work (do X, then Y, then Z), look for real dependencies — often X and Y can run in any order before Z.

# Context & Application

- **Typical contexts**: Designing Erlang systems, where the first design question is "what activities here are concurrent?"
- **Common applications**: Web servers handling many independent requests; any system with many independent ongoing activities.
- **Historical/stylistic notes**: Concurrency, not functional programming, is described as the defining feature of Erlang.

# Examples

**Example 1** (section 1.1.1): Sorting two packs of cards — neither pack must be sorted before the other, so the two sorting tasks are concurrent and may be done in either order, interleaved, or in parallel.

**Example 2** (section 1.1.1, "Processes: an example"): A web server receives independent page requests; because each request has little to do with any other, the requests are concurrent and can each be handled in a separate process.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **Erlang process** — the process is Erlang's unit of concurrency.
- **Functional programming** — the functional mindset is a natural match for concurrent programming.

## Related
- **Parallelism** — Erlang turns concurrency into parallelism automatically when CPUs are available.

## Contrasts With
- **Parallelism** — concurrency is the *potential* for simultaneous execution; parallelism is *actual* simultaneous execution on multiple CPUs.

# Common Errors

- **Error**: Treating tasks that must run in a fixed order as concurrent.
  **Correction**: Only tasks with no forced ordering are concurrent; preserve genuine dependencies.

- **Error**: Optimizing for parallel hardware as the first concern when restructuring code.
  **Correction**: The primary benefit of separating concurrent parts is clearer, more readable code; efficiency on multicore hardware is a secondary benefit.

# Common Confusions

- **Confusion**: Believing concurrent simply means "in parallel."
  **Clarification**: Concurrency means tasks *could* happen at the same time; parallelism means they *do*. A concurrent program runs correctly even on a single CPU.

- **Confusion**: Thinking tasks are concurrent only if they happen at the same instant.
  **Clarification**: The definition is about the absence of forced ordering, not about simultaneous timing.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1 "Concurrent programming with processes," section 1.1.1 "Understanding concurrency." See also Figure 1.1 (processes on uniprocessor vs. multiprocessor hardware).

# Verification Notes

- Definition source: Direct quotation of the semiformal definition in section 1.1.1.
- Confidence rationale: HIGH — the book explicitly states and discusses the definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
