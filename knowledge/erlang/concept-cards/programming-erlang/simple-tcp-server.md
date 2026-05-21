---
# === CORE IDENTIFICATION ===
concept: A Simple TCP Server
slug: simple-tcp-server

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
section: "A Simple TCP Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "nano server"
  - "single-shot TCP server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - packet-option
  - marshaling-with-term-to-binary
extends: []
related:
  - controlling-process
contrasts_with:
  - sequential-server
  - parallel-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a TCP server in Erlang?"
  - "How do I listen for and accept a TCP connection?"
  - "What is the simplest TCP server structure?"
---

# Quick Definition

A simple TCP server opens a listening port, accepts a single connection, serves one request, sends a reply, and terminates. It is the minimal server that demonstrates how to package and encode application data.

# Core Definition

The simple TCP server "opens port 2345 and then waits for a single message. This message is a binary that contains an Erlang term ... The server evaluates the expression and sends the result to the client by writing the result to the socket" ("A Simple TCP Server"). It is built from three `gen_tcp` calls: `gen_tcp:listen(Port, Options)` creates a listening socket; `gen_tcp:accept(Listen)` blocks until a client connects and returns a connection socket; `gen_tcp:close(Listen)` then closes the listening socket so no new connections are accepted. The pattern match `{ok, Listen} = gen_tcp:listen(...)` deliberately raises an exception if listen fails. "This program accepts only a single request; once the program has run to completion, then no more connections will be accepted."

# Prerequisites

- **gen_tcp module** — The server is built entirely from `gen_tcp` listen/accept/send/close.
- **packet option** — `{packet, 4}` frames each application message.
- **marshaling with term_to_binary** — The server decodes requests with `binary_to_term` and encodes replies with `term_to_binary`.

# Key Properties

1. `gen_tcp:listen/2` returns a listening socket; `gen_tcp:accept/1` returns a connection socket.
2. A listening socket can only be used as an argument to `gen_tcp:accept`.
3. After `accept` returns, the simple server closes the listening socket so no new connections come in.
4. It accepts exactly one connection, serves it, and terminates.
5. Uses `binary_to_term` to unmarshal the request and `term_to_binary` to marshal the reply.
6. Matching `{ok, Listen}` causes a pattern-match exception if `listen` returns `{error, Why}`.

# Construction / Recognition

## To construct a simple TCP server:
1. Call `gen_tcp:listen(2345, [binary, {packet, 4}, {reuseaddr, true}, {active, true}])`.
2. Match `{ok, Listen}` to bind the listening socket.
3. Call `gen_tcp:accept(Listen)` and match `{ok, Socket}`.
4. Call `gen_tcp:close(Listen)` to stop accepting new connections.
5. Enter `loop(Socket)` to receive `{tcp, Socket, Bin}`, decode, compute, and reply.

# Context & Application

- **Typical contexts**: A teaching example showing the minimal server skeleton and data packaging.
- **Common applications**: The basis for the sequential and parallel server variants.
- **Historical/stylistic notes**: Called the "nano server"; it "accepts a request, computes a reply, sends the reply, and terminates."

# Examples

**Example 1** ("A Simple TCP Server"): `start_nano_server/0` listens, accepts, closes the listening socket, and enters `loop(Socket)`.

## Worked Example

```erlang
start_nano_server() ->
    {ok, Listen} = gen_tcp:listen(2345, [binary, {packet, 4},
                                         {reuseaddr, true},
                                         {active, true}]),
    {ok, Socket} = gen_tcp:accept(Listen),
    gen_tcp:close(Listen),
    loop(Socket).

loop(Socket) ->
    receive
        {tcp, Socket, Bin} ->
            Str = binary_to_term(Bin),
            Reply = lib_misc:string2value(Str),
            gen_tcp:send(Socket, term_to_binary(Reply)),
            loop(Socket);
        {tcp_closed, Socket} ->
            io:format("Server socket closed~n")
    end.
```

# Relationships

## Related
- **Controlling process** — The process that calls `accept` becomes the controlling process for the socket.

## Contrasts With
- **Sequential server** — Reuses the listening socket to serve many connections one at a time.
- **Parallel server** — Spawns a process per connection to serve clients concurrently.

# Common Errors

- **Error**: Forgetting that the simple server terminates after one connection.
  **Correction**: To serve more than one client, use the sequential or parallel server variant.

- **Error**: Closing the connection socket instead of the listening socket after `accept`.
  **Correction**: Close the *listening* socket (`Listen`) to stop new connections; keep the connection socket open to serve the client.

# Common Confusions

- **Confusion**: Thinking closing the listening socket drops the active connection.
  **Clarification**: Closing the listening socket only prevents new connections; it does not affect the existing connection.

# Source Reference

Chapter 17: "Programming with Sockets", section "A Simple TCP Server". Code from `socket_examples.erl`.

# Verification Notes

- Definition source: Direct quotes from "A Simple TCP Server".
- Confidence rationale: HIGH — explicitly defined and fully coded.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
