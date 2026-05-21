---
concept: EPMD (Erlang Port Mapper Daemon)
slug: epmd
category: distribution
subcategory: distribution-infrastructure
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
  - "EPMD"
  - "Erlang Port Mapper Daemon"
  - "epmd"
prerequisites:
  - distributed-node
extends: []
related:
  - node-connection
contrasts_with: []
answers_questions:
  - "What is EPMD?"
  - "How do nodes find each other by name?"
  - "Which port does EPMD use?"
---

# EPMD (Erlang Port Mapper Daemon)

## Quick Definition

EPMD is the Erlang Port Mapper Daemon — a name server that runs on each computer in an Erlang cluster, letting nodes register and contact each other by name rather than port number.

## Core Definition

When you start a node, "it will connect to an application called Erlang Port Mapper Daemon (EPMD), which will run on each of the computers that are part of your Erlang cluster" (Ch. 26, "This Is My Boomstick"). EPMD "acts as a name server that lets nodes register themselves, contact other nodes by name rather than port numbers, and warn you about any name clashes." It listens on port 4369, the default port officially registered for EPMD by Ericsson.

## Prerequisites

- **Distributed-node** — EPMD maps node names; a node connects to EPMD on startup

## Key Properties

1. EPMD runs on each computer participating in the cluster
2. A starting node connects to EPMD automatically
3. EPMD acts as a name server: nodes register, then contact others by name not port
4. EPMD warns about name clashes
5. EPMD listens on port 4369 — the port officially registered for it by Ericsson
6. To go through a firewall, port 4369 should be opened, plus a range of ports for inter-node connections

## Construction / Recognition

### To work with EPMD across a firewall

1. Open port 4369 for EPMD
2. Open a range of ports for inter-node connections, configured with the `kernel` application variables `inet_dist_listen_min` and `inet_dist_listen_max`
3. Each node needs only one listen port per machine

## Context & Application

EPMD is the infrastructure that makes node-by-name addressing possible. Because Erlang assigns random inter-node ports by default, EPMD plus a configured port range is needed for firewalled deployments.

## Examples

**Example** (Ch. 26): Configuring the inter-node port range so connections are firewall-friendly —

```erlang
[{kernel,[
  {inet_dist_listen_min, 9100},
  {inet_dist_listen_max, 9115}
]}].
```

started with `erl -name the_army_of_darknodes -config ports`.

## Relationships

### Builds Upon

- **Distributed-node** — EPMD resolves node names

### Related

- **Node-connection** — EPMD enables nodes to locate each other before connecting

## Common Errors

- **Error**: Opening only the inter-node port range through a firewall but not port 4369.
  **Correction**: EPMD needs port 4369; without it nodes cannot resolve names.
- **Error**: Relying on default random inter-node ports behind a firewall.
  **Correction**: Set `inet_dist_listen_min`/`inet_dist_listen_max` to confine ports to a known range.

## Common Confusions

- **Confusion**: Thinking EPMD carries the actual inter-node traffic.
  **Clarification**: EPMD is a name/port mapper; node-to-node messages travel over separately negotiated connections.
- **Confusion**: Believing one EPMD serves the whole cluster.
  **Clarification**: EPMD runs on each computer in the cluster.

## Source Reference

Chapter 26, "Distribunomicon," sections "This Is My Boomstick" and "The Walls Are Made of Fire, and the Goggles Do Nothing."

## Verification Notes

- Definition: Direct adaptation from "This Is My Boomstick"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter defines EPMD and its port clearly
- Cross-references: `distributed-node`, `node-connection` planned this chapter
