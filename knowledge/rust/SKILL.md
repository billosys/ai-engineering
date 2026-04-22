---
name: rust-guidelines
description: |
  Comprehensive Rust best practices, idioms, and anti-patterns grounded in
  the Rust Reference, the Rustonomicon, the Rust API Guidelines, the Rust
  Performance Book, the Asynchronous Programming Book, the Rustdoc Book,
  the Edition Guide, the Cargo Book, the tokio tutorial, and a corpus of
  AI-audited anti-patterns.
  Use when: writing new Rust code, refactoring existing Rust, reviewing
  Rust for issues, debugging ownership/lifetime errors, designing public
  APIs, handling errors with `Result`/`?`/`thiserror`/`anyhow`, wiring
  concurrency (`Send`/`Sync`, threads, channels, `async`/`await`, `Pin`,
  `Tokio`), writing declarative or procedural macros, working with
  `unsafe` and FFI boundaries, organising crates and workspaces,
  writing rustdoc, choosing or migrating a Rust edition, instrumenting
  code with `tracing`/`log`/metrics, building CLI tools with `clap`, or
  managing Cargo projects end-to-end.
---

# Rust Coding Guidelines Skill

## Overview

This skill delivers the condensed wisdom of the most authoritative Rust sources — the Rust Reference, the Rustonomicon, the API Guidelines, the Performance Book, the Async Book, Rustdoc, the Edition Guide, the Cargo Book, and the tokio tutorial — reconciled with Pragmatic Rust and the Rust Design Patterns book, then pressure-tested against a corpus of AI-generated anti-patterns. The guides are split by topic into seventeen chapters (fifteen single-file, two multi-file). Each entry is a numbered pattern with a strength indicator (MUST / SHOULD / CONSIDER / AVOID), a one-line summary, paired ✅ GOOD / ❌ BAD Rust snippets, a rationale, and cross-references. Every chapter ends with a Summary Table and a Related Guidelines list.

The target environment is **Rust 2024 edition on the 1.85+ toolchain**, with explicit call-outs where 2018, 2021, or 2024 behaviour differs. The default toolchain is **`rustfmt` + `cargo check` + `clippy` + `cargo test`**, the default error-handling pair is **`thiserror` for libraries + `anyhow` for applications**, the default async runtime is **`tokio`**, the default logging frontend is **`tracing`**, and the default argument parser is **`clap` with derive**.

## When to Use This Skill

Activate this skill when the task involves:

- Writing new Rust code
- Refactoring existing Rust code
- Reviewing Rust code for issues, bugs, or style drift
- Debugging borrow-checker, lifetime, or `Send`/`Sync` errors
- Designing public APIs, type hierarchies, trait boundaries
- Handling errors with `Result`, `?`, `thiserror`, `anyhow`, `From` conversions, `Display`/`Error`
- Writing concurrent or asynchronous code: threads, channels, `async`/`await`, `tokio`, `select!`, `Pin`, structured concurrency
- Working with `unsafe`, raw pointers, FFI, `repr(C)`, uninitialised memory, data layout
- Writing declarative macros (`macro_rules!`) or procedural macros (derive, attribute, function-like)
- Organising crates, workspaces, `src/bin/`, `internal`-style modules, library vs application architecture
- Writing rustdoc comments, doctests, intra-doc links, `#[doc]` attributes
- Choosing, migrating, or interoperating across Rust editions (2015 / 2018 / 2021 / 2024)
- Instrumenting code with `tracing`, `log`, metrics, OpenTelemetry, panic hooks
- Building command-line applications with `clap` derive, subcommands, shell completions, exit codes
- Managing Cargo projects: packages, workspaces, features, profiles, build scripts, publishing, lints, cargo plugins
- Triaging AI-generated Rust for security, concurrency, `unsafe`-soundness, and idiomatic-style regressions

## Document Locations

All guideline documents are in `knowledge/rust/guides/`:

**Core chapters (fifteen single-file, two multi-file — seventeen total):**

