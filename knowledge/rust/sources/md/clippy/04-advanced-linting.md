# Type Checking

When we work on a new lint or improve an existing lint, we might want
to retrieve the type `Ty` of an expression `Expr` for a variety of
reasons. This can be achieved by utilizing the [`LateContext`][LateContext]
that is available for [`LateLintPass`][LateLintPass].

## `LateContext` and `TypeckResults`

The lint context [`LateContext`][LateContext] and [`TypeckResults`][TypeckResults]
(returned by `LateContext::typeck_results`) are the two most useful data structures
in `LateLintPass`. They allow us to jump to type definitions and other compilation
stages such as HIR.

> Note: `LateContext.typeck_results`'s return value is [`TypeckResults`][TypeckResults]
> and is created in the type checking step, it includes useful information such as types of
> expressions, ways to resolve methods and so on.

`TypeckResults` contains useful methods such as [`expr_ty`][expr_ty],
which gives us access to the underlying structure [`Ty`][Ty] of a given expression.

```rust
pub fn expr_ty(&self, expr: &Expr<'_>) -> Ty<'tcx>
```

As a side note, besides `expr_ty`, [`TypeckResults`][TypeckResults] contains a
[`pat_ty()`][pat_ty] method that is useful for retrieving a type from a pattern.

## `Ty`

`Ty` struct contains the type information of an expression.
Let's take a look at `rustc_middle`'s [`Ty`][Ty] struct to examine this struct:

```rust
pub struct Ty<'tcx>(Interned<'tcx, WithStableHash<TyS<'tcx>>>);
```

At a first glance, this struct looks quite esoteric. But at a closer look,
we will see that this struct contains many useful methods for type checking.

For instance, [`is_char`][is_char] checks if the given `Ty` struct corresponds
to the primitive character type.

### `is_*` Usage

In some scenarios, all we need to do is check if the `Ty` of an expression
is a specific type, such as `char` type, so we could write the following:

```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        // Get type of `expr`
        let ty = cx.typeck_results().expr_ty(expr);

        // Check if the `Ty` of this expression is of character type
        if ty.is_char() {
            println!("Our expression is a char!");
        }
    }
}
```

Furthermore, if we examine the [source code][is_char_source] for `is_char`,
we find something very interesting:

```rust
#[inline]
pub fn is_char(self) -> bool {
    matches!(self.kind(), Char)
}
```

Indeed, we just discovered `Ty`'s [`kind()` method][kind], which provides us
with [`TyKind`][TyKind] of a `Ty`.

## `TyKind`

`TyKind` defines the kinds of types in Rust's type system.
Peeking into [`TyKind` documentation][TyKind], we will see that it is an
enum of over 25 variants, including items such as `Bool`, `Int`, `Ref`, etc.

### `kind` Usage

The `TyKind` of `Ty` can be returned by calling [`Ty.kind()` method][kind].
We often use this method to perform pattern matching in Clippy.

For instance, if we want to check for a `struct`, we could examine if the
`ty.kind` corresponds to an [`Adt`][Adt] (algebraic data type) and if its
[`AdtDef`][AdtDef] is a struct:

```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        // Get type of `expr`
        let ty = cx.typeck_results().expr_ty(expr);
        // Match its kind to enter the type
        match ty.kind() {
            ty::Adt(adt_def, _) if adt_def.is_struct() => println!("Our `expr` is a struct!"),
            _ => ()
        }
    }
}
```

## `hir::Ty` and `ty::Ty`

We've been talking about [`ty::Ty`][middle_ty] this whole time without addressing [`hir::Ty`][hir_ty], but the latter
is also important to understand.

`hir::Ty` would represent *what* the user wrote, while `ty::Ty` is how the compiler sees the type and has more
information. Example:

```rust
fn foo(x: u32) -> u32 { x }
```

Here the HIR sees the types without "thinking" about them, it knows that the function takes an `u32` and returns
an `u32`. As far as `hir::Ty` is concerned those might be different types. But at the `ty::Ty` level the compiler
understands that they're the same type, in-depth lifetimes, etc...

