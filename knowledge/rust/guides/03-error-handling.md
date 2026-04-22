# Error Handling Guidelines

Patterns for designing and propagating errors in Rust: when to return `Result` vs panic, how to shape error types (`thiserror` for libraries, `anyhow` for applications), how to add context, chain sources, capture backtraces, stay exception-safe under unwinding, and marshal errors across an FFI boundary. Emphasis is on making errors actionable for callers and cheap for the happy path.


## EH-01: `Result` for Recoverable Failures, `panic!` for Bugs

**Strength**: MUST

**Summary**: Return `Result` when the caller can reasonably handle the failure at runtime. Panic only when you have detected a bug, an impossible state, or a contract violation that no caller can act on.

```rust
// ✅ GOOD: file missing / malformed — the caller can handle it
pub fn read_config(path: &Path) -> Result<Config, ConfigError> {
    let contents = std::fs::read_to_string(path)?;
    toml::from_str(&contents).map_err(ConfigError::parse)
}

// ✅ GOOD: an index-out-of-bounds is a caller bug — panic is correct
pub fn divide_by(x: u32, y: u32) -> u32 {
    assert!(y != 0, "divide_by called with y == 0 (contract violation)");
    x / y
}

// ❌ BAD: panicking on an expected runtime condition
pub fn read_config_bad(path: &Path) -> Config {
    let contents = std::fs::read_to_string(path)
        .expect("config must exist");         // user may legitimately not have it
    toml::from_str(&contents).unwrap()
}

// ❌ BAD: inventing an error variant for a bug the caller cannot act on
pub fn first(data: &[i32]) -> Result<i32, Error> {
    if data.is_empty() { return Err(Error::EmptyData); }  // should be a debug_assert
    Ok(data[0])
}
```

**Rationale**: Pragmatic Rust's M-PANIC-IS-STOP / M-PANIC-ON-BUG frames this cleanly: panics are "stop the program now," not a control-flow mechanism. If the failure is inherent (parsing, I/O, network, validation of external input), return `Result`. If the failure proves a bug in the caller or the library itself, panic — introducing an `Error` variant for it creates impossible-to-handle error-handling code.

**See also**: EH-02, EH-03, M-PANIC-IS-STOP, M-PANIC-ON-BUG

---

## EH-02: The Three Valid Reasons to Panic

**Strength**: SHOULD

**Summary**: A panic is justifiable in exactly three cases: a detected bug, a mathematically impossible state, or the user explicitly asked for panicking semantics.

```rust
use std::sync::LazyLock;

// 1. BUG — an invariant the type itself guarantees was violated somehow
impl<T> NonEmpty<T> {
    pub fn first(&self) -> &T {
        self.inner.first()
            .expect("NonEmpty invariant: constructor rejects empty input")
    }
}

// 2. IMPOSSIBLE — the Result variant is unreachable given the inputs
static DATE_RE: LazyLock<regex::Regex> = LazyLock::new(|| {
    regex::Regex::new(r"^\d{4}-\d{2}-\d{2}$")
        .expect("hardcoded regex is valid")      // literal input, cannot fail
});

// 3. USER-REQUESTED — the API contract says "panic on misuse", documented
impl<T> MyVec<T> {
    /// # Panics
    /// Panics if the vector is empty.
    pub fn head(&self) -> &T {
        self.first().expect("MyVec::head called on empty vector")
    }

    /// Non-panicking counterpart.
    pub fn try_head(&self) -> Option<&T> { self.first() }
}

// Const context is the fourth, narrow case: Result cannot be used in const fn.
const BITS: u32 = const { u32::from_str_radix("1010", 2).unwrap() };
```

**Rationale**: Anything outside these categories is either "bad input" (which wants `Result`) or "dangerous operation" (which is not the same as `unsafe` or `panic`). Always pair a panicking method with a `try_` alternative when feasible (EH-18) and document `# Panics` (EH-14).

**See also**: EH-01, EH-14, EH-18

---

## EH-03: Prefer Correct-by-Construction Over Panics

**Strength**: SHOULD

**Summary**: If you find yourself reaching for `assert!` or `panic!`, first consider whether the type system can rule out the bad state entirely.

```rust
use std::num::NonZeroU32;

// ❌ Runtime panic — caller sees it only when they hit it
pub fn divide(x: u32, y: u32) -> u32 {
    assert!(y != 0);
    x / y
}

// ✅ Correct-by-construction — impossible to call with zero
pub fn divide_nz(x: u32, y: NonZeroU32) -> u32 { x / y.get() }

// ❌ Panic on empty input
pub fn first_char_panic(s: &str) -> char {
    s.chars().next().expect("non-empty string required")
}

// ✅ The type encodes the invariant
pub struct NonEmptyStr(str);            // DST newtype, constructor enforces non-empty
pub fn first_char(s: &NonEmptyStr) -> char {
    // SAFETY: constructor guarantees at least one char.
    unsafe { s.0.chars().next().unwrap_unchecked() }
}
```

**Rationale**: Runtime panics fail at runtime — always worse than a compile error. When the invariant is cheap to carry in a type (`NonZero*`, newtypes, enums for state machines — see guide 05 TD-03, TD-06), prefer that over a panicking guard.

**See also**: EH-02, guide 05 TD-03, TD-06, TD-20

---

## EH-04: Libraries Define Their Own Error Types

**Strength**: MUST

**Summary**: Public library APIs return a named, matchable error type — not `Box<dyn Error>` and not `anyhow::Error`.

```rust
// ❌ OPAQUE: callers cannot react to specific failures
pub fn parse(input: &str) -> Result<Ast, Box<dyn std::error::Error>> { todo!() }

// ❌ OPAQUE (and pulls anyhow into your public API)
pub fn parse(input: &str) -> anyhow::Result<Ast> { todo!() }

// ✅ GOOD: named type — callers can pattern-match, log, retry, wrap
use thiserror::Error;

#[derive(Debug, Error)]
#[non_exhaustive]
pub enum ParseError {
    #[error("unexpected token '{found}' at position {position}, expected {expected}")]
    UnexpectedToken { found: String, expected: String, position: usize },

    #[error("unexpected end of input")]
    UnexpectedEof,

    #[error("invalid number")]
    InvalidNumber(#[from] std::num::ParseIntError),

    #[error("I/O error")]
    Io(#[from] std::io::Error),
}

pub fn parse(input: &str) -> Result<Ast, ParseError> { todo!() }
```

**Rationale**: A library's error type is part of its public contract. Consumers need to match on failure modes, add context, or translate into their own error. `Box<dyn Error>` erases that contract; `anyhow::Error` forces the library's choice of error framework onto every downstream user.

**See also**: EH-05, EH-11, M-APP-ERROR, C-GOOD-ERR

---

## EH-05: Applications Can Use `anyhow` / `eyre`

**Strength**: CONSIDER

**Summary**: Binaries — the leaf of the dependency graph — may use `anyhow::Result` (or `eyre::Result`) for convenient, context-rich error aggregation. Libraries must not.

