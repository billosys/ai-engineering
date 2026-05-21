---
# === CORE IDENTIFICATION ===
concept: Release Package
slug: release-package

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Releases"
chapter_number: null
pdf_page: null
section: "Creating a Release Package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "release tar"
  - "release tarball"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - release-resource-file
  - boot-script
extends: []
related:
  - release-directory-structure
  - release-handling
  - installing-a-release
  - release-upgrade-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a release?"
  - "What is a release package?"
---

# Quick Definition

A release package is a compressed tar file created by `systools:make_tar/1,2` that contains the code for all applications in a release, along with boot scripts and metadata needed to install the system at a target site.

# Core Definition

According to the OTP Design Principles "Releases" chapter: "The `systools:make_tar/1,2` function takes a `.rel` file as input and creates a zipped tar file with the code for the specified applications, a _release package_." The release package by default contains the .app files, the .rel file, object code for all applications structured according to the application directory structure, and the binary boot script renamed to `start.boot`. If a `relup` file, `sys.config`, or `sys.config.src` is found, these are also automatically included.

# Prerequisites

- **Release** -- The release concept must be understood.
- **Release Resource File** -- The .rel file is the primary input to `systools:make_tar`.
- **Boot Script** -- A boot script must be generated before creating the package (without the `local` option).

# Key Properties

1. Created by `systools:make_tar/1,2` from a .rel file.
2. Is a zipped tar file (.tar.gz).
3. Contains by default: .app files, the .rel file, all application object code, and `start.boot`.
4. Application directories are placed under `lib/` with versioned names (e.g., `lib/ch_app-1/ebin/`).
5. The .rel file is duplicated: once in `releases/` and once in `releases/Vsn/`.
6. Automatically includes `relup` and `sys.config` if present.
7. Options can include source code and ERTS binary.
8. Must not contain hard-coded absolute paths (no `local` option).

# Construction / Recognition

## To Construct/Create:
1. Generate a boot script without the `local` option: `systools:make_script("RelName").`
2. Create the release package: `systools:make_tar("RelName").`
3. Optionally ensure `relup`, `sys.config`, or `sys.config.src` files are available for automatic inclusion.

## To Identify/Recognize:
1. A `.tar.gz` file named after the release.
2. Contains a `lib/` directory with versioned application directories.
3. Contains a `releases/` directory with the .rel file, `start.boot`, and optionally `relup` and `sys.config`.

# Context & Application

Release packages are the standard deployment artifact for OTP systems. They are transferred to target environments and unpacked using the release handler. The first installation of a target system uses a release package, and subsequent upgrades also use release packages that include relup files describing how to upgrade from previous versions.

# Examples

**Example 1** (release_structure.md, "Creating a Release Package"): Creating a release package for `ch_rel-1`:

```erlang
1> systools:make_script("ch_rel-1").
ok
2> systools:make_tar("ch_rel-1").
ok
```

Contents of the resulting tar file:

```text
% tar tf ch_rel-1.tar
lib/kernel-9.2.4/ebin/kernel.app
lib/kernel-9.2.4/ebin/application.beam
...
lib/ch_app-1/ebin/ch_app.app
lib/ch_app-1/ebin/ch_app.beam
lib/ch_app-1/ebin/ch_sup.beam
lib/ch_app-1/ebin/ch3.beam
releases/ch_rel-1.rel
releases/A/ch_rel-1.rel
releases/A/start.boot
```

# Relationships

## Builds Upon
- **Release Resource File** -- The .rel file serves as input.
- **Boot Script** -- The boot script is included as `start.boot`.

## Enables
- **Installing a Release** -- The release package is what gets unpacked and installed on a target system.
- **Release Handling** -- Subsequent release packages enable upgrades and downgrades.

## Related
- **Release Directory Structure** -- The installed package follows the standard directory layout.
- **Release Upgrade File** -- The relup file, when present, is included in the package.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Creating a release package with a boot script generated using the `local` option.
  **Correction**: Always regenerate the boot script without `local` before calling `systools:make_tar`, as the installed location is unknown at packaging time.

- **Error**: Forgetting to include `sys.config` when creating release packages for systems that use release handling.
  **Correction**: A `sys.config` file (even if it contains just the empty list `[].`) must be present for release handling to work properly.

# Common Confusions

- **Confusion**: Wondering why the .rel file appears twice in the tar.
  **Clarification**: The .rel file is duplicated for compatibility: it appears in both `releases/` (for release_handler extraction) and `releases/Vsn/` (for unpacking without the release handler).

# Source Reference

OTP Design Principles, "Releases" chapter, section "Creating a Release Package" (release_structure.md).

# Verification Notes

- Definition source: Directly quoted from release_structure.md "Creating a Release Package" section.
- Confidence rationale: Explicitly defined with exact tar contents listed.
- Uncertainties: None.
- Cross-reference status: Cross-references release, release-resource-file, boot-script, installing-a-release, release-upgrade-file (new cards).
