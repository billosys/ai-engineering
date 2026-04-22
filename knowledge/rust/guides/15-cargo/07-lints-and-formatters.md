# Cargo Lints and Formatters

How to configure clippy and rustfmt at the manifest, config, and CI level. These patterns cover the user-facing side of the toolchain: turning lints on, declaring them declaratively, silencing false positives without losing discipline, and making formatting mechanical.

Pattern prefixes:

- `CG-L-XX` -- clippy usage and lint configuration
- `CG-F-XX` -- rustfmt usage and configuration

---

## CG-L-01: Run Clippy from the Developer Loop, Not Just CI

**Strength**: SHOULD

**Summary**: Use `cargo clippy` locally as a step between `cargo check` and `cargo test`. It catches bugs and idiom violations with almost the same latency as `check`, but finds issues that neither the compiler nor tests will.

```bash
# ❌ BAD: only run clippy on PR, find 30 issues at once
git push  # CI fails 10 minutes later with a pile of warnings

# ✅ GOOD: fast local loop
cargo check                          # 2s -- does it compile?
cargo clippy --all-targets           # 4s -- is it idiomatic?
cargo test                           # 20s -- does it work?

# Lint only your crate, not dependencies
cargo clippy --no-deps

# Lint a specific member of a workspace
cargo clippy -p my-crate --all-targets

# Apply machine-applicable suggestions automatically
cargo clippy --fix --allow-dirty --allow-staged
```

**Rationale**: `cargo clippy` reuses the same compilation artifacts as `cargo check`, so the second invocation is nearly free. `--all-targets` includes tests, examples, and benches, which otherwise get lint-ignored. Running it locally also prevents "clippy PR" commits that muddy history.

**See also**: CG-L-06 (CI enforcement), CG-B-13 (everyday command set)

---

## CG-L-02: Declare Lints in `[lints]` (Cargo 1.74+), Not Scattered Attributes

**Strength**: SHOULD

**Summary**: Since Cargo 1.74, a `[lints]` table in `Cargo.toml` lets you set lint levels once per crate. Prefer this over `#![warn(...)]` littered in `lib.rs` and over `RUSTFLAGS`. It composes with workspace inheritance and survives `cargo fix`.

```toml
# ❌ BAD: lint policy split across lib.rs, CI yaml, and a shell script
# lib.rs:
#![warn(clippy::pedantic)]
#![warn(missing_docs)]
# .github/workflows/ci.yml:
#   run: cargo clippy -- -D warnings -W clippy::nursery
# RUSTFLAGS="-W clippy::unwrap_used" cargo clippy

# ✅ GOOD: one source of truth in Cargo.toml
[lints.rust]
unsafe_code = "forbid"
missing_docs = "warn"

[lints.clippy]
pedantic = { level = "warn", priority = -1 }   # enable group at lower priority
unwrap_used = "deny"                           # specific lints win
expect_used = "deny"
module_name_repetitions = "allow"              # opt out of one pedantic lint

[lints.rustdoc]
broken_intra_doc_links = "deny"
```

**Rationale**: The `priority` field (default `0`) lets group settings act as a baseline that individual lints override -- set the group at `-1` so specific lints at priority `0` take precedence. The `[lints]` table is MSRV-gated to Cargo 1.74; older toolchains ignore it silently, which can surprise CI -- set `rust-version = "1.74"` or higher.

**See also**: CG-L-03 (allow discipline), CG-W-02 (workspace inheritance), CG-PUB-10 (rust-version/MSRV)

---

## CG-L-03: `#[allow(...)]` Must Be Narrow and Commented

**Strength**: SHOULD

**Summary**: When you silence a lint, do it at the smallest possible scope and leave a comment explaining why. Crate-wide `#![allow(clippy::too_many_arguments)]` is almost always wrong; an item-scoped allow with a one-line rationale almost always isn't.

```rust
// ❌ BAD: crate-wide silencer, no context
#![allow(clippy::unwrap_used)]
#![allow(clippy::missing_errors_doc)]

// ❌ BAD: item allow with no explanation
#[allow(clippy::too_many_arguments)]
pub fn render(a: u32, b: u32, c: u32, d: u32, e: u32, f: u32, g: u32, h: u32) { /* ... */ }

// ✅ GOOD: narrow scope, explains why the lint is wrong here
impl Config {
    // The builder pattern legitimately takes many args once, at the call site.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        host: String, port: u16, tls: bool, user: String,
        pass: String, db: String, timeout: Duration, retries: u32,
    ) -> Self { /* ... */ }
}

// ✅ GOOD: expression-level allow for a single unwrap
let value = CONFIG.get()
    // Safe: set_once runs before any reader in main().
    .unwrap_or_else(|| unreachable!());
```

**Rationale**: Unscoped allows decay: the reason they were added becomes invisible, and later refactors carry them forward unnecessarily. A scoped `#[allow(...)]` with a comment is a documented exception; a crate-wide one is a quiet opt-out. Prefer `#[expect(...)]` (Rust 1.81+) when available -- it warns if the lint stops firing, catching dead exemptions.

