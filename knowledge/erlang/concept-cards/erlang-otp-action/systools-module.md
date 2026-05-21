---
# === CORE IDENTIFICATION ===
concept: systools Module
slug: systools-module

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
section: "10.2.4. The script and boot files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - systools

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rel-file
extends: []
related:
  - boot-script
  - release-package
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the systools module?"
  - "What functions does systools provide for building releases?"
---

# Quick Definition

`systools` is the SASL module that turns a `.rel` file into the artifacts of a release — it generates boot scripts (`make_script`) and release packages (`make_tar`).

# Core Definition

`systools` is a module that is part of the SASL application, used to build the artifacts of a release from a `.rel` file. `systools:make_script/2` generates the `.script` and `.boot` files; `systools:script2boot/1` regenerates the `.boot` file from an edited `.script`; and `systools:make_tar/2` produces a compressed tarball release package containing all the release files ("Erlang and OTP in Action," Ch. 10, Sections 10.2.4 and 10.3.1).

# Prerequisites

- **.rel file** — `systools` functions take the release name of a `.rel` file as input.

# Key Properties

1. Part of the SASL application.
2. `make_script(Release, Options)` generates `.script` and `.boot` files; the `local` option writes absolute paths.
3. `script2boot(Release)` regenerates the `.boot` file after a manual `.script` edit.
4. `make_tar(Release, Options)` produces a `Release.tar.gz` release package; the `{erts, Path}` option bundles the runtime system.
5. Requires that `erl` was started with `-pa` paths to all the release's applications.
6. Reports version errors when the `.rel` file's versions do not match the local system.

# Construction / Recognition

## To Construct/Create:
This is a standard library module; you call it from the Erlang shell. There is nothing to create.

## To Identify/Recognize:
1. Calls of the form `systools:make_script(...)` or `systools:make_tar(...)` in build instructions.

# Context & Application

- **Typical contexts**: The release build step, run from an Erlang shell.
- **Common applications**: Generating boot files and packaging the Simple Cache release.
- **Historical/stylistic notes**: People have built additional community tools on top of `systools` because OTP's release process still needs manual steps.

# Examples

**Example 1** (Section 10.2.4): `systools:make_script("simple_cache", [local])` generates `simple_cache.script` and `simple_cache.boot`.

**Example 2** (Section 10.3.1): `systools:make_tar("simple_cache", [{erts, code:root_dir()}])` builds `simple_cache.tar.gz` with ERTS included.

# Relationships

## Builds Upon
- **.rel file** — `systools` reads release metadata from the `.rel` file.

## Enables
- **Boot script** — `make_script` produces the `.script`/`.boot` files.
- **Release package** — `make_tar` produces the release tarball.

# Common Errors

- **Error**: Calling `systools` functions without first adding application code paths with `-pa`.
  **Correction**: Start `erl` with `-pa` for every release application not on the default path.

# Common Confusions

- **Confusion**: Thinking `systools` is a build tool that runs at the OS shell.
  **Clarification**: `systools` is an Erlang module; its functions are called from inside an Erlang shell.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Sections 10.2.4 "The script and boot files" and 10.3.1 "Creating a release package."

# Verification Notes

- Definition source: Synthesized from Sections 10.2.4 and 10.3.1, which describe `systools` functions but do not give a single formal definition of the module.
- Confidence rationale: HIGH — every function is explicitly described, even though the module itself is not formally "defined."
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