```rust
use anyhow::{bail, ensure, Context, Result};

fn main() -> Result<()> {
    let path = std::env::var("CONFIG_PATH")
        .context("CONFIG_PATH not set")?;

    let contents = std::fs::read_to_string(&path)
        .with_context(|| format!("failed to read {path}"))?;

    ensure!(contents.len() < 1_000_000, "config file too large: {} bytes", contents.len());

    if contents.trim().is_empty() { bail!("config file is empty"); }

    let cfg: Config = toml::from_str(&contents)
        .with_context(|| format!("failed to parse {path}"))?;

    run(cfg).context("server crashed")
}
```

```rust
// ❌ In a LIBRARY — forces anyhow on every consumer, loses matchability
pub fn parse_config(path: &Path) -> anyhow::Result<Config> { todo!() }
```

**Rationale**: An application is the end of the call chain — its errors are printed, not matched. `anyhow` gives you `.context()`, `bail!`, `ensure!`, and nicely formatted error chains for free. In a library, however, the error type is part of your API; using `anyhow` hides it.

**See also**: EH-04, EH-08, M-APP-ERROR

---

## EH-06: `Option` vs `Result` Decision

**Strength**: SHOULD

**Summary**: Use `Option` when absence is a normal outcome with one self-evident reason. Use `Result` when failure has multiple reasons or benefits from a message.

```rust
// ✅ Option — only one possible reason for absence ("not in the map")
fn find_user(id: UserId, users: &HashMap<UserId, User>) -> Option<&User> {
    users.get(&id)
}

// ✅ Result — multiple failure modes that deserve distinction
fn parse_port(s: &str) -> Result<u16, ParsePortError> {
    let n: u16 = s.parse().map_err(|_| ParsePortError::InvalidFormat)?;
    if n < 1024 { return Err(ParsePortError::Reserved(n)); }
    Ok(n)
}

// ❌ Option loses information — caller cannot tell why it failed
fn parse_port_bad(s: &str) -> Option<u16> {
    let n: u16 = s.parse().ok()?;
    if n < 1024 { return None; }   // "reserved" and "not a number" conflated
    Some(n)
}

// Conversion idioms
fn to_result<T>(o: Option<T>) -> Result<T, NotFound> { o.ok_or(NotFound) }
fn to_option<T, E>(r: Result<T, E>) -> Option<T>     { r.ok() }
```

**Rationale**: `Option` is the right tool when the failure needs no explanation; `Result` when it does. Don't flatten a genuinely-multi-mode failure into `Option<T>` — callers have to guess.

**See also**: EH-32

---

## EH-07: Avoid `unwrap()` and `expect()` in Library Code

**Strength**: SHOULD

**Summary**: Libraries propagate errors. `unwrap()`/`expect()` is acceptable only when the success is provable at the call site — and even then, `expect` with a justifying message is preferable to `unwrap`.

```rust
// ❌ BAD: library panics on malformed user input
pub fn parse_config(s: &str) -> Config {
    serde_json::from_str(s).unwrap()
}

// ✅ GOOD: library returns Result
pub fn parse_config(s: &str) -> Result<Config, ConfigError> {
    serde_json::from_str(s).map_err(ConfigError::json)
}

// ✅ ACCEPTABLE: literal input — infallibility is provable
use std::sync::LazyLock;
static DATE_RE: LazyLock<regex::Regex> =
    LazyLock::new(|| regex::Regex::new(r"^\d{4}-\d{2}-\d{2}$")
        .expect("hardcoded regex is valid"));

// ✅ ACCEPTABLE: invariant enforced elsewhere — document the Panics section
impl<T> NonEmpty<T> {
    /// # Panics
    /// Never — the constructor rejects empty vectors.
    pub fn first(&self) -> &T {
        self.inner.first().expect("NonEmpty invariant")
    }
}

// ✅ ACCEPTABLE in tests
#[test]
fn parses_a_valid_config() {
    let cfg: Config = serde_json::from_str(VALID).unwrap();
    assert_eq!(cfg.port, 8080);
}
```

**Rationale**: Every `unwrap` in library code is a latent panic in someone else's application. `expect` at least documents the assumption, making the panic diagnosable when it fires.

---

## EH-08: Use `?` for Propagation

**Strength**: MUST

**Summary**: Propagate errors with `?`, not explicit `match`. The `?` operator calls `From` for you to convert error types.

```rust
// ❌ VERBOSE
fn fetch(url: &str) -> Result<User, AppError> {
    let response = match http::get(url) {
        Ok(r) => r,
        Err(e) => return Err(e.into()),
    };
    let body = match response.text() {
        Ok(b) => b,
        Err(e) => return Err(e.into()),
    };
    match serde_json::from_str(&body) {
        Ok(u) => Ok(u),
        Err(e) => Err(e.into()),
    }
}

// ✅ CONCISE
fn fetch(url: &str) -> Result<User, AppError> {
    let response = http::get(url)?;
    let body = response.text()?;
    let user = serde_json::from_str(&body)?;
    Ok(user)
}

// ? also works on Option, shorting out with None
fn first_word(s: &str) -> Option<&str> {
    let w = s.split_whitespace().next()?;
    Some(w.trim_end_matches('.'))
}
```

**Rationale**: `?` is the canonical propagation form. It applies `From::from` to the error, which is why implementing `From<UpstreamError>` for your error type (EH-09) makes `?` just work across type boundaries.

---

## EH-09: Error Conversion via `From`

**Strength**: MUST

**Summary**: Implement `From<UpstreamError>` for your error type. `?` calls it automatically; a `#[from]` attribute in `thiserror` generates it.

```rust
use thiserror::Error;

#[derive(Debug, Error)]
#[non_exhaustive]
pub enum AppError {
    #[error("I/O error")]
    Io(#[from] std::io::Error),            // auto From<io::Error>

    #[error("parse error")]
    Parse(#[from] std::num::ParseIntError),

    #[error("config missing key '{0}'")]
    MissingKey(String),                    // no From — constructed by hand
}

// Manual equivalent when not using thiserror:
impl From<std::io::Error> for AppError {
    fn from(e: std::io::Error) -> Self { AppError::Io(e) }
}

// Now ? automatically converts both:
fn read_number(path: &str) -> Result<i32, AppError> {
    let s = std::fs::read_to_string(path)?;    // io::Error → AppError
    let n: i32 = s.trim().parse()?;            // ParseIntError → AppError
    Ok(n)
}
```

**Rationale**: `From` is the type-system hook that makes `?` ergonomic. Without it, every call site needs a `.map_err(...)`. With it, propagation is free. Pair each `From` with a matching `#[error(...)]` message so the source chain displays usefully.

**See also**: EH-08, EH-12, C-CONV-TRAITS

---

## EH-10: Error Types Implement `std::error::Error`

**Strength**: MUST

**Summary**: Every public error type must implement `Error` plus `Debug`, `Display`, `Send`, and `Sync`. `Error` requires `Display + Debug`; `Send + Sync` lets errors cross threads.

