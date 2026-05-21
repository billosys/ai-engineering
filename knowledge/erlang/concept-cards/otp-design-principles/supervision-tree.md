---
# === CORE IDENTIFICATION ===
concept: Supervision Tree
slug: supervision-tree

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
  - "supervisor tree"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - worker-process
  - supervisor-process
  - behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervision tree?"
  - "How does OTP structure processes for fault tolerance?"
---

# Quick Definition

A supervision tree is a hierarchical arrangement of supervisor and worker processes that enables the design and programming of fault-tolerant software in Erlang/OTP.

# Core Definition

As defined in the OTP Design Principles Overview: "A basic concept in Erlang/OTP is the supervision tree. This is a process structuring model based on the idea of workers and supervisors." The supervision tree is described as "a hierarchical arrangement of code into supervisors and workers, which makes it possible to design and program fault-tolerant software."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Based on two kinds of processes: workers (perform computations) and supervisors (monitor workers).
2. Supervisors can restart workers if something goes wrong.
3. Hierarchical structure — supervisors can supervise other supervisors, forming a tree.
4. An application with processes is easiest implemented as a supervision tree using the standard behaviours.

# Construction / Recognition

## To Construct/Create:
1. Define a top-level supervisor process.
2. Specify child processes (workers or sub-supervisors) for each supervisor.
3. Workers perform actual work; supervisors monitor and restart children on failure.
4. Use OTP behaviours (`supervisor`, `gen_server`, `gen_statem`, `gen_event`) to implement each process.

## To Identify/Recognize:
1. A hierarchy of processes where parent processes (supervisors) monitor child processes.
2. Visualized with square boxes for supervisors and circles for workers.
3. Uses OTP behaviour modules for both supervisor and worker implementations.

# Context & Application

Supervision trees are the primary organizational pattern for Erlang/OTP applications. Any application that manages processes should be structured as a supervision tree. This structure is what enables OTP's fault-tolerance guarantees — when a worker crashes, its supervisor detects the failure and restarts it according to a defined strategy, isolating failures and preventing cascading crashes.

# Examples

**Example 1** (design_principles.md, "Supervision Trees"): The source provides a Mermaid diagram showing a multi-level supervision tree where a top-level "Type 1 Supervisor" has two children: another "Type 1 Supervisor" (which supervises a worker) and a "Type A Supervisor" (which in turn supervises another "Type A Supervisor" with a worker, and a "Type 1 Supervisor" with two workers).

# Relationships

## Builds Upon
- No prerequisites — this is a foundational OTP concept.

## Enables
- **Worker Process** — workers exist within supervision trees
- **Supervisor Process** — supervisors are defined in terms of supervision trees
- **Behaviour** — behaviours formalize the patterns used in supervision trees

## Related
- **application** — an application with processes is easiest implemented as a supervision tree
- **release** — a release is built from applications, each potentially containing supervision trees

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Implementing processes outside a supervision tree (standalone, unmonitored).
  **Correction**: Structure processes into supervision trees so failures are detected and handled automatically.

# Common Confusions

- **Confusion**: Thinking a supervision tree must be flat (one supervisor, many workers).
  **Clarification**: Supervision trees are hierarchical — supervisors can supervise other supervisors, forming arbitrarily deep trees.

# Source Reference

OTP Design Principles, Overview, "Supervision Trees" section (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Supervision Trees" section.
- Confidence rationale: High — explicitly defined as "a basic concept in Erlang/OTP" with detailed description.
- Uncertainties: None.
- Cross-reference status: References worker-process, supervisor-process, behaviour (planned cards).
