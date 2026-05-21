---
# === CORE IDENTIFICATION ===
concept: Sequential and Parallel Servers
slug: sequential-and-parallel-servers

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
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
  - "sequential server"
  - "parallel server"
  - "concurrent socket server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-tcp-server
  - spawn
extends:
  - simple-tcp-server
related:
  - gen-tcp
  - controlling-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between a sequential and a parallel server?"
  - "How do I make a TCP server handle many connections at once?"
---

# Quick Definition

A sequential server accepts one connection at a time; a parallel server spawns a new process for every accepted connection so multiple connections are served simultaneously. Both differ from the simple server only in how `gen_tcp:accept` is handled.

# Core Definition

By slightly changing the simple one-shot TCP server, the book derives two server types ("Sequential and Parallel Servers"). A **sequential server** accepts one connection at a time: it keeps the listening socket open and, after `loop(Socket)` finishes serving a connection, calls `seq_loop(Listen)` again to wait for the next. If a client connects while the server is busy, the connection is queued until the server finishes; if the queue exceeds the listen backlog, the connection is rejected. A **parallel server** accepts multiple parallel connections at the same time: the trick is to immediately `spawn` a new process each time `gen_tcp:accept` gets a new connection, so the spawned acceptor handles one client while the original process loops back to `accept` the next. All three servers call `gen_tcp:listen` and `gen_tcp:accept`; the only difference is whether these are called in a sequential or a parallel program — that is, the placement of the `spawn`.

# Prerequisites

- **A Simple TCP Server** — Both variants are derived by modifying the one-shot nano server.
- **spawn** — A parallel server depends on spawning a process per connection.

# Key Properties

1. A sequential server leaves the listening socket open and re-enters its accept loop after each connection.
2. A sequential server queues concurrent connection attempts up to the listen backlog, then rejects further ones.
3. A parallel server spawns a fresh process on each `gen_tcp:accept`, so connections run concurrently.
4. In a parallel server, the spawned process serves the connection while the original loops back to `accept`.
5. Stopping either server is done by killing the process(es) that started it — `gen_tcp` closes sockets when controlling processes die.
6. From R11B-3 on, multiple processes may call `gen_tcp:accept/1` on the same listen socket, allowing a pool of pre-spawned acceptors.

# Construction / Recognition

## To build a sequential server:

1. `gen_tcp:listen(...)`, then call `seq_loop(Listen)`.
2. In `seq_loop/1`: `{ok, Socket} = gen_tcp:accept(Listen)`, then `loop(Socket)`, then `seq_loop(Listen)` again.

## To build a parallel server:

1. `gen_tcp:listen(...)`, then `spawn(fun() -> par_connect(Listen) end)`.
2. In `par_connect/1`: `{ok, Socket} = gen_tcp:accept(Listen)`, immediately `spawn(fun() -> par_connect(Listen) end)`, then `loop(Socket)`.

# Context & Application

The sequential/parallel distinction is the canonical way to scale an Erlang socket server.

- **Typical contexts**: Any TCP service that must handle more than one client.
- **Common applications**: The chapter's SHOUTcast server is a parallel server serving many audio streams concurrently.
- **Historical/stylistic notes**: The book suggests limiting a parallel server's simultaneous connections with a counter incremented on connect and decremented on disconnect.

# Examples

**Example 1** ("A Sequential Server"): `start_seq_server/0` calls `seq_loop(Listen)`, which accepts a connection, serves it, then recurses to accept the next.

**Example 2** ("A Parallel Server"): `start_parallel_server/0` spawns `par_connect/1`, which accepts a connection, spawns another `par_connect/1`, then serves its own connection.

## Worked Example

The parallel server's core (from "A Parallel Server"):

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

- **A Simple TCP Server** — Both variants are edits of the simple nano server.

## Related

- **The gen_tcp module** — All three server forms use `gen_tcp:listen`/`accept`.
- **Controlling process** — Killing a server's process closes its sockets, the basis for stopping a server.

# Common Errors

- **Error**: Calling `gen_tcp:close(Listen)` in a sequential or parallel server.
  **Correction**: Leave the listening socket open so further connections can still be accepted.

- **Error**: In a parallel server, serving the connection before spawning the next acceptor.
  **Correction**: Spawn the next `par_connect` *before* entering `loop(Socket)`, so a new client can connect immediately.

# Common Confusions

- **Confusion**: Believing a parallel server needs fundamentally different socket calls.
  **Clarification**: It uses the same `gen_tcp:listen`/`accept`; only the placement of `spawn` differs.

# Source Reference

Chapter 17: "Programming with Sockets," section "Sequential and Parallel Servers" with subsections "A Sequential Server," "A Parallel Server," and "Notes." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of "Sequential and Parallel Servers."
- Confidence rationale: HIGH — both server forms are shown in full with explicit contrast.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
