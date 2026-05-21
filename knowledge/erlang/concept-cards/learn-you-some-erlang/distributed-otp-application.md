---
concept: Distributed OTP Application
slug: distributed-otp-application
category: applications-releases
subcategory: distribution
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distributed OTP Applications"
chapter_number: 27
pdf_page: null
section: "Adding More to OTP"
extraction_confidence: high
aliases:
  - "distributed application"
prerequisites:
  - otp-application
  - distributed-erlang
  - distributed-node
related:
  - distributed-application-config
  - erlang-release
extends:
  - otp-application
contrasts_with: []
answers_questions:
  - "What is a distributed OTP application?"
  - "How does an OTP application relate to distribution across nodes?"
---

# Distributed OTP Application

## Quick Definition

A distributed OTP application is an OTP application that defines takeover and failover mechanisms across a cluster of nodes, so it can be restarted on a backup node when the node running it dies.

## Core Definition

A distributed OTP application (or just "distributed application" in the OTP context) is a normal OTP application augmented so that OTP can move it between nodes for fault tolerance. In standard applications, the application controller dispatches to application masters; in distributed applications, the controller shares its work with a *distributed application controller* process (usually called `dist_ac`), which runs on every node and communicates with its peers. Distributed applications split the started state into *started* and *running*: a global distributed application is started on all nodes of a cluster but runs on only one node at a time. The non-running nodes simply wait for the running node to die so one of them can take over (Chapter 27, "Adding More to OTP").

## Prerequisites

- **OTP application** — A distributed application is an ordinary OTP application with extra configuration; you must know how to build the plain application first
- **Distributed Erlang** — Takeover/failover require nodes that are connected and can communicate
- **Distributed node** — The mechanism operates over named nodes that form a cluster

## Key Properties

1. Adds a `dist_ac` process per node alongside the standard application controller
2. Application state is refined: *started* (loaded and started on a node) vs. *running* (actively executing — only one node at a time for a global app)
3. Provides two recovery behaviors: failover and takeover
4. Assumes failures are hardware failures, not netsplits — risky in netsplit-prone networks (both backup and main could run the app)
5. Requires the application to be started as part of the node's boot procedure for the mechanism to work
6. Turning a normal application into a distributed one requires no code change beyond an extra `start/2` clause and configuration files
7. OTP makes no special provision for preserving state across moves — that is the developer's responsibility

## Construction / Recognition

## To Build a Distributed OTP Application

1. Build a normal OTP application (callback module, supervisor, app file)
2. Add a `start({takeover, OtherNode}, [])` clause to the application callback module's `start/2`
3. Write per-node config files declaring the `distributed`, `sync_nodes_mandatory`/`sync_nodes_optional`, and `sync_nodes_timeout` kernel parameters
4. Start each node with `-config` pointing at its config file, and start the application as part of node boot (e.g., via `-eval` or a release boot script)

## Context & Application

Distributed OTP applications are useful when you have redundant hardware and want a service to migrate from a failed main server to a backup. The chapter's `m8ball` (Magic 8 Ball) example runs on three nodes (`a`, `b`, `c`): node `a` is the main node, `b` and `c` are backups. The author notes that for many applications it is simpler to run many synchronized instances at once rather than force single-node execution; distributed OTP applications are most worthwhile when a true failover/takeover mechanism is genuinely needed, and they work best in combination with releases.

## Examples

**Example** (Chapter 27, "The Magic 8 Ball"): The `m8ball` application runs on nodes `a@ferdmbp`, `b@ferdmbp`, `c@ferdmbp`. Killing node `a` causes `b` to start running the app after the configured timeout; killing `b` moves it to `c`; restarting `a` triggers a takeover back to `a`.

## Relationships

## Builds Upon

- **OTP application** — A distributed application is an OTP application plus distribution configuration

## Related

- **Distributed application config** — The kernel config tuples that declare node priorities and synchronization
- **Erlang release** — Distributed OTP applications work best when packaged as releases that place all parts of the system correctly

## Contrasts With

- **Application failover** and **application takeover** — The two recovery operations a distributed application provides (see those cards)

## Common Errors

- **Error**: Starting the application manually from the shell after boot and expecting failover to work
  **Correction**: The application must be started *as part of the node's boot procedure* (e.g., `erl ... -eval 'application:start(m8ball)'` or a release boot script)

- **Error**: Assuming OTP preserves application state when it migrates
  **Correction**: OTP does not; you must explicitly share or persist vital state before failover happens

## Common Confusions

- **Confusion**: Thinking a distributed application runs on every node simultaneously
  **Clarification**: A global distributed application is *started* on all nodes but *running* on only one; the others wait

- **Confusion**: Believing distributed OTP applications protect against any failure
  **Clarification**: They assume hardware failure, not netsplits; during a netsplit the app may run as both main and backup

## Source Reference

Chapter 27: Distributed OTP Applications, sections "Adding More to OTP," "Taking and Failing Over," and "The Magic 8 Ball."

## Verification Notes

- Definition: Direct adaptation from "Adding More to OTP"
- Key Properties: Items 1-5 explicit in the chapter; items 6-7 synthesized from the m8ball walkthrough and the closing discussion
- Confidence: HIGH — the source explicitly defines and demonstrates the concept
- Cross-references: `otp-application`, `erlang-release`, `distributed-erlang`, `distributed-node` are shared slugs from other agents
