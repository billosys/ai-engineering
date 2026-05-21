---
concept: Parallel TCP Acceptor Pool
slug: parallel-tcp-acceptor
category: production-ops
subcategory: networking
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "Sockserv, Revisited"
extraction_confidence: high
aliases:
  - "acceptor pool"
  - "parallel acceptors"
  - "socket acceptor pool"
prerequisites:
  - tcp-socket
  - gen-tcp
  - supervisor
extends: []
related:
  - gen-server
contrasts_with: []
answers_questions:
  - "How do I serve many TCP connections in parallel?"
  - "How does a simple_one_for_one supervisor share a listen socket?"
  - "Why pre-spawn TCP acceptor processes?"
---

# Parallel TCP Acceptor Pool

## Quick Definition

A parallel TCP acceptor pool is a design where many worker processes wait on the same listen socket simultaneously, so multiple incoming connections can be accepted at once instead of serially.

## Core Definition

A naive TCP server accepts one connection at a time: each acceptor waits, sets up the connection, then spawns the next acceptor. With a queue of clients, "only one query at a time can be replied to," so the Nth client waits for N-1 setups (Ch. 23, "Sockserv, Revisited"). The fix is to keep "many acceptors already on standby." The book builds this with a `simple_one_for_one` supervisor: because that strategy shares one child specification with all children, the listen socket is placed in the spec and every spawned worker receives it. The supervisor pre-spawns about 20 acceptors so connections can be served without serialization.

## Prerequisites

- **Tcp-socket** — The pool shares one listen socket
- **Gen-tcp** — Acceptors call `gen_tcp:accept` on the shared listen socket
- **Supervisor** — A `simple_one_for_one` supervisor manages the worker pool

## Key Properties

1. A naive single-acceptor server serializes connection setup, forcing later clients to wait
2. A `simple_one_for_one` supervisor shares its child spec — including the listen socket — with all children
3. The listen socket is opened in the supervisor's `init/1` and passed into every worker
4. The supervisor pre-spawns a pool (the book uses 20) of acceptors on standby
5. Pre-spawning must be done from an external process (`spawn_link`), because the supervisor cannot answer messages during `init/1`
6. Each worker, on accepting a connection, starts a replacement acceptor so the pool stays full
7. Workers are `temporary` children, since a closed connection is a normal termination

## Construction / Recognition

### To build the pool

1. In the supervisor `init/1`, open the listen socket with `gen_tcp:listen`
2. Use a `simple_one_for_one` strategy with the listen socket baked into the child spec
3. `spawn_link` an external function that calls `start_socket/0` ~20 times to fill the pool
4. Each worker, after `gen_tcp:accept`, calls `start_socket/0` to spawn its replacement

## Context & Application

The book notes this pattern is the same one used in real servers like `cowboy` and `etorrent`. It scales connection acceptance and avoids the global-state reflex of a registered process holding the listen socket.

## Examples

**Example** (Ch. 23): The `sockserv_sup` supervisor —

```erlang
init([]) ->
    {ok, Port} = application:get_env(port),
    {ok, ListenSocket} = gen_tcp:listen(Port, [{active,once}, {packet,line}]),
    spawn_link(fun empty_listeners/0),
    {ok, {{simple_one_for_one, 60, 3600},
          [{socket, {sockserv_serv, start_link, [ListenSocket]},
            temporary, 1000, worker, [sockserv_serv]}]}}.

empty_listeners() ->
    [start_socket() || _ <- lists:seq(1,20)],
    ok.
```

## Relationships

### Builds Upon

- **Tcp-socket** — One listen socket is shared across the pool
- **Supervisor** — A `simple_one_for_one` supervisor enables shared child specs

### Related

- **Gen-server** — Each acceptor worker is a `gen_server`

## Common Errors

- **Error**: Calling `start_socket/0` from within the supervisor's own `init/1`.
  **Correction**: The supervisor cannot answer messages during `init`; pre-spawn from an external `spawn_link`ed process.
- **Error**: Doing `gen_tcp:accept` inside the worker's `init/1`.
  **Correction**: `accept` blocks and `init` is synchronous; cast `accept` to self and accept in `handle_cast`.

## Common Confusions

- **Confusion**: Thinking a registered global process must hold the listen socket.
  **Clarification**: A `simple_one_for_one` supervisor shares the socket via the child spec — no global state needed.
- **Confusion**: Believing one acceptor is enough.
  **Clarification**: One acceptor serializes connection setup; a pool lets many connections be accepted concurrently.

## Source Reference

Chapter 23, "Buckets of Sockets," section "Sockserv, Revisited."

## Verification Notes

- Definition: Direct adaptation from "Sockserv, Revisited"
- Key Properties: All explicit in source
- Confidence: HIGH — the section walks through the `sockserv_sup` design in detail
- Cross-references: `tcp-socket`, `gen-tcp` planned this chapter; `supervisor`, `gen-server` shared slugs
