---
# === CORE IDENTIFICATION ===
concept: Installing a Release
slug: installing-a-release

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.4. Installing a release"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - release installation
  - deploying a release

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-package
  - target-system
extends: []
related:
  - customizing-a-release-package
  - erts-version
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you install a release on a host machine?"
  - "What is the release_handler module?"
  - "Why does bundling ERTS make installation simpler?"
---

# Quick Definition

Installing a release means unpacking its package on a host machine and adjusting the root path so the bundled runtime and applications can start as a target system.

# Core Definition

OTP provides functionality for unpacking, installing, and upgrading releases through the `release_handler` module in SASL, but this is a fairly complex topic and is not commonly used — it cannot handle installing multiple releases in the same target directory. The book instead describes a simpler, more robust approach: because ERTS is included in the package, the tarball can be unpacked in any directory on a compatible host (using `tar` or `erl_tar:extract/2`) without Erlang/OTP installed separately. After unpacking, the `bin/install` script is run to adjust the root path, then `bin/<release>` starts the system ("Erlang and OTP in Action," Ch. 10, Section 10.4).

# Prerequisites

- **Release package** — Installation consumes a packaged release.
- **Target system** — Installation produces a running target system.

# Key Properties

1. `release_handler` (in SASL) is the OTP module for unpacking, installing, and upgrading releases.
2. `release_handler` cannot install multiple releases in the same target directory and is not commonly used.
3. The simple approach: unpack the tarball into a directory, run the install script, run the startup script.
4. A package with bundled ERTS needs no separate Erlang/OTP installation on the host.
5. A package can be unpacked into an empty directory or over a previously installed target system (a release upgrade).
6. Unpacking can be done with the OS `tar` utility or with `erl_tar:extract/2`.

# Construction / Recognition

## To Construct/Create:
1. Create a target directory: `mkdir target`.
2. Unpack the package: `erl_tar:extract("Release.tar.gz", [{cwd, "target"}, compressed])` or `tar -xzf`.
3. `cd` into the target directory and run `./bin/install` to adjust the root path.
4. Run `./bin/<release>` to start the system (ensure required contact nodes are running first).

## To Identify/Recognize:
1. A directory whose tree was extracted from a release package and whose `erl.src` has been instantiated into `erl`.

# Context & Application

- **Typical contexts**: Deploying an Erlang service onto production hosts.
- **Common applications**: Installing the Simple Cache release; installing it on top of a standard Erlang installation.
- **Historical/stylistic notes**: A minimal target system cannot run Appmon; the WebTool version of Appmon can be started from a contact node to inspect it via a browser.

# Examples

**Example 1** (Section 10.4): `erl_tar:extract("simple_cache-0.3.0.tar.gz", [{cwd, "target"}, compressed])` unpacks the package.

**Example 2** (Section 10.4): `cd target; ./bin/install; ./bin/simple_cache` adjusts the root path and starts the detached system.

# Relationships

## Builds Upon
- **Release package** — Installation unpacks and configures the package.

## Enables
- **Target system** — Installation produces a running target system.

## Related
- **Customizing a release package** — The install/startup scripts used here come from package customization.
- **ERTS version** — A bundled ERTS makes installation self-contained.

# Common Errors

- **Error**: Starting the installed system without required contact nodes running.
  **Correction**: Start at least one contact node first, with matching short names.

- **Error**: Expecting `release_handler` to manage several releases in one directory.
  **Correction**: `release_handler` cannot do this; use the simple unpack-and-install approach for multi-release directories.

# Common Confusions

- **Confusion**: Believing installation always requires a pre-installed Erlang/OTP on the host.
  **Clarification**: If ERTS is bundled in the package, the host needs no separate Erlang/OTP installation.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.4 "Installing a release." See sidebar "Automated tools for packaging and installation."

# Verification Notes

- Definition source: Direct adaptation of Section 10.4.
- Confidence rationale: HIGH — the book explicitly describes the installation procedure.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
