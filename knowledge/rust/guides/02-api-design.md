# API Design Guidelines

Patterns for designing public Rust APIs: naming, signatures, trait impls, construction, error surfaces, documentation, and future-proofing. Distilled from the Rust API Guidelines (the C-* guidelines) and the Pragmatic Rust library checklist (the M-* guidelines). Type-internal concerns (newtypes, `#[non_exhaustive]`, `Debug`/`Display` on domain types) live in `05-type-design.md`; this guide covers how types *connect* at an API boundary.


## API-01: Abstractions Don't Visibly Nest

**Strength**: SHOULD

**Summary**: Keep public type signatures flat. Service-like types should not nest type parameters, and user-visible types should expose at most one level of generic nesting.

```rust
// ❌ BAD: callers must name every layer
pub struct App {
    matrix: Matrix<f32, 4, 4, ArrayStorage<f32, 4, 4>>,
}

// ✅ GOOD: hide the internal parameterization
pub struct Matrix4x4 { inner: MatrixImpl<f32, 4, 4> }
pub struct App       { matrix: Matrix4x4 }

// ✅ OK: one level of nesting chosen by the caller
pub struct List<T> { items: Vec<T> }
let lists: List<Rc<RefCell<Item>>> = List { items: vec![] };
```

**Rationale**: Every type parameter in a public signature is cognitive load and a hazard for rustdoc readability. Internal generics are fine; exposing them forces every consumer to name types they don't care about.

**See also**: M-SIMPLE-ABSTRACTIONS

---

## API-02: Accept Borrowed, Return Owned

**Strength**: SHOULD

**Summary**: Default to `&T` / `&str` / `&[T]` on inputs and owned `T` / `String` / `Vec<T>` on outputs; return a borrow only when it is a view into an input.

```rust
// ✅ Borrow input, return owned
pub fn upper(s: &str) -> String { s.to_uppercase() }

// ✅ Return a borrow that refers back into an input
pub fn first_word(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}

// ❌ Force ownership the function doesn't need
pub fn upper_bad(s: String) -> String { s.to_uppercase() }
```

**Rationale**: Borrowing inputs is the maximally flexible signature — it works with owned values (via auto-deref) and with slices. Returning owned data is almost always what the caller wants; lifetimes on return types lock callers into a specific borrow graph.

**See also**: C-CALLER-CONTROL, ID-borrowed-types (core-idioms)

---

## API-03: Accept `impl AsRef<T>` Where Feasible

**Strength**: SHOULD

**Summary**: For path, string, and byte-slice parameters, accept `impl AsRef<Path>`, `impl AsRef<str>`, or `impl AsRef<[u8]>` so callers can pass either owned or borrowed data. Do not propagate `AsRef` into struct fields.

```rust
use std::path::{Path, PathBuf};

// ✅ Function signature: accept anything path-like
pub fn read_file(path: impl AsRef<Path>) -> std::io::Result<String> {
    std::fs::read_to_string(path.as_ref())
}

read_file("config.toml");
read_file(String::from("data.json"));
read_file(&PathBuf::from("./file"));

// ❌ Don't make struct fields generic over AsRef
pub struct Config<P: AsRef<Path>> { path: P }   // infects every consumer

// ✅ Store an owned, concrete type
pub struct Config { path: PathBuf }
```

**Rationale**: `impl AsRef<T>` monomorphizes — it is ergonomic without runtime cost. In field positions, the same bound forces every downstream type to carry the parameter, and the generality is wasted because the struct stores the value anyway.

**See also**: C-GENERIC, M-IMPL-ASREF

---

## API-04: Accept `impl Read` / `impl Write` (Sans-IO)

**Strength**: SHOULD

**Summary**: Functions that perform one-shot I/O should accept `impl Read` or `impl Write` (or their async cousins) rather than concrete types like `File`.

```rust
use std::io::Read;

// ✅ Works with files, sockets, stdin, in-memory buffers, cursors
pub fn parse_config<R: Read>(mut source: R) -> Result<Config, ConfigError> {
    let mut buf = String::new();
    source.read_to_string(&mut buf)?;
    Config::from_str(&buf)
}

parse_config(std::fs::File::open("c.toml")?);
parse_config(&b"key=value"[..]);
parse_config(std::io::Cursor::new(vec![b'x']));
```

**Rationale**: Sans-IO separates business logic from transport. Any parser works with any source; tests pass in-memory buffers; benchmarks use `Cursor`. This is the single biggest reusability lever in library design.

**See also**: C-RW-VALUE, M-IMPL-IO

---

## API-05: Accept `impl RangeBounds<T>` for Ranges

**Strength**: MUST

**Summary**: Functions taking a range should accept `impl RangeBounds<T>` — never two loose endpoints or a tuple.

```rust
use std::ops::RangeBounds;

// ✅ Accepts every range form
pub fn select<R: RangeBounds<usize>>(&self, range: R) -> &[Item] { /* ... */ todo!() }

self.select(1..3);
self.select(1..=3);
self.select(1..);
self.select(..3);
self.select(..);

// ❌ Hand-rolled endpoints
pub fn select_bad(&self, low: usize, high: usize) -> &[Item] { todo!() }
```

**Rationale**: Rust's range literals are expressive and canonical. `RangeBounds` covers all five forms with a single signature; anything else either loses expressiveness (`Range<usize>` rejects `..`) or reinvents the wheel.

**See also**: M-IMPL-RANGEBOUNDS

---

## API-06: Public Types Implement `Debug`, Never Empty

**Strength**: MUST

**Summary**: Every public type implements `Debug`, and the rendering always carries structural information — even for empty values.

```rust
// ✅ Default: derive
#[derive(Debug)]
pub struct Endpoint { url: String, timeout: std::time::Duration }

// ✅ Empty values must still render informatively
assert_eq!(format!("{:?}", Vec::<i32>::new()), "[]");
assert_eq!(format!("{:?}", ""), "\"\"");

// ✅ Sensitive fields: manual Debug with redaction, verified in tests
pub struct Credentials { username: String, password: String }

impl std::fmt::Debug for Credentials {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Credentials")
            .field("username", &self.username)
            .field("password", &"<redacted>")
            .finish()
    }
}
```

**Rationale**: `Debug` is assumed — by `assert_eq!`, logging frameworks, `dbg!`, and derive chains. An omitted `Debug` impl silently breaks downstream ergonomics because the orphan rule prevents users from adding it. An empty `Debug` output ("") loses the type-shape signal that makes the output useful. Full type-specific guidance (secret redaction, tests) lives in TD-12.

**See also**: C-DEBUG, C-DEBUG-NONEMPTY, M-PUBLIC-DEBUG, TD-12

---

## API-07: Don't Expose Smart Pointer Wrappers

**Strength**: MUST

**Summary**: `Arc<T>`, `Rc<T>`, `Box<T>`, `RefCell<T>`, `Mutex<T>` are implementation details. Don't put them in public parameter or return types — keep them inside the type.

```rust
// ❌ Infectious wrapper in the signature
pub fn start(config: Rc<RefCell<Config>>) -> Arc<Server> { todo!() }

// ✅ Clean boundary; wrapper is internal
pub struct Server { inner: Arc<ServerInner> }

impl Server {
    pub fn new(config: Config) -> Self {
        Self { inner: Arc::new(ServerInner::new(config)) }
    }
    pub fn start(&self) -> Result<(), ServerError> { self.inner.start() }
}

// Cheap handle-clone (see API-30)
impl Clone for Server {
    fn clone(&self) -> Self { Self { inner: Arc::clone(&self.inner) } }
}
```

**Rationale**: Two crates that disagree about which wrapper to use cannot compose. Callers should see `&T`, `&mut T`, or `T` and let the library decide how to share state internally.

**See also**: M-AVOID-WRAPPERS

---

## API-08: Use Named Types, Not `bool` or `Option`, for Parameters

**Strength**: SHOULD

**Summary**: Prefer enums and structs over `bool`, `u8`, or `Option` for public arguments whose meaning isn't obvious at the call site.

```rust
// ❌ Unclear at the call site
create_widget(true, false);
set_log_level("debug");                 // stringly-typed

// ✅ Enum: meaning is explicit and extensible
pub enum Size  { Small, Medium, Large }
pub enum Shape { Round, Square }
pub fn create_widget(size: Size, shape: Shape) -> Widget { /* ... */ todo!() }

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LogLevel { Debug, Info, Warn, Error }

impl std::str::FromStr for LogLevel {
    type Err = ParseLogLevelError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_ascii_lowercase().as_str() {
            "debug" => Ok(LogLevel::Debug),
            "info"  => Ok(LogLevel::Info),
            "warn" | "warning" => Ok(LogLevel::Warn),
            "error" => Ok(LogLevel::Error),
            _ => Err(ParseLogLevelError(s.into())),
        }
    }
}
```

