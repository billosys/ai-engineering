---
# === CORE IDENTIFICATION ===
concept: The restart_application Instruction
slug: restart-application-instruction

# === CLASSIFICATION ===
category: applications-releases
subcategory: upgrade-mechanisms
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Upgrade when Erlang/OTP has Changed"
chapter_number: null
pdf_page: null
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - restart_application
  - restart_application upgrade instruction

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
extends: []
related:
  - core-application-upgrade
  - restart-new-emulator-instruction
  - restart-emulator-instruction
  - non-upgradeable-applications
contrasts_with:
  - restart-new-emulator-instruction
  - restart-emulator-instruction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an application upgrade file (.appup)?"
  - "How do non-critical OTP applications handle upgrades?"
  - "What does restart_application do during a release upgrade?"
---

# Quick Definition

The `restart_application` instruction is an upgrade directive used in application upgrade files (appup) for non-critical applications, ensuring all modules in the application are reloaded to run new code without requiring a full emulator restart.

# Core Definition

As of Erlang/OTP 17, most applications deliver a valid application upgrade file (`appup`). Many of these applications use the `restart_application` instruction. These are applications for which it is not crucial to support real soft upgrade, for example, tools and library applications. The `restart_application` instruction ensures that all modules in the application are reloaded and thereby running the new code.

# Prerequisites

- Understanding of OTP application structure
- Basic familiarity with release handling and the `release_handler`
- Knowledge of application upgrade files (appup)

# Key Properties

1. Used by most OTP applications as of Erlang/OTP 17
2. Stops and restarts the application, reloading all modules
3. Does not require a full runtime system restart
4. Suitable for non-critical applications such as tools and library applications
5. Does not support real soft upgrade with state preservation via `code_change`

# Construction / Recognition

## To Construct/Create:
1. Create an `.appup` file for the application
2. Specify the `restart_application` instruction as the upgrade action for each version transition
3. Include the appup file in the application's `ebin` directory

## To Identify/Recognize:
1. Look for `restart_application` in an application's `.appup` file
2. Typically found in tool and library applications that do not need state-preserving upgrades
3. The application will be stopped and restarted during the upgrade process

# Context & Application

The `restart_application` instruction is the standard upgrade mechanism for the majority of OTP applications. It provides a simple and reliable way to upgrade applications that do not require preserving in-memory state across versions. This is appropriate for tools, library applications, and other non-critical components where a brief interruption during upgrade is acceptable.

# Examples

**Example 1** (typical usage): Most OTP tool and library applications ship with appup files that use `restart_application`. During a release upgrade, the release handler stops the application, loads the new module code, and restarts the application with the new version.

# Relationships

## Builds Upon
- **erlang-runtime-system** -- operates within the runtime system's module loading infrastructure

## Enables
- **core-application-upgrade** -- understanding restart_application helps explain why core applications need a different mechanism

## Related
- **non-upgradeable-applications** -- applications that cannot use even restart_application

## Contrasts With
- **restart-new-emulator-instruction** -- restart_new_emulator restarts the entire runtime system; restart_application only restarts the individual application
- **restart-emulator-instruction** -- restart_emulator is a more brutal full-system restart; restart_application is a targeted per-application restart

# Common Errors

- **Error**: Assuming restart_application preserves gen_server state across the upgrade
  **Correction**: restart_application stops and restarts the application entirely; for state-preserving upgrades, a real soft upgrade with code_change callbacks is needed

- **Error**: Using restart_application for core applications (ERTS, Kernel, STDLIB, SASL)
  **Correction**: Core applications require restart_new_emulator or restart_emulator, never restart_application

# Common Confusions

- **Confusion**: restart_application performs a soft upgrade
  **Clarification**: It does not perform a soft upgrade; it stops the application completely, reloads all modules, and restarts it. There is no code_change callback invoked.

# Source Reference

"Introduction" section, "Upgrade when Erlang/OTP has Changed" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly described in source text)
- Confidence rationale: The source provides a clear and explicit description of restart_application and its purpose
- Uncertainties: none
- Cross-reference status: verified against appup documentation references in source
