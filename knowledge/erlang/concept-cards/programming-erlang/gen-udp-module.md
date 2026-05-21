---
# === CORE IDENTIFICATION ===
concept: The gen_udp Module
slug: gen-udp-module

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
section: "UDP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_udp
  - "UDP socket library"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - udp-datagram
extends: []
related:
  - udp-broadcasting
  - marshaling-with-term-to-binary
contrasts_with:
  - gen-tcp-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I program with TCP/UDP sockets?"
  - "What library does Erlang use for UDP programming?"
  - "How do I write a UDP server in Erlang?"
---

# Quick Definition

`gen_udp` is the standard Erlang library module for programming UDP applications. It opens UDP sockets, sends datagrams, and delivers received datagrams as messages to the controlling process.

# Core Definition

`gen_udp` is one of the two main socket libraries — "`gen_tcp` for programming TCP applications and `gen_udp` for programming UDP applications" ("Programming with Sockets", chapter intro). The core functions are `gen_udp:open(Port, Options)` to open a UDP socket, `gen_udp:send(Socket, Host, Port, Data)` to send a datagram, and `gen_udp:close(Socket)` to close the socket. Received datagrams are delivered to the controlling process as `{udp, Socket, Host, Port, Bin}` messages. Writing a UDP client and server "is much easier than writing in the TCP case since we don't have to worry about maintaining connections" ("UDP" section).

# Prerequisites

- **Process** — Datagrams are delivered as messages to the socket's controlling process.
- **Message passing** — Received datagrams appear in the process mailbox.
- **UDP datagram** — Understanding UDP's unreliable, connectionless nature is required to use `gen_udp` correctly.

# Key Properties

1. Handles UDP — connectionless, unreliable datagram transport.
2. `gen_udp:open(Port, [binary])` opens a socket; `Port` 0 lets the system choose a free port (used by clients).
3. `gen_udp:send/4` requires the destination `Host` and `Port` on every send (no connection).
4. Received datagrams are `{udp, Socket, Host, Port, Bin}` messages, carrying the sender's address.
5. There are no "socket closed" messages to handle, unlike `gen_tcp`.
6. With the `{broadcast, true}` option, datagrams can be sent to a broadcast address.

# Construction / Recognition

## To write a UDP server:
1. Call `gen_udp:open(Port, [binary])` to open the socket.
2. Loop receiving `{udp, Socket, Host, Port, Bin}` messages.
3. Compute a reply and call `gen_udp:send(Socket, Host, Port, BinReply)`.

## To write a UDP client:
1. Call `gen_udp:open(0, [binary])` to open a socket on an arbitrary port.
2. Call `gen_udp:send(Socket, Host, Port, Request)`.
3. Wait for a `{udp, ...}` reply with a timeout, then `gen_udp:close(Socket)`.

# Context & Application

- **Typical contexts**: Lightweight request/response services and LAN broadcast.
- **Common applications**: The chapter's UDP factorial server and `broadcast` module both use `gen_udp`.
- **Historical/stylistic notes**: Armstrong emphasizes that UDP code is simpler than TCP code because there are no connections to manage.

# Examples

**Example 1** ("A UDP Factorial Server", `udp_test.erl`): `server(Port)` calls `gen_udp:open(Port, [binary])`, then loops receiving `{udp, Socket, Host, Port, Bin}`, computing `fac(binary_to_term(Bin))`, and replying with `gen_udp:send`.

**Example 2** ("The Simplest UDP Server and Client"): the client opens with `gen_udp:open(0, [binary])` and sends with `gen_udp:send(Socket, "localhost", 4000, Request)`.

## Worked Example

```erlang
%% The server
server(Port) ->
    {ok, Socket} = gen_udp:open(Port, [binary]),
    io:format("server opened socket:~p~n",[Socket]),
    loop(Socket).

loop(Socket) ->
    receive
        {udp, Socket, Host, Port, Bin} = Msg ->
            io:format("server received:~p~n",[Msg]),
            N = binary_to_term(Bin),
            Fac = fac(N),
            gen_udp:send(Socket, Host, Port, term_to_binary(Fac)),
            loop(Socket)
    end.
```

# Relationships

## Builds Upon
- **Message passing** — Received datagrams arrive as mailbox messages.

## Enables
- **UDP broadcasting** — Built with `gen_udp:open` plus the `{broadcast, true}` option.

## Related
- **marshaling with term_to_binary** — Used to encode/decode Erlang terms carried in datagrams.

## Contrasts With
- **gen_tcp module** — `gen_tcp` manages reliable connection-oriented streams; `gen_udp` manages connectionless datagrams.

# Common Errors

- **Error**: Forgetting that `gen_udp:send/4` needs the destination host and port every time.
  **Correction**: There is no connection — supply `Host` and `Port` on each send.

- **Error**: Blocking forever in a client `receive` for a UDP reply.
  **Correction**: Use an `after` timeout, since the reply may be lost.

# Common Confusions

- **Confusion**: Expecting `{udp_closed, Socket}` messages like TCP.
  **Clarification**: UDP is connectionless; there are no close messages to handle.

- **Confusion**: Thinking opening with port 0 fails.
  **Clarification**: Port 0 tells the system to assign an arbitrary free port — the normal idiom for clients.

# Source Reference

Chapter 17: "Programming with Sockets", section "UDP", subsections "The Simplest UDP Server and Client" and "A UDP Factorial Server". Code from `udp_test.erl`.

# Verification Notes

- Definition source: Direct synthesis from chapter intro and "UDP" section.
- Confidence rationale: HIGH — `gen_udp` and its functions are explicitly named and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
