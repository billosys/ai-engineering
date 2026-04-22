# Type Design Guidelines

Patterns for designing Rust types: leveraging the type system to prevent bugs, encode invariants at compile time, and express domain intent. Covers foundational decisions (newtype vs primitive, struct vs tuple, enum vs flag), construction patterns (builder, typestate), trait design for types (`Debug`, `Display`, common traits), and low-level type-system tools (`PhantomData`, variance, `repr`, DSTs, `Pin`, `!Unpin`).


## TD-01: Arguments Use Types, Not Bool or Option

**Strength**: SHOULD

**Summary**: Prefer named enums over `bool`, `Option`, or positional primitives for public API parameters.

```rust
// ❌ BAD: unclear bool arguments
let widget = Widget::new(true, false);
// What do true and false mean? Must check the docs.

// ✅ GOOD: explicit enum types
pub enum Size { Small, Medium, Large }
pub enum Shape { Round, Square }

let widget = Widget::new(Size::Small, Shape::Round);

// ❌ BAD: Option<bool> is ambiguous
fn configure(enable_caching: Option<bool>) { /* three states, unclear meaning */ }

// ✅ GOOD: three-state enum
pub enum CacheMode { Enabled, Disabled, Default }
fn configure(cache_mode: CacheMode) { /* ... */ }
```

```rust
// OK — meaning is obvious at the call site
fn set_visible(visible: bool) { }
fn is_empty() -> bool { /* ... */ true }
```

**Rationale**: Named enums are self-documenting, resist wrong-order argument bugs, and let the compiler check exhaustiveness. Use `bool` only when the word "true" reads unambiguously at the call site.

**See also**: C-CUSTOM-TYPE, TD-24

---

## TD-02: Use Strong Types Instead of Primitives

**Strength**: SHOULD

**Summary**: Prefer the most specific standard-library type available (`Duration`, `PathBuf`, `NonZeroU32`, `Instant`) and wrap domain values in newtypes.

```rust
use std::path::PathBuf;
use std::time::Duration;
use std::num::NonZeroU32;

// ❌ BAD: primitive obsession
pub struct Config {
    timeout_seconds: u64,
    max_retries: u32,
    config_file: String,
    user_id: u64,
    api_key: String,
}

// ✅ GOOD: strong, semantic types
pub struct Config {
    timeout: Duration,
    max_retries: NonZeroU32,
    config_file: PathBuf,
    user_id: UserId,
    api_key: ApiKey,
}

pub struct UserId(u64);
pub struct ApiKey(String);

impl ApiKey {
    pub fn new(key: String) -> Result<Self, InvalidApiKey> {
        if key.len() < 20 { return Err(InvalidApiKey); }
        Ok(Self(key))
    }
}
```

**Rationale**: Strong types prevent parameter-order bugs, catch unit-mismatch errors at compile time, and give you a single place to enforce validation. `Duration`, `PathBuf`, `Instant`, `SocketAddr`, and `NonZero*` are almost always correct where a raw integer or `String` would be ambiguous.

**See also**: M-STRONG-TYPES, C-NEWTYPE, TD-03

---

## TD-03: Newtypes for Semantic Distinctions and Invariants

**Strength**: SHOULD

**Summary**: Wrap primitives in a newtype whenever the value carries domain meaning, a unit, or a validity invariant. The wrapper is free at runtime, rigorous at compile time.

```rust
// Unit safety
pub struct Miles(f64);
pub struct Kilometers(f64);

impl Miles {
    pub fn to_km(self) -> Kilometers { Kilometers(self.0 * 1.60934) }
}

fn distance_ok(d: Miles) -> bool { d.0 > 100.0 }
// distance_ok(Kilometers(200.0));     // compile error
distance_ok(Kilometers(200.0).to_km_then_miles()); // must convert

// Distinct ID types
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct UserId(pub u64);
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct OrderId(pub u64);

fn get_user(id: UserId)   -> Option<User>  { /* ... */ None }
fn get_order(id: OrderId) -> Option<Order> { /* ... */ None }

// get_user(OrderId(1));                // compile error
get_user(UserId(1));                    // fine

// Validated constructor — construction is the only way to produce a value
pub struct NonEmptyString(String);

impl NonEmptyString {
    pub fn new(s: String) -> Result<Self, EmptyString> {
        if s.is_empty() { Err(EmptyString) } else { Ok(Self(s)) }
    }
    pub fn as_str(&self) -> &str { &self.0 }
}

fn process(name: NonEmptyString) {
    // No runtime check needed — the type enforces non-empty.
    println!("{}", name.as_str());
}
```

**Rationale**: One pattern covers unit safety, ID distinction, and validation-at-construction. Pair with `#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]` for ID types; `Copy` is appropriate when the inner type is `Copy` and equality is semantically by value. Don't forget to provide an accessor (`as_str`, `get`, `into_inner`) so consumers can extract the value when needed.

**See also**: C-NEWTYPE, TD-16 (use newtypes to hide implementation), TD-17 (PhantomData variants)

---

## TD-04: Prefer Structs Over Tuples for Named Data

**Strength**: SHOULD

