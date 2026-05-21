---
# === CORE IDENTIFICATION ===
concept: Installing a Release
slug: installing-a-release

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
section: "Installing a Release"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "release installation"
  - "release upgrade procedure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - release-handler
  - release-package
  - release-upgrade-file
extends: []
related:
  - release-directory-structure
  - boot-script
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform a release upgrade?"
  - "What is the procedure for installing a new release version?"
---

# Quick Definition

Installing a release is the multi-step procedure of unpacking a release package, evaluating the relup instructions to activate the new version, and making it permanent so it persists across reboots.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter, installing a release follows a defined lifecycle. First, the release package is _unpacked_ (`release_handler:unpack_release/1`), extracting files to `$ROOT/lib` and `$ROOT/releases/Vsn`. Then it is _installed_ (`release_handler:install_release/1`), during which the release handler evaluates relup instructions step by step. If installation fails, the system reboots using the old version; if it succeeds, the new version is active but not yet default. The release must be made _permanent_ (`release_handler:make_permanent/1`) to become the default after reboots. An installed but not permanent release can be _removed_ (`release_handler:remove_release/1`).

# Prerequisites

- **Release Handling** -- Installation is part of the release handling workflow.
- **Release Handler** -- The release handler process performs the installation.
- **Release Package** -- A release package must be available to unpack.
- **Release Upgrade File** -- The relup file contains the instructions evaluated during installation.

# Key Properties

1. Release lifecycle states: unpacked -> installed -> permanent (or removed).
2. `unpack_release(ReleaseName)` extracts files; new application directories go under `$ROOT/lib`, unchanged applications are not affected.
3. `install_release(Vsn)` evaluates relup instructions step by step; returns `{ok, FromVsn, []}` on success.
4. On installation failure, the system reboots using the old version automatically.
5. `make_permanent(Vsn)` makes the installed version the default for reboots; the previous version becomes "old."
6. `remove_release(Vsn)` deletes an installed-but-not-permanent release.
7. Application specifications are automatically updated during installation.
8. The `config_change/3` callback is invoked for running applications whose configuration changed.

# Construction / Recognition

## To Construct/Create:
1. Copy the release package to `$ROOT/releases`.
2. Unpack: `release_handler:unpack_release("ch_rel-2").` -> `{ok,"B"}`
3. Install: `release_handler:install_release("B").` -> `{ok,"A",[]}`
4. Verify the new version works correctly.
5. Make permanent: `release_handler:make_permanent("B").` -> `ok`

## To Identify/Recognize:
1. Use `release_handler:which_releases/0` to see the status of all releases.
2. Check `$ROOT/releases/RELEASES` and `$ROOT/releases/start_erl.data`.

# Context & Application

The installation procedure is the operational core of release handling. The explicit permanence step provides a safety net: if the new version has problems, a reboot automatically restores the previous version. This makes the upgrade process inherently safer than a simple code swap. The procedure is the same for upgrades and downgrades (to downgrade, install an older version).

# Examples

**Example 1** (release_handling.md, "Installing a Release"): Complete step-by-step upgrade of `ch_rel` from version "A" to version "B":

```erlang
%% Step 5: Unpack
1> release_handler:unpack_release("ch_rel-2").
{ok,"B"}

%% Step 6: Verify old code still running
2> ch3:available().
** exception error: undefined function ch3:available/0

%% Step 7: Install (evaluates relup, loads new ch3 module)
3> release_handler:install_release("B").
{ok,"A",[]}
4> ch3:available().
3
5> code:which(ch3).
".../lib/ch_app-2/ebin/ch3.beam"

%% Step 8: Make permanent
7> release_handler:make_permanent("B").
ok
```

Note that after installation, unchanged modules (e.g., `ch_sup`) still evaluate code from the old version (`ch_app-1`).

# Relationships

## Builds Upon
- **Release Handler** -- Performs the actual installation.
- **Release Upgrade File** -- Instructions evaluated during installation.
- **Release Package** -- The artifact being installed.

## Enables
- None directly.

## Related
- **Release Directory Structure** -- Installation creates new directories under `$ROOT/lib` and `$ROOT/releases`.
- **Boot Script** -- After permanence, the system boots with the new version's boot script.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Rebooting after installation but before making the release permanent.
  **Correction**: The system will revert to the previous permanent version. Always make the new version permanent after verifying it works: `release_handler:make_permanent(Vsn)`.

- **Error**: Not including `sys.config` in the release package.
  **Correction**: Even an empty `sys.config` (containing `[].`) must be present for release handling to work properly.

# Common Confusions

- **Confusion**: Thinking downgrading is a different procedure from upgrading.
  **Clarification**: To downgrade, simply call `release_handler:install_release(OldVsn)`. The relup file contains both upgrade and downgrade instructions.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Installing a Release" and the detailed example that follows (release_handling.md).

# Verification Notes

- Definition source: Directly from release_handling.md "Installing a Release" section and its step-by-step example.
- Confidence rationale: Explicitly documented with complete operational example.
- Uncertainties: None.
- Cross-reference status: Cross-references release-handling, release-handler, release-package, release-upgrade-file, boot-script, release-directory-structure (new cards).
