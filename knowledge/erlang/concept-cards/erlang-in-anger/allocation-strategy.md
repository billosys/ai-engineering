---
concept: Allocation Strategy
slug: allocation-strategy
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
  - "Memory allocation strategies"
  - "bf/aobf/aoff/gf/af"
prerequisites:
  - erlang-memory-model
related:
  - memory-fragmentation
  - mbcs-pool
contrasts_with: []
answers_questions:
  - "What memory allocation strategies does the BEAM offer?"
  - "When should I alter allocation strategies on my nodes?"
---

# Quick Definition

An allocation strategy is the algorithm a BEAM `alloc_util` allocator uses to pick a free memory block for an allocation; the VM offers seven strategies — `bf`, `aobf`, `aoff`, `aoffcbf`, `aoffcaobf`, `gf`, and `af` — each configurable per allocator.

# Core Definition

From section "Erlang's Memory Model": the Erlang VM has these memory allocation strategies: Best fit (`bf`), Address order best fit (`aobf`), Address order first fit (`aoff`), Address order first fit carrier best fit (`aoffcbf`), Address order first fit carrier address order best fit (`aoffcaobf`), Good fit (`gf`), and A fit (`af`). "Each of these strategies can be applied individually to every kind of allocator, so that the heap allocator and the binary allocator do not necessarily share the same strategy."

# Prerequisites

- `erlang-memory-model` — strategies operate over the carriers and blocks defined by the memory model.

# Key Properties

1. `bf` (best fit): builds a balanced binary tree of free block sizes and picks the smallest block that fits.
2. `aobf` (address order best fit): like `bf`, but ties broken by lowest address — tends to favor the same carriers.
3. `aoff` (address order first fit): searches by address order and uses the first block that fits.
4. `aoffcbf`: first picks a carrier that can fit the size, then best-fits within that carrier.
5. `aoffcaobf`: like `aoffcbf`, but ties within a carrier broken by lowest address.
6. `gf` (good fit): works like `bf` but searches only for a limited time (configurable via `mbsd`), taking the best fit found so far.
7. `af` (a fit): for temporary data — checks one existing block, uses it if the data fits, else allocates a new one.
8. Each strategy is configurable per `alloc_util` allocator (via the `M_as` VM option).

# Construction / Recognition

Strategies are set through VM options, configured per allocator. To choose one, the operator must determine the average data size, allocation/deallocation frequency, and whether data fits in `mbcs` or `sbcs`, then test candidate strategies under realistic load. The `recon_alloc` module provides helper functions for guidance.

# Context & Application

Allocation strategies are tuned to combat memory fragmentation. The author cautions that this is "a very long process for which there is no shortcut," requiring in-depth testing. (PR4: alter allocation strategies only after a thorough understanding of the load, and prefer fixing code over tuning allocators where possible.)

# Examples

From section "Erlang's Memory Model": "For best fit (`bf`), the VM builds a balanced binary tree of all the free blocks' sizes, and will try to find the smallest one that will accommodate the piece of data and allocate it there." And for `aoff`: "will favor the address order for its search, and as soon as a block fits, `aoff` uses it."

# Relationships

## Builds Upon
- `erlang-memory-model` — strategies act on its carriers.

## Enables
Nothing — terminal tuning card.

## Related
- `memory-fragmentation` — the problem allocation strategies are tuned to fix.
- `mbcs-pool` — another anti-fragmentation feature of the same allocators.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Changing strategies without first characterizing the node's data sizes and allocation patterns.
- Tuning allocators when rewriting the offending code would be the better fix (PR4).

# Common Confusions

- "Best fit" minimizes wasted space per allocation; "first fit" variants minimize search time and favor low addresses — they are different goals, not just different speeds.
- A strategy is per-allocator: the heap allocator and binary allocator can run different strategies.

# Source Reference

Chapter 7: Memory Leaks, Section "Erlang's Memory Model". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Erlang's Memory Model."
- Confidence rationale: high — the source enumerates and explains every strategy.
- Uncertainties: none.
- Cross-reference status: Verified
