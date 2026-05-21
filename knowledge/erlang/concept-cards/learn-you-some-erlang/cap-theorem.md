---
concept: CAP Theorem
slug: cap-theorem
category: distribution
subcategory: distribution-theory
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "My Other Cap Is a Theorem"
extraction_confidence: high
aliases:
  - "CAP theorem"
  - "CAP"
  - "Brewer's theorem"
prerequisites:
  - network-partition
  - distributed-erlang
extends: []
related:
  - network-partition
contrasts_with: []
answers_questions:
  - "What is the CAP theorem?"
  - "What are consistency, availability, and partition tolerance?"
  - "Why can't a distributed system have all three CAP properties?"
---

# CAP Theorem

## Quick Definition

The CAP theorem states that a distributed system has three core attributes — consistency, availability, and partition tolerance — and can guarantee only two of them at once.

## Core Definition

"There is sadly no way to keep an application alive and correct at the same time during a netsplit. This idea is known as the *CAP theorem*" (Ch. 26, "My Other Cap Is a Theorem"). The theorem states there are three core attributes to all distributed systems: **c**onsistency, **a**vailability, and **p**artition tolerance. **Consistency** means all operations look as if completed as a single indivisible block, even across many nodes — every node reports the same value. **Availability** means a non-dead node always returns a response (a "sorry, I'm dead" is not a real response). **Partition tolerance** means the system keeps working with useful data even when components cannot communicate. You can have only two: CA, CP, or AP — never all three.

## Prerequisites

- **Network-partition** — The theorem is fundamentally about behavior during partitions
- **Distributed-erlang** — CAP constrains the design of any distributed Erlang system

## Key Properties

1. Three attributes: consistency, availability, partition tolerance
2. Only two of the three can be guaranteed simultaneously: CA, CP, or AP
3. Consistency: all operations appear atomic and indivisible across nodes
4. Availability: a non-dead node always returns a usable response
5. Partition tolerance: the system keeps working despite lost messages between components
6. CA is usually dismissed — it requires assuming the network never fails (or fails atomically)
7. During a netsplit a system can be available or consistent, but not both
8. A quorum system turns the AP/CP choice into a dial: require M of N nodes to agree

## Construction / Recognition

### To apply the CAP theorem to a design

1. Accept that the network can partition, so failure must be an option (rules out pure CA)
2. Choose CP (stop modifications to stay consistent) or AP (allow divergent versions to stay available)
3. For AP, pick a conflict-resolution strategy (last write wins, random winner, logical/vector clocks, or push to the application)
4. Optionally use a quorum (M of N) to tune how much consistency you want, even per-query

## Context & Application

The book notes the practical value: if a customer demands all three, you can tell them it is "literally impossible." Some systems choose neither A nor C (favoring throughput/latency), and some relax consistency only during netsplits.

## Examples

**Example** (Ch. 26): The Chainsaw/Crossbow colonies during the fog (a netsplit). Under CP, Bill and Zoey are denied the right to change the meeting time, keeping data consistent. Under AP, each side keeps its own version (`Chainsaw: Friday night`, `Crossbow: Friday before dawn`), staying available but diverging.

## Relationships

### Builds Upon

- **Network-partition** — CAP describes the tradeoff forced by partitions

### Related

- **Network-partition** — AP systems must resolve the divergent data partitions cause

## Common Errors

- **Error**: Promising a system that is consistent and available during partitions.
  **Correction**: The CAP theorem makes that impossible; choose CP or AP.
- **Error**: Treating the AP/CP choice as a binary switch.
  **Correction**: A quorum system makes it a dial — set M of N required nodes, even per-query.

## Common Confusions

- **Confusion**: Thinking a "sorry, I can't answer" reply counts as availability.
  **Clarification**: Such a reply carries no useful information; it is not a real response.
- **Confusion**: Believing CA is a realistic choice.
  **Clarification**: CA requires assuming the network never fails or fails atomically — usually dismissed.

## Source Reference

Chapter 26, "Distribunomicon," section "My Other Cap Is a Theorem" (Consistency, Availability, Partition Tolerance, Zombie Survivors and CAP).

## Verification Notes

- Definition: Direct adaptation from "My Other Cap Is a Theorem"
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines CAP and each attribute precisely
- Cross-references: `network-partition`, `distributed-erlang` planned this chapter
