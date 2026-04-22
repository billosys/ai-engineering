# Macros

Guidelines for writing and consuming Rust macros: declarative `macro_rules!` for syntactic pattern-matching, procedural macros for arbitrary compile-time code generation, and the hygiene, scoping, and design trade-offs that make macros work (or fail) in practice.


## MC-01: Prefer Functions, Generics, and `const fn` Before Macros

**Strength**: MUST

**Summary**: Reach for a macro only when functions, generics, traits, or `const fn` genuinely cannot express the feature. Macros are harder to read, debug, type-check, and document.

```rust
// ❌ BAD: macro where a generic function would work
macro_rules! add {
    ($a:expr, $b:expr) => { $a + $b };
}

// ✅ GOOD: a generic function — typed, documented, debuggable
fn add<T: std::ops::Add<Output = T>>(a: T, b: T) -> T {
    a + b
}

// ✅ GOOD: macro where syntax sugar is the whole point
macro_rules! hashmap {
    ($($k:expr => $v:expr),* $(,)?) => {{
        let mut m = ::std::collections::HashMap::new();
        $( m.insert($k, $v); )*
        m
    }};
}

let m = hashmap! { "a" => 1, "b" => 2 };
```

**Rationale**: Functions give you type inference, error messages pointing at the bug, step-through debugging, and rustdoc. Macros bypass all of that. Legitimate reasons to reach for a macro: variable-arity syntax (`vec!`, `println!`), eager-formatted diagnostics, compile-time code generation (derive), or DSLs that cannot be typed.

**See also**: MC-18 (when to use `macro_rules!`), MC-19 (when to use proc-macros)

---

## MC-02: Choose Declarative vs Procedural by Complexity

**Strength**: SHOULD

**Summary**: Use `macro_rules!` for pattern-based syntactic sugar. Use procedural macros when you need to inspect structure, generate trait `impl`s, or transform arbitrary items.

```rust
// ✅ Declarative — pattern substitution
macro_rules! vec_of_strings {
    ($($x:expr),* $(,)?) => { vec![$($x.to_string()),*] };
}

// ✅ Procedural — introspection + code generation
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(Builder)]
pub fn derive_builder(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    quote! {
        impl #name {
            pub fn builder() -> /* ... */ { todo!() }
        }
    }.into()
}
```

**Rationale**: `macro_rules!` is simpler to write, requires no separate crate, and produces better-looking error messages — but cannot inspect type structure. Proc-macros can parse the input into an AST via `syn` and generate arbitrary output — but require a dedicated `proc-macro = true` crate, cost compile time, and produce worse error messages.

**See also**: MC-18, MC-19


---

## MC-03: Learn the Fragment Specifiers

**Strength**: MUST

**Summary**: Each metavariable `$name:kind` uses a fragment specifier that tells the parser what to match. Pick the most specific one that covers the inputs you expect.

```rust
// The standard fragment specifiers
macro_rules! showcase {
    ($e:expr)     => { /* any expression */ };
    ($s:stmt)     => { /* a statement without trailing ; */ };
    ($b:block)    => { /* {...} block */ };
    ($p:pat)      => { /* any pattern (2021+: top-level or-patterns) */ };
    ($t:ty)       => { /* a type */ };
    ($i:ident)    => { /* identifier or keyword (not _) */ };
    ($pa:path)    => { /* path like ::std::mem::replace */ };
    ($l:literal)  => { /* literal (optionally preceded by -) */ };
    ($m:meta)     => { /* contents of #[...] */ };
    ($lt:lifetime) => { /* 'a */ };
    ($v:vis)      => { /* possibly empty visibility — pub, pub(crate), ... */ };
    ($it:item)    => { /* a full item: fn, struct, mod, ... */ };
    ($tt:tt)      => { /* a single token tree — any token or grouped pair */ };
}
```

```rust
// ❌ BAD: too loose — accepts anything, gives bad errors downstream
macro_rules! loose { ($x:tt) => { $x + 1 }; }

// ✅ GOOD: specific — parser validates at the call site
macro_rules! tight { ($x:expr) => { $x + 1 }; }
```

**Rationale**: A specific specifier (like `expr`) gives the user a grammar error at the invocation, not deep inside the expansion. `tt` is the lingua franca for forwarding and parsing, but it defers validation.

**See also**: MC-04 (opacity), MC-05 (follow-set rules)

---

## MC-04: Most Fragment Captures Are Opaque — `tt` and `ident` Are Not

**Strength**: MUST

**Summary**: A captured `expr`, `ty`, `pat`, `stmt`, `block`, `item`, `path`, `meta`, `literal`, `lifetime`, or `vis` fragment becomes an opaque AST node. Only `tt` and `ident` can be re-matched by a downstream macro.

```rust
// ❌ BAD: forwarding $e:expr to another macro expecting literals
macro_rules! outer {
    ($e:expr) => { inner!($e) };   // inner sees an opaque expr, can't destructure
}
macro_rules! inner {
    (1) => { "one" };
    ($x:expr) => { "other" };
}
// outer!(1) expands to inner!(<opaque expr>) — takes the second rule

// ✅ GOOD: forward as tt, let inner rule match literally
macro_rules! outer_tt {
    ($($e:tt)*) => { inner!($($e)*) };
}
// outer_tt!(1) — inner sees the literal `1` and takes the first rule
```