**Rationale**: Named types self-document, resist parameter-swap bugs, and are extensible (add `ExtraLarge` without touching call sites). Strings pay validation cost at runtime; enums pay it at the boundary once. Full discussion lives in TD-01.

**See also**: C-CUSTOM-TYPE, TD-01

---

## API-09: Binary Types Implement `Binary`/`Octal`/`Hex`

**Strength**: SHOULD

**Summary**: Types representing bit patterns (flags, masks, hardware registers) should implement `Binary`, `Octal`, `LowerHex`, and `UpperHex`. Do not implement them for semantic quantities (nanoseconds, dollars).

```rust
use std::fmt;

#[derive(Clone, Copy, Debug)]
pub struct Permissions(u32);

impl fmt::Binary   for Permissions { fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { fmt::Binary::fmt(&self.0, f) } }
impl fmt::Octal    for Permissions { fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { fmt::Octal::fmt(&self.0, f) } }
impl fmt::LowerHex for Permissions { fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { fmt::LowerHex::fmt(&self.0, f) } }
impl fmt::UpperHex for Permissions { fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { fmt::UpperHex::fmt(&self.0, f) } }

println!("{:b} {:o} {:x} {:X}", p, p, p, p);

// ❌ Don't implement these for a quantity
pub struct Nanoseconds(u64); // no Binary/Hex — it's not a bit pattern
```

**Rationale**: Bitwise formatting is essential when debugging masks and flag combinations, misleading when the value is a numeric count.

**See also**: C-NUM-FMT

---

## API-10: Builder for 3+ Optional Parameters

**Strength**: SHOULD

**Summary**: When construction has three or more optional parameters (or conditional validation), provide a builder. Required parameters go into the builder's constructor, not into setter methods.

```rust
use std::time::Duration;

pub struct Server { /* ... */ }

pub struct ServerBuilder {
    host: String, port: u16,
    max_connections: usize, timeout: Duration, tls: Option<TlsConfig>,
}

impl ServerBuilder {
    pub fn new(host: impl Into<String>, port: u16) -> Self {
        Self {
            host: host.into(), port,
            max_connections: 100, timeout: Duration::from_secs(30), tls: None,
        }
    }
    pub fn max_connections(mut self, n: usize)       -> Self { self.max_connections = n; self }
    pub fn timeout(mut self, d: Duration)            -> Self { self.timeout = d; self }
    pub fn tls(mut self, cfg: TlsConfig)             -> Self { self.tls = Some(cfg); self }

    pub fn build(self) -> Result<Server, BuildError> {
        if self.timeout.is_zero() { return Err(BuildError::ZeroTimeout); }
        Ok(Server { /* ... */ })
    }
}

let server = ServerBuilder::new("localhost", 8080)
    .timeout(Duration::from_secs(60))
    .build()?;
```

**Rationale**: Builders prevent constructor combinatorial explosion (2^n for n optional params), centralize validation in `build`, and let new options be added without breaking call sites. Put required inputs in `new` so an empty `build()` cannot succeed with a half-constructed value. For deeper discussion and the consuming-vs-mutable-borrow tradeoff, see TD-10.

**See also**: C-BUILDER, M-INIT-BUILDER, TD-10

---

## API-11: Builder Required-Parameters Go in the Constructor

**Strength**: SHOULD

**Summary**: If the builder needs several required inputs, group them into a deps struct and accept `impl Into<Deps>` so callers can pass either the struct or a tuple.

```rust
#[derive(Debug, Clone)]
pub struct ConfigDeps { pub logger: Logger, pub config_path: PathBuf }

impl From<Logger> for ConfigDeps {
    fn from(logger: Logger) -> Self { Self { logger, config_path: "config.toml".into() } }
}
impl From<(Logger, PathBuf)> for ConfigDeps {
    fn from((logger, config_path): (Logger, PathBuf)) -> Self { Self { logger, config_path } }
}

impl Config {
    pub fn builder(deps: impl Into<ConfigDeps>) -> ConfigBuilder {
        ConfigBuilder::new(deps.into())
    }
}

let cfg = Config::builder(logger).build();
let cfg = Config::builder((logger.clone(), path)).build();
```

**Rationale**: Required inputs at the top mean `build()` can never be called on a half-initialized value. The `impl Into<Deps>` layer preserves ergonomic call sites while keeping a single source of truth for what must be provided.

**See also**: M-INIT-BUILDER, API-12

---

## API-12: Cascaded Initialization for Many Parameters

**Strength**: SHOULD

**Summary**: When four or more required parameters cluster semantically, group them into intermediate types rather than a long parameter list.

```rust
// ❌ Long, order-sensitive parameter list
impl Deposit {
    pub fn new(bank: &str, customer: &str, currency: &str, amount: u64) -> Self { todo!() }
}

// ✅ Cascaded: group related inputs into named types
pub struct Account  { bank: Bank, customer: Customer }
pub struct Currency { name: String, amount: u64 }

impl Account  { pub fn new(bank: Bank, customer: Customer) -> Self { Self { bank, customer } } }
impl Currency { pub fn new(name: String, amount: u64) -> Self { Self { name, amount } } }

impl Deposit {
    pub fn new(account: Account, amount: Currency) -> Self { Self { account, amount } }
}
```

**Rationale**: Parameter-swap bugs scale with list length. Named intermediate types both prevent them and become reusable primitives in their own right.

**See also**: M-INIT-CASCADED

---

## API-13: Collections Implement `FromIterator` and `Extend`

**Strength**: MUST

**Summary**: Any type that semantically contains a sequence should implement `FromIterator` (for `collect`) and `Extend` (for adding items).

```rust
pub struct MyVec<T> { items: Vec<T> }

impl<T> FromIterator<T> for MyVec<T> {
    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
        Self { items: iter.into_iter().collect() }
    }
}

impl<T> Extend<T> for MyVec<T> {
    fn extend<I: IntoIterator<Item = T>>(&mut self, iter: I) {
        self.items.extend(iter);
    }
}

let v: MyVec<i32> = (0..10).collect();
let (evens, odds): (MyVec<_>, MyVec<_>) = (0..10).partition(|n| n % 2 == 0);
```

**Rationale**: Without these, a collection can't participate in `collect`, `partition`, `unzip`, or `chain` — the idioms that make iterators fluent. Implementation is mechanical; absence is an ecosystem bug.

**See also**: C-COLLECT

---

## API-14: Constructors Are Static Inherent Methods

**Strength**: MUST

**Summary**: Name the primary constructor `new`. Use domain verbs for I/O resources (`open`, `connect`, `bind`). Use `with_*` for constructor variants and `from_*` for conversions that can't be a `From` impl.

```rust
impl<T> Vec<T> {
    pub fn new() -> Vec<T>                 { /* ... */ Vec { /* ... */ } }
    pub fn with_capacity(cap: usize) -> Vec<T> { /* ... */ todo!() }
}

impl File {
    pub fn open<P: AsRef<Path>>(p: P) -> std::io::Result<File> { /* ... */ todo!() }
    pub fn create<P: AsRef<Path>>(p: P) -> std::io::Result<File> { /* ... */ todo!() }
}

impl std::io::Error {
    // from_* because the source integer alone doesn't determine an encoding —
    // From<i32> would be ambiguous
    pub fn from_raw_os_error(code: i32) -> std::io::Error { /* ... */ todo!() }
}

impl Logger {
    pub fn new() -> Self { Self::default() }   // both new() and Default
}
```

**Rationale**: `new` is the canonical entry point — users look for it first. `from_` earns its keep where `From<T>` cannot apply: unsafe conversions (`Box::from_raw`), conversions with extra arguments (`u64::from_str_radix`), or source types whose bit representation is ambiguous (`u64::from_be`). Keep both `new()` and `Default` when both make sense and let them agree.

**See also**: C-CTOR

---

## API-15: Conversion Method Naming — `as_` / `to_` / `into_`

**Strength**: MUST

**Summary**: Name conversions by cost and ownership. `as_` is a free borrow-to-borrow; `to_` is an expensive conversion; `into_` consumes the input. The `mut` qualifier attaches where it appears in the return type: `as_mut_slice`, not `as_slice_mut`.

```rust
impl str {
    pub fn as_bytes(&self) -> &[u8]        { /* ... */ todo!() }   // free
    pub fn to_lowercase(&self) -> String   { /* ... */ todo!() }   // expensive
    pub fn to_owned(&self) -> String       { /* ... */ todo!() }   // expensive, borrowed → owned
}

impl String {
    pub fn into_bytes(self) -> Vec<u8>     { /* ... */ todo!() }   // consumes
}

impl<R> BufReader<R> {
    pub fn into_inner(self) -> R           { /* ... */ todo!() }   // unwrap a single-field wrapper
}

// ❌ Name lies about cost
impl str {
    pub fn to_bytes(&self) -> &[u8]        { todo!() }             // should be as_bytes
    pub fn as_lowercase(&self) -> String   { todo!() }             // should be to_lowercase
}
```

