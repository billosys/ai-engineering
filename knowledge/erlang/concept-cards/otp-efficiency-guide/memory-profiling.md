---
# === CORE IDENTIFICATION ===
concept: Memory Profiling
slug: memory-profiling

# === CLASSIFICATION ===
category: performance
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Profiling"
chapter_number: null
pdf_page: null
section: "Memory profiling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "memory analysis"
  - "heap profiling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - tprof
  - large-system-profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "How do I diagnose memory issues in an Erlang system?"
  - "What do I do when Erlang cannot allocate memory?"
---

# Quick Definition

Memory profiling in Erlang involves using `erlang:memory()`, `instrument`, process/port/ETS info functions, and crash dump analysis to diagnose memory allocation failures and understand memory usage patterns in a running or crashed system.

# Core Definition

The Erlang Efficiency Guide describes memory profiling in the context of a common failure mode: "The above slogan [`eheap_alloc: Cannot allocate ... bytes of memory`] is one of the more common reasons for Erlang to terminate. For unknown reasons the Erlang Run-Time System failed to allocate memory to use. When this happens a crash dump is generated that contains information about the state of the system as it ran out of memory. Use `crashdump_viewer` to get a view of the memory being used. Look for processes with large heaps or many messages, large ETS tables, and so on."

For running systems: "the most basic function to get information from is `erlang:memory()`. It returns the current memory usage of the system. `instrument` can be used to get a more detailed breakdown of where memory is used." Individual entities can be inspected using `process_info/2`, `erlang:port_info/2`, and `ets:info/1`.

# Prerequisites

- **Profiling Strategy** -- Understanding that memory issues require specific profiling approaches, not guessing.

# Key Properties

1. `erlang:memory()` returns current memory usage of the entire system.
2. `instrument` provides a more detailed breakdown of memory usage.
3. `process_info/2` can inspect memory usage of individual processes.
4. `erlang:port_info/2` can inspect memory usage of individual ports.
5. `ets:info/1` can inspect memory usage of ETS tables.
6. `crashdump_viewer` analyzes crash dumps when the system terminates from memory exhaustion.
7. Internal fragmentation can cause `erlang:memory(total)` to differ significantly from OS-reported memory.
8. `erlang:system_info(allocator)` provides raw data about memory allocation (hard to read).
9. `recon_alloc` can extract useful information from system_info allocator statistics.

# Construction / Recognition

## To Profile Memory in a Running System:
1. Call `erlang:memory()` for an overview of current memory usage.
2. Use `instrument` for a detailed breakdown if needed.
3. Inspect individual processes with `process_info(Pid, memory)` to find large heaps.
4. Inspect individual processes with `process_info(Pid, messages)` to find message queue buildup.
5. Check ETS tables with `ets:info/1` for large tables.
6. If reported memory differs from OS memory, check for internal fragmentation via `erlang:system_info(allocator)` or `recon_alloc`.

## To Analyze a Memory-Related Crash:
1. Locate the crash dump file generated when the system ran out of memory.
2. Open with `crashdump_viewer`.
3. Look for processes with large heaps.
4. Look for processes with many messages.
5. Look for large ETS tables.

# Context & Application

Memory exhaustion (`eheap_alloc: Cannot allocate ... bytes of memory`) is described as "one of the more common reasons for Erlang to terminate." This makes memory profiling a critical skill for Erlang operations.

The guide highlights an important subtlety: the system can enter a state where `erlang:memory(total)` is very different from OS-reported memory. This discrepancy is due to internal fragmentation within the Erlang run-time system's memory allocators. The raw allocator data from `erlang:system_info(allocator)` is described as "hard to read," but the third-party tool `recon_alloc` can extract useful information from these statistics.

# Examples

**Example 1** (profiling.md, "Memory profiling"): The source shows the common error message that triggers memory investigation: `eheap_alloc: Cannot allocate 1234567890 bytes of memory (of type "heap").`

**Example 2** (profiling.md, "Memory profiling"): The source describes using `crashdump_viewer` after an out-of-memory termination, looking for "processes with large heaps or many messages, large ETS tables, and so on."

**Example 3** (profiling.md, "Memory profiling"): The source describes the memory fragmentation scenario where `erlang:memory(total)` disagrees with OS-reported memory, and recommends `recon_alloc` to extract useful information from the raw allocator statistics.

# Relationships

## Builds Upon
- **profiling-strategy** -- memory profiling is one dimension of the overall profiling strategy

## Enables
- Diagnosis and resolution of memory exhaustion issues

## Related
- **tprof** -- tprof can measure heap allocations per function call, complementing system-level memory profiling
- **large-system-profiling** -- memory issues often manifest in large systems

## Contrasts With
- No direct contrasts in source. Memory profiling is distinct from time-based profiling but complementary.

# Common Errors

- **Error**: Relying solely on `erlang:memory(total)` to understand memory usage.
  **Correction**: Internal fragmentation can cause this value to differ significantly from OS-reported memory. Use `erlang:system_info(allocator)` or `recon_alloc` to investigate fragmentation.

- **Error**: Only checking process heaps and ignoring ETS tables and message queues.
  **Correction**: Large ETS tables and processes with many queued messages are also common sources of memory consumption.

# Common Confusions

- **Confusion**: Thinking `erlang:memory(total)` should match the OS-reported memory for the BEAM process.
  **Clarification**: Internal fragmentation within the Erlang run-time system can cause a significant discrepancy between these values. This does not indicate a bug.

- **Confusion**: Believing memory profiling requires the same tools as CPU profiling (fprof, eprof).
  **Clarification**: Memory profiling uses different functions and tools (`erlang:memory/0`, `instrument`, `process_info`, `crashdump_viewer`). fprof records garbage collection but not general memory usage.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "Memory profiling" section. References `crashdump_viewer`, `erlang:memory/0`, `instrument`, `process_info/2`, `erlang:port_info/2`, `ets:info/1`, `erlang:system_info(allocator)`, and `recon_alloc`.

# Verification Notes

- Definition: Synthesized from the source's "Memory profiling" section, which describes both crash analysis and running-system approaches.
- Key Properties: All functions and tools explicitly mentioned in source.
- Confidence: HIGH -- the source provides explicit tool listings and methodology.
- Cross-references: tprof, large-system-profiling slugs correspond to cards in this extraction.
- Uncertainties: None.
