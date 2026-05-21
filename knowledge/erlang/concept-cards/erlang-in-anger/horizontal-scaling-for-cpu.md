---
concept: Horizontal Scaling for CPU Exhaustion
slug: horizontal-scaling-for-cpu
category: production-ops
subcategory: scaling
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "CPU and Scheduler Hogs"
chapter_number: 8
pdf_page: null
section: "CPU and Scheduler Hogs"
extraction_confidence: medium
aliases:
  - "Scaling out for CPU"
prerequisites:
  - cpu-profiling-difficulty
related:
  - cpu-profiling-difficulty
contrasts_with: []
answers_questions:
  - "How do Erlang developers typically respond to CPU exhaustion?"
  - "What has to change when scaling Erlang code horizontally?"
---

# Quick Definition

Horizontal scaling is the usual Erlang response to CPU exhaustion: because CPU exhaustion bottlenecks throughput rather than crashing the node, developers add nodes, and only centralized global state needs reworking before code can scale out.

# Core Definition

From the chapter introduction: "Erlang developers will have a tendency to scale horizontally when they face such issues. It is often an easy enough job to scale out the more basic pieces of code out there. Only centralized global state (process registries, ETS tables, and so on) usually need to be modified." A footnote adds that this modification "usually takes the form of sharding or finding a state-replication scheme that's suitable, and little more" — Erlang's design tends to force code into a distribution-friendly shape from the start.

# Prerequisites

- `cpu-profiling-difficulty` — the chapter frames horizontal scaling as the alternative to local CPU optimization.

# Key Properties

1. CPU exhaustion bottlenecks throughput; it does not kill the node, so adding capacity is a viable response.
2. Scaling out basic Erlang code is usually easy.
3. Only centralized global state — process registries, ETS tables — typically needs modification.
4. The modification is usually sharding or a suitable state-replication scheme.
5. Erlang's design tends to push code toward distribution-friendly semantics from the outset.
6. Local optimization (profiling, reduction counting, scheduler monitoring) is the alternative to scaling out.

# Construction / Recognition

When a node is CPU-bound: decide between optimizing locally (find the hogs first) and scaling out. To scale out, add nodes and rework centralized global state via sharding or state replication; the bulk of stateless code usually runs unchanged.

# Context & Application

This is the strategic context for the whole CPU chapter. The chapter still teaches local diagnosis "if you want to optimize locally before scaling out at first," but horizontal scaling is presented as the common, often easier path for CPU bottlenecks.

# Examples

From the chapter introduction: "Only centralized global state (process registries, ETS tables, and so on) usually need to be modified."

# Relationships

## Builds Upon
- `cpu-profiling-difficulty` — scaling out is the alternative to the local-optimization techniques.

## Enables
Nothing — terminal strategy card.

## Related
- `cpu-profiling-difficulty` — the local-optimization counterpart.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Assuming all code scales freely; centralized global state (registries, ETS) must first be sharded or replicated.

# Common Confusions

- CPU exhaustion is a throughput bottleneck, not a crash — which is why adding nodes works, unlike with an unbounded memory leak.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, chapter introduction. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from the chapter introduction and its footnote.
- Confidence rationale: medium — the source discusses the strategy briefly as framing rather than as a detailed technique.
- Uncertainties: the source does not detail sharding/replication mechanics.
- Cross-reference status: Verified
