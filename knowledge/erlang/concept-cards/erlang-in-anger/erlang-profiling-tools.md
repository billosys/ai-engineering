---
concept: Erlang Profiling Tools
slug: erlang-profiling-tools
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
  - "eprof"
  - "fprof"
  - "eflame"
prerequisites:
  - cpu-profiling-difficulty
related:
  - reduction-counting
  - long-schedule-monitor
contrasts_with:
  - reduction-counting
answers_questions:
  - "What profiling tools are available for Erlang?"
  - "Which profiling approaches are preferable for production use and why?"
---

# Quick Definition

Erlang ships with three principal CPU profilers — `eprof` (oldest, time-percentage reports), `fprof` (concurrency-aware, deep but opaque reports), and `eflame` (flame graphs) — all of which use the tracing facility heavily and should not be run in production.

# Core Definition

From section "Profiling and Reduction Counts," the profiling applications are: `eprof`, "the oldest Erlang profiler around. It will give general percentage values and will mostly report in terms of time taken"; `fprof`, "a more powerful replacement of eprof. It will support full concurrency and generate in-depth reports ... so deep that they are usually considered opaque and hard to read"; and `eflame`, "the newest kid on the block ... It generates flame graphs to show deep call sequences and hot-spots." A chapter footnote warns: "All of these profilers work using Erlang tracing functionality with almost no restraint. They will have an impact on the run-time performance of the application, and shouldn't be used in production."

# Prerequisites

- `cpu-profiling-difficulty` — profiling is one of the two CPU-attribution approaches that concept frames.

# Key Properties

1. `eprof` — oldest; general percentage values; reports in time taken.
2. `fprof` — more powerful eprof replacement; full concurrency support; in-depth but opaque reports.
3. `eflame` — newest; produces flame graphs revealing deep call sequences and hot-spots at a glance.
4. All three are built on Erlang's tracing facility, used with almost no restraint.
5. All three impact run-time performance and should NOT be used in production.
6. They attribute CPU only to your own Erlang code, not to NIFs or GC work.

# Construction / Recognition

Choose a profiler by the report you want: `eprof` for quick percentages, `fprof` for exhaustive concurrent detail, `eflame` for a visual flame graph. Run them in development or test environments, not production. The book leaves thorough reading of each tool's documentation to the reader.

# Context & Application

These tools attribute CPU consumption within your own code paths during development and testing. Because they trace without rate limits and perturb performance, production CPU investigation should instead use reduction counting (`recon:proc_window`) and the system monitor.

# Examples

From section "Profiling and Reduction Counts": `fprof`'s reports "are so deep that they are usually considered opaque and hard to read," whereas `eflame` "allows one to quickly find issues with a single look at the final result."

# Relationships

## Builds Upon
- `cpu-profiling-difficulty` — profiling is one of the two attribution approaches.

## Enables
Nothing — terminal tooling card.

## Related
- `long-schedule-monitor` — the production-safe fallback when profiling cannot run.

## Contrasts With
- `reduction-counting` — reduction counting (`recon:proc_window`) is production-safe; these profilers are not.

# Common Errors

- Running `eprof`/`fprof`/`eflame` in production — they trace without restraint and degrade performance.
- Expecting profilers to reveal CPU spent in NIFs or garbage collection; they attribute only Erlang code.

# Common Confusions

- A profiler tells you which functions burn time/reductions; it does not catch hidden scheduler hogs (NIFs, long GC) — that needs the system monitor.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, Section "Profiling and Reduction Counts". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Profiling and Reduction Counts."
- Confidence rationale: high — the source names and characterizes each tool.
- Uncertainties: none.
- Cross-reference status: Verified
