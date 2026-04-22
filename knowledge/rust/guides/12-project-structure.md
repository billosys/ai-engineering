# Project Structure Guidelines

Patterns for organizing Rust projects: crates and workspaces, the module system and visibility, `src/` layout conventions, feature flags, lockfile discipline, MSRV and edition policy, testing scaffolding, and the different rules that apply to libraries versus applications.


## PS-01: Cargo Project Layout Follows Convention

**Strength**: MUST

**Summary**: Place files in the conventional directories so Cargo can auto-discover targets without explicit configuration.

```text
my-crate/
├── Cargo.toml
├── Cargo.lock
├── src/
│   ├── lib.rs            # library crate root
│   ├── main.rs           # binary crate root (same package OK)
│   └── bin/
│       ├── tool-a.rs     # → binary `tool-a`
│       └── tool-b/
│           ├── main.rs   # → binary `tool-b` (multi-file)
│           └── helper.rs
├── tests/                # integration tests (one binary per file)
│   └── smoke.rs
├── benches/              # cargo bench targets
│   └── throughput.rs
├── examples/             # runnable examples (cargo run --example)
│   └── quickstart.rs
├── build.rs              # optional build script
└── target/               # cargo output (gitignored)
```

**Rationale**: Cargo discovers targets from file placement. Fighting the layout (e.g., mixing integration tests into `src/`, renaming `lib.rs`) requires manual `[[bin]]` / `[[test]]` entries and surprises every contributor. Target names use `kebab-case`; module names use `snake_case`.

**See also**: PS-21, PS-23


## PS-02: Binary and Library Separation

**Strength**: SHOULD

**Summary**: Put real logic in `lib.rs`; keep `main.rs` a thin wrapper that parses arguments, wires dependencies, and calls into the library.

```rust
// ✅ src/lib.rs — testable, reusable
pub mod commands;
pub mod config;
pub mod error;

pub use config::Config;
pub use error::{Error, Result};

pub fn run(config: &Config) -> Result<()> {
    commands::build(config)?;
    Ok(())
}

// ✅ src/main.rs — thin, ~10-20 lines
use my_tool::{Config, run};

fn main() -> std::process::ExitCode {
    let config = match Config::from_args() {
        Ok(c) => c,
        Err(e) => { eprintln!("{e}"); return std::process::ExitCode::from(2); }
    };
    match run(&config) {
        Ok(()) => std::process::ExitCode::SUCCESS,
        Err(e) => { eprintln!("error: {e}"); std::process::ExitCode::FAILURE }
    }
}
```

**Rationale**: Integration tests and benchmarks can only import the library crate. Logic that lives in `main.rs` is unreachable from `tests/` and untestable except through subprocess exec. The library also becomes reusable from other binaries or downstream crates.


## PS-03: Application vs Library — Different Rules Apply

**Strength**: MUST

**Summary**: Applications and libraries have different obligations around error types, allocators, MSRV, and dependency leakage. Don't apply library rules to application code or vice versa.

| Concern | Library | Application |
|---------|---------|-------------|
| Error types | Situation-specific structs (EH guide) | `anyhow`/`eyre` permitted |
| Public API | Stable, semver-careful | Internal; can churn freely |
| Dependency leakage | Avoid (`std` types in signatures) | No external API to protect |
| `Cargo.lock` | Commit in bin crates; optional for pure libs | Always commit |
| MSRV | Declared and tested (PS-11) | Whatever your toolchain supports |
| Allocator | Don't set global allocator | `#[global_allocator]` (e.g., mimalloc) |

```rust
// ✅ Application main.rs — eyre is fine
use eyre::Result;
fn main() -> Result<()> {
    run_server()?;
    Ok(())
}

// ✅ Library error type — canonical struct
#[derive(Debug, thiserror::Error)]
#[error("parse error at line {line}: {message}")]
pub struct ParseError { pub line: usize, pub message: String }
```

**Rationale**: An application is the terminal consumer of errors — it logs, displays, or exits. A library is a middle node whose errors must be structured for downstream handling. A library that returns `anyhow::Error` hands its consumers an opaque trait object. An application that defines bespoke error enums for every module pays for architecture it doesn't need.

**See also**: M-APP-ERROR, M-ERRORS-CANONICAL-STRUCTS, PS-10


## PS-04: Module Declaration, Visibility, and `use`

**Strength**: MUST

**Summary**: Understand the three-keyword dance: `mod` declares a module (once per tree position), `pub` exposes items, `use` creates shortcuts in one scope.

```rust
// src/lib.rs — crate root
mod internal;        // private — only this crate sees it
pub mod error;       // public module — but contents need their own `pub`
pub mod config;

pub use config::Config;         // re-export at crate root (PS-06)
pub use error::{Error, Result};

// src/config.rs
use std::path::PathBuf;

pub struct Config {
    pub path: PathBuf,           // public field — see TD-05 for when to allow
    timeout_ms: u32,             // private field
}

impl Config {
    pub fn new(path: PathBuf) -> Self {
        Self { path, timeout_ms: 30_000 }
    }
    pub(crate) fn timeout_ms(&self) -> u32 { self.timeout_ms }
}
```

