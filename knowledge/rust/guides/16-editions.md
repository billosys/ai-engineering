# Rust Editions

How Rust evolves without breaking your code. A Rust edition is an opt-in, per-crate compatibility boundary (2015, 2018, 2021, 2024) that allows the language to introduce backwards-incompatible syntax and lint changes while preserving the stability guarantee. Each crate picks its own edition in `Cargo.toml`; crates on different editions interoperate seamlessly because all editions compile to the same internal IR and meet across ordinary function-call boundaries. Migration between editions is driven by `cargo fix --edition`, which runs edition-compatibility lints and applies fixes automatically — the compiler remains a single unified toolchain across every edition it supports.


## ED-01: An Edition Is an Opt-In Compatibility Boundary, Not a Language Version

**Strength**: CONSIDER

**Summary**: An edition is a per-crate syntactic profile. It is not a semver bump, not a minimum compiler version, and not a runtime or ABI choice.

```toml
# ✅ Cargo.toml — edition is a per-package field
[package]
name = "my_crate"
version = "0.1.0"
edition = "2024"         # purely a language-surface choice
rust-version = "1.85"    # this is the MSRV, tracked separately
```

```rust
// All editions compile to the same internal representation. Editions can:
//   - reserve keywords (async, await, dyn, gen)
//   - change path resolution rules
//   - promote lints from warn to error
//   - change default behaviors (closure capture, never fallback)
// Editions cannot change the ABI, the type system, or how compiled code runs.
```

**Rationale**: Treating an edition like a major version leads to wrong assumptions. The same `rustc` compiles every edition; upgrading the edition of *your* crate has no effect on dependents, and does not raise your MSRV by itself (though some edition features imply a minimum compiler). Think of it as a syntax profile the compiler reads per crate.

**See also**: ED-02, ED-03, Rust Reference "Editions"

---

## ED-02: Crates on Different Editions Interoperate via the Function Boundary

**Strength**: CONSIDER

**Summary**: Edition choice is private. A 2024 crate can depend on a 2015 crate and vice versa; the mutual surface is the function signature, not the source syntax.

```rust
// In crate A (edition = "2015")
pub fn compute(x: u32) -> u32 { x + 1 }

// In crate B (edition = "2024") — consumes A with zero ceremony
fn main() {
    let y = a::compute(41);   // works — signatures are edition-agnostic
    println!("{y}");
}
```

```rust
// Macros defined in crate A carry edition hygiene:
// tokens inside the macro are tagged with A's edition and
// parsed accordingly, even when expanded in a crate on a different edition.
```

**Rationale**: This is the "most consequential rule" of the edition system — without it, editions would fragment the ecosystem like Python 2/3. Because interoperability is guaranteed, library authors can stay on older editions without blocking downstream adoption, and you can upgrade your crate independently of your dependency graph.

**See also**: ED-01, ED-14, ED-guide "Editions do not split the ecosystem"

---

## ED-03: Use `cargo fix --edition` to Migrate

**Strength**: CONSIDER

**Summary**: The canonical migration is a five-step loop — update deps, run `cargo fix --edition`, bump the `edition` field, rebuild/retest, then reformat.

```console
# ✅ Canonical edition migration
$ cargo update                 # (1) refresh dependencies
$ cargo fix --edition          # (2) automatic source rewrites
#                                  edit Cargo.toml: edition = "20XX"   (3)
$ cargo build && cargo test    # (4) verify
$ cargo fmt                    # (5) reformat
```

```console
# ❌ Running cargo fix --edition without updating Cargo.toml
# The fixes are applied, but the crate is still on the old edition.
# You must manually set edition = "2024" (or the target year) afterward.
```

**Rationale**: `cargo fix --edition` runs `cargo check` with edition-compatibility lints enabled, then applies machine-applicable suggestions. It iterates: one round of fixes can unblock new warnings. If fixes fail to compile, Cargo backs them out automatically. What it *cannot* fix automatically: proc-macro internals, `macro_rules!` macros with tokens whose meaning shifts between editions, doctests, and build-script-generated code — those need hand-fixups.

**See also**: ED-04, ED-24 (Migration Checklist), Edition Guide Ch. 1

---

## ED-04: What `cargo fix --edition` Does *Not* Handle

**Strength**: CONSIDER

**Summary**: A handful of migrations require manual review — disjoint capture edge cases, tail-expression drop order, never-type fallback, APIT precise capturing, and some macros.

```rust
// ❌ cargo fix can't auto-fix this (tail_expr_drop_order):
fn f() {
    let x = (vec![0], vec![0]);
    let c = || drop(x.0);
    // Drop order of x.1 differs 2021 vs 2024 — needs human review.
}

// ❌ cargo fix can't auto-fix this (APIT + lifetime capture):
fn g<'a>(x: &'a (), y: impl Sized) -> impl Sized { (*x, y) }
// The anonymous impl Trait parameter needs a name before
// use<T> can be added — must convert to a named generic by hand.

// ❌ cargo fix can't auto-fix this (never fallback):
fn h<T: Default>() -> Result<T, ()> { Ok(T::default()) }
// h()?;     // 2021: T falls back to (); 2024: falls back to !
// Pick the intended T explicitly: h::<()>()?;
```