To get from a `hir::Ty` to a `ty::Ty`, you can use the [`lower_ty`][lower_ty] function outside of bodies or
the [`TypeckResults::node_type()`][node_type] method inside of bodies.

> **Warning**: Don't use `lower_ty` inside of bodies, because this can cause ICEs.

## Creating Types programmatically

A common usecase for creating types programmatically is when we want to check if a type implements a trait (see
[Trait Checking](trait_checking.md)).

Here's an example of how to create a `Ty` for a slice of `u8`, i.e. `[u8]`

```rust
use rustc_middle::ty::Ty;
// assume we have access to a LateContext
let ty = Ty::new_slice(cx.tcx, Ty::new_u8());
```

In general, we rely on `Ty::new_*` methods. These methods define the basic building-blocks that the
type-system and trait-system use to define and understand the written code.

## Useful Links

Below are some useful links to further explore the concepts covered
in this chapter:

- [Stages of compilation](https://rustc-dev-guide.rust-lang.org/compiler-src.html#the-main-stages-of-compilation)
- [Diagnostic items](https://rustc-dev-guide.rust-lang.org/diagnostics/diagnostic-items.html)
- [Type checking](https://rustc-dev-guide.rust-lang.org/hir-typeck/summary.html)
- [Ty module](https://rustc-dev-guide.rust-lang.org/ty.html)

[Adt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Adt
[AdtDef]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/adt/struct.AdtDef.html
[expr_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TypeckResults.html#method.expr_ty
[node_type]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TypeckResults.html#method.node_type
[is_char]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#method.is_char
[is_char_source]: https://github.com/rust-lang/rust/blob/d34f1f931489618efffc4007e6b6bdb9e10f6467/compiler/rustc_middle/src/ty/sty.rs#L1429-L1432
[kind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#method.kind
[LateContext]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/struct.LateContext.html
[LateLintPass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html
[pat_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/typeck_results/struct.TypeckResults.html#method.pat_ty
[Ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[TyKind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html
[TypeckResults]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TypeckResults.html
[middle_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[hir_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Ty.html
[lower_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/fn.lower_ty.html


---

# Trait Checking

Besides [type checking](type_checking.md), we might want to examine if
a specific type `Ty` implements certain trait when implementing a lint.
There are three approaches to achieve this, depending on if the target trait
that we want to examine has a [diagnostic item][diagnostic_items],
[lang item][lang_items], or neither.

## Using Diagnostic Items

As explained in the [Rust Compiler Development Guide][rustc_dev_guide], diagnostic items
are introduced for identifying types via [Symbols][symbol].

For instance, if we want to examine whether an expression implements
the `Iterator` trait, we could simply write the following code,
providing the `LateContext` (`cx`), our expression at hand, and
the symbol of the trait in question:

```rust
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;
use rustc_hir::Expr;
use rustc_lint::{LateContext, LateLintPass};

impl LateLintPass<'_> for CheckIteratorTraitLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let implements_iterator = (cx.tcx.get_diagnostic_item(sym::Iterator))
            .is_some_and(|id| implements_trait(cx, cx.typeck_results().expr_ty(expr), id, &[]));
        if implements_iterator {
            // [...]
        }

    }
}
```

> **Note**: Refer to [this index][symbol_index] for all the defined `Symbol`s.

## Using Lang Items

Besides diagnostic items, we can also use [`lang_items`][lang_items].
Take a look at the documentation to find that `LanguageItems` contains
all language items defined in the compiler.

Using one of its `*_trait` method, we could obtain the [DefId] of any
specific item, such as `Clone`, `Copy`, `Drop`, `Eq`, which are familiar
to many Rustaceans.

For instance, if we want to examine whether an expression `expr` implements
`Drop` trait, we could access `LanguageItems` via our `LateContext`'s
[TyCtxt], which provides a `lang_items` method that will return the id of
`Drop` trait to us. Then, by calling Clippy utils function `implements_trait`
we can check that the `Ty` of the `expr` implements the trait:

```rust
use clippy_utils::ty::implements_trait;
use rustc_hir::Expr;
use rustc_lint::{LateContext, LateLintPass};

impl LateLintPass<'_> for CheckDropTraitLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);
        if cx.tcx.lang_items()
            .drop_trait()
            .map_or(false, |id| implements_trait(cx, ty, id, &[])) {
                println!("`expr` implements `Drop` trait!");
            }
    }
}
```

## Using Type Path

If neither diagnostic item nor a language item is available, we can use
[`clippy_utils::paths`][paths] to determine get a trait's `DefId`.

> **Note**: This approach should be avoided if possible, the best thing to do would be to make a PR to [`rust-lang/rust`][rust] adding a diagnostic item.

Below, we check if the given `expr` implements [`core::iter::Step`](https://doc.rust-lang.org/std/iter/trait.Step.html):

```rust
use clippy_utils::paths;
use clippy_utils::ty::implements_trait;
use rustc_hir::Expr;
use rustc_lint::{LateContext, LateLintPass};

impl LateLintPass<'_> for CheckIterStep {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);
        if let Some(trait_def_id) = paths::ITER_STEP.first(cx)
            && implements_trait(cx, ty, trait_def_id, &[])
        {
            println!("`expr` implements the `core::iter::Step` trait!");
        }
    }
}
```

## Creating Types Programmatically

Traits are often generic over a type parameter, e.g. `Borrow<T>` is generic
over `T`. Rust allows us to implement a trait for a specific type. For example,
we can implement `Borrow<[u8]>` for a hypothetical type `Foo`. Let's suppose
that we would like to find whether our type actually implements `Borrow<[u8]>`.

To do so, we can use the same `implements_trait` function as above, and supply
a type parameter that represents `[u8]`. Since `[u8]` is a specialization of
`[T]`, we can use the  [`Ty::new_slice`][new_slice] method to create a type
that represents `[T]` and supply `u8` as a type parameter.
To create a `ty::Ty` programmatically, we rely on `Ty::new_*` methods. These
methods create a `TyKind` and then wrap it in a `Ty` struct. This means we
have access to all the primitive types, such as `Ty::new_char`,
`Ty::new_bool`, `Ty::new_int`, etc. We can also create more complex types,
such as slices, tuples, and references out of these basic building blocks.

For trait checking, it is not enough to create the types, we need to convert
them into [GenericArg]. In rustc, a generic is an entity that the compiler
understands and has three kinds, type, const and lifetime. By calling
`.into()` on a constructed [Ty], we wrap the type into a generic which can
then be used by the query system to decide whether the specialized trait
is implemented.

The following code demonstrates how to do this:

```rust

use rustc_middle::ty::Ty;
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;

let ty = todo!("Get the `Foo` type to check for a trait implementation");
let borrow_id = cx.tcx.get_diagnostic_item(sym::Borrow).unwrap(); // avoid unwrap in real code
let slice_of_bytes_t = Ty::new_slice(cx.tcx, cx.tcx.types.u8);
let generic_param = slice_of_bytes_t.into();
if implements_trait(cx, ty, borrow_id, &[generic_param]) {
    todo!("Rest of lint implementation")
}
```

In essence, the [Ty] struct allows us to create types programmatically in a
representation that can be used by the compiler and the query engine. We then
use the `rustc_middle::Ty` of the type we are interested in, and query the
compiler to see if it indeed implements the trait we are interested in.


[DefId]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html
[diagnostic_items]: https://rustc-dev-guide.rust-lang.org/diagnostics/diagnostic-items.html
[lang_items]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/lang_items/struct.LanguageItems.html
[paths]: https://github.com/rust-lang/rust-clippy/blob/master/clippy_utils/src/paths.rs
[rustc_dev_guide]: https://rustc-dev-guide.rust-lang.org/
[symbol]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Symbol.html
[symbol_index]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_span/symbol/sym/index.html
[TyCtxt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html
[Ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[rust]: https://github.com/rust-lang/rust
[new_slice]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#method.new_slice
[GenericArg]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.GenericArg.html


---

# Method Checking

In some scenarios we might want to check for methods when developing
a lint. There are two kinds of questions that we might be curious about:

-   Invocation: Does an expression call a specific method?
-   Definition: Does an `impl` define a method?

## Checking if an `expr` is calling a specific method

Suppose we have an `expr`, we can check whether it calls a specific
method, e.g. `our_fancy_method`, by performing a pattern match on
the [`ExprKind`] that we can access from `expr.kind`:

```rust
use rustc_hir as hir;
use rustc_lint::{LateContext, LateLintPass};
use clippy_utils::res::{MaybeDef, MaybeTypeckRes};
use clippy_utils::sym;

impl<'tcx> LateLintPass<'tcx> for OurFancyMethodLint {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx hir::Expr<'_>) {
        // Check our expr is calling a method with pattern matching
        if let hir::ExprKind::MethodCall(path, _, _, _) = &expr.kind
            // Check if the name of this method is `our_fancy_method`
            && path.ident.name == sym::our_fancy_method
            // Check if the method belongs to the `sym::OurFancyTrait` trait.
            // (for example, a `map` method could belong to user-defined trait instead of to `Iterator`)
            // See the next section for more information.
            && cx.ty_based_def(expr).opt_parent(cx).is_diag_item(cx, sym::OurFancyTrait)
        {
            println!("`expr` is a method call for `our_fancy_method`");
        }
    }
}
```

Take a closer look at the `ExprKind` enum variant [`MethodCall`] for more
information on the pattern matching. As mentioned in [Define
Lints](defining_lints.md#lint-types), the `methods` lint type is full of pattern
matching with `MethodCall` in case the reader wishes to explore more.

New symbols such as `our_fancy_method` need to be added to the `clippy_utils::sym` module.
This module extends the list of symbols already provided by the compiler crates
in `rustc_span::sym`.

If a trait defines only one method (such as the `std::ops::Deref` trait, which only has the `deref()` method),
one might be tempted to omit the method name check. This would work, but is not always advisable because:
- If a new method (possibly with a default implementation) were to be added to the trait, there would be a risk of
  matching the wrong method.
- Comparing symbols is very cheap and might prevent a more expensive lookup.

## Checking if a `impl` block implements a method

While sometimes we want to check whether a method is being called or not, other
times we want to know if our `Ty` defines a method.

To check if our `impl` block defines a method `our_fancy_method`, we will
utilize the [`check_impl_item`] method that is available in our beloved
[`LateLintPass`] (for more information, refer to the ["Lint
Passes"](lint_passes.md) chapter in the Clippy book). This method provides us
with an [`ImplItem`] struct, which represents anything within an `impl` block.

Let us take a look at how we might check for the implementation of
`our_fancy_method` on a type:

```rust
use clippy_utils::{return_ty, sym};
use clippy_utils::res::MaybeDef;
use rustc_hir::{ImplItem, ImplItemKind};
use rustc_lint::{LateContext, LateLintPass};

impl<'tcx> LateLintPass<'tcx> for MyTypeImpl {
    fn check_impl_item(&mut self, cx: &LateContext<'tcx>, impl_item: &'tcx ImplItem<'_>) {
        // Check if item is a method/function
        if let ImplItemKind::Fn(ref signature, _) = impl_item.kind
            // Check the method is named `our_fancy_method`
            && impl_item.ident.name.as_str() == "our_fancy_method"
            // We can also check it has a parameter `self`
            && signature.decl.implicit_self.has_implicit_self()
            // We can go even further and even check if its return type is `String`
            && return_ty(cx, impl_item.hir_id).is_diag_item(cx, sym::String)
        {
            println!("`our_fancy_method` is implemented!");
        }
    }
}
```

[`check_impl_item`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_lint/trait.LateLintPass.html#method.check_impl_item
[`ExprKind`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_hir/hir/enum.ExprKind.html
[`ImplItem`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_hir/hir/struct.ImplItem.html
[`LateLintPass`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_lint/trait.LateLintPass.html
[`MethodCall`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_hir/hir/enum.ExprKind.html#variant.MethodCall


---

# Dealing with macros and expansions

Sometimes we might encounter Rust macro expansions while working with Clippy.
While macro expansions are not as dramatic and profound as the expansion
of our universe, they can certainly bring chaos to the orderly world
of code and logic.

The general rule of thumb is that we should ignore code with macro
expansions when working with Clippy because the code can be dynamic
in ways that are difficult or impossible for us to foresee.

## False Positives

What exactly do we mean by _dynamic in ways that are difficult to foresee_?

Macros are [expanded][expansion] in the `EarlyLintPass` level,
so the Abstract Syntax Tree (AST) is generated in place of macros.
This means the code which we work with in Clippy is already expanded.

If we wrote a new lint, there is a possibility that the lint is
triggered in macro-generated code. Since this expanded macro code
is not written by the macro's user but really by the macro's author,
the user cannot and should not be responsible for fixing the issue
that triggers the lint.

Besides, a [Span] in a macro can be changed by the macro author.
Therefore, any lint check related to lines or columns should be
avoided since they might be changed at any time and become unreliable
or incorrect information.

Because of these unforeseeable or unstable behaviors, macro expansion
should often not be regarded as a part of the stable API.
This is also why most lints check if they are inside a macro or not
before emitting suggestions to the end user to avoid false positives.

## How to Work with Macros

Several functions are available for working with macros.

### The `Span::from_expansion` method

We could utilize a `span`'s [`from_expansion`] method, which
detects if the `span` is from a macro expansion / desugaring.
This is a very common first step in a lint:

```rust
if expr.span.from_expansion() {
    // We most likely want to ignore it.
    return;
}
```

### `Span::ctxt` method

The `span`'s context, given by the method [`ctxt`] and returning [SyntaxContext],
represents if the span is from a macro expansion and, if it is, which
macro call expanded this span.

Sometimes, it is useful to check if the context of two spans are equal.
For instance, suppose we have the following line of code that would
expand into `1 + 0`:

```rust
// The following code expands to `1 + 0` for both `EarlyLintPass` and `LateLintPass`
1 + mac!()
```

Assuming that we'd collect the `1` expression as a variable `left` and the
`0`/`mac!()` expression as a variable `right`, we can simply compare their
contexts. If the context is different, then we most likely are dealing with a
macro expansion and should just ignore it:

```rust
if left.span.ctxt() != right.span.ctxt() {
    // The code author most likely cannot modify this expression
    return;
}
```

> **Note**: Code that is not from expansion is in the "root" context.
> So any spans whose `from_expansion` returns `false` can be assumed
> to have the same context. Because of this, using `span.from_expansion()`
> is often sufficient.

Going a bit deeper, in a simple expression such as `a == b`,
`a` and `b` have the same context.
However, in a `macro_rules!` with `a == $b`, `$b` is expanded to
an expression that contains a different context from `a`.

Take a look at the following macro `m`:

```rust
macro_rules! m {
    ($a:expr, $b:expr) => {
        if $a.is_some() {
            $b;
        }
    }
}

let x: Option<u32> = Some(42);
m!(x, x.unwrap());
```

If the `m!(x, x.unwrap());` line is expanded, we would get two expanded
expressions:

- `x.is_some()` (from the `$a.is_some()` line in the `m` macro)
- `x.unwrap()` (corresponding to `$b` in the `m` macro)

Suppose `x.is_some()` expression's span is associated with the `x_is_some_span` variable
and `x.unwrap()` expression's span is associated with `x_unwrap_span` variable,
we could assume that these two spans do not share the same context:

```rust
// x.is_some() is from inside the macro
// x.unwrap() is from outside the macro
assert_ne!(x_is_some_span.ctxt(), x_unwrap_span.ctxt());
```

### The `in_external_macro` function

`Span` provides a method ([`in_external_macro`]) that can
detect if the given span is from a macro defined in a foreign crate.

Therefore, if we really want a new lint to work with macro-generated code,
this is the next line of defense to avoid macros not defined inside
the current crate since it is unfair to the user if Clippy lints code
which the user cannot change.

For example, assume we have the following code that is being examined
by Clippy:

```rust
#[macro_use]
extern crate a_foreign_crate_with_macros;

// `foo` macro is defined in `a_foreign_crate_with_macros`
foo!("bar");
```

Also assume that we get the corresponding variable `foo_span` for the
`foo` macro call, we could decide not to lint if `in_external_macro`
results in `true` (note that `cx` can be `EarlyContext` or `LateContext`):

```rust
if foo_span.in_external_macro(cx.sess().source_map()) {
    // We should ignore macro from a foreign crate.
    return;
}
```

### The `is_from_proc_macro` function
A common point of confusion is the existence of [`is_from_proc_macro`]
and how it differs from the other [`in_external_macro`]/[`from_expansion`] functions.

While [`in_external_macro`] and [`from_expansion`] both work perfectly fine for detecting expanded code
from *declarative* macros (i.e. `macro_rules!` and macros 2.0),
detecting *proc macro*-generated code is a bit more tricky, as proc macros can (and often do)
freely manipulate the span of returned tokens.

In practice, this often happens through the use of [`quote::quote_spanned!`] with a span from the input tokens. 

In those cases, there is no *reliable* way for the compiler (and tools like Clippy)
to distinguish code that comes from such a proc macro from code that the user wrote directly,
and [`in_external_macro`] will return `false`.

This is usually not an issue for the compiler and actually helps proc macro authors create better error messages,
as it allows associating parts of the expansion with parts of the macro input and lets the compiler
point the user to the relevant code in case of a compile error.

However, for Clippy this is inconvenient, because most of the time *we don't* want
to lint proc macro-generated code and this makes it impossible to tell what is and isn't proc macro code.

> NOTE: this is specifically only an issue when a proc macro explicitly sets the span to that of an **input span**.
>
> For example, other common ways of creating `TokenStream`s, such as `"fn foo() {...}".parse::<TokenStream>()`,
> sets each token's span to `Span::call_site()`, which already marks the span as coming from a proc macro
> and the usual span methods have no problem detecting that as a macro span.

As such, Clippy has its own `is_from_proc_macro` function which tries to *approximate*
whether a span comes from a proc macro, by checking whether the source text at the given span
lines up with the given AST node.

This function is typically used in combination with the other mentioned macro span functions,
but is usually called much later into the condition chain as it's a bit heavier than most other conditions,
so that the other cheaper conditions can fail faster. For example, the `borrow_deref_ref` lint:
```rs
impl<'tcx> LateLintPass<'tcx> for BorrowDerefRef {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, e: &rustc_hir::Expr<'tcx>) {
        if let ... = ...
            && ...
            && !e.span.from_expansion()
            && ...
            && ...
            && !is_from_proc_macro(cx, e)
            && ...
        {
            ...
        }
    }
}
```

### Testing lints with macro expansions
To test that all of these cases are handled correctly in your lint,
we have a helper auxiliary crate that exposes various macros, used by tests like so:
```rust
//@aux-build:proc_macros.rs

extern crate proc_macros;

fn main() {
    proc_macros::external!{ code_that_should_trigger_your_lint }
    proc_macros::with_span!{ span code_that_should_trigger_your_lint }
}
```
This exercises two cases:
- `proc_macros::external!` is a simple proc macro that echos the input tokens back but with a macro span:
this represents the usual, common case where an external macro expands to code that your lint would trigger,
and is correctly handled by `in_external_macro` and `Span::from_expansion`.

- `proc_macros::with_span!` echos back the input tokens starting from the second token
with the span of the first token: this is where the other functions will fail and `is_from_proc_macro` is needed


[`ctxt`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_span/struct.Span.html#method.ctxt
[expansion]: https://rustc-dev-guide.rust-lang.org/macro-expansion.html#expansion-and-ast-integration
[`from_expansion`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_span/struct.Span.html#method.from_expansion
[`in_external_macro`]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_span/struct.Span.html#method.in_external_macro
[Span]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_span/struct.Span.html
[SyntaxContext]: https://doc.rust-lang.org/stable/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html
[`is_from_proc_macro`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/fn.is_from_proc_macro.html
[`quote::quote_spanned!`]: https://docs.rs/quote/latest/quote/macro.quote_spanned.html
