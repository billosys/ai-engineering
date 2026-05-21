---
# === CORE IDENTIFICATION ===
concept: Version Scheme
slug: version-scheme

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
section: "Version Scheme"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP version scheme
  - "Major.Minor.Patch scheme"
  - OTP versioning

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - otp-version
  - application-version
  - version-ordering
  - branched-versions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP version scheme?"
  - "What distinguishes a major version bump from a minor or patch bump?"
---

# Quick Definition

The OTP version scheme, introduced in OTP 17.0, uses a `<Major>.<Minor>.<Patch>` format where Major increases for incompatible changes, Minor for new functionality, and Patch for pure bug fixes.

# Core Definition

Normally, a version is constructed as `<Major>.<Minor>.<Patch>`, where `<Major>` is the most significant part. The dot-separated parts consist of non-negative integers. "If all parts less significant than `<Minor>` equal `0`, they are omitted." The three normal parts are changed as follows:

- `<Major>` -- "Increases when major changes, including incompatibilities, are made."
- `<Minor>` -- "Increases when new functionality is added."
- `<Patch>` -- "Increases when pure bug fixes are made."

"When a part in the version number increases, all less significant parts are set to `0`." Versions with more than three dot-separated parts are possible (see branched-versions).

"An application version or an OTP version identifies source code versions. That is, it implies nothing about how the application or OTP has been built."

Source: "Version Scheme" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

Foundational concept with no prerequisites. The version scheme is the structural rule that governs how all OTP and application version numbers are formed.

# Key Properties

1. Format is `<Major>.<Minor>.<Patch>` with non-negative integer parts
2. Major increments for incompatible changes; minor for new functionality; patch for bug fixes
3. When any part increments, all less significant parts reset to `0`
4. Trailing zero parts less significant than Minor are omitted (e.g., `17.0` not `17.0.0`)
5. Versions with more than three parts are possible for branching
6. The scheme was introduced in OTP 17.0
7. Versions identify source code, not build artifacts

# Construction / Recognition

## To Construct/Create:
1. Start with `<Major>.0` for a new release
2. Increment `<Major>` and reset Minor/Patch to 0 for incompatible changes
3. Increment `<Minor>` and reset Patch to 0 for new functionality
4. Increment `<Patch>` for pure bug fixes
5. Omit trailing `.0` parts below Minor (e.g., write `6.0` not `6.0.0`)

## To Identify/Recognize:
1. A version string of dot-separated non-negative integers
2. Normal versions have exactly three parts (though trailing zeros may be omitted)
3. Versions with more than three parts indicate branching

# Context & Application

The version scheme is used consistently across both OTP versions and application versions as of OTP 17.0. It provides a predictable, semantic structure for understanding the nature and scope of changes between releases. The scheme enables users to assess compatibility risk: a major bump signals potential incompatibilities, a minor bump signals safe additions, and a patch bump signals pure fixes with no behavioral changes.

# Examples

**Example 1** (Versions section): Version `6.0` is a major release. When new functionality is added, it becomes `6.1`. A subsequent bug fix produces `6.1.1`. A further major change produces `7.0`, resetting minor and patch to zero.

**Example 2** (Versions section): The version `17.0` is written as `17.0` rather than `17.0.0` because parts less significant than Minor that equal `0` are omitted.

# Relationships

## Builds Upon
- No prerequisites — the version scheme is the foundational rule for all OTP versioning.

## Enables
- **otp-version** — OTP versions are structured according to this scheme
- **application-version** — application versions follow this same scheme
- **version-ordering** — the scheme's structure enables ordering rules for versions
- **branched-versions** — the scheme's extensibility to more than three parts enables branching

## Related
- **releases-and-patches** — releases and patches are defined in terms of the version scheme's Major, Minor, and Patch components

## Contrasts With
- No direct contrasts. Pre-OTP-17.0 versioning used a different, unspecified scheme.

# Common Errors

- **Error**: Assuming a version like `17.0` has a patch component of zero that was explicitly set.
  **Correction**: Trailing zero parts less significant than Minor are simply omitted in the representation. `17.0` and `17.0.0` refer to the same version.

- **Error**: Incrementing a minor version without resetting the patch to zero.
  **Correction**: When any version part increases, all less significant parts must be set to `0`. Version `6.1.3` followed by a minor bump becomes `6.2`, not `6.2.3`.

# Common Confusions

- **Confusion**: The version scheme describes how the software was compiled or built.
  **Clarification**: Versions identify source code versions only and imply nothing about build configuration.

- **Confusion**: The OTP version scheme is identical to Semantic Versioning (SemVer).
  **Clarification**: While similar in structure, the OTP version scheme has its own rules (e.g., omitting trailing zeros, support for more than three parts for branching) and predates the SemVer specification.

# Source Reference

"Version Scheme" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text with quoted rules)
- Confidence rationale: The source provides a precise, explicit definition of the scheme
- Uncertainties: none
- Cross-reference status: verified against source text
