---
# === CORE IDENTIFICATION ===
concept: Node Naming
slug: node-naming

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
section: "Nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - long names
  - short names
  - node name format

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - dynamic-node-names
  - distribution-command-line-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between long names and short names?"
  - "Why can't long-name and short-name nodes communicate?"
  - "What format does a node name take?"
---

# Quick Definition
Erlang nodes use either long names (`-name`, with full hostname) or short names (`-sname`, with just the hostname prefix). The choice affects the `host` part of the `name@host` atom. Long-name and short-name nodes cannot communicate with each other.

# Core Definition
The Erlang Reference Manual states that a node name is "an atom `name@host`. `name` is the name given by the user, and consists of alphanumerics, `-`, `_`, and `\\`. `host` is the full host name if long names are used, or the first part of the host name if short names are used." The manual explicitly warns: "A node with a long node name cannot communicate with a node with a short node name." (Distributed Erlang chapter, "Nodes" section).

# Prerequisites
- **erlang-node** -- Node naming is the mechanism by which nodes get their identity

# Key Properties
1. Long names use `-name` flag: `name@fully.qualified.hostname`
2. Short names use `-sname` flag: `name@hostname`
3. Long-name nodes and short-name nodes cannot communicate -- they are incompatible
4. The `name` part is chosen by the user
5. The `host` part is determined by the system's hostname
6. Both forms produce an atom as the node name
7. All nodes in a cluster must use the same naming convention
8. Names can also be set at runtime via `net_kernel:start/1` with `shortnames` or `longnames` option

# Construction / Recognition
## To Create Long Names:
```
erl -name mynode
```
Result: `mynode@full.domain.name`

## To Create Short Names:
```
erl -sname mynode
```
Result: `mynode@hostname`

## To Set at Runtime:
```erlang
net_kernel:start([mynode, shortnames]).
net_kernel:start([mynode, longnames]).
```

# Context & Application
The choice between long and short names depends on the network environment. Short names are simpler and work well in environments where all nodes are on the same subnet or where DNS resolution of short hostnames works. Long names are required when nodes span different domains or when the full hostname is needed for unambiguous identification.

**Typical contexts:**
- Development: short names for simplicity (`erl -sname dev`)
- Production: long names for explicit addressing across domains
- Testing: short names when all nodes run on the same machine

# Examples
**Example 1** (Distributed Erlang, "Nodes" section): Long name:
```erlang
% erl -name dilbert
(dilbert@uab.ericsson.se)1> node().
'dilbert@uab.ericsson.se'
```

**Example 2** (Distributed Erlang, "Nodes" section): Short name:
```erlang
% erl -sname dilbert
(dilbert@uab)1> node().
dilbert@uab
```

# Relationships
## Builds Upon
- **erlang-node** -- Naming is how nodes get their identity

## Enables
Nothing directly -- naming is a configuration choice.

## Related
- **dynamic-node-names** -- Dynamic names are a special mode where the name is assigned by a peer
- **distribution-command-line-flags** -- `-name` and `-sname` are distribution flags

## Contrasts With
No direct contrasts -- long and short names are two options within the same concept.

# Common Errors
- **Error**: Mixing long-name and short-name nodes in a cluster
  **Correction**: All nodes must use either all long names or all short names. They cannot interoperate.

- **Error**: Expecting the hostname part to be configurable independently of the system hostname
  **Correction**: The `host` part is derived from the system's network configuration. To control it, configure the system hostname or DNS.

# Common Confusions
- **Confusion**: Thinking short names are just abbreviated long names and can still connect to long-name nodes
  **Clarification**: They are fundamentally incompatible. A short-name node and a long-name node cannot establish a connection.

# Source Reference
Distributed Erlang chapter, "Nodes" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
