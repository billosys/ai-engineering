---
# === CORE IDENTIFICATION ===
concept: Concurrent TCP Server Pattern
slug: tcp-server-pattern

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: networking
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.1.1. A pattern for efficient TCP servers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - efficient TCP server pattern
  - accept-loop pattern
  - simple-one-for-one TCP server

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - supervisor
  - erlang-process
extends: []
related:
  - active-passive-sockets
  - gen-web-server
  - simple-text-protocol
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the pattern for an efficient concurrent TCP server in Erlang?"
  - "How does a gen_server handle multiple concurrent TCP connections?"
  - "Why use a simple-one-for-one supervisor for a TCP server?"
---

# Quick Definition

The efficient TCP server pattern uses a `gen_server` handler managed by a simple-one-for-one supervisor: each handler accepts one connection, then asks the supervisor to spawn a clone to wait for the next.

# Core Definition

A useful pattern for implementing a server that should handle multiple concurrent requests is to have a `gen_server` managed by a simple-one-for-one supervisor. A single `gen_server` child process — a handler — is initially spawned to wait on `accept`, listening for new connections. When a connection is established, this `gen_server` tells the supervisor to spawn a new handler process (a clone of the `gen_server`) and immediately proceeds with servicing the current connection while the clone takes over waiting for the next connection. This allows accepting connections with little or no delay between the `accept` and the further handling of the connection ("Erlang and OTP in Action," Ch. 11, Section 11.1.1).

# Prerequisites

- **gen_server** — Each connection handler is a `gen_server`.
- **supervisor** — A simple-one-for-one supervisor acts as the handler factory.
- **Process** — The pattern relies on Erlang's lightweight concurrency.

# Key Properties

1. A simple-one-for-one supervisor spawns all handlers dynamically; they are all the same type.
2. Exactly one handler is actively blocked on `accept` at any time.
3. On accepting a connection, a handler immediately asks the supervisor for a new clone before servicing the connection.
4. A handler never returns to the listening state; it dies when its session ends.
5. The listening socket must be owned by a long-lived process (not by any handler), so it is opened in the application startup code (`_app` module) and handed to the supervisor.
6. The framework can handle tens of thousands of simultaneous connections with little code.

# Construction / Recognition

## To Construct/Create:
1. Create an OTP application with an `_app`, `_sup`, and `_server` module.
2. Open the listening socket in the `_app` module's `start/2`.
3. Make `_sup` a simple-one-for-one supervisor; pass the listening socket into its child spec.
4. In `_server` (a `gen_server`), return a timeout of 0 from `init/1` so `handle_info(timeout, ...)` runs.
5. In `handle_info(timeout, ...)`, call `gen_tcp:accept/1`; when it returns, call the supervisor's `start_child` to spawn the next handler.
6. Have the `_app` module call `start_child` once to create the first handler.

## To Identify/Recognize:
1. A simple-one-for-one supervisor whose worker is a `gen_server` that blocks on `accept` and self-spawns a successor.

# Context & Application

- **Typical contexts**: Industrial-strength concurrent TCP servers in Erlang.
- **Common applications**: The `tcp_interface` and `gen_web_server` applications in this chapter.
- **Historical/stylistic notes**: This is "the most Erlang-like way" to work with sockets — very different from the single-threaded accept loops common in other languages.

# Examples

**Example 1** (Section 11.1.1, Figure 11.1): A new child process is spawned for handling each new TCP `accept` and the subsequent client communication.

**Example 2** (Section 11.1.3): `ti_server` returns timeout 0 from `init/1`, drops into `handle_info(timeout, ...)`, blocks on `gen_tcp:accept/1`, then calls `ti_sup:start_child()` to spawn the next handler.

# Relationships

## Builds Upon
- **gen_server** — Handlers are `gen_server` processes.
- **supervisor** — A simple-one-for-one supervisor manages handlers.

## Enables
- **gen_web_server** — The custom web server behaviour is built on this pattern.

## Related
- **Active vs. passive sockets** — The handler's socket mode affects flow control.
- **Simple text-based protocol** — A protocol layered on top of this framework.

# Common Errors

- **Error**: Opening the listening socket inside a handler or in the supervisor `init/1` unnecessarily.
  **Correction**: Open it in a long-lived process such as the `_app` module so it is not closed when a handler dies.

- **Error**: Blocking on `accept` in a process other callers are waiting on.
  **Correction**: Detach the handler from its starter (return timeout 0 from `init/1`) before blocking on `accept`.

# Common Confusions

- **Confusion**: Thinking the supervisor itself accepts connections.
  **Clarification**: The supervisor is only a factory; the `gen_server` handlers do the accepting and connection servicing.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.1.1 "A pattern for efficient TCP servers." See Figure 11.1.

# Verification Notes

- Definition source: Direct adaptation of Section 11.1.1, with construction steps from Section 11.1.3.
- Confidence rationale: HIGH — the book explicitly presents this as a named pattern.
- Uncertainties: None.
- Cross-reference status: `gen-server`, `supervisor`, `process` owned by other agents.
- Re-extraction notes: Fresh extraction; no prior card existed.