```rust
use std::fmt;

#[derive(Debug)]
pub struct EmptyInput;

impl fmt::Display for EmptyInput {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("input was empty")
    }
}

impl std::error::Error for EmptyInput {}

// The full contract any public error type should satisfy:
//    Error + Debug + Display + Send + Sync + 'static
// Automatic as long as every field is Send + Sync + 'static.
fn is_ok<E: std::error::Error + Send + Sync + 'static>(_: &E) {}
```

**Rationale**: `Display` is for users (see guide 05 TD-13 — `Error: Display + Debug` is what makes error types renderable). `Debug` is for programmers. `Send + Sync + 'static` is what `anyhow::Error`, `Box<dyn Error + Send + Sync>`, and most async error plumbing demand. Skipping any of these breaks composition with the ecosystem.

**See also**: EH-14, guide 05 TD-12, TD-13, C-GOOD-ERR

---

## EH-11: Don't Expose `ErrorKind` Directly

**Strength**: MUST

**Summary**: Keep the failure-mode enum private. Expose helper methods (`is_not_found`, `source`, accessors) instead of letting callers match on every variant.

```rust
use std::path::PathBuf;

pub struct ConfigError {
    kind: ErrorKind,
    backtrace: std::backtrace::Backtrace,
}

#[derive(Debug)]
pub(crate) enum ErrorKind {                     // pub(crate) — internal only
    NotFound(PathBuf),
    Parse { path: PathBuf, line: usize, msg: String },
    Io(std::io::Error),
}

impl ConfigError {
    pub fn is_not_found(&self) -> bool { matches!(self.kind, ErrorKind::NotFound(_)) }
    pub fn is_parse_error(&self) -> bool { matches!(self.kind, ErrorKind::Parse { .. }) }

    pub fn path(&self) -> Option<&Path> {
        match &self.kind {
            ErrorKind::NotFound(p) | ErrorKind::Parse { path: p, .. } => Some(p),
            _ => None,
        }
    }
}

// Adding a new ErrorKind variant is no longer a breaking change.
```

**Rationale**: A public variant list locks your failure taxonomy forever — adding a variant forces a major version bump. Hide the enum and provide intention-revealing queries. If you must expose the enum, mark it `#[non_exhaustive]` (EH-13).

**See also**: EH-13, EH-15, M-ERRORS-CANONICAL-STRUCTS

---

## EH-12: Add Context When You Add a Layer

**Strength**: SHOULD

**Summary**: Don't pass a raw `io::Error` up four layers. Either wrap it with domain-specific context (`thiserror` `#[source]`) or attach a `.context(...)` message (`anyhow`).

```rust
// ❌ Raw error — "No such file" but which file?
fn process_file(path: &Path) -> Result<Data, std::io::Error> {
    let contents = std::fs::read_to_string(path)?;
    todo!()
}

// ✅ thiserror: structured wrapping with a source chain
use thiserror::Error;

#[derive(Debug, Error)]
pub enum ProcessError {
    #[error("failed to read {path}")]
    ReadFile {
        path: PathBuf,
        #[source]                              // exposed via Error::source()
        source: std::io::Error,
    },
    #[error("failed to parse {path}")]
    Parse { path: PathBuf, #[source] source: serde_json::Error },
}

fn process_file(path: &Path) -> Result<Data, ProcessError> {
    let contents = std::fs::read_to_string(path)
        .map_err(|source| ProcessError::ReadFile { path: path.to_owned(), source })?;
    serde_json::from_str(&contents)
        .map_err(|source| ProcessError::Parse { path: path.to_owned(), source })
}

// ✅ anyhow (applications): free-form string context
use anyhow::{Context, Result};
fn process_file_app(path: &Path) -> Result<Data> {
    let contents = std::fs::read_to_string(path)
        .with_context(|| format!("failed to read {}", path.display()))?;
    let data = serde_json::from_str(&contents)
        .with_context(|| format!("failed to parse {}", path.display()))?;
    Ok(data)
}
```

**Rationale**: An error message is only as useful as the context it carries. Wrap at every layer where the calling code introduces new information (a filename, a request ID, a retry count). Use `with_context` rather than `context` when the message requires allocation — the closure isn't called on the happy path.

---

## EH-13: Mark Public Error Enums `#[non_exhaustive]`

**Strength**: SHOULD

**Summary**: If you must expose variants, add `#[non_exhaustive]` so adding a variant later isn't a breaking change.

```rust
#[derive(Debug, thiserror::Error)]
#[non_exhaustive]                              // callers must include _ arm
pub enum DatabaseError {
    #[error("connection failed")]
    ConnectionFailed(#[source] std::io::Error),

    #[error("query timed out after {duration:?}")]
    Timeout { duration: std::time::Duration },

    #[error("record not found: {0}")]
    NotFound(String),
}

// Consumer code is forced to carry a catch-all
match err {
    DatabaseError::ConnectionFailed(_) => retry(),
    DatabaseError::Timeout { .. }      => retry(),
    DatabaseError::NotFound(_)         => create(),
    _ => log_unexpected(),                     // forward-compatible
}
```

**Rationale**: Without `#[non_exhaustive]`, downstream `match` statements must be exhaustive — adding a variant is a breaking change. With it, the compiler forces callers to handle the "new variant" case up front, freeing you to grow the enum. See guide 05 TD-07.

**See also**: EH-11, guide 05 TD-07

---

## EH-14: Document Errors, Panics, and Safety

**Strength**: MUST

**Summary**: Public fallible functions must document an `# Errors` section. Panicking functions need a `# Panics` section. `unsafe` functions need a `# Safety` section.

```rust
/// Parses a network address from a string.
///
/// # Errors
///
/// - [`ParseError::InvalidFormat`] if the input is not `"host:port"`.
/// - [`ParseError::InvalidPort`] if the port is not a valid `u16`
///   or falls in the reserved range (`< 1024`).
pub fn parse_address(s: &str) -> Result<SocketAddr, ParseError> { todo!() }

/// Inserts an element at `index`, shifting later elements right.
///
/// # Panics
///
/// Panics if `index > self.len()`.
pub fn insert(&mut self, index: usize, element: T) { /* ... */ }

/// # Safety
///
/// The caller must ensure `ptr` is non-null, aligned, and points to a
/// valid `T` that will not be accessed through another reference during
/// this call.
pub unsafe fn from_raw(ptr: *mut T) -> Self { /* ... */ todo!() }
```

**Rationale**: These three sections are load-bearing rustdoc conventions (C-FAILURE). The tool-chain parses them; developers grep for them; `# Errors` in particular is the only place a caller can learn what to handle short of reading the source.

**See also**: guide 13 on documentation, C-FAILURE

---

## EH-15: Errors Are Canonical Structs with Backtraces

**Strength**: SHOULD

**Summary**: For crates that care about diagnostics, prefer a `struct { kind: ErrorKind, backtrace: Backtrace }` shape over a bare enum. It gives you a stable public type, private variants (EH-11), and always-on backtraces.

