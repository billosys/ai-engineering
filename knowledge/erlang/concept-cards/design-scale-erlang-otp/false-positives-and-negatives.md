---
# === CORE IDENTIFICATION ===
concept: False Positives and False Negatives in Alarms
slug: false-positives-and-negatives

# === CLASSIFICATION ===
category: production-ops
subcategory: observability
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Monitoring and Preemptive Support"
chapter_number: 15
pdf_page: 444
section: "Monitoring — Alarms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - false positive
  - false negative
  - alarm tuning

# === TYPED RELATIONSHIPS ===
prerequisites:
  - alarms
extends: []
related:
  - metrics
  - preemptive-support
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a false positive alarm?"
  - "What is a false negative alarm?"
---

# Quick Definition

A false positive is an alarm generated for a nonissue; a false negative is a missed alarm that should have been raised. Both must be managed by fine-tuning the alarm system.

# Core Definition

"A false positive is an alarm generated because of a nonissue. It could be caused by an overly sensitive threshold or even paranoid management asking you to monitor too much" (Cesarini & Vinoski, p. 458). "A false negative is when alarms should have been raised, but are not. This could be because of threshold configuration or lack of coverage in particular parts of the system" (pp. 458-459). Both are managed by configuring and fine-tuning alarms once the system is live.

# Prerequisites

- **Alarms** — False positives and negatives are alarm-tuning concepts; understand alarms first.

# Key Properties

1. A false positive is an alarm raised for a nonissue.
2. False positives are caused by overly sensitive thresholds or excessive monitoring.
3. Too many false positives cause serious alarms to be ignored.
4. A false negative is a missed alarm that should have been raised.
5. False negatives are caused by threshold misconfiguration or lack of coverage.
6. Both are managed by fine-tuning the alarm system once it is live.

# Construction / Recognition

## To Construct/Create:
This is a tuning concern, not an artifact. To manage them:
1. Eliminate false positives by adjusting overly sensitive thresholds.
2. Manage false negatives by reviewing, after every failure, which alarms could have been raised.
3. Start monitoring events that indicate imminent failure or service degradation.

## To Identify/Recognize:
1. A false positive fires when nothing is wrong; a false negative fails to fire when something is wrong.

# Context & Application

- **Typical contexts**: Fine-tuning a live monitoring system.
- **Common applications**: Adjusting disk-full thresholds; adding alarm coverage after a postmortem.
- **Historical/stylistic notes**: The same threshold (e.g., 70% disk full) can be a false positive on a slow-filling disk and a genuine warning on a fast-filling one — context decides.

# Examples

**Example 1** (p. 458): On a slowly filling disk, a 70% disk-full alarm could be active for months with no need for intervention (a false positive), while on a fast-filling disk the same alarm warrants waking someone in the middle of the night.

**Example 2** (pp. 458-459): After every failure or degradation of service, review which alarms could have been raised and start monitoring events indicating that failure or degradation is imminent — managing false negatives.

# Relationships

## Builds Upon
- **Alarms** — False positives/negatives are properties of an alarm system

## Enables
- Managing false positives and negatives enables a trustworthy alarm system.

## Related
- **Metrics** — Threshold-based alarm tuning depends on metric thresholds
- **Preemptive support** — Well-tuned alarms feed preemptive support automation

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Leaving overly sensitive thresholds in place
  **Correction**: Eliminate false positives; too many of them cause serious alarms to be ignored.

# Common Confusions

- **Confusion**: A false positive and a false negative are the same kind of mistake.
  **Clarification**: A false positive raises an alarm for a nonissue; a false negative fails to raise an alarm when there is a real issue.

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring — Alarms," pages 458-459.

# Verification Notes

- Definition source: Direct quotes from pp. 458-459.
- Confidence rationale: HIGH — the source explicitly defines both false positives and false negatives.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
