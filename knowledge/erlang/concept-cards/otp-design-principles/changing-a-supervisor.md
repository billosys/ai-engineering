---
# === CORE IDENTIFICATION ===
concept: Changing a Supervisor
slug: changing-a-supervisor

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Appup Cookbook"
chapter_number: null
pdf_page: null
section: "Changing a Supervisor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervisor upgrade"
  - "update supervisor instruction"
  - "{update, Module, supervisor}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - synchronized-code-replacement
  - child-specification
extends: []
related:
  - release-handling-instructions
  - restart-strategy
  - module-dependencies
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I change a supervisor's restart strategy during a release upgrade?"
  - "What appup instruction is used for supervisors?"
  - "Are child processes added or deleted automatically during a supervisor upgrade?"
---

# Quick Definition

A running supervisor's restart strategy, maximum restart frequency, and child specifications can be changed during a release upgrade using the special `{update, Module, supervisor}` instruction. Adding or deleting actual child processes is not automatic and must be scripted with `apply` instructions.

# Core Definition

The supervisor behaviour supports changing its internal state — the restart strategy and maximum restart frequency, as well as the existing child specifications (OTP Design Principles, "Appup Cookbook" > "Changing a Supervisor"). Because the supervisor changes its internal state, **synchronized code replacement** is required, using the special instruction `{update, Module, supervisor}`. During the upgrade the new callback module is loaded first (for both upgrade and downgrade), then the new return value of `init/1` is checked and the internal state changed accordingly.

Changing child *specifications* uses the same instruction, but does not affect already-running child processes; e.g. changing a child's start function only governs how it would be restarted later. The child specification `id` cannot be changed, and changing the `Modules` field can affect the release-handling process itself, since that field identifies which processes are touched by synchronized code replacement. Adding or deleting actual child processes is **not** handled automatically — new specs are added but children are not started or terminated without explicit `apply` instructions.

# Prerequisites

- **supervisor-behaviour** — you must understand supervisors, strategies, and child specs
- **synchronized-code-replacement** — supervisor changes require it
- **child-specification** — changing child specs is a core part of this operation

# Key Properties

1. Uses the dedicated instruction `{update, Module, supervisor}` (not a plain `load_module`/`update`).
2. The callback module is loaded before `init/1` is re-evaluated, for both upgrade and downgrade.
3. Restart strategy and maximum restart frequency can be changed by editing `init/1`.
4. Changing child specs does not restart or alter existing child processes.
5. A child specification `id` cannot be changed.
6. Adding/deleting child *processes* requires explicit `apply` instructions in the `.appup`.

# Construction / Recognition

## To Apply:
1. Edit `init/1` in the supervisor callback module to return the new strategy / child specs.
2. Write the `.appup` with `{update, Module, supervisor}` for both up- and downgrade.
3. For child-process additions/removals, add `apply` instructions to start/terminate them.

## To Recognize:
1. An `.appup` containing `{update, SupMod, supervisor}`.
2. A supervisor whose `init/1` return value differs between releases.

# Context & Application

- **Typical contexts**: live release upgrades that change supervision policy without downtime.
- **Common applications**: switching a supervisor from `one_for_one` to `one_for_all`; tightening restart frequency; revising a child's restart spec.

# Examples

**Example 1** (OTP Design Principles, "Changing a Supervisor"): changing `ch_sup`'s strategy from `one_for_one` to `one_for_all` —

```erlang
%% ch_sup.erl
init(_Args) ->
    {ok, {#{strategy => one_for_all, ...}, ...}}.
```

```erlang
%% ch_app.appup
{"2",
 [{"1", [{update, ch_sup, supervisor}]}],   % upgrade
 [{"1", [{update, ch_sup, supervisor}]}]}.   % downgrade
```

**Example 2**: changing an existing child specification uses the identical `{update, ch_sup, supervisor}` instruction; existing children are unaffected.

# Relationships

## Builds Upon
- **supervisor-behaviour** — the behaviour whose state is being changed
- **synchronized-code-replacement** — the mechanism this relies on

## Related
- **release-handling-instructions** — `{update, Module, supervisor}` is one such instruction
- **restart-strategy** — the property most commonly changed
- **module-dependencies** — load-order concerns in the same `.appup`

## Contrasts With
(none)

# Common Errors

- **Error**: Expecting child processes to be added/removed automatically when child specs change.
  **Correction**: Only specs are updated; start/terminate the processes explicitly with `apply` instructions.

- **Error**: Trying to change a child specification's `id` during upgrade.
  **Correction**: The `id` is immutable; restructure rather than rename in place.

# Common Confusions

- **Confusion**: Believing a plain `{update, Module, ...}` works for supervisors.
  **Clarification**: Supervisors require the special `{update, Module, supervisor}` form.

- **Confusion**: Thinking changing a child's start function restarts it.
  **Clarification**: It only governs future restarts; running children are untouched.

# Source Reference

Chapter "Appup Cookbook", section "Changing a Supervisor" (incl. "Changing Properties", "Changing Child Specifications", "Adding and Deleting Child Processes"), OTP Design Principles. Example references `ch_sup` from "Supervisor Behaviour".

# Verification Notes

- Definition source: Direct adaptation of the "Changing a Supervisor" section and its `ch_sup` example.
- Confidence rationale: HIGH — explicit instruction form, rules, and a worked `.appup` example.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified (`supervisor-behaviour`, `synchronized-code-replacement`, `child-specification`, `release-handling-instructions`, `restart-strategy`, `module-dependencies`).
- Re-extraction notes: New card filling a documented gap (was referenced by `synchronized-code-replacement`).
