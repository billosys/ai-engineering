---
# === CORE IDENTIFICATION ===
concept: Release Metadata File
slug: rel-file

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
  - .rel file
  - release file
  - release resource file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-release
  - application-metadata-file
extends: []
related:
  - boot-script
  - erts-version
contrasts_with:
  - application-metadata-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a .rel file?"
  - "What does the release metadata file contain?"
  - "What are the four elements of the .rel tuple?"
---

# Quick Definition

The `.rel` file is the release metadata file: a single Erlang tuple naming the release, its version, the required ERTS version, and the list of applications and versions it includes.

# Core Definition

Just as you need a `.app` file for each application, you need a *release file* with the extension `.rel` containing the metadata for each release. The metadata consists mainly of a list of the applications the release is made up of, plus the version of the Erlang Run-Time System (ERTS) the applications should run under. The `.rel` file contains a single Erlang tuple terminated by a period, with four elements: the atom `release`; a `{Name, Version}` pair (name as a string, not an atom); an `{erts, Version}` pair; and a list of `{App, Version}` pairs for the included applications. It is a high-level specification — the runtime system cannot read it directly at boot time ("Erlang and OTP in Action," Ch. 10, Section 10.2.3).

# Prerequisites

- **Erlang release** — The `.rel` file describes a release.
- **Application metadata file** — The application versions in the `.rel` file must match those declared in each application's `.app` file.

# Key Properties

1. A single Erlang tuple terminated by a period.
2. First element: the atom `release`.
3. Second element: a `{Name, Version}` pair; the name is a string, the version a conventional version string.
4. Third element: an `{erts, Version}` pair specifying the required ERTS version.
5. Fourth element: a complete list of `{App, Version}` pairs — all applications including all direct and indirect dependencies.
6. It is only a high-level specification; it does not point to an ERTS executable or give application locations, so it cannot start a system on its own.

# Construction / Recognition

## To Construct/Create:
1. Create a file `Name.rel`.
2. Write a tuple: `{release, {Name, Vsn}, {erts, ErtsVsn}, [AppVersionPairs]}`.
3. Ensure application versions match the `.app` files; set the `erts` version to your installed ERTS.
4. Place it where release-related files live (e.g., the `lib` directory during development).

## To Identify/Recognize:
1. A file with extension `.rel` whose single tuple starts with the atom `release`.

# Context & Application

- **Typical contexts**: The starting point for creating a release.
- **Common applications**: Input to `systools:make_script/2` and `systools:make_tar/2`.
- **Historical/stylistic notes**: You may keep several `.rel` files (different names) to build different release packages from one code base. The easiest way to find dependency versions is to run `make_script` and read its reports.

# Examples

**Example 1** (Listing 10.2): `simple_cache.rel` contains `{release, {"simple_cache", "0.1.0"}, {erts, "5.7.2"}, [{kernel, "2.13.2"}, {stdlib, "1.16.2"}, {sasl, "2.1.5.3"}, {mnesia, "4.4.10"}, {resource_discovery, "0.1.0"}, {simple_cache, "0.3.0"}]}`.

# Relationships

## Builds Upon
- **Erlang release** — The `.rel` file is the metadata definition of a release.

## Enables
- **Boot script** — The `.rel` file is used to generate the `.script` and `.boot` files.

## Related
- **ERTS version** — The `.rel` file pins the required ERTS version.

## Contrasts With
- **Application metadata file** — `.app` describes one application; `.rel` describes a whole release.

# Common Errors

- **Error**: Using an atom for the release name instead of a string.
  **Correction**: The release name in the `.rel` tuple must be a string.

- **Error**: Setting an `erts` version that does not match the installed runtime.
  **Correction**: Update the `erts` entry to match your installed ERTS (visible in the `erl` startup banner).

# Common Confusions

- **Confusion**: Thinking the runtime can boot directly from the `.rel` file.
  **Clarification**: The `.rel` file is only a high-level spec; it must be processed into `.script`/`.boot` files first.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.2.3 "The release metadata file." See Listing 10.2 (`simple_cache.rel`).

# Verification Notes

- Definition source: Direct adaptation of Section 10.2.3 and Listing 10.2.
- Confidence rationale: HIGH — the book explicitly describes the `.rel` file structure element by element.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
