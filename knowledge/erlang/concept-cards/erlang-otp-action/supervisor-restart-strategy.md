---
# === CORE IDENTIFICATION ===
concept: Supervisor Restart Strategy
slug: supervisor-restart-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.2.2 The supervisor restart strategy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - restart strategy
  - one_for_one
  - restart frequency

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervisor-implementation
extends:
  - supervisor
related:
  - child-specification
  - simple-one-for-one
  - supervision-tree
contrasts_with:
  - simple-one-for-one

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor restart strategy?"
  - "What does the one_for_one strategy do?"
  - "What is the restart frequency of a supervisor?"
---

# Quick Definition

A supervisor restart strategy is the `{How, Max, Within}` tuple returned from a supervisor's `init/1` that controls how children are restarted and how many restarts are allowed before the supervisor itself gives up.

# Core Definition

The value returned from a supervisor's `init/1` has the form `{ok, {RestartStrategy, Children}}`, where the `RestartStrategy` is a 3-tuple `{How, Max, Within}` (Ch. 4, Section 4.2.2). `How` selects the restart policy: `one_for_one` means that if a child process dies, that process — and only that one — is restarted, leaving other children unaffected. `Max` and `Within` together specify the allowed *restart frequency*: at most `Max` restarts within any period of `Within` seconds. If this limit is exceeded, the supervisor terminates itself and all its children and propagates the failure up the supervision tree. For example, `{one_for_one, 0, 1}` allows no automatic restarts within any 1-second window; `4` restarts per `3600` seconds is a common production value.

# Prerequisites

- **Supervisor** — The strategy governs a supervisor's behaviour.
- **Implementing a supervisor** — The strategy is part of `init/1`'s return value.

# Key Properties

1. A 3-tuple `{How, Max, Within}` in the supervisor's `init/1` return value.
2. `How` chooses the restart policy (e.g. `one_for_one`).
3. `one_for_one` restarts only the failed child, leaving siblings unaffected.
4. `Max` and `Within` define the allowed restart frequency (Max restarts per Within seconds).
5. Exceeding the limit makes the supervisor terminate itself and all children.
6. `{one_for_one, 0, 1}` allows no automatic restarts; `4` per `3600` is a common production setting.

# Construction / Recognition

## To Set a Restart Strategy:
1. In `init/1`, choose `How` (`one_for_one`, `simple_one_for_one`, etc.).
2. Choose `Max` — the maximum number of restarts.
3. Choose `Within` — the timeframe in seconds.
4. Return `{ok, {{How, Max, Within}, Children}}`.

# Context & Application

The restart strategy expresses the supervisor's fault-tolerance policy: how isolated a child failure is, and how much repeated failure is tolerated before escalation.

- **Typical contexts**: The `init/1` callback of every supervisor.
- **Common applications**: `tr_sup` uses `{one_for_one, 0, 1}` so problems in code show up clearly; `sc_sup` uses `simple_one_for_one` with zero restarts per second.

# Examples

**Example 1** (Ch. 4): `tr_sup` returns `RestartStrategy = {one_for_one, 0, 1}` — picking `0` and `1` deliberately to allow no automatic restarts while developing.

**Example 2** (Ch. 4): Figure 4.3 illustrates `one_for_one`: a crashing sibling does not affect healthy children.

# Relationships

## Builds Upon
- **Supervisor** — The strategy is part of a supervisor's configuration.

## Related
- **child-specification** — The other half of `init/1`'s return value.
- **supervision-tree** — Exceeding the restart limit propagates failure up the tree.

## Contrasts With
- **simple-one-for-one** — A distinct restart strategy for dynamic, identical children.

# Common Errors

- **Error**: Setting `Max`/`Within` carelessly so transient failures exhaust the limit and kill the supervisor.
  **Correction**: Tune the restart frequency to the application; `4` restarts per `3600` seconds is a common starting point.

# Common Confusions

- **Confusion**: Thinking `{one_for_one, 0, 1}` means "restart once per second."
  **Clarification**: It means at most `0` restarts within any `1`-second window — i.e. no automatic restarts.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.2.2 "The supervisor restart strategy," Figure 4.3.

# Verification Notes

- Definition source: Direct adaptation of Section 4.2.2.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: Other `How` strategies (`rest_for_one`, `one_for_all`) are mentioned but deferred to later chapters.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
