---
# === CORE IDENTIFICATION ===
concept: Installing an Upgrade
slug: installing-an-upgrade

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
section: "Installing an Upgrade"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - making a release permanent
  - install_release
  - unpack_release
  - release states

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handler
  - release-upgrade
extends: []
related:
  - releases-file
  - release-upgrade-file
  - init-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install and make a release upgrade permanent?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Installing an upgrade is the runtime procedure of unpacking a release, executing its `relup` to apply the upgrade, and — once verified stable — making it permanent. If installation fails or the node restarts before being made permanent, the old release is restored.

# Core Definition

To install an upgrade you place the upgrade tar in the target's `releases` directory and use `release_handler:unpack_release/1` to uncompress it (adding the new application to `lib` and a new version directory under `releases`); then `release_handler:install_release/1` triggers the software upgrade or downgrade by executing the `relup` instructions (Cesarini & Vinoski, p. 343-345, pdf p. 336). If issues arise and a restart is triggered, the system reboots and reverts to the old version. If the system is stable, the current (new) version is made permanent by calling `release_handler:make_permanent/1`. Because a release that is not made permanent reverts on restart, making it permanent is the step that commits the upgrade.

# Prerequisites

- **Release handler** — The install procedure is driven by `release_handler` functions; that concept comes first.
- **Release upgrade** — Installing is the runtime step of a release upgrade.

# Key Properties

1. The upgrade tar is placed in the target's `releases` directory.
2. `unpack_release/1` uncompresses it, adds the application to `lib`, and creates a version directory under `releases`.
3. `install_release/1` executes the `relup` instructions, applying the upgrade or downgrade.
4. If installation fails unrecoverably, the node restarts/reboots with the old release.
5. A successful install makes the new release *current* but not yet *permanent*.
6. `make_permanent/1` commits the upgrade — the new release is used on subsequent restarts.
7. Restarting (e.g. `init:restart/0`) before making the release permanent reverts to the old version.
8. `remove_release/1` deletes files specific to releases no longer needed.
9. The `RELEASES` file must exist (created by `create_RELEASES/4`) for downgrades after an upgrade is made permanent.

# Construction / Recognition

## To Install an Upgrade:
1. Place `Name.tar.gz` in the target's `releases` directory.
2. `release_handler:unpack_release("Name")`.
3. `release_handler:install_release("Vsn")` to execute the `relup`.
4. Test the upgraded system with diagnostic checks.
5. If stable, `release_handler:make_permanent("Vsn")`; otherwise restart to revert.
6. Optionally `release_handler:remove_release/1` to clean up old releases.

## To Recognize the State:
1. `release_handler:which_releases()` reports each release as unpacked, current, permanent, or old.

# Context & Application

- **Typical contexts**: Applying a release upgrade to a live embedded target system.
- **Common applications**: Live bug-fix and feature deployment with rollback safety.
- **Historical/stylistic notes**: Reverting to an old version after removal requires reinstalling it — recreating its `.appup`, `relup`, and tar file.

# Examples

**Example 1** (p. 343): Unpacking and confirming coexistence:

```erlang
1> release_handler:unpack_release("coffee-1.1").
{ok, "1.1"}
2> release_handler:which_releases().
[{"coffee","1.1",[...],unpacked},
 {"coffee","1.0",[...],permanent}]
```

**Example 2** (p. 344): Installing without making permanent, then `init:restart()` reverts the node to version 1.0; reinstalling and `make_permanent("1.1")` commits it; `remove_release("1.0")` then deletes the old release.

# Relationships

## Builds Upon
- **Release handler** — The install procedure is implemented by `release_handler` functions.
- **Release upgrade** — Installing is the runtime application step of a release upgrade.

## Related
- **RELEASES file** — Tracks installed releases; required for downgrades.
- **Release upgrade file** — `install_release/1` executes the `relup`.
- **Init module** — `init:restart/0` reverts a non-permanent upgrade.

# Common Errors

- **Error**: Restarting the node before making a successful upgrade permanent.
  **Correction**: A restart reverts to the old release; call `make_permanent/1` once the upgrade is verified stable.

- **Error**: Removing the old release before confirming the new one works.
  **Correction**: Keep the old release until the new one is permanent and proven; reverting after removal requires a full reinstall.

# Common Confusions

- **Confusion**: Thinking a successful install commits the upgrade.
  **Clarification**: A successful install makes the release current, not permanent; only `make_permanent/1` commits it.

- **Confusion**: Believing `unpack_release` applies the upgrade.
  **Clarification**: `unpack_release` only uncompresses and stages the release; `install_release` executes the `relup`.

# Source Reference

Chapter 11: Release Upgrades, section "Installing an Upgrade," pages 343-345 (pdf p. 336). See Figure 12-6 "Upgrading a release."

# Verification Notes

- Definition source: Direct adaptation of pp. 343-345.
- Confidence rationale: HIGH — the source walks through the install/make-permanent procedure with shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
