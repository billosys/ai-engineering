---
concept: Runtime Introspection
slug: runtime-introspection
category: production-ops
subcategory: observability
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
  - observability philosophy
  - in the large and in the small
prerequisites: []
extends: []
related:
  - vm-metrics-libraries
  - process-inspection
  - recon-library
contrasts_with: []
answers_questions:
  - "Why is the Erlang VM good for production observability?"
  - "How should I observe a production Erlang system?"
---

# Quick Definition

Runtime introspection is the practice of observing a live Erlang VM — its metrics, processes, ports, and state — both "in the large" (global VM statistics) and "in the small" (per-process detail), using facilities the VM exposes programmatically.

# Core Definition

"One of the best selling points of the Erlang VM for production use is how transparent it can be for all kinds of introspection, debugging, profiling, and analysis at run time" (Chapter 5, intro).

The recommended approach: "A practical approach to growing a system and keeping it healthy in production is to make sure all angles are observable: in the large, and in the small. There's no generic recipe to tell in advance what is going to be normal or not. You want to keep a lot of data and to look at it from time to time to form an idea about what your system looks like under normal circumstances."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The Erlang VM exposes introspection data programmatically, making it easy to build tools and watchdogs.
2. In times of need you can bypass tools and query the VM directly.
3. "Observe in the large" — global VM statistics independent of running code (memory, CPU, processes, ports).
4. "Observe in the small" — per-process and per-port detail (`process_info`, `port_info`).
5. There is no generic notion of "normal" — you must collect baseline data over time to recognize anomalies later.
6. Standard-library introspection features are powerful but scattered and easy to misuse; `recon` regroups production-safe versions.

# Construction / Recognition

Build observability by: (1) running a metrics library to keep long-term global data; (2) periodically reviewing baselines; (3) when something looks wrong, "digging in" with per-process/per-port tools to find the culprit.

# Context & Application

This is the organizing philosophy of the whole Runtime Metrics chapter. The "global view" tools answer *whether* something is wrong; the "digging in" tools answer *which process or port* is responsible.

# Examples

From Chapter 5, intro: "The advantage of having these runtime metrics accessible programmatically is that building tools relying on them is easy, and building automation for some tasks or watchdogs is equally simple. Then, in times of need, it's also possible to bypass the tools and go direct to the VM for information."

From Chapter 5, "Digging In": "Whenever some 'in the large' view (or logging, maybe) has pointed you towards a potential cause for an issue you're having, it starts being interesting to dig around with a purpose."

# Relationships

## Builds Upon

## Enables
- vm-metrics-libraries
- process-inspection

## Related
- recon-library

## Contrasts With

# Common Errors

- Trying to define "normal" values in advance instead of collecting baseline data over time.
- Using raw standard-library introspection in production without realizing some calls can copy enough data to kill the node — prefer the production-safe `recon` wrappers.

# Common Confusions

- Introspection is not just debugging-time activity: long-term metric collection is part of it, since some problems only show up over weeks.
- "In the large" and "in the small" are complementary, not alternatives — you usually need both.

# Source Reference

Chapter 5: Runtime Metrics, intro and "Digging In" sections. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from chapter intro.
- Confidence rationale: high — the chapter explicitly states this philosophy.
- Uncertainties: none.
- Cross-reference status: Verified
