---
# === CORE IDENTIFICATION ===
concept: Cargo Configuration
slug: cargo-configuration

# === CLASSIFICATION ===
category: package-management
subcategory: build-configuration
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "06-config"
chapter_number: 6
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "config.toml"
  - ".cargo/config.toml"
  - "Cargo configuration"
  - "Cargo config"
  - "cargo config file"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-manifest-reference
extends: []
related:
  - cargo-profiles
  - cargo-environment-variables
  - cargo-registries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where does Cargo look for configuration files and in what order?"
  - "How does Cargo merge configuration from multiple config files?"
  - "How do I set Cargo configuration via environment variables?"
  - "What is the precedence order between config files, env vars, and --config flags?"
  - "What configuration keys are available for build settings, HTTP, networking, and registries?"
  - "How do I configure target-specific settings like linker and runner?"
  - "How do I set custom environment variables for build processes via [env]?"
  - "How do I include additional configuration files?"
  - "Where are credentials stored and how are they managed?"
  - "How do config-relative paths work?"
  - "How do I define command aliases?"
  - "How do I override build scripts via target.<triple>.<links>?"
---

# Quick Definition

Cargo's configuration system uses hierarchical TOML files (`.cargo/config.toml`) that are discovered by walking up from the current directory to the root, with values merged so that deeper (more specific) directories take precedence. Configuration can also be set via environment variables (with `CARGO_` prefix, taking precedence over files) and `--config` CLI overrides (taking highest precedence). The system covers build settings, profiles, registries, credentials, HTTP/network options, target-specific settings, source replacement, terminal output, and custom environment variables.

# Core Definition

The source explains that "Cargo allows local configuration for a particular package as well as global configuration. It looks for configuration files in the current directory and all parent directories" (Ch. 6). The hierarchical probe path goes from `$PWD/.cargo/config.toml` up through every parent to `$CARGO_HOME/config.toml` (defaulting to `$HOME/.cargo/config.toml`).

**Merging rules**: "Numbers, strings, and booleans will use the value in the deeper config directory taking precedence over ancestor directories, where the home directory is the lowest priority. Arrays will be joined together with higher precedence items being placed later in the merged array."

**Three-tier precedence**: (1) `--config` CLI overrides take highest precedence, (2) environment variables (`CARGO_FOO_BAR` for `foo.bar`) take precedence over files, (3) config files use hierarchical merging. The source states: "Environment variables will take precedence over TOML configuration files."

The **configuration keys** span many sections: `[alias]` for command shortcuts, `[build]` for compiler settings (jobs, rustc, rustflags, target, target-dir, incremental), `[env]` for custom environment variables in build processes, `[http]` for network settings (proxy, timeout, TLS), `[net]` for network behavior (retry, offline, git-fetch-with-cli, SSH known hosts), `[profile]` for profile overrides, `[registries]` and `[registry]` for package registries and credentials, `[source]` for source replacement, `[target]` for per-platform settings (linker, runner, rustflags), and `[term]` for terminal output.

# Prerequisites

- **Cargo Manifest Reference** -- configuration extends and overrides settings from `Cargo.toml`

# Key Properties

1. **Hierarchical discovery**: config files probed from `$PWD/.cargo/config.toml` up through all parent directories to `$CARGO_HOME/config.toml`
2. **Merge semantics**: scalars use deepest value; arrays are concatenated with deeper items placed later
3. **Env var mapping**: `foo.bar` becomes `CARGO_FOO_BAR` (uppercase, dots/dashes to underscores); env vars override files
4. **--config CLI**: accepts `KEY=VALUE` TOML syntax or path to extra config file; highest precedence
5. **include directive**: `include = ["path.toml"]` loads additional config files; supports optional includes
6. **[alias]**: defines command shortcuts; recursive and supports arrays of strings; built-in aliases include b, c, d, t, r, rm
7. **[build]**: jobs, rustc, rustc-wrapper, rustc-workspace-wrapper, target, target-dir, rustflags, rustdocflags, incremental
8. **[env]**: sets environment variables for build scripts and rustc; supports `force` and `relative` flags
9. **[target.<triple>]**: linker, runner, rustflags, rustdocflags per target; also supports `cfg()` expressions
10. **[target.<triple>.<links>]**: overrides build scripts for packages declaring a `links` key
11. **credentials**: stored in `$CARGO_HOME/credentials.toml`; managed by `cargo login`/`cargo logout`
12. **config-relative paths**: for config files, paths are relative to the parent of the `.cargo` directory
13. **workspace limitation**: Cargo does not read config files from crates within a workspace when invoked from workspace root
14. **rustflags precedence**: CARGO_ENCODED_RUSTFLAGS > RUSTFLAGS > target-specific config > build.rustflags (first match wins)

