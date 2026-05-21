---
# === CORE IDENTIFICATION ===
concept: Application Upgrade File
slug: application-upgrade-file

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
section: "Application Upgrade File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".appup file"
  - "appup file"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - application
  - release-handling-instructions
extends: []
related:
  - release-upgrade-file
  - release-resource-file
  - simple-code-replacement
  - synchronized-code-replacement
  - module-dependencies
contrasts_with:
  - release-upgrade-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do .appup files relate to .relup files?"
  - "How do I write an .appup file?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

An application upgrade file (.appup) defines how to upgrade and downgrade between the current and previous versions of an application using release handling instructions.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "To define how to upgrade/downgrade between the current version and previous versions of an application, an _application upgrade file_, or in short `.appup` file is created." The file has the format `{Vsn, [{UpFromVsn1, InstructionsU1}, ...], [{DownToVsn1, InstructionsD1}, ...]}` where `Vsn` is the current version, each `UpFromVsn` is a previous version to upgrade from, each `DownToVsn` is a version to downgrade to, and each `Instructions` is a list of release handling instructions. The file must be named `Application.appup` and placed in the application's `ebin` directory. Version strings can also be specified as regular expressions.

# Prerequisites

- **Release Handling** -- The .appup file is part of the release handling framework.
- **Application** -- Each .appup file corresponds to a specific application.
- **Release Handling Instructions** -- The instructions used within the .appup file.

# Key Properties

1. Named `Application.appup` (e.g., `ch_app.appup`).
2. Placed in the application's `ebin` directory.
3. Current version `Vsn` must match the version in the `.app` file.
4. Contains two lists: one for upgrade instructions (from older versions) and one for downgrade instructions (to older versions).
5. Each version entry maps a source/target version to a list of instructions.
6. Version strings can be regular expressions for matching multiple versions.
7. Serves as input to `systools:make_relup/3,4` which generates the relup file.

# Construction / Recognition

## To Construct/Create:
1. Identify what changed between application versions.
2. Determine the appropriate instructions for each changed module (load_module, update, add_module, delete_module, etc.).
3. Consider module dependencies when ordering instructions.
4. Write upgrade instructions for each previous version.
5. Write corresponding downgrade instructions.
6. Save as `Application.appup` in the `ebin` directory.

## To Identify/Recognize:
1. A file named `Application.appup` in an `ebin` directory.
2. A 3-tuple containing a version string, an upgrade instruction list, and a downgrade instruction list.

# Context & Application

The .appup file is a per-application specification that describes how to transition between application versions. It is a critical input for generating the system-wide relup file. Writing correct .appup files requires understanding whether modules are functional or residence modules, whether internal state needs transformation, and what module dependencies exist. The Appup Cookbook provides examples for typical upgrade/downgrade scenarios.

# Examples

**Example 1** (release_handling.md, "Application Upgrade File"): A simple .appup file for upgrading `ch_app` from version "1" to "2" where only the callback module `ch3` changed (a functional module with a new function):

```erlang
{"2",
 [{"1", [{load_module, ch3}]}],
 [{"1", [{load_module, ch3}]}]
}.
```

**Example 2** (appup_cookbook.md, "Changing Internal State"): An .appup file requiring synchronized code replacement with state transformation:

```erlang
{"2",
 [{"1", [{update, ch3, {advanced, []}}]}],
 [{"1", [{update, ch3, {advanced, []}}]}]
}.
```

# Relationships

## Builds Upon
- **Release Handling** -- The .appup file is part of the release handling workflow (Step 5).
- **Release Handling Instructions** -- The .appup file contains release handling instructions.

## Enables
- **Release Upgrade File** -- .appup files are the primary input for generating the relup file.

## Related
- **Simple Code Replacement** -- The `load_module` instruction in .appup files.
- **Synchronized Code Replacement** -- The `update` instruction in .appup files.
- **Module Dependencies** -- Dependency ordering must be reflected in .appup instructions.

## Contrasts With
- **Release Upgrade File** -- The .appup file is per-application; the relup file is per-release. The .appup uses high-level instructions; the relup uses low-level instructions.

# Common Errors

- **Error**: Version string in .appup not matching the .app file version.
  **Correction**: The `Vsn` in the .appup file must exactly match the `vsn` in the corresponding .app file.

- **Error**: Incorrect instruction ordering when module dependencies exist.
  **Correction**: When module `m1` depends on `ch3`, use `{load_module, m1, [ch3]}` to ensure `ch3` is loaded first during upgrade.

# Common Confusions

- **Confusion**: Thinking an .appup file is needed when adding or removing an application entirely.
  **Clarification**: When adding or removing an application, no .appup file is needed. The `systools:make_relup` function compares .rel files and automatically adds `add_application` and `remove_application` instructions.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Application Upgrade File" (release_handling.md). Also referenced in "Appup Cookbook" chapter (appup_cookbook.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "Application Upgrade File" section.
- Confidence rationale: Explicitly defined with syntax specification and multiple examples.
- Uncertainties: None.
- Cross-reference status: Cross-references release-handling, application (existing card), release-upgrade-file, module-dependencies (new cards).
