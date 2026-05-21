---
concept: Tracing Principles
slug: tracing-principles
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Tracing Principles"
extraction_confidence: high
aliases:
  - "Pid specifications and trace patterns"
prerequisites:
  - tracing
related:
  - match-specification
  - recon-trace
  - erlang-tracing-tools
contrasts_with: []
answers_questions:
  - "What determines whether a given function or process gets traced?"
  - "How do pid specifications and trace patterns interact?"
---

# Quick Definition

Erlang tracing works in two parts — pid specifications (which processes to target) and trace patterns (which function calls to match); a call is traced only if it lies in the intersection of both.

# Core Definition

From section "Tracing Principles": "The Erlang Trace BIFs allow to trace any Erlang code at all. They work in two parts: pid specifications, and trace patterns. Pid specifications lets the user decide which processes to target. They can be specific pids, `all` pids, `existing` pids, or `new` pids (those not spawned at the time of the function call). The trace patterns represent functions ... What defines whether a specific function call gets traced or not is the intersection of both. If either the pid specification excludes a process or a trace pattern excludes a given call, no trace will be received."

# Prerequisites

- `tracing` — the principles describe how the tracing facility decides what to record.

# Key Properties

1. Tracing has two independent parts: pid specifications and trace patterns.
2. Pid specifications: a specific pid, `all`, `existing`, or `new` (processes not yet spawned at call time).
3. Trace patterns specify functions in two parts — module/function/arity, plus match specifications constraining arguments.
4. A call is traced only at the intersection of matching pids and matching patterns (a Venn diagram).
5. If either side excludes a call, no trace is produced.
6. `dbg` and the trace BIFs force you to reason about this Venn diagram explicitly; `redbug` and `recon_trace` abstract it away.

# Construction / Recognition

1. Decide the pid specification — specific pids, `all`, `existing`, or `new`.
2. Decide the trace pattern — module/function/arity, optionally narrowed with match specifications.
3. The traced set is the intersection: tighten either side to narrow what you receive.

# Context & Application

This model underlies every Erlang tracing tool. Understanding it (R4) explains why a trace produces nothing — usually because the pid spec or the pattern excluded the calls — and guides how to scope a trace narrowly and safely.

# Examples

From section "Tracing Principles": "If either the pid specification excludes a process or a trace pattern excludes a given call, no trace will be received. Tools like `dbg` (and trace BIFs) force you to work with this Venn diagram in mind."

# Relationships

## Builds Upon
- `tracing` — the principles govern the tracing facility.

## Enables
- `match-specification` — match specs are how trace patterns constrain arguments.
- `recon-trace` — `recon_trace` is built on these principles, with the Venn diagram abstracted.

## Related
- `erlang-tracing-tools` — `dbg`/BIFs expose this model directly.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Setting a pid spec or trace pattern that excludes the calls of interest, then concluding tracing "does not work" — the empty result is the intersection being empty.

# Common Confusions

- Pid specifications and trace patterns are independent sets; only their intersection is traced — broadening one does not help if the other still excludes the call.
- `existing` and `new` pids are distinct: `existing` matches processes alive at call time, `new` matches those spawned afterward.

# Source Reference

Chapter 9: Tracing, Section "Tracing Principles". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Tracing Principles."
- Confidence rationale: high — the source explicitly describes the two-part intersection model.
- Uncertainties: none.
- Cross-reference status: Verified
