---
concept: Long Schedule Monitor
slug: long-schedule-monitor
category: production-ops
subcategory: diagnostics
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "CPU and Scheduler Hogs"
chapter_number: 8
pdf_page: null
section: "System Monitors"
extraction_confidence: high
aliases:
  - "long_schedule monitor"
prerequisites:
  - cpu-profiling-difficulty
related:
  - gc-system-monitor
  - reduction-counting
  - busy-port
contrasts_with:
  - gc-system-monitor
answers_questions:
  - "How do I find CPU or scheduler hogs that profiling misses?"
  - "Why are long scheduling monitors useful for CPU over-consumption?"
---

# Quick Definition

The long schedule monitor uses `erlang:system_monitor/2` with the `long_schedule` (and `long_gc`) options to catch processes that run for excessively long uninterrupted periods — typically because of NIFs or other work that is hard to de-schedule.

# Core Definition

From section "System Monitors": when profiling and reduction counts reveal nothing, the work may be done by NIFs, garbage collections, and so on, which "may not always increment their reductions count correctly, so they won't show up with the previous methods, only through long run times." The best way to find such cases is `erlang:system_monitor/2` watching `long_gc` and `long_schedule`: the former shows garbage collection doing a lot of work, the latter "will likely catch issues with busy processes, either through NIFs or some other means, that end up making them hard to de-schedule."

# Prerequisites

- `cpu-profiling-difficulty` — the long schedule monitor is the fallback approach when reduction counting misses hidden work.

# Key Properties

1. Set via `erlang:system_monitor(MonitorPid, [{long_schedule, Delay}, {long_gc, Delay}])`.
2. `long_schedule` catches processes that run too long without yielding — often NIFs or other hard-to-de-schedule work.
3. `long_gc` catches garbage collection doing a lot of work; long GCs count toward scheduling time.
4. NIFs and GC may not increment reductions correctly, so they are invisible to reduction counting and profilers — only long run times expose them.
5. Monitor messages arrive as `{monitor, Pid, long_schedule, Info}` (and `long_gc`), with `Info` including timeout, `in`, and `out` functions.
6. Set thresholds to large-ish reasonable values (e.g. 1000 ms) to avoid noise.
7. The monitor can be moved into its own module reporting to long-term logging — a canary for performance degradation or overload.

# Construction / Recognition

1. Register a monitor process and call `erlang:system_monitor(self(), [{long_schedule, 1000}, {long_gc, 1000}])`.
2. Receive and log `{monitor, Pid, long_schedule|long_gc, Info}` messages.
3. Read `Info`'s `in`/`out` function entries to locate the long-running code.
4. Kill the monitor with `exit(whereis(temp_sys_monitor), kill)` or disconnect from the node.

# Context & Application

This is the production-safe last resort for CPU diagnosis when profiling and reduction counting come up empty. It catches scheduler hogs hidden inside NIFs or long garbage collections. Productionized, it serves as a continuous canary for overload.

# Examples

From section "System Monitors":

```erlang-repl
3> spawn_link(Setup(1000)).
<0.1293.0>
monitor=long_schedule pid=<0.54.0> info=[{timeout,1102},
                                         {in,{some_module,some_function,3}},
                                         {out,{some_module,some_function,3}}]
```

# Relationships

## Builds Upon
- `cpu-profiling-difficulty` — the second of the two CPU-attribution approaches.

## Enables
Nothing — terminal diagnostic card.

## Related
- `reduction-counting` — the technique this monitor backstops when reductions miss hidden work.
- `busy-port` — `busy_port`/`busy_dist_port` are other atoms the same system monitor accepts.

## Contrasts With
- `gc-system-monitor` — the same `erlang:system_monitor/2` mechanism; Chapter 7's card focuses on `long_gc`/`large_heap` for memory diagnosis, while this card focuses on `long_schedule` for CPU/scheduler diagnosis. Long GCs count toward scheduling time, so they overlap.

# Common Errors

- Setting `long_schedule`/`long_gc` thresholds too small, flooding the monitor with noise.
- Forgetting that killing the monitor (linked to the shell) will also kill the shell.

# Common Confusions

- A long schedule does not mean a process did a lot of *reduction* work — a process doing little reduction work but scheduled for long stretches points to a NIF or hard-to-de-schedule code.
- This and `gc-system-monitor` use one shared `erlang:system_monitor/2` slot — only one monitor exists per node.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, Section "System Monitors". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "System Monitors."
- Confidence rationale: high — the source explicitly describes the API and shows a session.
- Uncertainties: none.
- Cross-reference status: Verified