- `01-core-idioms.md` — Naming, formatting, imports, attributes, expression-oriented style, shared idioms
- `02-api-design.md` — Public surfaces, naming, flexibility, ergonomics, interoperability
- `03-error-handling.md` — `Result`, `?`, custom error types, `thiserror`, `anyhow`, panics vs errors
- `04-ownership-borrowing.md` — Ownership, borrows, lifetimes, RAII/OBRM, drop check, variance, splitting
- `05-type-design.md` — Structs, enums, newtypes, builders, typestate, `Pin`, variance, sealed traits, `?Sized`
- `06-traits.md` — Trait design, object safety, auto traits, HRTBs, `dyn`, supertraits, blanket impls
- `07-concurrency-async.md` — Threads, channels, atomics, `async`/`await`, `Pin`, structured concurrency, `tokio`
- `08-performance.md` — Build config, compile-time opt, hashing, allocations, type sizes, profiling workflow
- `09-unsafe-ffi.md` — `unsafe` discipline, soundness, `repr(C)`, `MaybeUninit`, `UnsafeCell`, FFI design, inline asm
- `10-macros.md` — `macro_rules!`, fragment opacity, push-down accumulation, proc macros, `trybuild`
- `11-anti-patterns.md` — 70 concrete traps (safety, soundness, API, `unsafe`, async, AI-misuse), each with a fix
- `12-project-structure.md` — Crates, workspaces, `bin`/`lib`/`examples`, MSRV, features, library vs application
- `13-documentation.md` — Doc comments, doctests, intra-doc links, `#[doc(…)]`, scraped examples, rustdoc lints
- `14-cli-tools/` — Command-line applications (project setup, `clap`, UX, config, testing, distribution)
- `15-cargo/` — Cargo mastery (basics, build system, plugins, publishing, configuration, advanced, lints, workspaces)
- `16-editions.md` — Rust editions 2015/2018/2021/2024, migration (`cargo fix --edition`), interop
- `17-observability.md` — `tracing`/`log`, structured events, spans, metrics, OpenTelemetry, panic hooks, correlation IDs

**Supporting material:**

- `knowledge/rust/sources/md/` — The upstream guides in markdown form (21 sources; the ground truth)
- `knowledge/rust/concept-cards/` — Single-pattern cards extracted from each source, one per upstream section
- `knowledge/rust/concept-cards/AUDIENCE.md` — Which sources target which audience; notes the `compiler-guide` and `clippy [lint-development]` sets as specialist (rustc/clippy contributors), not inlined into the main guides
- `knowledge/rust/extraction-metadata/` — How each card/pattern was derived and reconciled
- `knowledge/rust/workbench/` — Provenance records, the 2026-04 regeneration plan, the review report

Guides are the normative artefact. Concept cards and upstream sources are there when you need the original wording, deeper rationale, or an edge-case example.

## Document Selection Guide

Load documents based on the task. Anti-patterns (chapter 11) is the cheap safety net — load it first on any Rust task.

| Task | Load These Documents |
|------|---------------------|
| **Any Rust code** | `11-anti-patterns.md` (always load first) |
| **New code from scratch** | `11-anti-patterns.md`, `01-core-idioms.md`, `03-error-handling.md` |
| **API design** | `02-api-design.md`, `05-type-design.md`, `06-traits.md`, `13-documentation.md` |
| **Error handling** | `03-error-handling.md`, `11-anti-patterns.md` |
| **Ownership / lifetime / borrow-checker fights** | `04-ownership-borrowing.md`, `05-type-design.md` |
| **Type design — structs, enums, generics, `Pin`** | `05-type-design.md`, `06-traits.md` |
| **Trait design — object-safety, HRTBs, blanket impls** | `06-traits.md`, `05-type-design.md` |
| **Threads, channels, atomics** | `07-concurrency-async.md` (CA-01…CA-14), `04-ownership-borrowing.md` |
| **`async`/`await`, `tokio`, `Pin`, self-referential** | `07-concurrency-async.md` (CA-15…CA-50), `05-type-design.md` (TD-21…TD-23) |
| **Performance / profiling / allocation** | `08-performance.md`, `11-anti-patterns.md` |
| **`unsafe`, FFI, `repr(C)`, raw pointers** | `09-unsafe-ffi.md`, `04-ownership-borrowing.md` |
| **Macros — `macro_rules!` and proc macros** | `10-macros.md` |
| **Refactoring** | `11-anti-patterns.md`, then topic-specific |
| **Code review / quality audit** | `11-anti-patterns.md` (scan AP-01…AP-70), topic-specific |
| **Crate / workspace layout** | `12-project-structure.md`, `15-cargo/` |
| **Documentation — doc comments, doctests, intra-doc** | `13-documentation.md` |
| **Edition choice / migration** | `16-editions.md` |
| **Observability — `tracing`, metrics, panics** | `17-observability.md` |
| **CLI application** | `14-cli-tools/README.md`, then section-specific |
| **Cargo package / dependencies / workspaces** | `15-cargo/01-cargo-basics.md` |
| **Features / build scripts / profiles** | `15-cargo/02-cargo-build-system.md` |
| **Cargo subcommand plugin** | `15-cargo/03-cargo-plugins.md` |
| **Publishing to crates.io / SemVer** | `15-cargo/04-cargo-publishing.md` |
| **`.cargo/config.toml`, registries, linkers** | `15-cargo/05-cargo-configuration.md` |
| **CI, build optimisation, unstable features** | `15-cargo/06-cargo-advanced.md` |
| **Clippy and rustfmt policy** | `15-cargo/07-lints-and-formatters.md` |
| **`[lints]`, resolver v3, `dep:` prefix, workspace inheritance** | `15-cargo/08-manifest-and-workspace-advanced.md` |

### CLI Tools — When to Load Specific Sections