**Rationale**: The prefix is a contract. `as_` promises zero cost; writing `as_` on an expensive operation mis-trains every reader.

**See also**: C-CONV

---

## API-16: Conversions Live on the More Specific Type

**Strength**: SHOULD

**Summary**: Between two types where one carries additional invariants, put both directions of conversion on the specific type.

```rust
// str carries a UTF-8 invariant that [u8] does not → conversions live on str
impl str {
    pub fn as_bytes(&self) -> &[u8]                        { /* ... */ todo!() }
    pub fn from_utf8(b: &[u8]) -> Result<&str, std::str::Utf8Error> { /* ... */ todo!() }
}

// PathBuf is more specific than OsString → PathBuf owns the conversions
impl PathBuf {
    pub fn into_os_string(self) -> OsString                { /* ... */ todo!() }
}
```

**Rationale**: If every more-specific type pushed its conversion onto `[u8]`, the byte-slice API would drown in specialized helpers. Keeping the conversion on the invariant-carrying side concentrates related methods and leaves general types uncluttered.

**See also**: C-CONV-SPECIFIC

---

## API-17: Implement `From` / `TryFrom`, Never `Into` / `TryInto`

**Strength**: MUST

**Summary**: Implement `From` (or `TryFrom`) — the reverse direction comes free through blanket impls. Implementing `Into` directly skips the `From` impl that everyone else expects.

```rust
impl From<u16> for u32 {
    fn from(n: u16) -> u32 { n as u32 }
}
// `let x: u32 = 100u16.into();` — works automatically

impl TryFrom<u32> for u16 {
    type Error = std::num::TryFromIntError;
    fn try_from(n: u32) -> Result<u16, Self::Error> { u16::try_from(n) }
}

// ❌ Do not implement directly
impl Into<u32> for MyType { fn into(self) -> u32 { todo!() } }
impl TryInto<u16> for MyType { type Error = MyError; fn try_into(self) -> Result<u16, MyError> { todo!() } }
```

**Rationale**: `From` gives you `Into` for free; only one direction needs code. Implementing `Into` directly is redundant and denies the reverse-lookup that users rely on.

**See also**: C-CONV-TRAITS

---

## API-18: Serde Impls Live Behind a `serde` Feature

**Strength**: SHOULD

**Summary**: Data-structure types should support `serde::Serialize` and `Deserialize` gated on an optional feature named exactly `serde`.

```toml
[dependencies]
serde = { version = "1.0", optional = true, features = ["derive"] }

[features]
default = []
serde   = ["dep:serde"]
```

```rust
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct Config {
    pub host: String, pub port: u16, pub timeout_ms: u64,
}
```

**Rationale**: Serde is the de-facto serialization boundary in the Rust ecosystem. Opt-in via feature avoids forcing the compile cost on users who don't need it, and the feature name `serde` (not `serde_support`, not `with-serde`) matches the ecosystem convention and Cargo's implicit feature for optional dependencies.

**See also**: C-SERDE, C-FEATURE

---

## API-19: Destructors Never Fail, Never Block

**Strength**: MUST

**Summary**: `Drop` impls must not panic and should not block. Provide a separate `close`/`shutdown` method that returns `Result` when teardown can fail.

```rust
use std::net::{Shutdown, TcpStream};

pub struct Connection { socket: TcpStream, closed: bool }

impl Connection {
    // ✅ Explicit, fallible teardown
    pub fn close(mut self) -> std::io::Result<()> {
        if !self.closed {
            self.socket.shutdown(Shutdown::Both)?;
            self.closed = true;
        }
        Ok(())
    }
}

impl Drop for Connection {
    fn drop(&mut self) {
        if !self.closed {
            let _ = self.socket.shutdown(Shutdown::Both);  // best-effort, swallow
        }
    }
}

// ❌ Panicking drop — aborts on double-panic, undebuggable
impl Drop for BadConnection {
    fn drop(&mut self) { self.socket.shutdown(Shutdown::Both).unwrap(); }
}
```

**Rationale**: `Drop` runs during unwinding; a panic inside `Drop` while already panicking aborts the process. A blocking `Drop` turns a test timeout or a CTRL-C into a deadlock. Users who need to observe teardown errors call `close`; the `Drop` impl is purely defensive.

**See also**: C-DTOR-FAIL, C-DTOR-BLOCK

---

## API-20: Document Every Public Item With an Example

**Strength**: MUST

**Summary**: Every public item gets a rustdoc comment. Functions that return `Result` get an `# Errors` section; functions that can panic get a `# Panics` section; `unsafe` functions get a `# Safety` section. Examples use `?`, not `unwrap`.

```rust
/// A thread-safe counter with atomic increment and read.
///
/// # Examples
///
/// ```
/// # use my_crate::Counter;
/// let counter = Counter::new();
/// let prev = counter.increment();
/// assert_eq!(prev, 0);
/// assert_eq!(counter.get(), 1);
/// ```
#[derive(Debug)]
pub struct Counter { /* ... */ }

impl Counter {
    /// Parses a counter value from a string.
    ///
    /// # Errors
    ///
    /// Returns [`ParseCounterError`] if `s` is not a non-negative integer.
    ///
    /// # Examples
    ///
    /// ```
    /// # use std::error::Error;
    /// # use my_crate::Counter;
    /// # fn main() -> Result<(), Box<dyn Error>> {
    /// let c = Counter::from_str("42")?;
    /// assert_eq!(c.get(), 42);
    /// # Ok(())
    /// # }
    /// ```
    pub fn from_str(s: &str) -> Result<Self, ParseCounterError> { /* ... */ todo!() }
}
```

**Rationale**: Documentation is the API, not a companion to it. Examples are copy-pasted, so `unwrap` in an example teaches `unwrap` as the shape of error handling. The three canonical section names (`Errors`, `Panics`, `Safety`) are searched for by every Rust developer. Full doc-comment structure lives in guide `13-documentation.md`.

**See also**: C-EXAMPLE, C-QUESTION-MARK, C-FAILURE

---

## API-21: Hyperlink Between Doc Items

**Strength**: SHOULD

**Summary**: Use rustdoc's intra-doc link syntax (`` [`Type`] ``, `` [`Type::method`] ``) to cross-reference types, methods, and modules in prose. Link externally to RFCs, specs, and crates.

```rust
/// Builds a [`Request`] with sensible defaults.
///
/// See the [`Client::send`] documentation for how requests are dispatched,
/// and [RFC 7230] for HTTP/1.1 message syntax.
///
/// [`Request`]: crate::Request
/// [`Client::send`]: crate::Client::send
/// [RFC 7230]: https://datatracker.ietf.org/doc/html/rfc7230
pub struct RequestBuilder { /* ... */ }
```

**Rationale**: Navigable documentation is 10x more useful than flat prose. Intra-doc links are checked by `cargo doc`, so broken references fail CI instead of rotting silently.

**See also**: C-LINK

---

## API-22: Hide Implementation Noise with `#[doc(hidden)]`

**Strength**: SHOULD

**Summary**: Use `#[doc(hidden)]` on public-but-not-API items (derive plumbing, `From<PrivateError>` impls, re-exports required for macro hygiene). Use `pub(crate)` for items that need crate-internal access but no external visibility.

```rust
pub struct PublicError { /* ... */ }

// Private type kept out of the API surface
struct PrivateError;

// Required to make `?` work internally, but consumers should never see it
#[doc(hidden)]
impl From<PrivateError> for PublicError {
    fn from(_: PrivateError) -> PublicError { PublicError { /* ... */ } }
}

// A helper used by the `my_macro!` expansion — still callable as `__my_macro_internal`
// but not shown in rustdoc
#[doc(hidden)]
pub fn __my_macro_internal(s: &str) -> u64 { s.parse().unwrap_or(0) }
```

**Rationale**: Without `#[doc(hidden)]`, rustdoc lists every macro helper and cross-trait impl, burying the actual API. `pub(crate)` goes further by making the item invisible outside the crate; the two are complementary.

**See also**: C-HIDDEN

---

## API-23: Error Types Are Concrete, Meaningful, and Well-Behaved

**Strength**: MUST

**Summary**: Public fallible functions return a named error type that implements `std::error::Error + Display + Debug + Send + Sync`. Never return `Box<dyn Error>` or `String` from a library boundary. Never use `()` as an error type.

