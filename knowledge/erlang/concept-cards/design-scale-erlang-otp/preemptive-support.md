---
# === CORE IDENTIFICATION ===
concept: Preemptive Support and Support Automation
slug: preemptive-support

# === CLASSIFICATION ===
category: production-ops
subcategory: operations
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Monitoring and Preemptive Support"
chapter_number: 15
pdf_page: 444
section: "Preemptive Support"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - support automation
  - preemptive support automation
  - proactive support automation
  - self-support automation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monitoring
extends: []
related:
  - alarms
  - metrics
  - logs
  - oam
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is support automation?"
  - "How do I monitor a production system and provide preemptive support?"
---

# Quick Definition

Support automation is building a knowledge base that reduces service disruption by reacting to external stimuli and resolving problems before they escalate, through the analysis of metrics, events, alarms, and logs.

# Core Definition

"Support automation is the building of a knowledge base that is used to reduce service disruption by reacting to external stimuli and resolving problems before they escalate ... Automation is achieved through the collection and analysis of metrics, events, alarms, and configuration data. If certain patterns are detected in the metrics and sequence of events, a set of predefined actions are taken, preemptively trying to resolve the problem before it occurs" (Cesarini & Vinoski, p. 459). The chapter names three areas: proactive support automation (end-to-end health checks via external probes), preemptive support automation (analyzing data to predict and avert disruptions), and self-support automation (tools and libraries to diagnose and resolve problems).

# Prerequisites

- **Monitoring** — Support automation analyzes monitoring data (metrics, events, alarms, logs); understand monitoring first.

# Key Properties

1. Building a knowledge base to reduce service disruption by resolving problems before they escalate.
2. Achieved through collection and analysis of metrics, events, alarms, and configuration data.
3. Predefined actions are taken when patterns are detected.
4. Proactive support automation: reduces downtime via end-to-end health checks and external probes.
5. Preemptive support automation: gathers and analyzes data to predict disruptions before they occur.
6. Self-support automation: tools and libraries to diagnose and resolve problems, invoked by proactive/preemptive automation.
7. Need not be fully automated — DevOps analysis of logs, alarms, and metrics is valuable too.

# Construction / Recognition

## To Construct/Create:
1. Collect and analyze metrics, events, alarms, and configuration data.
2. Define patterns that predict disruption and the predefined actions to take.
3. Run external probes outside the network for proactive health checks.
4. Automate corrective actions: deleting files, reconfiguring load balancers, deploying nodes, throttling.

## To Identify/Recognize:
1. Recognize support automation by predefined corrective actions triggered automatically from monitoring data.

# Context & Application

- **Typical contexts**: Systems allowed only minutes of downtime per year.
- **Common applications**: Compressing logs on an 80% disk-full alarm; deploying nodes when capacity runs low; reconfiguring load balancers; enabling load regulation and backpressure.
- **Historical/stylistic notes**: If you are allowed only minutes of downtime per year, a corrective script must run through automation, not by waiting for a human to run it manually (p. 459).

# Examples

**Example 1** (p. 460): On an 80% disk-space alarm, automation starts compressing logs; if that does not help and a 90% alarm fires, it changes log wraparound time and shuts down noncritical logs; at 100%, it deletes anything not critical.

**Example 2** (p. 459): Lager clients send log entries asynchronously for speed, but as soon as the Lager mailbox hits a certain size the asynchronous calls are replaced by synchronous ones — an example of automated preemptive support adjusting behavior under load.

# Relationships

## Builds Upon
- **Monitoring** — Support automation analyzes monitoring data

## Enables
- Support automation enables resolving problems before they escalate, supporting five-nines availability.

## Related
- **Alarms** — Alarms trigger preemptive actions
- **Metrics** — Metric patterns predict disruptions
- **Logs** — Logs are analyzed for preemptive support
- **OAM** — Support automation is part of the OAM approach

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Detecting a problem and waiting for a human to manually run a corrective script
  **Correction**: With only minutes of downtime allowed per year, corrective scripts must run through automation.

- **Error**: Running external probes inside the firewall
  **Correction**: Make sure probes run outside your network — a defective switch can leave internal probes seeing nothing while external customers cannot access the system.

# Common Confusions

- **Confusion**: Proactive, preemptive, and self-support automation are the same.
  **Clarification**: Proactive uses external health checks to reduce downtime; preemptive analyzes data to predict disruptions; self-support is the diagnostic tooling invoked by the other two.

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Preemptive Support," pages 459-461. See the "A Needle in a Haystack" sidebar.

# Verification Notes

- Definition source: Direct quote from p. 459.
- Confidence rationale: HIGH — the source dedicates a named section defining support automation and its three areas.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
