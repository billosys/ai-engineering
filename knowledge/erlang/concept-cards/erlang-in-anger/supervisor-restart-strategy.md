---
concept: Supervisor Restart Strategy
slug: supervisor-restart-strategy
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Regular Applications"
extraction_confidence: high
aliases:
  - "Restart strategy"
prerequisites:
  - regular-application
  - let-it-crash
extends: []
related:
  - supervision-tree-navigation
  - behaviour-as-navigation-clue
contrasts_with: []
answers_questions:
  - "What can be said of processes under a one_for_all scheme for supervision?"
  - "How do restart strategies relate to child relationships?"
---

# Quick Definition

A supervisor's restart strategy declares how the failure of one child process affects its siblings, and thereby reflects the dependency relationships among those processes.

# Core Definition

From Chapter 1, section "Regular Applications": "The supervisor restart strategy reflects the relationship between processes under a supervisor." The four strategies:

- `one_for_one` and `simple_one_for_one` — for processes that are not directly dependent on each other, although their failures are still collectively counted toward total application shutdown.
- `rest_for_one` — for processes that depend on each other in a linear manner: a child's failure restarts it and all children started after it.
- `one_for_all` — for processes that entirely depend on each other: any child's failure restarts all of them.

# Prerequisites

- `regular-application` — restart strategies live in the supervisors of a regular application.
- `let-it-crash` — restart strategies are the mechanism implementing the "let it crash" philosophy.

# Key Properties

1. The strategy encodes the dependency relationship among a supervisor's children.
2. `one_for_one` / `simple_one_for_one`: children are independent; one crash does not restart the others (though failures count toward the supervisor's total shutdown limit).
3. `rest_for_one`: children depend linearly; a crash restarts the failing child and every child started after it.
4. `one_for_all`: children fully depend on each other; one crash restarts them all.
5. Reading a supervisor's strategy tells you, at a glance, how tightly coupled its children are.

# Construction / Recognition

When diving into code, read each supervisor's `init/1` to find its strategy. Use the strategy to infer process relationships: `one_for_all` means fully interdependent children; `rest_for_one` means a linear dependency chain; `one_for_one` means independent children.

# Context & Application

Restart strategies are a primary navigation clue when exploring a supervision tree, and a primary design decision when building one. They embody the OTP principle that restarting interdependent processes together returns the subsystem to a clean, known state.

# Examples

From Chapter 1, section "Regular Applications": "worker processes that depend on each other within the same application (say, a process that buffers socket communications and relays them to a finite-state machine in charge of understanding the protocol) are likely to be regrouped under the same supervisor and to fail together." A footnote warns that "Some developers will use `one_for_one` supervisors when `rest_for_one` is more appropriate" — such supervisors boot in strict order but forget that order on restart.

# Relationships

## Builds Upon
- `let-it-crash` — strategies are how crashes are handled.
- `regular-application` — supervisors live inside regular applications.

## Enables
- `supervision-tree-navigation` — strategy is a key clue during navigation.

## Related
- `behaviour-as-navigation-clue` — both reveal process roles and relationships.

## Contrasts With
Nothing directly — the four strategies contrast with one another.

# Common Errors

- Using `one_for_one` where `rest_for_one` is appropriate: the processes need strict start ordering, but the wrong strategy ignores that order on restart or when a predecessor dies (Chapter 1 footnote).

# Common Confusions

- `one_for_one` does not mean failures are "free": a child's crashes still count toward the supervisor's total restart limit, which can trigger application shutdown.
- `simple_one_for_one` is for many dynamically-added children of the same type, not a different dependency relationship from `one_for_one`.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Regular Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, section "Regular Applications."
- Confidence rationale: high — all four strategies explicitly described.
- Uncertainties: none.
- Cross-reference status: Verified
