---
# === CORE IDENTIFICATION ===
concept: Restart Strategy
slug: restart-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Supervision Tree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "one_for_one"
  - "one_for_all"
  - "restart frequency"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - supervision-tree
  - child-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor restart strategy?"
  - "What is the difference between one_for_one and one_for_all supervision?"
---

# Quick Definition

A restart strategy tells a supervisor how to react when a worker fails: `one_for_one` restarts only the failed worker; `one_for_all` kills and restarts all workers. A restart frequency (`MaxRestarts` in `Time` seconds) bounds the retries.

# Core Definition

A supervisor's `init/1` returns `{RestartStrategy, MaxRestarts, Time}`, where `RestartStrategy` "is one of the atoms `one_for_one` or `one_for_all`" (Programming Erlang, "The Supervision Tree"). In one-for-one supervision, "if a worker fails, it is restarted by the supervisor." In one-for-all supervision, "if any worker dies, then all the worker processes are killed (by calling the `terminate/2` function in the appropriate callback module). Then all the worker processes are restarted." `MaxRestarts` and `Time` specify a *restart frequency*: "If a supervisor performs more than `MaxRestarts` in `Time` seconds, then the supervisor will terminate all the worker processes and then itself" — this stops an endless crash-restart-crash loop.

# Prerequisites

- **Supervisor** — the restart strategy is part of a supervisor's `init/1` return value.

# Key Properties

1. Two strategies: `one_for_one` and `one_for_all`.
2. `one_for_one`: only the crashed worker is restarted.
3. `one_for_all`: all workers are terminated (via `terminate/2`) and restarted when any one fails.
4. The restart frequency `{Strategy, MaxRestarts, Time}` bounds retries.
5. Exceeding `MaxRestarts` within `Time` seconds makes the supervisor terminate all children and itself.
6. The frequency limit exists to prevent infinite crash loops where a process keeps crashing for the same reason.

# Construction / Recognition

## To Choose a Restart Strategy:
1. If the workers are independent, use `one_for_one`.
2. If the workers are interdependent (one crashing invalidates the others), use `one_for_all`.
3. Set `MaxRestarts` and `Time` so a persistently failing process eventually causes the supervisor to give up.
4. Place it as the first element of the supervisor `init/1` tuple: `{Strategy, MaxRestarts, Time}`.

## To Recognize:
1. The atom `one_for_one` or `one_for_all` as the first element of a supervisor's strategy tuple identifies the restart strategy.

# Context & Application

- **Typical contexts**: Every supervisor node in a supervision tree configures a restart strategy.
- **Common applications**: `sellaprime_supervisor` uses `{one_for_one, 3, 10}` — at most 3 restarts in 10 seconds, restarting only the failed server.
- **Historical/stylistic notes**: The two strategies correspond to the "two types of supervision tree" the book illustrates in Figure 10.

# Examples

**Example 1** ("The Supervision Tree"): `sellaprime_supervisor:init/1` returns a tuple beginning `{one_for_one, 3, 10}` — independent restart of the area and prime servers, bounded to 3 restarts per 10 seconds.

**Example 2** ("The Supervision Tree"): The book's description of one-for-all: "if any worker dies, then all the worker processes are killed ... Then all the worker processes are restarted."

# Relationships

## Builds Upon
- **Supervisor** — the restart strategy is configured in the supervisor's `init/1`.

## Enables
- **Supervision tree** — the strategy at each node determines the tree's recovery behaviour.

## Related
- **Child specification** — each child spec also carries a per-child `Restart` type (`permanent`/`transient`/`temporary`).

## Contrasts With
- (No direct contrast within this chapter — `one_for_one` and `one_for_all` are the two values of this same concept.)

# Common Errors

- **Error**: Using `one_for_all` when workers are independent, causing unnecessary mass restarts.
  **Correction**: Use `one_for_one` so an unrelated worker's crash doesn't disturb the others.

- **Error**: Setting `MaxRestarts` very high to "keep trying forever."
  **Correction**: The bound exists to stop crash loops; choose a frequency that lets the supervisor give up on a persistently failing process.

# Common Confusions

- **Confusion**: Confusing the supervisor restart strategy with the per-child `Restart` type.
  **Clarification**: The strategy (`one_for_one`/`one_for_all`) governs how the supervisor reacts; the child's `Restart` (`permanent`/`transient`/`temporary`) governs whether that specific child is restarted at all.

- **Confusion**: Thinking `one_for_all` restarts only the supervisor.
  **Clarification**: `one_for_all` terminates and restarts *all the worker processes* when any one dies.

# Source Reference

Chapter 23: Making a System with OTP, section "The Supervision Tree". No page numbers (EPUB-origin source). See Figure 10.

# Verification Notes

- Definition source: Direct quotes from "The Supervision Tree".
- Confidence rationale: HIGH — both strategies and the restart frequency are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
