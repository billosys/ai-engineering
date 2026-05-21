---
# === CORE IDENTIFICATION ===
concept: Target System Installation
slug: target-system-installation

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Installing a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "target_system:install/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - target-system-creation
extends: []
related:
  - basic-target-system
  - simple-target-system
  - embedded-target-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install a target system?"
  - "What does target_system:install/2 do?"
---

# Quick Definition

Target system installation is the process of extracting the target system tar archive into a destination directory and performing location-dependent configuration using `target_system:install/2`.

# Core Definition

As described in OTP System Principles, `target_system:install/2` takes the tar archive produced by `target_system:create/1` and a target directory path, then extracts the archive, substitutes location-dependent variables in source scripts to produce the final executables (`erl`, `start`, `start_erl`), and creates the `releases/RELEASES` file.

# Prerequisites

- A target system tar archive produced by `target_system:create/1`.
- A suitable target directory on the destination system.

# Key Properties

1. Extracts the tar archive into the target directory.
2. Reads `releases/start_erl.data` to determine the ERTS version.
3. Substitutes `%FINAL_ROOTDIR%` and `%EMU%` in `erl.src`, `start.src`, and `start_erl.src` with the actual root directory and `beam` respectively.
4. Places the resulting `erl`, `start`, and `start_erl` scripts in the target `bin/` directory.
5. Creates the `releases/RELEASES` file from `releases/<relname>.rel`.
6. The `RELEASES` file is what enables `release_handler` to manage code replacement (the difference between basic and simple target systems).

# Construction / Recognition

## To Construct/Create:
1. Have the `.tar.gz` file from `target_system:create/1` available.
2. Call `target_system:install("mysystem", "/usr/local/erl-target")`.
3. The target directory is now a complete, runnable target system.

## To Identify/Recognize:
1. A directory containing `bin/erl`, `bin/start`, `bin/start_erl` (generated from `.src` templates).
2. The file `releases/RELEASES` exists.
3. The `%FINAL_ROOTDIR%` placeholders have been replaced with actual paths.

# Context & Application

Installation is performed on the target machine (or into a directory that will be deployed to the target). The key insight is that `target_system:create/1` produces a location-independent archive, while `target_system:install/2` performs the location-dependent configuration. This separation allows the same archive to be installed in different directories on different machines. The `install/2` procedure differs from the standard OTP `Install` shell script in that `create/1` makes the package as complete as possible, leaving only location-dependent work for `install/2`.

# Examples

**Example 1** (Installing a Target System section): Installing to a target directory:

```text
2> target_system:install("mysystem", "/usr/local/erl-target").
```

This extracts `mysystem.tar.gz` into `/usr/local/erl-target`, substitutes path variables in the script templates, and creates the `RELEASES` file.

# Relationships

## Builds Upon
- **target-system-creation** — installation uses the tar archive produced by creation

## Enables
- **basic-target-system** — after installation, the system can be started via `bin/erl`
- **simple-target-system** — the `RELEASES` file created during installation enables code replacement
- **embedded-target-system** — the `bin/start` and `bin/start_erl` scripts enable embedded startup

## Related
- **target-system** — installation is the second step in deploying a target system

## Contrasts With
- No direct contrasts in source; implicitly contrasts with the standard OTP `Install` shell script approach.

# Common Errors

- **Error**: Installing to a directory without write permissions.
  **Correction**: Ensure the target directory is writable by the user running the installation.

- **Error**: Confusing `target_system:install/2` with `release_handler:install_release/1`.
  **Correction**: `target_system:install/2` is for initial installation of a target system; `release_handler:install_release/1` is for upgrading a running system to a new release version.

# Common Confusions

- **Confusion**: Thinking installation is the same as the standard OTP `Install` script.
  **Clarification**: The source notes that the `install/2` procedure "differs somewhat from that of the ordinary `Install` shell script." The `create/1` function makes the package as complete as possible, and `install/2` only handles location-dependent files.

# Source Reference

"Installing a Target System" and "Differences From the Install Script" sections, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly described step-by-step.
- Uncertainties: None.
- Cross-reference status: References target-system, target-system-creation, basic-target-system, simple-target-system, embedded-target-system.