**Rationale**: Substituted non-`tt`/`ident` fragments are AST nodes, not tokens. If a later macro needs to match `1` or `if`, it must receive a `tt` or `ident`. This is the core reason TT munchers (MC-13) use `$($tail:tt)*` for their queue.

---

## MC-05: Respect Follow-Set Restrictions

**Strength**: MUST

**Summary**: Certain fragment specifiers may only be followed by a restricted set of tokens. This prevents future grammar extensions from silently changing existing macros.

```rust
// Allowed follow-sets (summary)
// expr, stmt : => , ;
// pat        : => , = if in       (pre-2021 also |)
// pat_param  : => , = | if in
// ty, path   : => , = | ; : > >> [ { as where   + `block` metavar
// vis        : , priv-ident, type-start tokens, ident/ty/path metavar
// ident, tt, literal, lifetime, meta, block, item : anything

// ❌ BAD: $e:expr followed by [ is forbidden
// macro_rules! bad { ($e:expr [ $i:expr ]) => { $e[$i] }; }

// ✅ GOOD: restructure with a separator the parser accepts
macro_rules! index {
    ($e:expr; [$i:expr]) => { $e[$i] };
}
index!(arr; [0]);
```

**Rationale**: Rust may add new expression forms starting with `[` in a future edition. Follow-set rules guarantee that any token immediately after `$e:expr` belongs to the current grammar around expressions, so adding new syntax cannot change which rule matches.

---

## MC-06: Repetition — `*`, `+`, `?` with an Optional Separator

**Strength**: MUST

**Summary**: `$( ... ) sep op` repeats a pattern. Use `*` for zero-or-more, `+` for one-or-more, `?` for zero-or-one. The separator (if any) sits between, not after, the repeated element.

```rust
macro_rules! demo {
    // zero or more, comma-separated, trailing comma tolerated
    ( $( $e:expr ),* $(,)? ) => { /* ... */ };

    // one or more, semicolon-separated
    ( $( $stmt:stmt );+ ) => { /* ... */ };

    // optional trailing type annotation
    ( $name:ident $( : $ty:ty )? ) => { /* ... */ };
}

// ✅ Nested repetition — inner level must appear under the outer
macro_rules! group {
    ( $( ( $( $x:expr ),* ) );* ) => {
        vec![ $( vec![ $( $x ),* ] ),* ]
    };
}
let g = group!( (1, 2, 3); (4, 5); (6) );

// ❌ BAD: ? cannot take a separator
// macro_rules! bad { ( $( $x:ident ),? ) => {}; }

// ❌ BAD: adjacent repetitions at the same level are forbidden
// macro_rules! bad2 { ( $($a:expr),* $($b:expr),* ) => {}; }
```

**Rationale**: Every repetition in the transcriber must bind a metavariable at the same repetition depth in the matcher, and all metavariables inside one repetition must bind the same number of fragments. `?` has no separator because there is no gap between zero and one.

---

## MC-07: Rules Are Matched Top-to-Bottom — Order Specific Before General

**Strength**: MUST

**Summary**: The macro expander commits to the **first** matching rule and does not fall through to later rules if expansion errors. Put specific patterns first, fallbacks last.

```rust
// ✅ GOOD: specific first, catch-all last
macro_rules! parse_stmt {
    (let $n:ident = $e:expr)        => { let $n = $e; };
    (return $e:expr)                => { return $e; };
    ($($tt:tt)*)                    => { compile_error!(concat!(
        "unrecognized form: ", stringify!($($tt)*)
    )); };
}

// ❌ BAD: catch-all first swallows everything
macro_rules! swallowed {
    ($($tt:tt)*) => { /* always matches */ };
    (let $n:ident = $e:expr) => { /* never reached */ };
}
```

**Rationale**: No lookahead, no backtracking: the parser picks a rule by looking at the shape of the input one token at a time. If rule 1 matches but its expansion fails, rule 2 is not tried.

---

## MC-08: Mixed-Site Hygiene — What Leaks and What Doesn't

**Strength**: MUST

**Summary**: Identifiers introduced *inside* a `macro_rules!` expansion are isolated from the call site (hygienic for locals). Identifiers substituted *in* from the call site retain their call-site context. Item-level names (functions, types) resolve at the invocation site.

```rust
// Hygienic for locals
macro_rules! five {
    () => {{ let x = 5; x }};
}

let x = 10;
let y = five!();       // y = 5, outer x untouched

// ❌ BAD: macro's internal `let` is invisible to caller
macro_rules! using_a {
    ($e:expr) => {{ let a = 42; $e }};
}
// let four = using_a!(a / 10);  // error: unresolved name `a`

// ✅ GOOD: accept the identifier — now `a` shares call-site context
macro_rules! using_named {
    ($a:ident, $e:expr) => {{ let $a = 42; $e }};
}
let four = using_named!(a, a / 10);

// Items resolve at the call site — use absolute paths for reliability
macro_rules! new_vec {
    () => { ::std::vec::Vec::<i32>::new() };   // ✅ immune to shadowing
}
```

