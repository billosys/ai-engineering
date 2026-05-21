---
concept: Reduction
slug: reduction
category: performance
subcategory: scheduling
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "CPU"
extraction_confidence: high
aliases:
  - reductions
prerequisites: []
extends: []
related:
  - scheduler-utilization
  - process-inspection
contrasts_with: []
answers_questions:
  - "What is a reduction?"
  - "How can I tell if a process is doing a lot of work?"
---

# Quick Definition

A reduction is an arbitrary unit of work in the Erlang VM; every function call (including BIFs) increments a process's reduction counter, and the VM uses these counts to decide when to deschedule a process.

# Core Definition

"The VM internally uses a model based on *reductions*, which represent an arbitrary number of work actions. Every function call, including BIFs, will increment a process reduction counter. After a given number of reductions, the process gets descheduled" (Chapter 5, "CPU").

From "Processes": "The Erlang VM does scheduling based on *reductions*, an arbitrary unit of work that allows rather portable implementations of scheduling (time-based scheduling is usually hard to make work efficiently on as many OSes as Erlang runs on). The higher the reductions, the more work, in terms of CPU and function calls, a process is doing."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A reduction is an *arbitrary* unit of work — not tied to wall-clock time.
2. Every function call, including BIFs, increments the calling process's reduction counter.
3. After a fixed number of reductions, the process is descheduled — this is how Erlang achieves preemptive, fair scheduling.
4. Reduction-based scheduling is portable across the many operating systems Erlang runs on, unlike time-based scheduling.
5. A process's reduction count is a proxy for how much CPU/function-call work it is doing — higher means busier.
6. The `reductions` key of `process_info/2` (and `recon:info(Pid, work)`) exposes the count.

# Construction / Recognition

Read a process's reduction count via `process_info(Pid, reductions)` or `recon:info(Pid, work)`. Use `recon:proc_count(reductions, N)` or `recon:proc_window(reductions, N, Ms)` to find the busiest processes.

# Context & Application

Reductions underpin Erlang's preemptive scheduling and are the standard way to identify which processes are doing the most work, both for cumulative counts and for sliding-window sampling.

# Examples

From Chapter 5, "Processes":

```erlang-repl
2> recon:info(self(), work).
{work,[{reductions,11035}]}
```

`recon:proc_window(reductions, 3, 500)` ranks processes by reductions accumulated over a 500 ms window.

# Relationships

## Builds Upon

## Enables
- scheduler-utilization

## Related
- process-inspection

## Contrasts With

# Common Errors

- Treating a reduction as a fixed amount of CPU time — it is an arbitrary work unit, useful only for relative comparison.
- Comparing reduction counts of a long-lived process against a short-lived one without windowing — the long-lived one will look like a huge consumer simply because it had more time to accumulate.

# Common Confusions

- Reductions are about *work counting*, not timing — Erlang deliberately avoids time-based scheduling for portability.
- A high reduction count is meaningful relative to other processes or to a baseline, not as an absolute figure.

# Source Reference

Chapter 5: Runtime Metrics, Section "CPU" and Section "Digging In > Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — defined explicitly in two places.
- Uncertainties: none.
- Cross-reference status: Verified