```rust
#[derive(Debug, thiserror::Error)]
pub enum ConnectError {
    #[error("invalid address: {0}")]
    InvalidAddress(#[from] std::net::AddrParseError),
    #[error("connection refused")]
    ConnectionRefused,
    #[error("timeout after {0:?}")]
    Timeout(std::time::Duration),
    #[error("TLS error: {0}")]
    Tls(#[from] TlsError),
}

pub fn connect(addr: &str) -> Result<Connection, ConnectError> { /* ... */ todo!() }

// Callers can match on specific variants
match connect("localhost:8080") {
    Ok(c) => use_connection(c),
    Err(ConnectError::Timeout(d)) => retry_longer(d),
    Err(ConnectError::ConnectionRefused) => fallback(),
    Err(other) => return Err(other.into()),
}
```

Error messages are lowercase, no trailing punctuation: `"unexpected end of file"`, not `"Unexpected end of file."`.

**Rationale**: `Box<dyn Error>` discards every typed handling opportunity; `String` discards `source()`; `()` fails to implement `Error` at all. A concrete enum gives callers control, composes with `#[from]`, and survives logging and downcasting. Deeper error-design discussion lives in `03-error-handling.md`.

**See also**: C-GOOD-ERR

---

## API-24: Essential Functionality Is an Inherent Method

**Strength**: MUST

**Summary**: Core operations on a type are inherent methods, not trait methods. If a trait is part of the public API, its implementation should forward to the inherent method.

```rust
// ❌ Trait-gated core operation — callers must import the trait
pub trait Download { fn download(&self, url: &str) -> Result<Vec<u8>, HttpError>; }
impl Download for HttpClient { fn download(&self, url: &str) -> Result<Vec<u8>, HttpError> { todo!() } }

// ✅ Inherent method is discoverable via `client.<tab>`
impl HttpClient {
    pub fn download(&self, url: &str) -> Result<Vec<u8>, HttpError> { /* ... */ todo!() }
}

// Optional trait forwards to the inherent method
impl Download for HttpClient {
    fn download(&self, url: &str) -> Result<Vec<u8>, HttpError> {
        HttpClient::download(self, url)
    }
}
```

**Rationale**: Inherent methods appear in IDE completion and rustdoc for the type; trait methods require the caller to find and import the trait. Duplicating the impl via forwarding costs two lines and buys discoverability.

**See also**: C-METHOD, M-ESSENTIAL-FN-INHERENT

---

## API-25: Prefer Methods to Free Functions When the Receiver Is Clear

**Strength**: SHOULD

**Summary**: If an operation has a natural primary argument, make it a method. Free functions are for operations with no clear receiver or that combine equally-specific types.

```rust
// ✅ Method — autoborrow, discoverable, concise
impl Config {
    pub fn load(&mut self, path: &Path) -> Result<(), ConfigError> { /* ... */ todo!() }
    pub fn save(&self, path: &Path)     -> Result<(), ConfigError> { /* ... */ todo!() }
    pub fn validate(&self)              -> Result<(), ValidationError> { /* ... */ todo!() }
}
config.load(&path)?;

// ❌ Free function — verbose, requires import, loses autoborrow
pub fn load_config(config: &mut Config, path: &Path) -> Result<(), ConfigError> { todo!() }
load_config(&mut config, &path)?;

// ✅ Free function: no clear receiver
pub fn merge(a: &Config, b: &Config) -> Config { todo!() }
```

Choose the receiver deliberately: `&self` for reads, `&mut self` for in-place mutation, `self` for consuming transforms, no `self` for associated functions.

**Rationale**: Methods autoborrow, appear in rustdoc on the type page, and don't need a `use`. Free functions remain correct for symmetric or receiver-less operations.

**See also**: C-METHOD, M-REGULAR-FN

---

## API-26: Caller Decides Where Data Lives

**Strength**: SHOULD

**Summary**: Take parameters by value when the function genuinely needs ownership, by reference when it doesn't. Don't accept `&T` only to clone internally — let the caller move if they have a surplus.

```rust
// ❌ Unnecessary clone
fn store(b: &Bar) { let b = b.clone(); internal.insert(b); }

// ✅ Take ownership — caller clones if they still need the value
fn store(b: Bar) { internal.insert(b); }

// ❌ Consume when borrowing would suffice
fn peek(b: Bar) -> bool { b.is_valid() }

// ✅ Borrow
fn peek(b: &Bar) -> bool { b.is_valid() }
```

Do not use `T: Copy` as a bound to signal "cheap to copy" — use it only when the function actually needs copy semantics.

**Rationale**: Every mandatory clone is a performance and ownership tax the caller can't escape. Matching the signature to real usage lets the caller decide whether to move, borrow, or clone.

**See also**: C-CALLER-CONTROL

---

## API-27: Expose Intermediate Results

**Strength**: SHOULD

**Summary**: When a function computes useful byproducts, return them. Don't force the caller to repeat the work.

```rust
// ✅ Returns the insertion point on miss, not just a bool
pub fn binary_search<T: Ord>(xs: &[T], needle: &T) -> Result<usize, usize> { /* ... */ todo!() }

// ✅ Error carries the invalid-byte offset AND returns ownership of the input
pub struct FromUtf8Error { bytes: Vec<u8>, error: std::str::Utf8Error }
impl FromUtf8Error {
    pub fn into_bytes(self) -> Vec<u8>            { self.bytes }
    pub fn utf8_error(&self) -> std::str::Utf8Error { self.error }
}

// ✅ Returns the previous value, not just whether insertion happened
impl<K, V> HashMap<K, V> {
    pub fn insert(&mut self, k: K, v: V) -> Option<V> { /* ... */ todo!() }
}
```

**Rationale**: Returning only `bool` or `()` discards data the caller might need. Binary search that returns `Option<usize>` forces a second search for the insertion point; `from_utf8` that only returns `Utf8Error` strands the caller's original buffer.

**See also**: C-INTERMEDIATE

---

## API-28: Return Compound Values — No Out-Parameters

**Strength**: MUST

**Summary**: Return tuples or structs instead of mutating out-parameters. The only legitimate exception is a caller-owned buffer that the function fills.

```rust
// ✅ Return multiple values
pub fn parse_header(data: &[u8]) -> Result<(Header, usize), ParseError> { /* ... */ todo!() }

// ✅ Struct for richer returns
pub struct ParseOutcome { pub value: f64, pub unit: String, pub warnings: Vec<String> }
pub fn parse(input: &str) -> Result<ParseOutcome, ParseError> { /* ... */ todo!() }

// ❌ Out-parameter style — not idiomatic in Rust
pub fn parse_header_bad(data: &[u8], header: &mut Header) -> Result<usize, ParseError> { todo!() }

// ✅ Legitimate exception: filling a caller-owned buffer
impl<R> std::io::Read for R { /* ... */
    fn read(&mut self, buf: &mut [u8]) -> std::io::Result<usize>;
}
```

**Rationale**: Tuple and struct returns compile to the same code as out-parameters — Rust's return-value optimization handles the copy. Out-params only make sense when the memory is semantically owned by the caller (a buffer to fill, not a value to produce).

**See also**: C-NO-OUT

---

## API-29: Generic Reader/Writer Parameters Take by Value

**Strength**: MUST

**Summary**: Functions generic over `R: Read` or `W: Write` take the reader/writer by value. Callers pass `&mut r` when they need to retain ownership — the `impl Read for &mut R` blanket impl makes that work.

```rust
use std::io::{Read, Write};

pub fn parse<R: Read>(mut r: R) -> Result<Data, Error> {
    let mut buf = String::new();
    r.read_to_string(&mut buf)?;
    parse_str(&buf)
}

// One-shot consume
parse(std::fs::File::open("data.txt")?)?;

// Retain ownership
let mut f = std::fs::File::open("data.txt")?;
parse(&mut f)?;
parse(&mut f)?;
```

Document the pattern in rustdoc: `"pass `&mut reader` if you need to reuse the reader."`

**Rationale**: Taking by value accepts both owned and `&mut`-borrowed forms through a single signature. Taking by reference forces every caller to borrow, even when they have a one-shot value.

**See also**: C-RW-VALUE

---

## API-30: Services Implement Shared-Ownership `Clone`

**Strength**: MUST

**Summary**: Heavyweight service types (connection pools, background runtimes, shared caches) implement `Clone` using an inner `Arc` — cloning produces a new handle to the same state, not a deep copy.

```rust
struct ServiceInner { config: Config, pool: ConnectionPool }

#[derive(Clone)]
pub struct Service { inner: std::sync::Arc<ServiceInner> }

impl Service {
    pub fn new(config: Config) -> Self {
        Self { inner: std::sync::Arc::new(ServiceInner { config, pool: ConnectionPool::new() }) }
    }
    pub fn process(&self, data: &Data) -> Result<Outcome, ServiceError> {
        self.inner.process(data)
    }
}

// Consumers clone freely — one service, many handles
let s = Service::new(cfg);
let handler_a = ComponentA::new(s.clone());
let handler_b = ComponentB::new(s.clone());
```

