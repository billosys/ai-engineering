---
# === CORE IDENTIFICATION ===
concept: Restart Strategy
slug: restart-strategy

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
  - "restart type"
  - "supervisor strategy"
  - "RestartStrategy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervisor-specification
extends: []
related:
  - restart-intensity-and-period
  - one-for-one-strategy
  - one-for-all-strategy
  - rest-for-one-strategy
  - simple-one-for-one-strategy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a supervisor and define its child specifications?"
  - "What is the difference between the one_for_one and one_for_all restart strategies?"
---

# Quick Definition

A restart strategy tells a supervisor what to do to its *other* children when one child terminates abnormally. OTP provides four: `one_for_one`, `one_for_all`, `rest_for_one`, and `simple_one_for_one`.

# Core Definition

The restart strategy is the first element of the restart tuple `{RestartType, MaxRestart, MaxTime}`, which specifies what happens to the other children in a supervision tree if a child (worker or supervisor) terminates abnormally (Cesarini & Vinoski, p. 178). There are four restart types: `one_for_one` (restart only the crashed child), `one_for_all` (terminate and restart all children), `rest_for_one` (terminate and restart all children started *after* the crashed one), and `simple_one_for_one` (for dynamically added children sharing one child specification). The strategy is chosen to reflect the dependency relationships among the supervised children (pp. 178-180).

# Prerequisites

- **Supervisor** — A restart strategy is a property of a supervisor.
- **Supervisor specification** — The strategy is part of the restart tuple/map within the supervisor specification.

# Key Properties

1. Determines the effect of one child's abnormal termination on the other children.
2. Four values: `one_for_one`, `one_for_all`, `rest_for_one`, `simple_one_for_one`.
3. Appears as the first element of the `{RestartStrategy, MaxR, MaxT}` tuple, or the `strategy` key in the map form (Erlang 18.0+).
4. The right strategy depends on whether and how the children depend on each other.
5. Choosing well requires designing the start order together with the strategy.

# Construction / Recognition

## To Construct/Create:
1. Analyze the dependencies among the supervised children.
2. Pick `one_for_one` for independent children, `one_for_all` for fully interdependent ones, `rest_for_one` for children started in dependency order, `simple_one_for_one` for many identical dynamic children.
3. Place the chosen atom as the `strategy` of the supervisor specification.

## To Identify/Recognize:
1. It is the `strategy` key (map) or first tuple element of the supervisor's restart configuration.

# Context & Application

- **Typical contexts**: Every supervisor specification.
- **Common applications**: Tuning fault isolation versus coordinated restart.
- **Historical/stylistic notes**: The book stresses there is "no one size fits all" solution — the strategy depends on the requirements and the behavior you want from the system (p. 180).

# Examples

**Example 1** (p. 175): `frequency_sup` uses `rest_for_one` because the frequency allocator depends on the overload manager started before it.

**Example 2** (p. 184): `phone_sup` uses `one_for_one` because mobile devices run independently of each other.

## Worked Example

Selecting `rest_for_one` for dependency-ordered children (p. 175):

```erlang
init(_) ->
    ChildSpecList = [child(freq_overload), child(frequency)],
    {ok,{{rest_for_one, 2, 3600}, ChildSpecList}}.
```

`freq_overload` starts first; if it crashes, `frequency` (started after it) is terminated and both are restarted in order.

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Supervisor** — The strategy governs how a supervisor reacts to a child crash.

## Related
- **Restart intensity and period** — Accompany the strategy in the restart tuple.
- **One for one strategy** / **One for all strategy** / **Rest for one strategy** / **Simple one for one strategy** — The four specific strategy values.

## Contrasts With
- *(none — the four specific strategies contrast with each other on their own cards)*

# Common Errors

- **Error**: Choosing a strategy without designing the child start order.
  **Correction**: Design start order and restart strategy together; `rest_for_one` is meaningless without dependency-ordered children.

- **Error**: Using `one_for_one` for interdependent children that lose messages on restart.
  **Correction**: Use `rest_for_one` or `one_for_all` when a restarted child could miss requests from its dependents.

# Common Confusions

- **Confusion**: Thinking the restart strategy decides whether a *single* child restarts.
  **Clarification**: Whether a child restarts on its own termination is the *restart type* (`permanent`/`transient`/`temporary`); the restart *strategy* decides what happens to the *other* children.

# Source Reference

Chapter 7: Supervisors, "The restart specification," pages 178-180. See Figures 8-7 through 8-9.

# Verification Notes

- Definition source: Direct adaptation from pp. 178-180.
- Confidence rationale: HIGH — explicitly defined with all four values enumerated and illustrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
