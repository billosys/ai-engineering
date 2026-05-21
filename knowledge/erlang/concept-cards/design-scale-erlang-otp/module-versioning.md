---
# === CORE IDENTIFICATION ===
concept: Module Versioning
slug: module-versioning

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Two-Module Limit"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - vsn attribute
  - "-vsn"
  - md5 digest version
  - module version

# === TYPED RELATIONSHIPS ===
prerequisites:
  - two-module-limit
extends: []
related:
  - software-upgrade
  - code-change-callback
  - release-and-application-versions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a module's version determined in Erlang?"
  - "What must I understand before performing release upgrades?"
---

# Quick Definition

Module versioning is the tagging of a module with a version via the `-vsn(Version)` attribute. If the attribute is omitted, the compiler generates a 128-bit md5 digest of the module's code as its version.

# Core Definition

With two versions of code allowed in the runtime, a way is needed to determine the current version of a module — the `-vsn(Version)` module attribute achieves exactly that (Cesarini & Vinoski, p. 338, pdf p. 336). `Version` can be any Erlang term, most commonly a string, number, or atom; it is often set by a script triggered by the revision control system on commit. The `vsn` attribute is not mandatory: if omitted, the compiler generates it at compile time using `beam_lib:md5/1` to produce a 128-bit md5 digest of the module. The md5 digest is based on properties of the module but excludes compile date and irrelevant attributes, so the same code is always tagged with the same key regardless of compilation time, spaces, carriage returns, or comments. The version of a loaded module is retrieved with `Mod:module_info/0,1`.

# Prerequisites

- **Two-module limit** — Versioning exists to distinguish the two coexisting module versions; that limit is the motivation.

# Key Properties

1. The `-vsn(Version)` attribute tags a module with a version.
2. `Version` can be any Erlang term — commonly a string, number, or atom.
3. The attribute is optional; if omitted, the compiler generates an md5-digest version.
4. The md5 digest is a 128-bit key from `beam_lib:md5/1`.
5. The digest excludes compile date and code-irrelevant attributes — stable across recompiles of identical code.
6. Placed at the start of the module with the other attributes.
7. Retrieved via `Mod:module_info/0,1` (the `attributes` key).
8. Used to control state, schema, protocol, and data-format changes during upgrades.

# Construction / Recognition

## To Version a Module:
1. Add `-vsn(Version).` near the top of the module with the other attributes.
2. Or omit it and let the compiler generate the md5-digest version.
3. Optionally set `Version` from a revision-control script (e.g. `git describe --long`).

## To Recognize a Module's Version:
1. Call `Mod:module_info(attributes)` and read the `vsn` entry.
2. To reconstruct an md5 version, use `beam_lib:md5(Mod)`.

# Context & Application

- **Typical contexts**: Identifying which version of a module is running before and after an upgrade.
- **Common applications**: Controlling code_change behavior based on the version being upgraded from; tying version to revision-control state.
- **Historical/stylistic notes**: A common practice is setting `Version` to the output of `git describe --long` (most recent tag, commit count since, current hash).

# Examples

**Example 1** (p. 338): Without a `-vsn` directive, the compiler generates the md5 digest as the version:

```erlang
2> coffee:module_info(attributes).
[{vsn,[293551046745957884913825426256179654413]}]
3> {ok, {coffee, MD5Digest}} = beam_lib:md5(coffee).
4> <<Int:128/integer>> = MD5Digest, Int.
293551046745957884913825426256179654413
```

**Example 2** (p. 338): Adding `-vsn(1.0).` manually sets the version explicitly:

```erlang
-module(coffee).
-export(...).
-vsn(1.0).
```

```erlang
6> coffee:module_info(attributes).
[{vsn,[1.0]}]
```

# Relationships

## Builds Upon
- **Two-module limit** — Versioning distinguishes the two allowed module versions.

## Related
- **Software upgrade** — The version controls how upgrades adapt state.
- **Code change callback** — `code_change` receives the old version as its `Vsn` argument.
- **Release and application versions** — Module versions are the granular layer below application versions.

# Common Errors

- **Error**: Assuming every module has an explicit version.
  **Correction**: If no `-vsn` is given, the version is an md5 digest; use a wildcard in `code_change` when versions do not matter.

- **Error**: Expecting the md5 version to change when only comments or whitespace change.
  **Correction**: The md5 digest excludes such code-irrelevant differences; identical code yields the same key.

# Common Confusions

- **Confusion**: Thinking the `-vsn` attribute is mandatory.
  **Clarification**: It is optional; the compiler generates an md5-digest version when it is absent.

- **Confusion**: Believing `Version` must be a number.
  **Clarification**: It can be any Erlang term — string, number, or atom.

# Source Reference

Chapter 11: Release Upgrades, section "Two-Module Limit," page 338 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of p. 338.
- Confidence rationale: HIGH — the source explicitly describes the `-vsn` attribute and md5-digest fallback.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
