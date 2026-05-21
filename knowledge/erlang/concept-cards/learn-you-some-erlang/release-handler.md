---
concept: release_handler Module
slug: release-handler
category: production-ops
subcategory: code-upgrades
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Leveling Up in the Process Quest"
chapter_number: 22
pdf_page: null
section: "Upgrading the Release"
extraction_confidence: high
aliases:
  - "release_handler"
  - "release handler"
prerequisites:
  - relup
  - erlang-release
extends: []
related:
  - appup
  - hot-code-loading
contrasts_with: []
answers_questions:
  - "What does the release_handler module do?"
  - "How do I install and make a release upgrade permanent?"
  - "How do I roll back a release upgrade?"
---

# release_handler Module

## Quick Definition

`release_handler` is the OTP module that installs, activates, and makes permanent (or rolls back) release upgrades on a running system. It is part of the SASL application.

## Core Definition

`release_handler` drives the runtime side of a relup. The book uses it to take a running release, unpack a new version, install it, and then commit it permanently (Ch. 22, "Upgrading the Release"). It also maintains the `RELEASES` file that records where to find modules to load and reload. The relevant functions are introduced as the final steps of the relup procedure.

## Prerequisites

- **Relup** — `release_handler` consumes the relup and tar files produced by `systools`
- **Erlang-release** — It operates on installed release versions

## Key Properties

1. `release_handler:create_RELEASES(RootDir, ReleasesDir, Relfile, [{AppName, Vsn, LibDir}])` creates the `RELEASES` file; must be run before starting production
2. `release_handler:unpack_release("NameOfRel-Vsn")` unpacks a new release into an `unpacked` state
3. `release_handler:install_release(Vsn)` installs the release, moving it to a `current` state
4. `release_handler:make_permanent(Vsn)` commits the release, making it `permanent`
5. `release_handler:which_releases()` lists releases and their states (`unpacked`, `current`, `permanent`, `old`)
6. Downgrading is done by calling `install_release` with an older version
7. An empty module list in `which_releases()` output signals the `RELEASES` file was never created, which blocks rollback to the first version

## Construction / Recognition

### To install a release upgrade at runtime

1. From a shell running the old release, call `release_handler:unpack_release("processquest-1.1.0")`
2. Confirm with `release_handler:which_releases()` (state should be `unpacked`)
3. Call `release_handler:install_release("1.1.0")` (state becomes `current`)
4. Call `release_handler:make_permanent("1.1.0")` (state becomes `permanent`)
5. Verify; on failure, `install_release` an older version to roll back

## Context & Application

`release_handler` belongs to SASL, which must be included in the release for upgrades to work. The release states form a lifecycle: `unpacked` → `current` → `permanent`, with the previous release dropping to `old`.

## Examples

**Example** (Ch. 22):

```erlang
1> release_handler:unpack_release("processquest-1.1.0").
{ok,"1.1.0"}
3> release_handler:install_release("1.1.0").
{ok,"1.0.0",[]}
5> release_handler:make_permanent("1.1.0").
ok.
```

**Example** (Ch. 22): `release_handler:create_RELEASES("rel", "rel/releases", "rel/releases/1.0.0/processquest-1.0.0.rel", [...])` builds the `RELEASES` file so the first release can later be rolled back to.

## Relationships

### Builds Upon

- **Relup** — `release_handler` applies the relup at runtime

### Related

- **Appup** — Appups feed the relup that `release_handler` installs
- **Hot-code-loading** — `release_handler` is the controlled mechanism behind live release upgrades

## Common Errors

- **Error**: Skipping `create_RELEASES` before starting production.
  **Correction**: Always create the `RELEASES` file first, or rollback to the initial release fails.
- **Error**: Calling `make_permanent` while processes are blocked and cannot upgrade.
  **Correction**: Ensure processes are responsive; blocked ones are killed during the upgrade.

## Common Confusions

- **Confusion**: Thinking `install_release` is the final step.
  **Clarification**: Until `make_permanent` is called, the upgrade is `current` but not committed across restarts.
- **Confusion**: Believing `release_handler` builds the relup.
  **Clarification**: `systools` generates the relup; `release_handler` only applies it at runtime.

## Source Reference

Chapter 22, "Leveling Up in the Process Quest," section "Upgrading the Release." See the `release_handler` shell session and the `create_RELEASES` discussion.

## Verification Notes

- Definition: Direct adaptation from "Upgrading the Release"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter demonstrates each function
- Cross-references: `relup`, `appup`, `erlang-release`, `hot-code-loading` planned/shared
