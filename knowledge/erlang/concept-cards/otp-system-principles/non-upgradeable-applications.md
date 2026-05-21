---
# === CORE IDENTIFICATION ===
concept: Non-Upgradeable Applications
slug: non-upgradeable-applications

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
section: "Applications that Still do Not Allow Code Upgrade"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - applications that do not allow code upgrade
  - empty appup applications

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-application-instruction
  - restart-emulator-instruction
extends: []
related:
  - core-application-upgrade
  - restart-new-emulator-instruction
contrasts_with:
  - restart-application-instruction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an application upgrade file (.appup)?"
  - "What must I know before performing a release upgrade?"
  - "How do I upgrade a release that includes applications that do not support code upgrade?"
---

# Quick Definition

Non-upgradeable applications are OTP applications (such as Erl_interface) that do not support any form of code upgrade, indicated by an empty application upgrade file containing only `{Vsn,[],[]}`, and which require a handwritten relup with `restart_emulator` to be included in a release upgrade.

# Core Definition

A few applications, such as Erl_interface, do not support upgrade. This is indicated by an application upgrade file containing only `{Vsn,[],[]}`. Any attempt at creating a release upgrade file with such input fails. The only way to force an upgrade involving applications like this is to handwrite the file `relup`, preferably with only the `restart_emulator` instruction.

# Prerequisites

- Understanding of application upgrade files (appup) and their structure
- Familiarity with the `restart_emulator` instruction
- Knowledge of release upgrade file (relup) generation via `systools:make_relup`

# Key Properties

1. The appup file contains only `{Vsn,[],[]}` -- empty upgrade and downgrade instruction lists
2. `systools:make_relup` fails when such applications are included in the release
3. The only workaround is to handwrite the relup file
4. The recommended approach is to use only the `restart_emulator` instruction in the handwritten relup
5. Erl_interface is explicitly named as an example in the source documentation

# Construction / Recognition

## To Construct/Create:
1. When creating a release upgrade that includes non-upgradeable applications, do not rely on `systools:make_relup`
2. Handwrite a relup file containing only the `restart_emulator` instruction
3. Place the handwritten relup file in the appropriate release directory

## To Identify/Recognize:
1. Check the application's `.appup` file for the pattern `{Vsn,[],[]}`
2. If `systools:make_relup` fails with an error referencing a specific application, that application likely does not support upgrade
3. These are typically C-based or interface applications that do not have hot-loadable BEAM modules

# Context & Application

Non-upgradeable applications represent a practical limitation of OTP's hot code upgrade system. Not all applications consist of pure Erlang modules that can be hot-loaded. Applications that include native code, external interfaces, or other components that cannot be dynamically replaced at runtime ship with empty appup files to explicitly signal this limitation. When a release includes such applications, the standard relup generation tool will refuse to produce a relup, forcing the developer to handwrite one.

# Examples

**Example 1** (Erl_interface): The Erl_interface application ships with an appup file containing `{Vsn,[],[]}`. When a developer runs `systools:make_relup` for a release that includes Erl_interface, the tool fails. The developer must handwrite the relup file using only `restart_emulator` to force the upgrade.

**Example 2** (empty appup structure): The tuple `{Vsn,[],[]}` means: version `Vsn`, with an empty list of upgrade instructions and an empty list of downgrade instructions. This explicitly declares that no code upgrade path exists for any version transition.

# Relationships

## Builds Upon
- **restart-emulator-instruction** -- the only viable upgrade mechanism when non-upgradeable applications are present

## Enables
- Understanding of why some release upgrades cannot be automated and require manual intervention

## Related
- **core-application-upgrade** -- core applications also cannot be soft-upgraded, but they have a defined mechanism (restart_new_emulator) rather than being completely non-upgradeable
- **restart-new-emulator-instruction** -- cannot be used alone when non-upgradeable applications are present

## Contrasts With
- **restart-application-instruction** -- standard applications use restart_application for upgrade; non-upgradeable applications cannot use any application-level upgrade instruction

# Common Errors

- **Error**: Relying on `systools:make_relup` when the release includes non-upgradeable applications
  **Correction**: The tool will fail. You must handwrite the relup file with only the `restart_emulator` instruction.

- **Error**: Attempting to write custom appup instructions for non-upgradeable applications
  **Correction**: These applications cannot be upgraded at the application level. The entire runtime must be restarted.

# Common Confusions

- **Confusion**: An empty appup file means the application has no appup file at all
  **Clarification**: The appup file exists but contains `{Vsn,[],[]}`, which explicitly declares no upgrade path. A missing appup file is a different situation entirely.

- **Confusion**: Non-upgradeable means the application cannot be updated at all
  **Clarification**: The application can be updated, but only by restarting the entire runtime system (via `restart_emulator`). It cannot participate in any form of hot code upgrade.

# Source Reference

"Applications that Still do Not Allow Code Upgrade" section, "Upgrade when Erlang/OTP has Changed" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly described with specific example in source text)
- Confidence rationale: The source provides a clear description, names a specific example (Erl_interface), and prescribes the exact workaround
- Uncertainties: The source says "a few applications" but names only Erl_interface specifically
- Cross-reference status: verified against restart_emulator description in same chapter
