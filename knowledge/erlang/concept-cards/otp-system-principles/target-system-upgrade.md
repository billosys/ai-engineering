---
# === CORE IDENTIFICATION ===
concept: Target System Upgrade
slug: target-system-upgrade

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Creating the Next Version"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "release upgrade"
  - "target system versioning"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - target-system-creation
  - target-system-installation
  - embedded-target-system
extends: []
related:
  - simple-target-system
  - start-erl
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I upgrade a target system to a new version?"
  - "How do I create the next version of a target system?"
  - "What is the role of release_handler in target system upgrades?"
---

# Quick Definition

Upgrading a target system involves creating a new release version with updated `.rel` and `.appup` files, generating a `relup` file, packaging the new release, and using `release_handler` on the running target node to unpack, install, and make the new release permanent.

# Core Definition

As described in OTP System Principles, upgrading a target system is a multi-phase process spanning two environments: the development machine (creating the next version) and the target node (performing the upgrade). On the development side, a new `.rel` file, `.appup` files, and a `relup` file are created, then `target_system:create/1` packages everything. On the target side, `release_handler:unpack_release/1`, `release_handler:install_release/1`, and `release_handler:make_permanent/1` perform the upgrade.

# Prerequisites

- A running target system (preferably embedded with `-heart`).
- Understanding of `.rel`, `.appup`, and `relup` file formats.
- The new application versions available on the development code path.
- The old application versions available for generating the `relup`.

# Key Properties

1. **Creating the next version** requires: a new `.rel` file with updated versions, `.appup` files for changed applications, and generating a `relup` using `systools:make_relup/4`.
2. The `relup` file specifies upgrade and downgrade instructions between release versions.
3. The `path` option in `systools:make_relup/4` must point to the old application versions.
4. `target_system:create/1` automatically includes the `relup` file if present in the current directory.
5. **On the target node**, the upgrade tar file is placed in `releases/`.
6. `release_handler:unpack_release/1` extracts the new release.
7. `release_handler:install_release/1` installs and may restart the node (via `heart`) if ERTS, Kernel, STDLIB, or SASL changed.
8. After install, the new release is `current` but the old release is still `permanent`.
9. `release_handler:make_permanent/1` makes the new release permanent, ensuring it survives restarts.
10. `release_handler:which_releases/0` shows the status of all releases (current, permanent, old).

# Construction / Recognition

## To Construct/Create (new version):
1. Create a new `.rel` file (e.g., `mysystem2.rel`) with updated application versions.
2. Create `.appup` files for changed applications (e.g., `pea.appup`).
3. Start Erlang with the new application code on the path.
4. Generate the `relup`: `systools:make_relup("mysystem2", ["mysystem"], ["mysystem"], [{path, [...]}]).`
5. Create the release package: `target_system:create("mysystem2").`

## To Perform (on target):
1. Copy the new tar file to `releases/` on the target.
2. `release_handler:unpack_release("mysystem2").`
3. `release_handler:install_release(Vsn).`
4. `release_handler:make_permanent("SECOND").`

# Context & Application

Target system upgrades demonstrate OTP's support for hot code loading and release management. The upgrade process is designed for embedded target systems running with `-heart`, which enables automatic node restart when core applications change. The three-step process on the target (unpack, install, make permanent) provides a safety net: if the new release fails, the system can fall back to the old permanent release on restart. Only after confirming the new release works should it be made permanent.

# Examples

**Example 1** (Creating the Next Version section): The new `.rel` file:

```erlang
%% mysystem2.rel
{release,
 {"MYSYSTEM", "SECOND"},
 {erts, "6.0"},
 [{kernel, "3.0"},
  {stdlib, "2.0"},
  {sasl, "2.4"},
  {pea, "2.0"}]}.
```

**Example 2** (Creating the Next Version section): The `.appup` file for the changed application:

```erlang
%% pea.appup
{"2.0",
 [{"1.0",[{load_module,pea_lib}]}],
 [{"1.0",[{load_module,pea_lib}]}]}.
```

**Example 3** (Upgrading the Target System section): The three-step upgrade on the target:

```erlang
1> {ok,Vsn} = release_handler:unpack_release("mysystem2").
2> release_handler:install_release(Vsn).
{continue_after_restart,"FIRST",[]}
%% Node restarts via heart if ERTS/Kernel/STDLIB/SASL changed
3> release_handler:make_permanent("SECOND").
```

**Example 4** (Upgrading the Target System section): Checking release status after upgrade:

```erlang
3> release_handler:which_releases().
[{"MYSYSTEM","SECOND",
  ["kernel-3.0","stdlib-2.0","sasl-2.4","pea-2.0"],
  permanent},
 {"MYSYSTEM","FIRST",
  ["kernel-2.16.4","stdlib-1.19.4","sasl-2.3.4","pea-1.0"],
  old}]
```

# Relationships

## Builds Upon
- **target-system** — upgrades build on an existing target system
- **target-system-creation** — creating the next version uses the same `target_system:create/1` process
- **embedded-target-system** — upgrades are designed to work with embedded systems using `-heart`

## Enables
- No further concepts in this source; enables continued system evolution.

## Related
- **simple-target-system** — must have `releases/RELEASES` for `release_handler` to work
- **start-erl** — reads `new_start_erl.data` after upgrade to boot the new version

## Contrasts With
- No direct contrasts in source; implicitly contrasts with a full system reinstallation approach.

# Common Errors

- **Error**: Forgetting to make the new release permanent after confirming it works.
  **Correction**: Call `release_handler:make_permanent/1` after verifying the upgrade. Without this, a restart will revert to the old permanent release.

- **Error**: Not including the old application paths when generating the `relup`.
  **Correction**: Use the `path` option in `systools:make_relup/4` to point to the old application `ebin` directories.

- **Error**: Running the upgrade without `-heart` when ERTS, Kernel, STDLIB, or SASL have changed.
  **Correction**: Use `-heart` in the `bin/start` script so the node can automatically restart during such upgrades.

# Common Confusions

- **Confusion**: Thinking `install_release` makes the release permanent.
  **Clarification**: After `install_release`, the new release is `current` but the old is still `permanent`. If the node restarts before `make_permanent`, it reverts to the old release. This is a safety feature.

- **Confusion**: Thinking the `relup` file is created by `target_system:create/1`.
  **Clarification**: The `relup` must be generated separately with `systools:make_relup/4` before calling `target_system:create/1`. The create function only includes it if it already exists.

# Source Reference

"Creating the Next Version" and "Upgrading the Target System" sections, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text, synthesized across two sections.
- Confidence rationale: High — detailed step-by-step procedures with concrete examples.
- Uncertainties: None.
- Cross-reference status: References target-system, target-system-creation, embedded-target-system, simple-target-system, start-erl.
