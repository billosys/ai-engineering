---
# === CORE IDENTIFICATION ===
concept: Bottleneck
slug: bottleneck

# === CLASSIFICATION ===
category: performance
subcategory: capacity
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning — Finding Bottlenecks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bottlenecks
  - system limit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - capacity-testing
extends: []
related:
  - throughput
  - system-monitor
  - synchronous-load-regulation
  - balancing-erlang-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bottleneck?"
  - "How do I find bottlenecks in an Erlang system?"
---

# Quick Definition

A bottleneck is a backlog in a system, usually manifesting as long message queues; system limits include running out of ports, memory, or disk space.

# Core Definition

"Bottlenecks are backlogs in your system whose symptom is usually long message queues. System limits include running out of ports, memory, or even hard disk space. When you have found a bottleneck and removed it, rerun the stress test again to tackle the next bottleneck or system limit" (Cesarini & Vinoski, p. 431). "Most commonly, bottlenecks manifest themselves through long message queues" (p. 436).

# Prerequisites

- **Capacity testing** — Bottlenecks are found through stress testing; understand capacity testing first.

# Key Properties

1. A backlog in the system, usually shown by long message queues.
2. Distinct from system limits — running out of ports, memory, or hard disk space.
3. Found on a process and node basis by monitoring process memory usage and mailbox queues.
4. Removed iteratively — fix one, rerun the stress test, tackle the next.
5. The biggest challenge is often not finding bottlenecks but generating enough load to expose them.
6. Sometimes a bottleneck is deliberately added to throttle load (e.g., a FIFO queue for session initialization).

# Construction / Recognition

## To Construct/Create:
This is a flaw to find and remove, not to build. To find bottlenecks:
1. Monitor process memory usage with `erlang:memory()`.
2. Monitor message queues with the `i()` or `regs()` shell commands.
3. Use `percept`, `etop`, or `observer` for systems with many processes.
4. Use the system monitor for memory spikes and long garbage collections.

## To Identify/Recognize:
1. Recognize a bottleneck by long message queues backing up in a process's mailbox.

# Context & Application

- **Typical contexts**: Stress testing and balancing an Erlang system.
- **Common applications**: Diagnosing throughput degradation; finding the cause of node crashes.
- **Historical/stylistic notes**: Bottlenecks throttle requests, which can surprisingly keep the service alive even as it slows down (p. 435).

# Examples

**Example 1** (pp. 436-437): A log server receiving asynchronous `gen_server:cast` log requests faster than it can handle them builds a huge message queue in the consumer's mailbox — the manifestation of a bottleneck.

**Example 2** (p. 437): A memory spike from XML session parsing caused node crashes; the solution was a separate FIFO queue for session initialization — deliberately adding a bottleneck flattened the memory graphs without affecting throughput.

# Relationships

## Builds Upon
- **Capacity testing** — Bottlenecks are exposed by stress testing

## Enables
- Finding and removing bottlenecks enables stable, balanced systems.

## Related
- **Throughput** — A bottleneck degrades throughput
- **System monitor** — Used to surface memory-spike and long-GC bottlenecks
- **Synchronous load regulation** — A trick to remove message-queue bottlenecks
- **Balancing an Erlang system** — Removing bottlenecks balances the system

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Removing one bottleneck and assuming the system is now stable
  **Correction**: Rerun the stress test after each fix; another bottleneck or system limit usually waits behind it.

# Common Confusions

- **Confusion**: A bottleneck and a system limit are the same thing.
  **Clarification**: A bottleneck is a backlog (long message queues); a system limit is running out of a resource such as ports, memory, or disk.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning — Finding Bottlenecks," pages 431, 435-437. See Figures 15-5 and 15-6.

# Verification Notes

- Definition source: Direct quotes from pp. 431 and 436.
- Confidence rationale: HIGH — the source explicitly defines bottlenecks and how to find them.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