**Summary**: Use named struct fields whenever the meaning of a position isn't self-evident.

```rust
// ❌ UNCLEAR
fn parse_point(s: &str) -> Option<(f64, f64, f64)> { /* ... */ None }
let p = parse_point("1,2,3")?;
println!("x={}, y={}, z={}", p.0, p.1, p.2);

// ✅ CLEAR
#[derive(Debug, Clone, Copy)]
struct Point3D { x: f64, y: f64, z: f64 }

fn parse_point(s: &str) -> Option<Point3D> { /* ... */ None }

// Tuples remain fine when order is canonical
fn min_max(xs: &[i32]) -> Option<(i32, i32)> { /* ... */ None }
```

**Rationale**: Named fields document themselves, tolerate field reordering, and make refactoring safer. Tuples are appropriate for short-lived returns where the ordering is universally understood (`(min, max)`, `(width, height)`, `(line, column)`).

---

## TD-05: Struct Fields Are Private by Default

**Strength**: MUST

**Summary**: Keep fields private unless the struct is an explicit plain-data record. Expose controlled access through methods.

```rust
pub struct User {
    id: UserId,
    name: String,
    email: String,
    created_at: std::time::Instant,
}

impl User {
    pub fn new(id: UserId, name: String, email: String) -> Self {
        Self { id, name, email, created_at: std::time::Instant::now() }
    }

    pub fn id(&self) -> UserId { self.id }
    pub fn name(&self) -> &str { &self.name }

    pub fn set_name(&mut self, name: String) -> Result<(), EmptyName> {
        if name.is_empty() { return Err(EmptyName); }
        self.name = name;
        Ok(())
    }
}

// Legitimate exceptions — passive data, config
#[derive(Debug, Clone, PartialEq)]
pub struct Point { pub x: f64, pub y: f64 }

pub struct ServerConfig { pub host: String, pub port: u16 }
```

**Rationale**: Private fields let the type evolve without breaking callers — adding validation, changing representation, or upholding invariants is compatible. Public fields lock the representation forever. Use public fields only for passive value objects (`Point`, `Rect`) or configuration structs where every field is a legitimate input.

**See also**: C-STRUCT-PRIVATE, TD-07 (`#[non_exhaustive]` for public-field structs)

---

## TD-06: Use Enums for State Machines

**Strength**: SHOULD

**Summary**: Model mutually exclusive states as enum variants so invalid state combinations become unrepresentable.

```rust
use std::net::TcpStream;

// ❌ BAD: boolean flags admit invalid combinations
struct Connection {
    is_connected: bool,
    is_authenticated: bool,
    socket: Option<TcpStream>,
    user: Option<User>,
}
// is_authenticated = true but socket = None? compiles fine, crashes at runtime.

// ✅ GOOD: each state owns exactly the data it needs
enum Connection {
    Disconnected,
    Connected { socket: TcpStream },
    Authenticated { socket: TcpStream, user: User },
}

impl Connection {
    fn authenticate(&mut self, creds: &Credentials) -> Result<(), AuthError> {
        let old = std::mem::replace(self, Connection::Disconnected);
        match old {
            Connection::Connected { socket } => {
                let user = perform_auth(&socket, creds)?;
                *self = Connection::Authenticated { socket, user };
                Ok(())
            }
            Connection::Disconnected => Err(AuthError::NotConnected),
            already @ Connection::Authenticated { .. } => {
                *self = already;
                Err(AuthError::AlreadyAuthenticated)
            }
        }
    }
}
```

**Rationale**: The compiler enforces exactly-one-state and checks exhaustive handling. Each variant carries only the fields it needs, removing `Option` noise. Consider the typestate pattern (TD-11) when state transitions must be checked at compile time rather than at runtime.

---

## TD-07: Use `#[non_exhaustive]` for Extensibility

**Strength**: SHOULD

**Summary**: Mark public enums and structs `#[non_exhaustive]` when you expect to add variants or fields in future versions.

```rust
#[non_exhaustive]
#[derive(Debug)]
pub enum DatabaseError {
    ConnectionFailed,
    QueryFailed,
    Timeout,
}

#[non_exhaustive]
#[derive(Debug)]
pub struct QueryResult {
    pub rows: Vec<Row>,
    pub affected: usize,
}
```

```rust
// Consumers must include a wildcard arm — adding variants is no longer breaking
match err {
    DatabaseError::ConnectionFailed => { /* ... */ }
    DatabaseError::QueryFailed      => { /* ... */ }
    DatabaseError::Timeout          => { /* ... */ }
    _ => { /* forward-compatible */ }
}

// For structs: consumers can't construct with a literal, only via your constructors
// let r = QueryResult { rows, affected };   // error outside the defining crate
```

**Rationale**: Adding an enum variant or struct field is a major-version breaking change by default. `#[non_exhaustive]` defers that cost: downstream match statements must carry a catch-all arm, and struct literals are forbidden across crate boundaries, so the type is free to grow. Apply it to error enums and public config structs you reasonably expect to extend.

---

## TD-08: Use `bitflags` for Flag Sets

**Strength**: SHOULD

