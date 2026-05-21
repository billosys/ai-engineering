---
# === CORE IDENTIFICATION ===
concept: Controlling Process of a Socket
slug: controlling-process

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Sockets"
chapter_number: 17
pdf_page: null
section: "Notes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "socket owner"
  - "gen_tcp:controlling_process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - gen-tcp-module
extends: []
related:
  - socket-error-handling
  - active-and-passive-sockets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the controlling process of a socket?"
  - "What happens to a socket when its owning process dies?"
  - "How do I transfer socket ownership to another process?"
---

# Quick Definition

The controlling process of a socket is the process that created it. All messages from the socket are sent to this process, and if it dies, the socket is automatically closed.

# Core Definition

"The process that creates a socket (by calling `gen_tcp:accept` or `gen_tcp:connect`) is said to be the controlling process for that socket. All messages from the socket will be sent to the controlling process; if the controlling process dies, then the socket will be closed" ("Notes"). The controlling process for a socket "can be changed to `NewPid` by calling `gen_tcp:controlling_process(Socket, NewPid)`." This automatic linkage is the basis of socket error handling: a crashed controlling process causes its socket to close, which notifies the other end.

# Prerequisites

- **Process** — A socket is owned by exactly one process.
- **gen_tcp module** — Sockets are created by `gen_tcp:connect` / `gen_tcp:accept`.

# Key Properties

1. The controlling process is the process that created the socket via `gen_tcp:connect` or `gen_tcp:accept`.
2. All messages from the socket (`{tcp, Socket, Data}`, `{tcp_closed, Socket}`) go to the controlling process.
3. If the controlling process dies, the socket is automatically closed.
4. Ownership can be transferred with `gen_tcp:controlling_process(Socket, NewPid)`.
5. `gen_tcp` links itself to the controlling process, so a crash propagates to closing the socket.

# Construction / Recognition

## To recognize the controlling process:
1. Identify which process called `gen_tcp:connect` or `gen_tcp:accept` — that is the controlling process.

## To transfer ownership:
1. Call `gen_tcp:controlling_process(Socket, NewPid)` from the current controlling process.
2. `NewPid` then receives all future socket messages.

# Context & Application

- **Typical contexts**: Parallel servers where each connection-handling process owns its socket; designs that hand a socket off to a worker process.
- **Common applications**: The parallel server gives each spawned process ownership of its connection socket.
- **Historical/stylistic notes**: This ownership model is what makes socket error handling "extremely easy" — cleanup is automatic.

# Examples

**Example 1** ("Notes"): each process spawned by the parallel server is the controlling process for the socket it accepted.

**Example 2** ("Error Handling with Sockets"): when the controlling process of the server socket crashes, the socket is closed and the client receives `{tcp_closed, Socket}`.

# Relationships

## Related
- **Socket error handling** — Automatic socket closure on controlling-process death is the core of socket error handling.
- **Active and passive sockets** — Active sockets deliver messages to the controlling process.

# Common Errors

- **Error**: Expecting a socket to keep working after the process that created it has died.
  **Correction**: A socket is closed when its controlling process dies; transfer ownership with `gen_tcp:controlling_process/2` before the original process exits if the socket must outlive it.

# Common Confusions

- **Confusion**: Thinking any process can receive a socket's messages.
  **Clarification**: Only the controlling process receives socket messages; use `controlling_process/2` to change which process that is.

# Source Reference

Chapter 17: "Programming with Sockets", section "Notes" (under "Sequential and Parallel Servers") and "Error Handling with Sockets".

# Verification Notes

- Definition source: Direct quotes from "Notes".
- Confidence rationale: HIGH — the controlling process is explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used (`process`).
- Re-extraction notes: Fresh extraction; overwrites prior card.