**Rationale**: `mod foo;` is a declaration that loads the file exactly once; it is not `import` or `#include`. Marking a module `pub` only permits other code to _name_ the module — every item inside still needs its own `pub`. Idiomatic `use`: bring the parent module into scope for functions (`module::func()`), bring the full path for types (`HashMap`).

**See also**: PS-05, PS-06


## PS-05: Pick the Most Restrictive Visibility That Works

**Strength**: MUST

**Summary**: Default is private. Escalate to `pub(super)`, `pub(crate)`, or `pub(in path)` before `pub`.

```rust
// Visibility spectrum, in order of exposure:
struct Private;                        // current module only
pub(super) struct ParentVisible;       // parent module
pub(crate) struct CrateInternal;       // anywhere in this crate
pub(in crate::net) struct PathScoped;  // a specific subtree
pub struct PublicApi;                  // exported from the crate

// Mixed-visibility struct
pub struct Session {
    pub id: SessionId,             // public field
    pub(crate) token: Token,       // shared within the crate
    internal_state: State,         // private
}
```

**Rationale**: Every `pub` expands the commitment surface of your crate. `pub(crate)` is the workhorse for "I need this in a sibling module, but it is not API." When you later refactor, narrow visibility cuts the search space for who might break.


## PS-06: Re-export at Crate Root for a Flat Public API

**Strength**: SHOULD

**Summary**: Organize internals by domain, then `pub use` the important types at the crate root so consumers write `my_crate::Client` not `my_crate::client::pool::Client`.

```rust
// src/lib.rs — flat public API
pub use client::{Client, ClientBuilder};
pub use error::{Error, Result};
pub use server::Server;

// Internal modules — organized for development convenience
mod client;
mod server;
mod protocol;

// Private helper that's only used inside the crate
mod internal;
```

```rust
// ❌ forces deep imports on every consumer
use my_crate::client::builder::tls::TlsClientBuilder;

// ✅ flat public surface
use my_crate::TlsClientBuilder;
```

**Rationale**: Re-exports decouple the internal module tree from the published API. You can reorganize `src/` freely as long as the re-exports stay put. Group re-exports near the top of `lib.rs` so the public API is visible in one place.


## PS-07: Never Glob Re-export from Private Modules

**Strength**: MUST

**Summary**: Use explicit `pub use module::{A, B, C}`. Reserve `pub use module::*` for platform-HAL patterns where exactly one module is active.

```rust
// ❌ BAD — silently exports every new item
pub use internal::*;

// ✅ GOOD — explicit, greppable
pub use internal::{Parser, Token};

// ✅ OK — platform HAL, exactly one active
#[cfg(target_os = "linux")]
pub use linux::*;
#[cfg(target_os = "windows")]
pub use windows::*;
```

**Rationale**: Glob re-exports make code review useless — a reviewer can't tell from a diff whether a new public item was _intentionally_ exported. Explicit lists surface API surface changes in version control.

**See also**: M-NO-GLOB-REEXPORTS


## PS-08: Prefer Small, Focused Crates

**Strength**: SHOULD

**Summary**: When a module can reasonably be used on its own, split it into a separate crate. Err on the side of too many crates rather than too few.

```text
# ❌ monolithic
my-framework/
└── src/
    ├── client.rs
    ├── server.rs
    ├── protocol.rs
    └── macros.rs   # users pay to compile everything

# ✅ split
my-framework/           # umbrella (optional)
├── my-framework-core/   # shared protocol types
├── my-framework-client/ # client only
├── my-framework-server/ # server only
└── my-framework-macros/ # proc macros (must be its own crate)
```

**Rationale**: The crate is Rust's parallel-compilation unit; smaller crates compile faster, especially incrementally. Splitting also prevents cyclic dependencies, lets consumers depend only on what they need, and turns `pub(crate)` leaks into motivated API design. Proc macros _must_ live in their own crate — there is no alternative.

**See also**: M-SMALLER-CRATES, PS-09


## PS-09: Umbrella Crate with Feature-Gated Re-exports

**Strength**: CONSIDER

**Summary**: For split-crate projects, provide an umbrella crate that re-exports the pieces. Gate optional components behind features.

```toml
# my-framework/Cargo.toml
[package]
name = "my-framework"
version = "1.0.0"

[features]
default = ["client", "server"]
client = ["dep:my-framework-client"]
server = ["dep:my-framework-server"]
macros = ["dep:my-framework-macros"]

[dependencies]
my-framework-core = { version = "1", path = "../my-framework-core" }
my-framework-client = { version = "1", path = "../my-framework-client", optional = true }
my-framework-server = { version = "1", path = "../my-framework-server", optional = true }
my-framework-macros = { version = "1", path = "../my-framework-macros", optional = true }
```

