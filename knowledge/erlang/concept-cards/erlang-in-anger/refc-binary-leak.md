---
concept: Refc Binary Leak
slug: refc-binary-leak
category: anti-patterns
subcategory: binaries
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Binaries"
extraction_confidence: high
aliases:
  - "Binary memory leak"
  - "Reference-counted binary leak"
prerequisites:
  - refc-binary
related:
  - refc-binary-leak-detection
  - refc-binary-leak-fixes
  - routing-binaries-pattern
contrasts_with:
  - memory-fragmentation
answers_questions:
  - "Why do reference-counted binaries leak?"
  - "What kind of process is prone to a binary memory leak?"
---

# Quick Definition

A refc binary leak is the accumulation of reference-counted binary memory caused by processes that garbage collect too rarely, so the refcounts of binaries they reference are never decremented to zero and the binary heap grows.

# Core Definition

From section "Binaries": the refc-binary mechanism works fine in 99% of cases, but in some cases a process will either "do too little work to warrant allocations and garbage collection," or "eventually grow a large stack or heap with various data structures, collect them, then get to work with a lot of refc binaries." In the latter case, refilling the heap with binaries — even though a virtual heap accounts for the refc binaries' real size — can take a long time, giving long delays between garbage collections. Because a refc binary is freed only when all references are garbage-collected from all processes, infrequent GC means binary memory is never reclaimed.

# Prerequisites

- `refc-binary` — you must understand reference counting and the global binary heap before you can understand why it leaks.

# Key Properties

1. The leak is in the global binary heap (`binary_alloc`), not on any process's own heap.
2. Root cause: a process garbage collects too rarely to decrement binary refcounts.
3. Two prone profiles: processes that do too little work to trigger GC, and processes that grow a large heap, collect it, then start handling many binaries.
4. The virtual binary heap accounts for refc-binary size but cannot force timely collection.
5. The leak is per-process behaviour even though the leaked memory is global — a few processes can hold hundreds of thousands of binaries.

# Construction / Recognition

This is an anti-pattern recognized, not constructed. It is recognized by detecting that binary memory grows, then using `recon:bin_leak/1` to confirm that processes are holding large numbers of unreclaimed refc binaries (see `refc-binary-leak-detection`).

# Context & Application

This trap appears in long-lived processes that handle binaries intermittently — routers, parsers, connection handlers that idle between bursts. The author notes investigations at Heroku where "some processes hold hundreds of thousands of them" — a clear sign of a problem.

# Examples

From section "Binaries," footnote: "We've seen some processes hold hundreds of thousands of them during leak investigations at Heroku!"

# Relationships

## Builds Upon
- `refc-binary` — the leak is a failure mode of the reference-counting mechanism.

## Enables
- `refc-binary-leak-detection`, `refc-binary-leak-fixes` — diagnosis and remediation.

## Related
- `routing-binaries-pattern` — a specific binary-leak scenario and its fix.

## Contrasts With
- `memory-fragmentation` — a binary leak grows real Erlang-term binary memory; fragmentation is unused memory the OS still holds.

# Common Errors

- Assuming refc binaries are always reclaimed promptly; an idle or rarely-collecting process never triggers the GC that would free them.
- Looking only at process heaps and missing that the leaked memory is in the global binary allocator.

# Common Confusions

- A refc binary leak is not a true "leak" in the C sense — the memory is still reachable and will be freed once GC runs; it is a leak of *timeliness*, which is why forcing GC fixes it.

# Source Reference

Chapter 7: Memory Leaks, Section "Binaries". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted and synthesized from section "Binaries."
- Confidence rationale: high — the source explicitly describes the two leak-prone process profiles.
- Uncertainties: none.
- Cross-reference status: Verified
