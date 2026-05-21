---
# === CORE IDENTIFICATION ===
concept: Implementing a Supervisor
slug: supervisor-implementation

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.2.1 Implementing a supervisor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - supervisor module
  - "supervisor:start_link/3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - behaviour-callback-module
extends:
  - supervisor
related:
  - supervisor-restart-strategy
  - child-specification
  - root-supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you implement a supervisor module?"
  - "What does a supervisor's init/1 callback return?"
  - "What does supervisor:start_link/3 do?"
---

# Quick Definition

Implementing a supervisor means writing a module with `-behaviour(supervisor)`, an API function calling `supervisor:start_link/3`, and an `init/1` callback returning the restart strategy and child specifications.

# Core Definition

A supervisor is created by writing a module that implements the `supervisor` behaviour (Ch. 4, Section 4.2.1). The module typically has an API function (so it can be started from the application behaviour module) plus the behaviour callback `init/1`. The `start_link()` API function launches the supervisor by calling the library function `supervisor:start_link/3`, passing it the registration spec (e.g. `{local, ?SERVER}`), the module name, and an argument passed on to `init/1`. Most of the interesting work is in `init/1`, whose return value tells the OTP supervisor library exactly how the child processes should be started and managed and how the supervisor itself should behave: it returns `{ok, {RestartStrategy, Children}}`.

# Prerequisites

- **Supervisor** — Implementation produces a supervisor.
- **Behaviour callback module** — A supervisor is a behaviour callback module.

# Key Properties

1. The module declares `-behaviour(supervisor)`.
2. It usually has a `start_link` API function plus the `init/1` callback.
3. `start_link` calls `supervisor:start_link/3`.
4. `init/1` returns `{ok, {RestartStrategy, Children}}`.
5. `Children` is a list of child specifications.
6. The third argument of `start_link/3` is passed to `init/1`.

# Construction / Recognition

## To Implement a Supervisor:
1. Write a module with `-module` and `-behaviour(supervisor)`.
2. Add a `start_link/0` API function calling `supervisor:start_link({local, ?SERVER}, ?MODULE, [])`.
3. Implement `init/1`.
4. In `init/1`, define the restart strategy.
5. Build a list of child specifications.
6. Return `{ok, {RestartStrategy, Children}}`.

# Context & Application

A supervisor module is short — often two tiny modules' worth of code yields a lot of fault-tolerance functionality. The book recommends keeping supervisors small.

- **Typical contexts**: The root supervisor and any subsystem supervisors of an application.
- **Common applications**: `tr_sup` (Listing 4.3) and `sc_sup` (Listing 6.2).

# Examples

**Example 1** (Ch. 4, Listing 4.3): `tr_sup` implements `supervisor`; `start_link()` calls `supervisor:start_link({local, ?SERVER}, ?MODULE, [])`, and `init/1` returns the restart strategy and a single child spec for `tr_server`.

**Example 2** (Ch. 6, Listing 6.2): `sc_sup` is implemented similarly but with two API functions (`start_link/0` and `start_child/2`) and a `simple_one_for_one` strategy.

# Relationships

## Builds Upon
- **Supervisor** — Implementation produces a supervisor.

## Related
- **supervisor-restart-strategy** — Defined inside `init/1`.
- **child-specification** — `init/1` returns a list of them.
- **root-supervisor** — The `_sup` module is implemented this way.

## Contrasts With
- This is a procedure; the source draws no direct contrast.

# Common Errors

- **Error**: Passing a non-empty argument to `init/1` when it needs no input.
  **Correction**: Pass an empty list as the third argument to `supervisor:start_link/3`.

# Common Confusions

- **Confusion**: Thinking the supervisor module needs many callbacks like a `gen_server`.
  **Clarification**: A supervisor needs essentially only `init/1`; the rest is generic library code.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.2.1 "Implementing a supervisor," Listing 4.3. Chapter 6, Section 6.3.4, Listing 6.2.

# Verification Notes

- Definition source: Direct adaptation of Section 4.2.1.
- Confidence rationale: HIGH — explicit, worked treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