**Rationale**: Rust's hygiene is "mixed-site": locals and labels use the definition site, items use the invocation site. This prevents accidental local-variable capture (unlike C preprocessor) but still lets macros call user-visible functions. Always use absolute paths (`::std::...`, `$crate::...`) for items to avoid call-site shadowing.

**See also**: MC-09 (`$crate`), MC-20 (proc-macro hygiene)

---

## MC-09: Use `$crate` in Exported Macros

**Strength**: MUST

**Summary**: Inside a `#[macro_export]`ed macro, `$crate` expands to an absolute path to the defining crate. Always use it when referring to items in your own crate.

```rust
// In your library crate `mylib`
pub fn helper() { /* ... */ }

#[macro_export]
macro_rules! log_it {
    // ❌ BAD: won't compile when called from downstream crates
    // () => { crate::helper() };

    // ✅ GOOD: always resolves to mylib, even when the user renames it
    () => { $crate::helper() };
}

// Downstream crate (possibly renamed)
// use renamed_lib::log_it;
// log_it!();   // still calls mylib::helper
```

**Rationale**: Downstream code may rename your crate (`[dependencies] foo = { package = "mylib" }`) or use `extern crate mylib as bar`. `$crate` expands to whatever path resolves to your crate at the call site. Note: `$crate` does not work for referencing *other macros* — only non-macro items — so export every macro your macro depends on.

---

## MC-10: Mark Public Macros `#[macro_export]`; Scope Helpers Privately

**Strength**: SHOULD

**Summary**: `#[macro_export]` promotes a macro to `pub` and places it at the crate root for path-based import. Without it, macros have textual, crate-local scope. Prefer `pub use` re-exports for controlled public placement.

```rust
// In lib.rs
#[macro_export]
macro_rules! my_macro {
    () => { $crate::helpers::impl_detail() };
}

// Internal helper macro — no #[macro_export]
// Callers of my_macro! don't need it imported
mod helpers {
    macro_rules! impl_detail {
        () => { /* ... */ };
    }
    pub(crate) use impl_detail;
    pub fn actual_helper() { /* ... */ }
}
```

```rust
// Re-export from a module path rather than the crate root
pub mod prelude {
    pub use crate::my_macro;
}
// Users: use mylib::prelude::my_macro;
```

**Rationale**: `#[macro_export]` ignores module visibility and pins the macro to the crate root. Modern Rust (2018+) prefers `pub use crate::name` to control *where* the macro appears, while keeping `#[macro_export]` as the mechanism that makes it exportable at all. The old `#[macro_use] extern crate` form is legacy; use `use crate::macro_name;` in new code.

---

## MC-11: The TT Muncher Pattern

**Strength**: CONSIDER

**Summary**: Parse complex input by recursively matching a prefix, emitting output, and recursing on the tail captured as `$($tail:tt)*`.

```rust
macro_rules! mixed_rules {
    () => {};   // base case: empty input halts recursion

    // match: `trace IDENT;` then continue
    (trace $name:ident; $($tail:tt)*) => {{
        println!(concat!(stringify!($name), " = {:?}"), $name);
        mixed_rules!($($tail)*);
    }};

    // match: `trace IDENT = EXPR;` then continue
    (trace $name:ident = $init:expr; $($tail:tt)*) => {{
        let $name = $init;
        println!(concat!(stringify!($name), " = {:?}"), $name);
        mixed_rules!($($tail)*);
    }};
}

fn main() {
    let a = 42;
    mixed_rules!(
        trace a;
        trace b = "hello";
        trace b;
    );
}
```

**Rationale**: `$($tail:tt)*` is the only lossless way to forward arbitrary remaining input — any other specifier loses information at the AST boundary (MC-04). The trade-off: every "munch" step costs one recursion level, and `macro_rules!` has no tail-call optimization. Default recursion limit is 128; raise with `#![recursion_limit = "256"]` only as a last resort, and prefer matching multiple tokens per step for large inputs.

**See also**: MC-12 (push-down accumulation), MC-14 (internal rules)

---

## MC-12: Push-Down Accumulation for Building Up Results

**Strength**: CONSIDER

**Summary**: Macros must always expand to a *complete* syntax element — there is no way to expand to a partial expression. Accumulate tokens in a `tt` buffer through recursive calls, then emit the whole buffer at the terminating rule.

```rust
macro_rules! init_array {
    // Terminator — emit accumulated tokens, coerce to expression
    (@accum (0, $_e:expr) -> ($($body:tt)*)) => {
        init_array!(@as_expr [$($body)*])
    };
    // Recursive step — append one clone, recurse with count-1
    (@accum ($n:tt, $e:expr) -> ($($body:tt)*)) => {
        init_array!(@accum (pred!($n), $e) -> ($($body)* $e,))
    };
    // AST coercion helper
    (@as_expr $e:expr) => { $e };

    // Public entry point
    [$e:expr; $n:tt] => {{
        let e = $e;
        init_array!(@accum ($n, e.clone()) -> ())
    }};
}
```

