---
# === CORE IDENTIFICATION ===
concept: Release Handling
slug: release-handling

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Release Handling"
chapter_number: null
pdf_page: null
section: "Release Handling Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hot upgrade"
  - "live upgrade"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - release-resource-file
  - release-package
  - application
extends:
  - code-replacement
related:
  - application-upgrade-file
  - release-upgrade-file
  - release-handler
  - installing-a-release
  - release-handling-instructions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is release handling?"
  - "How do I perform a release upgrade?"
  - "What must I know before implementing release handling?"
---

# Quick Definition

Release handling is the OTP/SASL framework for upgrading and downgrading between different versions of an entire release at runtime, based on Erlang's code replacement capability.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "An important feature of the Erlang programming language is the ability to change module code at runtime, _code replacement_. [...] Based on this feature, the OTP application SASL provides a framework for upgrading and downgrading between different versions of an entire release in runtime. This is called _release handling_." The framework consists of offline support (`systools` for generating scripts and building release packages) and online support (`release_handler` for unpacking and installing release packages). The minimal system enabling release handling consists of the Kernel, STDLIB, and SASL applications.

# Prerequisites

- **Release** -- Must understand how to create and structure a release.
- **Release Resource File** -- New .rel files drive the upgrade process.
- **Release Package** -- New release packages are the deployment unit for upgrades.
- **Application** -- Understanding application structure is needed for .appup files.

# Key Properties

1. Requires the system to run as an embedded system.
2. Requires heartbeat monitoring for system reboots to work properly.
3. Uses .appup files (per-application upgrade instructions) and relup files (whole-release upgrade instructions).
4. Boot script in the release package must be generated from the same .rel file as the package itself.
5. System must be configured using a single `sys.config` file.
6. All release versions except the first must contain a `relup` file.
7. In distributed systems, the release handler is a locally registered process that must be called at each node.

# Construction / Recognition

## To Construct/Create (the 9-step workflow):
1. Create the initial release as described in the Releases chapter.
2. Transfer and install the release at the target environment.
3. Make modifications (e.g., error corrections) in the development environment.
4. Update the relevant .app files and write a new .rel file.
5. Create .appup files for each modified application.
6. Generate a relup file using `systools:make_relup/3,4`.
7. Create a new release package and transfer it to the target system.
8. Unpack the new release package using the release handler.
9. Install the new version using the release handler (evaluates relup instructions).

## To Identify/Recognize:
1. Presence of .appup files in application ebin directories.
2. Presence of a `relup` file in the release.
3. Use of `release_handler` functions (`unpack_release`, `install_release`, `make_permanent`).

# Context & Application

Release handling enables zero-downtime upgrades of production OTP systems. However, it is a complex process with many potential pitfalls. Complicated or circular dependencies between nodes, processes, or modules can make upgrades difficult. Non-affected processes continue normal execution during upgrades, which can lead to timing issues. The recommendation is to keep code changes as small as possible and always backwards compatible.

# Examples

**Example 1** (release_handling.md, "Release Handling Principles"): The release handling workflow is documented as a 9-step process, from creating the initial release through making the new version permanent. Key steps include creating .appup files (Step 5), generating the relup file (Step 6), and installing the release (Step 9).

# Relationships

## Builds Upon
- **Code Replacement** -- Release handling extends Erlang's basic code replacement capability to entire releases.
- **Release** -- A release must exist before it can be upgraded.

## Enables
- **Installing a Release** -- The release handling framework enables installing new release versions at runtime.

## Related
- **Application Upgrade File** -- .appup files define per-application upgrade instructions.
- **Release Upgrade File** -- The relup file orchestrates the entire release upgrade.
- **Release Handler** -- The SASL process that executes the upgrade.
- **Release Handling Instructions** -- The instructions used in .appup and relup files.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Not running the system as an embedded system.
  **Correction**: Release handling requires the runtime system to know which release it is running and to be able to change boot scripts and config files at runtime. This requires embedded mode.

- **Error**: Making large, non-backwards-compatible changes in a single upgrade.
  **Correction**: Change code in as small steps as possible and always keep it backwards compatible to minimize risks during the upgrade window.

# Common Confusions

- **Confusion**: Thinking release handling is the same as simply replacing module code.
  **Clarification**: Release handling orchestrates an entire release upgrade, including loading/unloading modules, starting/stopping applications, transforming process state, and potentially restarting the runtime system. Simple code replacement is just one part of this larger framework.

# Source Reference

OTP Design Principles, "Release Handling" chapter, sections "Release Handling Principles" and "Requirements" (release_handling.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "Release Handling Principles" section.
- Confidence rationale: Core concept explicitly defined with detailed workflow.
- Uncertainties: None.
- Cross-reference status: Cross-references release, application (existing cards), code-replacement, application-upgrade-file, release-upgrade-file, release-handler, installing-a-release (new cards).
