---
concept: recon_alloc:memory
slug: recon-alloc-memory
category: performance
subcategory: memory
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Memory"
extraction_confidence: high
aliases:
  - "recon_alloc:memory/1"
  - used allocated unused usage
prerequisites:
  - vm-memory-reporting
extends:
  - vm-memory-reporting
related:
  - memory-fragmentation
contrasts_with:
  - vm-memory-reporting
answers_questions:
  - "How do I get a global view of memory?"
  - "Why does the OS report more memory than erlang:memory()?"
---

# Quick Definition

`recon_alloc:memory/1` reports memory by digging into the VM's allocators, distinguishing memory *used* by Erlang data from memory *allocated* (reserved) by the VM — the latter being the figure relevant to OS limits like `ulimit`.

# Core Definition

"If you want the total amount of memory owned by the virtual machine, as in the amount that will trip system limits (`ulimit`), this value is more difficult to get from within the VM... Fortunately, recon has the function `recon_alloc:memory/1` to figure it out" (Chapter 5, "Memory").

# Prerequisites

- `vm-memory-reporting`: `recon_alloc:memory/1` complements `erlang:memory()` by exposing the reserved-vs-used distinction it lacks.

# Key Properties

1. The argument selects what is reported:
   - `used` — memory actively used for allocated Erlang data.
   - `allocated` — memory reserved by the VM (used plus reserved-but-not-yet-used); this is the value to compare against `ulimit` and OS-reported values.
   - `unused` — memory reserved by the VM but not allocated; equals `allocated - used`.
   - `usage` — a ratio 0.0..1.0 of used over allocated memory.
2. It reads the VM's memory allocators directly.
3. Additional options exist but are mostly needed only when investigating memory leaks (covered in the Memory Leaks chapter).

# Construction / Recognition

Call `recon_alloc:memory(allocated)` to get the OS-relevant total, `recon_alloc:memory(used)` for the actively-used figure, `recon_alloc:memory(unused)` for the gap, or `recon_alloc:memory(usage)` for the ratio.

# Context & Application

Used when you need to reconcile Erlang's memory view with what the operating system sees — e.g. when a node approaches a `ulimit` or when `top`/`htop` shows far more memory than `erlang:memory()`. A low `usage` ratio with high `allocated` can indicate memory fragmentation.

# Examples

From Chapter 5, "Memory": "`allocated` reports the memory that is reserved by the VM. It includes the memory used, but also the memory yet-to-be-used but still given by the OS. This is the amount you want if you're dealing with `ulimit` and OS-reported values."

# Relationships

## Builds Upon
- vm-memory-reporting

## Enables

## Related
- memory-fragmentation

## Contrasts With
- vm-memory-reporting

# Common Errors

- Confusing `used` with `allocated` — `used` is the smaller, active figure; `allocated` is what the OS has granted the VM.
- Forgetting that `usage` is a ratio (0.0..1.0), not a percentage or a byte count.

# Common Confusions

- `recon_alloc:memory/1` is not the same as `erlang:memory()`: the former exposes allocator reservations the latter cannot see.
- `unused` memory is not a leak — it is reserved capacity the VM holds for future allocation.

# Source Reference

Chapter 5: Runtime Metrics, Section "Memory". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — all four argument values explicitly defined.
- Uncertainties: none.
- Cross-reference status: Verified
