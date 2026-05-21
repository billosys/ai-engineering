---
concept: Tick Time and Heartbeats
slug: tick-time
category: distribution
subcategory: distribution-failure
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Bandwidth Is Infinite"
extraction_confidence: high
aliases:
  - "heartbeat"
  - "heartbeats"
  - "tick time"
  - "net ticktime"
prerequisites:
  - node-connection
extends: []
related:
  - net-kernel
  - network-partition
contrasts_with: []
answers_questions:
  - "What are Erlang heartbeats?"
  - "What is the tick time?"
  - "How does Erlang decide a node is dead?"
---

# Tick Time and Heartbeats

## Quick Definition

Heartbeats are small messages Erlang nodes exchange at a regular interval to confirm they are alive. The tick time is the interval (heartbeat delay × 4) after which an unresponsive node is considered dead.

## Core Definition

"Erlang knows whether nodes are alive by sending *heartbeats*. Heartbeats are small messages sent at a regular interval between two nodes, basically saying, 'I'm still alive'" (Ch. 26, "Bandwidth Is Infinite"). If a node never replies, it is assumed dead and gets no future communications. Heartbeats travel over the same TCP channel as regular messages. The default heartbeat delay is 15 seconds (15,000 ms); after four failed heartbeats a remote node is considered dead, and the heartbeat delay multiplied by 4 is called the *tick time* (Ch. 26, "The net_kernel Module").

## Prerequisites

- **Node-connection** — Heartbeats run between connected nodes

## Key Properties

1. Heartbeats are small "I'm still alive" messages exchanged between nodes
2. They are sent over the same TCP connection as regular messages
3. The default heartbeat delay is 15 seconds (15,000 ms)
4. After four failed heartbeats, a remote node is considered dead
5. The tick time equals the heartbeat delay × 4
6. A large message can hold back heartbeats; too many large messages cause false node-down detection and connection closure
7. The heartbeat delay can be set via `net_kernel:start/1`'s third argument; tick time via `net_kernel:set_net_ticktime/1`

## Construction / Recognition

### To tune heartbeat behavior

1. Set the heartbeat delay at startup: `net_kernel:start([Name, Type, HeartbeatMs])`
2. Change tick time at runtime: `net_kernel:set_net_ticktime(Seconds)`
3. Raise the tick time when a node is expected to send large messages

## Context & Application

The interaction between heartbeats and large messages is a key reason the book repeatedly advises keeping inter-node messages small. Because all communications between two nodes share one TCP connection and are ordered, one large message can delay every heartbeat behind it.

## Examples

**Example** (Ch. 26): The book likens heartbeats to zombie survivors routinely pinging each other — "Bill, are you there?" — and if Bill never replies he is assumed dead and cut off from future communications.

## Relationships

### Builds Upon

- **Node-connection** — Heartbeats monitor connected nodes

### Related

- **Net-kernel** — Sets the heartbeat delay and tick time
- **Network-partition** — Missed heartbeats are how a partition is detected as a node-down

## Common Errors

- **Error**: Sending large messages without raising the tick time.
  **Correction**: Large messages delay heartbeats; raise the tick time or keep messages small to avoid false disconnections.

## Common Confusions

- **Confusion**: Thinking heartbeats travel on a separate channel.
  **Clarification**: They share the same TCP connection as regular messages, so large messages can block them.
- **Confusion**: Confusing the heartbeat delay with the tick time.
  **Clarification**: The tick time is the heartbeat delay multiplied by four.

## Source Reference

Chapter 26, "Distribunomicon," sections "Bandwidth Is Infinite" and "The net_kernel Module."

## Verification Notes

- Definition: Direct adaptation from "Bandwidth Is Infinite" and "The net_kernel Module"
- Key Properties: All explicit in source
- Confidence: HIGH — the source gives exact heartbeat and tick-time values
- Cross-references: `node-connection`, `net-kernel`, `network-partition` planned this chapter
