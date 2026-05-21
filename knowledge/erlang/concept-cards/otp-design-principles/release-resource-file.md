---
# === CORE IDENTIFICATION ===
concept: Release Resource File
slug: release-resource-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Releases"
chapter_number: null
pdf_page: null
section: "Release Resource File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".rel file"
  - "rel file"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - release
extends: []
related:
  - boot-script
  - release-package
  - application-upgrade-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do .app files relate to .rel files in a release?"
  - "What is a release resource file?"
  - "How do I create a release?"
---

# Quick Definition

A release resource file (.rel file) defines a release by specifying its name, version, the ERTS version it runs on, and the list of applications with their versions that comprise the release.

# Core Definition

According to the OTP Design Principles "Releases" chapter: "To define a release, create a _release resource file_, or in short a `.rel` file. In the file, specify the name and version of the release, which ERTS version it is based on, and which applications it consists of." The .rel file has the format `{release, {Name,Vsn}, {erts, EVsn}, [{Application1, AppVsn1}, ..., {ApplicationN, AppVsnN}]}.` and must be named `Rel.rel`, where `Rel` is a unique name.

# Prerequisites

- **Application** -- Each application listed in the .rel file must have a corresponding .app file.
- **Release** -- Understanding the release concept is necessary to understand the role of the .rel file.

# Key Properties

1. Specifies the release name and version as strings.
2. Specifies the ERTS version the release is based on.
3. Lists all applications (as atoms) and their versions (as strings).
4. Must include at minimum the Kernel and STDLIB applications.
5. Must include SASL if the release is to be upgraded.
6. The file must be named `Rel.rel` where `Rel` is a unique identifier.
7. Used as input to `systools:make_script/1,2` and `systools:make_tar/1,2`.

# Construction / Recognition

## To Construct/Create:
1. Choose a unique release name and version string.
2. Determine the target ERTS version.
3. List all applications the release depends on, including Kernel, STDLIB, and optionally SASL.
4. Include each application name (atom) paired with its version string.
5. Save as `RelName.rel`.

## To Identify/Recognize:
1. A file with the `.rel` extension.
2. Contains a tuple starting with the atom `release`.
3. Contains nested tuples for the release identity, ERTS version, and application list.

# Context & Application

The .rel file is the central artifact that defines what constitutes a release. It serves as the input for both boot script generation (`systools:make_script`) and release package creation (`systools:make_tar`). The `systools` functions read both the .rel file and corresponding .app files to perform syntax and dependency checks. When a new release version is created for an upgrade, a new .rel file must be written with updated version numbers.

# Examples

**Example 1** (release_structure.md, "Release Resource File"): Given a `ch_app` application with this .app file:

```erlang
{application, ch_app,
 [{description, "Channel allocator"},
  {vsn, "1"},
  {modules, [ch_app, ch_sup, ch3]},
  {registered, [ch3]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {ch_app,[]}}
 ]}.
```

The corresponding .rel file `ch_rel-1.rel` is:

```erlang
{release,
 {"ch_rel", "A"},
 {erts, "14.2.5"},
 [{kernel, "9.2.4"},
  {stdlib, "5.2.3"},
  {sasl, "4.2.1"},
  {ch_app, "1"}]
}.
```

The .rel file must include `kernel`, `stdlib`, and `sasl` because `ch_app` declares them as dependencies in its .app file.

# Relationships

## Builds Upon
- **Application** -- Each entry in the .rel file corresponds to an application defined by a .app file.

## Enables
- **Boot Script** -- The .rel file is the primary input for generating boot scripts.
- **Release Package** -- The .rel file is the primary input for creating release packages.

## Related
- **Application Upgrade File** -- When upgrading, .appup files work alongside .rel files to define the upgrade path.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Omitting dependent applications from the .rel file.
  **Correction**: Every application listed in the `applications` key of any included .app file must itself be listed in the .rel file. `systools:make_script` will catch missing dependencies.

- **Error**: Using incorrect version strings that do not match .app files.
  **Correction**: The version strings in the .rel file must exactly match the `vsn` field in the corresponding .app files.

# Common Confusions

- **Confusion**: Confusing the .rel file with the .app file.
  **Clarification**: The .app file defines a single application (its modules, dependencies, start function). The .rel file defines an entire release by listing which applications and versions compose the complete system.

# Source Reference

OTP Design Principles, "Releases" chapter, section "Release Resource File" (release_structure.md).

# Verification Notes

- Definition source: Directly quoted from release_structure.md "Release Resource File" section.
- Confidence rationale: Explicitly defined concept with exact syntax specification and examples.
- Uncertainties: None.
- Cross-reference status: Cross-references application (existing card), release, boot-script, release-package, application-upgrade-file (new cards).
