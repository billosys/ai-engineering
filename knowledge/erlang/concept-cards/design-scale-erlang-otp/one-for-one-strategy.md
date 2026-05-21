---
# === CORE IDENTIFICATION ===
concept: One for One Strategy
slug: one-for-one-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "The restart specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "one_for_one"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
extends:
  - restart-strategy
related:
  - rest-for-one-strategy
contrasts_with:
  - one-for-all-strategy
  - rest-for-one-strategy
  - simple-one-for-one-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the one_for_one and one_for_all restart strategies?"
---

# Quick Definition

`one_for_one` is the supervisor restart strategy in which only the crashed child is restarted; all other children keep running. It is ideal when supervised children do not depend on each other.

# Core Definition

Under the `one_for_one` strategy, only the crashed process is restarted (Cesarini & Vinoski, p. 178). This strategy is ideal if the workers do not depend on each other and the termination of one will not affect the others. The book's example: a supervisor monitoring the worker processes that control the instant-messaging sessions of hundreds of thousands of users — if one process crashes, only that user's session is affected, and all other workers should continue running independently (pp. 178-179).

# Prerequisites

- **Restart strategy** — `one_for_one` is one of the four restart strategy values.

# Key Properties

1. Only the crashed child is terminated and restarted.
2. All sibling children continue running, unaffected.
3. Appropriate when children are independent of one another.
4. Specified as the atom `one_for_one` in the supervisor specification.

# Construction / Recognition

## To Construct/Create:
1. Confirm the supervised children do not depend on each other.
2. Set `strategy => one_for_one` (or the first tuple element) in the supervisor specification.

## To Identify/Recognize:
1. The supervisor specification's strategy is `one_for_one`.
2. A crash of one child leaves siblings running.

# Context & Application

- **Typical contexts**: Supervisors of large numbers of independent worker processes.
- **Common applications**: Per-user session processes, per-connection processes that share no state.
- **Historical/stylistic notes**: `phone_sup` uses `one_for_one` because mobile devices run independently of each other (p. 184).

# Examples

**Example 1** (pp. 178-179): A supervisor of instant-messaging session processes — if one crashes, only that user is affected.

**Example 2** (p. 184): `phone_sup`'s `init/1` returns `{ok, {{one_for_one, 10, 3600}, []}}`.

## Worked Example

`phone_sup` using `one_for_one` (p. 184):

```erlang
init([]) ->
    {ok, {{one_for_one, 10, 3600}, []}}.
```

A maximum of 10 restarts per hour; each phone FSM is restarted independently of the others.

# Relationships

## Builds Upon
- **Restart strategy** — `one_for_one` is one specific restart strategy.

## Enables
- *(none)*

## Related
- **Rest for one strategy** — Also suits dependency-aware setups; `one_for_one` is the no-dependency case.

## Contrasts With
- **One for all strategy** — Restarts *all* children on any crash; `one_for_one` restarts only the crashed one.
- **Rest for one strategy** — Restarts children started after the crashed one; `one_for_one` restarts none of the siblings.
- **Simple one for one strategy** — For many identical dynamic children; `one_for_one` allows heterogeneous static children.

# Common Errors

- **Error**: Using `one_for_one` for children that exchange synchronous requests and would lose them on a sibling's restart.
  **Correction**: Use `rest_for_one` or `one_for_all` when a restarted sibling would leave dependents in an inconsistent state.

# Common Confusions

- **Confusion**: Thinking `one_for_one` means "one restart only."
  **Clarification**: It means one *child* is restarted (the crashed one); the number of allowed restarts is set separately by intensity and period.

# Source Reference

Chapter 7: Supervisors, "The restart specification," pages 178-179. See Figure 8-7 (One for one).

# Verification Notes

- Definition source: Direct adaptation from pp. 178-179.
- Confidence rationale: HIGH — explicitly defined and illustrated with a figure and example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
