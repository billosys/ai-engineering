# Core Rust Idioms

Foundational idioms every Rust programmer uses daily: naming and casing discipline, constructor and iterator conventions, ownership-shaped patterns like `mem::take`, closure capture control, RAII, `Option`/`Result` combinators, `format!` and `let-else`, plus the style-guide rules (indentation, trailing commas, attribute placement, imports, lint overrides) that `rustfmt` and `clippy` enforce. Type-level design (newtypes, enums, traits) lives in `05-type-design.md`; this guide covers the day-to-day idioms that shape readable Rust code.


## ID-02: `mem::take` and `mem::replace` to Move Out of `&mut`

**Strength**: SHOULD

**Summary**: Use `std::mem::take` or `std::mem::replace` to move a value out of a mutable reference — essential for transforming enums without cloning.

```rust
use std::mem;

enum State {
    Loading { url: String },
    Ready { data: Vec<u8> },
    Error { message: String },
}

impl State {
    // ❌ BAD: clone to satisfy the borrow checker
    fn to_ready_bad(&mut self, data: Vec<u8>) {
        if let State::Loading { url } = self {
            let url = url.clone();          // unnecessary allocation
            *self = State::Ready { data };
            log::info!("loaded from {url}");
        }
    }

    // ✅ GOOD: mem::take moves the String out, leaves String::default()
    fn to_ready(&mut self, data: Vec<u8>) {
        if let State::Loading { url } = self {
            let url = mem::take(url);       // zero-cost for String
            *self = State::Ready { data };
            log::info!("loaded from {url}");
        }
    }
}

// mem::replace returns the old value — use when you need both
fn swap_config(current: &mut String, new: String) -> String {
    mem::replace(current, new)
}
```

**Rationale**: `mem::take` replaces a value behind `&mut` with `T::default()` and returns the old value; `mem::replace` lets you supply any replacement. Both avoid the "cannot move out of borrowed content" error without cloning. They're free for `String`, `Vec`, `Option`, and other cheap-default types.

**See also**: `Option::take`, ID-35 (temporary mutability), 11-anti-patterns.md (clone to satisfy borrow checker)

---

## ID-04: Ad-hoc Conversions Follow `as_` / `to_` / `into_`

**Strength**: MUST

**Summary**: Conversion prefixes communicate cost and ownership: `as_` is free and borrowed, `to_` allocates, `into_` consumes `self`.

```rust
// ✅ GOOD: cost-signalling prefixes

impl str {
    // as_* — free, borrowed → borrowed
    pub fn as_bytes(&self) -> &[u8] { /* reinterpret */ todo!() }

    // to_* — expensive, creates owned data
    pub fn to_lowercase(&self) -> String { /* allocates, iterates */ todo!() }
}

impl String {
    // into_* — consumes self, transfers ownership
    pub fn into_bytes(self) -> Vec<u8> { /* zero-cost move */ todo!() }
}

// ❌ BAD: prefix misleads about cost
impl std::path::Path {
    pub fn to_os_str(&self) -> &std::ffi::OsStr { todo!() }   // should be as_os_str
    pub fn as_path_buf(&self) -> std::path::PathBuf { todo!() } // should be to_path_buf
}

// Copy types use to_* even though the receiver is by value
impl f64 {
    pub fn to_radians(self) -> f64 { self * std::f64::consts::PI / 180.0 }
    pub fn to_degrees(self) -> f64 { self * 180.0 / std::f64::consts::PI }
}
```

**Rationale**: These prefixes are codified in the Rust API Guidelines (C-CONV). Picking the right one tells the caller the cost without reading the implementation.

**See also**: C-CONV, ID-20 (getters), 02-api-design.md (`From`/`Into`)

---

## ID-05: Document Every Magic Value

**Strength**: MUST

**Summary**: Hardcoded constants must explain *why* the value was chosen, what breaks if it changes, and any external dependency.

```rust
// ❌ BAD: naked literal, no context
const TIMEOUT: u64 = 86400;

// Better — inline rationale
// Wait at most a day; matches api.foo.com's request lifetime policy.
const TIMEOUT: u64 = 60 * 60 * 24;

// ✅ GOOD: named, typed, documented
/// How long we wait for the upstream server.
///
/// Chosen to exceed the worst-case processing time observed on
/// `api.foo.com`. Reducing this risks aborting valid long-running
/// requests; increasing it risks holding connection slots too long.
const UPSTREAM_SERVER_TIMEOUT: std::time::Duration =
    std::time::Duration::from_secs(60 * 60 * 24);
```

**Rationale**: Magic numbers become maintenance hazards. A comment explaining the *reason* lets the next reader (including future you) change the value safely.

**See also**: M-DOCUMENTED-MAGIC

---

## ID-06: Avoid Weasel Words in Names

**Strength**: MUST

**Summary**: Names like `Service`, `Manager`, `Helper`, `Factory` add no information. Name types after what they actually are or do.

```rust
// ❌ BAD: weasel words
pub struct BookingService { bookings: Vec<Booking> }
pub struct ConnectionManager { /* pool */ }
pub struct UserFactory;

// ✅ GOOD: the name describes the thing
pub struct Bookings { items: Vec<Booking> }
pub struct ConnectionPool { /* ... */ }
pub struct UserBuilder { /* ... */ }

// When you need to accept a factory as a parameter, use a closure type
pub fn with_user<F: Fn() -> User>(_make: F) { /* ... */ }

struct Booking;
struct User;
```

**Rationale**: `Service`, `Manager`, and `Factory` are common in languages with rigid class hierarchies. Rust types are free to be named after their purpose: a collection of bookings is `Bookings`, a connection pool is `ConnectionPool`, a factory is a `Builder` or an `impl Fn() -> T`.

**See also**: M-CONCISE-NAMES, ID-10 (Builder)

---

## ID-07: Casing Conforms to RFC 430

**Strength**: MUST

**Summary**: `UpperCamelCase` for types and enum variants; `snake_case` for functions, methods, variables, fields, modules, and macros; `SCREAMING_SNAKE_CASE` for `const` and immutable `static`. Acronyms in type names are capitalized as one word (`HttpResponse`, not `HTTPResponse`).

