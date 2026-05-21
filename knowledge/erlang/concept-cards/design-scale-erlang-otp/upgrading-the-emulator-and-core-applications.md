---
# === CORE IDENTIFICATION ===
concept: Upgrading the Emulator and Core Applications
slug: upgrading-the-emulator-and-core-applications

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
section: "Upgrading the Emulator and Core Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - restart_new_emulator
  - emulator upgrade
  - core application upgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
extends: []
related:
  - low-level-instructions
  - erlang-runtime-system
  - release-upgrade-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I upgrade the Erlang emulator and core applications?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Upgrading the emulator and core applications means replacing `erts`, `kernel`, `stdlib`, or `sasl`. It requires a VM restart, triggered by the `restart_new_emulator` instruction, which is the first instruction executed in the `relup`.

# Core Definition

You upgrade the emulator and the core applications by providing their new versions in the new release file; the rest is taken care of when generating the `relup` (Cesarini & Vinoski, p. 354-355, pdf p. 336). Upgrading the emulator and core applications (`erts`, `kernel`, `stdlib`, and `sasl`) requires a restart of the virtual machine, usually triggered by the `restart_new_emulator` instruction. Unlike other upgrades, this is the first instruction executed in the file, starting the new emulator and new core applications together with the old versions of the remaining applications; this two-phase approach allows the remaining behaviors and special processes to call `code_change` using the new core-application versions.

# Prerequisites

- **Release upgrade** — Emulator/core upgrades are a special case of a release upgrade; that concept comes first.

# Key Properties

1. Triggered by providing new `erts`/core-application versions in the new `.rel` file.
2. Core applications are `erts`, `kernel`, `stdlib`, and `sasl`.
3. Requires a VM restart, normally via `restart_new_emulator`.
4. `restart_new_emulator` is the first instruction executed in the `relup`.
5. It is a two-phase approach: new emulator and core apps start with old versions of the rest, which are upgraded afterward.
6. `restart_emulator` (different instruction) restarts the VM with new versions of all applications, and must be last in the `relup`.
7. Include the `erts` option in `systools:make_tar/2` when upgrading the runtime so the emulator is in the tar.
8. Running different application versions across the phase boundary can cause non–backward-compatibility clashes — test thoroughly.

# Construction / Recognition

## To Upgrade the Emulator and Core Applications:
1. Provide the new `erts` and core-application versions in the new `.rel` file.
2. Include the `erts` option in the `systools:make_tar/2` call.
3. Let `systools:make_relup/3,4` generate the `relup` with `restart_new_emulator` first.
4. Optionally hand-edit the `relup` to use `restart_emulator` for an all-applications restart.

## To Recognize It:
1. A `restart_new_emulator` instruction at the start of a `relup` file.

# Context & Application

- **Typical contexts**: Release upgrades that change the Erlang runtime or core OTP applications.
- **Common applications**: Moving a deployed system to a newer OTP version.
- **Historical/stylistic notes**: Deprecated functions are kept for two major releases; spanning many releases risks calling functions removed from upgraded core applications.

# Examples

**Example 1** (p. 354): `restart_new_emulator` is the first instruction in the `relup`, starting the new emulator and core applications together with the old versions of the remaining applications, which are upgraded afterward.

**Example 2** (p. 354-355): Hand-editing the `relup` to replace `restart_new_emulator` with `restart_emulator` restarts the emulator with new versions for all applications; `restart_emulator` must be the last instruction, and anything after it is ignored.

# Relationships

## Builds Upon
- **Release upgrade** — Emulator/core upgrades are a special case of release upgrade.

## Related
- **Low-level instructions** — `restart_new_emulator` and `restart_emulator` are low-level instructions.
- **Erlang runtime system** — The emulator being upgraded.
- **Release upgrade file** — The `relup` carries the restart instructions.

# Common Errors

- **Error**: Forgetting the `erts` option in `systools:make_tar/2` when upgrading the runtime.
  **Correction**: Include the `erts` option so the new emulator is part of the upgrade tar.

- **Error**: Spanning many releases in one upgrade and calling functions removed from core applications.
  **Correction**: Replace deprecated functions promptly and upgrade in several tested steps; deprecated functions survive only two major releases.

# Common Confusions

- **Confusion**: Confusing `restart_new_emulator` with `restart_emulator`.
  **Clarification**: `restart_new_emulator` runs first and starts the new emulator with old non-core apps; `restart_emulator` runs last and restarts the VM with new versions of all applications.

- **Confusion**: Thinking core-application upgrades behave like ordinary upgrades.
  **Clarification**: They require a VM restart and use a two-phase approach, unlike ordinary application upgrades.

# Source Reference

Chapter 11: Release Upgrades, section "Upgrading the Emulator and Core Applications" (including "Non–backward-Compatible Upgrades and Downgrades"), pages 354-355 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 354-355.
- Confidence rationale: HIGH — the source explicitly describes emulator/core upgrades and the restart instructions.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