**Rationale**: The auto-fixer is deliberately conservative — it only applies rewrites that cannot change behavior. Anything involving drop ordering, type inference fallback, or anonymous generics must be decided by a human. Treat the list of flagged `rust-2024-compatibility` lints as a review checklist, not a todo list the compiler already finished.

**See also**: ED-03, ED-16, ED-19, ED-21

---

## ED-05: Pick the Latest Stable Edition for New Crates

**Strength**: SHOULD

**Summary**: `cargo new` defaults to the latest stable edition. Keep that default unless you need an older edition for a specific downstream constraint.

```toml
# ✅ New crates — accept the cargo new default
[package]
name = "new_crate"
version = "0.1.0"
edition = "2024"        # latest stable as of Rust 1.85
rust-version = "1.85"   # match the edition's minimum compiler
```

```toml
# ❌ Omitting `edition` — defaults to 2015, which you almost never want
[package]
name = "legacy_crate"
version = "0.1.0"
# (no edition field — silently uses Rust 2015)
```

**Rationale**: Newer editions resolve long-standing papercuts (disjoint captures, `if let` deadlocks, precise RPIT capture, unsafe-extern clarity). The cost is a higher MSRV, which is almost always acceptable for a new crate. Older editions are only appropriate when you must support an ancient toolchain that still ships with users.

**See also**: ED-01, ED-06

---

## ED-06: The Style Edition Is Independent from the Language Edition

**Strength**: CONSIDER

**Summary**: `rustfmt` has its own `style_edition`, governed by RFC 3338. Pin it in `rustfmt.toml` so editor-format-on-save and CI produce identical output.

```toml
# ✅ rustfmt.toml — pin the style edition for the whole repo
style_edition = "2024"
```

```console
# Invocation equivalents
$ cargo fmt                             # uses the crate's Cargo.toml edition
$ rustfmt lib.rs --edition 2024         # both parsing and style
$ rustfmt lib.rs --style-edition 2024   # style only, parse as default
```

```rust
// 2021 style                                // 2024 style
use std::num::{NonZeroU16, NonZeroU32,       use std::num::{NonZeroU8, NonZeroU16,
               NonZeroU64, NonZeroU8};                      NonZeroU32, NonZeroU64};
// ASCIIbetical — NonZeroU8 sorts last      // version sort — numeric order
```

**Rationale**: Before RFC 3338, rustfmt was locked by its stability guarantee: any formatting bug was permanent. The style edition decouples formatting evolution from the language: the 2024 style edition fixes ~15 accumulated formatting issues (version-sort imports, raw-identifier sorting, nested-tuple spacing, indent regressions). Without a project-level `rustfmt.toml`, editors often invoke rustfmt directly and fall back to style 2015 while `cargo fmt` uses 2024, producing a flip-flop on save.

**See also**: ED-22, Rust Style Guide Ch. 8

---

## ED-07: Rust 2015 Is the Default When `edition` Is Absent

**Strength**: CONSIDER

**Summary**: A `Cargo.toml` with no `edition` field uses Rust 2015 — not the latest. `cargo new` writes the field explicitly; hand-written manifests frequently do not.

```toml
# ✅ Explicit — no ambiguity
[package]
name = "foo"
version = "0.1.0"
edition = "2024"
```

```toml
# ⚠️ Missing field — silently falls back to edition = "2015"
[package]
name = "foo"
version = "0.1.0"
```

**Rationale**: The 2015 default exists for backwards compatibility with pre-edition manifests; it should not be the edition you end up on by accident. Always write the field explicitly — it's one line, and it prevents a subtle class of bugs where 2015-era path semantics or missing ergonomics mysteriously apply.

**See also**: ED-05, ED-08

---

## ED-08: Rust 2015 Baseline — `extern crate` and Anchored Paths

**Strength**: AVOID

**Summary**: Rust 2015 predates the module-path overhaul: `extern crate` is required, `use` paths are anchored at the crate root, and trait methods allow anonymous parameters. Don't write new code this way.

```rust
// Rust 2015 (don't write new code this way)
extern crate rand;                  // ❌ required in 2015, redundant in 2018+

use rand::Rng;                      // anchored at crate root
mod submodule {
    use ::chrono::Utc;              // :: prefix meant crate root / external
}

trait Foo {
    fn foo(&self, u8);              // ❌ anonymous parameter allowed in 2015
}
```

```rust
// Rust 2018+ equivalent — idiomatic today
use rand::Rng;                      // implicit extern; modern path resolution
mod submodule {
    use chrono::Utc;                // crate names in scope everywhere
}

trait Foo {
    fn foo(&self, _value: u8);      // ✅ parameter must be named
}
```

**Rationale**: 2015 is supported forever, but the ergonomics are actively worse: `extern crate` boilerplate, path-resolution surprises in submodules, and weaker trait-method checking. Treat 2015 as a compatibility target for old crates you maintain, not a style you emulate.

**See also**: ED-09, ED-10, Edition Guide Ch. 2

---

## ED-09: Rust 2018 — `dyn Trait` Is Required for Trait Objects

**Strength**: CONSIDER

**Summary**: The bare-trait syntax (`Box<Error>`) was deprecated in 2018 and is a hard error in 2021+. Always write `dyn Trait`.

```rust
// ❌ Rust 2015 style — ambiguous with impl Trait
fn boxed() -> Box<std::error::Error> { todo!() }
fn borrowed(x: &std::error::Error) { /* ... */ }

// ✅ Rust 2018+ — explicit dynamic dispatch
fn boxed() -> Box<dyn std::error::Error> { todo!() }
fn borrowed(x: &dyn std::error::Error) { /* ... */ }
```