| Task | Load These Sections |
|------|---------------------|
| **Starting a CLI project** | `14-cli-tools/01-project-setup.md` (CLI-01…CLI-04) |
| **Argument parsing** | `14-cli-tools/02-argument-parsing.md` (CLI-05…CLI-15, CLI-53, CLI-54) |
| **CLI error handling / exit codes** | `14-cli-tools/03-error-handling.md` (CLI-16…CLI-20, CLI-55, CLI-56) |
| **Output formatting / colours / prompts / panics** | `14-cli-tools/04-output-and-ux.md` (CLI-21…CLI-28, CLI-57, CLI-58) |
| **Config files / precedence / XDG** | `14-cli-tools/05-configuration.md` (CLI-29…CLI-33) |
| **Testing CLIs (`assert_cmd`, snapshots)** | `14-cli-tools/06-testing.md` (CLI-34…CLI-38) |
| **Distribution / `cargo-binstall` / man pages** | `14-cli-tools/07-distribution.md` (CLI-39…CLI-42, CLI-59) |
| **Signals / completions / piping / cross-platform** | `14-cli-tools/08-advanced-topics.md` (CLI-43…CLI-46) |
| **Avoiding CLI pitfalls** | `14-cli-tools/09-common-pitfalls.md` (CLI-49…CLI-52) |

## Workflow

### For Writing New Code

1. **Load anti-patterns first**: Read `11-anti-patterns.md` — know what NOT to do before writing a line.
2. **Load core idioms**: Read `01-core-idioms.md` for naming, formatting, expression-oriented style, attribute discipline.
3. **Load topic-specific docs**: Based on what you're building (error handling, concurrency, `unsafe`, API, CLI, …).
4. **Set up the crate**: `cargo new`, pick edition (`2024` by default), add a `[lints]` section in `Cargo.toml`, pin MSRV.
5. **Write code**: Small APIs, `Result` everywhere, `?` for propagation, `Send`/`Sync` where crossing threads, `#[must_use]` on builders.
6. **Self-review**: Walk AP-01…AP-70 one last time. Run `cargo fmt`, `cargo check`, `cargo clippy -- -D warnings`, `cargo test`.

### For API Design

1. **Load `02-api-design.md`, `05-type-design.md`, `06-traits.md`, `13-documentation.md`**.
2. **Start with types, not functions**: Newtypes for invariants (TD-03), enums for closed sets (TD-06), `#[non_exhaustive]` on public enums you may extend (TD-07).
3. **Return owned, accept borrowed**: `fn take(s: &str)` not `fn take(s: String)`; `fn give() -> String`, not `-> &str` (unless lifetimes justify it).
4. **Derive the standard traits**: `Debug` on every public type (M-PUBLIC-DEBUG); `Display` on error and user-facing types; `Clone`, `PartialEq`, `Eq`, `Hash`, `Default` where they make sense and are stable.
5. **Seal trait hierarchies you don't want extended downstream** (TR-26); prefer `&self` receivers on traits you want to be object-safe (TR-17).
6. **Document every public item** with rustdoc (DC-01). Include `# Errors`, `# Panics`, `# Safety` sections where applicable.

### For Error Handling

1. **Load `03-error-handling.md`** plus **AP-01…AP-10** in `11-anti-patterns.md`.
2. **Return, don't panic**: Errors are values. `panic!` / `unwrap` / `expect` are for programmer invariants, never for expected failure modes reachable from user input.
3. **`thiserror` in libraries, `anyhow` in applications**: never the reverse. Libraries produce typed errors so callers can react; applications aggregate them.
4. **Use `?` for propagation**, `From` impls for conversion, and `#[source]` / `#[from]` to preserve the chain.
5. **Document `# Errors`** on every `Result`-returning public function. Document `# Panics` on every function that may panic.
6. **Never swallow errors**: `let _ = x;` on a `Result` is a bright-line anti-pattern (AP-04) except at documented boundaries.

### For Concurrency and Async

1. **Load `07-concurrency-async.md`** plus the CA-\* rows of the anti-patterns chapter.
2. **`Send` and `Sync` are the contract**: `Send` means safe to move across threads; `Sync` means `&T` is safe to share. Most types get these automatically; `*mut T`, `Rc`, `RefCell` do not.
3. **Spawn needs a `JoinHandle`** or an explicit scope (CA-01, CA-09). Never detach unless you've written the rationale down.
4. **`async fn` is not magic**: a future does nothing until polled. Every `.await` is a cancellation point. Cancellation-safety is a property of every async function you write (CA-28).
5. **Pin is address-stability**: if your future borrows into itself, it must be `!Unpin`, and you must not move it after it's been polled. Prefer `pin-project`/`pin-project-lite` over manual unsafe pinning (CA-24).
6. **`select!` races, `join!` awaits all, `try_join!` short-circuits**. Prefer structured concurrency (`JoinSet`, scopes) over bare `spawn` without a lifecycle.

### For `unsafe` and FFI