**Summary**: For a set of orthogonal boolean options, use the `bitflags` crate rather than multiple `bool` parameters or a `Vec<Enum>`.

```rust
use bitflags::bitflags;

bitflags! {
    pub struct Permissions: u32 {
        const READ    = 0b0001;
        const WRITE   = 0b0010;
        const EXECUTE = 0b0100;
        const DELETE  = 0b1000;
    }
}

fn check(perms: Permissions) {
    if perms.contains(Permissions::READ)    { /* ... */ }
    if perms.contains(Permissions::WRITE)   { /* ... */ }
    if perms.intersects(Permissions::READ | Permissions::WRITE) { /* either */ }
}

let p = Permissions::READ | Permissions::WRITE;
check(p);
```

**Rationale**: `bitflags` gives you O(1) storage, natural `|` / `&` composition, and standard derive-friendly behavior. It is the de-facto Rust idiom for flag sets, including throughout the standard library and OS-binding crates.

**See also**: C-BITFLAG

---

## TD-09: Don't Duplicate Derived Trait Bounds on Structs

**Strength**: MUST

**Summary**: Put trait bounds on impls, not on type definitions — unless the bound is an invariant of the type itself.

```rust
// ✅ GOOD — no bounds on the definition
pub struct Container<T> {
    items: Vec<T>,
}

#[derive(Clone, Debug, PartialEq)]
pub struct Container<T> { items: Vec<T> }
// derive generates impls that add bounds only to the impl blocks

// ❌ BAD — bounds on the definition leak to every user
pub struct Container<T: Clone + Debug + PartialEq> {
    items: Vec<T>,
}
// Now `Container<RawPointer>` is impossible even if you never clone.

// ✅ Invariant-carrying bounds DO belong on the definition
pub struct Sorted<T: Ord> {
    items: Vec<T>,
}
// `T: Ord` is required for the type's sorted invariant to make sense.
```

**Rationale**: Bounds on `struct` definitions propagate into every function that mentions the type. A derive-driven bound is noise — `#[derive(Clone)]` already adds `T: Clone` to the `impl Clone` block. Put bounds on the type only when they express an invariant the type itself relies on (like `Sorted<T: Ord>`).

**See also**: C-STRUCT-BOUNDS

---

## TD-10: Builder Pattern for Complex Construction

**Strength**: SHOULD

**Summary**: When a type has many optional parameters, provide a builder; terminate with `build(self)` that consumes the builder and runs final validation.

```rust
use std::time::Duration;

pub struct Server { /* ... */ }

pub struct ServerBuilder {
    host: String,
    port: u16,
    max_connections: usize,
    timeout: Duration,
    tls: Option<TlsConfig>,
}

impl ServerBuilder {
    pub fn new(host: impl Into<String>, port: u16) -> Self {
        Self {
            host: host.into(), port,
            max_connections: 100,
            timeout: Duration::from_secs(30),
            tls: None,
        }
    }
    pub fn max_connections(mut self, n: usize) -> Self { self.max_connections = n; self }
    pub fn timeout(mut self, d: Duration)       -> Self { self.timeout = d; self }
    pub fn tls(mut self, cfg: TlsConfig)        -> Self { self.tls = Some(cfg); self }

    pub fn build(self) -> Result<Server, BuildError> {
        if self.timeout.is_zero() { return Err(BuildError::ZeroTimeout); }
        /* ... construct ... */
        Ok(Server { /* ... */ })
    }
}

// Consuming builder — `self` → `Self` — chains cleanly
let server = ServerBuilder::new("localhost", 8080)
    .max_connections(1000)
    .timeout(Duration::from_secs(60))
    .build()?;
```

**Rationale**: Builders isolate optional parameters from required ones, give every step a descriptive name at the call site, and centralize validation in `build`. Prefer consuming (`self` → `Self`) for chainable construction; use `&mut self` → `&mut Self` only when the builder itself needs to survive chaining (e.g., conditional configuration based on runtime state).

**See also**: C-BUILDER, TD-11 (typestate builders enforce order at compile time)

---

## TD-11: The Typestate Pattern

**Strength**: CONSIDER

**Summary**: Encode state as a generic type parameter so the compiler rejects invalid transitions without any runtime check.

```rust
use std::marker::PhantomData;

// Zero-sized state markers
pub struct Unlocked;
pub struct Locked;

pub struct Door<State> {
    id: u32,
    _state: PhantomData<State>,
}

impl Door<Unlocked> {
    pub fn open(&self)            { println!("door {} opens", self.id); }
    pub fn lock(self) -> Door<Locked> {
        Door { id: self.id, _state: PhantomData }
    }
}

impl Door<Locked> {
    // Note: no `open` — a locked door cannot be opened without unlocking first
    pub fn unlock(self) -> Door<Unlocked> {
        Door { id: self.id, _state: PhantomData }
    }
}

pub fn new_door(id: u32) -> Door<Unlocked> { Door { id, _state: PhantomData } }

let door = new_door(1);
door.open();
let door = door.lock();
// door.open();                // compile error: no `open` on Door<Locked>
let door = door.unlock();
door.open();                   // fine again
```