**Rationale**: A service is almost always shared; if `Clone` deep-copied the pool, nothing would work. The `Arc` is invisible to the consumer — they see `Clone` that acts like any other.

**See also**: M-SERVICES-CLONE

---

## API-31: Smart Pointers Don't Gain Inherent Methods — Use Associated Functions

**Strength**: MUST

**Summary**: Types that implement `Deref` (smart pointers, string types, collections) should not add inherent methods that take `self`, because they conflict with Deref-forwarded calls. Use associated functions that take the pointer by name.

```rust
// ✅ Associated function — the call site makes the receiver type unambiguous
impl<T: ?Sized> Box<T> {
    pub fn into_raw(b: Box<T>) -> *mut T { /* ... */ todo!() }
}
let b: Box<String> = Box::new("x".into());
let ptr = Box::into_raw(b);

// ❌ If `into_raw` were a method, which type owns it?
// b.into_raw()        // Box<String>::into_raw or String::into_raw (if that existed)?

// Same pattern for Rc/Arc
use std::rc::Rc;
let r = Rc::new(String::from("hello"));
let count = Rc::strong_count(&r);
let raw   = Rc::into_raw(r);

// Constructors are fine as inherent — there's nothing to collide with yet
impl<T> Box<T> { pub fn new(v: T) -> Self { Box::new(v) } }
```

Corollary: only implement `Deref` and `DerefMut` for genuine smart pointers (`Box`, `Rc`, `Arc`, `Cow`, `String` → `str`, `Vec` → `[T]`, `MutexGuard`). Using `Deref` for inheritance or subtyping between domain types — the "Deref polymorphism" anti-pattern — confuses method resolution and silently inserts dereferences users can't predict.

**Rationale**: Method-resolution order searches `Self`, then the `Deref::Target`. Inherent methods on `Box<T>` that take `self` make the call `b.into_raw()` ambiguous between `Box` and `T`. Associated functions sidestep the problem by naming the type at the call site.

**See also**: C-SMART-PTR, C-DEREF

---

## API-32: Operator Overloads Are Unsurprising

**Strength**: MUST

**Summary**: Only implement `Add`, `Mul`, `BitOr`, etc., when the operation genuinely resembles the operator's mathematical or logical meaning — with expected properties like associativity and commutativity.

```rust
use std::ops::Add;

// ✅ Vector addition — associative, commutative
#[derive(Clone, Copy)]
pub struct Vec3 { x: f64, y: f64, z: f64 }

impl Add for Vec3 {
    type Output = Vec3;
    fn add(self, o: Vec3) -> Vec3 {
        Vec3 { x: self.x + o.x, y: self.y + o.y, z: self.z + o.z }
    }
}

// ✅ BitOr on a bitflag set
let perms = Permissions::READ | Permissions::WRITE;

// ❌ Surprising
impl Add for HttpRequest { /* ... */ }   // what does adding requests mean?
impl Mul for Logger      { /* ... */ }   // ???
```

**Rationale**: Operators come with strong user expectations. Overloading them for unrelated concepts produces unreadable code and misleads consumers who rely on algebraic properties.

**See also**: C-OVERLOAD

---

## API-33: Getters Omit the `get_` Prefix

**Strength**: SHOULD

**Summary**: Name getters after the field: `name()`, not `get_name()`. The mutable variant gets a `_mut` suffix: `name_mut()`. The bare name `get` is reserved for types with a single obvious thing to retrieve (`Cell::get`).

```rust
pub struct Person { name: String, age: u32 }

impl Person {
    pub fn name(&self) -> &str                  { &self.name }
    pub fn name_mut(&mut self) -> &mut String   { &mut self.name }
    pub fn age(&self) -> u32                    { self.age }
}

// ✅ Bare `get` on single-purpose wrappers
std::cell::Cell::new(5).get();

// ✅ Unsafe opt-out variant for validated access
impl<T> Vec<T> {
    fn get(&self, i: usize) -> Option<&T>              { self.as_slice().get(i) }
    unsafe fn get_unchecked(&self, i: usize) -> &T     { self.as_slice().get_unchecked(i) }
}

// ❌ get_ prefix
impl Person { pub fn get_name(&self) -> &str { &self.name } }  // drop the prefix
```

**Rationale**: Method syntax already signals retrieval; `get_` is redundant noise inherited from Java/C#. Dropping it keeps signatures short and reads as natural English.

**See also**: C-GETTER

---

## API-34: Iterator Methods Are `iter`/`iter_mut`/`into_iter`

**Strength**: MUST

**Summary**: Collections provide the canonical trio: `iter(&self) -> Iter<'_, T>`, `iter_mut(&mut self) -> IterMut<'_, T>`, and `into_iter(self) -> IntoIter<T>`. The iterator type name matches the method name.

```rust
pub struct MyList<T> { /* ... */ }

pub struct Iter<'a, T>    { /* ... */ ph: std::marker::PhantomData<&'a T> }
pub struct IterMut<'a, T> { /* ... */ ph: std::marker::PhantomData<&'a mut T> }
pub struct IntoIter<T>    { /* ... */ items: Vec<T> }

impl<T> MyList<T> {
    pub fn iter(&self) -> Iter<'_, T>              { /* ... */ todo!() }
    pub fn iter_mut(&mut self) -> IterMut<'_, T>   { /* ... */ todo!() }
    pub fn into_iter(self) -> IntoIter<T>          { /* ... */ todo!() }
}

// Heterogeneous views get descriptive names
impl<K, V> std::collections::HashMap<K, V> {
    pub fn keys(&self)   -> std::collections::hash_map::Keys<'_, K, V>   { /* ... */ todo!() }
    pub fn values(&self) -> std::collections::hash_map::Values<'_, K, V> { /* ... */ todo!() }
}
```

**Rationale**: The pattern is universal in std — breaking it makes generic code that expects `iter()` stop working on your type, and surprises every user who expected to just call `.iter()`. Domain-specific iterators (`bytes`, `chars`, `keys`) are named for what they yield.

**See also**: C-ITER, C-ITER-TY

---

## API-35: Naming Follows RFC 430

**Strength**: MUST

**Summary**: `UpperCamelCase` for types, traits, and enum variants; `snake_case` for functions, methods, and modules; `SCREAMING_SNAKE_CASE` for consts and statics. Acronyms count as one word: `Uuid`, `Http`, `Xid`.

```rust
// ✅ Canonical casing
pub struct HttpClient;
pub enum ColorSpace { Srgb, DisplayP3 }
pub trait Serialize { fn serialize(&self) -> String; }
pub fn parse_config() -> Config { todo!() }
pub const MAX_CONNECTIONS: usize = 100;
pub static DEFAULT_TIMEOUT: std::time::Duration = std::time::Duration::from_secs(30);

mod http_client;
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str { if x.len() > y.len() { x } else { y } }
fn parse<T: std::str::FromStr>(s: &str) -> Result<T, T::Err> { s.parse() }

// ❌ Wrong casing
pub struct HTTPClient;      // acronym should be Http
pub fn ParseConfig() { }    // should be parse_config
```

Error types follow verb-object-error order: `ParseIntError`, `JoinPathsError` — not `IntParseError`.

**Rationale**: Consistency lets readers identify what kind of item a name refers to at a glance, and lets code from different crates compose visually. Word-order consistency inside a crate matters more than picking any specific order.

**See also**: C-CASE, C-WORD-ORDER, RFC 430

---

## API-36: Cargo Feature Names Are Bare

**Strength**: SHOULD

**Summary**: Feature names are the bare thing they enable — `serde`, `std`, `tokio` — not `use-serde`, `with-tokio`, or `no-std`. Features must be additive.

```toml
# ✅ Idiomatic
[features]
default = ["std"]
std     = []
serde   = ["dep:serde"]
tokio   = ["dep:tokio"]

# ❌ Placeholders and negatives
[features]
use-serde = ["dep:serde"]           # drop `use-`
with-tokio = ["dep:tokio"]          # drop `with-`
no-std = []                          # negatives break additivity
```

**Rationale**: Cargo creates an implicit feature with the dependency's bare name for optional dependencies; matching that convention is what downstream users search for. Negative feature names ("no-std") cannot be composed — enabling them in one dependency disables the code everywhere.

**See also**: C-FEATURE

---

## API-37: Newtypes for Type-Safe Distinctions

**Strength**: SHOULD

**Summary**: Wrap a primitive in a named struct whenever the value carries a unit, an ID role, or a validity invariant. The wrapper is free at runtime; full discussion lives in TD-03.

