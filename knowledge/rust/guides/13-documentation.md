# Documentation Guidelines

Patterns for writing Rust documentation with rustdoc: the mechanics of doc comments and the `#[doc]` attribute, the canonical section structure (`# Examples`, `# Errors`, `# Panics`, `# Safety`), doctest directives and conventions, intra-doc links, re-export inlining, rustdoc lints, and the supporting Cargo metadata that makes a crate discoverable on crates.io and docs.rs.


## DC-01: Every Public Item Has Documentation

**Strength**: MUST

**Summary**: Every public function, method, type, trait, macro, and module gets at least a one-sentence summary. Enforce it with `#![warn(missing_docs)]`.

```rust
// ❌ BAD: no documentation
pub fn process(input: &str) -> Result<Output, Error> {
    todo!()
}

// ✅ GOOD: summary sentence is sufficient for simple helpers
/// Parses `input` and returns the processed output.
pub fn process(input: &str) -> Result<Output, Error> {
    todo!()
}
```

```rust
// At the crate root — make the compiler enforce the rule
#![warn(missing_docs)]
#![warn(rustdoc::missing_crate_level_docs)]
```

**Rationale**: Public API without documentation forces readers into the source. `missing_docs` (shared with rustc) and `missing_crate_level_docs` (rustdoc-only) catch the omission at build time. The summary is the contract; if there isn't one yet, there isn't a stable API yet.

**See also**: DC-02, DC-16

---

## DC-02: `///` Documents the Next Item, `//!` Documents the Enclosing Item

**Strength**: MUST

**Summary**: Use `///` (outer) before an item, and `//!` (inner) at the top of `lib.rs` or a module to document the module/crate itself.

```rust
// ✅ GOOD: `//!` at the top of lib.rs documents the crate
//! Fast, ergonomic HTTP client.
//!
//! See the [`Client`] type for the main entry point.

/// Documents the function it precedes.
pub fn connect() { /* ... */ }

// ✅ GOOD: `//!` inside a module documents that module
pub mod parser {
    //! Parsers for configuration formats.

    /// Documents `Parser`.
    pub struct Parser;
}

// ❌ BAD: `///` at the top of lib.rs documents "the next item"
// and leaves the crate root undocumented.
```

**Rationale**: Both forms desugar to `#[doc = "..."]` — `///` to the outer attribute on the following item, `//!` to an inner attribute on the enclosing item. Using the wrong one silently misfiles your documentation.

**See also**: DC-03, DC-26

---

## DC-03: The First Sentence Is ~15 Words on One Line

**Strength**: MUST

**Summary**: The first sentence before the first blank line is the summary shown in module listings and search — keep it to roughly 15 words on a single line.

```rust
// ✅ GOOD: summary fits on one line
/// Opens a file in read-only mode at `path`.
pub fn open_file(path: &str) -> Result<File, Error> { todo!() }

// ❌ BAD: summary wraps to multiple lines, creating widows in listings
/// Opens a file at the specified path for reading and returns a File handle
/// that can be used to read the contents of the file from disk.
pub fn open_file2(path: &str) -> Result<File, Error> { todo!() }
```

**Rationale**: Rustdoc extracts everything before the first blank line as the summary. If that wraps in the module overview, each item in the list becomes harder to skim. Put detail in a second paragraph.

**See also**: M-FIRST-DOC-SENTENCE, DC-04

---

## DC-04: Use the Canonical Sections

**Strength**: MUST

**Summary**: Use these Markdown H1 sections, in this order: `# Examples`, `# Errors`, `# Panics`, `# Safety`. Include each one when it applies.

```rust
/// Parses a configuration file at `path`.
///
/// Reads the file, parses it as TOML, and validates it against the schema.
///
/// # Examples
///
/// ```
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let config = my_crate::parse_config("app.toml")?;
/// assert_eq!(config.port, 8080);
/// # Ok(())
/// # }
/// ```
///
/// # Errors
///
/// Returns an error if the file cannot be read, the TOML is malformed,
/// or a required field is missing.
///
/// # Panics
///
/// Panics if `path` contains interior NUL bytes.
pub fn parse_config(path: &str) -> Result<Config, Error> { todo!() }
```

```rust
/// Reads a `T` from the raw pointer.
///
/// # Safety
///
/// `ptr` must be non-null, properly aligned for `T`, and point to a valid,
/// initialized `T`. If `T` is not `Copy`, the caller must not use the
/// original value afterwards.
pub unsafe fn read_ptr<T>(ptr: *const T) -> T { unsafe { ptr.read() } }
```

**Rationale**: Consistent section names are how the whole ecosystem (including lint tooling like `clippy::missing_errors_doc`, `missing_panics_doc`, and `missing_safety_doc`) finds failure-mode documentation. Follow the order: Examples, Errors, Panics, Safety.

**See also**: M-CANONICAL-DOCS, C-FAILURE, DC-05, DC-06, DC-07

---

## DC-05: Document Every `Result` With an `# Errors` Section

**Strength**: MUST

**Summary**: Every function returning `Result` lists the conditions under which it returns `Err` and what the error reflects.

```rust
/// Reads exactly `n` bytes from `reader` into `buf`.
///
/// # Errors
///
/// Returns an error if:
/// - The reader reaches EOF before `n` bytes have been read
///   ([`io::ErrorKind::UnexpectedEof`]).
/// - An I/O error occurs during reading (propagated from `reader`).
pub fn read_exact<R: std::io::Read>(reader: &mut R, buf: &mut [u8]) -> std::io::Result<()> {
    reader.read_exact(buf)
}
```