```rust
use std::backtrace::Backtrace;
use std::fmt;

pub struct ConfigError {
    kind: ErrorKind,
    backtrace: Backtrace,
}

#[derive(Debug)]
pub(crate) enum ErrorKind {
    NotFound(std::io::Error),
    Parse(toml::de::Error),
    InvalidFormat { field: String, reason: String },
}

impl ConfigError {
    pub(crate) fn not_found(err: std::io::Error) -> Self {
        Self { kind: ErrorKind::NotFound(err), backtrace: Backtrace::capture() }
    }
    pub(crate) fn parse(err: toml::de::Error) -> Self {
        Self { kind: ErrorKind::Parse(err), backtrace: Backtrace::capture() }
    }
    pub fn is_not_found(&self) -> bool { matches!(self.kind, ErrorKind::NotFound(_)) }
    pub fn backtrace(&self) -> &Backtrace { &self.backtrace }
}

impl fmt::Display for ConfigError { /* see EH-17 */
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.kind {
            ErrorKind::NotFound(_)              => f.write_str("configuration file not found"),
            ErrorKind::Parse(_)                 => f.write_str("failed to parse configuration"),
            ErrorKind::InvalidFormat { field, reason } =>
                write!(f, "invalid field {field}: {reason}"),
        }
    }
}

impl fmt::Debug for ConfigError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{self}\n{}", self.backtrace)
    }
}

impl std::error::Error for ConfigError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match &self.kind {
            ErrorKind::NotFound(e)       => Some(e),
            ErrorKind::Parse(e)          => Some(e),
            ErrorKind::InvalidFormat { .. } => None,
        }
    }
}
```

**Rationale**: A canonical struct gives you control: variant additions don't break callers (EH-11), backtraces are always present, and you can implement `Debug` to include the backtrace for logs without polluting `Display`. See the Common Patterns section at the end for the full reusable template.

**See also**: EH-16, EH-17, M-ERRORS-CANONICAL-STRUCTS

---

## EH-16: Capture a Backtrace When the Error Is Born

**Strength**: MUST

**Summary**: Call `Backtrace::capture()` in every error constructor and in every `From` impl. Capture is free when `RUST_BACKTRACE` is unset, but invaluable when it's set.

```rust
use std::backtrace::Backtrace;

impl DatabaseError {
    pub(crate) fn connection_failed(err: std::io::Error) -> Self {
        Self { kind: ErrorKind::Connection(err), backtrace: Backtrace::capture() }
    }
}

impl From<std::io::Error> for DatabaseError {
    fn from(err: std::io::Error) -> Self {
        // Capture HERE — the ? site is where the error was born
        Self { kind: ErrorKind::Io(err), backtrace: Backtrace::capture() }
    }
}

// A private bail! macro makes "construct + capture" a one-liner
macro_rules! bail {
    ($kind:expr) => {
        return Err($crate::DatabaseError {
            kind: $kind,
            backtrace: std::backtrace::Backtrace::capture(),
        });
    };
}

fn do_query() -> Result<(), DatabaseError> {
    if !is_valid() { bail!(ErrorKind::InvalidQuery); }
    Ok(())
}
```

**Rationale**: `Backtrace::capture()` reads an env var; if backtraces are disabled it returns immediately. Capturing at construction means the stack is still the original stack — not a flattened chain of `?` returns. On stable Rust, `std::backtrace::Backtrace` is the canonical API.

**See also**: EH-15, EH-17, M-ERRORS-CANONICAL-STRUCTS

---

## EH-17: `Display` Renders the Summary, `Debug` Renders Everything

**Strength**: MUST

**Summary**: `Display` writes one line of prose — the cause chain is exposed via `source()`. `Debug` may additionally render the backtrace.

```rust
use std::fmt;

impl fmt::Display for ConfigError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.kind {
            ErrorKind::NotFound(_) => f.write_str("configuration file not found"),
            ErrorKind::Parse(_)    => f.write_str("failed to parse configuration"),
            ErrorKind::InvalidFormat { field, reason } =>
                write!(f, "invalid field '{field}': {reason}"),
        }
    }
}

impl fmt::Debug for ConfigError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{self}\n{}", self.backtrace)
    }
}

// Walking the chain — the canonical consumer pattern
fn log_chain(err: &dyn std::error::Error) {
    eprintln!("error: {err}");
    let mut cur = err.source();
    while let Some(e) = cur {
        eprintln!("  caused by: {e}");
        cur = e.source();
    }
}
```

**Rationale**: `Display` is the one-line summary that ends up in user-facing logs. The full chain is reconstructable from `Error::source()`. Duplicating the chain into `Display` (e.g., `write!(f, "{}: {}", self, source)`) double-prints when a consumer walks the chain themselves.

**See also**: EH-10, guide 05 TD-13, M-PUBLIC-DISPLAY

---

## EH-18: Provide Fallible and Panicking Variants

**Strength**: CONSIDER

**Summary**: When a panicking operation is convenient but a `Result` version is sometimes needed, provide both — name the fallible one with `try_`.

```rust
impl<T> Stack<T> {
    /// # Panics
    /// Panics if the stack is empty.
    pub fn pop(&mut self) -> T {
        self.try_pop().expect("pop on empty stack")
    }

    /// Non-panicking counterpart.
    pub fn try_pop(&mut self) -> Option<T> { self.inner.pop() }
}

// Std library precedent
// let v = vec![1, 2, 3];
// v[99]             // panics
// v.get(99)         // Option<&T>
// str::from_utf8    // Result
// str::from_utf8_unchecked  // unsafe, no check — the _unchecked convention (C-VALIDATE)
```

**Rationale**: Panicking variants are ergonomic for tests, REPLs, and provable-success call sites; fallible variants are required in production paths. Give consumers both; the `try_` prefix is the standard Rust convention.

**See also**: EH-02, C-VALIDATE

---

## EH-19: Fallible Constructors

**Strength**: SHOULD

**Summary**: When construction validates input, return `Result` from `new`. Reserve `try_new` for when an infallible `new` exists alongside.

```rust
// Option A: construction is usually fallible — new returns Result
impl Config {
    pub fn new(path: &Path) -> Result<Self, ConfigError> {
        let s = std::fs::read_to_string(path)?;
        toml::from_str(&s).map_err(ConfigError::parse)
    }
}

// Option B: infallible new + checked try_new (std-style)
pub struct PositiveInt(i32);

impl PositiveInt {
    /// # Panics
    /// Panics if `value <= 0`.
    pub fn new(value: i32) -> Self {
        Self::try_new(value).expect("value must be positive")
    }
    pub fn try_new(value: i32) -> Option<Self> {
        (value > 0).then_some(Self(value))
    }
}

// Option C: FromStr for string parsing
impl std::str::FromStr for Config {
    type Err = ConfigError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        toml::from_str(s).map_err(ConfigError::parse)
    }
}
```

**Rationale**: Library constructors that touch I/O or validate input almost always need `Result`. Panicking constructors belong only where the invariant is statically obvious (literals, tests) or where the std convention expects them. See guide 05 TD-03 for validated-newtype constructors.

---

## EH-20: Return the Consumed Argument on Error

**Strength**: CONSIDER

**Summary**: If a fallible function takes an owned argument, return that argument inside the error on failure — so the caller can retry without cloning.

