---
# === CORE IDENTIFICATION ===
concept: Customizing a Release Package
slug: customizing-a-release-package

# === CLASSIFICATION ===
category: applications-releases
subcategory: packaging
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.3.3. Customizing a release package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - release package customization
  - adding startup scripts to a release

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-package
extends:
  - release-package
related:
  - installing-a-release
  - erts-version
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you customize a release package?"
  - "Why add a bin directory to a release package?"
  - "How do you support installing multiple releases in one target directory?"
---

# Quick Definition

Customizing a release package means manually adding files `make_tar` did not — typically a `bin` directory with install and startup scripts — and re-creating the tarball with `erl_tar`.

# Core Definition

`systools:make_tar()` does not set up everything you may want in a release package. Customizing a release package involves manually adding artifacts — most commonly a top-level `bin` directory containing installation and startup scripts — and then re-creating the tarball with the `erl_tar` module. The install script substitutes the actual root path into the `erl.src` template; the startup script wraps the `erl` command line used to launch the system. Optionally, the release version subdirectory under `releases` can be renamed from `Version` to `ReleaseName-Version` to allow several releases to coexist in one target directory ("Erlang and OTP in Action," Ch. 10, Section 10.3.3).

# Prerequisites

- **Release package** — Customization edits the contents of a package produced by `make_tar`.

# Key Properties

1. A `bin/install` script copies `erl.src` to `erl`, replacing the `%FINAL_ROOTDIR%` string with the real install path (via `sed`).
2. A `bin/<release>` startup script wraps the `erl` invocation with `-sname`, `-boot`, `-config`, and `-detached`.
3. Scripts must be made executable (`chmod a+x ./bin/*`).
4. Renaming the version subdirectory to `ReleaseName-Version` lets multiple releases share a target directory without clashing.
5. The `.rel` file may be copied into the version subdirectory so the original survives later unpacks.
6. The customized tree is re-packaged with `erl_tar:create/3`.

# Construction / Recognition

## To Construct/Create:
1. Unpack the `make_tar` tarball into a working directory.
2. Create a `bin` directory and add an `install` script and a startup script; adjust ERTS version numbers.
3. `chmod a+x ./bin/*`.
4. Optionally rename `releases/Version` to `releases/ReleaseName-Version` and fix script paths.
5. Re-create the tarball with `erl_tar:create("Name-Vsn.tar.gz", ["erts-...", "lib", "releases", "bin"], [compressed])`.

## To Identify/Recognize:
1. A release package containing a top-level `bin` directory with install/startup scripts.

# Context & Application

- **Typical contexts**: Preparing a release for real-world installation and operation.
- **Common applications**: Adding an installer that fixes up `$ROOT`, and a daemon launcher script.
- **Historical/stylistic notes**: The fine-grained `ReleaseName-Version` layout is incompatible with `release_handler`-based installs.

# Examples

**Example 1** (Section 10.3.3): A `bin/install` script: `ROOT=\`pwd\``, `DIR=./erts-5.7.4/bin`, `sed s:%FINAL_ROOTDIR%:$ROOT: $DIR/erl.src > $DIR/erl`.

**Example 2** (Section 10.3.3): A `bin/simple_cache` startup script runs `./erts-5.7.4/bin/erl -sname cache -boot ./releases/0.1.0/start -config ./releases/0.1.0/sys -detached`.

# Relationships

## Builds Upon
- **Release package** — Customization elaborates the package `make_tar` produced.

## Enables
- **Installing a release** — Custom install/startup scripts make installation and launch convenient.

## Related
- **ERTS version** — Scripts reference the `erts-<version>` directory by name.

# Common Errors

- **Error**: Forgetting to `chmod a+x` the new scripts.
  **Correction**: Set the executable flag with `chmod a+x ./bin/*`.

- **Error**: Renaming the version directory but leaving stale paths in the startup script.
  **Correction**: Update the paths in the startup script to match the renamed version subdirectory.

# Common Confusions

- **Confusion**: Thinking the fine-grained `ReleaseName-Version` layout works with `release_handler`.
  **Clarification**: The customizations for multi-release target directories are not compatible with `release_handler`-based installation.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.3.3 "Customizing a release package."

# Verification Notes

- Definition source: Direct adaptation of Section 10.3.3.
- Confidence rationale: HIGH — the book gives concrete scripts and explicit instructions.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
