---
# === CORE IDENTIFICATION ===
concept: Client-Server Process
slug: client-server-process

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: design-patterns
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "Introducing Client-Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "client-server"
  - "client/server pattern"
  - "rpc pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn
  - message-passing
  - receive
extends: []
related:
  - selective-receive
  - process-identifier
  - registered-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the client-server pattern in Erlang?"
  - "How do I build a request/response server from processes?"
  - "How does gen_server relate to the client/server pattern?"
---

# Quick Definition

A client-server process pair is two processes — a client that sends a request and a server that computes a reply and responds. It is built from just `spawn`, `send`, and `receive`, and is the foundation of OTP's `gen_server`.

# Core Definition

"Client-server architectures are central to Erlang" (Armstrong, "Concurrent Programming," "Introducing Client-Server"). The client and server "are separate processes, and normal Erlang message passing is used for communication." The words client and server "refer to the roles": "the client always initiates a computation by sending a request to the server. The server computes a reply and sends a response to the client." Because the server does not know who to reply to, the client must include a reply address — `Pid ! {self(), Request}`. A utility `rpc(Pid, Request)` encapsulates "sending a request to a server and waiting for a response." The server is a tail-recursive `loop/0` with a `receive` per request shape; `spawn` and `rpc` can be hidden behind named API functions (`start/0`, `area/2`). "All we needed were the three primitives, `spawn`, `send`, and `receive`."

# Prerequisites

- **Spawn** — The server process is created with `spawn`.
- **Message passing** — Requests and responses travel as messages.
- **receive** — The server's loop dispatches on incoming requests via `receive`.

# Key Properties

1. Client and server are separate processes; client and server are *roles*, not heavyweight machines.
2. The client initiates by sending a request; the server computes and sends a response.
3. The client includes its own Pid (`self()`) in the request so the server can reply.
4. The server is a tail-recursive `loop/0` whose `receive` clauses handle each request shape.
5. An `rpc/2` helper encapsulates send-request-then-await-response.
6. The reply pattern `{Pid, Response}` (selective receive) ensures the client matches only its server's reply.
7. `spawn` and `rpc` can be hidden behind named API functions for a clean interface.

# Construction / Recognition

## To Construct/Create:
1. Write a server `loop/0` with a `receive` clause per request shape; reply with `From ! {self(), Result}` and tail-call `loop()`.
2. Add a catch-all clause so every message is handled.
3. Write `rpc(Pid, Request) -> Pid ! {self(), Request}, receive {Pid, Response} -> Response end.`
4. Provide `start/0` (which spawns `loop/0`) and named request functions that call `rpc`.

## To Identify/Recognize:
1. A `loop/0` with a `receive` and tail-recursive self-calls is the server.
2. An `rpc`-style function pairing a send with a matching receive marks the client side.

# Context & Application

- **Typical contexts**: Any service that answers requests; the conceptual basis for OTP's `gen_server`.
- **Common applications**: Computation servers, registries, state holders accessed by many clients.
- **Historical/stylistic notes**: Armstrong notes "this pattern will repeat over and over again in major and minor variations, but the underlying ideas are always the same."

# Examples

**Example 1** ("Introducing Client-Server"): `area_server1` — server `loop/0` matches `{From, {rectangle, Width, Ht}} -> From ! Width * Ht, loop()` and a catch-all `{From, Other} -> From ! {error,Other}`.

**Example 2** ("Introducing Client-Server"): `rpc(Pid, Request) -> Pid ! {self(), Request}, receive {Pid, Response} -> Response end.` — the `{Pid, Response}` pattern fixes the bug of accepting any message.

**Example 3** ("Introducing Client-Server"): `area_server_final` hides `spawn`/`rpc` behind `start/0` and `area/2`, so `Pid = area_server_final:start()` then `area_server_final:area(Pid, {rectangle, 10, 8})` returns `80`.

# Relationships

## Builds Upon
- **Spawn**, **Message passing**, **receive** — the three primitives the pattern is built from.

## Enables
- (The OTP `gen_server` behaviour generalizes this pattern — covered in a later chapter.)

## Related
- **Selective receive** — The `{Pid, Response}` reply pattern relies on it.
- **Process identifier** — `self()` provides the client's reply address.
- **Registered process** — A server is often registered under a name.

## Contrasts With
- None.

# Common Errors

- **Error**: Writing `rpc` to receive any message, so an unrelated message is misread as the server's reply.
  **Correction**: Match `{Pid, Response}` with the server's `Pid` bound, so only its reply matches.

- **Error**: Sending a request without `self()`, leaving the server with nowhere to reply.
  **Correction**: Always send `{self(), Request}` so the server has a `From` address.

# Common Confusions

- **Confusion**: Thinking a "server" must be heavyweight software on a dedicated machine.
  **Clarification**: In Erlang client and server are just process *roles*; both can run on the same machine.

- **Confusion**: Believing client-server requires a network.
  **Clarification**: It uses ordinary message passing; the processes may be local or on different machines.

# Source Reference

Chapter 12: "Concurrent Programming," section "Introducing Client-Server." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the client-server discussion and the `area_server1`/`area_server_final` examples.
- Confidence rationale: HIGH — the pattern is built up step by step in the source.
- Uncertainties: None.
- Cross-reference status: Cross-refs verified against KB slugs.
- Re-extraction notes: Fresh extraction; new card (no prior file).
