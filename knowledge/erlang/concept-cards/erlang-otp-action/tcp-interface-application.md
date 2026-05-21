---
# === CORE IDENTIFICATION ===
concept: tcp_interface Application
slug: tcp-interface-application

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: networking
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.1.2. Sketching the tcp_interface application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - tcp_interface
  - ti_server

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tcp-server-pattern
  - otp-application
extends:
  - tcp-server-pattern
related:
  - simple-text-protocol
  - active-passive-sockets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the tcp_interface application?"
  - "What modules make up the tcp_interface application?"
  - "How is a TCP interface added to the cache as a separate application?"
---

# Quick Definition

`tcp_interface` is the OTP application built in this chapter that gives the Simple Cache a concurrent text-over-TCP interface, structured as three modules following the efficient TCP server pattern.

# Core Definition

`tcp_interface` is a separate OTP application that provides a text-over-TCP interface to the Simple Cache, implemented so that additional external interfaces can be added later without disturbing existing code. Like every application it has a `.app` file, an application behaviour module `ti_app`, and a top-level supervisor `ti_sup`; it also has `ti_server` for the `gen_server`-based connection-handler processes. It is a concrete realization of the efficient concurrent TCP server pattern ("Erlang and OTP in Action," Ch. 11, Section 11.1.2).

# Prerequisites

- **Concurrent TCP server pattern** — `tcp_interface` is an implementation of that pattern.
- **OTP application** — `tcp_interface` is a standard OTP application.

# Key Properties

1. Implemented as its own OTP application so interfaces are pluggable into a release.
2. `ti_app` — the application behaviour module; opens the listening socket and spawns the first handler.
3. `ti_sup` — a simple-one-for-one supervisor acting as a factory for `ti_server` handlers.
4. `ti_server` — the `gen_server` connection handler; one is spawned per connection.
5. The listening socket is opened in active mode (`{active, true}`); the dedicated socket inherits this.
6. `ti_app:start/2` reads the listen port from configuration, defaulting to 1155.

# Construction / Recognition

## To Construct/Create:
1. Create a `tcp_interface` directory with `ebin/tcp_interface.app` and `src/{ti_app,ti_sup,ti_server}.erl`.
2. In `ti_app:start/2`, read the port from config (default 1155), open the listening socket, start `ti_sup` with the socket, then call `ti_sup:start_child()`.
3. Make `ti_sup` a simple-one-for-one supervisor whose child spec carries the listening socket.
4. In `ti_server`, return timeout 0 from `init/1`, block on `accept` in `handle_info(timeout, ...)`, spawn the next handler, then service the connection.

## To Identify/Recognize:
1. An application with `ti_app`, `ti_sup`, and `ti_server` modules following the TCP server pattern.

# Context & Application

- **Typical contexts**: A pluggable external interface for an Erlang service.
- **Common applications**: Letting non-Erlang clients use the Simple Cache over TCP via telnet.
- **Historical/stylistic notes**: The book keeps the supervision deliberately oversimplified (a single simple-one-for-one supervisor); a realistic app would add another supervision level.

# Examples

**Example 1** (Section 11.1.2): The directory layout is `tcp_interface/ebin/tcp_interface.app` and `tcp_interface/src/{ti_app,ti_sup,ti_server}.erl`.

**Example 2** (Section 11.1.5): After starting the cache and `tcp_interface`, multiple telnet sessions can connect simultaneously and exchange protocol commands — something the single-connection RPC server of Chapter 3 could not do.

# Relationships

## Builds Upon
- **Concurrent TCP server pattern** — `tcp_interface` is a direct application of that pattern.

## Enables
- **Simple text-based protocol** — The protocol is implemented in `ti_server`'s `handle_data/3`.

## Related
- **Active vs. passive sockets** — `tcp_interface` uses active-mode sockets.

# Common Errors

- **Error**: Putting socket-opening code in the `ti_sup` supervisor.
  **Correction**: Open the listening socket in `ti_app`, then hand it to the supervisor — keep code out of supervisors.

# Common Confusions

- **Confusion**: Thinking `tcp_interface` must be part of every release of the cache.
  **Clarification**: It is a separate application; a release may include it, another interface, or none.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.1.2 "Sketching the tcp_interface application" and 11.1.3 "Fleshing out the TCP server." See Listings 11.1–11.3.

# Verification Notes

- Definition source: Direct adaptation of Sections 11.1.2 and 11.1.3.
- Confidence rationale: HIGH — the book explicitly describes the application's purpose and module structure.
- Uncertainties: Listings 11.1–11.3 appear as images; module behavior described from surrounding prose.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
