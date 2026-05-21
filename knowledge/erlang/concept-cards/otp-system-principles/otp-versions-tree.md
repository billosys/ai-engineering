---
# === CORE IDENTIFICATION ===
concept: OTP Versions Tree
slug: otp-versions-tree

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
section: "OTP Versions Tree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - version tree
  - OTP version tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - version-scheme
  - version-ordering
  - branched-versions
  - releases-and-patches
extends: []
related:
  - otp-version
  - otp-versions-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP version scheme?"
  - "What distinguishes branched versions from normal versions?"
---

# Quick Definition

The OTP Versions Tree is a visual representation of all released OTP versions, rooted at OTP 17.0, that shows the branching structure of releases and patches using color-coded nodes: green for main track, blue for maintenance branches, and gray for customer-specific branches.

# Core Definition

"All released OTP versions can be found in the OTP Versions Tree, which is automatically updated whenever we release a new OTP version." The tree is available at `http://www.erlang.org/download/otp_versions_tree.html`.

A key property of the tree: "each version number explicitly determines its position in the version tree. All that is required to build the tree are the version numbers themselves."

The tree is rooted at OTP 17.0, "which is when we introduced the new version scheme." The tree uses three color categories:

- **Green versions**: normal versions released on the main track
- **Blue versions**: versions on old `maint` branches that have branched off from the main track when a new OTP release was introduced
- **Gray versions**: versions on branches created to resolve particular issues for specific customers based on a specific base version; these "will typically become dead ends very quickly if not immediately"

Source: "OTP Versions Tree" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **version-scheme** — the tree structure derives from the version numbering rules
- **version-ordering** — understanding total and partial ordering is necessary to read the tree
- **branched-versions** — the tree visualizes how branched versions relate to the main track
- **releases-and-patches** — the tree shows the relationship between releases and their patches

# Key Properties

1. Rooted at OTP 17.0 (when the version scheme was introduced)
2. Automatically updated when new OTP versions are released
3. The tree structure is entirely determined by the version numbers themselves
4. Green nodes: main track releases and patches
5. Blue nodes: maintenance branch versions (old `maint` branches)
6. Gray nodes: customer-specific branch versions (typically dead ends)
7. Old `maint` branches always branch off from the main track when the next OTP release is introduced
8. Available online at erlang.org

# Construction / Recognition

## To Construct/Create:
1. Start with OTP 17.0 as the root
2. Place each version number at its position determined by the version number itself
3. Normal versions (three parts) form the main track (green)
4. Maintenance branch versions form blue branches off the main track
5. Customer-specific branches form gray branches off specific base versions

## To Identify/Recognize:
1. Visit `http://www.erlang.org/download/otp_versions_tree.html`
2. Green versions are on the active main development track
3. Blue versions are on older maintenance branches still receiving patches
4. Gray versions are one-off customer fixes unlikely to receive further updates

# Context & Application

The OTP Versions Tree provides the definitive visual overview of the entire OTP release history since 17.0. It is useful for understanding which versions are on the main track versus maintenance branches, planning upgrades by seeing the full version lineage, and understanding why certain version numbers have more than three parts. The fact that the tree is fully determined by the version numbers themselves demonstrates the self-documenting nature of the OTP version scheme.

# Examples

**Example 1** (Versions section): The main track shows a sequence like `17.0` (green) -> `17.1` (green) -> `17.2` (green) -> ... -> `18.0` (green). When `18.0` was introduced, a `maint` branch was created from the `17.x` line, and subsequent `17.x` patches on that branch are shown in blue.

**Example 2** (Versions section): A gray version like `17.3.2.1` would appear as a branch off `17.3.2`, created to solve a specific customer issue. This gray branch is a dead end -- it receives no further updates.

# Relationships

## Builds Upon
- **version-scheme** — the tree structure is derived from the version scheme rules
- **branched-versions** — the tree makes branching relationships visually explicit
- **releases-and-patches** — the tree shows how patches relate to their parent releases

## Enables
- No downstream concepts -- this is a visualization tool for understanding the version landscape.

## Related
- **otp-version** — each node in the tree is an OTP version
- **otp-versions-table** — provides the underlying data that the tree visualizes

## Contrasts With
- No direct contrasts.

# Common Errors

- **Error**: Assuming blue (maintenance) versions are less stable or less important than green (main track) versions.
  **Correction**: Blue versions are actively maintained patches on older releases. They may be the most appropriate versions for production systems that cannot upgrade to the latest major release.

- **Error**: Planning to use a gray (customer-specific) version for a new deployment.
  **Correction**: Gray versions are created for specific customers and specific issues. They typically become dead ends immediately and should not be adopted for general use.

# Common Confusions

- **Confusion**: The tree requires external metadata (release dates, changelogs) to construct.
  **Clarification**: The tree structure is entirely determined by the version numbers themselves. No additional metadata is needed to build it.

# Source Reference

"OTP Versions Tree" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly described in source text)
- Confidence rationale: The source clearly describes the tree, its root, its color coding, and its derivation from version numbers
- Uncertainties: none
- Cross-reference status: verified against source text
