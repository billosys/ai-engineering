# Trait Design and Implementation

Guidelines for designing traits, implementing them well, and using trait objects. Covers trait-as-interface vs trait-as-bound framing, associated types vs generics, coherence and blanket impls, object safety, auto traits, operator overloads, extension traits, and the generic-machinery features (supertraits, `where` clauses, HRTBs, `dyn` upcasting) that make them fit together.


## TR-01: `impl Trait` in Argument Position

**Strength**: SHOULD

**Summary**: Use `impl Trait` for single-use generic parameters; use a named type parameter `<T>` when callers need to refer to the type.

```rust
// ✅ GOOD: concise for a throwaway bound
fn sum(iter: impl Iterator<Item = i32>) -> i32 {
    iter.sum()
}

// Equivalent — verbose for the same meaning
fn sum_generic<I: Iterator<Item = i32>>(iter: I) -> i32 {
    iter.sum()
}

// ✅ GOOD: multiple `impl Trait` compose
fn send_all(items: impl IntoIterator<Item = impl AsRef<str>>) {
    for item in items {
        send(item.as_ref());
    }
}

// ❌ LIMITATION: callers can't turbofish `impl Trait`
fn process(iter: impl Iterator<Item = i32>) { /* ... */ }
// process::<std::vec::IntoIter<i32>>(v);   // not allowed

// ✅ Use a named parameter when the caller benefits from naming T
fn process_named<I: Iterator<Item = i32>>(iter: I) { /* ... */ }
```

**Rationale**: `impl Trait` in argument position is sugar for an anonymous generic parameter — monomorphized the same way, with the same zero-cost abstraction. Switch to a named `<T>` when you need turbofish, a `where` clause that references the type, or the type repeats in the signature.

**See also**: TR-10, API-41

---

## TR-02: Blanket Implementations

**Strength**: CONSIDER

**Summary**: Implement a trait for every type meeting a bound; this is how standard ergonomics like `ToString` / `Into` work.

```rust
use std::fmt::Display;

// ✅ Blanket impl — anything Display automatically gains `.log()`
pub trait Loggable {
    fn log(&self);
}
impl<T: Display + ?Sized> Loggable for T {
    fn log(&self) { println!("[LOG] {self}"); }
}

"hello".log();   // works
42.log();        // works

// ✅ Blanket impl for references — enables `&T: MyTrait` when `T: MyTrait`
impl<T: MyTrait + ?Sized> MyTrait for &T {
    fn method(&self) { (**self).method() }
}

// ✅ Blanket impl for Box — forwarding through the pointer
impl<T: MyTrait + ?Sized> MyTrait for Box<T> {
    fn method(&self) { (**self).method() }
}

// ❌ CAUTION: blanket impls are final for your trait
// If you later add `impl MyTrait for String`, it conflicts with the
// blanket above (since String: Display). Pick one discipline and stick to it.
```

**Rationale**: Blanket impls give users implementations "for free" when a bound holds. They also lock you in — adding a specific impl later that overlaps is a breaking change. Use them when you want universal coverage (ext traits, conversion traits), not when some types need bespoke behavior.

**See also**: TR-03 (orphan rule interaction), TR-05 (extension traits lean on blanket impls)

---

## TR-03: Coherence and the Orphan Rule

**Strength**: MUST

**Summary**: You can implement a trait for a type only if you own the trait, the type, or both. This is the orphan rule, and it guarantees every `(Trait, Type)` pair has at most one implementation in the entire program.

```rust
pub trait MyTrait {}

// ✅ Your trait, foreign type
impl MyTrait for String {}

// ✅ Foreign trait, your type
pub struct MyType;
impl std::fmt::Display for MyType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "MyType")
    }
}

// ❌ Foreign trait, foreign type — orphan rule violation
// impl std::fmt::Display for Vec<u8> {}

// ✅ Workaround: newtype wrapper
pub struct MyBytes(pub Vec<u8>);
impl std::fmt::Display for MyBytes {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{} bytes", self.0.len())
    }
}

// ✅ Blanket impl counts as "owning" through the trait
pub trait MyExt {
    fn my_method(&self);
}
impl<T: std::fmt::Display + ?Sized> MyExt for T {
    fn my_method(&self) { println!("ext: {self}"); }
}
```

**Rationale**: Without the orphan rule, two crates could both `impl Trait for Foo` and the compiler would have no principled way to pick. The newtype workaround (wrap in a `struct MyWrapper(Foreign)`) is the canonical escape hatch when you need both-foreign combinations — see TD-03.

**See also**: TR-05 (extension traits), TD-03 (newtype pattern)

---

## TR-04: Essential Functionality Is Inherent

**Strength**: MUST

**Summary**: Put a type's core methods in an inherent `impl` block. Trait impls should forward to inherent methods, not carry the primary implementation.

```rust
// ❌ BAD: core method only reachable via trait
pub struct HttpClient { /* ... */ }

pub trait Download {
    fn download_file(&self, url: &str);
}

impl Download for HttpClient {
    fn download_file(&self, url: &str) {
        // Users must `use Download;` to find this method at all.
    }
}

// ✅ GOOD: core method inherent; trait forwards
impl HttpClient {
    pub fn download_file(&self, url: &str) {
        // real logic here
    }
}

impl Download for HttpClient {
    fn download_file(&self, url: &str) {
        HttpClient::download_file(self, url)
    }
}
```

**Rationale**: Inherent methods are discoverable without trait imports, appear prominently in rustdoc, and work with autocomplete out of the box. Use traits to express shared contracts across types, not to hide your type's own API behind an import requirement.

**See also**: M-ESSENTIAL-FN-INHERENT, API-24

---

## TR-05: Extension Traits for Foreign Types

**Strength**: CONSIDER

**Summary**: Add convenience methods to types you don't own with an `*Ext` trait plus a blanket impl. Users `use YourExt;` to enable them.