```rust
// my-framework/src/lib.rs
pub use my_framework_core::*;

#[cfg(feature = "client")]
pub use my_framework_client as client;

#[cfg(feature = "server")]
pub use my_framework_server as server;

#[cfg(feature = "macros")]
pub use my_framework_macros::derive_proto;
```

**Rationale**: The umbrella gives consumers one name to depend on and one version line to upgrade. Advanced users can depend on individual crates directly when they want to minimize transitive deps. Umbrellas that pin sibling versions with `=` or exact requirements keep the ecosystem consistent.


## PS-10: Don't Leak External Types in the Public API

**Strength**: SHOULD

**Summary**: Prefer `std` types in public signatures. If a third-party type must appear, gate it behind a feature flag so consumers opt in.

```rust
// ❌ leaks bytes::Bytes — users locked to your version of bytes
pub fn parse(input: bytes::Bytes) -> ParsedMessage { /* ... */ }

// ✅ accept std slice — no bytes dependency leaks
pub fn parse(input: &[u8]) -> ParsedMessage { /* ... */ }

// ✅ or gate the interop behind a feature
#[cfg(feature = "bytes")]
pub fn parse_bytes(input: bytes::Bytes) -> ParsedMessage { /* ... */ }
```

**Rationale**: Any type in your public API becomes part of your semver contract. Only `std` types carry a permanent stability guarantee. Leaking `bytes::Bytes` locks your consumers into whatever version of `bytes` you depend on; a diamond-dependency collision forces every consumer to upgrade in lockstep.

**See also**: M-DONT-LEAK-TYPES, M-HIDE-DEPS


## PS-11: Declare an MSRV and Test It

**Strength**: SHOULD

**Summary**: Set `rust-version` in `Cargo.toml`. Treat MSRV bumps as breaking changes for libraries; test the declared MSRV in CI.

```toml
[package]
name = "my-crate"
version = "0.4.2"
edition = "2024"
rust-version = "1.75"   # MSRV declared
```

```yaml
# .github/workflows/ci.yml — test the MSRV in CI
- uses: dtolnay/rust-toolchain@master
  with:
    toolchain: "1.75"
- run: cargo check --all-features
```

**Rationale**: Consumers pin their toolchain conservatively. Silent bumps in your MSRV break them without a version signal. Declaring `rust-version` also lets Cargo's resolver prefer dependency versions that match. For applications, MSRV is less critical — you control the build toolchain — but the field still documents intent.


## PS-12: Pick an Edition Deliberately

**Strength**: MUST

**Summary**: Set `edition` in `Cargo.toml` to the latest edition your MSRV supports. Editions change lexer/parser rules but not runtime semantics.

```toml
[package]
edition = "2024"          # or "2021", "2018", "2015"
```

**Rationale**: Editions enable cleaner syntax (e.g., disjoint captures, `let_chains`, changes to the prelude) without forcing the whole ecosystem to upgrade at once. Crates of different editions interoperate freely. Without a declared edition, Cargo defaults to 2015 for backward compatibility — almost never what you want.


## PS-13: Features Are Additive

**Strength**: MUST

**Summary**: Every feature must be purely additive. Adding a feature may only _add_ items, never remove or modify them. Every feature combination must compile.

```rust
// ❌ BAD — subtractive: enabling `no-std` removes items
#[cfg(not(feature = "no-std"))]
use std::collections::HashMap;

// ✅ GOOD — additive: enabling `std` adds std-dependent items
#[cfg(feature = "std")]
use std::collections::HashMap;

#[cfg(not(feature = "std"))]
use hashbrown::HashMap;

// ❌ BAD — mutually exclusive features
#[cfg(all(feature = "tokio", not(feature = "async-std")))]
pub mod tokio_runtime;

// ✅ GOOD — both can coexist
#[cfg(feature = "tokio")]
pub mod tokio_runtime;
#[cfg(feature = "async-std")]
pub mod async_std_runtime;
```

**Rationale**: Cargo unifies features across the dependency graph. If crate A enables `feature-x` on your crate and crate B enables `feature-y`, both must compile together — Cargo will not choose between them. Subtractive features cause "works on my machine" breakage whenever two consumers disagree on what to disable.

**See also**: M-FEATURES-ADDITIVE


## PS-14: Optional Dependencies and Feature Gates

**Strength**: SHOULD

**Summary**: Optional dependencies are the canonical way to make a feature pay for itself. Gate the code _and_ the dependency together.

```toml
[dependencies]
serde = { version = "1", optional = true }
tokio = { version = "1", features = ["rt", "macros"], optional = true }

[features]
default = []
serde = ["dep:serde"]               # activate the crate named serde
async-tokio = ["dep:tokio"]         # explicit dep: prefix (Rust 2021+)
full = ["serde", "async-tokio"]     # feature aggregation
```

```rust
// src/lib.rs — gate the impls, not just the module
pub struct Event { /* ... */ }

#[cfg(feature = "serde")]
impl serde::Serialize for Event {
    fn serialize<S: serde::Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        /* ... */
        todo!()
    }
}
```

