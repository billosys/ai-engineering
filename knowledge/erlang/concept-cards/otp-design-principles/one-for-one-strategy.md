---
# === CORE IDENTIFICATION ===
concept: One-for-One Strategy
slug: one-for-one-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervisors
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Restart Strategy / one_for_one"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "one_for_one"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
  - supervisor-behaviour
extends:
  - restart-strategy
related:
  - child-specification
  - child-restart-type
contrasts_with:
  - one-for-all-strategy
  - rest-for-one-strategy
  - simple-one-for-one-supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes one_for_one from one_for_all restart strategies?"
  - "How do restart strategies affect child processes?"
---

# Quick Definition

The `one_for_one` restart strategy means that if a child process terminates, only that process is restarted; sibling processes are unaffected.

# Core Definition

If a child process terminates, only that process is restarted. This is the default restart strategy when no `strategy` key is specified in the supervisor flags. It is appropriate when child processes are independent of each other. (Source: sup_princ.md, "Restart Strategy / one_for_one")

# Prerequisites

- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- One-for-one is a specific variant of restart strategy.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Strategies apply to supervisor processes.

# Key Properties

1. **Isolated restart**: Only the terminated child is restarted.
2. **Default strategy**: Used when `strategy` is not specified in supervisor flags.
3. **Independent children**: Appropriate when children do not depend on each other.
4. **No cascading effect**: Sibling processes continue running undisturbed.

# Construction / Recognition

## To Construct/Create:
1. Set `strategy => one_for_one` in supervisor flags, or omit the `strategy` key entirely (it defaults to `one_for_one`).

```erlang
SupFlags = #{strategy => one_for_one, intensity => 1, period => 5}
```

## To Identify/Recognize:
1. Look for `strategy => one_for_one` in the supervisor flags map, or absence of a `strategy` key.

# Context & Application

Use `one_for_one` when each child process is independent and a failure in one does not affect the ability of others to continue. This is the most common restart strategy and is suitable for pools of independent workers, separate service processes within an application, or any scenario where children do not share critical mutable state.

# Examples

**Example 1** (sup_princ.md, "one_for_one"): If child P2 terminates, only P2 is restarted. Children P1, P3, and Pn continue running.

**Example 2** (sup_princ.md, "Example"): Supervisor with one_for_one strategy:

```erlang
SupFlags = #{strategy => one_for_one, intensity => 1, period => 5},
ChildSpecs = [#{id => ch3,
                start => {ch3, start_link, []},
                shutdown => brutal_kill}],
{ok, {SupFlags, ChildSpecs}}.
```

# Relationships

## Builds Upon
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- One-for-one is a variant of restart strategy.

## Enables
- Independent child process management without cascading effects.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Determines whether a specific child is restarted at all.

## Contrasts With
- **[One-for-All Strategy](/concept-cards/otp-design-principles/one-for-all-strategy.md)** -- Restarts all children, not just the failed one.
- **[Rest-for-One Strategy](/concept-cards/otp-design-principles/rest-for-one-strategy.md)** -- Restarts the failed child plus all children started after it.
- **[Simple One-for-One Supervisor](/concept-cards/otp-design-principles/simple-one-for-one-supervisor.md)** -- A specialized variant for dynamic homogeneous children.

# Common Errors

- **Error**: Using `one_for_one` when children have interdependencies that require coordinated restart.
  **Correction**: If children share state or depend on each other, use `one_for_all` or `rest_for_one` to ensure consistent restart.

# Common Confusions

- **Confusion**: `one_for_one` means only one child can ever be restarted.
  **Clarification**: It means that for any single child failure, only that one child is restarted. Multiple children can fail and be restarted independently over time.

# Source Reference

sup_princ.md, "Restart Strategy / one_for_one" section.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md.
- Confidence rationale: High -- explicitly defined with diagram.
- Uncertainties: None.
- Cross-reference status: Contrasts with all other strategy cards.
