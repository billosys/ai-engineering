---
# === CORE IDENTIFICATION ===
concept: OTP Supported Releases
slug: otp-supported-releases

# === CLASSIFICATION ===
category: applications-releases
subcategory: support-policy
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Support, Compatibility, Deprecations, and Removal"
chapter_number: null
pdf_page: null
section: "Supported Releases"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP support policy
  - OTP release support

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - otp-compatibility
  - otp-deprecation-policy
  - otp-removal-policy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which OTP releases receive bug fixes?"
  - "Where should I submit pull requests for OTP?"
  - "What is the OTP support policy?"
---

# Quick Definition

OTP's support policy states that bugs are generally only fixed on the latest release, new features target the upcoming release under development, and pull requests are only accepted on the `maint` and `master` branches of the OTP git repository.

# Core Definition

In general, bugs are only fixed on the latest release, and new features are introduced in the upcoming release that is under development. However, when the OTP team, for internal reasons, fixes bugs on older releases, these will be available and announced as well. Pull requests are only accepted on the `maint` and the `master` branches in the git repository. The `maint` branch contains changes planned for the next maintenance patch package on the latest OTP release and the `master` branch contains changes planned for the upcoming OTP release.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Bug fixes target only the latest OTP release
2. New features target the upcoming (under development) release
3. Older release fixes may be made available when done for internal reasons, but this is not guaranteed
4. Pull requests are accepted only on two branches: `maint` and `master`
5. The `maint` branch corresponds to maintenance patches for the latest release
6. The `master` branch corresponds to the next major OTP release

# Construction / Recognition

## To Construct/Create:
1. Not applicable -- this is a policy, not a constructed artifact

## To Identify/Recognize:
1. Check whether an OTP release is the latest version to determine if it receives active bug fixes
2. Consult the `maint` branch for the latest release's maintenance patches
3. Consult the `master` branch for upcoming release features

# Context & Application

Understanding OTP's support policy is essential for planning production system maintenance. Since only the latest release receives bug fixes, organizations running older OTP versions must either upgrade or accept that bugs they encounter may not be fixed upstream. This policy also guides open-source contributors: pull requests against older release branches will not be accepted. The strategy described in this document was introduced in Erlang/OTP 21.

# Examples

**Example 1** (branch targeting): A developer discovers a bug in OTP 26. If OTP 27 is the latest release, the fix should be submitted as a pull request against the `maint` branch (for OTP 27 maintenance) or the `master` branch (for OTP 28 development). A pull request targeting an OTP 26 branch would not be accepted.

**Example 2** (internal fixes): Occasionally the OTP team fixes bugs on older releases for their own internal reasons. When this happens, the fixes are made publicly available and announced, but external users should not depend on this happening for any particular bug.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **otp-compatibility** -- understanding what is supported informs expectations about compatibility guarantees
- **otp-deprecation-policy** -- the support policy provides context for how deprecation timelines work
- **otp-removal-policy** -- knowing the release cadence helps understand removal timelines

## Related
- **otp-compatibility** -- compatibility guarantees complement the support policy
- **otp-deprecation-policy** -- deprecation notices appear in release notes of supported releases
- **otp-removal-policy** -- removal is phased across releases subject to this support policy

## Contrasts With
- None

# Common Errors

- **Error**: Expecting bug fixes to be backported to older OTP releases
  **Correction**: Bugs are generally only fixed on the latest release. Plan to upgrade if you need fixes.

- **Error**: Submitting pull requests against release-specific branches other than `maint` or `master`
  **Correction**: Only `maint` (latest release patches) and `master` (next release) accept pull requests.

# Common Confusions

- **Confusion**: The `maint` branch tracks maintenance for all supported releases
  **Clarification**: The `maint` branch only contains changes for the next maintenance patch package of the single latest OTP release.

# Source Reference

"Supported Releases" section, "Support, Compatibility, Deprecations, and Removal" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly stated policy in source text)
- Confidence rationale: The source provides a clear, unambiguous policy statement
- Uncertainties: none
- Cross-reference status: unverified (references versions.md for release/patch definitions)
