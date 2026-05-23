---
concept: Memory Carriers
slug: memory-carriers
category: performance
subcategory: memory-management
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erts_alloc"
chapter_number: null
pdf_page: null
section: "The alloc_util Framework"
extraction_confidence: high
aliases:
  - "multiblock carrier"
  - "singleblock carrier"
  - "alloc_util framework"
  - "MBC"
  - "SBC"
prerequisites:
  - erts-alloc
extends:
  - erts-alloc
related:
  - allocator-tuning
contrasts_with: []
answers_questions:
  - "What distinguishes multi-block carriers from single-block carriers?"
  - "How does the alloc_util framework manage memory?"
  - "What allocation strategies are available?"
---

# Quick Definition

Memory carriers are the memory regions that `alloc_util`-based allocators manage. There are two types: multiblock carriers (MBCs) hold multiple smaller memory blocks and use allocation strategies like best fit or good fit; singleblock carriers (SBCs) hold one large block each. Blocks larger than the singleblock carrier threshold (`sbct`) go into SBCs; smaller blocks go into MBCs.

# Core Definition

The ERTS documentation states: "Internally a framework called `alloc_util` is used for implementing allocators. `sys_alloc` and `mseg_alloc` do not use this framework." (erts_alloc, The alloc_util Framework).

The carrier system works as follows:

- "An allocator manages multiple areas, called carriers, in which memory blocks are placed. A carrier is either placed in a separate memory segment (allocated through `mseg_alloc`), or in the heap segment (allocated through `sys_alloc`)."
- "Multiblock carriers are used for storage of several blocks."
- "Singleblock carriers are used for storage of one block."
- "Blocks that are larger than the value of the singleblock carrier threshold (`sbct`) parameter are placed in singleblock carriers."
- "Blocks that are smaller than the value of parameter `sbct` are placed in multiblock carriers."

Each allocator normally creates a "main multiblock carrier" that is never deallocated, sized by the `mmbcs` parameter. Additional MBCs allocated through `mseg_alloc` grow from `smbcs` (smallest) to `lmbcs` (largest) over `mbcgs` growth stages.

Free block coalescing is performed immediately using boundary tags (headers and footers), achieving constant time complexity.

# Prerequisites

- **erts-alloc** -- Carriers are the internal structure of the allocator library

# Key Properties

1. Two carrier types: multiblock (multiple blocks) and singleblock (one block)
2. The `sbct` parameter determines the threshold: blocks >= `sbct` get SBCs, blocks < `sbct` get MBCs
3. The main multiblock carrier is never deallocated; its size is set by `mmbcs`
4. MBC sizes grow from `smbcs` to `lmbcs` over `mbcgs` growth stages
5. Carriers are allocated either through `mseg_alloc` (memory segments via `mmap`) or `sys_alloc` (heap via `malloc`)
6. SBCs allocated through `mseg_alloc` are sized to whole pages
7. Free block coalescing uses boundary tags for constant-time complexity
8. Abandoned carriers can migrate between allocator instances when utilization drops below `acul`
9. Carrier pools allow memory carriers to migrate between allocator instances sharing the same pool

# Construction / Recognition

## To Construct/Create:

Carriers are managed internally by `alloc_util`. Configuration is via `+M` flags:

```text
erl +MHsbct 512       # eheap_alloc singleblock carrier threshold: 512 KB
erl +MHmmbcs 1024     # eheap_alloc main multiblock carrier size: 1024 KB
erl +MHsmbcs 256      # eheap_alloc smallest mseg MBC size: 256 KB
erl +MHlmbcs 10240    # eheap_alloc largest mseg MBC size: 10240 KB
erl +MHmbcgs 10       # eheap_alloc MBC growth stages: 10
```

## To Identify/Recognize:

1. Output from `erlang:system_info({allocator, Alloc})` shows carrier counts and sizes
2. Crash dump allocator sections show MBC and SBC statistics
3. The `instrument` module can be used with `+M<S>atags true` to inspect allocation tags

# Context & Application

The carrier architecture is central to understanding ERTS memory behavior. Key implications:

