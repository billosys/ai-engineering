---
concept: gen_udp Module
slug: gen-udp
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
  - "gen_udp"
prerequisites:
  - udp-socket
extends: []
related:
  - gen-tcp
  - inet-socket-option
  - controlling-process
contrasts_with:
  - gen-tcp
answers_questions:
  - "What is the gen_udp module?"
  - "How do I send and receive UDP datagrams in Erlang?"
---

# gen_udp Module

## Quick Definition

`gen_udp` is the standard Erlang module for working with UDP sockets — opening, sending, receiving, and closing connectionless datagram sockets.

## Core Definition

`gen_udp` provides "only a few basic operations with UDP: setting up a socket, sending messages, receiving messages, and closing a connection" (Ch. 23, "UDP Sockets"). A socket is created with `gen_udp:open/1-2`, datagrams are sent with `gen_udp:send/4`, polled with `gen_udp:recv/2-3` in passive mode, and closed with `gen_udp:close/1`. The module is one of two main socket options in the standard distribution, alongside `gen_tcp`.

## Prerequisites

- **Udp-socket** — `gen_udp` is the API for UDP sockets

## Key Properties

1. `gen_udp:open(PortNumber)` opens a socket; `open/2` accepts an options list
2. Options control data type (`list`/`binary`), delivery mode (`{active, true|false}`), IP version (`inet4`/`inet6`), and `{broadcast, true|false}`
3. `gen_udp:send(OwnSocket, RemoteAddress, RemotePort, Message)` sends a datagram
4. `RemoteAddress` may be a domain name string/atom, an IPv4 4-tuple, or an IPv6 8-tuple
5. `Message` may be a string, binary, or IO list
6. `gen_udp:recv(Socket, Length)` polls a passive socket; the `Length` argument is ignored for `gen_udp`
7. `recv/3` adds a timeout, returning `{error, timeout}` if no message arrives in time
8. `gen_udp:controlling_process(Socket, Pid)` transfers socket ownership

## Construction / Recognition

### To exchange UDP data

1. `{ok, Socket} = gen_udp:open(Port, [binary, {active, true}])`
2. `gen_udp:send(Socket, {127,0,0,1}, RemotePort, "message")`
3. Receive `{udp, Socket, FromIp, FromPort, Msg}` (active) or `gen_udp:recv(Socket, 0)` (passive)
4. `gen_udp:close(Socket)`

## Context & Application

`gen_udp` is used wherever lightweight, low-latency, connectionless messaging is appropriate.

## Examples

**Example** (Ch. 23): Sending from a second shell —

```erlang
1> {ok, Socket} = gen_udp:open(8790).
{ok,#Port<0.587>}
2> gen_udp:send(Socket, {127,0,0,1}, 8789, "hey there!").
ok
```

**Example** (Ch. 23): A passive-mode `recv` with timeout: `gen_udp:recv(Socket, 0, 2000)` returns `{error, timeout}` when nothing arrives.

## Relationships

### Builds Upon

- **Udp-socket** — `gen_udp` is the concrete API for that concept

### Related

- **Inet-socket-option** — Socket options passed to `open/2` come from the `inet` option set
- **Controlling-process** — `gen_udp:controlling_process/2` transfers ownership

### Contrasts With

- **Gen-tcp** — The connection-based counterpart

## Common Errors

- **Error**: Relying on `recv/2`'s length argument to bound the datagram.
  **Correction**: The length is ignored for `gen_udp`; that argument matters only for `gen_tcp`.
- **Error**: Calling `recv` on an active socket.
  **Correction**: `recv` is for passive sockets; active sockets deliver `{udp, ...}` messages instead.

## Common Confusions

- **Confusion**: Thinking `gen_udp:send` opens a connection.
  **Clarification**: UDP is connectionless; `send/4` names the remote address and port directly each call.

## Source Reference

Chapter 23, "Buckets of Sockets," section "UDP Sockets."

## Verification Notes

- Definition: Direct adaptation from "UDP Sockets"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates the full `gen_udp` API
- Cross-references: `udp-socket`, `gen-tcp`, `inet-socket-option`, `controlling-process` planned this chapter
