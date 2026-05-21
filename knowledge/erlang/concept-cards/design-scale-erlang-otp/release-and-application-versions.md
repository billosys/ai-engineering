---
# === CORE IDENTIFICATION ===
concept: Release and Application Versions
slug: release-and-application-versions

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-principles
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Release and Application Versions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - OTP version
  - version numbering scheme
  - semantic versioning (Erlang/OTP)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-resource-file
extends: []
related:
  - otp-application
  - module-versioning
  - release-upgrade
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are releases and applications versioned in Erlang/OTP?"
  - "What concepts are needed before building a supervision tree?"
---

# Quick Definition

Erlang/OTP versions releases and applications with a three-integer `Major.Minor.Patch` scheme. An OTP version is a set of specific application versions that have been tested together with an emulator version.

# Core Definition

An OTP version is a set of specific application versions listed in the rel file that have been tested together with an emulator version (Cesarini & Vinoski, p. 290-291, pdf p. 282). An application version is a set of module versions and resources, listed in the app file or contained in the `priv` directory. Starting with OTP 17, application and OTP versions share the same numbering scheme: three integers of the format `<Major>.<Minor>.<Patch>`, where major releases include substantial, possibly non–backwards-compatible changes; minor releases add new functionality; and the patch number increments for bug fixes.

# Prerequisites

- **Release resource file** — Versions are recorded in the `.rel` file; understanding it is required.

# Key Properties

1. Format is `<Major>.<Minor>.<Patch>` since OTP 17.
2. Incrementing major resets minor and patch to 0; incrementing minor resets patch to 0.
3. Trailing 0s are usually removed — `17.1.0` is equivalent to `17.1`.
4. Higher versions include features and bug fixes from lower minor and patch releases (barring removed features and incompatible changes).
5. Versions can have more than three parts, to denote compatible-patch branches of older releases.
6. There is no limit to how many branched versions you can have.
7. Prereleases (release candidates) use the `-rcVsn` suffix, e.g. `17-rc1`.
8. The running OTP release is found with `erlang:system_info(otp_release)`; the `OTP_VERSION` file in `releases` records it (development environment only).

# Construction / Recognition

## To Version a Release or Application:
1. Choose a `Major.Minor.Patch` triple following semantic-versioning rules.
2. Bump major for substantial/incompatible changes (reset minor and patch).
3. Bump minor for new functionality (reset patch).
4. Bump patch for bug fixes.
5. For a compatible patch on an old release branch, add a fourth part (e.g. `17.1.3.1`).

## To Recognize the Running Version:
1. Call `erlang:system_info(otp_release)`.
2. Read the `OTP_VERSION` file in the `releases` directory (development environment).

# Context & Application

- **Typical contexts**: Tracking exactly which release, application, and module versions are running in production.
- **Common applications**: Supporting long-running systems years after deployment; sanity checks during boot-file generation.
- **Historical/stylistic notes**: Fixes in a branched version (e.g. `17.1.3.1`) are not guaranteed to be in `17.2`, since `17.2` may predate the branch.

# Examples

**Example 1** (p. 290): A version `17.1.0` is equivalent to `17.1` because trailing 0s are removed.

**Example 2** (p. 291): Fixes in application or release version `17.1.3.1` are not guaranteed to be included in `17.2`, as `17.2` might have been released before `17.1.3.1`.

**Example 3** (p. 291): The release candidate `17-rc1` uses the `-rcVsn` suffix.

# Relationships

## Builds Upon
- **Release resource file** — The `.rel` file ties release, application, and erts versions together.

## Related
- **OTP application** — An application version is a set of module versions and resources.
- **Module versioning** — Module versions (via the `-vsn` attribute) are the granular layer below application versions.
- **Release upgrade** — Upgrades bump application and release versions.

# Common Errors

- **Error**: Assuming a higher version always contains all fixes of a lower one.
  **Correction**: Branched versions (e.g. `17.1.3.1`) may post-date a higher minor release; verify the branch lineage.

- **Error**: Not bumping versions when changing code.
  **Correction**: Discipline in bumping module, application, and release versions is essential for diagnosing what is actually running in production.

# Common Confusions

- **Confusion**: Thinking an OTP version means those application versions are the only ones that work together.
  **Clarification**: It only means they have been tested together; you can swap and change application and emulator versions, just without that guarantee.

- **Confusion**: Believing Erlang versions are always exactly three parts.
  **Clarification**: Versions can have more than three parts to denote patch branches of older releases.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Release and Application Versions," pages 290-291 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 290-291.
- Confidence rationale: HIGH — the source explicitly defines OTP versions, application versions, and the numbering scheme.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
