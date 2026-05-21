---
# === CORE IDENTIFICATION ===
concept: Takeover
slug: takeover

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: distributed-recovery
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Distributed Applications"
chapter_number: null
pdf_page: null
section: "Takeover"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-application
  - distributed-application-configuration
  - application-callback-module
  - failover
extends: []
related:
  - application-master
contrasts_with:
  - failover

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes failover from takeover in distributed applications?"
---

# Quick Definition

Takeover is the process by which a distributed application is moved from a lower-priority node to a higher-priority node that has just started (or restarted), as determined by the node ordering in the `distributed` configuration parameter.

# Core Definition

According to the OTP Design Principles "Distributed Applications" chapter: "If a node is started, which has higher priority according to `distributed` than the node where a distributed application is running, the application is restarted at the new node and stopped at the old node. This is called a takeover." The application is started on the new node by calling `Module:start({takeover, Node}, StartArgs)` where `Node` is the old node.

# Prerequisites

- **Distributed Application** — takeover only applies to distributed applications.
- **Distributed Application Configuration** — node priority in the `distributed` parameter determines when takeover occurs.
- **Application Callback Module** — `start/2` is called with `{takeover, Node}` as `StartType`.
- **Failover** — takeover typically occurs after a previous failover moved the application to a lower-priority node.

# Key Properties

1. Triggered when a node with higher priority (according to `distributed`) starts or restarts.
2. The application is restarted at the higher-priority node and stopped at the current (lower-priority) node.
3. The callback is called as `Module:start({takeover, Node}, StartArgs)` where `Node` is the old node.
4. Takeover is initiated via `application:takeover/2`.
5. Only nodes with strictly higher priority trigger a takeover; nodes with undefined relative priority (in a tuple) do not.

# Construction / Recognition

## To Construct/Create:
1. Configure the `distributed` parameter with a clear node priority order.
2. Ensure the application callback module handles `{takeover, Node}` as a `StartType`.
3. When a higher-priority node restarts, call `application:takeover/2` to move the application.

## To Identify/Recognize:
1. An application moving from a lower-priority node to a newly started higher-priority node.
2. The callback `start/2` receiving `{takeover, Node}` as `StartType`.
3. The application being stopped on the old node after starting on the new node.

# Context & Application

Takeover complements failover to provide a complete high-availability strategy. After a failure causes an application to fail over to a standby node, takeover ensures that when the preferred node recovers, the application migrates back to it. This allows the system to automatically return to its optimal configuration after transient failures.

# Examples

**Example 1** (distributed_applications.md, "Takeover"): With `myapp` running on `cp3` (after failover from `cp1` and `cp2`), if `cp2` restarts, no takeover occurs because the order between `cp2` and `cp3` is undefined (they are in a tuple `{cp2@cave, cp3@cave}`).

**Example 2** (distributed_applications.md, "Takeover"): "However, if `cp1` also restarts, the function `application:takeover/2` moves `myapp` to `cp1`, as `cp1` has a higher priority than `cp3` for this application. In this case, `Module:start({takeover, cp3@cave}, StartArgs)` is executed at `cp1` to start the application."

**Example 3** (distributed_applications.md, "Takeover"): The configuration `[cp1@cave, {cp2@cave, cp3@cave}]` gives `cp1@cave` the highest priority. Nodes `cp2@cave` and `cp3@cave` have equal priority (undefined order within the tuple), so neither can take over from the other.

# Relationships

## Builds Upon
- **Distributed Application** — takeover is a feature of distributed applications.
- **Distributed Application Configuration** — node priority order determines takeover eligibility.
- **Application Callback Module** — `start/2` handles `{takeover, Node}`.
- **Failover** — takeover typically reverses a previous failover.

## Enables
- No further concepts — takeover is an end mechanism.

## Related
- **Application Master** — a new application master is created on the takeover node; the old one is stopped.

## Contrasts With
- **Failover** — failover is triggered by a node going down (reactive, moves to lower-priority node); takeover is triggered by a higher-priority node coming up (proactive, moves to higher-priority node). Failover uses `{failover, Node}` or `normal`; takeover uses `{takeover, Node}`.

# Common Errors

- **Error**: Not handling `{takeover, Node}` in the callback module.
  **Correction**: The callback module must pattern-match on `{takeover, Node}` in `start/2` to properly handle the takeover scenario, potentially migrating state from the old node.

- **Error**: Expecting takeover between nodes of equal priority (nodes in a tuple).
  **Correction**: Takeover only occurs when the new node has strictly higher priority. Nodes listed in a tuple in the `distributed` parameter have undefined relative order and will not trigger takeover between each other.

# Common Confusions

- **Confusion**: Thinking takeover happens automatically without `application:takeover/2`.
  **Clarification**: The source indicates that `application:takeover/2` is called to initiate the takeover when a higher-priority node restarts.

- **Confusion**: Thinking takeover transfers application state automatically.
  **Clarification**: Takeover restarts the application on the new node via `Module:start({takeover, Node}, StartArgs)`. Any state transfer must be implemented by the application itself.

- **Confusion**: Confusing takeover with failover.
  **Clarification**: Failover happens when a node goes down (the application moves to a standby); takeover happens when a preferred node comes back up (the application returns to its preferred location).

# Source Reference

OTP Design Principles, "Distributed Applications" chapter, "Takeover" section (distributed_applications.md).

# Verification Notes

- Definition source: Directly quoted from distributed_applications.md "Takeover" section.
- Confidence rationale: High — explicitly defined with examples showing when takeover does and does not occur.
- Uncertainties: None.
- Cross-reference status: References distributed-application, distributed-application-configuration, application-callback-module, failover.
