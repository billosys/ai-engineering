---
# === CORE IDENTIFICATION ===
concept: Release Handler
slug: release-handler

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
section: "The Release Handler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - release_handler
  - release handler process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
extends: []
related:
  - installing-an-upgrade
  - releases-file
  - release-upgrade-file
  - target-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the release handler?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

The release handler is the SASL process responsible for unpacking, installing, upgrading, removing, and making permanent releases locally on each node. It moves each release through the unpacked, current, permanent, and old states.

# Core Definition

The release handler is part of the SASL application — one of the core OTP applications that must be in every release because it contains tools required to build, install, and upgrade the release itself (Cesarini & Vinoski, p. 345-349, pdf p. 336). It is the process responsible for unpacking, installing, and upgrading releases locally on each node, as well as removing them and making them permanent. The release handler assumes a release tar file created with `systools:make_tar/1,2` and placed in the `releases` directory. Each release version can be in one of four states — *unpacked*, *current*, *permanent*, or *old* — and state transitions occur when `release_handler` functions are called.

# Prerequisites

- **Release upgrade** — The release handler performs upgrade steps; the release-upgrade concept comes first.

# Key Properties

1. A process in the SASL application's supervision tree.
2. Manages releases through four states: unpacked, current, permanent, old.
3. At any time there is always a release that is either current or permanent.
4. `create_RELEASES/4` — creates the first `RELEASES` file.
5. `unpack_release/1` — unpacks `Name.tar.gz` from `releases`, adding applications to `lib`.
6. `install_release/1,2` — triggers the upgrade/downgrade by executing the `relup`.
7. `check_install_release/1,2` — validates an install before the point of no return.
8. `make_permanent/1` — makes the upgraded release the one used on reboot.
9. `remove_release/1` — deletes old applications and release files no longer in use.
10. `reboot_old_release/1` — reverts to an old (not removed) release.
11. `which_releases/0,1` — returns all releases and their states.
12. Intended to work with embedded target systems.

# Construction / Recognition

## To Use the Release Handler:
1. Place the upgrade tar in the target's `releases` directory.
2. Call `release_handler:unpack_release("Name")`.
3. Call `release_handler:install_release("Vsn")` to apply the `relup`.
4. Test; if stable call `release_handler:make_permanent("Vsn")`.
5. Optionally call `remove_release/1` for old releases or `reboot_old_release/1` to revert.

## To Recognize It:
1. The `release_handler` process in the SASL supervision tree.
2. Calls of the form `release_handler:*` on a running node.

# Context & Application

- **Typical contexts**: Performing live release upgrades on embedded target systems.
- **Common applications**: Unpacking, installing, validating, and making releases permanent; removing or reverting releases.
- **Historical/stylistic notes**: The release handler also exports functions to upgrade/downgrade single applications, meant for testing, not production (changes are not persistent across restarts).

# Examples

**Example 1** (p. 343-344): A full upgrade sequence on the running coffee node:

```erlang
1> release_handler:unpack_release("coffee-1.1").
{ok, "1.1"}
6> release_handler:install_release("1.1").
{ok,"1.0",[]}
3> release_handler:make_permanent("1.1").
ok
4> release_handler:remove_release("1.0").
ok
```

**Example 2** (p. 346): `release_handler:create_RELEASES(RootDir, Releases, RelFile, [])` creates the first `RELEASES` file before any upgrade.

# Relationships

## Builds Upon
- **Release upgrade** — The release handler executes the release-upgrade workflow.

## Related
- **Installing an upgrade** — The runtime procedure the release handler drives.
- **RELEASES file** — The release handler's persistent state.
- **Release upgrade file** — `install_release/1` executes the `relup`.
- **Target system** — The release handler is intended for embedded target systems.

# Common Errors

- **Error**: Using the release handler with a simple target system.
  **Correction**: The release handler is intended for embedded target systems; with simple systems you must manage the correct boot and config files yourself on restart.

- **Error**: Using the single-application upgrade functions in production.
  **Correction**: Those functions are for testing only — their changes are not persistent across system restarts.

# Common Confusions

- **Confusion**: Thinking the release handler builds the release.
  **Clarification**: It unpacks, installs, upgrades, removes, and makes releases permanent; the release tar is built beforehand with `systools:make_tar`.

- **Confusion**: Believing the release handler is needed for the first installation.
  **Clarification**: For the first target installation it matters only if Erlang is already installed on the target; the first release is often built manually.

# Source Reference

Chapter 11: Release Upgrades, section "The Release Handler," pages 345-349 (pdf p. 336). See Figure 12-4 "The release handler process" and Figure 12-5 "Managing a release."

# Verification Notes

- Definition source: Direct adaptation of pp. 345-349.
- Confidence rationale: HIGH — the source explicitly describes the release handler and each of its functions.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
