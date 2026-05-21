---
# === CORE IDENTIFICATION ===
concept: Module Dependencies (Release Upgrade)
slug: module-dependencies

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
section: "Module Dependencies"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "DepMods"
  - "load order dependencies"
  - "dependent modules in appup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application-upgrade-file
  - synchronized-code-replacement
extends: []
related:
  - release-handling-instructions
  - changing-a-supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I ensure one module is loaded before another during a release upgrade?"
  - "What is the DepMods element in a release handling instruction?"
  - "Why can a runtime error occur during upgrade if module load order is wrong?"
---

# Quick Definition

When one module calls a new function in another, the called module must be loaded first during an upgrade (and last during a downgrade). This load ordering is declared with the `DepMods` element of a `load_module` or `update` instruction in the `.appup` file.

# Core Definition

If module `m1` adds a call to a newly introduced function in module `ch3` (e.g. `ch3:available/0`), a runtime error can occur during a release upgrade if the new `m1` is loaded and called *before* the new `ch3` is loaded (OTP Design Principles, "Appup Cookbook" > "Module Dependencies"). Therefore `ch3` must be loaded before `m1` on upgrade, and conversely on downgrade. `m1` is said to be *dependent on* `ch3`. This dependency is expressed by the `DepMods` element of a release-handling instruction:

```text
{load_module, Module, DepMods}
{update, Module, {advanced, Extra}, DepMods}
```

`DepMods` is a list of modules on which `Module` depends. `systools` knows the difference between up- and downgrading and generates a correct `relup` in which `ch3` is loaded before `m1` when upgrading, and `m1` before `ch3` when downgrading.

# Prerequisites

- **application-upgrade-file** — `DepMods` is declared inside the `.appup`
- **synchronized-code-replacement** — load ordering matters during code replacement

# Key Properties

1. A dependency means the depended-on module must be loaded first on upgrade.
2. Declared via the `DepMods` list in `{load_module, Module, DepMods}` or `{update, Module, {advanced, Extra}, DepMods}`.
3. `DepMods` lists the modules that `Module` depends on.
4. `systools` automatically reverses the order for downgrade in the generated `relup`.
5. Dependencies can be expressed within one `.appup` (same application) or across two `.appup` files (different applications).

# Construction / Recognition

## To Apply:
1. Identify which module calls a newly added function in another module.
2. List the depended-on module(s) in the `DepMods` element of the dependent module's instruction.
3. Let `systools` generate the `relup`; it orders loads correctly for both directions.

## To Recognize:
1. A `load_module` or `update` instruction with a non-empty third/fourth `DepMods` argument.
2. Cross-`.appup` ordering between cooperating applications.

# Context & Application

- **Typical contexts**: live upgrades where a caller and callee evolve together and load order affects correctness.
- **Common applications**: adding an interface function to a library module that an application module begins to call.

# Examples

**Example 1** (OTP Design Principles, "Module Dependencies"): `m1` (in `myapp`) depends on `ch3` —

```erlang
%% myapp.appup
{"2",
 [{"1", [{load_module, m1, [ch3]}]}],
 [{"1", [{load_module, m1, [ch3]}]}]}.

%% ch_app.appup
{"2",
 [{"1", [{load_module, ch3}]}],
 [{"1", [{load_module, ch3}]}]}.
```

**Example 2**: same-application form, ordering both loads in one instruction list —

```erlang
{"2",
 [{"1", [{load_module, ch3}, {load_module, m1, [ch3]}]}],
 [{"1", [{load_module, ch3}, {load_module, m1, [ch3]}]}]}.
```

# Relationships

## Builds Upon
- **application-upgrade-file** — the `.appup` where `DepMods` is written
- **synchronized-code-replacement** — the broader mechanism load order serves

## Related
- **release-handling-instructions** — `load_module`/`update` are such instructions
- **changing-a-supervisor** — another Appup Cookbook scenario in the same file

## Contrasts With
(none)

# Common Errors

- **Error**: Loading a calling module before the module providing a newly added function.
  **Correction**: Declare the dependency in `DepMods` so the callee loads first on upgrade.

- **Error**: Hand-ordering instructions for downgrade.
  **Correction**: `systools` reverses order automatically in the generated `relup`; declare the dependency once.

# Common Confusions

- **Confusion**: Believing load order does not matter because all modules are eventually loaded.
  **Clarification**: A new caller can execute against an old callee mid-upgrade, raising a runtime error; order is what prevents this.

- **Confusion**: Thinking `DepMods` lists modules that depend on `Module`.
  **Clarification**: It lists modules that `Module` depends *on*.

# Source Reference

Chapter "Appup Cookbook", section "Module Dependencies" (OTP Design Principles), including the `m1`/`ch3` `.appup` examples and the `systools`/`relup` ordering note.

# Verification Notes

- Definition source: Direct adaptation of the "Module Dependencies" section and its examples.
- Confidence rationale: HIGH — explicit instruction forms and two worked `.appup` examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified (`application-upgrade-file`, `synchronized-code-replacement`, `release-handling-instructions`, `changing-a-supervisor`).
- Re-extraction notes: New card filling a documented gap (was referenced by `application-upgrade-file`).
