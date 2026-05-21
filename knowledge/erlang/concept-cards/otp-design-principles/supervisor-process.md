---
# === CORE IDENTIFICATION ===
concept: Supervisor Process
slug: supervisor-process

# === CLASSIFICATION ===
category: applications-releases
subcategory: process-structure
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Overview"
chapter_number: null
pdf_page: null
section: "Supervision Trees"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "supervisor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - supervisor-behaviour
  - child-specification
contrasts_with:
  - worker-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor process in OTP?"
  - "How do supervisors relate to workers in a supervision tree?"
---

# Quick Definition

A supervisor is a process in a supervision tree that monitors worker processes (and other supervisors) and can restart them if something goes wrong.

# Core Definition

According to the OTP Design Principles Overview: "Supervisors are processes that monitor workers. A supervisor can restart a worker if something goes wrong." Supervisors share a similar structure, "with the sole distinction lying in the child processes they supervise." A supervisor is implemented using the `supervisor` behaviour.

# Prerequisites

- **Supervision Tree** — supervisors are defined as components within a supervision tree.

# Key Properties

1. Monitor child processes (workers or other supervisors).
2. Can restart child processes when they fail.
3. All supervisors share a similar structure — they differ only in which children they supervise.
4. Implemented using the `supervisor` OTP behaviour.
5. Represented as square boxes in supervision tree diagrams.

# Construction / Recognition

## To Construct/Create:
1. Create a callback module that uses the `supervisor` behaviour.
2. Define child specifications listing the processes to supervise.
3. Define a restart strategy (e.g., one-for-one, one-for-all).
4. Start the supervisor using `supervisor:start_link/2` or `supervisor:start_link/3`.

## To Identify/Recognize:
1. A process that does not perform application work but monitors other processes.
2. Uses the `-behaviour(supervisor)` module attribute.
3. Represented as square boxes in OTP supervision tree diagrams.
4. Can supervise both workers and other supervisors (forming a tree).

# Context & Application

Supervisors are the backbone of OTP's fault-tolerance model. They form the non-leaf nodes of a supervision tree. When a child process crashes, the supervisor detects the failure (via process links) and restarts the child according to its configured strategy. This enables the "let it crash" philosophy: workers don't need defensive error handling because their supervisors handle recovery.

# Examples

**Example 1** (design_principles.md, "Supervision Trees"): The supervision tree diagram shows multiple supervisor nodes (labeled "Type 1 Supervisor" and "Type A Supervisor") arranged hierarchically, each supervising either workers or other supervisors.

**Example 2** (design_principles.md, "Behaviours"): The `supervisor` behaviour is listed as one of the four standard Erlang/OTP behaviours, described as "for implementing a supervisor in a supervision tree."

# Relationships

## Builds Upon
- **Supervision Tree** — supervisors are one of the two process types in a supervision tree.

## Enables
- **supervisor-behaviour** — the OTP behaviour used to implement supervisors
- **child-specification** — supervisors use child specs to define their children

## Related
- **Worker Process** — the processes that supervisors monitor and restart

## Contrasts With
- **Worker Process** — workers perform actual work; supervisors monitor and manage workers.

# Common Errors

- **Error**: Putting application logic in a supervisor process.
  **Correction**: Supervisors should only monitor and restart children. Business logic belongs in worker processes.

# Common Confusions

- **Confusion**: Thinking supervisors can only supervise workers.
  **Clarification**: Supervisors can supervise other supervisors, forming a hierarchical tree. This is shown in the source's diagram where supervisors appear at multiple levels.

# Source Reference

OTP Design Principles, Overview, "Supervision Trees" and "Behaviours" sections (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Supervision Trees" section.
- Confidence rationale: High — explicitly defined in the source.
- Uncertainties: Restart strategies and child specifications are mentioned but detailed in other chapters (sup_princ.md).
- Cross-reference status: References supervision-tree, worker-process, supervisor-behaviour, child-specification (planned cards from other agents).
