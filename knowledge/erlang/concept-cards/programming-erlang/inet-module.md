---
# === CORE IDENTIFICATION ===
concept: The inet Module
slug: inet-module

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
section: "The Hybrid Approach (Partial Blocking)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - inet
  - "inet:setopts"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
extends: []
related:
  - active-and-passive-sockets
  - controlling-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I change socket options after a socket is opened?"
  - "How do I find out where a connection came from?"
  - "What does inet:setopts do?"
---

# Quick Definition

The `inet` module provides functions for inspecting and adjusting open sockets — most notably `inet:setopts/2` to change socket options at runtime and `inet:peername/1` to discover the remote address of a connection.

# Core Definition

The `inet` module is used to manipulate sockets after they have been created. `inet:setopts(Socket, Options)` changes a socket's options at runtime — for example, re-enabling reception on an `{active, once}` socket or explicitly setting `{packet, N}`, `binary`, `{nodelay, true}`, and `{active, true}` after a connection is accepted ("Notes" and "The Hybrid Approach"). `inet:peername(Socket)` returns `{ok, {IP_Address, Port}} | {error, Why}` — "the IP address and port of the other end of the connection so the server can discover who initiated the connection" (sidebar "Finding Out Where Connections Come From"). `inet:ifget/2` retrieves interface attributes such as the broadcast address.

# Prerequisites

- **gen_tcp module** — `inet` functions operate on sockets created by `gen_tcp` (and `gen_udp`).

# Key Properties

1. `inet:setopts(Socket, Opts)` changes socket options on an already-open socket.
2. Re-enabling an `{active, once}` socket requires `inet:setopts(Socket, [{active, once}])`.
3. `inet:peername(Socket)` returns the remote endpoint's IP address and port.
4. IPv4 addresses are 4-tuples of integers 0–255; IPv6 addresses are 8-tuples of integers 0–65535.
5. `inet:ifget("eth0", [broadaddr])` retrieves a network interface's broadcast address.

# Construction / Recognition

## To re-enable an active-once socket:
1. After processing a `{tcp, Socket, Data}` message, call `inet:setopts(Socket, [{active, once}])`.
2. Loop back to `receive` the next message.

## To find a connection's origin:
1. Call `inet:peername(Socket)`.
2. Match `{ok, {IP_Address, Port}}` to obtain the remote address.

# Context & Application

- **Typical contexts**: Implementing traffic shaping with `{active, once}`; explicitly configuring accepted sockets; identifying or blocking abusive clients.
- **Common applications**: The hybrid (partial-blocking) server pattern; the `broadcast` module's use of `inet:ifget` to find the broadcast address.
- **Historical/stylistic notes**: After accepting a connection, the book recommends explicitly setting required options with `inet:setopts`.

# Examples

**Example 1** ("Notes"): After `gen_tcp:accept`, the code calls `inet:setopts(Socket, [{packet,4},binary,{nodelay,true},{active, true}])`.

**Example 2** ("The Hybrid Approach"): `inet:setopts(Sock, [{active, once}])` re-arms the socket for one more message.

**Example 3** (sidebar): `inet:peername(Socket)` reveals the IP and port of a spamming client.

# Relationships

## Related
- **Active and passive sockets** — `inet:setopts` switches and re-arms the `{active, ...}` mode.
- **Controlling process** — `inet` operates on sockets owned by the controlling process.

# Common Errors

- **Error**: Forgetting to call `inet:setopts(Socket, [{active, once}])` after handling a message on an active-once socket.
  **Correction**: An `{active, once}` socket delivers exactly one message; it must be explicitly re-armed before the next message arrives.

# Common Confusions

- **Confusion**: Thinking socket options are fixed once a socket is opened.
  **Clarification**: Most options can be changed at runtime with `inet:setopts/2`.

# Source Reference

Chapter 17: "Programming with Sockets", sections "Notes", "The Hybrid Approach (Partial Blocking)", and the sidebar "Finding Out Where Connections Come From".

# Verification Notes

- Definition source: Synthesized from multiple chapter sections that use `inet`.
- Confidence rationale: HIGH — `inet:setopts` and `inet:peername` are explicitly used and described.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