```rust
// ✅ GOOD
pub struct HttpResponse {          // UpperCamelCase, acronym as word
    status_code: u16,              // snake_case field
    body: String,
}

pub enum Direction { North, South, East, West }   // UpperCamelCase variants

const MAX_RETRIES: u32 = 3;
static DEFAULT_NAME: &str = "unnamed";

fn parse_url(input: &str) -> HttpResponse { /* ... */ todo!() }
mod network_io { /* snake_case module */ }
macro_rules! my_macro { () => {}; }

// ❌ BAD
pub struct HTTPResponse {          // acronym in caps
    StatusCode: u16,               // PascalCase field
    Body: String,
}
const maxRetries: u32 = 3;         // wrong case for const
fn ParseUrl() {}                   // wrong case for fn
```

**Rationale**: The compiler's default lints (`non_camel_case_types`, `non_snake_case`, `non_upper_case_globals`) enforce these conventions — disabling them is almost always wrong. Consistent casing makes Rust code scannable at a glance and lets autocomplete work predictably across crates.

**See also**: ID-25 (word order), Rust API Guidelines C-CASE

---

## ID-08: Owned Collections Simplify Lifetimes

**Strength**: CONSIDER

**Summary**: `Vec<T>`, `String`, and `Box<T>` own heap data, so structs that hold them need no lifetime parameters. Prefer owned collections in fields unless zero-copy is a measured requirement.

```rust
// ✅ GOOD: owned — no lifetime on the struct
pub struct UserDatabase {
    users: Vec<String>,
}

impl UserDatabase {
    pub fn new() -> Self { Self { users: Vec::new() } }
    pub fn add(&mut self, name: String) { self.users.push(name); }
}

// ❌ AWKWARD: borrowing forces lifetime parameters everywhere
pub struct UserDatabaseRef<'a> {
    users: &'a [String],
}
// every function, every caller, every impl must carry `'a`
```

**Rationale**: The heap allocation is almost always cheaper than the cognitive cost of pervasive lifetime parameters. Reach for borrowed fields only when profiling shows allocation pressure or when the type is a genuine short-lived view (like an iterator).

**See also**: 04-ownership-borrowing.md

---

## ID-10: `new` and `Default` for Simple Construction

**Strength**: SHOULD

**Summary**: Rust has no constructor keyword — the convention is an associated function `fn new(...) -> Self`. Implement `Default` when a zero/empty instance makes sense; if `new()` takes no arguments it must agree with `Default::default()`.

```rust
pub struct Config {
    timeout_ms: u64,
    retries: u32,
    verbose: bool,
}

impl Config {
    /// Creates a `Config` with the given timeout and conventional defaults.
    pub fn new(timeout_ms: u64) -> Self {
        Self { timeout_ms, retries: 3, verbose: false }
    }
}

impl Default for Config {
    fn default() -> Self {
        Self { timeout_ms: 5_000, retries: 3, verbose: false }
    }
}

// Alternate constructors use descriptive names (with_, from_)
impl Config {
    pub fn with_retries(retries: u32) -> Self {
        Self { retries, ..Self::default() }
    }
}

// Derive Default when every field's default is correct
#[derive(Default)]
pub struct Counter {
    count: u64,
    reset_at: Option<std::time::Instant>,
}

let c1 = Config::new(1_000);
let c2 = Config::default();
let c3 = Config { verbose: true, ..Config::default() };
```

**Rationale**: `new` is expected by every Rust consumer; `Default` plugs into generic code (`Option::unwrap_or_default`, `mem::take`, struct update syntax). For construction with many optional parameters, reach for the Builder pattern (TD-10).

**See also**: TD-10 (Builder), ID-31 (constructors as associated fn), C-CTOR, C-COMMON-TRAITS

---

## ID-13: Programming Bugs Panic, Recoverable Failures Return `Result`

**Strength**: MUST

**Summary**: Panic on contract violations (the caller did something the function forbids). Return `Result` for conditions the caller can reasonably handle.

```rust
// ❌ BAD: contract violation dressed up as a recoverable error
fn divide_by(x: u32, y: u32) -> Result<u32, DivisionError> {
    if y == 0 { return Err(DivisionError::DivideByZero); }
    Ok(x / y)
}

// ✅ GOOD: contract violation panics with a clear message
fn divide_by(x: u32, y: u32) -> u32 {
    assert!(y != 0, "divide_by: y must be non-zero (got {x}/{y})");
    x / y
}

// ✅ BETTER: make the bug unrepresentable at the type level
use std::num::NonZeroU32;

fn divide_by_nz(x: u32, y: NonZeroU32) -> u32 {
    x / y.get()
}

#[derive(Debug)]
pub enum DivisionError { DivideByZero }
```

```rust
// ✅ Recoverable — the caller might have a corrupt or absent file
fn parse_config(path: &std::path::Path) -> Result<Config, std::io::Error> {
    let _content = std::fs::read_to_string(path)?;
    /* ... */
    Ok(Config::default())
}
```

**Rationale**: Panics signal *the program has a bug*; `Result` signals *a normal failure mode the caller is responsible for*. Conflating the two pollutes error types with impossible variants and blurs responsibility.

**See also**: ID-28, M-PANIC-ON-BUG, 03-error-handling.md

---

## ID-15: Feature Names Without Placeholder Prefixes

**Strength**: MUST

**Summary**: Don't prefix Cargo features with `use-` or `with-`. Name the feature after what it enables.

```toml
# ❌ BAD: Cargo.toml
[features]
default  = ["use-std"]
use-std  = []
with-serde = ["dep:serde"]

# ✅ GOOD
[features]
default = ["std"]
std     = []
serde   = ["dep:serde"]

[dependencies]
serde = { version = "1", optional = true }
```

```rust
// In lib.rs — gated on the feature name directly
#![cfg_attr(not(feature = "std"), no_std)]

#[cfg(feature = "serde")]
mod serde_support;
```

**Rationale**: Cargo implicitly creates a feature with the dependency's own name for every optional dependency. Manual features should follow the same convention so downstream `features = [...]` arrays read uniformly.

**See also**: C-FEATURE

---

## ID-18: Finalize Resources in Destructors (RAII)

**Strength**: MUST

**Summary**: Rust has no `finally`. Put cleanup in `Drop::drop` so it runs on every exit path — normal return, early `?`, and unwinding panic.

```rust
use std::path::PathBuf;

pub struct TempFile {
    path: PathBuf,
}

impl TempFile {
    pub fn new() -> std::io::Result<Self> {
        let path = std::env::temp_dir().join(uuid::Uuid::new_v4().to_string());
        std::fs::File::create(&path)?;
        Ok(Self { path })
    }
    pub fn path(&self) -> &std::path::Path { &self.path }
}

