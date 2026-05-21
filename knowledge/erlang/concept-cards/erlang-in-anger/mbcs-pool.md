---
concept: Multiblock Carrier Pool
slug: mbcs-pool
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
  - "mbcs pool"
  - "Abandoned carriers"
prerequisites:
  - erlang-memory-model
related:
  - memory-fragmentation
  - allocation-strategy
contrasts_with: []
answers_questions:
  - "What is the mbcs pool?"
  - "How does the VM cache mostly-empty carriers to fight fragmentation?"
---

# Quick Definition

The multiblock carrier pool (`mbcs` pool) is a per-allocator, per-scheduler feature introduced in Erlang 17.0 that caches mostly-empty ("abandoned") multiblock carriers so they can be reused or migrated rather than deallocated — a defense against memory fragmentation.

# Core Definition

From section "Erlang's Memory Model": "starting with Erlang version 17.0, each `alloc_util` allocator on each scheduler has what is called a `mbcs` pool. The `mbcs` pool is a feature used to fight against memory fragmentation on the VM. When an allocator gets to have one of its multiblock carriers become mostly empty, the carrier becomes abandoned. This abandoned carrier will stop being used for new allocations, until new multiblock carriers start being required. When this happens, the carrier will be fetched from the `mbcs` pool."

# Prerequisites

- `erlang-memory-model` — the pool is a feature of `alloc_util` allocators and multiblock carriers defined by the memory model.

# Key Properties

1. Introduced in Erlang 17.0; each `alloc_util` allocator on each scheduler has its own `mbcs` pool.
2. When a multiblock carrier becomes mostly empty it is *abandoned* — the emptiness threshold is configurable via the `acul` option.
3. An abandoned carrier stops receiving new allocations until new multiblock carriers are again needed.
4. Carriers can be fetched from the pool across multiple `alloc_util` allocators of the same type across schedulers.
5. The pool lets the VM cache mostly-empty carriers without forcing deallocation of their memory.
6. It enables migration of lightly-loaded carriers across schedulers according to need.
7. If the feature consumes too much memory it can be disabled with `+MBacul 0`.

# Construction / Recognition

This is an automatic VM feature, not something constructed by the operator. It is recognized when reasoning about why mostly-empty carriers persist in memory. It is tuned via the `acul` (abandon carrier utilization limit) option, or disabled with `+MBacul 0`.

# Context & Application

The `mbcs` pool exists specifically because abandoned carriers would otherwise be a fragmentation source: a carrier holding one tiny term cannot be returned to the OS. By pooling and migrating such carriers, the VM reuses them for later allocation spikes and shifts them between schedulers.

# Examples

From section "Erlang's Memory Model": "This allows the VM to cache mostly-empty carriers without forcing deallocation of their memory. It also enables the migration of carriers across schedulers when they contain little data, according to their needs."

# Relationships

## Builds Upon
- `erlang-memory-model` — the pool is built on multiblock carriers and per-scheduler allocators.

## Enables
Nothing — terminal feature card.

## Related
- `memory-fragmentation` — the pool is a built-in mitigation for fragmentation.
- `allocation-strategy` — another per-allocator anti-fragmentation control.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Disabling the pool (`+MBacul 0`) without cause; it is a fragmentation defense and removing it can worsen fragmentation.

# Common Confusions

- An "abandoned" carrier is not freed memory — it is a carrier kept in the pool, mostly empty, available for future reuse or cross-scheduler migration.

# Source Reference

Chapter 7: Memory Leaks, Section "Erlang's Memory Model". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Erlang's Memory Model."
- Confidence rationale: high — the source explicitly describes the feature, its version, and its config options.
- Uncertainties: none.
- Cross-reference status: Verified
