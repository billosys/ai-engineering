---
# === CORE IDENTIFICATION ===
concept: Branched Versions
slug: branched-versions

# === CLASSIFICATION ===
category: applications-releases
subcategory: versioning
tier: advanced

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
  - branch versions
  - multi-part versions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - version-scheme
  - version-ordering
extends:
  - version-scheme
related:
  - otp-versions-tree
  - releases-and-patches
contrasts_with:
  - version-ordering

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes branched versions from normal versions?"
  - "What distinguishes a major version bump from a minor or patch bump?"
---

# Quick Definition

Branched versions are OTP or application versions with more than three dot-separated parts, created when branching off from another version branch. They introduce partial ordering: versions on different branches cannot be compared.

# Core Definition

"Versions can have more than three parts, resulting in partial ordering. Such versions are only used when branching off from another branch." When an extra part is added to a version number beyond the normal three, a new branch of versions is created. "The new branch has a linear order against the base version. However, versions on different branches have no order, and therefore one can only conclude that they all include what is included in their closest common ancestor."

When branching multiple times from the same base version, "0 parts are added between the base version and the least significant 1 part until a unique version is found."

Source: "Order of Versions" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **version-scheme** — the `<Major>.<Minor>.<Patch>` structure that branched versions extend
- **version-ordering** — the total ordering of normal versions that branched versions break into partial ordering

# Key Properties

1. Have more than three dot-separated parts
2. Created by branching off from another version branch
3. Have linear order against the base version (and versions less than or equal to it)
4. Have no order relative to versions on different branches
5. All branches from the same base share a closest common ancestor
6. Multiple branches from the same base use zero-padding to create unique versions
7. Can be compared with normal versions that are less than or equal to the base version

# Construction / Recognition

## To Construct/Create:
1. Start with a base version (e.g., `6.0.2`)
2. First branch: append `.1` to get `6.0.2.1`
3. Second branch from same base: insert `0` padding to get `6.0.2.0.1`
4. Third branch from same base: further padding to get `6.0.2.0.0.1`
5. Subsequent versions on a branch increment the least significant part

## To Identify/Recognize:
1. Count the dot-separated parts: more than three indicates a branched version
2. The parts before the extra parts identify the base version
3. In the OTP versions tree, branched versions on old maintenance branches are marked blue, and customer-specific branches are marked gray

# Context & Application

Branched versions arise in practice when maintenance patches or customer-specific fixes must be applied to an older OTP release that has already been superseded. For example, if OTP 26.2 is the current release but a critical fix is needed for a customer still on 26.0.2, a branched version `26.0.2.1` may be created. This fix will not necessarily appear in 26.0.3 or later, since those versions are on the main track. Branched versions are essential for understanding the OTP maintenance model but are encountered less frequently than normal versions.

# Examples

**Example 1** (Versions section): "The version `6.0.2.1` is a branched version from the base version `6.0.2`. Versions of the form `6.0.2.<X>` can be compared with normal versions smaller than or equal to `6.0.2`, and other versions on the form `6.0.2.<X>`."

**Example 2** (Versions section): "The version `6.0.2.1` will include all changes in `6.0.2`. However, `6.0.3` will most likely _not_ include all changes in `6.0.2.1` (note that these versions have no order)."

**Example 3** (Versions section): Multiple branches from the same base: "A second branched version from the base version `6.0.2` will be version `6.0.2.0.1`, and a third branched version will be `6.0.2.0.0.1`."

# Relationships

## Builds Upon
- **version-scheme** — branched versions extend the normal three-part scheme with additional parts
- **version-ordering** — branched versions break total ordering into partial ordering

## Enables
- **otp-versions-tree** — the tree visualization shows how branched versions relate to the main track

## Related
- **releases-and-patches** — branched versions typically arise from emergency patches on older releases

## Contrasts With
- **version-ordering** — normal versions have total ordering; branched versions on different branches have no defined order relative to each other

# Common Errors

- **Error**: Assuming `6.0.3` includes all changes from `6.0.2.1`.
  **Correction**: `6.0.3` and `6.0.2.1` are on different branches and have no order. `6.0.3` will most likely not include the changes specific to `6.0.2.1`.

- **Error**: Treating branched versions as sequential patches on the main track.
  **Correction**: Branched versions represent a separate line of development. Only versions on the same branch or the base version line can be compared.

# Common Confusions

- **Confusion**: A branched version like `6.0.2.1` is "between" `6.0.2` and `6.0.3`.
  **Clarification**: `6.0.2.1` is on a separate branch from the base `6.0.2`. It is not between `6.0.2` and `6.0.3`; it and `6.0.3` have no ordering relationship.

- **Confusion**: The zero-padding in `6.0.2.0.1` indicates a version less than `6.0.2.1`.
  **Clarification**: `6.0.2.0.1` is on a completely different branch from `6.0.2.1`. They share the common ancestor `6.0.2` but have no order relative to each other. The zeros are used solely to create a unique version identifier for the second branch from the same base.

# Source Reference

"Order of Versions" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text with detailed examples)
- Confidence rationale: The source provides a thorough explanation with concrete examples
- Uncertainties: none
- Cross-reference status: verified against source text
