---
# === CORE IDENTIFICATION ===
concept: The gen_tcp Module
slug: gen-tcp

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
section: "Using TCP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_tcp
  - "gen_tcp module"
  - TCP library

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - binary
extends: []
related:
  - tcp-socket
  - simple-tcp-server
  - active-and-passive-sockets
  - controlling-process
contrasts_with:
  - udp-socket

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I program with TCP/UDP sockets?"
  - "What library does Erlang use for TCP programming?"
---

# Quick Definition

`gen_tcp` is the standard Erlang library module for programming TCP applications — opening connections, listening for connections, sending data, and closing sockets.

# Core Definition

`gen_tcp` is one of the two main libraries for programming with sockets, the other being `gen_udp` for UDP applications ("Programming with Sockets," chapter introduction). It provides the operations needed to write both TCP clients and TCP servers. A client opens a connection with `gen_tcp:connect(Host, Port, Options)`; a server listens for connections with `gen_tcp:listen(Port, Options)` and accepts them with `gen_tcp:accept(ListenSocket)`. Data is sent with `gen_tcp:send/2` and sockets are closed with `gen_tcp:close/1`. The book uses `gen_tcp` to build clients, servers, and the parallel/sequential server variants throughout the chapter ("Using TCP").

# Prerequisites

- **Process** — Each socket has a controlling process; socket messages are delivered to that process's mailbox.
- **Message passing** — In active mode, incoming TCP data arrives as `{tcp, Socket, Data}` messages, just like ordinary inter-process messages.
- **Binary** — Sockets are typically opened with the `binary` option so data arrives as binaries; the book uses `term_to_binary`/`binary_to_term` to encode terms over the wire.

# Key Properties

1. Provides `connect/3`, `listen/2`, `accept/1`, `send/2`, `recv/2`, `close/1`, and `controlling_process/2`.
2. `gen_tcp:connect` and `gen_tcp:listen` take an options list controlling socket behaviour (`binary`, `{packet, N}`, `{active, ...}`, `{reuseaddr, true}`, etc.).
3. The arguments to `{packet, N}` used by client and server must agree, or communication fails.
4. `gen_tcp` links itself to the controlling process; if that process dies, the socket is automatically closed.
5. A listening socket can only be passed to `gen_tcp:accept`; it does not itself carry data.
6. As of R11B-3, several processes may call `gen_tcp:accept/1` on the same listen socket, enabling a pool of pre-spawned acceptors.

# Construction / Recognition

## To use gen_tcp as a client:

1. Call `gen_tcp:connect(Host, Port, Options)` to open a socket.
2. Call `gen_tcp:send(Socket, Data)` to send a request.
3. Receive `{tcp, Socket, Bin}` messages (active mode) or call `gen_tcp:recv` (passive mode).
4. Handle `{tcp_closed, Socket}` when the peer closes the connection.

## To use gen_tcp as a server:

1. Call `gen_tcp:listen(Port, Options)` to obtain a listening socket.
2. Call `gen_tcp:accept(Listen)` to wait for and accept a connection.
3. Process data on the returned connection socket.
4. Decide whether to loop (sequential server) or `spawn` an acceptor (parallel server).

# Context & Application

`gen_tcp` underpins virtually all networked Erlang programs — web clients, web servers, RPC over TCP, and streaming servers like the chapter's SHOUTcast example.

- **Typical contexts**: Reliable, ordered, stream-based communication over the Internet.
- **Common applications**: HTTP clients/servers, term-passing servers, parallel connection handlers.
- **Historical/stylistic notes**: The book recommends `term_to_binary`/`binary_to_term` with `{packet,4}` framing as a fast alternative to text protocols like XML.

# Examples

**Example 1** ("Fetching Data from a Server"): `nano_get_url/1` opens a socket to port 80 with `gen_tcp:connect(Host, 80, [binary, {packet, 0}])`, sends an HTTP GET, and accumulates `{tcp,Socket,Bin}` fragments.

**Example 2** ("A Simple TCP Server"): `start_nano_server/0` calls `gen_tcp:listen(2345, [binary, {packet, 4}, {reuseaddr, true}, {active, true}])` then `gen_tcp:accept(Listen)`.

## Worked Example

The `nano_client_eval` client (from "A Simple TCP Server"):

```erlang
nano_client_eval(Str) ->
    {ok, Socket} =
        gen_tcp:connect("localhost", 2345,
                        [binary, {packet, 4}]),
    ok = gen_tcp:send(Socket, term_to_binary(Str)),
    receive
        {tcp,Socket,Bin} ->
            io:format("Client received binary = ~p~n",[Bin]),
            Val = binary_to_term(Bin),
            io:format("Client result = ~p~n",[Val]),
            gen_tcp:close(Socket)
    end.
```

# Relationships

## Builds Upon

- **Process** — `gen_tcp` delivers socket events as messages to a controlling process.

## Enables

- **Simple TCP server** — Built directly from `gen_tcp:listen`/`accept`/`send`.
- **Sequential and parallel servers** — Variations on how `gen_tcp:accept` results are handled.
- **Controlling process** — A `gen_tcp` concept governing socket ownership.

## Related

- **TCP socket** — The communication endpoint `gen_tcp` operates on.
- **Active and passive sockets** — Reception modes set via `gen_tcp` options.

## Contrasts With

- **UDP socket** — `gen_udp` provides the connectionless, unreliable counterpart.

# Common Errors

- **Error**: Using mismatched `{packet, N}` values between client and server.
  **Correction**: Both ends must use the same packet length-header size, or nothing works.

- **Error**: Forgetting to handle `{tcp_closed, Socket}`, leaving a loop waiting forever.
  **Correction**: Always match on `{tcp_closed, Socket}` in the receive loop.

# Common Confusions

- **Confusion**: Believing the listening socket and the connection socket are interchangeable.
  **Clarification**: The listening socket can only be passed to `gen_tcp:accept`; the socket returned by `accept` is the one used to talk to the client.

- **Confusion**: Thinking `{packet, N}` refers to physical network packets.
  **Clarification**: It refers to the length of an application-level request/response message, not the packet seen on the wire.

# Source Reference

Chapter 17: "Programming with Sockets," sections "Using TCP," "Fetching Data from a Server," "A Simple TCP Server." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Synthesized from the chapter introduction and "Using TCP."
- Confidence rationale: HIGH — the module and its core functions are explicitly named and demonstrated with multiple code examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards for this chapter.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source/concept.
