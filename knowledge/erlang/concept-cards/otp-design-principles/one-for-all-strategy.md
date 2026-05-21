---
# === CORE IDENTIFICATION ===
concept: One-for-All Strategy
slug: one-for-all-strategy

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
section: "Restart Strategy / one_for_all"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "one_for_all"

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
  - one-for-one-strategy
  - rest-for-one-strategy
  - simple-one-for-one-supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes one_for_one from one_for_all restart strategies?"
  - "How do restart strategies affect child processes?"
---

# Quick Definition

The `one_for_all` restart strategy means that if any child process terminates, all remaining child processes are terminated and then all children (including the failed one) are restarted.

# Core Definition

If a child process terminates, all remaining child processes are terminated. Subsequently, all child processes, including the terminated one, are restarted. Processes are terminated right to left (reverse start order) and restarted left to right (start order). (Source: sup_princ.md, "Restart Strategy / one_for_all")

# Prerequisites

- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- One-for-all is a specific variant of restart strategy.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Strategies apply to supervisor processes.

# Key Properties

1. **Full restart**: All children are terminated and restarted when any child fails.
2. **Termination order**: Remaining children are terminated in reverse start order (right to left).
3. **Restart order**: All children are restarted in start order (left to right).
4. **Tightly coupled children**: Appropriate when all children depend on each other.
5. **Temporary exception**: A `temporary` child is never restarted, even under `one_for_all` -- it is terminated but not restarted.

# Construction / Recognition

## To Construct/Create:
1. Set `strategy => one_for_all` in supervisor flags.

```erlang
SupFlags = #{strategy => one_for_all, intensity => 1, period => 5}
```

## To Identify/Recognize:
1. Look for `strategy => one_for_all` in the supervisor flags map.

# Context & Application

Use `one_for_all` when children are tightly coupled and none can function correctly without the others. This is common when children share state or resources that become inconsistent when one child dies. For example, a database connection pool manager and its associated worker processes might use this strategy if workers cannot function without the pool manager.

# Examples

**Example 1** (sup_princ.md, "one_for_all"): If child P2 terminates, the supervisor terminates P1, P3, and Pn (right to left), then restarts all of P1, P2, P3, and Pn (left to right).

# Relationships

## Builds Upon
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- One-for-all is a variant of restart strategy.

## Enables
- Coordinated restart of tightly coupled process groups.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Temporary children are not restarted even under one-for-all.

## Contrasts With
- **[One-for-One Strategy](/concept-cards/otp-design-principles/one-for-one-strategy.md)** -- Restarts only the failed child, not siblings.
- **[Rest-for-One Strategy](/concept-cards/otp-design-principles/rest-for-one-strategy.md)** -- Restarts only subsequent children, not predecessors.

# Common Errors

- **Error**: Using `one_for_all` for independent children, causing unnecessary disruption on every failure.
  **Correction**: Only use `one_for_all` when children genuinely depend on each other. Use `one_for_one` for independent children.

# Common Confusions

- **Confusion**: Under `one_for_all`, automatic shutdown is triggered when the supervisor terminates a sibling.
  **Clarification**: The automatic shutdown facility only applies when significant children terminate by themselves. Termination of a child as a consequence of a sibling's termination in the `one_for_all` strategy does not trigger automatic shutdown.

# Source Reference

sup_princ.md, "Restart Strategy / one_for_all" section with diagram.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md.
- Confidence rationale: High -- explicitly defined with diagram showing termination and restart order.
- Uncertainties: None.
- Cross-reference status: Contrasts with one-for-one-strategy, rest-for-one-strategy.
