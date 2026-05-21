---
concept: VM Metrics Libraries
slug: vm-metrics-libraries
category: production-ops
subcategory: observability
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Global View"
extraction_confidence: high
aliases:
  - metrics applications
  - folsom
  - exometer
  - vmstats
prerequisites:
  - runtime-introspection
extends: []
related:
  - vm-memory-reporting
  - scheduler-utilization
  - process-count-metric
contrasts_with: []
answers_questions:
  - "How do I keep long-term metrics on an Erlang node?"
  - "What libraries collect Erlang VM metrics?"
---

# Quick Definition

VM metrics libraries are Erlang applications that collect, store, and forward VM-level metrics (memory, processes, ports, scheduler usage) so that long-term, "in the large" views of a node's health are available.

# Core Definition

"For a view of the VM in the large, it's useful to track statistics and metrics general to the VM, regardless of the code running on it. Moreover, you should aim for a solution that allows long-term views of each metric — some problems show up as a very long accumulation over weeks that couldn't be detected over small time windows" (Chapter 5, "Global View").

# Prerequisites

- `runtime-introspection`: metrics libraries are the tooling that implements the "in the large" half of the observability philosophy.

# Key Properties

1. Provide *long-term* metric storage, which is needed to detect slow leaks and weekly/daily activity patterns.
2. Common options the book lists:
   - `folsom` — stores metrics in memory within the VM, global or app-specific.
   - `vmstats` and `statsderl` — send node metrics to graphite through `statsd`.
   - `exometer` — a fuller metrics system that can integrate with `folsom` and many back-ends (graphite, collectd, statsd, Riak, SNMP).
   - `ehmon` — outputs directly to standard output for later collection (splunk, agents).
   - custom hand-rolled solutions, typically ETS tables plus a process periodically dumping data.
   - as a last resort, a function printing stats in a loop in a shell (recon's `recon:node_stats_print/2`).
3. The book's advice: "explore them a bit, pick one, and get a persistence layer that will let you look through your metrics over time."

# Construction / Recognition

Pick one library, integrate it into the application, and connect it to a persistence/visualization back-end so metrics survive and can be reviewed over weeks.

# Context & Application

Used to establish baselines so anomalies (memory leaks, process leaks, traffic spikes) become visible. Some issues — e.g. a slow leak over weeks, or irregular spikes tied to time of day/week — require *months* of data to confirm.

# Examples

From Chapter 5, "Global View": "Good examples for issues exposed by a long-term view include memory or process leaks, but also could be regular or irregular spikes in activities relative to the time of the day or week, which can often require having months of data to be sure about it."

# Relationships

## Builds Upon
- runtime-introspection

## Enables
- vm-memory-reporting
- scheduler-utilization
- process-count-metric

## Related

## Contrasts With

# Common Errors

- Relying only on short time windows — long-accumulation problems will be invisible.
- Collecting metrics without a persistence layer, so historical baselines are lost.

# Common Confusions

- These libraries are building blocks for *global* metrics; they do not replace per-process "digging in" tools.
- `recon:node_stats_print/2` is a stopgap for emergencies, not a substitute for a real metrics pipeline.

# Source Reference

Chapter 5: Runtime Metrics, Section "Global View". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from the chapter, library list quoted.
- Confidence rationale: high — the chapter explicitly enumerates the options.
- Uncertainties: relative maturity of the libraries has changed since publication.
- Cross-reference status: Verified
