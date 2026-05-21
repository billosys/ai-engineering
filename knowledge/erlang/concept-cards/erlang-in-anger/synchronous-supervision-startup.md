---
concept: Synchronous Supervision Startup
slug: synchronous-supervision-startup
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "Supervisors and start_link Semantics"
extraction_confidence: high
aliases:
  - "Synchronous start phases"
prerequisites:
  - supervisor-restart-strategy
  - let-it-crash
extends: []
related:
  - supervisor-init-guarantees
  - connect-in-init-anti-pattern
contrasts_with: []
answers_questions:
  - "Are Erlang supervision trees started depth-first or breadth-first? Synchronously or asynchronously?"
---

# Quick Definition

Erlang supervision trees start synchronously and depth-first: each process can block its siblings and cousins from booting until it has successfully initialized.

# Core Definition

From Chapter 2, section "Supervisors and start_link Semantics": "One very important part of Erlang supervisors and their supervision trees is that *their start phases are synchronous*. Each OTP process has the potential to prevent its siblings and cousins from booting. If the process dies, it's retried again, and again, until it works, or fails too often."

There is no backoff or cooldown period before a supervisor restarts a crashed child.

# Prerequisites

- `supervisor-restart-strategy` — startup is part of the same supervision machinery.
- `let-it-crash` — the retry-until-it-works behaviour is the crash/restart cycle applied at boot.

# Key Properties

1. Start phases are synchronous — a child's `init` must return before its siblings start.
2. Children are started depth-first and in order.
3. A process that fails to initialize is retried again and again until it works or fails too often.
4. There is no backoff or cooldown period between restart attempts.
5. A child stuck failing during init can prevent the whole application — and thus the system — from booting.

# Construction / Recognition

This is the default behaviour of every supervisor. Recognize its consequence: if an application fails to boot after "too many fruitless restarts," the system may shut down. The fix is not to add a cooldown but to make initialization provide guarantees (see `supervisor-init-guarantees`).

# Context & Application

This property is why initialization code must be carefully designed: anything done in `init` that can fail repeatedly (such as connecting to a remote service) can take down the whole node at boot.

# Examples

From Chapter 2, section "Supervisors and start_link Semantics": "When a network-based application tries to set up a connection during its initialization phase and the remote service is down, the application fails to boot after too many fruitless restarts. Then the system may shut down." Jim Gray's paper is cited: handling transient bugs with retries improves Mean Time Between Failures by a factor of 4.

# Relationships

## Builds Upon
- `let-it-crash` — retry-on-failure applied at boot time.
- `supervisor-restart-strategy` — the same supervision mechanism.

## Enables
- `supervisor-init-guarantees` — the synchronous-startup property is *why* init must provide guarantees.

## Related
- `connect-in-init-anti-pattern` — the trap that synchronous startup makes dangerous.

## Contrasts With
Nothing directly.

# Common Errors

- Expecting a built-in backoff before restart — there is none. Developers often argue for a cooldown supervisor; the book strongly opposes this, recommending guarantee-providing init instead.

# Common Confusions

- "Synchronous" startup does not mean slow by design — it means ordered and blocking; the point is that later processes can rely on earlier ones being healthy.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "Supervisors and start_link Semantics". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "Supervisors and start_link Semantics."
- Confidence rationale: high — the synchronous, depth-first, no-cooldown properties are stated explicitly.
- Uncertainties: none.
- Cross-reference status: Verified
