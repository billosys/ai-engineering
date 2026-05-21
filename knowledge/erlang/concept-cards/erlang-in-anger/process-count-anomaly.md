---
concept: Process Count Anomaly
slug: process-count-anomaly
category: production-ops
subcategory: crash-analysis
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "Too Many (or too few) Processes"
extraction_confidence: high
aliases:
  - too many processes
  - too few processes
prerequisites:
  - crash-dump-analysis
  - process-count-metric
extends: []
related:
  - port-count-anomaly
contrasts_with: []
answers_questions:
  - "How do I read a crash dump?"
  - "What should I look for if the process count is suspiciously low?"
---

# Quick Definition

A process count anomaly is a crash-dump process count that is much higher or much lower than the node's normal average — each direction pointing at a different class of failure.

# Core Definition

"The process count is mostly useful when you know your node's usual average count, in order to figure if it's abnormal or not. A count that is higher than normal may reveal a specific leak or overload, depending on applications. If the process count is extremely low compared to usual, see if the node terminated with a slogan like..." (Chapter 6, "Too Many (or too few) Processes").

# Prerequisites

- `crash-dump-analysis`: this is one branch of the crash-dump workflow.
- `process-count-metric`: interpreting the anomaly requires knowing the baseline count.

# Key Properties

1. Only meaningful relative to the node's *usual average* process count.
2. **Higher than normal** → likely a process leak or overload, depending on the application.
3. **Extremely low** → check whether the node died with a slogan like:
   `Kernel pid terminated (application_controller) ({application_terminated, <AppName>, shutdown})`.
4. That slogan means a specific application reached its maximum restart frequency within its supervisors, which shut the node down.
5. In the low-count case, the error logs that led to the cascading failure should be combed over.

# Construction / Recognition

Compare the dump's "Number of processes" against the node's baseline. If high, look for leaks/overload. If very low, read the termination slogan; if it names an application shutdown, investigate that application's supervisor restart history and preceding error logs.

# Context & Application

Used during crash-dump analysis to decide whether the crash was a resource leak/overload (high count) or a supervisor cascade failure (low count).

# Examples

From Chapter 6, "Too Many (or too few) Processes":

```text
Kernel pid terminated (application_controller)
  ({application_terminated, <AppName>, shutdown})
```

"In such a case, the issue is that a specific application (`<AppName>`) has reached its maximal restart frequency within its supervisors, and that prompted the node to shut down."

# Relationships

## Builds Upon
- crash-dump-analysis
- process-count-metric

## Enables

## Related
- port-count-anomaly

## Contrasts With

# Common Errors

- Interpreting the process count without a baseline — there is no universal "normal."
- Ignoring the termination slogan when the count is low — the slogan is the key clue for supervisor-cascade shutdowns.

# Common Confusions

- A *low* process count is counterintuitive as a failure symptom, but it signals a supervisor restart-intensity shutdown, not a leak.
- High and low counts point at opposite failure modes; the direction of the deviation matters.

# Source Reference

Chapter 6: Reading Crash Dumps, Section "Too Many (or too few) Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly described with the termination slogan.
- Uncertainties: none.
- Cross-reference status: Verified
