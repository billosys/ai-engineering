---
# === CORE IDENTIFICATION ===
concept: Cargo Workspaces
slug: cargo-workspaces

# === CLASSIFICATION ===
category: package-management
subcategory: workspace-management
tier: intermediate

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "02-workspaces"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo workspace"
  - "workspace configuration"
  - "virtual workspace"
  - "workspace members"
  - "[workspace] section"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-manifest-reference
  - creating-a-cargo-project
extends:
  - cargo-dependencies
related:
  - cargo-project-layout
  - cargo-toml-vs-cargo-lock
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Cargo workspace and when should I use one?"
  - "How do I configure workspace members and default-members?"
  - "What is a virtual workspace and how does it differ from a rooted workspace?"
  - "How do I share dependency versions across workspace members?"
  - "How does workspace.package inheritance work?"
  - "What is the workspace resolver field and when must I set it?"
  - "How do I use workspace.dependencies to centralize dependency management?"
  - "What are the key workspace directories and metadata tables?"
---

# Quick Definition

A Cargo workspace is a collection of one or more packages (called members) that share a common `Cargo.lock`, output directory, and Cargo settings. Workspaces are configured via a `[workspace]` table in a root `Cargo.toml` and come in two forms: rooted workspaces (root package with members) and virtual workspaces (no root package, only members).

# Core Definition

The source defines workspaces as: "A *workspace* is a collection of one or more packages, called *workspace members*, that are managed together" (Ch. 2). Key characteristics include: workspaces share a common `Cargo.lock` at the workspace root, share a common output directory (defaults to `target/` at the root), share `[patch]`, `[replace]`, and `[profile.*]` sections (only the root manifest's are used; members' are ignored), and the `[workspace]` section is only valid in the root manifest.

The root manifest is identified by the `[workspace]` table and defines the workspace. It comes in two forms: a **rooted workspace** where the root manifest also defines a `[package]` (the root is both the workspace root and a member), or a **virtual workspace** where the root manifest has `[workspace]` but no `[package]` -- it exists solely to organize members. The source notes: "The primary use case for a virtual manifest is when there is no 'primary' package, or you want to keep all packages organized in separate directories" (Ch. 2).

Members are enumerated via the `workspace.members` field, which accepts a list of path globs: "Each entry is a path to a directory that contains a `Cargo.toml`" (Ch. 2). The `workspace.exclude` field removes directories from matching. Non-root members point back to the workspace with `package.workspace` or rely on Cargo's automatic detection (walking up the directory tree to find the first `Cargo.toml` with `[workspace]`).

Workspace dependency inheritance (via `[workspace.dependencies]`) allows declaring dependencies once in the root manifest and referencing them from members with `dependency-name.workspace = true`. The source explains: "workspace.dependencies keys are not dependencies. They don't directly make the dependencies available" -- members must still opt in. Fields like `features`, `default-features`, and `optional` can be added or overridden per member.

Similarly, `[workspace.package]` allows defining shared package metadata (version, authors, edition, etc.) that members inherit with `field.workspace = true`.

# Prerequisites

- **Cargo Manifest Reference** -- understanding the full manifest format is needed since workspaces interact with multiple manifest sections
- **Creating a Cargo Project** -- workspaces organize multiple Cargo packages together

# Key Properties

1. **Shared Cargo.lock**: All workspace members share a single lockfile at the workspace root, ensuring consistent dependency versions
2. **Shared output directory**: The default `target/` directory is at the workspace root; configurable via `workspace.target-dir` or `CARGO_TARGET_DIR`
3. **Two workspace forms**: Rooted (root has `[package]` + `[workspace]`) and virtual (root has `[workspace]` only, no `[package]`)
4. **Members via glob patterns**: `workspace.members` accepts path globs like `["crates/*"]` to match directories containing `Cargo.toml` files
5. **Exclude field**: `workspace.exclude` removes paths from the members glob; useful for directories that have their own `Cargo.toml` but should not be members
6. **Package selection with default-members**: `workspace.default-members` controls which packages Cargo operates on when no `--package` flag is given; defaults to the root package (rooted) or all members (virtual)
7. **workspace.dependencies inheritance**: Dependencies declared in `[workspace.dependencies]` can be referenced by members using `dep.workspace = true`; members can add `features` or set `optional = true` on top
8. **workspace.package inheritance**: Common metadata fields (version, edition, authors, license, etc.) can be defined once and inherited by members with `field.workspace = true`
9. **Resolver field requirement**: Virtual workspaces must explicitly set `workspace.resolver` since there is no root package to infer the edition-based default
10. **Only root manifest matters for some sections**: `[patch]`, `[replace]`, and `[profile.*]` are read only from the root manifest; member-level definitions are ignored
11. **workspace.metadata**: A freeform table ignored by Cargo, available for external tooling