**Rationale**: State transitions become function signatures; illegal operations fail to compile. Zero runtime cost (the marker is `PhantomData<State>`). Use this for session-type APIs, builder flows with required-before-optional steps, and any FSM where wrong-state calls are a common bug.

**See also**: TD-17 (`PhantomData`), TD-19 (ZSTs)

---

## TD-12: Public Types Implement `Debug`

**Strength**: MUST

**Summary**: Every public type must implement `Debug`. For types carrying secrets, implement `Debug` manually and redact sensitive fields.

```rust
use std::fmt::{self, Debug, Formatter};

// Most types: derive
#[derive(Debug)]
pub struct Endpoint { url: String, timeout: std::time::Duration }

// Secret-bearing types: custom impl
pub struct UserCredentials {
    username: String,
    password: String,
    api_key: String,
}

impl Debug for UserCredentials {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        f.debug_struct("UserCredentials")
            .field("username",  &self.username)
            .field("password",  &"<redacted>")
            .field("api_key",   &"<redacted>")
            .finish()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn secrets_never_leak() {
        let c = UserCredentials {
            username: "alice".into(),
            password: "hunter2".into(),
            api_key:  "sk-abc".into(),
        };
        let out = format!("{:?}", c);
        assert!(!out.contains("hunter2"));
        assert!(!out.contains("sk-abc"));
    }
}
```

**Rationale**: `Debug` is assumed available for logging, assertions (`assert_eq!`), error reporting, and derive-chains. Skipping it silently degrades library ergonomics. When fields are sensitive, the manual impl must be paired with a unit test that proves the secret isn't rendered.

**See also**: M-PUBLIC-DEBUG

---

## TD-13: Readable Types Implement `Display`

**Strength**: MUST

**Summary**: Implement `Display` for types meant to be read by end users or developers. Error types must implement it (required by `std::error::Error`).

```rust
use std::fmt::{self, Display, Formatter};

pub struct UserId(u64);
impl Display for UserId {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "user:{}", self.0)
    }
}

#[derive(Debug)]
pub struct ValidationError { field: String, message: String }

impl Display for ValidationError {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "validation failed for '{}': {}", self.field, self.message)
    }
}

impl std::error::Error for ValidationError {}
```

**Rationale**: `Debug` is for programmers; `Display` is the user-facing rendering. Error types in particular need a clean, one-line message free of `Debug`'s structural noise. Do not duplicate information between `Debug` and `Display` — keep `Debug` structural, `Display` prose.

**See also**: M-PUBLIC-DISPLAY, EH-guide (error types and `std::error::Error`)

---

## TD-14: Eagerly Implement Common Traits

**Strength**: SHOULD

**Summary**: Derive `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash`, `Default`, `PartialOrd`, `Ord` whenever they are semantically appropriate.

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct UserId(u64);

#[derive(Debug, Clone, Default)]
pub struct Config {
    timeout: Option<std::time::Duration>,
    retries: Option<u32>,
}

// Manual for non-derivable cases (float comparison, custom ordering)
#[derive(Debug, Clone, Copy)]
pub struct Temperature(f64);
impl PartialEq for Temperature {
    fn eq(&self, other: &Self) -> bool { self.0 == other.0 }
}
impl PartialOrd for Temperature {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.0.partial_cmp(&other.0)
    }
}
```

**Rationale**: A `UserId` that isn't `Hash` can't be a `HashMap` key. A `Config` without `Default` forces consumers to name every field. Standard-trait availability is what lets generic code and std-lib collections work with your type.

**See also**: C-COMMON-TRAITS

---

## TD-15: Associated Types vs Generic Parameters

**Strength**: SHOULD

**Summary**: Use an associated type when each implementor has exactly one canonical choice. Use a generic parameter when many implementations per type make sense.

```rust
// ✅ Associated type — each iterator has one Item
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}

// ✅ Generic parameter — String can be From<&str>, From<char>, From<Vec<u8>>...
pub trait From<T> {
    fn from(value: T) -> Self;
}
```

**Rationale**: Associated types are simpler at the call site (no turbofish, no redundant bounds) and reflect a functional dependency. Generic parameters are the right fit when multiple, independently valid implementations are expected.

**See also**: TR-guide (trait design)

---

## TD-16: Newtypes Hide Implementation Details

**Strength**: SHOULD

**Summary**: Wrap complex return types in a named struct so your public API doesn't leak implementation.

```rust
use std::iter::{Enumerate, Skip};

// ❌ BAD: exposes Enumerate<Skip<I>> — can't change implementation
pub fn transform_leaky<I: Iterator>(input: I) -> Enumerate<Skip<I>> {
    input.skip(3).enumerate()
}

// ✅ GOOD: newtype wraps the iterator chain
pub struct Transform<I>(Enumerate<Skip<I>>);

impl<I: Iterator> Iterator for Transform<I> {
    type Item = (usize, I::Item);
    fn next(&mut self) -> Option<Self::Item> { self.0.next() }
}

pub fn transform<I: Iterator>(input: I) -> Transform<I> {
    Transform(input.skip(3).enumerate())
}

