---
# === CORE IDENTIFICATION ===
concept: Release Directory Structure
slug: release-directory-structure

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
section: "Directory Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "target system directory layout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - release-package
extends: []
related:
  - installing-a-release
  - release-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of an installed OTP release?"
  - "What must I know before creating a release?"
---

# Quick Definition

The release directory structure is the standardized layout under `$ROOT` where installed release code, runtime executables, and release metadata are organized by the release handler.

# Core Definition

According to the OTP Design Principles "Releases" chapter, the directory structure installed by the release handler from a release package follows a standard layout rooted at `$ROOT`. This structure contains: `lib/` with versioned application directories (each having `ebin` and `priv` subdirectories), `erts-EVsn/bin` with runtime system executables, `releases/Vsn` with the .rel file and `start.boot` (plus optionally `relup` and `sys.config`), and `bin/` with top-level runtime executables. Applications are not required to be located under `$ROOT/lib`; additional installation directories can be specified using the `variables` option in `systools:make_script/2`.

# Prerequisites

- **Release** -- Understanding releases is fundamental to understanding their installed structure.
- **Release Package** -- The directory structure results from unpacking a release package.

# Key Properties

1. Rooted at `$ROOT`, the installation root directory.
2. `$ROOT/lib/App-AVsn/` contains application directories with `ebin/` and `priv/` subdirectories.
3. `$ROOT/erts-EVsn/bin/` contains Erlang runtime system executables.
4. `$ROOT/releases/Vsn/` contains the .rel file, `start.boot`, and optionally `relup` and `sys.config`.
5. `$ROOT/bin/` contains top-level runtime system executables.
6. Multiple `$ROOT` directories can coexist, each containing different parts of the system.
7. Supports disk-less and read-only client nodes via a `clients/` directory structure.

# Construction / Recognition

## To Construct/Create:
1. Create a release package with `systools:make_tar/1,2`.
2. Unpack the release package at the target site using the release handler or manually.
3. The directory structure is created automatically during unpacking.

## To Identify/Recognize:
1. A directory containing `lib/`, `releases/`, `bin/`, and optionally `erts-EVsn/`.
2. Application directories under `lib/` follow the naming convention `AppName-Version`.
3. The `releases/` directory contains version subdirectories with boot scripts.

# Context & Application

Understanding the release directory structure is essential for system administrators managing OTP deployments and for developers creating release handling scripts. The structure supports multiple release versions coexisting, enabling smooth upgrades and rollbacks. The `$ROOT/releases/RELEASES` and `$ROOT/releases/start_erl.data` files track which versions are old, current, and permanent.

# Examples

**Example 1** (release_structure.md, "Directory Structure"): The standard directory structure:

```text
$ROOT/lib/App1-AVsn1/ebin
                    /priv
         /App2-AVsn2/ebin
                    /priv
     /erts-EVsn/bin
     /releases/Vsn
     /bin
```

**Example 2** (release_structure.md, "Directory Structure"): Disk-less client node structure:

```text
$ROOT/...
    /clients/ClientName1/bin
                        /releases/Vsn
            /ClientName2/bin
                        /releases/Vsn
```

# Relationships

## Builds Upon
- **Release Package** -- The directory structure results from unpacking a release package.

## Enables
- **Installing a Release** -- Knowing the directory layout is required for the release handler to install new versions.

## Related
- **Release Handler** -- The release handler creates and manages this directory structure.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming applications must reside under `$ROOT/lib`.
  **Correction**: Applications can be in multiple installation directories. Use the `variables` option in `systools:make_script/2` to introduce additional root directories.

# Common Confusions

- **Confusion**: Thinking there is only one release version directory under `releases/`.
  **Clarification**: Multiple version directories can exist simultaneously under `releases/`, allowing the system to switch between old, current, and permanent versions.

# Source Reference

OTP Design Principles, "Releases" chapter, section "Directory Structure" (release_structure.md).

# Verification Notes

- Definition source: Directly from the "Directory Structure" section of release_structure.md.
- Confidence rationale: Explicitly documented with directory layout diagrams.
- Uncertainties: None.
- Cross-reference status: Cross-references release, release-package, installing-a-release, release-handler (new cards).
