---
# === CORE IDENTIFICATION ===
concept: Resource Discovery Server
slug: resource-discovery-server

# === CLASSIFICATION ===
category: distribution
subcategory: resource-discovery
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.3.3 Implementing the resource discovery application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "resource_discovery module"
  - "resource discovery gen_server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resource-discovery
  - gen-server
extends: []
related:
  - resource-discovery-algorithm
  - resource-trading
  - resource-discovery-terminology
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the resource discovery application implemented?"
  - "What state does the resource discovery server hold?"
  - "What API does the resource discovery server expose?"
---

# Quick Definition

The resource discovery server is the `gen_server` (module `resource_discovery`) that runs on each node, holding the node's "I want," "I have," and discovered-resources state and exposing the discovery API.

# Core Definition

The resource discovery server is a `gen_server` implementation (module `resource_discovery`) registered locally under a fixed name on each node, so it can be addressed by name even from remote nodes. Its state record has three fields (Ch. 8, Section 8.3.3): `target_resource_types` — the "I want" list, the resource types being sought; `local_resource_tuples` — the "I have" part, a `dict` of resources present on the local node; and `found_resource_tuples` — a `dict` caching discovered resource instances matching the wanted list. It exposes API functions: `start_link/0`, `add_target_resource_type/1` and `add_local_resource/2` (asynchronous casts that store data), `fetch_resources/1` (a synchronous call returning known resources of a type), and `trade_resources/0` (a cast that triggers the discovery algorithm).

# Prerequisites

- **resource-discovery** — The server is the implementation of the resource discovery system.
- **gen_server** — The server is a `gen_server` behaviour implementation.

# Key Properties

1. Implemented as a `gen_server` in the `resource_discovery` module.
2. Registered locally under a fixed name on each node.
3. State record fields: `target_resource_types`, `local_resource_tuples`, `found_resource_tuples`.
4. Uses the `dict` module to map resource types to lists of resources.
5. API: `start_link/0`, `add_target_resource_type/1`, `add_local_resource/2`, `fetch_resources/1`, `trade_resources/0`.
6. Add/store operations are asynchronous casts; `fetch_resources` is a synchronous call.

# Construction / Recognition

## To Use the Server:
1. Start it with `start_link/0` (registers it locally by name).
2. Register target types with `add_target_resource_type/1` and local resources with `add_local_resource/2`.
3. Trigger discovery with `trade_resources/0`.
4. Retrieve discovered resources with `fetch_resources/1`.

## To Recognize:
1. A `gen_server` named `resource_discovery` with the three-field state record.

# Context & Application

- **Typical contexts**: One instance per node in a discovery-enabled cluster.
- **Common applications**: Underpinning a distributed cache's awareness of peer instances.
- **Historical/stylistic notes**: The book keeps it a single module with no supervision; a fuller OTP version exists at erlware.org.

# Examples

**Example 1** (Section 8.3.3): `init([])` returns the initial state with `target_resource_types = []`, and `local_resource_tuples`/`found_resource_tuples` as empty `dict`s.

**Example 2** (Section 8.3.3): `add_local_resource(Type, Instance)` casts `{add_local_resource, {Type, Instance}}` to the server, which stores it under the type in `local_resource_tuples`.

# Relationships

## Builds Upon
- **resource-discovery** — The server implements the discovery system.
- **gen_server** — The server is a `gen_server`.

## Enables
- **resource-trading** — `trade_resources/0` triggers the trading algorithm.

## Related
- **resource-discovery-algorithm** — The server's `handle_cast` clauses implement the algorithm.
- **resource-discovery-terminology** — The server's state holds resources, types, and tuples.

## Contrasts With
- None.

# Common Errors

- **Error**: Using `gen_server:call` between discovery servers on different nodes.
  **Correction**: Use `cast` for inter-server messages; a synchronous call risks deadlock if both servers call each other.

# Common Confusions

- **Confusion**: Thinking one global discovery server serves the whole cluster.
  **Clarification**: Each node runs its own local instance, all registered under the same name.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.3.3 "Implementing the resource discovery application."

# Verification Notes

- Definition source: Directly adapted from Section 8.3.3 code listings.
- Confidence rationale: HIGH — the book gives the full module implementation.
- Uncertainties: None.
- Cross-reference status: Verified.
