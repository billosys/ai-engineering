---
# === CORE IDENTIFICATION ===
concept: RESTful Cache Interface (http_interface)
slug: restful-cache-interface

# === CLASSIFICATION ===
category: api-design
subcategory: web-interfaces
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.2.4. Implementing the RESTful protocol with gen_web_server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - http_interface application
  - hi_server

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rest
  - gen-web-server
  - otp-application
extends:
  - gen-web-server
related:
  - http-protocol
contrasts_with:
  - simple-text-protocol

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a RESTful interface to the cache implemented with gen_web_server?"
  - "What do GET, PUT, and DELETE map to in the cache interface?"
  - "What HTTP replies does the RESTful cache interface produce?"
---

# Quick Definition

`http_interface` is the OTP application that exposes the Simple Cache over HTTP, implemented as a thin `gen_web_server` callback module (`hi_server`) mapping `GET`/`PUT`/`DELETE` onto cache operations.

# Core Definition

The RESTful HTTP interface to the cache is a separate active application, `http_interface`, with an application behaviour module (`hi_app`), a top-level supervisor (`hi_sup`), and the `hi_server` module that implements the interface as a `gen_web_server` callback module. The supervisor uses ordinary one-for-one supervision and starts a single permanent child — one `gen_web_server` instance — via `hi_server:start_link/1`. Only `hi_server` knows the implementation rests on `gen_web_server`. The protocol maps `GET /key` to `simple_cache:lookup(Key)`, `PUT /key` to `simple_cache:insert(Key, Body)`, and `DELETE /key` to `simple_cache:delete(Key)` ("Erlang and OTP in Action," Ch. 11, Section 11.2.4).

# Prerequisites

- **REST** — The interface follows REST principles.
- **gen_web_server** — `hi_server` is a callback module of the `gen_web_server` behaviour.
- **OTP application** — `http_interface` is a standard OTP application.

# Key Properties

1. `http_interface` is a separate active application with `hi_app`, `hi_sup`, and `hi_server` modules.
2. `hi_sup` uses ordinary one-for-one supervision and starts a single permanent `gen_web_server` instance.
3. The port is read with `application:get_env/2` in `hi_app:start/2`, defaulting to 1156 (separate from `tcp_interface`'s 1155).
4. `GET /key` → `simple_cache:lookup(Key)`: `200 OK` with the value as body, or `404 Not Found` with an empty body.
5. `PUT /key` → `simple_cache:insert(Key, Body)`: always `200 OK` with an empty body.
6. `DELETE /key` → `simple_cache:delete(Key)`: always `200 OK` with an empty body.
7. Unimplemented HTTP methods return `501 Not Implemented`.
8. Keys and stored data are treated as binaries; the leading slash is stripped via binary pattern matching.

# Construction / Recognition

## To Construct/Create:
1. Create the `http_interface` application: `.app` file plus `hi_app`, `hi_sup`, `hi_server`.
2. In `hi_app:start/2`, read the port (default 1156) and pass it to `hi_sup:start_link/1`.
3. In `hi_sup`, use one-for-one supervision; start one permanent `hi_server` child.
4. In `hi_server`, declare `-behaviour(gen_web_server)`, export the callbacks, and implement `get/3`, `put/4`, `delete/3`, leaving other methods to return `501`.
5. Compile with `-pa ./gen_web_server/ebin` so the compiler can check the behaviour interface.

## To Identify/Recognize:
1. An application whose `hi_server` declares `-behaviour(gen_web_server)` and maps HTTP verbs to `simple_cache` calls.

# Context & Application

- **Typical contexts**: Exposing an Erlang service to non-Erlang, RESTful clients.
- **Common applications**: `curl -T put.txt http://localhost:1156/xyzzy` then `curl http://localhost:1156/xyzzy` stores and retrieves a value.
- **Historical/stylistic notes**: The same value can be looked up via the TCP interface — but as a binary, since the HTTP interface stores everything as binaries.

# Examples

**Example 1** (Section 11.2.4): `curl -T put.txt http://localhost:1156/xyzzy` stores `Erlang` under key `xyzzy`; `curl http://localhost:1156/xyzzy` returns `Erlang`.

**Example 2** (Section 11.2.4): Looking up the same key over the TCP interface gives `OK:{ok,<<"Erlang\n">>}.` because the HTTP interface treats keys and data as binaries.

# Relationships

## Builds Upon
- **gen_web_server** — `hi_server` is a callback module of that behaviour.
- **REST** — The interface implements REST principles.

## Related
- **HTTP protocol basics** — The interface speaks HTTP.

## Contrasts With
- **Simple text-based protocol** — A bespoke text protocol over raw TCP; this is a structured RESTful interface over standard HTTP.

# Common Errors

- **Error**: Reusing `tcp_interface`'s port 1155 for the HTTP interface.
  **Correction**: Default the HTTP interface to a separate port (1156) so both interfaces can run together.

- **Error**: Storing non-binary Erlang terms and expecting `GET` to return them.
  **Correction**: The found value must be a binary, string, or IO-list to be sent on the socket.

# Common Confusions

- **Confusion**: Thinking every module of `http_interface` depends on `gen_web_server`.
  **Clarification**: Only `hi_server` knows the implementation uses `gen_web_server`.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.4 "Implementing the RESTful protocol with gen_web_server." See Figure 11.4 and Listing 11.8.

# Verification Notes

- Definition source: Direct adaptation of Section 11.2.4.
- Confidence rationale: HIGH — the book describes the application structure and protocol mapping explicitly.
- Uncertainties: Listing 11.8 appears as an image; callback behavior described from surrounding prose.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
