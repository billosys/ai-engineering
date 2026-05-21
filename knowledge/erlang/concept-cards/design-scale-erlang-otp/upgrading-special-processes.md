---
# === CORE IDENTIFICATION ===
concept: Upgrading Special Processes
slug: upgrading-special-processes

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-upgrades
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Upgrading Special Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - system_code_change
  - "system_code_change/4"
  - special process upgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
  - code-change-callback
extends: []
related:
  - high-level-instructions
  - low-level-instructions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I upgrade a special process during a release upgrade?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Upgrading special processes is the upgrade of non-behavior OTP-compliant processes. It works like upgrading a behavior, but the special process's callback module implements `system_code_change/4` instead of `code_change`.

# Core Definition

Upgrading special processes is no different from upgrading behaviors (Cesarini & Vinoski, p. 351-352, pdf p. 336). For a simple code replacement, the new module is loaded through the `add_module` instruction; for a synchronized code replacement, the same `update` high-level instruction used for OTP behaviors applies. Upon receiving a message of the format `{system, From, Msg}`, the special process invokes `proc_lib:handle_system_msg/6`, which suspends the process. If the `update` command had the `{advanced, Extra}` parameter, the callback `Mod:system_code_change(LoopData, Module, Vsn, Extra)` is called in the special process callback module, returning `{ok, NewLoopData}`.

# Prerequisites

- **Release upgrade** — Upgrading special processes is a release-upgrade activity; that concept comes first.
- **Code change callback** — `system_code_change/4` is the special-process analogue of `code_change`.

# Key Properties

1. Special processes are upgraded with the same instructions as behaviors.
2. Simple code replacement -> `add_module` instruction; synchronized -> `update` instruction.
3. A `{system, From, Msg}` message makes the process call `proc_lib:handle_system_msg/6`, which suspends it.
4. `{advanced, Extra}` in the `update` command triggers `Mod:system_code_change(LoopData, Module, Vsn, Extra)`.
5. `system_code_change/4` returns `{ok, NewLoopData}`.
6. `Vsn` is the version being upgraded to, or `{downgrade, Vsn}` for a downgrade; `Vsn` is a string in both cases.
7. Special processes with `dynamic` module dependencies answer the `{get_modules, From}` system message with their current module list, informing the release handler whether to suspend them.

# Construction / Recognition

## To Upgrade a Special Process:
1. For a simple replacement, use the `add_module` instruction in the `.appup`.
2. For a synchronized replacement, use the `update` instruction (with `{advanced, Extra}` if state must change).
3. Implement `system_code_change/4` in the special process callback module.
4. For processes with `dynamic` modules, handle the `{get_modules, From}` system message.

## To Recognize It:
1. A `system_code_change/4` clause in a special process callback module.

# Context & Application

- **Typical contexts**: Upgrading hand-written OTP-compliant processes that are not standard behaviors.
- **Common applications**: Migrating special-process loop data during a release upgrade.
- **Historical/stylistic notes**: The `{get_modules, From}` mechanism exists for processes whose module dependencies are set to `dynamic` in the supervisor specification.

# Examples

**Example 1** (p. 351): The special-process upgrade callback signature — `Mod:system_code_change(LoopData, Module, Vsn, Extra)` returns `{ok, NewLoopData}`; `Module` is the callback module name and `Vsn` is the target version (or `{downgrade, Vsn}`).

**Example 2** (p. 351-352): When upgrading, processes whose supervisor child specs set module dependencies to `dynamic` reply to `{get_modules, From}` with `From ! {modules, ModuleList}`, informing the release handler whether they belong to a dependency chain.

# Relationships

## Builds Upon
- **Release upgrade** — Special-process upgrade is part of a release upgrade.
- **Code change callback** — `system_code_change/4` is the special-process equivalent.

## Related
- **High-level instructions** — `update` and `add_module` drive special-process upgrades.
- **Low-level instructions** — The generated `relup` commands suspend/resume special processes.

# Common Errors

- **Error**: Expecting a special process to use `code_change`.
  **Correction**: Special processes implement `system_code_change/4`, not the behavior `code_change`.

- **Error**: Ignoring the `{get_modules, From}` message in a special process with dynamic modules.
  **Correction**: Reply with the current module list so the release handler knows whether to suspend the process.

# Common Confusions

- **Confusion**: Thinking special processes need a different upgrade mechanism than behaviors.
  **Clarification**: They use the same `update`/`add_module` instructions; only the callback (`system_code_change/4`) differs.

- **Confusion**: Believing `Vsn` is always a plain version.
  **Clarification**: On a downgrade `Vsn` is `{downgrade, Vsn}`; in both cases the version itself is a string.

# Source Reference

Chapter 11: Release Upgrades, section "Upgrading Special Processes," pages 351-352 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 351-352.
- Confidence rationale: HIGH — the source explicitly describes special-process upgrades and `system_code_change/4`.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
