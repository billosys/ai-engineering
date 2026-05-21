---
concept: Memory Leak Detection
slug: memory-leak-detection
category: production-ops
subcategory: diagnostics
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Common Sources of Leaks"
extraction_confidence: high
aliases:
  - "Finding memory leaks"
  - "Memory trend analysis"
prerequisites:
  - vm-memory-reporting
related:
  - atom-leak
  - ets-leak
  - process-leak
  - refc-binary-leak
  - memory-fragmentation
  - gc-system-monitor
contrasts_with:
  - memory-fragmentation
answers_questions:
  - "How do I detect a memory leak on an Erlang node?"
  - "What memory types should I watch for trends?"
---

# Quick Definition

Memory leak detection on a BEAM node is the practice of looking for worrisome upward trends across the memory categories reported by `erlang:memory()`, then narrowing the search to the specific category (atom, code, ETS, processes, binaries) that is growing.

# Core Definition

The chapter "Memory Leaks" identifies two ways memory leaks become visible: through a crash dump that complains about memory, or by spotting a worrisome trend in monitored data. The chapter focuses on the latter because such leaks are easier to investigate and watch grow in real time. The first step in any investigation is to look at trends: "Check for all types of memory using `erlang:memory()` or some variant of it." The operator asks whether any memory type is growing faster than others, whether any type takes the majority of available space, and whether any type never goes down and always up (other than atoms).

# Prerequisites

- `vm-memory-reporting` — you must be able to read per-type memory figures from `erlang:memory()` or an equivalent metrics library before you can spot a trend.

# Key Properties

1. Two discovery channels: a crash dump that complains about memory, or a trend in monitored data.
2. Trend analysis over absolute snapshots is the entry point — a single reading cannot reveal a leak.
3. Diagnostic questions: which type grows fastest, which type dominates, which type only ever grows.
4. Atoms are a noted exception to the "always going up" alarm because they are cached forever by design.
5. Crashes during peak load suggest overload management problems; crashes at any time (even as load drops) suggest a real memory leak.
6. Each memory type (atom, binary, code, ETS, processes) has its own dedicated remediation path.

# Construction / Recognition

1. Ask for data: is there a crash dump, and does it complain about memory?
2. Determine whether crashes are cyclical, predictable, or correlated with load peaks.
3. If a memory leak is suspected, install a metrics library and/or `recon`.
4. Sample `erlang:memory()` over time and look for an upward trend.
5. Identify the dominant or fastest-growing memory category.
6. Branch into the category-specific investigation (atom, code, ETS, process, binary, or fragmentation).

# Context & Application

This is the diagnostic gateway for the whole chapter. It runs on long-lived production nodes that are monitored continuously. When no specific data type stands out, the investigation moves on to binary leaks, memory fragmentation, or a leaking C driver/NIF/VM.

# Examples

From section "Common Sources of Leaks": the interesting questions to ask include "Do crashes coincide with peaks in load on your systems, or do they seem to happen at more or less any time? Crashes that happen especially during peak times are often due to bad overload management ... Crashes that happen at any time, even when load goes down following a peak are more likely to be actual memory issues."

# Relationships

## Builds Upon
- `vm-memory-reporting` — supplies the per-type figures used for trend analysis.

## Enables
- `atom-leak`, `ets-leak`, `process-leak`, `refc-binary-leak`, `memory-fragmentation` — the category-specific investigations branched into from here.

## Related
- `gc-system-monitor` — used when process memory spikes need to be correlated with garbage collection.

## Contrasts With
- `memory-fragmentation` — a leak grows Erlang-term memory; fragmentation shows the OS reporting much more memory than `erlang:memory()` does.

# Common Errors

- Reacting to a single snapshot instead of a trend; some memory use is legitimate and stable.
- Alarming over rising atom memory — atoms grow by design unless dynamically created.
- Assuming peak-time crashes are leaks when they are usually overload-management failures.

# Common Confusions

- A memory leak (growing Erlang-term memory) is distinct from memory fragmentation (OS holding memory the VM no longer actively uses). Detection differs: a leak shows in `erlang:memory()`; fragmentation shows as a gap between `erlang:memory()` and OS figures.

# Source Reference

Chapter 7: Memory Leaks, Section "Common Sources of Leaks". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from section "Common Sources of Leaks," with a direct quote on crash timing.
- Confidence rationale: high — the chapter explicitly lays out the detection workflow.
- Uncertainties: none.
- Cross-reference status: Verified
