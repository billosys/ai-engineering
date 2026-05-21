---
concept: True Bottleneck
slug: true-bottleneck
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Planning for Overload"
extraction_confidence: high
aliases: []
prerequisites:
  - message-queue-overload
extends: []
related:
  - back-pressure
  - load-shedding
  - timeout-selection
contrasts_with: []
answers_questions:
  - "What is a true bottleneck? How can you find it?"
  - "What is a true bottleneck?"
---

# Quick Definition

A true bottleneck is the point in a system that cannot be optimized further — where overload can no longer be pushed downstream — making all prior optimizations effectively in vain.

# Core Definition

From Chapter 3, section "Planning for Overload": after enlarging the crashed component, then its drain, then the pipes, "the overload gets pushed further down the system, until the sewers can't take it anymore." Eventually "there's a point where things can't be improved anymore at the bathroom's level... By finding that point, we identified what the *true bottleneck* of the system was, and all the prior optimization was nice (and likely expensive), but it was more or less in vain."

# Prerequisites

- `message-queue-overload` — the true bottleneck is found while chasing an overload problem.

# Key Properties

1. The point where the system genuinely cannot be made faster — too many logs, a database needing consistency, or simply not enough organizational knowledge or manpower.
2. Found only after iteratively optimizing every component upstream of it.
3. Optimizations made *before* finding it are largely wasted effort — overload was merely relocated, not removed.
4. Once identified, the response shifts: instead of optimizing further, you make incoming information lighter (compression, better algorithms/data representation, caching) or restrict/discard input.
5. It is the deepest point in the system; bottlenecks causing queue growth "[are] usually not at the edge of the system, but deep inside it."

# Construction / Recognition

Recognize it by iteratively optimizing: enlarge the crashed component, then its drain, then the pipes. When optimization stops yielding improvement — typically at a database requiring consistency, a logging subsystem, or an organizational limit — you have found the true bottleneck.

# Context & Application

Identifying the true bottleneck tells you to stop optimizing and instead apply overload-management strategies (back-pressure or load-shedding), or to lighten the input. It also informs *where* synchronous back-pressure must originate — at the bottleneck, deep in the system.

# Examples

From Chapter 3, section "Planning for Overload": the true bottleneck manifests as "too many logs sent around, there's a bottleneck on databases that *need* the consistency, or there's simply not enough knowledge or manpower in your organization to improve things there."

# Relationships

## Builds Upon
- `message-queue-overload` — the problem whose investigation reveals the bottleneck.

## Enables
- `back-pressure`, `load-shedding` — the strategies adopted once the true bottleneck is found.

## Related
- `timeout-selection` — timeouts must account for the bottleneck being deep in the system.

## Contrasts With
Nothing directly.

# Common Errors

- Continuing to optimize after the true bottleneck is found — effort is wasted relocating overload rather than removing it.
- Looking for the bottleneck at the system's edge; it is usually deep inside.

# Common Confusions

- The true bottleneck is not necessarily a code problem — it can be an organizational limit (knowledge or manpower) or an unavoidable consistency requirement.

# Source Reference

Chapter 3: Planning for Overload, Section "Planning for Overload" (chapter introduction). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3 introduction.
- Confidence rationale: high — the term is explicitly named and defined.
- Uncertainties: none.
- Cross-reference status: Verified
