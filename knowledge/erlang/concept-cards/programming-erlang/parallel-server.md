---
# === CORE IDENTIFICATION ===
concept: Parallel Server
slug: parallel-server

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
  - "concurrent server"
  - "multi-connection server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - simple-tcp-server
  - spawn
extends:
  - simple-tcp-server
related:
  - controlling-process
contrasts_with:
  - sequential-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a parallel server?"
  - "How do I handle multiple simultaneous TCP connections?"
  - "What is the difference between a sequential and a parallel server?"
---

# Quick Definition

A parallel server is a TCP server that accepts multiple connections at the same time, spawning a fresh process to handle each new connection so clients are served concurrently.

# Core Definition

A parallel server is "one that accepts multiple parallel connections at the same time" ("Sequential and Parallel Servers"). "The trick to making a parallel server is to immediately spawn a new process each time `gen_tcp:accept` gets a new connection" ("A Parallel Server"). Each accepted connection runs in its own process, so a slow client cannot block other clients. As of Erlang R11B-3, several processes may call `gen_tcp:accept/1` on the same listening socket, which "simplifies making a parallel server, because you can have a pool of prespawned processes, all waiting in `gen_tcp:accept/1`."

# Prerequisites

- **gen_tcp module** — Uses `gen_tcp:listen/2` and `gen_tcp:accept/1`.
- **Simple TCP server** — The parallel server is a modification of the single-shot server.
- **spawn** — A new process is spawned per accepted connection.

# Key Properties

1. Serves multiple connections concurrently.
2. A new process is spawned immediately for each accepted connection.
3. After accepting, the connection-handling process spawns another `par_connect` process before serving its own client, keeping an acceptor always available.
4. Can potentially create many thousands of connections; the maximum may be limited with a connection counter.
5. From R11B-3 onward, multiple processes can call `gen_tcp:accept/1` on the same listening socket — enabling a prespawned acceptor pool.
6. Stopped by killing the controlling process(es).

# Construction / Recognition

## To construct a parallel server:
1. Call `gen_tcp:listen(...)` to obtain the listening socket.
2. `spawn` a process running `par_connect(Listen)`.
3. In `par_connect`, call `gen_tcp:accept(Listen)`.
4. Immediately `spawn` another `par_connect(Listen)` to keep accepting.
5. Serve the current connection with `loop(Socket)`.

## To recognize a parallel server:
1. There is a `spawn` for every accepted connection.
2. Multiple clients can be served simultaneously without blocking one another.

# Context & Application

- **Typical contexts**: Servers handling many simultaneous clients — web servers, chat servers, streaming servers.
- **Common applications**: The SHOUTcast server and IRC-style servers follow this pattern.
- **Historical/stylistic notes**: Limiting maximum simultaneous connections is recommended via a counter incremented on connect and decremented on disconnect.

# Examples

**Example 1** ("A Parallel Server"): `start_parallel_server/0` listens then `spawn(fun() -> par_connect(Listen) end)`.

## Worked Example

```erlang
start_parallel_server() ->
    {ok, Listen} = gen_tcp:listen(...),
    spawn(fun() -> par_connect(Listen) end).

par_connect(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    spawn(fun() -> par_connect(Listen) end),
    loop(Socket).
```

# Relationships

## Builds Upon
- **Simple TCP server** — Adds a `spawn` per connection.

## Enables
- **Controlling process** — Each spawned process becomes the controlling process for its socket.

## Contrasts With
- **Sequential server** — A sequential server serves one client at a time; a parallel server serves many concurrently.

# Common Errors

- **Error**: Spawning the next acceptor after serving the current connection instead of before.
  **Correction**: Spawn the next `par_connect` immediately after `accept` returns, so the server keeps accepting while a connection is being served.

- **Error**: Allowing unbounded connections.
  **Correction**: Maintain a counter to cap the number of simultaneous connections.

# Common Confusions

- **Confusion**: Thinking each connection needs its own listening socket.
  **Clarification**: All connection processes share one listening socket; from R11B-3 multiple processes may even call `accept` on it.

# Source Reference

Chapter 17: "Programming with Sockets", section "Sequential and Parallel Servers", subsection "A Parallel Server", plus the "Notes" subsection.

# Verification Notes

- Definition source: Direct quotes from "A Parallel Server" and "Notes".
- Confidence rationale: HIGH — explicitly defined and coded.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used (`spawn`).
- Re-extraction notes: Fresh extraction.