// ✅ Also good: `impl Trait` when the type need not be named
pub fn transform_opaque<I: Iterator>(input: I)
    -> impl Iterator<Item = (usize, I::Item)>
{
    input.skip(3).enumerate()
}
```

**Rationale**: Exposing `Enumerate<Skip<I>>` locks you in — changing the implementation is a breaking change, and consumers see noise in rustdoc. A named newtype keeps the public surface stable; `impl Trait` is even more opaque when you don't need to name the return type.

**See also**: C-NEWTYPE-HIDE, API guide (return opaque wrappers for iterators)

---

## TD-17: `PhantomData` Tracks Ownership, Variance, and Lifetimes

**Strength**: SHOULD

**Summary**: Use `PhantomData<T>` when a type logically owns or references `T` but has no real field of that type — required for raw-pointer wrappers, type-level tags, and lifetime-parameterized types.

```rust
use std::marker::PhantomData;

// Ownership-semantic: wrapper that logically owns a T
pub struct MyBox<T> {
    ptr: *mut T,
    _owned: PhantomData<T>,    // tells dropck `T` may be dropped
}

// Lifetime tracking in a raw-pointer iterator (stdlib's real slice::Iter shape)
pub struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
    _marker: PhantomData<&'a T>,   // covariant in 'a and T
}

// Type-level tag: distinct types sharing one representation
pub struct Id<T> { id: u64, _tag: PhantomData<fn() -> T> }

struct User;
struct Order;

type UserId  = Id<User>;
type OrderId = Id<Order>;
// fn(T) -> T marker makes the tag invariant — exchange-proof
```

**Rationale**: Without `PhantomData`, the compiler treats unused type parameters as errors ("parameter is never used") and cannot infer correct variance or drop-check behavior. `PhantomData<&'a T>` establishes covariance in `'a`; `PhantomData<fn(T) -> T>` establishes invariance (useful for type tags that should not be exchanged); `PhantomData<T>` declares logical ownership (affects dropck). Choose the form that matches the semantics you want.

**See also**: TD-18 (variance), nomicon §3 "Data Representation"

---

## TD-18: Choose Variance Deliberately

**Strength**: CONSIDER

**Summary**: If a type is generic over another type or lifetime, understand whether it should be covariant, contravariant, or invariant — the wrong choice breaks soundness or usability.

| PhantomData marker | Variance in T | When to use |
|--------------------|---------------|-------------|
| `PhantomData<T>` | covariant | owns a T, standard wrapper |
| `PhantomData<&'a T>` | covariant in T and `'a` | shared-reference semantics |
| `PhantomData<&'a mut T>` | invariant in T, covariant in `'a` | mutable-reference semantics |
| `PhantomData<fn(T)>` | contravariant in T | function-argument semantics |
| `PhantomData<fn() -> T>` | covariant in T | function-return semantics |
| `PhantomData<fn(T) -> T>` | invariant in T | type tag that must not be exchanged |
| `PhantomData<*mut T>` | invariant in T | interior mutability through raw pointer |

```rust
use std::marker::PhantomData;

// Covariant: &'a Cat is a subtype of &'a Animal
struct Covariant<'a, T> { _t: PhantomData<&'a T> }

// Invariant: a type tag must not admit subtype substitution
struct Tag<T> { _t: PhantomData<fn(T) -> T> }
```

**Rationale**: Rust's variance rules propagate automatically through normal fields, but `PhantomData` is the knob for raw pointers and type-level programming. Incorrect variance either rejects valid code (overly invariant wrapper) or compiles unsound APIs (covariant when invariance is required). When in doubt, default to invariance — `PhantomData<fn(T) -> T>` is almost always safe.

**See also**: TD-17, The Rustonomicon §3.8 "PhantomData" and §3.10 "Subtyping and Variance"

---

## TD-19: Zero-Sized Types for Tokens and Type-Level State

**Strength**: CONSIDER

**Summary**: Types with no fields occupy no memory; use them as capability tokens, type-level tags, and generic parameters that express intent without runtime cost.

```rust
use std::marker::PhantomData;

// Unit tags as type parameters — no runtime cost
pub struct Meters;
pub struct Feet;

pub struct Distance<Unit> {
    value: f64,
    _unit: PhantomData<Unit>,
}

impl Distance<Meters> {
    pub fn new(value: f64) -> Self { Self { value, _unit: PhantomData } }
    pub fn to_feet(self) -> Distance<Feet> {
        Distance { value: self.value * 3.281, _unit: PhantomData }
    }
}
// size_of::<Distance<Meters>>() == size_of::<f64>()

// Capability token — construction is proof of authorization
pub struct AdminToken(());     // private field blocks construction

pub fn issue_admin_token(auth: &Auth) -> Option<AdminToken> {
    if auth.is_admin() { Some(AdminToken(())) } else { None }
}

