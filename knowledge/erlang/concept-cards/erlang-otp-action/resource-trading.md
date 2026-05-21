---
# === CORE IDENTIFICATION ===
concept: Resource Trading
slug: resource-trading

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
  - "trade_resources"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resource-discovery-server
  - resource-discovery-algorithm
extends: []
related:
  - inter-node-messaging
  - process-communication-by-copying
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is resource trading?"
  - "How does trade_resources broadcast and reply work?"
---

# Quick Definition

Resource trading is the broadcast-and-reply exchange triggered by `trade_resources/0`: a node sends its local resources to every discovery server in the cluster, and each replies with its own, until all nodes are synchronized.

# Core Definition

Resource trading is the operation that drives the resource discovery algorithm. The API function `trade_resources/0` sends a simple cast (the atom `trade_resources`) to the local discovery server. The server then broadcasts a message of the form `{trade_resources, {node(), ResourceTuples}}` asynchronously to the discovery server on every connected node — including the local node itself, for a symmetry that updates the local list without extra code. Each receiving server checks the sender's resources against its "I want" list, caches the matching ones, and replies with a message of the same shape but using the atom `noreply` in place of the sender's node name, to indicate no further reply is needed (otherwise messages would bounce forever). After the originating server has received and handled all replies, every node holds the same matching information. Because trading uses only asynchronous casts between servers, it avoids the deadlock risk a synchronous call between mutually calling servers would create (Ch. 8, Section 8.3.3).

# Prerequisites

- **resource-discovery-server** — Trading is an operation of the discovery server.
- **resource-discovery-algorithm** — Trading is how the algorithm is executed.

# Key Properties

1. Triggered by the `trade_resources/0` API cast.
2. Broadcasts `{trade_resources, {node(), ResourceTuples}}` to all connected discovery servers.
3. Includes the local node in the broadcast for symmetry.
4. Replies reuse the message shape but tag with `noreply` to stop bouncing.
5. Uses asynchronous `gen_server:cast` to avoid inter-server deadlock.
6. After all replies, every node has consistent matching information.

# Construction / Recognition

## How Trading Works:
1. `trade_resources/0` casts `trade_resources` to the local server.
2. The server broadcasts its local resources to all `[node() | nodes()]` discovery servers.
3. Each receiver caches matching resources and replies, tagging the reply `noreply`.
4. The originator handles all replies; the cluster is now synchronized.

## To Recognize:
1. A `gen_server:cast({Server, Node}, {trade_resources, ...})` broadcast over `nodes()`.

# Context & Application

- **Typical contexts**: Synchronizing a node with the cluster after it joins.
- **Common applications**: A cache calling `trade_resources()` at startup to find peer caches.
- **Historical/stylistic notes**: The book notes the missing piece is automatic triggering of trading (e.g., from a supervisor) so it need not be called manually.

# Examples

**Example 1** (Section 8.3.3): The `handle_cast(trade_resources, State)` clause builds `AllNodes = [node() | nodes()]` and casts `{trade_resources, {node(), ResourceTuples}}` to each.

**Example 2** (Section 8.3.3): The reply has the same shape as the broadcast but uses the atom `noreply` instead of a node name, so messages do not bounce back and forth forever.

# Relationships

## Builds Upon
- **resource-discovery-server** — Trading is implemented in the server's `handle_cast` clauses.
- **resource-discovery-algorithm** — Trading executes the discovery algorithm.

## Enables
- None.

## Related
- **inter-node-messaging** — Trading messages are sent to registered servers on remote nodes.
- **process-communication-by-copying** — A whole `dict` can be sent as-is because of copy semantics.

## Contrasts With
- None.

# Common Errors

- **Error**: Replying to a trade message with a node name instead of `noreply`.
  **Correction**: Tag replies with `noreply` so the exchange terminates instead of bouncing forever.

# Common Confusions

- **Confusion**: Thinking trading must use synchronous calls to be reliable.
  **Clarification**: It deliberately uses asynchronous casts; synchronous calls between mutually trading servers would deadlock.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.3.3 "Implementing the resource discovery application," subsection "Fetching and trading information" and the "Using cast between servers" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 8.3.3.
- Confidence rationale: HIGH — the book gives the trading code and explains the message shapes.
- Uncertainties: None.
- Cross-reference status: Verified.
