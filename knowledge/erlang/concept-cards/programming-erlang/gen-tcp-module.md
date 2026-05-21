---
# === CORE IDENTIFICATION ===
concept: The gen_tcp Module
slug: gen-tcp-module

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
section: "Using TCP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_tcp
  - "TCP socket library"

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
  - inet-module
contrasts_with:
  - gen-udp-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I program with TCP/UDP sockets?"
  - "What library does Erlang use for TCP programming?"
  - "How do I open a TCP connection in Erlang?"
---

# Quick Definition

`gen_tcp` is the standard Erlang library module for programming TCP applications. It provides functions to connect to servers, listen for connections, accept connections, send data, and receive data over reliable TCP byte streams.

# Core Definition

`gen_tcp` is one of the two main libraries for programming with sockets — it handles the Transmission Control Protocol (TCP), which "provides a reliable stream of bytes that are delivered in order as long as the connection is established" ("Programming with Sockets", chapter intro). The core `gen_tcp` functions used in the chapter are: `gen_tcp:connect(Host, Port, Options)` to open a client connection, `gen_tcp:listen(Port, Options)` to create a listening socket, `gen_tcp:accept(Listen)` to accept an incoming connection, `gen_tcp:send(Socket, Data)` to send data, `gen_tcp:recv(Socket, N)` to receive data from a passive socket, and `gen_tcp:close(Socket)` to close a socket (chapter "Using TCP" and following sections).

# Prerequisites

- **Process** — Socket messages are delivered to the controlling process; understanding processes is required.
- **Message passing** — Data arriving on an active socket appears as `{tcp, Socket, Data}` messages in the process mailbox.
- **Binary** — Sockets are usually opened in `binary` mode, so received data arrives as binaries.

# Key Properties

1. Handles TCP — a reliable, ordered, connection-oriented byte stream.
2. `gen_tcp:connect/3` is used by clients; `gen_tcp:listen/2` plus `gen_tcp:accept/1` are used by servers.
3. Data received on an active socket is delivered as `{tcp, Socket, Bin}` messages; socket closure is signaled by `{tcp_closed, Socket}`.
4. Socket options (`binary`, `{packet, N}`, `{active, ...}`, `{reuseaddr, true}`, `{nodelay, true}`) are passed at connect/listen time.
5. `gen_tcp` links itself to the controlling process — if that process dies, the socket is automatically closed.

# Construction / Recognition

## To open a client connection:
1. Call `gen_tcp:connect(Host, Port, Options)` with options such as `[binary, {packet, 0}]`.
2. Match `{ok, Socket}` to bind the connected socket.
3. Use `gen_tcp:send/2` to send and `receive` to collect `{tcp, Socket, Bin}` messages.
4. Call `gen_tcp:close(Socket)` when finished.

## To open a server:
1. Call `gen_tcp:listen(Port, Options)` to obtain a listening socket.
2. Call `gen_tcp:accept(Listen)` — this blocks until a client connects.
3. Communicate over the returned `Socket`.

# Context & Application

- **Typical contexts**: Writing TCP clients (web clients, RPC clients) and servers in Erlang.
- **Common applications**: HTTP-style clients, term-evaluation servers, the SHOUTcast audio server, any program that interacts with other machines on the Internet.
- **Historical/stylistic notes**: Armstrong notes that most of the more interesting programs he writes involve sockets, because they let applications interact with other machines on the Internet.

# Examples

**Example 1** ("Fetching Data from a Server"): `nano_get_url/1` opens a socket with `gen_tcp:connect(Host, 80, [binary, {packet, 0}])`, sends `"GET / HTTP/1.0\r\n\r\n"` with `gen_tcp:send`, and collects reply fragments as `{tcp,Socket,Bin}` messages.

**Example 2** ("A Simple TCP Server"): `start_nano_server/0` calls `gen_tcp:listen(2345, [binary, {packet, 4}, {reuseaddr, true}, {active, true}])` then `gen_tcp:accept(Listen)`.

## Worked Example

The client `nano_client_eval/1` connects, encodes a term and sends it:

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
- **Message passing** — Active sockets deliver data via the process mailbox.

## Enables
- **Simple TCP server** — Built directly from `gen_tcp:listen/accept`.
- **Active and passive sockets** — Configured via `gen_tcp` socket options.

## Related
- **TCP socket** — The communication channel `gen_tcp` manages.
- **inet module** — Used to set socket options after a socket is open.
- **Controlling process** — The process that owns a `gen_tcp` socket.

## Contrasts With
- **gen_udp module** — Handles unreliable, connectionless UDP datagrams instead of reliable TCP streams.

# Common Errors

- **Error**: Using mismatched `{packet, N}` values on client and server.
  **Correction**: The `packet` argument used by client and server must agree; if the server opens with `{packet,2}` and the client with `{packet,4}`, nothing works.

- **Error**: Forgetting to handle `{tcp_closed, Socket}`.
  **Correction**: Always include a `{tcp_closed, Socket}` clause in the receive loop so the program can detect the end of data.

# Common Confusions

- **Confusion**: Thinking each TCP `send` produces exactly one `{tcp, Socket, Bin}` message on the other side.
  **Clarification**: TCP is a byte stream; replies arrive fragmented as a sequence of messages unless `{packet, N}` framing is used.

- **Confusion**: Believing `gen_tcp` requires manual cleanup if a process crashes.
  **Clarification**: `gen_tcp` links itself to the controlling process; if that process dies, the socket is closed automatically.

# Source Reference

Chapter 17: "Programming with Sockets", sections "Using TCP", "Fetching Data from a Server", and "A Simple TCP Server". Code examples from `socket_examples.erl`.

# Verification Notes

- Definition source: Direct synthesis from chapter intro and "Using TCP" section.
- Confidence rationale: HIGH — the module and its core functions are explicitly named and demonstrated throughout the chapter.
- Uncertainties: None.
- Cross-reference status: Verified concept names; canonical slugs used.
- Re-extraction notes: Fresh extraction.
