---
# === CORE IDENTIFICATION ===
concept: Distributed Erlang
slug: distributed-erlang

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.1 The fundamentals of Erlang distribution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang distribution"
  - "distributed programming in Erlang"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
  - erlang-process
extends: []
related:
  - process-communication-by-copying
  - location-transparency
  - erlang-node
  - erlang-cluster
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is distributed Erlang?"
  - "What two features make distribution easy in Erlang?"
  - "Why is Erlang's communication model a good fit for distributed programming?"
---

# Quick Definition

Distributed Erlang is Erlang's built-in support for running programs across multiple connected VM instances; it works because Erlang processes communicate only by copying data and because message destinations are location transparent.

# Core Definition

Distributed Erlang refers to Erlang's facilities for running a program across separate computers (or separate VM instances) that communicate over a network. Two fundamental features make it possible (Ch. 8, Section 8.1): *process communication by copying* — processes communicate strictly by asynchronous message passing, with the receiver effectively getting a private copy of the data, so no shared memory is involved — and *location transparency* — the send operation `!` works identically whether the recipient is local or remote, with all routing information encoded in the process identifier. Because Erlang always uses message passing and never sharing, the distributed case is practically identical to the local case, and much code can be written without regard to where processes will eventually run.

# Prerequisites

- **message-passing** — Distribution is built directly on Erlang's message-passing model.
- **process** — Distribution concerns where processes run and how they communicate.

# Key Properties

1. Built on asynchronous message passing, never shared memory.
2. Rests on two pillars: communication by copying and location transparency.
3. The distributed case is practically identical in code to the local case.
4. Enables fault tolerance — one machine crashing need not halt its neighbors.
5. Programs can be moved between one and many machines without changing communication code.
6. Networked communication introduces extra nondeterminism (delays, network failures).

# Construction / Recognition

## To Use Distributed Erlang:
1. Start Erlang VMs as named nodes (`erl -name` or `-sname`).
2. Connect nodes into a cluster (e.g., via `net_adm:ping/1`).
3. Send messages to remote processes exactly as you would locally.

## To Recognize:
1. Code sending messages to `{RegisteredName, Node}` tuples or remote pids is using distribution.

# Context & Application

- **Typical contexts**: Multi-machine systems, fault-tolerant services, scalable clusters.
- **Common applications**: Distributing a cache across web servers; resource discovery; replicated databases.
- **Historical/stylistic notes**: Solving the rewrite-to-distribute problem was a goal of Erlang's creators from the start.

# Examples

**Example 1** (Section 8.1): A Simple Cache on machine A and another on machine B — to make an insert on A available on B, A must communicate with B, which implies distribution.

**Example 2** (Section 8.1.2): The same expression `Pid ! "my message"` sends a message whether the recipient is on the local or a remote machine.

# Relationships

## Builds Upon
- **message-passing** — Distribution extends Erlang's message-passing model across the network.

## Enables
- **erlang-node** — Distribution is realized through networked nodes.
- **erlang-cluster** — Connected nodes form a cluster.

## Related
- **process-communication-by-copying** — One of the two pillars of distribution.
- **location-transparency** — The other pillar.

## Contrasts With
- None.

# Common Errors

- **Error**: Assuming a sent message will always arrive promptly as it does locally.
  **Correction**: Over a network, messages can be delayed or lost; a robust sender must be prepared for non-delivery.

# Common Confusions

- **Confusion**: Thinking you must rewrite communication code to go distributed.
  **Clarification**: Because Erlang always uses message passing, the same code works locally and distributed.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.1 "The fundamentals of Erlang distribution," Figures 8.1–8.3.

# Verification Notes

- Definition source: Synthesized from Section 8.1.
- Confidence rationale: HIGH — the book explicitly enumerates the two enabling features.
- Uncertainties: None.
- Cross-reference status: Verified; `message-passing` and `process` are owned by Agent 1.