impl Drop for TempFile {
    fn drop(&mut self) {
        // Runs on normal return, ?-propagation, or unwinding panic
        let _ = std::fs::remove_file(&self.path);
    }
}

fn process() -> std::io::Result<()> {
    let temp = TempFile::new()?;
    write_data(temp.path())?;
    run_analysis(temp.path())?;
    Ok(())
    // TempFile::drop runs here — even if write_data or run_analysis failed
}

// Guard pattern: lock-like APIs return a Drop-guard that releases on scope exit
use std::sync::Mutex;

fn push(m: &Mutex<Vec<i32>>, v: i32) {
    let mut guard = m.lock().unwrap();      // acquires
    guard.push(v);
}                                            // guard drops → releases lock

fn write_data(_: &std::path::Path) -> std::io::Result<()> { Ok(()) }
fn run_analysis(_: &std::path::Path) -> std::io::Result<()> { Ok(()) }
```

**Rationale**: Manual cleanup is forgotten, skipped on early return, and skipped entirely on panic. Wrapping the resource in a type that owns the cleanup moves that responsibility from every call site into one `Drop` impl. This is the foundation of `MutexGuard`, `File`, `BufWriter`, `ScopeGuard`, and most of the ecosystem's resource management.

**Caveats**: Destructors do *not* run if the process aborts (`std::process::abort`, double panic, SIGKILL). Don't rely on `Drop` for critical external effects (database commits, file syncs) — do those explicitly and treat `Drop` as a best-effort cleanup.

**See also**: TD-05 (private fields protect invariants), 07-concurrency-async.md (lock guards)

---

## ID-20: Getter Names Match the Field

**Strength**: MUST

**Summary**: Drop the `get_` prefix. `self.timeout()` is a getter for `timeout`. Use `_mut` suffix for mutable access and reserve `get` for contexts where one canonical access exists (like `Cell::get`) or where the operation can fail (`slice::get`).

```rust
use std::time::Duration;
use std::net::SocketAddr;

pub struct Connection {
    timeout: Duration,
    address: SocketAddr,
}

impl Connection {
    // ✅ GOOD: field-named getters
    pub fn timeout(&self) -> Duration { self.timeout }
    pub fn address(&self) -> &SocketAddr { &self.address }
    pub fn timeout_mut(&mut self) -> &mut Duration { &mut self.timeout }
}

// ❌ BAD: redundant get_ prefix
impl Connection {
    pub fn get_timeout(&self) -> Duration { self.timeout }
    pub fn get_address(&self) -> &SocketAddr { &self.address }
}

// ✅ GOOD: `get` is fine when the operation is partial or there's one obvious thing
impl<T> std::cell::Cell<T> where T: Copy {
    pub fn get(&self) -> T { /* sole payload */ todo!() }
}

// slice::get returns Option — the name signals bounds-checking
// slice::get_unchecked is unsafe indexing
```

**Rationale**: `get_` is redundant noise. Field-named getters compose cleanly at call sites (`user.name().trim()`), and the `_mut` suffix is the standard signal for mutable access.

**See also**: C-GETTER, ID-23 (iterator method pairs)

---

## ID-22: Iterate Over `Option`

**Strength**: CONSIDER

**Summary**: `Option<T>` implements `IntoIterator` — treat it as a zero-or-one element iterator when composing with iterator combinators.

```rust
// Extend a Vec with a maybe-present value
let turing: Option<&str> = Some("Turing");
let mut logicians = vec!["Curry", "Kleene", "Markov"];
logicians.extend(turing);                 // pushes "Turing" iff Some

// Chain an Option onto an iterator
let extras: Option<&str> = Some("Church");
for name in logicians.iter().chain(extras.iter()) {
    println!("{name}");
}

// Flatten out a Vec<Option<T>> — Option implements IntoIterator
let values: Vec<Option<i32>> = vec![Some(1), None, Some(2), None, Some(3)];
let sum: i32 = values.into_iter().flatten().sum();    // 6

// Prefer `if let Some(x) = opt` over `for x in opt` for simple conditional use
// Prefer `std::iter::once(x)` when the value is always present
```

**Rationale**: `Option::iter`, `Option::into_iter`, and `.flatten()` let you compose optional values with the rest of the iterator ecosystem without branching. This keeps code linear — no `if let` pyramids in the middle of a pipeline.

**See also**: ID-27 (combinators), Iterator::filter_map

---

## ID-23: Collections Expose `iter` / `iter_mut` / `into_iter`

**Strength**: MUST

**Summary**: A collection of `T` provides three iterator entry points: `iter()` yields `&T`, `iter_mut()` yields `&mut T`, `into_iter()` yields `T` (consumes the collection).

```rust
pub struct MyList<T> { items: Vec<T> }

impl<T> MyList<T> {
    pub fn iter(&self) -> std::slice::Iter<'_, T> { self.items.iter() }
    pub fn iter_mut(&mut self) -> std::slice::IterMut<'_, T> { self.items.iter_mut() }
    pub fn into_iter(self) -> std::vec::IntoIter<T> { self.items.into_iter() }
}

// Consumers pick the access mode they need
let mut list = MyList { items: vec![1, 2, 3] };

for v in list.iter()     { println!("{v}"); }   // & — borrow each
for v in list.iter_mut() { *v *= 2; }           // &mut — mutate in place
for v in list.into_iter() { println!("{v}"); }  // T — consumes list

// str is a special case: it's not a homogeneous collection, so instead of
// iter() it offers chars(), bytes(), lines(), split(...) — each with a
// specific interpretation
```

**Rationale**: This triplet is assumed by every consumer: `for x in &coll`, `for x in &mut coll`, and `for x in coll` all just work when you follow it (the `IntoIterator` impls on `&C`, `&mut C`, and `C` delegate to `iter`/`iter_mut`/`into_iter` respectively).

**See also**: C-ITER, ID-24 (iterator type naming)

---

## ID-24: Iterator Type Names Match the Producing Method

**Strength**: SHOULD

**Summary**: `iter()` returns a type called `Iter`; `iter_mut()` returns `IterMut`; `into_iter()` returns `IntoIter`. Domain iterators follow the same shape (`Keys`, `Values`, `Drain`, ...).

```rust
// Standard library
impl<T> Vec<T> {
    pub fn iter(&self) -> std::slice::Iter<'_, T> { todo!() }
    pub fn iter_mut(&mut self) -> std::slice::IterMut<'_, T> { todo!() }
    pub fn into_iter(self) -> std::vec::IntoIter<T> { todo!() }
    pub fn drain<R>(&mut self, _range: R) -> std::vec::Drain<'_, T> { todo!() }
}

