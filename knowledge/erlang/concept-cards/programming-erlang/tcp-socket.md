---
# === CORE IDENTIFICATION ===
concept: TCP Socket
slug: tcp-socket

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
section: "Using TCP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - socket
  - "stream socket"
  - "TCP/IP socket"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp
extends: []
related:
  - controlling-process
  - active-and-passive-sockets
  - packet-framing-option
contrasts_with:
  - udp-socket

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a TCP socket?"
  - "What is the difference between TCP and UDP?"
---

# Quick Definition

A TCP socket is a communication channel that lets a machine exchange a reliable, ordered stream of bytes with another machine over the Internet using the Transmission Control Protocol.

# Core Definition

A socket is "a communication channel that allows machines to communicate over the Internet using the Internet Protocol (IP)" ("Programming with Sockets," chapter introduction). TCP — the Transmission Control Protocol — provides a reliable stream of bytes that are delivered in order as long as the connection is established. Sending data by TCP incurs a larger overhead than UDP; the trade-off is reliability and ordering versus speed. TCP socket data is "just an undifferentiated stream of bytes" that may be broken into arbitrary-sized fragments during transmission, so applications need a framing convention (the `{packet, N}` option) to know where one message ends and the next begins ("A Simple TCP Server").

# Prerequisites

- **The gen_tcp module** — TCP sockets in Erlang are created and operated on exclusively through `gen_tcp`.

# Key Properties

1. Provides a reliable, ordered, bidirectional byte stream while the connection is established.
2. Connection-oriented: a connection must be established before data is exchanged.
3. Data is an undifferentiated byte stream; transmission may fragment it arbitrarily.
4. Higher overhead than UDP in exchange for reliability and ordering.
5. Each socket has a controlling process; if that process dies the socket is closed.
6. When a peer finishes/closes, the controlling process receives a `{tcp_closed, Socket}` message.

# Construction / Recognition

## To create a TCP socket:

1. As a client, call `gen_tcp:connect(Host, Port, Options)`.
2. As a server, call `gen_tcp:listen(Port, Options)` then `gen_tcp:accept/1`; the socket returned by `accept` is the connection socket.

## To recognize TCP-socket behaviour:

1. Data arrives as an in-order stream (no datagram boundaries unless `{packet, N}` is set).
2. Connection loss surfaces as a `{tcp_closed, Socket}` message rather than silently dropping data.

# Context & Application

TCP sockets are the right choice whenever an application needs guaranteed, ordered delivery — file transfer, HTTP, RPC, and the book's term-passing servers.

- **Typical contexts**: Reliable client/server communication over IP.
- **Common applications**: Web clients and servers, streaming servers, distributed services.
- **Historical/stylistic notes**: The book pairs TCP sockets with `term_to_binary` to send Erlang terms directly between nodes.

# Examples

**Example 1** ("Fetching Data from a Server"): `nano_get_url/1` opens a TCP socket to port 80 of www.google.com in `binary`, `{packet, 0}` mode and reads the HTTP response as a sequence of `{tcp,Socket,Bin}` fragments.

**Example 2** ("A Simple TCP Server"): The nano server opens a TCP socket on port 2345 with 4-byte packet framing and exchanges encoded Erlang terms with a client.

# Relationships

## Builds Upon

- **The gen_tcp module** — All TCP-socket operations go through `gen_tcp`.

## Enables

- **Controlling process** — Every TCP socket is owned by a controlling process.
- **Active and passive sockets** — TCP sockets can be opened in either reception mode.

## Related

- **Packet framing option** — `{packet, N}` imposes message boundaries on the TCP stream.

## Contrasts With

- **UDP socket** — Connectionless and unreliable; messages may be lost, reordered, or duplicated, whereas a TCP stream is reliable and ordered.

# Common Errors

- **Error**: Assuming a single `gen_tcp:recv` or one `{tcp,...}` message contains a whole logical request.
  **Correction**: TCP fragments data arbitrarily; reassemble fragments, or use `{packet, N}` so the driver does it.

# Common Confusions

- **Confusion**: Thinking TCP guarantees message boundaries.
  **Clarification**: TCP guarantees an ordered byte stream, not message framing; framing is the application's responsibility (or the `{packet, N}` option's).

- **Confusion**: Believing TCP is always preferable to UDP.
  **Clarification**: TCP costs more overhead; UDP is better for many small messages from many clients where occasional loss is tolerable.

# Source Reference

Chapter 17: "Programming with Sockets," chapter introduction and sections "Using TCP" and "A Simple TCP Server." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction's socket and TCP definitions.
- Confidence rationale: HIGH — TCP and sockets are explicitly defined in the opening paragraphs.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
