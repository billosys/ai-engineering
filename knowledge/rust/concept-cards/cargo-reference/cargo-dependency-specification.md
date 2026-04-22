---
# === CORE IDENTIFICATION ===
concept: Cargo Dependency Specification
slug: cargo-dependency-specification

# === CLASSIFICATION ===
category: package-management
subcategory: dependency-management
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "03-specifying-dependencies"
chapter_number: 3
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "version requirement syntax"
  - "caret requirements"
  - "tilde requirements"
  - "path dependencies"
  - "git dependencies"
  - "dependency specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-dependencies
extends:
  - cargo-dependencies
related:
  - cargo-features
  - cargo-toml-vs-cargo-lock
  - cargo-publishing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What version requirement syntaxes does Cargo support (caret, tilde, wildcard, comparison)?"
  - "How do default/caret version requirements work in Cargo?"
  - "How do I specify a dependency from a git repository?"
  - "How do I specify a path dependency for local development?"
  - "How do I use platform-specific dependencies?"
  - "What are dev-dependencies and build-dependencies?"
  - "How do I rename a dependency in Cargo.toml?"
  - "How do I inherit dependencies from a workspace?"
  - "How do I use the [patch] section to override dependencies?"
  - "What is the difference between path, git, and registry dependencies?"
  - "How do multiple locations work for dependencies?"
---

# Quick Definition

Cargo supports specifying dependencies from crates.io (with version requirement syntax), git repositories (with optional branch/tag/rev pinning), local filesystem paths, and alternative registries. Version requirements use SemVer-compatible defaults (caret), with tilde, wildcard, and comparison operators available for finer control. Dependencies can be scoped to platforms, build scripts, or tests, renamed via the `package` key, inherited from workspaces, and overridden with `[patch]`.

# Core Definition

The source explains that dependencies are specified in `Cargo.toml` using several location types and version constraint syntaxes. The fundamental version requirement is the **default/caret requirement**, which allows SemVer-compatible updates: "Versions are considered compatible if their left-most non-zero major/minor/patch component is the same" (Ch. 3). The bare version string `"1.2.3"` is equivalent to `"^1.2.3"`, meaning `>=1.2.3, <2.0.0`. This extends to pre-1.0 versions: `"0.2.3"` means `>=0.2.3, <0.3.0`, and `"0.0.3"` means `>=0.0.3, <0.0.4`.

Beyond crates.io, dependencies can come from **git repositories** (with `git`, `branch`, `tag`, or `rev` keys) or **local paths** (with the `path` key). The source notes a key distinction: "Cargo fetches the `git` repository at that location and traverses the file tree to find `Cargo.toml`" for git deps, but "local paths must point to the exact folder" for path deps. Dependencies can also be scoped as `[dev-dependencies]` (tests/examples/benchmarks only, not propagated), `[build-dependencies]` (build scripts only), or platform-specific under `[target.'cfg(...)'.dependencies]`.

The `[patch]` section enables overriding any dependency source for local development and testing. As the source states: "The `[patch]` table is made of dependency-like sub-tables. Each key after `[patch]` is a URL of the source that is being patched."

# Prerequisites

- **Creating a Cargo Project** -- a project with `Cargo.toml` must exist before specifying dependencies
- **Cargo Dependencies** -- basic understanding of adding dependencies to `Cargo.toml`

# Key Properties

1. **Default/caret requirements**: `"1.2.3"` equals `^1.2.3` equals `>=1.2.3, <2.0.0`; the left-most non-zero component defines the compatibility range
2. **Tilde requirements**: `~1.2.3` means `>=1.2.3, <1.3.0` -- only patch-level changes allowed when minor is specified
3. **Wildcard requirements**: `1.*` means `>=1.0.0, <2.0.0`; bare `*` is not allowed on crates.io
4. **Comparison requirements**: explicit ranges like `>= 1.2.0`, `< 2`, or exact pins with `= 1.2.3`
5. **Git dependencies**: specify `git` URL plus optional `branch`, `tag`, or `rev`; Cargo traverses the repo tree to find the crate
6. **Path dependencies**: specify `path` key pointing to exact directory; no tree traversal unlike git
7. **Multiple locations**: combine `version` with `path` or `git` to use local source during development and registry version when published
8. **Platform-specific deps**: use `[target.'cfg(windows)'.dependencies]` syntax with `not`, `any`, `all` operators
9. **Dev-dependencies**: not propagated to dependents, used only for tests/examples/benchmarks
10. **Build-dependencies**: available only to build scripts, not to the package itself
11. **Dependency renaming**: `package` key allows using a different local name for a dependency
12. **Workspace inheritance**: `workspace = true` inherits dependency specification from `[workspace.dependencies]`
13. **[patch] overrides**: temporarily replace a dependency source for the entire workspace; applies transitively but defined only at top level
14. **Pre-release handling**: version requirements exclude pre-releases unless explicitly specified

