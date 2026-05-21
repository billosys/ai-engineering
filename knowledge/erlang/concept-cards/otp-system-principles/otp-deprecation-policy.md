---
# === CORE IDENTIFICATION ===
concept: OTP Deprecation Policy
slug: otp-deprecation-policy

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
section: "Deprecation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP deprecation
  - Erlang deprecation policy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-supported-releases
extends: []
related:
  - otp-compatibility
contrasts_with:
  - otp-removal-policy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP deprecation policy?"
  - "What distinguishes deprecation from removal in OTP?"
  - "Does deprecation mean a feature will be removed?"
---

# Quick Definition

OTP deprecation occurs when newer, preferred alternatives are introduced. Critically, deprecation does NOT imply future removal of the functionality unless an upcoming removal is explicitly stated in the deprecation notice.

# Core Definition

Deprecation of functionality occurs when newer, preferred alternatives are introduced. The deprecation does **not** imply future removal of the functionality unless an upcoming removal is explicitly stated in the deprecation notice. Deprecated functionality will be documented as deprecated and highlighted in a release note as early as possible. If appropriate, the compiler will issue warnings when the deprecated functionality is used.

# Prerequisites

- Understanding of OTP's supported releases and release cadence

# Key Properties

1. Deprecation signals that newer, preferred alternatives exist
2. Deprecation does NOT imply removal unless explicitly stated in the deprecation notice
3. Deprecated functionality is documented as deprecated
4. Deprecation is highlighted in release notes as early as possible
5. The compiler may issue warnings when deprecated functionality is used (when appropriate)
6. A centralized "Deprecations" documentation page lists all deprecated functionality

# Construction / Recognition

## To Construct/Create:
1. Not applicable -- this is a policy, not a constructed artifact

## To Identify/Recognize:
1. Check the "Deprecations" page in OTP documentation for a comprehensive list
2. Look for deprecation notices in release notes
3. Watch for compiler warnings when using deprecated functions or modules
4. Read the deprecation notice carefully to determine whether removal is also planned

# Context & Application

OTP's deprecation policy is notably conservative: deprecation alone does not promise removal. This means deprecated functionality may remain available indefinitely, and users are not forced to migrate away from deprecated features on any particular timeline. However, users should still prefer the newer alternatives, as deprecated functionality may eventually be scheduled for removal (which would be announced separately). The compiler warnings serve as the primary mechanism for alerting developers to deprecated usage in their codebases.

# Examples

**Example 1** (deprecation without removal): A function is deprecated in OTP 25 with the notice "Use new_function/2 instead." Since the notice does not mention upcoming removal, the deprecated function may remain available indefinitely. Users should migrate to the new function but are not under immediate pressure.

**Example 2** (deprecation with removal): A function is deprecated in OTP 26 with the notice "Deprecated; will be removed in OTP 28. Use replacement_function/1 instead." This deprecation explicitly states removal, so users must migrate before OTP 28.

# Relationships

## Builds Upon
- **otp-supported-releases** -- deprecation notices appear in release notes within the supported release framework

## Enables
- **otp-removal-policy** -- removal requires at least one release of prior deprecation

## Related
- **otp-compatibility** -- deprecation is a mechanism for managing compatibility transitions over time

## Contrasts With
- **otp-removal-policy** -- deprecation does not imply removal; removal is a separate, stronger action that requires explicit announcement and at least one release of prior deprecation

# Common Errors

- **Error**: Treating all deprecation notices as signals of imminent removal
  **Correction**: Deprecation does NOT imply removal unless the deprecation notice explicitly states that removal is planned. Read the notice carefully.

- **Error**: Ignoring deprecation warnings from the compiler
  **Correction**: While deprecated functionality may persist, the warnings indicate that preferred alternatives exist. Migrating early avoids future disruption if removal is eventually announced.

# Common Confusions

- **Confusion**: Deprecation and removal are the same thing in OTP
  **Clarification**: They are explicitly distinct. Deprecation means "a better alternative exists." Removal means "this will cease to exist." Deprecation does not imply removal unless explicitly stated.

- **Confusion**: All deprecated functions produce compiler warnings
  **Clarification**: The source states compiler warnings are issued "if appropriate," meaning not all deprecated functionality necessarily triggers warnings.

# Source Reference

"Deprecation" section, "Support, Compatibility, Deprecations, and Removal" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (explicitly stated policy in source text, with emphasis on the non-implication of removal)
- Confidence rationale: The source provides a clear, concise policy statement with the key distinction bolded in the original text
- Uncertainties: none
- Cross-reference status: references "Deprecations" documentation page (unverified)
