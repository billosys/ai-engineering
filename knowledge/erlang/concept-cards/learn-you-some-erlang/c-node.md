---
concept: C Node
slug: c-node
category: distribution
subcategory: distribution-interop
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "The Network Is Homogeneous"
extraction_confidence: medium
aliases:
  - "C node"
  - "C nodes"
  - "non-Erlang node"
prerequisites:
  - distributed-erlang
  - distributed-node
extends: []
related:
  - node-connection
contrasts_with: []
answers_questions:
  - "What is a C node?"
  - "How can a non-Erlang program join an Erlang cluster?"
  - "How does a foreign program interoperate with distributed Erlang?"
---

# C Node

## Quick Definition

A C node is a program written in C (or another language) that implements Erlang's distribution protocol and pretends to be an Erlang node, letting non-Erlang code participate in an Erlang cluster.

## Core Definition

Because all Erlang nodes assume peers speak the same protocol, foreign programs must either learn that protocol or use a translation layer (Ch. 26, "The Network Is Homogeneous"). "Learning to speak Erlang's protocol is relatively simple. If you respect the protocol, you can pretend to be another Erlang node, even if you're not writing Erlang." That is the principle behind *C nodes* — "programs that implement Erlang's protocol and then pretend they are Erlang nodes in a cluster, allowing you to distribute work without too much effort." The name says C, but nodes in other languages work the same way.

## Prerequisites

- **Distributed-erlang** — C nodes plug into the Erlang distribution layer
- **Distributed-node** — A C node behaves as a node in the cluster

## Key Properties

1. A C node is a non-Erlang program implementing Erlang's distribution protocol
2. It pretends to be an Erlang node and joins a cluster like one
3. "C node" names C but applies to any language implementing the protocol
4. It lets you distribute work to non-Erlang components without much effort
5. Erlang's distribution protocol is entirely public, making this feasible
6. An alternative to a full C node is a data-exchange format like BERT or BERT-RPC, similar to the Erlang external term format

## Construction / Recognition

### To interoperate a foreign program with Erlang

1. Implement Erlang's (public) distribution protocol in the foreign program — it becomes a C node
2. Or use a translation layer / open exchange format (XML, JSON, or BERT/BERT-RPC) instead

## Context & Application

C nodes address the "network is homogeneous" fallacy: not every component will be Erlang. The book points to the official C node tutorial and to BERT-RPC as exchange-format alternatives.

## Examples

**Example** (Ch. 26): The book's "duck" framing — "If it quacks like a duck and walks like a duck, then it must be a duck" — a foreign program respecting Erlang's protocol is treated as an Erlang node.

## Relationships

### Builds Upon

- **Distributed-erlang** — C nodes use the distribution layer
- **Distributed-node** — A C node acts as a node in the cluster

### Related

- **Node-connection** — A C node connects into the cluster like any node

## Common Errors

- **Error**: Assuming every component of a distributed Erlang system must be written in Erlang.
  **Correction**: A C node (or BERT/BERT-RPC layer) lets non-Erlang programs join.

## Common Confusions

- **Confusion**: Thinking a "C node" must be written in C.
  **Clarification**: Any language can implement Erlang's protocol; "C node" is just the conventional name.

## Source Reference

Chapter 26, "Distribunomicon," section "The Network Is Homogeneous."

## Verification Notes

- Definition: Direct adaptation from "The Network Is Homogeneous"
- Key Properties: All explicit in source
- Confidence: MEDIUM — the source describes C nodes concisely and points to external docs rather than demonstrating one
- Cross-references: `distributed-erlang`, `distributed-node`, `node-connection` planned this chapter