# Construction / Recognition

## Hierarchical Config Discovery:
```text
/projects/foo/bar/baz/.cargo/config.toml
/projects/foo/bar/.cargo/config.toml
/projects/foo/.cargo/config.toml
/projects/.cargo/config.toml
/.cargo/config.toml
$CARGO_HOME/config.toml
```

## Environment Variable Override:
```console
# Sets the equivalent of target.x86_64-unknown-linux-gnu.runner
CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_RUNNER="my-runner" cargo test
```

## --config CLI Override:
```console
cargo --config net.git-fetch-with-cli=true fetch
cargo --config profile.dev.package.image.opt-level=3 build
cargo --config ./path/to/extra-config.toml build
```

## Config File with Common Sections:
```toml
[alias]
b = "build"
rr = "run --release"

[build]
jobs = 4
target-dir = "target"
rustflags = ["-C", "target-cpu=native"]

[env]
OPENSSL_DIR = { value = "vendor/openssl", relative = true }

[target.x86_64-unknown-linux-gnu]
linker = "clang"
runner = "my-emulator"
```

## Include Directive:
```toml
include = [
    { path = "required.toml" },
    { path = "optional.toml", optional = true },
]
```

## Build Script Override via Config:
```toml
[target.x86_64-unknown-linux-gnu.foo]
rustc-link-lib = ["foo"]
rustc-link-search = ["/path/to/foo"]
rustc-cfg = ['key="value"']
rustc-env = {key = "value"}
```

# Context & Application

This card covers Cargo's configuration system as specified in Chapter 6 of the Cargo Reference. The hierarchical config file system allows project-specific, team-wide, and user-global settings to coexist and merge naturally. The env var override mechanism enables CI/CD pipelines and developer-specific overrides without modifying files. Key practical applications include: setting cross-compilation targets and linkers per project (`.cargo/config.toml` checked into VCS), configuring build caches via `RUSTC_WRAPPER` (e.g., sccache), defining command aliases for workflows, setting custom environment variables for OpenSSL and similar native dependencies, configuring HTTP proxies for corporate environments, overriding build scripts for system libraries, and managing registry authentication. The `[env]` section is particularly useful for reproducible builds by ensuring native dependency paths are consistent. The four-way rustflags precedence system (encoded env, env, target config, build config) is a frequent source of confusion that this chapter clarifies precisely.

# Examples

**Example 1** (Ch. 6): Complete config overview showing all major sections:
```toml
[alias]
b = "build"
c = "check"
t = "test"
r = "run"
rr = "run --release"

[build]
jobs = 1
rustc = "rustc"
target = "triple"
target-dir = "target"
rustflags = ["...", "..."]
incremental = true

[env]
ENV_VAR_NAME = "value"
ENV_VAR_NAME_2 = { value = "value", force = true }
ENV_VAR_NAME_3 = { value = "relative/path", relative = true }
```

**Example 2** (Ch. 6): Merging behavior for hierarchical config:
> "Numbers, strings, and booleans will use the value in the deeper config directory taking precedence over ancestor directories, where the home directory is the lowest priority. Arrays will be joined together with higher precedence items being placed later in the merged array."

**Example 3** (Ch. 6): Rustflags four-source precedence:
> "1. `CARGO_ENCODED_RUSTFLAGS` environment variable. 2. `RUSTFLAGS` environment variable. 3. All matching `target.<triple>.rustflags` and `target.<cfg>.rustflags` config entries joined together. 4. `build.rustflags` config value."

