---
# === CORE IDENTIFICATION ===
concept: Process Performance Tuning
slug: process-performance

# === CLASSIFICATION ===
category: performance
subcategory: caveats
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.4. Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "process performance"
  - "min_heap_size"
  - "process hibernation"
  - "spawn_opt"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-performance
extends: []
related:
  - erlang-process
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What costs are involved in spawning and initializing processes?"
  - "When should you set a process's initial heap size?"
  - "What does hibernating a process do?"
---

# Quick Definition

Process performance tuning addresses the cost of OTP behaviour initialization, the option to set a larger initial heap size for short-lived processes, and hibernation to shrink the footprint of long-idle processes.

# Core Definition

Processes are the fundamental execution environment of an Erlang program — all code runs inside some process. Processes are cheap, but what each process does affects overall performance. Spawning a bare process takes microseconds, but initializing an OTP behaviour-container process is more expensive: `gen_server:start_link()` runs the `init/1` callback and does not return until it finishes, making startup deterministic. For large numbers of transient processes, a greater proportion of time is spent in OTP library code, so for speed-critical cases it can pay to roll your own lightweight processes with direct `spawn` (error-prone, a last resort). For rapidly spawned-and-dying processes, setting a large initial heap via `spawn_opt` with `{min_heap_size, Words}` avoids later garbage collection and reallocation. For very many long-idle processes, `erlang:hibernate/3` (or `proc_lib:hibernate/3` for OTP processes) discards the call stack, forces a garbage collection, and suspends the process with a minimal footprint until a message arrives (Chapter 14, Section 14.3.4).

# Prerequisites

- **Function call performance** — Continues the efficiency-caveats discussion at the process level.

# Key Properties

1. Spawning a bare process costs only microseconds; OTP behaviour initialization costs much more.
2. `gen_server:start_link()` runs `init/1` and blocks until it returns, for deterministic startup.
3. For huge numbers of transient processes, OTP overhead dominates; raw `spawn` can be used as a last resort.
4. The default process heap is 233 words (932 bytes on 32-bit) and grows/shrinks automatically.
5. `spawn_opt(Fun, [{min_heap_size, Words}])` sizes the heap up front, avoiding GC/realloc for short-lived processes.
6. A larger initial heap trades memory (over-approximated per process) for speed.
7. `erlang:hibernate(Mod, Func, Args)` throws away the call stack, GCs, and suspends until a message arrives; the call never returns.
8. OTP/`proc_lib`-based processes must use `proc_lib:hibernate/3` so the OTP libraries are restored on wake.

# Construction / Recognition

## To Construct/Create:
1. For speed-critical transient processes, consider raw `spawn` over an OTP behaviour (carefully).
2. For known-size short-lived processes, spawn with `spawn_opt(Fun, [{min_heap_size, Words}])`.
3. For many long-idle processes, have each call `erlang:hibernate/3` (or `proc_lib:hibernate/3` for OTP processes) while waiting.

# Context & Application

- **Typical contexts**: Systems with very large numbers of processes — connection handlers, monitors.
- **Common applications**: The book cites `ti_server` connection handlers (one process per TCP connection) as a case where process-init time adds up.
- **Historical/stylistic notes**: Hibernation suits systems monitoring a very large number of mostly-idle external entities.

# Examples

**Example 1** (Section 14.3.4): `erlang:spawn_opt(Fun, [{min_heap_size, Words}])` allocates the heap once, so the process needs no memory management between spawn and death.

**Example 2** (Section 14.3.4): A process that calls `erlang:hibernate/3` while waiting wakes up behaving as if it had called `apply(Mod, Func, Args)`, but with nowhere to return to.

# Relationships

## Related
- **Process** — The fundamental execution unit whose performance this card tunes.
- **gen_server** — OTP behaviour whose initialization cost motivates some of these techniques.

# Common Errors

- **Error**: Using `erlang:hibernate/3` directly in a `gen_server` or other `proc_lib`-based process.
  **Correction**: Use `proc_lib:hibernate/3` so the OTP libraries are properly re-set up on wake.

- **Error**: Abandoning OTP behaviours for raw `spawn` prematurely.
  **Correction**: This is error-prone and a last resort — do it only for proven hot spots, with experience.

# Common Confusions

- **Confusion**: Thinking `erlang:hibernate/3` returns control after the process wakes.
  **Clarification**: It discards the stack and never returns; the process resumes as a fresh `apply` of the given MFA.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.4 "Processes," Figure 14.4.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.4.
- Confidence rationale: HIGH — the techniques are explicitly described.
- Uncertainties: The 233-word default heap size is implementation-era-specific.
- Cross-reference status: References Agent 1- and Agent 2-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
