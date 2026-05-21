---
concept: Process Memory Layout
slug: process-memory-layout
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
  - "Per-process heap and stack"
  - "Generational GC layout"
prerequisites:
  - erlang-memory-model
related:
  - refc-binary
  - gc-system-monitor
contrasts_with: []
answers_questions:
  - "How is an individual Erlang process's memory laid out?"
  - "What triggers a minor versus a full-sweep garbage collection?"
---

# Quick Definition

An Erlang process's memory is a single region with the heap growing from one end and the stack from the other; it also holds an old heap and a virtual binary heap, and runs generational garbage collection — minor GCs that promote survivors to the old heap, and periodic full-sweep GCs.

# Core Definition

From section "Erlang's Memory Model," subsection "The Process Level": each process has a region with the heap on one end and the stack on the other. In practice there is more — an old heap and a new heap for generational GC, and a virtual binary heap to account for the space of reference-counted binaries (in `binary_alloc`, not `eheap_alloc`). Memory is allocated until the stack or heap cannot fit, triggering a minor GC: it moves data worth keeping into the old heap, collects the rest, and may reallocate more space. After a number of minor GCs and/or reallocations, a full-sweep GC inspects both heaps and frees more space.

# Prerequisites

- `erlang-memory-model` — the per-process layout sits inside the `eheap_alloc` sub-allocator of the global model.

# Key Properties

1. Heap and stack occupy opposite ends of one memory region and grow toward each other.
2. Generational GC uses a new heap and an old heap.
3. A virtual binary heap accounts for refc-binary size, even though that memory lives in `binary_alloc`.
4. A minor GC fires when the heap or stack can no longer fit; it promotes survivors to the old heap.
5. After a number of minor GCs/reallocations, a full-sweep GC inspects both new and old heaps.
6. When a process dies, stack and heap are freed at once and refc-binary counters are decremented.
7. Over 80% of the time freed memory is just marked available in the sub-allocator; only when memory and its multiblock carrier are fully unused is it returned to `mseg_alloc`/`sys_alloc`.

# Construction / Recognition

This is a structural model. It explains GC behaviour observed via the `gc-system-monitor` (`long_gc`, `large_heap`) and the spiky-memory phenomenon. No procedure — it is invoked when reasoning about why a process garbage collects or grows.

# Context & Application

This layout explains the refc-binary leak: a process that grows a large heap and then handles binaries may GC rarely because the virtual binary heap, though it accounts for binary size, still permits long delays between collections. It also explains why killing or hibernating a process is an effective binary-leak fix — death frees everything at once.

# Examples

From section "Erlang's Memory Model," subsection "The Process Level": the region is depicted as `[heap   ||    stack]`, and "After a given number of minor GCs and/or reallocations, a full-sweep GC is performed, which inspects both the new and old heaps, frees up more space."

# Relationships

## Builds Upon
- `erlang-memory-model` — the process layout is the per-process detail of the global model.

## Enables
Nothing — terminal structural card.

## Related
- `refc-binary` — the virtual binary heap accounts for refc binaries here.
- `gc-system-monitor` — monitors the GC behaviour this layout produces.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Assuming a dead process's memory returns to the OS immediately; over 80% of the time it is just marked available in the sub-allocator.

# Common Confusions

- The virtual binary heap is an accounting device, not real storage — the binary data itself lives in `binary_alloc`, separate from the process heap (`eheap_alloc`).
- Minor GC and full-sweep GC are distinct: minor GC promotes survivors to the old heap; full-sweep inspects both heaps.

# Source Reference

Chapter 7: Memory Leaks, Section "Erlang's Memory Model" (subsection "The Process Level"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Erlang's Memory Model," subsection "The Process Level."
- Confidence rationale: high — the source describes the layout and GC cycle directly.
- Uncertainties: none.
- Cross-reference status: Verified
