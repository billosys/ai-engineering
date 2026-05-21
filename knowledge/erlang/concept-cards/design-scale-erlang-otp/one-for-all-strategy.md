---
# === CORE IDENTIFICATION ===
concept: One for All Strategy
slug: one-for-all-strategy

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
  - "one_for_all"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
extends:
  - restart-strategy
related:
  - rest-for-one-strategy
contrasts_with:
  - one-for-one-strategy
  - rest-for-one-strategy
  - simple-one-for-one-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the one_for_one and one_for_all restart strategies?"
---

# Quick Definition

`one_for_all` is the supervisor restart strategy in which, when any child terminates, *all* children are terminated and restarted. It suits groups of children that all depend on each other.

# Core Definition

Under the `one_for_all` strategy, if a process terminates, all processes are terminated and restarted (Cesarini & Vinoski, p. 179). This strategy is used if all or most of the processes depend on each other. The book's example: a very complex FSM handling a protocol stack, split into separate FSMs that communicate with each other asynchronously and all depend on each other — if one terminates, the others would have to be terminated as well (p. 179).

# Prerequisites

- **Restart strategy** — `one_for_all` is one of the four restart strategy values.

# Key Properties

1. Termination of any one child causes *all* children to be terminated and restarted.
2. Appropriate when all or most children depend on each other.
3. Specified as the atom `one_for_all` in the supervisor specification.
4. The restart of all children is total, not ordered relative to the crashed child.

# Construction / Recognition

## To Construct/Create:
1. Confirm that the supervised children are mutually interdependent.
2. Set `strategy => one_for_all` (or the first tuple element) in the supervisor specification.

## To Identify/Recognize:
1. The supervisor specification's strategy is `one_for_all`.
2. A crash of any child takes down and restarts every sibling.

# Context & Application

- **Typical contexts**: Supervisors of a small set of tightly coupled processes.
- **Common applications**: A protocol stack split into communicating FSMs that all share state.
- **Historical/stylistic notes**: The book presents `one_for_all` as the choice "if all or most of the processes depend on each other" (p. 179).

# Examples

**Example 1** (p. 179): A protocol-stack FSM split into separate asynchronously communicating FSMs that all depend on each other — `one_for_all` is the recommended strategy.

## Worked Example

The book does not provide a full `one_for_all` code example; it describes the protocol-stack case (p. 179). A supervisor specification using it would read:

```erlang
%% All children interdependent: any crash restarts them all
{ok, {#{strategy => one_for_all, intensity => 2, period => 3600},
      ChildSpecList}}.
```

# Relationships

## Builds Upon
- **Restart strategy** — `one_for_all` is one specific restart strategy.

## Enables
- *(none)*

## Related
- **Rest for one strategy** — Also handles dependencies, but only restarts children started after the crashed one.

## Contrasts With
- **One for one strategy** — Restarts only the crashed child; `one_for_all` restarts every child.
- **Rest for one strategy** — Restarts only children started after the crashed one; `one_for_all` restarts all of them.
- **Simple one for one strategy** — For many identical dynamic children; `one_for_all` is for a fixed interdependent set.

# Common Errors

- **Error**: Using `one_for_all` for independent children.
  **Correction**: Use `one_for_one` so an isolated crash does not needlessly restart unrelated, healthy processes.

# Common Confusions

- **Confusion**: Believing `one_for_all` restarts children in dependency order like `rest_for_one`.
  **Clarification**: `one_for_all` terminates and restarts the *whole* set; `rest_for_one` restarts only the suffix of children started after the crashed one.

# Source Reference

Chapter 7: Supervisors, "The restart specification," page 179. See Figure 8-8 (One for all).

# Verification Notes

- Definition source: Direct adaptation from p. 179.
- Confidence rationale: HIGH — explicitly defined and illustrated with a figure.
- Uncertainties: The source provides a described scenario but no full code listing for `one_for_all`; the worked example is constructed from the strategy's documented form.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
