---
concept: Worker Process
slug: worker-process
category: fault-tolerance
subcategory: supervision
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Supervisor Concepts"
extraction_confidence: high
aliases:
  - worker
prerequisites:
  - process
extends: []
related:
  - supervisor
  - supervision-tree
contrasts_with:
  - supervisor
answers_questions:
  - "What is a supervisor?"
  - "What must I understand before using supervisors?"
---

# Worker Process

## Quick Definition

A worker is a process that does actual application work and may crash while doing so. Workers are defined in opposition to supervisors and should always run under a supervisor.

## Core Definition

"Workers are defined a bit in opposition of supervisors. If supervisors are supposed to be processes that do nothing but make sure their children are restarted when they die, workers are processes that are in charge of doing actual work and that may die while doing so. They are usually not trusted to be safe" (Ch. 17, "Supervisor Concepts").

## Prerequisites

- **Process** — A worker is an Erlang process.

## Key Properties

1. Workers perform the actual work of an application.
2. Workers may crash and are "usually not trusted to be safe."
3. "Workers should never be used in any position except under a supervisor."
4. In a child specification, a worker has `Type = worker` (any OTP process that is not a supervisor).
5. A worker trapping exits runs its `terminate` function when the supervisor sends `shutdown`.

## Construction / Recognition

## To Recognise a Worker

1. It does domain work (handles requests, computes, holds state) — not just supervision.
2. It is typically a `gen_server`, `gen_fsm`/`gen_statem`, or `gen_event` manager.
3. Its child spec declares `Type = worker`.
4. It sits as a leaf (or near-leaf) in the supervision tree.

## Context & Application

The onion-layer design principle (Ch. 18) places the riskiest workers deep in the supervision tree and the processes that cannot afford to crash closer to the root. Workers embody "let it crash": rather than defensive coding, a worker crashes and its supervisor restarts it into a known-good state.

In the `band_supervisor`, each musician is a `gen_server` worker; in the process-pool example, the pooled jobs are workers under a `simple_one_for_one` worker supervisor.

## Examples

**Example 1** (Ch. 17): The `musicians` `gen_server` is a worker; its child spec ends with `worker, [musicians]`.

**Example 2** (Ch. 17): A musician with `skill=bad` crashes with reason `bad_note` — a worker dying while doing work.

## Relationships

## Builds Upon

- **Process** — A worker is a process.

## Related

- **supervisor** — Workers run under supervisors.
- **supervision-tree** — Workers are the leaves of the tree.

## Contrasts With

- **supervisor** — A supervisor does no work and never crashes from work; a worker does the work and may crash.

## Common Errors

- **Error**: Spawning a worker outside any supervision tree.
  **Correction**: Always place workers under a supervisor so they are accountable and shut down cleanly.

## Common Confusions

- **Confusion**: Thinking a worker must be a `gen_server`.
  **Clarification**: A worker is *any* OTP process that is not a supervisor — a `gen_server`, `gen_event` manager, FSM, etc.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Supervisor Concepts"; `Type` field in "Child Specifications."

## Verification Notes

- Definition: Direct quote from "Supervisor Concepts."
- Key Properties: Adapted from the section and the `Type` subsection.
- Confidence: HIGH — explicitly defined.
