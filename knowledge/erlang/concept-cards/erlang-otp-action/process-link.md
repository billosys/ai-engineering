---
# === CORE IDENTIFICATION ===
concept: Process Link
slug: process-link

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: links-and-signals
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.1 How process links work"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - link
  - linked processes

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - process-termination
extends: []
related:
  - exit-signal
  - trapping-exit-signals
  - supervision
  - fault-tolerance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process link?"
  - "How do process links work?"
  - "What happens to linked processes when one crashes?"
---

# Quick Definition

A process link is a bidirectional connection between two processes that causes an exit signal to propagate between them, so a group of linked processes behaves as a unit with respect to termination.

# Core Definition

"When an Erlang process dies unexpectedly, an *exit signal* is generated. All processes that are *linked* to the dying process receive this signal" (Chapter 1, section 1.2.1). By default, receiving such a signal causes the receiver to exit as well and propagate the signal on to any other processes it is linked to, "and so on, until all the processes that are linked directly or indirectly to each other have exited." This cascading behavior allows a group of processes to behave as a single application with respect to termination: there is never a need to find and kill leftover processes before restarting a subsystem. Because a process encapsulates all its state, a group of linked processes can die safely and have all their complex state cleaned out of existence.

# Prerequisites

- **Erlang process** — links connect two processes.
- **Process termination** — links matter when a process terminates.

# Key Properties

1. A link connects two processes bidirectionally.
2. When a linked process dies unexpectedly, an exit signal is generated.
3. By default, linked processes receiving the signal also exit.
4. The signal propagates transitively through all directly or indirectly linked processes.
5. A group of linked processes thus terminates as a unit.

# Construction / Recognition

## To Identify/Recognize:
1. Two processes are linked, forming an edge in a graph of processes.
2. On unexpected death, the exit signal travels every link.
3. Unless trapped, each linked process exits and re-propagates the signal.

# Context & Application

- **Typical contexts**: Grouping collaborating processes so they live and die together.
- **Common applications**: Subsystems that must be restarted as a whole; the foundation supervisors are built on.
- **Historical/stylistic notes**: Links plus signal trapping plus supervisors give Erlang fine-grained "reboots" of subsystems.

# Examples

**Example 1** (Figure 1.2): An exit signal triggered by a crashing process is propagated to all its linked processes, generally making those terminate as well so the whole group is cleaned up.

**Example 2** (section 1.2.1): If one process in a group of linked collaborators crashes, all its collaborators also terminate, and all the complex state created is "snuffed out of existence cleanly and easily."

# Relationships

## Builds Upon
- **Erlang process** — links join processes.

## Enables
- **Supervision** — supervisors rely on links to detect failures.

## Related
- **Exit signal** — what travels along a link.
- **Trapping exit signals** — overrides the default propagation.
- **Fault tolerance** — links are Erlang's unique mechanism for handling process failures.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting a crash in one linked process to leave the others running.
  **Correction**: By default, all linked processes exit too; use signal trapping to override this.

# Common Confusions

- **Confusion**: Thinking links are one-directional or that they only inform, not terminate.
  **Clarification**: Links propagate exit signals that by default cause linked processes to exit; the group terminates together.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.2.1 "How process links work." See Figure 1.2.

# Verification Notes

- Definition source: Direct adaptation from section 1.2.1.
- Confidence rationale: HIGH — links and their cascading behavior are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
