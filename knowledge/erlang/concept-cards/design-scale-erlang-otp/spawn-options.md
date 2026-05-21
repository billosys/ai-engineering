---
# === CORE IDENTIFICATION ===
concept: Behavior Spawn Options
slug: spawn-options

# === CLASSIFICATION ===
category: performance
subcategory: process-tuning
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 127
section: "Spawn Options"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{spawn_opts, OptsList}"
  - "spawn_opt options"
  - behavior spawn opts

# === TYPED RELATIONSHIPS ===
prerequisites:
  - the-sys-module
extends: []
related:
  - memory-management-and-garbage-collection
  - spawn-options-to-avoid
  - init-timeout
contrasts_with:
  - spawn-options-to-avoid

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the sys module relate to OTP behaviors?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

Spawn options let you override a behavior process's default memory and garbage-collector settings at start time, passed in the behavior's `Opts` field as `[{spawn_opts, OptsList}]` — the same options taken by the `spawn_opt/4` BIF.

# Core Definition

When starting a behavior, "you can change the default memory and garbage collector settings to address performance and memory utilization" (Cesarini & Vinoski, p. 127). The settings are the same ones taken by the `spawn_opt/4` BIF, but passed as `[{spawn_opts, OptsList}]` in the behavior's `Opts` field alongside the debug options. The authors stress that spawn options should be used with care: "The only way to be sure you have performance issues and bottlenecks related to memory management is by profiling and benchmarking your systems." Premature optimization of memory management often makes programs slower; the vast majority of cases do not call for it, but those that do benefit greatly from a larger heap or different garbage collection frequency (pp. 127-128).

# Prerequisites

- **The sys module** — Spawn options are passed through the same behavior `Opts` field as the `sys`-related debug options.

# Key Properties

1. Passed as `[{spawn_opts, OptsList}]` in the behavior `Opts` field, together with `[{debug, DbgList}]`.
2. `OptsList` accepts the same entries as the `spawn_opt/4` BIF.
3. Memory-related options include `min_heap_size`, `min_bin_vheap_size`, and `fullsweep_after`.
4. Misuse can degrade performance — always profile and benchmark before tuning.
5. Some `spawn_opt` options (`monitor`, `priority`) are disallowed or discouraged for behaviors (see contrasting card).

# Construction / Recognition

## To Apply Spawn Options:
1. Decide which memory option to tune (`min_heap_size`, `min_bin_vheap_size`, `fullsweep_after`).
2. Benchmark the system with the candidate value.
3. Pass `[{spawn_opt, [{min_heap_size, 1024}]}]` (or similar) as the behavior's `Opts` argument to its start function.
4. Verify with `process_info(Pid, garbage_collection)`.

# Context & Application

- **Typical contexts**: Performance-critical behaviors after profiling reveals memory-management bottlenecks.
- **Common applications**: Pre-sizing the heap of a short-lived burst-of-work process; tuning garbage collection frequency.
- **Historical/stylistic notes**: The book parks detailed performance tuning until Chapter 13 and recommends consulting the `spawn_opt` BIF documentation in the `erlang` module manual page (p. 128, p. 134).

# Examples

**Example 1** (p. 129): Starting `frequency` with a pre-sized heap so no garbage collection is triggered:

```erlang
{ok, Pid} = gen_server:start_link({local, frequency}, frequency, [],
                                  [{spawn_opt, [{min_heap_size, 1024}]}]).
```

**Example 2** (p. 131): `process_info(Pid, garbage_collection)` reports the effective settings — note `min_heap_size` shows `1598`, the next Fibonacci value above the requested `1024`.

# Relationships

## Builds Upon
- *(No prior concept in this scope; relies on the behavior `Opts` field discussed alongside the sys module.)*

## Enables
- **memory-management-and-garbage-collection** — Spawn options are the mechanism for applying memory and GC tuning.
- **init-timeout** — Another option passed in the same `Opts` field.

## Related
- **memory-management-and-garbage-collection** — Spawn options carry the `min_heap_size`, `min_bin_vheap_size`, and `fullsweep_after` settings.

## Contrasts With
- **spawn-options-to-avoid** — `monitor`, `link`, and `priority` should not be used with behaviors even though they are valid `spawn_opt` entries.

# Common Errors

- **Error**: Tuning spawn options based on intuition rather than measurement.
  **Correction**: Always profile and benchmark first; premature memory-management optimization commonly makes programs slower.

# Common Confusions

- **Confusion**: Thinking every `spawn_opt/4` option is safe to use with OTP behaviors.
  **Clarification**: Behaviors accept the memory options, but `monitor` is disallowed and `priority` is strongly discouraged (see "Spawn Options to Avoid").

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Spawn Options," pages 127-128; see also "Summing Up," page 134.

# Verification Notes

- Definition source: Direct quotes from pp. 127-128; examples from pp. 129-131.
- Confidence rationale: HIGH — the source explicitly defines the option format and gives shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
