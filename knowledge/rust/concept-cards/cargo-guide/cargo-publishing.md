---
# === CORE IDENTIFICATION ===
concept: Cargo Publishing
slug: cargo-publishing

# === CLASSIFICATION ===
category: package-management
subcategory: crate-publishing
tier: intermediate

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "09-publishing"
chapter_number: 9
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "publishing crates"
  - "cargo publish"
  - "publishing to crates.io"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-dependencies
  - cargo-toml-vs-cargo-lock
extends: []
related:
  - cargo-ci
  - cargo-home
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I publish a crate to crates.io?"
  - "What metadata must be in Cargo.toml before publishing?"
  - "How do I authenticate with crates.io?"
  - "What does cargo publish actually do step by step?"
  - "How do I yank a version that is broken?"
  - "How do I manage crate ownership?"
  - "Can I delete a published crate version?"
  - "How do I do a dry run before publishing?"
  - "How do I control which files are included in the published crate?"
---

# Quick Definition

Publishing a crate to crates.io involves authenticating with `cargo login`, ensuring required metadata is present in `Cargo.toml`, optionally dry-running with `cargo publish --dry-run`, and then uploading with `cargo publish`. Published versions are permanent and cannot be overwritten or deleted, but broken versions can be yanked with `cargo yank`. Crate ownership is managed with `cargo owner`.

# Core Definition

The source states: "Publishing a crate is when a specific version is uploaded to be hosted on crates.io" (Ch. 9). The chapter covers the complete publishing lifecycle:

**Authentication**: You need a crates.io account (via GitHub), an API token, and to run `cargo login`. The token is stored in `~/.cargo/credentials.toml` and is described as "a secret" that "should not be shared with anyone else."

**Pre-publish requirements**: The source specifies required metadata fields: `license` or `license-file`, `description`, `homepage`, `repository`, and `readme`. Crate names are "allocated on a first-come-first-serve basis."

**Publishing steps**: `cargo publish` performs five steps: verification checks, compression into a `.crate` file, extraction and compilation verification, upload to crates.io, and registry-side checks. The source strongly recommends `cargo publish --dry-run` first.

**Permanence**: "A publish is permanent. The version can never be overwritten, and the code cannot be deleted."

**Management**: `cargo yank` marks a version as broken (prevents new dependencies but does not break existing ones), and `cargo owner` manages named owners and team owners.

# Prerequisites

- **Cargo Dependencies** -- understanding how published crates become dependencies for others
- **Cargo.toml vs Cargo.lock** -- understanding the manifest metadata and versioning

# Key Properties

1. **Permanent publication**: Versions cannot be overwritten or deleted once published
2. **First-come-first-serve naming**: Crate names are unique and allocated when first published
3. **Five-step publish process**: Verify, compress, test-extract, upload, registry checks
4. **Required metadata**: license, description, homepage, repository, readme
5. **API token authentication**: Token stored in `~/.cargo/credentials.toml` via `cargo login`
6. **10MB size limit**: crates.io limits `.crate` files to 10MB
7. **cargo yank**: Prevents new dependencies on a version without deleting code
8. **cargo owner**: Manages named owners (full rights) and team owners (restricted rights)
9. **File control**: `exclude` and `include` keys in `Cargo.toml` control which files are packaged
10. **Dry run**: `cargo publish --dry-run` or `cargo package` tests packaging without uploading

# Construction / Recognition

## Authentication:
```console
$ cargo login
please paste the API Token found on https://crates.io/me below
abcdefghijklmnopqrstuvwxyz012345
```

## Required Cargo.toml Metadata:
```toml
[package]
name = "my_crate"
version = "0.1.0"
license = "MIT"
description = "A useful crate"
homepage = "https://example.com"
repository = "https://github.com/user/my_crate"
readme = "README.md"
```

## Dry Run:
```console
$ cargo publish --dry-run
```

## Publishing:
```console
$ cargo publish
```

## Yanking a Broken Version:
```console
$ cargo yank --version 1.0.1
$ cargo yank --version 1.0.1 --undo
```

