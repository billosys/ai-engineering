---
# === CORE IDENTIFICATION ===
concept: start_erl
slug: start-erl

# === CLASSIFICATION ===
category: production-ops
subcategory: startup
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Starting a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "start_erl script"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - target-system-installation
extends: []
related:
  - run-erl
  - embedded-target-system
  - system-configuration-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is start_erl and what role does it play?"
  - "How does start_erl determine which release to boot?"
---

# Quick Definition

`start_erl` is a shell script that acts as an embedded variant of `erl`, reading `start_erl.data` to determine the ERTS and release versions and booting the correct release with the appropriate boot file.

# Core Definition

As described in OTP System Principles, `start_erl` is called by `run_erl` in the embedded target system startup chain (`bin/start` calls `bin/run_erl`, which calls `bin/start_erl`). The source states: "roughly, `start_erl` is an embedded variant of `erl`." It reads version information from `start_erl.data` and boots the system with the correct release.

# Prerequisites

- An installed target system with `releases/start_erl.data` present.
- A `sys.config` file in the release version directory.

# Key Properties

1. Generated from `erts-<version>/bin/start_erl.src` during `target_system:install/2`, with `%FINAL_ROOTDIR%` and `%EMU%` substituted.
2. Requires three inputs: the root directory, the releases directory, and the location of `start_erl.data`.
3. Reads the ERTS runtime version and release version from `start_erl.data` (e.g., `"5.10.4 FIRST"`).
4. Starts the runtime system of the ERTS version found.
5. Provides the `-boot` flag pointing to `releases/<version>/start.boot`.
6. Assumes `sys.config` exists in the release version directory.
7. The `start_erl` script "is normally not to be altered by the user."

# Construction / Recognition

## To Construct/Create:
1. `target_system:install/2` automatically generates `bin/start_erl` from `erts-<version>/bin/start_erl.src`.
2. The `start_erl.data` file is created during `target_system:create/1` with the format `"<erts_version> <release_version>"`.

## To Identify/Recognize:
1. Located at `bin/start_erl` in the target system.
2. Called by `run_erl` as part of the embedded startup chain.
3. Reads `start_erl.data` to determine which release to boot.

# Context & Application

`start_erl` is a critical component of the embedded target system startup chain. Unlike `bin/start` (which is an example and should be customized), `start_erl` is not meant to be modified. It serves as the bridge between `run_erl` (which provides logging) and the actual Erlang runtime. During upgrades, the `release_handler` writes a `new_start_erl.data` file with the new version information, which `start_erl` reads on the next restart.

# Examples

**Example 1** (Starting a Target System section): The `start_erl` requirements:

```text
start_erl requires:
1. The root directory ("/usr/local/erl-target")
2. The releases directory ("/usr/local/erl-target/releases")
3. The location of the file start_erl.data
```

**Example 2** (Starting a Target System section): What `start_erl` does at runtime:

1. Reads `"5.10.4"` (ERTS version) and `"FIRST"` (release version) from `start_erl.data`.
2. Starts the runtime system of ERTS version 5.10.4.
3. Passes `-boot releases/FIRST/start.boot` to boot the release.

**Example 3** (Upgrading the Target System section): In the `bin/start` script, `start_erl` is invoked by `run_erl`:

```text
$ROOTDIR/bin/run_erl -daemon /tmp/ $ROOTDIR/log "exec $ROOTDIR/bin/start_erl $ROOTDIR\
$RELDIR $START_ERL_DATA -heart"
```

# Relationships

## Builds Upon
- **target-system-installation** — `start_erl` is generated during installation from `start_erl.src`

## Enables
- **embedded-target-system** — `start_erl` is the core of embedded target system boot
- **target-system-upgrade** — `start_erl` reads `new_start_erl.data` after an upgrade to boot the new release

## Related
- **run-erl** — `run_erl` calls `start_erl` in the startup chain
- **system-configuration-parameters** — `start_erl` assumes `sys.config` exists in the release directory

## Contrasts With
- No direct contrasts in source; implicitly contrasts with the standard `erl` script (interactive, no automatic version selection).

# Common Errors

- **Error**: Modifying the `start_erl` script.
  **Correction**: The source states `start_erl` "is normally not to be altered by the user." Customize `bin/start` instead.

- **Error**: Missing `start_erl.data` file.
  **Correction**: This file is created by `target_system:create/1`. Ensure the creation step completed successfully.

# Common Confusions

- **Confusion**: Confusing `start_erl` with the `start` script.
  **Clarification**: `bin/start` is the user-editable entry point; `bin/start_erl` is the system-level script that reads version data and boots the correct release. Edit `start`, not `start_erl`.

# Source Reference

"Starting a Target System" section, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly described with requirements, behavior, and usage guidance.
- Uncertainties: None.
- Cross-reference status: References run-erl, embedded-target-system, system-configuration-parameters, target-system-installation, target-system-upgrade.