**Rationale**: Intermediate macro expansions cannot be partial array literals (`[a, a,`) — those are not valid syntax. Buffering tokens inside a `tt` group defers parsing until the buffer is complete. Push-down accumulation is commonly paired with TT munchers (MC-11) and internal rules (MC-14).

---

## MC-13: AST Coercion Forces `tt` Substitutions Into a Grammar Category

**Strength**: CONSIDER

**Summary**: The parser sometimes rejects substituted `tt` sequences even when the tokens form valid syntax. Wrap them in a trivial pass-through macro (`as_expr!`, `as_item!`, `as_pat!`, `as_stmt!`) to force re-parsing.

```rust
macro_rules! as_expr { ($e:expr) => { $e }; }
macro_rules! as_item { ($i:item) => { $i }; }
macro_rules! as_pat  { ($p:pat)  => { $p }; }
macro_rules! as_stmt { ($s:stmt) => { $s }; }

// Typical use: push-down accumulator emits [tokens], then coerces
macro_rules! finish {
    ($($tokens:tt)*) => { as_expr!([$($tokens)*]) };
}

// There is no `as_ty!` — macros cannot appear in type position
```

**Rationale**: Fragment specifiers inside a coercion macro's matcher force the parser to interpret the `tt` stream as the named grammar category. The coercion macros are zero-cost at runtime and are often embedded as `@as_expr` internal rules (MC-14) inside a larger macro.

---

## MC-14: Internal Rules — The `@`-Prefix Convention

**Strength**: SHOULD

**Summary**: Fold helper macros into the main macro as `@tag`-prefixed rules. `@` is never valid in prefix position in Rust source, so it cannot clash with real input.

```rust
#[macro_export]
macro_rules! foo {
    // Internal rules first — @-prefixed, private by convention
    (@as_expr $e:expr) => { $e };
    (@accum ($($acc:tt)*) $next:tt $($rest:tt)*) => {
        foo!(@accum ($($acc)* $next) $($rest)*)
    };
    (@accum ($($acc:tt)*)) => { foo!(@as_expr [$($acc)*]) };

    // Public entry point — bare rule, matches user input
    ($($tt:tt)*) => { foo!(@accum () $($tt)*) };
}
```

**Rationale**: `#[macro_export]`ed macros must bring their own helpers — there is no private macro visibility across crates. Internal rules keep the helpers out of the public namespace. Always place `@`-prefixed rules *before* a catch-all `$($tt:tt)*` rule; otherwise the catch-all swallows the `@` tokens first.

---

## MC-15: The Callback Pattern for Macro Composition

**Strength**: CONSIDER

**Summary**: Macros don't evaluate nested macro calls before pattern matching. To compose macros, have the inner macro accept a callback name and invoke it with the result.

```rust
// ❌ BAD: inner_macro!(outer_macro!(x)) — outer_macro! is not expanded first
// Inner sees the literal tokens `outer_macro ! ( x )`, not the expansion

// ✅ GOOD: callback pattern
macro_rules! with_larch {
    ($cb:ident) => { $cb!(larch) };
}
macro_rules! recognise {
    (larch) => { "it's a larch" };
    ($other:tt) => { "unknown tree" };
}

let s = with_larch!(recognise);   // "it's a larch"

// Forward arbitrary extra args via tt repetition
macro_rules! callback {
    ($cb:ident ( $($args:tt)* )) => { $cb!($($args)*) };
}
```

**Rationale**: Macro expansion is outside-in, not inside-out. The outer macro sees the tokens of the inner invocation, not its expansion. Callbacks invert the flow: the producing macro calls the consumer macro directly with finished tokens.

---

## MC-16: Count at Compile Time via Slice Length

**Strength**: CONSIDER

**Summary**: Counting tokens in `macro_rules!` is surprisingly tricky. The scalable, non-`const` technique is `<[()]>::len(&[$(replace_expr!($tts ())),*])`. For `const` counts of distinct identifiers, use a hidden enum.

```rust
macro_rules! replace_expr { ($_t:tt $sub:expr) => { $sub }; }

// ✅ Scales to tens of thousands of tokens — but not const
macro_rules! count_tts {
    ($($tts:tt)*) => { <[()]>::len(&[$(replace_expr!($tts ())),*]) };
}
let n = count_tts!(a b c d);  // 4

// ✅ Const-evaluable, but identifiers must be distinct
macro_rules! count_idents {
    ($($id:ident),* $(,)?) => {{
        #[allow(dead_code, non_camel_case_types)]
        enum __Count { $($id,)* __Sentinel }
        __Count::__Sentinel as u32
    }};
}
const N: u32 = count_idents!(A, B, C);  // 3
```

**Rationale**: The naive `0 $(+ 1)*` approach builds a deeply nested AST that crashes the compiler past ~500 tokens. Recursion hits `recursion_limit`. Slice-length scales but the result is runtime-only. Enum counting produces a `const` but is not hygienic (the sentinel name must not collide with an input). Always use `usize`-typed literals inside counting expansions — untyped literals trigger pathological type inference.

---

## MC-17: Use `compile_error!` for Actionable Macro Errors

**Strength**: SHOULD

**Summary**: Catch bad invocations with a fallback rule that emits `compile_error!` pointing at the expected syntax.

