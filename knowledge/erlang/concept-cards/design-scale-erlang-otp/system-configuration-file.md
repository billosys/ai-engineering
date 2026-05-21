---
# === CORE IDENTIFICATION ===
concept: System Configuration File
slug: system-configuration-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-files
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Creating a Release Package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sys.config
  - ".config file"
  - configuration file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - release-package
  - start-scripts-and-configuration
  - arguments-and-flags
  - upgrading-environment-variables
contrasts_with:
  - application-resource-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the system configuration file?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The system configuration file (`sys.config`) holds application-specific environment variables for a release, overriding values in the individual app files. It must be present at install time or the system will not start.

# Core Definition

The system configuration file contains application-specific environment variables (Cesarini & Vinoski, Table 11-1, p. 311; "Creating a Release Package," p. 285, pdf p. 282). It is used to generate target-specific values at install time, overriding those specified in the app files. The configuration file must be named `sys.config`, although the name can be changed by tweaking the arguments passed to the emulator. It is optional at packaging time, but must be present (possibly empty) when the system is installed — otherwise the system will not start.

# Prerequisites

- **Release** — `sys.config` configures a release; the release concept comes first.

# Key Properties

1. Has the `.config` extension; conventionally named `sys.config`.
2. Contains application-specific environment variables.
3. Overrides values specified in the individual application app files.
4. Optional at packaging time but mandatory at install time (an empty file is acceptable).
5. Placed in the `releases/Vsn` directory alongside the `.rel` file.
6. The name can be overridden via the `-config filename` flag to the emulator.
7. During a release upgrade the new package includes a new (mandatory) `sys.config`; the application controller compares old and new environment variables and calls `config_change/3`.

# Construction / Recognition

## To Create and Place It:
1. Create the file (it can be empty: `[].`); conventionally name it `sys.config`.
2. Place it in the same directory as the `.rel` file so `make_tar/2` picks it up.
3. After untarring, confirm it landed in `releases/Vsn`; if not, copy it there during installation.

## To Recognize It:
1. Look for `sys.config` in the `releases/Vsn` directory.
2. Confirm it holds a list of `{Application, [{Key, Value}]}` configuration tuples.

# Context & Application

- **Typical contexts**: Supplying deployment-specific configuration that differs across installations.
- **Common applications**: Customizing configuration per installation across tens of thousands of deployments; supplying release-wide environment variables at upgrade time.
- **Historical/stylistic notes**: Configuration may be identical across all deployments, individually customized per target, or a combination of both.

# Examples

**Example 1** (p. 285): The `sys.config` file is included in the `releases/1.0` directory when it sits alongside the `.rel` file at packaging time.

**Example 2** (Ch. 11, p. 326): An empty configuration file used for the coffee release:

```erlang
$ cat sys.config
[].
```

# Relationships

## Related
- **Release package** — `sys.config` is bundled into the package's `releases/Vsn` directory.
- **Start scripts and configuration** — Start scripts point at `sys.config` via `-config`.
- **Arguments and flags** — The `-config filename` flag overrides the config file name/location.
- **Upgrading environment variables** — A new `sys.config` is shipped on every upgrade.

## Contrasts With
- **Application resource file** — The `.app` file describes one application's defaults; `sys.config` overrides those defaults release-wide at deployment.

# Common Errors

- **Error**: Omitting `sys.config` from both the package and the installation.
  **Correction**: It is optional only at packaging time; ensure it is present (even empty) when installing, or the system will not start.

- **Error**: Leaving `sys.config` in a directory different from the `.rel` file at packaging time.
  **Correction**: Place it alongside the `.rel` file so `make_tar/2` picks it up, or copy it to `releases/Vsn` during installation.

# Common Confusions

- **Confusion**: Thinking the file must literally be named `sys.config`.
  **Clarification**: `sys.config` is the conventional name; it can be changed via the `-config` flag.

- **Confusion**: Believing `sys.config` and the app file serve the same purpose.
  **Clarification**: The app file holds an application's default environment; `sys.config` provides deployment-specific overrides for the whole release.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Creating a Release Package," page 285, and Table 11-1 (Erlang/OTP file types), page 311 (pdf p. 282). See also Chapter 11 "Upgrading Environment Variables."

# Verification Notes

- Definition source: Synthesized from the `make_tar` discussion on p. 285 and Table 11-1 on p. 311.
- Confidence rationale: HIGH — the source explicitly describes `sys.config`, its naming, optionality, and placement.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