# Construction / Recognition

## Creating a Virtual Workspace:

```toml
# Root Cargo.toml (no [package])
[workspace]
resolver = "2"
members = [
    "crates/core",
    "crates/utils",
    "crates/cli",
]

[workspace.package]
version = "1.0.0"
edition = "2024"
authors = ["Team"]
license = "MIT"

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

## Member Inheriting from Workspace:

```toml
# crates/core/Cargo.toml
[package]
name = "my-core"
version.workspace = true
edition.workspace = true
authors.workspace = true
license.workspace = true

[dependencies]
serde.workspace = true
tokio = { workspace = true, features = ["macros"] }
```

## Creating a Rooted Workspace:

```toml
[package]
name = "my-app"
version = "1.0.0"
edition = "2024"

[workspace]
members = ["sub-crate"]
```

## Using Glob Patterns for Members:

```toml
[workspace]
members = ["crates/*"]
exclude = ["crates/experimental"]
```

## Recognizing Default-Members:

```toml
[workspace]
members = ["crates/*"]
default-members = ["crates/cli", "crates/core"]
```
When you run `cargo build` without `--package`, only `cli` and `core` are built.

# Context & Application

Workspaces are essential for organizing multi-crate Rust projects. Common patterns include: a virtual workspace with shared libraries and multiple binaries, a framework with a core library and extension crates, or a monorepo with related but independently publishable crates.

The dependency inheritance feature (`[workspace.dependencies]`) is particularly valuable for keeping versions in sync across many crates. Rather than updating `serde = "1.0.200"` in twenty `Cargo.toml` files, you update it once in the root. Members can still customize by adding features or marking dependencies optional.

The `[workspace.package]` inheritance reduces boilerplate for shared metadata. The source lists all inheritable fields: `version`, `authors`, `categories`, `description`, `documentation`, `edition`, `exclude`, `homepage`, `include`, `keywords`, `license`, `license-file`, `publish`, `readme`, `repository`, `rust-version`.

Virtual workspaces must set `workspace.resolver` explicitly because there is no root package whose edition could determine the default resolver version. For edition 2021 and later, `resolver = "2"` is standard.

The `default-members` field is useful when a workspace has many crates but developers typically work on a subset. It controls which packages are affected by commands like `cargo build` or `cargo test` when no explicit `--package` selection is made.

# Examples

**Example 1** (Ch. 2): Workspace members with glob patterns:
```toml
[workspace]
members = ["member1", "path/to/member2", "crates/*"]
```
The source notes: "The `members` list also supports globs to match multiple paths."

**Example 2** (Ch. 2): Using `exclude` to remove matched paths:
```toml
[workspace]
members = ["crates/*"]
exclude = ["crates/foo", "path/to/other"]
```
"The `exclude` key can be used to prevent paths from being included in a workspace."

**Example 3** (Ch. 2): Workspace dependency inheritance:
```toml
# [workspace] root
[workspace.dependencies]
cc = "1"
rand = "0.8"
regex = { version = "1", features = ["std"] }
```
```toml
# Member Cargo.toml
[dependencies]
regex = { workspace = true, features = ["unicode"] }

[build-dependencies]
cc.workspace = true