// Function-named iterator
pub struct PercentEncode<'a> { /* ... */ _p: std::marker::PhantomData<&'a ()> }

pub fn percent_encode(_input: &str) -> PercentEncode<'_> {
    PercentEncode { _p: std::marker::PhantomData }
}
```

**Rationale**: Matching type names to method names makes rustdoc, error messages, and `use` paths predictable. It also signals that the type is an iterator — no further explanation needed.

---

## ID-25: Consistent Word Order in Names

**Strength**: SHOULD

**Summary**: Within a crate, keep word order consistent for related types. Standard library uses `Parse<Thing>Error`, `Into<Thing>`, `From<Thing>`.

```rust
// ✅ GOOD: consistent Parse<T>Error ordering, as stdlib does
pub struct ParseBoolError;
pub struct ParseCharError;
pub struct ParseFloatError;
pub struct ParseIntError;

// ❌ BAD: every combination imaginable
pub struct ParseBoolError;
pub struct CharParseError;
pub struct ErrorParseFloat;

// ✅ GOOD: with_<thing> builder methods
impl RequestBuilder {
    pub fn with_header(self, _k: &str, _v: &str) -> Self { self }
    pub fn with_timeout(self, _d: std::time::Duration) -> Self { self }
    pub fn with_body(self, _body: String) -> Self { self }
}

struct RequestBuilder;
```

**Rationale**: Consistent word order makes autocomplete predictable and makes new additions guessable. If `ParseIntError` exists, a user looking for the float equivalent will type `ParseF` before `Float`.

---

## ID-26: On-Stack Dispatch via Enums, Not Trait Objects

**Strength**: CONSIDER

**Summary**: When the set of implementing types is closed and fits in source, prefer an enum with an inherent `impl` over `Box<dyn Trait>`. Enums dispatch statically, allocate on the stack, and enable exhaustive matching.

```rust
// ✅ Closed set — enum dispatch is zero-cost, stack-allocated
pub enum Operation {
    Add(i32),
    Mul(i32),
    Div(i32),
}

impl Operation {
    pub fn apply(&self, value: i32) -> i32 {
        match self {
            Operation::Add(x) => value + x,
            Operation::Mul(x) => value * x,
            Operation::Div(x) => value / x,
        }
    }
}

pub fn run(ops: &[Operation], seed: i32) -> i32 {
    ops.iter().fold(seed, |acc, op| op.apply(acc))
}

// Use Box<dyn Trait> when the set of types is open (plugins) or when
// consumers outside your crate can add implementations.
pub trait Op { fn apply(&self, value: i32) -> i32; }

pub fn run_dyn(ops: &[Box<dyn Op>], seed: i32) -> i32 {
    ops.iter().fold(seed, |acc, op| op.apply(acc))
}
```

**Rationale**: Enums give you static dispatch, exhaustive match checking, and no heap traffic. Trait objects are the right tool when the type set is genuinely open (user-extensible plugins) or when you need to store a heterogeneous collection of unrelated types that only share a behavior.

**See also**: TD-27 (object safety), 06-traits.md

---

## ID-27: `Option` / `Result` Combinators Over `match`

**Strength**: SHOULD

**Summary**: Use `?`, `map`, `and_then`, `ok_or`, `unwrap_or_else` to compose `Option` and `Result` values. Reserve `match` for situations where you genuinely need exhaustive multi-arm handling.

```rust
// ❌ VERBOSE
fn user_email(id: i32) -> Option<String> {
    match find_user(id) {
        Some(user) => match user.email {
            Some(email) => Some(email.to_lowercase()),
            None => None,
        },
        None => None,
    }
}

// ✅ CONCISE
fn user_email(id: i32) -> Option<String> {
    find_user(id)?.email.map(|e| e.to_lowercase())
}

// Common shapes
// opt.unwrap_or(default)              — eager default
// opt.unwrap_or_else(|| compute())    — lazy default
// opt.ok_or(Error::NotFound)?         — Option → Result, propagate
// res.map_err(Error::from)?           — convert error and propagate
// res.ok()                            — Result → Option, discard error
// res.and_then(|x| x.validate())      — chain fallible step

struct User { email: Option<String> }
fn find_user(_id: i32) -> Option<User> { None }
```

**Rationale**: Combinators read top-to-bottom as the transformation pipeline, while nested `match` forces the reader to track success/failure through each level. `?` in particular is the idiomatic way to propagate errors — only write `match` on `Result` when you need to do real work on the error.

**See also**: 03-error-handling.md

---

## ID-28: A Panic Means "Stop the Program"

**Strength**: MUST

**Summary**: Panics are not exceptions. Don't panic for recoverable failures, and don't design code that assumes panics will be caught.

```rust
// ❌ BAD: panic on a recoverable I/O failure
fn load_config(path: &str) -> Config {
    let text = std::fs::read_to_string(path).unwrap();  // PANICS
    parse(&text).unwrap()                                // PANICS
}

// ✅ GOOD: return Result
fn load_config(path: &str) -> Result<Config, LoadError> {
    let text = std::fs::read_to_string(path).map_err(LoadError::Io)?;
    parse(&text).map_err(LoadError::Parse)
}

// ✅ Acceptable panic: an invariant the caller was responsible for upholding
fn take_first(xs: &[i32]) -> i32 {
    assert!(!xs.is_empty(), "take_first: empty slice");
    xs[0]
}

#[derive(Debug)]
enum LoadError { Io(std::io::Error), Parse(String) }
struct Config;
fn parse(_: &str) -> Result<Config, String> { Ok(Config) }
```

**Rationale**: With `panic = "abort"` the program simply terminates; with unwinding, `catch_unwind` exists but it's for very narrow use cases (test frameworks, FFI boundaries). Code that expects panics to be routinely caught is fragile.

**See also**: ID-13, M-PANIC-IS-STOP, 03-error-handling.md

---

## ID-29: Pass Variables to Closures via Block-Scoped Rebinding

**Strength**: SHOULD

**Summary**: When a `move` closure needs some variables moved, others cloned, and others borrowed, use a block expression to rebind them before the closure — keep the preparation local and the names clean.

```rust
use std::rc::Rc;
use std::thread;

