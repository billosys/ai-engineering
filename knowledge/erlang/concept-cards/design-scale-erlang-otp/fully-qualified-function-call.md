---
# === CORE IDENTIFICATION ===
concept: Fully Qualified Function Call
slug: fully-qualified-function-call

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
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
  - remote call
  - "Module:Function call"
  - external call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - software-upgrade
extends: []
related:
  - two-module-limit
  - code-change-callback
  - module-versioning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fully qualified function call and why does it matter for upgrades?"
  - "What must I understand before performing release upgrades?"
---

# Quick Definition

A fully qualified function call is a call of the form `Module:Function(...)`, with the module name as an explicit prefix. It is the mechanism by which a process running old code switches to the current version of a module.

# Core Definition

A process running the old module version will continue doing so until it issues a fully qualified function call — i.e., a call of the format `Module:Function(...)`, where the module name is used as a prefix to the function (Cesarini & Vinoski, p. 337, pdf p. 336). When a fully qualified function call occurs, the runtime checks whether the process is running the current version of the code; if it is, the call continues using the current code, and if the process is still running the old version, the pointer to the code is switched to the current version before the call is made. Calls to library modules are always fully qualified (you are calling another module) so they automatically use the current version; recursive calls controlling a process's receive-evaluate loop tend to recurse locally without a fully qualified call.

# Prerequisites

- **Software upgrade** — The fully qualified call is the upgrade-switch mechanism; the upgrade concept comes first.

# Key Properties

1. Has the form `Module:Function(...)` with an explicit module prefix.
2. Triggers the runtime to switch a process from old to current code.
3. Library-module calls are inherently fully qualified, so they always use the current version.
4. Local recursive calls (no module prefix) do not switch versions.
5. Receive-evaluate loops must either be made fully qualified or trigger one via an upgrade message.
6. The version switch happens before the call is made, only if the process is still on the old version.

# Construction / Recognition

## To Use It for an Upgrade:
1. Either change the loop's recursive call to `?MODULE:loop(...)`, or
2. Add an `{upgrade, Data}` message to the receive loop that issues `?MODULE:code_change(...)`.
3. The fully qualified call switches the process to the current code.

## To Recognize It:
1. Look for a `Module:Function(...)` call with an explicit prefix (often `?MODULE:...`).

# Context & Application

- **Typical contexts**: Designing receive-evaluate loops so they can pick up upgraded code.
- **Common applications**: Triggering `code_change` during a software upgrade; library calls automatically running the newest code.
- **Historical/stylistic notes**: The recommended upgrade design separates loading the new module from each process's fully qualified trigger of the upgrade.

# Examples

**Example 1** (p. 339): The coffee FSM's receive loop triggers a fully qualified call on the upgrade message: `{upgrade, Data} -> ?MODULE:code_change(fun selection/0, Data)`.

**Example 2** (p. 343): After loading version 1.1, ordering an espresso via the shell does a fully qualified call using the current version, while the FSM process still runs the old version until it makes its own fully qualified call.

# Relationships

## Builds Upon
- **Software upgrade** — The fully qualified call is the mechanism that completes an upgrade for a process.

## Related
- **Two-module limit** — The call moves a process from the old version to the current one.
- **Code change callback** — Typically invoked via a fully qualified call during an upgrade.
- **Module versioning** — The runtime checks the process's version when a fully qualified call occurs.

# Common Errors

- **Error**: Keeping a receive-evaluate loop with only local recursive calls.
  **Correction**: Local calls never switch versions; make the loop call fully qualified or add an upgrade-trigger message.

- **Error**: Assuming a process picks up new code on the next message.
  **Correction**: Only a fully qualified call switches the version; ordinary local recursion keeps the old code.

# Common Confusions

- **Confusion**: Thinking library calls need special handling for upgrades.
  **Clarification**: Library calls are inherently fully qualified, so they automatically use the current version.

- **Confusion**: Believing the version switch happens immediately when new code loads.
  **Clarification**: The switch happens only when the process next makes a fully qualified call.

# Source Reference

Chapter 11: Release Upgrades, section "Software Upgrades," page 337 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of p. 337.
- Confidence rationale: HIGH — the source explicitly defines fully qualified calls and their role in version switching.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