1. **Load `09-unsafe-ffi.md`** and the US-\* rows of the anti-patterns chapter.
2. **Every `unsafe { }` block needs a `// SAFETY:` comment** explaining why the invariants hold (US-02). No exceptions.
3. **Soundness is monotonic**: adding `unsafe` to a safe API must never introduce UB when called from safe code. If you can't prove that, don't expose it.
4. **`UnsafeCell` is the only interior-mutability primitive**. `repr(C)`, `repr(transparent)`, `repr(packed)` exist for specific layout contracts — do not mix them up.
5. **`MaybeUninit` is mandatory for uninitialised memory** — you cannot have a `&T` or `&mut T` to uninitialised storage, even briefly.
6. **FFI boundaries**: `extern "C"`, `#[repr(C)]` types only, never panic across the boundary (wrap panics with `catch_unwind`), document the calling ABI.
7. **Run Miri** on unsafe code (`cargo +nightly miri test`). Skipping Miri on unsafe code is an anti-pattern (AP-68).

### For Macros

1. **Load `10-macros.md`**.
2. **Prefer `macro_rules!` for ergonomic leaves**, proc macros when you need to inspect or generate at the token level.
3. **Fragment specifiers form a hygienic contract**: `:ident`, `:ty`, `:expr`, `:pat`, `:tt`. Once you match `:expr` you can only re-use it as `:expr` — follow-set restrictions matter (MC-05).
4. **`$crate` for all crate-internal paths** in exported `macro_rules!` — users who glob-import will thank you (MC-09).
5. **Proc macros go in a `proc-macro = true` crate** that typically has no non-proc-macro exports. Re-export the macro from the parent crate so users write one `use`.
6. **Test proc macros with `trybuild`** for negative cases (MC-27). Positive cases are just normal tests on the generated code.

### For CLI Applications

1. **Load `14-cli-tools/README.md`** for the map, then load the section that matches what you're doing.
2. **`clap` derive is the default** (CLI-05). Never parse `std::env::args()` by hand (CLI-49). Validate at parse time, not later.
3. **Exit codes are part of the API**: `0` success, `1` generic failure, `2` usage error; return `ExitCode` from `main` (CLI-55) and treat `BrokenPipe` as a clean exit (CLI-56).
4. **Data to stdout, everything else to stderr** (CLI-27). Detect TTYs before turning on colour (CLI-23) or prompting interactively (CLI-25).
5. **Offer a machine-readable mode** (`--json`, CLI-26) whenever the tool is likely to be composed in a pipeline.
6. **Ship shell completions** (`clap_complete`, CLI-44) and man pages (`clap_mangen`, CLI-59) from a `build.rs` or a subcommand.

### For Cargo Work

1. **Load `15-cargo/README.md`** for navigation, then the specific sub-guide.
2. **Package vs. workspace vs. virtual manifest** are three distinct shapes (CG-B-10, CG-W-\*). Choose deliberately. Use `[workspace.package]` and `[workspace.dependencies]` for shared metadata and versions.
3. **Features are additive** (CG-BS-01). Default features should be the "batteries-included" set a new user expects. Use `dep:` prefix (CG-ECO-\*) to decouple feature names from optional dependency names.
4. **Build scripts are sandboxed I/O**: emit `cargo::rustc-*` directives (CG-BS-08); never write outside `OUT_DIR`; declare every `rerun-if-changed` dependency.
5. **Publishing is one-way**: `cargo publish --dry-run`, run the CG-PUB-02 pre-flight checklist, pin `rust-version` to your verified MSRV, and tag the release.
6. **CI runs `fmt` + `clippy -D warnings` + `test` + `doc` + `miri` (unsafe only) + `cargo deny`** (CG-A-03, CG-A-08).

### For Refactoring

1. **Load `11-anti-patterns.md`** first.
2. **Scan the code for each PREFIX-NN** you recognise (note the ID for commit messages).
3. **Load the affirmative chapter** for anything you want to replace.
4. **Refactor one pattern at a time**, run `cargo test && cargo clippy -- -D warnings` after each.
5. **Reference pattern IDs in commit messages** (e.g. `refactor(errors): replace String error with thiserror enum (AP-05)`).

### For Code Review

1. **Load `11-anti-patterns.md`** and walk AP-01…AP-70.
2. **Load topic chapters** based on what the PR touches (concurrency? `unsafe`? API? macros?).
3. **Check for `unwrap`/`expect` on non-invariant paths, missing `Send`/`Sync`, unbounded lifetimes, missing `// SAFETY:` comments, missing `#[must_use]`, missing `# Errors`/`# Panics` docs, and stale MSRV** — these are the recurring regressions.
4. **Report findings by pattern ID** for unambiguous follow-up.

### For Edition Migration

1. **Load `16-editions.md`**.
2. **Run `cargo fix --edition` first** (ED-06). The rewrites it produces are mechanical and safe; eyeball the diff.
3. **Then bump `edition = "2024"` in `Cargo.toml`** and re-run `cargo check`. Expected breakers: match ergonomics (ED-18), RPIT lifetime capture (ED-19), `if let` temporary scope (ED-20), never-type fallback (ED-21).
4. **Library maintainers must think about downstream interop** — editions are per-crate, not per-workspace, but feature resolver v2/v3 is workspace-wide (ED-12, ED-24).

