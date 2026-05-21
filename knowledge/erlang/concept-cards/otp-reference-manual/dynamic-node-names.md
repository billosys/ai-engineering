---
# === CORE IDENTIFICATION ===
concept: Dynamic Node Names
slug: dynamic-node-names

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "Dynamic Node Name"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - dynamic node name
  - undefined node name

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-connections
  - hidden-nodes
extends:
  - erlang-node
related:
  - distribution-command-line-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a dynamic node name?"
  - "How does a node get a dynamic name?"
  - "What happens if the connection that provided the dynamic name is lost?"
---

# Quick Definition
A dynamic node name is assigned to an Erlang node that starts with its name set to `undefined`. Such a node requests a dynamic name from the first node it connects to. It operates as a hidden, non-listening, temporary client node.

# Core Definition
The Erlang Reference Manual states: "If the node name is set to _`undefined`_, the node will be started in a special mode to be the temporary client of another node. The node will then request a dynamic node name from the first node it connects to." The following distribution settings are automatically applied: `-dist_listen false -hidden -kernel dist_auto_connect never`. This means `net_kernel:connect_node/1` must be used to establish connections. "If the first established connection is closed (which gave the node its dynamic name), then any other connections will also be closed and the node will lose its dynamic node name. A new call to `net_kernel:connect_node/1` can be made to get a new dynamic node name. The node name may change if the distribution is dropped and then set up again." (Distributed Erlang chapter, "Dynamic Node Name" section).

# Prerequisites
- **erlang-node** -- Dynamic naming is an alternative to static node naming
- **node-connections** -- Connections must be established explicitly with `net_kernel:connect_node/1`
- **hidden-nodes** -- Dynamic-name nodes automatically become hidden nodes

# Key Properties
1. Node starts with name set to `undefined`
2. Requests a dynamic name from the first node it connects to
3. Automatically set to hidden mode (`-hidden`)
4. Does not listen for incoming connections (`-dist_listen false`)
5. Automatic connections are disabled (`-kernel dist_auto_connect never`)
6. Must use `net_kernel:connect_node/1` to connect
7. Losing the first connection (the one that assigned the name) causes all connections to close and the name to be lost
8. A new dynamic name can be obtained by reconnecting
9. The node name may change between connection sessions
10. Supported since Erlang/OTP 23 -- both client and peer must be OTP 23+

# Construction / Recognition
## To Construct/Create:
1. Start the node with name `undefined`: `erl -name undefined` or via `net_kernel:start/1`
2. Connect to a peer: `net_kernel:connect_node(PeerNode)`
3. The peer assigns a dynamic name

## To Identify/Recognize:
1. A node with a dynamic name can be identified by its ephemeral naming pattern
2. The node is always hidden and non-listening

# Context & Application
Dynamic node names are designed for temporary, ephemeral client nodes that need to connect to a cluster briefly without requiring a pre-assigned identity. This is useful for tools, scripts, or short-lived tasks that need distributed Erlang functionality without the overhead of permanent node setup.

**Typical contexts:**
- Short-lived scripts connecting to a running cluster
- Temporary diagnostic or debugging clients
- Automated tools that spawn many ephemeral connections
- Scenarios where unique pre-assigned names are impractical

# Examples
**Example 1** (Distributed Erlang, "Dynamic Node Name" section): Automatic settings: "In addition, these distribution settings will be set: `-dist_listen false -hidden -kernel dist_auto_connect never`"

**Example 2** (Distributed Erlang, "Dynamic Node Name" section): Connection loss behavior: "If the first established connection is closed (which gave the node its dynamic name), then any other connections will also be closed and the node will lose its dynamic node name."

# Relationships
## Builds Upon
- **erlang-node** -- Dynamic naming is an alternative node naming mode
- **node-connections** -- Connections must be explicit
- **hidden-nodes** -- Dynamic-name nodes are automatically hidden

## Enables
Nothing directly.

## Related
- **distribution-command-line-flags** -- Settings applied automatically

## Contrasts With
No direct contrasts -- dynamic naming is a mode, not an alternative to a single other concept.

# Common Errors
- **Error**: Expecting the dynamic node name to persist after the initial connection closes
  **Correction**: Losing the connection that assigned the dynamic name causes the name and all other connections to be lost. The node must reconnect to get a new name.

- **Error**: Trying to use dynamic node names with OTP versions before 23
  **Correction**: "The _dynamic node name_ feature is supported from Erlang/OTP 23. Both the temporary client node and the first connected peer node (supplying the dynamic node name) must be at least Erlang/OTP 23."

# Common Confusions
- **Confusion**: Thinking a dynamic-name node can accept incoming connections
  **Clarification**: Dynamic-name nodes are started with `-dist_listen false`, meaning they do not listen for incoming connections. All connections must be initiated by the dynamic-name node itself.

# Source Reference
Distributed Erlang chapter, "Dynamic Node Name" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- complete, self-contained section with explicit definition and version requirements
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
