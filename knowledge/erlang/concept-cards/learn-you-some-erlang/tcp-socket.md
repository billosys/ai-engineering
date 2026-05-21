---
concept: TCP Socket
slug: tcp-socket
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
  - "TCP socket"
  - "listen socket"
  - "accept socket"
prerequisites:
  - process
  - udp-socket
extends: []
related:
  - gen-tcp
  - socket-active-vs-passive-mode
  - controlling-process
contrasts_with:
  - udp-socket
answers_questions:
  - "What is a TCP socket?"
  - "How do I open a TCP socket in Erlang?"
  - "What is the difference between a listen socket and an accept socket?"
---

# TCP Socket

## Quick Definition

A TCP socket is a connection-based, stateful network endpoint. It provides reliable, ordered, session-isolated communication after a handshake, at the cost of more setup overhead than UDP.

## Core Definition

TCP "is said to be stateful, connection-based. Before being able to send messages, you must do a handshake" (Ch. 23, "UDP and TCP: Bro-tocols"). The protocol handles lost packets, reordering, and isolated sessions. In Erlang TCP differs from UDP in that clients and servers are different things: a server opens a *listen socket* with `gen_tcp:listen/2`, then any process can call `gen_tcp:accept/1-2` to get an *accept socket* once a client connects. A client calls `gen_tcp:connect/3` and behaves much like `gen_udp` (Ch. 23, "TCP Sockets").

## Prerequisites

- **Process** — The process that opens a socket owns it and reads its messages
- **Udp-socket** — TCP sockets share most of the UDP socket interface; UDP is presented first

## Key Properties

1. TCP is connection-based and requires a handshake before data transfer
2. TCP guarantees ordered, reliable delivery within a session
3. A server uses a *listen socket* (waits for connection requests) and *accept sockets* (one per established connection)
4. More than one process can call `accept` on the same listen socket and block waiting
5. A client socket is created with `gen_tcp:connect/3`
6. TCP-specific options include `{backlog, N}`, `{keepalive, true|false}`, and `{packet, N}`
7. Closing an accept socket closes only that socket; closing a listen socket closes no established accept sockets but interrupts pending `accept` calls

## Construction / Recognition

### Server side

1. Open a listen socket: `{ok, Listen} = gen_tcp:listen(Port, Options)`
2. Accept connections: `{ok, AcceptSocket} = gen_tcp:accept(Listen)` (blocks until a client connects)
3. Communicate over the accept socket; close with `gen_tcp:close/1`

### Client side

1. Connect: `{ok, Socket} = gen_tcp:connect(Address, Port, Options)`
2. Send/receive; close with `gen_tcp:close/1`

## Context & Application

TCP is chosen when reliable, ordered, multi-message exchanges are needed. The book notes the listen socket is bound to the process that opened it, so that process must stay alive while accepting connections.

## Examples

**Example** (Ch. 23): Server opens a listen socket and accepts —

```erlang
1> {ok, ListenSocket} = gen_tcp:listen(8091, [{active, true}, binary]).
{ok,#Port<0.661>}
2> {ok, AcceptSocket} = gen_tcp:accept(ListenSocket).
```

**Example** (Ch. 23): Client connects and sends; the server flushes `{tcp, #Port<0.729>, <<"Hey there first shell!">>}`.

## Relationships

### Builds Upon

- **Udp-socket** — Shares most of its interface; UDP introduces the simpler model first

### Related

- **Gen-tcp** — The module providing the TCP socket API
- **Socket-active-vs-passive-mode** — Controls how received data is delivered
- **Controlling-process** — TCP accept and client sockets can have ownership transferred

### Contrasts With

- **Udp-socket** — Connectionless, unordered, unreliable; faster and lighter

## Common Errors

- **Error**: Letting the process that opened the listen socket die while still serving connections.
  **Correction**: The listen socket is bound to its owner; keep that process alive (the naive server idles forever for this reason).
- **Error**: Calling `accept` with a short timeout and then crashing on `{error, timeout}`.
  **Correction**: Use `accept/1` without a timeout, or handle the timeout result explicitly.

## Common Confusions

- **Confusion**: Thinking the listen socket and accept socket are the same thing.
  **Clarification**: The listen socket only waits for connection requests; each accepted connection yields a separate accept socket.
- **Confusion**: Believing closing the listen socket closes all client connections.
  **Clarification**: It closes none of the established accept sockets; it only interrupts pending `accept` calls.

## Source Reference

Chapter 23, "Buckets of Sockets," sections "UDP and TCP: Bro-tocols" and "TCP Sockets." See the `gen_tcp:listen`/`accept`/`connect` shell sessions.

## Verification Notes

- Definition: Direct adaptation from "TCP Sockets"
- Key Properties: All explicit in source
- Confidence: HIGH — the section walks through TCP sockets thoroughly
- Cross-references: `gen-tcp`, `udp-socket`, `socket-active-vs-passive-mode`, `controlling-process` planned this chapter; `process` shared
