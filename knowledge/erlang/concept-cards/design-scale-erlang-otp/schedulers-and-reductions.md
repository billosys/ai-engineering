---
# === CORE IDENTIFICATION ===
concept: Schedulers and Reductions
slug: schedulers-and-reductions

# === CLASSIFICATION ===
category: performance
subcategory: beam-scheduling
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Multicore, Schedulers, and Reductions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reduction count
  - BEAM scheduler
  - run queue
  - preemptive scheduling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the BEAM virtual machine schedule processes?"
  - "What is a reduction count?"
  - "How does Erlang give soft real-time guarantees?"
---

# Quick Definition

For each core, the BEAM VM runs a scheduler thread that executes a group of processes. Schedulers preempt processes based on a reduction count — an approximation of executed workload.

# Core Definition

"For every core, the BEAM virtual machine starts a thread that runs a scheduler. Each scheduler is responsible for a group of processes, and at any one time, a process from each scheduler executes in parallel on each core. Processes that are not suspended and are ready to execute are placed in the scheduler's run queue" (Cesarini & Vinoski, p. 33). "Schedulers decide when to preempt processes based on an approximation of the workload they have executed. This approximation is called the reduction count. ... Function calls and BIFs are assigned a value of one or more reductions. ... Each process is allowed to execute a predefined number of reductions before being preempted" (pp. 33-34).

# Prerequisites

- **Processes and message passing** — Schedulers exist to run processes; the concept presupposes the process model.

# Key Properties

1. One scheduler thread per core; each owns a group of processes.
2. Ready, non-suspended processes wait in a scheduler's run queue.
3. A reduction count approximates work done; BIFs/calls cost one or more reductions.
4. A process runs a fixed reduction budget, then is preempted to the end of the run queue.
5. Reduction values and budgets are deliberately undocumented to discourage premature optimization.
6. Processes migrate between run queues to balance load; unused schedulers can be paused for energy saving.
7. Preemptive multitasking plus per-process garbage collection give predictable soft real-time properties.

# Construction / Recognition

## To Construct:
1. Write ordinary Erlang processes — scheduling is automatic.
2. At VM startup, optionally limit thread/scheduler counts or bind schedulers to cores.

## To Recognize:
1. Soft real-time fairness under load is the observable effect of reduction-based preemption.

# Context & Application

- **Typical contexts**: Multicore scaling; soft real-time systems under sustained load.
- **Common applications**: Running one process per concurrent activity and letting the VM scale across cores.
- **Historical/stylistic notes**: Unlike event-loop frameworks, Erlang offers preemptive multitasking; only dropping into misbehaving C (a NIF/driver) can block a scheduler.

# Examples

**Example 1** (p. 33): The VM "starts a separate thread pool used for drivers and file I/O that can operate without blocking any scheduler threads."

**Example 2** (p. 33): The book notes the VM avoids letting "processes in a run queue with 10 processes get twice as much CPU time as those in a run queue with 20 processes" by migrating processes to even out queue sizes.

# Relationships

## Builds Upon
- **Processes and message passing** — Schedulers run the process model.

## Enables
- *(none specific in scope)*

## Related
- *(none additional in scope)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Hand-tuning code against assumed reduction costs.
  **Correction**: Reduction values are intentionally undocumented and vary by release/hardware; optimize only from measurements.

# Common Confusions

- **Confusion**: Believing one blocked process freezes the whole VM, as in an event loop.
  **Clarification**: Erlang preempts cooperatively-or-not; only a misbehaving NIF/driver in C can block a scheduler.

# Source Reference

Chapter 1: Introducing Erlang, Section "Multicore, Schedulers, and Reductions," pages 33-34.

# Verification Notes

- Definition source: Direct quotes from pp. 33-34.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
