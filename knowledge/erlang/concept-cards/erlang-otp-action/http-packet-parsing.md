---
# === CORE IDENTIFICATION ===
concept: HTTP Packet Parsing on Sockets
slug: http-packet-parsing

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: networking
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
  - "{packet, http_bin}"
  - http_bin socket option
  - built-in HTTP packet parsing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - http-protocol
  - active-passive-sockets
extends: []
related:
  - gen-web-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the {packet, http_bin} socket option do?"
  - "What messages does an HTTP-parsing socket send?"
  - "How do you handle the request body after parsing headers?"
---

# Quick Definition

With the `{packet, http_bin}` socket option, the Erlang runtime parses incoming HTTP for you and delivers the request line, each header, and the end-of-headers marker as structured, easy-to-handle messages.

# Core Definition

The `{packet, http_bin}` option tells a socket that incoming data is expected to be formatted as HTTP; the socket parses the text and sends structured messages instead of raw bytes, saving boring work and speeding up HTTP handling. The request line arrives as `{http, Socket, {http_request, Method, Uri, Version}}`; each header arrives as `{http, Socket, {http_header, Length, Name, ReservedField, Value}}`; the empty line ending the headers arrives as `{http, Socket, http_eoh}`. The method name is an atom for the seven common HTTP methods and a binary for unrecognized ones. To read a request body, the socket is switched from `{packet, http_bin}` to `{packet, raw}` ("Erlang and OTP in Action," Ch. 11, Section 11.2.2 "The gws_server module").

# Prerequisites

- **HTTP protocol basics** — You must understand HTTP request structure to use the parsed messages.
- **Active and passive sockets** — Parsed messages are delivered via the socket's active mode.

# Key Properties

1. Enabled with the `{packet, http_bin}` option (incoming data delivered as binaries).
2. Request line message: `{http, Socket, {http_request, Method, Uri, Version}}`.
3. Header message: `{http, Socket, {http_header, Length, Name, ReservedField, Value}}`.
4. End-of-headers message: `{http, Socket, http_eoh}`.
5. Method is an atom for the seven common methods (e.g., `'PUT'`), a binary for others (e.g., `<<"PATCH">>`).
6. To collect a body, switch to `{packet, raw}`; subsequent data arrives as ordinary `{tcp, Socket, Data}` messages.

# Construction / Recognition

## To Construct/Create:
1. Open the listening socket with `{packet, http_bin}` (plus `binary`).
2. Handle `{http_request, ...}`, `{http_header, ...}`, and `http_eoh` messages in `handle_info`.
3. On `Content-Length`, store the count in state; on `Expect: "100-continue"`, send a `100 Continue` reply.
4. At `http_eoh`, if `content_remaining` is zero process the request; otherwise switch to `{packet, raw}` and accumulate the body until the counter reaches zero.

## To Identify/Recognize:
1. `handle_info` clauses matching `{http, _, {http_request, ...}}`, `{http_header, ...}`, and `http_eoh`.

# Context & Application

- **Typical contexts**: Implementing an HTTP server without writing a parser.
- **Common applications**: The `gws_server` module of `gen_web_server`.
- **Historical/stylistic notes**: Built-in parsing both saves code and speeds up HTTP handling.

# Examples

**Example 1** (Section 11.2.2): A `PUT` request arrives as `{http, Socket, {http_request, 'PUT', <<"/foo">>, {1,1}}}`.

**Example 2** (Section 11.2.2): Unrecognized methods arrive with a binary name, e.g. `<<"MKCOL">>` for the WebDAV `MKCOL` method.

# Relationships

## Builds Upon
- **HTTP protocol basics** — The parsed messages mirror HTTP's request/header structure.

## Enables
- **gen_web_server** — `gws_server` relies on `{packet, http_bin}` to handle HTTP.

## Related
- **Active and passive sockets** — Parsed messages are delivered through active-mode delivery.

# Common Errors

- **Error**: Staying in `{packet, http_bin}` mode while reading the body.
  **Correction**: Switch to `{packet, raw}` after `http_eoh` when a non-empty body is expected.

- **Error**: Forgetting to re-arm `{active, once}` in every `handle_info` clause that continues reading.
  **Correction**: Re-enable `{active, once}` after handling each message.

# Common Confusions

- **Confusion**: Expecting all HTTP method names to be atoms.
  **Clarification**: Only the seven common methods are atoms; unrecognized methods are delivered as binaries.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.2, subsection "The gws_server module and the use of {active, once}."

# Verification Notes

- Definition source: Direct adaptation of the `gws_server` subsection.
- Confidence rationale: HIGH — the book explicitly describes the message forms and the `{packet, http_bin}`/`{packet, raw}` switch.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