pub fn delete_everything(_proof: AdminToken) {
    // the caller must have proven admin status to reach here
}
```

**Rationale**: A ZST is a statement that carries no data but constrains what the type system will accept. This is how APIs like `std::marker::Send`, custom phantom tags, and capability tokens encode requirements with zero overhead.

**See also**: TD-11 (typestate), TD-17 (`PhantomData`)

---

## TD-20: Use `NonZero*` and Niche Types for Memory Efficiency

**Strength**: CONSIDER

**Summary**: Replace integers that cannot be zero with `std::num::NonZero*`; the compiler then folds `Option<NonZeroU32>` into the same size as `u32`.

```rust
use std::num::{NonZeroU32, NonZeroUsize};

pub struct RetryCount(NonZeroU32);       // zero retries is not a valid state

pub fn index_of(haystack: &str, needle: char) -> Option<NonZeroUsize> {
    haystack.find(needle).and_then(NonZeroUsize::new)
}

// `Option<NonZeroU32>` is 4 bytes — the zero bit pattern encodes `None`.
// `Option<u32>` is 8 bytes — separate discriminant byte + padding.
```

**Rationale**: Niche optimization lets `Option<T>` reuse an unused bit pattern in `T` as the `None` discriminant. `NonZeroU32`, `&T`, `Box<T>`, and `NonNull<T>` all have such niches. Prefer these types whenever the invariant holds — you get compiler-checked non-zero semantics plus smaller memory footprint for containers of `Option`s.

**See also**: PF-guide (performance book on type size), nomicon §3.2 "Exotic Sizes"

---

## TD-21: Choose `repr` Deliberately for Layout-Sensitive Types

**Strength**: CONSIDER

**Summary**: For types that cross FFI boundaries, appear in raw byte streams, or need predictable layout, set `#[repr(...)]` explicitly instead of trusting Rust's default (unspecified) layout.

```rust
// ✅ FFI-compatible struct layout
#[repr(C)]
pub struct Header {
    pub magic: u32,
    pub version: u16,
    pub flags: u16,
}

// ✅ Transparent wrapper — same ABI and layout as the inner type
#[repr(transparent)]
pub struct Millimeters(pub f32);

// ✅ Sized discriminant, FFI-safe enum
#[repr(u8)]
pub enum Opcode { Nop = 0x00, Ret = 0x01, Jmp = 0x02 }

// ⚠️ Packed — no padding, but misaligned field access; rarely needed outside FFI
#[repr(C, packed)]
pub struct Wire { kind: u8, value: u32 }

// ✅ Aligned — stronger alignment than default
#[repr(align(64))]
pub struct CacheLine(pub [u8; 64]);
```

**Rationale**: The default Rust layout is unspecified and may change between compiler versions. `#[repr(C)]` gives you C-equivalent layout for FFI; `#[repr(transparent)]` lets a newtype inherit the inner type's ABI exactly (critical for `NonNull<T>` / `Option<NonNull<T>>` niche optimization to carry across the wrapper); `#[repr(packed)]` removes padding at the cost of unaligned access (take references carefully — `&packed_field` is often unsound).

**See also**: Nomicon §3.3–3.5 "alternative representations", US-guide (unsafe + FFI)

---

## TD-22: Handle DSTs and `?Sized` Bounds Explicitly

**Strength**: CONSIDER

**Summary**: Most generic parameters are implicitly `Sized`. For APIs that should accept slices, strings, or trait objects, relax with `?Sized`.

```rust
use std::fmt::Display;

// `T: Sized` is implicit — this function only accepts sized T
pub fn log_sized<T: Display>(v: &T) {
    println!("{v}");
}

// `?Sized` opts out — accepts &str, [u8], dyn Display, etc.
pub fn log_any<T: ?Sized + Display>(v: &T) {
    println!("{v}");
}

// Works because &str, str, and [T] are DSTs carrying length in the wide pointer
log_any("hello");                 // &str (T = str, DST)
log_any(&42_u32);                 // &u32 (T = u32, sized)
log_any(&*format!("world"));      // &str slice of an owned String
```

**Rationale**: Rust's `Sized` bound is implicit on every generic parameter so that `T` can be stored, copied, or passed by value. That default disallows `str`, `[T]`, and `dyn Trait`. When your function only ever touches `&T`, `Box<T>`, or `Rc<T>`, add `?Sized` to accept slices and trait objects without forcing consumers to wrap them.

**See also**: Nomicon §3.6 "Dynamically Sized Types"

---

## TD-23: Use `Pin<Ptr<T>>` for Address-Sensitive Types

**Strength**: CONSIDER

**Summary**: When a type relies on its address staying fixed (self-references, intrusive linked lists, hand-rolled futures), require pinned access in its API.

```rust
use std::pin::Pin;

pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut std::task::Context<'_>)
        -> std::task::Poll<Self::Output>;
}

// Callers produce a Pin by heap-allocating or using `pin!`
let fut = async { 42 };
let mut fut = Box::pin(fut);        // Pin<Box<impl Future>>
// or, on the stack:
// let mut fut = std::pin::pin!(fut); // Pin<&mut impl Future>
```

**Rationale**: `Pin<P>` is a wrapper that promises the pointee will not move before being dropped (as long as the pointee is `!Unpin`). The poll signature `self: Pin<&mut Self>` is the convention that tells callers "you must pin this value before polling." Use this when your type contains self-references or hands out pointers to its own fields.

