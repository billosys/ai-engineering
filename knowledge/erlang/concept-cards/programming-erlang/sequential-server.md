---
# === CORE IDENTIFICATION ===
concept: Sequential Server
slug: sequential-server

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
section: "Sequential and Parallel Servers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "one-connection-at-a-time server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - simple-tcp-server
extends:
  - simple-tcp-server
related: []
contrasts_with:
  - parallel-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a sequential server?"
  - "How do I write a server that handles one connection at a time?"
  - "What is the difference between a sequential and a parallel server?"
---

# Quick Definition

A sequential server is a TCP server that accepts and fully serves one connection at a time before accepting the next. New connections queue while the server is busy.

# Core Definition

A sequential server is "one that accepts one connection at a time" ("Sequential and Parallel Servers"). It is built by keeping the listening socket open and looping: accept a connection, serve it to completion, then loop back to accept the next. Unlike the simplest server (which terminates after one connection), the sequential server does not close the listening socket and recurses into the accept loop after each client is served. "If a client tries to connect to the server while the server is busy with an existing connection, then the connection will be queued until the server has finished with the existing connection. If the number of queued connections exceeds the listen backlog, then the connection will be rejected."

# Prerequisites

- **gen_tcp module** — Uses `gen_tcp:listen/2` and `gen_tcp:accept/1`.
- **Simple TCP server** — The sequential server is a small modification of the single-shot server.

# Key Properties

1. Handles exactly one connection at a time.
2. The listening socket is kept open (not closed after accept) so further connections can be served.
3. After serving one client, the server loops back to `gen_tcp:accept`.
4. Connections arriving while the server is busy are queued.
5. If queued connections exceed the listen backlog, new connections are rejected.
6. Stopped by killing the process that started the server.

# Construction / Recognition

## To construct a sequential server:
1. Call `gen_tcp:listen(...)` to obtain the listening socket.
2. Enter a loop function `seq_loop(Listen)`.
3. In the loop, call `gen_tcp:accept(Listen)` to get a connection socket.
4. Serve that connection fully with `loop(Socket)`.
5. Recurse: call `seq_loop(Listen)` to accept the next connection.

## To recognize a sequential server:
1. The listening socket is reused across connections.
2. There is no `spawn` per connection — one connection blocks the next.

# Context & Application

- **Typical contexts**: Servers where requests are short and concurrency is unnecessary, or where serializing requests is desirable.
- **Common applications**: Simple request/response services with low connection volume.
- **Historical/stylistic notes**: Presented alongside the parallel server as the two variants derivable from the single-shot server.

# Examples

**Example 1** ("A Sequential Server"): `start_seq_server/0` listens, then calls `seq_loop(Listen)`.

## Worked Example

```erlang
start_seq_server() ->
    {ok, Listen} = gen_tcp:listen(...),
    seq_loop(Listen).

seq_loop(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    loop(Socket),
    seq_loop(Listen).

loop(..) -> %% as before
```

# Relationships

## Builds Upon
- **Simple TCP server** — Adds a loop that reuses the listening socket.

## Contrasts With
- **Parallel server** — A parallel server spawns a new process per connection so multiple clients are served simultaneously.

# Common Errors

- **Error**: Closing the listening socket after the first accept.
  **Correction**: Keep the listening socket open so subsequent connections can be served.

- **Error**: Expecting concurrent clients to be served simultaneously.
  **Correction**: A sequential server serializes clients; use a parallel server for concurrency.

# Common Confusions

- **Confusion**: Thinking queued connections are lost while the server is busy.
  **Clarification**: They are queued up to the listen backlog; only connections beyond the backlog are rejected.

# Source Reference

Chapter 17: "Programming with Sockets", section "Sequential and Parallel Servers", subsection "A Sequential Server".

# Verification Notes

- Definition source: Direct quotes from "Sequential and Parallel Servers".
- Confidence rationale: HIGH — the server type is explicitly defined and coded.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
