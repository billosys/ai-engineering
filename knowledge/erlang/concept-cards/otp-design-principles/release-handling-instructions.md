---
# === CORE IDENTIFICATION ===
concept: Release Handling Instructions
slug: release-handling-instructions

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Release Handling"
chapter_number: null
pdf_page: null
section: "Release Handling Instructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "appup instructions"
  - "relup instructions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - application-upgrade-file
extends: []
related:
  - simple-code-replacement
  - synchronized-code-replacement
  - release-upgrade-file
  - functional-module
  - residence-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What instructions are available for release handling?"
  - "How do I write an .appup file?"
---

# Quick Definition

Release handling instructions are the commands used in .appup and relup files to control how modules are loaded, processes are updated, applications are managed, and the runtime system is restarted during upgrades and downgrades.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "OTP supports a set of _release handling instructions_ that are used when creating `.appup` files. The release handler understands a subset of these, the _low-level_ instructions. To make it easier for the user, there are also a number of _high-level_ instructions, which are translated to low-level instructions by `systools:make_relup`." Key instructions include: `load_module` (simple code replacement), `update` (synchronized code replacement), `add_module`/`delete_module` (module lifecycle), `add_application`/`remove_application`/`restart_application` (application lifecycle), `apply` (arbitrary function call), `restart_new_emulator` (runtime upgrade), and `restart_emulator` (forced reboot).

# Prerequisites

- **Release Handling** -- Instructions are used within the release handling framework.
- **Application Upgrade File** -- Instructions are written in .appup files.

# Key Properties

1. Two categories: high-level (user-facing, translated by systools) and low-level (understood directly by the release handler).
2. `load_module` -- loads a new module version (simple code replacement for functional modules).
3. `update` with `{advanced, Extra}` -- synchronized code replacement triggering `code_change/3`.
4. `update` with `supervisor` -- updates supervisor internal state from new `init/1` return value.
5. `add_module`/`delete_module` -- loads/unloads modules (required in embedded mode).
6. `add_application`/`remove_application`/`restart_application` -- manages entire applications.
7. `apply` -- calls an arbitrary function `{M, F, A}` during upgrade.
8. `restart_new_emulator` -- must be first instruction in relup; used when upgrading ERTS or core applications.
9. `restart_emulator` -- must be last instruction in relup; forces a system reboot after all other instructions.

# Construction / Recognition

## To Construct/Create:
1. Analyze what changed between versions.
2. For each changed functional module, use `load_module`.
3. For changed residence modules or state changes, use `update` with `{advanced, Extra}`.
4. For supervisor changes, use `update` with `supervisor`.
5. For new/removed modules, use `add_module`/`delete_module`.
6. For new/removed applications, use `add_application`/`remove_application`.
7. When all else fails, use `restart_application`.

## To Identify/Recognize:
1. Tuples within the instruction lists of .appup or relup files.
2. Instruction atoms: `load_module`, `update`, `add_module`, `delete_module`, `add_application`, `remove_application`, `restart_application`, `apply`, `restart_new_emulator`, `restart_emulator`.

# Context & Application

Choosing the right instructions is the core skill in writing .appup files. The choice depends on the nature of the change (functional module vs. residence module, state transformation required, supervisor restructuring, etc.) and must account for module dependencies and instruction ordering. The release handler finds affected processes by traversing supervision trees and checking child specification `Modules` fields.

# Examples

**Example 1** (release_handling.md, "Release Handling Instructions"): Module-level instructions:

```erlang
{load_module, Module}             %% Simple code replacement
{update, Module, {advanced, Extra}} %% Synchronized with state change
{update, Module, supervisor}      %% Supervisor update
{add_module, Module}              %% Load new module
{delete_module, Module}           %% Unload module
```

**Example 2** (release_handling.md, "Release Handling Instructions"): Application-level instructions:

```text
{add_application, Application}
{remove_application, Application}
{restart_application, Application}
```

**Example 3** (release_handling.md, "Release Handling Instructions"): The release handler finds processes using a module by checking child specifications:

```erlang
{Id, StartFunc, Restart, Shutdown, Type, Modules}
```

A process uses a module if the name is listed in `Modules`. For event managers (`Modules=dynamic`), the event manager reports currently installed handlers.

# Relationships

## Builds Upon
- **Release Handling** -- Instructions are the building blocks of the release handling process.
- **Application Upgrade File** -- Instructions are written in .appup files.

## Enables
- **Simple Code Replacement** -- The `load_module` instruction.
- **Synchronized Code Replacement** -- The `update` instruction.

## Related
- **Functional Module** -- Determines use of `load_module`.
- **Residence Module** -- Determines use of `update`.
- **Release Upgrade File** -- Contains the final ordered list of low-level instructions.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `delete_module` while processes still use the module as a residence module.
  **Correction**: Any process with `Module` as residence module is killed by `delete_module`. Ensure all such processes are terminated first.

- **Error**: Placing `restart_new_emulator` anywhere other than the first instruction.
  **Correction**: `restart_new_emulator` must always be the first instruction in a relup. `systools:make_relup` enforces this automatically.

# Common Confusions

- **Confusion**: Thinking `restart_new_emulator` and `restart_emulator` are interchangeable.
  **Clarification**: `restart_new_emulator` is specifically for upgrading ERTS or core applications (Kernel, STDLIB, SASL) and must be first in the relup. `restart_emulator` is for any other reason requiring a reboot and must be last. They serve different purposes and have different placement requirements.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Release Handling Instructions" (release_handling.md).

# Verification Notes

- Definition source: Directly from release_handling.md "Release Handling Instructions" section.
- Confidence rationale: Explicitly documented with all instructions listed and described.
- Uncertainties: None.
- Cross-reference status: Cross-references release-handling, application-upgrade-file, functional-module, residence-module, release-upgrade-file (new cards).
