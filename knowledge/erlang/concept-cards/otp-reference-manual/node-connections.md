---
# === CORE IDENTIFICATION ===
concept: Node Connections
slug: node-connections

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "Node Connections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - node connection
  - cluster connectivity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-naming
extends: []
related:
  - transitive-connections
  - hidden-nodes
  - epmd
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang nodes connect to each other?"
  - "When are connections established automatically?"
  - "How can a node be disconnected?"
---

# Quick Definition
Erlang nodes are loosely connected. A connection is established automatically the first time another node's name is used (e.g., via `spawn(Node, M, F, A)` or `net_adm:ping(Node)`). Connections are transitive by default. If a node goes down, its connections are automatically removed.

# Core Definition
The Erlang Reference Manual states: "The nodes in a distributed Erlang system are loosely connected. The first time the name of another node is used, for example, if `spawn(Node, M, F, A)` or `net_adm:ping(Node)` is called, a connection attempt to that node is made." The manual also states: "If a node goes down, all connections to that node are removed. Calling `erlang:disconnect_node(Node)` forces disconnection of a node." And: "The list of (visible) nodes currently connected to is returned by `nodes/0`." (Distributed Erlang chapter, "Node Connections" section).

# Prerequisites
- **erlang-node** -- Must have named nodes to connect
- **node-naming** -- Nodes must use compatible naming (all long or all short)

# Key Properties
1. Connections are established lazily -- on first use of a remote node's name
2. Connection triggers include: `spawn(Node, ...)`, `net_adm:ping(Node)`, sending messages to `{Name, Node}`
3. Connections are transitive by default (see transitive-connections)
4. If a node goes down, all connections to it are removed automatically
5. `disconnect_node(Node)` forces disconnection
6. `nodes/0` returns the list of currently connected visible nodes
7. Transitive connections can be disabled with `-connect_all false`
8. `monitor_node(Node, true)` can be used to detect when a connection is lost

# Construction / Recognition
## To Establish:
1. Use any operation that references a remote node: `spawn(Node, M, F, A)`, `{Name, Node} ! Msg`
2. Call `net_adm:ping(Node)` to explicitly connect
3. Call `net_kernel:connect_node(Node)` for explicit connection

## To Disconnect:
1. Call `erlang:disconnect_node(Node)`

## To Query:
1. `nodes/0` -- list of connected visible nodes
2. `nodes(hidden)` -- list of connected hidden nodes
3. `nodes(connected)` -- all connected nodes (visible and hidden)
4. `is_alive/0` -- whether the current runtime is a node

# Context & Application
Automatic connection establishment makes distributed Erlang systems easy to set up -- simply referencing another node causes a connection. The transitive nature means that connecting to one node in a cluster typically connects to all nodes. This creates a fully meshed network by default.

**Typical contexts:**
- Building clusters where all nodes know about each other
- Systems that grow dynamically as new nodes join
- Monitoring node health with `monitor_node/2`

# Examples
**Example 1** (Distributed Erlang, "Node Connections" section): Automatic connection: "The first time the name of another node is used, for example, if `spawn(Node, M, F, A)` or `net_adm:ping(Node)` is called, a connection attempt to that node is made."

**Example 2** (Distributed Erlang, "Node Connections" section): Forced disconnection: `erlang:disconnect_node(Node)` forces disconnection.

# Relationships
## Builds Upon
- **erlang-node** -- Connections link named nodes
- **node-naming** -- Compatible naming is required for connections

## Enables
- **transitive-connections** -- Default connection behavior is transitive

## Related
- **hidden-nodes** -- Hidden nodes do not participate in transitive connections
- **epmd** -- EPMD maps node names to addresses for connection establishment
- **distribution-bifs** -- BIFs for managing connections

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Assuming connections are permanent and never break
  **Correction**: Network issues, node crashes, or explicit disconnection remove connections. Use `monitor_node/2` to detect connection loss.

- **Error**: Forgetting that `-connect_all false` is needed when nodes have different cookies
  **Correction**: With transitive connections and different cookies, automatic connection attempts to incompatible nodes will fail. Use `-connect_all false` to manage connections explicitly.

# Common Confusions
- **Confusion**: Thinking explicit connection setup is always required
  **Clarification**: In most cases, simply using a node's name triggers automatic connection. Explicit connection via `net_adm:ping/1` is only needed when you want to connect without performing an operation.

# Source Reference
Distributed Erlang chapter, "Node Connections" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description of connection behavior
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
