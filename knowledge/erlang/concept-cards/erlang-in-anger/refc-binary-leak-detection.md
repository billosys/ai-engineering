---
concept: Refc Binary Leak Detection
slug: refc-binary-leak-detection
category: production-ops
subcategory: diagnostics
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Detecting Leaks"
extraction_confidence: high
aliases:
  - "recon:bin_leak"
  - "binary_memory inspection"
prerequisites:
  - refc-binary-leak
  - process-memory-inspection
related:
  - refc-binary-leak-fixes
  - recon-proc-window
contrasts_with: []
answers_questions:
  - "How do I detect a refc binary leak?"
  - "How do I find the processes holding the most binary memory?"
---

# Quick Definition

Refc binary leak detection uses `recon:bin_leak(Max)` — which snapshots binary references, forces a global garbage collection, snapshots again, and reports the per-process delta — together with `recon:proc_count(binary_memory, N)` to find processes holding the most binary memory.

# Core Definition

From section "Detecting Leaks": "Detecting leaks for reference-counted binaries is easy enough: take a measure of all of each process' list of binary references (using the `binary` attribute), force a global garbage collection, take another snapshot, and calculate the difference." This is done with `recon:bin_leak(Max)`, which "will show how many individual binaries were held and then freed by each process as a delta." A value of `-5580` means 5580 fewer refc binaries after the call than before. Top consumers by total binary memory are found with the `recon`-specific `binary_memory` attribute via `recon:proc_count(binary_memory, N)`.

# Prerequisites

- `refc-binary-leak` — you need to understand the leak before measuring it.
- `process-memory-inspection` — `binary_memory` ranking is a specialization of per-process memory ranking.

# Key Properties

1. `recon:bin_leak(Max)` snapshots, forces a global GC, snapshots again, and reports per-process deltas.
2. A negative delta (e.g. `-5580`) counts binaries freed by the forced GC — a large negative number flags a leaking process.
3. Watching the node's total memory before and after `bin_leak/1` reveals how much idling refc-binary memory existed.
4. `recon:proc_count(binary_memory, N)` ranks processes by total refc-binary memory referenced, catching processes holding a few *large* binaries rather than many small ones.
5. Because `bin_leak/1` garbage collects the whole node first, `proc_count(binary_memory, N)` should be run *before* `bin_leak/1` if you want an undisturbed picture.
6. Not every nonzero number is bad — some refc binaries are legitimately held at any time.

# Construction / Recognition

1. Optionally run `recon:proc_count(binary_memory, N)` first, before any forced GC.
2. Run `recon:bin_leak(Max)` and observe the per-process deltas.
3. Compare node total memory before and after the call.
4. Identify processes with large negative deltas or large `binary_memory` values.
5. Inspect those processes' work to plan a fix.

# Context & Application

This is the confirmation step after binary memory shows an upward trend. It distinguishes a real leak (large per-process deltas, big memory drop after GC) from normal binary use (small, stable numbers).

# Examples

From section "Detecting Leaks":

```erlang-repl
1> recon:bin_leak(5).
[{<0.4612.0>,-5580,
  [{current_function,{gen_fsm,loop,7}},
   {initial_call,{proc_lib,init_p,5}}]},
 ...]
```

And ranking by total binary memory:

```erlang-repl
1> recon:proc_count(binary_memory, 3).
[{<0.169.0>,77301349,
  [app_sup,
   {current_function,{gen_server,loop,6}},
   {initial_call,{proc_lib,init_p,5}}]},
 ...]
```

# Relationships

## Builds Upon
- `refc-binary-leak` — the condition being measured.
- `process-memory-inspection` — `binary_memory` is a specialized ranking attribute.

## Enables
- `refc-binary-leak-fixes` — once a leaking process is found, the fixes apply.

## Related
- `recon-proc-window` — sliding-window process ranking, a sibling technique.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Running `recon:proc_count(binary_memory, N)` after `bin_leak/1`, which already GC'd the whole node and distorts the picture.
- Treating any nonzero `bin_leak` delta as a problem; some held binaries are normal.

# Common Confusions

- `recon:bin_leak/1` does not just measure — it forces a node-wide garbage collection as part of the measurement, which itself reduces memory.
- `proc_count(memory, N)` ranks by total process memory; `proc_count(binary_memory, N)` ranks specifically by refc-binary memory referenced.

# Source Reference

Chapter 7: Memory Leaks, Section "Detecting Leaks". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Detecting Leaks."
- Confidence rationale: high — the source explicitly defines the algorithm and shows output.
- Uncertainties: none.
- Cross-reference status: Verified