# Construction / Recognition

## Version Requirement Syntax:
```notrust
1.2.3  :=  >=1.2.3, <2.0.0   (default/caret)
0.2.3  :=  >=0.2.3, <0.3.0   (left-most non-zero)
0.0.3  :=  >=0.0.3, <0.0.4   (patch-only)
~1.2.3 :=  >=1.2.3, <1.3.0   (tilde)
~1.2   :=  >=1.2.0, <1.3.0   (tilde)
1.*    :=  >=1.0.0, <2.0.0   (wildcard)
>= 1.2, < 1.5                (comparison, comma-separated)
```

## Git Dependency with Branch:
```toml
[dependencies]
regex = { git = "https://github.com/rust-lang/regex.git", branch = "next" }
```

## Path Dependency for Local Development:
```toml
[dependencies]
hello_utils = { path = "hello_utils" }
```

## Multiple Locations (local + published):
```toml
[dependencies]
bitflags = { path = "my-bitflags", version = "1.0" }
```

## Platform-Specific Dependencies:
```toml
[target.'cfg(windows)'.dependencies]
winhttp = "0.4.0"

[target.'cfg(unix)'.dependencies]
openssl = "1.0.1"
```

## Dev and Build Dependencies:
```toml
[dev-dependencies]
tempdir = "0.3"

[build-dependencies]
cc = "1.0.3"
```

## Dependency Renaming:
```toml
[dependencies]
foo = "0.1"
bar = { git = "https://github.com/example/project.git", package = "foo" }
```

## Workspace Inheritance:
```toml
[dependencies]
regex = { workspace = true, features = ["unicode"] }
```

## Patching a Dependency:
```toml
[patch.crates-io]
uuid = { path = "../path/to/uuid" }
```

# Context & Application

This card covers the reference-level specification for all dependency types in Cargo. It complements the guide-level `cargo-dependencies` card (which covers the basic workflow of adding and updating dependencies) with the full syntax and semantics. Chapter 3 is the largest chapter in the Cargo Reference because dependency specification is the most complex and varied aspect of Cargo configuration. The version requirement syntax -- particularly the default/caret behavior where the left-most non-zero component defines the compatibility boundary -- is critical knowledge for every Rust developer. The `[patch]` section, multiple-location pattern, and workspace inheritance are essential for monorepo and multi-crate development workflows.

# Examples

**Example 1** (Ch. 3): Default requirement for pre-1.0 crates:
```notrust
0.2.3  :=  >=0.2.3, <0.3.0
0.0.3  :=  >=0.0.3, <0.0.4
```
> "Versions are considered compatible if their left-most non-zero major/minor/patch component is the same. This is different from SemVer which considers all pre-1.0.0 packages to be incompatible."

**Example 2** (Ch. 3): Git dependency with version validation:
```toml
[dependencies]
regex = { version = "1.10.3", git = "https://github.com/rust-lang/regex.git", branch = "next" }
```
> "The `version` key does _not_ affect which commit is used when Cargo retrieves the `git` dependency, but Cargo checks the version information in the dependency's `Cargo.toml` file against the `version` key and raises an error if the check fails."

**Example 3** (Ch. 3): Path vs git tree traversal difference:
```toml
# git key accepts the repo root URL and Cargo traverses the tree
regex-lite = { git = "https://github.com/rust-lang/regex.git" }
# path key requires the member name to be included
regex-lite = { path = "../regex/regex-lite" }
```

