---
# === CORE IDENTIFICATION ===
concept: Software Upgrade
slug: software-upgrade

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-upgrades
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Software Upgrades"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - hot code loading
  - dynamic module loading
  - live upgrade
  - software downgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module-versioning
extends: []
related:
  - code-change-callback
  - fully-qualified-function-call
  - release-upgrade
  - two-module-limit
contrasts_with:
  - release-upgrade

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a software upgrade in Erlang?"
  - "What must I understand before performing release upgrades?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

A software upgrade is the replacement of running code with a new version without stopping the system. Erlang's built-in dynamic module loading is the foundation on which OTP builds coordinated, controlled upgrade tools.

# Core Definition

The built-in functionality in the Erlang VM that allows dynamic module loading might work for simple patches where the upgrade is backward-compatible (Cesarini & Vinoski, p. 336-339, pdf p. 336). A new module is loaded with the shell command `l(Module)`, `code:load_file(Module)`, or by recompiling with `c(Module)` or `make:files(ModuleList,[load])`. At any one time the runtime can have two versions of a module loaded — the *old* and the *current*. A process running the old version continues doing so until it issues a fully qualified function call, at which point the runtime switches it to the current version. Complex systems need to be upgraded in a coordinated and controlled manner; the built-in functionality provides the foundations for the tools that coordinate and control these upgrades.

# Prerequisites

- **Module versioning** — Upgrades depend on distinguishing module versions; the `-vsn` attribute and the two-version model are required.

# Key Properties

1. Loads new code while the system keeps running.
2. New code loaded via `l/1`, `code:load_file/1`, `c/1`, or `make:files/2`.
3. At most two module versions exist at once: old and current.
4. A process on the old version keeps running it until a fully qualified call switches it to the current version.
5. Library-module calls are fully qualified and automatically use the current version.
6. Local recursive calls (receive-evaluate loops) must be made fully qualified or triggered by an upgrade message.
7. A process running the old version is unconditionally terminated when a third version is loaded or `code:purge/1` removes the old code.
8. Built-in upgrades handle simple backward-compatible patches; API changes, protocol changes, and state changes need coordinated OTP upgrades.

# Construction / Recognition

## To Perform a Basic Software Upgrade:
1. Compile the new module version into a code-path directory (e.g. `patches`).
2. Load it with `code:load_file/1` or `l/1` — it becomes the current version.
3. For receive-evaluate-loop processes, send an `{upgrade, Data}` message that triggers a fully qualified call to `code_change/2`.
4. In `code_change/2`, adapt the process state and tail-call back into the loop in the new module.

## To Recognize an Upgrade Path:
1. Look for a `{upgrade, Data}` message handled in every state.
2. Look for a fully qualified `?MODULE:code_change/2` call.

# Context & Application

- **Typical contexts**: Patching bugs and adding features to a live system without downtime.
- **Common applications**: Systems requiring 100% availability — coffee machines, telecom switches — where firmware upgrades cannot interrupt service.
- **Historical/stylistic notes**: The recommended approach separates loading the new module from each process's trigger of the upgrade.

# Examples

**Example 1** (p. 339): Generic upgrade code for the coffee FSM handles `{upgrade, Data}` in every state, calling `?MODULE:code_change(fun selection/0, Data)`:

```erlang
selection() ->
 receive
   ...
   {upgrade, Data} ->
     ?MODULE:code_change(fun selection/0, Data);
   ...
 end.
code_change({payment, Type, Price, Paid}, _) ->
 payment(Type, Price, Paid);
code_change(State, _) ->
 State().
```

**Example 2** (p. 343): Loading version 1.1 of the coffee module with `l(coffee)` while the FSM process still runs the old version; ordering an espresso uses the current version, the FSM process uses the old.

# Relationships

## Builds Upon
- **Module versioning** — Upgrades rely on distinguishing old and current module versions.

## Enables
- **Release upgrade** — OTP's release-upgrade tools build on basic software-upgrade mechanics.

## Related
- **Code change callback** — `code_change` adapts process state during an upgrade.
- **Fully qualified function call** — The mechanism that switches a process to the current code.
- **Two-module limit** — Why only two versions can coexist.

## Contrasts With
- **Release upgrade** — A software upgrade replaces modules; a release upgrade is the coordinated, OTP-tooled, multi-application version of it.

# Common Errors

- **Error**: Loading a third module version while a process still runs the oldest.
  **Correction**: A process running the now-deleted old version is unconditionally terminated; upgrade or trigger code_change before loading again.

- **Error**: Relying on local recursive calls to pick up new code.
  **Correction**: Local calls do not switch versions; make the call fully qualified or trigger one via an upgrade message.

# Common Confusions

- **Confusion**: Thinking dynamic module loading alone handles any upgrade.
  **Clarification**: It handles simple backward-compatible patches; API, protocol, or state changes require coordinated OTP upgrades.

- **Confusion**: Believing a process picks up new code immediately on load.
  **Clarification**: A process keeps running its current version until it makes a fully qualified call.

# Source Reference

Chapter 11: Release Upgrades, section "Software Upgrades," pages 336-339 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 336-339.
- Confidence rationale: HIGH — the source explicitly describes the software-upgrade mechanism and the old/current version model.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
