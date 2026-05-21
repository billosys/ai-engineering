---
concept: Distributed Erlang
slug: distributed-erlang
category: distribution
subcategory: distribution-model
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "This Is My Boomstick"
extraction_confidence: high
aliases:
  - "distributed Erlang"
  - "Erlang distribution"
  - "network transparency"
prerequisites:
  - process
  - message-passing
extends: []
related:
  - distributed-node
  - node-connection
  - distributed-message-passing
  - cap-theorem
contrasts_with: []
answers_questions:
  - "What is distributed Erlang?"
  - "Why does Erlang support distribution?"
  - "What does Erlang's distribution layer provide and not provide?"
---

# Distributed Erlang

## Quick Definition

Distributed Erlang is the language's built-in layer for running many VMs (nodes) that communicate transparently over a network, extending processes and message passing across machines.

## Core Definition

Erlang's distributed layer "was first added in order to provide fault tolerance" (Ch. 26). Software on a single machine dies with that machine; software on many machines can survive hardware failure if built correctly. Distributed Erlang provides "the few basic building blocks of distribution: ways to have many nodes (VMs) communicating with each other, serializing and deserializing data in communications, extending the concepts of multiple processes to many nodes, ways to monitor network failures." It is a "tools, not solutions" approach — it tells you when parts go up or down and lets you do things over the network, but provides no silver bullet for software-specific problems like "what happens when stuff crashes."

## Prerequisites

- **Process** — Distribution extends the process model across machines
- **Message-passing** — Remote processes communicate by the same message passing as local ones

## Key Properties

1. Distribution was added primarily for fault tolerance and component redundancy
2. It provides near-complete network transparency: data structures, including pids, work the same remotely and locally
3. Messages are serialized and unserialized automatically
4. Links and monitors can be set up across the network
5. It gives tools to detect node up/down events, not solutions to crashes
6. Connecting nodes everyone-to-everyone limits scaling (one ephemeral port per node, much chatter)
7. Connected nodes remain fully independent: separate process registries, ETS tables, and loaded modules

## Construction / Recognition

### To use distributed Erlang

1. Start named nodes (VMs)
2. Connect them so they form a mesh
3. Send messages, set up links/monitors, and spawn processes across nodes as if local

## Context & Application

Erlang originally ran on telephone switches in single physical locations with failover hardware nearby — which is why the distribution layer assumes a safe, reliable, homogeneous network. The book frames distributed programming as "fighting monsters in the dark": Erlang gives you tools (a machete, flashlight, mustache) but you still face the hard problems.

## Examples

**Example** (Ch. 26): A zombie-survivor analogy — Zoey, Bill, Rick, and Daryl share walkie-talkie frequencies; when any two connect, the connections spread so everyone can reach everyone, mirroring how Erlang nodes form a full mesh.

## Relationships

### Enables

- **Distributed-node** — The unit of a distributed Erlang system
- **Node-connection** — How nodes join into a cluster
- **Distributed-message-passing** — Transparent cross-node messaging

### Related

- **Cap-theorem** — The fundamental constraint on distributed system design

## Common Errors

- **Error**: Expecting distributed Erlang to handle crashes and netsplits for you.
  **Correction**: It only provides detection tools; recovery logic is application-specific.
- **Error**: Building one giant fully-connected mesh of hundreds of nodes.
  **Correction**: Mesh connectivity does not scale well; split into smaller clusters.

## Common Confusions

- **Confusion**: Thinking distributed Erlang shares state across nodes.
  **Clarification**: Connected nodes stay fully independent — separate registries, ETS tables, and modules.
- **Confusion**: Believing remote pids behave differently from local ones.
  **Clarification**: Network transparency means pids and messages work the same locally and remotely.

## Source Reference

Chapter 26, "Distribunomicon," section "This Is My Boomstick."

## Verification Notes

- Definition: Direct adaptation from the chapter introduction and "This Is My Boomstick"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter is dedicated to distribution
- Cross-references: `distributed-node`, `node-connection`, `distributed-message-passing`, `cap-theorem` planned this chapter; `process`, `message-passing` shared slugs