**Fragmentation**: Even when Erlang processes free memory, carriers may not be returned to the OS if they still contain any allocated blocks. This is the primary cause of "memory not returned to OS" issues in production.

**Carrier abandonment**: When utilization of an MBC drops below the `acul` threshold, the carrier is "abandoned" -- no new allocations are made in it. When another allocator instance needs memory, it first tries to fetch an abandoned carrier before creating a new one. This feature requires specific allocation strategies (`aoff`, `aoffcbf`, `aoffcaobf`, `ageffcaoff`, `ageffcbf`, `ageffcaobf`) and multiple thread-specific instances.

**Super carriers**: The `+MMscs` flag creates a large contiguous virtual address space region where `mseg_alloc` preferentially creates carriers. This can improve memory locality and enable large page support (`+MMlp`).

# Examples

**Example 1** (erts_alloc, The alloc_util Framework): MBC growth formula:

"If `nc` is the current number of multiblock carriers (the main multiblock carrier excluded) managed by an allocator, the size of the next `mseg_alloc` multiblock carrier allocated by this allocator is roughly `smbcs+nc*(lmbcs-smbcs)/mbcgs` when `nc <= mbcgs`, and `lmbcs` when `nc > mbcgs`."

**Example 2** (erts_alloc, The alloc_util Framework): The available allocation strategies:

- **Best fit** -- Find the smallest block satisfying the request (balanced BST, O(log N) by number of sizes)
- **Address order best fit** -- Smallest block, lowest address if tied (O(log N) by number of blocks)
- **Address order first fit** -- Lowest address satisfying request (O(log N))
- **Good fit** -- Try to find best fit with limited search depth (constant time with default depth 3)
- **A fit** -- Inspect only one block (constant time, only for `temp_alloc`)
- Plus carrier-level strategies: `aoffcbf`, `aoffcaobf`, `ageffcaoff`, `ageffcbf`, `ageffcaobf`

**Example 3** (erts_alloc, Flags): Carrier abandonment configuration:

"Carriers are abandoned when memory utilization in the allocator instance falls below the utilization value used. Once a carrier is abandoned, no new allocations are made in it. When an allocator instance gets an increased multiblock carrier need, it first tries to fetch an abandoned carrier from another allocator instance."

# Relationships

## Builds Upon

- **erts-alloc** -- Carriers are the internal structure managed by the allocator library

## Related

- **allocator-tuning** -- Carrier sizes, thresholds, and strategies are the primary tuning knobs

# Common Errors

- **Error**: Setting `sbct` too low, causing many small singleblock carriers
  **Correction**: SBCs have higher per-block overhead; keep `sbct` high enough that only genuinely large allocations use SBCs

- **Error**: Not enabling carrier abandonment when running many schedulers
  **Correction**: Without abandonment (`+M<S>acul`), per-scheduler allocator instances can accumulate underutilized carriers; enable it with strategies that support it

# Common Confusions

- **Confusion**: Thinking the main multiblock carrier is deallocated when empty
  **Clarification**: The main MBC is never deallocated; it persists for the lifetime of the runtime

- **Confusion**: Believing all allocation strategies support carrier abandonment
  **Clarification**: Only `aoff`, `aoffcbf`, `aoffcaobf`, `ageffcaoff`, `ageffcbf`, and `ageffcaobf` support abandoned carriers

- **Confusion**: Thinking multiblock and singleblock refer to the number of carriers
  **Clarification**: "Multiblock" means the carrier holds multiple memory blocks; "singleblock" means it holds exactly one. The distinction is about the carrier's internal structure.

# Source Reference

- "erts_alloc" reference (The alloc_util Framework section, including carrier sizing, allocation strategies, and carrier abandonment)
- "erts_alloc" reference (Flags for Configuration of Allocators Based on alloc_util)

# Verification Notes

- Carrier definitions: Directly quoted from erts_alloc.md, The alloc_util Framework
- Growth formula: Directly quoted from source
- Strategy list: Complete list from source with time complexities
- Abandonment: Quoted from +M<S>acul flag description
- Confidence: HIGH -- carrier architecture is thoroughly documented with formulas and strategy descriptions