## Critical Rules (Always Apply)

These rules should be followed in ALL Rust code without needing to load documents:

### Parameters and Return Types

```rust
// ❌ BAD — owned parameters where a borrow is enough; concrete vec/string types
fn count(data: &String, items: &Vec<i32>) -> usize

// ✅ GOOD — borrow the slice types
fn count(data: &str, items: &[i32]) -> usize

// ✅ GOOD — accept AsRef for path-like APIs
fn open<P: AsRef<Path>>(path: P) -> io::Result<File>

// ✅ GOOD — return owned types from constructors, borrow-returning fns need lifetimes
pub fn build() -> Config { /* … */ }
pub fn name(&self) -> &str { &self.name }
```

### Derives and `#[must_use]`

```rust
// ✅ GOOD — public types implement Debug (M-PUBLIC-DEBUG); add Clone/PartialEq where sensible
#[derive(Debug, Clone, PartialEq)]
pub struct Config { /* … */ }

// ✅ GOOD — #[must_use] on builders, Result-like wrappers, fallible ops
#[must_use = "this `Result` may be an `Err`; handle it"]
pub enum MyResult<T> { Ok(T), Err(Error) }

// ❌ BAD — deriving Debug on a secret-holding type leaks credentials to logs
#[derive(Debug)]
pub struct ApiToken(String);

// ✅ GOOD — custom Debug that redacts (M-PUBLIC-DEBUG)
pub struct ApiToken(String);
impl fmt::Debug for ApiToken {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "ApiToken(***)")
    }
}
```

### Error Handling

```rust
// ❌ BAD — panics on library paths
let value = something.unwrap();

// ❌ BAD — stringly-typed errors lose structure
return Err(format!("bad input: {s}"));

// ✅ GOOD — propagate with `?`
let value = something()?;

// ✅ GOOD — typed error in a library with thiserror
#[derive(Debug, thiserror::Error)]
pub enum ParseError {
    #[error("unknown field: {0}")]
    UnknownField(String),
    #[error("io error")]
    Io(#[from] std::io::Error),
}

// ✅ GOOD — anyhow in an application binary
fn main() -> anyhow::Result<()> {
    let cfg = load_config().context("loading config")?;
    run(cfg)
}
```

### Ownership, Borrowing, RAII

```rust
// ✅ GOOD — RAII / OBRM: resources released via Drop, automatically
fn copy_file(src: &Path, dst: &Path) -> io::Result<()> {
    let mut input = File::open(src)?;          // closed on scope exit
    let mut output = File::create(dst)?;       // closed on scope exit
    io::copy(&mut input, &mut output)?;
    Ok(())
}

// ❌ BAD — manual cleanup that forgets error paths
fn copy_file_bad(src: &Path, dst: &Path) -> io::Result<()> {
    let input = open_raw(src);
    let output = open_raw(dst);
    // if copy errors here, both FDs leak
    raw_copy(input, output)?;
    close(input);
    close(output);
    Ok(())
}

// ✅ GOOD — split a borrow by field instead of cloning
let (left, right) = slice.split_at_mut(mid);
```

### Concurrency

```rust
// ❌ BAD — detached thread, no handle, panic lost
std::thread::spawn(|| do_work());

// ✅ GOOD — scoped thread: borrows local data; joined at scope end
std::thread::scope(|s| {
    for chunk in data.chunks_mut(N) {
        s.spawn(|| work_on(chunk));
    }
});

// ❌ BAD — blocking I/O inside an async fn
async fn bad() -> io::Result<String> {
    std::fs::read_to_string("file.txt")        // BLOCKS the runtime!
}

// ✅ GOOD — async I/O, or spawn_blocking for CPU/blocking work
async fn good() -> io::Result<String> {
    tokio::fs::read_to_string("file.txt").await
}
```

### `unsafe`

```rust
// ❌ BAD — unsafe block with no explanation
let slice = unsafe { std::slice::from_raw_parts(ptr, len) };

// ✅ GOOD — every unsafe block carries a SAFETY comment
// SAFETY: `ptr` is the start of a region we just allocated with
// `alloc::alloc(Layout::array::<u8>(len).unwrap())`; `len` matches that
// layout; the region is not aliased; it outlives `'_`.
let slice = unsafe { std::slice::from_raw_parts(ptr, len) };
```

### Macros

```rust
// ❌ BAD — macro paths that break under glob imports
macro_rules! count { ($($x:expr),*) => { [$($x),*].len() }; }

// ✅ GOOD — $crate-anchored paths survive re-export
#[macro_export]
macro_rules! count {
    ($($x:expr),*) => { <[()]>::len(&[$($crate::replace_expr!($x ())),*]) };
}
```

### CLI Applications

```rust
// ❌ BAD — hand-parsing argv
let args: Vec<String> = std::env::args().collect();
if args.contains(&"--verbose".to_string()) { /* … */ }