## Managing Ownership:
```console
$ cargo owner --add github-handle
$ cargo owner --remove github-handle
$ cargo owner --add github:rust-lang:owners
$ cargo owner --remove github:rust-lang:owners
```

# Context & Application

This is the most comprehensive chapter in the Cargo Guide, covering the full lifecycle of crate publication. The emphasis on permanence and security (token management, yanking vs. deleting) reflects crates.io's design as a permanent archive. The ownership model with named owners (full rights) and team owners (restricted rights) addresses both individual and organizational workflows. The source also discusses the full release process, recommending changelog entries, git tags, and tools like `cargo-release`, `cargo-smart-release`, and `release-plz`. GitHub team permission issues are covered in detail, reflecting a common pain point for organizational users.

# Examples

**Example 1** (Ch. 9): Checking which files will be included:
```console
$ cargo package --list
```
> "crates.io currently has a 10MB size limit on the `.crate` file."

**Example 2** (Ch. 9): Excluding files from the package:
```toml
[package]
# ...
exclude = [
    "public/assets/*",
    "videos/*",
]
```

**Example 3** (Ch. 9): Including only specific files:
```toml
[package]
# ...
include = [
    "**/*.rs",
]
```

**Example 4** (Ch. 9): Yank semantics:
> "A yank does not delete any code. This feature is not intended for deleting accidentally uploaded secrets... The semantics of a yanked version are that no new dependencies can be created against that version, but all existing dependencies continue to work."

**Example 5** (Ch. 9): Named vs. team owners:
> "If a user name is given to `--add`, that user is invited as a 'named' owner, with full rights to the crate... If a team name is given to `--add`, that team is invited as a 'team' owner, with restricted right to the crate."

# Relationships

## Builds Upon
- **Cargo Dependencies** -- publishing makes your crate available as a dependency for others
- **Cargo.toml vs Cargo.lock** -- the manifest must contain required metadata for publishing

## Enables
- Others can depend on your published crate (via the dependency mechanism)

## Related
- **cargo-ci** -- CI verification is typically performed before publishing
- **cargo-home** -- the credentials file and installed crates live in the Cargo home

## Contrasts With
- None within this source

# Common Errors

- **Error**: Publishing without required metadata fields.
  **Correction**: Ensure `license`, `description`, `homepage`, `repository`, and `readme` are filled in before publishing.

- **Error**: Publishing with large test data or assets accidentally included.
  **Correction**: Run `cargo package --list` and check the `.crate` file size before publishing. Use `exclude` or `include` in `Cargo.toml` to control packaged files.

- **Error**: Thinking `cargo yank` deletes the code and secrets.
  **Correction**: "A yank does not delete any code. This feature is not intended for deleting accidentally uploaded secrets... If that happens, you must reset those secrets immediately."

- **Error**: Attempting to overwrite a previously published version.
  **Correction**: "The version can never be overwritten." Increment the version number in `Cargo.toml` and publish a new version.

# Common Confusions

- **Confusion**: Thinking yanked versions break existing users.
  **Clarification**: "All packages with a `Cargo.lock` will not break, while any future `Cargo.lock` files generated will not list the yanked version." Yanking only prevents new dependencies.

- **Confusion**: Thinking team owners have the same rights as named owners.
  **Clarification**: Team owners can publish and yank but "do not have the ability to add or remove owners." Named owners have full rights including managing other owners.

- **Confusion**: Thinking you can reclaim or reuse a crate name after publishing.
  **Clarification**: "Once a crate name is taken, it cannot be used for another crate." Names are permanent, first-come-first-serve.

# Source Reference

Chapter 9: Publishing on crates.io -- sections "Before your first publish," "Before publishing a new crate," "Packaging a crate," "Uploading the crate," "Publishing a new version of an existing crate," "Managing a crates.io-based crate," and "GitHub permissions." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 9 -- "Publishing a crate is when a specific version is uploaded to be hosted on crates.io"
- Confidence rationale: HIGH -- the source provides comprehensive step-by-step instructions with examples
- Uncertainties: Some GitHub OAuth details may change over time; the source acknowledges GitHub's "Enterprise Grade" access control complexity
- Cross-reference status: All slugs reference cards within this extraction set
