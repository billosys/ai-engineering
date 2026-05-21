---
concept: Memory Fragmentation
slug: memory-fragmentation
category: performance
subcategory: memory
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Memory Fragmentation"
extraction_confidence: high
aliases:
  - "Allocator fragmentation"
prerequisites:
  - erlang-memory-model
related:
  - allocation-strategy
  - mbcs-pool
  - vm-memory-reporting
contrasts_with:
  - memory-leak-detection
answers_questions:
  - "What is memory fragmentation?"
  - "How do I find out a node is suffering from fragmentation?"
  - "How do I tell a leak from fragmentation?"
---

# Quick Definition

Memory fragmentation is the condition where the Erlang VM has obtained large amounts of memory from the OS but cannot fully reuse it for new Erlang terms, so the OS reports much higher memory use than `erlang:memory()` does.

# Core Definition

From section "Memory Fragmentation": fragmentation "is by far one of the trickiest issues of running long-lived Erlang nodes (often when individual node uptime reaches many months), and will show up relatively rarely." The general symptoms are "large amounts of memory being allocated during peak load, and that memory not going away after the fact. The damning factor will be that the node will internally report much lower usage (through `erlang:memory()`) than what is reported by the operating system." The `recon_alloc` module was developed specifically to detect and help resolve such issues.

# Prerequisites

- `erlang-memory-model` — fragmentation is a property of carriers and sub-allocators, so the memory model must be understood first.

# Key Properties

1. The defining symptom: OS-reported memory greatly exceeds `erlang:memory()`.
2. Memory is allocated during a peak load and never released afterward.
3. It mainly afflicts long-lived nodes — often after months of uptime — and is rare.
4. `recon_alloc:memory(usage)` returns 0–1: a value near 100% means no fragmentation, just heavy use.
5. `recon_alloc:memory(allocated)` should closely match the OS figure if the issue is fragmentation or an Erlang-term leak.
6. `recon_alloc:fragmentation(current)` vs `recon_alloc:fragmentation(max)` reveals fragmentation triggered by usage spikes.

# Construction / Recognition

1. Call `recon_alloc:memory(usage)` — if close to 1.0, there is no fragmentation, only heavy usage.
2. Check that `recon_alloc:memory(allocated)` matches the OS figure (confirms fragmentation or Erlang-term leak rather than NIF/driver leak).
3. Call `recon_alloc:memory(allocated_types)` to find which util allocator holds the most memory.
4. Compare `recon_alloc:fragmentation(current)` with `recon_alloc:fragmentation(max)`; a big difference points to spike-driven fragmentation in specific allocator types.

# Context & Application

Fragmentation appears on nodes with bursty, varied allocation patterns — peak loads that allocate many differently-sized terms which leave carriers partly empty and unreclaimable. Remediation is to tune allocation strategies, a long, test-heavy process.

# Examples

From section "Finding Fragmentation": "call `recon_alloc:memory(usage)`. This will return a value between 0 and 1 representing a percentage of memory that is being actively used by Erlang terms versus the memory that the Erlang VM has obtained from the OS for such purposes. If the usage is close to 100%, you likely do not have memory fragmentation issues. You're just using a lot of it."

# Relationships

## Builds Upon
- `erlang-memory-model` — fragmentation is a carrier/allocator phenomenon.

## Enables
- `allocation-strategy` — choosing a different strategy is the remediation for fragmentation.

## Related
- `mbcs-pool` — the VM feature designed to fight fragmentation.
- `vm-memory-reporting` — the gap between VM-reported and OS-reported memory is the diagnostic signal.

## Contrasts With
- `memory-leak-detection` — a leak grows live Erlang-term memory (visible in `erlang:memory()`); fragmentation is dead space the OS still holds but `erlang:memory()` does not count (DG4).

# Common Errors

- Confusing high usage with fragmentation — `recon_alloc:memory(usage)` near 1.0 means the node simply needs more memory.
- Concluding fragmentation without checking that `recon_alloc:memory(allocated)` matches the OS — otherwise a NIF/driver leak could be the cause.

# Common Confusions

- Fragmentation vs leak: a leak shows growth in `erlang:memory()`; fragmentation shows a gap between `erlang:memory()` and OS figures with no growth in live terms.
- Fragmentation vs NIF/driver leak: if `recon_alloc:memory(allocated)` does *not* match the OS, suspect a NIF or driver instead.

# Source Reference

Chapter 7: Memory Leaks, Section "Memory Fragmentation". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Memory Fragmentation."
- Confidence rationale: high — the source explicitly defines symptoms and diagnostics.
- Uncertainties: none.
- Cross-reference status: Verified