**Rationale**: Users need to know which variants they have to handle and which causes are retryable. Empty "Errors" sections or "returns an error if something goes wrong" are worse than nothing.

**See also**: C-FAILURE, DC-15, EH guide

---

## DC-06: Document Every Panic With a `# Panics` Section

**Strength**: MUST

**Summary**: If the function can panic for any reason other than a caller-provided closure misbehaving, list the conditions.

```rust
/// Inserts `element` at `index`, shifting later elements right.
///
/// # Panics
///
/// Panics if `index > len`.
///
/// # Examples
///
/// ```should_panic
/// let mut v = vec![1, 2, 3];
/// v.insert(10, 4); // index out of bounds
/// ```
pub fn insert<T>(v: &mut Vec<T>, index: usize, element: T) {
    v.insert(index, element);
}
```

**Rationale**: A panic in library code terminates the caller's thread. Users can only avoid it if the condition is documented. Exhaustive coverage isn't required (you don't have to warn that a user-supplied `Display` impl could panic), but every panic you *can* describe should be documented.

**See also**: C-FAILURE

---

## DC-07: `unsafe fn` Requires a `# Safety` Section

**Strength**: MUST

**Summary**: Every `unsafe fn` must document the invariants the caller must uphold. No exceptions.

```rust
/// Reads `T` from `ptr` without moving or dropping it.
///
/// # Safety
///
/// The caller must ensure that:
/// * `ptr` is non-null and properly aligned for `T`.
/// * `ptr` points to a valid, initialized instance of `T`.
/// * The memory referenced by `ptr` is valid for reads of `size_of::<T>()`
///   bytes.
/// * If `T` is not `Copy`, the caller does not use the value at `ptr`
///   afterwards.
pub unsafe fn read<T>(ptr: *const T) -> T { unsafe { ptr.read() } }
```

**Rationale**: Without a `# Safety` section an `unsafe fn` cannot be used soundly. `clippy::missing_safety_doc` catches the omission; enable it. The corresponding `// SAFETY:` comment in the *caller* site should be able to cite this list directly.

**See also**: C-FAILURE, guide 09 (unsafe-ffi)

---

## DC-08: Every Public Item Has an Example

**Strength**: SHOULD

**Summary**: Give every public function, method, type, trait, and macro an `# Examples` section that shows *why* you'd call it, not just *how*.

```rust
/// Returns a builder for a new HTTP client.
///
/// # Examples
///
/// ```
/// use my_http::Client;
/// # use std::time::Duration;
/// let client = Client::builder()
///     .timeout(Duration::from_secs(30))
///     .build();
/// let _ = client;
/// ```
pub fn builder() -> ClientBuilder { ClientBuilder::new() }
```

**Rationale**: Examples are the most-read part of any docs page and the most likely to be copied. A mechanical "call the function" example teaches nothing; a motivating example ("with a custom timeout", "collected into a Vec") is what users actually need. Examples are also doctests — they compile and run as part of `cargo test`, so they keep working as the API evolves.

**See also**: C-EXAMPLE, DC-09, DC-10

---

## DC-09: Examples Use `?`, Not `unwrap` or `try!`

**Strength**: MUST

**Summary**: Example code is copied verbatim. Use `?` inside a hidden `fn main() -> Result<...>` or with a trailing hidden `Ok::<(), E>(())`, not `unwrap`.

```rust
// ✅ GOOD: hidden main, `?` at the ergonomics layer users should learn
/// Loads configuration from disk.
///
/// # Examples
///
/// ```
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let cfg = my_crate::load_config("app.toml")?;
/// assert_eq!(cfg.port, 8080);
/// # Ok(())
/// # }
/// ```
pub fn load_config(path: &str) -> Result<Config, Error> { todo!() }
```

```rust
// ✅ GOOD: equivalent shorthand since Rust 1.34 — no explicit main
/// ```
/// let n: u32 = "42".parse()?;
/// assert_eq!(n, 42);
/// # Ok::<(), std::num::ParseIntError>(())
/// ```
```

```rust
// ❌ BAD: teaches unwrap as the default error-handling pattern
/// ```
/// let cfg = my_crate::load_config("app.toml").unwrap();
/// ```
```

**Rationale**: Using `unwrap()` in docs teaches users that `unwrap` is the normal way to handle `Result`. `try!` has been deprecated since Rust 1.13. The hidden-line technique (`# `) keeps the example readable while still compiling as a real test.

**See also**: C-QUESTION-MARK, C-EXAMPLE

---

## DC-10: Hide Boilerplate with `#` Lines

**Strength**: SHOULD

**Summary**: Prefix setup lines with `# ` to compile them but not render them. Use this to remove `use` statements, `fn main()` wrappers, mock setup, and `Ok(())` returns.

```rust
/// Sends a request over an established connection.
///
/// # Examples
///
/// ```
/// # struct Connection;
/// # struct Request;
/// # impl Connection {
/// #     fn send(&self, _: Request) -> Result<(), std::io::Error> { Ok(()) }
/// # }
/// # let connection = Connection;
/// # let request = Request;
/// let response = connection.send(request)?;
/// # Ok::<(), std::io::Error>(())
/// ```
pub fn dummy() {}
```

```rust
// ## is the escape — it renders as `# ` (useful for shell prompts in docs).
/// ```text
/// ## cd target/doc
/// ```
```

**Rationale**: Doc tests are compiled as real programs, but most of the scaffolding (imports, error wrappers, test setup) clutters the rendered output. `# ` keeps tests honest without making examples unreadable.

**See also**: DC-09, "Easy doc initialization"

---

