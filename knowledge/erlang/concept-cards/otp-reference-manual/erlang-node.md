---
# === CORE IDENTIFICATION ===
concept: Erlang Node
slug: erlang-node

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
  - node
  - named runtime system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang-system
extends: []
related:
  - node-naming
  - node-connections
  - hidden-nodes
  - dynamic-node-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang node?"
  - "How is a node different from a plain Erlang runtime system?"
  - "What format does a node name have?"
---

# Quick Definition
A node is an Erlang runtime system that has been given a name using the `-name` (long names) or `-sname` (short names) command-line flag. The node name is an atom in the format `name@host`.

# Core Definition
The Erlang Reference Manual states: "A _node_ is an executing Erlang runtime system that has been given a name, using the command-line flag `-name` (long names) or `-sname` (short names)." The format is: "The format of the node name is an atom `name@host`. `name` is the name given by the user, and consists of alphanumerics, `-`, `_`, and `\\`. `host` is the full host name if long names are used, or the first part of the host name if short names are used." The node name can also be set at runtime by calling `net_kernel:start/1`. A runtime system without a name reports `nonode@nohost` from `node/0`. (Distributed Erlang chapter, "Nodes" section).

# Prerequisites
- **distributed-erlang-system** -- Nodes exist within the context of distributed Erlang

# Key Properties
1. A node is an Erlang runtime system with a name
2. Node names are atoms in the format `name@host`
3. `-name` flag gives long names (full hostname): e.g., `dilbert@uab.ericsson.se`
4. `-sname` flag gives short names (first part of hostname): e.g., `dilbert@uab`
5. A node with long names cannot communicate with a node using short names
6. Node name can be set at runtime via `net_kernel:start/1`
7. An unnamed runtime system returns `nonode@nohost` from `node/0`
8. The `name` part can contain alphanumerics, `-`, `_`, and `\`

# Construction / Recognition
## To Construct/Create:
1. Start with `-name Name` for long names: `erl -name dilbert`
2. Start with `-sname Name` for short names: `erl -sname dilbert`
3. Or set at runtime: `net_kernel:start([dilbert, shortnames])`

## To Identify/Recognize:
1. `node()` returns the name of the current node
2. `is_alive()` returns `true` if the runtime system is a node
3. `nodes()` returns connected visible nodes
4. `node(Pid)` returns the node where a pid, reference, or port is located

# Context & Application
Naming a runtime system is the first step in enabling distribution. Without a name, the runtime system is isolated and cannot participate in a distributed Erlang cluster. The choice between long and short names must be consistent across all nodes in a cluster.

**Typical contexts:**
- Starting production systems as named nodes for clustering
- Development and testing with short names for convenience
- Runtime name assignment for dynamic cluster membership

# Examples
**Example 1** (Distributed Erlang, "Nodes" section): Starting with long names:
```erlang
% erl -name dilbert
(dilbert@uab.ericsson.se)1> node().
'dilbert@uab.ericsson.se'
```

**Example 2** (Distributed Erlang, "Nodes" section): Starting with short names:
```erlang
% erl -sname dilbert
(dilbert@uab)1> node().
dilbert@uab
```

**Example 3** (Distributed Erlang, "Nodes" section): Setting the name at runtime:
```erlang
% erl
1> node().
nonode@nohost
2> net_kernel:start([dilbert,shortnames]).
{ok,<0.102.0>}
(dilbert@uab)3> node().
dilbert@uab
```

# Relationships
## Builds Upon
- **distributed-erlang-system** -- Nodes are the components of a distributed system

## Enables
- **node-naming** -- Long vs. short name conventions
- **node-connections** -- Named nodes can connect to each other
- **hidden-nodes** -- Hidden nodes are a special kind of named node
- **dynamic-node-names** -- Dynamic names are assigned by a peer node

## Related
Nothing additional.

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Trying to connect a long-name node to a short-name node
  **Correction**: The source explicitly states: "A node with a long node name cannot communicate with a node with a short node name." All nodes in a cluster must use the same naming convention.

# Common Confusions
- **Confusion**: Thinking an unnamed Erlang runtime system is a node
  **Clarification**: An unnamed runtime system (returning `nonode@nohost`) is not a node and cannot participate in distribution. A name must be assigned via `-name`, `-sname`, or `net_kernel:start/1`.

# Source Reference
Distributed Erlang chapter, "Nodes" section.

# Verification Notes
- Definition source: Direct from source -- complete with examples
- Confidence rationale: High -- explicit definition with illustrative examples from the manual
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