// ✅ GOOD: clear, local rebinding
let num1 = Rc::new(1);
let num2 = Rc::new(2);
let num3 = Rc::new(3);

let closure = {
    // num1 is moved (captured by move)
    let num2 = num2.clone();      // cloned
    let num3 = num3.as_ref();     // borrowed
    move || *num1 + *num2 + *num3
};

// ❌ BAD: _cloned / _borrowed names pollute the outer scope
let num2_cloned = num2.clone();
let num3_borrowed = num3.as_ref();
let bad = move || *num2_cloned + *num3_borrowed;

// Threading — `move` captures everything the closure mentions
fn spawn_worker(data: Vec<u8>) -> thread::JoinHandle<usize> {
    thread::spawn(move || data.len())
}

// Clone before `move` when the original must live on
fn spawn_and_keep(name: String) -> (String, thread::JoinHandle<()>) {
    let for_thread = name.clone();
    let handle = thread::spawn(move || println!("thread: {for_thread}"));
    (name, handle)
}
```

**Rationale**: Without this pattern you end up with `foo_cloned`, `foo_borrowed`, and `foo_for_thread` names leaking into the surrounding function. The block-expression rebinding co-locates the capture preparation with the closure.

**See also**: ID-35 (temporary mutability), 07-concurrency-async.md

---

## ID-30: `Option<T>` Instead of Sentinel Values

**Strength**: MUST

**Summary**: Represent absence with `Option`, not a magic value like `-1`, `""`, or `u32::MAX`.

```rust
// ❌ BAD: sentinels require documentation and get forgotten
pub struct User {
    pub name: String,
    pub age: i32,       // -1 means "unknown"
    pub email: String,  // "" means "not provided"
}

// ✅ GOOD: absence is in the type
pub struct UserGood {
    pub name: String,
    pub age: Option<u32>,
    pub email: Option<String>,
}

// Consumers must handle absence explicitly
fn describe(u: &UserGood) -> String {
    match u.age {
        Some(a) => format!("{} ({a})", u.name),
        None => format!("{} (age unknown)", u.name),
    }
}
```

**Rationale**: Sentinel values silently coexist with valid values — nothing stops `age: -1` from being added into a sum or compared with `<`. `Option` forces the absence case to be acknowledged at every use site.

**See also**: TD-20 (`NonZeroU32`), 03-error-handling.md

---

## ID-31: Prefer Free Functions Over Associated Functions for Unrelated Work

**Strength**: SHOULD

**Summary**: Associated functions belong to the type — use them for constructors and trait implementations. Put general-purpose helpers at module scope as free functions.

```rust
pub struct Database;

impl Database {
    // ✅ Constructor — belongs on the type
    pub fn new() -> Self { Self }

    // ✅ Method — operates on an instance
    pub fn query(&self, _sql: &str) -> Vec<Row> { vec![] }
}

// ❌ BAD: general helper masquerading as associated fn
impl Database {
    fn valid_identifier(s: &str) -> bool {
        s.chars().all(|c| c.is_ascii_alphanumeric() || c == '_')
    }
}

// ✅ GOOD: free function
pub fn is_valid_identifier(s: &str) -> bool {
    s.chars().all(|c| c.is_ascii_alphanumeric() || c == '_')
}

struct Row;
```

**Rationale**: Associated functions are pulled into everyone's `Database::valid_identifier` namespace whether they want them or not; free functions live at module scope where they're found by module path. The convention is: associated fn only when the function conceptually belongs to the type.

**See also**: M-REGULAR-FN

---

## ID-33: Return Consumed Arguments on Error

**Strength**: CONSIDER

**Summary**: When a function consumes an argument by value and can fail, return the argument inside the error so the caller can retry or recover.

```rust
pub struct Message(pub String);

#[derive(Debug)]
pub struct SendError {
    pub message: Message,               // returned to the caller
    pub source: std::io::Error,
}

pub fn send(msg: Message) -> Result<(), SendError> {
    match try_write(&msg.0) {
        Ok(()) => Ok(()),
        Err(source) => Err(SendError { message: msg, source }),
    }
}

// Caller can retry without pre-cloning the message
let mut msg = Message(String::from("hello"));
for _ in 0..3 {
    match send(msg) {
        Ok(()) => break,
        Err(e) => msg = e.message,
    }
}

fn try_write(_: &str) -> Result<(), std::io::Error> { Ok(()) }
```

**Rationale**: Without this pattern, callers must `clone()` arguments preemptively "in case" the call fails. Returning the value on error lets them pay that cost only when needed. The standard library uses this pattern in `String::from_utf8` (`FromUtf8Error` contains the original `Vec<u8>`).

**See also**: 03-error-handling.md

---

## ID-34: Build Strings with `format!`

**Strength**: SHOULD

**Summary**: Prefer `format!` or `write!` over manual `push_str` chains. `String` concatenation with `+` is fine for two pieces.

```rust
// ❌ VERBOSE: manual push_str
fn greet_bad(name: &str, age: u32) -> String {
    let mut s = String::from("Hello, ");
    s.push_str(name);
    s.push_str("! You are ");
    s.push_str(&age.to_string());
    s.push_str(" years old.");
    s
}

// ✅ GOOD: format! reads like the output
fn greet(name: &str, age: u32) -> String {
    format!("Hello, {name}! You are {age} years old.")
}

// When writing into an existing buffer, use write!
use std::fmt::Write;
fn append_greeting(buf: &mut String, name: &str) {
    write!(buf, "Hello, {name}!").expect("writing to String cannot fail");
}

// Two-piece concatenation: + is concise and clear
let full = first_name.to_string() + " " + last_name;

// For performance-critical assembly with known capacity, reserve up front
fn csv_row(fields: &[&str]) -> String {
    let cap = fields.iter().map(|s| s.len() + 1).sum();
    let mut row = String::with_capacity(cap);
    for (i, f) in fields.iter().enumerate() {
        if i > 0 { row.push(','); }
        row.push_str(f);
    }
    row
}