```rust
// ❌ Caller must clone before every attempt
pub fn send(value: String) -> Result<(), SendError> { /* ... */ Err(SendError) }
pub struct SendError;

let mut v = long_string.clone();             // wasted clone on the happy path
while send(v.clone()).is_err() { /* ... */ }

// ✅ Hand the value back on failure — no pre-emptive cloning
pub fn send(value: String) -> Result<(), SendError> {
    if nondeterministic_fail() { Err(SendError(value)) } else { Ok(()) }
}
pub struct SendError(pub String);

let mut value = long_string;
let ok = 'retry: {
    for _ in 0..3 {
        value = match send(value) {
            Ok(()) => break 'retry true,
            Err(SendError(v)) => v,          // recover the move
        };
    }
    false
};
```

**Rationale**: Standard-library precedent is `String::from_utf8` returning `FromUtf8Error` with `.into_bytes()` giving the original `Vec<u8>` back. Moves are cheap; forcing callers to clone pre-emptively is expensive and ugly. Apply this whenever a function's argument is large, owned, and the operation can be retried.

**See also**: `String::from_utf8`, `mpsc::SendError`

---

## EH-21: Provide Contextual Helper Methods

**Strength**: SHOULD

**Summary**: Expose context via methods (`path()`, `line()`, `is_timeout()`) rather than forcing callers into the internal variant.

```rust
impl ConfigError {
    pub fn is_not_found(&self) -> bool { matches!(self.kind, ErrorKind::NotFound { .. }) }
    pub fn is_parse_error(&self) -> bool { matches!(self.kind, ErrorKind::Parse { .. }) }

    pub fn path(&self) -> Option<&Path> {
        match &self.kind {
            ErrorKind::NotFound { path } | ErrorKind::Parse { path, .. } => Some(path),
            _ => None,
        }
    }

    pub fn line(&self) -> Option<usize> {
        if let ErrorKind::Parse { line, .. } = &self.kind { Some(*line) } else { None }
    }
}

// Stable consumer pattern
match load_config() {
    Err(e) if e.is_not_found() => eprintln!("missing: {:?}", e.path()),
    Err(e) => eprintln!("failed at line {:?}: {e}", e.line()),
    Ok(cfg) => run(cfg),
}
```

**Rationale**: Helpers give callers a stable query surface without exposing `ErrorKind` (EH-11). Adding variants later only requires adding methods, never breaks existing consumers.

---

## EH-22: Redact Sensitive Data in Error `Display` and `Debug`

**Strength**: MUST

**Summary**: Errors leak into logs. Any error type holding tokens, passwords, API keys, or PII must implement `Display` and `Debug` manually to redact — and test the redaction.

```rust
pub struct AuthError {
    kind: ErrorKind,
    backtrace: std::backtrace::Backtrace,
}

enum ErrorKind {
    InvalidToken { token: String },
    InvalidPassword { username: String, password: String },
}

impl std::fmt::Display for AuthError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match &self.kind {
            ErrorKind::InvalidToken { .. } =>
                f.write_str("invalid authentication token"),
            ErrorKind::InvalidPassword { username, .. } =>
                write!(f, "invalid password for user '{username}'"),
        }
    }
}

impl std::fmt::Debug for AuthError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // Debug also redacts — no #[derive(Debug)]!
        write!(f, "{self}\n{}", self.backtrace)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn secrets_are_never_rendered() {
        let e = AuthError::invalid_password("alice".into(), "hunter2".into());
        let d = format!("{e}");
        let b = format!("{e:?}");
        assert!(!d.contains("hunter2"));
        assert!(!b.contains("hunter2"));
    }
}
```

**Rationale**: `#[derive(Debug)]` is the usual culprit — it prints every field. Errors flow into logs, crash reports, issue trackers. Manual `Debug` + a redaction test is the only durable defense. See guide 05 TD-12 for the same pattern on non-error types.

**See also**: guide 05 TD-12, M-PUBLIC-DEBUG

---

## EH-23: Separate Error Types per Context

**Strength**: SHOULD

**Summary**: Don't lump unrelated failures into one global error enum. Create a `ConfigError`, a `DatabaseError`, a `DownloadError` — share variants only when the contexts genuinely overlap.

```rust
// ❌ one error to rule them all
pub enum AppError {
    ConfigNotFound, ConfigParseError,
    DbConnection, DbTimeout, DbNotFound,
    HttpTimeout, HttpInvalidUrl,
    VmOutOfMemory, VmStartFailed,
    // ... grows unboundedly
}

// ✅ context-specific
pub struct ConfigError   { kind: ConfigKind,   backtrace: Backtrace }
pub struct DatabaseError { kind: DatabaseKind, backtrace: Backtrace }
pub struct DownloadError { kind: DownloadKind, backtrace: Backtrace }

pub fn load_config() -> Result<Config, ConfigError> { todo!() }
pub fn start_vm()    -> Result<Vm,     VmError>     { todo!() }
pub fn download()    -> Result<(),     DownloadError> { todo!() }

// The top-level binary aggregates, if it wants to:
#[derive(thiserror::Error, Debug)]
pub enum AppError {
    #[error(transparent)] Config(#[from] ConfigError),
    #[error(transparent)] Db(#[from] DatabaseError),
    #[error(transparent)] Download(#[from] DownloadError),
}
```

**Rationale**: A global error enum becomes a dumping ground — consumers get forced into variants they can't handle. Context-specific errors keep the failure surface small and matchable; the binary's top-level error composes them.

---

## EH-24: `ok_or` / `ok_or_else` to Convert `Option` to `Result`

**Strength**: SHOULD

**Summary**: Use `ok_or` when the error is a simple value; `ok_or_else` when constructing the error is non-trivial (allocation, capture, time).

```rust
// Simple error value — ok_or
fn find(id: UserId, m: &HashMap<UserId, User>) -> Result<User, NotFound> {
    m.get(&id).cloned().ok_or(NotFound)
}

// Allocating message — ok_or_else (closure only runs on None)
fn config_value(key: &str) -> Result<String, ConfigError> {
    std::env::var(key).ok().ok_or_else(|| ConfigError::missing(key.to_owned()))
}

// ❌ DON'T use ok_or with allocation — the string is built every call
fn bad(key: &str) -> Result<String, ConfigError> {
    std::env::var(key).ok().ok_or(ConfigError::missing(format!("missing {key}")))
}
```

**Rationale**: `ok_or` takes its argument eagerly — you pay the cost even on the `Some` branch. `ok_or_else` is lazy. Same rule applies to `unwrap_or` vs `unwrap_or_else`.

---

## EH-25: `#[must_use]` on Fallible Return Types

**Strength**: SHOULD

**Summary**: `Result` is already `#[must_use]`. For custom fallible return types (or for functions where ignoring the `Result` is a bug you want to flag), add `#[must_use]` with a reason.

