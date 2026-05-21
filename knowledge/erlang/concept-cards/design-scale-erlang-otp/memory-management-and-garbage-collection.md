---
# === CORE IDENTIFICATION ===
concept: BEAM Memory Management and Garbage Collection
slug: memory-management-and-garbage-collection

# === CLASSIFICATION ===
category: performance
subcategory: memory
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 128
section: "Memory Management and Garbage Collection"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - garbage collection
  - GC
  - "min_heap_size"
  - "fullsweep_after"
  - "min_bin_vheap_size"
  - generational garbage collector
  - virtual binary heap

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn-options
extends:
  - spawn-options
related:
  - init-timeout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the sys module relate to OTP behaviors?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

BEAM's garbage collector is a per-process generational semispace copying collector; its heap and GC behavior can be tuned per process via the `min_heap_size`, `min_bin_vheap_size`, and `fullsweep_after` spawn options.

# Core Definition

Erlang's garbage collection is "a per-process generational semispace copying collector that uses Cheney's copy collection algorithm together with a global large object space" (Cesarini & Vinoski, p. 128). When a process fills its heap, the BEAM triggers a GC that copies live data to a new heap and frees the old space. It is *generational*: data surviving two sweeps is copied from the *young heap* to the *old heap*; if young-heap collection cannot free enough memory, a *full-sweep* collection inspects and frees both heaps (pp. 128-129). Heap growth follows a Fibonacci series starting at 12 and 38 words, up to 833,026 words, then grows by 20%. Binaries larger than 64 bytes live in a shared binary heap accessed by reference; each process has a local *virtual binary heap* that triggers GC of unreferenced large binaries (pp. 129-130). Three tunable memory options exist: `min_heap_size` (the *maximum* size the heap grows to before GC is triggered — the name is misleading), `min_bin_vheap_size` (initial/minimum virtual binary heap space before binary GC), and `fullsweep_after` (number of generational GCs before a full sweep).

# Prerequisites

- **Behavior spawn options** — The memory and GC settings are applied through the `[{spawn_opts, OptsList}]` field, so spawn options are the delivery mechanism.

# Key Properties

1. Per-process: GC of process and virtual binary heaps is done per process, preserving soft real-time properties.
2. Generational: live data surviving two sweeps moves from the young heap to the old heap.
3. Full-sweep collection is triggered when young-heap GC fails to free enough memory, after a configured number of generational GCs, and on every `hibernate`.
4. Heap growth follows a Fibonacci recurrence (base 12 and 38 words) up to 833,026 words, then +20%.
5. `min_heap_size` — actually the maximum heap size before GC triggers; ideal for short-lived burst-of-work processes.
6. `min_bin_vheap_size` — virtual binary heap space (for binaries >64 bytes) before binary GC.
7. `fullsweep_after` — generational GCs before a full sweep; `0` disables generational GC; default (`65535`) is much higher than expected.
8. Binaries ≤64 bytes live on the normal heap; larger ones live in the shared binary heap and are reference-counted.

# Construction / Recognition

## To Tune Memory Management:
1. Benchmark to confirm the bottleneck is memory-related.
2. Choose the option: `min_heap_size` for burst processes, `min_bin_vheap_size` for binary-heavy ones, `fullsweep_after` for short-lived data.
3. Pass it via `[{spawn_opt, [...]}]` (per-process) or via `+hms`/`+hmbs` flags / `erlang:system_flag/2` (global, not recommended).
4. Verify with `process_info(Pid, garbage_collection)`; stress and soak test over days.

# Context & Application

- **Typical contexts**: Performance tuning of behaviors after profiling.
- **Common applications**: Pre-sizing a heap so a burst process never triggers GC; setting a low `fullsweep_after` to promptly free large binaries.
- **Historical/stylistic notes**: A large `min_heap_size` plus the default `fullsweep_after` of 65535 risks the old heap growing unbounded and the system running out of memory before the first full sweep (p. 131).

# Examples

**Example 1** (pp. 128-129): Tracing `gc_start`/`gc_end` with `dbg` while allocating five frequencies measured 9 microseconds of GC time (911,345 − 911,336).

**Example 2** (p. 129): Spawning `frequency` with `{min_heap_size, 1024}` provides enough memory to allocate all frequencies without triggering the garbage collector.

# Relationships

## Builds Upon
- **Behavior spawn options** — Memory management tuning is delivered through spawn options.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **Behavior spawn options** — `min_heap_size`, `min_bin_vheap_size`, and `fullsweep_after` are spawn options.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Setting a large `min_heap_size` while leaving the default `fullsweep_after` of 65535, causing the old heap to grow until the system runs out of memory.
  **Correction**: Tune the two together; lower `fullsweep_after` (the docs suggest 10 or 20) when keeping a large heap, and soak test for days.

- **Error**: Setting heap sizes globally with `+hms`/`+hmbs` for all processes.
  **Correction**: Tune on a per-process basis; global flags are advisable only with relatively few processes and only when benchmarks show a gain.

# Common Confusions

- **Confusion**: Reading `min_heap_size` as a minimum (floor) for the heap.
  **Clarification**: The name is misleading — it is the *maximum* size the heap grows to before GC is triggered. Also, because growth follows the Fibonacci series, the effective value is the next series value ≥ the requested size (e.g., 1024 → 1598).

# Source Reference

Chapter 4: Controlling OTP Behaviors, Sections "Memory Management and Garbage Collection" and "How BEAM's Garbage Collection Works," pages 128-132.

# Verification Notes

- Definition source: Direct quotes from pp. 128-130.
- Confidence rationale: HIGH — the source gives an explicit, detailed technical description of the GC algorithm and each option.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
