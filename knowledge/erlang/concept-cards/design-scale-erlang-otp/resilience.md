---
# === CORE IDENTIFICATION ===
concept: Resilience
slug: resilience

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: availability-properties
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Resilience"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - resilient system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - availability
extends: []
related:
  - fault-tolerance
  - reliability
  - back-off-algorithm
contrasts_with:
  - fault-tolerance
  - reliability

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is resilience?"
  - "How does a system recover quickly from failure?"
---

# Quick Definition

Resilience is the ability of a system to recover quickly from failure — for example, a node restarting after a crash or a redundant network kicking in.

# Core Definition

"Resilience is the ability of a system to recover quickly from failure" (Cesarini & Vinoski, p. 404). The trick "is to isolate failure, separating the business logic from the error handling. If a process crashes, its dependencies are terminated and quickly restarted. If a node goes down, a heartbeat script triggers an immediate restart. If a network or hardware outage occurs, the redundant network is used" (p. 405).

# Prerequisites

- **Availability** — Resilience is one of the concepts availability encompasses; understand availability first.

# Key Properties

1. The ability to recover quickly from failure.
2. Achieved by isolating failure and separating business logic from error handling.
3. A crashed process has its dependencies terminated and is quickly restarted.
4. A downed node is restarted by a heartbeat script.
5. A network/hardware outage triggers use of a redundant network.
6. Nodes that do too much have more failure causes and longer recovery times.

# Construction / Recognition

## To Construct/Create:
1. Isolate functionality in manageable quantities across different node types.
2. Separate business logic from error handling.
3. Use heartbeat scripts to detect node failure and trigger restarts (or machine reboots).
4. Provide redundant networks and hardware.

## To Identify/Recognize:
1. A system is resilient if, after a failure, it recovers on its own with minimal downtime.

# Context & Application

- **Typical contexts**: Systems requiring high availability with minimal recovery time.
- **Common applications**: Process restarts under supervision, node restarts via heartbeat, redundant-network failover.
- **Historical/stylistic notes**: A heartbeat script may decide, based on the number of restarts in the last hour, whether to restart the process or reboot the whole machine (p. 404).

# Examples

**Example 1** (pp. 404-405, Figure 14-2): A web server node crashes before handling a request; a heartbeat script detects the failure and restarts the process or reboots the machine; once back up, the repeatedly failing client request is finally accepted and handled.

**Example 2** (p. 405): If a node does too much, you increase the possible causes of a crash through complexity and increase the recovery time — arguing for small, isolated node types.

# Relationships

## Builds Upon
- **Availability** — Resilience is a component of availability

## Enables
- Resilience enables minimal downtime through fast self-recovery.

## Related
- **Fault tolerance** — A sibling component of availability
- **Reliability** — A sibling component of availability
- **Back-off algorithm** — Clients reconnecting after recovery should use back-off to avoid surges

## Contrasts With
- **Fault tolerance** — Resilience is recovering quickly from failure; fault tolerance is acting predictably during it
- **Reliability** — Resilience is fast recovery; reliability is continued correct function under predefined conditions

# Common Errors

- **Error**: Building one node that does too much
  **Correction**: Complexity multiplies crash causes and lengthens recovery; isolate functionality in small node types.

# Common Confusions

- **Confusion**: Resilience means a system never fails.
  **Clarification**: Resilience means it recovers quickly after failure — failure still occurs but downtime is minimized.

# Source Reference

Chapter 13: Systems That Never Stop, "Resilience," pages 404-406. See Figure 14-2.

# Verification Notes

- Definition source: Direct quote from p. 404.
- Confidence rationale: HIGH — the source explicitly defines resilience.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
