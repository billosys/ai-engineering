---
concept: Process Leak
slug: process-leak
category: production-ops
subcategory: memory
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
  - "Leaking processes"
  - "Unlinked process leak"
prerequisites:
  - memory-leak-detection
related:
  - process-memory-inspection
  - ets-leak
contrasts_with:
  - process-memory-inspection
answers_questions:
  - "How could I verify if a leak is caused by forgetting to kill processes?"
  - "How do I find unlinked or unmonitored processes?"
---

# Quick Definition

A process leak is the accumulation of processes that are never terminated — typically processes left unlinked and unmonitored so that no supervisor or parent ever cleans them up.

# Core Definition

From section "Processes": process memory can grow in several ways, the most interesting being "process leaks (as in, you're leaking processes), specific processes leaking their memory." When the global process count itself indicates a leak, the investigation looks for unlinked processes or peeks inside supervisors' children lists for anything weird-looking. The chapter gives a shell one-liner to find processes with neither links nor monitors, since those are the ones nothing will clean up.

# Prerequisites

- `memory-leak-detection` — recognizing a rising process count is the precondition for this investigation.

# Key Properties

1. A process leak is distinct from a single process leaking its own memory.
2. Processes with neither links nor monitors are prime suspects — nothing tears them down.
3. The `process_info(P, [links, monitors])` attributes reveal whether a process is connected to anything.
4. `supervisor:count_children(SupervisorPidOrName)` shows a supervisor's child counts for sanity-checking.
5. Multiple causes can coexist, so several metrics are worth investigating.

# Construction / Recognition

1. Confirm the global process count indicates a leak.
2. Run the shell one-liner to list processes with neither links nor monitors.
3. For supervisors, call `supervisor:count_children/1` and check whether the numbers look normal.
4. Investigate the suspect processes' initial calls and current functions to find what spawns them without supervision.

# Context & Application

This investigation applies when a node steadily accumulates processes — for example, request handlers spawned with `spawn/1` instead of being supervised, or one-off workers that never terminate. Unlinked, unmonitored processes are invisible to OTP cleanup and leak silently.

# Examples

From section "Processes," finding unlinked and unmonitored processes:

```erlang-repl
1> [P || P <- processes(),
         [{_,Ls},{_,Ms}] <- [process_info(P, [links,monitors])],
         []==Ls, []==Ms].
```

The chapter notes: "This will return a list of processes with neither. For supervisors, just fetching `supervisor:count_children(SupervisorPidOrName)` and seeing what looks normal can be a good pointer."

# Relationships

## Builds Upon
- `memory-leak-detection` — one branch of the leak investigation.

## Enables
Nothing — terminal investigation card.

## Related
- `process-memory-inspection` — used when individual processes, rather than process counts, are the problem.
- `ets-leak` — another category checked when overall counts grow.

## Contrasts With
- `process-memory-inspection` — a process leak is too many processes; the inspection concept addresses individual processes that each consume too much memory.

# Common Errors

- Spawning processes with `spawn/1` outside any supervision, so crashes and exits never clean them up.
- Looking only at supervisor children and missing rogue unlinked processes.

# Common Confusions

- "Leaking processes" (count grows) is not the same as "a process leaking memory" (one process's footprint grows); the diagnostics differ.

# Source Reference

Chapter 7: Memory Leaks, Section "Processes" (subsection "Links and Monitors"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from section "Processes," with the source's verbatim shell one-liner.
- Confidence rationale: high — the source explicitly describes the detection technique.
- Uncertainties: none.
- Cross-reference status: Verified
