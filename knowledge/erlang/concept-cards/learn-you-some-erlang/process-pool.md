---
concept: Process Pool
slug: process-pool
category: applications-releases
subcategory: design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building an Application"
chapter_number: 18
pdf_page: null
section: "A Pool of Processes"
extraction_confidence: high
aliases:
  - process pool
  - worker pool
  - "ppool"
prerequisites:
  - supervisor
  - simple-one-for-one-supervisor
  - supervision-tree
extends: []
related:
  - supervision-tree
  - simple-one-for-one-supervisor
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
  - "What is a supervisor?"
---

# Process Pool

## Quick Definition

A process pool limits how many processes run concurrently and queues jobs when the worker limit is reached, managing and rationing resources in a generic way.

## Core Definition

"The idea behind such a process pool is to manage and limit resources running in a system in a generic manner. A pool allows us to limit how many processes run at once. A pool can also queue up jobs when the running workers' limit is hit. The jobs can then be run as soon as resources are freed up, or they can simply block by telling the user they can't do anything else" (Ch. 18, "A Pool of Processes").

## Prerequisites

- **Supervisor** — A pool is built from supervisors.
- **simple_one_for_one supervisor** — Workers are added dynamically under one.
- **Supervision tree** — The pool's components form a tree.

## Key Properties

1. It caps the number of concurrently running worker processes.
2. It queues jobs when the limit is hit; queued jobs run when resources free up.
3. It can also refuse a job outright (non-blocking) or block the caller (blocking) until room exists.
4. In the book's `ppool`, a top supervisor (`ppool_supersup`) holds many pools.
5. Each pool is a `gen_server` (counter + queue) plus a `simple_one_for_one` worker supervisor.
6. Workers are `temporary` — the pool does not assume how or whether to restart them.

## Construction / Recognition

## To Build a Process Pool

1. Add a top supervisor to hold and isolate individual pools.
2. Per pool, add a `gen_server` to track the worker count and job queue.
3. Per pool, add a `simple_one_for_one` supervisor for the workers.
4. Have the server dynamically attach its worker supervisor and start/queue workers via it.

## Context & Application

Process pools are useful to limit concurrent connections, cap open file descriptors, give subsystems different resource priorities, and keep a bursty application stable by queuing work. The `ppool` application is reused throughout Chapters 18–21: turned into an OTP application (Ch. 19), depended on by `erlcount` (Ch. 20), and packaged into a release (Ch. 21).

## Examples

**Example 1** (Ch. 18): `ppool` — `ppool_supersup` → per-pool `ppool_sup` → (`ppool_serv` + `ppool_worker_sup`) → workers.

**Example 2** (Ch. 18): Use cases — "Limit a server to at most N concurrent connections," "Limit how many files can be opened by an application."

## Relationships

## Builds Upon

- **Supervision tree** — The pool is a multi-level supervision tree.
- **simple_one_for_one supervisor** — Manages the dynamic worker children.

## Common Errors

- **Error**: Putting all pools under one supervisor with no isolating layer.
  **Correction**: Add a top supervisor so one pool crashing repeatedly cannot trip the restart limit for sibling pools.

## Common Confusions

- **Confusion**: Thinking a process pool restarts failed jobs automatically.
  **Clarification**: In `ppool`, workers are `temporary` — the pool deliberately does not restart them, since it cannot know the right restart policy and the caller often needs the worker pid.

## Source Reference

Chapter 18: "Building an Application," sections "A Pool of Processes," "A Pool's Tree," and "Implementing the Supervisors."

## Verification Notes

- Definition: Direct quotes from "A Pool of Processes."
- Key Properties: Synthesised from the architecture sections.
- Confidence: HIGH — extensively developed as the chapter's running example.
