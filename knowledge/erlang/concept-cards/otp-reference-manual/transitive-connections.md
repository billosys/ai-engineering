---
# === CORE IDENTIFICATION ===
concept: Transitive Connections
slug: transitive-connections

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
  - transitive node connections
  - fully connected mesh

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node-connections
extends:
  - node-connections
related:
  - hidden-nodes
  - distribution-command-line-flags
contrasts_with:
  - hidden-nodes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean that Erlang node connections are transitive?"
  - "How do you disable transitive connections?"
  - "Why would you want to disable transitive connections?"
---

# Quick Definition
By default, Erlang node connections are transitive: if node A connects to node B, and B is connected to node C, then A automatically attempts to connect to C. This creates a fully connected mesh. Transitive connections can be disabled with `-connect_all false`.

# Core Definition
The Erlang Reference Manual states: "Connections are by default transitive. If a node A connects to node B, and node B has a connection to node C, then node A also tries to connect to node C. This feature can be turned off by using the command-line flag `-connect_all false`." (Distributed Erlang chapter, "Node Connections" section).

# Prerequisites
- **node-connections** -- Transitive connections are a property of node connections

# Key Properties
1. Transitive by default -- connecting to one node connects to all its peers
2. Creates a fully connected mesh network
3. Can be disabled with `-connect_all false` command-line flag
4. Hidden nodes do not participate in transitive connections
5. When disabled, connections must be established explicitly
6. Necessary to disable when nodes in the network have different cookies

# Construction / Recognition
## Default Behavior:
Node A connects to B, B is connected to C -> A automatically connects to C.

## To Disable:
Start the node with `-connect_all false`.

## To Identify:
When `nodes/0` returns nodes you never explicitly connected to, transitive connections are in effect.

# Context & Application
Transitive connections simplify cluster setup -- connecting to a single node connects you to the entire cluster. However, this can be problematic in heterogeneous environments where not all nodes should communicate (e.g., nodes with different cookies or security domains).

**Typical contexts:**
- Default cluster behavior in homogeneous environments
- Must disable for multi-cookie environments
- Must disable for operation/maintenance nodes that should not join the full mesh

# Examples
**Example 1** (Distributed Erlang, "Node Connections" section): "Connections are by default transitive. If a node A connects to node B, and node B has a connection to node C, then node A also tries to connect to node C."

**Example 2** (Distributed Erlang, "Security" section): Why to disable: "The default when a connection is established between two nodes is to immediately connect all other visible nodes as well. [...] If there are nodes with different cookies, this method can be inappropriate [...] and the command-line flag `-connect_all false` must be set."

# Relationships
## Builds Upon
- **node-connections** -- Transitive connections extend the base connection mechanism

## Enables
Nothing directly -- transitive connections are a default behavior.

## Related
- **hidden-nodes** -- Hidden nodes are excluded from transitive connections
- **distribution-command-line-flags** -- `-connect_all false` disables transitivity

## Contrasts With
- **hidden-nodes** -- Hidden nodes must have connections set up explicitly; they are not discovered transitively

# Common Errors
- **Error**: Connecting to a node in a large cluster without realizing transitive connections will connect you to every node
  **Correction**: In large or heterogeneous environments, use `-connect_all false` to control which nodes connect.

# Common Confusions
- **Confusion**: Thinking `-connect_all false` prevents all automatic connections
  **Clarification**: It only prevents transitive (indirect) connections. Direct connections triggered by using a node's name still happen. To prevent all automatic connections, also set `-kernel dist_auto_connect never`.

# Source Reference
Distributed Erlang chapter, "Node Connections" section, with additional context from "Security" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description with clear toggling mechanism
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