// ✅ GOOD — clap derive; types, help, version for free
use clap::Parser;

#[derive(Parser)]
#[command(version, about)]
struct Cli {
    /// File to process
    input: std::path::PathBuf,
    /// Show more detail
    #[arg(short, long, action = clap::ArgAction::Count)]
    verbose: u8,
}

fn main() -> std::process::ExitCode {
    let cli = Cli::parse();
    match run(cli) {
        Ok(()) => std::process::ExitCode::SUCCESS,
        Err(e) => { eprintln!("error: {e:#}"); std::process::ExitCode::FAILURE }
    }
}
```

### Documentation

```rust
/// Parse a configuration file.
///
/// # Errors
///
/// Returns [`ConfigError::Io`] if the file cannot be read and
/// [`ConfigError::Parse`] if the contents are malformed.
///
/// # Examples
///
/// ```
/// # use mylib::parse_config;
/// let cfg = parse_config("config.toml")?;
/// # Ok::<_, mylib::ConfigError>(())
/// ```
pub fn parse_config(path: &str) -> Result<Config, ConfigError> { /* … */ }
```

## Pattern ID Reference

Each chapter uses a prefix for pattern IDs. Cross-references throughout the guides use these prefixes.

### Core Guides

| Prefix | Chapter |
|--------|---------|
| `ID-NN`  | `01-core-idioms.md` |
| `API-NN` | `02-api-design.md` |
| `EH-NN`  | `03-error-handling.md` |
| `OB-NN`  | `04-ownership-borrowing.md` |
| `TD-NN`  | `05-type-design.md` |
| `TR-NN`  | `06-traits.md` |
| `CA-NN`  | `07-concurrency-async.md` |
| `PF-NN`  | `08-performance.md` |
| `US-NN`  | `09-unsafe-ffi.md` |
| `MC-NN`  | `10-macros.md` |
| `AP-NN`  | `11-anti-patterns.md` |
| `PS-NN`  | `12-project-structure.md` |
| `DC-NN`  | `13-documentation.md` |
| `ED-NN`  | `16-editions.md` |
| `LO-NN`  | `17-observability.md` |

### CLI Tools Collection (`14-cli-tools/`)

| Prefix | Range |
|--------|-------|
| `CLI-NN` | CLI-01…CLI-59, across nine section files |

Rough ranges: CLI-01…04 (setup), CLI-05…15 + CLI-53…54 (argument parsing), CLI-16…20 + CLI-55…56 (errors), CLI-21…28 + CLI-57…58 (output/UX), CLI-29…33 (config), CLI-34…38 (testing), CLI-39…42 + CLI-59 (distribution), CLI-43…46 (advanced topics), CLI-49…52 (common pitfalls).

### Cargo Mastery Collection (`15-cargo/`)

| Prefix | Sub-guide |
|--------|-----------|
| `CG-B-NN`   | `01-cargo-basics.md` |
| `CG-BS-NN`  | `02-cargo-build-system.md` |
| `CG-P-NN`   | `03-cargo-plugins.md` |
| `CG-PUB-NN` | `04-cargo-publishing.md` |
| `CG-CF-NN`  | `05-cargo-configuration.md` |
| `CG-A-NN`   | `06-cargo-advanced.md` |
| `CG-L-NN` / `CG-F-NN` | `07-lints-and-formatters.md` |
| `CG-M-NN` / `CG-W-NN` / `CG-ECO-NN` | `08-manifest-and-workspace-advanced.md` |

## Strength Indicators

The guides use a graded strength scale. MUST is non-negotiable; SHOULD is firm convention; CONSIDER is context-dependent; AVOID labels anti-patterns.

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness, safety, or soundness | Always follow |
| **SHOULD** | Strong community/project convention | Follow unless you have a specific justification |
| **CONSIDER** | Context-dependent recommendation | Evaluate case by case |
| **AVOID** | Anti-pattern | Do not use |

The anti-patterns chapter (`11-anti-patterns.md`) uses **AVOID** on every entry — the entry's title is the thing to avoid.

## Example Usage

### Task: "Write a function that loads configuration from a file, with timeouts"

1. Load: `11-anti-patterns.md`, `01-core-idioms.md`, `03-error-handling.md`, `13-documentation.md`.
2. Apply:
   - **EH-03 / EH-04** Define a `ConfigError` with `thiserror`, one variant per failure mode, `#[from]` the underlying IO/parse errors.
   - **EH-02 / EH-06** Propagate with `?`; no `unwrap` / `expect` outside test code (AP-03, AP-06).
   - **ID-10** Accept `impl AsRef<Path>` — not `&PathBuf`, not `&str`.
   - **API-12** Return `Result<Config, ConfigError>`; document errors in `# Errors`.
   - **DC-02 / DC-07** First line is a complete sentence. Include a doctest.