**See also**: TD-24, TD-25, CA-guide (async and Pin), `std::pin` documentation

---

## TD-24: Mark Address-Sensitive Types with `PhantomPinned`

**Strength**: SHOULD

**Summary**: Include `std::marker::PhantomPinned` as a field to make a type `!Unpin`, signalling to the compiler and to users that it requires pinning.

```rust
use std::marker::PhantomPinned;
use std::pin::Pin;

pub struct Intrusive {
    data: String,
    ptr_into_data: *const u8,
    _pin: PhantomPinned,          // !Unpin — must stay put
}

impl Intrusive {
    // Construct boxed + pinned, then initialize the self-pointer with unsafe
    pub fn new(data: String) -> Pin<Box<Self>> {
        let mut boxed = Box::pin(Self {
            data, ptr_into_data: std::ptr::null(), _pin: PhantomPinned,
        });
        // SAFETY: we will not move the box; `data` is stable behind the Pin.
        unsafe {
            let mut_ref: Pin<&mut Self> = boxed.as_mut();
            let this = Pin::get_unchecked_mut(mut_ref);
            this.ptr_into_data = this.data.as_ptr();
        }
        boxed
    }
}
```

**Rationale**: `Unpin` is an auto-trait — types become `!Unpin` only when they contain a `!Unpin` field. `PhantomPinned` is the stable-Rust knob for this. Without it, `Pin<&mut T>` silently degrades to `&mut T` and your self-reference invariant can be moved away from under you.

**See also**: TD-23, TD-25, Async Reference §2 "Pinning"

---

## TD-25: Avoid Self-Referential Types in Safe Code

**Strength**: AVOID

**Summary**: Don't hand-roll self-referential types. Reach for `Rc`/`Arc`, `Weak`, `ouroboros`, `yoke`, or refactor the data flow instead.

```rust
// ❌ Impossible to write safely — there is no 'self lifetime
struct Bad {
    field: String,
    r: &'self str,      // no such thing in Rust
}

// ✅ Usual fixes
use std::rc::Rc;

// 1. Separate the data and the pointer into two owners
pub struct Ok1 {
    data: Rc<String>,
    // consumers get Rc<String> — no internal pointer needed
}

// 2. Store indices, not references
pub struct Ok2 {
    chunks: Vec<String>,
    current: usize,     // index into chunks — survives moves
}

// 3. Use a helper crate when the internal pointer is unavoidable
// See the `ouroboros` or `self_cell` crates for safe abstractions.
```

**Rationale**: Rust's move semantics make raw self-references fundamentally unsound — moving the struct invalidates the internal pointer without the borrow checker noticing. `Pin` lets libraries implement this carefully with `unsafe`, but application code almost always has a cleaner alternative: `Rc`/`Arc`, indices, or a dedicated crate. If you genuinely need it, see TD-23 / TD-24.

**See also**: TD-23, TD-24

---

## TD-26: Sealed Traits Control Implementation Surface

**Strength**: CONSIDER

**Summary**: When a trait is for use by downstream crates but implementation must stay internal, seal it with a private supertrait.

```rust
mod private {
    pub trait Sealed {}
}

pub trait Protocol: private::Sealed {
    fn handshake(&self);
}

// Internal types implement both the sealed marker and the public trait
pub struct Http;
impl private::Sealed for Http {}
impl Protocol for Http {
    fn handshake(&self) { /* ... */ }
}

pub struct Grpc;
impl private::Sealed for Grpc {}
impl Protocol for Grpc {
    fn handshake(&self) { /* ... */ }
}

// Downstream crates can call Protocol methods but cannot `impl Protocol for MyType {}`
// because they cannot implement `private::Sealed`.
```

**Rationale**: Sealed traits give you the option to add required methods to the trait later without a major-version bump — only your own implementors need updating. They are the right choice when a trait enumerates a closed set of types (protocols, wire formats, supported primitives).

**See also**: TR-guide (trait design), API-guidelines C-SEALED

---

## TD-27: Design Traits for Object Safety When Useful

**Strength**: SHOULD

**Summary**: If a trait is likely to be used as `&dyn Trait` or `Box<dyn Trait>`, design it to be object-safe; gate generic methods behind `where Self: Sized`.

```rust
pub trait Draw {
    fn draw(&self, canvas: &mut Canvas);
    fn bounds(&self) -> Rect;
}
// Usable as `Box<dyn Draw>`

let shapes: Vec<Box<dyn Draw>> = vec![
    Box::new(Circle { radius: 10.0 }),
    Box::new(Rectangle { width: 20.0, height: 15.0 }),
];
for shape in &shapes { shape.draw(&mut canvas); }

// Mixed: object-safe core + generic extension
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;          // object-safe

    fn map<B, F>(self, f: F) -> Map<Self, F>
    where
        Self: Sized,                                    // excluded from trait object
        F: FnMut(Self::Item) -> B,
    { /* ... */ todo!() }
}
```

**Rationale**: Object safety enables runtime polymorphism (`Box<dyn Trait>`), which in turn enables heterogeneous collections and dynamic dispatch. The cost is banning generic methods, `Self`-returning methods (other than receiver), and `Sized` methods — gate those behind `where Self: Sized` so they remain available on concrete types.

