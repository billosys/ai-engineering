# The HIR

The HIR – "High-Level Intermediate Representation" – is the primary IR used
in most of rustc.
It is a compiler-friendly representation of the abstract
syntax tree (AST) that is generated after parsing, macro expansion, and name
resolution (see [Lowering](./hir/lowering.md) for how the HIR is created).
Many parts of HIR resemble Rust surface syntax quite closely, with
the exception that some of Rust's expression forms have been desugared away.
For example, `for` loops are converted into a `loop` and do not appear in
the HIR.
This makes HIR more amenable to analysis than a normal AST.

This chapter covers the main concepts of the HIR.

You can view the HIR representation of your code by passing the
`-Z unpretty=hir-tree` flag to rustc:

```bash
cargo rustc -- -Z unpretty=hir-tree
```


You can also use the `-Z unpretty=hir` option to generate a HIR
that is closer to the original source code expression:

```bash
cargo rustc -- -Z unpretty=hir
```

## Out-of-band storage and the `Crate` type

The top-level data-structure in the HIR is the [`Crate`], which stores
the contents of the crate currently being compiled (we only ever
construct HIR for the current crate).
Whereas in the AST the crate
data structure basically just contains the root module, the HIR
`Crate` structure contains a number of maps and other things that
serve to organize the content of the crate for easier access.