**Rationale**: Users who don't need `serde` support shouldn't compile `serde`. The `dep:` prefix (Rust 2021+) decouples feature names from dependency names — otherwise enabling `[features] foo = [...]` silently creates a `foo` feature on every optional dep of the same name.


## PS-15: Dev-Dependencies for Tests, Benches, and Examples

**Strength**: MUST

**Summary**: Put test-only, bench-only, and example-only dependencies in `[dev-dependencies]`. They are not part of your published crate.

```toml
[dependencies]
serde = "1"

[dev-dependencies]
criterion = "0.5"
tempfile = "3"
tokio = { version = "1", features = ["full", "test-util"] }

[[bench]]
name = "throughput"
harness = false          # required for criterion
```

**Rationale**: Consumers don't need your test fixtures. Dev-dependencies never appear in your published crate's dependency graph, don't count against MSRV, and don't participate in feature unification for release builds. Putting `criterion` in `[dependencies]` would force every downstream user to compile it.


## PS-16: Gate Test Utilities Behind a `test-util` Feature

**Strength**: MUST

**Summary**: Mocks, safety bypasses, and inspectors that expose internals must live behind a `test-util` feature — never unconditionally.

```rust
// Gate the mock constructor
impl Database {
    pub fn new(url: &str) -> Result<Self, DbError> { /* ... */ todo!() }

    #[cfg(feature = "test-util")]
    pub fn new_mocked() -> (Self, MockCtrl) { /* ... */ todo!() }
}

// Gate safety bypasses
impl HttpClient {
    #[cfg(feature = "test-util")]
    pub fn bypass_certificate_checks(&mut self) {
        self.verify_tls = false;
    }
}

// Gate whole mock modules
#[cfg(feature = "test-util")]
pub mod mock {
    pub struct MockCtrl { /* ... */ }
}
```

```toml
[features]
default = []
test-util = []
```

**Rationale**: Test utilities often bypass safety checks or expose private state. If they're unconditionally public, consumers can (and will) use them in production. A feature flag ensures they only compile when explicitly requested, typically in `[dev-dependencies]` of downstream tests.

**See also**: M-TEST-UTIL


## PS-17: Conditional Compilation with `#[cfg]`

**Strength**: SHOULD

**Summary**: Use `#[cfg(...)]` for platform, feature, and build-profile variations. Keep the predicate close to the item it guards.

```rust
// Platform-specific
#[cfg(target_os = "linux")]
fn home_dir() -> PathBuf { PathBuf::from(std::env::var("HOME").unwrap()) }

#[cfg(target_os = "windows")]
fn home_dir() -> PathBuf { PathBuf::from(std::env::var("USERPROFILE").unwrap()) }

// Feature-gated async variant
#[cfg(feature = "async")]
pub async fn fetch(&self) -> Result<Data> { /* ... */ todo!() }

// Test-only helper
#[cfg(test)]
fn fixture() -> Data { /* ... */ todo!() }

// Debug-only expensive assertion
#[cfg(debug_assertions)]
fn validate(&self) { /* ... */ }

// Combined predicates
#[cfg(all(unix, feature = "async"))]
fn unix_async() { /* ... */ }

#[cfg(any(target_os = "linux", target_os = "macos"))]
fn posix() { /* ... */ }
```

**Rationale**: `#[cfg]` is evaluated at compile time — the guarded code is not parsed as Rust if the predicate is false (only as a token tree). Prefer it over runtime branches for platform code because the LSP and `cargo check` will still validate inactive branches when you switch targets.


## PS-18: Module Files — `foo.rs` vs `foo/mod.rs`

**Strength**: SHOULD

**Summary**: Prefer the modern `foo.rs` + `foo/` submodule form. Use `foo/mod.rs` only when you specifically want the module's own file to live with its children.

```text
# ✅ modern layout (preferred)
src/
├── lib.rs
├── parser.rs              # module `parser`
└── parser/
    ├── lexer.rs           # module `parser::lexer`
    └── ast.rs             # module `parser::ast`

# legacy (also supported)
src/
├── lib.rs
└── parser/
    ├── mod.rs             # module `parser`
    ├── lexer.rs
    └── ast.rs
```

**Rationale**: The `parser.rs` form keeps the module's code alongside its siblings in the file tree; the `mod.rs` form sinks it into the directory. The modern form is easier to navigate because every module has a unique filename. Don't mix the two in one crate.


## PS-19: Use a Dedicated Error Module

**Strength**: SHOULD

**Summary**: Centralize error types in `src/error.rs` and re-export at the crate root. Libraries follow canonical-struct error design.

```rust
// src/error.rs
use std::backtrace::Backtrace;

#[derive(Debug, thiserror::Error)]
#[error("{kind}")]
pub struct Error {
    kind: ErrorKind,
    #[source]
    source: Option<Box<dyn std::error::Error + Send + Sync>>,
    backtrace: Backtrace,
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum ErrorKind {
    #[error("I/O failure")]
    Io,
    #[error("parse error at line {line}")]
    Parse { line: usize },
    #[error("not found: {0}")]
    NotFound(String),
}

impl Error {
    pub fn is_not_found(&self) -> bool { matches!(self.kind, ErrorKind::NotFound(_)) }
    pub fn is_io(&self) -> bool { matches!(self.kind, ErrorKind::Io) }
}

pub type Result<T> = std::result::Result<T, Error>;
```