**See also**: C-OBJECT, TR-guide


## Type Design Checklist

When creating a new public type, walk this list:

```rust
// 1. Representation — primitive, newtype, struct, enum?
pub struct UserId(u64);

// 2. Common traits — which are semantically appropriate?
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]

// 3. Validation — does construction guarantee an invariant?
impl UserId {
    pub fn new(id: u64) -> Result<Self, InvalidId> { /* ... */ Ok(Self(id)) }
}

// 4. Display — is this user-facing?
impl std::fmt::Display for UserId { /* ... */ }

// 5. Accessors — how do consumers extract the value?
impl UserId { pub fn get(&self) -> u64 { self.0 } }

// 6. Copy vs Clone — trivial-to-duplicate or not?
// Copy if small, no heap, no Drop. Clone if any of those.

// 7. Default — is there a sensible default?
impl Default for Config { fn default() -> Self { /* ... */ todo!() } }

// 8. Extensibility — #[non_exhaustive] on enums and config structs?

// 9. Layout — does this cross FFI? Do I need #[repr(C)] or #[repr(transparent)]?

// 10. Address stability — is this self-referential? (If yes, see TD-23/24/25.)
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| TD-01 Arguments use types, not bool/Option | SHOULD | Named enums over positional bool |
| TD-02 Strong types over primitives | SHOULD | `Duration`, `PathBuf`, newtypes |
| TD-03 Newtypes for semantics and invariants | SHOULD | Units, IDs, validation |
| TD-05 Struct fields are private | MUST | Preserve evolution freedom |
| TD-06 Enums for state machines | SHOULD | Make invalid states unrepresentable |
| TD-07 `#[non_exhaustive]` for extensibility | SHOULD | Future-compatible enums and configs |
| TD-09 Don't duplicate derived bounds | MUST | Bounds on impls, not definitions |
| TD-10 Builder for complex construction | SHOULD | Chainable, validating `build` |
| TD-11 Typestate pattern | CONSIDER | Compile-time state enforcement |
| TD-12 Public types implement Debug | MUST | Redact secrets, test the redaction |
| TD-13 Readable types implement Display | MUST | Required by `std::error::Error` |
| TD-14 Eagerly implement common traits | SHOULD | `Hash`, `Default`, `Clone` for ergonomics |
| TD-17 `PhantomData` tracks variance | SHOULD | Required for raw-pointer wrappers |
| TD-20 `NonZero*` for niche optimization | CONSIDER | `Option<NonZeroU32>` is 4 bytes |
| TD-21 `repr` for layout-sensitive types | CONSIDER | `repr(C)`, `repr(transparent)` for FFI |
| TD-23 `Pin<Ptr<T>>` for address-sensitive | CONSIDER | Futures, self-references |
| TD-24 `PhantomPinned` on `!Unpin` types | SHOULD | Stable-Rust opt-out of `Unpin` |
| TD-25 Avoid self-referential types | AVOID | Use `Rc`/indices or a helper crate |
| TD-26 Sealed traits | CONSIDER | Closed trait implementation surface |
| TD-27 Object-safe traits | SHOULD | Gate generic methods on `Self: Sized` |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `Debug` conventions, derive choice, and `Default`.
- **API Design**: See `02-api-design.md` for public-API patterns, argument conventions, and return types.
- **Error Handling**: See `03-error-handling.md` for error-type design and `Display`/`std::error::Error` requirements.
- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for how ownership shapes API signatures.
- **Traits**: See `06-traits.md` for deeper trait-design patterns — bounds, coherence, blanket impls.
- **Concurrency and Async**: See `07-concurrency-async.md` for `Send`/`Sync`/`Unpin` implications in concurrent code.
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for `#[repr(C)]`, `MaybeUninit`, and the soundness obligations of unsafe type design.


## External References

- [The Rust Reference — Type System](https://doc.rust-lang.org/reference/types.html)
- [The Rust Reference — Special Types and Traits](https://doc.rust-lang.org/reference/special-types-and-traits.html)
- [The Rustonomicon — Data Representation](https://doc.rust-lang.org/nomicon/data.html)
- [The Rustonomicon — Subtyping and Variance](https://doc.rust-lang.org/nomicon/subtyping.html)
- [Rust API Guidelines — Type Safety](https://rust-lang.github.io/api-guidelines/type-safety.html)
- [Async Book — Pinning](https://rust-lang.github.io/async-book/pinning.html)
- [`std::pin`](https://doc.rust-lang.org/std/pin/index.html) and [`std::marker::PhantomData`](https://doc.rust-lang.org/std/marker/struct.PhantomData.html) / [`PhantomPinned`](https://doc.rust-lang.org/std/marker/struct.PhantomPinned.html)
- Pragmatic Rust Guidelines: M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY, M-STRONG-TYPES, C-NEWTYPE, C-BUILDER, C-COMMON-TRAITS, C-STRUCT-PRIVATE, C-STRUCT-BOUNDS, C-SEALED, C-OBJECT, C-BITFLAG