[`Crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/hir/struct.Crate.html

For example, the contents of individual items (e.g. modules,
functions, traits, impls, etc) in the HIR are not immediately
accessible in the parents.
So, for example, if there is a module item `foo` containing a function `bar()`:

```rust
mod foo {
    fn bar() { }
}
```

then in the HIR the representation of module `foo` (the [`Mod`]
struct) would only have the **`ItemId`** `I` of `bar()`.
To get the details of the function `bar()`, we would lookup `I` in the
`items` map.

[`Mod`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Mod.html

One nice result from this representation is that one can iterate
over all items in the crate by iterating over the key-value pairs
in these maps (without the need to trawl through the whole HIR).
There are similar maps for things like trait items and impl items,
as well as "bodies" (explained below).

The other reason to set up the representation this way is for better
integration with incremental compilation.
This way, if you gain access
to an [`&rustc_hir::Item`] (e.g. for the mod `foo`), you do not immediately
gain access to the contents of the function `bar()`.
Instead, you only
gain access to the **id** for `bar()`, and you must invoke some
function to lookup the contents of `bar()` given its id; this gives
the compiler a chance to observe that you accessed the data for
`bar()`, and then record the dependency.

[`&rustc_hir::Item`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Item.html

<a id="hir-id"></a>

## Identifiers in the HIR

The HIR uses a bunch of different identifiers that coexist and serve different purposes.

- A [`DefId`], as the name suggests, identifies a particular definition, or top-level
  item, in a given crate.
  It is composed of two parts: a [`CrateNum`] which identifies
  the crate the definition comes from, and a [`DefIndex`] which identifies the definition
  within the crate.
  Unlike [`HirId`]s, there isn't a [`DefId`] for every expression, which
  makes them more stable across compilations.

- A [`LocalDefId`] is basically a [`DefId`] that is known to come from the current crate.
  This allows us to drop the [`CrateNum`] part, and use the type system to ensure that
  only local definitions are passed to functions that expect a local definition.

- A [`HirId`] uniquely identifies a node in the HIR of the current crate.
  It is composed of two parts:
  an `owner` and a `local_id` that is unique within the `owner`.
  This combination makes for more stable values which are helpful for incremental compilation.
  Unlike [`DefId`]s, a [`HirId`] can refer to [fine-grained entities][Node] like expressions,
  but stays local to the current crate.

- A [`BodyId`] identifies a HIR [`Body`] in the current crate.
  It is currently only a wrapper around a [`HirId`].
  For more info about HIR bodies, please refer to the
  [HIR chapter][hir-bodies].

These identifiers can be converted into one another through the `TyCtxt`.

[`DefId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html
[`LocalDefId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.LocalDefId.html
[`HirId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/struct.HirId.html
[`BodyId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.BodyId.html
[Node]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.Node.html
[`CrateNum`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.CrateNum.html
[`DefIndex`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefIndex.html
[`Body`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Body.html
[hir-bodies]: ./hir.md#hir-bodies

## HIR Operations

Most of the time when you are working with the HIR, you will do so via `TyCtxt`.
It contains a number of methods, defined in the `hir::map` module and
mostly prefixed with `hir_`, to convert between IDs of various kinds and to
lookup data associated with a HIR node.

[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html

For example, if you have a [`LocalDefId`], and you would like to convert it
to a [`HirId`], you can use [`tcx.local_def_id_to_hir_id(def_id)`][local_def_id_to_hir_id].
You need a `LocalDefId`, rather than a `DefId`, since only local items have HIR nodes.

[local_def_id_to_hir_id]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.local_def_id_to_hir_id

Similarly, you can use [`tcx.hir_node(n)`][hir_node] to lookup the node for a
[`HirId`].
This returns a `Option<Node<'hir>>`, where [`Node`] is an enum
defined in the map.
By matching on this, you can find out what sort of
node the `HirId` referred to and also get a pointer to the data
itself. Often, you know what sort of node `n` is – e.g. if you know
that `n` must be some HIR expression, you can do
[`tcx.hir_expect_expr(n)`][expect_expr], which will extract and return the
[`&hir::Expr`][Expr], panicking if `n` is not in fact an expression.

[hir_node]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.hir_node
[`Node`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.Node.html
[expect_expr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.expect_expr
[Expr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Expr.html

Finally, you can find the parents of nodes, via
calls like [`tcx.parent_hir_node(n)`][parent_hir_node].

[parent_hir_node]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.parent_hir_node


## HIR Bodies

A [`rustc_hir::Body`] represents some kind of executable code, such as the body
of a function/closure or the definition of a constant.
Bodies are associated with an **owner**, which is typically some kind of item
(e.g. an `fn()` or `const`), but could also be a closure expression
(e.g. `|x, y| x + y`). You can use the `TyCtxt` to find the body
associated with a given def-id ([`hir_maybe_body_owned_by`]) or to find
the owner of a body ([`hir_body_owner_def_id`]).

[`rustc_hir::Body`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Body.html
[`hir_maybe_body_owned_by`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.hir_maybe_body_owned_by
[`hir_body_owner_def_id`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.hir_body_owner_def_id


---

# AST lowering

The AST lowering step converts AST to [HIR](../hir.md).
This means many structures are removed if they are irrelevant
for type analysis or similar syntax agnostic analyses. Examples
of such structures include but are not limited to

* Parenthesis
    * Removed without replacement, the tree structure makes order explicit
* `for` loops
    * Converted to `match` + `loop` + `match`
* Universal `impl Trait`
    * Converted to generic arguments
      (but with some flags, to know that the user didn't write them)
* Existential `impl Trait`
    * Converted to a virtual `existential type` declaration

The implementation of AST lowering is in the [`rustc_ast_lowering`] crate.
The entry point is [`lower_to_hir`], which retrieves the post-expansion AST
and resolver data from [`TyCtxt`] and builds the [`hir::Crate`] for the whole crate.

Lowering is organized around HIR owners. [`lower_to_hir`] first indexes the
crate and then [`ItemLowerer::lower_node`] lowers each crate, item, associated
item, and foreign item.

Most of the lowering logic lives on [`LoweringContext`]. The implementation is
split across multiple files in the [`rustc_ast_lowering`] crate such as `item.rs`,
`expr.rs`, `pat.rs`, `path.rs`, and others, but they all share the same [`LoweringContext`]
state and ID‑lowering machinery.

Each owner is lowered in its own [`with_hir_id_owner`] scope. This is why the
`HirId` invariants below matter: `lower_node_id` maps AST `NodeId`s into the
current owner, while `next_id` creates fresh HIR-only nodes introduced during
desugaring.

Lowering needs to uphold several invariants in order to not trigger the
sanity checks in [`compiler/rustc_passes/src/hir_id_validator.rs`][hir_id_validator]:

1. A `HirId` must be used if created. So if you use the `lower_node_id`,
  you *must* use the resulting `NodeId` or `HirId` (either is fine, since
  any `NodeId`s in the `HIR` are checked for existing `HirId`s)
2. Lowering a `HirId` must be done in the scope of the *owning* item.
  This means you need to use `with_hir_id_owner` if you are creating parts
  of an item other than the one being currently lowered. This happens for
  example during the lowering of existential `impl Trait`
3. A `NodeId` that will be placed into a HIR structure must be lowered,
  even if its `HirId` is unused. Calling
  `let _ = self.lower_node_id(node_id);` is perfectly legitimate.
4. If you are creating new nodes that didn't exist in the `AST`, you *must*
  create new ids for them. This is done by calling the `next_id` method,
  which produces both a new `NodeId` as well as automatically lowering it
  for you so you also get the `HirId`.

[`rustc_ast_lowering`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/index.html
[`lower_to_hir`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/fn.lower_to_hir.html
[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html
[`hir::Crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/hir/struct.Crate.html
[`ItemLowerer::lower_node`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/item/struct.ItemLowerer.html
[`LoweringContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/struct.LoweringContext.html
[`with_hir_id_owner`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/struct.LoweringContext.html#method.with_hir_id_owner
[hir_id_validator]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_passes/src/hir_id_validator.rs

If you are creating new `DefId`s, since each `DefId` needs to have a
corresponding `NodeId`, it is advisable to add these `NodeId`s to the
`AST` so you don't have to generate new ones during lowering. This has
the advantage of creating a way to find the `DefId` of something via its
`NodeId`. If lowering needs this `DefId` in multiple places, you can't
generate a new `NodeId` in all those places because you'd also get a new
`DefId` then. With a `NodeId` from the `AST` this is not an issue.

Having the `NodeId` also allows the `DefCollector` to generate the `DefId`s
instead of lowering having to do it on the fly. Centralizing the `DefId`
generation in one place makes it easier to refactor and reason about.


---

# HIR Debugging

Use the `-Z unpretty=hir` flag to produce a human-readable representation of the HIR.
For cargo projects this can be done with `cargo rustc -- -Z unpretty=hir`.
This output is useful when you need to see at a glance how your code was desugared and transformed
during AST lowering.

For a full `Debug` dump of the data in the HIR, use the `-Z unpretty=hir-tree` flag.
This may be useful when you need to see the full structure of the HIR from the perspective of the
compiler.

If you are trying to correlate `NodeId`s or `DefId`s with source code, the
`-Z unpretty=expanded,identified` flag may be useful.

TODO: anything else? [#1159](https://github.com/rust-lang/rustc-dev-guide/issues/1159)


---

# Ambig/Unambig Types and Consts

Types and Consts args in the AST/HIR can be in two kinds of positions ambiguous (ambig) or unambiguous (unambig). Ambig positions are where
it would be valid to parse either a type or a const, unambig positions are where only one kind would be valid to
parse.

```rust
fn func<T, const N: usize>(arg: T) {
    //                          ^ Unambig type position
    let a: _ = arg; 
    //     ^ Unambig type position

    func::<T, N>(arg);
    //     ^  ^
    //     ^^^^ Ambig position 

    let _: [u8; 10];
    //      ^^  ^^ Unambig const position
    //      ^^ Unambig type position
}

```

Most types/consts in ambig positions are able to be disambiguated as either a type or const during parsing. The only exceptions to this are paths and inferred generic arguments.

## Paths

```rust
struct Foo<const N: usize>;

fn foo<const N: usize>(_: Foo<N>) {}
```

At parse time we parse all unbraced generic arguments as *types* (ie they wind up as [`ast::GenericArg::Ty`]). In the above example this means we would parse the generic argument to `Foo` as an `ast::GenericArg::Ty` wrapping a [`ast::Ty::Path(N)`].

Then during name resolution:
- When encountering a single segment path with no generic arguments in generic argument position, we will first try to resolve it in the type namespace and if that fails we then attempt to resolve in the value namespace.
- All other kinds of paths we only try to resolve in the type namespace

See [`LateResolutionVisitor::visit_generic_arg`] for where this is implemented.

Finally during AST lowering when we attempt to lower a type argument, we first check if it is a `Ty::Path` and if it resolved to something in the value namespace. If it did then we create an *anon const* and lower to a const argument instead of a type argument.

See [`LoweringContext::lower_generic_arg`] for where this is implemented.

Note that the ambiguity for paths is not propgated into the HIR; there's no `hir::GenericArg::Path` which is turned into either a `Ty` or `Const` during HIR ty lowering (though we could do such a thing).

## Inferred arguments (`_`)

```rust
struct Foo<const N: usize>;

fn foo() {
    let _unused: Foo<_>;
}
```

The only generic arguments which remain ambiguous after lowering are inferred generic arguments (`_`) in path segments. In the above example it is not clear at parse time whether the `_` argument to `Foo` is an inferred type argument, or an inferred const argument.

In ambig AST positions, inferred argumentsd are parsed as an [`ast::GenericArg::Ty`] wrapping a [`ast::Ty::Infer`]. Then during AST lowering when lowering an `ast::GenericArg::Ty` we check if it is an inferred type and if so lower to a [`hir::GenericArg::Infer`].

In unambig AST positions, inferred arguments are parsed as either `ast::Ty::Infer` or [`ast::AnonConst`]. The `AnonConst` case is quite strange, we use [`ast::ExprKind::Underscore`] to represent the "body" of the "anon const" although in reality we do not actually lower this to an anon const in the HIR.

It may be worth seeing if we can refactor the AST to have `ast::GenericArg::Infer` and then get rid of this overloaded meaning of `AnonConst`, as well as the reuse of `ast::Ty::Infer` in ambig positions.

In unambig AST positions, during AST lowering we lower inferred arguments to [`hir::TyKind::Infer`][ty_infer] or [`hir::ConstArgKind::Infer`][const_infer] depending on whether it is a type or const position respectively.
In ambig AST positions, during AST lowering we lower inferred arguments to [`hir::GenericArg::Infer`][generic_arg_infer]. See [`LoweringContext::lower_generic_arg`] for where this is implemented.

A naive implementation of this would result in there being potentially 5 places where you might think an inferred type/const could be found in the HIR from looking at the structure of the HIR:
1. In unambig type position as a `TyKind::Infer`
2. In unambig const arg position as a `ConstArgKind::Infer`
3. In an ambig position as a [`GenericArg::Type(TyKind::Infer)`][generic_arg_ty]
4. In an ambig position as a [`GenericArg::Const(ConstArgKind::Infer)`][generic_arg_const]
5. In an ambig position as a `GenericArg::Infer`

Note that places 3 and 4 would never actually be possible to encounter as we always lower to `GenericArg::Infer` in generic arg position. 

This has a few failure modes:
- People may write visitors which check for `GenericArg::Infer` but forget to check for `hir::TyKind/ConstArgKind::Infer`, only handling infers in ambig positions by accident.
- People may write visitors which check for `TyKind/ConstArgKind::Infer` but forget to check for `GenericArg::Infer`, only handling infers in unambig positions by accident.
- People may write visitors which check for `GenericArg::Type/Const(TyKind/ConstArgKind::Infer)` and `GenericArg::Infer`, not realising that we never represent inferred types/consts in ambig positions as a `GenericArg::Type/Const`.
- People may write visitors which check for *only* `TyKind::Infer` and not `ConstArgKind::Infer` forgetting that there are also inferred const arguments (and vice versa).

To make writing HIR visitors less error prone when caring about inferred types/consts we have a relatively complex system:

1. We have different types in the compiler for when a type or const is in an unambig or ambig position, `Ty<AmbigArg>` and `Ty<()>`. [`AmbigArg`][ambig_arg] is an uninhabited type which we use in the `Infer` variant of `TyKind` and `ConstArgKind` to selectively "disable" it if we are in an ambig position.

2. The [`visit_ty`][visit_ty] and [`visit_const_arg`][visit_const_arg] methods on HIR visitors only accept the ambig position versions of types/consts. Unambig types/consts are implicitly converted to ambig types/consts during the visiting process, with the `Infer` variant handled by a dedicated [`visit_infer`][visit_infer] method.

This has a number of benefits:
- It's clear that `GenericArg::Type/Const` cannot represent inferred type/const arguments
- Implementors of `visit_ty` and `visit_const_arg` will never encounter inferred types/consts making it impossible to write a visitor that seems to work right but handles edge cases wrong 
- The `visit_infer` method handles *all* cases of inferred type/consts in the HIR making it easy for visitors to handle inferred type/consts in one dedicated place and not forget cases

[ty_infer]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.TyKind.html#variant.Infer
[const_infer]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.ConstArgKind.html#variant.Infer
[generic_arg_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.GenericArg.html#variant.Type
[generic_arg_const]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.GenericArg.html#variant.Const
[generic_arg_infer]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.GenericArg.html#variant.Infer
[ambig_arg]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.AmbigArg.html
[visit_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/intravisit/trait.Visitor.html#method.visit_ty
[visit_const_arg]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/intravisit/trait.Visitor.html#method.visit_const_arg
[visit_infer]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/intravisit/trait.Visitor.html#method.visit_infer
[`LateResolutionVisitor::visit_generic_arg`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/late/struct.LateResolutionVisitor.html#method.visit_generic_arg
[`LoweringContext::lower_generic_arg`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/struct.LoweringContext.html#method.lower_generic_arg
[`ast::GenericArg::Ty`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/enum.GenericArg.html#variant.Type
[`ast::Ty::Infer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/enum.TyKind.html#variant.Infer
[`ast::AnonConst`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/struct.AnonConst.html
[`hir::GenericArg::Infer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.GenericArg.html#variant.Infer
[`ast::ExprKind::Underscore`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/enum.ExprKind.html#variant.Underscore
[`ast::Ty::Path(N)`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/enum.TyKind.html#variant.Path
