---
# === CORE IDENTIFICATION ===
concept: Process Identifier
slug: process-identifier

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-model
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Pid"
  - "PID"
  - "process id"
  - "self()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - spawn
  - message-passing
  - registered-process
contrasts_with:
  - registered-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Pid in Erlang?"
  - "How do I get a process's own identifier?"
  - "How is a process addressed for message sending?"
---

# Quick Definition

A process identifier (Pid) is the value that identifies a process. It is what `spawn` returns and what `!` sends messages to; `self()` yields the current process's own Pid.

# Core Definition

`spawn` "returns a `Pid` (short for process identifier)" and "You can use a `Pid` to send messages to the process" (Armstrong, "Concurrent Programming," "The Concurrency Primitives"). A Pid is printed in a form like `<0.36.0>`. The BIF `self()` returns the Pid of the calling process; this is how a client includes its own address in a request so the server knows where to reply: "`self()` is the PID of the client process" (Armstrong, "Concurrent Programming," "Introducing Client-Server"). When a process is created, only its parent knows its Pid — no other process knows about it unless the Pid is shared, which makes Pids secure.

# Prerequisites

- **Process** — A Pid identifies a process; you must know what a process is.

# Key Properties

1. A Pid is the value that uniquely identifies a process.
2. `spawn` returns the Pid of the newly created process.
3. `self()` returns the Pid of the calling process.
4. A Pid is the target of the send operator `!`.
5. Pids print in the form `<0.36.0>`.
6. Initially only the parent process knows a new process's Pid — making it private and secure.
7. A Pid can be carried inside a message (e.g. `{self(), Request}`) to provide a reply address.

# Construction / Recognition

## To Construct/Create:
1. Obtain a Pid from `spawn` (the new process) or `self()` (the current process).
2. Pass Pids in messages, or register them under a name, to share them.

## To Identify/Recognize:
1. A value printed as `<X.Y.Z>` is a Pid.
2. A `self()` call produces the current process's Pid.

# Context & Application

- **Typical contexts**: Addressing processes for message sending; client/server request/response correlation.
- **Common applications**: Including `self()` in a request as a reply address; binding a Pid into a `receive` pattern for selective receive.
- **Historical/stylistic notes**: Not revealing a process's Pid is a security property — "if you don't reveal the PID of a process, other processes can't interact with it in any way."

# Examples

**Example 1** ("The Concurrency Primitives"): `Pid = spawn(area_server0, loop, [])` binds `Pid` to `<0.36.0>`, the new process's identifier.

**Example 2** ("Introducing Client-Server"): `Pid ! {self(), {rectangle, 6, 10}}` — `self()` supplies the client's own Pid as a reply address.

**Example 3** ("Introducing Client-Server"): In `rpc`, the pattern `{Pid, Response}` uses the already-bound `Pid` so only the reply from that exact process matches.

# Relationships

## Builds Upon
- **Process** — A Pid is the identity of a process.

## Enables
- **Message passing** — `!` sends to a Pid.
- **Spawn** — `spawn` produces Pids.

## Related
- **Registered process** — Registration binds an atom name to a Pid.

## Contrasts With
- **Registered process** — A Pid is private to whoever holds it; a registered name is a public, system-wide alias for a Pid.

# Common Errors

- **Error**: Sending a request without `self()`, so the server has no reply address.
  **Correction**: Include `self()` in the request message (e.g. `{self(), Request}`).

- **Error**: Expecting a Pid to remain a valid target after the process has terminated.
  **Correction**: A dead process's Pid no longer receives messages; check liveness or use links/monitors.

# Common Confusions

- **Confusion**: Thinking `self()` returns the parent's Pid.
  **Clarification**: `self()` always returns the Pid of the process that calls it.

- **Confusion**: Believing every process's Pid is globally visible.
  **Clarification**: Only the parent knows a new process's Pid until it is explicitly shared or registered.

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives," "Introducing Client-Server," and "Registered Processes." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the Pid/`self()` descriptions in the named sections.
- Confidence rationale: HIGH — Pid and `self()` are defined explicitly.
- Uncertainties: None.
- Cross-reference status: Cross-refs verified against KB slugs.
- Re-extraction notes: Fresh extraction; new card (no prior file).
