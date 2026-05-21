---
# === CORE IDENTIFICATION ===
concept: Sequential Bottleneck
slug: sequential-bottleneck

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
section: "Avoid Sequential Bottlenecks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sequential bottlenecks
  - sequentialness

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - multicore-efficiency-rules
  - smp-erlang
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a sequential bottleneck and why does it limit parallel speedup?"
  - "Why should I avoid registered processes in performance-critical code?"
---

# Quick Definition

A sequential bottleneck is a point where several concurrent processes must all access a sequential resource, limiting how much the program can be parallelized.

# Core Definition

"A sequential bottleneck is where several concurrent processes need access to a sequential resource. A typical example is I/O. Typically we have a single disk, and all output to the disk is ultimately sequential." Some "sequentialness" is intrinsic to a problem and cannot be removed — "Certain events happen in a certain sequential order, and no matter how we try, we can't change this order." Where the bottleneck is not intrinsic, "the only solution... is to change the algorithm concerned" from a nondistributed to a distributed algorithm ("Avoid Sequential Bottlenecks").

# Prerequisites

- **Process** — A bottleneck arises when many concurrent processes contend for one resource.

# Key Properties

1. It occurs when multiple concurrent processes need a single sequential resource.
2. Some sequentialness is intrinsic to the problem and cannot be removed.
3. I/O is a typical example — a single disk has one set of heads.
4. Every registered process is a potential sequential bottleneck.
5. The usual fix is to change the algorithm from a nondistributed to a distributed one.
6. A registered server used despite this should "respond to all requests as quickly as possible."

# Construction / Recognition

## To Identify/Recognize:
1. Look for a single resource (a disk, a registered process, a server) that many processes must funnel through.
2. A registered process used as a server is a candidate bottleneck.

## To Address:
1. Determine whether the sequentialness is intrinsic; if so, it cannot be removed.
2. If not intrinsic, redesign the algorithm as a distributed algorithm (e.g., partition the resource).
3. Avoid creating registered processes; if you must, make the server respond quickly.

# Context & Application

- **Typical contexts**: Parallelizing programs for multicore CPUs and networked systems.
- **Common applications**: Splitting a single ticket-booking agency into multiple agencies that each own a disjoint subset of tickets removes the single-agency bottleneck.
- **Historical/stylistic notes**: Distributed algorithms have a vast research literature but little library adoption, "because the need for such algorithms is not apparent until we try to program networked algorithms or multicore computers." Distributed hash tables are one such research area.

# Examples

**Example 1** ("Avoid Sequential Bottlenecks"): Disk I/O — "we have a single disk, and all output to the disk is ultimately sequential. The disk has one set of heads, not two, and we can't change that."

**Example 2** ("A Distributed Ticket-Booking System"): A single ticket agency booking all tickets is a sequential bottleneck. Using two agencies — one given even-numbered tickets, one odd-numbered — removes the bottleneck while guaranteeing no ticket is sold twice; an agency that runs out can request a bundle from the other.

# Relationships

## Builds Upon
- This card builds on the process concept; it has no elaborating prerequisite card.

## Enables
- Recognizing bottlenecks is required to satisfy the multicore efficiency rules.

## Related
- **Multicore efficiency rules** — "Avoid sequential bottlenecks" is one of the four rules.
- **SMP Erlang** — Bottlenecks cap the speedup observed when varying the number of schedulers.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Liberally registering processes in performance-critical code.
  **Correction**: Avoid registered processes; each is a potential sequential bottleneck.

- **Error**: Doing slow work inside a server that many processes call.
  **Correction**: Make the server respond to all requests as quickly as possible, or partition the resource.

# Common Confusions

- **Confusion**: Believing every sequential bottleneck can be parallelized away.
  **Clarification**: Some sequentialness is intrinsic to the problem and cannot be removed; only non-intrinsic bottlenecks can be fixed, and that requires changing the algorithm.

# Source Reference

Chapter 26: Programming Multicore CPUs, Section "Avoid Sequential Bottlenecks," including the subsection "A Distributed Ticket-Booking System."

# Verification Notes

- Definition source: Direct quote from "Avoid Sequential Bottlenecks."
- Confidence rationale: HIGH — the source explicitly defines the term and gives the ticket-booking example.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
