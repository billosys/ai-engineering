---
# === CORE IDENTIFICATION ===
concept: OTP Versions Table
slug: otp-versions-table

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
section: "OTP Versions Table"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - otp_versions.table
  - OTP versions file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-version
  - application-version
extends: []
related:
  - version-scheme
  - releases-and-patches
  - otp-versions-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the OTP version relate to application versions?"
  - "How do I determine which OTP version includes a specific application version?"
---

# Quick Definition

The `otp_versions.table` file is a text file in the OTP source tree that maps every OTP version (from 17.0 onward) to its constituent application versions, distinguishing changed from unchanged applications in each release.

# Core Definition

"The text file `<OTP source root>/otp_versions.table`, which is part of the source code, contains information about all OTP versions from OTP 17.0 up to the current OTP version." Each line has the following format:

```text
<OtpVersion> : <ChangedAppVersions> # <UnchangedAppVersions> :
```

Where:

- `<OtpVersion>` has the format `OTP-<VSN>`, matching the git tag used to identify the source
- `<ChangedAppVersions>` and `<UnchangedAppVersions>` are space-separated lists in the format `<application>-<vsn>`
- `<ChangedAppVersions>` corresponds to "changed applications with new version numbers in this OTP version"
- `<UnchangedAppVersions>` corresponds to "unchanged application versions in this OTP version"

"Both of them can be empty, but not at the same time. If `<ChangedAppVersions>` is empty, no changes have been made that change the build result of any application." All whitespace in the file is either space (character 32) or line-break (character 10). "The order of lines is undefined."

Source: "OTP Versions Table" subsection of "OTP Version" section, "Versions" chapter, OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **otp-version** — the table maps OTP versions to their contents
- **application-version** — the table entries list application versions in `<application>-<vsn>` format

# Key Properties

1. Located at `<OTP source root>/otp_versions.table`
2. Covers all OTP versions from 17.0 to the current version
3. Each line maps one OTP version to its application versions
4. Distinguishes changed applications (before `#`) from unchanged (after `#`)
5. OTP version format is `OTP-<VSN>`, matching git tags
6. Application version format is `<application>-<vsn>`
7. Either changed or unchanged list can be empty, but not both simultaneously
8. Empty changed list means no application build results changed (e.g., build system fix only)
9. Line order is undefined
10. Only uses space (char 32) and line-break (char 10) as whitespace

# Construction / Recognition

## To Construct/Create:
1. File is maintained as part of the OTP source code (not user-created)
2. Each line follows the format: `OTP-<VSN> : <changed> # <unchanged> :`

## To Identify/Recognize:
1. Located at the root of the OTP source tree as `otp_versions.table`
2. Each line starts with `OTP-` followed by a version number
3. Lines contain `:` and `#` delimiters separating the three fields

# Context & Application

The `otp_versions.table` file is the definitive machine-readable reference for determining which application versions belong to which OTP version. It is invaluable for answering questions like "which OTP versions contain a specific application version?" or "when was a particular application version introduced?" The file is designed to be queried with standard UNIX text-processing tools like `grep` and `sed`.

# Examples

**Example 1** (Versions section): Finding which OTP versions include `kernel-3.0`:

```bash
$ grep ' kernel-3\.0 ' otp_versions.table
```

**Example 2** (Versions section): Finding in which OTP version `kernel-3.0` was introduced (filtering out lines where it appears only as unchanged):

```bash
$ sed 's/#.*//;/ kernel-3\.0 /!d' otp_versions.table
```

The `sed` command first removes everything after `#` (the unchanged applications), then deletes lines that do not contain ` kernel-3.0 `. This leaves only lines where `kernel-3.0` appears in the changed applications list, showing when it was first introduced.

**Example 3** (Versions section): A line in the file might look like:

```text
OTP-17.0 : erts-6.0 kernel-3.0 stdlib-2.0 # compiler-5.0 crypto-3.3 :
```

This indicates that in OTP 17.0, `erts`, `kernel`, and `stdlib` had new versions, while `compiler` and `crypto` were unchanged.

# Relationships

## Builds Upon
- **otp-version** — each line in the table is keyed by an OTP version
- **application-version** — each line lists application versions as its values

## Enables
- No downstream concepts -- this is a reference and query tool.

## Related
- **version-scheme** — the version numbers in the table follow the OTP version scheme
- **releases-and-patches** — the table records which applications changed in each release or patch
- **otp-versions-tree** — the tree and the table are complementary views of the same version data

## Contrasts With
- No direct contrasts.

# Common Errors

- **Error**: Assuming the lines in `otp_versions.table` are in chronological or version order.
  **Correction**: The order of lines is explicitly undefined. Do not rely on line position to infer version ordering.

- **Error**: Searching for an application version without proper escaping in grep/sed patterns.
  **Correction**: Use escaped dots (`\.`) and space-delimited patterns (e.g., `' kernel-3\.0 '`) to avoid matching unintended versions like `kernel-3.0.1`.

# Common Confusions

- **Confusion**: An empty `<ChangedAppVersions>` section means the OTP version is identical to the previous one.
  **Clarification**: An empty changed list means no application build results changed, but there may have been changes (e.g., to the build system) that warranted a new OTP version.

- **Confusion**: The `otp_versions.table` file is generated or derived from git tags.
  **Clarification**: The file is part of the source code and is maintained alongside it. The `OTP-<VSN>` format matches git tags, but the file itself is a source artifact.

# Source Reference

"OTP Versions Table" subsection of "OTP Version" section, "Versions" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly defined with format specification and examples)
- Confidence rationale: The source provides the exact file format, location, and usage examples
- Uncertainties: none
- Cross-reference status: verified against source text