## DC-11: Doctest Directives Control Compilation and Execution

**Strength**: SHOULD

**Summary**: Use code-block attributes to tell rustdoc how a block should behave: `no_run`, `should_panic`, `compile_fail`, `ignore`, `text`, or an edition tag.

```rust
/// Opens a TCP connection. The example compiles but we don't actually dial out.
///
/// ```no_run
/// let stream = std::net::TcpStream::connect("example.com:80")?;
/// # Ok::<(), std::io::Error>(())
/// ```
pub fn connect() {}

/// Panics if the index is out of bounds.
///
/// ```should_panic
/// let v = vec![1, 2, 3];
/// let _ = v[10];
/// ```
pub fn panicking_index() {}

/// The type system guarantees this value cannot be mutated.
///
/// ```compile_fail
/// let x = 1;
/// x = 2; // cannot assign twice to immutable variable
/// ```
pub fn immutability_proof() {}

/// Non-Rust snippet; rendered verbatim, not compiled.
///
/// ```text
/// error[E0308]: mismatched types
/// ```
pub fn rendering_a_diagnostic() {}

/// Compile with the 2024 edition regardless of the crate's edition.
///
/// ```edition2024
/// async fn example() {}
/// ```
pub fn edition_specific() {}
```

**Rationale**: Defaults are runnable, compiled doctests. Use `no_run` for network/IO, `should_panic` when the panic is the point, `compile_fail` to assert an invariant the type system enforces, `text` for non-Rust output, and `ignore` only as a last resort (it's rarely what you want — prefer `text` or hiding lines with `#`). Edition tags pin a specific edition for a block.

**See also**: DC-06 (`should_panic` for panic examples), DC-19 (rustdoc lints catch typos like `should-panic`)

---

## DC-12: Use Intra-Doc Links for Cross-References

**Strength**: MUST

**Summary**: Link to other items by Rust path using `[Type]`, `[`Type`]`, `[Type::method]`, or `[crate::module::Type]` — not by manual URL.

```rust
/// An HTTP connection.
///
/// Create one with [`Client::connect`] or [`Client::builder`]. Errors
/// are reported as [`Error`], which wraps [`std::io::Error`] for
/// transport-level failures.
///
/// See also [`Response`] and the [`crate::auth`] module.
pub struct Connection;

impl Client {
    /// Creates a connection. For TLS, see [`Self::connect_tls`].
    pub fn connect() -> Result<Connection, Error> { todo!() }
    /// Creates a TLS-encrypted connection.
    pub fn connect_tls() -> Result<Connection, Error> { todo!() }
}
# pub struct Client;
# pub struct Response;
# #[derive(Debug)] pub enum Error {}
# pub mod auth {}
```

```rust
// Disambiguate namespaces when a name exists as multiple kinds
/// See [`struct@Foo`] for the struct and [`fn@Foo`] for the constructor.
/// Or use the suffix forms: [`Foo()`] for the function, [`some_macro!`]
/// for a macro.

// Backticks are stripped — `[`Vec`]` renders as code AND links
/// Returns a [`Vec<T>`] collecting the items.

// Fragment specifiers link to a section
/// See [formatting parameters] for the full syntax.
///
/// [formatting parameters]: std::fmt#formatting-parameters
```

**Rationale**: Intra-doc links are checked at doc-build time — a broken link is a `rustdoc::broken_intra_doc_links` warning. They survive refactoring (a renamed item updates its links), follow re-exports, and produce correct URLs regardless of where the docs are hosted. `#[doc(hidden)]` items are *not* linkable.

**See also**: C-LINK, DC-13, DC-19

---

## DC-13: Hyperlink Liberally in Prose

**Strength**: SHOULD

**Summary**: Sprinkle intra-doc links through prose — every type name, method reference, and related-item mention should be a link.

```rust
/// Sends a GET request to `url` and returns the [`Response`].
///
/// Returns [`Error::InvalidUrl`] if `url` doesn't parse, or
/// [`Error::Timeout`] if the deadline elapses. See [`Self::post`] for
/// POST requests and [`ClientBuilder::timeout`] for configuring the
/// deadline.
pub async fn get(&self, url: &str) -> Result<Response, Error> { todo!() }
# pub struct Response;
# pub enum Error { InvalidUrl, Timeout }
# pub struct ClientBuilder;
# impl ClientBuilder { pub fn timeout(self, _: std::time::Duration) -> Self { self } }
```

**Rationale**: Rustdoc already auto-links types that appear in the function signature, so prose is where you add value — linking to *related* items the signature doesn't reveal. The `rustdoc::redundant_explicit_links` lint warns when you write `[`Foo`](Foo)` where `[`Foo`]` would do.

**See also**: C-LINK, DC-12

---

## DC-14: Use Lists and Headers Sparingly

**Strength**: SHOULD

**Summary**: Rust docs favor prose. Use bullets only when you're genuinely enumerating items, and avoid `**bold**` for emphasis.

```rust
// ❌ BAD: over-formatted, reads like marketing
/// **Process** user data
///
/// ## Features
/// - Validates input
/// - **Normalizes** data
/// - Stores in database
pub fn process_user() {}

// ✅ GOOD: natural prose
/// Validates the user, normalizes their profile fields, and persists the
/// result to the database.
pub fn process_user_2() {}

// ✅ OK: a bullet list that really is a list
/// Supported configuration formats:
/// - TOML
/// - JSON
/// - YAML
pub fn parse_config() {}
```

**Rationale**: The canonical-sections model (`# Examples`, `# Errors`, etc.) provides the structure. Additional headers and bullet lists usually just add noise.

---