```rust
// src/lib.rs
mod error;
pub use error::{Error, Result};
```

**Rationale**: Keeping the inner `ErrorKind` `pub(crate)` lets you add variants without breaking consumers; they interact via `is_*()` helper methods. See the error-handling guide (`03-error-handling.md`) for the full design.

**See also**: M-ERRORS-CANONICAL-STRUCTS


## PS-20: Prelude Module for Frequently-Used Items

**Strength**: CONSIDER

**Summary**: Provide `prelude` only for items users _will_ import everywhere. Don't dump the whole API into it.

```rust
// src/prelude.rs
//! Commonly-used items.
//!
//! ```
//! use my_crate::prelude::*;
//! ```

pub use crate::{Error, Result};
pub use crate::traits::{Serialize, Deserialize};
// ⚠️ only add items that are:
// 1. Used in most user code
// 2. Distinctively named (unlikely to collide)
// 3. Stable across versions
```

**Rationale**: A prelude is a glob-import invitation, which means it competes with every other glob import in the user's scope. Reserve it for traits needed in nearly every module (`Read`, `Write` analogues) and the canonical `Error` / `Result`. Don't prelude concrete types users import case-by-case.


## PS-21: Unit Tests In-File, Integration Tests in `tests/`

**Strength**: MUST

**Summary**: Unit tests go in a `#[cfg(test)] mod tests` block in the same file. Integration tests go in `tests/`, test the public API only, and each file compiles to its own binary.

```rust
// src/parser.rs — unit tests with access to private items
pub fn parse(input: &str) -> Result<Ast, ParseError> { /* ... */ todo!() }

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_basic_input() {
        assert!(parse("x = 1").is_ok());
    }

    #[test]
    fn rejects_unclosed_paren() {
        assert!(parse("(x").is_err());
    }
}
```

```rust
// tests/smoke.rs — integration test, public API only
use my_crate::{Config, run};

#[test]
fn full_workflow() {
    let config = Config::default();
    assert!(run(&config).is_ok());
}

// tests/common/mod.rs — shared helpers (mod.rs avoids a test binary)
pub fn fixture(name: &str) -> String {
    std::fs::read_to_string(format!("tests/fixtures/{name}")).unwrap()
}
```

**Rationale**: Unit tests can exercise `pub(crate)` and private items; integration tests verify the API surface as an external user sees it. Helpers for integration tests go in `tests/common/mod.rs` specifically — Cargo treats any other file in `tests/` as its own test binary.


## PS-22: Benchmarks Live in `benches/`

**Strength**: SHOULD

**Summary**: Use `benches/` with `harness = false` for `criterion` or similar. Put benchmark setup behind dev-dependencies only.

```toml
[dev-dependencies]
criterion = "0.5"

[[bench]]
name = "throughput"
harness = false
```

```rust
// benches/throughput.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use my_crate::parse;

fn bench_parse(c: &mut Criterion) {
    c.bench_function("parse small", |b| b.iter(|| parse(black_box("x = 1"))));
}

criterion_group!(benches, bench_parse);
criterion_main!(benches);
```

**Rationale**: The built-in `#[bench]` harness is unstable and limited; `criterion` is the community standard. `harness = false` lets criterion's `main!` macro take over. Benchmarks only run under `cargo bench`, so they never slow down normal builds.


## PS-23: Libraries Work Out of the Box

**Strength**: MUST

**Summary**: A library must build on all Tier 1 platforms with only `cargo` and `rustc` — no protoc, no make, no perl, no cmake.

```rust
// ❌ build.rs — requires users to install protoc
fn main() {
    prost_build::compile_protos(&["proto/api.proto"], &["proto/"]).unwrap();
}

// ✅ generate once before publishing; check in the output
// src/generated.rs is committed to git
include!(concat!(env!("OUT_DIR"), "/api.rs"));
// build.rs only regenerates when an opt-in feature is on
fn main() {
    #[cfg(feature = "codegen")]
    prost_build::compile_protos(&["proto/api.proto"], &["proto/"]).unwrap();
}
```

**Rationale**: A library imposes its build requirements on every downstream user. If one dep in a 200-crate tree needs Perl, every consumer must install Perl — the source calls this "a self-inflicted death sentence in the open source space." Pre-generate artifacts during publishing; optional regen sits behind a `codegen` feature.

**See also**: M-OOBE


## PS-24: Native `-sys` Crates Are Self-Contained

**Strength**: MUST

**Summary**: FFI `-sys` crates must embed upstream source, build via `cc` from `build.rs`, and avoid requiring external toolchains at consumer build time.