```rust
pub struct Miles(pub f64);
pub struct Kilometers(pub f64);

impl Miles {
    pub fn to_km(self) -> Kilometers { Kilometers(self.0 * 1.60934) }
}

fn too_far(d: Miles) -> bool { d.0 > 100.0 }
// too_far(Kilometers(200.0));       // compile error
too_far(Kilometers(200.0).to_miles());

pub struct EmailAddress(String);
impl EmailAddress {
    pub fn new(s: String) -> Result<Self, InvalidEmail> {
        if s.contains('@') { Ok(Self(s)) } else { Err(InvalidEmail) }
    }
    pub fn as_str(&self) -> &str { &self.0 }
}
```

**Rationale**: Unit confusion, argument-swap bugs, and un-validated inputs collapse into one pattern. In an API context, newtypes also hide representation — consumers depend on the wrapper, not the inner type.

**See also**: C-NEWTYPE, M-STRONG-TYPES, TD-03

---

## API-38: Types Are `Send` + `Sync` Where Possible

**Strength**: MUST

**Summary**: Public types should be `Send` and `Sync` unless the design genuinely forbids it. Futures and any type held across `.await` must be `Send` for work-stealing runtimes. Assert thread-safety with a compile-time check.

```rust
// ✅ Automatically Send + Sync
pub struct Request { url: String, headers: Vec<(String, String)> }

// Compile-time assertion
#[cfg(test)]
mod tests {
    fn assert_send<T: Send>() {}
    fn assert_sync<T: Sync>() {}
    #[test] fn request_is_send_sync() {
        assert_send::<super::Request>();
        assert_sync::<super::Request>();
    }
}

// ❌ Don't opt out gratuitously
pub struct Config {
    name: String,
    _not_sync: std::marker::PhantomData<*const ()>,   // blocks Sync for no reason
}
```

**Rationale**: `!Send` types are infectious across `.await` points — one `Rc` inside a future taints the whole thing and makes it incompatible with Tokio. Compile-time assertions catch accidental regressions from adding an `Rc` or raw-pointer field.

**See also**: C-SEND-SYNC, M-TYPES-SEND

---

## API-39: Validate Inputs — Prefer Static Types, Then Runtime Checks, Then `_unchecked` Opt-Outs

**Strength**: MUST

**Summary**: Rust APIs reject the robustness principle. Validate at the boundary, in this order of preference: (1) static enforcement via types; (2) dynamic check returning `Result`/`Option`; (3) `debug_assert!` for expensive checks; (4) `_unchecked` (often `unsafe`) variants for opt-out.

```rust
// (1) Static: the type rules out invalid inputs
pub struct Ascii(u8);
impl Ascii { pub fn new(b: u8) -> Option<Self> { (b < 128).then_some(Self(b)) } }
fn process(a: Ascii) { /* ... */ }

// (2) Dynamic with Result
pub fn connect(addr: &str, port: u16) -> Result<Connection, ConnectError> {
    if port == 0            { return Err(ConnectError::InvalidPort); }
    if addr.trim().is_empty() { return Err(ConnectError::InvalidAddress); }
    /* ... */ todo!()
}

// (3) debug_assert! for expensive invariant checks
pub fn merge(a: &Sorted<i32>, b: &Sorted<i32>) -> Vec<i32> {
    debug_assert!(a.is_sorted() && b.is_sorted());
    /* ... */ todo!()
}

// (4) _unchecked opt-out — usually unsafe
impl String {
    pub fn from_utf8(v: Vec<u8>) -> Result<Self, std::string::FromUtf8Error> { /* ... */ todo!() }
    pub unsafe fn from_utf8_unchecked(v: Vec<u8>) -> Self { /* ... */ todo!() }
}
```

Validate at the API boundary, not in a subroutine five calls deep — fail the 500-item batch on the first bad element before you start processing.

**Rationale**: Static enforcement has negligible runtime cost and catches bugs at compile time. Dynamic checks surface the failure cleanly via `Result`. `debug_assert!` lets you keep checks in tests without paying for them in release. `_unchecked` gives informed users an escape.

**See also**: C-VALIDATE

---

## API-40: Concrete Types > Generics > `dyn Trait`

**Strength**: SHOULD

**Summary**: For dependency injection, prefer the simplest escalation that works. Start with concrete types, graduate to generics with narrow trait bounds, fall back to `dyn Trait` only when generic nesting becomes unreadable.

```rust
// Level 1: concrete type — simplest and most readable
pub struct MyDatabase { /* ... */ }
impl MyDatabase {
    pub async fn store(&self, obj: Object) -> Result<(), DbError> { /* ... */ todo!() }
    pub async fn load(&self, id: Id)       -> Option<Object>      { /* ... */ todo!() }
}
pub async fn run(db: MyDatabase) { /* ... */ }

// Level 2: narrow traits + generics when a second impl becomes necessary
pub trait Store  { fn store(&self, o: Object) -> impl Future<Output = Result<(), DbError>>; }
pub trait Load   { fn load(&self, id: Id)     -> impl Future<Output = Option<Object>>;      }

pub async fn run_g<D: Store + Load>(db: D) { /* ... */ }

// Level 3: dyn Trait only when generics force unreadable nesting
pub async fn run_dyn(db: Arc<dyn StoreAndLoad + Send + Sync>) { /* ... */ }
```

**Rationale**: Concrete types compile the fastest, produce the clearest error messages, and read most directly. Generics buy flexibility at the cost of signature complexity. `dyn Trait` buys heterogeneity at the cost of object-safety constraints and dynamic dispatch. Moving up the ladder is easy; moving down is a breaking change.

**See also**: C-GENERIC, M-DI-HIERARCHY

---

## API-41: Use Generics to Minimize Parameter Assumptions

**Strength**: SHOULD

**Summary**: Replace concrete-type parameters with the narrowest trait bound the function actually needs: `impl IntoIterator<Item = T>` instead of `&[T]`, `impl AsRef<Path>` instead of `&Path`.

```rust
// ❌ Only accepts Vec<i64>
fn sum_bad(c: &Vec<i64>) -> i64 { c.iter().sum() }

// ✅ Works on Vec, slice, array, HashSet drain, ranges, ...
fn sum<I: IntoIterator<Item = i64>>(iter: I) -> i64 { iter.into_iter().sum() }

sum(vec![1, 2, 3]);
sum([1, 2, 3]);
sum(1..=10);

// ✅ Generic path parameter accepts &str, String, Path, PathBuf, OsString, ...
pub fn read_config<P: AsRef<std::path::Path>>(p: P) -> Result<Config, ConfigError> { todo!() }
```

Don't generalize past what the function actually needs — `fn len<C: std::ops::Index<usize>>` is spurious if the function only calls `.len()`.

**Rationale**: Narrow generic bounds accept every concrete type that satisfies them, with static dispatch and no runtime cost. Monomorphization costs binary size, so don't generalize where it buys nothing.

**See also**: C-GENERIC

---

## API-42: Design Traits for Object Safety When Useful

**Strength**: SHOULD

**Summary**: If a trait might be used as `Box<dyn Trait>` or `&dyn Trait`, make it object-safe. Generic or `Self`-returning methods go behind `where Self: Sized`.

```rust
pub trait Draw {
    fn draw(&self, canvas: &mut Canvas);
    fn bounds(&self) -> Rect;
}
let shapes: Vec<Box<dyn Draw>> = vec![Box::new(Circle::new(1.0)), Box::new(Square::new(2.0))];

// Mixed: object-safe core + static-dispatch conveniences
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;                   // object-safe

    fn collect<B: FromIterator<Self::Item>>(self) -> B
    where Self: Sized,                                          // excluded from dyn
    { /* ... */ todo!() }
}
```

Full trait-design discussion (coherence, blanket impls, associated types) lives in `06-traits.md`.

**Rationale**: Object-safe traits enable heterogeneous collections and dynamic dispatch — `dyn Draw` over shapes, `dyn Write` over sinks. Losing the ability is a one-way door; reclaiming it later is a breaking change.

**See also**: C-OBJECT

---

## API-43: Sealed Traits Control the Implementation Surface

**Strength**: CONSIDER

**Summary**: When a trait is intended for internal implementors only (wire formats, backends, primitive selectors), seal it with a private supertrait. Document the seal.

```rust
mod private { pub trait Sealed {} }

/// A database backend.
///
/// This trait is sealed; implementing it outside `my_crate` is not supported.
pub trait Backend: private::Sealed {
    fn execute(&self, query: &str) -> Result<(), DbError>;
    fn execute_batch(&self, queries: &[&str]) -> Result<(), DbError> {
        queries.iter().try_for_each(|q| self.execute(q))
    }
}

pub struct Postgres;
impl private::Sealed for Postgres {}
impl Backend for Postgres { fn execute(&self, _: &str) -> Result<(), DbError> { Ok(()) } }
```

**Rationale**: A sealed trait can gain required methods in a non-breaking release (only internal impls need updating). The tradeoff: downstream crates can't implement the trait, so seal only what is genuinely a closed set.

**See also**: C-SEALED

---

## API-44: Hide Return-Type Noise With Newtypes or `impl Trait`

