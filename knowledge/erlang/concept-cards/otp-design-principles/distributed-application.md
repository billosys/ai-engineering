---
# === CORE IDENTIFICATION ===
concept: Distributed Application
slug: distributed-application

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
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "distributed app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-controller
  - application-configuration
extends:
  - application
related:
  - failover
  - takeover
  - distributed-application-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distributed application?"
---

# Quick Definition

A distributed application is an OTP application whose control is distributed across multiple Erlang nodes so that if the node running the application goes down, it can be restarted on another node.

# Core Definition

According to the OTP Design Principles "Distributed Applications" chapter: "In a distributed system with several Erlang nodes, it can be necessary to control applications in a distributed manner. If the node, where a certain application is running, goes down, the application is to be restarted at another node. Such an application is called a distributed application." The source makes an important distinction: "Note that it is the control of the application that is distributed. All applications can be distributed in the sense that they, for example, use services on other nodes."

# Prerequisites

- **Application** — a distributed application is an application with distributed control.
- **Application Controller** — the controller on each node participates in distributed application management.
- **Application Configuration** — distributed applications are configured via Kernel configuration parameters.

# Key Properties

1. It is the control of the application that is distributed, not the application code itself.
2. Controlled by both the application controller and a distributed application controller process (`dist_ac`), both part of Kernel.
3. Configured via the Kernel `distributed` configuration parameter.
4. Must be started by calling `application:start(Application)` at all involved nodes.
5. Runs on the first operational node listed in the `distributed` configuration.
6. If the running node goes down, the application restarts on another node (failover).
7. If a higher-priority node comes up, the application moves to it (takeover).
8. Requires an addressing mechanism (such as `global` or `pg` modules) since the application can move between nodes.
9. All involved nodes must have the same value for `distributed` and `sync_nodes_timeout`.

# Construction / Recognition

## To Construct/Create:
1. Configure the `distributed` parameter in Kernel's configuration on all participating nodes.
2. Configure `sync_nodes_mandatory`, `sync_nodes_optional`, and `sync_nodes_timeout` for node coordination.
3. Create identical (or compatible) system configuration files for each node.
4. Start all participating nodes with their configuration files.
5. Call `application:start(Application)` at all involved nodes.

## To Identify/Recognize:
1. An application listed in the Kernel `distributed` configuration parameter.
2. The `dist_ac` process is involved in managing the application.
3. The application can move between nodes via failover or takeover.

# Context & Application

Distributed applications provide high availability for critical services. When a node hosting the application fails, the application automatically restarts on a standby node. This is distinct from simply having processes communicate across nodes — distributed application control means the entire application lifecycle (start, stop, failover, takeover) is coordinated across a set of nodes.

# Examples

**Example 1** (distributed_applications.md, "Introduction"): "If the node, where a certain application is running, goes down, the application is to be restarted at another node. Such an application is called a distributed application."

**Example 2** (distributed_applications.md, "Starting and Stopping Distributed Applications"): Starting the `myapp` distributed application: "the distributed application can be started by calling `application:start(Application)` at all of these nodes." It starts on the first operational node in the priority list. "The application is started as usual. That is, an application master is created and calls the application callback function: `Module:start(normal, StartArgs)`."

**Example 3** (distributed_applications.md, "Starting and Stopping Distributed Applications"): Starting three nodes with configuration:
```text
> erl -sname cp1 -config cp1
> erl -sname cp2 -config cp2
> erl -sname cp3 -config cp3
```
When all nodes are operational, `myapp` is started at `cp1` (the highest-priority node).

# Relationships

## Builds Upon
- **Application** — a distributed application extends the application concept with distributed control.
- **Application Controller** — the controller on each node participates in coordination.
- **Application Configuration** — Kernel configuration parameters control distribution.

## Enables
- **Failover** — distributed applications enable automatic failover to standby nodes.
- **Takeover** — distributed applications enable takeover when higher-priority nodes rejoin.

## Related
- **Distributed Application Configuration** — the specific Kernel parameters that configure distribution.

## Contrasts With
- No direct contrasts in source, though the source distinguishes distributed control from distributed use of services.

# Common Errors

- **Error**: Only calling `application:start/1` on one node.
  **Correction**: The source states the application "can be started by calling `application:start(Application)` at all of these nodes." All involved nodes must call start.

- **Error**: Having different `distributed` or `sync_nodes_timeout` values on different nodes.
  **Correction**: "All involved nodes must have the same value for `distributed` and `sync_nodes_timeout`. Otherwise the system behavior is undefined."

# Common Confusions

- **Confusion**: Thinking "distributed application" means an application whose processes run on multiple nodes simultaneously.
  **Clarification**: "It is the control of the application that is distributed." The application runs on one node at a time; the distribution is about which node controls (runs) it and how failover/takeover work.

# Source Reference

OTP Design Principles, "Distributed Applications" chapter, "Introduction" and "Starting and Stopping Distributed Applications" sections (distributed_applications.md).

# Verification Notes

- Definition source: Directly quoted from distributed_applications.md "Introduction" section.
- Confidence rationale: High — explicitly defined with clear distinction between distributed control and distributed use.
- Uncertainties: None.
- Cross-reference status: References application, application-controller, application-configuration, failover, takeover, distributed-application-configuration.
