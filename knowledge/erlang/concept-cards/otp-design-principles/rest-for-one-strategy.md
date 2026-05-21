---
# === CORE IDENTIFICATION ===
concept: Rest-for-One Strategy
slug: rest-for-one-strategy

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
section: "Restart Strategy / rest_for_one"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "rest_for_one"

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
  - one-for-all-strategy
  - simple-one-for-one-supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do restart strategies affect child processes?"
  - "What distinguishes one_for_one from one_for_all restart strategies?"
---

# Quick Definition

The `rest_for_one` restart strategy means that if a child process terminates, that child and all children started after it (in start order) are terminated and then restarted.

# Core Definition

If a child process terminates, the child processes after the terminated process in start order are terminated. Subsequently, the terminated child process and the remaining child processes (those started after it) are restarted. Processes are terminated right to left and restarted left to right. Children started before the terminated process are unaffected. (Source: sup_princ.md, "Restart Strategy / rest_for_one")

# Prerequisites

- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- Rest-for-one is a specific variant of restart strategy.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Strategies apply to supervisor processes.

# Key Properties

1. **Partial cascading restart**: Only the failed child and subsequent children (in start order) are affected.
2. **Predecessor preservation**: Children started before the failed child continue running.
3. **Termination order**: Affected children are terminated in reverse start order.
4. **Restart order**: Affected children are restarted in start order.
5. **Sequential dependency**: Appropriate when later children depend on earlier ones.

# Construction / Recognition

## To Construct/Create:
1. Set `strategy => rest_for_one` in supervisor flags.

```erlang
SupFlags = #{strategy => rest_for_one, intensity => 5, period => 30}
```

## To Identify/Recognize:
1. Look for `strategy => rest_for_one` in the supervisor flags map.

# Context & Application

Use `rest_for_one` when children have a sequential dependency chain -- later children depend on earlier ones, but not vice versa. For example, if process A provides a service that processes B and C need, but B and C do not depend on each other, and A does not depend on B or C, then `rest_for_one` ensures that when A fails, B and C are also restarted (since they depend on A), but when C fails, only C is restarted (A and B are fine).

# Examples

**Example 1** (sup_princ.md, "rest_for_one"): If child P2 terminates under `rest_for_one`, the supervisor terminates P3 and Pn (children after P2 in start order), then restarts P2, P3, and Pn. P1 is unaffected because it was started before P2.

# Relationships

## Builds Upon
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- Rest-for-one is a variant of restart strategy.

## Enables
- Sequential dependency management in supervision trees.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Temporary children are not restarted even when terminated by rest-for-one cascading.

## Contrasts With
- **[One-for-One Strategy](/concept-cards/otp-design-principles/one-for-one-strategy.md)** -- Does not restart any siblings.
- **[One-for-All Strategy](/concept-cards/otp-design-principles/one-for-all-strategy.md)** -- Restarts all siblings, including predecessors.

# Common Errors

- **Error**: Incorrect child ordering when using `rest_for_one` -- placing dependent children before their dependencies.
  **Correction**: Children that others depend on must be listed first in the child specification list, since `rest_for_one` only restarts children *after* the failed one.

# Common Confusions

- **Confusion**: `rest_for_one` restarts the "rest" of the children in some random order.
  **Clarification**: "Rest" means children that come after the failed child in the start order. Termination happens right-to-left and restart happens left-to-right, maintaining the original start sequence.

# Source Reference

sup_princ.md, "Restart Strategy / rest_for_one" section with diagram.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md.
- Confidence rationale: High -- explicitly defined with diagram.
- Uncertainties: None.
- Cross-reference status: Contrasts with one-for-one-strategy, one-for-all-strategy.
