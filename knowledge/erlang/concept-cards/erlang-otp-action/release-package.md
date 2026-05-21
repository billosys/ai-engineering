---
# === CORE IDENTIFICATION ===
concept: Release Package
slug: release-package

# === CLASSIFICATION ===
category: applications-releases
subcategory: packaging
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.3. Release packaging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - release tarball
  - release package tarball

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-release
  - rel-file
  - boot-script
extends: []
related:
  - target-system
  - sys-config
  - erts-version
  - installing-a-release
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release package?"
  - "How do you create a release package?"
  - "What does a release package contain?"
---

# Quick Definition

A release package is a compressed tarball produced by `systools:make_tar/2` that bundles a release's applications, boot files, configuration, and optionally ERTS for easy installation and deployment.

# Core Definition

Once a release is defined, you package it up for easy installation, distribution, and deployment. A release package is created with `systools:make_tar/2` from the `systools` module, which produces a compressed tarball (`.tar.gz`) containing all the files in the package. The package always contains the `lib` and `releases` directories; if the `erts` option is given, it also contains a top-level `erts-<version>` directory with the runtime system executables. OTP provides this packaging functionality, but some manual tweaking is generally needed ("Erlang and OTP in Action," Ch. 10, Section 10.3).

# Prerequisites

- **Erlang release** — A package is the deployable form of a release.
- **.rel file** — Names the release passed to `make_tar`.
- **Boot script** — A non-`local` boot script must be generated before packaging.

# Key Properties

1. Created by `systools:make_tar(Release, Options)`; produces `Release.tar.gz`.
2. Always contains `lib` (the applications, by default only `ebin` and `priv` per app) and `releases` (the `.rel` file and version subdirectory).
3. With the `erts` option, also contains `erts-<version>/bin` with the runtime executables.
4. Bundling ERTS makes the package OS-dependent (executables tied to a specific OS/architecture).
5. Application directory names include version numbers, allowing multiple versions to coexist for upgrades/rollbacks.
6. The directory layout matches that of a standard Erlang/OTP installation.

# Construction / Recognition

## To Construct/Create:
1. Start `erl` with `-pa` paths to the release's applications.
2. Run `systools:make_script("Release", [])` (without `local`) to get a portable boot script.
3. Run `systools:make_tar("Release", [{erts, code:root_dir()}])` to include ERTS, or `make_tar("Release", [])` to exclude it.
4. The result is `Release.tar.gz`.

## To Identify/Recognize:
1. A `.tar.gz` whose extracted tree contains `lib`, `releases`, and optionally `erts-<version>`.

# Context & Application

- **Typical contexts**: Producing a deployable artifact for a target host.
- **Common applications**: Shipping the Simple Cache service to production machines.
- **Historical/stylistic notes**: Erlang manipulates tar files via the `erl_tar` module in `stdlib`, so a separate `tar` utility is not required.

# Examples

**Example 1** (Section 10.3.1): `systools:make_tar("simple_cache", [{erts, code:root_dir()}])` produces `simple_cache.tar.gz` with ERTS bundled from the current installation.

**Example 2** (Section 10.3.2): Unpacking the tarball yields `erts-5.7.4/`, `lib/` (with versioned application directories), and `releases/` (with `simple_cache.rel` and `0.1.0/start.boot`, `0.1.0/sys.config`).

# Relationships

## Builds Upon
- **Erlang release** — The package is the bundled form of a release.
- **Boot script** — A portable boot file is bundled into the package.

## Enables
- **Target system** — Installing a package produces a target system.
- **Installing a release** — The package is the input to installation.

## Related
- **ERTS version** — A bundled ERTS appears as `erts-<version>`.
- **sys.config** — Bundled inside `releases/<version>`.

# Common Errors

- **Error**: Packaging with a `local`-option boot script.
  **Correction**: Regenerate the boot script without `local` before calling `make_tar`.

- **Error**: Installing an ERTS-bundled package on an incompatible OS/architecture.
  **Correction**: Bundled ERTS executables are OS- and architecture-specific; build per-platform packages or ship ERTS separately.

# Common Confusions

- **Confusion**: Believing `make_tar` produces a finished, install-ready product with no manual steps.
  **Clarification**: OTP's packaging is helpful but generally needs manual tweaking, such as adding installation/startup scripts.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.3 "Release packaging" (10.3.1 "Creating a release package," 10.3.2 "Release package contents").

# Verification Notes

- Definition source: Direct adaptation of Sections 10.3, 10.3.1, 10.3.2.
- Confidence rationale: HIGH — the book explicitly describes packaging and package contents.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