### Task: "Review this async pipeline for cancellation safety and resource leaks"

1. Load: `11-anti-patterns.md`, `07-concurrency-async.md`, `03-error-handling.md`.
2. Check:
   - **CA-18 / CA-28** Is every `.await` a safe cancel point? What happens if the future is dropped mid-flight?
   - **CA-02 / CA-24** `Pin`/`!Unpin` discipline. If the future self-borrows, does it use `pin-project`?
   - **CA-35 / CA-38** `tokio::select!` arms: is every branch cancel-safe, or wrapped in `biased;` where order matters?
   - **CA-12 / CA-40** Channels — sender closes, receivers drain; bounded vs unbounded chosen consciously.
   - **AP-19** No blocking I/O / `std::thread::sleep` inside an async fn.
   - **AP-20** No holding a `std::sync::Mutex` guard across an `.await`.

### Task: "Add `unsafe` code for a zero-copy buffer"

1. Load: `09-unsafe-ffi.md`, `04-ownership-borrowing.md`, `05-type-design.md`.
2. Apply:
   - **US-02** Every `unsafe { }` block gets a `// SAFETY:` comment.
   - **US-06 / US-08** `MaybeUninit<T>` for uninitialised storage; never `&T` / `&mut T` into uninit memory.
   - **US-14 / US-16** `UnsafeCell` for any interior mutability; pick `repr(C)` vs `repr(transparent)` deliberately.
   - **US-22** Document the public safety contract in a `# Safety` section on every `pub unsafe fn` and on any safe API with a hidden unsafe obligation.
   - **AP-68** Add a Miri CI job. No exceptions.

### Task: "Design a public API for a pluggable authentication layer"

1. Load: `02-api-design.md`, `05-type-design.md`, `06-traits.md`, `13-documentation.md`.
2. Apply:
   - **API-08 / API-14** Use a sealed trait (`TR-26`) to control the extension surface; expose a newtype for credentials.
   - **TR-17 / TR-18** Keep the trait object-safe unless you need generic associated types; document both forms.
   - **TD-07** `#[non_exhaustive]` on public enums you expect to extend (auth methods, error kinds).
   - **TD-03** Newtype wrappers around `String` for `UserId`, `SessionId`; derive `Debug`-redacted for secrets.
   - **DC-04** Include `# Examples` on the trait, not just on the impls.

### Task: "Instrument a service for production: logs, traces, metrics"

1. Load: `17-observability.md`, `07-concurrency-async.md`, `03-error-handling.md`.
2. Apply:
   - **LO-02 / LO-03** `tracing` not `println!`; `log` only if you're a library that should be frontend-agnostic.
   - **LO-05 / LO-06** Span per request/operation; `#[instrument]` on handlers; event fields are structured, not interpolated.
   - **LO-09** Metrics via a `metrics` or `prometheus` facade; counter/gauge/histogram choice documented.
   - **LO-12 / LO-13** Panic hook that emits an error event with the location and message; correlation ID propagates through spans.
   - **LO-17** `RUST_LOG` compatible directives; default verbosity is `info`, `-v` → `debug`, `-vv` → `trace`.

### Task: "Build a CLI tool that reads files, pipes to stdout, survives Ctrl-C"

1. Load: `14-cli-tools/README.md` for the map; then `14-cli-tools/01-project-setup.md`, `14-cli-tools/02-argument-parsing.md`, `14-cli-tools/04-output-and-ux.md`, `14-cli-tools/08-advanced-topics.md`.
2. Apply:
   - **CLI-01 / CLI-03** Separate `src/lib.rs` (testable logic) from `src/main.rs` (thin entry).
   - **CLI-05 / CLI-53** `clap` derive; `ValueEnum` for closed-set string args.
   - **CLI-27 / CLI-56** Data to stdout; `BrokenPipe` is a clean exit (exit code 0).
   - **CLI-43** Install a `ctrl_c` handler that sets a cancellation token; respect it in the main loop.
   - **CLI-46** Detect whether stdin is a TTY (`IsTerminal::is_terminal`) before reading interactively; detect stdout TTY before colourising.
   - **CLI-55** Return `ExitCode` from `main`, not `std::process::exit`.

### Task: "Migrate a crate from edition 2021 to edition 2024"

1. Load: `16-editions.md`, `11-anti-patterns.md`.
2. Apply:
   - **ED-06** Start with `cargo fix --edition` on a clean tree; review the diff.
   - **ED-18** Inspect every `match` on a reference — `2024` removes some `ref`/`ref mut` ergonomics.
   - **ED-19** Audit `impl Trait` returns that implicitly captured lifetimes — now they capture them explicitly with `use<…>`.
   - **ED-20** `if let … = foo().scope();` in `2024` drops the temporary at the end of the outer statement — refactor any code that depended on the old drop timing.
   - **ED-21** Never-type fallback changed to `!` — code that accidentally used `()` fallback will now see `!` and may need annotations.
   - **ED-24** Check `edition = "2024"` in `Cargo.toml` and update MSRV to 1.85+.

