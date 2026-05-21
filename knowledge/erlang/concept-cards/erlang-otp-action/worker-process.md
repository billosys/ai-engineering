---
# === CORE IDENTIFICATION ===
concept: Worker Process
slug: worker-process

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.2.3 Writing the child specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - worker
  - worker behaviour

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - erlang-process
extends: []
related:
  - supervision-tree
  - child-specification
  - gen-server
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a worker process in a supervision tree?"
  - "How does a worker differ from a supervisor?"
  - "What worker behaviours does OTP provide?"
---

# Quick Definition

A worker process is any process in a supervision tree that does actual work and does not implement the `supervisor` behaviour. Workers are the leaves of the supervision tree.

# Core Definition

A worker process is any process in a supervision tree that does not implement the `supervisor` behaviour (Ch. 4, Section 4.2.3). Workers are the processes that do the work of an active application; they are started indirectly by supervisors and restarted by them if necessary. The standard OTP worker behaviours are `gen_server`, `gen_event`, and `gen_fsm`; these conform to interfaces and return-value conventions and set up process links so they can be hooked into a supervision tree. Code that is not based on a standard behaviour can still be included via the `supervisor_bridge` adapter. A child specification's `Type` field distinguishes a `worker` from a `supervisor`.

# Prerequisites

- **Supervisor** — Workers are children of supervisors.
- **Process** — A worker is a process.

# Key Properties

1. Any supervision-tree process that is not a supervisor.
2. Does the actual work of the application.
3. Started and restarted by a supervisor.
4. Standard worker behaviours: `gen_server`, `gen_event`, `gen_fsm`.
5. Marked `worker` in the `Type` field of its child specification.
6. Non-behaviour code can be a worker via `supervisor_bridge`.

# Construction / Recognition

## To Recognize a Worker:
1. Check the child specification `Type` field — `worker` means a worker process.
2. Confirm the module does not implement the `supervisor` behaviour.

# Context & Application

Workers carry the application's functionality; supervisors keep them alive. The division — workers do work, supervisors monitor — is central to OTP fault tolerance.

- **Typical contexts**: Servers, event handlers, state machines under a supervisor.
- **Common applications**: `tr_server` is a worker under `tr_sup`; each `sc_element` is a worker under `sc_sup`.

# Examples

**Example 1** (Ch. 4): In the `tr_server` child specification, the `Type` field is `worker`, because the server process is clearly a worker.

**Example 2** (Ch. 6): The `sc_element` processes are workers under the `sc_sup` simple-one-for-one supervisor.

# Relationships

## Related
- **supervision-tree** — Workers are the leaves of the tree.
- **child-specification** — A worker is described by a child specification with `Type` `worker`.
- **gen-server** — A common worker behaviour.

## Contrasts With
- **supervisor** — A supervisor only monitors and restarts; a worker does actual work and does not implement the `supervisor` behaviour.

# Common Errors

- **Error**: Marking a child supervisor as `worker` in its child specification.
  **Correction**: Use `supervisor` as the `Type` so the parent knows the child is also a supervisor.

# Common Confusions

- **Confusion**: Thinking only `gen_server` processes can be workers.
  **Clarification**: Any non-supervisor process is a worker; `gen_event` and `gen_fsm` processes, and even non-behaviour code via `supervisor_bridge`, are workers too.

# Source Reference

Chapter 4: OTP applications and supervision, Sections 4.2 and 4.2.3 ("Writing the child specification").

# Verification Notes

- Definition source: Direct adaptation of Sections 4.2 and 4.2.3.
- Confidence rationale: HIGH — explicit definition in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
