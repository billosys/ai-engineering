---
concept: Network Partition
slug: network-partition
category: distribution
subcategory: distribution-failure
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Dead or Dead-Alive"
extraction_confidence: high
aliases:
  - "netsplit"
  - "network partition"
  - "split-brain"
prerequisites:
  - distributed-erlang
  - node-connection
extends: []
related:
  - cap-theorem
  - distributed-node
contrasts_with: []
answers_questions:
  - "What is a network partition?"
  - "How does Erlang decide whether an unreachable node is dead?"
  - "Why is a returning living-dead node dangerous?"
---

# Network Partition

## Quick Definition

A network partition (netsplit) is a failure where parts of a distributed system can no longer communicate. There is no reliable way to tell whether an unreachable node is dead or merely cut off.

## Core Definition

The most problematic distributed-computing issue is that "there is no good way to know whether something is dead or alive (without being able to contact it)" (Ch. 26, "Dead or Dead-Alive"). When a node becomes unresponsive, you cannot distinguish a hardware failure, a crashed application, network congestion, or a downed network. Erlang made the default decision of "considering unreachable nodes as dead nodes and reachable nodes as alive" — a pessimistic approach that reacts quickly to catastrophic failure, assuming the network is less likely to fail than hardware or software. The danger is the "living dead node" that never actually died and returns with its own divergent data and connections.

## Prerequisites

- **Distributed-erlang** — Partitions are a hazard of distributed systems
- **Node-connection** — A partition is a loss of node connectivity

## Key Properties

1. A partition cuts a system so parts can no longer communicate
2. An unreachable node cannot be distinguished from a dead one without contacting it
3. Erlang's default is pessimistic: unreachable = dead, reachable = alive
4. The pessimistic choice reacts fast to catastrophic failures
5. An optimistic approach (assume nodes still alive) would delay crash measures and wait for reintegration
6. A "living dead" node — one wrongly assumed dead — can return with divergent state, causing inconsistency
7. Erlang detects nodes via heartbeats; missed heartbeats over the tick time mark a node down

## Construction / Recognition

### To reason about a partition

1. Recognize that an unresponsive node may be dead, congested, or merely isolated
2. Accept that Erlang treats unreachable nodes as dead by default
3. Design for the case where a "dead" node returns alive with conflicting data

## Context & Application

The book illustrates with a two-data-center money system: during a partition, either stop all transactions (lose availability) or allow both sides to process (a $1,000 account can be spent twice for $2,000). This dilemma motivates the CAP theorem.

## Examples

**Example** (Ch. 26): Rick can reach Bill and Zoey but not Daryl; no one can tell if Daryl was devoured by zombies, has a dead battery, is asleep, or is underground — the same dilemma a node faces with an unreachable peer.

**Example** (Ch. 26): The fog between the Chainsaw and Crossbow colonies is "the equivalent of a netsplit" — survivors can reach their own colony but the colonies cannot reach each other.

## Relationships

### Builds Upon

- **Distributed-erlang** — Partitions are inherent to distribution
- **Node-connection** — A partition is a connectivity loss between nodes

### Related

- **Cap-theorem** — Partitions force the consistency-vs-availability tradeoff
- **Distributed-node** — Nodes are what get partitioned

## Common Errors

- **Error**: Assuming an unresponsive node is definitely dead and acting irreversibly.
  **Correction**: It may be only isolated; design for its possible return with divergent state.
- **Error**: Linking/monitoring heavily across nodes and being surprised by a flood on partition.
  **Correction**: All remote links/monitors fire at once on a netsplit; use `erlang:monitor_node/2` to get one event per node instead.

## Common Confusions

- **Confusion**: Thinking "dead" in a distributed setting means "not running."
  **Clarification**: It means "cannot be reached" — the node may still be running and serving requests.
- **Confusion**: Believing Erlang resolves partitions for you.
  **Clarification**: Erlang only detects them; partition handling is application-specific.

## Source Reference

Chapter 26, "Distribunomicon," sections "Dead or Dead-Alive" and "The Network Is Reliable."

## Verification Notes

- Definition: Direct adaptation from "Dead or Dead-Alive"
- Key Properties: All explicit in source
- Confidence: HIGH — the section explains partitions and Erlang's pessimistic stance
- Cross-references: `distributed-erlang`, `node-connection`, `cap-theorem`, `distributed-node` planned this chapter
