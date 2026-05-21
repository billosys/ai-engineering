---
# === CORE IDENTIFICATION ===
concept: Upgrading Environment Variables
slug: upgrading-environment-variables

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
section: "Upgrading Environment Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - config_change callback
  - "config_change/3"
  - application environment variable upgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
extends: []
related:
  - system-configuration-file
  - installing-an-upgrade
  - code-change-callback
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are application environment variables upgraded during a release upgrade?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Upgrading environment variables is the process by which a release upgrade reconciles old and new application environment variables. The application controller compares them and invokes the optional `config_change/3` callback in the new application callback module.

# Core Definition

When upgrading a release, the new package includes a new (mandatory) `sys.config` and a new app file for every new and upgraded application; these files may contain new or updated environment variables (Cesarini & Vinoski, p. 351, pdf p. 336). During the upgrade, the application controller compares old environment variables with their current counterparts in the start scripts (set with `-application key value`), config files, and app files, updating any differences. When done, the callback `Module:config_change(Updated, New, Deleted)` is called in the new application callback module, prior to resuming the processes, where `Updated`, `New`, and `Deleted` are lists of `{Key, Value}` tuples.

# Prerequisites

- **Release upgrade** — Environment-variable upgrading happens as part of a release upgrade; that concept comes first.

# Key Properties

1. A release upgrade ships a new, mandatory `sys.config` and new app files.
2. The application controller compares old and current environment variables across start scripts, config files, and app files.
3. The optional `Module:config_change(Updated, New, Deleted)` callback is then invoked in the new application callback module.
4. It is called before the processes are resumed.
5. `Updated`, `New`, and `Deleted` are each lists of `{Key, Value}` tuples.
6. The callback is optional and can be omitted.
7. It is useful when process states depend on environment variables read at startup.
8. Making a release permanent changes the `sys.config` pointed to by the start scripts to the new version.

# Construction / Recognition

## To Handle Environment-Variable Upgrades:
1. Ship updated environment variables in the new `sys.config` and app files.
2. Optionally implement `config_change/3` in the new application callback module.
3. In `config_change/3`, react to the `Updated`, `New`, and `Deleted` `{Key, Value}` lists.
4. Make the release permanent to commit the new `sys.config`.

## To Recognize It:
1. A `config_change/3` clause in an application callback module.

# Context & Application

- **Typical contexts**: Release upgrades that add, change, or remove application environment variables.
- **Common applications**: Re-deriving process state from configuration values read at startup.
- **Historical/stylistic notes**: The new `sys.config` is committed only when the release is made permanent, because rebooting a non-permanent release reverts to the previous one.

# Examples

**Example 1** (p. 351): The callback signature invoked after the application controller reconciles variables — `Module:config_change(Updated, New, Deleted)`, where each argument is a list of `{Key, Value}` tuples.

**Example 2** (p. 351): The new `sys.config` pointed to by the start scripts changes only when `make_permanent` is called — because a non-permanent release reverts on reboot.

# Relationships

## Builds Upon
- **Release upgrade** — Environment-variable reconciliation is a step of a release upgrade.

## Related
- **System configuration file** — A new `sys.config` is shipped with every upgrade.
- **Installing an upgrade** — Making the release permanent commits the new `sys.config`.
- **Code change callback** — `config_change/3` complements `code_change` for configuration-dependent state.

# Common Errors

- **Error**: Assuming `config_change/3` runs after processes resume.
  **Correction**: It is invoked before the processes are resumed.

- **Error**: Expecting the new `sys.config` to take effect immediately on install.
  **Correction**: The start scripts point at the new `sys.config` only once the release is made permanent.

# Common Confusions

- **Confusion**: Thinking `config_change/3` is mandatory.
  **Clarification**: It is an optional callback that can be omitted; it is useful only when state depends on startup environment variables.

- **Confusion**: Confusing `config_change/3` with `code_change/3`.
  **Clarification**: `config_change/3` reconciles application environment variables; `code_change` migrates behavior process state.

# Source Reference

Chapter 11: Release Upgrades, section "Upgrading Environment Variables," page 351 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of p. 351.
- Confidence rationale: HIGH — the source explicitly describes the `config_change/3` callback and the application controller's reconciliation.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
