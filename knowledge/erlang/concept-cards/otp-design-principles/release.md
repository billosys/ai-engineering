---
# === CORE IDENTIFICATION ===
concept: Release
slug: release

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
section: "Release Concept"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OTP release"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
extends: []
related:
  - release-resource-file
  - boot-script
  - release-package
  - release-directory-structure
  - release-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release in OTP?"
  - "How do I create a release?"
  - "What must I know before creating a release?"
---

# Quick Definition

A release is a complete system consisting of one or more user-developed OTP applications together with a subset of the Erlang/OTP applications, packaged for deployment.

# Core Definition

According to the OTP Design Principles "Releases" chapter: "When you have written one or more applications, you might want to create a complete system with these applications and a subset of the Erlang/OTP applications. This is called a _release_." A release is defined by a release resource file (.rel) that specifies the included applications, and is used to generate boot scripts and release packages. A system transferred to and installed at another site is called a _target system_.

# Prerequisites

- **Application** -- A release is composed of one or more OTP applications; understanding the application structure and .app files is essential.

# Key Properties

1. A release is defined by a release resource file (.rel file).
2. The minimal release must include at least the Kernel and STDLIB applications.
3. If the release is to be upgraded, it must also include the SASL application.
4. The .rel file is used to generate boot scripts and release packages.
5. A release creates a self-contained, deployable system.

# Construction / Recognition

## To Construct/Create:
1. Write the application code and create .app files for each application.
2. Create a release resource file (.rel) specifying the release name, version, ERTS version, and all included applications with their versions.
3. Generate boot scripts using `systools:make_script/1,2`.
4. Create a release package using `systools:make_tar/1,2`.

## To Identify/Recognize:
1. A .rel file defining name, version, ERTS version, and application list.
2. Generated boot scripts (.script and .boot files).
3. A release package (.tar.gz file) containing all application code and boot scripts.

# Context & Application

Releases are the standard mechanism for packaging and deploying OTP-based systems. They enable a complete system to be transferred to a target environment, started via a boot script, and upgraded or downgraded using the release handling framework. Every production OTP deployment should be structured as a release.

# Examples

**Example 1** (release_structure.md, "Release Resource File"): The `ch_rel-1.rel` file for the channel allocator application:

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

Starting the system with this release's boot script automatically loads and starts all listed applications:

```text
% erl -boot ch_rel-1
```

# Relationships

## Builds Upon
- **Application** -- A release is composed of one or more applications, each defined by a .app file.

## Enables
- **Release Handling** -- Once a release exists, upgrades and downgrades between release versions can be performed at runtime.
- **Boot Script** -- A release resource file is used to generate boot scripts.
- **Release Package** -- A release resource file is used to create release packages for deployment.

## Related
- **Release Resource File** -- The .rel file that defines the release.
- **Release Directory Structure** -- The standard directory layout for an installed release.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Forgetting to include the SASL application in the release.
  **Correction**: If the release will ever need to be upgraded, SASL must be included in the .rel file. The minimal upgradable release requires Kernel, STDLIB, and SASL.

- **Error**: Not including all dependency applications in the .rel file.
  **Correction**: All applications listed in the `applications` key of each .app file must also appear in the .rel file. The `systools:make_script` function checks dependencies automatically.

# Common Confusions

- **Confusion**: Conflating a release with an application.
  **Clarification**: An application is a single functional component. A release is a complete system that bundles multiple applications together with a boot script for deployment.

# Source Reference

OTP Design Principles, "Releases" chapter, sections "Release Concept" and "Release Resource File" (release_structure.md).

# Verification Notes

- Definition source: Directly quoted from the "Release Concept" section of release_structure.md.
- Confidence rationale: The concept is explicitly defined with a clear definition and examples.
- Uncertainties: None.
- Cross-reference status: Cross-references application (existing card), release-resource-file, boot-script, release-package, release-handling (new cards).
