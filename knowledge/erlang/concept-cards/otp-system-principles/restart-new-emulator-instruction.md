---
# === CORE IDENTIFICATION ===
concept: The restart_new_emulator Instruction
slug: restart-new-emulator-instruction

# === CLASSIFICATION ===
category: applications-releases
subcategory: upgrade-mechanisms
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Upgrade when Erlang/OTP has Changed"
chapter_number: null
pdf_page: null
section: "Upgrade of Core Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - restart_new_emulator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-application-instruction
extends: []
related:
  - core-application-upgrade
  - non-upgradeable-applications
contrasts_with:
  - restart-emulator-instruction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does restart_new_emulator differ from restart_emulator?"
  - "What is a release upgrade file (relup)?"
  - "What must I know before performing a release upgrade?"
---

# Quick Definition

The `restart_new_emulator` instruction is a release upgrade directive that restarts the Erlang runtime system with new versions of core applications (ERTS, Kernel, STDLIB, SASL) while keeping old versions of all other applications, enabling a controlled two-step upgrade.

# Core Definition

The `restart_new_emulator` upgrade instruction is always the very first instruction executed in a release upgrade involving core applications. It restarts the runtime system with the new versions of the core applications (ERTS, Kernel, STDLIB, SASL) and the old versions of all other applications. When the node is back up, all other upgrade instructions are executed, making sure each application is finally running its new version.

# Prerequisites

- Understanding of the `restart_application` instruction and standard appup files
- Familiarity with release upgrade files (relup) and the `release_handler`
- Knowledge of which applications constitute the OTP core (ERTS, Kernel, STDLIB, SASL)

# Key Properties

1. Always placed as the very first instruction in a release upgrade file
2. Restarts the entire Erlang runtime system (emulator)
3. Loads new versions of core applications only (ERTS, Kernel, STDLIB, SASL)
4. Retains old versions of all non-core applications after the restart
5. Remaining upgrade instructions execute after the node comes back up
6. Enables a two-step upgrade that preserves the standard upgrade path for non-core applications

# Construction / Recognition

## To Construct/Create:
1. Use `systools:make_relup/3,4` to generate a relup file; `restart_new_emulator` is automatically included when core application versions change
2. Alternatively, handwrite a relup file with `restart_new_emulator` as the first instruction

## To Identify/Recognize:
1. Look for `restart_new_emulator` as the first instruction in a `.relup` file
2. Present whenever a release upgrade involves changes to ERTS, Kernel, STDLIB, or SASL
3. Followed by additional instructions (e.g., `restart_application`) for non-core applications

# Context & Application

This instruction is the standard mechanism for upgrading between OTP releases. It solves the problem of needing to restart the runtime system for core changes while still allowing non-core applications to go through their normal upgrade procedures (including `code_change` callbacks with potential side effects). The two-step design ensures consistency: non-core application upgrades behave identically whether or not core applications are changing simultaneously.

# Examples

**Example 1** (relup structure): A typical relup file for an OTP version upgrade contains `restart_new_emulator` as its first instruction. After the runtime restarts with new ERTS, Kernel, STDLIB, and SASL, subsequent instructions like `restart_application` for user applications execute to complete the upgrade.

**Example 2** (design justification): The source explains: "It might seem strange to do a two-step upgrade instead of just restarting the runtime system with the new version of all applications. The reason for this design decision is to allow code_change functions to have side effects, for example, changing data on disk."

# Relationships

## Builds Upon
- **restart-application-instruction** -- understanding per-application restarts is prerequisite to understanding why the two-step approach is needed

## Enables
- **core-application-upgrade** -- this instruction is the mechanism that makes core application upgrades possible

## Related
- **non-upgradeable-applications** -- applications that cannot participate in any upgrade may still be present during a restart_new_emulator upgrade

## Contrasts With
- **restart-emulator-instruction** -- restart_emulator restarts with ALL new application versions at once; restart_new_emulator restarts with only new core applications, deferring non-core upgrades to subsequent instructions

# Common Errors

- **Error**: Placing other upgrade instructions before `restart_new_emulator` in the relup file
  **Correction**: `restart_new_emulator` must always be the very first instruction. Instructions placed before it would execute in the old runtime, which is not supported.

- **Error**: Expecting non-core applications to be upgraded during the restart
  **Correction**: Non-core applications remain at their old versions after restart_new_emulator. They are upgraded by subsequent instructions after the node is back up.

# Common Confusions

- **Confusion**: `restart_new_emulator` and `restart_emulator` do the same thing
  **Clarification**: They are fundamentally different. `restart_new_emulator` does a partial upgrade (core apps only, then upgrades non-core apps via subsequent instructions). `restart_emulator` does a full upgrade of all applications in a single restart with no subsequent instructions executed.

# Source Reference

"Upgrade of Core Applications" section, "Upgrade when Erlang/OTP has Changed" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly described in source text)
- Confidence rationale: The source provides a thorough and clear description of the instruction, its placement, and its behavior
- Uncertainties: none
- Cross-reference status: verified against restart_emulator contrast in the same section
