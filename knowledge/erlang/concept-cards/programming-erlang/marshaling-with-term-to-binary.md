---
# === CORE IDENTIFICATION ===
concept: Marshaling with term_to_binary
slug: marshaling-with-term-to-binary

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
  - marshaling
  - "term_to_binary / binary_to_term"
  - "Erlang term encoding"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
extends: []
related:
  - packet-option
  - gen-tcp-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I encode Erlang terms for sending over a socket?"
  - "What is marshaling and demarshaling?"
  - "Why use term_to_binary instead of XML?"
---

# Quick Definition

Marshaling is encoding an Erlang term into a binary for transmission; demarshaling is the inverse. The BIFs `term_to_binary/1` and `binary_to_term/1` do this — converting any Erlang term to a wire-ready binary and back.

# Core Definition

When sending data over a socket, the application must decide how data within a request or response is encoded and decoded — "encoding the data is sometimes called marshaling, and decoding the data is sometimes called demarshaling" ("A Simple TCP Server"). The book uses "the simplest possible way of encoding and decoding messages using `term_to_binary` to encode Erlang terms and using its inverse, `binary_to_term`, to decode the data." This gives "a significant advantage over text-based methods such as HTTP or XML": using these BIFs "is typically more than an order of magnitude faster than performing an equivalent operation using XML terms and involves sending far less data."

# Prerequisites

- **Binary** — `term_to_binary` produces a binary; `binary_to_term` consumes one.

# Key Properties

1. `term_to_binary(Term)` encodes any Erlang term as a binary.
2. `binary_to_term(Bin)` is the exact inverse, reconstructing the term.
3. More than an order of magnitude faster than equivalent XML encoding/decoding.
4. Produces far less data on the wire than text-based formats.
5. Works with any Erlang term — tuples, lists, atoms, numbers, etc.
6. Typically paired with the `{packet, N}` socket option, which handles framing.

# Construction / Recognition

## To marshal/demarshal over a socket:
1. On the sending side, call `term_to_binary(Term)` and pass the result to `gen_tcp:send/2` (or `gen_udp:send/4`).
2. Open sockets with a `{packet, N}` option so each encoded term is a framed message.
3. On the receiving side, take the `Bin` from the `{tcp, Socket, Bin}` message and call `binary_to_term(Bin)` to recover the term.

# Context & Application

- **Typical contexts**: Erlang-to-Erlang communication over TCP or UDP sockets where both ends speak Erlang.
- **Common applications**: The chapter's nano evaluation server and the UDP factorial server both encode terms with `term_to_binary` and decode with `binary_to_term`.
- **Historical/stylistic notes**: Armstrong contrasts this favorably with text-based protocols like HTTP and XML for speed and compactness.

# Examples

**Example 1** ("A Simple TCP Server", client): `ok = gen_tcp:send(Socket, term_to_binary(Str))` encodes the request; the server decodes with `Str = binary_to_term(Bin)`.

**Example 2** ("A UDP Factorial Server"): the server computes `N = binary_to_term(Bin)` and replies with `gen_udp:send(Socket, Host, Port, term_to_binary(Fac))`.

# Relationships

## Related
- **packet option** — Handles message framing; marshaling handles encoding. Together they give a complete protocol in two lines.
- **gen_tcp module** — `term_to_binary` output is sent via `gen_tcp:send`.

# Common Errors

- **Error**: Calling `binary_to_term` on data that was not produced by `term_to_binary`.
  **Correction**: Both ends must use the same encoding; only decode binaries that were term-encoded.

- **Error**: Mismatched `{packet, N}` so the binary arrives fragmented.
  **Correction**: Use an agreed nonzero `{packet, N}` so each encoded term arrives as one complete message before calling `binary_to_term`.

# Common Confusions

- **Confusion**: Thinking a text format like XML must be used to send structured data.
  **Clarification**: For Erlang-to-Erlang links, `term_to_binary` is faster and more compact than XML.

# Source Reference

Chapter 17: "Programming with Sockets", section "A Simple TCP Server" (encoding/decoding discussion) and section "A UDP Factorial Server".

# Verification Notes

- Definition source: Direct quotes from "A Simple TCP Server".
- Confidence rationale: HIGH — marshaling/demarshaling and the BIFs are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slug `binary` used.
- Re-extraction notes: Fresh extraction.
