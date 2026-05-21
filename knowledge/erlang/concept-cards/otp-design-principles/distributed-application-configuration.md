---
# === CORE IDENTIFICATION ===
concept: Distributed Application Configuration
slug: distributed-application-configuration

# === CLASSIFICATION ===
category: distribution
subcategory: distributed-applications
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Distributed Applications"
chapter_number: null
pdf_page: null
section: "Specifying Distributed Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "distributed config"
  - "dist_ac configuration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - distributed-application
  - application-configuration
extends:
  - application-configuration
related:
  - failover
  - takeover
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure distributed application failover?"
  - "What is a distributed application?"
---

# Quick Definition

Distributed application configuration consists of Kernel configuration parameters (`distributed`, `sync_nodes_mandatory`, `sync_nodes_optional`, `sync_nodes_timeout`) that specify where a distributed application can run and how participating nodes coordinate at startup.

# Core Definition

According to the OTP Design Principles "Distributed Applications" chapter: "Distributed applications are controlled by both the application controller and a distributed application controller process called `dist_ac`. Both processes are part of the Kernel application. Distributed applications are thus specified by configuring the Kernel application." The configuration uses four key parameters: `distributed` (which nodes can run each application, with priorities and timeouts), `sync_nodes_mandatory` (nodes that must be started), `sync_nodes_optional` (nodes that can be started), and `sync_nodes_timeout` (how long to wait for other nodes).

# Prerequisites

- **Application** — the configuration is for applications.
- **Distributed Application** — this configuration enables distributed application control.
- **Application Configuration** — distributed configuration uses the same system configuration file mechanism.

# Key Properties

1. `distributed = [{Application, [Timeout,] NodeDesc}]`:
   - `Application` — atom, the application name.
   - `Timeout` — optional integer, milliseconds to wait before restarting on another node (defaults to 0).
   - `NodeDesc = [Node | {Node,...,Node}]` — node names in priority order; nodes in a tuple have undefined relative order.
2. `sync_nodes_mandatory = [Node]` — nodes that must be started within the timeout.
3. `sync_nodes_optional = [Node]` — nodes that can be started within the timeout.
4. `sync_nodes_timeout = integer() | infinity` — milliseconds to wait for other nodes.
5. All involved nodes must have the same `distributed` and `sync_nodes_timeout` values.
6. Configuration placed in system configuration files (`Name.config`) loaded with `-config Name`.
7. If not all mandatory nodes are up within the timeout, the node terminates.
8. When all mandatory nodes are up (or timeout elapses with all mandatory nodes present), applications start.

# Construction / Recognition

## To Construct/Create:
1. Create a system configuration file for each node.
2. Configure the `distributed` parameter with the application, optional timeout, and node priority list.
3. Configure `sync_nodes_mandatory` with nodes that must participate (different for each node — exclude self).
4. Configure `sync_nodes_timeout` with the same value on all nodes.
5. Start each node with `erl -sname NodeName -config ConfigFile`.

## To Identify/Recognize:
1. A system configuration file with a `kernel` section containing `distributed`, `sync_nodes_mandatory`, and `sync_nodes_timeout` keys.
2. Multiple nodes started with `-config` pointing to compatible configuration files.

# Context & Application

The distributed application configuration is the foundation for OTP's built-in high-availability mechanism. By specifying a priority-ordered list of nodes for each application, and a timeout before failover, system designers can ensure that critical applications continue running even when nodes fail. The configuration must be consistent across all participating nodes.

# Examples

**Example 1** (distributed_applications.md, "Specifying Distributed Applications"): Configuration file `cp1.config` for node `cp1@cave`:
```erlang
[{kernel,
  [{distributed, [{myapp, 5000, [cp1@cave, {cp2@cave, cp3@cave}]}]},
   {sync_nodes_mandatory, [cp2@cave, cp3@cave]},
   {sync_nodes_timeout, 5000}
  ]
 }
].
```
This specifies that `myapp` prefers `cp1@cave`, with `cp2@cave` and `cp3@cave` as equal-priority fallbacks. If `cp1` goes down, the system waits 5000ms before restarting `myapp` on the node with fewer running applications.

**Example 2** (distributed_applications.md, "Specifying Distributed Applications"): "The system configuration files for `cp2@cave` and `cp3@cave` are identical, except for the list of mandatory nodes, which is to be `[cp1@cave, cp3@cave]` for `cp2@cave` and `[cp1@cave, cp2@cave]` for `cp3@cave`."

**Example 3** (distributed_applications.md, "Specifying Distributed Applications"): The `NodeDesc` structure `[cp1@cave, {cp2@cave, cp3@cave}]` means `cp1@cave` has highest priority, while `cp2@cave` and `cp3@cave` have equal (undefined) priority relative to each other.

# Relationships

## Builds Upon
- **Distributed Application** — this configuration enables distributed application control.
- **Application Configuration** — uses the same system configuration file mechanism.

## Enables
- **Failover** — the `distributed` parameter with timeout and node priorities enables failover.
- **Takeover** — the node priority order in `distributed` determines when takeover occurs.

## Related
- **Application Controller** — the controller uses this configuration.
- **Application Configuration** — distributed configuration extends the general configuration mechanism.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Using different `distributed` values on different nodes.
  **Correction**: "All involved nodes must have the same value for `distributed` and `sync_nodes_timeout`. Otherwise the system behavior is undefined."

- **Error**: Including the node itself in its own `sync_nodes_mandatory` list.
  **Correction**: Each node's mandatory list should contain the other participating nodes, not itself.

# Common Confusions

- **Confusion**: Thinking the tuple syntax `{cp2@cave, cp3@cave}` means both nodes run the application simultaneously.
  **Clarification**: The tuple means these nodes have equal priority. Only one node runs the application; the tuple controls failover preference when the priority between these nodes is undefined.

- **Confusion**: Thinking the `Timeout` in `distributed` is the sync timeout.
  **Clarification**: The `Timeout` in the `distributed` parameter (e.g., 5000) is how long to wait before restarting the application on another node after the current node goes down. The `sync_nodes_timeout` is a separate value for how long to wait for nodes to come up at boot.

# Source Reference

OTP Design Principles, "Distributed Applications" chapter, "Specifying Distributed Applications" section (distributed_applications.md).

# Verification Notes

- Definition source: Directly from distributed_applications.md "Specifying Distributed Applications" section with all four parameters documented.
- Confidence rationale: High — all configuration parameters explicitly defined with format, semantics, and a concrete example.
- Uncertainties: None.
- Cross-reference status: References distributed-application, application-configuration, failover, takeover, application-controller.
