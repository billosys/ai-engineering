---
concept: Erlang's Memory Model
slug: erlang-memory-model
category: performance
subcategory: memory
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Erlang's Memory Model"
extraction_confidence: high
aliases:
  - "BEAM memory allocators"
  - "Allocator hierarchy"
prerequisites: []
related:
  - allocation-strategy
  - mbcs-pool
  - memory-fragmentation
  - refc-binary
contrasts_with: []
answers_questions:
  - "How are the BEAM sub-allocators related to mseg_alloc and sys_alloc?"
  - "What are multiblock and single block carriers?"
---

# Quick Definition

Erlang's memory model is a hierarchical allocator system: two top-level allocators (`mseg_alloc`, `sys_alloc`) supply memory to nine `alloc_util` sub-allocators, each of which carves memory into multiblock and single block carriers, with one instance of each sub-allocator per scheduler.

# Core Definition

From section "Erlang's Memory Model": "Erlang's memory model, for the entire virtual machine, is hierarchical. There are two main allocators, and a bunch of sub-allocators (numbered 1-9). The sub-allocators are the specific allocators used directly by Erlang code and the VM for most data types." Each sub-allocator requests memory from `mseg_alloc` and `sys_alloc`. By default there is one instance of each sub-allocator per scheduler (one scheduler per core), plus one for linked-in drivers using async threads.

# Prerequisites

This is a foundational concept within this source's memory chapter — it has no prerequisites within this source, though it is itself a prerequisite for the fragmentation and allocation-strategy material.

# Key Properties

1. Two top-level allocators: `mseg_alloc` and `sys_alloc`; an optional *super carrier* (since R16B03) can pre-allocate and cap all VM memory.
2. Nine `alloc_util` sub-allocators: `temp_alloc`, `eheap_alloc`, `binary_alloc`, `ets_alloc`, `driver_alloc`, `sl_alloc`, `ll_alloc`, `fix_alloc`, `std_alloc`.
3. `eheap_alloc` holds process heaps; `binary_alloc` holds refc binaries (their "global heap"); `ets_alloc` holds ETS data; `ll_alloc` holds Erlang code and the atom table.
4. One instance of each sub-allocator exists per scheduler, plus one for async-thread drivers.
5. Multiblock carriers (`mbcs`) hold many terms at once — about 8 MB by default, configurable.
6. When an allocation exceeds the single block carrier threshold (`sbct`), it goes into a single block carrier (`sbcs`) of its own.
7. Single block carriers use `mseg_alloc` for the first `mmsbc` entries, then switch to `sys_alloc`.
8. `mseg_alloc` keeps reclaimed carriers in memory for a while so the next allocation spike can reuse them.

# Construction / Recognition

This is a structural model, not a procedure. To inspect it in practice, `recon_alloc:memory(allocated_types)` reports which util allocator holds the most memory; `recon_alloc:fragmentation/1` reports per-allocator usage ratios. The complete map of which data type lives in which allocator is in `erts/emulator/beam/erl_alloc.types`.

# Context & Application

Understanding this model is the precondition for diagnosing memory fragmentation and for deciding whether and how to tune allocation strategies. It explains why refc binaries (`binary_alloc`) and process heaps (`eheap_alloc`) are separate, and why ETS (`ets_alloc`) memory is isolated and un-collected.

# Examples

From section "The Global Level": "`binary_alloc`: the allocator used for reference counted binaries (what their 'global heap' is). Reference counted binaries stored in an ETS table remain in this allocator." And: "For each `mbc`, the VM will set aside a given amount of memory (about 8MB by default in our case ...), and each term allocated will be free to go look into the many multiblock carriers to find some decent space in which to reside."

# Relationships

## Builds Upon
Nothing within this source — it is the structural foundation of the memory chapter.

## Enables
- `allocation-strategy` — strategies operate on the carriers defined here.
- `mbcs-pool` — the pool is a per-allocator feature of this model.
- `memory-fragmentation` — fragmentation is a pathology of carriers.

## Related
- `refc-binary` — refc binaries are allocated by the `binary_alloc` sub-allocator.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Treating "Erlang memory" as one pool; it is nine sub-allocators, each per-scheduler, fed by two top-level allocators.

# Common Confusions

- `mseg_alloc`/`sys_alloc` are the *suppliers*; the nine `alloc_util` sub-allocators are the *consumers* that hand memory to Erlang terms (R7).
- A multiblock carrier holds many terms; a single block carrier holds exactly one large term that exceeded `sbct`.

# Source Reference

Chapter 7: Memory Leaks, Section "Erlang's Memory Model" (subsection "The Global Level"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Erlang's Memory Model."
- Confidence rationale: high — the source describes the hierarchy in detail.
- Uncertainties: none.
- Cross-reference status: Verified
