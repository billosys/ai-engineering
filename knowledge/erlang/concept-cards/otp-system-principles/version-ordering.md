---
# === CORE IDENTIFICATION ===
concept: Version Ordering
slug: version-ordering

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
section: "Order of Versions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - order of versions
  - version comparison
  - version ordering rules

# === TYPED RELATIONSHIPS ===
prerequisites:
  - version-scheme
extends: []
related:
  - otp-version
  - application-version
  - branched-versions
contrasts_with:
  - branched-versions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP version scheme?"
  - "What distinguishes branched versions from normal versions?"
---

# Quick Definition

Normal OTP and application versions (with three parts) have a total (linear) order, determined by comparing each part as integers from most significant to least significant. Versions with more than three parts introduce partial ordering.

# Core Definition

"Version numbers in general are only partially ordered. However, normal version numbers (with three parts) as of OTP 17.0 have a total or linear order. This applies both to normal OTP versions and normal application versions."

The comparison algorithm: "When comparing two version numbers with a defined order, one compares each part as standard integers, starting from the most significant part and moving towards the less significant parts. The order is determined by the first parts of the same significance that differ."

A key semantic consequence: "A larger OTP version encompasses all changes present in a smaller OTP version. The same principle applies to application versions."

Source: "Order of Versions" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **version-scheme** — the `<Major>.<Minor>.<Patch>` structure must be understood before ordering rules make sense

# Key Properties

1. Normal versions (three parts) have a total/linear order
2. Comparison proceeds from most significant to least significant part
3. Parts are compared as standard integers
4. The first differing part determines the order
5. A larger version encompasses all changes present in any smaller version
6. Versions with more than three parts are only partially ordered
7. The total ordering applies to both OTP versions and application versions

# Construction / Recognition

## To Construct/Create:
1. To compare two normal versions, compare Major parts first
2. If Major parts are equal, compare Minor parts
3. If Minor parts are equal, compare Patch parts
4. The version with the first larger differing part is the greater version

## To Identify/Recognize:
1. If both versions have exactly three parts, they have a defined total order
2. If either version has more than three parts, ordering may be partial (see branched-versions)
3. Two versions on different branches have no order relative to each other

# Context & Application

Version ordering is essential for determining whether one version includes all changes from another. When upgrading or troubleshooting, you need to know that version `6.1.2` includes all fixes from `6.1.1`, `6.1`, `6.0`, etc. The total ordering of normal versions makes upgrade paths straightforward. The partial ordering introduced by branched versions reflects the reality that branch-specific patches may not flow into the main track.

# Examples

**Example 1** (Versions section): Comparing `6.1.2` and `6.2.0`: Major parts are equal (both `6`), Minor parts differ (`1` < `2`), so `6.1.2 < 6.2.0`. Version `6.2.0` encompasses all changes present in `6.1.2`.

**Example 2** (Versions section): Comparing `17.0` and `17.1`: Major parts are equal (both `17`), Minor parts differ (`0` < `1`), so `17.0 < 17.1`.

# Relationships

## Builds Upon
- **version-scheme** — the `<Major>.<Minor>.<Patch>` structure defines the parts that are compared

## Enables
- **branched-versions** — understanding total ordering is necessary to understand when and why partial ordering arises with branched versions

## Related
- **otp-version** — OTP versions are ordered by these rules
- **application-version** — application versions are ordered by these rules
- **releases-and-patches** — patches produce new versions that are ordered relative to the base release

## Contrasts With
- **branched-versions** — normal versions have total ordering; branched versions introduce partial ordering where some version pairs have no defined relationship

# Common Errors

- **Error**: Assuming all versions can be compared (i.e., have a total order).
  **Correction**: Only normal versions (three parts) have a total order. Branched versions (more than three parts) on different branches cannot be compared.

- **Error**: Comparing version parts as strings rather than integers.
  **Correction**: Version parts must be compared as standard integers. String comparison would incorrectly rank `9` above `10`.

# Common Confusions

- **Confusion**: A larger version number means a completely different and unrelated codebase.
  **Clarification**: A larger version encompasses all changes present in smaller versions. Version `6.2` includes everything from `6.1`, `6.0`, etc.

# Source Reference

"Order of Versions" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text with quoted rules)
- Confidence rationale: The source provides clear, explicit ordering rules
- Uncertainties: none
- Cross-reference status: verified against source text
