---
concept: UDP Socket
slug: udp-socket
category: production-ops
subcategory: networking
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "UDP Sockets"
extraction_confidence: high
aliases:
  - "UDP socket"
  - "datagram socket"
prerequisites:
  - process
extends: []
related:
  - gen-udp
  - tcp-socket
  - socket-active-vs-passive-mode
contrasts_with:
  - tcp-socket
answers_questions:
  - "What is a UDP socket?"
  - "When should I use UDP instead of TCP?"
  - "How do I open and use a UDP socket in Erlang?"
---

# UDP Socket

## Quick Definition

A UDP socket is a connectionless network endpoint built on the User Datagram Protocol. It sends and receives small untagged datagrams with no session, ordering, or delivery guarantees.

## Core Definition

UDP is "a protocol built on top of the IP layer that provides a few helpful abstractions, such as port numbers" and is "a connectionless protocol" (Ch. 23, "UDP and TCP: Bro-tocols"). Data received from a UDP port is broken into small untagged datagrams without a session; there is no guarantee fragments arrive in order, or at all. In Erlang, a single UDP socket over a given port can both send and receive data. The book likens it to mailboxes receiving tiny slips of paper with no guarantee of delivery.

## Prerequisites

- **Process** — The process that opens a UDP socket owns it and receives its messages

## Key Properties

1. UDP is connectionless — no handshake is required before sending
2. Datagrams may arrive out of order, duplicated, or not at all
3. A single socket over one port both sends and receives
4. Port numbers range 1-65535: well-known (0-1023), registered (1024-49151), dynamic/private (49152+)
5. In active mode the owner receives messages of the form `{udp, Socket, FromIp, FromPort, Message}`
6. A socket is represented as a `#Port<...>` value and can be linked like a pid
7. Opening an already-bound port returns `{error, eaddrinuse}`

## Construction / Recognition

### To use a UDP socket

1. Open: `{ok, Socket} = gen_udp:open(PortNumber)` (or with an options list)
2. Send: `gen_udp:send(OwnSocket, RemoteAddress, RemotePort, Message)`
3. Receive: in active mode, receive `{udp, Socket, FromIp, FromPort, Msg}`; in passive mode, call `gen_udp:recv(Socket, Length)`
4. Close: `gen_udp:close(Socket)`

## Context & Application

UDP is chosen when packets are small, occasional loss is acceptable, exchanges are not complex, and low latency is essential. For complex multi-message sessions, TCP is preferred.

## Examples

**Example** (Ch. 23): Opening a binary, active UDP socket and the duplicate-open error —

```erlang
1> {ok, Socket} = gen_udp:open(8789, [binary, {active,true}]).
{ok,#Port<0.676>}
2> gen_udp:open(8789, [binary, {active,true}]).
{error,eaddrinuse}
```

**Example** (Ch. 23): A flushed active-mode message: `Shell got {udp,#Port<0.676>,{127,0,0,1},8790,<<"hey there!">>}`.

## Relationships

### Related

- **Gen-udp** — The module providing the UDP socket API
- **Socket-active-vs-passive-mode** — Determines whether datagrams arrive as messages or via `recv`

### Contrasts With

- **Tcp-socket** — Connection-based, ordered, reliable; heavier to set up

## Common Errors

- **Error**: Opening a port already in use.
  **Correction**: Each port can be opened once; handle `{error, eaddrinuse}` or pick another port.
- **Error**: Expecting `recv/2`'s length argument to limit data with `gen_udp`.
  **Correction**: The length argument is ignored for `gen_udp` (unlike `gen_tcp`).

## Common Confusions

- **Confusion**: Assuming UDP datagrams arrive reliably and in order.
  **Clarification**: UDP gives no delivery, ordering, or duplication guarantees.
- **Confusion**: Thinking you need one port per conversation.
  **Clarification**: A single UDP port can serve all queries; if you need ordered sessions, use TCP instead.

## Source Reference

Chapter 23, "Buckets of Sockets," sections "UDP and TCP: Bro-tocols" and "UDP Sockets." See the `gen_udp:open` shell sessions.

## Verification Notes

- Definition: Direct adaptation from "UDP and TCP: Bro-tocols" and "UDP Sockets"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates UDP sockets in detail
- Cross-references: `gen-udp`, `tcp-socket`, `socket-active-vs-passive-mode` planned this chapter; `process` shared
