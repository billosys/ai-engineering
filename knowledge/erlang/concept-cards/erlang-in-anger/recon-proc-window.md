---
concept: recon:proc_window
slug: recon-proc-window
category: production-ops
subcategory: live-debugging
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Digging In > Processes"
extraction_confidence: high
aliases:
  - "recon:proc_window/3"
  - proc_window
prerequisites:
  - process-inspection
extends: []
related:
  - recon-proc-count
contrasts_with:
  - recon-proc-count
answers_questions:
  - "How do I find the busiest processes right now?"
  - "How do I find top memory-consuming processes?"
---

# Quick Definition

`recon:proc_window(Attribute, Num, Milliseconds)` ranks the top `Num` processes by how much a chosen attribute *changed* between two samples taken `Milliseconds` apart — a sliding-window view that catches short-lived and currently-active offenders.

# Core Definition

"There is however a problem when most processes are short-lived, usually too short to inspect through other tools, or when a moving window is what we need (for example, what processes are busy accumulating memory or running code *right now*). For this use case, Recon has the `recon:proc_window(Attribute, Num, Milliseconds)` function. It is important to see this function as a snapshot over a sliding window" (Chapter 5, "Digging In > Processes").

# Prerequisites

- `process-inspection`: `proc_window` ranks processes by `process_info` attributes.

# Key Properties

1. Signature: `recon:proc_window(Attribute, Num, Milliseconds)`.
2. Takes two samples at an interval of `Milliseconds` and ranks by the *difference*.
3. Catches short-lived processes and processes active "right now" that `proc_count` would miss.
4. Sampling-window caveat: if the sampling time is too long relative to process lifetimes, long-lived processes (which had more time to accumulate) skew the results. Make the sampling interval *smaller* than the typical process lifetime.
5. Warning: it builds a dictionary differentiating two snapshots, which can be heavy on memory and time with tens of thousands of processes.

# Construction / Recognition

Call `recon:proc_window(reductions, 3, 500)` to rank by reductions accumulated over a 500 ms window. Choose a window shorter than your processes' typical lifespan to avoid skew.

# Context & Application

Use `proc_window` when the suspect processes are short-lived, or when you want a "what is busy *now*" view. The book illustrates the timeline `--w---- [Sample1] ---x-------------y----- [Sample2] ---z-->`: processes living entirely between samples are measured well; those straddling a single sample are not.

# Examples

From Chapter 5, "Digging In > Processes":

```erlang-repl
5> recon:proc_window(reductions, 3, 500).
[{<0.46.0>,51728,
  [{current_function,{queue,in,2}},
   {initial_call,{erlang,apply,2}}]},
 {<0.49.0>,5728,
  [{current_function,{dict,new,0}}, ...]},
 {<0.43.0>,650,
  [{current_function,{timer,sleep,1}}, ...]}]
```

# Relationships

## Builds Upon
- process-inspection

## Enables

## Related

## Contrasts With
- recon-proc-count

# Common Errors

- Choosing a sampling window longer than typical process lifetimes — long-lived processes then dominate the ranking falsely.
- Running it on a node with tens of thousands of processes without expecting a memory/time cost from the two-snapshot dictionary.

# Common Confusions

- `proc_window` measures *change between two samples*, not absolute totals — that is what makes it suited to short-lived processes.
- It is the right tool for "right now" questions; `proc_count` is for cumulative, long-lived offenders.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with timeline explanation and example.
- Uncertainties: none.
- Cross-reference status: Verified
