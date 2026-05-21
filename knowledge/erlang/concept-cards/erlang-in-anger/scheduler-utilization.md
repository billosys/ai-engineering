---
concept: Scheduler Utilization
slug: scheduler-utilization
category: performance
subcategory: scheduling
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "CPU"
extraction_confidence: high
aliases:
  - scheduler wall time
  - "recon:scheduler_usage"
prerequisites:
  - runtime-introspection
extends: []
related:
  - reduction
  - vm-metrics-libraries
contrasts_with: []
answers_questions:
  - "What is scheduler wall time / utilization?"
  - "Why can't I trust top or htop for CPU usage with Erlang?"
  - "How does scheduler utilization relate to OS CPU usage?"
---

# Quick Definition

Scheduler utilization (scheduler wall time) is the fraction of time each Erlang scheduler spends actually running Erlang work — processes, NIFs, BIFs, garbage collection — versus idling or trying to schedule; it is the accurate substitute for OS CPU usage on Erlang nodes.

# Core Definition

"The most accurate representation for this data is the scheduler wall time. It's an optional metric that needs to be turned on by hand on a node, and polled at regular intervals. It will reveal the time percentage a scheduler has been running processes and normal Erlang code, NIFs, BIFs, garbage collection, and so on, versus the amount of time it has spent idling or trying to schedule processes" (Chapter 5, "CPU").

"The value here represents *scheduler utilization* rather than CPU utilization. The higher the ratio, the higher the workload."

# Prerequisites

- `runtime-introspection`: scheduler utilization is the "in the large" CPU metric for the VM.

# Key Properties

1. CPU is hard to profile in Erlang because the VM does scheduling work unrelated to processes, uses a reduction-based model, and busy-loops scheduler threads to keep latency low.
2. Scheduler wall time is an *optional* metric — it must be enabled by hand and polled at intervals.
3. `recon:scheduler_usage(N)` polls for `N` milliseconds and returns a per-scheduler ratio (0.0..1.0).
4. Because scheduler threads busy-loop, the OS may report a core as busy while the scheduler is merely waiting for work — so `htop` overstates real Erlang load.
5. Scheduler usage can read *higher* (1.0) than the OS reports: schedulers waiting on OS resources count as utilized because they cannot do more work.
6. The `+sbwt none|very_short|short|medium|long|very_long` VM flag controls the busy-wait behavior.
7. Better than CPU usage or load average for capacity planning headroom.

# Construction / Recognition

Enable scheduler wall time on the node, then call `recon:scheduler_usage(1000)` (poll for 1 second) and read the per-scheduler ratios. Poll regularly to track over time.

# Context & Application

Used for capacity planning and diagnosing whether a node is truly CPU-bound. An Erlang node will commonly look busy to the OS while still having room to absorb a much higher workload.

# Examples

From Chapter 5, "CPU":

```erlang-repl
1> recon:scheduler_usage(1000).
[{1,0.9919596133421669},
 {2,0.9369579039389054},
 {3,1.9294092120138725e-5},
 {4,1.2087551402238991e-5}]
```

Two schedulers at ~99.2% and ~93.7%, two essentially idle. Meanwhile `htop` might show all four cores at 70.4%, 20.6%, 100.0%, 40.2% — busy-looping makes the OS overstate usage.

# Relationships

## Builds Upon
- runtime-introspection

## Enables

## Related
- reduction
- vm-metrics-libraries

## Contrasts With

# Common Errors

- Trusting `top`/`htop` CPU readings for Erlang capacity decisions — busy-waiting schedulers inflate OS CPU figures.
- Forgetting to enable scheduler wall time before polling — it is off by default.

# Common Confusions

- Scheduler utilization measures *scheduler busyness*, not raw CPU usage; the two can diverge in both directions.
- A scheduler can report 1.0 even when the CPU is not maxed, if it is blocked waiting on OS resources.

# Source Reference

Chapter 5: Runtime Metrics, Section "CPU". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with worked example and the htop contrast.
- Uncertainties: none.
- Cross-reference status: Verified
