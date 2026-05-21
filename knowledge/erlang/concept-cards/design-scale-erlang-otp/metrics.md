---
# === CORE IDENTIFICATION ===
concept: Metrics
slug: metrics

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
section: "Monitoring — Metrics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - metric
  - counter
  - gauge
  - meter

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monitoring
extends: []
related:
  - logs
  - alarms
  - oam
  - system-monitor
contrasts_with:
  - logs
  - alarms

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a metric?"
  - "What are counters, gauges, meters, and histograms?"
---

# Quick Definition

Metrics are sets of numeric data collected at regular intervals and organized chronologically, obtained by polling a value at a point in time across all levels of the application stack.

# Core Definition

"Metrics are sets of numeric data collected at regular intervals and organized in chronological order. Metrics are retrieved from all levels of your application stack" — OS and network layers, the middleware layer (including the Erlang VM), and the business layer (Cesarini & Vinoski, p. 452). Earlier the book states "metrics are obtained by polling a value at a particular point in time" (p. 445). Metrics have a timestamp and are stored in a time series database optimized for timestamp-indexed data.

# Prerequisites

- **Monitoring** — Metrics are one of the three monitoring facilities; understand monitoring first.

# Key Properties

1. Sets of numeric data collected at regular intervals, organized chronologically.
2. Obtained by polling a value at a particular point in time.
3. Retrieved from all stack levels: OS/network, middleware (Erlang VM), and business layer.
4. An amount is a discrete/continuous value with increment/decrement; a counter is a common form of amount.
5. A gauge is a counter giving a value at a point in time (e.g., ongoing sessions, memory usage).
6. A meter gives an increment-only counter in a unit of time, evened out with mean rates and moving averages; a spiral is a meter with a sliding-window count.
7. Histograms group readings (often time) with statistical analysis — averages, min/max, percentiles.
8. Stored in a time series database, often aggregated and consolidated over time.

# Construction / Recognition

## To Construct/Create:
1. Identify values to poll at OS/network, middleware, and business levels.
2. Choose the metric type: counter/amount, gauge, meter/spiral, or histogram.
3. Poll at regular intervals, attaching a timestamp.
4. Store in a time series database; aggregate and consolidate over time.

## To Identify/Recognize:
1. Recognize a metric as numeric data polled at intervals and indexed by timestamp.

# Context & Application

- **Typical contexts**: Production monitoring across the whole stack.
- **Common applications**: Developers improve performance; DevOps detect abnormal behavior; operations predict trends and optimize cost; marketing studies user trends.
- **Historical/stylistic notes**: ETS tables have the atomic `ets:update_counter` operation; recommended metrics applications include folsom and exometer.

# Examples

**Example 1** (p. 452): An incremental counter `login` bumped each time someone tries to log on, with `login_success`/`login_failure` and per-failure-type counters such as `bad_password`, `unknown_user`, `user_suspended`, `userdb_error`.

**Example 2** (pp. 454-455, Figure 16-3): A counter showing the total length of all process message queues over a 12-hour period, plotted when investigating a 3:34 AM out-of-memory node crash — there was a 3-hour window the issue could have been noticed.

# Relationships

## Builds Upon
- **Monitoring** — Metrics are one of the three monitoring facilities

## Enables
- Metrics enable trend detection, performance tuning, and abnormal-behavior detection.

## Related
- **Logs** — A sibling monitoring facility
- **Alarms** — Threshold-based alarms are raised from metrics
- **OAM** — Metrics are fed into the OAM infrastructure
- **System monitor** — System-monitor events can be counted as metrics

## Contrasts With
- **Logs** — A metric is a polled numeric value; a log records a discrete state-changing event
- **Alarms** — A metric is raw numeric data; an alarm is an event raised when a metric crosses a threshold

# Common Errors

- **Error**: Using `ets:update_counter` for metrics without regard to multicore scaling
  **Correction**: ETS counters are fast but beware of global locks and bottlenecks when scaling on multicore architectures.

# Common Confusions

- **Confusion**: A gauge and a counter are the same.
  **Clarification**: A counter is an amount with increment/decrement; a gauge is a counter giving a value at a particular point in time (e.g., ongoing sessions, memory usage).

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring — Metrics," pages 452-455. See the Exometer sidebar and Figures 16-2 and 16-3.

# Verification Notes

- Definition source: Direct quote from p. 452, with the polling characterization from p. 445.
- Confidence rationale: HIGH — the source dedicates a named subsection defining metrics and all the sub-types.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
