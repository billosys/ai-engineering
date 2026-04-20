---
concept: Stability and Releases
slug: deno-stability-and-releases
category: platform
subcategory: release management
tier: advanced
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/stability_and_releases.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Deno release channels"
  - "Deno versioning"
  - "Deno LTS"
  - "Deno unstable APIs"
prerequisites:
  - deno
extends: []
related:
  - deno-cli
  - deno-namespace-apis
  - deno-in-ci
contrasts_with: []
answers_questions:
  - "What are Deno's release channels?"
  - "How does Deno handle unstable APIs?"
  - "What is Deno LTS?"
  - "How often does Deno release new versions?"
---

# Quick Definition

Deno follows a 12-week minor release schedule with four release channels (stable, LTS, RC, canary), semantic versioning guarantees since 1.0, and explicit `--unstable-*` flags for experimental APIs.

# Core Definition

"As of Deno 1.0.0, the `Deno` namespace APIs are stable. That means we will strive to make code working under 1.0.0 continue to work in future versions."

Deno offers four release channels:

- **`stable`** -- Semver minor/patch releases on a 12-week schedule. "This is the default distribution channel that is recommended for most users."
- **`lts`** -- Long-term support for a specific stable release, "recommended for enterprise users who prefer not to upgrade so often." Receives security patches, critical bug fixes, and potentially critical performance improvements. API changes and major features are not backported. Note: LTS support will be discontinued after April 30, 2026.
- **`rc`** -- Release candidate for the upcoming minor release.
- **`canary`** -- Unstable release that "changes multiple times per day, allows to try out latest bug fixes and new features."

Unstable APIs are gated behind explicit `--unstable-*` flags (e.g., `--unstable-kv`). Some non-runtime features (e.g., `--unstable-sloppy-imports`) are also behind unstable flags.

The Deno Standard Library (`jsr.io/@std`) follows its own stability: modules at version 1.0.0+ are stable; 0.x modules are unstable.

# Prerequisites

- **Deno** -- Understanding the runtime is needed to understand its release process.

# Key Properties

1. **12-week release cycle** -- New minor versions (e.g., v2.1.0, v2.2.0) every 12 weeks with patch releases as needed.
2. **Four channels** -- stable, lts, rc, canary.
3. **Semantic versioning** -- Stable APIs guaranteed not to break within a major version.
4. **Unstable API flags** -- New APIs start as unstable (`--unstable-*`) before being stabilized.
5. **LTS backports** -- Security patches, critical bug fixes only. No new features. LTS ends April 2026.
6. **Standard library versioning** -- 1.0.0+ modules are stable; 0.x modules may change.
7. **Self-upgrade** -- `deno upgrade` installs the latest version; `deno upgrade --version X.Y.Z` installs a specific version.

# Construction / Recognition

## To Use:
- Install stable: `curl -fsSL https://deno.land/install.sh | sh`
- Upgrade: `deno upgrade`
- Install specific version: `deno upgrade --version 2.1.0`
- Use unstable API: `deno run --unstable-kv main.ts`
- Pin in CI: `deno-version: v2.x` in GitHub Actions.

## LTS Schedule (from source):

| LTS Version | Start         | End            |
|-------------|---------------|----------------|
| v2.1        | Feb 1, 2025   | Apr 30, 2025   |
| v2.2        | May 1, 2025   | Oct 31, 2025   |
| v2.5        | Nov 1, 2025   | Apr 30, 2026   |

# Context & Application

- **Enterprise deployments**: LTS channel provides stability with minimal upgrade frequency.
- **Early adopters**: Canary channel for testing upcoming features.
- **CI/CD**: Pin to stable or LTS; optionally test against canary with `continue-on-error`.
- **Library authors**: Target stable APIs; use unstable flags for experimental feature access.

# Examples

**Example 1** (from source): Using an unstable flag.
```shell
deno run --unstable-kv main.ts
```
(Section: "Unstable APIs")

**Example 2** (from source): Upgrading to a specific version.
```shell
deno upgrade --version 1.0.1
```
(Section: from installation.md "Updating")

# Relationships

## Builds Upon
- **Deno** -- Release management is about the runtime itself.

## Enables
- Predictable upgrade planning for production deployments.
- Safe experimentation with unstable APIs.

## Related
- **deno-cli** -- `deno upgrade` manages versions.
- **deno-namespace-apis** -- Some Deno namespace APIs are behind unstable flags.
- **deno-in-ci** -- CI matrices can include canary and LTS versions.

# Common Errors

- **Error**: Using an unstable API without the corresponding `--unstable-*` flag.
  **Correction**: Unstable APIs require explicit flags, e.g., `--unstable-kv`.

- **Error**: Expecting LTS to receive new features.
  **Correction**: "API changes and major new features will not be backported" to LTS.

# Common Confusions

- **Confusion**: Standard library stability follows the same rules as runtime stability.
  **Clarification**: The standard library has its own versioning. Modules at 1.0.0+ are stable; 0.x modules are unstable. "It is not necessary to use any unstable flags to use unstable standard library modules."

- **Confusion**: Canary is a beta release.
  **Clarification**: Canary "changes multiple times per day" and is far less stable than a beta or RC.

# Source Reference

- runtime/fundamentals/stability_and_releases.md: Full documentation of release channels, LTS schedule, unstable APIs, and standard library stability.
- runtime/getting_started/installation.md: `deno upgrade` documentation.

# Verification Notes

- High confidence: Release channels, LTS table, and unstable API policy directly quoted from source.
- LTS discontinuation warning (April 2026) noted directly from source.
