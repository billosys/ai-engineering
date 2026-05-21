---
# === CORE IDENTIFICATION ===
concept: Error Handling with Sockets
slug: socket-error-handling

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
section: "Error Handling with Sockets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "tcp_closed message"
  - "automatic socket cleanup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - controlling-process
  - gen-tcp-module
extends: []
related:
  - error-handling-philosophy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle errors with sockets?"
  - "What happens when a socket's controlling process crashes?"
  - "How does a client learn that a server has died?"
---

# Quick Definition

Error handling with sockets is largely automatic: each socket has a controlling process, and if that process dies the socket is closed, sending the other end a `{tcp_closed, Socket}` message.

# Core Definition

"Error handling with sockets is extremely easy — basically you don't have to do anything. As we said earlier, each socket has a controlling process ... If the controlling process dies, then the socket will be automatically closed" ("Error Handling with Sockets"). Consequently, "if we have, for example, a client and a server and the server dies because of a programming error, the socket owned by the server will be automatically closed, and the client will be sent a `{tcp_closed, Socket}` message." This fits Erlang's broader let-it-crash philosophy: the socket layer handles cleanup, and the program only needs to handle the `{tcp_closed, Socket}` message.

# Prerequisites

- **Controlling process** — Automatic cleanup depends on the socket's controlling process.
- **gen_tcp module** — Socket close messages are part of the `gen_tcp` message protocol.

# Key Properties

1. Each socket has a controlling process; cleanup is tied to it.
2. If the controlling process dies, the socket is automatically closed.
3. When one end's socket closes, the other end receives `{tcp_closed, Socket}`.
4. The application does not need explicit error-handling code beyond handling `{tcp_closed, Socket}`.
5. A crash in the controlling process produces a normal Erlang error report, and the socket cleanup follows automatically.

# Construction / Recognition

## To handle socket errors:
1. In the receive loop, include a `{tcp_closed, Socket}` clause.
2. Treat `{tcp_closed, Socket}` as the signal that the connection (or the other end's process) has ended.
3. Rely on the runtime to close sockets owned by crashed processes.

# Context & Application

- **Typical contexts**: Any client/server pair built on `gen_tcp`.
- **Common applications**: The `error_test` example deliberately crashes the server to show the client receiving `{tcp_closed, Socket}`.
- **Historical/stylistic notes**: An instance of Erlang's general error-handling philosophy — let the process crash; cleanup is automatic.

# Examples

**Example 1** ("Error Handling with Sockets", `socket_examples.erl`): `error_test/0` spawns a server, connects, and sends `<<"123">>`; the server crashes calling `atom_to_list` on a binary, and the client then receives `Any={tcp_closed,#Port<0.152>}`.

# Relationships

## Related
- **Error-handling philosophy** — Socket error handling is a concrete instance of Erlang's let-it-crash approach.

# Common Errors

- **Error**: Writing elaborate manual cleanup code for sockets.
  **Correction**: Rely on automatic closure when the controlling process dies; only handle the `{tcp_closed, Socket}` message.

- **Error**: Omitting a `{tcp_closed, Socket}` clause from the receive loop.
  **Correction**: Always handle `{tcp_closed, Socket}` so the program detects connection termination.

# Common Confusions

- **Confusion**: Thinking a crashed server leaves the client hanging forever.
  **Clarification**: The server's socket closes automatically and the client is promptly sent `{tcp_closed, Socket}`.

# Source Reference

Chapter 17: "Programming with Sockets", section "Error Handling with Sockets". Code from `socket_examples.erl`.

# Verification Notes

- Definition source: Direct quotes from "Error Handling with Sockets".
- Confidence rationale: HIGH — explicitly described with a demonstrating example.
- Uncertainties: None.
- Cross-reference status: Verified; `error-handling-philosophy` is an existing card.
- Re-extraction notes: Fresh extraction; overwrites prior card.