## DC-15: Describe Parameters in Prose, Not Tables

**Strength**: SHOULD

**Summary**: Weave parameter descriptions into the summary and extended docs. Don't build a `# Parameters` table.

```rust
// ❌ BAD: Java/C#-style parameter table
/// Copies a file.
///
/// # Parameters
/// - `src`: source path
/// - `dst`: destination path
/// - `overwrite`: whether to overwrite
pub fn copy_file(src: &std::path::Path, dst: &std::path::Path, overwrite: bool) {}

// ✅ GOOD: prose that mentions the parameter names
/// Copies the file at `src` to `dst`. If `overwrite` is `true`, an
/// existing file at `dst` is replaced; otherwise the function errors.
pub fn copy_file2(src: &std::path::Path, dst: &std::path::Path, overwrite: bool) {}
```

**Rationale**: The signature already shows the types. Prose can explain the interactions (`overwrite: true` vs. `false`) that a table can't. Inline backtick-quoted names make the connection to the signature obvious.

---

## DC-16: Document Public Fields and Enum Variants

**Strength**: SHOULD

**Summary**: Every `pub` field, enum variant, and associated constant deserves its own doc comment.

```rust
/// Client configuration.
#[derive(Debug, Clone)]
pub struct Config {
    /// Server hostname or IP. Required.
    pub host: String,

    /// Port, defaults to `443` for TLS.
    pub port: u16,

    /// Connect deadline. `None` disables the timeout.
    pub timeout: Option<std::time::Duration>,
}

/// Possible parse errors.
#[non_exhaustive]
#[derive(Debug)]
pub enum ParseError {
    /// The input contained a character not allowed by the grammar.
    InvalidChar { line: usize, column: usize },

    /// The input ended before a complete value was parsed.
    UnexpectedEof,

    /// An underlying I/O error occurred.
    Io(std::io::Error),
}
```

**Rationale**: `missing_docs` will catch undocumented public fields if enabled at the crate root. Each variant in an error enum carries a distinct meaning; users need to match on the right one.

---

## DC-17: Crate-Level Docs Are the Front Page

**Strength**: MUST

**Summary**: `lib.rs` opens with `//!` documentation that gives a tagline, a minimal runnable example, and pointers to the main types.

```rust
//! # `my_http` — Ergonomic async HTTP client
//!
//! A small, `tokio`-based HTTP client with connection pooling, automatic
//! retries, and a typed response API.
//!
//! ## Quick start
//!
//! ```
//! # async fn example() -> Result<(), Box<dyn std::error::Error>> {
//! let client = my_http::Client::new();
//! let body = client.get("https://example.com/").await?.text().await?;
//! println!("{body}");
//! # Ok(()) }
//! ```
//!
//! ## Where to go next
//!
//! - [`Client`] — the main entry point
//! - [`ClientBuilder`] — configuration
//! - [`Error`] — error type and variants
//! - The [`auth`] module for credential handling

#![warn(missing_docs)]
#![warn(rustdoc::broken_intra_doc_links)]

pub struct Client;
pub struct ClientBuilder;
#[derive(Debug)] pub enum Error {}
pub mod auth {
    //! Credentials and signing helpers.
}
```

**Rationale**: The crate root is the first thing docs.rs shows. Users evaluate the crate from that page; if it's empty they close the tab. The quick-start example also smoke-tests the top-level API.

**See also**: C-CRATE-DOC, DC-26

---

## DC-18: Document Modules Like Mini-Crates

**Strength**: MUST

**Summary**: Every public module gets a `//!` header: what it contains, when to use it, at least one example.

```rust
pub mod config {
    //! Configuration loading and validation.
    //!
    //! Parses TOML and YAML into a typed [`Config`] tree, merging in
    //! environment-variable overrides (prefixed with `MYAPP_`).
    //!
    //! # Examples
    //!
    //! ```
    //! # fn main() -> Result<(), Box<dyn std::error::Error>> {
    //! # std::env::set_var("MYAPP_PORT", "9090");
    //! let cfg = my_crate::config::load_toml("app.toml")?;
    //! assert_eq!(cfg.port, 9090); // env override wins
    //! # Ok(()) }
    //! ```

    # pub struct Config { pub port: u16 }
    # pub fn load_toml(_: &str) -> Result<Config, std::io::Error> { Ok(Config { port: 9090 }) }
}
```

**Rationale**: `std::fmt`, `std::pin`, and `std::option` are the canonical examples of good module docs. They explain *why the module exists* in addition to what it contains. `rustdoc::missing_crate_level_docs` enforces crate-level docs; `missing_docs` enforces per-module docs when modules are public.

**See also**: M-MODULE-DOCS

---

## DC-19: Turn On the Rustdoc Lints

**Strength**: SHOULD

**Summary**: Enable `missing_docs`, `broken_intra_doc_links`, `invalid_codeblock_attributes`, and friends at the crate root.

```rust
#![warn(missing_docs)]                             // every public item has docs
#![warn(rustdoc::missing_crate_level_docs)]        // lib.rs has //! docs
#![deny(rustdoc::broken_intra_doc_links)]          // [`Foo`] must resolve
#![warn(rustdoc::private_intra_doc_links)]         // don't link from pub to priv
#![warn(rustdoc::invalid_codeblock_attributes)]    // catch `should-panic` typos
#![warn(rustdoc::invalid_html_tags)]               // `<h1>` without `</h1>`
#![warn(rustdoc::invalid_rust_codeblocks)]         // rustdoc can still parse them
#![warn(rustdoc::bare_urls)]                       // `http://...` -> `<http://...>`
#![warn(rustdoc::unescaped_backticks)]             // `` `foo(a, b) ``
#![warn(rustdoc::redundant_explicit_links)]        // `[`Foo`](Foo)` -> `[`Foo`]`
```

```rust
// Namespacing rule: only `missing_docs` is un-prefixed (it's shared with rustc).
// Everything else is `rustdoc::lint_name`.
#![warn(missing_docs)]                     // ✅ correct (shared)
#![warn(broken_intra_doc_links)]           // ❌ wrong — unknown lint to rustc
#![warn(rustdoc::broken_intra_doc_links)]  // ✅ correct
```

**Rationale**: Rustdoc lints (except `missing_docs`) only run during `cargo doc`, so CI must include a doc build. Denying `broken_intra_doc_links` is the single highest-value change you can make — it turns documentation rot into a build error.

**See also**: DC-12, DC-22

---

## DC-20: `#[doc = ...]` and `#[doc = include_str!(...)]`

