---
concept: gen_tcp Module
slug: gen-tcp
category: production-ops
subcategory: networking
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "TCP Sockets"
extraction_confidence: high
aliases:
  - "gen_tcp"
prerequisites:
  - tcp-socket
extends: []
related:
  - gen-udp
  - inet-socket-option
  - controlling-process
contrasts_with:
  - gen-udp
answers_questions:
  - "What is the gen_tcp module?"
  - "How do I open a TCP socket in Erlang?"
  - "How do I write a TCP client and server with gen_tcp?"
---

# gen_tcp Module

## Quick Definition

`gen_tcp` is the standard Erlang module for working with TCP sockets — listening, accepting, connecting, sending, receiving, and closing connection-based sockets.

## Core Definition

`gen_tcp` provides the TCP socket API. Unlike `gen_udp`, it distinguishes server and client roles: a server calls `gen_tcp:listen/2` to create a listen socket and `gen_tcp:accept/1-2` to accept connections, while a client calls `gen_tcp:connect/3` (Ch. 23, "TCP Sockets"). It is one of the two main socket options in the standard Erlang distribution.

## Prerequisites

- **Tcp-socket** — `gen_tcp` is the API for TCP sockets

## Key Properties

1. `gen_tcp:listen(Port, Options)` creates a listen socket that waits for connection requests
2. `gen_tcp:accept(ListenSocket)` blocks until a client connects, returning an accept socket; `accept/2` adds a timeout
3. `gen_tcp:connect(Address, Port, Options)` creates a client socket; an optional `Timeout` may be supplied
4. `gen_tcp:send(Socket, Data)` sends data; `gen_tcp:close(Socket)` closes a socket
5. Most options are shared with `gen_udp`; TCP adds `{backlog, N}`, `{keepalive, true|false}`, `{packet, N}`
6. In active mode the owner receives `{tcp, Socket, Data}`, plus `{tcp_closed, Socket}` and `{tcp_error, Socket, Reason}`
7. `gen_tcp:controlling_process(Socket, Pid)` transfers socket ownership

## Construction / Recognition

### To build a TCP server

1. `{ok, Listen} = gen_tcp:listen(Port, [binary, {active, once}])`
2. `{ok, Accept} = gen_tcp:accept(Listen)`
3. Handle `{tcp, Accept, Data}` messages; `gen_tcp:send(Accept, Reply)`

### To build a TCP client

1. `{ok, Socket} = gen_tcp:connect(Address, Port, Options)`
2. `gen_tcp:send(Socket, Data)` and receive replies

## Context & Application

`gen_tcp` is used for reliable, ordered, session-based network services. The book's `sockserv` and the naive echo server are built on it; the same pattern underlies servers like `cowboy`.

## Examples

**Example** (Ch. 23): A naive echo acceptor —

```erlang
acceptor(ListenSocket) ->
    {ok, Socket} = gen_tcp:accept(ListenSocket),
    spawn(fun() -> acceptor(ListenSocket) end),
    handle(Socket).
```

**Example** (Ch. 23): `{packet, line}` passed to `gen_tcp:listen` makes received packets split into separate lines, queued line by line.

## Relationships

### Builds Upon

- **Tcp-socket** — `gen_tcp` is the concrete API for that concept

### Related

- **Inet-socket-option** — Options to `listen`/`connect` come from the `inet` option set
- **Controlling-process** — `gen_tcp:controlling_process/2` transfers ownership

### Contrasts With

- **Gen-udp** — The connectionless counterpart

## Common Errors

- **Error**: Accepting connections one at a time in a single sequential acceptor.
  **Correction**: Spawn a replacement acceptor before handling each connection (or pre-spawn many), or queued clients wait serially.
- **Error**: Doing `gen_tcp:accept` inside an OTP `init/1`.
  **Correction**: `accept` blocks and `init` is synchronous; cast a message to self and accept in the loop instead.

## Common Confusions

- **Confusion**: Thinking `gen_tcp` works like `gen_udp` with no distinct server role.
  **Clarification**: TCP servers must `listen` then `accept`; clients `connect`.

## Source Reference

Chapter 23, "Buckets of Sockets," sections "TCP Sockets" and "Sockserv, Revisited."

## Verification Notes

- Definition: Direct adaptation from "TCP Sockets"
- Key Properties: All explicit in source
- Confidence: HIGH — the section and the `sockserv` example demonstrate `gen_tcp` thoroughly
- Cross-references: `tcp-socket`, `gen-udp`, `inet-socket-option`, `controlling-process` planned this chapter