```rust
// foo-sys/build.rs
fn main() {
    cc::Build::new()
        .file("vendor/foo/foo.c")
        .file("vendor/foo/bar.c")
        .include("vendor/foo/include")
        .compile("foo");

    // ❌ No Makefiles, CMake (unless via the cmake crate),
    //    Python/Perl scripts, or external bindgen at build time.
}
```

**Rationale**: If a `-sys` crate downloads sources in `build.rs`, every CI job needs network access to the same server. If it shells out to `make`, every user needs make. Embed sources (verifiable by Git URL + SHA), pre-generate `bindgen` output, and make any external tool optional behind a feature.

**See also**: M-SYS-CRATES


## PS-25: Lockfile Discipline

**Strength**: SHOULD

**Summary**: Commit `Cargo.lock` for binary crates and applications. For pure libraries, it's optional — but "when in doubt, commit it."

```text
# .gitignore entries for a typical Rust project
/target/
**/*.rs.bk        # rustfmt backup
*.pdb             # debug info (Windows)

# Do NOT gitignore Cargo.lock for binaries/apps
# For libraries, the tradeoff:
#   - committed: reproducible CI builds, but you must `cargo update` regularly
#   - gitignored: library tests always run against latest compatible deps
```

**Rationale**: `Cargo.lock` pins exact dependency versions. Binary crates need reproducible builds in production. Pure libraries historically omitted the lockfile so CI always tested against the latest compatible deps; the modern recommendation is still to commit it and schedule a weekly `cargo update` run. Published libraries ignore their committed lockfile when used as deps, so committing costs nothing downstream.


## PS-26: Workspaces for Multi-Crate Projects

**Strength**: SHOULD

**Summary**: A workspace shares one `Cargo.lock` and one `target/` across multiple member crates. Use a virtual workspace when there's no single root crate.

```toml
# Cargo.toml at workspace root (virtual workspace)
[workspace]
resolver = "2"
members = ["crates/*"]
exclude = ["crates/experimental"]

[workspace.package]
version = "0.5.0"
edition = "2024"
authors = ["Team Awesome"]
license = "MIT OR Apache-2.0"
repository = "https://github.com/example/my-project"
rust-version = "1.75"

[workspace.dependencies]
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["rt-multi-thread"] }
thiserror = "1"

[workspace.lints.rust]
unsafe_code = "deny"

[workspace.lints.clippy]
pedantic = { level = "warn", priority = -1 }
```

```toml
# crates/core/Cargo.toml — member inherits shared config
[package]
name = "my-project-core"
version.workspace = true
edition.workspace = true
license.workspace = true
rust-version.workspace = true

[dependencies]
serde.workspace = true
thiserror.workspace = true

[lints]
workspace = true
```

**Rationale**: A workspace cuts duplication: one place to set versions, lints, edition, and MSRV. Members share build artifacts, so touching one crate only rebuilds its dependents. Virtual workspaces (no `[package]` at root) are appropriate when no single crate is "the" project — just members.


## PS-27: Use `pub(crate)` for Internal Cross-Module APIs

**Strength**: SHOULD

**Summary**: Items shared across modules but not intended for external consumers should be `pub(crate)`, not `pub`.

```rust
// src/protocol/frame.rs — internal, shared within the crate
pub(crate) struct Frame {
    pub(crate) header: Header,
    pub(crate) payload: Vec<u8>,
}

impl Frame {
    pub(crate) fn decode(bytes: &[u8]) -> Result<Self, DecodeError> { /* ... */ todo!() }
}

// src/client/connection.rs
use crate::protocol::frame::Frame;   // visible within the crate

pub struct Connection {
    current: Option<Frame>,           // private field, Frame type never leaks
}
```

**Rationale**: `pub(crate)` lets you keep internal types out of the public API without manually plumbing them through private accessor methods. Refactoring is safer: you can grep the crate for every use, confident nothing external depends on these items.


## PS-28: Use `#[expect]`, not `#[allow]`, for Lint Overrides

**Strength**: MUST

**Summary**: `#[expect(lint, reason = "...")]` warns if the suppression becomes unnecessary. `#[allow]` silently persists forever.

```rust
// ❌ stale once refactored — no warning
#[allow(clippy::too_many_arguments)]
fn process(a: A, b: B, c: C, d: D, e: E, f: F, g: G, h: H) { /* ... */ }

// ✅ flags itself when no longer needed, with a reason
#[expect(
    clippy::too_many_arguments,
    reason = "public API frozen in 1.0; collapse in 2.0"
)]
fn process(a: A, b: B, c: C, d: D, e: E, f: F, g: G, h: H) { /* ... */ }

#[expect(
    clippy::cast_possible_truncation,
    reason = "bounds checked on line 42"
)]
let index = large_value as u32;
```

**Rationale**: `#[allow]` accumulates like tech debt — every suppression stays forever, even after the code changes to make it unnecessary. `#[expect]` turns the lint into a positive assertion: "this lint _should_ fire here." If the lint stops firing, the compiler warns you to remove the suppression.

**See also**: M-LINT-OVERRIDE-EXPECT


## PS-29: Consistent Static Verification

**Strength**: MUST