**Strength**: CONSIDER

**Summary**: `///` is sugar for `#[doc = "..."]`. Drop to the attribute form to build docs dynamically — most usefully to share a README.

```rust
// Sugar equivalence
/// This is a doc comment.
fn a() {}

#[doc = " This is a doc comment."]
fn b() {}

// Multiple #[doc] attributes are merged
#[doc = "Processes"]
#[doc = " input data and"]
#[doc = " returns the result."]
fn c() {}
```

```rust
// Single source of truth for README and crate-level docs
#![doc = include_str!("../README.md")]
```

```rust
// Test that the README's code blocks compile, without polluting the crate
#[cfg(doctest)]
#[doc = include_str!("../README.md")]
pub struct ReadmeDoctests;
```

**Rationale**: `#[doc = include_str!("../README.md")]` keeps the README and the crate's front page in sync — users see the same content on GitHub and docs.rs. Wrap with `#[cfg(doctest)]` on a dummy type if you just want the README's examples tested without making the README your crate-level docs.

**See also**: DC-17, DC-31

---

## DC-21: `#[doc(hidden)]` Hides Items From Docs

**Strength**: SHOULD

**Summary**: Use `#[doc(hidden)]` to keep an item out of the rendered docs without changing its visibility. Use `pub(crate)` when the item should actually be private.

```rust
pub struct PublicError(InternalError);
struct InternalError;

// This impl is a public API detail but users will never name `InternalError`.
// Hide it from the rendered docs but keep it callable.
#[doc(hidden)]
impl From<InternalError> for PublicError {
    fn from(e: InternalError) -> Self { PublicError(e) }
}

// Items that must be `pub` so macros in the same crate can reach them,
// but that aren't part of the public API.
#[doc(hidden)]
pub mod __private {
    pub fn macro_helper() {}
}

// If the item doesn't need to be public at all, use `pub(crate)`.
pub(crate) fn internal_helper() {}
```

**Rationale**: `#[doc(hidden)]` is a documentation-only marker: the item remains callable and is still part of the semver surface. `pub(crate)` is the real access restriction. Reach for `#[doc(hidden)]` only when visibility can't be reduced (macro internals, required trait impls).

**See also**: C-HIDDEN, DC-22

---

## DC-22: `#[doc(inline)]` and `#[doc(no_inline)]` Control Re-Export Rendering

**Strength**: SHOULD

**Summary**: Use `#[doc(inline)]` on a `pub use` to present the item as if it were defined here. Use `#[doc(no_inline)]` to keep it in the opaque "Re-exports" section.

```rust
// Private module — items are automatically inlined at the re-export site
mod inner {
    /// The main client type.
    pub struct Client;
}
pub use self::inner::Client;

// Public module — default is NOT inlined (you'd see "Re-exports: pub use ...")
pub mod detail {
    /// Low-level parser.
    pub struct Parser;
}

// Force inlining so `Parser` appears at the crate root alongside native items
#[doc(inline)]
pub use self::detail::Parser;

// External dependency (Rust 2018+) — NOT inlined by default, add #[doc(inline)]
// explicitly if you want the re-export to feel like a first-class item.
#[doc(inline)]
pub use serde_json::Value as Json;

// Large re-export list — keep out of the flat item listing
#[doc(no_inline)]
pub use self::detail::*;
```

**Rationale**: The default inlining rules are: inline from private modules, don't inline from public modules, don't inline external dependencies (since Rust 2018). Override those defaults when the default presentation obscures your intended API shape — `#[doc(inline)]` on a facade-pattern re-export, `#[doc(no_inline)]` when a glob re-export would flood the page.

**See also**: M-DOC-INLINE

---

## DC-23: Search Aliases with `#[doc(alias = "...")]`

**Strength**: CONSIDER

**Summary**: Add `#[doc(alias)]` attributes so users find items under alternate names — protocol-level names, FFI bindings, acronyms.

```rust
/// A first-in, first-out queue.
#[doc(alias = "FIFO")]
#[doc(alias = "queue")]
pub struct Fifo<T> { /* ... */ items: Vec<T> }

// FFI: wrap a C function while keeping the C name discoverable
impl Fifo<()> {
    /// Enqueues an item.
    #[doc(alias = "lib_fifo_push")]
    pub fn push(&mut self, _item: ()) { /* ... */ }
}

// Equivalent list syntax
#[doc(alias("FIFO", "queue"))]
pub struct Fifo2<T> { items: Vec<T> }
```

**Rationale**: Aliases affect only the search index — the canonical name is unchanged. Especially valuable for FFI bindings, where users know the C function name but not the Rust wrapper, and for well-known acronyms (`FIFO`, `UUID`, `URL`).

