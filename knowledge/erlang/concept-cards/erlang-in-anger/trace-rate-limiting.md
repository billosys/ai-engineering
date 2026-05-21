---
concept: Trace Rate Limiting
slug: trace-rate-limiting
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Tracing with Recon"
extraction_confidence: high
aliases:
  - "Trace limits"
prerequisites:
  - recon-trace
related:
  - recon-trace
  - erlang-tracing-tools
contrasts_with: []
answers_questions:
  - "How do I trace function calls safely in production without flooding the node?"
  - "How do I rate-limit trace output?"
---

# Quick Definition

Trace rate limiting caps how many trace messages a trace can produce — either as a static absolute count or as a number of matches per time interval — so that a production trace cannot flood the node with messages.

# Core Definition

From section "Tracing with Recon": "It will also be possible to rate limit based on two manners: a static count, or a number of matches per time interval." In `recon_trace:calls/2,3` the second argument is this limit: a bare integer is a static count (`recon_trace:calls({lists, seq, 2}, 100)` prints at most 100 calls), and a `{Count, Milliseconds}` tuple is a per-interval rate (`{100, 1000}` is at most 100 calls per second). When the limit is reached, recon prints "Recon tracer rate limit tripped."

# Prerequisites

- `recon-trace` — rate limiting is the `Max` argument of `recon_trace:calls`.

# Key Properties

1. Two forms: a static absolute count, or `{Count, TimeInMs}` matches per interval.
2. A static count of 1 prints at most one trace, then trips the limiter.
3. `{100, 1000}` means at most 100 traced calls per 1000 ms.
4. When the limit is reached, recon emits "Recon tracer rate limit tripped."
5. Rate limiting is what makes `recon_trace` (and `redbug`) production-safe — `dbg` and the raw BIFs lack it.
6. Even with rate limiting, extremely broad patterns or very high limits can still destabilize a node.

# Construction / Recognition

Pass the limit as the second argument to `recon_trace:calls`. Use a small static count to peek at a few calls; use `{Count, Ms}` for an ongoing rate-limited trace. Start with the most restrictive limits and widen progressively.

# Context & Application

Rate limiting is the safety mechanism for production tracing. Without it, a trace on a hot function generates more messages than any process can handle and can take the node down. With it, the trace self-limits and reports when it does.

# Examples

From section "Example Sessions":

```erlang-repl
1> recon_trace:calls({queue, new, '_'}, 1).
1
13:14:34.086078 <0.44.0> queue:new()
Recon tracer rate limit tripped.
```

And the per-interval form: `recon_trace:calls({lists, seq, 2}, {100, 1000})` — at most 100 calls per second.

# Relationships

## Builds Upon
- `recon-trace` — rate limiting is `recon_trace:calls`'s `Max` argument.

## Enables
Nothing — terminal mechanism card.

## Related
- `erlang-tracing-tools` — `redbug` also rate-limits; `dbg` and BIFs do not.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Setting a very high absolute limit or a lax per-interval rate on a broad pattern — the node can still be destabilized.
- Tracing all of `io` or every function; even rate limiting cannot fully protect against such scope.

# Common Confusions

- A static count is a *total* cap (the trace stops after N); a `{Count, Time}` rate is *ongoing* (it keeps tracing, capped per interval).
- Rate limiting reduces risk but does not eliminate it — pattern breadth still matters.

# Source Reference

Chapter 9: Tracing, Sections "Tracing with Recon" and "Example Sessions". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Tracing with Recon."
- Confidence rationale: high — the source explicitly describes both rate-limit forms and shows them in sessions.
- Uncertainties: none.
- Cross-reference status: Verified