**Summary**: Use `rustfmt`, `clippy`, and appropriate lint profiles. Declare them in `Cargo.toml` so every contributor runs the same checks.

```toml
[lints.rust]
unsafe_code = "deny"
missing_debug_implementations = "warn"
missing_docs = "warn"
unused_lifetimes = "warn"
rust_2018_idioms = { level = "warn", priority = -1 }

[lints.clippy]
pedantic = { level = "warn", priority = -1 }
cargo = { level = "warn", priority = -1 }
# project-specific deviations:
module_name_repetitions = "allow"
```

**Rationale**: `[lints]` in `Cargo.toml` (stable since 1.74) replaces fragile `#![warn]` attributes at the crate root and is inheritable across workspace members. `priority = -1` lets you enable a group and still override individual lints above it. CI should run `cargo fmt --check && cargo clippy --all-targets --all-features -- -D warnings`.

**See also**: M-STATIC-VERIFICATION


## PS-30: Design for AI and Maintainability

**Strength**: CONSIDER

**Summary**: APIs designed for human ergonomics also work well for LLMs. Strong types, thorough docs, runnable examples, and mockable test surfaces help both.

```rust
// ✅ strong types + doc example + mockable — LLM-friendly
use std::time::Duration;

/// Fetches the configured endpoint with the given timeout.
///
/// # Example
/// ```
/// # use std::time::Duration;
/// # use my_crate::{Client, Endpoint};
/// let client = Client::new(Endpoint::from_url("https://example.com")?);
/// let resp = client.fetch(Duration::from_secs(5))?;
/// # Ok::<_, my_crate::Error>(())
/// ```
pub fn fetch(&self, timeout: Duration) -> Result<Response, Error> { /* ... */ todo!() }

// ❌ stringly-typed, no docs — LLM will guess wrong
pub fn f(&self, url: &str, t: u64) -> Result<String, String> { /* ... */ todo!() }
```

**Rationale**: AI agents can't reason about correctness the way a senior engineer can — they rely on the compiler and tests for feedback loops. Strong types turn semantic mistakes into compile errors. Runnable doc examples let agents verify their usage. Mockable APIs let them iterate without real I/O. These are also the properties that make APIs good for humans under time pressure.

**See also**: M-DESIGN-FOR-AI


## Common Project Structures

### Simple library

```text
my-lib/
├── Cargo.toml
├── Cargo.lock
├── README.md
├── LICENSE-MIT
├── LICENSE-APACHE
├── .gitignore
├── src/
│   ├── lib.rs
│   ├── error.rs
│   └── parser.rs
├── tests/
│   ├── smoke.rs
│   └── common/
│       └── mod.rs
├── benches/
│   └── parse.rs
└── examples/
    └── quickstart.rs
```

### Library + binary in one package

```text
my-tool/
├── Cargo.toml            # [[bin]] implicit from src/main.rs
├── src/
│   ├── lib.rs            # logic (testable)
│   ├── main.rs           # thin wrapper
│   ├── cli.rs
│   └── commands/
│       ├── build.rs
│       └── clean.rs
├── tests/
│   └── cli_integration.rs
└── examples/
    └── programmatic.rs
```

### Multi-crate workspace with umbrella

```text
my-project/
├── Cargo.toml            # [workspace], [workspace.package], [workspace.dependencies]
├── Cargo.lock
├── README.md
└── crates/
    ├── my-project/          # umbrella — re-exports
    │   ├── Cargo.toml
    │   └── src/lib.rs
    ├── my-project-core/     # shared types
    │   ├── Cargo.toml
    │   └── src/lib.rs
    ├── my-project-client/
    │   ├── Cargo.toml
    │   └── src/lib.rs
    ├── my-project-server/
    │   ├── Cargo.toml
    │   └── src/lib.rs
    └── my-project-macros/   # proc macros (must be its own crate)
        ├── Cargo.toml
        └── src/lib.rs
```

### Virtual workspace (no umbrella)

```text
my-monorepo/
├── Cargo.toml            # only [workspace] — no [package]
├── Cargo.lock
└── crates/
    ├── auth/
    ├── billing/
    └── dashboard/
```


## Project Checklist

A starting `Cargo.toml` incorporating the guidelines above:

```toml
[package]
name = "my-crate"
version = "0.1.0"
edition = "2024"
rust-version = "1.75"                            # PS-11
authors = ["Jane Doe <jane@example.com>"]
license = "MIT OR Apache-2.0"
repository = "https://github.com/example/my-crate"
homepage = "https://example.com/my-crate"
documentation = "https://docs.rs/my-crate"
readme = "README.md"
keywords = ["parser", "config"]
categories = ["parsing"]
description = """
A fast, ergonomic parser for configuration files.
Supports TOML, YAML, and JSON with a unified API.
"""

[features]
default = ["std"]
std = []
serde = ["dep:serde"]                            # PS-14
test-util = []                                   # PS-16

[dependencies]
serde = { version = "1", features = ["derive"], optional = true }
thiserror = "1"

