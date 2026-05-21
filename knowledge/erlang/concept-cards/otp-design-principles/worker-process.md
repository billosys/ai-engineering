---
# === CORE IDENTIFICATION ===
concept: Worker Process
slug: worker-process

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
  - "worker"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - behaviour
  - gen-server
  - gen-event
contrasts_with:
  - supervisor-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a worker process in OTP?"
  - "What role do workers play in a supervision tree?"
---

# Quick Definition

A worker is a process in a supervision tree that performs computations and other actual work, as opposed to a supervisor which monitors other processes.

# Core Definition

According to the OTP Design Principles Overview: "Workers are processes that perform computations and other actual work." Workers are one of the two fundamental process types in a supervision tree, alongside supervisors. The source notes that "many of the workers are servers in a server-client relation, finite-state machines, or event handlers."

# Prerequisites

- **Supervision Tree** — workers are defined as components within a supervision tree.

# Key Properties

1. Perform computations and actual work (as opposed to monitoring).
2. Are monitored by supervisor processes, which can restart them on failure.
3. Commonly implemented using OTP behaviours: `gen_server`, `gen_statem`, or `gen_event`.
4. Represented as circles in supervision tree diagrams.

# Construction / Recognition

## To Construct/Create:
1. Implement the process using an OTP behaviour (e.g., `gen_server`, `gen_statem`, `gen_event`).
2. Define it as a child of a supervisor in the supervisor's child specification.
3. Use `start_link` to allow the supervisor to link to and monitor the worker.

## To Identify/Recognize:
1. A process in a supervision tree that does not itself supervise other processes.
2. Represented as circles (not squares) in OTP supervision tree diagrams.
3. Implements one of the standard OTP worker behaviours.

# Context & Application

Workers are the leaf nodes of a supervision tree. They perform the actual business logic of an application — handling client requests, managing state, processing events, and so on. Their lifecycle is managed by their parent supervisor, which restarts them according to a defined strategy when they crash.

# Examples

**Example 1** (design_principles.md, "Supervision Trees"): In the supervision tree diagram, workers appear as circle nodes at the leaves of the tree. The diagram shows workers supervised by different types of supervisors at various levels of the hierarchy.

**Example 2** (design_principles.md, "Behaviours"): The `ch1` module is an example of a worker — a simple server that keeps track of channels and allows clients to allocate and free them.

# Relationships

## Builds Upon
- **Supervision Tree** — workers are one of the two process types in a supervision tree.

## Enables
- **gen_server** — gen_server is the most common behaviour for implementing workers
- **gen_event** — gen_event provides event handling workers

## Related
- **Behaviour** — workers are typically implemented using OTP behaviours

## Contrasts With
- **Supervisor Process** — supervisors monitor workers; workers perform actual work.

# Common Errors

- **Error**: Creating a worker process outside of a supervision tree using plain `spawn`.
  **Correction**: Use `gen_server:start_link/4` or equivalent to ensure the worker is linked to its supervisor.

# Common Confusions

- **Confusion**: Thinking workers must use OTP behaviours.
  **Clarification**: While the source strongly recommends behaviours for consistency and manageability, the text notes that "code written without using behaviours can be more efficient, but the increased efficiency is at the expense of generality."

# Source Reference

OTP Design Principles, Overview, "Supervision Trees" and "Behaviours" sections (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Supervision Trees" section.
- Confidence rationale: High — explicitly defined in the source.
- Uncertainties: None.
- Cross-reference status: References supervision-tree, supervisor-process, behaviour, gen-server, gen-event (planned cards).
