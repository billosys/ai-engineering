---
# === CORE IDENTIFICATION ===
concept: Releases and Patches
slug: releases-and-patches

# === CLASSIFICATION ===
category: applications-releases
subcategory: versioning
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Versions"
chapter_number: null
pdf_page: null
section: "Releases and Patches"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP releases
  - maintenance patches
  - emergency patches
  - patch packages

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-version
  - version-scheme
extends: []
related:
  - application-version
  - branched-versions
  - otp-versions-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release in the context of OTP versioning?"
  - "How do maintenance patches relate to emergency patches?"
  - "What distinguishes a major version bump from a minor or patch bump?"
  - "What distinguishes a major version bump from a minor or patch bump?"
---

# Quick Definition

An OTP release is a new major version (e.g., `<Major>.0`), while patches are subsequent versions with the same major number. Patches come in two forms: planned maintenance patch packages (usually incrementing Minor) and unplanned emergency patch packages (usually incrementing Patch).

# Core Definition

"When a new OTP release is released it will have an OTP version on the form `<Major>.0` where the major OTP version number equals the release number. The major version number is increased one step since the last major version. All other OTP versions with the same major OTP version number are patches on that OTP release."

"Patches are either released as maintenance patch packages or emergency patch packages. The only difference is that maintenance patch packages are planned and usually contain more changes than emergency patch packages. Emergency patch packages are released to solve one or more specific issues when such are discovered."

The version component affected depends on the nature of the changes: "The release of a maintenance patch package usually implies an increase of the OTP `<Minor>` version, while the release of an emergency patch package usually implies an increase of the OTP `<Patch>` version. However, this is not always the case, as changes in OTP versions are determined by actual code modifications rather than whether the patch was planned or not."

Source: "Releases and Patches" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **otp-version** — releases and patches are defined in terms of OTP version numbers
- **version-scheme** — the Major.Minor.Patch structure determines how releases and patches are numbered

# Key Properties

1. A new OTP release has version `<Major>.0`, where Major equals the release number
2. Major is incremented by one from the previous release
3. All versions with the same Major number are patches on that release
4. Maintenance patch packages are planned and typically larger in scope
5. Emergency patch packages are unplanned, solving specific discovered issues
6. Maintenance patches usually increment Minor; emergency patches usually increment Patch
7. The version component incremented is determined by actual code changes, not patch type

# Construction / Recognition

## To Construct/Create:
1. For a new release: increment Major by one, set Minor and Patch to 0 (e.g., `26.0`)
2. For a maintenance patch: typically increment Minor (e.g., `26.0` to `26.1`)
3. For an emergency patch: typically increment Patch (e.g., `26.1` to `26.1.1`)
4. Actual version component choice depends on the nature of the code changes

## To Identify/Recognize:
1. A version of the form `<Major>.0` is a release
2. A version with the same Major but non-zero Minor or Patch is a patch
3. The distinction between maintenance and emergency patches is not encoded in the version number itself

# Context & Application

Understanding the distinction between releases and patches is essential for planning upgrades and assessing risk. A new release (major version bump) may contain incompatible changes requiring code modifications. Maintenance patches add new functionality with lower risk. Emergency patches are the safest to apply, typically containing only targeted bug fixes. In production environments, emergency patches should be applied promptly when they address relevant issues, while maintenance patches and new releases warrant more thorough testing.

# Examples

**Example 1** (Versions section): OTP 26 is released as version `26.0`. Subsequent maintenance patches produce `26.1`, `26.2`, etc. An emergency fix on `26.1` produces `26.1.1`.

**Example 2** (Versions section): A maintenance patch package for OTP 26 that adds new functionality to several applications would typically be released as `26.1` (Minor increment). An emergency patch fixing a critical bug in one application would typically be released as `26.1.1` (Patch increment).

# Relationships

## Builds Upon
- **otp-version** — releases and patches are identified by their OTP version numbers
- **version-scheme** — the Major.Minor.Patch structure determines how releases and patches relate

## Enables
- **otp-versions-tree** — the tree visualizes the relationship between releases, maintenance patches, and emergency patches
- **branched-versions** — emergency patches on old releases may require branched versions

## Related
- **application-version** — each patch changes the versions of one or more applications within the OTP release
- **otp-versions-table** — the table records which application versions changed in each patch

## Contrasts With
- No direct contrasts. Maintenance and emergency patches are distinguished within this concept.

# Common Errors

- **Error**: Assuming the version component (Minor vs. Patch) directly indicates whether a patch is maintenance or emergency.
  **Correction**: While maintenance patches usually increment Minor and emergency patches usually increment Patch, the actual version component is determined by the nature of the code changes, not the patch classification.

- **Error**: Treating all patches as equally safe to apply.
  **Correction**: Maintenance patches may add new functionality and are larger in scope. Emergency patches are narrowly targeted. Risk assessment should consider the scope of changes.

# Common Confusions

- **Confusion**: Emergency patches are more important or significant than maintenance patches.
  **Clarification**: Emergency patches are unplanned responses to specific discovered issues. They are typically smaller and more narrowly focused than maintenance patches, not more significant.

- **Confusion**: The release number and the OTP version are different identifiers.
  **Clarification**: The release number equals the Major part of the OTP version. OTP release 26 corresponds to OTP version `26.x.y`.

# Source Reference

"Releases and Patches" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text with quoted definitions)
- Confidence rationale: The source provides clear definitions of releases, maintenance patches, and emergency patches
- Uncertainties: none
- Cross-reference status: verified against source text
