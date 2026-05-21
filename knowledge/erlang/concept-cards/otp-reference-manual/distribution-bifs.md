---
# === CORE IDENTIFICATION ===
concept: Distribution BIFs
slug: distribution-bifs

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
section: "Distribution BIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - distribution built-in functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-connections
  - distributed-erlang-system
extends: []
related:
  - distributed-security
  - distribution-command-line-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What BIFs are available for distributed Erlang programming?"
  - "How do you query the current node name?"
  - "How do you list connected nodes?"
  - "How do you spawn a process on a remote node?"
---

# Quick Definition
Distribution BIFs are built-in functions for working with distributed Erlang systems, including querying node information (`node/0`, `nodes/0`, `is_alive/0`), managing connections (`disconnect_node/1`, `monitor_node/2`), handling cookies (`get_cookie/0`, `set_cookie/1,2`), and spawning remote processes (`spawn_link/2,4`, `spawn_opt/3,5`).

# Core Definition
The Erlang Reference Manual lists the following distribution BIFs:
- `disconnect_node(Node)` -- "Forces the disconnection of a node."
- `erlang:get_cookie/0` -- "Returns the magic cookie of the current node."
- `erlang:get_cookie(Node)` -- "Returns the magic cookie for node `Node`."
- `is_alive/0` -- "Returns `true` if the runtime system is a node and can connect to other nodes, `false` otherwise."
- `monitor_node(Node, Bool)` -- "Monitors the status of `Node`. A `{nodedown, Node}` message is received if the connection to it is lost."
- `node/0` -- "Returns the name of the current node. Allowed in guards."
- `node(Arg)` -- "Returns the node where `Arg`, a pid, reference, or port, is located."
- `nodes/0` -- "Returns a list of all visible nodes this node is connected to."
- `nodes(Arg)` -- "Depending on `Arg`, this function can return a list not only of visible nodes, but also hidden nodes and previously known nodes, and so on."
- `erlang:set_cookie(Cookie)` -- "Sets the magic cookie, `Cookie` to use when connecting all nodes that have no explicit cookie set."
- `erlang:set_cookie(Node, Cookie)` -- "Sets the magic cookie used when connecting `Node`."
- `spawn_link(Node, Fun)`, `spawn_link(Node, Module, Name, Args)` -- "Creates a process at a remote node."
- `spawn_opt(Node, Fun, Opts)`, `spawn_opt(Node, Module, Name, Args, Opts)` -- "Creates a process at a remote node."
(Distributed Erlang chapter, "Distribution BIFs" section).

# Prerequisites
- **erlang-node** -- BIFs operate on nodes
- **node-connections** -- BIFs manage and query connections
- **distributed-erlang-system** -- BIFs are the API for distributed programming

# Key Properties
1. Node identity: `node/0` (current node), `node/1` (node of a pid/ref/port), `is_alive/0`
2. Node listing: `nodes/0` (visible), `nodes/1` (configurable: hidden, connected, known)
3. Connection management: `disconnect_node/1`, `monitor_node/2`
4. Cookie management: `get_cookie/0,1`, `set_cookie/1,2`
5. Remote spawning: `spawn_link/2,4`, `spawn_opt/3,5`
6. `node/0` is allowed in guard expressions
7. `monitor_node/2` delivers `{nodedown, Node}` messages on connection loss

# Construction / Recognition
## Node Identity:
```erlang
node()                    %% returns current node name
node(Pid)                 %% returns node where Pid is located
is_alive()                %% true if this runtime is a node
```

## Node Listing:
```erlang
nodes()                   %% visible connected nodes
nodes(hidden)             %% hidden connected nodes
nodes(connected)          %% all connected nodes
```

## Connection Management:
```erlang
disconnect_node(Node)     %% force disconnect
monitor_node(Node, true)  %% receive {nodedown, Node} on disconnect
```

## Cookie Management:
```erlang
erlang:get_cookie()                %% current cookie
erlang:set_cookie(Cookie)          %% set default cookie
erlang:set_cookie(Node, Cookie)    %% set per-node cookie
```

## Remote Spawning:
```erlang
spawn_link(Node, fun() -> ... end)
spawn_link(Node, Module, Function, Args)
spawn_opt(Node, Module, Function, Args, [monitor])
```

# Context & Application
Distribution BIFs are the core API for building distributed Erlang applications. They provide low-level primitives that higher-level frameworks (like OTP's `global`, `pg`, and `rpc` modules) build upon.

**Typical contexts:**
- Querying cluster topology
- Monitoring node health
- Spawning processes on specific nodes for load distribution
- Managing security credentials

# Examples
**Example 1** (Distributed Erlang, "Distribution BIFs" section): The complete BIF table as listed in the source, covering identity, listing, connection, cookie, and spawn operations.

**Example 2** (Distributed Erlang, "Distribution BIFs" section): Node monitoring: "`monitor_node(Node, Bool)` -- Monitors the status of `Node`. A `{nodedown, Node}` message is received if the connection to it is lost."

# Relationships
## Builds Upon
- **erlang-node** -- BIFs query and manage nodes
- **node-connections** -- BIFs manage connections
- **distributed-erlang-system** -- BIFs are the API for distribution

## Enables
Nothing directly -- BIFs are the API layer.

## Related
- **distributed-security** -- Cookie BIFs manage authentication
- **distribution-command-line-flags** -- Some flags correspond to BIF calls (e.g., `-setcookie`)

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Using `nodes/0` and expecting to see hidden nodes
  **Correction**: `nodes/0` only returns visible nodes. Use `nodes(hidden)` for hidden nodes or `nodes(connected)` for all.

- **Error**: Forgetting that `monitor_node/2` can deliver multiple `{nodedown, Node}` messages for the same node
  **Correction**: Each call to `monitor_node(Node, true)` adds a monitor. Multiple monitors mean multiple `{nodedown, _}` messages. Call `monitor_node(Node, false)` to remove one.

# Common Confusions
- **Confusion**: Thinking `node/0` in a guard means the node identity can change during evaluation
  **Clarification**: `node/0` returns the current node's name, which does not change during the lifetime of a running node (except in the dynamic node name case). It is allowed in guards for pattern matching convenience.

# Source Reference
Distributed Erlang chapter, "Distribution BIFs" section.

# Verification Notes
- Definition source: Direct from source -- complete BIF listing reproduced
- Confidence rationale: High -- explicit table with descriptions
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
