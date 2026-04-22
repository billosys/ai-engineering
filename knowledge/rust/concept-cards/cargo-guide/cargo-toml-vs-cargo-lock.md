---
# === CORE IDENTIFICATION ===
concept: Cargo.toml vs Cargo.lock
slug: cargo-toml-vs-cargo-lock

# === CLASSIFICATION ===
category: project-organization
subcategory: configuration-files
tier: foundational

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "06-cargo-toml-vs-cargo-lock"
chapter_number: 6
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "manifest vs lockfile"
  - "Cargo.toml and Cargo.lock"
  - "Cargo lockfile"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-dependencies
extends: []
related:
  - cargo-manifest
  - creating-a-cargo-project
  - cargo-ci
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between Cargo.toml and Cargo.lock?"
  - "Which file do I edit by hand and which does Cargo maintain?"
  - "Should I commit Cargo.lock to version control?"
  - "How does Cargo.lock ensure reproducible builds?"
  - "What problem does Cargo.lock solve for Git-sourced dependencies?"
  - "How do I update the locked dependency versions?"
---

# Quick Definition

`Cargo.toml` is the human-written manifest that describes dependencies broadly (e.g., a SemVer range or a Git URL). `Cargo.lock` is the Cargo-maintained lockfile that records the exact versions and revisions used. Together they ensure reproducible builds: `Cargo.toml` says what you want, `Cargo.lock` records what you got. When in doubt, check `Cargo.lock` into version control.

# Core Definition

The source provides a clear summary: "`Cargo.toml` is about describing your dependencies in a broad sense, and is written by you. `Cargo.lock` contains exact information about your dependencies. It is maintained by Cargo and should not be manually edited." (Ch. 6). The chapter illustrates the problem `Cargo.lock` solves using a Git dependency example: without the lockfile, two developers building the same manifest at different times could get different commits, leading to different builds. `Cargo.lock` eliminates this by recording the exact commit SHA or version used on the first build, and subsequent builds reuse those exact versions.

The source advises: "When in doubt, check `Cargo.lock` into the version control system (e.g. Git)." The chapter also demonstrates `cargo update` as the mechanism to explicitly opt into newer dependency versions, which writes a new `Cargo.lock`.

# Prerequisites

- **Cargo Dependencies** -- understanding how dependencies are declared in `Cargo.toml` is necessary to understand the distinction

# Key Properties

1. **Cargo.toml is human-written**: A manifest file where you declare dependencies broadly
2. **Cargo.lock is Cargo-maintained**: Should not be manually edited; Cargo generates and updates it
3. **Reproducible builds**: `Cargo.lock` ensures identical builds across different machines and times
4. **Exact revisions recorded**: For Git dependencies, the lockfile stores the full commit SHA
5. **First-build locking**: Cargo records exact versions on the first build; subsequent builds reuse them
6. **Explicit updates via cargo update**: `cargo update` (all) or `cargo update <name>` (specific) refreshes locked versions
7. **Version control guidance**: "When in doubt, check `Cargo.lock` into the version control system"

# Construction / Recognition

## Cargo.toml (broad dependency declaration):
```toml
[package]
name = "hello_world"
version = "0.1.0"

[dependencies]
regex = { git = "https://github.com/rust-lang/regex.git" }
```

## Cargo.lock (exact revision recorded by Cargo):
```toml
[[package]]
name = "hello_world"
version = "0.1.0"
dependencies = [
 "regex 1.5.0 (git+https://github.com/rust-lang/regex.git#9f9f693768c584971a4d53bc3c586c33ed3a6831)",
]

[[package]]
name = "regex"
version = "1.5.0"
source = "git+https://github.com/rust-lang/regex.git#9f9f693768c584971a4d53bc3c586c33ed3a6831"
```

## Updating locked versions:
```console
$ cargo update         # updates all dependencies
$ cargo update regex   # updates just "regex"
```

# Context & Application

