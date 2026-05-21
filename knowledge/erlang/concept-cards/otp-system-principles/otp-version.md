---
# === CORE IDENTIFICATION ===
concept: OTP Version
slug: otp-version

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
section: "OTP Version"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP release version
  - OTP version number

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - application-version
  - version-scheme
  - otp-versions-table
  - releases-and-patches
contrasts_with:
  - application-version

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP version scheme?"
  - "How does the OTP version relate to application versions?"
  - "How do I retrieve the current OTP version?"
---

# Quick Definition

An OTP version identifies a specific set of tested application versions bundled together as a coherent Erlang/OTP release. As of OTP 17, the OTP release number corresponds to the major part of the OTP version.

# Core Definition

The OTP version as a concept was introduced in OTP 17. "OTP of a specific version is a set of applications of specific versions. The application versions identified by an OTP version correspond to application versions that have been tested together by the Erlang/OTP team at Ericsson AB." While it is possible to combine applications from different OTP versions, it is "always preferred to use OTP applications from one single OTP version."

Release candidates use an `-rc<N>` suffix. The suffix `-rc0` is used during development up to the first release candidate.

Source: "OTP Version" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

Foundational concept with no prerequisites. The OTP version is the top-level identifier for an Erlang/OTP release.

# Key Properties

1. As of OTP 17, the release number equals the major part of the OTP version
2. An OTP version identifies a tested set of application versions
3. Release candidates carry an `-rc<N>` suffix
4. The `-rc0` suffix is used during development before the first release candidate
5. An OTP version identifies source code versions and implies nothing about how OTP has been built
6. Mixing application versions from different OTP versions is possible but not recommended

# Construction / Recognition

## To Construct/Create:
1. The OTP version follows the `<Major>.<Minor>.<Patch>` scheme (see version-scheme)
2. A new OTP release starts at `<Major>.0` (e.g., `17.0`, `26.0`)
3. Patches increment the minor or patch component

## To Identify/Recognize:
1. Read from `<OTP source root>/OTP_VERSION` in a source tree
2. Read from `<OTP installation root>/releases/<OTP release number>/OTP_VERSION` in an installed system
3. Construct the path via `filename:join([code:root_dir(), "OTP_VERSION"])` (source tree) or `filename:join([code:root_dir(), "releases", erlang:system_info(otp_release), "OTP_VERSION"])` (installed system)
4. A `**` suffix on the version string indicates the system was patched using `otp_patch_apply`

# Context & Application

The OTP version is the primary identifier for understanding which Erlang/OTP distribution you are running. It determines which application versions are guaranteed to work together. When deploying production systems or reporting bugs, specifying the exact OTP version is essential. No `OTP_VERSION` file is placed in a target system created by OTP tools because a target system may mix versions in ways that make the base OTP version ambiguous.

# Examples

**Example 1** (Versions section): An OTP version like `17.0` corresponds to OTP release 17. All applications bundled within that version (e.g., `kernel-3.0`, `stdlib-2.0`, `erts-6.0`) have been tested together.

**Example 2** (Versions section): Reading the OTP version from an installed system:

```erlang
filename:join([code:root_dir(), "releases",
               erlang:system_info(otp_release), "OTP_VERSION"]).
```

**Example 3** (Versions section): If the `OTP_VERSION` file reads `26.1.2**`, the `**` suffix indicates the system has been patched using `otp_patch_apply` and contains application versions from multiple OTP versions, with `26.1.2` as the base.

# Relationships

## Builds Upon
- No prerequisites — this is the foundational versioning concept for Erlang/OTP.

## Enables
- **application-version** — individual application versions are defined within the context of an OTP version
- **releases-and-patches** — OTP releases and patches are organized around OTP version numbers
- **otp-versions-table** — the `otp_versions.table` file maps OTP versions to their constituent application versions

## Related
- **version-scheme** — the rules governing how OTP version numbers are structured and incremented
- **otp-versions-tree** — the visual representation of all released OTP versions

## Contrasts With
- **application-version** — an OTP version identifies the whole release; an application version identifies a single application within that release

# Common Errors

- **Error**: Mixing applications from different OTP versions and expecting them to be compatible.
  **Correction**: Always prefer using OTP applications from a single OTP version. Mixed versions have not been tested together by the Erlang/OTP team.

- **Error**: Assuming the `OTP_VERSION` file is always present and accurate.
  **Correction**: Target systems created by OTP tools do not include an `OTP_VERSION` file. Systems patched by means other than `otp_patch_apply` may have an incorrect `OTP_VERSION` file.

# Common Confusions

- **Confusion**: The OTP version and the OTP release number are different things.
  **Clarification**: As of OTP 17, the OTP release number corresponds to the major part of the OTP version. OTP release 26 has OTP version `26.x.y`.

- **Confusion**: An OTP version describes how the system was built.
  **Clarification**: An OTP version identifies source code versions only. It implies nothing about build configuration or compilation options.

# Source Reference

"OTP Version" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined in source text)
- Confidence rationale: The source provides a clear, explicit definition of OTP version
- Uncertainties: none
- Cross-reference status: verified against source text
