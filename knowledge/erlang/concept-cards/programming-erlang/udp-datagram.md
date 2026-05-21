---
# === CORE IDENTIFICATION ===
concept: UDP Datagram
slug: udp-datagram

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
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
  - datagram
  - "User Datagram Protocol message"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - gen-udp-module
  - udp-broadcasting
contrasts_with:
  - tcp-socket

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a UDP datagram?"
  - "What is the difference between TCP and UDP?"
  - "When should I use UDP instead of TCP?"
---

# Quick Definition

A UDP datagram is a short message sent between machines using the User Datagram Protocol. Datagrams are unreliable — they may arrive out of order, not at all, or more than once — but if they arrive, they arrive undamaged.

# Core Definition

"UDP lets applications send short messages (called datagrams) to each other, but there is no guarantee of delivery for these messages. They can also arrive out of order" ("Programming with Sockets", chapter intro). UDP is "a connectionless protocol, which means the client does not have to establish a connection to the server before sending it a message." Datagrams are unreliable: "if a client sends a sequence of UDP datagrams to a server, then the datagrams might arrive out of order, not at all, or even more than once, but the individual datagrams, if they arrive, will be undamaged" ("UDP" section). Large datagrams may be split into fragments, but the IP protocol reassembles them before delivery.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Connectionless — no connection setup required before sending.
2. Unreliable — no guarantee of delivery.
3. Unordered — datagrams may arrive in any order or be duplicated.
4. Datagrams that do arrive are undamaged (intact).
5. Lower overhead and faster than TCP.
6. Well suited to applications where many clients send small messages to a server.

# Construction / Recognition

## To send/receive UDP datagrams in Erlang:
1. Open a UDP socket with `gen_udp:open(Port, [binary])`.
2. Send a datagram with `gen_udp:send(Socket, Host, Port, Data)`.
3. Receive datagrams as `{udp, Socket, Host, Port, Bin}` messages.
4. Because delivery is not guaranteed, clients must use a timeout when waiting for a reply.

## To recognize when UDP fits:
1. The application can tolerate lost or reordered messages.
2. Many clients send small, independent messages.

# Context & Application

- **Typical contexts**: Lightweight request/response where occasional loss is acceptable; broadcasting on a local network.
- **Common applications**: The chapter builds a UDP factorial server and a UDP broadcast channel.
- **Historical/stylistic notes**: TCP and UDP are described as the two core Internet protocols; UDP trades reliability for speed.

# Examples

**Example 1** ("A UDP Factorial Server"): A server receives a number as a UDP datagram, computes its factorial, and sends the result back as a datagram.

**Example 2** ("The Simplest UDP Server and Client"): A client opens a socket, sends a request datagram, and waits up to 2000 ms for a reply, returning `error` on timeout because UDP is unreliable.

# Relationships

## Related
- **gen_udp module** — The Erlang library for sending and receiving UDP datagrams.
- **UDP broadcasting** — Uses UDP datagrams sent to a broadcast address.

## Contrasts With
- **TCP socket** — TCP is connection-oriented, reliable, and ordered; UDP is connectionless, unreliable, and unordered.

# Common Errors

- **Error**: Waiting for a UDP reply without a timeout.
  **Correction**: Always use an `after` timeout in the receive, since the reply datagram may never arrive.

- **Error**: Assuming datagrams arrive in send order.
  **Correction**: Add sequence numbers in the application if ordering matters.

# Common Confusions

- **Confusion**: Believing a corrupt datagram can still be delivered.
  **Clarification**: A datagram either arrives undamaged or does not arrive at all.

- **Confusion**: Thinking UDP is "broken" because it loses messages.
  **Clarification**: Unreliability is a deliberate trade-off — UDP is faster and connectionless, ideal for many small messages.

# Source Reference

Chapter 17: "Programming with Sockets", chapter introduction and section "UDP".

# Verification Notes

- Definition source: Direct quotes from chapter intro and "UDP" section.
- Confidence rationale: HIGH — UDP and datagrams are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
