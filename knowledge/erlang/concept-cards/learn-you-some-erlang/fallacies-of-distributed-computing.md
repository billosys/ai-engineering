---
concept: Fallacies of Distributed Computing
slug: fallacies-of-distributed-computing
category: distribution
subcategory: distribution-theory
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Fallacies of Distributed Computing"
extraction_confidence: high
aliases:
  - "fallacies of distributed computing"
  - "eight fallacies"
prerequisites:
  - distributed-erlang
extends: []
related:
  - network-partition
  - cap-theorem
contrasts_with: []
answers_questions:
  - "What are the fallacies of distributed computing?"
  - "Which distributed-computing assumptions does Erlang make?"
  - "What must I know before doing distributed Erlang?"
---

# Fallacies of Distributed Computing

## Quick Definition

The fallacies of distributed computing are eight false assumptions people make about distributed systems. Awareness of them is a prerequisite for designing distributed Erlang applications correctly.

## Core Definition

The book devotes a section to "eight major assumptions people make (some of which Erlang's designers made for various reasons) that end up biting them in the ass later" (Ch. 26, "Fallacies of Distributed Computing"), citing Arnon Rotem-Gal-Oz's "Fallacies of Distributed Computing Explained." Understanding which assumptions hold and which Erlang itself makes is necessary to use Erlang's distribution tools well.

## Prerequisites

- **Distributed-erlang** — The fallacies frame how to use Erlang's distribution layer

## Key Properties

1. **The network is reliable** — it is not; Erlang offers no special measures but does detect failures via links/monitors
2. **There is no latency** — there is; Erlang's async, timeout-based design adapts well, but your design may still assume fast replies
3. **Bandwidth is infinite** — it is not; keep messages small, since large messages can block heartbeats
4. **The network is secure** — it is not; Erlang assumes a safe network (no built-in security) — use SSL or tunneling
5. **Topology doesn't change** — it does; avoid hardcoding node names and hostnames
6. **There is only one administrator** — there is not; provide diagnostics and handle multiple protocol versions
7. **Transport cost is zero** — it is not, in time (serialization) or money (bandwidth); small messages help
8. **The network is homogeneous** — it is not; rely on well-documented, open data formats

## Construction / Recognition

### To apply the fallacies

1. Before building a distributed app, ask which fallacies you could run into
2. For each, check whether Erlang protects you or whether your design must
3. Favor small descriptive messages, no hardcoded topology, open data formats, and explicit failure handling

## Context & Application

Erlang's design (asynchronous messages, timeouts, links/monitors, "send events not state") naturally mitigates several fallacies — but not security, and not assumptions you bake into your own application.

## Examples

**Example** (Ch. 26): For "the network is homogeneous," the book recommends C nodes (programs implementing Erlang's protocol) or open exchange formats like BERT/BERT-RPC, rather than assuming every component speaks Erlang.

**Example** (Ch. 26): For "bandwidth is infinite," a large message can hold back heartbeats on the shared TCP connection until a node is wrongly considered unresponsive and disconnected.

## Relationships

### Builds Upon

- **Distributed-erlang** — The fallacies contextualize Erlang's distribution tools

### Related

- **Network-partition** — "The network is reliable" fallacy underlies partitions
- **Cap-theorem** — Reliability and partition assumptions lead into CAP

## Common Errors

- **Error**: Hardcoding node names, hostnames, or IP addresses.
  **Correction**: Topology changes; use registries (e.g. `global`) that abstract location.
- **Error**: Sending large messages across nodes.
  **Correction**: Large messages cost time and bandwidth and can block heartbeats; keep messages small.

## Common Confusions

- **Confusion**: Thinking Erlang's distribution layer handles all eight fallacies.
  **Clarification**: It mitigates several by design, but offers no security and cannot fix assumptions in your code.
- **Confusion**: Believing serialization is free.
  **Clarification**: Larger structures take longer to serialize and deserialize — transport cost is not zero.

## Source Reference

Chapter 26, "Distribunomicon," section "Fallacies of Distributed Computing" (including "Fallacies in a Nutshell").

## Verification Notes

- Definition: Direct adaptation from "Fallacies of Distributed Computing"
- Key Properties: All eight fallacies explicit in source
- Confidence: HIGH — the section enumerates and explains each fallacy
- Cross-references: `distributed-erlang`, `network-partition`, `cap-theorem` planned this chapter
