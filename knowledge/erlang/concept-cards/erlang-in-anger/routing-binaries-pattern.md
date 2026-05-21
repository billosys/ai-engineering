---
concept: Routing Binaries Pattern
slug: routing-binaries-pattern
category: anti-patterns
subcategory: binaries
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Routing Binaries"
extraction_confidence: high
aliases:
  - "Middleman binary router"
prerequisites:
  - refc-binary-leak
related:
  - refc-binary-leak-fixes
contrasts_with: []
answers_questions:
  - "Why does a router process leak binary memory?"
  - "How do I avoid a middleman process accumulating refc binaries?"
---

# Quick Definition

The routing binaries pattern is the anti-pattern in which a middleman process routes binaries between other processes, thereby acquiring a reference to every binary that passes through it and becoming a major source of refc-binary leaks; the fix is to have the router return a pid and let the original caller move the binary itself.

# Core Definition

From section "Routing Binaries": "The problematic use case is usually having a middleman process routing binaries from one process to another one. That middleman process will therefore acquire a reference to every binary passing through it and risks being a common major source of refc binaries leaks." The solution: "have the router process return the pid to route to and let the original caller move the binary around. This will make it so that only processes that do need to touch the binaries will do so." This can be implemented transparently inside the router's API functions, with no visible change for callers.

# Prerequisites

- `refc-binary-leak` — the pattern is a specific cause of a refc-binary leak, so the leak mechanism must be understood first.

# Key Properties

1. A middleman router that forwards binaries acquires a reference to every binary it forwards.
2. Because routers are long-lived and rarely GC'd at the right moment, they become a major leak source.
3. The fix decouples routing decisions from data movement: the router returns a destination pid.
4. The caller then sends the binary directly to the destination, so only processes that *need* the binary ever reference it.
5. The fix can be hidden inside the router's API functions — callers need no code change.

# Construction / Recognition

To recognize: `recon:bin_leak/1` flags a long-lived router/dispatcher process holding many binaries. To fix: change the router's API so its routing function returns the target pid; have the caller send the binary directly to that pid; keep the API surface unchanged so callers are unaffected.

# Context & Application

This applies to dispatcher, proxy, or broker processes that sit between producers and consumers of binary data. The pattern concentrates binary references in one process that does little real work and therefore rarely garbage collects.

# Examples

From section "Routing Binaries": "A fix for this can be implemented transparently in the router's API functions, without any visible change required by the callers."

# Relationships

## Builds Upon
- `refc-binary-leak` — this is a specific scenario of the general leak.

## Enables
Nothing — terminal anti-pattern card.

## Related
- `refc-binary-leak-fixes` — the general set of binary-leak remedies.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Routing binary payloads *through* a dispatcher process instead of returning a destination and letting the caller deliver the data.

# Common Confusions

- The router does not need to touch the binary content to leak — merely holding a reference (by receiving the message) is enough to pin the refc binary.

# Source Reference

Chapter 7: Memory Leaks, Section "Routing Binaries". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Routing Binaries."
- Confidence rationale: high — the source explicitly describes the pattern and its fix.
- Uncertainties: none.
- Cross-reference status: Verified