```rust
macro_rules! config {
    (name: $n:expr, port: $p:expr) => { /* ... */ };
    ($($tt:tt)*) => {
        compile_error!(concat!(
            "invalid `config!` invocation; expected: ",
            "config!(name: \"...\", port: ...)"
        ));
    };
}

// Proc-macro equivalent: emit syn::Error with a helpful span
// or panic with a clear message — both surface at the invocation.
```

**Rationale**: Without a catch-all, a bad invocation produces noisy "no rules matched" errors. `compile_error!` lets you spell out the correct form. In proc-macros, prefer `syn::Error::new_spanned(&token, msg).to_compile_error()` because it reports the error at the user's tokens rather than inside your macro.

---

## MC-18: When to Reach for `macro_rules!`

**Strength**: CONSIDER

**Summary**: Declarative macros are the right tool for variable-arity syntax, small DSLs over literal tokens, and eager-evaluated formatting arguments.

```rust
// ✅ Variable-arity syntax
// vec![1, 2, 3]  println!("{}", x)  assert_eq!(a, b)

// ✅ Format-like — each argument must be eager
macro_rules! dbg_named {
    ($name:expr, $e:expr) => {
        eprintln!("{} = {:#?}", $name, $e);
    };
}

// ✅ Small DSL — literal tokens as structure
macro_rules! matrix {
    ( $( [ $($x:expr),* ] );* ) => {
        vec![ $( vec![ $($x),* ] ),* ]
    };
}
let m = matrix![[1, 2, 3]; [4, 5, 6]];
```