**Example 4** (Ch. 3): Patching for bug fix testing:
```toml
[patch.crates-io]
uuid = { path = "../path/to/uuid" }
```
> "Here we declare that we're *patching* the source `crates-io` with a new dependency. This will effectively add the local checked out version of `uuid` to the crates.io registry for our local package."

**Example 5** (Ch. 3): Build-dependency isolation:
> "The build script **does not** have access to the dependencies listed in the `dependencies` or `dev-dependencies` section. Build dependencies will likewise not be available to the package itself unless listed under the `dependencies` section as well."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- dependencies are specified in an existing project's `Cargo.toml`
- **Cargo Dependencies** -- extends the guide-level introduction with full reference syntax

## Enables
- **cargo-features** -- optional dependencies and feature-gated dependencies build on dependency specification
- **cargo-publishing** -- published crates must have their dependencies satisfy crates.io constraints (no bare path/git deps)

## Related
- **cargo-toml-vs-cargo-lock** -- `Cargo.lock` pins the resolved versions of specified dependencies
- **cargo-build-performance** -- dependency count and feature choices affect build times

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `"0.2.3"` and expecting it to allow updates to `0.3.0`.
  **Correction**: For pre-1.0 versions, the left-most non-zero component defines the compatibility boundary. `"0.2.3"` means `>=0.2.3, <0.3.0`, not `>=0.2.3, <1.0.0`.

- **Error**: Specifying a path dependency without the `version` key and trying to publish.
  **Correction**: "Crates that use dependencies specified with only a path are not permitted on crates.io." Add `version` alongside `path` for publishable crates.

- **Error**: Using `path` key and expecting Cargo to traverse subdirectories to find the crate.
  **Correction**: "The local paths must point to the exact folder with the dependency's `Cargo.toml`." Only git dependencies support tree traversal.

- **Error**: Defining `[patch]` in a non-root workspace member.
  **Correction**: "Cargo only looks at the patch settings in the `Cargo.toml` manifest at the root of the workspace. Patch settings defined in dependencies will be ignored."

- **Error**: Using `[target.'cfg(feature = "...")'.dependencies]` to conditionally include deps.
  **Correction**: "You cannot use `[target.'cfg(feature = "fancy-feature")'.dependencies]` to add dependencies based on optional features. Use the `[features]` section instead."

# Common Confusions

- **Confusion**: Thinking caret (`^`) and default requirements are different things.
  **Clarification**: They are identical. The source states: "`log = \"^1.2.3\"` is exactly equivalent to `log = \"1.2.3\"`." Caret requirements are the default strategy; the `^` prefix is optional.

- **Confusion**: Thinking `version` in a git dependency controls which commit is fetched.
  **Clarification**: "The `version` key does _not_ affect which commit is used when Cargo retrieves the `git` dependency." It is only used to validate the version in the fetched crate's `Cargo.toml`.

- **Confusion**: Thinking dev-dependencies are propagated to downstream users.
  **Clarification**: "These dependencies are *not* propagated to other packages which depend on this package." Dev-deps are purely local to tests, examples, and benchmarks.

- **Confusion**: Thinking `[patch]` only affects direct dependencies.
  **Clarification**: "`[patch]` applies *transitively*" -- it affects the patched crate everywhere in the dependency graph, but "can only be defined at the *top level*."

# Source Reference

Chapter 3: Specifying Dependencies -- sections on version requirement syntax, crates.io/registry/git/path dependencies, multiple locations, platform-specific dependencies, dev-dependencies, build-dependencies, renaming dependencies, workspace inheritance, overriding dependencies (patch/replace/paths), source replacement, and dependency resolution. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 3 -- version requirement syntax table, dependency specification rules, and [patch] semantics
- Confidence rationale: HIGH -- the source provides exhaustive syntax examples, explicit rules for each dependency type, and detailed explanations of version resolution behavior
- Uncertainties: The `[replace]` section is deprecated in favor of `[patch]`; resolver version 3 behavior (edition 2024) may evolve
- Cross-reference status: References cargo-dependencies (guide-level), cargo-features (Ch. 4), cargo-toml-vs-cargo-lock, cargo-publishing
