---
# === CORE IDENTIFICATION ===
concept: gen_web_server Custom Behaviour
slug: gen-web-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: custom-behaviours
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.2.2. Implementing a generic web server behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_web_server
  - generic web server behaviour

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - tcp-server-pattern
  - custom-behaviour
extends:
  - tcp-server-pattern
related:
  - http-packet-parsing
  - active-passive-sockets
  - restful-cache-interface
  - http-protocol
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the gen_web_server behaviour?"
  - "How does a custom behaviour with many implementations work?"
  - "How does gen_web_server differ from gen_server in process structure?"
---

# Quick Definition

`gen_web_server` is a custom OTP behaviour built in this chapter — a reusable, scaled-down web server container whose callback module supplies one function per HTTP method.

# Core Definition

`gen_web_server` is a custom OTP behaviour: a generic web server provided as a separate, reusable library application. A behaviour has three parts — container, interface, and implementation; with `gen_web_server` the author provides the container and interface, leaving the implementation to callback modules. The `gen_web_server.erl` front-end module provides the API and defines the behaviour interface (a `behaviour_info/1` function returning nine callbacks, all but `init/1` corresponding to HTTP methods). Each instance of the behaviour consists of a single supervisor managing a varying, unbounded number of dynamically created connection-handler processes — unlike a `gen_server` instance, which is a single process. Each instance manages one IP/port combination ("Erlang and OTP in Action," Ch. 11, Section 11.2.2).

# Prerequisites

- **OTP behaviour** — `gen_web_server` is itself an OTP behaviour.
- **Concurrent TCP server pattern** — Each instance uses the simple-one-for-one TCP server pattern.
- **Custom behaviour** — `gen_web_server` is defined by writing a `behaviour_info/1` function.

# Key Properties

1. A library application — no `mod` entry, no `_app` or top-level supervisor module; it need not be started.
2. Three modules: `gen_web_server` (front end / interface), `gws_connection_sup` (simple-one-for-one supervisor), `gws_server` (per-connection `gen_server` handler).
3. Defines nine callbacks: `init/1` plus one per HTTP method (`get`, `put`, `delete`, etc.) and `other_methods/4`.
4. Each request is delegated to the matching callback in the implementation module.
5. An instance is many processes (a supervisor plus unbounded handlers), not one — contrasting with `gen_server`.
6. Each instance manages a specific IP address/TCP port; one node can run many instances.
7. Provides an `http_reply` utility for building proper HTTP replies (also used internally for `100 Continue`).

# Construction / Recognition

## To Construct/Create:
1. Create a `gen_web_server` application with `gen_web_server.erl`, `gws_connection_sup.erl`, `gws_server.erl`.
2. In `gen_web_server.erl`, export `behaviour_info/1` returning the nine callbacks, plus `start_link` functions and the `http_reply` utility.
3. In `gws_connection_sup`, open the listening socket in `init/1` and start the first `gws_server` handler.
4. In `gws_server` (a `gen_server`), accept connections, dispatch parsed HTTP requests to the callback module.
5. To use it, write a callback module declaring `-behaviour(gen_web_server)` and implementing the callbacks.

## To Identify/Recognize:
1. A module declaring `-behaviour(gen_web_server)` and exporting `init/1`, `get/3`, `put/4`, `delete/3`, etc.

# Context & Application

- **Typical contexts**: Building RESTful HTTP interfaces in Erlang while learning custom behaviour design.
- **Common applications**: The `http_interface` application's `hi_server` is a `gen_web_server` callback module.
- **Historical/stylistic notes**: Explicitly "just a quick-and-dirty web server" — not for production; real servers are Yaws, MochiWeb, or `inets httpd`.

# Examples

**Example 1** (Section 11.2.2, Figure 11.2): A `gen_web_server` instance is one `gws_connection_sup` supervisor managing many `gws_server` connection processes.

**Example 2** (Listing 11.5): `gen_web_server:behaviour_info(callbacks)` returns nine callbacks; a `PUT` request is dispatched to the implementation module's `put/4` function.

# Relationships

## Builds Upon
- **Concurrent TCP server pattern** — Each instance is a simple-one-for-one TCP server.
- **OTP behaviour** — `gen_web_server` is a behaviour with container, interface, and implementation parts.

## Enables
- **RESTful cache interface** — `hi_server` is a `gen_web_server` callback module.

## Related
- **HTTP packet parsing** — `gws_server` uses `{packet, http_bin}` to parse HTTP.
- **Active vs. passive sockets** — `gws_server` uses `{active, once}`.

## Contrasts With
- **gen_server** — A `gen_server` instance is a single process; a `gen_web_server` instance is a supervisor plus an unbounded set of handlers.

# Common Errors

- **Error**: Adding a `mod` entry or top-level supervisor to the `gen_web_server` application.
  **Correction**: It is a library application — no `mod`, no `_app`, no top-level supervisor.

- **Error**: Opening the listening socket in `gen_web_server:start_link/4` or in a `gws_server`.
  **Correction**: The listening socket must be owned by the long-lived `gws_connection_sup` process; open it in that supervisor's `init/1`.

# Common Confusions

- **Confusion**: Treating `gen_web_server` as a production-grade web server.
  **Clarification**: It is a teaching example for custom behaviours; it lacks chunking, persistent connections, and more.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.2 "Implementing a generic web server behaviour." See Figure 11.2 and Listings 11.5–11.7.

# Verification Notes

- Definition source: Direct adaptation of Section 11.2.2.
- Confidence rationale: HIGH — the book builds the behaviour explicitly and describes its structure in detail.
- Uncertainties: Listings 11.5–11.7 appear as images; behavior described from surrounding prose.
- Cross-reference status: `otp-behaviour`, `gen-server` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
