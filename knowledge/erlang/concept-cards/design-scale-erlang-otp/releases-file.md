---
# === CORE IDENTIFICATION ===
concept: RELEASES File
slug: releases-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-files
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Creating a Release Upgrade"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - RELEASES
  - releases/RELEASES
  - create_RELEASES

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handler
extends: []
related:
  - installing-an-upgrade
  - release-directory-structure
  - release-resource-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the RELEASES file?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

The `RELEASES` file, stored in the `releases` directory, is the release handler's persistent record of every installed release — their applications, versions, absolute paths, and state. It is required for upgrading and downgrading.

# Core Definition

The `RELEASES` file is created in the `releases` directory and is required for upgrading and downgrading releases (Cesarini & Vinoski, p. 326, 346, pdf p. 336). It contains the persistent state of the release handler: a list with an entry for every release that has been installed, where each entry has information similar to the rel file — release and `erts` versions, application names and versions — plus an absolute path to each application directory and the release's state. It is created by `release_handler:create_RELEASES/4`, and the Erlang VM must have write permission to the `releases` directory.

# Prerequisites

- **Release handler** — The `RELEASES` file is the release handler's persistent state; that concept comes first.

# Key Properties

1. Stored in the `releases` directory; required for upgrades and downgrades.
2. Holds the release handler's persistent state.
3. A list with one entry per installed release.
4. Each entry: release name, version, `erts` version, `{App, Vsn, AbsolutePath}` tuples, and state.
5. Created by `release_handler:create_RELEASES(Root, RelDir, RelFile, AppDirs)`.
6. The VM must have write permission to the `releases` directory.
7. If absent during an upgrade, a new one is created — but it contains only the upgraded release, so downgrading to the original after a failed first upgrade is impossible.
8. `which_releases/0,1` reads the `RELEASES` file; `remove_release/1` updates it.

# Construction / Recognition

## To Create the RELEASES File:
1. Bring the first release up and running.
2. Compute `RootDir = code:root_dir()`, `RelDir = RootDir ++ "/releases"`, and the `.rel` file path.
3. Call `release_handler:create_RELEASES(RootDir, RelDir, RelFile, [])`.

## To Recognize It:
1. A file named `RELEASES` in the `releases` directory.
2. It holds a list of `{release, Name, Vsn, ErtsVsn, [...], State}` tuples.

# Context & Application

- **Typical contexts**: Enabling reliable upgrades and downgrades on a target system.
- **Common applications**: Tracking installed releases; reverting to the original version after a failed upgrade.
- **Historical/stylistic notes**: Chapter 10's release example got away without a `RELEASES` file because it is only really needed when downgrading to a release after a failed upgrade.

# Examples

**Example 1** (p. 326): The first `RELEASES` file for the coffee 1.0 release:

```erlang
[{release,"coffee","1.0","7.2",
  [{kernel,"4.1.1","/Users/francescoc/ernie/lib/kernel-4.1.1"},
   {stdlib,"2.7","/Users/francescoc/ernie/lib/stdlib-2.7"},
   {sasl,"2.6.1","/Users/francescoc/ernie/lib/sasl-2.6.1"},
   {coffee,"1.0","/Users/francescoc/ernie/lib/coffee-1.0"}],
  permanent}].
```

**Example 2** (p. 326): Creating it from the running node — `release_handler:create_RELEASES(RootDir, Releases, RelFile, [])` returns `ok`.

# Relationships

## Builds Upon
- **Release handler** — The `RELEASES` file is the release handler's persistent state.

## Related
- **Installing an upgrade** — Upgrades and downgrades update the `RELEASES` file.
- **Release directory structure** — The `RELEASES` file lives in the `releases` directory.
- **Release resource file** — Each `RELEASES` entry resembles a `.rel` file plus absolute paths.

# Common Errors

- **Error**: Skipping `create_RELEASES` for the first release.
  **Correction**: Without it, a failed first upgrade leaves no way to downgrade to the original after making the upgrade permanent — you must reinstall the node.

- **Error**: Pointing `releases` at a directory the VM cannot write.
  **Correction**: The VM needs write permission to the `releases` directory to create and update the `RELEASES` file.

# Common Confusions

- **Confusion**: Thinking the `RELEASES` file is the same as a `.rel` file.
  **Clarification**: Each `RELEASES` entry resembles a `.rel` file but also includes absolute application paths and the release state, and the file lists all installed releases.

- **Confusion**: Believing a `RELEASES` file auto-created during the first upgrade is sufficient.
  **Clarification**: An auto-created file contains only the upgraded release, so it cannot support downgrading to the original.

# Source Reference

Chapter 11: Release Upgrades, sections "Creating a Release Upgrade" and "The Release Handler," pages 326 and 346 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 326 and 346.
- Confidence rationale: HIGH — the source explicitly describes the `RELEASES` file, its contents, and `create_RELEASES`.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