This chapter addresses one of the most common questions for new Rust developers: what is `Cargo.lock` and should I commit it? The source uses a concrete Git dependency example to demonstrate how builds can diverge without a lockfile, making the case for reproducibility. The guidance to check `Cargo.lock` into version control applies especially to binary projects and applications. The chapter also connects forward to CI practices, recommending pairing lockfile management with "Verifying Latest Dependencies" in CI. This guide-level explanation complements the cargo-getting-started `cargo-manifest` card by focusing on the two-file system and the reproducibility guarantee rather than just the manifest format.

# Examples

**Example 1** (Ch. 6): The reproducibility problem with Git dependencies:
> "If you build this package today, and then you send a copy to me, and I build this package tomorrow, something bad could happen. There could be more commits to `regex` in the meantime, and my build would include new commits while yours would not."

**Example 2** (Ch. 6): Specifying a fixed revision manually (the tedious alternative):
```toml
[dependencies]
regex = { git = "https://github.com/rust-lang/regex.git", rev = "9f9f693" }
```
> "Now our builds will be the same. But there's a big drawback: now you have to manually think about SHA-1s every time you want to update our library."

**Example 3** (Ch. 6): Cargo.lock solves this automatically:
> "Cargo will take the latest commit and write that information out into your `Cargo.lock` when you build for the first time."

**Example 4** (Ch. 6): The update workflow:
> "When you're ready to opt in to a new version of the library, Cargo can re-calculate the dependencies and update things for you."

# Relationships

## Builds Upon
- **Cargo Dependencies** -- the lockfile records exact versions for the dependencies declared in the manifest

## Enables
- **cargo-ci** -- CI strategies depend on understanding lockfile behavior (e.g., verifying latest dependencies)
- **cargo-publishing** -- published crates should include `Cargo.lock` for binary crates

## Related
- **cargo-manifest** -- `Cargo.toml` is the manifest described here at a guide level
- **creating-a-cargo-project** -- `cargo new` generates the initial `Cargo.toml` and the first build creates `Cargo.lock`

## Contrasts With
- None within this source (the two files complement each other)

# Common Errors

- **Error**: Manually editing `Cargo.lock` to change dependency versions.
  **Correction**: The source states `Cargo.lock` "should not be manually edited." Use `cargo update` to change locked versions.

- **Error**: Not committing `Cargo.lock` to version control for a binary project.
  **Correction**: "When in doubt, check `Cargo.lock` into the version control system." This ensures reproducible builds for collaborators.

- **Error**: Expecting `cargo build` to automatically pick up new dependency versions.
  **Correction**: Cargo uses the locked versions in `Cargo.lock`. You must explicitly run `cargo update` to get newer versions.

# Common Confusions

- **Confusion**: Thinking `Cargo.toml` and `Cargo.lock` are redundant.
  **Clarification**: They serve different roles. `Cargo.toml` is the broad specification (what you want); `Cargo.lock` is the exact record (what you got). Both are necessary for the combination of flexibility and reproducibility.

- **Confusion**: Thinking `Cargo.lock` should never be committed (because library crates historically didn't require it).
  **Clarification**: The source's guidance is "when in doubt, check `Cargo.lock` into the version control system." The FAQ discusses when alternatives might apply, but the default advice is to commit it.

- **Confusion**: Thinking `cargo update` ignores the SemVer constraints in `Cargo.toml`.
  **Clarification**: `cargo update` respects the version requirements in `Cargo.toml`. It finds the latest compatible version within the specified range and updates the lockfile accordingly.

# Source Reference

Chapter 6: Cargo.toml vs Cargo.lock. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 6 -- "`Cargo.toml` is about describing your dependencies in a broad sense, and is written by you. `Cargo.lock` contains exact information about your dependencies."
- Confidence rationale: HIGH -- the source provides clear definitions, a motivating example, and concrete lockfile content
- Uncertainties: The FAQ guidance on when not to commit `Cargo.lock` is referenced but not detailed in this chapter
- Cross-reference status: cargo-manifest references cargo-getting-started cards; other slugs are within this extraction set