**Example 4** (Ch. 6): Target-specific cfg-based configuration:
```toml
[target.'cfg(all(target_arch = "arm", target_os = "none"))']
runner = "my-arm-wrapper"
rustflags = ["...", "..."]
```

**Example 5** (Ch. 6): Custom environment variables with relative paths:
```toml
[env]
OPENSSL_DIR = { value = "vendor/openssl", relative = true }
TMPDIR = { value = "/home/tmp", force = true }
```
> "`relative` flag evaluates the value as a config-relative path... The value of the environment variable will be the full absolute path."

# Relationships

## Builds Upon
- **Cargo Manifest Reference** -- config extends and can override manifest settings, particularly profiles and registry configuration

## Enables
- Per-project build customization checked into version control
- CI/CD configuration via environment variables
- Cross-compilation setup with target-specific linkers and runners
- Build script overriding for system library integration
- Source replacement for vendoring and mirroring

## Related
- **cargo-profiles** -- profiles can be defined and overridden in config files
- **cargo-environment-variables** -- env vars provide an alternative configuration mechanism; config keys have corresponding env var names
- **cargo-registries** -- registry configuration and credential management are part of the config system

## Contrasts With
- None within this source

# Common Errors

- **Error**: Placing a config file inside a workspace member crate and expecting it to be read when building from the workspace root.
  **Correction**: "When being invoked from a workspace, Cargo does not read config files from crates within the workspace." Config must be at or above the workspace root level.

- **Error**: Setting `RUSTFLAGS` and also `build.rustflags` in config and expecting both to apply.
  **Correction**: The four sources are "mutually exclusive" -- the first one found wins. If `RUSTFLAGS` is set, `build.rustflags` in config is ignored entirely.

- **Error**: Using `RUSTFLAGS` without `--target` and expecting flags to only apply to the project code.
  **Correction**: "Without `--target`, the flags will be passed to all compiler invocations (including build scripts and proc macros) because dependencies are shared."

- **Error**: Expecting the `.toml` extension file to take precedence when both `.cargo/config` and `.cargo/config.toml` exist.
  **Correction**: "If both files exist, Cargo will use the file without the extension."

# Common Confusions

- **Confusion**: Thinking config-relative paths are relative to the config file itself.
  **Clarification**: "For config files, paths are relative to the parent directory of the directory where the config files were defined." So a path in `/my/project/.cargo/config.toml` is relative to `/my/project/`, not to `/my/project/.cargo/`.

- **Confusion**: Thinking `[env]` variables override existing environment variables.
  **Clarification**: "By default, the variables specified will not override values that already exist in the environment. This behavior can be changed by setting the `force` flag."

- **Confusion**: Thinking `[patch]` in config and `Cargo.toml` combine.
  **Clarification**: "If a given dependency is patched both in a cargo configuration file and a `Cargo.toml` file, the patch in the configuration file is used." They do not merge.

- **Confusion**: Thinking target `cfg()` matching includes Cargo features or build script values.
  **Clarification**: "`cfg` values come from those built-in to the compiler... Do not try to match on `debug_assertions`, `test`, Cargo features like `feature=\"foo\"`, or values set by build scripts."

# Source Reference

Chapter 6: Configuration -- sections on hierarchical structure, configuration format (full TOML overview), environment variables, command-line overrides, including extra configuration files, config-relative paths, executable paths with arguments, credentials, and all configuration keys: paths, [alias], [build], [credential-alias], [doc], [cargo-new], [env], [future-incompat-report], [cache], [http], [install], [net], [patch], [profile], [resolver], [registries], [registry], [source], [target], and [term]. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 6 -- "This document explains how Cargo's configuration system works, as well as available keys or configuration"
- Confidence rationale: HIGH -- comprehensive documentation of all config keys with types, defaults, and environment variable mappings
- Uncertainties: Some config keys do not support environment variables due to technical issues; the `.cargo/config` (no .toml) compatibility may eventually be deprecated
- Cross-reference status: References cargo-profiles (Ch. 5), cargo-environment-variables (Ch. 7), cargo-build-cache (Ch. 9), cargo-registries (Ch. 12)
