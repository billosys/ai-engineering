---
concept: Process Memory Inspection
slug: process-memory-inspection
category: production-ops
subcategory: diagnostics
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Processes"
extraction_confidence: high
aliases:
  - "Per-process memory inspection"
  - "proc_count memory"
prerequisites:
  - memory-leak-detection
related:
  - process-leak
  - recon-proc-window
  - refc-binary-leak-detection
  - gc-system-monitor
contrasts_with:
  - process-leak
answers_questions:
  - "If a node died with a process having a lot of memory, how do I find which one?"
  - "How do I find the processes using the most memory?"
---

# Quick Definition

Process memory inspection is the technique of ranking processes by their `memory` attribute — typically with `recon:proc_count(memory, N)` — to find the individual processes consuming the most memory on a node.

# Core Definition

From section "Processes," subsection "Memory Used": "you can find which individual processes use the most memory by looking for their `memory` attribute. You can look things up either as absolute terms or as a sliding window." For memory leaks, "unless you're in a predictable fast increase, absolute values are usually those worth digging into first," obtained with `recon:proc_count(memory, N)`. The `memory` attribute is the most encompassing — it usually covers all other memory types a process holds.

# Prerequisites

- `memory-leak-detection` — recognizing that process memory is the growing category precedes per-process inspection.

# Key Properties

1. Processes can be ranked by the `memory` attribute as absolute values or as a sliding window.
2. For leaks, absolute values are usually examined first; a sliding window suits predictable fast increases.
3. `recon:proc_count(memory, N)` returns the top N processes with their initial call and current function.
4. The `memory` attribute usually encompasses all other process memory types, including `message_queue_len`.
5. Other attributes (e.g. `message_queue_len`) can also be ranked when a more specific cause is suspected.

# Construction / Recognition

1. Confirm process memory is the growing category.
2. Run `recon:proc_count(memory, 3)` (or another N) for absolute values, or `recon:proc_window/3` for a sliding window.
3. Read the returned initial call and current function to identify the offending code.
4. Dig deeper into the suspect process, possibly with `recon:info/1`.

# Context & Application

This is the per-process counterpart to overall trend analysis. It is used when total process memory is growing but the process count is stable — meaning one or a few processes are bloating rather than processes multiplying. It also helps post-mortem: identifying which process held the most memory when a node died.

# Examples

From section "Processes," subsection "Memory Used":

```erlang-repl
1> recon:proc_count(memory, 3).
[{<0.175.0>,325276504,
  [myapp_stats,
   {current_function,{gen_server,loop,6}},
   {initial_call,{proc_lib,init_p,5}}]},
 {<0.169.0>,73521608,
  [myapp_giant_sup,
   {current_function,{gen_server,loop,6}},
   {initial_call,{proc_lib,init_p,5}}]},
 {<0.72.0>,4193496,
  [gproc,
   {current_function,{gen_server,loop,6}},
   {initial_call,{proc_lib,init_p,5}}]}]
```

# Relationships

## Builds Upon
- `memory-leak-detection` — this is one branch of the leak investigation.

## Enables
- `refc-binary-leak-detection` — refc-binary inspection builds on the same per-process ranking idea.

## Related
- `recon-proc-window` — the sliding-window variant of process ranking.
- `gc-system-monitor` — used when spiky per-process memory needs correlating with garbage collection.

## Contrasts With
- `process-leak` — process leak is about too many processes; this concept is about individual processes that are each too large.

# Common Errors

- Using a sliding window when a stable absolute leak is what you actually have.
- Inspecting `message_queue_len` first when `memory` already encompasses it.

# Common Confusions

- A high-memory process is not necessarily a leak — it may legitimately need that memory; ranking points you to a candidate, not a verdict.

# Source Reference

Chapter 7: Memory Leaks, Section "Processes" (subsection "Memory Used"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Processes," subsection "Memory Used."
- Confidence rationale: high — the source explicitly defines the technique and shows output.
- Uncertainties: none.
- Cross-reference status: Verified