```rust
// ✅ Extension trait with the `*Ext` naming convention
pub trait StrExt {
    fn truncate_to(&self, n: usize) -> &str;
}

impl StrExt for str {
    fn truncate_to(&self, n: usize) -> &str {
        match self.char_indices().nth(n) {
            Some((i, _)) => &self[..i],
            None => self,
        }
    }
}

// ✅ Typical shape: base trait + Ext trait with default methods
pub trait AsyncRead {
    fn poll_read(/* ... */) -> /* ... */ { todo!() }
}

pub trait AsyncReadExt: AsyncRead {
    fn read_to_end<'a>(&'a mut self, buf: &'a mut Vec<u8>)
    where
        Self: Sized,
    {
        /* default implementation in terms of poll_read */
    }
}

// Blanket impl: everyone who implements the base trait gets the Ext trait
impl<T: AsyncRead + ?Sized> AsyncReadExt for T {}

// Usage requires bringing the trait into scope
use some_crate::StrExt;
let s = "hello world";
let t = s.truncate_to(5);
```

**Rationale**: Extension traits give you API growth without requiring a newtype wrapper or violating coherence. The `*Ext` convention signals "this trait exists only to decorate another type with methods." Pair with a blanket impl so users don't have to implement the Ext trait themselves.

**See also**: TR-02, TR-03, API-45

---

## TR-06: Forwarding Implementations for Wrapper Types

**Strength**: SHOULD

**Summary**: When you wrap a type, forward common traits (`Debug`, `Clone`, `Display`, `PartialEq`, etc.) to the inner value so the wrapper composes cleanly.

```rust
use std::fmt;

pub struct Logged<T> {
    inner: T,
    name: String,
}

// ✅ Forward Debug when T: Debug
impl<T: fmt::Debug> fmt::Debug for Logged<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Logged")
            .field("name", &self.name)
            .field("inner", &self.inner)
            .finish()
    }
}

// ✅ Forward Clone when T: Clone
impl<T: Clone> Clone for Logged<T> {
    fn clone(&self) -> Self {
        Self { inner: self.inner.clone(), name: self.name.clone() }
    }
}

// ✅ Generic container: forward via iterator shape
impl<T> Extend<T> for Logged<Vec<T>> {
    fn extend<I: IntoIterator<Item = T>>(&mut self, iter: I) {
        self.inner.extend(iter);
    }
}
```

**Rationale**: Wrappers should behave as much like their inner type as the domain allows; forwarding `Debug`/`Clone`/`Default` keeps them usable in generic contexts. Do **not** reach for `Deref` to forward every method — see TR-21.

**See also**: TR-21, TD-03 (newtypes)

---

## TR-07: Associated Types vs Generic Parameters

**Strength**: SHOULD

**Summary**: Associated types when each implementor has one canonical choice; generic parameters when multiple implementations make sense.

```rust
// ✅ Associated type — each iterator yields exactly one Item
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}
// impl Iterator for Counter { type Item = u32; ... }
// You can't have two Iterator impls for Counter with different Items.

// ✅ Generic parameter — String: From<&str>, From<char>, From<Box<str>>, ...
pub trait From<T> {
    fn from(value: T) -> Self;
}

// ✅ Mix: generic input, associated output/error
pub trait Converter<Input> {
    type Output;
    type Error;
    fn convert(&self, input: Input) -> Result<Self::Output, Self::Error>;
}

// ❌ AVOID: a generic parameter where an associated type is needed
pub trait BadIterator<Item> {            // forces callers to track Item
    fn next(&mut self) -> Option<Item>;  // ambiguous: `Vec<u8>.next::<u8>()`?
}
```

**Rationale**: Associated types express a functional dependency — "for this impl, there's one Item." That lets call sites write `v.next()` without a turbofish. Generic parameters are right when the same `Self` type legitimately has multiple implementations (conversions, arithmetic across types).

**See also**: TD-15 (type-design angle on this same choice)

---

## TR-08: Eagerly Implement Common Traits

**Strength**: SHOULD

**Summary**: Public types should derive or implement the standard suite — `Debug`, `Clone`, `Copy` (where cheap), `PartialEq`, `Eq`, `Hash`, `Default`, `PartialOrd`, `Ord`, `Display` (where readable).

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct UserId(u64);

