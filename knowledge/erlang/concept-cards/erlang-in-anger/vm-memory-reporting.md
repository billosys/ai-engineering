---
concept: VM Memory Reporting
slug: vm-memory-reporting
category: performance
subcategory: memory
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Memory"
extraction_confidence: high
aliases:
  - "erlang:memory()"
  - memory types
prerequisites:
  - runtime-introspection
extends: []
related:
  - recon-alloc-memory
  - refc-binary
contrasts_with:
  - recon-alloc-memory
answers_questions:
  - "How do I get a global view of memory?"
  - "What kind of values are reported for Erlang's memory?"
  - "Why does the OS report more memory than erlang:memory()?"
---

# Quick Definition

`erlang:memory()` reports how much memory the Erlang VM has *allocated* (actively used), broken down by category (processes, system, atoms, binary, code, ETS) — a global, in-VM view of memory consumption.

# Core Definition

"The memory reported by the Erlang VM in most tools will be a variant of what is reported by `erlang:memory()`" (Chapter 5, "Memory").

"All the values returned are in bytes, and they represent memory *allocated* (memory actively used by the Erlang VM, not the memory set aside by the operating system for the Erlang VM). It will sooner or later look much smaller than what the operating system reports."

# Prerequisites

- `runtime-introspection`: this is the standard "in the large" memory metric.

# Key Properties

1. All values are in bytes.
2. They report *allocated* (actively used) memory, not memory reserved from the OS — so they read smaller than `top`/`htop`.
3. `total` = `processes` + `system`.
4. `processes` — memory used by Erlang processes, their stacks and heaps.
5. `processes_used` — subset of `processes` actually in use.
6. `system` — everything else: ETS tables, atoms, refc binaries, plus hidden VM data; `system` is *incomplete* unless the VM is instrumented.
7. `atom` / `atom_used`, `binary`, `code`, `ets` — further category breakdowns.
8. To get the OS-relevant total (the figure that trips `ulimit`), `erlang:memory()` is not enough — you must dig into the VM's allocators (use `recon_alloc:memory/1`).

# Construction / Recognition

Call `erlang:memory()` in a shell, or read the equivalent fields from a metrics library. To get the `ulimit`-relevant total instead, use `recon_alloc:memory(allocated)`.

# Context & Application

Used for a quick global memory breakdown and for tracking categories over time. The discrepancy with OS-reported memory is expected and is a frequent source of confusion during incident response.

# Examples

From Chapter 5, "Memory":

```erlang-repl
1> erlang:memory().
[{total,13772400},
 {processes,4390232},
 {processes_used,4390112},
 {system,9382168},
 {atom,194289},
 {atom_used,173419},
 {binary,979264},
 {code,4026603},
 {ets,305920}]
```

# Relationships

## Builds Upon
- runtime-introspection

## Enables
- recon-alloc-memory

## Related
- refc-binary

## Contrasts With
- recon-alloc-memory

# Common Errors

- Using `erlang:memory()`'s `total` to reason about `ulimit` or OS limits — it reports allocated, not reserved, memory; use `recon_alloc:memory(allocated)` instead.
- Treating `system` as a complete figure — it omits hidden data unless the VM is instrumented.

# Common Confusions

- Erlang reporting less memory than the OS is *normal*: the VM holds OS-granted memory it has not yet allocated to Erlang data.
- `total` is just `processes + system`, not the VM's full footprint.

# Source Reference

Chapter 5: Runtime Metrics, Section "Memory". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with field-by-field breakdown.
- Uncertainties: none.
- Cross-reference status: Verified