---

## DC-24: Feature-Gate with `#[doc(cfg(...))]`

**Strength**: SHOULD

**Summary**: For items behind Cargo features, use `#[cfg_attr(docsrs, doc(cfg(feature = "...")))]` so docs.rs renders a "Available on crate feature `x` only" banner.

```rust
// lib.rs — enable the feature-gating attribute on docs.rs
#![cfg_attr(docsrs, feature(doc_cfg))]

/// Async parser, available behind the `async` feature.
#[cfg(feature = "async")]
#[cfg_attr(docsrs, doc(cfg(feature = "async")))]
pub struct AsyncParser { /* ... */ }
```

```toml
# Cargo.toml — build docs with all features and the `docsrs` cfg set
[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]
```

**Rationale**: Without `doc(cfg)`, a user on docs.rs sees `AsyncParser` with no indication it requires a feature flag, tries to use it, and gets a confusing "not found" error. The banner tells them exactly what to enable. The `doc_cfg` feature is unstable, so gate it behind `#[cfg(docsrs)]` and only use nightly on docs.rs.

**See also**: DC-26

---

## DC-25: `#[cfg(doc)]` for Platform-Independent Docs

**Strength**: CONSIDER

**Summary**: Use `#[cfg(any(target_os = "...", doc))]` to make platform-specific items appear in documentation on all platforms.

```rust
/// Windows-only handle wrapper.
#[cfg(any(windows, doc))]
pub struct WindowsHandle(usize);

/// Unix-only file descriptor wrapper.
#[cfg(any(unix, doc))]
pub struct UnixFd(i32);
```

**Rationale**: Rustdoc sets `cfg(doc)` whenever it's building documentation. Adding `, doc` to a `cfg` predicate keeps the item visible in docs even when the build target wouldn't normally include it. Note that `cfg(doc)` is not passed to doctests — they still obey the real build configuration.

---

## DC-26: Fill In All the Cargo Metadata

**Strength**: MUST

**Summary**: A publishable crate sets `description`, `license`, `repository`, `keywords`, `categories`, `readme`, `rust-version`, and (when needed) `documentation`, `homepage`, and docs.rs metadata.

```toml
[package]
name          = "my_http"
version       = "0.3.0"
edition       = "2021"
rust-version  = "1.75"
description   = "An ergonomic async HTTP client built on tokio."
license       = "MIT OR Apache-2.0"
repository    = "https://github.com/example/my_http"
readme        = "README.md"
keywords      = ["http", "client", "async", "tokio"]
categories    = ["web-programming::http-client", "asynchronous"]

# Only set these if they differ from the defaults:
# documentation = "https://docs.example.com/my_http"   # default is docs.rs
# homepage      = "https://my-http.example.com"        # default is repository

[package.metadata.docs.rs]
all-features     = true
rustdoc-args     = ["--cfg", "docsrs"]
default-target   = "x86_64-unknown-linux-gnu"
```

**Rationale**: Good metadata is what makes your crate discoverable on crates.io and what lets docs.rs build correct documentation. The `documentation` field is only needed if you're hosting docs outside docs.rs; `homepage` is only for a distinct project site (not a duplicate of the repo URL).

**See also**: C-METADATA, guide 12 (project-structure)

---

## DC-27: Link to the Playground and External Docs

**Strength**: CONSIDER

**Summary**: Set crate-level doc attributes for a logo, favicon, and (for user-facing examples) a playground URL.

```rust
#![doc(
    html_logo_url = "https://example.com/my_http/logo.svg",
    html_favicon_url = "https://example.com/my_http/favicon.ico",
    html_root_url = "https://docs.rs/my_http/0.3.0",
)]
```

**Rationale**: `html_root_url` is only needed when rustdoc can't infer where your crate's docs live (for crates not on docs.rs, or when external tools consume the docs). Set a logo if the crate has a brand, otherwise leave the defaults alone — a bland default is better than a stretched ad.

---

## DC-28: Maintain a CHANGELOG and Tag Releases

**Strength**: MUST

**Summary**: Every release gets a CHANGELOG entry and an annotated Git tag. Breaking changes are called out explicitly.

```markdown
# Changelog

All notable changes to this project will be documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-04-20

### Added
- `Client::builder` for configuring timeouts and retries.

### Changed
- **Breaking:** `Client::get` now returns `Response` instead of `String`.
  Call `.text().await?` on the result to restore the previous behavior.

### Fixed
- Resolved a deadlock in the connection pool under high concurrency.

## [0.2.0] - 2026-01-15
...
```

```bash
# Annotated tags survive `git describe` and carry the release message
git tag -a -m "Release 0.3.0" 0.3.0
git push --tags
```

**Rationale**: Users need to know what changed before upgrading. Annotated tags carry metadata that lightweight tags don't, and several Git commands skip unannotated ones.

**See also**: C-RELNOTES

---

## DC-29: Document Trait Contracts and Implementation Requirements

**Strength**: SHOULD

**Summary**: On a public trait, document the invariants implementers must uphold, the default-method behavior, and which methods are required vs. provided.

```rust
/// A stable, deterministic byte encoding.
///
/// # Implementing
///
/// Implementations must ensure:
///
/// 1. Equal values produce equal byte sequences (determinism).
/// 2. The encoding fully represents the value — round-tripping via
///    [`Self::from_bytes`] yields an equal value.
/// 3. Implementations are panic-free on well-formed input.
///
/// The blanket `impl<T: AsRef<[u8]>>` handles anything already byte-like;
/// prefer implementing directly on your concrete type otherwise.
pub trait ToBytes {
    /// Encodes `self` into a byte sequence.
    fn to_bytes(&self) -> Vec<u8>;

    /// Decodes a byte sequence into `Self`.
    ///
    /// # Errors
    ///
    /// Returns an error if `bytes` is not a valid encoding.
    fn from_bytes(bytes: &[u8]) -> Result<Self, std::io::Error>
    where
        Self: Sized;
}
```

