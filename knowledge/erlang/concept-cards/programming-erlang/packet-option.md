---
# === CORE IDENTIFICATION ===
concept: The packet Socket Option
slug: packet-option

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
  - "{packet, N}"
  - "packet length header"
  - "message framing option"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - tcp-socket
extends: []
related:
  - marshaling-with-term-to-binary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I know how much data makes up a single request?"
  - "What does the {packet, N} socket option do?"
  - "How does Erlang frame messages over a TCP byte stream?"
---

# Quick Definition

The `{packet, N}` socket option makes the Erlang TCP driver prefix every application message with an N-byte length count and reassemble fragmented data into complete messages before delivering them to the application.

# Core Definition

TCP socket data "is just an undifferentiated stream of bytes" that can be broken into arbitrary-sized fragments, so a convention is needed to know how much data is one request or response. "In the Erlang case we use the simple convention that every logical request or response will be preceded by an `N` (1, 2, or 4) byte length count. This is the meaning of the `{packet, N}` argument in the `gen_tcp:connect` and `gen_tcp:listen` functions" ("A Simple TCP Server"). The word *packet* here "refers to the length of an application request or response message, not to the physical packet seen on the wire." With `{packet, N}` set, "the Erlang drivers will make sure that all fragmented data messages are reassembled to the correct lengths before delivering them to the application." `{packet, 0}` means the TCP data is delivered directly to the application unmodified.

# Prerequisites

- **gen_tcp module** — `{packet, N}` is passed to `gen_tcp:connect/3` and `gen_tcp:listen/2`.
- **TCP socket** — The option exists because raw TCP is an unframed byte stream.

# Key Properties

1. `N` can be 0, 1, 2, or 4.
2. `{packet, 0}` delivers the raw byte stream unmodified.
3. `{packet, N}` (N = 1, 2, 4) prefixes each message with an N-byte length header.
4. The driver reassembles fragmented data into complete framed messages automatically.
5. The `packet` value used by client and server must agree, or communication fails.
6. "Packet" refers to the application message length, not the wire-level IP packet.

# Construction / Recognition

## To use packet framing:
1. Open the client socket with `gen_tcp:connect(Host, Port, [binary, {packet, N}])`.
2. Open the server's listening socket with `gen_tcp:listen(Port, [binary, {packet, N}, ...])`.
3. Ensure the same `N` is used on both ends.
4. Send a complete message with `gen_tcp:send/2`; the driver delivers it framed.

## To recognize correct framing:
1. Each `gen_tcp:send` corresponds to exactly one `{tcp, Socket, Bin}` message of the right length on the other side.

# Context & Application

- **Typical contexts**: Any TCP protocol where the application needs discrete request/response messages rather than a raw stream.
- **Common applications**: The chapter's nano server uses `{packet, 4}` so each binary-encoded Erlang term is a self-delimiting message.
- **Historical/stylistic notes**: Combined with `term_to_binary`/`binary_to_term`, `{packet, 4}` gives a complete packaging-and-encoding convention "in two lines of code."

# Examples

**Example 1** ("Fetching Data from a Server"): `gen_tcp:connect(Host, 80, [binary, {packet, 0}])` delivers raw HTTP bytes unmodified.

**Example 2** ("A Simple TCP Server"): `gen_tcp:listen(2345, [binary, {packet, 4}, {reuseaddr, true}, {active, true}])` frames each message with a 4-byte length header.

# Relationships

## Related
- **marshaling with term_to_binary** — `{packet, N}` handles framing while `term_to_binary` handles encoding; together they form the full convention.

# Common Errors

- **Error**: Using `{packet, 2}` on the server and `{packet, 4}` on the client.
  **Correction**: The `packet` argument must agree on both ends — otherwise nothing works.

- **Error**: Using `{packet, 0}` and then assuming one message arrives per send.
  **Correction**: With `{packet, 0}` the data is an unframed stream; use a nonzero `N` for message framing.

# Common Confusions

- **Confusion**: Thinking `{packet, N}` refers to network/IP packets.
  **Clarification**: It refers to the length of an application-level message, not the physical packet on the wire.

- **Confusion**: Believing the application must handle fragmentation itself.
  **Clarification**: With `{packet, N}`, the Erlang driver reassembles fragments before delivery.

# Source Reference

Chapter 17: "Programming with Sockets", sections "Fetching Data from a Server" and "A Simple TCP Server".

# Verification Notes

- Definition source: Direct quotes from "A Simple TCP Server".
- Confidence rationale: HIGH — the option is explicitly defined and explained.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
