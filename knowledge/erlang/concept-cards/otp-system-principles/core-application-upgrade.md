---
# === CORE IDENTIFICATION ===
concept: Core Application Upgrade
slug: core-application-upgrade

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
  - core application soft upgrade
  - ERTS/Kernel/STDLIB/SASL upgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-application-instruction
  - restart-new-emulator-instruction
extends: []
related:
  - restart-emulator-instruction
  - non-upgradeable-applications
contrasts_with:
  - restart-application-instruction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes core application upgrades from other application upgrades?"
  - "What must I know before performing a release upgrade?"
  - "Why is a two-step upgrade used for core applications?"
---

# Quick Definition

Core application upgrade refers to the special upgrade procedure required for ERTS, Kernel, STDLIB, and SASL, which never allow real soft upgrade and instead require a full restart of the Erlang runtime system via `restart_new_emulator`.

# Core Definition

The core applications ERTS, Kernel, STDLIB, and SASL never allow real soft upgrade, but require the Erlang runtime system to be restarted. This is indicated to the `release_handler` by the upgrade instruction `restart_new_emulator`. The instruction is always the very first instruction executed, and it restarts the runtime system with the new versions of the core applications and the old versions of all other applications. When the node is back up, all other upgrade instructions are executed, making sure each application is finally running its new version.

# Prerequisites

- Understanding of the `restart_application` instruction and standard application upgrades
- Familiarity with the `restart_new_emulator` instruction
- Knowledge of the release handler and release upgrade files (relup)

# Key Properties

1. Applies exclusively to the four core applications: ERTS, Kernel, STDLIB, and SASL
2. Never permits real soft upgrade under any circumstances
3. Uses a two-step process: first restart the emulator with new core apps (old non-core), then upgrade the remaining applications
4. The two-step design allows `code_change` functions in non-core applications to have side effects (e.g., changing data on disk)
5. Guarantees that the upgrade mechanism for non-core applications does not differ depending on whether core applications are also changing

# Construction / Recognition

## To Construct/Create:
1. Generate a release upgrade file (relup) that includes core application version changes
2. The `restart_new_emulator` instruction will automatically be placed first
3. Other application upgrade instructions follow and execute after the runtime restarts

## To Identify/Recognize:
1. Any release upgrade that changes ERTS, Kernel, STDLIB, or SASL versions involves a core application upgrade
2. The presence of `restart_new_emulator` as the first instruction in a relup file signals a core application upgrade
3. The upgrade requires the runtime system to fully restart

# Context & Application

Core application upgrades are unavoidable when upgrading between OTP major versions, since the core applications always change. Understanding this mechanism is critical for planning production upgrades, as the runtime system restart means a brief interruption of service. The two-step design is intentional: it ensures that non-core application upgrades proceed identically regardless of whether core applications have also changed, and it permits `code_change` callbacks in non-core applications to execute their side effects reliably in the new runtime environment.

# Examples

**Example 1** (two-step upgrade): When upgrading from OTP 25 to OTP 26, the relup file contains `restart_new_emulator` as its first instruction. The runtime system restarts with the new ERTS, Kernel, STDLIB, and SASL but retains old versions of all user applications. After the node boots, the release handler executes the remaining instructions (e.g., `restart_application` for each non-core application) to complete the upgrade.

**Example 2** (design rationale): The two-step approach exists because non-core applications may have `code_change` functions with side effects such as disk data migration. If the runtime restarted with all new code at once, these side effects could not be managed in a controlled, sequential manner.

# Relationships

## Builds Upon
- **restart-new-emulator-instruction** -- core application upgrades are the primary use case for this instruction
- **restart-application-instruction** -- non-core applications within a core upgrade still use standard upgrade instructions

## Enables
- Understanding of why **restart-emulator-instruction** exists as an alternative when the two-step process is not needed

## Related
- **non-upgradeable-applications** -- some applications cannot participate in any upgrade and require special handling even during core upgrades

## Contrasts With
- **restart-application-instruction** -- standard application upgrades do not require a runtime restart; core upgrades always do

# Common Errors

- **Error**: Attempting to soft-upgrade ERTS, Kernel, STDLIB, or SASL without restarting the runtime system
  **Correction**: These core applications never support soft upgrade. The runtime system must always be restarted when their versions change.

- **Error**: Assuming non-core applications are also upgraded during the initial restart
  **Correction**: The first restart loads only the new core applications. Non-core applications remain at their old versions until subsequent upgrade instructions execute.

# Common Confusions

- **Confusion**: Why not restart the runtime with all new applications at once?
  **Clarification**: The two-step process exists to allow `code_change` functions in non-core applications to execute with side effects, and to ensure the upgrade mechanism for non-core applications is consistent regardless of whether core applications change.

# Source Reference

"Upgrade of Core Applications" section, "Upgrade when Erlang/OTP has Changed" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly described with rationale in source text)
- Confidence rationale: The source provides detailed explanation of the mechanism and its design rationale
- Uncertainties: none
- Cross-reference status: verified against restart_new_emulator and restart_emulator descriptions in same source
