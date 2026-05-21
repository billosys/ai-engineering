---
# === CORE IDENTIFICATION ===
concept: Simple Text-Based Protocol
slug: simple-text-protocol

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
section: "11.1.4. The simple text-based protocol"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - text-based TCP protocol
  - request/reply text protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tcp-interface-application
extends: []
related:
  - tcp-server-pattern
  - rest
contrasts_with:
  - rest

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the simple text-based protocol for the cache?"
  - "How is a text request parsed into an Erlang function call?"
  - "What does a reply in the text protocol look like?"
---

# Quick Definition

The simple text-based protocol is a minimal request/reply line protocol over TCP that maps text commands like `lookup[eric]` directly onto `simple_cache` function calls.

# Core Definition

The simple text-based protocol is a minimal plain-text protocol layered over the `tcp_interface` TCP server, exposing the `simple_cache` API functions `insert/2`, `lookup/1`, and `delete/1`. A request has the grammar `Call -> Function ArgList`, where `Function` is `"insert"`, `"lookup"`, or `"delete"` and `ArgList` is an Erlang-list literal. A reply has the form `"OK:" Term ".\n"` or `"ERROR:" Term ".\n"`. It is a simple request/reply protocol where a well-behaved client sends one request at a time and waits for a reply, naturally throttling the request rate ("Erlang and OTP in Action," Ch. 11, Section 11.1.4).

# Prerequisites

- **tcp_interface application** — The protocol is implemented in the `ti_server` module of `tcp_interface`.

# Key Properties

1. Request grammar: `Call -> Function ArgList`; `Function` is `insert | lookup | delete`; `ArgList` is `[]` or `[Terms]`.
2. `insert` takes two arguments (key and value); `lookup` and `delete` take one (the key).
3. Keys and values can be any Erlang terms.
4. Reply form: `"OK:" Term ".\n"` for success, `"ERROR:" Term ".\n"` for failure.
5. Plain text — easy to implement, use, and debug.
6. Request/reply with one in-flight request keeps traffic at a manageable level per connection.

# Construction / Recognition

## To Construct/Create:
1. In `handle_data/3`, split the incoming string at the first `[` into a function name and a raw argument list.
2. Append `"."` to the argument list and tokenize it with `erl_scan:string/2`.
3. Parse the tokens with `erl_parse:parse_term/1` to get the real argument list.
4. Use `apply(simple_cache, list_to_atom(Function), Args)` to make the call.
5. Send `io_lib:fwrite("OK:~p.~n", [Result])`, wrapping it in `try/catch` to emit `"ERROR:~p.~n"` on failure.

## To Identify/Recognize:
1. Lines such as `insert[eric,{"Eric","Merritt"}]` or `lookup[eric]` followed by `OK:`/`ERROR:` replies.

# Context & Application

- **Typical contexts**: A warm-up exercise before building the RESTful HTTP interface.
- **Common applications**: Letting any TCP client (e.g., telnet) drive the cache regardless of language.
- **Historical/stylistic notes**: Reusing `erl_scan`/`erl_parse` means no custom parser is needed; the protocol is easy to adapt to similar servers.

# Examples

**Example 1** (Section 11.1.4): `insert[eric,{"Eric","Merritt"}]` and `lookup[eric]` are valid requests.

**Example 2** (Section 11.1.4): `OK:{"Eric","Merritt"}.` is the reply to `lookup[eric]`; `ERROR:bad_request` is the response to malformed input.

# Relationships

## Builds Upon
- **tcp_interface application** — The protocol is the payload layer of that application.

## Related
- **Concurrent TCP server pattern** — The protocol runs on top of the TCP server framework.

## Contrasts With
- **REST** — A simple custom text protocol; REST is a more structured, standardized HTTP-based interface to the same cache.

# Common Errors

- **Error**: Sending a request without the `[` argument-list bracket.
  **Correction**: Always include the bracketed Erlang-list argument; without `[` parsing fails and yields an `ERROR:` reply.

- **Error**: Sending multiple requests without waiting for replies.
  **Correction**: The protocol is request/reply — send one request and wait for its reply before the next.

# Common Confusions

- **Confusion**: Thinking the protocol can only carry strings.
  **Clarification**: Keys and values may be any Erlang terms, parsed via `erl_scan`/`erl_parse`.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.1.4 "The simple text-based protocol" and 11.1.5 "Text interface implementation." See Listing 11.4.

# Verification Notes

- Definition source: Direct adaptation of Section 11.1.4 and the `handle_data/3` listing in 11.1.5.
- Confidence rationale: HIGH — the book gives the protocol grammar and a complete implementation listing.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
