---
# === CORE IDENTIFICATION ===
concept: Supervision Tree
slug: supervision-tree

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.3 Layering processes for fault tolerance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - layering processes
  - layered system of supervisors

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision
extends:
  - supervision
related:
  - fault-tolerance
  - let-it-crash
  - distributed-erlang
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervision tree?"
  - "Why layer supervisors instead of using a single level?"
  - "How does layering define working base states?"
---

# Quick Definition

A supervision tree is a multi-layer hierarchy of supervisors and workers, allowing subsystems to be restarted at different levels and defining different known-good base states to revert to.

# Core Definition

"A system shouldn't be structured as a single-level hierarchy of supervisors and workers. In any complex system, you'll want a *supervision tree* with multiple layers that allows subsystems to be restarted at different levels in order to cope with unexpected problems of varying kinds" (Chapter 1, section 1.2.2). Layering "brings related subsystems together under a common supervisor" and "defines different levels of working base states that you can revert to" (section 1.2.3). If a low-level supervisor cannot restart its group, it can give up and escalate the problem to a supervisor higher in the tree, which may take broader action.

# Prerequisites

- **Supervision** — a supervision tree is composed of supervisors and workers.

# Key Properties

1. It is a multi-layer hierarchy of supervisors and workers.
2. Subsystems can be restarted at different levels of the tree.
3. Each layer defines a working base state the system can revert to.
4. A supervisor that cannot recover escalates the failure to its parent supervisor.
5. Restarts can range from a small group to an entire branch of the tree.

# Construction / Recognition

## To Construct/Create:
1. Group related workers under a local supervisor.
2. Group related supervisors under a higher-level supervisor.
3. Continue layering until the whole system forms one tree.
4. Define the restart behavior and escalation at each level.

# Context & Application

- **Typical contexts**: Any non-trivial OTP system.
- **Common applications**: Isolating subsystems so they can be restarted in fractions of a second to keep the system running despite unpredicted errors.
- **Historical/stylistic notes**: Layering is what makes Erlang's "reboots" granular — a small subsystem can be restarted without disturbing the rest.

# Examples

**Example 1** (Figure 1.4): Two worker groups A and B are supervised separately; both, with their supervisors, form a larger group C under a higher supervisor. If supervisor A dies, its survivors are killed and C is informed so the whole left branch restarts; B is unaffected unless C shuts everything down.

**Example 2** (section 1.2.3): Group A processes and encodes multimedia data while group B presents it; bad data crashes a process in A, the A supervisor restores A's base state, and B continues unaware. If A repeatedly fails to restart, its supervisor escalates to C, which may then also shut down B.

# Relationships

## Builds Upon
- **Supervision** — the tree is built from supervisors and their workers.

## Enables
- Multi-level, escalating fault recovery.

## Related
- **Fault tolerance** — layering organizes a system for individually restartable subsystems.
- **Let it crash** — the tree provides the recovery structure crashes rely on.
- **Distributed Erlang** — layering on one machine still shares hardware; distribution addresses that.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Structuring a complex system as a single-level supervisor-and-workers hierarchy.
  **Correction**: Use a multi-layer supervision tree so subsystems can be restarted at appropriate levels.

# Common Confusions

- **Confusion**: Thinking the supervision tree protects against hardware failure.
  **Clarification**: On a single machine, layering cannot save you from a failed disk, network, or power; distribution is needed for that.

# Source Reference

Chapter 1: The Erlang/OTP platform, sections 1.2.2 and 1.2.3 "Layering processes for fault tolerance." See Figure 1.4.

# Verification Notes

- Definition source: Direct adaptation from sections 1.2.2 and 1.2.3.
- Confidence rationale: HIGH — the supervision tree and layering are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