**Rationale**: `dyn Trait` makes the static/dynamic dispatch distinction symmetric with `impl Trait`. Without `dyn`, the reader can't tell at a glance whether `Box<Error>` is monomorphized or a vtable. The 2021 edition promoted `bare_trait_objects` from warning to hard error; `cargo fix --edition` rewrites these automatically.

**See also**: ED-12, Edition Guide Ch. 3 "New keywords"

---

## ED-10: Rust 2018 — Module Paths Work the Same Everywhere

**Strength**: CONSIDER

**Summary**: In 2018+, `use` paths don't need a `::crate_name::` prefix, external crates are in scope in every module, and `crate::` means "root of this crate." `mod.rs` is no longer required.

```rust
// ✅ Rust 2018+ module paths
mod submodule {
    use chrono::Utc;                  // external crate in scope everywhere
    use crate::helpers::log;          // crate:: = root of current crate
    use super::sibling::thing;        // super:: = parent module
}

// ✅ foo.rs and foo/bar.rs coexist — no foo/mod.rs needed
// src/
//   lib.rs
//   foo.rs            <- module foo's body
//   foo/
//     bar.rs          <- child module foo::bar
```

```rust
// ❌ 2015 idioms that 2018+ made unnecessary
extern crate chrono;
mod submodule {
    use ::chrono::Utc;                // :: used to mean crate-root-or-external
}
```

**Rationale**: The 2015 module system was the #1 friction point for new Rust programmers. 2018 unified the rules: paths in `use` behave like paths anywhere else, external crates are just names, and `crate::` is an unambiguous self-reference. This one change accounts for most of why 2015 code "feels" different.

**See also**: ED-09, ED-11

---

## ED-11: Rust 2018 — `async`/`await` Keywords (Feature Landed in 1.39)

**Strength**: CONSIDER

**Summary**: 2018 reserved `async`, `await`, and `try` as keywords. The actual `async fn`/`.await` feature shipped later, in Rust 1.39 (November 2019) — the reservation made room for it without another edition bump.

```rust
// ❌ 2015 usage that's illegal in 2018+
// let async = 1;              // `async` is a reserved keyword
// fn try() { }                // `try` is reserved (future `try` blocks)

// ✅ Escape hatch — raw identifiers preserve the name
let r#async = 1;
fn r#try() { }

// ✅ The actual feature (Rust 1.39.0+)
async fn fetch() -> u32 { 42 }
let fut = fetch();
let v = fut.await;
```

**Rationale**: Reserving keywords in one edition and landing the feature in a later minor release is a core edition pattern — see also `gen` in 2024 (ED-19). `cargo fix --edition` rewrites any identifier named `async`/`await`/`try` to the raw form automatically.

**See also**: ED-19, Edition Guide Ch. 3

---

## ED-12: Rust 2021 — `IntoIterator for [T; N]` Makes `array.into_iter()` By-Value

**Strength**: CONSIDER

**Summary**: Since Rust 1.53 every edition sees `for x in [1, 2, 3]` yield values. But `array.into_iter()` as a *method call* only iterates by value on edition 2021+; on 2015/2018 it still deref-resolves to `(&array).into_iter()`.

```rust
// ✅ Works by value in every edition (since Rust 1.53)
for x in [1u8, 2, 3] { /* x: u8 */ }
let _ = IntoIterator::into_iter([1, 2, 3]);

// ✅ Edition 2021+ method syntax — by value
let a = [1u8, 2, 3];
for x in a.into_iter() { /* x: u8 (2021+) / &u8 (2015, 2018) */ }

// ✅ Edition-independent way to iterate by reference
for x in a.iter() { /* x: &u8 in all editions */ }
```

