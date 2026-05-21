---
# === CORE IDENTIFICATION ===
concept: Sockets and SSL Transport
slug: sockets-and-ssl-transport

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-transport
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Sockets and SSL"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - socket transport
  - custom socket layer
  - "gen_tcp/ssl layer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
extends: []
related:
  - demilitarized-zone
  - system-monitor
contrasts_with:
  - distributed-erlang

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use sockets instead of distributed Erlang?"
  - "How do I choose network protocols for my nodes?"
---

# Quick Definition

A socket-based transport is a thin layer above the `ssl` or `gen_tcp` libraries used to connect nodes when distributed Erlang is not the right tool — for reasons of security, throughput, or bottleneck avoidance.

# Core Definition

"When distributed Erlang is not the right tool for the job, adding a thin layer above the ssl or gen_tcp libraries starts making sense. You open one or more sockets between the nodes, controlling the flow of information sent and received" (Cesarini & Vinoski, p. 392). It is appropriate when bottlenecks occur in the global name server, `rex`, or the net kernel, or in the distributed Erlang port itself — which handles only one request at a time and is designed for control messages rather than data transfer — or when distributed Erlang must be avoided for security reasons.

# Prerequisites

- **Distributed Erlang** — A socket transport is the alternative chosen when distributed Erlang is unsuitable; understand it first.

# Key Properties

1. A thin layer above the `ssl` or `gen_tcp` libraries.
2. One or more sockets are opened between nodes, with explicit flow control.
3. Used when the dist port, global name server, `rex`, or net kernel become bottlenecks.
4. Used when distributed Erlang must be avoided for security (e.g., across a DMZ).
5. Multiple connections help when transferring large volumes of data (images, logs, emails).
6. Can be implemented with a process-pool library such as Poolboy, or a few dozen lines of custom code.

# Construction / Recognition

## To Construct/Create:
1. Start with a single socket connection between nodes.
2. Build a thin connection API over `gen_tcp` or `ssl`.
3. Add more connections only when metrics show a single connection is a bottleneck.
4. Optionally base the socket library on a process pool such as Poolboy.

## To Identify/Recognize:
1. Recognize a socket transport as an explicit, application-level connection layer rather than transparent distributed Erlang.

# Context & Application

- **Typical contexts**: Front-end-to-logic communication across a DMZ; high-volume data transfer.
- **Common applications**: Transferring images, logs, emails, and email attachments; high-RPC-rate links (gen_rpc benchmarked above 60,000 RPC requests/second).
- **Historical/stylistic notes**: Avoid premature optimization — the volumes of data have to be substantial for multiple connections to pay off (p. 393).

# Examples

**Example 1** (pp. 392-393): An instant-messaging system coped with a single TCP connection from the DMZ; when upgraded to also handle larger email messages, queues built up in front-end nodes and the VM ran out of memory — adding multiple connections removed the bottleneck.

**Example 2** (p. 393): The `gen_rpc` application on GitHub has been benchmarked doing in excess of 60,000 RPC requests per second.

# Relationships

## Builds Upon
- **Distributed Erlang** — A socket transport replaces it when it is unsuitable

## Enables
- A socket transport enables secure, flow-controlled, high-volume internode links.

## Related
- **Demilitarized zone** — Socket transport is used across a DMZ instead of distributed Erlang
- **System monitor** — Used to detect distributed-port congestion that motivates sockets

## Contrasts With
- **Distributed Erlang** — Sockets are explicit and flow-controlled; distributed Erlang is transparent but can bottleneck on a single port

# Common Errors

- **Error**: Adding many connections preemptively
  **Correction**: Start with a single connection and add more only when metrics show a problem multiple connections can fix.

# Common Confusions

- **Confusion**: A socket transport must be a large framework.
  **Clarification**: In its simplest guise it is a thin layer of a few dozen lines of code, highly optimized for the application's traffic and security requirements.

# Source Reference

Chapter 12: Distributed Architectures, "Sockets and SSL," pages 392-394. See Figure 13-8.

# Verification Notes

- Definition source: Direct quote from p. 392.
- Confidence rationale: HIGH — the source dedicates a named section to socket-based transport with a concrete war story.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