let first_name = "Ada";
let last_name = "Lovelace";
```

**Rationale**: `format!` is readable and handles `Display` / `Debug` formatting uniformly. Don't micro-optimize into `push_str` chains without a measured reason — the generated code is often similar, and `format!` is less error-prone.

**See also**: `std::fmt::Write`, 08-performance.md

---

## ID-35: Temporary Mutability via Block or Shadowing

**Strength**: SHOULD

**Summary**: Scope mutation to the setup phase, then rebind as immutable. Two forms: inner-block with returned value, or shadow with a new `let`.

```rust
// Pattern 1 — nested block, returns the value
let data = {
    let mut temp = fetch_data();
    temp.sort();
    temp.dedup();
    temp                            // block evaluates to `temp`
};
// `data` is immutable from here

// Pattern 2 — shadow with let
let mut data = fetch_data();
data.sort();
data.dedup();
let data = data;                    // rebind as immutable
// `data` is immutable from here

// Pattern 3 — chain into a collect (no `mut` at all)
let data: Vec<_> = fetch_data()
    .into_iter()
    .filter(|x| *x > 0)
    .collect();

fn fetch_data() -> Vec<i32> { vec![3, 1, 2, 1] }
```

**Rationale**: Limiting mutability to the preparation phase signals intent, prevents accidental later mutation, and enables the compiler to catch mistakes. Both patterns compile to identical code — pick whichever reads better in context.

**See also**: ID-29 (block-scoped closure capture)

---

## ID-38: `let ... else` for Pattern-Matched Early Return

**Strength**: SHOULD

**Summary**: Use `let PATTERN = expr else { diverge; }` to destructure when the happy path must continue and any other pattern must exit (return, break, continue, panic).

```rust
// ❌ VERBOSE: match just to early-return
fn process_user(id: Option<i32>) -> Result<User, Error> {
    let id = match id {
        Some(id) => id,
        None => return Err(Error::MissingId),
    };
    lookup(id)
}

// ✅ CONCISE: let-else
fn process_user_good(id: Option<i32>) -> Result<User, Error> {
    let Some(id) = id else {
        return Err(Error::MissingId);
    };
    lookup(id)
}

// Works with any refutable pattern
fn parse_pair(s: &str) -> Option<(&str, &str)> {
    let Some((k, v)) = s.split_once('=') else {
        return None;
    };
    Some((k.trim(), v.trim()))
}

struct User;
enum Error { MissingId }
fn lookup(_: i32) -> Result<User, Error> { Ok(User) }
```

**Rationale**: `let ... else` keeps the happy path at the current indentation level. The `else` block must diverge (`return`, `break`, `continue`, `panic!`, `std::process::exit`, etc.) — the compiler checks this.

---

## ID-39: Prefer Borrowed Types for Function Arguments

**Strength**: MUST

**Summary**: Take `&str`, `&[T]`, and `&T` instead of `&String`, `&Vec<T>`, and `&Box<T>`. Deref coercion lets the former accept the latter for free; the reverse requires allocation.

```rust
// ❌ BAD: &String can only accept &String
fn count_vowels_bad(word: &String) -> usize {
    word.chars().filter(|c| "aeiou".contains(*c)).count()
}
// count_vowels_bad("literal");            // ERROR: &str does not coerce to &String

// ✅ GOOD: &str accepts &String, &str, Box<str>, slice-of-split, everything
fn count_vowels(word: &str) -> usize {
    word.chars().filter(|c| "aeiou".contains(*c)).count()
}

let s = String::from("cautious");
count_vowels(&s);                        // &String → &str via Deref
count_vowels("elephant");                // &'static str
for word in s.split(' ') { count_vowels(word); }   // &str from split

// Same rule for slices
fn total(values: &[i32]) -> i32 { values.iter().sum() }

total(&vec![1, 2, 3]);                   // &Vec<i32> → &[i32]
total(&[1, 2, 3]);                       // &[i32; 3] → &[i32]
```

**Rationale**: `&String` is two levels of indirection (reference to a `String`, which itself holds a pointer). `&str` is one. Beyond layout, `&str` is strictly more general — any `&String` coerces to `&str`, but `&str` cannot coerce back without allocating. Clippy's `ptr_arg` lint catches `&String` / `&Vec<T>` automatically.

**Clippy**: `clippy::ptr_arg`

**See also**: ID-08 (owned collections for fields), 04-ownership-borrowing.md

---

## ID-41: Iterator Chains Over Manual Loops

**Strength**: SHOULD

**Summary**: Express transformations as iterator chains (`map`, `filter`, `fold`, `collect`) rather than imperative `for` loops with mutable accumulators.

```rust
struct Person { name: String, age: u32 }

// ❌ IMPERATIVE: mutable state, multiple branches
fn adult_names_bad(people: &[Person]) -> Vec<String> {
    let mut names = Vec::new();
    for p in people {
        if p.age >= 18 {
            names.push(p.name.clone());
        }
    }
    names
}

// ✅ FUNCTIONAL: linear pipeline
fn adult_names(people: &[Person]) -> Vec<String> {
    people.iter()
        .filter(|p| p.age >= 18)
        .map(|p| p.name.clone())
        .collect()
}

// Reach for a specialized adapter when one fits
fn first_admin<'a>(users: &'a [User]) -> Option<&'a User> {
    users.iter().find(|u| u.is_admin)
}

fn sum_positives(xs: &[i32]) -> i32 {
    xs.iter().filter(|x| **x > 0).sum()
}

struct User { is_admin: bool }
```

**Rationale**: Iterator chains are lazy (allocations only in the final `collect`), compose into the rest of the ecosystem, and the compiler inlines them to loops as tight as hand-written code. When a loop contains side effects across many branches, imperative form may still be clearer — pick the form that communicates intent.

**See also**: 08-performance.md (zero-cost abstractions)

---

## ID-42: Type Aliases for Unwieldy Types

**Strength**: CONSIDER

**Summary**: Introduce a `type` alias when a compound type repeats, but remember aliases are transparent — they don't create a new type (use a newtype for that, see TD-03).

```rust
// ❌ REPETITIVE
fn register(
    cb: Box<dyn Fn(&str) -> Result<Vec<u8>, Box<dyn std::error::Error + Send + Sync>> + Send + Sync>,
) { /* ... */ }

// ✅ CLEARER
type BoxError = Box<dyn std::error::Error + Send + Sync>;
type ProcessResult = Result<Vec<u8>, BoxError>;
type ProcessCallback = Box<dyn Fn(&str) -> ProcessResult + Send + Sync>;

fn register(cb: ProcessCallback) { /* ... */ }

// ⚠️ Aliases are transparent — they do NOT prevent mixing
type UserId = u64;
type OrderId = u64;