```rust
// Result already carries must_use. Custom types need it explicitly:
#[must_use = "a TransactionReceipt must be committed or rolled back"]
pub struct TransactionReceipt { /* ... */ }

// Sometimes a function's Result is more important than the default warning:
impl Config {
    #[must_use = "ignoring save() may silently drop config changes"]
    pub fn save(&self) -> Result<(), SaveError> { todo!() }
}

// Usage: the following emits an unused_must_use warning
// config.save();
```

**Rationale**: Silent `Result` drops are one of the top sources of production bugs. The default lint catches many; a tailored message flags the rest more loudly.

---

## EH-26: Return `Result` from `main`

**Strength**: SHOULD

**Summary**: Let `main` return `Result` (or `anyhow::Result`) so `?` works and the runtime prints the error for you.

```rust
// ❌ manual error handling
fn main() {
    if let Err(e) = run() {
        eprintln!("error: {e}");
        std::process::exit(1);
    }
}

// ✅ Result-returning main
fn main() -> Result<(), Box<dyn std::error::Error>> {
    run()?;
    Ok(())
}

// ✅ anyhow for full context chain rendering
fn main() -> anyhow::Result<()> {
    let cfg = load_config().context("failed to load configuration")?;
    run(cfg).context("server crashed")?;
    Ok(())
}

// ✅ ExitCode when you need precise control
use std::process::ExitCode;
fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(e) => { eprintln!("error: {e:#}"); ExitCode::FAILURE }   // {:#} = chain
    }
}
```

**Rationale**: A `Result`-returning `main` has two benefits: `?` works at the top level, and the runtime prints the error's `Debug` impl (including the backtrace if present) on failure. `anyhow::Result` elevates this with chain-aware rendering.

---

## EH-27: Unsafe Code Must Be Exception-Safe

**Strength**: MUST

**Summary**: Unsafe code must maintain memory safety across every possible panic point — this is *minimal exception safety*. User-provided closures, `Clone`, `Ord::cmp`, debug-mode arithmetic, and allocator failure can all unwind.

```rust
use std::ptr;

// ❌ EXCEPTION-UNSAFE: clone() may panic, length set too early,
//    drop() then reads uninitialized memory.
impl<T: Clone> MyVec<T> {
    unsafe fn push_all_bad(&mut self, src: &[T]) {
        self.reserve(src.len());
        let end = self.as_mut_ptr().add(self.len());
        self.set_len(self.len() + src.len());    // BUG: too early
        for (i, x) in src.iter().enumerate() {
            ptr::write(end.add(i), x.clone());   // clone may panic!
        }
    }
}

// ✅ Fix: update length per iteration — drop sees only initialized slots
impl<T: Clone> MyVec<T> {
    unsafe fn push_all(&mut self, src: &[T]) {
        self.reserve(src.len());
        let start_len = self.len();
        let end = self.as_mut_ptr().add(start_len);
        for (i, x) in src.iter().enumerate() {
            ptr::write(end.add(i), x.clone());   // panic → length still tracks init'd
            self.set_len(start_len + i + 1);
        }
    }
}
```

**Rationale**: The Nomicon defines minimal exception safety: "never violate memory safety on panic." Unsafe code that temporarily breaks invariants must restore them before any potentially-panicking call — either by ordering (finish all panics before touching invariants) or by a guard struct whose `Drop` restores invariants (EH-28). Maximal exception safety — the program still behaves correctly — is a stronger target for safe code.

**See also**: EH-28, EH-29, guide 09 on unsafe, Nomicon §7

---

## EH-28: The Guard Pattern Is Rust's `finally`

**Strength**: CONSIDER

**Summary**: When an operation leaves a data structure temporarily invalid, store the in-flight state in a guard struct whose `Drop` restores the invariant — whether the code completes or panics.

```rust
use std::ptr;

// BinaryHeap::sift_up holds a logical "hole" while comparing. If Ord::cmp
// panics mid-operation, the hole must be refilled or the heap is corrupt.
struct Hole<'a, T: 'a> {
    data: &'a mut [T],
    elt: Option<T>,        // the removed element
    pos: usize,            // the index of the hole
}

impl<'a, T> Drop for Hole<'a, T> {
    fn drop(&mut self) {
        // SAFETY: pos is in bounds; elt is always Some until Drop runs.
        unsafe {
            let p = self.pos;
            ptr::write(&mut self.data[p], self.elt.take().unwrap());
        }
    }
}

// If the comparison closure panics while Hole is alive, Drop still runs
// and the element is written back — the heap stays valid.
```

**Rationale**: Rust has no `try { } finally { }`. The guard pattern is the idiomatic substitute — `Drop` always runs during unwinding. Use it any time you remove/move a value into a temporary that needs to be restored on panic.

**See also**: EH-27, Nomicon §7

---

## EH-29: Use `catch_unwind` Only at Trust Boundaries

**Strength**: CONSIDER

**Summary**: `std::panic::catch_unwind` is for thread-top-level isolation and for catching panics at FFI boundaries — not for routine error handling.

```rust
use std::panic::{catch_unwind, AssertUnwindSafe};

// ✅ FFI boundary — a panic across the C ABI is undefined behavior
#[no_mangle]
pub extern "C" fn my_library_call(input: *const u8, len: usize) -> i32 {
    let result = catch_unwind(AssertUnwindSafe(|| {
        // ... Rust logic that could panic ...
        process(input, len)
    }));
    match result {
        Ok(Ok(()))  => 0,
        Ok(Err(_))  => 1,                // normal error
        Err(_panic) => -1,               // panic, absorbed at boundary
    }
}

// ✅ Worker-thread isolation — one task's panic shouldn't kill the pool
let result = catch_unwind(|| run_task());

// ❌ BAD: using catch_unwind as try/catch for recoverable errors
fn bad_parse(s: &str) -> Option<i32> {
    catch_unwind(|| s.parse().unwrap()).ok().flatten()  // use Result instead
}
```

**Rationale**: Two facts constrain `catch_unwind`: (1) with `panic = "abort"` it does nothing — the process dies — so code must never *rely* on it for correctness; (2) unwinding is expensive — the runtime optimizes for the no-panic case. Reserve it for "this panic must not escape" boundaries: FFI exports, thread roots, plugin hosts.

**See also**: EH-27, EH-30, EH-31, Nomicon §7

---

## EH-30: Know Your `panic` Strategy: `abort` vs `unwind`

**Strength**: SHOULD

**Summary**: `panic = "unwind"` (default for most targets) runs destructors and is catchable; `panic = "abort"` terminates immediately. Your crate's behavior — and correctness — must not depend on the caller's choice.

```toml
# Cargo.toml — application-level choice
[profile.release]
panic = "abort"           # smaller binaries, no unwinding machinery

[profile.dev]
panic = "unwind"          # default; tests use unwind even with abort in release
```

```rust
// A library cannot assume unwinding runs — code must be correct with either.
// This is WHY:
// - Drop may not run on panic (if abort is active, nothing runs)
// - catch_unwind is a no-op with abort
// - Poisoning (EH-31) is based on drop-during-unwind, so it silently
//   doesn't engage under abort
```

