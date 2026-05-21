---
concept: Asking for Permission
slug: ask-for-permission
category: production-ops
subcategory: overload
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Asking For Permission"
extraction_confidence: high
aliases:
  - "Circuit breakers"
  - "SafetyValve"
prerequisites:
  - back-pressure
extends:
  - back-pressure
related:
  - synchronous-call-back-pressure
  - timeout-selection
contrasts_with:
  - synchronous-call-back-pressure
answers_questions:
  - "What is an alternative to having timeouts?"
  - "How can a system explicitly report overload?"
---

# Quick Definition

Asking for permission is a back-pressure mechanism in which a caller must request the right to use a critical resource before doing so; the bottleneck itself grants or denies that right.

# Core Definition

From Chapter 3, section "Asking For Permission": "A somewhat simpler approach to back-pressure is to identify the resources we want to block on, those that cannot be made faster and are critical to your business and users. Lock these resources behind a module or procedure where a caller must ask for the right to make a request and use them."

The key principle: "the edge of the system (or subsystem) may block and ask for the right to process data, but the critical bottleneck in code is the one to determine whether that right can be granted or not."

# Prerequisites

- `back-pressure` — asking for permission is a form of back-pressure.

# Key Properties

1. Critical, un-speedupable resources are gated behind a module or procedure that grants/denies permission.
2. Permission can be based on memory, CPU, overall load, a bounded call count, concurrency, response times, or combinations.
3. The edge asks for the right; the bottleneck decides whether to grant it.
4. Avoids making every abstraction layer synchronous and avoids the tricky timer/timeout problem entirely.
5. Allows *explicit* reporting of overload — the interface can say "the system is overloaded" or "you hit a rate limit," unlike implicit (synchronous) back-pressure.
6. Tools: the *SafetyValve* application is a system-wide framework for this; circuit breakers (`breaky`, `fuse`, Klarna's `circuit_breaker`) suit service/system-failure cases; ad-hoc solutions can use processes or ETS.

# Construction / Recognition

Identify the critical bottleneck resource. Place a permission gate at the bottleneck, keyed on a chosen variable (load, concurrency, etc.). At the edge (or control point), call the gate before doing work; proceed only if granted. Use SafetyValve, a circuit breaker library, or an ad-hoc ETS/process solution.

# Context & Application

This is the recommended alternative when synchronous back-pressure's per-layer timeout problem becomes intractable, or when you need to explicitly report overload to users rather than letting them merely observe slowness.

# Examples

From Chapter 3, section "Asking For Permission": "The *SafetyValve* application is a system-wide framework that can be used when you know back-pressure is what you'll need." For service/system failures: "there are plenty of circuit breaker applications available. Examples include `breaky`, `fuse`, or Klarna's `circuit_breaker`."

# Relationships

## Builds Upon
- `back-pressure` — a realization of the strategy.

## Enables
Explicit overload reporting to users.

## Related
- `timeout-selection` — the problem this approach sidesteps.

## Contrasts With
- `synchronous-call-back-pressure` — synchronous calls give *implicit* back-pressure and force per-layer timeout decisions; asking for permission is *explicit* and puts a single guard at the bottleneck.

# Common Errors

- Placing the permission decision at the edge instead of the bottleneck — the bottleneck must be the authority that grants or denies.

# Common Confusions

- Asking for permission is still back-pressure, not load-shedding — a denied caller is slowed/blocked, not silently dropped (though the caller may then choose to give up).
- A circuit breaker is a specialized "ask for permission" mechanism for service-failure cases, not a separate category.

# Source Reference

Chapter 3: Planning for Overload, Section "Asking For Permission". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Asking For Permission."
- Confidence rationale: high — explicitly described with named tooling.
- Uncertainties: none.
- Cross-reference status: Verified
