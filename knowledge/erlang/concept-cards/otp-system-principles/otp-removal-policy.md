---
# === CORE IDENTIFICATION ===
concept: OTP Removal Policy
slug: otp-removal-policy

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
section: "Removal"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP removal
  - OTP feature removal policy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-deprecation-policy
extends: []
related:
  - otp-compatibility
  - otp-supported-releases
contrasts_with:
  - otp-deprecation-policy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes deprecation from removal in OTP?"
  - "How is functionality removed from OTP?"
  - "What is the minimum deprecation period before removal?"
---

# Quick Definition

OTP's removal policy requires that legacy solutions be gradually phased out over a sufficient period, with at least one release of deprecation (including an explicit removal announcement) before functionality is actually removed.

# Core Definition

It can become necessary to remove legacy solutions. In such instances, they will be gradually phased out over a sufficient period to allow users to adjust. Before functionality is removed, it will be deprecated for at least one release, with an explicit announcement about the upcoming removal. Peripheral, trace, and debug functionality is at greater risk of removal than functionality in the language itself and core libraries used during operation.

# Prerequisites

- Understanding of OTP's deprecation policy, since removal requires prior deprecation

# Key Properties

1. Removal is applied to "legacy solutions" -- functionality that has become obsolete
2. Phased out gradually over a "sufficient period" to allow user adjustment
3. Requires at least one full release of deprecation before removal
4. The deprecation notice must explicitly announce the upcoming removal
5. Peripheral, trace, and debug functionality faces greater risk of removal than core language and library functionality
6. Two documentation pages track removal: "Scheduled for Removal" (planned) and "Removed Functionality" (completed)

# Construction / Recognition

## To Construct/Create:
1. Not applicable -- this is a policy, not a constructed artifact

## To Identify/Recognize:
1. Check the "Scheduled for Removal" documentation page for functionality planned for removal in upcoming releases
2. Check the "Removed Functionality" documentation page for functionality that has already been removed
3. Look for deprecation notices that explicitly mention upcoming removal

# Context & Application

The removal policy provides a predictable lifecycle for OTP functionality: a feature is first deprecated with an explicit removal notice, then removed after at least one release. This gives users a minimum of one full release cycle to migrate. The "at least one release" minimum means the actual deprecation period may be longer depending on the significance of the functionality. The distinction between core and peripheral functionality means that tracing, debugging, and other peripheral features may be removed with less notice than core language features, though the one-release minimum still applies.

# Examples

**Example 1** (minimum timeline): A function deprecated in OTP 26 with an explicit removal notice could be removed as early as OTP 27. Users have the entire OTP 26 lifecycle to migrate to the replacement.

**Example 2** (risk gradient): A debugging utility function in a peripheral module faces greater risk of removal than a function in the `lists` module or the `gen_server` behaviour, which are core to the language and used during operation.

**Example 3** (documentation tracking): The "Scheduled for Removal" page lists all functionality planned for removal in upcoming releases, giving users advance notice. After removal, the functionality moves to the "Removed Functionality" page for historical reference.

# Relationships

## Builds Upon
- **otp-deprecation-policy** -- removal requires prior deprecation; the deprecation notice must explicitly state that removal is planned

## Enables
- Understanding of the full lifecycle of OTP functionality (introduction, deprecation, removal)

## Related
- **otp-compatibility** -- removal is the ultimate end of backward compatibility for a feature
- **otp-supported-releases** -- the release cadence determines the practical timeline between deprecation and removal

## Contrasts With
- **otp-deprecation-policy** -- deprecation alone does NOT imply removal; removal is a separate, stronger commitment that must be explicitly announced and requires at least one release of prior deprecation

# Common Errors

- **Error**: Assuming deprecated functionality will be removed in the next release
  **Correction**: The minimum is at least one release of deprecation, but the actual period may be longer. Only functionality with an explicit removal announcement in the deprecation notice is scheduled for removal.

- **Error**: Ignoring the "Scheduled for Removal" documentation page
  **Correction**: This page is the authoritative source for upcoming removals and should be checked before upgrading OTP versions.

# Common Confusions

- **Confusion**: All deprecated functionality will eventually be removed
  **Clarification**: Deprecation does NOT imply removal. Only functionality with an explicit removal announcement will be removed. Some deprecated features may persist indefinitely.

- **Confusion**: Core language features and peripheral features have the same removal risk
  **Clarification**: Peripheral, trace, and debug functionality is explicitly stated to be at greater risk of removal than core language and library functionality.

# Source Reference

"Removal" section, "Support, Compatibility, Deprecations, and Removal" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly stated policy in source text)
- Confidence rationale: The source provides a clear policy statement with specific minimum requirements
- Uncertainties: "sufficient period" is subjective and not precisely defined beyond the one-release minimum
- Cross-reference status: references "Scheduled for Removal" and "Removed Functionality" documentation pages (unverified)
