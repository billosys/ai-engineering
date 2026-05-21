---
# === CORE IDENTIFICATION ===
concept: Release Upgrade
slug: release-upgrade

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-upgrades
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Creating a Release Upgrade"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - OTP release upgrade
  - live release upgrade
  - release downgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - software-upgrade
extends: []
related:
  - application-upgrade-file
  - release-upgrade-file
  - release-handler
  - code-change-callback
  - installing-an-upgrade
contrasts_with:
  - software-upgrade

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform a release upgrade?"
  - "What must I understand before performing release upgrades?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A release upgrade is the coordinated, OTP-tooled process of moving a running, deployed release from one version to another. It is built from new application versions, application upgrade files, and release resource and upgrade files.

# Core Definition

To upgrade releases using the tools and design principles provided by OTP, you start with a baseline consisting of a properly packaged and deployed OTP release (Cesarini & Vinoski, p. 343-344, pdf p. 336). A release upgrade also requires: one or more new versions of existing applications, zero or more new applications, an application upgrade (`.appup`) file for each changed application, and release resource (`.rel`) and release upgrade (`relup`) files. The new `.rel` file, the `.appup` files, and the old release's `.rel` file are used to generate the `relup` file, which contains all the commands executed during the upgrade. After installing the new code on the target, the `relup` instructions are run; if anything fails the system is restarted using the old release; if stable, the release is made permanent.

# Prerequisites

- **Release** — A release upgrade moves between releases; the release concept comes first.
- **Software upgrade** — Release upgrades build on the basic software-upgrade mechanics.

# Key Properties

1. Requires a baseline of a properly packaged, deployed OTP release.
2. Needs new application versions, optionally new applications, `.appup` files, and `.rel`/`relup` files.
3. The `relup` is generated from the new `.rel`, the old `.rel`, and the `.appup` files.
4. Installing the upgrade runs the `relup` instructions on the target.
5. If the upgrade fails, the system restarts with the old release.
6. After observation and testing, a stable release is made permanent.
7. Restarting before making the release permanent reverts to the old release.
8. Supports both upgrades and downgrades.

# Construction / Recognition

## To Perform a Release Upgrade:
1. Add new functionality, bump module and application versions, package into applications.
2. Write an `.appup` file for each changed application; place it in `ebin`.
3. Create the new `.rel` file; generate the boot file and the `relup` file.
4. Build a tar package and deploy it to the target's `releases` directory.
5. Unpack with `release_handler:unpack_release/1`, install with `install_release/1`.
6. Test; if stable call `make_permanent/1`, otherwise restart to revert.

## To Recognize It:
1. Presence of `.appup` files and a `relup` file in a release.
2. Use of `release_handler` functions on a running node.

# Context & Application

- **Typical contexts**: Deploying bug fixes and new features to a live system without downtime.
- **Common applications**: Systems requiring five-nines availability where upgrades cannot interrupt service.
- **Historical/stylistic notes**: The book notes that for clusters with redundant nodes, rolling upgrades (shut down, upgrade, restart one node at a time) are often simpler than live release upgrades.

# Examples

**Example 1** (p. 343): The coffee FSM application is upgraded from version 1.0 to 1.1, adding a new `service` state — a simple upgrade with no drivers, NIFs, new applications, or state changes.

**Example 2** (p. 344): The required steps summarized — bump versions, write `.appup` files, create the `relup`, build a package, unpack and install it, then make it permanent if stable.

# Relationships

## Builds Upon
- **Release** — A release upgrade moves between release versions.
- **Software upgrade** — It uses and coordinates the underlying software-upgrade mechanics.

## Related
- **Application upgrade file** — `.appup` files describe per-application upgrade instructions.
- **Release upgrade file** — The `relup` file holds the low-level upgrade commands.
- **Release handler** — Performs the unpack/install/make-permanent steps.
- **Code change callback** — Migrates behavior state during the upgrade.
- **Installing an upgrade** — The runtime procedure that applies a release upgrade.

## Contrasts With
- **Software upgrade** — A software upgrade replaces modules; a release upgrade coordinates whole-release transitions with OTP tooling, rollback, and permanence.

# Common Errors

- **Error**: Attempting an upgrade without a properly packaged, deployed baseline release.
  **Correction**: A release upgrade requires a baseline OTP release; the first release is usually created manually.

- **Error**: Restarting the node before making a successful upgrade permanent.
  **Correction**: Restarting before `make_permanent/1` reverts to the old release; make the release permanent once it is verified stable.

# Common Confusions

- **Confusion**: Thinking a release upgrade is the same as loading a new module.
  **Clarification**: A release upgrade is a coordinated, multi-application process with `.appup`/`relup` files, rollback, and permanence — not just module loading.

- **Confusion**: Believing live release upgrades are always the best choice.
  **Clarification**: For redundant clusters, rolling upgrades one node at a time are often simpler and safer.

# Source Reference

Chapter 11: Release Upgrades, section "Creating a Release Upgrade," pages 343-344 (pdf p. 336). See Figure 12-3 "Coffee FSM version transitions."

# Verification Notes

- Definition source: Direct adaptation of pp. 343-344.
- Confidence rationale: HIGH — the source explicitly enumerates what a release upgrade requires and the steps involved.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
