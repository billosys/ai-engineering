---
# === CORE IDENTIFICATION ===
concept: The packet Socket Option
slug: packet-framing-option

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
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
  - "{packet, N}"
  - "packet option"
  - "length-prefix framing"
  - "{packet, 0}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tcp-socket
  - gen-tcp
extends: []
related:
  - simple-tcp-server
  - binary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang frame messages on a TCP stream?"
  - "What does the {packet, N} socket option do?"
---

# Quick Definition

The `{packet, N}` socket option tells Erlang to prefix every application message with an `N`-byte length count, so the driver can split the TCP byte stream back into whole messages.

# Core Definition

TCP socket data is just an undifferentiated stream of bytes that may be broken into arbitrary-sized fragments during transmission, so an application needs a convention for how much data makes up one logical request or response ("A Simple TCP Server"). Erlang's convention is the `{packet, N}` option to `gen_tcp:connect` and `gen_tcp:listen`: every logical request or response is preceded by an `N`-byte length count, where `N` is 1, 2, or 4. The word *packet* here refers to the length of an application message, not the physical packet seen on the wire. With `{packet, 0}`, TCP data is delivered directly to the application unmodified, with no framing. Once a socket is opened with a non-zero `{packet, N}` option, the application no longer worries about fragmentation — "the Erlang drivers will make sure that all fragmented data messages are reassembled to the correct lengths before delivering them to the application."

# Prerequisites

- **TCP socket** — Framing exists to impose message boundaries on a TCP byte stream.
- **The gen_tcp module** — The option is passed to `gen_tcp:connect`/`gen_tcp:listen` (or set via `inet:setopts`).

# Key Properties

1. `N` may be 0, 1, 2, or 4 — the size in bytes of the length header prefixed to each message.
2. `{packet, 0}` means no framing: data is delivered to the application unmodified.
3. With non-zero `N`, the Erlang driver reassembles fragments into whole messages of the correct length.
4. The `{packet, N}` value used by client and server must agree — if the server uses `{packet,2}` and the client `{packet,4}`, nothing works.
5. Combined with `term_to_binary`/`binary_to_term`, two lines of code give full message packaging and encoding.

# Construction / Recognition

## To use packet framing:

1. Open the socket with `{packet, N}` in the options list, e.g. `gen_tcp:listen(2345, [binary, {packet, 4}])`.
2. Use the *same* `N` on both client and server.
3. Send and receive whole logical messages; the driver handles fragmentation and reassembly.

## To recognize when to use it:

1. If the protocol has discrete request/response messages, use a non-zero `{packet, N}`.
2. If the protocol is a raw stream (e.g. fetching an HTTP page), use `{packet, 0}` and reassemble manually.

# Context & Application

`{packet, N}` is the standard way to send discrete messages over TCP in Erlang without writing framing code.

- **Typical contexts**: Term-passing servers, RPC over TCP.
- **Common applications**: The nano server uses `{packet, 4}`; the HTTP fetch example uses `{packet, 0}`.
- **Historical/stylistic notes**: The book contrasts this with text-based protocols, noting term framing plus `term_to_binary` is far faster and smaller than XML.

# Examples

**Example 1** ("Fetching Data from a Server"): `nano_get_url/1` opens the socket with `{packet, 0}` so raw HTTP data is delivered unmodified and reassembled by the application.

**Example 2** ("A Simple TCP Server"): `start_nano_server/0` listens with `{packet, 4}`, so each application message is preceded by a 4-byte length header and the driver reassembles fragmented data.

# Relationships

## Builds Upon

- **TCP socket** — Framing adds message boundaries to a raw TCP stream.

## Related

- **A Simple TCP Server** — The nano server relies on `{packet, 4}` for its message boundaries.
- **Binary** — Framed messages are typically binaries carrying `term_to_binary`-encoded terms.

# Common Errors

- **Error**: Using different `{packet, N}` values on client and server.
  **Correction**: Both ends must use the identical packet size, or no messages are decoded correctly.

- **Error**: Using `{packet, 0}` and assuming each `{tcp,...}` message is a whole request.
  **Correction**: With `{packet, 0}` data is unframed; either reassemble fragments yourself or use a non-zero `N`.

# Common Confusions

- **Confusion**: Thinking `{packet, N}` controls the physical network packet size.
  **Clarification**: It controls the length of an application-level message; physical packets are unrelated.

# Source Reference

Chapter 17: "Programming with Sockets," sections "A Simple TCP Server" and "Fetching Data from a Server." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the framing discussion in "A Simple TCP Server."
- Confidence rationale: HIGH — the `{packet, N}` convention is explicitly defined and used in multiple examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
