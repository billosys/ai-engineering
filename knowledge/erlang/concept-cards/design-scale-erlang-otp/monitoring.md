---
# === CORE IDENTIFICATION ===
concept: Monitoring
slug: monitoring

# === CLASSIFICATION ===
category: production-ops
subcategory: observability
tier: foundational

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
  - system monitoring
  - observability

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - logs
  - metrics
  - alarms
  - oam
  - preemptive-support
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is monitoring?"
  - "How do I monitor a production system?"
---

# Quick Definition

Monitoring is achieving visibility into what is happening in a system and the ability to act on it, done through a combination of logs, metrics, and alarms.

# Core Definition

"Your secret sauce to high availability is achieving a high level of visibility into what is going on in your system and the ability to act on the information you collect" (Cesarini & Vinoski, p. 444). "Monitoring is done using a combination of the following facilities" — logs (record state changes), metrics (poll a value at a point in time), and alarms (events associated with a state, raised and cleared by criteria) (p. 445). Monitoring serves two purposes: preemptive support and postmortem debugging.

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is the umbrella concept of chapter 15, under which logs, metrics, and alarms sit.

# Key Properties

1. Achieving visibility into what is happening in a system, plus the ability to act on it.
2. Done through a combination of logs, metrics, and alarms.
3. Serves preemptive support (early warning) and postmortem debugging.
4. Information must be stored for later access — historical data is essential.
5. Should be developed alongside the system's configuration and management (OAM) functionality.
6. Without visibility you can only guess the current state and cannot spot trends.

# Construction / Recognition

## To Construct/Create:
1. Combine logs, metrics, and alarms to capture state changes, polled values, and events.
2. Store information for later access, including historical data and crash snapshots.
3. Develop monitoring alongside the OAM functionality of the system.
4. Review the data both manually and through automation.

## To Identify/Recognize:
1. Recognize monitoring as the combined logging/metrics/alarms infrastructure that gives visibility into a live system.

# Context & Application

- **Typical contexts**: Production systems, especially those aiming for five-nines availability.
- **Common applications**: Preemptive support (catching early warning signs); postmortem debugging (state snapshots plus historical data).
- **Historical/stylistic notes**: "Errors ... won't [politely manifest themselves when you are watching]. The system will wait for your lunch or coffee break ... before crashing" (p. 444).

# Examples

**Example 1** (p. 444): Monitoring lets a DevOps team pick up early warning signs — a disk filling up triggers a housekeeping script; steadily increasing load triggers deployment of more nodes before capacity runs out.

**Example 2** (pp. 459-460, "A Needle in a Haystack"): Nodes crashed and restarted for months unnoticed because nobody monitored message queues, CPU utilization, or logs — had any been monitored, the issue would have been caught immediately.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- **Logs** — One of the three monitoring facilities
- **Metrics** — One of the three monitoring facilities
- **Alarms** — One of the three monitoring facilities
- **Preemptive support** — Built on monitoring data

## Related
- **Logs** — Record state changes
- **Metrics** — Polled numeric values
- **Alarms** — Events associated with a state
- **OAM** — Monitoring is developed alongside OAM functionality

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Bolting monitoring on as an afterthought
  **Correction**: Develop monitoring in conjunction with the system's configuration and management (OAM) functionality from the start.

# Common Confusions

- **Confusion**: Monitoring is only for postmortem debugging.
  **Clarification**: It serves both postmortem debugging and preemptive support — catching early warning signs before issues escalate.

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring," pages 444-447.

# Verification Notes

- Definition source: Synthesized from pp. 444-445; the three-facility list quoted from p. 445.
- Confidence rationale: HIGH — the source dedicates a named section to monitoring and enumerates its facilities.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