#[derive(Debug, Clone, Default)]
pub struct Config {
    timeout: Option<std::time::Duration>,
    retries: Option<u32>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub enum Status { Pending, Active, Completed }

impl Default for Status {
    fn default() -> Self { Status::Pending }
}

// Custom when derive doesn't fit — e.g., floats
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

```rust
// ✅ Don't derive traits that are semantically wrong
pub struct FileHandle { fd: std::os::fd::RawFd }          // no Clone — FDs aren't copyable
pub struct DbConnection { conn: *mut sqlite3::sqlite3 }   // no Clone — handles aren't shareable
// MutexGuard intentionally doesn't implement Clone
```

**Rationale**: A `UserId` without `Hash` can't key a `HashMap`. A `Config` without `Default` forces every caller to fill in all fields. Missing `Debug` breaks `assert_eq!`, `dbg!`, and `thiserror`. These traits are the ambient contract users expect; not deriving them is a decision that should be justified.

**See also**: C-COMMON-TRAITS, TD-12, TD-13, TD-14

---

## TR-09: Trait Definition — Behavior, Not Data

**Strength**: SHOULD

**Summary**: Traits describe behavior, not storage. Prefer abstract capabilities over getter/setter pairs, and provide useful defaults where possible.

```rust
// ❌ BAD: trait as data accessor pair
pub trait HasName {
    fn get_name(&self) -> &str;
    fn set_name(&mut self, name: &str);
}

// ✅ GOOD: trait as a behavior
pub trait Named {
    fn name(&self) -> &str;
}

// ✅ Default methods in terms of required methods
pub trait Greet {
    fn name(&self) -> &str;                        // required

    fn greet(&self) -> String {                    // default
        format!("Hello, {}!", self.name())
    }
}

// ✅ Associated types scope the trait's output vocabulary
pub trait Parser {
    type Output;
    type Error;
    fn parse(&self, input: &str) -> Result<Self::Output, Self::Error>;
}

// ✅ Default methods can be overridden when a type has a faster path
pub trait Drawable {
    fn draw(&self, canvas: &mut Canvas);
    fn draw_at(&self, canvas: &mut Canvas, x: i32, y: i32) {
        canvas.translate(x, y);
        self.draw(canvas);
        canvas.translate(-x, -y);
    }
}
```

**Rationale**: Traits coupling directly to storage (get/set pairs) are rarely abstractable — each type ends up with a slightly different notion of "the name." A behavior-shaped trait (`Named`, `Greet`, `Drawable`) composes with blanket impls, default methods, and generic code. Reserve data-shaped interfaces for concrete structs.

**See also**: TR-12 (narrow traits), TR-20 (supertraits)

---

## TR-10: Keep Trait Bounds Minimal and Scoped

**Strength**: SHOULD

**Summary**: Put bounds on `impl` blocks and individual methods — not on type definitions. Use `where` clauses when bounds grow beyond a trivial list.

```rust
// ❌ BAD: bounds on the struct definition leak to every use
pub struct Container<T: Clone + Debug + PartialEq> {
    items: Vec<T>,
}

// ✅ GOOD: unbounded definition, bounds on relevant impls only
pub struct Container<T> {
    items: Vec<T>,
}

impl<T> Container<T> {
    pub fn new() -> Self { Self { items: Vec::new() } }
    pub fn push(&mut self, item: T) { self.items.push(item); }
}

impl<T: Clone> Container<T> {
    pub fn duplicate_last(&mut self) {
        if let Some(last) = self.items.last() {
            self.items.push(last.clone());
        }
    }
}

impl<T: std::fmt::Debug> Container<T> {
    pub fn debug_print(&self) {
        for item in &self.items { println!("{item:?}"); }
    }
}

// ✅ GOOD: `where` clause when bounds get complex
fn merge<K, V, I>(map: &mut std::collections::HashMap<K, V>, iter: I)
where
    K: std::hash::Hash + Eq + Clone,
    V: Clone,
    I: IntoIterator<Item = (K, V)>,
{
    for (k, v) in iter { map.insert(k, v); }
}
```

**Rationale**: Bounds on the type definition cascade into every function signature that mentions the type — even ones that don't need the bound. Bound each `impl` or method individually so `Container<RawFd>` remains usable if you never call `duplicate_last`. `where` clauses make complex bounds readable and play nicer with associated types.

**See also**: TD-09 (struct bound hygiene), API-41

---

## TR-11: Marker Traits

**Strength**: CONSIDER

**Summary**: Method-less traits mark type properties — stdlib's `Copy`, `Send`, `Sync`, `Sized`, `Unpin` are marker traits, and you can define your own for domain invariants.

```rust
// Standard markers you rely on constantly
// - Sized:   size known at compile time (implicit on all generic params)
// - Copy:    bitwise-copyable (must also be Clone, no Drop)
// - Send:    safe to transfer ownership across threads
// - Sync:    safe to share &T across threads (T: Sync iff &T: Send)
// - Unpin:   not address-sensitive; pinning has no effect

// ✅ Your own marker for a type-level invariant
pub trait ThreadSafeCache: Send + Sync {}
impl<T: Send + Sync> ThreadSafeCache for T {}

// ✅ Typestate marker (see TD-11 for full pattern)
use std::marker::PhantomData;
pub struct Unvalidated;
pub struct Validated;

pub struct Email<State> {
    value: String,
    _state: PhantomData<State>,
}

impl Email<Unvalidated> {
    pub fn validate(self) -> Result<Email<Validated>, ValidationError> {
        /* ... */ Ok(Email { value: self.value, _state: PhantomData })
    }
}

impl Email<Validated> {
    pub fn send(&self) { /* only validated emails reach here */ }
}
```

**Rationale**: Marker traits carry no runtime cost — they're purely compile-time assertions. Use them to collapse a bundle of bounds into a named concept (`ThreadSafeCache = Send + Sync`), to pin down invariants at the type level, or to enable downstream impls to opt in or out.

**See also**: TR-13 (auto traits), TD-11 (typestate), TD-24 (`PhantomPinned`)

---

## TR-12: Narrow Traits Over Wide Traits

**Strength**: SHOULD

**Summary**: Split large traits into small ones. Depend on just the capability you need; combine narrow traits via supertraits when a type needs the whole set.

```rust
// ❌ BAD: one mega-trait forces users to implement everything
trait Database {
    async fn store(&self, id: Id, obj: Object) -> Result<(), DbError>;
    async fn load(&self, id: Id) -> Result<Object, DbError>;
    async fn delete(&self, id: Id) -> Result<(), DbError>;
    async fn update_config(&self, file: std::path::PathBuf);
}

// ✅ GOOD: one capability per trait
trait Store  { async fn store(&self, id: Id, obj: Object) -> Result<(), DbError>; }
trait Load   { async fn load(&self, id: Id) -> Result<Object, DbError>; }
trait Delete { async fn delete(&self, id: Id) -> Result<(), DbError>; }

// ✅ Combine with a supertrait alias when callers need the full set
trait DataAccess: Store + Load + Delete {}
impl<T: Store + Load + Delete> DataAccess for T {}

// Functions depend on just what they need
async fn read_only(db: impl Load) { /* only `load` available */ }
async fn full_access(db: impl DataAccess) { /* all three */ }
```

**Rationale**: Narrow traits follow the interface-segregation principle: callers specify minimum requirements, mocks in tests become trivial, and implementors can provide subsets. The supertrait `DataAccess` is an "aggregator" trait that documents the combined capability without forcing a single huge implementation block.

**See also**: TR-20 (supertraits), M-DI-HIERARCHY

---

## TR-13: Auto Traits and Negative Implementations

**Strength**: CONSIDER

**Summary**: `Send`, `Sync`, `Unpin`, `UnwindSafe`, and `RefUnwindSafe` are *auto traits* — implemented automatically when every field implements them. Negative impls (`impl !Trait for T`) override that propagation.

```rust
use std::marker::PhantomData;

// A struct is automatically Send + Sync because every field is
struct Stats {
    data: Vec<i32>,   // Send + Sync
    count: usize,     // Send + Sync
}

// A struct becomes !Sync automatically because Rc<T> is !Sync
struct NotSync {
    shared: std::rc::Rc<i32>,
}

// Raw pointers opt out via negative impls in std:
//   impl<T: ?Sized> !Send for *const T {}
//   impl<T: ?Sized> !Send for *mut T   {}
// So any type containing *mut T is !Send by default.
pub struct RawOwned<T> {
    ptr: *mut T,
    _owns: PhantomData<T>,
}
// RawOwned<T> is !Send even if T: Send.

// ✅ When you know the invariant holds, re-assert with unsafe
//    (e.g., the pointer is exclusively owned by self)
unsafe impl<T: Send> Send for RawOwned<T> {}
unsafe impl<T: Sync> Sync for RawOwned<T> {}

// Unpin is the same mechanism — opt out with PhantomPinned
use std::marker::PhantomPinned;
pub struct SelfRef {
    data: String,
    ptr: *const u8,
    _pin: PhantomPinned,   // makes the whole type !Unpin
}
```

**Rationale**: Auto traits are the main reason Rust concurrency "just works" for the easy cases — you don't declare that `Vec<u32>` is `Send`, the compiler infers it from its fields. Negative impls (in stable Rust: via stdlib on `*const T` / `*mut T`, or via `PhantomPinned` for `Unpin`) are how the compiler knows to stop the propagation. When you `unsafe impl Send/Sync` to re-enable, you're promising the invariant holds.

**See also**: TR-11, TD-24 (`PhantomPinned`), 07-concurrency-async

---

## TR-14: Object Safety / `dyn` Compatibility

**Strength**: MUST

**Summary**: To be used as `dyn Trait`, a trait must be object-safe — no generic methods, no `Self`-returning methods, no `Self: Sized` requirements on required methods. Gate non-object-safe methods behind `where Self: Sized`.

```rust
// ✅ Object-safe
pub trait Draw {
    fn draw(&self, canvas: &mut Canvas);
    fn bounds(&self) -> Rect;
}

let shapes: Vec<Box<dyn Draw>> = vec![
    Box::new(Circle { radius: 10.0 }),
    Box::new(Rectangle { width: 20.0, height: 15.0 }),
];

// ❌ Not object-safe: generic method
pub trait Serialize {
    fn serialize<W: std::io::Write>(&self, w: W);
}
// let _: &dyn Serialize;   // error: cannot be made into an object

// ❌ Not object-safe: returns Self
pub trait Duplicate {
    fn duplicate(&self) -> Self;
}

// ✅ Mixed — object-safe core, non-object-safe extensions gated on Sized
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;  // object-safe

    fn map<B, F>(self, f: F) -> Map<Self, F>
    where
        Self: Sized,                            // excluded from vtable
        F: FnMut(Self::Item) -> B,
    { /* ... */ todo!() }
}

// ✅ Object-safe serialization: accept a trait object for the sink
pub trait Serializable {
    fn serialize_to(&self, w: &mut dyn std::io::Write) -> std::io::Result<()>;
}
```

**Rationale**: The vtable behind `dyn Trait` needs a fixed layout — one function pointer per method, with a known calling convention. Generic methods would need infinite vtable slots; `-> Self` would need to know the concrete size. Gating the non-object-safe parts with `Self: Sized` lets the core trait stay dyn-compatible while still offering rich chainable methods on concrete impls.

**See also**: TR-15, TR-17, TD-27

---

## TR-15: Trait Object Forms — `&dyn`, `Box<dyn>`, `Rc<dyn>`, `Arc<dyn>`

**Strength**: SHOULD

**Summary**: Choose the pointer type based on ownership and sharing needs; `dyn Trait` is unsized so it always appears behind a pointer.

```rust
// &dyn Trait — borrowed, zero-cost, most common for parameters
fn render(shape: &dyn Draw, canvas: &mut Canvas) {
    shape.draw(canvas);
}

// &mut dyn Trait — exclusive borrow of a trait object
fn mutate(item: &mut dyn Update) {
    item.tick();
}

// Box<dyn Trait> — owned, single-owner, heap-allocated
let plugins: Vec<Box<dyn Plugin>> = vec![
    Box::new(AuthPlugin),
    Box::new(LoggingPlugin),
];

// Rc<dyn Trait> — shared ownership, single-threaded
let node: std::rc::Rc<dyn Node> = std::rc::Rc::new(LeafNode);
let also: std::rc::Rc<dyn Node> = node.clone();

// Arc<dyn Trait> — shared ownership, thread-safe
let handler: std::sync::Arc<dyn EventHandler + Send + Sync>
    = std::sync::Arc::new(MyHandler);

// Lifetime annotations on trait objects
let shape: &'static dyn Draw = &STATIC_CIRCLE;   // lives forever
let tmp:   &dyn Draw         = &local_circle;    // borrowed from local
```

```rust
// ❌ dyn Trait on its own is unsized — always behind a pointer
// let x: dyn Draw = Circle { radius: 1.0 };   // error: Sized not satisfied

// ✅ Use a helper when you need a heterogeneous owned collection
pub struct Scene {
    items: Vec<Box<dyn Draw>>,
}
impl Scene {
    pub fn add<T: Draw + 'static>(&mut self, item: T) {
        self.items.push(Box::new(item));
    }
}
```

**Rationale**: Each form expresses a different ownership shape: `&dyn` borrows, `Box<dyn>` owns once, `Rc<dyn>` / `Arc<dyn>` share. The `'static` bound on `Scene::add` is necessary because the trait object doesn't retain a named lifetime for its data. Reach for `&dyn` first; escalate only when ownership demands it.

**See also**: TR-22 (extra bounds on trait objects), TR-24 (upcasting), OB-22

---

## TR-16: Operator Overloads Are Unsurprising

**Strength**: MUST

**Summary**: Implement `std::ops` traits only when the operator reads naturally and obeys the usual algebraic laws. Never use `+` to mean "append", "log", or "merge".

```rust
use std::ops::{Add, Mul, Neg};

// ✅ GOOD: vector arithmetic reads like math
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Vec2 { x: f64, y: f64 }

impl Add for Vec2 {
    type Output = Vec2;
    fn add(self, rhs: Vec2) -> Vec2 {
        Vec2 { x: self.x + rhs.x, y: self.y + rhs.y }
    }
}

impl Mul<f64> for Vec2 {
    type Output = Vec2;
    fn mul(self, s: f64) -> Vec2 { Vec2 { x: self.x * s, y: self.y * s } }
}

impl Neg for Vec2 {
    type Output = Vec2;
    fn neg(self) -> Vec2 { Vec2 { x: -self.x, y: -self.y } }
}

let a = Vec2 { x: 1.0, y: 2.0 };
let b = Vec2 { x: 3.0, y: 4.0 };
let _c = a + b;   // vector addition
let _d = a * 2.0; // scalar multiplication
let _e = -a;      // negation

// ❌ BAD: + means "log this"
pub struct Logger { msgs: Vec<String> }
impl Add<String> for Logger {
    type Output = Logger;
    fn add(mut self, m: String) -> Logger { self.msgs.push(m); self }
}
// let log = Logger { msgs: vec![] } + "oops".to_string();   // unreadable

// ✅ Use a named method
impl Logger {
    pub fn log(&mut self, m: String) { self.msgs.push(m); }
}
```

```rust
// Expected algebraic properties for numeric-looking types
assert_eq!(a + b, b + a);              // commutative
assert_eq!((a + b) * 2.0, a * 2.0 + b * 2.0);  // distributive
assert_eq!(a + Vec2 { x: 0.0, y: 0.0 }, a);     // identity
```

**Rationale**: Operators carry strong cross-language expectations — readers assume `a + b` is associative, commutative, and zero-cost. Breaking those expectations turns code into a puzzle. Keep `+`, `*`, `-`, `[]` for their mathematical meanings and use methods (`.append`, `.log`, `.merge`) for domain operations.

**See also**: API-32, C-OP-TRAITS

---

## TR-17: Concrete > Generic > `dyn`

**Strength**: SHOULD

**Summary**: Default to concrete types. Reach for generics when callers need flexibility; reach for trait objects only when generics would produce unmanageable nesting or when you genuinely need runtime type mixing.

```rust
// ✅ Best: concrete type — simplest, fastest
pub struct Service {
    db: PostgresDatabase,
}

// ✅ Generic: flexibility without runtime cost, monomorphized
pub struct Service<D: Database> {
    db: D,
}

// ⚠️ Consider dyn when generics nest excessively or types are open-ended
pub struct Service {
    db: Box<dyn Database>,      // erase one level of generics
}

// ✅ Heterogeneous collection — only dyn works here
let plugins: Vec<Box<dyn Plugin>> = load_plugins();
```

```rust
// Cost summary:
//  concrete T     : zero runtime cost, zero flexibility
//  impl Trait / T : zero runtime cost (monomorphized), generic flexibility
//                   — compile time and binary size can grow
//  dyn Trait      : small vtable indirection, no inlining through boundary
//                   — one function body, open-ended extensibility
```

**Rationale**: Generics are zero-cost abstraction but they propagate into every caller and can explode compile times when deeply nested. Trait objects have a tiny runtime cost (one indirect call) but collapse an arbitrary set of types into a single function body. Escalate only when the next rung gives you something the previous rung can't.

**See also**: TR-14, TR-15, API-40, M-SIMPLE-ABSTRACTIONS

---

## TR-18: `From` / `TryFrom` for Conversions

**Strength**: SHOULD

**Summary**: Implement `From<T>` for infallible conversions and `TryFrom<T>` for fallible ones. `Into`, `try_into`, and the `?` operator all fall out for free.

```rust
// ✅ Infallible conversion
pub struct EmailAddress(String);

impl From<String> for EmailAddress {
    fn from(s: String) -> Self { EmailAddress(s) }
}

// Now .into() and `?` through From work
fn make_user(email: String) -> User {
    User { email: email.into() }
}

// ✅ Widening integer conversions
// (std already provides u32 -> u64; this is the pattern)
impl From<u32> for MyIndex {
    fn from(small: u32) -> MyIndex { MyIndex(small as u64) }
}

// ✅ Wrapping related types in an enum
pub enum IpAddr {
    V4(std::net::Ipv4Addr),
    V6(std::net::Ipv6Addr),
}
impl From<std::net::Ipv4Addr> for IpAddr {
    fn from(a: std::net::Ipv4Addr) -> Self { IpAddr::V4(a) }
}
impl From<std::net::Ipv6Addr> for IpAddr {
    fn from(a: std::net::Ipv6Addr) -> Self { IpAddr::V6(a) }
}

// ✅ Error-type From impls let `?` bubble naturally
pub enum AppError { Io(std::io::Error), Json(serde_json::Error) }
impl From<std::io::Error>    for AppError { fn from(e: std::io::Error)    -> Self { AppError::Io(e)   } }
impl From<serde_json::Error> for AppError { fn from(e: serde_json::Error) -> Self { AppError::Json(e) } }

fn load(path: &str) -> Result<Data, AppError> {
    let s = std::fs::read_to_string(path)?;   // io::Error -> AppError
    let data = serde_json::from_str(&s)?;      // serde::Error -> AppError
    Ok(data)
}

// ✅ Fallible conversion: TryFrom
impl TryFrom<u32> for u16 {
    type Error = std::num::TryFromIntError;
    fn try_from(n: u32) -> Result<u16, Self::Error> { /* provided by std */ todo!() }
}
```

**Rationale**: Implement `From`, never `Into` — the blanket `impl<T, U: From<T>> Into<U> for T` gives you `.into()` for free. Use `TryFrom` for anything that can fail (parsing, narrowing, validation) and keep the `Error` type descriptive. This is the idiom that makes `?` and `thiserror::Error(#[from])` feel seamless.

**See also**: API-17, EH-09, C-CONV-TRAITS

---

## TR-19: Sealed Traits for Closed Implementation Sets

**Strength**: CONSIDER

**Summary**: When a trait should be implementable only inside your crate, require a private supertrait. Downstream users can call the trait's methods but not `impl` it.

```rust
mod private {
    pub trait Sealed {}
}

/// This trait is sealed; you cannot implement it from another crate.
pub trait Protocol: private::Sealed {
    fn handshake(&self);
}

pub struct Http;
pub struct Grpc;

impl private::Sealed for Http {}
impl private::Sealed for Grpc {}

impl Protocol for Http { fn handshake(&self) { /* ... */ } }
impl Protocol for Grpc { fn handshake(&self) { /* ... */ } }

// In a downstream crate:
// impl Protocol for MyCustom {}     // error: Sealed is not in scope
```

**Rationale**: Sealed traits let you add required methods in minor versions without breaking downstream implementors — there are none. They also enable exhaustive reasoning (the set of impls is known). Use them for protocol enumerations, supported-type lists, and anywhere "extend via impl" would break your invariants. See TD-26 for the type-design angle.

**See also**: TD-26, C-SEALED, API-43

---

## TR-20: Supertraits for Composition

**Strength**: SHOULD

**Summary**: When trait `A` requires functionality from trait `B`, declare it with `trait A: B { ... }`. Methods from `B` are then available inside `A`'s default methods and in generic code bounded by `A`.

```rust
use std::fmt::{Debug, Display};
use std::hash::Hash;

// ✅ Require Debug for better errors
pub trait Repository: Debug {
    fn save(&mut self, item: &Item) -> Result<(), SaveError>;
}

// ✅ Alias trait: anything meeting the bundle is a CacheKey
pub trait CacheKey: Clone + Hash + Eq + Debug {}
impl<T: Clone + Hash + Eq + Debug> CacheKey for T {}

// ✅ Standard library pattern
pub trait Error: Debug + Display {
    fn source(&self) -> Option<&(dyn Error + 'static)> { None }
}

// ✅ Supertrait methods are visible inside default-method bodies
pub trait OutlinePrint: Display {
    fn outline_print(&self) {
        let s = self.to_string();               // via Display
        let bar = "*".repeat(s.len() + 4);
        println!("{bar}\n* {s} *\n{bar}");
    }
}
```

**Rationale**: Supertraits replace "one giant trait" with composable building blocks and let default methods leverage external capabilities. Use them when your trait genuinely needs the functionality; resist bundling traits together just to reduce typing at use-site — that's what aliases and `where` clauses are for.

**See also**: TR-12 (narrow traits), TR-09

---

## TR-21: `Deref` Is for Smart Pointers, Not Inheritance

**Strength**: AVOID (as inheritance), CONSIDER (for genuine smart pointers)

**Summary**: Implement `Deref` only when your type is a pointer-like wrapper that logically refers to a `Target`. Do not use `Deref` to forward methods from a contained struct — that's fake inheritance, and it doesn't work for trait bounds.

```rust
use std::ops::Deref;

// ✅ CORRECT: smart pointer — MyBox<T> logically IS a pointer to T
pub struct MyBox<T>(T);
impl<T> Deref for MyBox<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.0 }
}

// std follows the same rule: Vec<T>: Deref<Target=[T]>, String: Deref<Target=str>

// ❌ BAD: fake inheritance
pub struct Animal { species: String }
impl Animal { pub fn speak(&self) { println!("{}!", self.species); } }

pub struct Dog { animal: Animal }
impl Deref for Dog {
    type Target = Animal;
    fn deref(&self) -> &Animal { &self.animal }
}
// dog.speak() compiles — but:
//   - Dog is NOT Animal; generic functions over &Animal won't accept &Dog
//   - Traits implemented on Animal are NOT implemented on Dog
//   - `self` inside speak() is &Animal, not &Dog — surprising to readers

// ✅ Instead: explicit delegation (or the `delegate` / `ambassador` crates)
impl Dog {
    pub fn speak(&self) { self.animal.speak(); }
}
```

**Rationale**: `Deref` is a contract that says "this type is a pointer; dereferencing yields a `Target`." Using it to emulate OO inheritance breaks every expectation: no subtyping, no trait forwarding, surprising `self` semantics, and rustdoc doesn't inline the delegated methods. If you want method delegation, write it explicitly or use a delegation crate. Main treatment of the anti-pattern is in guide 11 (AP-14).

**See also**: AP-14 (guide 11), TR-06 (forwarding traits, not methods), TD-03

---

## TR-22: Extra Bounds on Trait Objects (`dyn Trait + Send + Sync`)

**Strength**: SHOULD

**Summary**: Auto traits can be added as extra bounds on a trait object. Use them on returned / stored trait objects to keep types `Send`, `Sync`, or `'static` for concurrent code and downcasting.

```rust
use std::error::Error;

// ✅ Single-threaded boxed error — the bare minimum
fn parse(s: &str) -> Result<i32, Box<dyn Error>> {
    Ok(s.parse()?)
}

// ✅ Send: can cross threads (e.g., returned from a tokio task)
async fn load() -> Result<Data, Box<dyn Error + Send>> { todo!() }

// ✅ Send + Sync: shareable — the common std-style error shape
pub fn read_config() -> Result<Config, Box<dyn Error + Send + Sync>> { todo!() }

// ✅ Send + Sync + 'static: also downcastable via Error::downcast_ref
pub fn handler() -> Result<(), Box<dyn Error + Send + Sync + 'static>> { todo!() }

// ✅ Storing trait objects in shared state
use std::sync::Arc;
pub struct Router {
    handlers: Vec<Arc<dyn Handler + Send + Sync>>,
}

// Lifetime form for non-'static trait objects
pub fn borrow_handler<'a>(h: &'a dyn Handler) -> &'a dyn Handler { h }
```

```rust
// ❌ BAD: missing Send makes this unusable in a `tokio::spawn`
async fn bad() -> Result<Data, Box<dyn Error>> { todo!() }
// the future returned from bad() is `!Send` if awaited with a !Send error

// ✅ Add + Send (and + Sync if shared)
async fn good() -> Result<Data, Box<dyn Error + Send + Sync>> { todo!() }
```

**Rationale**: A bare `Box<dyn Error>` is neither `Send` nor `Sync`, so it poisons any containing future. Adding `+ Send + Sync` is how you keep async and multi-threaded code working across `.await` points and `std::thread::spawn`. The `+ 'static` bound is required if you want to call `Error::downcast_ref::<T>` (downcasting needs a static TypeId).

**See also**: TR-13 (auto traits), TR-15, EH-10, API-38

---

## TR-23: Higher-Ranked Trait Bounds (`for<'a>`)

**Strength**: CONSIDER

**Summary**: Use `for<'a>` when a bound must hold for *every* lifetime — most commonly with closures that take references.

```rust
// ✅ A callback that must work for any borrow lifetime
fn call_with_str<F>(f: F) -> usize
where
    F: for<'a> Fn(&'a str) -> usize,
{
    let owned = String::from("hello");
    let a = f(&owned);                      // borrows for a short lifetime
    let b = f("static literal");            // borrows for 'static
    a + b
}

// The caller passes a closure whose lifetime parameter is universal
let n = call_with_str(|s| s.len());

// ✅ Without for<'a>, this wouldn't type-check:
//    fn bad<F, 'a>(f: F) where F: Fn(&'a str) -> usize
//    — the caller would have to commit to a single 'a before passing f.

// ✅ HRTBs appear implicitly in Fn trait bounds — you see them spelled out
//    when the compiler asks for help, or when you name a complex closure type.

// ✅ HRTBs on trait objects
let printer: Box<dyn for<'a> Fn(&'a str)> = Box::new(|s| println!("{s}"));
printer("owned".to_string().as_str());
printer("static");
```

**Rationale**: Most closure bounds don't need explicit HRTBs because `Fn(&str)` is sugar for `for<'a> Fn(&'a str)`. You see them explicitly when the function is itself generic over lifetimes and needs the closure to work for any of them — for example, iterator adapters, parser combinators, and `serde` visitor APIs. Spelling them out can also be required to disambiguate when the compiler can't infer universality.

**See also**: OB-09 (lifetime elision), The Rust Reference §Trait Bounds

---

## TR-24: `dyn` Upcasting (Rust 2024)

**Strength**: CONSIDER

**Summary**: As of Rust 1.86 (edition 2024), a `&dyn SubTrait` / `Box<dyn SubTrait>` can be upcast directly to `&dyn SuperTrait` via a normal coercion.

```rust
trait Animal {
    fn name(&self) -> &str;
}

trait Dog: Animal {
    fn breed(&self) -> &str;
}

struct Labrador;
impl Animal for Labrador { fn name(&self) -> &str { "Rex" } }
impl Dog for Labrador    { fn breed(&self) -> &str { "Labrador" } }

// ✅ Rust 2024+ : direct upcast
fn print_name(d: &dyn Dog) {
    let a: &dyn Animal = d;       // works — upcast coercion
    println!("{}", a.name());
}

// ✅ Also works for Box<dyn>
let boxed: Box<dyn Dog> = Box::new(Labrador);
let _animal: Box<dyn Animal> = boxed;   // upcast

// Pre-2024 workaround (no longer required):
// trait Dog: Animal {
//     fn as_animal(&self) -> &dyn Animal;
// }
// impl Dog for Labrador {
//     fn as_animal(&self) -> &dyn Animal { self }
// }
```

**Rationale**: Before trait-object upcasting stabilized, users had to write explicit `as_super` methods or use `std::any::Any` acrobatics to move between a child and parent trait object. The 2024-edition feature makes the subtype relationship of trait objects match what the type system already allowed for references to concrete types. Prefer the direct coercion on any new codebase targeting `edition = "2024"`.

**See also**: TR-14, TR-20, Rust 1.86 release notes, RFC 3324

---

## TR-25: Use `dyn Trait` for Runtime Polymorphism

**Strength**: SHOULD

**Summary**: Reach for trait objects when you need heterogeneous collections, plugin-style extensibility, or when monomorphization would blow up binary size or compile time.

```rust
// ✅ Plugin manager — impls registered at runtime
pub trait Plugin {
    fn name(&self) -> &str;
    fn execute(&mut self) -> Result<(), PluginError>;
}

pub struct PluginManager {
    plugins: Vec<Box<dyn Plugin>>,
}

impl PluginManager {
    pub fn register(&mut self, p: Box<dyn Plugin>) { self.plugins.push(p); }
    pub fn run_all(&mut self) -> Result<(), PluginError> {
        for p in &mut self.plugins { p.execute()?; }
        Ok(())
    }
}

// ✅ Heterogeneous scene — multiple shape types in one Vec
pub struct Scene {
    items: Vec<Box<dyn Draw>>,
}
impl Scene {
    pub fn add<T: Draw + 'static>(&mut self, t: T) {
        self.items.push(Box::new(t));
    }
    pub fn render(&self, canvas: &mut Canvas) {
        for item in &self.items { item.draw(canvas); }
    }
}

// ✅ Callbacks with heterogeneous closures
pub struct Events {
    handlers: Vec<Box<dyn FnMut(&Event) + Send>>,
}
impl Events {
    pub fn on<F: FnMut(&Event) + Send + 'static>(&mut self, f: F) {
        self.handlers.push(Box::new(f));
    }
}
```

**Rationale**: Generics demand you know every concrete type at compile time. Trait objects are the answer for open-ended sets — plugins you load at runtime, UI trees with mixed components, callbacks from arbitrary closures. Accept the one-indirect-call cost in exchange for runtime flexibility; when static dispatch would work, follow TR-17 and prefer it.

**See also**: TR-15, TR-17, TR-22

---

## TR-26: Use Custom Traits to Tame Complex Bounds

**Strength**: CONSIDER

**Summary**: When a bound gets repeated across many impl blocks — especially one involving `Fn` traits — introduce a named trait with a blanket impl. The name becomes documentation and the bound becomes readable.

```rust
use std::fmt::Display;

pub struct Error;
pub enum Status { Ok, Warn, Fail }

// ❌ BEFORE: verbose bounds repeated everywhere
pub struct Value<G, S, T>
where
    G: FnMut() -> Result<T, Error>,
    S: Fn(&T) -> Status,
    T: Display,
{
    getter: G,
    status: S,
}

impl<G, S, T> Value<G, S, T>
where
    G: FnMut() -> Result<T, Error>,       // repeated
    S: Fn(&T) -> Status,
    T: Display,
{
    pub fn refresh(&mut self) -> Result<T, Error> { (self.getter)() }
}

// ✅ AFTER: a Getter trait names the concept; T is now G::Output
pub trait Getter {
    type Output: Display;
    fn get(&mut self) -> Result<Self::Output, Error>;
}

impl<F, T> Getter for F
where
    F: FnMut() -> Result<T, Error>,
    T: Display,
{
    type Output = T;
    fn get(&mut self) -> Result<T, Error> { self() }
}

pub struct Value2<G: Getter, S: Fn(&G::Output) -> Status> {
    getter: G,
    status: S,
}
```

**Rationale**: Long bounds appearing on every `impl` block are a readability tax — and they leak into public docs. Promoting the bound to a named trait drops one type parameter, documents the role, and opens space for specialized implementations beyond the closure blanket impl. The downside is discoverability: make sure your rustdoc mentions that closures implement the trait automatically.

**See also**: TR-02, TR-10, design-patterns "trait for bounds"


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| TR-01 `impl Trait` in arg position | SHOULD | Anonymous generic for throwaway bounds |
| TR-02 Blanket implementations | CONSIDER | `impl<T: Bound> MyTrait for T` — final, use deliberately |
| TR-03 Coherence / orphan rule | MUST | Own the trait or the type; newtype escape hatch |
| TR-04 Essential functionality is inherent | MUST | Trait impls forward to inherent methods |
| TR-05 Extension traits for foreign types | CONSIDER | `*Ext` + blanket impl |
| TR-06 Forwarding on wrappers | SHOULD | Forward `Debug`/`Clone`/... to inner type |
| TR-07 Associated types vs generics | SHOULD | One canonical choice → associated; many → generic |
| TR-08 Eagerly implement common traits | SHOULD | `Debug`/`Clone`/`Eq`/`Hash`/`Default`/`Display` |
| TR-09 Traits describe behavior | SHOULD | Not getter/setter data shapes |
| TR-10 Minimal, scoped bounds | SHOULD | Bounds on impls and methods, not definitions |
| TR-11 Marker traits | CONSIDER | `Copy`/`Send`/`Sync`/`Unpin` + your own |
| TR-12 Narrow traits over wide | SHOULD | Interface segregation; aggregate via supertraits |
| TR-13 Auto traits + negative impls | CONSIDER | `Send`/`Sync`/`Unpin` propagate; `PhantomPinned`, `!Send` opt out |
| TR-14 Object safety | MUST | No generic methods, no `-> Self`; gate with `Self: Sized` |
| TR-15 Trait object forms | SHOULD | `&dyn` / `Box<dyn>` / `Rc<dyn>` / `Arc<dyn>` |
| TR-16 Operator overloads unsurprising | MUST | Math semantics only, never "append" or "log" |
| TR-17 Concrete > generic > `dyn` | SHOULD | Escalate only as needed |
| TR-18 `From` / `TryFrom` conversions | SHOULD | Drives `?` and `.into()` for free |
| TR-19 Sealed traits | CONSIDER | Private supertrait closes the impl set |
| TR-20 Supertraits for composition | SHOULD | `trait Sub: Super` |
| TR-21 `Deref` for smart pointers only | AVOID | Not for fake inheritance — see guide 11 |
| TR-22 Extra bounds on trait objects | SHOULD | `Box<dyn Error + Send + Sync + 'static>` |
| TR-23 Higher-ranked trait bounds | CONSIDER | `for<'a> Fn(&'a T)` — universal over lifetimes |
| TR-24 `dyn` upcasting (Rust 2024) | CONSIDER | `&dyn Sub` coerces to `&dyn Super` directly |
| TR-25 `dyn Trait` for runtime polymorphism | SHOULD | Heterogeneous collections, plugins, callbacks |
| TR-26 Custom traits tame complex bounds | CONSIDER | `Getter` trait hides `FnMut() -> Result<...>` |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `Default`, derive choice, and common-trait idioms.
- **API Design**: See `02-api-design.md` for object-safe public traits (API-42), sealed traits (API-43), and `From`/`Into` conventions (API-17).
- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for variance, lifetime parameters on trait objects, and smart-pointer selection (OB-22).
- **Type Design**: See `05-type-design.md` for the type-design framing of associated types (TD-15), sealed traits (TD-26), object safety (TD-27), and `PhantomPinned` (TD-24).
- **Anti-Patterns**: See `11-anti-patterns.md` for the full treatment of `Deref` polymorphism (AP-14) and other trait-related mistakes.


## External References

- [Rust API Guidelines — Interoperability](https://rust-lang.github.io/api-guidelines/interoperability.html) — C-COMMON-TRAITS, C-CONV-TRAITS, C-SEALED, C-OP-TRAITS
- [The Rust Reference — Traits](https://doc.rust-lang.org/reference/items/traits.html) and [Object Safety](https://doc.rust-lang.org/reference/items/traits.html#object-safety)
- [The Rust Reference — Special Types and Traits](https://doc.rust-lang.org/reference/special-types-and-traits.html) — auto traits, `Send`/`Sync`, `Sized`, `?Sized`
- [The Rust Programming Language — Advanced Traits](https://doc.rust-lang.org/book/ch20-03-advanced-traits.html) and [Trait Objects](https://doc.rust-lang.org/book/ch18-02-trait-objects.html)
- [The Rustonomicon — Higher-Rank Trait Bounds](https://doc.rust-lang.org/nomicon/hrtb.html) and [Subtyping and Variance](https://doc.rust-lang.org/nomicon/subtyping.html)
- [Rust 1.86 release notes — `dyn` upcasting](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0.html)
- [`std::marker`](https://doc.rust-lang.org/std/marker/index.html) — `Send`, `Sync`, `Sized`, `Unpin`, `PhantomData`, `PhantomPinned`
- Pragmatic Rust Guidelines: M-ESSENTIAL-FN-INHERENT, M-DI-HIERARCHY, M-SIMPLE-ABSTRACTIONS, C-COMMON-TRAITS, C-CONV-TRAITS, C-SEALED, C-OP-TRAITS