**Rationale**: `macro_rules!` lives in a single file in your crate, produces clean error spans, and composes with rustfmt (it just doesn't format inside the body). For anything beyond light syntactic sugar — inspecting struct fields, matching on types, generating impls — move to a proc-macro.

---

## MC-19: When to Reach for a Procedural Macro

**Strength**: CONSIDER

**Summary**: Use a proc-macro when you need to inspect the *structure* of an item (fields, variants, generics), generate trait impls, or parse a real grammar. Accept the cost: a separate crate, `syn` + `quote` dependencies, and worse error messages.

```rust
// Cargo.toml of the proc-macro crate:
// [lib]
// proc-macro = true
// [dependencies]
// syn = { version = "2", features = ["full"] }
// quote = "1"
// proc-macro2 = "1"

use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput, Data, Fields};

#[proc_macro_derive(FieldNames)]
pub fn field_names(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;

    let names = match &input.data {
        Data::Struct(s) => match &s.fields {
            Fields::Named(f) => f.named.iter()
                .map(|f| f.ident.as_ref().unwrap().to_string())
                .collect::<Vec<_>>(),
            _ => return syn::Error::new_spanned(
                name, "FieldNames requires named fields"
            ).to_compile_error().into(),
        },
        _ => return syn::Error::new_spanned(
            name, "FieldNames only works on structs"
        ).to_compile_error().into(),
    };

    quote! {
        impl #name {
            pub const FIELD_NAMES: &'static [&'static str] = &[ #(#names),* ];
        }
    }.into()
}
```

**Rationale**: `syn` gives you a full Rust AST; `quote` gives you template-style code generation with spanned splices (`#ident`, `#(#iter),*`). `proc-macro2` re-exports `TokenStream` so your macro can be tested as a normal library. Proc-macros can also panic or return `compile_error!` — panics become compiler errors, loops hang the compiler, so guard against infinite recursion.

---

## MC-20: Procedural Macros Are Unhygienic — Use Absolute Paths

**Strength**: MUST

**Summary**: Proc-macro output behaves as if written inline at the call site. Any name you emit resolves at the invocation, so always qualify.

```rust
// ❌ BAD: resolves to whatever `Option` is in scope at the call site
quote! { let x: Option<u32> = None; }

// ✅ GOOD: absolute paths are immune to shadowing
quote! { let x: ::std::option::Option<u32> = ::std::option::Option::None; }

// ✅ GOOD: for items from your own crate, accept a crate-path parameter
//    (proc-macros cannot use $crate — it's macro_rules!-only)
#[proc_macro_derive(MyDerive, attributes(mycrate))]
pub fn my_derive(input: TokenStream) -> TokenStream {
    // Parse a #[mycrate(crate = "::my_real_crate")] attribute, defaulting
    // to `::mycrate`, so the user can rename the crate.
    // ...
    # TokenStream::new()
}
```

**Rationale**: Unlike `macro_rules!`, proc-macros have no hygiene for anything. If the user wrote `struct Option;` in scope, `Option::None` in your output refers to their struct. Absolute paths plus `__prefixed` internal identifiers are the standard defense. For cross-crate item references, take a crate-path attribute (the `serde(crate = "...")` convention) — `$crate` does not exist in proc-macros.

---

## MC-21: Three Procedural Macro Flavors

**Strength**: MUST

**Summary**: Pick the flavor by what the user writes: `#[derive(X)]` for append-only generation, `#[attr]` for transforming an annotated item, `name!(...)` for arbitrary syntax.

```rust
// 1. Derive — appends items after the target; original is untouched
#[proc_macro_derive(Builder, attributes(builder))]
pub fn derive_builder(input: TokenStream) -> TokenStream { /* ... */
    # TokenStream::new()
}

// 2. Attribute — replaces the annotated item
#[proc_macro_attribute]
pub fn route(attr: TokenStream, item: TokenStream) -> TokenStream {
    // attr   = contents of the #[route(...)] parens
    // item   = the annotated fn/struct/etc.
    // return = zero or more items replacing `item`
    item
}

// 3. Function-like — replaces the invocation entirely
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
    // input = tokens between the delimiters of sql!(...)
    "fn compiled_query() -> &'static str { \"SELECT 1\" }"
        .parse().unwrap()
}
```

```rust
// Using them
#[derive(Builder)]
struct Config { host: String, port: u16 }

#[route(GET, "/users")]
fn list_users() { /* ... */ }

sql!(SELECT id, name FROM users);
```

**Rationale**: Derive is the right choice when you want to add (not change) trait impls next to an existing type. Attribute is the right choice when you need to rewrite a function (adding instrumentation, router registration, async-to-sync transformation). Function-like is the right choice when the input is a DSL that cannot be expressed as a Rust item.

---

## MC-22: Derive Helper Attributes Are Inert

**Strength**: CONSIDER

**Summary**: Declare helper attributes with `attributes(name, ...)` on `#[proc_macro_derive]`. They become visible on the item and its fields but do nothing on their own — they exist so your derive can read them.

```rust
#[proc_macro_derive(Serialize, attributes(serde))]
pub fn derive_serialize(input: TokenStream) -> TokenStream {
    // Look for #[serde(...)] attributes on fields; they are inert
    // to the compiler but your derive can inspect them.
    # TokenStream::new()
}

// User code
#[derive(Serialize)]
struct User {
    #[serde(rename = "user_id")]
    id: u64,

    #[serde(skip)]
    cache: Option<String>,
}
```

**Rationale**: Helper attributes give the derive a configuration channel without polluting the global attribute namespace. Because they are inert, the compiler accepts them even if no derive consumes them — useful for cfg-gated derives.

---

## MC-23: Spans Preserve User-Facing Error Locations

**Strength**: SHOULD

**Summary**: Every token in a proc-macro carries a `Span` — the source location. Attach spans from user tokens to your generated tokens so errors point at the user's code, not at the macro.

```rust
use proc_macro2::Span;
use quote::{quote, quote_spanned};
use syn::spanned::Spanned;

# fn gen(field: &syn::Field) -> proc_macro2::TokenStream {
let ty = &field.ty;

// ❌ BAD: generated assertion error points inside the proc-macro
let check = quote! {
    const _: () = assert!(std::mem::size_of::<#ty>() <= 64);
};

// ✅ GOOD: error span points at the offending field in the user's struct
let check = quote_spanned! { field.ty.span() =>
    const _: () = assert!(std::mem::size_of::<#ty>() <= 64);
};
# check
# }
```

**Rationale**: `quote_spanned!` (and `syn::Error::new_spanned`) let you attach a user-originating span to generated tokens. The result: compiler errors and IDE squiggles land on the struct field that caused the problem, not on the derive invocation or — worse — somewhere in your proc-macro crate.

---

## MC-24: Make Macro Invocations Look Like Rust

**Strength**: SHOULD

**Summary**: Design the call syntax to mirror existing Rust syntax wherever possible. Users should be able to guess the shape of the DSL from its first line.

```rust
// ✅ GOOD: evocative — mirrors struct-literal syntax
macro_rules! point {
    ( $name:ident { x: $x:expr, y: $y:expr $(,)? } ) => {
        struct $name { x: f64, y: f64 }
        impl $name {
            fn new() -> Self { Self { x: $x, y: $y } }
        }
    };
}
point!(Origin { x: 0.0, y: 0.0 });

// ✅ GOOD: attribute macro — looks like a normal attribute
#[route(GET, "/users/:id")]
fn get_user() { /* ... */ }

// ❌ BAD: invented syntax that does not follow any convention
macro_rules! weird {
    ( ~> $x:expr ~> ) => { /* ... */ };
}
weird!(~> 1 + 2 ~>);
```

**Rationale**: Rust's standard macros (`vec!`, `println!`, `matches!`, `todo!`) feel like language features precisely because their syntax echoes the surrounding language. Custom tokens like `~>` or `|=>|` turn every reader into a lexer.

**See also**: C-EVOCATIVE, C-MACRO-ATTR (Rust API guidelines)

---

## MC-25: Document Macros Like Functions — Plus the Grammar

**Strength**: MUST

**Summary**: Every public macro needs a doc comment covering the invocation syntax, a worked example in a doctest, and the expansion model when it matters.

```rust
/// Build a `HashMap<K, V>` from key–value pairs.
///
/// # Syntax
///
/// ```text
/// hashmap! {
///     key1 => value1,
///     key2 => value2,
/// }
/// ```
///
/// Trailing commas are permitted. Keys and values are evaluated once each,
/// in source order.
///
/// # Examples
///
/// ```
/// # use mylib::hashmap;
/// let m = hashmap! {
///     "alice" => 30,
///     "bob" => 25,
/// };
/// assert_eq!(m["alice"], 30);
/// ```
///
/// # Panics
///
/// Never. This macro only delegates to `HashMap::insert`.
#[macro_export]
macro_rules! hashmap {
    ($($k:expr => $v:expr),* $(,)?) => {{
        let mut m = ::std::collections::HashMap::new();
        $( m.insert($k, $v); )*
        m
    }};
}
```

**Rationale**: Macro syntax is not discoverable from the signature the way function signatures are. Doctests are the *only* way to make the invocation syntax compiler-checked. For proc-macros, document the attribute options and their defaults, and include an example of a typical input/output pair.

**See also**: DC-guide (documentation guidelines)

---

## MC-26: Debug Macros with `cargo expand` and Friends

**Strength**: SHOULD

**Summary**: When a macro goes wrong, look at the expanded source.

```text
# Stable, third-party — works for macro_rules! and proc-macros
$ cargo install cargo-expand
$ cargo expand
$ cargo expand --test test_name
$ cargo expand path::to::module

# Nightly-only alternatives
#![feature(trace_macros, log_syntax)]

// Trace every invocation of a macro in a region
trace_macros!(true);
my_macro!(foo bar);
trace_macros!(false);

// Print tokens at a specific point during expansion
macro_rules! probe {
    ($($tt:tt)*) => { log_syntax!($($tt)*); /* ... */ };
}
```

```rust
// Ad-hoc debugging: force a compile error showing the matched input
macro_rules! inspect {
    ($($tt:tt)*) => { compile_error!(stringify!($($tt)*)); };
}

// For proc-macros: eprintln! during `cargo build` prints to the build log
#[proc_macro]
pub fn debug_me(input: TokenStream) -> TokenStream {
    eprintln!("INPUT: {}", input);
    input
}
```

**Rationale**: `cargo expand` is the single most effective macro-debugging tool. For deeper investigation of `macro_rules!` recursion, `trace_macros!` shows each invocation. For proc-macros, add unit tests using `proc-macro2::TokenStream` (which is testable outside a proc-macro crate) and snapshot-test the output with a crate like `insta`.

---

## MC-27: Test Proc-Macros with `trybuild`

**Strength**: SHOULD

**Summary**: Exercise the user-facing error messages by compiling example files and comparing output.

```rust
// tests/ui.rs
#[test]
fn ui() {
    let t = trybuild::TestCases::new();
    t.pass("tests/ui/pass_*.rs");
    t.compile_fail("tests/ui/fail_*.rs");
}

// tests/ui/fail_non_struct.rs
use mylib::Builder;
#[derive(Builder)]
enum NotAStruct { A, B }
fn main() {}

// tests/ui/fail_non_struct.stderr (captured with `TRYBUILD=overwrite cargo test`)
// error: Builder only works on structs
//   --> tests/ui/fail_non_struct.rs:3:10
//    |
// 3  | #[derive(Builder)]
//    |          ^^^^^^^
```

**Rationale**: Your proc-macro's error quality is part of its API. `trybuild` snapshot-tests the actual compiler output, so regressions in error messages fail CI. For `macro_rules!` macros, ordinary unit tests with `assert_eq!` on expanded values are usually enough; reserve `trybuild` for compile-fail coverage.

---

## MC-28: `macro_rules!` Has Real Limits — Know Them

**Strength**: MUST

**Summary**: `macro_rules!` cannot appear in type position, cannot produce partial syntax, cannot backtrack, and has a recursion limit.

```rust
// ❌ CANNOT: use a macro in type position
// fn f(x: my_type_macro!()) -> i32 { x + 1 }   // error

// ❌ CANNOT: expand to a partial item (half a struct, etc.)
// Every expansion must be a complete expression, statement, item, etc.

// ❌ CANNOT: backtrack — once a rule commits to consuming tokens for
// a fragment, it cannot undo. Design matchers to be unambiguous from
// the first token onward.

// ❌ CANNOT: inspect the name or fields of a captured type.
//            `$T:ty` is opaque — use a proc-macro if you need introspection.

// ⚠️ recursion_limit (default 128) caps TT muncher depth
#![recursion_limit = "256"]   // raise only after exhausting redesigns
```

**Rationale**: These limits are why proc-macros exist. If your macro needs to look at a struct's field types, generate a type alias, or recurse over thousands of items, move to a proc-macro. Raising `recursion_limit` is a short-term patch — the real fix is matching multiple tokens per step, or using accumulation / iteration-based proc-macros.

---

## MC-29: Procedural Macros Live in Their Own Crate

**Strength**: MUST

**Summary**: A `proc-macro = true` crate cannot be used from itself. For a library that exposes both regular items and proc-macros, split into a runtime crate and a `*-macros` companion, and re-export the macros from the runtime crate.

```toml
# Workspace layout
# mylib/          — regular library, re-exports everything
# mylib-macros/   — proc-macro crate

# mylib-macros/Cargo.toml
[package]
name = "mylib-macros"
[lib]
proc-macro = true
[dependencies]
syn = "2"
quote = "1"
proc-macro2 = "1"

# mylib/Cargo.toml
[package]
name = "mylib"
[dependencies]
mylib-macros = { version = "=0.1.0", path = "../mylib-macros" }
```

```rust
// mylib/src/lib.rs
pub use mylib_macros::Builder;    // re-export the derive

pub trait BuilderTarget { /* runtime trait the derive generates code for */ }
```

**Rationale**: Proc-macros must be compiled to a dylib loaded by rustc, which is why they live alone. Re-exporting from the main crate means users write `use mylib::Builder;` without caring about the split — and it lets the runtime crate version-pin the macro crate via `=`. This is the `serde` / `serde_derive`, `thiserror` / `thiserror-impl` pattern.


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| MC-01 Prefer functions/generics | MUST | Macro only when types can't express it |
| MC-02 Declarative vs procedural | SHOULD | Pattern-match → `macro_rules!`; introspect → proc-macro |
| MC-03 Learn fragment specifiers | MUST | Pick the most specific category |
| MC-04 `tt`/`ident` are the only re-matchable fragments | MUST | Others are opaque AST nodes |
| MC-05 Respect follow-set restrictions | MUST | `expr`/`stmt` → only `=> , ;`, etc. |
| MC-06 Repetition operators | MUST | `* + ?` with optional separator |
| MC-07 Rules match top-to-bottom | MUST | Specific before general, no backtrack |
| MC-08 Mixed-site hygiene | MUST | Locals hygienic; items resolve at call site |
| MC-09 Use `$crate` in exported macros | MUST | Survives crate renaming |
| MC-10 `#[macro_export]` + `pub use` | SHOULD | Control where the macro appears |
| MC-11 TT muncher | CONSIDER | Recursive parse via `$($tail:tt)*` |
| MC-12 Push-down accumulation | CONSIDER | Build in a `tt` buffer, emit at the end |
| MC-13 AST coercion | CONSIDER | `as_expr!`, `as_item!`, `as_pat!`, `as_stmt!` |
| MC-14 Internal rules (`@tag`) | SHOULD | Private helpers inside one macro |
| MC-15 Callback pattern | CONSIDER | Compose macros by passing an ident |
| MC-16 Count via slice length | CONSIDER | Scales; use enum for `const` |
| MC-17 `compile_error!` for bad input | SHOULD | Actionable errors beat "no rules matched" |
| MC-19 Proc-macro when you need introspection | CONSIDER | `syn` + `quote` + dedicated crate |
| MC-20 Proc-macros are unhygienic | MUST | Always use absolute paths |
| MC-21 Three proc-macro flavors | MUST | derive / attribute / function-like |
| MC-22 Helper attributes are inert | CONSIDER | `attributes(name, ...)` on derive |
| MC-23 Preserve spans | SHOULD | `quote_spanned!` for good error locations |
| MC-24 Macros mirror Rust syntax | SHOULD | Evocative, attribute-shaped, struct-shaped |
| MC-25 Document syntax + doctest | MUST | Doctests are the only checked examples |
| MC-26 Debug with `cargo expand` | SHOULD | Read the expansion; don't guess |
| MC-27 `trybuild` for proc-macros | SHOULD | Snapshot compile-fail output |
| MC-28 Know `macro_rules!` limits | MUST | No type position, no partial syntax, no backtrack |
| MC-29 Proc-macros in their own crate | MUST | Split runtime and macros; re-export |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for when a generic function should replace a macro.
- **API Design**: See `02-api-design.md` for `C-EVOCATIVE` and `C-MACRO-ATTR` — macro surface design.
- **Type Design**: See `05-type-design.md` for types that macros commonly generate (builders, typestate flows).
- **Traits**: See `06-traits.md` for the trait impls that `#[derive]` and custom derives produce.
- **Documentation**: See `13-documentation.md` for doctest conventions; macros *need* doctests.
- **Anti-patterns**: See `11-anti-patterns.md` for common macro misuse (macros where a function works, unhygienic captures, untested proc-macros).


## External References

- [The Rust Reference — Macros by Example](https://doc.rust-lang.org/reference/macros-by-example.html) — normative rules for `macro_rules!`, fragment specifiers, follow-sets, hygiene
- [The Rust Reference — Procedural Macros](https://doc.rust-lang.org/reference/procedural-macros.html) — the three flavors, `TokenStream` semantics, helper attributes
- [The Rust Programming Language — Ch. 20.5 "Macros"](https://doc.rust-lang.org/book/ch20-06-macros.html) — tutorial-level introduction
- [The Little Book of Rust Macros](https://veykril.github.io/tlborm/) — deep dive into patterns (TT munchers, push-down accumulation, internal rules, counting)
- [`syn` documentation](https://docs.rs/syn/) — parsing Rust source into an AST for proc-macros
- [`quote` documentation](https://docs.rs/quote/) — template-style code generation with spans
- [`proc-macro2` documentation](https://docs.rs/proc-macro2/) — testable token streams
- [`trybuild` documentation](https://docs.rs/trybuild/) — compile-pass / compile-fail testing for proc-macros
- [`cargo-expand`](https://github.com/dtolnay/cargo-expand) — view the expanded source of any crate
- Pragmatic Rust Guidelines: C-EVOCATIVE, C-MACRO-ATTR (macro-shaped APIs), C-DEBUG (proc-macro-generated types still implement `Debug`)
