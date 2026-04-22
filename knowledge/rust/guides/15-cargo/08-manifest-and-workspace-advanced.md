# Cargo Manifest and Workspace (Advanced)

Deep coverage of `Cargo.toml` structure, manifest style, dependency overrides, and workspace mechanics beyond the basics in Guide 01. Also catalogues the ecosystem tooling you should know about.

Pattern prefixes:

- `CG-M-XX` -- manifest structure, style, and overrides
- `CG-W-XX` -- workspace layout, inheritance, and resolver behaviour
- `CG-ECO-XX` -- ecosystem tooling

---

## CG-M-01: Know the Cargo.toml Section Inventory

**Strength**: SHOULD

**Summary**: `Cargo.toml` has a fixed set of recognised sections. Knowing what exists and what each is for prevents ad-hoc keys and helps you find the right knob without guessing.

```toml
# ❌ BAD: ad-hoc keys under [package] -- silently ignored
[package]
name = "myapp"
my-custom-field = "oops"   # Cargo warns about unknown keys

# ✅ GOOD: every section has a defined role
[package]                  # Identity + metadata (see CG-M-02)
[lib]                      # Library target config
[[bin]]                    # Binary target(s), array-of-tables
[[example]]                # Example target(s)
[[test]]                   # Integration test target(s)
[[bench]]                  # Benchmark target(s)

[dependencies]             # Normal runtime deps
[dev-dependencies]         # Deps for tests/examples/benches only
[build-dependencies]       # Deps for build.rs only
[target.'cfg(unix)'.dependencies]  # Platform-specific (CG-BS-15)

[features]                 # Feature flags (CG-BS-01..04, CG-BS-13)

[profile.dev]              # Per-profile build settings
[profile.release]
[profile.test]
[profile.bench]
[profile.my-custom]        # Custom profile, inherits from a base

[lints.rust]               # Declarative lints (CG-L-02, Cargo 1.74+)
[lints.clippy]
[lints.rustdoc]

[patch.crates-io]          # Override deps for this build tree (CG-M-03)
[replace]                  # Deprecated -- use [patch] (CG-M-04)

[workspace]                # Workspace definition (CG-W-01..05)
[workspace.dependencies]
[workspace.package]
[workspace.lints]
[workspace.metadata.*]     # Arbitrary tooling metadata
[package.metadata.*]       # Arbitrary tooling metadata
```

**Rationale**: The `[*.metadata]` sections are the one place Cargo deliberately ignores -- they exist for third-party tools (docs.rs, cargo-release, etc.) to read. Everything else is schema-checked. If a key is flagged as unknown, you've either typoed or are using a feature that requires a newer MSRV (`[lints]` is 1.74+, inheritable workspace fields are 1.64+).

**See also**: CG-M-02 (style), CG-B-03 (package metadata), CG-BS-01 (features)

---

## CG-M-02: Follow the Cargo.toml Style Conventions

**Strength**: SHOULD

**Summary**: The Rust Style Guide defines formatting rules for `Cargo.toml` itself. They're not enforced by a formatter today, but matching them keeps diffs clean and matches what the ecosystem expects.

```toml
# ❌ BAD: random key order, quoted keys, no spacing
[package]
"description"="A thing that does stuff"
"name"="my-crate"
authors=["alice@example.com"]
license="BSD"
version="0.1.0"
edition="2024"

# ✅ GOOD: name/version first, description last, bare keys, SPDX, full authors
[package]
name = "my-crate"
version = "0.1.0"
authors = ["Alice Smith <alice@example.com>"]
edition = "2024"
license = "MIT OR Apache-2.0"
repository = "https://github.com/example/my-crate"
description = """
Fast and ergonomic TOML parser with zero-copy deserialization.
"""

[dependencies]
# Version-sort keys within ordinary sections
serde = { version = "1.0", features = ["derive"] }
toml = "0.8"

# Inline table when it fits; break out otherwise
[dependencies.extremely_long_crate_name_goes_right_here]
path = "extremely_long_path_name_goes_right_here"
version = "4.5.6"
features = ["a", "b", "c"]
```

**Rationale**: Rules in the Rust Style Guide, Ch. 6: 100-column line width, 4-space indent, blank line only between sections, `[package]` first with `name`/`version` at the top and `description` last, version-sorted keys in all other sections, bare keys (no quotes) for standard names, single space around `=`, SPDX license expressions, `Full Name <email>` authors. The `MIT/Apache-2.0` shorthand is accepted by convention; `MIT OR Apache-2.0` is standard SPDX.