**Rationale**: Libraries are configured by their consumer. `panic = "abort"` makes `catch_unwind` a no-op and prevents `Drop` from running — so correctness-critical cleanup must never rely on panic unwinding. Treat panic as "stop the program" (M-PANIC-IS-STOP) and you are correct under both strategies.

**See also**: EH-29, EH-31

---

## EH-31: Poison State After Panic in Shared Data

**Strength**: CONSIDER

**Summary**: For types that survive panics (typically behind a `Mutex` / `RwLock` / long-lived reference), mark the state *poisoned* so future operations refuse (or explicitly acknowledge) a potentially inconsistent state.

```rust
use std::sync::Mutex;

// std's Mutex is the canonical poisoning example:
let m = Mutex::new(0i32);

// std::thread::spawn(|| {
//     let _g = m.lock().unwrap();
//     panic!("boom");
// }).join().ok();

// Now m.lock() returns Err(PoisonError) — the data may be mid-mutation.
match m.lock() {
    Ok(g)  => println!("clean: {g}"),
    Err(p) => {
        // Explicit: "I accept the risk" — get the data anyway
        let g = p.into_inner();
        println!("poisoned but recovered: {g}");
    }
}

// Roll your own: an in-flight flag that a guard struct sets/clears
pub struct Poisoned<T> { value: T, poisoned: bool }

impl<T> Poisoned<T> {
    pub fn update(&mut self, f: impl FnOnce(&mut T)) -> Result<(), Poison> {
        if self.poisoned { return Err(Poison); }
        struct Guard<'a, T> { p: &'a mut Poisoned<T> }
        impl<T> Drop for Guard<'_, T> {
            fn drop(&mut self) { self.p.poisoned = std::thread::panicking(); }
        }
        let g = Guard { p: self };
        f(&mut g.p.value);
        std::mem::forget(g);                     // no panic → don't poison
        Ok(())
    }
}
```

**Rationale**: Poisoning is not about memory safety (that is guaranteed by minimal exception safety, EH-27) — it is about *logic safety*. After a panic, a data structure may be half-updated; poisoning forces a conscious decision before re-using it.

**See also**: EH-27, EH-28, Nomicon §7 "Poisoning"

---

## EH-32: Marshal Errors Across FFI Boundaries

**Strength**: SHOULD

**Summary**: Rust errors cannot cross the C ABI as `Result`. Convert to one of: (a) an integer error code, (b) an integer code plus a getter for a description string, or (c) a `#[repr(C)]` mirror struct.

```rust
use std::os::raw::{c_char, c_int};

// === Strategy A: flat enum → integer code
#[repr(i32)]
pub enum DbError { Ok = 0, ReadOnly = 1, Io = 2, Corrupted = 3 }

impl From<DbError> for c_int {
    fn from(e: DbError) -> c_int { e as c_int }
}

// === Strategy B: structured enum → code + accessor function
pub enum ParseError { BadChar { line: u32, ch: char }, Eof }

#[no_mangle]
pub extern "C" fn parse_error_code(e: &ParseError) -> c_int {
    match e {
        ParseError::BadChar { .. } => 1,
        ParseError::Eof            => 2,
    }
}

// Returns an owned, null-terminated C string. Caller must call `parse_error_free`.
#[no_mangle]
pub extern "C" fn parse_error_message(e: &ParseError) -> *mut c_char {
    let msg = match e {
        ParseError::BadChar { line, ch } => format!("bad '{ch}' at line {line}\0"),
        ParseError::Eof                  => "unexpected end of input\0".to_owned(),
    };
    std::ffi::CString::new(msg.trim_end_matches('\0')).unwrap().into_raw()
}

#[no_mangle]
pub unsafe extern "C" fn parse_error_free(p: *mut c_char) {
    if !p.is_null() { drop(std::ffi::CString::from_raw(p)); }
}

// === Strategy C: #[repr(C)] mirror struct for structural errors
struct Internal { expected: char, line: u32, ch: u16 }

#[repr(C)]
pub struct c_parse_error { pub expected: c_char, pub line: u32, pub ch: u16 }

impl From<Internal> for c_parse_error {
    fn from(e: Internal) -> Self {
        c_parse_error { expected: e.expected as c_char, line: e.line, ch: e.ch }
    }
}

// === Every #[no_mangle] export must catch panics (EH-29)
```

**Rationale**: C callers have no concept of `Result`, `Error`, or unwinding. Flatten errors to the model C understands, document ownership for any allocated strings (the caller frees via a paired function), and always wrap the Rust body in `catch_unwind` (EH-29) — unwinding across the C ABI is UB.

**See also**: EH-29, guide 09 on unsafe/FFI

---

## EH-33: Consider a Private `bail!` Macro

**Strength**: CONSIDER

**Summary**: For crates with many error-construction sites, a private `bail!` macro makes "construct kind + capture backtrace + return" a one-liner.

```rust
// crate::error
macro_rules! bail {
    ($kind:expr) => {
        return Err($crate::error::MyError {
            kind: $kind,
            backtrace: std::backtrace::Backtrace::capture(),
        });
    };
}
pub(crate) use bail;

// Usage
fn handle(req: &Request) -> Result<Response, MyError> {
    if !req.is_valid() {
        bail!(ErrorKind::InvalidRequest);
    }
    let user = authenticate(req)?;
    if !user.has_permission() {
        bail!(ErrorKind::PermissionDenied { user: user.name.clone() });
    }
    Ok(Response::ok())
}
```

**Rationale**: Backtrace capture (EH-16) is easy to forget. A `bail!` macro makes the correct construction the path of least resistance. Keep it `pub(crate)` — it's an implementation aid, not API.

**See also**: EH-16


## Common Patterns

### The Full Error Template

A reusable skeleton for a library's canonical error type. Follow EH-15, EH-16, EH-17 together:

