---
# === CORE IDENTIFICATION ===
concept: Release Handler
slug: release-handler

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
section: "Installing a Release"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "release_handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - release-package
  - release-upgrade-file
extends: []
related:
  - installing-a-release
  - release-directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the release handler?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

The release handler is a SASL application process that manages the unpacking, installation, permanence, and removal of release packages on a target system.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "To install the new version of the release in runtime, the _release handler_ is used. This is a process belonging to the SASL application, which handles unpacking, installation, and removal of release packages. The `release_handler` module communicates with this process." The release handler provides the online support portion of the release handling framework, complementing the offline support provided by `systools`. In distributed systems, the release handler is a locally registered process that must be called at each node where an upgrade or downgrade is needed.

# Prerequisites

- **Release Handling** -- The release handler is the runtime component of release handling.
- **Release Package** -- The release handler operates on release packages.
- **Release Upgrade File** -- The release handler evaluates relup instructions.

# Key Properties

1. A process belonging to the SASL application.
2. Communicates through the `release_handler` module API.
3. Four key operations: `unpack_release`, `install_release`, `make_permanent`, `remove_release`.
4. Evaluates relup instructions step by step during installation.
5. If installation fails, the system can be rebooted to the old version.
6. If installation succeeds, the new version must be made permanent explicitly.
7. Locally registered process -- in distributed systems, must be called on each node.
8. Tracks release version status (old, current, permanent) in `$ROOT/releases/RELEASES` and `$ROOT/releases/start_erl.data`.

# Construction / Recognition

## To Construct/Create:
1. The release handler is automatically started as part of the SASL application.
2. No manual construction is needed.

## To Identify/Recognize:
1. Accessed through the `release_handler` module API.
2. Part of the SASL application's process tree.
3. Its state is persisted in `$ROOT/releases/RELEASES` and `$ROOT/releases/start_erl.data`.

# Context & Application

The release handler is the primary interface for deploying upgrades on running OTP systems. It manages the full lifecycle of a release version: unpacking the package, installing it (evaluating relup instructions), making it permanent (so it survives reboots), and eventually removing old versions. Understanding the release handler's state machine (unpacked -> installed -> permanent) is essential for production operations.

# Examples

**Example 1** (release_handling.md, "Installing a Release"): The complete upgrade sequence using the release handler:

```erlang
%% Unpack the new release package
1> release_handler:unpack_release("ch_rel-2").
{ok,"B"}

%% Install the new version (evaluates relup instructions)
3> release_handler:install_release("B").
{ok,"A",[]}

%% Make the new version permanent
7> release_handler:make_permanent("B").
ok
```

# Relationships

## Builds Upon
- **Release Handling** -- The release handler implements the runtime portion of release handling.
- **Release Upgrade File** -- The release handler evaluates the instructions in the relup.

## Enables
- **Installing a Release** -- The release handler is the mechanism for installing releases.

## Related
- **Release Directory Structure** -- The release handler creates and manages the directory structure.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Forgetting to make a successfully installed release permanent.
  **Correction**: After verifying the new version works correctly, call `release_handler:make_permanent(Vsn)`. Otherwise, a system reboot will revert to the previous version.

- **Error**: Assuming the release handler synchronizes across distributed nodes automatically.
  **Correction**: The release handler is a locally registered process. In distributed systems, it must be called at each node individually. Use the `sync_nodes` instruction for coordination.

# Common Confusions

- **Confusion**: Thinking installation and permanence are the same thing.
  **Clarification**: Installation makes the new version active but not default. If the system reboots after installation but before permanence, it reverts to the previous permanent version. Making it permanent sets it as the default for future reboots.

# Source Reference

OTP Design Principles, "Release Handling" chapter, sections "Installing a Release" and "Distributed Systems" (release_handling.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "Installing a Release" section.
- Confidence rationale: Explicitly defined with clear API examples.
- Uncertainties: None.
- Cross-reference status: Cross-references release-handling, release-package, release-upgrade-file, installing-a-release, release-directory-structure (new cards).