**See also**: CG-M-01 (section inventory), CG-PUB-01 (required metadata)

---

## CG-M-03: Override Dependencies with `[patch]`, Not Forks in `[dependencies]`

**Strength**: SHOULD

**Summary**: When you need to temporarily point at a fork or local copy of a third-party dep (including transitive ones), use `[patch]` at the top-level manifest. It rewrites the whole dependency graph without changing every call site.

```toml
# ❌ BAD: change every user to a git dep -- doesn't cover transitives
[dependencies]
serde = { git = "https://github.com/myfork/serde", branch = "fix-123" }
# `some_lib` still pulls its own `serde` from crates.io -> two copies, type mismatch

# ✅ GOOD: patch the registry itself -- transitives see the override
[dependencies]
serde = "1.0"
some_lib = "0.5"

[patch.crates-io]
serde = { git = "https://github.com/myfork/serde", branch = "fix-123" }

# ✅ GOOD: patch to a local checkout while debugging
[patch.crates-io]
hyper = { path = "../hyper" }

# ✅ GOOD: patch a non-crates.io source
[patch."https://github.com/rust-lang/my-source"]
my_dep = { path = "../my_dep" }
```

**Rationale**: `[patch]` only applies at the workspace root -- writing it in a member manifest has no effect. The patched version must be SemVer-compatible with what `[dependencies]` asks for, or the dep graph won't resolve. For a parallel major version (e.g., patching `0.5` while the registry has `0.6`), add an entry to `[dependencies]` as well. Remove patches before publishing: they don't end up in the packaged crate, but they do mean the patched version is what you tested against.

**See also**: CG-M-04 ([replace] is deprecated), CG-B-08 (git dependencies)

---

## CG-M-04: `[replace]` Is Deprecated -- Always Use `[patch]`

**Strength**: AVOID

**Summary**: `[replace]` predates `[patch]` and has narrower semantics: exact-version matching, no transitive rewriting, no support for non-registry sources. Every use case is better served by `[patch]`.

```toml
# ❌ BAD: deprecated; requires the exact version string
[replace]
"serde:1.0.180" = { git = "https://github.com/myfork/serde" }
# Only matches serde = "=1.0.180" in the lockfile;
# bumping lockfile breaks the override silently.

# ✅ GOOD: [patch] is range-based and actively maintained
[patch.crates-io]
serde = { git = "https://github.com/myfork/serde" }
```

**Rationale**: The Cargo reference flags `[replace]` as legacy. It's still processed, which is why you'll see it in old codebases, but no new feature work has been added to it since `[patch]` landed. `[patch]` is strictly more capable: it accepts semver ranges, supports non-registry sources, and is what the Cargo team documents as the recommended override mechanism.

**See also**: CG-M-03 ([patch] usage)

---

## CG-W-01: Choose Virtual or Rooted Workspace Deliberately

**Strength**: SHOULD

**Summary**: A workspace can be **virtual** (root `Cargo.toml` has `[workspace]` only, no `[package]`) or **rooted** (root is itself a crate plus a `[workspace]`). Pick the one that matches reality -- don't default to rooted because `cargo new` starts that way.

```toml
# ✅ GOOD: virtual workspace -- multi-crate monorepo with no "main" crate
# /Cargo.toml
[workspace]
resolver = "2"              # MUST set for virtual workspaces (CG-W-05)
members = ["app", "core", "macros", "cli"]

[workspace.package]
version = "0.4.0"
edition = "2024"
license = "MIT OR Apache-2.0"
repository = "https://github.com/example/myproject"

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
```

```toml
# ✅ GOOD: rooted workspace -- a single crate with internal sub-crates
# /Cargo.toml
[package]
name = "myapp"
version = "1.2.0"
edition = "2024"
# resolver is inferred from edition; "2" since 2021.

[workspace]
members = ["crates/macros", "crates/plugin-api"]

[dependencies]
# deps for myapp
```

```toml
# ❌ BAD: rooted workspace where the root crate is an empty shim
[package]
name = "monorepo-root"      # nothing uses this crate
version = "0.0.0"
[lib]
path = "dummy.rs"
[workspace]
members = ["app", "core"]
```

**Rationale**: Virtual workspaces separate project-level config (members, shared deps, workspace-wide lints) from crate-level config. Rooted workspaces are correct when one crate is obviously the product and the rest are internal implementation details. The dummy-root pattern is an anti-pattern: it means `cargo build` at the root silently builds nothing useful and `cargo publish` at the root is nonsense.

**See also**: CG-W-05 (resolver requirement), CG-B-10 (workspace basics)

