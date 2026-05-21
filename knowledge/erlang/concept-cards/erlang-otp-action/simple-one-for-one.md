---
# === CORE IDENTIFICATION ===
concept: simple_one_for_one Supervision
slug: simple-one-for-one

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.3.4 Implementing the supervisor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - simple_one_for_one
  - "simple-one-for-one supervision"
  - "supervisor as factory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervisor-restart-strategy
  - child-specification
extends:
  - supervisor-restart-strategy
related:
  - sc-element
  - supervisor-start-child
contrasts_with:
  - supervisor-restart-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple_one_for_one supervisor?"
  - "How does simple_one_for_one differ from one_for_one?"
  - "How do you dynamically add children to a simple_one_for_one supervisor?"
---

# Quick Definition

A `simple_one_for_one` supervisor can start only one type of child but any number of them, all added dynamically at runtime from a single shared child specification — effectively a factory for identical worker processes.

# Core Definition

`simple_one_for_one` is a supervisor restart strategy for a supervisor that does not have statically specified permanent children but instead any number of dynamically added children all of the same type (Ch. 6, Section 6.3.4). With other strategies such as `one_for_one`, a supervisor typically manages children that all start when the supervisor starts and run for as long as it does. A `simple_one_for_one` supervisor can start only one type of child but any number of them; all its children are added dynamically at runtime, and no child is started when the supervisor starts up. Its `init/1` must specify exactly one child specification — the template — but it is not started with the supervisor. New children are started with a simplified form of `supervisor:start_child/2` that only supplies the per-child extra arguments, since the supervisor already knows the shared specification.

# Prerequisites

- **Supervisor** — `simple_one_for_one` is a supervisor strategy.
- **Supervisor restart strategy** — It is one of the available `How` values.
- **Child specification** — A `simple_one_for_one` supervisor has exactly one template child spec.

# Key Properties

1. Starts only one type of child, but any number of them.
2. All children are added dynamically at runtime.
3. No child is started when the supervisor starts up.
4. `init/1` must specify exactly one (template) child specification.
5. New children are started via a simplified `supervisor:start_child/2`.
6. Effectively a factory for identical worker processes.

# Construction / Recognition

## To Set Up a simple_one_for_one Supervisor:
1. In `init/1`, set the strategy to `simple_one_for_one`.
2. Provide exactly one child specification — the template for all children.
3. Mark the children appropriately (e.g. `temporary`, `brutal_kill`).
4. Add an API function calling `supervisor:start_child/2` with the per-child extra arguments.

# Context & Application

`simple_one_for_one` suits cases where many identical, dynamically created processes are needed — like one process per cached value.

- **Typical contexts**: Factories of identical worker processes; connection pools; per-item processes.
- **Common applications**: `sc_sup` is a `simple_one_for_one` supervisor — a factory for `sc_element` processes.

# Examples

**Example 1** (Ch. 6, Listing 6.2): `sc_sup` uses `simple_one_for_one` with zero restarts per 1 second; children are `temporary` with `brutal_kill` shutdown.

**Example 2** (Ch. 6): `sc_sup:start_child/2` calls `supervisor:start_child/2` with extra args `Value` and `LeaseTime`, which are appended to the template spec's empty arg list, producing `sc_element:start_link(Value, LeaseTime)`.

# Relationships

## Builds Upon
- **Supervisor restart strategy** — `simple_one_for_one` is a specific `How` value.

## Related
- **sc-element** — The dynamically created children of the cache's `simple_one_for_one` supervisor.
- **supervisor-start-child** — Used to add children at runtime.

## Contrasts With
- **supervisor-restart-strategy** — Under `one_for_one` children start with the supervisor; under `simple_one_for_one` all children are dynamic and identical.

# Common Errors

- **Error**: Specifying multiple child specifications for a `simple_one_for_one` supervisor.
  **Correction**: `init/1` must specify exactly one — the shared template.

# Common Confusions

- **Confusion**: Expecting children to start when the supervisor starts.
  **Clarification**: A `simple_one_for_one` supervisor starts no children at startup; all are added dynamically later.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.3.4 "Implementing the supervisor," including the "Simple-one-for-one supervision" subsection and Listing 6.2.

# Verification Notes

- Definition source: Direct adaptation of Section 6.3.4.
- Confidence rationale: HIGH — explicit, dedicated treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
