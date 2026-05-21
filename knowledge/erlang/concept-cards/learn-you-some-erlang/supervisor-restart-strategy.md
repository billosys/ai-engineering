---
concept: Supervisor Restart Strategy
slug: supervisor-restart-strategy
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Restart Strategies"
extraction_confidence: high
aliases:
  - restart strategy
  - "one_for_one"
  - "one_for_all"
  - "rest_for_one"
prerequisites:
  - supervisor
extends: []
related:
  - child-specification
  - restart-intensity
  - simple-one-for-one-supervisor
contrasts_with: []
answers_questions:
  - "What is a supervisor?"
  - "How do I write a supervisor?"
---

# Supervisor Restart Strategy

## Quick Definition

A restart strategy tells a supervisor which children to restart when one child dies. The four strategies are `one_for_one`, `one_for_all`, `rest_for_one`, and `simple_one_for_one`.

## Core Definition

The restart strategy is the first element of the supervisor's `init/1` flags tuple: `{RestartStrategy, MaxRestart, MaxTime}`. "The `RestartStrategy` part of the definition can be `one_for_one`, `one_for_all`, `rest_for_one`, or `simple_one_for_one`" (Ch. 17, "Restart Strategies").

## Prerequisites

- **Supervisor** — Restart strategies are part of a supervisor's configuration.

## Key Properties

1. **`one_for_one`** — If one child dies, only that child is restarted. Use when children are independent.
2. **`one_for_all`** — If one child dies, *all* children are restarted. Use when children depend heavily on each other.
3. **`rest_for_one`** — If a child dies, it and all children started *after* it are restarted; earlier children are untouched. Use for chained dependencies.
4. **`simple_one_for_one`** — A supervisor of one child type, used to add children dynamically (covered separately).
5. The strategy is chosen per-supervisor, declared in the `init/1` return.

## Construction / Recognition

## To Choose a Strategy

1. If children are independent and can lose state without affecting siblings → `one_for_one`.
2. If all children must stay synchronised → `one_for_all`.
3. If children form a start-order dependency chain (A → B → C) → `rest_for_one`.
4. If you dynamically spawn many children of one type → `simple_one_for_one`.

## Context & Application

The book's `band_supervisor` shows all three static strategies: a "lenient" supervisor uses `one_for_one` (fires only the failing musician), an "angry" one uses `rest_for_one` (fires the failing musician and those after it), and a "jerk" uses `one_for_all` (fires the whole band on any mistake).

A `one_for_all` restart is *not* triggered by a `temporary` child dying, but a `temporary` child may still be restarted under `one_for_all` if a `permanent` child dies first.

## Examples

**Example 1** (Ch. 17): `init(lenient) -> init({one_for_one, 3, 60});` — only the crashing musician is replaced.

**Example 2** (Ch. 17): `init(angry) -> init({rest_for_one, 2, 60});` — when the drummer crashes, the drummer and the keytar player (started after) are both fired.

**Example 3** (Ch. 17): `init(jerk) -> init({one_for_all, 1, 60});` — any single mistake fires the entire band.

## Relationships

## Builds Upon

- **Supervisor** — The strategy is part of a supervisor's `init/1`.

## Related

- **child-specification** — Children's restart *types* interact with the strategy.
- **restart-intensity** — Paired with the strategy in the flags tuple.
- **simple-one-for-one-supervisor** — A distinct strategy for dynamic children.

## Common Errors

- **Error**: Using `one_for_one` for children whose states must stay synchronised.
  **Correction**: Use `one_for_all` so a crash restarts the whole interdependent group.

## Common Confusions

- **Confusion**: Thinking `rest_for_one` restarts the children before the failed one.
  **Clarification**: It restarts the failed child and everything started *after* it; earlier children are left running.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Restart Strategies" (subsections `one_for_one`, `one_for_all`, `rest_for_one`, `simple_one_for_one`).

## Verification Notes

- Definition: Direct quote listing the four strategies.
- Key Properties: Adapted from each strategy's subsection.
- Confidence: HIGH — each strategy explicitly described.
