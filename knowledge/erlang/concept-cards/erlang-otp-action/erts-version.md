---
# === CORE IDENTIFICATION ===
concept: ERTS Version
slug: erts-version

# === CLASSIFICATION ===
category: applications-releases
subcategory: metadata
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.2.3. The release metadata file"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang Run-Time System version"
  - "erts version"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rel-file
extends: []
related:
  - erlang-release
  - release-package
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the ERTS version?"
  - "How does the ERTS version differ from the Erlang/OTP release number?"
  - "How do you find the ERTS version of your installation?"
---

# Quick Definition

The ERTS version identifies the Erlang Run-Time System the release's applications were compiled for; it is distinct from the Erlang/OTP distribution number such as R13B03.

# Core Definition

A `.rel` file specifies the version of the Erlang Run-Time System (ERTS) that the release's applications should run under, to ensure the version on which the applications run is the version they were compiled for. The ERTS version is given as an `{erts, Version}` pair where the version is a string. The ERTS version is *not* the same as the version of the Erlang/OTP distribution (for example, R13B03) — it is a separate internal version number such as 5.7.4 ("Erlang and OTP in Action," Ch. 10, Section 10.2.3).

# Prerequisites

- **.rel file** — The ERTS version is one of the four elements of the `.rel` tuple.

# Key Properties

1. Given as a string in an `{erts, Version}` pair in the `.rel` file.
2. Distinct from the Erlang/OTP distribution name (e.g., R13B03 vs ERTS 5.7.4).
3. Shown in the `erl` startup banner, e.g. `Erlang R13B03 (erts-5.7.4)`.
4. Also obtainable via the BREAK menu's `v` (version) option.
5. Ensures applications run under the runtime version they were compiled against.

# Construction / Recognition

## To Construct/Create:
1. Start `erl` and read the ERTS version from the banner, or use the BREAK menu `v` option.
2. Put that value into the `{erts, Version}` entry of the `.rel` file.

## To Identify/Recognize:
1. Look for `erts-<version>` in the `erl` startup banner.

# Context & Application

- **Typical contexts**: Pinning the runtime version in a release definition.
- **Common applications**: When ERTS is bundled into a release package, the package directory is named `erts-<version>`.
- **Historical/stylistic notes**: If the `.rel` ERTS version does not match the local system, `systools:make_script` reports version errors.

# Examples

**Example 1** (Section 10.2.3): The `erl` banner `Erlang R13B03 (erts-5.7.4)` shows distribution R13B03 and ERTS version 5.7.4.

**Example 2** (Section 10.2.3): The BREAK menu's `v` option prints `Erlang (BEAM) emulator version 5.7.4`.

# Relationships

## Builds Upon
- **.rel file** — The ERTS version is declared inside the `.rel` tuple.

## Enables
- **Release package** — A bundled ERTS appears as the `erts-<version>` directory in the package.

## Related
- **Erlang release** — Pinning ERTS guarantees a release runs on the runtime it was built for.

# Common Errors

- **Error**: Putting the Erlang/OTP distribution name (R13B03) where the ERTS version is expected.
  **Correction**: Use the ERTS version number (e.g., 5.7.4), not the distribution name.

# Common Confusions

- **Confusion**: Treating "R13B03" and "5.7.4" as the same version.
  **Clarification**: They are different version schemes — R13B03 names the distribution; 5.7.4 names the ERTS within it.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.2.3 "The release metadata file."

# Verification Notes

- Definition source: Direct adaptation of Section 10.2.3.
- Confidence rationale: HIGH — the book explicitly distinguishes ERTS version from distribution version.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
