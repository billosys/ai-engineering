---
# === CORE IDENTIFICATION ===
concept: HTTP Protocol Basics
slug: http-protocol

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
section: "11.2.1. A quick-and-dirty introduction to HTTP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "HTTP"
  - "Hypertext Transfer Protocol"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rest
  - gen-web-server
  - http-packet-parsing
contrasts_with:
  - simple-text-protocol

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of an HTTP request?"
  - "What are the HTTP verbs GET, PUT, and DELETE used for?"
  - "What is the Expect: 100-continue header?"
---

# Quick Definition

HTTP is a plain-text request/reply protocol over TCP in which a client sends a verb, a resource, and headers, and the server replies with a status code, headers, and an optional body.

# Core Definition

HTTP is a plain-text protocol, making it easy to read and debug. An HTTP request begins with a request line specifying the request type (verb), the resource, and the protocol version (e.g., `GET /foo HTTP/1.1`), followed by header lines (each `Name: Value`), an empty line, and an optional message body. A reply begins with the protocol version, a numeric status code, and a reason phrase (e.g., `HTTP/1.1 200 OK`), followed by headers, an empty line, and the body. HTTP defines eight verbs in total; the chapter uses `GET`, `PUT`, and `DELETE`. All HTTP talks about is *resources* and *representations of resources* ("Erlang and OTP in Action," Ch. 11, Section 11.2.1).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A request has four parts: request line, header lines, an empty line, the message body.
2. A reply has the same structure but starts with version + status code + reason phrase.
3. The first digit of a status code indicates its general class (e.g., 4xx = client error).
4. `GET` asks for a copy of a resource's representation; `PUT` uploads/stores; `DELETE` removes a resource.
5. The `Content-Type` header tells the client what kind of data the body holds; `Content-Length` gives the body size.
6. `Expect: 100-continue` lets a server reply `100 Continue` before the client transmits a (possibly large) body.

# Construction / Recognition

## To Construct/Create:
1. Send a request line `VERB /resource HTTP/1.1`.
2. Add header lines, each `Name: Value`.
3. Add an empty line, then the body if any.

## To Identify/Recognize:
1. Inspect raw traffic (e.g., with `nc` and `curl`): a first line with a verb or status code, header lines, a blank line, a body.

# Context & Application

- **Typical contexts**: The transport for the cache's RESTful interface.
- **Common applications**: Web browsers send `GET` for pages; the chapter maps `GET`/`PUT`/`DELETE` onto cache operations.
- **Historical/stylistic notes**: A *resource* is intentionally abstract — even a pizza delivery could be modeled with HTTP verbs.

# Examples

**Example 1** (Section 11.2.1): `curl http://localhost:1156/foo` produces the request line `GET /foo HTTP/1.1` plus `User-Agent`, `Host`, and `Accept` headers.

**Example 2** (Section 11.2.1): A `PUT` of `put.txt` adds `Content-Length: 7` and `Expect: 100-continue`, followed by an empty line and the body `Erlang`.

**Example 3** (Section 11.2.1): A missing resource yields `HTTP/1.1 404 Not Found`; a successful page request yields `HTTP/1.1 200 OK` with headers and an HTML body.

# Relationships

## Related
- **REST** — REST is an architectural style summarizing central HTTP ideas.
- **gen_web_server** — The custom behaviour that implements a subset of HTTP.
- **HTTP packet parsing** — Erlang sockets can parse HTTP for you.

## Contrasts With
- **Simple text-based protocol** — A bespoke line protocol; HTTP is a standardized, widely supported protocol.

# Common Errors

- **Error**: Forgetting the empty line that separates headers from the body.
  **Correction**: Always terminate the header section with a blank line before the body.

- **Error**: Ignoring `Expect: 100-continue`, leaving the client to pause before sending the body.
  **Correction**: Reply `100 Continue` so the client proceeds immediately.

# Common Confusions

- **Confusion**: Thinking a "resource" is always a file.
  **Clarification**: A resource is an abstract concept; the server decides what `GET`/`PUT`/`DELETE` mean for it.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.1 "A quick-and-dirty introduction to HTTP."

# Verification Notes

- Definition source: Direct adaptation of Section 11.2.1.
- Confidence rationale: HIGH — the book explicitly explains HTTP request/reply structure with examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