**See also**: CG-L-02 (declarative lint policy), CG-L-05 (restriction group)

---

## CG-L-04: Tune Lints with `clippy.toml`, Not Environment Variables

**Strength**: SHOULD

**Summary**: Some clippy lints take parameters (type-complexity threshold, disallowed names, disallowed types, MSRV). Configure them in `clippy.toml` (or `.clippy.toml`) at the crate/workspace root rather than via env vars or per-invocation flags.

```toml
# clippy.toml at workspace root

# Raise the type-complexity threshold for generated code
type-complexity-threshold = 350

# Ban specific identifiers
disallowed-names = ["foo", "bar", "baz", "tmp"]

# Ban specific types / methods
disallowed-types = [
    { path = "std::sync::Mutex", reason = "use parking_lot::Mutex" },
]
disallowed-methods = [
    { path = "std::env::set_var", reason = "not thread-safe; use a config layer" },
]

# Gate MSRV-dependent suggestions
msrv = "1.74"

# Extend the default list (use `..` to keep defaults)
doc-valid-idents = ["..", "MyProduct", "OpenGL"]
```

**Rationale**: `clippy.toml` lives next to `Cargo.toml`, is discovered automatically, and applies uniformly to every `cargo clippy` invocation -- CI, local, editor. Setting `msrv` here makes clippy suppress suggestions that require newer Rust (e.g., `let ... else`), which matters for libraries with older MSRVs. Use `..` in list options to extend the built-in defaults instead of replacing them.

**See also**: CG-L-02 (lint levels in Cargo.toml), CG-PUB-10 (MSRV)

---

## CG-L-05: Never Enable `clippy::restriction` as a Group -- Cherry-Pick

**Strength**: MUST

**Summary**: The `clippy::restriction` group is a grab-bag of opinionated lints, some of which contradict each other (one forbids `unwrap`, another suggests it elsewhere). Enabling it wholesale produces noise that cannot be resolved. Cherry-pick individual restriction lints instead.

```toml
# ❌ BAD: enabling the whole group causes contradictory warnings
[lints.clippy]
restriction = "warn"

# ✅ GOOD: cherry-pick the ones you actually want
[lints.clippy]
# Force explicit error handling in libraries
unwrap_used = "deny"
expect_used = "deny"
# Forbid implicit float truncation
as_conversions = "warn"
# Require explicit returns of () -- matter of taste, not contradictory
needless_return = "allow"    # suppress the default-warn version if desired
```

```rust
// ✅ GOOD: example of a cherry-picked restriction lint catching a real bug
#[deny(clippy::unwrap_used)]
fn parse_config(path: &Path) -> Result<Config, Error> {
    let text = std::fs::read_to_string(path)?;
    // would be `toml::from_str(&text).unwrap()` -- caught by the lint
    Ok(toml::from_str(&text)?)
}
```

**Rationale**: The Clippy docs are explicit: "You shouldn't enable the whole lint group, but cherry-pick lints." The group exists as a catalogue of available opt-ins, not as a recommended baseline. Common picks: `unwrap_used`, `expect_used`, `panic`, `todo`, `unimplemented`, `print_stdout` (for libraries), `dbg_macro`.

**See also**: CG-L-02 (declarative lint config), CG-L-03 (allow discipline)

---

## CG-L-06: Enforce Lints in CI with `-D warnings`

**Strength**: SHOULD

**Summary**: A warning that CI tolerates is a warning that will be committed. Run clippy in CI with `-D warnings` so any warning fails the build; developers fix them locally instead of accumulating debt.

```yaml
# ❌ BAD: warnings silently accumulate
- run: cargo clippy --all-targets --all-features

# ✅ GOOD: fail on any warning, including rustc warnings, from any target
- run: cargo clippy --workspace --all-targets --all-features -- -D warnings

# ✅ GOOD: with a separate fmt check
- run: cargo fmt --all --check
- run: cargo clippy --workspace --all-targets --all-features -- -D warnings
- run: cargo test --workspace --all-features
```

```toml
# Alternative: set lint levels in Cargo.toml so -D warnings is redundant
# but also works for developers who forget.
[lints.clippy]
all = { level = "deny", priority = -1 }
pedantic = { level = "warn", priority = -1 }
```

**Rationale**: `-D warnings` promotes every warning to a deny-level diagnostic, including warnings from `rustc` (not just clippy). Pair with `--all-targets` to lint tests/examples/benches and `--all-features` (or an explicit matrix) to cover feature-gated code. For libraries, combine with `cargo hack` (see CG-BS-14) to ensure lints pass for every feature combination.

**See also**: CG-L-02 (declarative lints), CG-BS-14 (feature matrix), CG-A-08 (CI pipeline)

---

## CG-F-01: `cargo fmt --all --check` in CI, `cargo fmt --all` Locally

**Strength**: MUST

**Summary**: Formatting should be mechanical: there is one correct answer per file, and a machine produces it. In CI, run `cargo fmt --all --check` to fail on unformatted code. Locally, run `cargo fmt --all` to apply it. Never review formatting in PRs.