---

## CG-W-02: Inherit Workspace Lints -- Member Must Opt In

**Strength**: SHOULD

**Summary**: `[workspace.lints]` defines lint policy once, but member crates don't inherit it automatically. Each member must declare `[lints] workspace = true` to pick it up. Make this a convention in your repo.

```toml
# ✅ GOOD: workspace root
# /Cargo.toml
[workspace]
members = ["app", "core", "cli"]

[workspace.lints.rust]
unsafe_code = "forbid"
missing_docs = "warn"

[workspace.lints.clippy]
pedantic = { level = "warn", priority = -1 }
unwrap_used = "deny"
expect_used = "deny"
```

```toml
# ✅ GOOD: every member opts in
# /core/Cargo.toml
[package]
name = "core"
version.workspace = true
edition.workspace = true

[lints]
workspace = true

[dependencies]
serde = { workspace = true }
```

```toml
# ❌ BAD: member forgets [lints] workspace = true
# /core/Cargo.toml
[package]
name = "core"
# ... lints from workspace are NOT applied.
# CI may pass for `cargo clippy -p app` but fail for `cargo clippy -p core`.
```

**Rationale**: The opt-in requirement prevents accidental lint changes when adding a member (e.g., a vendored crate you don't control). The same rule applies to `[package]` inheritance: `version.workspace = true`, `edition.workspace = true`, etc. Inheritable fields under `[workspace.package]` were stabilised in Cargo 1.64; `[workspace.lints]` requires Cargo 1.74.

**See also**: CG-L-02 (declarative lints), CG-M-02 (style)

---

## CG-W-03: Use Glob Patterns and `exclude` to Manage Many Members

**Strength**: CONSIDER

**Summary**: `workspace.members` accepts globs; `workspace.exclude` removes paths that a glob would otherwise match. In a large monorepo, this beats maintaining an explicit list that drifts from reality.

```toml
# ✅ GOOD: globs scale with the repo
[workspace]
members = [
    "crates/*",
    "services/*",
    "tools/*",
]
exclude = [
    "crates/experimental-*",   # opt out individual crates
    "tools/archived",
]

# ✅ GOOD: explicit list for small, stable workspaces
[workspace]
members = ["app", "core", "cli"]
```

```
# Directory layout matching the glob example
/Cargo.toml
/crates/
    auth/            # included
    database/        # included
    experimental-ml/ # excluded
/services/
    api/             # included
/tools/
    archived/        # excluded
    codegen/         # included
```

**Rationale**: Globs mean adding a new crate under `crates/` is a single `cargo new --lib crates/newthing` with no workspace edit. The `exclude` list lets you keep in-tree code (for grep-ability or shared CI) without it being built by default. Beware: excluded paths can still be dependencies of included crates via path specifiers -- they're excluded from the workspace membership, not from the dep graph.

**See also**: CG-W-04 (default-members), CG-W-01 (virtual workspaces)

---

## CG-W-04: Use `default-members` to Scope Default Commands

**Strength**: CONSIDER

**Summary**: In a workspace with many members, `cargo build` and `cargo test` run against every member. Set `workspace.default-members` to a subset -- typically the user-facing crates -- so the default command does what you want.

```toml
# ✅ GOOD: default builds the app binaries; tests still run everywhere with --workspace
[workspace]
members = [
    "crates/core",
    "crates/macros",
    "crates/plugin-a",
    "crates/plugin-b",
    "app",
    "cli",
]
default-members = ["app", "cli"]
```

```bash
# Now:
cargo build                  # builds only `app` and `cli`
cargo build --workspace      # builds everything
cargo test -p core           # tests one specific member
cargo test --workspace       # tests everything
```

**Rationale**: Without `default-members`, `cargo build` in a virtual workspace builds all members -- often including test-helper crates, generated code, or feature-flag probes that slow feedback. `default-members` does not affect `--workspace` or `-p` selection; it only changes the "no flag" default. Don't use it to hide work-in-progress crates: CI should still pass `--workspace`.

**See also**: CG-W-03 (members/exclude), CG-B-11 (workspace commands)

---

## CG-W-05: Set `resolver = "2"` Explicitly in Virtual Workspaces

**Strength**: MUST

**Summary**: A virtual workspace (no root `[package]`) does not have an edition, so Cargo cannot infer the feature resolver from it. You must set `resolver = "2"` in `[workspace]` or you get resolver v1 behaviour and a warning.

```toml
# ❌ BAD: virtual workspace without resolver -- warning + wrong feature unification
[workspace]
members = ["app", "core"]
# warning: virtual workspace defaulting to `resolver = "1"`

# ✅ GOOD: explicit resolver
[workspace]
resolver = "2"
members = ["app", "core"]

# ✅ GOOD: rooted workspace -- resolver inferred from [package] edition
[package]
name = "myapp"
edition = "2021"            # resolver 2 is the default for edition >= 2021
[workspace]
members = ["crates/macros"]
```

**Rationale**: Resolver v2 (the default since edition 2021) fixes a real bug in v1: under v1, enabling a feature for `build-dependencies` or `dev-dependencies` would leak that feature into the normal dep graph, causing bloat and sometimes compile failures. There is no reason to use v1 today; the only reason it exists as a default for virtual workspaces is backwards compatibility. A misconfigured resolver shows up as "features I didn't enable are on" in the output of `cargo tree -e features`.

**See also**: CG-BS-13 (optional deps and features), CG-W-01 (virtual workspaces)

---

## CG-ECO-01: Know the Core Ecosystem Tools

**Strength**: SHOULD

**Summary**: Several cargo extensions are near-standard. Knowing what each one does lets you reach for the right one instead of writing a shell script that half-solves the problem.

| Tool | Install | What it does |
|------|---------|--------------|
| `cargo-edit` | `cargo install cargo-edit` | Built-in since 1.62: `cargo add`, `cargo rm`, `cargo upgrade` for managing deps |
| `cargo-outdated` | `cargo install cargo-outdated` | Lists deps with newer versions available |
| `cargo-audit` | `cargo install cargo-audit` | Scans `Cargo.lock` against the RustSec advisory DB |
| `cargo-deny` | `cargo install cargo-deny` | Policy for licenses, bans, sources, advisories; CI-oriented |
| `cargo-machete` | `cargo install cargo-machete` | Finds unused dependencies declared in `Cargo.toml` |
| `cargo-udeps` | `cargo install cargo-udeps` | Like machete but uses compiler output (nightly only, more accurate) |
| `cargo-shear` | `cargo install cargo-shear` | Faster alternative to machete; checks workspaces |
| `cargo-hack` | `cargo install cargo-hack` | Feature-matrix testing -- `--each-feature`, `--feature-powerset` |
| `cargo-nextest` | `cargo install cargo-nextest` | Faster test runner with better output |
| `cargo-release` | `cargo install cargo-release` | Automates version bump, tag, publish |
| `cargo-expand` | `cargo install cargo-expand` | Shows code after macro expansion (nightly) |
| `cargo-flamegraph` | `cargo install cargo-flamegraph` | Profiling wrapper |
| `cargo-bloat` | `cargo install cargo-bloat` | Shows what's taking binary size |
| `cargo-tree` | built-in | `cargo tree`, `cargo tree -e features`, `cargo tree -i foo` |
| `cargo-llvm-cov` | `cargo install cargo-llvm-cov` | Coverage using LLVM source-based coverage |

```bash
# ✅ GOOD: a solid CI dep-hygiene suite
cargo fmt --all --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-features
cargo hack check --each-feature --no-dev-deps
cargo machete
cargo deny check        # requires a deny.toml
cargo audit             # advisories; can also live under cargo-deny
```

**Rationale**: None of these tools are required, but each solves a specific recurring problem. `cargo-deny` in particular is worth adopting early: it enforces license policy (critical for enterprise use), blocks known-vulnerable transitives, and flags duplicate versions of the same crate in your graph. Install via `cargo install --locked` to avoid transitive breakage; pin versions in CI with `cargo install --locked cargo-deny@0.14.22` so tool upgrades are intentional.

**See also**: CG-BS-14 (cargo hack for features), CG-A-11 (dep update strategy), CG-PUB-08 (release automation)

---

## Best Practices Summary

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| CG-M-01 | SHOULD | Know the full Cargo.toml section inventory |
| CG-M-02 | SHOULD | Follow Cargo.toml style conventions |
| CG-M-03 | SHOULD | Use `[patch]` for dep overrides |
| CG-M-04 | AVOID | Don't use `[replace]` -- use `[patch]` |
| CG-W-01 | SHOULD | Choose virtual vs rooted workspace deliberately |
| CG-W-02 | SHOULD | Inherit workspace lints; members opt in |
| CG-W-03 | CONSIDER | Use member globs + `exclude` at scale |
| CG-W-04 | CONSIDER | Use `default-members` to scope default commands |
| CG-W-05 | MUST | Set `resolver = "2"` in virtual workspaces |
| CG-ECO-01 | SHOULD | Know the core ecosystem tools |