### Task: "Prepare a crate for publishing"

1. Load: `15-cargo/04-cargo-publishing.md`, `13-documentation.md`, `02-api-design.md`.
2. Apply:
   - **CG-PUB-01** Fill in `description`, `license`, `repository`, `readme`, `categories`, `keywords`, `rust-version`.
   - **CG-PUB-02** Pre-publish checklist: `cargo publish --dry-run`, `cargo doc --no-deps`, `cargo test --all-features && cargo test --no-default-features`, `cargo clippy -- -D warnings`, `cargo msrv verify`.
   - **CG-PUB-03 / CG-PUB-04** SemVer: bump `MAJOR` for any breaking change, even one that "no one uses"; use `cargo-semver-checks`.
   - **DC-14 / DC-15** Crate-level doc comment with an overview and a runnable example; `#![deny(missing_docs)]` in the crate root for published libraries.

## Integration Notes

- **Code blocks use `rust` syntax** with the `✅ GOOD` / `❌ BAD` comment convention. Bash snippets use `bash`, TOML `toml`, etc.
- **Pattern IDs are `PREFIX-NN`** (e.g. `TD-03`, `AP-68`). Numbers are stable within a chapter; fold-merges preserve the lower number.
- **Cross-references in-guide** use `See also: TR-17, API-12` style at the end of an entry.
- **Each chapter ends with a Summary Table** of every pattern and a Related Guidelines list — use either as a compressed index before loading the full chapter.
- **Strength labels are uppercase bold** (`**MUST**`, `**SHOULD**`, `**CONSIDER**`, `**AVOID**`). Consistent casing lets you `grep` for everything at a given severity.
- **Clippy lints** are referenced as `clippy::lint_name`. The same lint is referenced in `15-cargo/07-lints-and-formatters.md` as an enforceable rule.
- **`knowledge/rust/sources/md/`** holds the 21 upstream guides (Rust Reference, Rustonomicon, API Guidelines, Performance Book, Async Book, tokio tutorial, Rustdoc, Edition Guide, Cargo Book, Pragmatic Rust, Rust Design Patterns, Rust Book, clap, cli-apps, clippy, style-guide, rust-macros, …). Every pattern in the guides is traceable to at least one source.
- **`knowledge/rust/concept-cards/`** holds single-pattern cards — 384 of them — useful when you want the distilled reference without pulling in an entire chapter. See `AUDIENCE.md` for notes on specialist card sets (`compiler-guide`, `clippy [lint-development]`) that are intentionally *not* promoted to the main guides.
- **`knowledge/rust/workbench/`** records the regeneration plan, review reports, and provenance decisions.

## Quick Reference for Common Tasks

| I want to… | Read this |
|------------|-----------|
| Write any Rust code | Start with `11-anti-patterns.md`, then `01-core-idioms.md` |
| Design a public API | `02-api-design.md` (→ `05`, `06`, `13`) |
| Handle errors | `03-error-handling.md` (+ `11-anti-patterns.md` AP-01…AP-10) |
| Fix a borrow-checker / lifetime error | `04-ownership-borrowing.md` |
| Design structs, enums, generics, `Pin` types | `05-type-design.md` |
| Design traits; decide object-safety / blanket impls | `06-traits.md` |
| Write threads / channels / atomics | `07-concurrency-async.md` (CA-01…CA-14) |
| Write `async fn` / `tokio` / `select!` | `07-concurrency-async.md` (CA-15…CA-50) |
| Profile and optimise performance | `08-performance.md` |
| Write `unsafe` or FFI code | `09-unsafe-ffi.md` (and run Miri) |
| Write `macro_rules!` or proc macros | `10-macros.md` |
| Review for anti-patterns | `11-anti-patterns.md` (walk AP-01…AP-70) |
| Lay out a crate or workspace | `12-project-structure.md` + `15-cargo/` |
| Write rustdoc / doctests / intra-doc links | `13-documentation.md` |
| Build a CLI with `clap` | `14-cli-tools/README.md` → section-specific |
| Manage dependencies / features / workspaces | `15-cargo/01-cargo-basics.md`, `15-cargo/02-cargo-build-system.md`, `15-cargo/08-manifest-and-workspace-advanced.md` |
| Publish to crates.io | `15-cargo/04-cargo-publishing.md` |
| Choose or migrate an edition | `16-editions.md` |
| Add `tracing`, metrics, panic hooks | `17-observability.md` |
| Triage a `Send`/`Sync` error | `06-traits.md` (TR-13) + `07-concurrency-async.md` (CA-02, CA-03) |
| Prevent secret leakage in `Debug` output | `02-api-design.md` (API-18) + `17-observability.md` (LO-15) |
| Sequence `unsafe` code review | `09-unsafe-ffi.md` (walk US-01…US-32) + `11-anti-patterns.md` (AP-60…AP-70) |