[dev-dependencies]                               # PS-15
criterion = "0.5"
tempfile = "3"

[[bench]]                                        # PS-22
name = "throughput"
harness = false

[lints.rust]                                     # PS-29
unsafe_code = "deny"
missing_debug_implementations = "warn"
missing_docs = "warn"
unused_lifetimes = "warn"

[lints.clippy]
pedantic = { level = "warn", priority = -1 }
cargo = { level = "warn", priority = -1 }

[package.metadata.docs.rs]                       # better docs.rs output
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[package.metadata.release]                       # cargo-release configuration
pre-release-commit-message = "release: v{{version}}"
tag-message = "v{{version}}"
sign-tag = true
```

And a minimal `.gitignore` for Rust:

```text
/target/
**/*.rs.bk
*.pdb

# Keep Cargo.lock committed for binaries / apps (PS-25)
# Pure libraries may choose to gitignore it; commit when in doubt.
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| PS-01 Cargo layout conventions | MUST | Place files where Cargo expects them |
| PS-02 Binary/library separation | SHOULD | Logic in `lib.rs`, `main.rs` is a shell |
| PS-03 Application vs library rules | MUST | Different obligations; don't mix them up |
| PS-04 `mod`/`pub`/`use` basics | MUST | Declare once, expose explicitly |
| PS-05 Restrictive visibility | MUST | Private → `pub(crate)` → `pub` |
| PS-06 Flat public API via re-exports | SHOULD | Crate root is the API surface |
| PS-07 No glob re-exports | MUST | Explicit lists; globs hide changes |
| PS-08 Prefer small crates | SHOULD | Compile time + modularity |
| PS-10 Don't leak external types | SHOULD | `std` types in public signatures |
| PS-11 Declare MSRV | SHOULD | `rust-version` + CI check |
| PS-12 Set `edition` | MUST | Latest your MSRV supports |
| PS-13 Features are additive | MUST | Every combination must compile |
| PS-14 Optional deps | SHOULD | Use `dep:` prefix to decouple names |
| PS-15 Dev-dependencies | MUST | Test/bench-only deps never leak |
| PS-16 `test-util` feature | MUST | Gate mocks and safety bypasses |
| PS-19 Dedicated error module | SHOULD | Central, re-exported, canonical |
| PS-21 Unit vs integration tests | MUST | `#[cfg(test)]` in-file + `tests/` |
| PS-23 Libraries work OOBE | MUST | No external tools at build time |
| PS-24 Self-contained `-sys` | MUST | `cc` + embedded source |
| PS-25 Lockfile discipline | SHOULD | Commit for bins; optional for libs |
| PS-26 Workspaces | SHOULD | Shared lockfile, lints, metadata |
| PS-27 `pub(crate)` for internals | SHOULD | Keep cross-module sharing internal |
| PS-28 `#[expect]` over `#[allow]` | MUST | Detect stale suppressions |
| PS-29 Static verification in CI | MUST | `[lints]` in `Cargo.toml` |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for lint profile and formatting defaults.
- **API Design**: See `02-api-design.md` for public-API shape, argument conventions, and return types that interact with the re-export and visibility rules here.
- **Error Handling**: See `03-error-handling.md` for the full canonical error-struct design referenced in PS-19.
- **Type Design**: See `05-type-design.md` for newtype, `#[non_exhaustive]`, and field-visibility decisions that shape the public surface.
- **Documentation**: See `13-documentation.md` for the doc comments, crate-level intros, and runnable examples that make the public API navigable.


## External References

- [Cargo Book — Package Layout](https://doc.rust-lang.org/cargo/guide/project-layout.html)
- [Cargo Book — Workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)
- [Cargo Book — Features](https://doc.rust-lang.org/cargo/reference/features.html)
- [Cargo Book — Manifest](https://doc.rust-lang.org/cargo/reference/manifest.html)
- [Cargo Book — `Cargo.toml` vs `Cargo.lock`](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html)
- [The Rust Reference — Modules](https://doc.rust-lang.org/reference/items/modules.html)
- [The Rust Reference — Visibility and Privacy](https://doc.rust-lang.org/reference/visibility-and-privacy.html)
- [The Rust Book — Packages, Crates, and Modules](https://doc.rust-lang.org/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html)
- [Rust Style Guide — `Cargo.toml` Conventions](https://doc.rust-lang.org/nightly/style-guide/cargo.html)
- [Rust RFC 2495 — MSRV](https://rust-lang.github.io/rfcs/2495-min-rust-version.html)
- Pragmatic Rust Guidelines: M-SMALLER-CRATES, M-HIDE-DEPS, M-DONT-LEAK-TYPES, M-FEATURES-ADDITIVE, M-OOBE, M-SYS-CRATES, M-TEST-UTIL, M-NO-GLOB-REEXPORTS, M-AVOID-STATICS, M-APP-ERROR, M-ERRORS-CANONICAL-STRUCTS, M-LINT-OVERRIDE-EXPECT, M-STATIC-VERIFICATION, M-DESIGN-FOR-AI