```yaml
# ❌ BAD: formatting concerns leak into code review
# reviewer: "can you fix the indentation on line 47"

# ✅ GOOD: CI rejects anything unformatted
jobs:
  fmt:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: rustup component add rustfmt
      - run: cargo fmt --all --check
```

```bash
# Local: format the whole workspace (all members, all targets)
cargo fmt --all

# Format one crate only
cargo fmt -p my-crate

# Format a specific file (bypasses Cargo.toml discovery)
rustfmt src/lib.rs

# See what would change without applying
cargo fmt --all -- --check --verbose
```

**Rationale**: `--all` descends into workspace members; without it, `cargo fmt` formats only the current package. `--check` returns nonzero on diff, which is what CI wants. Formatting in a separate commit keeps diffs reviewable; formatting as part of a feature commit mixes noise with intent.

**See also**: CG-F-02 (rustfmt.toml), CG-F-03 (editor/hook integration)

---

## CG-F-02: Pin Formatting Rules in `rustfmt.toml` with `style_edition`

**Strength**: SHOULD

**Summary**: Put a `rustfmt.toml` (or `.rustfmt.toml`) at the workspace root and set `style_edition` to the Rust edition whose formatting rules you want. Without it, your formatting floats with the toolchain; with it, formatting is reproducible.

```toml
# rustfmt.toml at workspace root

# Lock in the formatting rules for a specific edition
# (Rust 1.75+; defaults to `edition` from Cargo.toml if unset)
style_edition = "2024"

# Common tweaks
max_width = 100                # default; matches the Rust Style Guide
hard_tabs = false
newline_style = "Unix"
use_field_init_shorthand = true
use_try_shorthand = true

# Import grouping (2024 default; explicit for older toolchains)
group_imports = "StdExternalCrate"
imports_granularity = "Crate"

# Stable wrap for long literals
wrap_comments = false          # unstable on stable rustfmt
```

```rust
// Effect of group_imports = "StdExternalCrate", imports_granularity = "Crate"

// ❌ BAD (unformatted)
use crate::foo::Bar;
use std::collections::HashMap;
use serde::Deserialize;
use crate::foo::Baz;
use std::io::Read;

// ✅ GOOD (after cargo fmt)
use std::{collections::HashMap, io::Read};

use serde::Deserialize;

use crate::foo::{Bar, Baz};
```

**Rationale**: `style_edition` decouples formatting rules from the compiler edition, so you can upgrade the toolchain without reformatting. Options marked "unstable" in the rustfmt docs only work on nightly -- stick to stable options to keep CI on stable rustc. The 100-column width matches the Rust Style Guide and is also what `Cargo.toml` conventions use.

**See also**: CG-M-02 (Cargo.toml style), CG-F-01 (fmt in CI)

---

## CG-F-03: Automate Formatting on Save and at Commit Time

**Strength**: CONSIDER

**Summary**: Running `cargo fmt` manually is forgettable. Wire it into the editor (format on save) and a pre-commit hook so unformatted code never reaches a branch. This removes the only remaining human step in the formatting loop.

```jsonc
// .vscode/settings.json (rust-analyzer)
{
    "[rust]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "rust-lang.rust-analyzer"
    },
    "rust-analyzer.rustfmt.rangeFormatting.enable": true
}
```

```yaml
# .pre-commit-config.yaml (uses https://pre-commit.com)
repos:
  - repo: https://github.com/doublify/pre-commit-rust
    rev: v1.0
    hooks:
      - id: fmt
        args: [--all, --]
      - id: clippy
        args: [--all-targets, --, -D, warnings]
```

```bash
# Minimal git hook, no framework
# .git/hooks/pre-commit
#!/bin/sh
cargo fmt --all --check || {
    echo "Run 'cargo fmt --all' to fix formatting."
    exit 1
}
```

**Rationale**: Format-on-save is free once configured; pre-commit hooks catch the case where you edit outside the IDE. Both are strictly optional -- CI remains the enforcement layer (CG-F-01) -- but they dramatically cut feedback latency from "CI failed" (minutes) to "editor saved" (milliseconds).

**See also**: CG-F-01 (CI enforcement), CG-L-01 (clippy in the dev loop)

---

## Best Practices Summary

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| CG-L-01 | SHOULD | Run clippy between `check` and `test` locally |
| CG-L-02 | SHOULD | Put lint levels in `[lints]` (Cargo 1.74+) |
| CG-L-03 | SHOULD | `#[allow(...)]` must be narrow and commented |
| CG-L-04 | SHOULD | Tune lint parameters in `clippy.toml` |
| CG-L-05 | MUST | Cherry-pick `clippy::restriction`; never enable the group |
| CG-L-06 | SHOULD | CI: `cargo clippy ... -- -D warnings` |
| CG-F-01 | MUST | CI: `cargo fmt --all --check` |
| CG-F-02 | SHOULD | Pin rules in `rustfmt.toml` with `style_edition` |
| CG-F-03 | CONSIDER | Format on save + pre-commit hook |
