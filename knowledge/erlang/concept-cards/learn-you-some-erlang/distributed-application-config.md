---
concept: Distributed Application Configuration
slug: distributed-application-config
category: applications-releases
subcategory: distribution
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distributed OTP Applications"
chapter_number: 27
pdf_page: null
section: "Making the Application Distributed"
extraction_confidence: high
aliases:
  - "distributed kernel config"
  - "sync_nodes"
prerequisites:
  - distributed-otp-application
related:
  - application-failover
  - application-takeover
contrasts_with: []
answers_questions:
  - "How do I configure which nodes run a distributed OTP application?"
  - "What are sync_nodes_mandatory and sync_nodes_timeout?"
---

# Distributed Application Configuration

## Quick Definition

Distributed application configuration is the set of `kernel` config tuples that declare which nodes can run a distributed application, in what priority order, and how nodes synchronize at startup.

## Core Definition

To make a distributed OTP application work, each node is started with a config file that sets `kernel` parameters describing the distribution. The general structure is a `kernel` tuple containing a `distributed` entry (the application name, a restart timeout, and a node list), `sync_nodes_mandatory`/`sync_nodes_optional` lists, and a `sync_nodes_timeout`. These configuration files — not code — define which nodes are main and which are backups (Chapter 27, "Making the Application Distributed").

## Prerequisites

- **Distributed OTP application** — This configuration only has meaning for a distributed application

## Key Properties

1. The `distributed` tuple has the form `{AppName, TimeOutBeforeRestart, NodeList}`
2. `NodeList` like `[A, B, C, D]` makes `A` the main node and `B`, `C`, `D` successive backups
3. `NodeList` may group equal-priority backups: `[A, {B, C}, D]` makes `B` and `C` equal secondary backups
4. `sync_nodes_mandatory` lists nodes that must be up before this node proceeds; `sync_nodes_optional` lists nodes that may be up
5. `sync_nodes_timeout` (`MaxTime`) is the maximum time to wait for mandatory nodes; if exceeded, all nodes crash before starting
6. A VM started with these values stays locked until all mandatory nodes are up and synchronized
7. Each node typically has its own config file because its `sync_nodes_mandatory` list excludes itself
8. The application must still be started as part of the node's boot procedure for the configuration to take effect

## Construction / Recognition

## To Configure a Three-Node Distributed Application

1. Create one config file per node (e.g., `a.config`, `b.config`, `c.config`)
2. In each, put `{kernel, [{distributed, [{App, Timeout, NodeList}]}, {sync_nodes_mandatory, OtherNodes}, {sync_nodes_timeout, MaxTime}]}`
3. Set `sync_nodes_mandatory` on each node to the *other* nodes it must wait for
4. Start each node with `erl -sname <name> -config config/<name> -pa ebin/`

## Context & Application

The config files lock the VMs at startup until the cluster forms, guaranteeing all nodes synchronize before tests or services begin. The author recommends consulting the `kernel` application documentation for the full set of options, and notes that if a node cannot expect every peer to be up, some peers should be made optional rather than mandatory.

## Examples

**Example** (Chapter 27, "Making the Application Distributed"): node `a`'s config —
`[{kernel, [{distributed, [{m8ball, 5000, [a@ferdmbp, {b@ferdmbp, c@ferdmbp}]}]}, {sync_nodes_mandatory, [b@ferdmbp, c@ferdmbp]}, {sync_nodes_timeout, 30000}]}].`
Starting the third VM unlocks all three at once.

## Relationships

## Builds Upon

- **Distributed OTP application** — Configuration is what turns the plain application into a distributed one

## Related

- **Application failover** — The `TimeOutBeforeRestart` value governs the failover delay
- **Application takeover** — The node-list order defines which node is "main" and thus triggers takeover

## Common Errors

- **Error**: Setting `sync_nodes_timeout` too short for the cluster to boot
  **Correction**: All nodes crash if mandatory nodes do not appear within the timeout; increase it as needed

- **Error**: Listing the node's own name in its `sync_nodes_mandatory`
  **Correction**: Each node lists only the *other* required nodes

## Common Confusions

- **Confusion**: Thinking the node list defines where the app runs simultaneously
  **Clarification**: The list is a priority ordering; the app runs on one node, with the others as ranked backups

## Source Reference

Chapter 27: Distributed OTP Applications, section "Making the Application Distributed" (the per-node config files and the general structure template).

## Verification Notes

- Definition: Direct adaptation from the config-file discussion
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicit config examples and a generalized template are given
- Cross-references: verified against planned cards in this extraction
