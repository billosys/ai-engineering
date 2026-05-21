---
concept: Garbage Collection System Monitor
slug: gc-system-monitor
category: production-ops
subcategory: diagnostics
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Garbage Collections"
extraction_confidence: high
aliases:
  - "long_gc monitor"
  - "large_heap monitor"
prerequisites:
  - process-memory-inspection
related:
  - long-schedule-monitor
  - process-memory-inspection
contrasts_with:
  - long-schedule-monitor
answers_questions:
  - "How can I find out if garbage collections are taking too long to run?"
  - "How do I monitor long GC?"
---

# Quick Definition

The garbage collection system monitor uses `erlang:system_monitor/2` with the `long_gc` and `large_heap` options to receive a message whenever a process's garbage collection runs too long or its heap grows too large.

# Core Definition

From section "Garbage Collections": monitoring every garbage collection from the shell in real time would be costly, so "setting up Erlang's system monitor might be the best way to go at it." Erlang's system monitor "will allow you to track information such as long garbage collection periods and large process heaps." A monitor for `long_gc` notifies the monitoring process every time a garbage collection takes longer than a given threshold; `large_heap` notifies when a heap exceeds a given word count.

# Prerequisites

- `process-memory-inspection` — once a system monitor flags a process, you dig into it (e.g. with `recon:info/1`), which builds on per-process inspection.

# Key Properties

1. Set with `erlang:system_monitor(MonitorPid, [{long_gc, Milliseconds}])` (and/or `{large_heap, NumWords}`).
2. Always check `erlang:system_monitor()` first — only one monitor can be installed, so you must not steal it from a coworker or application.
3. Monitor messages arrive in the monitor process's mailbox as `{monitor, Pid, long_gc, Info}` tuples.
4. The monitor is cleared with `erlang:system_monitor(undefined)`; exiting or killing the monitor process also frees it.
5. Start with large threshold values when unsure — small thresholds flood the mailbox with messages.
6. Useful for catching spiky processes whose memory is high only for short periods.

# Construction / Recognition

1. Run `erlang:system_monitor()` to confirm nothing else holds the monitor.
2. Install it: `erlang:system_monitor(self(), [{long_gc, 500}])`.
3. Collect notifications (e.g. via `flush()` in the shell).
4. Optionally add `{large_heap, NumWords}` to catch oversized heaps.
5. Unset with `erlang:system_monitor(undefined)` and verify with `erlang:system_monitor()`.
6. Correlate the flagged processes with observed memory increases; dig in with `recon:info/1`.

# Context & Application

This catches processes that consume large amounts of memory only briefly, or whose garbage collection takes so long it harms latency. On long-lived nodes with operational overhead this may be tolerable, but when memory becomes scarce, spiky behaviour is worth eliminating.

# Examples

From section "Garbage Collections":

```erlang-repl
1> erlang:system_monitor().
undefined
2> erlang:system_monitor(self(), [{long_gc, 500}]).
undefined
3> flush().
Shell got {monitor,<4683.31798.0>,long_gc,
                   [{timeout,515},
                    {old_heap_block_size,0},
                    {heap_block_size,75113},
                    {mbuf_size,0},
                    {stack_size,19},
                    {old_heap_size,0},
                    {heap_size,33878}]}
5> erlang:system_monitor(undefined).
{<0.26706.4961>,[{long_gc,500}]}
```

# Relationships

## Builds Upon
- `process-memory-inspection` — flagged processes are then inspected per-process.

## Enables
Nothing — terminal diagnostic card.

## Related
- `long-schedule-monitor` — the same `erlang:system_monitor/2` mechanism, used in Chapter 8 for `long_schedule`/`long_gc` to find CPU hogs.

## Contrasts With
- `long-schedule-monitor` — this card focuses on `long_gc`/`large_heap` for memory diagnosis; the long-schedule monitor focuses on `long_schedule` for CPU/scheduler diagnosis. Long GCs do count toward scheduling time, so the two overlap.

# Common Errors

- Installing a system monitor without first checking `erlang:system_monitor()` — overwriting a coworker's or an application's monitor.
- Setting `long_gc`/`large_heap` thresholds too small, flooding the monitor's mailbox.

# Common Confusions

- `large_heap` is measured in words, not bytes — a small number can match almost everything.
- Only one system monitor exists per node; installing a new one replaces any existing one.

# Source Reference

Chapter 7: Memory Leaks, Section "Garbage Collections". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Garbage Collections."
- Confidence rationale: high — the source explicitly shows the API and a worked session.
- Uncertainties: none.
- Cross-reference status: Verified