```rust
use std::backtrace::Backtrace;
use std::fmt;

// ===== 1. Public error struct — opaque to consumers =====
pub struct MyError {
    kind: ErrorKind,
    backtrace: Backtrace,
}

// ===== 2. Internal variants — pub(crate) so callers can't match them =====
#[derive(Debug)]
pub(crate) enum ErrorKind {
    Upstream(UpstreamError),
    Validation { field: String, reason: String },
    NotFound,
}

// ===== 3. Constructors — each captures a Backtrace =====
impl MyError {
    pub(crate) fn upstream(err: UpstreamError) -> Self {
        Self { kind: ErrorKind::Upstream(err), backtrace: Backtrace::capture() }
    }
    pub(crate) fn validation(field: String, reason: String) -> Self {
        Self {
            kind: ErrorKind::Validation { field, reason },
            backtrace: Backtrace::capture(),
        }
    }
    pub(crate) fn not_found() -> Self {
        Self { kind: ErrorKind::NotFound, backtrace: Backtrace::capture() }
    }

    // ===== 4. Public query methods — stable even as variants evolve =====
    pub fn is_not_found(&self)   -> bool { matches!(self.kind, ErrorKind::NotFound) }
    pub fn is_validation(&self)  -> bool { matches!(self.kind, ErrorKind::Validation { .. }) }
    pub fn field(&self) -> Option<&str> {
        if let ErrorKind::Validation { field, .. } = &self.kind { Some(field) } else { None }
    }
    pub fn backtrace(&self) -> &Backtrace { &self.backtrace }
}

// ===== 5. Display — one-line summary. source() carries the chain. =====
impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.kind {
            ErrorKind::Upstream(_)      => f.write_str("upstream call failed"),
            ErrorKind::Validation { field, reason } =>
                write!(f, "validation failed for '{field}': {reason}"),
            ErrorKind::NotFound         => f.write_str("not found"),
        }
    }
}

// ===== 6. Debug includes the backtrace. NEVER #[derive(Debug)] — would leak fields. =====
impl fmt::Debug for MyError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{self}\n{}", self.backtrace)
    }
}

// ===== 7. Error::source exposes the cause chain =====
impl std::error::Error for MyError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match &self.kind {
            ErrorKind::Upstream(e) => Some(e),
            _                       => None,
        }
    }
}

// ===== 8. From impls — enable ? propagation =====
impl From<UpstreamError> for MyError {
    fn from(err: UpstreamError) -> Self { Self::upstream(err) }
}

// ===== 9. Optional: private bail! macro for terse construction =====
macro_rules! bail {
    ($kind:expr) => {
        return Err(MyError {
            kind: $kind,
            backtrace: Backtrace::capture(),
        });
    };
}
pub(crate) use bail;

// ===== 10. MSRV-safe note =====
// `std::backtrace::Backtrace` is stable since Rust 1.65. If your MSRV
// predates it, gate the field behind a `cfg` or omit it.

#[derive(Debug)]
pub struct UpstreamError;
impl fmt::Display for UpstreamError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { f.write_str("upstream") }
}
impl std::error::Error for UpstreamError {}
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| EH-01 Result for recoverable, panic for bugs | MUST | Don't invent Err variants for invariant violations |
| EH-02 Three valid reasons to panic | SHOULD | Bug, impossible, user-requested |
| EH-03 Correct-by-construction over panics | SHOULD | Encode invariants in types |
| EH-04 Libraries define their own error types | MUST | Never `Box<dyn Error>` or `anyhow` in public APIs |
| EH-05 Applications may use anyhow/eyre | CONSIDER | Binaries only — never libraries |
| EH-07 Avoid unwrap/expect in libraries | SHOULD | Use `expect` with justification if you must |
| EH-08 Use `?` for propagation | MUST | Never manual match-and-return |
| EH-09 Error conversion via `From` | MUST | Drives `?`; `#[from]` in thiserror |
| EH-10 Error types implement `std::error::Error` | MUST | `+ Debug + Display + Send + Sync + 'static` |
| EH-11 Don't expose ErrorKind directly | MUST | Provide `is_*` helpers instead |
| EH-12 Add context when you add a layer | SHOULD | `#[source]` or `.with_context(\|\| ...)` |
| EH-13 `#[non_exhaustive]` on public error enums | SHOULD | Future-compatible variants |
| EH-14 Document Errors, Panics, Safety | MUST | Rustdoc sections are load-bearing |
| EH-15 Errors are canonical structs | SHOULD | `kind` + `backtrace` + helpers |
| EH-16 Capture a Backtrace when born | MUST | Constructors and From impls |
| EH-17 Display summary, Debug full | MUST | `source()` carries the chain |
| EH-18 Fallible and panicking variants | CONSIDER | `try_` prefix for fallible |
| EH-20 Return consumed argument on error | CONSIDER | Caller retries without cloning |
| EH-22 Redact sensitive data in errors | MUST | Manual Display+Debug and test |
| EH-23 Separate error types per context | SHOULD | Avoid global error enums |
| EH-25 `#[must_use]` on fallible returns | SHOULD | Catch silently-dropped Results |
| EH-26 Return Result from main | SHOULD | `anyhow::Result` for chain rendering |
| EH-27 Unsafe code must be exception-safe | MUST | Minimal safety: no UB on unwind |
| EH-28 Guard pattern is Rust's finally | CONSIDER | Drop restores invariants on panic |
| EH-29 catch_unwind only at trust boundaries | CONSIDER | FFI exports, thread roots |
| EH-30 Know your panic strategy | SHOULD | Don't rely on unwinding for correctness |
| EH-31 Poison state after panic | CONSIDER | Force a conscious re-use decision |
| EH-32 Marshal errors across FFI | SHOULD | Integer codes or `#[repr(C)]` mirror |
| EH-33 Consider a private bail! macro | CONSIDER | Correct-by-default construction |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for panic-vs-Result decision and `?` usage in idiomatic code.
- **API Design**: See `02-api-design.md` for fallible constructors, `try_` naming, and returning references-vs-owned values alongside errors.
- **Type Design**: See `05-type-design.md` — especially TD-12 (Debug), TD-13 (Display), TD-07 (`#[non_exhaustive]`), TD-03 (validated newtypes), TD-20 (`NonZero*`).
- **Traits**: See `06-traits.md` for trait-object error usage (`Box<dyn Error + Send + Sync>`), coherence, and blanket impls.
- **Concurrency and Async**: See `07-concurrency-async.md` for `Send + Sync + 'static` error bounds in spawned tasks.
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for the unsafe exception-safety rules (EH-27, EH-28) in depth, and the FFI marshalling story (EH-32).
- **Documentation**: See `13-documentation.md` for the `# Errors`, `# Panics`, `# Safety` rustdoc conventions.


## External References

- [The Rust Book, Ch. 9 — Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [`std::error::Error`](https://doc.rust-lang.org/std/error/trait.Error.html) and [`std::backtrace::Backtrace`](https://doc.rust-lang.org/std/backtrace/struct.Backtrace.html)
- [`std::panic::catch_unwind`](https://doc.rust-lang.org/std/panic/fn.catch_unwind.html)
- [The Rustonomicon, Ch. 7 — Unwinding](https://doc.rust-lang.org/nomicon/unwinding.html) and [Exception Safety](https://doc.rust-lang.org/nomicon/exception-safety.html) and [Poisoning](https://doc.rust-lang.org/nomicon/poisoning.html)
- [Rust Design Patterns — Return consumed argument on error](https://rust-unofficial.github.io/patterns/idioms/on-stack-dyn-dispatch.html) and [Error Handling in FFI](https://rust-unofficial.github.io/patterns/patterns/ffi/errors.html)
- [Rust API Guidelines — Dependability](https://rust-lang.github.io/api-guidelines/dependability.html) (C-VALIDATE, C-DTOR-FAIL) and [Documentation](https://rust-lang.github.io/api-guidelines/documentation.html) (C-QUESTION-MARK, C-FAILURE)
- [`thiserror`](https://docs.rs/thiserror) and [`anyhow`](https://docs.rs/anyhow)
- Pragmatic Rust Guidelines: M-PANIC-IS-STOP, M-PANIC-ON-BUG, M-APP-ERROR, M-ERRORS-CANONICAL-STRUCTS, M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY
- Rust API Guidelines: C-GOOD-ERR, C-FAILURE, C-QUESTION-MARK, C-CONV-TRAITS, C-VALIDATE