**Rationale**: A trait is a contract. Without the "Implementing" section, users have to guess whether the trait requires total functions, panic-freedom, or particular ordering. State the invariants so implementers can comply and callers can rely on them.

---

## DC-30: Easy Doc Initialization With Hidden Helpers

**Strength**: CONSIDER

**Summary**: When a type is expensive to construct, wrap each doc example in a hidden helper `fn` so callers see only the relevant call.

```rust
pub struct Connection { /* many fields */ }
pub struct Request;
pub struct Response;

impl Connection {
    /// Sends `request` and returns the server's response.
    ///
    /// # Examples
    ///
    /// ```
    /// # struct Connection; struct Request; struct Response;
    /// # impl Connection { fn send(&self, _: Request) -> Response { Response } }
    /// # fn call_send(connection: Connection, request: Request) {
    /// let response = connection.send(request);
    /// # let _ = response;
    /// # }
    /// ```
    pub fn send(&self, _request: Request) -> Response { Response }
}
```

**Rationale**: The example compiles (proving the method call is valid) without forcing every reader to scroll past three lines of setup. The trade-off is that any assertions inside the hidden function compile but never *run* — for testable assertions, fall back to a `#[doc(hidden)]` public helper constructor.

---

## DC-31: Keep README and Crate Docs in Sync

**Strength**: CONSIDER

**Summary**: `#![doc = include_str!("../README.md")]` makes the README the single source of truth for both the GitHub landing page and the docs.rs front page.

```rust
// lib.rs
#![doc = include_str!("../README.md")]
#![warn(missing_docs)]

// If the README uses `cargo` code blocks or GitHub-flavored features
// that rustdoc can't parse, confine the inclusion to the doctest:
#[cfg(doctest)]
#[doc = include_str!("../README.md")]
pub struct ReadmeDoctests;
```

**Rationale**: Drift between README and crate docs is a steady source of confusion. Including the README directly eliminates it. Caveats: the README must be valid rustdoc Markdown, intra-doc links must work relative to the crate, and code blocks must compile as doctests (or be marked `text` / `ignore`).

---

## DC-32: Prefer `--document-private-items` for Internal Docs

**Strength**: CONSIDER

**Summary**: Run `cargo doc --document-private-items` to generate internal documentation; tune `private_intra_doc_links` accordingly.

```bash
# Internal docs (includes private items, marked with a lock icon)
cargo doc --document-private-items --open

# Public docs (what users see on docs.rs)
cargo doc --no-deps --open
```

```rust
// If some public item genuinely needs to link to a private one, acknowledge it
#![allow(rustdoc::private_intra_doc_links)]
```

**Rationale**: Internal docs are a useful onboarding tool for larger codebases. The `private_intra_doc_links` lint catches the case where a public item links to a private one — such a link works when the user runs `cargo doc` locally with `--document-private-items`, but breaks on docs.rs where only the public view is built.

---

## DC-33: Enable Scraped Examples for Real-World Usage

**Strength**: CONSIDER

**Summary**: Enable rustdoc's scraped-examples feature so code in `examples/` auto-appears on the docs for items it uses.

```toml
# Cargo.toml
[package.metadata.docs.rs]
cargo-args = ["-Zunstable-options", "-Zrustdoc-scrape-examples"]
```

```bash
# Locally
cargo doc -Zunstable-options -Zrustdoc-scrape-examples
```

**Rationale**: Scraped examples let the code in your `examples/` directory double as documentation. Rustdoc pulls snippets that call each public item (up to five per item, smallest first, one visible by default with the rest under a toggle). Currently unstable — requires nightly — but widely used on docs.rs.

---

## Documentation Checklist

A one-shot template for documenting a public item. Delete sections that don't apply.

```rust
/// Summary sentence in one line, ~15 words or fewer.
///
/// Extended description: what this does, when to use it, and how it
/// relates to [`Neighbor`] types via intra-doc links.
///
/// # Examples
///
/// ```
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// use my_crate::item;
/// let value = item("input")?;
/// assert_eq!(value.status(), "ok");
/// # Ok(()) }
/// ```
///
/// # Errors
///
/// (For Result-returning functions.) Returns [`Error::InvalidInput`] if
/// `input` is empty, [`Error::Io`] if disk I/O fails.
///
/// # Panics
///
/// (When applicable.) Panics if the global allocator fails.
///
/// # Safety
///
/// (Required for `unsafe fn`.) The caller must ensure that `input`
/// points to a valid, initialized buffer of at least `len` bytes.
pub fn item(input: &str) -> Result<Value, Error> { todo!() }
# struct Neighbor; struct Value; impl Value { fn status(&self) -> &str { "ok" } }
# enum Error { InvalidInput, Io }
```

Reference checklist:

1. First sentence ≤ 15 words, one line (DC-03).
2. Extended description uses intra-doc links for every type mentioned (DC-12, DC-13).
3. `# Examples` uses `?`, not `unwrap`; hides boilerplate with `#` lines (DC-09, DC-10).
4. `# Errors` / `# Panics` / `# Safety` present when applicable (DC-05, DC-06, DC-07).
5. Every `pub` field and variant has its own doc comment (DC-16).
6. Crate-level and module-level `//!` docs exist (DC-17, DC-18).
7. Crate-root attribute block enables the rustdoc lints (DC-19).
8. Cargo.toml has full metadata and docs.rs configuration (DC-26).


