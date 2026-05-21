---
concept: CPU Profiling Difficulty on the BEAM
slug: cpu-profiling-difficulty
category: performance
subcategory: profiling
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "CPU and Scheduler Hogs"
chapter_number: 8
pdf_page: null
section: "CPU and Scheduler Hogs"
extraction_confidence: high
aliases:
  - "Why CPU analysis is hard in Erlang"
prerequisites: []
related:
  - erlang-profiling-tools
  - reduction-counting
  - long-schedule-monitor
contrasts_with: []
answers_questions:
  - "Why is it hard to analyze CPU usage on an Erlang node?"
  - "What are the two main approaches to pin CPU issues?"
---

# Quick Definition

CPU profiling is hard on the BEAM because everything is concurrent and runs inside a virtual machine, so there is no guarantee of pinning consumption to a specific process, driver, NIF, or library; the two main approaches are profiling/reduction-counting for your own code, and scheduler monitoring for everything else.

# Core Definition

From the chapter introduction: "It is generally difficult to properly analyze the CPU usage of an Erlang node to pin problems to a specific piece of code. With everything concurrent and in a virtual machine, there is no guarantee you will find out if a specific process, driver, your own Erlang code, NIFs you may have installed, or some third-party library is eating up all your processing power." The existing approaches are limited to "profiling and reduction-counting if it's in your code, and to monitoring the scheduler's work if it might be anywhere else (but also your code)."

# Prerequisites

This is a foundational framing concept within this source's CPU chapter — it has no prerequisites within this source.

# Key Properties

1. Concurrency plus virtual-machine execution makes CPU consumption hard to attribute.
2. The suspect could be a process, a driver, your Erlang code, a NIF, or a third-party library.
3. Two approach families: profiling/reduction-counting (for your own Erlang code) and scheduler monitoring (for anything, including your code).
4. CPU exhaustion acts as a bottleneck capping a node's throughput, rather than killing it outright like a memory leak.
5. Erlang developers tend to scale horizontally to escape CPU limits; only centralized global state usually needs modification.

# Construction / Recognition

When a node is CPU-bound: first try profiling tools or `recon:proc_window(reductions, ...)` to attribute usage to your code; if nothing stands out (work hidden in NIFs or GC), fall back to `erlang:system_monitor/2` with `long_schedule`/`long_gc`.

# Context & Application

This framing opens the chapter and motivates both the profiling section and the system-monitor section. It is invoked whenever a node is throughput-limited and the operator wants to optimize locally before scaling out.

# Examples

From the chapter introduction: "The existing approaches are often limited to profiling and reduction-counting if it's in your code, and to monitoring the scheduler's work if it might be anywhere else (but also your code)."

# Relationships

## Builds Upon
Nothing within this source — it is the chapter's framing premise.

## Enables
- `erlang-profiling-tools`, `reduction-counting`, `long-schedule-monitor` — the concrete techniques the two approaches comprise.

## Related
- `long-schedule-monitor` — the fallback when reduction counting reveals nothing.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Expecting one tool to attribute all CPU use; profiling covers your code, scheduler monitoring covers NIFs/GC/everything else.

# Common Confusions

- CPU exhaustion is a bottleneck (caps throughput), not a crash cause like a memory leak — the failure mode differs.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, chapter introduction. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter introduction.
- Confidence rationale: high — the source explicitly states the difficulty and the two approaches.
- Uncertainties: none.
- Cross-reference status: Verified
