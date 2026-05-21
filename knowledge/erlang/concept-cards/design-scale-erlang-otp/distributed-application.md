---
# === CORE IDENTIFICATION ===
concept: Distributed Application
slug: distributed-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "Distributed Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "distributed applications"
  - "application failover and takeover"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-environment
extends: []
related:
  - application-controller
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does distributed Erlang relate to scaling a system out?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A distributed application is an OTP application configured to run on one node of a cluster with a defined precedence order, automatically failing over to another node if its node goes down and being taken over by a higher-precedence node when one becomes available.

# Core Definition

OTP comes with a distribution mechanism for migrating applications across nodes (Cesarini & Vinoski, p. 221). Distributed applications are managed by the *distributed application controller* (`dist_ac` module), an instance of which runs in every distributed node's kernel supervision tree. To run a distributed application you configure environment variables in the `kernel` application — chiefly `distributed`, which lists the application, a timeout, and the node precedence order, plus `sync_nodes_mandatory`, `sync_nodes_optional`, and `sync_nodes_timeout`. If the node running the application fails, the application *fails over* to the next node in the precedence list; if a higher-precedence node appears, the application is migrated to it in a *takeover* (pp. 221-225).

# Prerequisites

- **OTP application** — A distributed application is an OTP application with distribution configured.
- **Application environment** — Distribution is configured through `kernel` environment variables.

# Key Properties

1. Configured via `kernel` environment variables, not application code.
2. `distributed` lists `{App, Timeout, NodePrecedence}`.
3. *Failover* — when the running node fails, the application moves to the next node in precedence.
4. *Takeover* — when a higher-precedence node appears, the application migrates back to it.
5. `sync_nodes_mandatory` nodes must all be up for the system to start; `sync_nodes_optional` nodes need not be.
6. Nodes grouped in a tuple share the same precedence.
7. The mechanism assumes reliable networks and is a stopgap, not a no-single-point-of-failure design.

# Construction / Recognition

## To Construct/Create:
1. Create a config file setting the `kernel` `distributed`, `sync_nodes_mandatory`, `sync_nodes_optional`, and `sync_nodes_timeout` variables.
2. Start each node with that config file (`erl -config dist ...`).
3. Start `sasl` and the application on the nodes; the supervision tree runs only on the highest-precedence node.

## To Identify/Recognize:
1. A `kernel` config with a `distributed` entry for the application.
2. The application's supervision tree runs on only one node at a time.

# Context & Application

- **Typical contexts**: Small clusters needing a single running instance of an application with automatic relocation.
- **Common applications**: Migrating a stateful service across a handful of nodes.
- **Historical/stylistic notes**: The book calls it a limited approach and warns: pick mandatory nodes with care, and for a true no-single-point-of-failure design do not require any node to be up (p. 225).

# Examples

**Example 1** (p. 222): A `dist.config` distributing `bsc` across four nodes with `[n1@localhost,{n2@localhost,n3@localhost},n4@localhost]` precedence — `n2` and `n3` share precedence.

**Example 2** (pp. 224-225): Shell walkthrough showing the `bsc` tree starting only on `n1`, failing over to `n2`/`n3` when `n1` halts, and being taken over again when `n1` returns.

## Worked Example

The `dist.config` distributing the `bsc` application (p. 222):

```erlang
[{kernel, [{distributed, [{bsc, 1000, [n1@localhost,
                                       {n2@localhost,n3@localhost},
                                       n4@localhost]}]},
           {sync_nodes_mandatory, [n1@localhost]},
           {sync_nodes_optional, [n2@localhost,n3@localhost,n4@localhost]},
           {sync_nodes_timeout, 15000}]},
 {bsc, [{frequencies, [1,2,3,4,5,6]}]}].
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Application controller** — Distributed applications are handled by the related `dist_ac` distributed application controller.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Designating too many nodes as `sync_nodes_mandatory`.
  **Correction**: Pick mandatory nodes carefully; the system will not start unless every mandatory node is up.

- **Error**: Relying on distributed applications for a no-single-point-of-failure design.
  **Correction**: It is a stopgap assuming reliable networks; do failover/takeover prerequisite checks in start phases or worker processes.

# Common Confusions

- **Confusion**: Thinking a distributed application runs on all nodes simultaneously.
  **Clarification**: It runs on one node at a time — the highest-precedence available node; other nodes only stand by for failover.

# Source Reference

Chapter 8: Applications, "Distributed Applications," pages 221-225. See Figures 9-8 to 9-10 (failover and takeover).

# Verification Notes

- Definition source: Direct adaptation from pp. 221-225.
- Confidence rationale: HIGH — explicitly defined with the `dist.config` file and a detailed failover/takeover walkthrough.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