[dev-dependencies]
rand.workspace = true
```
The source explains: "The `features` list will be unioned with the features declared in `workspace.dependencies`."

**Example 4** (Ch. 2): Workspace package inheritance:
```toml
[workspace.package]
version = "1.2.3"
authors = ["Nice Folks"]
description = "A short description of my package"
```
```toml
[package]
name = "my-package"
version.workspace = true
authors.workspace = true
description.workspace = true
```

**Example 5** (Ch. 2): The resolver requirement for virtual workspaces:
> "If the workspace does not have a root package, the workspace must have `workspace.resolver` set since there is no `package.edition` to infer it from."

# Relationships

## Builds Upon
- **Cargo Manifest Reference** -- workspaces are configured through manifest sections
- **Cargo Dependencies** -- workspace dependency inheritance builds on top of standard dependency specification

## Enables
- **Cargo Project Layout** -- workspaces define the top-level organization for multi-crate projects

## Related
- **Cargo.toml vs Cargo.lock** -- workspaces share a single lockfile, making this distinction especially important

## Contrasts With
- None within this source

# Common Errors

- **Error**: Placing `[patch]` or `[profile.*]` in a member's `Cargo.toml` expecting it to take effect.
  **Correction**: Only the root manifest's `[patch]`, `[replace]`, and `[profile.*]` are used. Member-level definitions of these sections are ignored.

- **Error**: Forgetting to set `resolver` in a virtual workspace.
  **Correction**: Virtual workspaces have no root package, so there is no `package.edition` to infer the resolver. Set `workspace.resolver = "2"` explicitly.

- **Error**: Declaring a dependency in `[workspace.dependencies]` and expecting members to automatically use it.
  **Correction**: `workspace.dependencies` keys are not direct dependencies. Each member must explicitly opt in with `dep-name.workspace = true` in its own dependency section.

- **Error**: Trying to override the `version` of a workspace dependency in a member.
  **Correction**: Members cannot change the version of a workspace dependency. They can only add `features`, set `default-features`, or add `optional = true`. To use a different version, declare the dependency directly without `workspace = true`.

- **Error**: Having both `[workspace]` and `package.workspace` in the same manifest.
  **Correction**: A crate cannot be both a workspace root (containing `[workspace]`) and a member of another workspace (containing `package.workspace`). These are mutually exclusive.

# Common Confusions

- **Confusion**: Thinking a virtual workspace is less capable than a rooted workspace.
  **Clarification**: Virtual workspaces have the same capabilities. The only difference is that a virtual workspace has no root package -- its `Cargo.toml` only contains `[workspace]` (and optionally `[workspace.package]`, `[workspace.dependencies]`, etc.). The source calls this the "primary use case" when there is no single primary package.

- **Confusion**: Expecting each workspace member to have its own `Cargo.lock`.
  **Clarification**: All workspace members share a single `Cargo.lock` at the workspace root. This ensures consistent dependency resolution across the entire workspace.

- **Confusion**: Believing `default-members` controls which packages are included in the workspace.
  **Clarification**: `default-members` only controls which packages Cargo operates on by default when no `--package` flag is given. All entries in `members` are still part of the workspace. Use `exclude` to keep directories out of the workspace entirely.

- **Confusion**: Thinking `workspace.dependencies` features replace per-member features.
  **Clarification**: Features are unioned. If `[workspace.dependencies]` declares `regex = { version = "1", features = ["std"] }` and a member adds `features = ["unicode"]`, the member gets both `std` and `unicode`.

# Source Reference

Chapter 2: Workspaces, from the Cargo Reference. Online documentation with no page numbers. Covers: workspace definition, the `[workspace]` section, member selection (members and exclude), package selection (default-members), the `[workspace.package]` table, the `[workspace.dependencies]` table, the `[workspace.lints]` table, the `[workspace.metadata]` table, and resolver configuration.

# Verification Notes

- Definition: Direct quote from Ch. 2 opening paragraph
- Virtual vs rooted: Both forms explicitly described in source
- Dependency inheritance: Fields and behavior described with examples directly from source
- Package inheritance: Inheritable field list enumerated in source
- Resolver requirement: Explicitly stated for virtual workspaces
- Feature unioning: Directly stated in source text
- Confidence: HIGH -- this is the official reference documentation with clear, unambiguous definitions and examples
- Cross-references: Slugs reference cards from cargo-getting-started, cargo-guide, and cargo-reference sets