**Rationale**: The real trait impl was added in all editions for consistency (you can't have an impl exist in one edition but not another — editions mix). The 2021-gated piece is only the legacy method-call resolution that used to deref arrays to slice references. If you want by-reference behavior, say `.iter()` — it reads more clearly anyway.

**See also**: ED-22 (analogous `Box<[T]>` change in 2024)

---

## ED-13: Rust 2021 — Disjoint Closure Captures

**Strength**: CONSIDER

**Summary**: On edition 2021+, closures capture individual field paths (`a.x`) rather than the whole variable (`a`). This enables previously-rejected code and can change drop order and closure trait impls.

```rust
// ✅ Compiles in 2021; rejected in 2018 (would capture all of `a`)
struct S { x: Vec<i32>, y: String }
let a = S { x: vec![1], y: String::from("hi") };
drop(a.x);                              // move one field
let c = || println!("{}", a.y);         // 2021: captures only a.y
c();

// ⚠️ Trait-impl shift — wrapper was Send, raw field isn't
struct Ptr(*mut i32);
unsafe impl Send for Ptr {}
let px = Ptr(std::ptr::null_mut());
// 2018: closure captures `px` (Send) — thread::spawn OK
// 2021: closure captures px.0 (*mut i32, !Send) — may fail
let c = move || { let _ = &px; /* force whole-px capture */ };

// ✅ Force whole-variable capture: `let _ = &x` is NOT a no-op
let x = (vec![22], vec![23]);
let c = move || {
    let _ = &x;                         // forces x to be captured intact
    println!("{:?}", x.0);
};
```

**Rationale**: RFC 2229 made captures precise, which is almost always what you want. The two gotchas — drop order (fields not captured drop with the outer variable, not the closure) and auto-trait shifts (`Send`/`Sync`/`Clone` are now per-captured-field) — are exactly why `cargo fix --edition` conservatively inserts `let _ = &var;` dummy bindings. After migration, review each dummy let and delete the ones whose variable has no side-effectful `Drop`.

**See also**: ED-04, Edition Guide Ch. 4 RFC 2229

---

## ED-14: Rust 2021 — Feature Resolver v2 Becomes Default

**Strength**: CONSIDER

**Summary**: On edition 2021, `resolver = "2"` is implied. Features no longer unify across `[dependencies]`, `[build-dependencies]`, `[dev-dependencies]`, and proc-macros — each kind resolves independently. Virtual workspaces must still set it explicitly.

```toml
# ✅ Edition 2021 top-level package — resolver = "2" is implicit
[package]
name = "app"
edition = "2021"

# ⚠️ Virtual workspace — must be explicit
[workspace]
resolver = "2"
members = ["crate-a", "crate-b"]
```

```toml
# Common breakage pattern — a build-dependency used to leak features.
# Under resolver v2 you must request the feature where you need it.
[dependencies]
bstr = { version = "1", default-features = false, features = ["unicode"] }
```

```console
# Diagnostic commands
$ cargo tree -d                        # packages built multiple times
$ cargo tree -f '{p} {f}'              # features per package
$ cargo tree -e features -i bstr       # where a feature flows in from
```

**Rationale**: v1 unified all features for a crate regardless of how it was pulled in — convenient, but meant unrelated build-deps could silently enable runtime features (bloating size, changing behavior). v2 resolves per dependency kind, which is correct but sometimes means `A.needs("x")` no longer works just because some transitive build-dep happened to request `x`. No auto-fix exists — you add the features back explicitly.

**See also**: ED-23 (resolver v3 in 2024)

---

## ED-15: Rust 2021 — Prelude Adds `TryFrom`, `TryInto`, `FromIterator`

**Strength**: CONSIDER

**Summary**: On edition 2021+, `TryFrom`, `TryInto`, and `FromIterator` are in scope without `use`. If you had a local trait with conflicting method names, resolve the ambiguity with fully qualified syntax.

```rust
// ✅ 2021+: no import required
let n: i32 = i64::try_from(100_i64).unwrap();
let s: String = ['a', 'b'].into_iter().collect();

// ⚠️ Ambiguity only when a user trait shadows a prelude method name
trait MyFromIter<A> { fn from_iter(x: Option<A>); }
impl<T> MyFromIter<()> for Vec<T> {
    fn from_iter(_: Option<()>) {}
}

// ❌ Ambiguous in 2021: MyFromIter::from_iter vs FromIterator::from_iter
// Vec::<i32>::from_iter(None);

// ✅ Fully qualified syntax picks a winner
<Vec<i32> as MyFromIter<()>>::from_iter(None);
```

**Rationale**: Adding items to the prelude is non-breaking unless the item is a trait (inherent/manually-imported items always win). Only traits can silently collide via method resolution, which is why this was deferred to an edition. Inherent methods still take precedence over prelude-trait methods, so most codebases needed zero changes.

**See also**: ED-22 (`Future`/`IntoFuture` in 2024 prelude)

---

## ED-16: Rust 2021 — Panic/Assert Always Format Their First Argument

**Strength**: CONSIDER

**Summary**: On edition 2021+, `panic!`/`assert!`/`unreachable!` treat the first argument as a format string, just like `println!`. Single non-string arguments must use `std::panic::panic_any`.

```rust
// ❌ 2018 allowances that are errors in 2021+
// panic!("Value: {}");          // error — missing format argument
// panic!(my_error);             // error — must be a string literal
// panic!(123);                  // error — not a format string

// ✅ 2021+ equivalents
panic!("Value: {{}}");                         // escape the braces
panic!("{}", my_error);                        // format via Display
std::panic::panic_any(123);                    // non-string payload (function, not macro!)

// ✅ Implicit format args — only works after this change
let name = "world";
panic!("hello {name}");                        // interpolates `name`
```

**Rationale**: The pre-2021 behavior was inconsistent: single-arg `panic!(x)` treated `x` as opaque, but multi-arg `panic!("{}", x)` formatted. That meant `panic!("hello {name}")` would panic with the literal string "hello {name}" rather than interpolating — directly incompatible with the implicit-format-args feature (RFC 2795). The 2021 change also unifies `core::panic!` and `std::panic!`, removing a `#![no_std]` toggle footgun.

**See also**: Rust 1.50+ `non_fmt_panics` lint

---

## ED-17: Rust 2021 — Reserved Prefix Syntax and C-String Literals

**Strength**: CONSIDER

**Summary**: Edition 2021+ reserves `ident"..."`, `ident#foo`, and `ident'c'` as syntax errors, leaving room for future features. The first beneficiary: `c"..."` C-string literals (stable in Rust 1.77+).

```rust
// ❌ 2018 macros tokenized `z"hey"` as two tokens (`z`, "hey");
//    2021 makes any `prefix"..."` sequence a reservation — insert a space.
// my_macro!(z"hey");       // 2021: error — reserved prefix
// my_macro!(z "hey");      // ✅ space disambiguates

// ✅ C-string literals (Rust 1.77+, requires edition 2021)
use core::ffi::CStr;

let s: &CStr = c"hello";                          // NUL-terminated automatically
let r: &CStr = cr"C:\path\with\backslashes";      // raw C-string
let q: &CStr = cr#""quoted""#;                    // # delimiter for interior "
assert_eq!(s, CStr::from_bytes_with_nul(b"hello\0").unwrap());
```

**Rationale**: Reserving prefix syntax in 2021 meant features like `c"..."`, and potentially `f"hello {name}"` or `s"..."` in the future, don't need their own edition boundary. C-string literals replaced a cottage industry of `cstr!()` proc macros and hand-rolled `from_bytes_with_nul(b"...\0")` calls. Interior NUL bytes are rejected at compile time.

**See also**: ED-19 (same reservation mechanism extended in 2024)

---

## ED-18: Rust 2024 — RPIT Captures All In-Scope Lifetimes (Use `use<>` to Opt Out)

**Strength**: CONSIDER

**Summary**: On edition 2024+, a bare-function `impl Trait` return captures every in-scope generic parameter, including lifetimes. Use `+ use<...>` to narrow the capture set, or `+ use<>` for none.

```rust
// ✅ 2024 default: 'a is captured
fn f<'a>(x: &'a ()) -> impl Sized { *x }
// equivalent to:
fn f_explicit<'a>(x: &'a ()) -> impl Sized + use<'a> { *x }

// ✅ Opt out of capturing 'a — the returned opaque is 'static-friendly
fn g<'a>(x: &'a ()) -> impl Sized + use<> { *x }

// ✅ Replace the old Captures / outlives tricks
// Old: fn h<'a, T>(x: &'a (), y: T) -> impl Sized + Captures<(&'a (), T)>
fn h<'a, T>(x: &'a (), y: T) -> impl Sized + use<'a, T> { (x, y) }

// ⚠️ APIT case — cargo fix can't handle; convert to a named generic first
// Before: fn k<'a>(x: &'a (), y: impl Sized) -> impl Sized { (*x, y) }
fn k<'a, T: Sized>(x: &'a (), y: T) -> impl Sized + use<T> { (*x, y) }
```

**Rationale**: This is the single largest language change in 2024. Previously, bare-function RPIT inconsistently captured lifetimes (only those syntactically in a bound), while trait-impl RPIT, RPITIT, and `async fn` already captured everything. Unifying the rules eliminates the `Captures<...>` and `T: 'a` workarounds. `cargo fix --edition` auto-inserts `use<>` on affected functions to preserve 2021 semantics; `use<..>` bounds themselves are stable since 1.82 in every edition.

**See also**: RFC 3498, RFC 3617

---

## ED-19: Rust 2024 — `if let` Temporaries Drop Before `else`; Tail Expressions Drop Early

**Strength**: CONSIDER

**Summary**: On edition 2024+, scrutinee temporaries in `if let … else` are dropped before the `else` branch executes, and tail-expression temporaries can be dropped before local variables. `let` chains become available as a side effect.

```rust
use std::sync::RwLock;

// ✅ 2024: read lock released before `else` — no deadlock
fn try_set(lock: &RwLock<Option<bool>>) {
    if let Some(v) = *lock.read().unwrap() {
        println!("have {v}");
    } else {
        let mut w = lock.write().unwrap();          // 2021: DEADLOCK
        if w.is_none() { *w = Some(true); }         // 2024: fine
    }
}

// ✅ 2024: let chains — enabled by the if-let rescoping
fn first_two(xs: &[u8]) -> Option<u8> {
    let mut it = xs.iter();
    if let Some(a) = it.next() && let Some(b) = it.next() {
        a.checked_add(*b)
    } else { None }
}

// ⚠️ Tail-expression drop change — both directions possible
use std::cell::RefCell;
fn len() -> usize {
    let c = RefCell::new(String::from(".."));
    c.borrow().len()          // 2021: error — c drops before Ref; 2024: compiles
}

// ❌ Regression — compiles in 2021, fails in 2024
// let x = { &String::from("1234") }.len();
// Fix: lift the temporary to a let binding
let s = String::from("1234");
let x = s.len();
```

**Rationale**: `if let` deadlock-through-the-else-branch was the single most-reported ergonomic bug with lock guards. The fix has a cost: the `tail_expr_drop_order` lint cannot auto-rewrite, because there's no semantics-preserving transform. Treat its warnings as a manual-review list — drop order only matters for types with side-effectful `Drop`, but those are exactly where silent changes bite.

**See also**: ED-04, RFC 3606

---

## ED-20: Rust 2024 — Never-Type Fallback Flips from `()` to `!`

**Strength**: CONSIDER

**Summary**: When the compiler coerces `!` to a type it cannot infer, it now defaults to `!` instead of `()`. Most code is unaffected, but a few patterns (`f()?` with generic `Ok`, always-panicking closures) break and need explicit types.

```rust
// Pattern 1: generic ? operator
fn f<T: Default>() -> Result<T, ()> { Ok(T::default()) }
// f()?;                         // 2021: T = (); 2024: T = ! (no Default for !)
let _: () = f()?;                // ✅ fix — annotate the consumer

// Pattern 2: closure that always panics
trait Unit {}
impl Unit for () {}
fn run<R: Unit>(_: impl FnOnce() -> R) {}
// run(|| panic!());             // 2021: R = (); 2024: R = ! (not Unit)
run(|| -> () { panic!() });       // ✅ fix — annotate the closure return

// Pattern 3: one branch diverges, the other is unconstrained
// if cond { Default::default() } else { return };    // 2024: T = !, no Default
let _: () = if true { Default::default() } else { return };  // ✅
```

**Rationale**: The `()` fallback blocked stabilization of `!` as a proper type and produced surprising inferences (`{ panic!() };` silently evaluating as `()`). There's no auto-fix: the remedy is always "tell the compiler which concrete type you meant," which it cannot guess. The plan is to make this change apply to all editions eventually — enabling `#![warn(dependency_on_unit_never_type_fallback)]` before the migration surfaces every affected site.

**See also**: ED-04

---

## ED-21: Rust 2024 — `unsafe` Becomes More Explicit in Four Places

**Strength**: CONSIDER

**Summary**: `extern` blocks must be `unsafe extern`, several attributes must use `#[unsafe(...)]`, `unsafe_op_in_unsafe_fn` warns by default, and references to `static mut` are denied.

```rust
// ✅ unsafe extern blocks — items default to unsafe; mark individually
unsafe extern "C" {
    pub safe fn sqrt(x: f64) -> f64;                          // callable safely
    pub unsafe fn strlen(s: *const std::ffi::c_char) -> usize;
    pub fn free(p: *mut std::ffi::c_void);                    // defaults to unsafe
    pub safe static IMPORTANT_BYTES: [u8; 256];
}

// ✅ unsafe attributes — symbol-affecting attrs are now explicitly unsafe
#[unsafe(no_mangle)]
pub fn exported() {}

// ✅ unsafe_op_in_unsafe_fn — body must wrap unsafe ops even inside unsafe fn
unsafe fn get_unchecked<T>(s: &[T], i: usize) -> &T {
    unsafe { s.get_unchecked(i) }                              // explicit now required
}

// ❌ static mut references — denied in 2024 (was UB even in 2021)
// static mut COUNTER: u64 = 0;
// let r = unsafe { &COUNTER };                               // denied
// ✅ Replacements
use std::sync::atomic::{AtomicU64, Ordering};
static COUNTER: AtomicU64 = AtomicU64::new(0);
COUNTER.fetch_add(1, Ordering::Relaxed);

// For raw addresses of mutable statics, use &raw const / &raw mut
static mut GLOBAL: i32 = 0;
let ptr = &raw const GLOBAL;                                   // ✅ not a reference
```

**Rationale**: Each change closes a specific hole: extern-block signatures are promises the author can't fully verify, symbol-affecting attributes can silently replace the allocator, `unsafe fn` historically conflated "caller must be careful" with "body has free access to unsafe ops," and *taking* a reference to `static mut` is instantaneous UB (not just reading/writing it). `cargo fix --edition` wraps existing code in the new syntax, but `static_mut_refs` often requires a behavioral replacement (atomic / `Mutex` / `OnceLock`).

**See also**: US-guide (unsafe Rust), RFC 3484, RFC 3325, RFC 2585

---

## ED-22: Rust 2024 — Prelude Adds `Future`/`IntoFuture`; `Box<[T]>::into_iter()` Flips

**Strength**: CONSIDER

**Summary**: The 2024 prelude adds `Future` and `IntoFuture`; `Box<[T]>` gains `IntoIterator` with edition-dependent `.into_iter()`; `std::env::set_var`/`remove_var` become `unsafe`.

```rust
// ✅ Future / IntoFuture in prelude — no import needed
async fn fetch() -> u32 { 42 }
let fut = fetch();
// let value = fut.await;   // inside an async context

// ⚠️ Method ambiguity — only from glob imports, not explicit use
mod custom {
    pub trait MyPoller { fn poll(&self); }
    impl<T> MyPoller for T {}
}
// use custom::*;                     // ambiguous with Future::poll
// fully qualified syntax resolves:
// <_ as custom::MyPoller>::poll(&fut);

// ⚠️ Box<[T]> — same shape as arrays-in-2021 (ED-12)
let b: Box<[u32]> = vec![1, 2, 3].into_boxed_slice();
for x in b.iter() { /* x: &u32 — all editions */ }
let c: Box<[u32]> = vec![1, 2, 3].into_boxed_slice();
for x in c { /* x: u32 in all editions since 1.80 */ }
// method call is edition-gated:
// c.into_iter() — 2021: &u32; 2024: u32

// ⚠️ set_var is unsafe — process env isn't thread-safe on POSIX
// std::env::set_var("FOO", "1");            // 2024: error
unsafe { std::env::set_var("FOO", "1"); }   // ✅ audit single-threadedness
```

**Rationale**: The prelude additions are low-collision (inherent methods and explicit imports shadow the prelude). The `Box<[T]>` shim mirrors the 2021 array change — `for x in box_slice` already yielded values since 1.80; only the method-call form was deferred. Environment variables being `unsafe` reflects a genuine soundness bug: `setenv` is UB to call concurrently with any other `getenv`/`setenv`, and parallel test harnesses have hit this in production.

**See also**: ED-12, ED-15, ED-21

---

## ED-23: Rust 2024 — Cargo Resolver v3 and Manifest Cleanup

**Strength**: CONSIDER

**Summary**: Edition 2024 implies `resolver = "3"` (Rust-version-aware dependency selection). Hyphenated keys replace underscored variants. Inherited `default-features = false` without workspace-level opt-out is a hard error.

```toml
# ✅ 2024 package — resolver = "3" is implicit
[package]
name = "app"
edition = "2024"
rust-version = "1.85"             # resolver v3 uses this when picking versions

# ⚠️ Virtual workspaces — still need resolver explicit
[workspace]
resolver = "3"
members = ["a", "b"]
```

```toml
# ❌ Removed in 2024 (underscore variants no longer accepted)
# [project]                       use [package]
# [dev_dependencies]              use [dev-dependencies]
# [build_dependencies]            use [build-dependencies]
# default_features = false        use default-features = false
# crate_type = ...                use crate-type = ...
# proc_macro = true               use proc-macro = true
```

```toml
# ❌ 2024 error — default-features = false on the inheritor
# only works when the workspace also sets it to false
[workspace.dependencies]
regex = "1.10"

[dependencies]
# regex = { workspace = true, default-features = false }    # ERROR in 2024

# ✅ Either set it workspace-wide:
#   [workspace.dependencies]
#   regex = { version = "1.10", default-features = false }
# or omit it from the package (it never had effect before either).
```

**Rationale**: Resolver v3 prefers dependency versions whose `rust-version` is compatible with yours, falling back to incompatible ones only when nothing compatible exists. Combined with `rust-version = "1.85"` in your manifest, this makes `cargo update` dramatically safer for downstream CI. The key/table cleanup removes years of historical-artifact duplicate names.

**See also**: ED-14 (resolver v2)

---

## ED-24: Rust 2024 — `gen` Keyword Reserved, Fragment Specifiers, and `unsafe_op_in_unsafe_fn`

**Strength**: CONSIDER

**Summary**: 2024 reserves `gen` for future generator blocks, changes the `:expr` macro fragment specifier, and elevates `unsafe_op_in_unsafe_fn` from opt-in to default warn.

```rust
// ❌ gen as an identifier — disallowed in 2024
// fn gen() { }
// ✅ use raw identifier or rename
fn r#gen() { }

// ⚠️ Macro fragment specifier — :expr now matches `const { ... }` and `_`
macro_rules! example {
    ($e:expr)        => { "new behavior — matches const { 1+1 } and _" };
    (const $e:expr)  => { "specific const rule" };
}
// If you needed 2021 matching behavior, use :expr_2021:
macro_rules! legacy {
    ($e:expr_2021)   => { "2021 expr matching preserved" };
}

// ✅ unsafe_op_in_unsafe_fn — now default warn (deny on migration)
// (See ED-21 for the full shape.)
```

**Rationale**: `gen` reservation follows the `async`/`await` playbook (ED-11): reserve the keyword in one edition, stabilize the feature later. `:expr` growing to match const blocks and `_` is the normal evolution; `:expr_2021` is a permanent preservation specifier, not a temporary shim. `missing_fragment_specifier` (e.g., `$e:` with nothing after) also becomes a hard error — these were accepted-but-meaningless tokens for too long.

**See also**: ED-11, ED-21


## Migration Checklist

A concrete sequence for moving a crate from 2021 to 2024 (the same template works for any upgrade):

```rust
// 1. Preflight
//    - Ensure `cargo check --all-targets --all-features` is clean on 2021.
//    - Check MSRV: edition 2024 needs rustc >= 1.85. Update `rust-version`.

// 2. Enable the compatibility lints *before* switching the edition.
#![warn(rust_2024_compatibility)]
// (Or on the command line: RUSTFLAGS="-W rust-2024-compatibility")
// Pay particular attention to lints with no auto-fix:
//   - tail_expr_drop_order
//   - dependency_on_unit_never_type_fallback
//   - impl_trait_overcaptures (APIT cases)

// 3. Run the automatic migration.
//    $ cargo update
//    $ cargo fix --edition
//    $ cargo fix --edition --all-targets --all-features
//    Repeat with different --target and --features if your code is cfg-heavy.

// 4. Flip the edition.
//    Cargo.toml:
//      [package]
//      edition = "2024"

// 5. Rebuild and retest.
//    $ cargo build --all-targets --all-features
//    $ cargo test --all-targets --all-features

// 6. Manual review — items cargo fix flagged but could not rewrite:
//    - tail_expr_drop_order warnings: audit each; only matters for
//      types with side-effectful Drop (locks, file handles, channels).
//    - never-type fallback: add explicit type annotations where T inferred via !.
//    - RPIT + APIT: rename anonymous `impl Trait` parameters to named generics,
//      then re-run cargo fix to add `+ use<...>` bounds.
//    - static_mut_refs: replace with atomics / Mutex / OnceLock.
//    - Disjoint-capture dummy lets inserted by cargo fix: many can be deleted
//      if the variable has no side-effectful Drop.

// 7. Reformat with the new style edition.
//    rustfmt.toml:
//      style_edition = "2024"
//    $ cargo fmt
//    Commit formatting separately from functional changes — the diff is large.

// 8. Virtual workspaces only: set resolver explicitly.
//    [workspace]
//    resolver = "3"

// 9. CI: run with `--locked` (reproducibility) AND unlocked (catch latest-dep
//    issues — especially relevant after resolver v3 changes selection).
```


## Summary Table

| Card | Edition | Key Point |
|------|---------|-----------|
| ED-01 Edition is an opt-in compatibility boundary | all | Per-crate, syntactic, same compiler |
| ED-02 Editions interoperate via function boundary | all | Edition choice is private; macros have hygiene |
| ED-03 `cargo fix --edition` drives migration | all | 5-step loop: update, fix, bump, verify, format |
| ED-04 What `cargo fix` does *not* handle | all | Drop order, never fallback, APIT, some macros |
| ED-05 New crates take the latest edition | all | Accept `cargo new` default |
| ED-06 Style edition is independent | 2024 | Pin `style_edition` in `rustfmt.toml` |
| ED-07 2015 is the absent-field default | 2015 | Write the `edition` key explicitly |
| ED-08 2015 baseline — `extern crate`, anchored paths | 2015 | Legacy; don't emulate for new code |
| ED-09 2018 requires `dyn Trait` | 2018 | Bare `Trait` is error in 2021+ |
| ED-10 2018 module paths unified | 2018 | `crate::`, no `mod.rs`, external names in scope |
| ED-11 2018 reserved `async`/`await`/`try` | 2018 | Feature landed in 1.39; raw idents as escape |
| ED-12 2021 `array.into_iter()` by value | 2021 | Only method syntax is edition-gated |
| ED-13 2021 disjoint closure captures | 2021 | Drop order / Send shifts; `let _ = &x` to force full capture |
| ED-14 2021 feature resolver v2 | 2021 | Features no longer unify across dep kinds |
| ED-15 2021 prelude adds `TryFrom`/`TryInto`/`FromIterator` | 2021 | Fully qualified syntax resolves trait conflicts |
| ED-16 2021 panic/assert always format | 2021 | `panic_any` for non-string payloads |
| ED-17 2021 reserved prefix syntax; c-strings | 2021 | `c"..."` / `cr"..."` since 1.77 |
| ED-18 2024 RPIT captures in-scope lifetimes | 2024 | `+ use<...>` to narrow, `+ use<>` for none |
| ED-19 2024 `if let` temporary scope | 2024 | Deadlock-through-else fixed; `let` chains enabled |
| ED-20 2024 never-type fallback flips to `!` | 2024 | Annotate `f::<()>()?` and closure returns |
| ED-21 2024 explicit `unsafe` | 2024 | `unsafe extern`, `#[unsafe(no_mangle)]`, `unsafe{}` in `unsafe fn`, no `&static mut` |
| ED-22 2024 prelude adds `Future`/`IntoFuture`; `Box<[T]>` iter | 2024 | `set_var` now `unsafe` |
| ED-23 2024 cargo resolver v3; manifest cleanup | 2024 | `rust-version`-aware; hyphen-only keys |
| ED-24 2024 `gen` reserved; `:expr` change | 2024 | `:expr_2021` preserves old macro behavior |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for derive, trait impls, and idioms that assume modern editions.
- **API Design**: See `02-api-design.md` for public-API conventions — prelude-trait method names, `dyn Trait` in signatures, `use<..>` in return types.
- **Type Design**: See `05-type-design.md` — `#[non_exhaustive]`, builders, and typestate interact with edition-level language surface.
- **Project Structure**: See `12-project-structure.md` for workspace setup, `Cargo.toml` conventions, and resolver selection.


## External References

- [The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)
- [The Rust Reference — Editions](https://doc.rust-lang.org/reference/editions.html)
- [The Cargo Book — the `edition` field](https://doc.rust-lang.org/cargo/reference/manifest.html#the-edition-field)
- [The Cargo Book — Resolver versions](https://doc.rust-lang.org/cargo/reference/resolver.html#resolver-versions)
- [RFC 2052 — Epochs (the edition system)](https://rust-lang.github.io/rfcs/2052-epochs.html)
- [RFC 3085 — Rust 2021 Edition](https://rust-lang.github.io/rfcs/3085-edition-2021.html)
- [RFC 3501 — Rust 2024 Edition](https://rust-lang.github.io/rfcs/3501-edition-2024.html)
- [RFC 2229 — Disjoint closure captures](https://rust-lang.github.io/rfcs/2229-capture-disjoint-fields.html)
- [RFC 3498 — Lifetime capture rules in RPIT](https://rust-lang.github.io/rfcs/3498-lifetime-capture-rules-2024.html)
- [RFC 3617 — Precise capturing with `use<>`](https://rust-lang.github.io/rfcs/3617-precise-capturing.html)
- [RFC 3338 — `style_edition` in rustfmt](https://rust-lang.github.io/rfcs/3338-style-evolution.html)
- [RFC 3484 — Unsafe extern blocks](https://rust-lang.github.io/rfcs/3484-unsafe-extern-blocks.html)
- [RFC 3325 — Unsafe attributes](https://rust-lang.github.io/rfcs/3325-unsafe-attributes.html)
- [RFC 2585 — `unsafe_op_in_unsafe_fn`](https://rust-lang.github.io/rfcs/2585-unsafe-block-in-unsafe-fn.html)
- [RFC 3513 — `gen` blocks](https://rust-lang.github.io/rfcs/3513-gen-blocks.html)
- [RFC 3606 — Tail expression temporary scope](https://rust-lang.github.io/rfcs/3606-tail-expr-temps.html)
