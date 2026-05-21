---
# === CORE IDENTIFICATION ===
concept: Application Version
slug: application-version

# === CLASSIFICATION ===
category: applications-releases
subcategory: versioning
tier: foundational

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Versions"
chapter_number: null
pdf_page: null
section: "Application Version"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - app version
  - application version number

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-version
extends: []
related:
  - version-scheme
  - otp-versions-table
contrasts_with:
  - otp-version

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the OTP version relate to application versions?"
  - "How do I determine which OTP version includes a specific application version?"
---

# Quick Definition

An application version identifies a specific source code version of an individual OTP application (e.g., `kernel-3.0`). Application versions follow the same version scheme as OTP versions but never include the `-rc<N>` suffix.

# Core Definition

As of OTP 17.0, application versions use the same `<Major>.<Minor>.<Patch>` version scheme as the OTP version. However, application versions differ from OTP versions in two key ways: they never include the `-rc<N>` (release candidate) suffix, and "a major increment in an application version does not necessarily imply a major increment of the OTP version. This depends on whether the major change in the application is considered a major change for OTP as a whole or not."

An application version identifies source code versions only and implies nothing about how the application has been built.

Source: "Application Version" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **otp-version** — application versions exist within the context of OTP versions; an OTP version bundles a specific set of application versions

# Key Properties

1. Uses the same `<Major>.<Minor>.<Patch>` version scheme as OTP versions
2. Never includes the `-rc<N>` release candidate suffix
3. A major increment in an application version does not necessarily cause a major increment in the OTP version
4. Identifies source code versions, not build artifacts
5. Each application version is uniquely associated with one or more OTP versions via `otp_versions.table`

# Construction / Recognition

## To Construct/Create:
1. Follow the `<Major>.<Minor>.<Patch>` scheme
2. Increment `<Major>` for incompatible changes, `<Minor>` for new functionality, `<Patch>` for bug fixes
3. Do not append `-rc<N>` suffixes (those are OTP-version-only)

## To Identify/Recognize:
1. Application versions appear in the format `<application>-<vsn>` (e.g., `kernel-3.0`, `stdlib-2.0`)
2. Look up specific application versions in the `otp_versions.table` file
3. Application versions with normal parts smaller than the OTP 17.0 baseline do not adhere to the current versioning scheme

# Context & Application

Application versions are essential for tracking which version of a particular OTP library or framework component is in use. When troubleshooting or reporting issues, the specific application version (not just the OTP version) may be needed to identify whether a bug fix or feature is present. The `otp_versions.table` file provides the definitive mapping between OTP versions and their constituent application versions.

# Examples

**Example 1** (Versions section): In OTP 17.0, the kernel application was at version `kernel-3.0` and stdlib was at `stdlib-2.0`. These are the baseline versions for the current versioning scheme.

**Example 2** (Versions section): If the kernel application receives a major incompatible change bumping it from `kernel-8.0` to `kernel-9.0`, the OTP version might only receive a minor bump (e.g., from `26.1` to `26.2`) if the kernel change is not considered a major change for OTP as a whole.

# Relationships

## Builds Upon
- **otp-version** — application versions are defined and tested within the context of specific OTP versions

## Enables
- **otp-versions-table** — the `otp_versions.table` file tracks which application versions belong to which OTP versions

## Related
- **version-scheme** — application versions follow the same version scheme as OTP versions
- **releases-and-patches** — patches to an OTP release may change specific application versions

## Contrasts With
- **otp-version** — an OTP version identifies the whole release; an application version identifies a single application. OTP versions may have `-rc<N>` suffixes; application versions never do. A major application version bump does not necessarily cause a major OTP version bump.

# Common Errors

- **Error**: Assuming a major application version bump means a major OTP version bump.
  **Correction**: Whether an application's major change constitutes a major OTP change depends on whether it is considered major for OTP as a whole.

- **Error**: Comparing application versions from before OTP 17.0 with current versions.
  **Correction**: Application versions with normal parts smaller than the OTP 17.0 baseline list do not adhere to the current versioning scheme and have no defined order relative to post-17.0 versions.

# Common Confusions

- **Confusion**: Application versions and OTP versions always increment in lockstep.
  **Clarification**: Application versions and OTP versions are incremented independently. An OTP patch may change only a few application versions while leaving others unchanged.

# Source Reference

"Application Version" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text)
- Confidence rationale: The source clearly defines application versions and their relationship to OTP versions
- Uncertainties: none
- Cross-reference status: verified against source text