fn get_user(id: UserId) {}
// let oid: OrderId = 1;
// get_user(oid);    // ← compiles! UserId and OrderId are both u64

// Use a newtype when type distinction matters — see TD-03
```

**Rationale**: Type aliases give you domain vocabulary and shorten signatures, but they don't enforce anything. If you want to prevent mixing `UserId` and `OrderId`, reach for a newtype (TD-03).

**See also**: TD-03 (newtypes), TD-16 (hide implementation)

---

## ID-43: Handle Reserved-Word Collisions with Raw Identifiers

**Strength**: MUST

**Summary**: When you need an identifier that collides with a Rust keyword, use a raw identifier `r#keyword` or a trailing underscore `keyword_`. Never misspell.

```rust
// ✅ GOOD: raw identifier preserves the intended name
let r#type = "keyword";
fn r#match(input: &str) -> bool { !input.is_empty() }

struct Config {
    r#type: String,          // field named "type"
    r#mod: bool,             // field named "mod"
}

// ✅ ALSO ACCEPTABLE: trailing underscore
let type_ = "keyword";
fn match_(input: &str) -> bool { !input.is_empty() }

// ❌ BAD: misspelling harms searchability
let typ = "keyword";         // don't
let krate = "my-crate";      // don't — the real word is "crate"
fn mtch(input: &str) -> bool { false } // don't
```

**Rationale**: Misspelled identifiers can't be found with a straightforward grep for the real word, and they signal "I worked around a compiler restriction" rather than "I'm naming this thing precisely." Raw identifiers are purpose-built for this; the trailing underscore is the conventional fallback.

---

## ID-44: Follow `rustfmt` — 4 Spaces, 100 Columns, Trailing Commas

**Strength**: MUST

**Summary**: Use `rustfmt` defaults: 4 spaces (never tabs), 100-column line width, block indent, trailing commas on multi-line comma-separated lists, at most one blank line between items.

```rust
// ✅ GOOD: block indent, trailing comma on multi-line
fn register(
    name: &str,
    handler: Box<dyn Fn(&str) + Send>,
    timeout: std::time::Duration,
) -> Result<(), RegisterError> {
    // 4-space indent, 100-col max
    Ok(())
}

let array = [
    first_element,
    second_element,
    third_element,
];

// ❌ BAD: visual indent aligns to the delimiter
fn register(name: &str,
            handler: Box<dyn Fn(&str) + Send>,
            timeout: std::time::Duration)
           -> Result<(), RegisterError> {
    Ok(())
}

struct RegisterError;
const first_element: i32 = 1;
const second_element: i32 = 2;
const third_element: i32 = 3;
```

```text
// Rule of thumb for the breaks
// - one-line fits in 100 cols → keep on one line, no trailing comma
// - doesn't fit → break after (, each element block-indented 4 spaces,
//   closing delimiter on its own line at the parent's indent,
//   trailing comma on the last element
```

**Rationale**: Block indent produces smaller diffs — renaming `register` doesn't reindent every argument. Trailing commas on multi-line lists mean adding or removing items touches exactly one line. These are `rustfmt`'s defaults; the entire ecosystem has settled on them.

**See also**: 10-tooling.md (`rustfmt` configuration)

---

## ID-45: Sort and Group Imports

**Strength**: SHOULD

**Summary**: Split imports into groups (stdlib, external crates, current crate), version-sort within each group, and let `rustfmt` handle the layout. Prefer nested `use` over many parallel `use` lines.

```rust
// ✅ GOOD: grouped, version-sorted, nested where it shortens
use std::collections::{BTreeMap, HashMap};
use std::io::{self, Read, Write};
use std::path::PathBuf;

use serde::{Deserialize, Serialize};
use tokio::sync::mpsc;

use crate::error::Error;
use crate::model::{Order, OrderId, User, UserId};

// ❌ BAD: ungrouped, unsorted, no nesting
use crate::model::User;
use std::io::Read;
use serde::Serialize;
use std::collections::HashMap;
use crate::model::Order;
use std::io::Write;
use crate::error::Error;
use serde::Deserialize;
```

**Rationale**: Grouped imports make dependencies at a glance: stdlib usage, third-party crates, and the current crate's own modules. Nesting (`io::{self, Read, Write}`) compresses related imports from the same path into one line. `rustfmt` with `group_imports = "StdExternalCrate"` enforces this automatically.

**See also**: ID-44, 10-tooling.md

---

## ID-46: Attribute Placement and Derive Combining

**Strength**: SHOULD

**Summary**: Put each attribute on its own line above the item it decorates, with doc comments before attributes. Combine multiple `derive` attributes into a single `#[derive(...)]`.

```rust
// ✅ GOOD
/// A user record.
///
/// Values are validated on construction.
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
#[non_exhaustive]
#[repr(C)]
pub struct User {
    pub id: u64,
    pub name: String,
}

// Inner attributes go at the top of the item they apply to
pub mod net {
    #![allow(dead_code)]
    // ...
}

// ❌ BAD: multiple derives instead of one
#[derive(Debug)]
#[derive(Clone)]
#[derive(PartialEq)]
pub struct User2 { pub id: u64 }

// ❌ BAD: attribute and item on one line
#[derive(Debug)] pub struct User3 { pub id: u64 }
```

**Rationale**: Each attribute on its own line makes diffs clean — adding or removing one trait from a derive is a one-line change. Combining derives into one `#[derive(...)]` is the standard style; tooling (including `rustfmt`) assumes it.

**See also**: ID-44, TD-14 (common derives)

---

## ID-47: Prefer `#[expect(...)]` Over `#[allow(...)]`

**Strength**: SHOULD

**Summary**: When overriding a lint in a specific location, use `#[expect(lint, reason = "...")]`. It produces a warning if the lint *doesn't* fire, so stale suppressions surface instead of accumulating.

```rust
// ❌ BAD: silent forever, even after the underlying issue is fixed
#[allow(clippy::unused_async)]
pub async fn handler(req: Request) -> Response {
    process(req)
}

// ✅ GOOD: warns if the lint stops firing
#[expect(
    clippy::unused_async,
    reason = "handler trait requires async, I/O will be added soon",
)]
pub async fn handler2(req: Request) -> Response {
    process(req)
}

// ✅ `#[allow]` still has its place: generated code and macro expansions
// where the lint cannot be reliably predicted per-call.
#[allow(dead_code)]
mod generated { /* macro output */ }

