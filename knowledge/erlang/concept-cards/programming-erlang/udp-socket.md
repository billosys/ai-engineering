---
# === CORE IDENTIFICATION ===
concept: UDP Socket
slug: udp-socket

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
section: "UDP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_udp
  - "UDP datagram socket"
  - "User Datagram Protocol socket"
  - datagram

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - binary
extends: []
related:
  - gen-tcp
contrasts_with:
  - tcp-socket

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I program with TCP/UDP sockets?"
  - "What is the difference between TCP and UDP?"
---

# Quick Definition

A UDP socket sends and receives short, connectionless messages (datagrams) using the `gen_udp` module; delivery is fast but unreliable — datagrams may be lost, reordered, or duplicated.

# Core Definition

UDP — the User Datagram Protocol — "lets applications send short messages (called datagrams) to each other, but there is no guarantee of delivery for these messages. They can also arrive out of order" ("Programming with Sockets," chapter introduction). UDP is a connectionless protocol: the client does not establish a connection before sending, which makes UDP well suited to applications where large numbers of clients send small messages to a server ("UDP"). In Erlang, UDP sockets are programmed with the `gen_udp` module — `gen_udp:open/2` opens a socket, `gen_udp:send/4` sends a datagram to a host and port, and incoming datagrams arrive as `{udp, Socket, Host, Port, Bin}` messages. Writing UDP clients and servers is easier than TCP because there are no connections to maintain and no "socket closed" messages to handle.

# Prerequisites

- **Process** — Incoming datagrams are delivered as messages to the socket's controlling process.
- **Message passing** — UDP data surfaces as `{udp, Socket, Host, Port, Bin}` messages.
- **Binary** — Sockets are typically opened in `binary` mode so datagrams arrive as binaries.

# Key Properties

1. Connectionless — no connection is established before sending.
2. Unreliable — datagrams may be lost, arrive out of order, or even be delivered twice.
3. Individual datagrams, if they arrive, arrive undamaged; IP reassembles fragmented datagrams.
4. Opened with `gen_udp:open(Port, Options)`; `Port = 0` lets the system assign an ephemeral port.
5. Datagrams arrive as `{udp, Socket, Host, Port, Bin}` messages including the sender's address.
6. No "socket closed" messages — the server cannot block a client by refusing to read.

# Construction / Recognition

## To build a UDP server:

1. Call `gen_udp:open(Port, [binary])` to open the socket.
2. Loop on `receive {udp, Socket, Host, Port, Bin} -> ... end`.
3. Compute a reply and send it with `gen_udp:send(Socket, Host, Port, BinReply)`.

## To build a UDP client:

1. Open a socket with `gen_udp:open(0, [binary])`.
2. Send a request with `gen_udp:send(Socket, Host, Port, Request)`.
3. Wait for `{udp, Socket, _, _, Bin}` with an `after` timeout, since a reply may never arrive.
4. Close the socket with `gen_udp:close(Socket)`.

# Context & Application

UDP suits low-latency, high-volume, loss-tolerant traffic.

- **Typical contexts**: Online gaming, broadcast/multicast, simple request/response services.
- **Common applications**: The book's UDP factorial server, LAN broadcasting via `{broadcast, true}`.
- **Historical/stylistic notes**: UDP is "often used for online gaming where low latency is required, and it doesn't matter if the odd packet is lost" ("UDP Packet Gotchas").

# Examples

**Example 1** ("A UDP Factorial Server"): `udp_test` opens port 4000, receives a number, computes its factorial, and sends back `term_to_binary(Fac)`.

**Example 2** ("Broadcasting to Multiple Machines"): `broadcast:send/1` opens a UDP socket with `{broadcast, true}` and sends an iolist to every machine on the LAN.

## Worked Example

A minimal UDP client with a timeout (from "The Simplest UDP Server and Client"):

```erlang
client(Request) ->
    {ok, Socket} = gen_udp:open(0, [binary]),
    ok = gen_udp:send(Socket, "localhost", 4000, Request),
    Value = receive
                {udp, Socket, _, _, Bin} ->
                    {ok, Bin}
            after 2000 ->
                    error
            end,
    gen_udp:close(Socket),
    Value.
```

# Relationships

## Builds Upon

- **Process** — Datagrams are delivered to the controlling process's mailbox.

## Related

- **The gen_tcp module** — `gen_udp` is the connectionless sibling library.

## Contrasts With

- **TCP socket** — TCP is connection-oriented, reliable, and ordered; UDP is connectionless, unreliable, and may reorder or duplicate datagrams. TCP delivers `{tcp_closed,...}` on disconnect; UDP has no such notion.

# Common Errors

- **Error**: Treating a UDP reply as guaranteed and looping forever waiting for it.
  **Correction**: Always use an `after` timeout — datagrams can be lost entirely.

- **Error**: Assuming a reply matches its request in an RPC built on UDP.
  **Correction**: A datagram may be delivered twice; tag requests with a unique `make_ref()` and verify the returned reference.

# Common Confusions

- **Confusion**: Believing a datagram that arrives may be corrupted or partial.
  **Clarification**: If a datagram arrives at all, it arrives undamaged; IP reassembles fragments before delivery.

- **Confusion**: Thinking the server can throttle a UDP client the way it can a TCP client.
  **Clarification**: UDP is connectionless — the server has no idea who the clients are and cannot block them.

# Source Reference

Chapter 17: "Programming with Sockets," sections "UDP," "The Simplest UDP Server and Client," "A UDP Factorial Server," "UDP Packet Gotchas," "Broadcasting to Multiple Machines." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and "UDP" section.
- Confidence rationale: HIGH — UDP is explicitly defined and demonstrated with full client/server code.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
