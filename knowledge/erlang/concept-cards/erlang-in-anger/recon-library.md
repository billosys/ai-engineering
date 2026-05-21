---
concept: recon Library
slug: recon-library
category: production-ops
subcategory: tooling
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - recon
prerequisites: []
extends: []
related:
  - runtime-introspection
  - process-inspection
  - crash-dump-analysis
contrasts_with: []
answers_questions:
  - "What is recon?"
  - "How do I safely introspect a production Erlang node?"
---

# Quick Definition

`recon` is a library that regroups common Erlang introspection, metrics, and crash-analysis operations into production-safe, ready-to-use functions and scripts.

# Core Definition

"To make the text lighter and to be more usable, common operations have been regrouped in the `recon` library, and are generally production-safe" (Chapter 5, intro).

The book notes that standard-library introspection features "aren't all in one place, and can make it too easy to shoot yourself in the foot within a production system. They also tend to be closer to building blocks than usable tools" — `recon` exists to fix that.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Regroups scattered standard-library introspection building blocks into usable, production-safe functions.
2. Memory: `recon_alloc:memory/1`.
3. CPU: `recon:scheduler_usage/1`.
4. Processes: `recon:info/1-2`, `recon:proc_count/2`, `recon:proc_window/3`.
5. Ports: `recon:port_types/0`, `recon:port_info/1-2`, `recon:inet_count/2`, `recon:inet_window/3`.
6. Emergency metrics: `recon:node_stats_print/2`.
7. Crash dumps: ships scripts `erl_crashdump_analyzer.sh` and `queue_fun.awk` under `script/`.
8. "Generally production-safe" — but some entry points (e.g. `recon:info(Pid, [Keys])` with unsafe keys) can still fetch dangerous data.

# Construction / Recognition

Add `recon` as a dependency, then call its functions from a shell or tooling. The crash-dump scripts are run from the shell against an `erl_crash.dump` file.

# Context & Application

Used throughout the Runtime Metrics and Crash Dumps chapters as the practical toolkit for both live introspection and post-mortem analysis, sparing operators from assembling raw standard-library calls.

# Examples

From Chapter 5: `recon:scheduler_usage(1000)`, `recon:proc_count(memory, 3)`, `recon:port_types()`. From Chapter 6: `./recon/script/erl_crashdump_analyzer.sh erl_crash.dump`.

# Relationships

## Builds Upon

## Enables
- process-inspection
- crash-dump-analysis

## Related
- runtime-introspection

## Contrasts With

# Common Errors

- Assuming *everything* in recon is safe — `recon:info(Pid, [Keys])` can still request dangerous keys like `messages`.

# Common Confusions

- recon does not add new VM capabilities; it packages existing standard-library introspection into safer, more ergonomic forms.

# Source Reference

Chapter 5: Runtime Metrics, intro; Chapter 6: Reading Crash Dumps (scripts). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter intro.
- Confidence rationale: high — the role of recon is explicitly stated.
- Uncertainties: none.
- Cross-reference status: Verified
