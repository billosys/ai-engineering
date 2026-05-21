---
concept: Process Identifier
slug: process-identifier
category: processes-concurrency
subcategory: concurrency-primitives
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Spawning Processes"
extraction_confidence: high
aliases:
  - "pid"
  - "Pid"
  - "PID"
prerequisites:
  - process
extends: []
related:
  - spawn
  - message-passing
  - named-process
contrasts_with: []
answers_questions:
  - "What is a pid?"
  - "How do I refer to a process?"
---

# Process Identifier

## Quick Definition

A process identifier (pid) is the value that identifies an Erlang process and serves as its address for message passing. It is returned by `spawn` and by `self/0`.

## Core Definition

The result of `spawn/1` — printed like `<0.44.0>` — "is called a *process identifier*, often just written as *pid*... The pid is an arbitrary value representing any process that exists (or might have existed) at some point in the VM's life. It is used as an address to communicate with the process." A process gets its own pid from the BIF `self/0`. Because pids change when a process is restarted, code that must survive restarts often registers the process under a stable name instead (Hébert, ch. 10, "Spawning Processes").

## Prerequisites

- **Process** — A pid identifies a process

## Key Properties

1. A pid is an arbitrary value identifying a process
2. Printed in the form `<X.Y.Z>` (e.g. `<0.44.0>`)
3. Returned by `spawn/1` and `spawn/3`; a process gets its own via `self/0`
4. Used as the address for the `!` send operator
5. A pid may refer to a process that existed at some point — not necessarily a live one
6. A restarted process gets a new pid; stable references use registered names

## Construction / Recognition

## To Obtain and Use a Pid

1. Capture the return value of `spawn`: `Pid = spawn(...)`
2. Get the current process's pid with `self()`
3. Resolve a registered name to a pid with `whereis(Name)`
4. Send to it: `Pid ! Message`

## Examples

> **From spawn** (ch. 10): `spawn(F).` returns `<0.44.0>`.
>
> **From self** (ch. 10): `self()` returns the shell's pid `<0.41.0>`; after `exit(self())` a later `self()` returns a different pid because the process restarted.

## Relationships

## Builds Upon

- **Process** — A pid is a process's identity

## Related

- **Spawn** — Produces a pid
- **Message passing** — Uses the pid as the send address
- **Named process** — A stable atom name avoids depending on a changeable pid

## Common Errors

- **Error**: Storing a pid long-term and assuming it stays valid across a restart
  **Correction**: Restarted processes get new pids; use a registered name for stable addressing

## Common Confusions

- **Confusion**: Thinking a pid guarantees a live process
  **Clarification**: A pid may refer to a process that has since died

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "So Long and Thanks for All the Fish!", subsection "Spawning Processes."

## Verification Notes

- Definition: directly from ch. 10
- Confidence: HIGH — explicitly defined
