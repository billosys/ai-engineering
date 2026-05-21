---
# === CORE IDENTIFICATION ===
concept: Operations, Administration, and Maintenance
slug: oam

# === CLASSIFICATION ===
category: production-ops
subcategory: operations
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Monitoring and Preemptive Support"
chapter_number: 15
pdf_page: 444
section: "Monitoring"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - OAM
  - "O&M"
  - operations and maintenance
  - OAM node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monitoring
  - semantic-node-type
extends: []
related:
  - logs
  - metrics
  - alarms
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is OAM?"
  - "What is an OAM node?"
---

# Quick Definition

OAM is the operations, administration, and maintenance functionality of a system — the configuration, management, and monitoring part — often placed in its own dedicated node.

# Core Definition

"Monitoring should be developed in conjunction with the configuration and management functionality of your system. We refer to this functionality as the operations, administration, and maintenance (OAM) part, or O&M if it does not allow you to configure and manage your business logic" (Cesarini & Vinoski, p. 445). "In the telecom world, this noncritical OAM functionality is put in its own node (or node pair for redundancy) ... namely reducing the overhead on the front-end, logic, and service nodes while increasing resilience" (p. 446).

# Prerequisites

- **Monitoring** — Monitoring is developed in conjunction with OAM; understand monitoring first.
- **Semantic node type** — The OAM node is a dedicated node type.

# Key Properties

1. The operations, administration, and maintenance functionality of a system.
2. Covers configuration, management, and monitoring; "O&M" if it excludes business-logic management.
3. Often placed in its own node (or node pair for redundancy).
4. Reduces overhead on front-end, logic, and service nodes while increasing resilience.
5. Only critical OAM functionality (a few alarms, liveness checks) is placed in non-OAM nodes.
6. The OAM node acts as a hub toward the organization's wider operations and maintenance infrastructure.

# Construction / Recognition

## To Construct/Create:
1. Build configuration, management, and monitoring functionality as the OAM part of the system.
2. Place noncritical OAM functionality in a dedicated OAM node (or redundant node pair).
3. Keep only critical OAM functionality (critical alarms, liveness checks) in other node types.
4. Connect the OAM node to the wider OAM infrastructure via standards such as SNMP/MIBs, YANG/NETCONF, or REST.

## To Identify/Recognize:
1. Recognize OAM as the inspect/manage/troubleshoot functionality that needs no Erlang knowledge to use.

# Context & Application

- **Typical contexts**: Production systems requiring operability without Erlang expertise.
- **Common applications**: Configuration changes, alarm aggregation, liveness checks; hub to tools such as Graphite, Cacti, Nagios, Chef, Splunk, or NewRelic.
- **Historical/stylistic notes**: In many Erlang systems "designed by architects who have never had to support a live system," OAM support is missing, incomplete, or bolted on (p. 446).

# Examples

**Example 1** (p. 446): If the only way to find the number of active sessions is by manually adding the size of ETS session tables across all nodes, or changing live config means calling `application:set_env`, the OAM design is wrong — all systems should let you inspect, manage, and troubleshoot without Erlang knowledge.

**Example 2** (pp. 446-447, Figure 16-1): The OAM node acts as a hub toward the wider operations and maintenance infrastructure, which also monitors the network, switches, load balancers, firewalls, hardware, OS, and stack.

# Relationships

## Builds Upon
- **Monitoring** — Monitoring is developed in conjunction with OAM
- **Semantic node type** — The OAM node is a dedicated node type

## Enables
- OAM enables operability of a system without Erlang knowledge.

## Related
- **Logs** — Collected and managed via OAM
- **Metrics** — Fed into the OAM infrastructure
- **Alarms** — Aggregated and consolidated in the OAM node

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Bolting OAM on as an afterthought
  **Correction**: Develop OAM functionality alongside monitoring from the start; it is the secret sauce of high availability.

# Common Confusions

- **Confusion**: OAM and O&M are different things.
  **Clarification**: They are the same family of functionality; the book uses "O&M" specifically when it does not allow configuring/managing business logic, and "OAM" to mean both.

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring," pages 445-447. See Figure 16-1.

# Verification Notes

- Definition source: Direct quote from p. 445.
- Confidence rationale: HIGH — the source explicitly defines OAM and the OAM node.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
