---
concept: erts_alloc Memory Allocator Library
slug: erts-alloc
category: performance
subcategory: memory-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erts_alloc"
chapter_number: null
pdf_page: null
section: "Description / Allocators"
extraction_confidence: high
aliases:
  - "erts_alloc"
  - "ERTS memory allocators"
  - "Erlang memory allocator"
prerequisites: []
extends: []
related:
  - memory-carriers
  - allocator-tuning
  - crash-dump
contrasts_with: []
answers_questions:
  - "What is erts_alloc?"
  - "How does erts_alloc relate to process heaps and ETS storage?"
  - "What memory allocators does the Erlang runtime use?"
---

# Quick Definition

`erts_alloc` is the Erlang runtime system's internal memory allocator library. It provides multiple specialized allocators -- each dedicated to a specific type of data (process heaps, binaries, ETS, drivers, etc.) -- to reduce memory fragmentation by separating differently-used memory blocks into different memory areas.

# Core Definition

The ERTS documentation states: "`erts_alloc` is an Erlang runtime system internal memory allocator library. `erts_alloc` provides the Erlang runtime system with a number of memory allocators." (erts_alloc, Description).

The following allocators are present:

- **`temp_alloc`** -- Temporary allocations (always enabled, cannot be disabled)
- **`eheap_alloc`** -- Erlang heap data, such as Erlang process heaps
- **`binary_alloc`** -- Erlang binary data
- **`ets_alloc`** -- ETS table data
- **`driver_alloc`** -- Driver data
- **`literal_alloc`** -- Constant terms in Erlang code (always enabled)
- **`sl_alloc`** -- Memory blocks expected to be short-lived
- **`ll_alloc`** -- Memory blocks expected to be long-lived (e.g., Erlang code)
- **`fix_alloc`** -- Fast allocator for frequently used fixed-size data types
- **`std_alloc`** -- Most memory blocks not handled by other allocators
- **`sys_alloc`** -- The default OS `malloc` implementation (always enabled)
- **`mseg_alloc`** -- Memory segment allocator using `mmap`; used by other allocators to allocate segments

The source explains the design rationale: "The main idea with the `erts_alloc` library is to separate memory blocks that are used differently into different memory areas, to achieve less memory fragmentation. By putting less effort in finding a good fit for memory blocks that are frequently allocated than for those less frequently allocated, a performance gain can be achieved."

# Prerequisites

None -- this is a foundational ERTS subsystem.

# Key Properties

1. Multiple specialized allocators, each for a different data type (heaps, binaries, ETS, drivers, etc.)
2. `sys_alloc`, `literal_alloc`, and `temp_alloc` are always enabled and cannot be disabled
3. `mseg_alloc` is always enabled if available (requires `mmap`) and is used by other allocators
4. All other allocators can be enabled or disabled; disabled allocators fall back to `sys_alloc`
5. By default, all allocators are enabled
6. Most allocators use the `alloc_util` framework internally (except `sys_alloc` and `mseg_alloc`)
7. Each allocator manages memory in carriers (multiblock or singleblock)
8. `mseg_alloc` maintains a segment cache to reduce system calls
9. Per-scheduler thread instances reduce lock contention (default: `NoSchedulers+1` instances)
10. Allocator status and settings are inspectable via `erlang:system_info(allocator)` and `erlang:system_info({allocator, Alloc})`

# Construction / Recognition

## To Construct/Create:

`erts_alloc` is built into the runtime and configured via command-line flags:

```text
erl +MHe true       # enable eheap_alloc (H = eheap_alloc)
erl +MEe true       # enable ets_alloc   (E = ets_alloc)
erl +Mea max        # enable all allocators (default)
erl +Mea min        # disable all allocators that can be disabled
```

Allocator letter codes:
- B: binary_alloc, D: std_alloc, E: ets_alloc, F: fix_alloc
- H: eheap_alloc, I: literal_alloc, L: ll_alloc, M: mseg_alloc
- R: driver_alloc, S: sl_alloc, T: temp_alloc, Y: sys_alloc

## To Identify/Recognize:

1. Command-line flags starting with `+M`
2. `erlang:system_info(allocator)` or `erlang:system_info({allocator, Alloc})` calls
3. Memory allocation categories in crash dumps and `instrument` module output

# Context & Application

Understanding `erts_alloc` is essential for diagnosing memory issues in production Erlang systems. The separation of allocators by data type means that:

- Process heap memory issues show up in `eheap_alloc`
- Binary leaks show up in `binary_alloc`
- ETS memory growth shows up in `ets_alloc`
- Driver memory issues show up in `driver_alloc`

This separation allows targeted diagnosis and tuning. For example, if `binary_alloc` shows high fragmentation, you can tune its allocation strategy or carrier sizes without affecting other allocators.

Pre-allocators exist for frequently used fixed-size data types, providing faster allocation at the cost of a fixed memory reservation at startup.

# Examples

**Example 1** (erts_alloc, Allocators): The full list of allocators showing the design philosophy of separating memory by use:

```text
eheap_alloc  - Erlang process heaps
binary_alloc - Erlang binary data
ets_alloc    - ETS data
driver_alloc - Driver data
literal_alloc - Constant terms in Erlang code
sl_alloc     - Short-lived memory blocks
ll_alloc     - Long-lived memory blocks (e.g., Erlang code)
fix_alloc    - Frequently used fixed size data types
std_alloc    - Everything else
temp_alloc   - Temporary allocations
```

**Example 2** (erts_alloc, Allocators): The `mseg_alloc` description:

"A memory segment allocator. It is used by other allocators for allocating memory segments and is only available on systems that have the `mmap` system call. Memory segments that are deallocated are kept for a while in a segment cache before they are destroyed. When segments are allocated, cached segments are used if possible instead of creating new segments. This to reduce the number of system calls made."

# Relationships

## Related

- **memory-carriers** -- Allocators manage memory through carriers (multiblock and singleblock)
- **allocator-tuning** -- Allocators are configured via `+M` command-line flags
- **crash-dump** -- Crash dumps contain allocator statistics useful for post-mortem analysis

# Common Errors

- **Error**: Disabling allocators (e.g., `+Mea min`) without understanding the performance impact
  **Correction**: When allocators are disabled, all allocation falls back to `sys_alloc`, losing the benefits of specialized allocation strategies and increasing fragmentation

- **Error**: Not checking allocator status when diagnosing memory issues
  **Correction**: Use `erlang:system_info({allocator, Alloc})` to inspect current settings and status of each allocator

# Common Confusions

- **Confusion**: Thinking `erts_alloc` is a single allocator
  **Clarification**: It is a library containing multiple specialized allocators, each optimized for different memory usage patterns

- **Confusion**: Assuming process memory only comes from `eheap_alloc`
  **Clarification**: Process heaps use `eheap_alloc`, but binaries referenced by a process use `binary_alloc`, and ETS tables owned by a process use `ets_alloc`

- **Confusion**: Believing `sys_alloc` and `mseg_alloc` use the `alloc_util` framework
  **Clarification**: These two allocators do NOT use `alloc_util`; the carrier and strategy concepts do not apply to them

# Source Reference

- "erts_alloc" reference (Description, Allocators, The alloc_util Framework sections)
- "erts_alloc" reference (System Flags Effecting erts_alloc)

# Verification Notes

- Definition: Directly quoted from erts_alloc.md Description
- Allocator list: Complete list from erts_alloc.md Allocators section
- Design rationale: Directly quoted from source
- Confidence: HIGH -- the allocator library is thoroughly documented with all allocators listed
