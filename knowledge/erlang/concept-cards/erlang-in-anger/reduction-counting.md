---
concept: Reduction Counting for CPU Hogs
slug: reduction-counting
category: performance
subcategory: profiling
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "CPU and Scheduler Hogs"
chapter_number: 8
pdf_page: null
section: "Profiling and Reduction Counts"
extraction_confidence: high
aliases:
  - "proc_window reductions"
  - "Reduction-based CPU profiling"
prerequisites:
  - cpu-profiling-difficulty
  - reduction
related:
  - recon-proc-window
  - erlang-profiling-tools
  - long-schedule-monitor
contrasts_with:
  - erlang-profiling-tools
answers_questions:
  - "How do I find CPU or scheduler hogs in production?"
  - "How do I use reduction counts to identify busy processes?"
---

# Quick Definition

Reduction counting finds CPU hogs by ranking processes with `recon:proc_window(reductions, N, Interval)` — a high reduction count over a short window correlates directly with high CPU usage, and it is safe to run in production.

# Core Definition

From section "Profiling and Reduction Counts": the production-safe alternative to profilers is `recon:proc_window/3`. "The reduction count has a direct link to function calls in Erlang, and a high count is usually the synonym of a high amount of CPU usage." The technique is most useful "while a system is already rather busy, with a relatively short interval. Repeat it many times, and you should hopefully see a pattern emerge where the same processes (or the same kind of processes) tend to always come up on top."

# Prerequisites

- `cpu-profiling-difficulty` — reduction counting is one of the two CPU-attribution approaches.
- `reduction` — the unit being counted; you must understand reductions to interpret the counts.

# Key Properties

1. A reduction count is directly linked to function calls; a high count usually means high CPU usage.
2. `recon:proc_window(reductions, N, Interval)` ranks the top N processes by reductions over the interval.
3. The window must be short and the system already busy for the result to be meaningful.
4. Repeating the call many times reveals a stable pattern of the same processes (or kinds of processes) on top.
5. Returned data includes `current_function` and `initial_call`, plus code location via `recon:info(Pid, location)` or `process_info(Pid, current_stacktrace)`.
6. It is production-safe, unlike `eprof`/`fprof`/`eflame`.

# Construction / Recognition

1. While the node is busy, run `recon:proc_window(reductions, 3, 500)`.
2. Repeat the call many times with a short interval.
3. Watch for the same processes or process kinds recurring at the top.
4. Use `current_function` and code location to identify the hogging code.

# Context & Application

This is the production counterpart to the profiling tools. It attributes CPU to processes running your Erlang code. Work hidden in NIFs or garbage collection may not increment reductions correctly, so reduction counting can miss it — the system monitor covers that gap.

# Examples

From section "Profiling and Reduction Counts":

```erlang-repl
1> recon:proc_window(reductions, 3, 500).
[{<0.46.0>,51728,
  [{current_function,{queue,in,2}},
   {initial_call,{erlang,apply,2}}]},
 {<0.49.0>,5728,
  [{current_function,{dict,new,0}},
   {initial_call,{erlang,apply,2}}]},
 {<0.43.0>,650,
  [{current_function,{timer,sleep,1}},
   {initial_call,{erlang,apply,2}}]}]
```

# Relationships

## Builds Upon
- `cpu-profiling-difficulty` — one of the two attribution approaches.
- `reduction` — the counted unit.

## Enables
Nothing — terminal technique card.

## Related
- `recon-proc-window` — the sliding-window ranking function this technique uses.
- `long-schedule-monitor` — the fallback for work that does not increment reductions.

## Contrasts With
- `erlang-profiling-tools` — `eprof`/`fprof`/`eflame` are deeper but production-unsafe; reduction counting is shallower but production-safe.

# Common Errors

- Running `proc_window` on an idle system or with a long interval — the result will not reveal the real hogs.
- Sampling only once; the pattern emerges only across repeated calls.

# Common Confusions

- A high reduction count strongly suggests high CPU use but is a correlation, not a measurement of time — and NIF/GC work may not raise reductions at all.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, Section "Profiling and Reduction Counts". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Profiling and Reduction Counts."
- Confidence rationale: high — the source explicitly describes the technique and shows output.
- Uncertainties: none.
- Cross-reference status: Verified