## Module Template

Drop this at the top of a new module; delete the sections that don't apply.

```rust
//! Short one-sentence summary of what this module provides.
//!
//! Extended description: what kinds of types live here, the problem this
//! module solves, and how it relates to sibling modules via
//! [`crate::sibling`] links.
//!
//! # Examples
//!
//! ```
//! # fn main() -> Result<(), Box<dyn std::error::Error>> {
//! use my_crate::my_module::{Thing, do_thing};
//!
//! let thing = Thing::new();
//! do_thing(&thing)?;
//! # Ok(()) }
//! ```
//!
//! # Design
//!
//! (Optional.) Key architectural decisions — zero-copy parsing, single
//! dispatch point, cancellation strategy — anything that informs how
//! callers should reason about the module.
//!
//! # Feature flags
//!
//! (Optional.) This module is available when the `foo` feature is enabled.

#![warn(missing_docs)]

/// A thing this module operates on.
pub struct Thing { /* ... */ }

impl Thing {
    /// Constructs a new `Thing` with default settings.
    pub fn new() -> Self { Self {} }
}

/// Does the thing.
///
/// # Errors
///
/// Returns an error if the thing is in an invalid state.
pub fn do_thing(_: &Thing) -> Result<(), std::io::Error> { Ok(()) }
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| DC-01 Every public item documented | MUST | `#![warn(missing_docs)]` at the crate root |
| DC-02 `///` vs `//!` | MUST | Outer documents next item, inner documents enclosing |
| DC-03 First sentence ≤ 15 words | MUST | Summary line stays on one line in listings |
| DC-04 Canonical sections | MUST | `# Examples` → `# Errors` → `# Panics` → `# Safety` |
| DC-05 `# Errors` section on `Result` | MUST | Document which variants occur and why |
| DC-06 `# Panics` section | MUST | Every documented panic condition |
| DC-07 `# Safety` required on `unsafe fn` | MUST | Enumerate every caller obligation |
| DC-08 Every item has an example | SHOULD | Show *why*, not just *how* |
| DC-09 Examples use `?`, not `unwrap` | MUST | Hidden `fn main() -> Result<...>` pattern |
| DC-10 Hide boilerplate with `#` | SHOULD | Compile but don't render setup lines |
| DC-11 Doctest directives | SHOULD | `no_run`, `should_panic`, `compile_fail`, `text` |
| DC-12 Intra-doc links | MUST | `[`Type`]`, `[Type::method]`, `[crate::path]` |
| DC-13 Hyperlink in prose | SHOULD | Every type/method mention is a link |
| DC-15 Parameters in prose | SHOULD | No parameter tables |
| DC-17 Crate-level `//!` docs | MUST | Tagline, quick-start example, top-level pointers |
| DC-18 Module-level `//!` docs | MUST | Every public module has a header |
| DC-19 Enable rustdoc lints | SHOULD | Deny `broken_intra_doc_links`, warn on the rest |
| DC-20 `#[doc = include_str!]` | CONSIDER | Share a README as crate-level docs |
| DC-21 `#[doc(hidden)]` for noise | SHOULD | Hide from docs; use `pub(crate)` for real privacy |
| DC-22 `#[doc(inline)]` / `no_inline` | SHOULD | Present re-exports as first-class or as a block |
| DC-23 `#[doc(alias)]` for search | CONSIDER | FFI names, acronyms, alternate spellings |
| DC-24 `#[doc(cfg(feature = ...))]` | SHOULD | Show feature gates in docs.rs |
| DC-26 Cargo metadata complete | MUST | description, license, repository, keywords, categories |
| DC-28 CHANGELOG + annotated tags | MUST | Label breaking changes explicitly |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `Debug`/`Display` impls that the docs describe.
- **API Design**: See `02-api-design.md` for naming and signature patterns that shape the docs.
- **Error Handling**: See `03-error-handling.md` for the error types the `# Errors` section describes.
- **Type Design**: See `05-type-design.md` for invariants that the `# Safety` section enforces.
- **Project Structure**: See `12-project-structure.md` for the Cargo.toml metadata and repository layout that support DC-26.


## External References

- [The Rustdoc Book](https://doc.rust-lang.org/rustdoc/) — authoritative reference for doc comments, doctests, intra-doc links, `#[doc]` attributes, re-export inlining, lints, and advanced features.
- [Rust API Guidelines — Documentation](https://rust-lang.github.io/api-guidelines/documentation.html) — C-CRATE-DOC, C-EXAMPLE, C-QUESTION-MARK, C-FAILURE, C-LINK, C-METADATA, C-RELNOTES, C-HIDDEN.
- [The Rust Programming Language — Chapter 14.2: Publishing a Crate to Crates.io](https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io.html) — Cargo metadata, crate-level docs, tagging releases.
- [RFC 1574 — API Documentation Conventions](https://rust-lang.github.io/rfcs/1574-more-api-documentation-conventions.html) — "Link all the things."
- [RFC 1687 — Crate-Level Documentation](https://rust-lang.github.io/rfcs/1687-crates-io-default-ranking.html) — what belongs on the front page.
- [docs.rs: About](https://docs.rs/about) — feature builds, `[package.metadata.docs.rs]` configuration, `--cfg docsrs`.
- Pragmatic Rust Guidelines: M-CANONICAL-DOCS, M-DOC-INLINE, M-FIRST-DOC-SENTENCE, M-MODULE-DOCS.
