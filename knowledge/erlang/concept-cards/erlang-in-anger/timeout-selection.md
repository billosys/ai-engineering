---
concept: Timeout Selection
slug: timeout-selection
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "How Long Should a Time Out Be"
extraction_confidence: high
aliases:
  - "How long should a timeout be"
prerequisites:
  - synchronous-call-back-pressure
extends: []
related:
  - back-pressure
  - ask-for-permission
contrasts_with: []
answers_questions:
  - "When going synchronous, how should timeouts be chosen?"
---

# Quick Definition

Timeout selection is the difficulty of choosing how long synchronous back-pressure calls should wait — timers at the system edge must be longer than the deeper ones, and "infinite" timeouts are rarely justifiable.

# Core Definition

From Chapter 3, section "How Long Should a Time Out Be": "What's particularly tricky about applying back-pressure to handle overload via synchronous calls is having to determine what the typical operation should be taking in terms of time, or rather, at what point the system should time out... the timer at the edge of the system will need to have a longer wait time than those within, unless you plan on having operations reported as timing out at the edge even though they succeeded internally."

# Prerequisites

- `synchronous-call-back-pressure` — timeout selection is a problem created by synchronous back-pressure.

# Key Properties

1. The first timer starts at the edge, but the critical operation happens deep within — so edge timeouts must exceed internal ones.
2. If an edge timeout is shorter than an internal one, operations are reported as timed out even though they succeeded internally.
3. "Infinite" timeouts are tempting but hard to justify — Pat Helland's response: propose a 30-year timeout, and if 30 years seems silly, so should infinity.
4. In Erlang, the value `infinity` avoids creating a timer (saving resources) — but if used, a well-defined timeout must exist somewhere in the call sequence.
5. Timeout selection is ultimately a case-by-case issue; sometimes a different flow-control mechanism is more practical.

# Construction / Recognition

When introducing synchronous calls: estimate typical operation time per layer; set each layer's timeout longer than the layers beneath it; avoid plain `infinity` unless a real timeout exists elsewhere in the sequence; if timeout choice becomes intractable, consider an alternative mechanism (asking for permission).

# Context & Application

This problem arises directly from implementing back-pressure with synchronous calls. Its difficulty is one of the main reasons the book offers "asking for permission" as a simpler alternative.

# Examples

From Chapter 3, section "How Long Should a Time Out Be": Pat Helland is quoted — "I typically propose they set the timeout to 30 years. That, in turn, generates a response that I need to be reasonable and not silly. *Why is 30 years silly but infinity is reasonable?*"

# Relationships

## Builds Upon
- `synchronous-call-back-pressure` — the source of the problem.

## Enables
Nothing.

## Related
- `back-pressure` — the parent strategy.
- `ask-for-permission` — the alternative that sidesteps per-layer timeout decisions.

## Contrasts With
Nothing directly.

# Common Errors

- Setting all layers to the same timeout, so edge calls time out before deep ones finish.
- Using `infinity` everywhere with no bounded timeout anywhere in the call sequence.

# Common Confusions

- An `infinity` timeout is not "no timeout system" — in Erlang it specifically avoids creating a timer; the risk is unbounded waiting, not resource cost.

# Source Reference

Chapter 3: Planning for Overload, Section "How Long Should a Time Out Be". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "How Long Should a Time Out Be."
- Confidence rationale: high — the edge-vs-internal rule and the infinity discussion are explicit.
- Uncertainties: none.
- Cross-reference status: Verified
