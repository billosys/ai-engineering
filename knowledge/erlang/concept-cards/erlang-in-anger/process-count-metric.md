---
concept: Process Count Metric
slug: process-count-metric
category: production-ops
subcategory: observability
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Processes"
extraction_confidence: high
aliases:
  - process count
  - "length(processes())"
prerequisites:
  - runtime-introspection
extends: []
related:
  - port
  - process-count-anomaly
contrasts_with: []
answers_questions:
  - "What's a valuable process-related metric for a global view?"
  - "How do I detect a process leak?"
---

# Quick Definition

The process count — the number of live processes on a node — is a global metric used to gauge overall load and to detect process leaks, since Erlang convention is one process per concurrent task.

# Core Definition

"Trying to get a global view of processes is helpful when trying to assess how much work is being done in the VM in terms of *tasks*. A general good practice in Erlang is to use processes for truly concurrent activities... and therefore the number of processes on a node can be used as a metric for load" (Chapter 5, "Processes").

The count is obtained with `length(processes())`.

# Prerequisites

- `runtime-introspection`: process count is a core "in the large" metric.

# Key Properties

1. Obtained with the expression `length(processes())`.
2. Because Erlang uses one process per concurrent activity (e.g. one per web request/connection, one per user), the count is a meaningful load metric.
3. Tracking it *over time* helps characterize load and detect process leaks.
4. Most metrics libraries track it automatically; the manual expression is the fallback.
5. Most useful when you know the node's *usual average* — that baseline is what makes an anomaly recognizable.

# Construction / Recognition

Call `length(processes())` in a shell, or read the equivalent from a metrics library. Compare against the known baseline; a steady climb suggests a leak.

# Context & Application

Used to assess load and detect process leaks. It is also a key field in a crash dump (the "Number of processes" line), where it is interpreted against the node's normal count.

# Examples

From Chapter 5, "Processes":

```erlang-repl
1> length(processes()).
56535
```

"Tracking this value over time can be extremely helpful to try and characterize load or detect process leaks."

# Relationships

## Builds Upon
- runtime-introspection

## Enables

## Related
- port
- process-count-anomaly

## Contrasts With

# Common Errors

- Interpreting a raw count without a baseline — a number is only "high" or "low" relative to the node's normal value.
- Looking only at a snapshot instead of a trend, which hides slow leaks.

# Common Confusions

- A high process count is not inherently bad — Erlang systems routinely run tens of thousands of processes; the concern is *deviation from normal*.
- Process count measures task concurrency, not memory or CPU directly.

# Source Reference

Chapter 5: Runtime Metrics, Section "Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with example.
- Uncertainties: none.
- Cross-reference status: Verified