**Strength**: SHOULD

**Summary**: Don't return `Enumerate<Skip<I>>` or other adapter chains from a public API — wrap in a newtype or use `-> impl Trait` so the concrete type is not part of the contract.

```rust
use std::iter::{Enumerate, Skip};

// ❌ Exposes the adapter stack — changing it is a breaking change
pub fn transform_leaky<I: Iterator>(i: I) -> Enumerate<Skip<I>> { i.skip(3).enumerate() }

// ✅ Newtype wraps the chain — can be Debug, Clone, combined with other trait bounds
pub struct Transform<I>(Enumerate<Skip<I>>);
impl<I: Iterator> Iterator for Transform<I> {
    type Item = (usize, I::Item);
    fn next(&mut self) -> Option<Self::Item> { self.0.next() }
}
pub fn transform<I: Iterator>(i: I) -> Transform<I> { Transform(i.skip(3).enumerate()) }

// ✅ impl Trait — even more opaque; good for closures and simple cases
pub fn items(&self) -> impl Iterator<Item = &Item> + '_ {
    self.data.iter().filter(|i| i.is_active())
}

pub fn make_adder(n: i32) -> impl Fn(i32) -> i32 { move |x| x + n }
```

`impl Trait` trades expressiveness for concision: it cannot name the type for consumers (so they can't put it in a `struct` field) and cannot express trait combinations that aren't in the signature (`impl Iterator<Item=T> + Debug + Clone` is possible, but unwieldy).

**Rationale**: A visible adapter stack freezes implementation choices at the API boundary. A newtype gives you room to change the underlying pipeline without breaking callers. `impl Trait` is even tighter when the type need not be named.

**See also**: C-NEWTYPE-HIDE

---

## API-45: Extension Traits for Foreign Types

**Strength**: CONSIDER

**Summary**: To add methods to a type defined in another crate (including std), declare a trait with the methods and implement it for the foreign type. Name it with an `Ext` suffix.

```rust
/// Extension methods for [`Option<String>`].
pub trait OptionStringExt {
    /// Returns `true` if this contains a non-empty string.
    fn is_non_empty(&self) -> bool;
    /// Returns the string, defaulting to empty.
    fn unwrap_or_empty(self) -> String;
}

impl OptionStringExt for Option<String> {
    fn is_non_empty(&self) -> bool       { self.as_ref().is_some_and(|s| !s.is_empty()) }
    fn unwrap_or_empty(self) -> String   { self.unwrap_or_default() }
}

// Downstream:
// use my_crate::OptionStringExt;
// name.is_non_empty();
```

**Rationale**: The orphan rule prevents inherent-method additions to foreign types; extension traits are the safe, scoped alternative. Users opt in via `use`, so there's no risk of accidental override.

---

## API-46: Don't Leak External Types Into Public APIs

**Strength**: SHOULD

**Summary**: Prefer `std` types at the API boundary. If you expose a type from a third-party crate in a public signature, that crate becomes a public dependency — pinning you to its semver and blocking your 1.0.

```rust
// ❌ Exposes url::Url in the public surface — url is now a public dep
pub fn request(url: url::Url) -> Response { /* ... */ todo!() }

// ✅ Accept a string and parse internally, or expose your own type
pub fn request(url: &str) -> Result<Response, UrlError> { /* ... */ todo!() }

// ✅ If the external type is genuinely the boundary (e.g., serde), feature-gate it
#[cfg(feature = "serde")]
pub fn from_value(v: serde_json::Value) -> Result<Self, DeserError> { todo!() }
```

Watch out for sneaky public dependencies: `impl From<other_crate::Error> for MyError` makes `other_crate` public even if the variant holding it is private.

**Rationale**: A stable (>= 1.0) crate must have only stable public dependencies. Leaked types also fragment the ecosystem — if two crates expose different major versions of the same dependency, their types are incompatible.

**See also**: C-STABLE, M-DONT-LEAK-TYPES

---

## API-47: Macros Mirror Rust Syntax

**Strength**: SHOULD

**Summary**: Macro input should look like the Rust code it produces: use `struct`, `enum`, `const`, and punctuation (semicolons for constants, commas for arguments) that match the output. Support attributes, visibility, and arbitrary scopes.

```rust
// ✅ Syntax mirrors the generated output
bitflags::bitflags! {
    #[derive(Default, Debug)]
    pub struct Flags: u8 {
        #[cfg(windows)] const CONTROL = 0b0001;
        #[cfg(unix)]    const TERMINAL = 0b0010;
        const COMMON = 0b0100;
    }
}

// Private variant
bitflags::bitflags! {
    struct PrivateFlags: u8 { const A = 0b0001; }
}

// ❌ Ad-hoc DSL that users have to memorize
// flag_struct! { name=Flags ty=u8 A=1 B=2 C=4 }
```

A well-behaved macro:
- Uses familiar keywords (`struct`, `const`) — **C-EVOCATIVE**
- Passes attributes through to generated items — **C-MACRO-ATTR**
- Works at module scope *and* inside functions (avoid `super::` in generated code) — **C-ANYWHERE**
- Accepts a visibility specifier (`$vis:vis`) — **C-MACRO-VIS**
- Accepts all `$t:ty` forms: primitives, paths, generics — **C-MACRO-TY**

**Rationale**: Users shouldn't have to learn a new micro-language for each macro. If the generated code is Rust, the invocation should feel like writing Rust.

**See also**: C-EVOCATIVE, C-MACRO-ATTR, C-ANYWHERE, C-MACRO-VIS, C-MACRO-TY

---

## API-48: Crate-Level Documentation and Metadata

**Strength**: SHOULD

**Summary**: `lib.rs` starts with a `//!` module doc: overview, one motivating example, pointers to the main entry types. `Cargo.toml` carries full metadata for discoverability on crates.io.

```rust
//! # my_crate
//!
//! `my_crate` parses and validates foo configurations.
//!
//! ## Quick start
//!
//! ```
//! use my_crate::Config;
//! # fn main() -> Result<(), Box<dyn std::error::Error>> {
//! let cfg = Config::from_str("host = 'example.com'\nport = 8080\n")?;
//! assert_eq!(cfg.host(), "example.com");
//! # Ok(())
//! # }
//! ```
//!
//! See [`Config`] for the full API.
```

```toml
[package]
name = "my_crate"
version = "0.3.0"
authors = ["Jane Doe <jane@example.com>"]
license = "MIT OR Apache-2.0"
description = "Parses and validates foo configurations."
repository = "https://github.com/jane/my_crate"
keywords = ["config", "foo", "parsing"]
categories = ["config", "parser-implementations"]
readme = "README.md"
# Only set `documentation` if docs are hosted off docs.rs.
# Only set `homepage` if there's a separate site distinct from the repo.
```

Tag every release with an annotated tag (`git tag -a v0.3.0 -m "..."`), and maintain `CHANGELOG.md` with breaking changes clearly called out (per RFC 1105).

**Rationale**: Crate-level docs are the first page users see on docs.rs. Missing metadata means the crate doesn't surface in search. Annotated tags survive operations that strip lightweight tags.

**See also**: C-CRATE-DOC, C-METADATA, C-RELNOTES

---

## API-49: License Dual MIT OR Apache-2.0

**Strength**: SHOULD

**Summary**: Unless you have a specific reason to choose otherwise, dual-license under MIT OR Apache-2.0 — the Rust project's own licensing and the ecosystem default.

```toml
[package]
license = "MIT OR Apache-2.0"
```

Include both `LICENSE-MIT` and `LICENSE-APACHE` in the repo root. Add a contribution clause to the README:

```text
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
```

**Rationale**: MIT-only is permissive but lacks patent provisions; Apache-2.0-only imposes restrictions that some users reject. Dual licensing gives downstream consumers the choice. Apache-2.0-only is explicitly *not* recommended for maximum compatibility.

**See also**: C-PERMISSIVE

---

## API-50: FFI Escape Hatches for Native Handles

**Strength**: SHOULD

**Summary**: Types that wrap an OS handle or FFI pointer must provide `unsafe fn from_native(h: Native) -> Self` plus `fn into_native(self) -> Native` and `fn to_native(&self) -> Native`. Document the safety contract on `from_native`.

```rust
pub struct Handle { raw: std::os::raw::c_int /* HNATIVE */ }

impl Handle {
    pub fn new() -> Self { /* ... */ todo!() }

    /// Wrap a native handle obtained elsewhere.
    ///
    /// # Safety
    ///
    /// * `raw` must be a valid, currently-open handle.
    /// * The handle must not be closed by another path while this wrapper is live.
    /// * Ownership of `raw` is transferred to the returned `Handle`.
    pub unsafe fn from_native(raw: std::os::raw::c_int) -> Self { Self { raw } }

    pub fn into_native(self) -> std::os::raw::c_int {
        let raw = self.raw;
        std::mem::forget(self);     // don't run Drop
        raw
    }

    pub fn to_native(&self) -> std::os::raw::c_int { self.raw }
}
```

**Rationale**: Systems code often sources handles from platform APIs the library doesn't wrap. Without escape hatches, users are forced into unsafe transmutes. With them, interop is explicit and the safety contract is documented. FFI-specific patterns (`#[repr(C)]`, UTF-8 round-tripping) live in `09-unsafe-ffi.md`.

**See also**: M-ESCAPE-HATCHES


## API Design Checklist

Before publishing a public type or function, walk this list:

```rust
// 1. Name — RFC 430 casing? verb-object-error for errors? feature names bare?
// 2. Parameters — borrow vs own matches actual need? impl AsRef / Read / RangeBounds?
// 3. Return type — compound via tuple/struct, never out-param (except buffer fill)?
// 4. Errors — concrete enum? Error + Display + Debug + Send + Sync? not `()`?
// 5. Traits implemented — Debug? Clone? PartialEq? Default? Send + Sync?
// 6. Construction — `new` inherent? builder when 3+ optional params?
// 7. Validation — static type first, then Result, then debug_assert!, then _unchecked?
// 8. Documentation — every pub item? # Errors / # Panics / # Safety as needed? `?` in examples?
// 9. Hidden details — #[doc(hidden)] on bridging impls? pub(crate) on internals?
// 10. Future-proofing — sealed traits? newtype-hide on complex returns? no leaked external types?
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| API-01 Abstractions don't visibly nest | SHOULD | Keep public signatures flat |
| API-02 Accept borrowed, return owned | SHOULD | `&T` in, `T` out |
| API-03 Accept `impl AsRef<T>` | SHOULD | Ergonomic path/str/bytes params |
| API-04 Accept `impl Read`/`Write` | SHOULD | Sans-IO for composability |
| API-05 Accept `impl RangeBounds<T>` | MUST | One signature for all range forms |
| API-06 Debug on all public types | MUST | Never empty, redact secrets |
| API-07 Hide smart-pointer wrappers | MUST | `Arc`/`Rc`/`Box` are internal |
| API-08 Named types over bool/Option | SHOULD | Enums, not ambiguous primitives |
| API-09 Binary/Octal/Hex for bit types | SHOULD | Bitflag formatting, not quantities |
| API-10 Builder for 3+ optional params | SHOULD | Chainable, validating `build` |
| API-11 Required params in builder ctor | SHOULD | Compile-time completeness |
| API-12 Cascade 4+ required params | SHOULD | Group into named types |
| API-13 `FromIterator` + `Extend` | MUST | `collect`/`partition`/`unzip` support |
| API-14 Constructors are static inherent | MUST | `new`, `open`, `with_*`, `from_*` |
| API-15 `as_`/`to_`/`into_` naming | MUST | Cost + ownership in the name |
| API-16 Conversions on specific type | SHOULD | Keep general types uncluttered |
| API-17 Impl `From`, never `Into` | MUST | Blanket `Into` comes free |
| API-18 Serde behind `serde` feature | SHOULD | Opt-in, exact feature name |
| API-19 Destructors don't fail or block | MUST | Separate `close` returning `Result` |
| API-20 Document every public item | MUST | Errors/Panics/Safety, `?` in examples |
| API-21 Hyperlink doc prose | SHOULD | Intra-doc links, checked by rustdoc |
| API-22 `#[doc(hidden)]` for plumbing | SHOULD | Hide bridging impls from docs |
| API-23 Concrete, well-behaved errors | MUST | `Error + Display + Debug + Send + Sync` |
| API-24 Essential fns are inherent | MUST | Discoverable without trait import |
| API-25 Methods when receiver is clear | SHOULD | Autoborrow, rustdoc, `use`-free |
| API-26 Caller controls data placement | SHOULD | No hidden clones, no `Copy`-as-hint |
| API-27 Expose intermediate results | SHOULD | Don't discard useful byproducts |
| API-28 No out-parameters | MUST | Tuples/structs — RVO handles it |
| API-29 Reader/writer by value | MUST | `&mut R: Read` blanket impl |
| API-30 Services implement shared Clone | MUST | `Arc<Inner>` pattern |
| API-31 Smart pointers use static fns | MUST | `Box::into_raw(b)`, not `b.into_raw()` |
| API-32 Operator overloads unsurprising | MUST | Math-like semantics only |
| API-33 Getters omit `get_` | SHOULD | `name()`, `name_mut()` |
| API-34 `iter`/`iter_mut`/`into_iter` | MUST | Plus matching type names |
| API-35 RFC 430 naming | MUST | `UpperCamelCase`, `snake_case`, etc. |
| API-36 Bare feature names | SHOULD | `serde`, not `use-serde` |
| API-37 Newtypes for distinctions | SHOULD | Zero-cost compile-time safety |
| API-38 Types are `Send` + `Sync` | MUST | Futures especially; assert at compile |
| API-39 Validate inputs strictly | MUST | Static > runtime > `debug_assert!` > `_unchecked` |
| API-40 Concrete > generic > `dyn` | SHOULD | Escalate only as needed |
| API-41 Generics minimize assumptions | SHOULD | `IntoIterator`, `AsRef<Path>` |
| API-42 Object-safe traits when useful | SHOULD | `where Self: Sized` for extensions |
| API-43 Sealed traits for closed sets | CONSIDER | Private supertrait |
| API-44 Hide return-type noise | SHOULD | Newtype or `impl Trait` |
| API-45 Extension traits for foreign types | CONSIDER | `*Ext` naming |
| API-46 Don't leak external types | SHOULD | std types at boundaries |
| API-47 Macros mirror Rust syntax | SHOULD | `struct`, `$vis`, attribute passthrough |
| API-48 Crate-level docs + metadata | SHOULD | `//!` doc, full `Cargo.toml` |
| API-49 Dual MIT OR Apache-2.0 | SHOULD | Ecosystem default |
| API-50 FFI escape hatches | SHOULD | `unsafe from_native`, `into_native`, `to_native` |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for borrowed-type parameters, `Default`, and derive choice.
- **Error Handling**: See `03-error-handling.md` for error-type anatomy, `#[from]`, and `?` ergonomics.
- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for how ownership shapes signatures.
- **Type Design**: See `05-type-design.md` for newtypes, `#[non_exhaustive]`, `bitflags`, struct bounds, and `PhantomData`.
- **Traits**: See `06-traits.md` for trait coherence, blanket impls, and associated types vs generic params.
- **Concurrency and Async**: See `07-concurrency-async.md` for `Send`/`Sync` implications and `!Send` futures.
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for `#[repr(C)]`, FFI string passing, and soundness obligations.
- **Anti-Patterns**: See `11-anti-patterns.md` for Deref polymorphism and other traps this guide warns against.
- **Project Structure**: See `12-project-structure.md` for workspace layout, feature organization, and crate splitting.
- **Documentation**: See `13-documentation.md` for the full rustdoc template.


## External References

- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) — the canonical C-* checklist
- [Rust API Guidelines Checklist](https://rust-lang.github.io/api-guidelines/checklist.html) — quick reference
- [RFC 430 — Finalizing naming conventions](https://github.com/rust-lang/rfcs/blob/master/text/0430-finalizing-naming-conventions.md)
- [RFC 199 — Ownership variants for iterator methods](https://github.com/rust-lang/rfcs/blob/master/text/0199-ownership-variants.md)
- [RFC 1105 — API evolution (breaking changes)](https://github.com/rust-lang/rfcs/blob/master/text/1105-api-evolution.md)
- [RFC 1574 — API documentation conventions](https://github.com/rust-lang/rfcs/blob/master/text/1574-more-api-documentation-conventions.md)
- [RFC 1687 — Crate-level documentation](https://github.com/rust-lang/rfcs/blob/master/text/1687-crates-io-default-ranking.md)
- [The Cargo Book — Features](https://doc.rust-lang.org/cargo/reference/features.html)
- [`std::error::Error`](https://doc.rust-lang.org/std/error/trait.Error.html), [`std::convert::From`](https://doc.rust-lang.org/std/convert/trait.From.html), [`std::ops::RangeBounds`](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html)
- Pragmatic Rust Guidelines: M-SIMPLE-ABSTRACTIONS, M-AVOID-WRAPPERS, M-DI-HIERARCHY, M-INIT-BUILDER, M-INIT-CASCADED, M-SERVICES-CLONE, M-IMPL-ASREF, M-IMPL-RANGEBOUNDS, M-IMPL-IO, M-ESSENTIAL-FN-INHERENT, M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY, M-REGULAR-FN, M-STRONG-TYPES, M-DONT-LEAK-TYPES, M-ESCAPE-HATCHES, M-TYPES-SEND
