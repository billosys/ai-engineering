---
concept: Socket Active vs Passive Mode
slug: socket-active-vs-passive-mode
category: production-ops
subcategory: networking
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "More Control with Inet"
extraction_confidence: high
aliases:
  - "active mode"
  - "passive mode"
  - "active once"
  - "{active, once}"
prerequisites:
  - tcp-socket
  - udp-socket
extends: []
related:
  - inet-socket-option
  - gen-tcp
  - gen-udp
contrasts_with: []
answers_questions:
  - "What is the difference between active and passive socket mode?"
  - "What is active once mode?"
  - "How do I choose between active and passive mode?"
---

# Socket Active vs Passive Mode

## Quick Definition

A socket's mode determines how received data reaches your code: active mode delivers data as process messages; passive mode requires you to poll with `recv`. Active once mode delivers exactly one message, then reverts to passive.

## Core Definition

When opening a socket, the `{active, true}` option means data arrives "as messages," while `{active, false}` means data arrives "as results of a function call" via `recv` (Ch. 23, "UDP Sockets"). Passive mode is faster when you expect a message right away and avoids mailbox scanning, but turns the process into an active poller. Active mode fits event-driven code (just `receive` the packets) but is vulnerable to flooding because all incoming data is blindly converted to messages. `{active, once}` is a compromise: the socket delivers one message then becomes passive, giving active semantics with passive-mode safety (Ch. 23, "More Control with Inet").

## Prerequisites

- **Tcp-socket** — Mode applies to TCP sockets
- **Udp-socket** — Mode applies to UDP sockets too

## Key Properties

1. `{active, true}` — received data is delivered as `{tcp, ...}` / `{udp, ...}` messages to the owner's mailbox
2. `{active, false}` — passive; data is fetched by calling `gen_tcp:recv` / `gen_udp:recv`
3. `{active, once}` — one message is delivered, then the socket reverts to passive
4. Passive mode is faster for expected messages and avoids mailbox scanning
5. Active mode suits event-driven code but exposes the VM to flooding by external senders
6. Passive mode rate-limits by delegating blocking, queuing, and discarding to lower layers
7. Mode can be changed at runtime with `inet:setopts/2` without restarting the socket

## Construction / Recognition

### To pick a mode

1. If you expect a message immediately and want speed/rate-limiting: use passive (`{active, false}`) with `recv`
2. If you want event-driven `receive`/`handle_info` handling: use active (`{active, true}`)
3. If you want active semantics plus flood protection: use `{active, once}`, re-arming with `inet:setopts(Socket, [{active, once}])` after each message

## Context & Application

The book's `sockserv` uses `{active, once}` and re-arms it inside its `send` helper after every reply, so rate-limiting is governed by how fast the server sends.

## Examples

**Example** (Ch. 23): Switching a passive socket to active at runtime —

```erlang
4> inet:setopts(Accept, [{active, true}]).
ok
5> flush().
Shell got {tcp,#Port<0.598>,"hey there"}
```

**Example** (Ch. 23): With `{active, once}`, after one `flush()` shows `"one"`, the message `"two"` is not delivered until `inet:setopts(Accept, [{active, once}])` is called again.

## Relationships

### Related

- **Inet-socket-option** — `{active, ...}` is an `inet` option, changeable via `inet:setopts/2`
- **Gen-tcp** / **Gen-udp** — Mode is set when opening sockets with these modules

## Common Errors

- **Error**: Rapidly toggling between active and passive with `inet:setopts/2`.
  **Correction**: That risks race conditions; use `{active, once}` for safe back-and-forth.
- **Error**: Leaving a socket in `{active, false}` after dropping a message in a server.
  **Correction**: Re-arm the socket (e.g. `{active, once}`) after replying, or the client is locked out.

## Common Confusions

- **Confusion**: Thinking active mode is always more convenient.
  **Clarification**: Active mode lets external senders flood the VM with messages; passive mode provides rate limiting.
- **Confusion**: Believing `{active, once}` is permanent.
  **Clarification**: It delivers exactly one message then reverts to passive; it must be re-armed.

## Source Reference

Chapter 23, "Buckets of Sockets," sections "UDP Sockets" and "More Control with Inet."

## Verification Notes

- Definition: Direct adaptation from "More Control with Inet"
- Key Properties: All explicit in source
- Confidence: HIGH — the section explains and demonstrates all three modes
- Cross-references: `tcp-socket`, `udp-socket`, `inet-socket-option`, `gen-tcp`, `gen-udp` planned this chapter