struct Request;
struct Response;
fn process(_: Request) -> Response { Response }
```

**Rationale**: `#[allow]` is write-only — once added, it's invisible forever. `#[expect]` turns that around: the compiler warns you when the suppression is no longer needed, so lint-debt doesn't accumulate.

**See also**: M-LINT-OVERRIDE-EXPECT, 10-tooling.md

---

## ID-48: Prefer Expression-Oriented Style

**Strength**: SHOULD

**Summary**: `if`, `match`, `loop`, and blocks are expressions in Rust — use them to initialize bindings directly instead of declaring uninitialized `let` and assigning in branches.

```rust
// ❌ IMPERATIVE: uninit let + branch assignment
let x;
if condition() {
    x = 1;
} else {
    x = 0;
}

// ✅ EXPRESSION: if as a value
let x = if condition() { 1 } else { 0 };

// match as an initializer
let kind = match parse_kind(&input) {
    Some(k) => k,
    None => Kind::Default,
};

// loop returns its `break` value
let first_match = loop {
    if let Some(c) = iter.next() {
        if c.is_alphabetic() { break Some(c); }
    } else {
        break None;
    }
};

// Block as an initializer — the last expression is the value
let scaled = {
    let base = measure();
    base * 2 + 1
};

fn condition() -> bool { true }
enum Kind { Default }
fn parse_kind(_: &str) -> Option<Kind> { None }
fn measure() -> i32 { 10 }
let input = String::new();
let mut iter = "abc".chars();
```

**Rationale**: Expression-oriented code eliminates a class of bugs (uninit reads, missing else branches) and makes control flow visible in a single scan. Reach for imperative form only when the body has substantial statements on both branches.

---


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| ID-02 `mem::take` / `mem::replace` | SHOULD | Move out of `&mut` without cloning |
| ID-04 `as_` / `to_` / `into_` naming | MUST | Prefix signals cost and ownership |
| ID-05 Document magic values | MUST | Explain why, not just what |
| ID-06 Avoid weasel words | MUST | `Bookings`, not `BookingService` |
| ID-07 Casing follows RFC 430 | MUST | `UpperCamelCase`, `snake_case`, `SCREAMING_SNAKE_CASE` |
| ID-08 Owned collections in fields | CONSIDER | Trade a heap slot for no lifetimes |
| ID-10 `new` and `Default` | SHOULD | Standard construction entry points |
| ID-13 Bugs panic, errors return | MUST | Contract violation vs. recoverable failure |
| ID-15 Feature names without `use-` / `with-` | MUST | Name features after what they enable |
| ID-18 RAII finalization | MUST | Cleanup in `Drop`, not on every exit path |
| ID-20 Field-named getters | MUST | Drop `get_`, use `_mut` suffix |
| ID-22 Iterate over `Option` | CONSIDER | Zero-or-one element iterator |
| ID-23 `iter` / `iter_mut` / `into_iter` | MUST | Standard collection iterator triplet |
| ID-24 Iterator type names | SHOULD | `Iter`, `IterMut`, `IntoIter` |
| ID-25 Consistent word order | SHOULD | `ParseBoolError` / `ParseIntError` |
| ID-26 Enums over `Box<dyn>` for closed sets | CONSIDER | Static dispatch, stack allocation |
| ID-27 `Option` / `Result` combinators | SHOULD | `?`, `map`, `and_then` over `match` |
| ID-28 Panic means stop | MUST | Don't catch for control flow |
| ID-29 Closure capture via block rebinding | SHOULD | Keep prep local to the closure |
| ID-30 `Option` over sentinels | MUST | Absence belongs in the type |
| ID-31 Free fn over associated fn | SHOULD | Associated fn = belongs to the type |
| ID-33 Return consumed args on error | CONSIDER | Enables retry without pre-cloning |
| ID-34 `format!` for string building | SHOULD | Readable, handles `Display`/`Debug` |
| ID-35 Temporary mutability | SHOULD | Scope mutation to setup only |
| ID-38 `let ... else` | SHOULD | Destructure + early return, flat happy path |
| ID-39 Borrowed types for arguments | MUST | `&str`, `&[T]`, `&T` |
| ID-41 Iterator chains over loops | SHOULD | Functional pipeline, lazy, inlined |
| ID-42 Type aliases for complex types | CONSIDER | Aliases are transparent, not newtypes |
| ID-43 Raw identifiers for keyword collisions | MUST | `r#type`, not `typ` |
| ID-44 `rustfmt` defaults | MUST | 4 spaces, 100 cols, trailing commas |
| ID-45 Sort and group imports | SHOULD | stdlib / external / crate, version-sorted |
| ID-46 Attribute placement and derive combining | SHOULD | One attribute per line, one `derive` |
| ID-47 `#[expect]` over `#[allow]` | SHOULD | Stale suppressions surface automatically |
| ID-48 Expression-oriented style | SHOULD | `if`, `match`, `loop`, block return values |


## Related Guidelines

- **API Design**: See `02-api-design.md` for argument conventions, return types, and public-surface shaping.
- **Error Handling**: See `03-error-handling.md` for how `Result`, `?`, and error-type design expand on ID-13, ID-27, ID-28, ID-33.
- **Type Design**: See `05-type-design.md` for newtypes, enums-as-state-machines, `#[non_exhaustive]`, and the `Debug`/`Display`/`Default` conventions that back ID-10.
- **Traits**: See `06-traits.md` for object safety and the trait-design story behind ID-26.
- **Anti-patterns**: See `11-anti-patterns.md` for `clone()`-to-satisfy-borrow-checker, deref polymorphism, and other mistakes related to ID-02 and ID-39.


## External References

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/)
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
- [RFC 430 — Naming Conventions](https://github.com/rust-lang/rfcs/blob/master/text/0430-finalizing-naming-conventions.md)
- [Clippy Lint Index](https://rust-lang.github.io/rust-clippy/master/)
- Pragmatic Rust Guidelines: M-CONCISE-NAMES, M-DOCUMENTED-MAGIC, M-PANIC-IS-STOP, M-PANIC-ON-BUG, M-REGULAR-FN, M-LINT-OVERRIDE-EXPECT, M-STATIC-VERIFICATION, M-UPSTREAM-GUIDELINES
- Rust API Guidelines checklist items: C-CASE, C-CONV, C-GETTER, C-ITER, C-CTOR, C-COMMON-TRAITS, C-FEATURE
