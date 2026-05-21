---
# === CORE IDENTIFICATION ===
concept: Failover
slug: failover

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
section: "Failover"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-application
  - distributed-application-configuration
  - application-callback-module
extends: []
related:
  - application-master
  - start-phases
contrasts_with:
  - takeover

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure distributed application failover?"
  - "What distinguishes failover from takeover in distributed applications?"
---

# Quick Definition

Failover is the automatic restart of a distributed application on another node when the node currently running the application goes down, with the new node selected according to the priority list in the `distributed` configuration.

# Core Definition

According to the OTP Design Principles "Distributed Applications" chapter: "If the node where the application is running goes down, the application is restarted (after the specified time-out) at the first operational node that is listed in the list of nodes in the `distributed` configuration parameter. This is called a failover." The application is normally started with `Module:start(normal, StartArgs)`, but if the application has `start_phases` defined, it is started with `Module:start({failover, Node}, StartArgs)` where `Node` is the terminated node.

# Prerequisites

- **Distributed Application** — failover only applies to distributed applications.
- **Distributed Application Configuration** — the `distributed` parameter defines the failover node priority and timeout.
- **Application Callback Module** — the callback module's `start/2` is called with appropriate `StartType` during failover.

# Key Properties

1. Triggered when the node running a distributed application goes down.
2. The application restarts after the timeout specified in the `distributed` configuration parameter.
3. Restarts on the first operational node in the priority list.
4. When choosing among equal-priority nodes (in a tuple), the system selects the node with the fewest running applications.
5. Normally called as `Module:start(normal, StartArgs)`.
6. If the application has `start_phases` defined, called as `Module:start({failover, Node}, StartArgs)` where `Node` is the terminated node.
7. Failover can cascade: if the failover node also goes down, the application fails over again to the next available node.

# Construction / Recognition

## To Construct/Create:
1. Configure the `distributed` parameter in Kernel with the application, timeout, and node priority list.
2. Ensure the application callback module handles `{failover, Node}` as a `StartType` if start phases are used.
3. Start the application on all participating nodes.
4. Failover happens automatically when a node goes down.

## To Identify/Recognize:
1. An application restarting on a different node after its original node went down.
2. The callback `start/2` receiving `{failover, Node}` as `StartType` (when start phases are defined).
3. A delay before restart corresponding to the configured timeout.

# Context & Application

Failover is the primary high-availability mechanism for distributed OTP applications. It ensures that critical services continue operating even when hardware or software failures take down individual nodes. The timeout parameter allows a grace period for the original node to recover before the application is moved, preventing unnecessary restarts during brief network partitions or node restarts.

# Examples

**Example 1** (distributed_applications.md, "Failover"): If `cp1` goes down, the system waits 5 seconds (the configured timeout), then restarts `myapp` on the node with fewer running applications — either `cp2` or `cp3`.

**Example 2** (distributed_applications.md, "Failover"): Cascading failover: "Suppose now that `cp2` goes also down and does not restart within 5 seconds. `myapp` is now restarted on `cp3`."

**Example 3** (distributed_applications.md, "Failover"): The callback invocation differs based on start phases:
- Without start phases: `Module:start(normal, StartArgs)`
- With start phases: `Module:start({failover, Node}, StartArgs)` where `Node` is the terminated node.

# Relationships

## Builds Upon
- **Distributed Application** — failover is a feature of distributed applications.
- **Distributed Application Configuration** — the timeout and node priority list control failover behavior.
- **Application Callback Module** — `start/2` is called during failover.

## Enables
- No further concepts — failover is an end mechanism.

## Related
- **Application Master** — a new application master is created on the failover node.
- **Start Phases** — the presence of start phases changes the `StartType` passed to `start/2` during failover.

## Contrasts With
- **Takeover** — failover happens when a node goes down (unplanned); takeover happens when a higher-priority node comes up (planned recovery). Failover uses `{failover, Node}` as StartType; takeover uses `{takeover, Node}`.

# Common Errors

- **Error**: Not handling `{failover, Node}` in the callback module when start phases are used.
  **Correction**: If the application uses start phases, the callback module must handle `{failover, Node}` as a `StartType` in `start/2`.

- **Error**: Expecting immediate failover without considering the configured timeout.
  **Correction**: The application waits for the timeout period before failing over. In the example, this is 5000ms (5 seconds).

# Common Confusions

- **Confusion**: Thinking failover preserves the application's state.
  **Clarification**: Failover restarts the application from scratch on the new node. The source shows `Module:start(normal, StartArgs)` is called — there is no state transfer. Application state persistence must be handled separately.

- **Confusion**: Confusing failover with takeover.
  **Clarification**: Failover is triggered by a node going down; takeover is triggered by a higher-priority node coming up. Failover moves the application to a lower-priority node; takeover moves it to a higher-priority node.

# Source Reference

OTP Design Principles, "Distributed Applications" chapter, "Failover" section (distributed_applications.md).

# Verification Notes

- Definition source: Directly quoted from distributed_applications.md "Failover" section.
- Confidence rationale: High — explicitly defined with clear trigger condition, behavior, and examples.
- Uncertainties: None.
- Cross-reference status: References distributed-application, distributed-application-configuration, application-callback-module, takeover, start-phases.
