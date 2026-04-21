# Analysis

This part discusses the many analyses that the compiler uses to check various
properties of the code and to inform later stages. Typically, this is what people
mean when they talk about "Rust's type system". This includes the
representation, inference, and checking of types, the trait system, and the
borrow checker. These analyses do not happen as one big pass or set of
contiguous passes. Rather, they are spread out throughout various parts of the
compilation process and use different intermediate representations. For example,
type checking happens on the HIR, while borrow checking happens on the MIR.
Nonetheless, for the sake of presentation, we will discuss all of these
analyses in this part of the guide.


---

# Generic parameter definitions

This chapter will discuss how rustc tracks what generic parameters are introduced. For example given some `struct Foo<T>` how does rustc track that `Foo` defines some type parameter `T` (and no other generic parameters).

This will *not* cover how we track generic parameters introduced via `for<'a>` syntax (e.g. in where clauses or `fn` types), which is covered elsewhere in the [chapter on `Binder`s ][ch_binders].

# `ty::Generics`

The generic parameters introduced by an item are tracked by the [`ty::Generics`] struct. Sometimes items allow usage of generics defined on parent items, this is accomplished via the `ty::Generics` struct having an optional field to specify a parent item to inherit generic parameters of. For example given the following code:

```rust,ignore
trait Trait<T> {
    fn foo<U>(&self);
}
```

The `ty::Generics` used for `foo` would contain `[U]` and a parent of `Some(Trait)`. `Trait` would have a `ty::Generics` containing `[Self, T]` with a parent of `None`.

The [`GenericParamDef`] struct is used to represent each individual generic parameter in a `ty::Generics` listing. The `GenericParamDef` struct contains information about the generic parameter, for example its name, defid, what kind of parameter it is (i.e. type, const, lifetime).

`GenericParamDef` also contains a `u32` index representing what position the parameter is (starting from the outermost parent), this is the value used to represent usages of generic parameters (more on this in the [chapter on representing types][ch_representing_types]).

Interestingly, `ty::Generics` does not currently contain _every_ generic parameter defined on an item. In the case of functions it only contains the _early bound_ parameters.

[ch_representing_types]: ./ty.md
[`ty::Generics`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Generics.html
[`GenericParamDef`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/generics/struct.GenericParamDef.html
[ch_binders]: ./ty-module/binders.md


---

# `EarlyBinder` and instantiating parameters

Given an item that introduces a generic parameter `T`, whenever we refer to types inside of `foo` (i.e. the return type or argument types) from outside of `foo` we must take care to handle the generic parameters defined on `foo`. As an example:

```rust,ignore
fn foo<T, U>(a: T, _b: U) -> T { a }

fn main() {
    let c = foo::<i32, u128>(1, 2);
}
```

When type checking `main` we cannot just naively look at the return type of `foo` and assign the type `T` to the variable `c`, The function `main` does not define any generic parameters, `T` is completely meaningless in this context. More generally whenever an item introduces (binds) generic parameters, when accessing types inside the item from outside, the generic parameters must be instantiated with values from the outer item.

In rustc we track this via the [`EarlyBinder`] type, the return type of `foo` is represented as an `EarlyBinder<Ty>` with the only way to access `Ty` being to provide arguments for any generic parameters `Ty` might be using. This is implemented via the [`EarlyBinder::instantiate`] method which discharges the binder returning the inner value with all the generic parameters replaced by the provided arguments.

To go back to our example, when type checking `main` the return type of `foo` would be represented as `EarlyBinder(T/#0)`. Then, because we called the function with `i32, u128` for the generic arguments, we would call `EarlyBinder::instantiate` on the return type with `[i32, u128]` for the args. This would result in an instantiated return type of `i32` that we can use as the type of the local `c`.

Here are some more examples:

```rust,ignore
fn foo<T>() -> Vec<(u32, T)> { Vec::new() }
fn bar() {
    // the return type of `foo` before instantiating it would be:
    // `EarlyBinder(Adt(Vec, &[Tup(&[u32, T/#=0])]))`
    // we then instantiate the binder with `[u64]` resulting in the type:
    // `Adt(Vec, &[Tup(&[u32, u64])])`
    let a = foo::<u64>();
}
```

```rust,ignore
struct Foo<A, B> {
    x: Vec<A>,
    ..
}

fn bar(foo: Foo<u32, f32>) { 
    // the type of `foo`'s `x` field before instantiating it would be:
    // `EarlyBinder(Vec<A/#0>)`
    // we then instantiate the binder with `[u32, f32]` as those are the
    // generic arguments to the `Foo` struct. This results in a type of:
    // `Vec<u32>`
    let y = foo.x;
}
```

In the compiler the `instantiate` call for this is done in [`FieldDef::ty`] ([src][field_def_ty_src]), at some point during type checking `bar` we will wind up calling `FieldDef::ty(x, &[u32, f32])` in order to obtain the type of `foo.x`.

**Note on indices:** It is a bug if the index of a `Param` does not match what the `EarlyBinder` binds. For
example, if the index is out of bounds or the index of a lifetime corresponds to a type parameter.
These sorts of errors are caught earlier in the compiler during name resolution where we disallow references
to generics parameters introduced by items that should not be nameable by the inner item. 

[`FieldDef::ty`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.FieldDef.html#method.ty
[field_def_ty_src]: https://github.com/rust-lang/rust/blob/44d679b9021f03a79133021b94e6d23e9b55b3ab/compiler/rustc_middle/src/ty/mod.rs#L1421-L1426
[`EarlyBinder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.EarlyBinder.html
[`EarlyBinder::instantiate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.EarlyBinder.html#method.instantiate

---

As mentioned previously when _outside_ of an item, it is important to instantiate the `EarlyBinder` with generic arguments before accessing the value inside, but the setup for when we are conceptually inside of the binder already is a bit different.

For example:
```rust
impl<T> Trait for Vec<T> {
    fn foo(&self, b: Self) {}
}
```

When constructing a `Ty` to represent the `b` parameter's type we need to get the type of `Self` on the impl that we are inside. This can be acquired by calling the [`type_of`] query with the `impl`'s `DefId`, however, this will return a `EarlyBinder<Ty>` as the impl block binds generic parameters that may have to be discharged if we are outside of the impl.

The `EarlyBinder` type provides an [`instantiate_identity`] function for discharging the binder when you are "already inside of it". This is effectively a more performant version of writing `EarlyBinder::instantiate(GenericArgs::identity_for_item(..))`. Conceptually this discharges the binder by instantiating it with placeholders in the root universe (we will talk about what this means in the next few chapters). In practice though it simply returns the inner value with no modification taking place.

[`type_of`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.type_of
[`instantiate_identity`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.EarlyBinder.html#method.instantiate_identity


---

# `Binder` and Higher ranked regions

Sometimes, we define generic parameters not on an item but as part of a type or a where clause.
As an example, the type `for<'a> fn(&'a u32)` or the where clause `for<'a> T: Trait<'a>` both introduce a generic lifetime named `'a`.
Currently, there is no stable syntax for `for<T>` or `for<const N: usize>`,
but on nightly, `feature(non_lifetime_binders)` can be used to write where clauses (but not types) using `for<T>`/`for<const N: usize>`.

The `for` is referred to as a "binder" because it brings new names into scope.
In rustc we use the `Binder` type to track where these parameters are introduced and what the parameters are (i.e. how many and whether the parameter is a type/const/region). A type such as `for<'a> fn(&'a u32)` would be
represented in rustc as:
```
Binder(
    fn(&RegionKind::Bound(DebruijnIndex(0), BoundVar(0)) u32) -> (),
    &[BoundVariableKind::Region(...)],
)
```

Usages of these parameters is represented by the `RegionKind::Bound` (or `TyKind::Bound`/`ConstKind::Bound` variants).
These bound regions/types/consts are composed of two main pieces of data:
- A [DebruijnIndex](../appendix/background.md#what-is-a-de-bruijn-index) to specify which binder we are referring to.
- A [`BoundVar`] which specifies which of the parameters that the `Binder` introduces we are referring to.

We also sometimes store some extra information for diagnostics reasons via the [`BoundTyKind`]/[`BoundRegionKind`],
but this is not important for type equality, or, more generally, the semantics of `Ty`.
(omitted from the above example)

In debug output (and also informally when talking to each other),
we tend to write these bound variables in the format of `^DebruijnIndex_BoundVar`.
The above example would instead be written as `Binder(fn(&'^0_0), &[BoundVariableKind::Region])`.
Sometimes, when the `DebruijnIndex` is `0`, we just omit it and would write `^0`.

Another concrete example, this time a mixture of `for<'a>` in a where clause and a type:
```
where
    for<'a> Foo<for<'b> fn(&'a &'b T)>: Trait,
```
This would be represented as
```
Binder(
    Foo<Binder(
        fn(&'^1_0 &'^0 T/#0),
        [BoundVariableKind::Region(...)]
    )>: Trait,
    [BoundVariableKind::Region(...)]
)
```

Note how the `'^1_0` refers to the `'a` parameter.
We use a `DebruijnIndex` of `1` to refer to the binder one level up from the innermost one, and a var of `0` to refer to the first parameter bound which is `'a`.
We also use `'^0` to refer to the `'b` parameter, the `DebruijnIndex` is `0` (referring to the innermost binder) so we omit it, leaving only the boundvar of `0` referring to the first parameter bound which is `'b`.

We did not always explicitly track the set of bound vars introduced by each `Binder`,
and this caused a number of bugs (read: ICEs [#81193](https://github.com/rust-lang/rust/issues/81193), [#79949](https://github.com/rust-lang/rust/issues/79949), [#83017](https://github.com/rust-lang/rust/issues/83017)).
By tracking these explicitly, we can assert when constructing higher ranked where clauses/types that there are no escaping bound variables or variables from a different binder.
See the following example of an invalid type inside of a binder:
```
Binder(
    fn(&'^1_0 &'^1 T/#0),
    &[BoundVariableKind::Region(...)],
)
```
This would cause all kinds of issues as the region `'^1_0` refers to a binder at a higher level than the outermost binder i.e. it is an escaping bound var.
The `'^1` region (also writeable as `'^0_1`) is also ill formed as the binder it refers to does not introduce a second parameter.
Modern day rustc will ICE when constructing this binder due to both of those reasons.
In the past, we would have simply allowed this to work and then ran into issues in other parts of the codebase.

[`Binder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Binder.html
[`BoundVar`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.BoundVar.html
[`BoundRegionKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.BoundRegionKind.html
[`BoundTyKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.BoundTyKind.html


---

# Instantiating `Binder`s

Much like [`EarlyBinder`], when accessing the inside of a [`Binder`], we must first discharge it by replacing the bound vars with some other value.
This is for much the same reason as with `EarlyBinder`, types referencing parameters introduced by the `Binder` do not make any sense outside of that binder.
See the following erroring example:
```rust,ignore
fn foo<'a>(a: &'a u32) -> &'a u32 {
    a
}
fn bar<T>(a: fn(&u32) -> T) -> T {
    a(&10)
}

fn main() {
    let higher_ranked_fn_ptr = foo as for<'a> fn(&'a u32) -> &'a u32;
    // Attempt to infer `T=for<'a> &'a u32` which is not satsifiable
    let references_bound_vars = bar(higher_ranked_fn_ptr);
}
```
In this example, we are providing an argument of type `for<'a> fn(&'^0 u32) -> &'^0 u32` to `bar`.
We do not want to allow `T` to be inferred to the type `&'^0 u32` as it would be rather nonsensical (and likely unsound if we did not happen to ICE).
`main` doesn't know about `'a` so the borrow checker would not be able to handle a borrow with lifetime `'a`.

Unlike `EarlyBinder` we typically do not instantiate `Binder` with some concrete set of arguments from the user, i.e. `['b, 'static]` as arguments to a `for<'a1, 'a2> fn(&'a1 u32, &'a2 u32)`. Instead we usually instantiate the binder with inference variables or placeholders.

## Instantiating with inference variables

We instantiate binders with inference variables when we are trying to infer a possible instantiation of the binder, e.g. calling higher ranked function pointers or attempting to use a higher ranked where-clause to prove some bound. For example, given the `higher_ranked_fn_ptr` from the example above, if we were to call it with `&10_u32` we would:
- Instantiate the binder with infer vars yielding a signature of `fn(&'?0 u32) -> &'?0 u32)`
- Equate the type of the provided argument `&10_u32` (&'static u32) with the type in the signature, `&'?0 u32`, inferring `'?0 = 'static`
- The provided arguments were correct as we were successfully able to unify the types of the provided arguments with the types of the arguments in fn ptr signature

As another example of instantiating with infer vars, given some `for<'a> T: Trait<'a>` where-clause, if we were attempting to prove that `T: Trait<'static>` holds we would:
- Instantiate the binder with infer vars yielding a where clause of `T: Trait<'?0>`
- Equate the goal of `T: Trait<'static>` with the instantiated where clause, inferring `'?0 = 'static`
- The goal holds because we were successfully able to unify `T: Trait<'static>` with `T: Trait<'?0>`

Instantiating binders with inference variables can be accomplished by using the [`instantiate_binder_with_fresh_vars`] method on [`InferCtxt`].
Binders should be instantiated with infer vars when we only care about one specific instantiation of the binder, if instead we wish to reason about all possible instantiations of the binder then placeholders should be used instead.

## Instantiating with placeholders

Placeholders are very similar to `Ty/ConstKind::Param`/`ReEarlyParam`, they represent some unknown type that is only equal to itself.
`Ty`/`Const` and `Region` all have a [`Placeholder`] variant that is comprised of a [`Universe`] and a [`BoundVar`].

The `Universe` tracks which binder the placeholder originated from, and the `BoundVar` tracks which parameter on said binder that this placeholder corresponds to.
Equality of placeholders is determined solely by whether the universes are equal and the `BoundVar`s are equal.
See the [chapter on Placeholders and Universes][ch_placeholders_universes] for more information.

When talking with other rustc devs or seeing `Debug` formatted `Ty`/`Const`/`Region`s, `Placeholder` will often be written as `'!UNIVERSE_BOUNDVARS`.
For example, given some type `for<'a> fn(&'a u32, for<'b> fn(&'b &'a u32))`,
after instantiating both binders (assuming the `Universe` in the current `InferCtxt` was `U0` beforehand),
the type of `&'b &'a u32` would be represented as `&'!2_0 &!1_0 u32`.

When the universe of the placeholder is `0`, it will be entirely omitted from the debug output, i.e. `!0_2` would be printed as `!2`.
This rarely happens in practice though as we increase the universe in the `InferCtxt` when instantiating a binder with placeholders,
so usually the lowest universe placeholders encounterable are ones in `U1`.

`Binder`s can be instantiated with placeholders via the [`enter_forall`] method on `InferCtxt`.
It should be used whenever the compiler should care about any possible instantiation of the binder instead of one concrete instantiation.

Note: in the original example of this chapter it was mentioned that we should not infer a local variable to have type `&'^0 u32`.
This code is prevented from compiling via universes (as explained in the linked chapter)

### Why have both `RePlaceholder` and `ReBound`?

You may be wondering why we have both of these variants, afterall the data stored in `Placeholder` is effectively equivalent to that of `ReBound`: something to track which binder, and an index to track which parameter the `Binder` introduced.

The main reason for this is that `Bound` is a more syntactic representation of bound variables whereas `Placeholder` is a more semantic representation.
As a concrete example:
```rust
impl<'a> Other<'a> for &'a u32 { }

impl<T> Trait for T
where
    for<'a> T: Other<'a>,
{ ... }

impl<T> Bar for T
where
    for<'a> &'a T: Trait
{ ... }
```

Given these trait implementations, `u32: Bar` should _not_ hold.
`&'a u32` only implements `Other<'a>` when the lifetime of the borrow and the lifetime on the trait are equal.
However, if we only used `ReBound` and did not have placeholders, it may be easy to accidentally believe that trait bound does hold.
To explain this, let's walk through an example of trying to prove `u32: Bar` in a world where rustc did not have placeholders:
- We start by trying to prove `u32: Bar`
- We find the `impl<T> Bar for T` impl, we would wind up instantiating the `EarlyBinder` with `u32` (note: this is not _quite_ accurate as we first instantiate the binder with an inference variable that we then infer to be `u32` but that distinction is not super important here)
- There is a where clause `for<'a> &'^0 T: Trait` on the impl, as we instantiated the early binder with `u32` we actually have to prove `for<'a> &'^0 u32: Trait`
- We find the `impl<T> Trait for T` impl, we would wind up instantiating the `EarlyBinder` with `&'^0 u32`
- There is a where clause `for<'a> T: Other<'^0>`, as we instantiated the early binder with `&'^0 u32` we actually have to prove `for<'a> &'^0 u32: Other<'^0>`
- We find the `impl<'a> Other<'a> for &'a u32` and this impl is enough to prove the bound as the lifetime on the borrow and on the trait are both `'^0`

This end result is incorrect as we had two separate binders introducing their own generic parameters, the trait bound should have ended up as something like `for<'a1, 'a2> &'^1 u32: Other<'^0>` which is _not_ satisfied by the `impl<'a> Other<'a> for &'a u32`.

While in theory we could make this work it would be quite involved and more complex than the current setup, we would have to:
- "rewrite" bound variables to have a higher `DebruijnIndex` whenever instantiating a `Binder`/`EarlyBinder` with a `Bound` ty/const/region
- When inferring an inference variable to a bound var, if that bound var is from a binder entered after creating the infer var, we would have to lower the `DebruijnIndex` of the var.
- Separately track what binder an inference variable was created inside of, also what the innermost binder it can name parameters from (currently we only have to track the latter)
- When resolving inference variables rewrite any bound variables according to the current binder depth of the infcx
- Maybe more (while writing this list items kept getting added so it seems naive to think this is exhaustive)

Fundamentally, all of this complexity is because `Bound` ty/const/regions have a different representation for a given parameter on a `Binder` depending on how many other `Binder`s there are between the binder introducing the parameter, and its usage.
For example, given the following code:
```rust
fn foo<T>()
where
    for<'a> T: Trait<'a, for<'b> fn(&'b T, &'a u32)>
{ ... }
```
That where clause would be written as `for<'a> T: Trait<'^0, for<'b> fn(&'^0 T, &'^1_0 u32)>`.
Despite there being two references to the `'a` parameter,
they are both represented differently, `^0` and `^1_0`,
due to the fact that the latter usage is nested under a second `Binder` for the inner function pointer type.

This is in contrast to `Placeholder` ty/const/regions which do not have this limitation due to the fact that `Universe`s are specific to the current `InferCtxt` not the usage site of the parameter.

It is trivially possible to instantiate `EarlyBinder`s and unify inference variables with existing `Placeholder`s as no matter what context the `Placeholder` is in, it will have the same representation.
As an example, if we were to instantiate the binder on the higher ranked where clause from above, it would be represented like
`T: Trait<'!1_0, for<'b> fn(&'^0 T, &'!1_0 u32)>`.
The `RePlaceholder` representation for both usages of `'a` are the same despite one being underneath another `Binder`.

If we were to then instantiate the binder on the function pointer we would get a type such as:
`fn(&'!2_0 T, ^'!1_0 u32)`
the `RePlaceholder` for the `'b` parameter is in a higher universe to track the fact that its binder was instantiated after the binder for `'a`.

## Instantiating with `ReLateParam`

As discussed in [the chapter about representing types][representing-types], `RegionKind` has two variants for representing generic parameters, `ReLateParam` and `ReEarlyParam`.
`ReLateParam` is conceptually a `Placeholder` that is always in the root universe (`U0`).
It is used when instantiating late bound parameters of functions/closures while inside of them.
Its actual representation is relatively different from both `ReEarlyParam` and `RePlaceholder`:
- A `DefId` for the item that introduced the late bound generic parameter
- A [`BoundRegionKind`] which either specifies the `DefId` of the generic parameter and its name (via a `Symbol`), or that this placeholder is representing the anonymous lifetime of a `Fn`/`FnMut` closure's self borrow.
  There is also a variant for `BrAnon` but this is not used for `ReLateParam`.

For example, given the following code:
```rust,ignore
impl Trait for Whatever {
    fn foo<'a>(a: &'a u32) -> &'a u32 {
        let b: &'a u32 = a;
        b
    }
}
```
the lifetime `'a` in the type `&'a u32` in the function body would be represented as:
```
ReLateParam(
    {impl#0}::foo,
    BoundRegionKind::BrNamed({impl#0}::foo::'a, "'a")
)
```

In this specific case of referencing late bound generic parameters of a function from inside the body,
this is done implicitly during `hir_ty_lowering`,
rather than explicitly when instantiating a `Binder` somewhere.
In some cases however, we do explicitly instantiate a `Binder` with `ReLateParam`s.

Generally, whenever we have a `Binder` for late bound parameters on a function/closure,
and we are conceptually inside of the binder already,
we use [`liberate_late_bound_regions`] to instantiate it with `ReLateParam`s.
That makes this operation the `Binder` equivalent to `EarlyBinder`'s `instantiate_identity`.

As a concrete example, accessing the signature of a function we are type checking will be represented as `EarlyBinder<Binder<FnSig>>`.
As we are already "inside" of these binders, we would call `instantiate_identity` followed by `liberate_late_bound_regions`.

[`liberate_late_bound_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.liberate_late_bound_regions
[representing-types]: param-ty-const-regions.md
[`BoundRegionKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.BoundRegionKind.html
[`enter_forall`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/struct.InferCtxt.html#method.enter_forall
[ch_placeholders_universes]: ../borrow-check/region-inference/placeholders-and-universes.md
[`instantiate_binder_with_fresh_vars`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/struct.InferCtxt.html#method.instantiate_binder_with_fresh_vars
[`InferCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/struct.InferCtxt.html
[`EarlyBinder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.EarlyBinder.html
[`Binder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.Binder.html
[`Placeholder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Placeholder.html
[`Universe`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.UniverseIndex.html
[`BoundVar`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.BoundVar.html


---


# Early vs Late bound parameters

> **NOTE**: This chapter largely talks about early/late bound as being solely relevant when discussing function item types/function definitions. This is potentially not completely true, async blocks and closures should likely be discussed somewhat in this chapter.

See also these blog posts from when the distinction between early and late bound parameters was
introduced: [Intermingled parameter lists] and [Intermingled parameter lists, take 2].

[Intermingled parameter lists]: https://smallcultfollowing.com/babysteps/blog/2013/10/29/intermingled-parameter-lists/
[Intermingled parameter lists, take 2]: https://smallcultfollowing.com/babysteps/blog/2013/11/04/intermingled-parameter-lists/

## What does it mean to be "early" bound or "late" bound

Every function definition has a corresponding ZST that implements the `Fn*` traits known as a [function item type][function_item_type].
This part of the chapter will talk a little bit about the "desugaring" of function item types as it is useful context for explaining the difference between early bound and late bound generic parameters.

Let's start with a very trivial example involving no generic parameters:

```rust
fn foo(a: String) -> u8 {
    # 1
    /* snip */
}
```

If we explicitly wrote out the definitions for the function item type corresponding to `foo` and its associated `Fn` impl it would look something like this:
```rust,ignore
struct FooFnItem;

impl Fn<(String,)> for FooFnItem {
    type Output = u8;
    /* fn call(&self, ...) -> ... { ... } */
}
```

The builtin impls for the `FnMut`/`FnOnce` traits as well as the impls for `Copy` and `Clone` were omitted for brevity reasons (although these traits *are* implemented for function item types).

A slightly more complicated example would involve introducing generic parameters to the function:
```rust
fn foo<T: Sized>(a: T) -> T {
    # a
    /* snip */
}
```
Writing out the definitions would look something like this:
```rust,ignore
struct FooFnItem<T: Sized>(PhantomData<fn(T) -> T>);

impl<T: Sized> Fn<(T,)> for FooFnItem<T> {
    type Output = T;
    /* fn call(&self, ...) -> ... { ... } */
}
```

Note that the function item type `FooFnItem` is generic over some type parameter `T` as defined on the function `foo`.
However, not all generic parameters defined on functions are also defined on the function item type as demonstrated here:
```rust
fn foo<'a, T: Sized>(a: &'a T) -> &'a T {
    # a
    /* snip */
}
```
With its "desugared" form looking like so:
```rust,ignore
struct FooFnItem<T: Sized>(PhantomData<for<'a> fn(&'a T) -> &'a T>);

impl<'a, T: Sized> Fn<(&'a T,)> for FooFnItem<T> {
    type Output = &'a T;
    /* fn call(&self, ...) -> ... { ... } */
}
```

The lifetime parameter `'a` from the function `foo` is not present on the function item type `FooFnItem` and is instead introduced on the builtin impl solely for use in representing the argument types.

Generic parameters not all being defined on the function item type means that there are two steps where generic arguments are provided when calling a function.
1. Naming the function (e.g. `let a = foo;`) the arguments for `FooFnItem` are provided.
2. Calling the function (e.g. `a(&10);`) any parameters defined on the builtin impl are provided.

This two-step system is where the early vs late naming scheme comes from, early bound parameters are provided in the *earliest* step (naming the function), whereas late bound parameters are provided in the *latest* step (calling the function).

Looking at the desugaring from the previous example we can tell that `T` is an early bound type parameter and `'a` is a late bound lifetime parameter as `T` is present on the function item type but `'a` is not.
See this example of calling `foo` annotated with where each generic parameter has an argument provided:
```rust
fn foo<'a, T: Sized>(a: &'a T) -> &'a T {
    # a
    /* snip */
}

// Here we provide a type argument `String` to the
// type parameter `T` on the function item type
let my_func = foo::<String>;

// Here (implicitly) a lifetime argument is provided
// to the lifetime parameter `'a` on the builtin impl.
my_func(&String::new());
```

[function_item_type]: https://doc.rust-lang.org/reference/types/function-item.html

## Differences between early and late bound parameters

### Higher ranked function pointers and trait bounds

A generic parameter being late bound allows for more flexible usage of the function item.
For example, if we have some function `foo` with an early bound lifetime parameter and some function `bar` with a late bound lifetime parameter `'a`, we would have the following builtin `Fn` impls:
```rust,ignore
impl<'a> Fn<(&'a String,)> for FooFnItem<'a> { /* ... */ }
impl<'a> Fn<(&'a String,)> for BarFnItem { /* ... */ }
```

The `bar` function has a strictly more flexible signature as the function item type can be called with a borrow with *any* lifetime, whereas the `foo` function item type would only be callable with a borrow with the same lifetime on the function item type.
We can show this by simply trying to call `foo`'s function item type multiple times with different lifetimes:

```rust
// The `'a: 'a` bound forces this lifetime to be early bound.
fn foo<'a: 'a>(b: &'a String) -> &'a String { b }
fn bar<'a>(b: &'a String) -> &'a String { b }

// Early bound generic parameters are instantiated here when naming
// the function `foo`. As `'a` is early bound an argument is provided.
let f = foo::<'_>;

// Both function arguments are required to have the same lifetime as
// the lifetime parameter being early bound means that `f` is only
// callable for one specific lifetime.
//
// As we call this with borrows of different lifetimes, the borrow checker
// will error here.
f(&String::new());
f(&String::new());
```

The lifetime parameter on `foo` being early bound requires all callers of `f` to provide a borrow with the same lifetime.
In this example, we call `foo`'s function item type twice, each time with a borrow of a temporary.
These two borrows could not possibly have lifetimes that overlap as the temporaries are only alive during the function call, not after, so we get a compilation error.

If the lifetime parameter on `foo` was late bound, this would be able to compile as each caller could provide a different lifetime argument for its borrow.
See the following example, which demonstrates this using the `bar` function defined above:

```rust
# fn foo<'a: 'a>(b: &'a String) -> &'a String { b }
# fn bar<'a>(b: &'a String) -> &'a String { b }
#
// Early bound parameters are instantiated here, however as `'a` is
// late bound it is not provided here.
let b = bar;

// Late bound parameters are instantiated separately at each call site
// allowing different lifetimes to be used by each caller.
b(&String::new());
b(&String::new());
```

This is reflected in the ability to coerce function item types to higher ranked function pointers and prove higher ranked `Fn` trait bounds.
We can demonstrate this with the following example:
```rust
// The `'a: 'a` bound forces this lifetime to be early bound.
fn foo<'a: 'a>(b: &'a String) -> &'a String { b }
fn bar<'a>(b: &'a String) -> &'a String { b }

fn accepts_hr_fn(_: impl for<'a> Fn(&'a String) -> &'a String) {}

fn higher_ranked_trait_bound() {
    let bar_fn_item = bar;
    accepts_hr_fn(bar_fn_item);

    let foo_fn_item = foo::<'_>;
    // errors
    accepts_hr_fn(foo_fn_item);
}

fn higher_ranked_fn_ptr() {
    let bar_fn_item = bar;
    let fn_ptr: for<'a> fn(&'a String) -> &'a String = bar_fn_item;

    let foo_fn_item = foo::<'_>;
    // errors
    let fn_ptr: for<'a> fn(&'a String) -> &'a String = foo_fn_item;
}
```

In both of these cases, the borrow checker errors as it does not consider `foo_fn_item` to be callable with a borrow of any lifetime.
This is due to the fact that the lifetime parameter on `foo` is early bound, causing `foo_fn_item` to have a type of `FooFnItem<'_>` which (as demonstrated by the desugared `Fn` impl) is only callable with a borrow of the same lifetime `'_`.

### Turbofishing in the presence of late bound parameters

As mentioned previously, the distinction between early and late bound parameters means that there are two places where generic parameters are instantiated:
- When naming a function (early)
- When calling a function (late)

There is currently no syntax for explicitly specifying generic arguments for late bound parameters during the call step; generic arguments can only be specified for early bound parameters when naming a function.
The syntax `foo::<'static>();`, despite being part of a function call, behaves as `(foo::<'static>)();` and instantiates the early bound generic parameters on the function item type.

See the following example:
```rust
fn foo<'a>(b: &'a u32) -> &'a u32 { b }

let f /* : FooFnItem<????> */ = foo::<'static>;
```

The above example errors as the lifetime parameter `'a` is late bound and so cannot be instantiated as part of the "naming a function" step.
If we make the lifetime parameter early bound we will see this code start to compile:
```rust
fn foo<'a: 'a>(b: &'a u32) -> &'a u32 { b }

let f /* : FooFnItem<'static> */ = foo::<'static>;
```

What the current implementation of the compiler aims to do is error when specifying lifetime arguments to a function that has both early *and* late bound lifetime parameters.
In practice, due to excessive breakage, some cases are actually only future compatibility warnings ([#42868](https://github.com/rust-lang/rust/issues/42868)):
- When the amount of lifetime arguments is the same as the number of early bound lifetime parameters, a FCW is emitted instead of an error
- An error is always downgraded to a FCW when using method call syntax

To demonstrate this we can write out the different kinds of functions and give them both a late and early bound lifetime:
```rust,ignore
fn free_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}

struct Foo;

trait Trait: Sized {
    fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ());
    fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ());
}

impl Trait for Foo {
    fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
    fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
}

impl Foo {
    fn inherent_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
    fn inherent_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
}
```

Then, for the first case, we can call each function with a single lifetime argument (corresponding to the one early bound lifetime parameter) and note that it only results in a FCW rather than a hard error.
```rust
#![deny(late_bound_lifetime_arguments)]

# fn free_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
#
# struct Foo;
#
# trait Trait: Sized {
#     fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ());
#     fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ());
# }
#
# impl Trait for Foo {
#     fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
#     fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
# }
#
# impl Foo {
#     fn inherent_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
#     fn inherent_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
# }
#
// Specifying as many arguments as there are early
// bound parameters is always a future compat warning
Foo.trait_method::<'static>(&(), &());
Foo::trait_method::<'static>(Foo, &(), &());
Foo::trait_function::<'static>(&(), &());
Foo.inherent_method::<'static>(&(), &());
Foo::inherent_function::<'static>(&(), &());
free_function::<'static>(&(), &());
```

For the second case we call each function with more lifetime arguments than there are lifetime parameters (be it early or late bound) and note that method calls result in a FCW as opposed to the free/associated functions which result in a hard error:
```rust
# fn free_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
#
# struct Foo;
#
# trait Trait: Sized {
#     fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ());
#     fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ());
# }
#
# impl Trait for Foo {
#     fn trait_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
#     fn trait_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
# }
#
# impl Foo {
#     fn inherent_method<'a: 'a, 'b>(self, _: &'a (), _: &'b ()) {}
#     fn inherent_function<'a: 'a, 'b>(_: &'a (), _: &'b ()) {}
# }
#
// Specifying more arguments than there are early
// bound parameters is a future compat warning when
// using method call syntax.
Foo.trait_method::<'static, 'static, 'static>(&(), &());
Foo.inherent_method::<'static, 'static, 'static>(&(), &());
// However, it is a hard error when not using method call syntax.
Foo::trait_method::<'static, 'static, 'static>(Foo, &(), &());
Foo::trait_function::<'static, 'static, 'static>(&(), &());
Foo::inherent_function::<'static, 'static, 'static>(&(), &());
free_function::<'static, 'static, 'static>(&(), &());
```

Even when specifying enough lifetime arguments for both the late and early bound lifetime parameter, these arguments are not actually used to annotate the lifetime provided to late bound parameters.
We can demonstrate this by turbofishing `'static` to a function while providing a non-static borrow:
```rust
struct Foo;

impl Foo {
    fn inherent_method<'a: 'a, 'b>(self, _: &'a (), _: &'b String ) {}
}

Foo.inherent_method::<'static, 'static>(&(), &String::new());
```

This compiles even though the `&String::new()` function argument does not have a `'static` lifetime, this is because "extra" lifetime arguments are discarded rather than taken into account for late bound parameters when actually calling the function.

### Liveness of types with late bound parameters

When checking type outlives bounds involving function item types we take into account early bound parameters.
For example:

```rust
fn foo<T>(_: T) {}

fn requires_static<T: 'static>(_: T) {}

fn bar<T>() {
    let f /* : FooFnItem<T> */ = foo::<T>;
    requires_static(f);
}
```

As the type parameter `T` is early bound, the desugaring of the function item type for `foo` would look something like `struct FooFnItem<T>`.
Then, in order for `FooFnItem<T>: 'static` to hold, we must also require `T: 'static` to hold as otherwise we would wind up with soundness bugs.

Unfortunately, due to bugs in the compiler, we do not take into account early bound *lifetimes*, which is the cause of the open soundness bug [#84366](https://github.com/rust-lang/rust/issues/84366).
This means that it's impossible to demonstrate a "difference" between early/late bound parameters for liveness/type outlives bounds as the only kind of generic parameters that are able to be late bound are lifetimes which are handled incorrectly.

Regardless, in theory the code example below *should* demonstrate such a difference once [#84366](https://github.com/rust-lang/rust/issues/84366) is fixed:
```rust
fn early_bound<'a: 'a>(_: &'a String) {}
fn late_bound<'a>(_: &'a String) {}

fn requires_static<T: 'static>(_: T) {}

fn bar<'b>() {
    let e = early_bound::<'b>;
    // this *should* error but does not
    requires_static(e);

    let l = late_bound;
    // this correctly does not error
    requires_static(l);
}
```

## Requirements for a parameter to be late bound

### Must be a lifetime parameter

Type and Const parameters are not able to be late bound as we do not have a way to support types such as `dyn for<T> Fn(Box<T>)` or `for<T> fn(Box<T>)`.
Calling such types requires being able to monomorphize the underlying function which is not possible with indirection through dynamic dispatch.

### Must not be used in a where clause

Currently when a generic parameter is used in a where clause it must be early bound.
For example:
```rust
# trait Trait<'a> {}
fn foo<'a, T: Trait<'a>>(_: &'a String, _: T) {}
```

In this example the lifetime parameter `'a` is considered to be early bound as it appears in the where clause `T: Trait<'a>`.
This is true even for "trivial" where clauses such as `'a: 'a` or those implied by wellformedness of function arguments, for example:
```rust
fn foo<'a: 'a>(_: &'a String) {}
fn bar<'a, T: 'a>(_: &'a T) {}
```

In both of these functions the lifetime parameter `'a` would be considered to be early bound even though the where clauses they are used in arguably do not actually impose any constraints on the caller.

The reason for this restriction is a combination of two things:
- We cannot prove bounds on late bound parameters until they have been instantiated
- Function pointers and trait objects do not have a way to represent yet to be proven where clauses from the underlying function

Take the following example:
```rust
trait Trait<'a> {}
fn foo<'a, T: Trait<'a>>(_: &'a T) {}

let f = foo::<String>;
let f = f as for<'a> fn(&'a String);
f(&String::new());
```

At *some point* during type checking an error should be emitted for this code as `String` does not implement `Trait` for any lifetime.

If the lifetime `'a` were late bound then this becomes difficult to check.
When naming `foo` we do not know what lifetime should be used as part of the `T: Trait<'a>` trait bound as it has not yet been instantiated.
When coercing the function item type to a function pointer we have no way of tracking the `String: Trait<'a>` trait bound that must be proven when calling the function.

If the lifetime `'a` is early bound (which it is in the current implementation in rustc), then the trait bound can be checked when naming the function `foo`.
Requiring parameters used in where clauses to be early bound gives a natural place to check where clauses defined on the function.

Finally, we do not require lifetimes to be early bound if they are used in *implied bounds*, for example:
```rust
fn foo<'a, T>(_: &'a T) {}

let f = foo;
f(&String::new());
f(&String::new());
```

This code compiles, demonstrating that the lifetime parameter is late bound, even though `'a` is used in the type `&'a T` which implicitly requires `T: 'a` to hold.
Implied bounds can be treated specially as any types introducing implied bounds are in the signature of the function pointer type, which means that when calling the function we know to prove `T: 'a`.

### Must be constrained by argument types

It is important that builtin impls on function item types do not wind up with unconstrained generic parameters as this can lead to unsoundness.
This is the same kind of restriction as applies to user written impls, for example the following code results in an error:
```rust
trait Trait {
    type Assoc;
}

impl<'a> Trait for u8 {
    type Assoc = &'a String;
}
```

The analogous example for builtin impls on function items would be the following:
```rust,ignore
fn foo<'a>() -> &'a String { /* ... */ }
```
If the lifetime parameter `'a` were to be late bound we would wind up with a builtin impl with an unconstrained lifetime, we can manually write out the desugaring for the function item type and its impls with `'a` being late bound to demonstrate this:
```rust,ignore
// NOTE: this is just for demonstration, in practice `'a` is early bound
struct FooFnItem;

impl<'a> Fn<()> for FooFnItem {
    type Output = &'a String;
    /* fn call(...) -> ... { ... } */
}
```

In order to avoid such a situation we consider `'a` to be early bound which causes the lifetime on the impl to be constrained by the self type:
```rust,ignore
struct FooFnItem<'a>(PhantomData<fn() -> &'a String>);

impl<'a> Fn<()> for FooFnItem<'a> {
    type Output = &'a String;
    /* fn call(...) -> ... { ... } */
}
```


---

# The `ty` module: representing types

The `ty` module defines how the Rust compiler represents types internally.
It also defines the
*typing context* (`tcx` or `TyCtxt`), which is the central data structure in the compiler.

## `ty::Ty`

When we talk about how rustc represents types, we usually refer to a type called `Ty`.
There are quite a few modules and types for `Ty` in the compiler ([Ty documentation][ty]).

[ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/index.html

The specific `Ty` we are referring to is [`rustc_middle::ty::Ty`][ty_ty] (and not
[`rustc_hir::Ty`][hir_ty]).
The distinction is important, so we will discuss it first before going into the details of `ty::Ty`.

[ty_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[hir_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Ty.html

## `rustc_hir::Ty` vs `ty::Ty`

The HIR in rustc can be thought of as the high-level intermediate representation.
It is more or less the AST (see [this chapter](hir.md)) as it represents the
syntax that the user wrote, and is obtained after parsing and some *desugaring*. It has a
representation of types, but in reality it reflects more of what the user wrote, that is, what they
wrote so as to represent that type.

In contrast, `ty::Ty` represents the semantics of a type, that is, the *meaning* of what the user
wrote.
For example, `rustc_hir::Ty` would record the fact that a user used the name `u32` twice
in their program, but the `ty::Ty` would record the fact that both usages refer to the same type.

**Example: `fn foo(x: u32) → u32 { x }`**

In this function, we see that `u32` appears twice.
We know that that is the same type,
i.e. the function takes an argument and returns an argument of the same type,
but from the point of view of the HIR,
there would be two distinct type instances because these
are occurring in two different places in the program.
That is, they have two different [`Span`s][span] (locations).

[span]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html

**Example: `fn foo(x: &u32) -> &u32`**

In addition, HIR might have information left out.
This type
`&u32` is incomplete, since in the full Rust type there is actually a lifetime, but we didn’t need
to write those lifetimes.
There are also some elision rules that insert information.
The result may look like `fn foo<'a>(x: &'a u32) -> &'a u32`.

In the HIR level, these things are not spelled out and you can say the picture is rather incomplete.
However, at the `ty::Ty` level, these details are added and it is complete.
Moreover, we will have
exactly one `ty::Ty` for a given type, like `u32`, and that `ty::Ty` is used for all `u32`s in the
whole program, not a specific usage, unlike `rustc_hir::Ty`.

Here is a summary:

| [`rustc_hir::Ty`][hir_ty] | [`ty::Ty`][ty_ty] |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Describe the *syntax* of a type: what the user wrote (with some desugaring).  | Describe the *semantics* of a type: the meaning of what the user wrote. |
| Each `rustc_hir::Ty` has its own spans corresponding to the appropriate place in the program. | Doesn’t correspond to a single place in the user’s program. |
| `rustc_hir::Ty` has generics and lifetimes; however, some of those lifetimes are special markers like [`LifetimeKind::Implicit`][implicit]. | `ty::Ty` has the full type, including generics and lifetimes, even if the user left them out |
| `fn foo(x: u32) -> u32 { }` - Two `rustc_hir::Ty` representing each usage of `u32`, each has its own `Span`s, and `rustc_hir::Ty` doesn’t tell us that both are the same type | `fn foo(x: u32) -> u32 { }` - One `ty::Ty` for all instances of `u32` throughout the program, and `ty::Ty` tells us that both usages of `u32` mean the same type. |
| `fn foo(x: &u32) -> &u32 { }` - Two `rustc_hir::Ty` again. Lifetimes for the references show up in the `rustc_hir::Ty`s using a special marker, [`LifetimeKind::Implicit`][implicit]. | `fn foo(x: &u32) -> &u32 { }`- A single `ty::Ty`. The `ty::Ty` has the hidden lifetime param. |

[implicit]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/enum.LifetimeKind.html#variant.Implicit

**Order**

HIR is built directly from the AST, so it happens before any `ty::Ty` is produced.
After HIR is built, some basic type inference and type checking is done.
During the type inference, we
figure out what the `ty::Ty` of everything is and we also check if the type of something is
ambiguous.
The `ty::Ty` is then used for type checking while making sure everything has the expected type.
The [`hir_ty_lowering` module][hir_ty_lowering] is where the code responsible for
lowering a `rustc_hir::Ty` to a `ty::Ty` is located.
The main routine used is `lower_ty`.
This occurs during the type-checking phase, but also in other parts of the compiler that want to ask
questions like "what argument types does this function expect?"

[hir_ty_lowering]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/hir_ty_lowering/index.html

**How semantics drive the two instances of `Ty`**

You can think of HIR as the perspective of the type information that assumes the least.
We assume two things are distinct until they are proven to be the same thing.
In other words, we know less about them, so we should assume less about them.

They are syntactically two strings: `"u32"` at line N column 20 and `"u32"` at line N column 35. We
don’t know that they are the same yet.
So, in the HIR we treat them as if they are different.
Later,
we determine that they semantically are the same type and that’s the `ty::Ty` we use.

Consider another example: `fn foo<T>(x: T) -> u32`.
Suppose that someone invokes `foo::<u32>(0)`.
This means that `T` and `u32` (in this invocation) actually turns out to be the same type, so we
would eventually end up with the same `ty::Ty` in the end, but we have distinct `rustc_hir::Ty`.
(This is a bit over-simplified, though, since during type checking, we would check the function
generically and would still have a `T` distinct from `u32`.
Later, when doing code generation,
we would always be handling "monomorphized" (fully substituted) versions of each function,
and hence we would know what `T` represents (and specifically that it is `u32`).)

Here is one more example:

```rust
mod a {
    type X = u32;
    pub fn foo(x: X) -> u32 { 22 }
}
mod b {
    type X = i32;
    pub fn foo(x: X) -> i32 { x }
}
```

Here the type `X` will vary depending on context, clearly.
If you look at the `rustc_hir::Ty`,
you will get back that `X` is an alias in both cases (though it will be mapped via name resolution
to distinct aliases).
But if you look at the `ty::Ty` signature, it will be either `fn(u32) -> u32`
or `fn(i32) -> i32` (with type aliases fully expanded).

## `ty::Ty` implementation

[`rustc_middle::ty::Ty`][ty_ty] is actually a wrapper around
[`Interned<WithCachedTypeInfo<TyKind>>`][tykind].
You can ignore `Interned` in general; you will basically never access it explicitly.
We always hide them within `Ty` and skip over it via `Deref` impls or methods.
`TyKind` is a big enum with variants to represent many different Rust types
(e.g. primitives, references, algebraic data types, generics, lifetimes, etc).
`WithCachedTypeInfo` has a few cached values like `flags` and `outer_exclusive_binder`.
They
are convenient hacks for efficiency and summarize information about the type that we may want to
know, but they don’t come into the picture as much here.
Finally, [`Interned`](./memory.md) allows the `ty::Ty` to be a thin pointer-like
type.
This allows us to do cheap comparisons for equality, along with the other benefits of interning.

[tykind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html

## Allocating and working with types

To allocate a new type, you can use the various `new_*` methods defined on
[`Ty`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html).
These have names that correspond mostly to the various kinds of types.
For example:

```rust,ignore
let array_ty = Ty::new_array_with_const_len(tcx, ty, count);
```

These methods all return a `Ty<'tcx>` – note that the lifetime you get back is the lifetime of the
arena that this `tcx` has access to.
Types are always canonicalized and interned (so we never allocate exactly the same type twice).

You can also find various common types in the `tcx` itself by accessing its fields:
`tcx.types.bool`, `tcx.types.char`, etc. (See [`CommonTypes`] for more.)

[`CommonTypes`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.CommonTypes.html

<!-- N.B: This section is linked from the type comparison internal lint. -->
## Comparing types

Because types are interned, it is possible to compare them for equality efficiently using `==`
– however, this is almost never what you want to do unless you happen to be hashing and looking
for duplicates.
This is because often in Rust there are multiple ways to represent the same type,
particularly once inference is involved.

For example, the type `{integer}` (`ty::Infer(ty::IntVar(..))` an integer inference variable,
the type of an integer literal like `0`) and `u8` (`ty::UInt(..)`) should often be treated as
equal when testing whether they can be assigned to each other (which is a common operation in
diagnostics code).
`==` on them will return `false` though, since they are different types.

The simplest way to compare two types correctly requires an inference context (`infcx`).
If you have one, you can use `infcx.can_eq(param_env, ty1, ty2)`
to check whether the types can be made equal.
This is typically what you want to check during diagnostics, which is concerned with questions such
as whether two types can be assigned to each other, not whether they're represented identically in
the compiler's type-checking layer.

When working with an inference context, you have to be careful to ensure that potential inference
variables inside the types actually belong to that inference context.
If you are in a function that has access to an inference context already, this should be the case.
Specifically, this is the case during HIR type checking or MIR borrow checking.

Another consideration is normalization.
Two types may actually be the same, but one is behind an associated type.
To compare them correctly, you have to normalize the types first.
This is primarily a concern during HIR type checking and with all types from a `TyCtxt` query
(for example from `tcx.type_of()`).

When a `FnCtxt` or an `ObligationCtxt` is available during type checking, `.normalize(ty)`
should be used on them to normalize the type.
After type checking, diagnostics code can use `tcx.normalize_erasing_regions(ty)`.

There are also cases where using `==` on `Ty` is fine.
This is, for example, the case in late lints
or after monomorphization, since type checking has been completed, meaning all inference variables
are resolved and all regions have been erased.
In these cases, if you know that inference variables
or normalization won't be a concern, `#[allow]` or `#[expect]`ing the lint is recommended.

When diagnostics code does not have access to an inference context, it should be threaded through
the function calls if one is available in some place (like during type checking).

If no inference context is available at all, then one can be created as described in
[type-inference].
But this is only useful when the involved types (for example, if
they came from a query like `tcx.type_of()`) are actually substituted with fresh
inference variables using [`fresh_args_for_item`].
This can be used to answer questions like "can `Vec<T>` for any `T` be unified with `Vec<u32>`?".

[type-inference]: ./type-inference.md#creating-an-inference-context
[`fresh_args_for_item`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_infer/infer/struct.InferCtxt.html#method.fresh_substs_for_item

## `ty::TyKind` Variants

Note: `TyKind` is **NOT** the functional programming concept of *Kind*.

Whenever working with a `Ty` in the compiler, it is common to match on the kind of type:

```rust,ignore
fn foo(x: Ty<'tcx>) {
  match x.kind {
    ...
  }
}
```

The `kind` field is of type `TyKind<'tcx>`, which is an enum defining all of the different kinds of
types in the compiler.

> N.B. inspecting the `kind` field on types during type inference can be risky, as there may be
> inference variables and other things to consider, or sometimes types are not yet known and will
> become known later.

There are a lot of related types, and we’ll cover them in time (e.g regions/lifetimes,
“substitutions”, etc).

There are many variants on the `TyKind` enum, which you can see by looking at its
[documentation][tykind].
Here is a sampling:

- [**Algebraic Data Types (ADTs)**][kindadt] An [*algebraic data type*][wikiadt] is a  `struct`,
  `enum` or `union`.
  Under the hood, `struct`, `enum` and `union` are actually implemented
  the same way: they are all [`ty::TyKind::Adt`][kindadt].
  It’s basically a user defined type.
  We will talk more about these later.
- [**Foreign**][kindforeign] Corresponds to `extern type T`.
- [**Str**][kindstr] Is the type str.
  When the user writes `&str`, `Str` is how we represent the `str` part of that type.
- [**Slice**][kindslice] Corresponds to `[T]`.
- [**Array**][kindarray] Corresponds to `[T; n]`.
- [**RawPtr**][kindrawptr] Corresponds to `*mut T` or `*const T`.
- [**Ref**][kindref] `Ref` stands for safe references, `&'a mut T` or `&'a T`.
  `Ref` has some
  associated parts, like `Ty<'tcx>` which is the type that the reference references.
  `Region<'tcx>` is the lifetime or region of the reference and `Mutability` if the reference
  is mutable or not.
- [**Param**][kindparam] Represents a type parameter (e.g. the `T` in `Vec<T>`).
- [**Error**][kinderr] Represents a type error somewhere so that we can print better diagnostics.
  We will discuss this more later.
- [**And many more**...][kindvars]

[wikiadt]: https://en.wikipedia.org/wiki/Algebraic_data_type
[kindadt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Adt
[kindforeign]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Foreign
[kindstr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Str
[kindslice]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Slice
[kindarray]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Array
[kindrawptr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.RawPtr
[kindref]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Ref
[kindparam]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Param
[kinderr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variant.Error
[kindvars]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/ty_kind/enum.TyKind.html#variants

## Import conventions

Although there is no hard and fast rule, the `ty` module tends to be used like so:

```rust,ignore
use ty::{self, Ty, TyCtxt};
```

In particular, since they are so common, the `Ty` and `TyCtxt` types are imported directly.
Other
types are often referenced with an explicit `ty::` prefix (e.g. `ty::TraitRef<'tcx>`). But some
modules choose to import a larger or smaller set of names explicitly.

## Type errors

There is a `TyKind::Error` that is produced when the user makes a type error.
The idea is that
we would propagate this type and suppress other errors that come up due to it so as not to overwhelm
the user with cascading compiler error messages.

There is an **important invariant** for `TyKind::Error`.
The compiler should **never** produce `Error` unless we **know** that an error has already been
reported to the user.
This is usually
because (a) you just reported it right there or (b) you are propagating an existing Error type (in
which case the error should've been reported when that error type was produced).

It's important to maintain this invariant because the whole point of the `Error` type is to suppress
other errors -- i.e., we don't report them. If we were to produce an `Error` type without actually
emitting an error to the user, then this could cause later errors to be suppressed, and the
compilation might inadvertently succeed!

Sometimes there is a third case.
You believe that an error has been reported, but you believe it
would've been reported earlier in the compilation, not locally.
In that case, you can create a "delayed bug" with [`delayed_bug`] or [`span_delayed_bug`].
This will make a note that you expect
compilation to yield an error -- if, however, compilation should succeed, then it will trigger a
compiler bug report.

[`delayed_bug`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.DiagCtxt.html#method.delayed_bug
[`span_delayed_bug`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.DiagCtxt.html#method.span_delayed_bug

For added safety, it's not actually possible to produce a `TyKind::Error` value
outside of [`rustc_middle::ty`][ty]; there is a private member of
`TyKind::Error` that prevents it from being constructable elsewhere.
Instead,
one should use the [`Ty::new_error`][terr] or [`Ty::new_error_with_message`][terrmsg] methods.
These methods either take an `ErrorGuaranteed`
or call `span_delayed_bug` before returning an interned `Ty` of kind `Error`.
If you were already planning to use [`span_delayed_bug`], then you can just pass the
span and message to [`ty_error_with_message`][terrmsg] instead to avoid a redundant delayed bug.

[terr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#method.new_error
[terrmsg]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#method.new_error_with_message


## `TyKind` variant shorthand syntax

When looking at the debug output of `Ty` or simply talking about different types in the compiler, you may encounter syntax that is not valid Rust but is used to concisely represent internal information about types.
Below is a quick reference cheat sheet to tell what the various syntax actually means:

- Generic parameters: `{name}/#{index}` e.g. `T/#0`, where `index` corresponds to its position in the list of generic parameters
- Inference variables: `?{id}` e.g. `?x`/`?0`, where `id` identifies the inference variable
- Variables from binders: `^{binder}_{index}` e.g. `^0_x`/`^0_2`, where `binder` and `index` identify which variable from which binder is being referred to
- Placeholders: `!{id}` or `!{id}_{universe}` e.g. `!x`/`!0`/`!x_2`/`!0_2`, representing some unique type in the specified universe. The universe is often elided when it is `0`

These should be covered in more depth in later chapters.


---

# ADTs and Generic Arguments

The term `ADT` stands for "Algebraic data type", in rust this refers to a struct, enum, or union.

## ADTs Representation

Let's consider the example of a type like `MyStruct<u32>`, where `MyStruct` is defined like so:

```rust,ignore
struct MyStruct<T> { x: u8, y: T }
```

The type `MyStruct<u32>` would be an instance of `TyKind::Adt`:

```rust,ignore
Adt(&'tcx AdtDef, GenericArgs<'tcx>)
//  ------------  ---------------
//  (1)            (2)
//
// (1) represents the `MyStruct` part
// (2) represents the `<u32>`, or "substitutions" / generic arguments
```

There are two parts:

- The [`AdtDef`][adtdef] references the struct/enum/union but without the values for its type
  parameters.
  In our example, this is the `MyStruct` part *without* the argument `u32`.
  (Note that in the HIR, structs, enums and unions are represented differently, but in `ty::Ty`,
  they are all represented using `TyKind::Adt`.)
- The [`GenericArgs`] is a list of values that are to be substituted
for the generic parameters.
 In our example of `MyStruct<u32>`, we would end up with a list like `[u32]`.
We’ll dig more into generics and substitutions in a little bit.

[adtdef]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.AdtDef.html
[`GenericArgs`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.GenericArgs.html

### **`AdtDef` and `DefId`**

For every type defined in the source code, there is a unique `DefId` (see [this
chapter](../hir.md#identifiers-in-the-hir)).
This includes ADTs and generics.
In the `MyStruct<T>` definition we gave above,
there are two `DefId`s: one for `MyStruct` and one for `T`.
Notice that the code above does not generate a new `DefId` for `u32`
because it is not defined in that code (it is only referenced).

`AdtDef` is more or less a wrapper around `DefId` with lots of useful helper methods.
There is essentially a one-to-one relationship between `AdtDef` and `DefId`.
You can get the `AdtDef` for a `DefId` with the [`tcx.adt_def(def_id)` query][adtdefq].
`AdtDef`s are all interned, as shown by the `'tcx` lifetime.

[adtdefq]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.adt_def

## Question: Why not substitute “inside” the `AdtDef`?

Recall that we represent a generic struct with `(AdtDef, args)`.
So why bother with this scheme?

Well, the alternate way we could have chosen to represent types would be to always create a new,
fully-substituted form of the `AdtDef` where all the types are already substituted.
This seems like less of a hassle.
However, the `(AdtDef, args)` scheme has some advantages over this.

First, `(AdtDef, args)` scheme has an efficiency win:

```rust,ignore
struct MyStruct<T> {
  ... 100s of fields ...
}

// Want to do: MyStruct<A> ==> MyStruct<B>
```

in an example like this, we can instantiate `MyStruct<A>` as `MyStruct<B>` (and so on) very cheaply,
by just replacing the one reference to `A` with `B`.
But if we eagerly instantiated all the fields,
that could be a lot more work because we might have to go through all of the fields in the `AdtDef`
and update all of their types.

A bit more deeply, this corresponds to structs in Rust being [*nominal* types][nominal] — which
means that they are defined by their *name* (and that their contents are then indexed from the
definition of that name, and not carried along “within” the type itself).

[nominal]: https://en.wikipedia.org/wiki/Nominal_type_system


## The `GenericArgs` type

Given a generic type `MyType<A, B, …>`, we have to store the list of generic arguments for `MyType`.

In rustc this is done using [`GenericArgs`].
`GenericArgs` is a thin pointer to a slice of [`GenericArg`] representing a list of generic arguments for a generic item.
For example, given a `struct HashMap<K, V>` with two type parameters, `K` and `V`, the `GenericArgs` used to represent the type `HashMap<i32, u32>` would be represented by `&'tcx [tcx.types.i32, tcx.types.u32]`.

`GenericArg` is conceptually an `enum` with three variants, one for type arguments, one for const arguments and one for lifetime arguments.
In practice that is actually represented by [`GenericArgKind`] and [`GenericArg`] is a more space efficient version that has a method to
turn it into a `GenericArgKind`.

The actual `GenericArg` struct stores the type, lifetime or const as an interned pointer with the discriminant stored in the lower 2 bits.
Unless you are working with the `GenericArgs` implementation specifically, you should generally not have to deal with `GenericArg` and instead
make use of the safe [`GenericArgKind`](#genericargkind) abstraction obtainable via the `GenericArg::unpack()` method.

In some cases you may have to construct a `GenericArg`, this can be done via `Ty/Const/Region::into()` or `GenericArgKind::pack`.

```rust,ignore
// An example of unpacking and packing a generic argument.
fn deal_with_generic_arg<'tcx>(generic_arg: GenericArg<'tcx>) -> GenericArg<'tcx> {
    // Unpack a raw `GenericArg` to deal with it safely.
    let new_generic_arg: GenericArgKind<'tcx> = match generic_arg.unpack() {
        GenericArgKind::Type(ty) => { /* ... */ }
        GenericArgKind::Lifetime(lt) => { /* ... */ }
        GenericArgKind::Const(ct) => { /* ... */ }
    };
    // Pack the `GenericArgKind` to store it in a generic args list.
    new_generic_arg.pack()
}
```

[list]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.List.html
[`GenericArg`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.GenericArg.html
[`GenericArgKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.GenericArgKind.html
[`GenericArgs`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.GenericArgs.html

So pulling it all together:

```rust,ignore
struct MyStruct<T>(T);
type Foo = MyStruct<u32>
```

For the `MyStruct<U>` written in the `Foo` type alias, we would represent it in the following way:

- There would be an `AdtDef` (and corresponding `DefId`) for `MyStruct`.
- There would be a `GenericArgs` containing the list `[GenericArgKind::Type(Ty(u32))]`
- And finally a `TyKind::Adt` with the `AdtDef` and `GenericArgs` listed above.

## Nested generic args

```rust
struct MyStruct<T>(T);

impl<T> MyStruct<T> {
    fn func<T2, T3>() {}
}

fn main() {
    MyStruct::<u32>::func::<bool, char>();
}
```

The construct `MyStruct::<u32>::func::<bool, char>` is represented by a tuple: a DefId pointing at `func`, and then a
`GenericArgs` list that "walks" all containing generic parameters - in this case, the list would be `[u32, bool, char]`.

The [`ty::Generics`] type (returned by the [`generics_of`] query) contains the information of how a nested hierarchy
gets flattened down to a list, and lets you figure out which index in the `GenericArgs` list corresponds to which
generic.
The general theme of how it works is outermost to innermost (`T` before `T2` in the example), left to right
(`T2` before `T3`), but there are several complications:

- Traits have an implicit `Self` generic parameter which is the first (i.e. 0th) generic parameter. Note that `Self` doesn't mean a generic parameter in all situations, see [Res::SelfTyAlias](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def/enum.Res.html#variant.SelfTyAlias) and [Res::SelfCtor](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def/enum.Res.html#variant.SelfCtor).
- Only early-bound generic parameters are included, [late-bound generics] are not.
- ... and more...

Check out [`ty::Generics`] for exact specifics on how the flattening works.

[`ty::Generics`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Generics.html
[`generics_of`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.generics_of
[late-bound generics]: ../early-late-parameters.md


---

# Parameter `Ty`/`Const`/`Region`s

When inside of generic items, types can be written that use in scope generic parameters, for example `fn foo<'a, T>(_: &'a Vec<T>)`.
In this specific case, the `&'a Vec<T>` type would be represented internally as:
```
TyKind::Ref(
  RegionKind::LateParam(DefId(foo), DefId(foo::'a), "'a"),
  TyKind::Adt(Vec, &[TyKind::Param("T", 0)])
)
```

There are three separate ways we represent usages of generic parameters:
- [`TyKind::Param`]/[`ConstKind::Param`]/[`RegionKind::EarlyParam`] for early bound generic parameters (note: all type and const parameters are considered early bound, see the [chapter on early vs late bound parameters][ch_early_late_bound] for more information)
- [`TyKind::Bound`]/[`ConstKind::Bound`]/[`RegionKind::Bound`] for references to parameters introduced via higher ranked bounds or higher ranked types i.e. `for<'a> fn(&'a u32)` or `for<'a> T: Trait<'a>`. This is discussed in the [chapter on `Binder`s][ch_binders].
- [`RegionKind::LateParam`] for late bound lifetime parameters, `LateParam` is discussed in the [chapter on instantiating `Binder`s][ch_instantiating_binders].

This chapter only covers `TyKind::Param` `ConstKind::Param` and `RegionKind::EarlyParam`.

## Ty/Const Parameters

As `TyKind::Param` and `ConstKind::Param` are implemented identically this section only refers to `TyKind::Param` for simplicity.
However you should keep in mind that everything here also is true of `ConstKind::Param`

Each `TyKind::Param` contains two things: the name of the parameter and an index.

See the following concrete example of a usage of `TyKind::Param`:
```rust,ignore
struct Foo<T>(Vec<T>);
```
The `Vec<T>` type is represented as `TyKind::Adt(Vec, &[GenericArgKind::Type(Param("T", 0))])`.

The name is somewhat self explanatory; it's the name of the type parameter.
The index of the type parameter is an integer indicating
its order in the list of generic parameters in scope.
Note that this includes parameters defined on items on outer scopes than the item the parameter is defined on.
Consider the following examples:

```rust,ignore
struct Foo<A, B> {
  // A would have index 0
  // B would have index 1

  .. // some fields
}
impl<X, Y> Foo<X, Y> {
  fn method<Z>() {
    // inside here, X, Y and Z are all in scope
    // X has index 0
    // Y has index 1
    // Z has index 2
  }
}
```

Concretely, given the `ty::Generics` for the item the parameter is defined on,
if the index is `2` and if we start from the root `parent`, it will be the third parameter to be introduced.
For example in the above example, `Z` has index `2` and is the third generic parameter to be introduced, starting from the `impl` block.

The index fully defines the `Ty` and is the only part of `TyKind::Param` that matters for reasoning about the code we are compiling.

Generally, we do not care what the name is, and we only use the index.
The name is included for diagnostics and debug logs as otherwise it would be
incredibly difficult to understand the output, i.e. `Vec<Param(0)>: Sized` vs `Vec<T>: Sized`. In debug output, parameter types are
often printed out as `{name}/#{index}`, for example in the function `foo` if we were to debug print `Vec<T>` it would be written as `Vec<T/#0>`.

An alternative representation would be to only have the name.
However, using an index is more efficient as it means we can index into `GenericArgs` when instantiating generic parameters with some arguments.
We would otherwise have to store `GenericArgs` as a `HashMap<Symbol, GenericArg>` and do a hashmap lookup everytime we used a generic item.

In theory an index would also allow for having multiple distinct parameters that use the same name, e.g.
`impl<A> Foo<A> { fn bar<A>() { .. } }`.
The rules against shadowing make this difficult but those language rules could change in the future.

### Lifetime parameters

In contrast to `Ty`/`Const`'s `Param` singular `Param` variant, lifetimes have two variants for representing region parameters: [`RegionKind::EarlyParam`] and [`RegionKind::LateParam`].
The reason for this is due to function's distinguishing between [early and late bound parameters][ch_early_late_bound] which is discussed in an earlier chapter (see link).

`RegionKind::EarlyParam` is structured identically to `Ty/Const`'s `Param` variant; it is simply a `u32` index and a `Symbol`.
For lifetime parameters defined on non-function items, we always use `ReEarlyParam`.
For functions, we use `ReEarlyParam` for any early bound parameters and `ReLateParam` for any late bound parameters.
Note that, just like `Ty` and `Const` params, we often debug format them as `'SYMBOL/#INDEX`.

An example:

```rust,ignore
// This function would have its signature represented as:
//
// ```
// fn(
//     T/#2,
//     Ref('a/#0, Ref(ReLateParam(...), u32))
// ) -> Ref(ReLateParam(...), u32)
// ```
fn foo<'a, 'b, T: 'a>(one: T, two: &'a &'b u32) -> &'b u32 {
    ...
}
```

`RegionKind::LateParam` is discussed more in the chapter on [instantiating binders][ch_instantiating_binders].

[ch_early_late_bound]: ../early-late-parameters.md
[ch_binders]: ./binders.md
[ch_instantiating_binders]: ./instantiating-binders.md
[`BoundRegionKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.BoundRegionKind.html
[`RegionKind::EarlyParam`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.RegionKind.html#variant.ReEarlyParam
[`RegionKind::LateParam`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.RegionKind.html#variant.ReLateParam
[`ConstKind::Param`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.ConstKind.html#variant.Param
[`TyKind::Param`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TyKind.html#variant.Param
[`TyKind::Bound`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TyKind.html#variant.Bound
[`ConstKind::Bound`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.ConstKind.html#variant.Bound
[`RegionKind::Bound`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.RegionKind.html#variant.ReBound


---

<!-- date-check: may 2024 -->
# `TypeFoldable` and `TypeFolder`

In [a previous chapter], we discussed instantiating binders.
This involves looking at everything inside of a `Early(Binder)`
to find any usages of the bound vars in order to replace them.
Binders can wrap an arbitrary Rust type `T`, not just a `Ty`.
So, how do we implement the `instantiate` methods on the `Early/Binder` types?

The answer is a couple of traits:
[`TypeFoldable`]
and
[`TypeFolder`].

- `TypeFoldable` is implemented by types that embed type information. It allows you to recursively
  process the contents of the `TypeFoldable` and do stuff to them.
- `TypeFolder` defines what you want to do with the types you encounter while processing the
  `TypeFoldable`.

For example, the `TypeFolder` trait has a method [`fold_ty`]
that takes a type as input and returns a new type as a result.
`TypeFoldable` invokes the `TypeFolder` `fold_foo` methods on itself,
giving the `TypeFolder` access to its contents (the types, regions, etc that are contained within).

You can think of it with this analogy to the iterator combinators we have come to love in Rust:

```rust,ignore
vec.iter().map(|e1| foo(e2)).collect()
//             ^^^^^^^^^^^^ analogous to `TypeFolder`
//         ^^^ analogous to `TypeFoldable`
```

So to reiterate:

- `TypeFolder`  is a trait that defines a “map” operation.
- `TypeFoldable`  is a trait that is implemented by things that embed types.

In the case of `subst`, we can see that it is implemented as a `TypeFolder`: [`ArgFolder`].
Looking at its implementation, we see where the actual substitutions are happening.

However, you might also notice that the implementation calls this `super_fold_with` method. What is
that? It is a method of `TypeFoldable`. Consider the following `TypeFoldable` type `MyFoldable`:

```rust,ignore
struct MyFoldable<'tcx> {
  def_id: DefId,
  ty: Ty<'tcx>,
}
```

The `TypeFolder` can call `super_fold_with` on `MyFoldable` if it just wants to replace some of the
fields of `MyFoldable` with new values. If it instead wants to replace the whole `MyFoldable` with a
different one, it would call `fold_with` instead (a different method on `TypeFoldable`).

In almost all cases, we don’t want to replace the whole struct; we only want to replace `ty::Ty`s in
the struct, so usually we call `super_fold_with`. A typical implementation that `MyFoldable` could
have might do something like this:

```rust,ignore
my_foldable: MyFoldable<'tcx>
my_foldable.subst(..., subst)

impl TypeFoldable for MyFoldable {
  fn super_fold_with(&self, folder: &mut impl TypeFolder<'tcx>) -> MyFoldable {
    MyFoldable {
      def_id: self.def_id.fold_with(folder),
      ty: self.ty.fold_with(folder),
    }
  }

  fn super_visit_with(..) { }
}
```

Notice that here, we implement `super_fold_with` to go over the fields of `MyFoldable` and call
`fold_with` on *them*. That is, a folder may replace  `def_id` and `ty`, but not the whole
`MyFoldable` struct.

Here is another example to put things together: suppose we have a type like `Vec<Vec<X>>`. The
`ty::Ty` would look like: `Adt(Vec, &[Adt(Vec, &[Param(X)])])`. If we want to do `subst(X => u32)`,
then we would first look at the overall type. We would see that there are no substitutions to be
made at the outer level, so we would descend one level and look at `Adt(Vec, &[Param(X)])`. There
are still no substitutions to be made here, so we would descend again. Now we are looking at
`Param(X)`, which can be substituted, so we replace it with `u32`. We can’t descend any more, so we
are done, and  the overall result is `Adt(Vec, &[Adt(Vec, &[u32])])`.

One last thing to mention: often when folding over a `TypeFoldable`, we don’t want to change most
things. We only want to do something when we reach a type. That means there may be a lot of
`TypeFoldable` types whose implementations basically just forward to their fields’ `TypeFoldable`
implementations. Such implementations of `TypeFoldable` tend to be pretty tedious to write by hand.
For this reason, there is a `derive` macro that allows you to `#![derive(TypeFoldable)]`. It is
defined [here].

**`subst`** In the case of substitutions the [actual folder]
is going to be doing the indexing we’ve already mentioned.
There we define a `Folder` and call `fold_with` on the `TypeFoldable` to process yourself.
Then [fold_ty] the method that process each type it looks for a `ty::Param` and for those
it replaces it for something from the list of substitutions, otherwise recursively process the type.
To replace it, calls [ty_for_param]
and all that does is index into the list of substitutions with the index of the `Param`.

[a previous chapter]: ty-module/instantiating-binders.md
[`TypeFoldable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/trait.TypeFoldable.html
[`TypeFolder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/trait.TypeFolder.html
[`fold_ty`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/trait.TypeFolder.html#method.fold_ty
[`ArgFolder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/binder/struct.ArgFolder.html
[here]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_macros/src/type_foldable.rs
[actual folder]: https://github.com/rust-lang/rust/blob/75ff3110ac6d8a0259023b83fd20d7ab295f8dd6/src/librustc_middle/ty/subst.rs#L440-L451
[fold_ty]: https://github.com/rust-lang/rust/blob/75ff3110ac6d8a0259023b83fd20d7ab295f8dd6/src/librustc_middle/ty/subst.rs#L512-L536
[ty_for_param]: https://github.com/rust-lang/rust/blob/75ff3110ac6d8a0259023b83fd20d7ab295f8dd6/src/librustc_middle/ty/subst.rs#L552-L587


---

# Aliases and Normalization

## Aliases

In Rust there are a number of types that are considered equal to some "underlying" type, for example inherent associated types, trait associated types, free type aliases (`type Foo = u32`), and opaque types (`-> impl RPIT`). We consider such types to be "aliases", alias types are represented by the [`TyKind::Alias`][tykind_alias] variant, with the kind of alias tracked by the [`AliasTyKind`][aliaskind] enum.

Normalization is the process of taking these alias types and replacing them with the underlying type that they are equal to. For example given some type alias `type Foo = u32`, normalizing `Foo` would give `u32`.

The concept of an alias is not unique to *types* and the concept also applies to constants/const generics. However, right now in the compiler we don't really treat const aliases as a "first class concept" so this chapter mostly discusses things in the context of types (even though the concepts transfer just fine).

[tykind_alias]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/enum.TyKind.html#variant.Alias
[aliaskind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/enum.AliasTyKind.html

### Rigid, Ambiguous and Unnormalized Aliases

Aliases can either be "rigid", "ambiguous", or simply unnormalized.

We consider types to be rigid if their "shape" isn't going to change, for example `Box` is rigid as no amount of normalization can turn a `Box` into a `u32`, whereas `<vec::IntoIter<u32> as Iterator>::Item` is not rigid as it can be normalized to `u32`.

Aliases are rigid when we will never be able to normalize them further. A concrete example of a *rigid* alias would be `<T as Iterator>::Item` in an environment where there is no `T: Iterator<Item = ...>` bound, only a `T: Iterator` bound:
```rust
fn foo<T: Iterator>() {
    // This alias is *rigid*
    let _: <T as Iterator>::Item;
}

fn bar<T: Iterator<Item = u32>>() {
    // This alias is *not* rigid as it can be normalized to `u32`
    let _: <T as Iterator>::Item;
}
```

When an alias can't yet be normalized but may wind up normalizable in the [current environment](./typing-parameter-envs.md), we consider it to be an "ambiguous" alias. This can occur when an alias contains inference variables which prevent being able to determine how the trait is implemented:
```rust
fn foo<T: Iterator, U: Iterator>() {
    // This alias is considered to be "ambiguous"
    let _: <_ as Iterator>::Item;
}
```

The reason we call them "ambiguous" aliases is because its *ambiguous* whether this is a rigid alias or not.

The source of the `_: Iterator` trait impl is *ambiguous* (i.e. unknown), it could be some `impl Iterator for u32` or it could be some `T: Iterator` trait bound, we don't know yet. Depending on why `_: Iterator` holds the alias could be an unnormalized alias or it could be a rigid alias; it's *ambiguous* what kind of alias this is.

Finally, an alias can just be unnormalized, `<Vec<u32> as IntoIterator>::Iter` is an unnormalized alias as it can already be normalized to `std::vec::IntoIter<u32>`, it just hasn't been done yet.

---

It is worth noting that Free and Inherent aliases cannot be rigid or ambiguous as naming them also implies having resolved the definition of the alias, which specifies the underlying type of the alias.

### Diverging Aliases

An alias is considered to "diverge" if its definition does not specify an underlying non-alias type to normalize to. A concrete example of diverging aliases:
```rust
type Diverges = Diverges;

trait Trait {
    type DivergingAssoc;
}
impl Trait for () {
    type DivergingAssoc = <() as Trait>::DivergingAssoc;
}
```
In this example both `Diverges` and `DivergingAssoc` are "trivial" cases of diverging type aliases where they have been defined as being equal to themselves. There is no underlying type that `Diverges` can ever be normalized to.

We generally try to error when diverging aliases are defined, but this is entirely a "best effort" check. In the previous example the definitions are "simple enough" to be detected and so errors are emitted. However, in more complex cases, or cases where only some instantiations of generic parameters would result in a diverging alias, we don't emit an error:
```rust
trait Trait {
    type DivergingAssoc<U: Trait>;
}
impl<T: ?Sized> Trait for T {
    // This alias always diverges but we don't emit an error because
    // the compiler can't "see" that.
    type DivergingAssoc<U: Trait> = <U as Trait>::DivergingAssoc<U>;
}
```

Ultimately this means that we have no guarantee that aliases in the type system are non-diverging. As aliases may only diverge for some specific generic arguments, it also means that we only know whether an alias diverges once it is fully concrete. This means that codegen/const-evaluation also has to handle diverging aliases:
```rust
trait Trait {
    type Diverges<U: Trait>;
}
impl<T: ?Sized> Trait for T {
    type Diverges<U: Trait> = <U as Trait>::Diverges<U>;
}

fn foo<T: Trait>() {
    let a: T::Diverges<T>;
}

fn main() {
    foo::<()>();
}
```
In this example we only encounter an error from the diverging alias during codegen of `foo::<()>`, if the call to `foo` is removed then no compilation error will be emitted.

### Opaque Types

Opaque types are a relatively special kind of alias, and are covered in their own chapter: [Opaque types](./opaque-types-type-alias-impl-trait.md).

### Const Aliases

Unlike type aliases, const aliases are not represented directly in the type system, instead const aliases are always an anonymous body containing a path expression to a const item. This means that the only "const alias" in the type system is an anonymous unevaluated const body.

As such there is no `ConstKind::Alias(AliasCtKind::Projection/Inherent/Free, _)`, instead we only have `ConstKind::Unevaluated` which is used for representing anonymous constants.

```rust
fn foo<const N: usize>() {}

const FREE_CONST: usize = 1 + 1;

fn bar() {
    foo::<{ FREE_CONST }>();
    // The const arg is represented with some anonymous constant:
    // ```pseudo-rust
    // const ANON: usize = FREE_CONST;
    // foo::<ConstKind::Unevaluated(DefId(ANON), [])>();
    // ```
}
```

This is likely to change as const generics functionality is improved, for example `feature(associated_const_equality)` and `feature(min_generic_const_args)` both require handling const aliases similarly to types (without an anonymous constant wrapping all const args).

## What is Normalization

### Structural vs Deep normalization

There are two forms of normalization, structural (sometimes called *shallow*) and deep. Structural normalization should be thought of as only normalizing the "outermost" part of a type. On the other hand deep normalization will normalize *all* aliases in a type.

In practice structural normalization can result in more than just the outer layer of the type being normalized, but this behaviour should not be relied upon. Unnormalizable non-rigid aliases making use of bound variables (`for<'a>`) cannot be normalized by either kind of normalization.

As an example: conceptually, structurally normalizing the type `Vec<<u8 as Identity>::Assoc>` would be a no-op, whereas deeply normalizing would give `Vec<u8>`. In practice even structural normalization would give `Vec<u8>`, though, again, this should not be relied upon.

Changing the alias to use bound variables will result in different behaviour; `Vec<for<'a> fn(<&'a u8 as Identity>::Assoc)>` would result in no change when structurally normalized, but would result in `Vec<for<'a> fn(&'a u8)>` when deeply normalized.

### Core normalization logic

Structurally normalizing aliases is a little bit more nuanced than replacing the alias with whatever it is defined as being equal to in its definition; the result of normalizing an alias should either be a rigid type or an inference variable (which will later be inferred to a rigid type). To accomplish this we do two things:

First, when normalizing an ambiguous alias it is normalized to an inference variable instead of leaving it as-is, this has two main effects:
- Even though an inference variable is not a rigid type, it will always wind up inferred *to* a rigid type so we ensure that the result of normalization will not need to be normalized again
- Inference variables are used in all cases where a type is non-rigid, allowing the rest of the compiler to not have to deal with *both* ambiguous aliases *and* inference variables

Secondly, instead of having normalization directly return the type specified in the definition of the alias, we normalize the type first before returning it[^1]. We do this so that normalization is idempotent/callers do not need to run it in a loop.

```rust
#![feature(lazy_type_alias)]

type Foo<T: Iterator> = Bar<T>;
type Bar<T: Iterator> = <T as Iterator>::Item;

fn foo() {
    let a_: Foo<_>;
}
```

In this example:
- Normalizing `Foo<?x>` would result in `Bar<?x>`, except we want to normalize aliases in the type `Foo` is defined as equal to
- Normalizing `Bar<?x>` would result in `<?x as Iterator>::Item`, except, again, we want to normalize aliases in the type `Bar` is defined as equal to
- Normalizing `<?x as Iterator>::Item` results in some new inference variable `?y`, as `<?x as Iterator>::Item` is an ambiguous alias
- The final result is that normalizing `Foo<?x>` results in `?y`

## How to normalize

When interfacing with the type system it will often be the case that it's necessary to request a type be normalized. There are a number of different entry points to the underlying normalization logic and each entry point should only be used in specific parts of the compiler.

<!-- date-check: May 2025 -->
An additional complication is that the compiler is currently undergoing a transition from the old trait solver to the new trait solver.
As part of this transition our approach to normalization in the compiler has changed somewhat significantly, resulting in some normalization entry points being "old solver only" slated for removal in the long-term once the new solver has stabilized.
The transition can be tracked via the [WG-trait-system-refactor](https://github.com/rust-lang/rust/labels/WG-trait-system-refactor) label in Github.

Here is a rough overview of the different entry points to normalization in the compiler:
- `infcx.at.structurally_normalize`
- `infcx.at.(deeply_)?normalize`
- `infcx.query_normalize`
- `tcx.normalize_erasing_regions`
- `traits::normalize_with_depth(_to)`
- `EvalCtxt::structurally_normalize`

### Outside of the trait solver

The [`InferCtxt`][infcx] type exposes the "main" ways to normalize during analysis: [`normalize`][normalize], [`deeply_normalize`][deeply_normalize] and [`structurally_normalize`][structurally_normalize]. These functions are often wrapped and re-exposed on various `InferCtxt` wrapper types, such as [`FnCtxt`][fcx] or [`ObligationCtxt`][ocx] with minor API tweaks to handle some arguments or parts of the return type automatically.

#### Structural `InferCtxt` normalization

[`infcx.at.structurally_normalize`][structurally_normalize] exposes structural normalization that is able to handle inference variables and regions. It should generally be used whenever inspecting the kind of a type.

Inside of HIR Typeck there is a related method of normalization- [`fcx.structurally_resolve`][structurally_resolve], which will error if the type being resolved is an unresolved inference variable. When the new solver is enabled it will also attempt to structurally normalize the type.

Due to this there is a pattern in HIR typeck where a type is first normalized via `normalize` (only normalizing in the old solver), and then `structurally_resolve`'d (only normalizing in the new solver). This pattern should be preferred over calling `structurally_normalize` during HIR typeck as `structurally_resolve` will attempt to make inference progress by evaluating goals whereas `structurally_normalize` does not.

#### Deep `InferCtxt` normalization

##### `infcx.at.(deeply_)?normalize`

There are two ways to deeply normalize with an `InferCtxt`, `normalize` and `deeply_normalize`. The reason for this is that `normalize` is a "legacy" normalization entry point used only by the old solver, whereas `deeply_normalize` is intended to be the long term way to deeply normalize. Both of these methods can handle regions.

When the new solver is stabilized the `infcx.at.normalize` function will be removed and everything will have been migrated to the new deep or structural normalization methods. For this reason the `normalize` function is a no-op under the new solver, making it suitable only when the old solver needs normalization but the new solver does not.

Using `deeply_normalize` will result in errors being emitted when encountering ambiguous aliases[^2] as it is not possible to support normalizing *all* ambiguous aliases to inference variables[^3]. `deeply_normalize` should generally only be used in cases where we do not expect to encounter ambiguous aliases, for example when working with types from item signatures.

##### `infcx.query_normalize`

[`infcx.query_normalize`][query_norm] is very rarely used, it has almost all the same restrictions as `normalize_erasing_regions` (cannot handle inference variables, no diagnostics support) with the main difference being that it retains lifetime information. For this reason `normalize_erasing_regions` is the better choice in almost all circumstances as it is more efficient due to caching lifetime-erased queries.

In practice `query_normalize` is used for normalization in the borrow checker, and elsewhere as a performance optimization over `infcx.normalize`. Once the new solver is stabilized it is expected that `query_normalize` can be removed from the compiler as the new solvers normalization implementation should be performant enough for it to not be a performance regression.

##### `tcx.normalize_erasing_regions`

[`normalize_erasing_regions`][norm_erasing_regions] is generally used by parts of the compiler that are not doing type system analysis. This normalization entry point does not handle inference variables, lifetimes, or any diagnostics. Lints and codegen make heavy use of this entry point as they typically are working with fully inferred aliases that can be assumed to be well formed (or at least, are not responsible for erroring on).

[query_norm]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/at/struct.At.html#method.query_normalize
[norm_erasing_regions]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.normalize_erasing_regions
[normalize]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/at/struct.At.html#method.normalize
[deeply_normalize]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/normalize/trait.NormalizeExt.html#tymethod.deeply_normalize
[structurally_normalize]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/trait.StructurallyNormalizeExt.html#tymethod.structurally_normalize_ty
[infcx]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/infer/struct.InferCtxt.html
[fcx]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/fn_ctxt/struct.FnCtxt.html
[ocx]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/struct.ObligationCtxt.html
[structurally_resolve]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/fn_ctxt/struct.FnCtxt.html#method.structurally_resolve_type

### Inside of the trait solver

[`traits::normalize_with_depth(_to)`][norm_with_depth] and [`EvalCtxt::structurally_normalize`][eval_ctxt_structural_norm] are only used by the internals of the trait solvers (old and new respectively). It is effectively a raw entry point to the internals of how normalization is implemented by each trait solver. Other normalization entry points cannot be used from within the internals of trait solving as it wouldn't handle goal cycles and recursion depth correctly.

[norm_with_depth]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/normalize/fn.normalize_with_depth.html
[eval_ctxt_structural_norm]:  https://doc.rust-lang.org/nightly/nightly-rustc/rustc_next_trait_solver/solve/struct.EvalCtxt.html#method.structurally_normalize_term

## When/Where to normalize (Old vs New solver)

One of the big changes between the old and new solver is our approach to when we expect aliases to be normalized.

### Old solver

All types are expected to be normalized as soon as possible, so that all types encountered in the type system are either rigid or an inference variable (which will later be inferred to a rigid term).

As a concrete example: equality of aliases is implemented by assuming they're rigid and recursively equating the generic arguments of the alias.

### New solver

It's expected that all types potentially contain ambiguous or unnormalized aliases. Whenever an operation is performed that requires aliases to be normalized, it's the responsibility of that logic to normalize the alias (this means that matching on `ty.kind()` pretty much always has to structurally normalize first).

As a concrete example: equality of aliases is implemented by a custom goal kind ([`PredicateKind::AliasRelate`][aliasrelate]) so that it can handle normalization of the aliases itself instead of assuming all alias types being equated are rigid.

Despite this approach we still deeply normalize during [writeback][writeback] for performance/simplicity, so that types in the MIR can still be assumed to have been deeply normalized.

[aliasrelate]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.PredicateKind.html#variant.AliasRelate
[writeback]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/writeback/index.html

---

There were a few main issues with the old solver's approach to normalization that motivated changing things in the new solver:

### Missing normalization calls

It was a frequent occurrence that normalization calls would be missing, resulting in passing unnormalized types to APIs expecting everything to already be normalized. Treating ambiguous or unnormalized aliases as rigid would result in all sorts of weird errors from aliases not being considered equal to one another, or surprising inference guidance from equating unnormalized aliases' generic arguments.

### Normalizing parameter environments

Another problem was that it was not possible to normalize `ParamEnv`s correctly in the old solver as normalization itself would expect a normalized `ParamEnv` in order to give correct results. See the chapter on `ParamEnv`s for more information: [`Typing/ParamEnv`s: Normalizing all bounds](./typing-parameter-envs.md#normalizing-all-bounds)

### Unnormalizable non-rigid aliases in higher ranked types

Given a type such as `for<'a> fn(<?x as Trait<'a>::Assoc>)`, it is not possible to correctly handle this with the old solver's approach to normalization.

If we were to normalize it to `for<'a> fn(?y)` and register a goal to normalize `for<'a> <?x as Trait<'a>>::Assoc -> ?y`, this would result in errors in cases where `<?x as Trait<'a>>::Assoc` normalized to `&'a u32`. The inference variable `?y` would be in a lower [universe] than the placeholders made when instantiating the `for<'a>` binder.

Leaving the alias unnormalized would also be wrong as the old solver expects all aliases to be rigid. This was a soundness bug before the new solver was stabilized in coherence: [relating projection substs is unsound during coherence](https://github.com/rust-lang/rust/issues/102048).

Ultimately this means that it is not always possible to ensure all aliases inside of a value are rigid.

[universe]: borrow-check/region-inference/placeholders-and-universes.md#what-is-a-universe
[deeply_normalize]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/normalize/trait.NormalizeExt.html#tymethod.deeply_normalize

## Handling uses of diverging aliases

Diverging aliases, like ambiguous aliases, are normalized to inference variables. As normalizing diverging aliases results in trait solver cycles, it always results in an error in the old solver. In the new solver it only results in an error if we wind up requiring all goals to hold in the current context. E.g. normalizing diverging aliases during HIR typeck will result in an error in both solvers.

Alias well formedness doesn't require that the alias doesn't diverge[^4], this means that checking an alias is well formed isn't sufficient to cause an error to be emitted for diverging aliases; actually attempting to normalize the alias is required.

Erroring on diverging aliases being a side effect of normalization means that it is very *arbitrary* whether we actually emit an error, it also differs between the old and new solver as we now normalize in less places.

An example of the ad-hoc nature of erroring on diverging aliases causing "problems":
```rust
trait Trait {
    type Diverges<D: Trait>;
}

impl<T> Trait for T {
    type Diverges<D: Trait> = D::Diverges<D>;
}

struct Bar<T: ?Sized = <u8 as Trait>::Diverges<u8>>(Box<T>);
```

In this example a diverging alias is used but we happen to not emit an error as we never explicitly normalize the defaults of generic parameters. If the `?Sized` opt out is removed then an error is emitted because we wind up happening to normalize a `<u8 as Trait>::Diverges<u8>: Sized` goal which as a side effect results in erroring about the diverging alias.

Const aliases differ from type aliases a bit here; well formedness of const aliases requires that they can be successfully evaluated (via [`ConstEvaluatable`][const_evaluatable] goals). This means that simply checking well formedness of const arguments is sufficient to error if they would fail to evaluate. It is somewhat unclear whether it would make sense to adopt this for type aliases too or if const aliases should stop requiring this for well formedness[^5].

[^1]: In the new solver this is done implicitly

[^2]: There is a subtle difference in how ambiguous aliases in binders are handled between old and new solver. In the old solver we fail to error on some ambiguous aliases inside of higher ranked types whereas the new solver correctly errors.

[^3]: Ambiguous aliases inside of binders cannot be normalized to inference variables, this will be covered more later.

[^4]: As checking aliases are non-diverging cannot be done until they are fully concrete, this would either imply that we cant check aliases are well formed before codegen/const-evaluation or that aliases would go from being well-formed to not well-formed after monomorphization.

[^5]: Const aliases certainly wouldn't be *less* sound than type aliases if we stopped doing this

[const_evaluatable]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.ClauseKind.html#variant.ConstEvaluatable


---

# Typing/Parameter Environments

## Typing Environments

When interacting with the type system there are a few variables to consider that can affect the results of trait solving.
The set of in-scope where clauses, and what phase of the compiler type system operations are being performed in (the [`ParamEnv`][penv] and [`TypingMode`][tmode] structs respectively).

When an environment to perform type system operations in has not yet been created,
the [`TypingEnv`][tenv] can be used to bundle all of the external context required into a single type.

Once a context to perform type system operations in has been created (e.g. an [`ObligationCtxt`][ocx] or [`FnCtxt`][fnctxt]) a `TypingEnv` is typically not stored anywhere as only the `TypingMode` is a property of the whole environment,
whereas different `ParamEnv`s can be used on a per-goal basis.

[ocx]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/struct.ObligationCtxt.html
[fnctxt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/fn_ctxt/struct.FnCtxt.html

## Parameter Environments

### What is a `ParamEnv`

The [`ParamEnv`][penv] is a list of in-scope where-clauses,
it typically corresponds to a specific item's where clauses.
Some clauses are not explicitly written but are instead implicitly added in the [`predicates_of`][predicates_of] query,
such as `ConstArgHasType` or (some) implied bounds.

In most cases `ParamEnv`s are initially created via the [`param_env` query][query] which returns a `ParamEnv` derived from the provided item's where clauses.
A `ParamEnv` can also be created with arbitrary sets of clauses that are not derived from a specific item,
such as in [`compare_method_predicate_entailment`][method_pred_entailment] where we create a hybrid `ParamEnv` consisting of the impl's where clauses and the trait definition's function's where clauses.

---

If we have a function such as:
```rust
// `foo` would have a `ParamEnv` of:
// `[T: Sized, T: Trait, <T as Trait>::Assoc: Clone]`
fn foo<T: Trait>()
where
    <T as Trait>::Assoc: Clone,
{}
```
If we were conceptually inside of `foo` (for example, type-checking or linting it) we would use this `ParamEnv` everywhere that we interact with the type system.
This would allow things such as [normalization], evaluating generic constants,
and proving where clauses/goals, to rely on `T` being sized, implementing `Trait`, etc.

A more concrete example:
```rust
// `foo` would have a `ParamEnv` of:
// `[T: Sized, T: Clone]`
fn foo<T: Clone>(a: T) {
    // when typechecking `foo` we require all the where clauses on `requires_clone`
    // to hold in order for it to be legal to call. This means we have to
    // prove `T: Clone`. As we are type checking `foo` we use `foo`'s
    // environment when trying to check that `T: Clone` holds.
    //
    // Trying to prove `T: Clone` with a `ParamEnv` of `[T: Sized, T: Clone]`
    // will trivially succeed as bound we want to prove is in our environment.
    requires_clone(a);
}
```

Or alternatively an example that would not compile:
```rust
// `foo2` would have a `ParamEnv` of:
// `[T: Sized]`
fn foo2<T>(a: T) {
    // When typechecking `foo2` we attempt to prove `T: Clone`.
    // As we are type checking `foo2` we use `foo2`'s environment
    // when trying to prove `T: Clone`.
    //
    // Trying to prove `T: Clone` with a `ParamEnv` of `[T: Sized]` will
    // fail as there is nothing in the environment telling the trait solver
    // that `T` implements `Clone` and there exists no user written impl
    // that could apply.
    requires_clone(a);
}
```

[predicates_of]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/collect/predicates_of/fn.predicates_of.html
[method_pred_entailment]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/check/compare_impl_item/fn.compare_method_predicate_entailment.html
[query]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.param_env
[normalization]: normalization.md

### Acquiring a `ParamEnv`

Using the wrong [`ParamEnv`][penv] when interacting with the type system can lead to ICEs,
illformed programs compiling, or erroring when we shouldn't.
See [#82159](https://github.com/rust-lang/rust/pull/82159) and [#82067](https://github.com/rust-lang/rust/pull/82067) as examples of PRs that modified the compiler to use the correct param env and in the process fixed ICEs.

In the large majority of cases, when a `ParamEnv` is required it either already exists somewhere in scope,
or above in the call stack and should be passed down.
A non exhaustive list of places where you might find an existing `ParamEnv`:
- During typeck `FnCtxt` has a [`param_env` field][fnctxt_param_env]
- When writing late lints the `LateContext` has a [`param_env` field][latectxt_param_env]
- During well formedness checking the `WfCheckingCtxt` has a [`param_env` field][wfckctxt_param_env]
- The `TypeChecker` used for MIR Typeck has a [`param_env` field][mirtypeck_param_env]
- In the next-gen trait solver all `Goal`s have a [`param_env` field][goal_param_env] specifying what environment to prove the goal in
- When editing an existing [`TypeRelation`][typerelation] if it implements [`PredicateEmittingRelation`][predicate_emitting_relation] then a [`param_env` method][typerelation_param_env] will be available.

If you aren't sure if there's a `ParamEnv` in scope somewhere that can be used it can be worth opening a thread in the [`#t-compiler/help`][compiler_help] Zulip channel where someone may be able to point out where a `ParamEnv` can be acquired from.

Manually constructing a `ParamEnv` is typically only needed at the start of some kind of top level analysis (e.g. hir typeck or borrow checking).
In such cases there are three ways it can be done:
- Calling the [`tcx.param_env(def_id)` query][param_env_query] which returns the environment associated with a given definition.
- Creating an empty environment with [`ParamEnv::empty`][env_empty].
- Using [`ParamEnv::new`][param_env_new] to construct an env with an arbitrary set of where clauses.
  Then calling [`traits::normalize_param_env_or_error`][normalize_env_or_error] to handle normalizing and elaborating all the where clauses in the env.

Using the `param_env` query is by far the most common way to construct a `ParamEnv` as most of the time the compiler is performing an analysis as part of some specific definition.

Creating an empty environment with `ParamEnv::empty` is typically only done either in codegen (indirectly via [`TypingEnv::fully_monomorphized`][tenv_mono]),
or as part of some analysis that do not expect to ever encounter generic parameters
(e.g. various parts of coherence/orphan check).

Creating an env from an arbitrary set of where clauses is usually unnecessary and should only be done if the environment you need does not correspond to an actual item in the source code (e.g. [`compare_method_predicate_entailment`][method_pred_entailment]).

[param_env_new]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.ParamEnv.html#method.new
[normalize_env_or_error]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/fn.normalize_param_env_or_error.html
[fnctxt_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/fn_ctxt/struct.FnCtxt.html#structfield.param_env
[latectxt_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/context/struct.LateContext.html#structfield.param_env
[wfckctxt_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/check/wfcheck/struct.WfCheckingCtxt.html#structfield.param_env
[goal_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/canonical/ir/solve/struct.Goal.html#structfield.param_env
[typerelation_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/trait.PredicateEmittingRelation.html#tymethod.param_env
[typerelation]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/relate/trait.TypeRelation.html
[mirtypeck_param_env]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/type_check/struct.TypeChecker.html#structfield.param_env
[env_empty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.ParamEnv.html#method.empty
[param_env_query]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/fn_ctxt/struct.FnCtxt.html#structfield.param_env
[method_pred_entailment]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_analysis/check/compare_impl_item/fn.compare_method_predicate_entailment.html
[predicate_emitting_relation]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/relate/combine/trait.PredicateEmittingRelation.html
[tenv_mono]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TypingEnv.html#method.fully_monomorphized
[compiler_help]: https://rust-lang.zulipchat.com/#narrow/channel/182449-t-compiler.2Fhelp

### How are `ParamEnv`s constructed

Creating a [`ParamEnv`][pe] is more complicated than simply using the list of where clauses defined on an item as written by the user.
We need to both elaborate supertraits into the env and fully normalize all aliases.
This logic is handled by [`traits::normalize_param_env_or_error`][normalize_env_or_error] (even though it does not mention anything about elaboration).

#### Elaborating supertraits

When we have a function such as `fn foo<T: Copy>()` we would like to be able to prove `T: Clone` inside of the function as the `Copy` trait has a `Clone` supertrait.
Constructing a `ParamEnv` looks at all of the trait bounds in the env and explicitly adds new where clauses to the `ParamEnv` for any supertraits found on the traits.

A concrete example would be the following function:
```rust
trait Trait: SuperTrait {}
trait SuperTrait: SuperSuperTrait {}

// `bar`'s unelaborated `ParamEnv` would be:
// `[T: Sized, T: Copy, T: Trait]`
fn bar<T: Copy + Trait>(a: T) {
    requires_impl(a);
}

fn requires_impl<T: Clone + SuperSuperTrait>(a: T) {}
```

If we did not elaborate the env then the `requires_impl` call would fail to typecheck as we would not be able to prove `T: Clone` or `T: SuperSuperTrait`.
In practice we elaborate the env which means that `bar`'s `ParamEnv` is actually:
`[T: Sized, T: Copy, T: Clone, T: Trait, T: SuperTrait, T: SuperSuperTrait]`
This allows us to prove `T: Clone` and `T: SuperSuperTrait` when type checking `bar`.

The `Clone` trait has a `Sized` supertrait however we do not end up with two `T: Sized` bounds in the env (one for the supertrait and one for the implicitly added `T: Sized` bound) as the elaboration process (implemented via [`util::elaborate`][elaborate]) deduplicates where clauses.

A side effect of this is that even if no actual elaboration of supertraits takes place,
the existing where clauses in the env are _also_ deduplicated.
See the following example:
```rust
trait Trait {}
// The unelaborated `ParamEnv` would be:
// `[T: Sized, T: Trait, T: Trait]`
// but after elaboration it would be:
// `[T: Sized, T: Trait]`
fn foo<T: Trait + Trait>() {}
```

The [next-gen trait solver][next-gen-solver] also requires this elaboration to take place.

[elaborate]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/traits/util/fn.elaborate.html
[next-gen-solver]: ./solve/trait-solving.md

#### Normalizing all bounds

In the old trait solver the where clauses stored in `ParamEnv` are required to be fully normalized as otherwise the trait solver will not function correctly.
A concrete example of needing to normalize the `ParamEnv` is the following:
```rust
trait Trait<T> {
    type Assoc;
}

trait Other {
    type Bar;
}

impl<T> Other for T {
    type Bar = u32;
}

// `foo`'s unnormalized `ParamEnv` would be:
// `[T: Sized, U: Sized, U: Trait<T::Bar>]`
fn foo<T, U>(a: U) 
where
    U: Trait<<T as Other>::Bar>,
{
    requires_impl(a);
}

fn requires_impl<U: Trait<u32>>(_: U) {}
```

As humans we can tell that `<T as Other>::Bar` is equal to `u32` so the trait bound on `U` is equivalent to `U: Trait<u32>`.
In practice trying to prove `U: Trait<u32>` in the old solver in this environment would fail as it is unable to determine that `<T as Other>::Bar` is equal to `u32`.

To work around this we normalize `ParamEnv`'s after constructing them so that `foo`'s `ParamEnv` is actually: `[T: Sized, U: Sized, U: Trait<u32>]` which means the trait solver is now able to use the `U: Trait<u32>` in the `ParamEnv` to determine that the trait bound `U: Trait<u32>` holds.

This workaround does not work in all cases as normalizing associated types requires a `ParamEnv` which introduces a bootstrapping problem.
We need a normalized `ParamEnv` in order for normalization to give correct results, but we need to normalize to get that `ParamEnv`.
Currently we normalize the `ParamEnv` once using the unnormalized param env and it tends to give okay results in practice even though there are some examples where this breaks ([example]).

In the next-gen trait solver the requirement for all where clauses in the `ParamEnv` to be fully normalized is not present and so we do not normalize when constructing `ParamEnv`s.

[example]: https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=e6933265ea3e84eaa47019465739992c
[pe]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.ParamEnv.html
[normalize_env_or_error]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/fn.normalize_param_env_or_error.html

## Typing Modes

Depending on what context we are performing type system operations in,
different behaviour may be required.
For example during coherence there are stronger requirements about when we can consider goals to not hold or when we can consider types to be unequal.

Tracking which "phase" of the compiler type system operations are being performed in is done by the [`TypingMode`][tmode] enum.
The documentation on the `TypingMode` enum is quite good so instead of repeating it here verbatim we would recommend reading the API documentation directly.

[penv]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.ParamEnv.html
[tenv]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TypingEnv.html
[tmode]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TypingMode.html


---

# Type inference

Type inference is the process of automatic detection of the type of an
expression.

It is what allows Rust to work with fewer or no type annotations,
making things easier for users:

```rust
fn main() {
    let mut things = vec![];
    things.push("thing");
}
```

Here, the type of `things` is *inferred* to be `Vec<&str>` because of the value
we push into `things`.

The type inference is based on the standard Hindley-Milner (HM) type inference
algorithm, but extended in various ways to accommodate subtyping, region
inference, and higher-ranked types.

## A note on terminology

We use the notation `?T` to refer to inference variables, also called
existential variables.

We use the terms "region" and "lifetime" interchangeably. Both refer to
the `'a` in `&'a T`.

The term "bound region" refers to a region that is bound in a function
signature, such as the `'a` in `for<'a> fn(&'a u32)`. A region is
"free" if it is not bound.

## Creating an inference context

You create an inference context by doing something like
the following:

```rust,ignore
let infcx = tcx.infer_ctxt().build();
// Use the inference context `infcx` here.
```

`infcx` has the type `InferCtxt<'tcx>`, the same `'tcx` lifetime as on
the `tcx` it was built from.

The `tcx.infer_ctxt` method actually returns a builder, which means
there are some kinds of configuration you can do before the `infcx` is
created. See `InferCtxtBuilder` for more information.

<a id="vars"></a>

## Inference variables

The main purpose of the inference context is to house a bunch of
**inference variables** – these represent types or regions whose precise
value is not yet known, but will be uncovered as we perform type-checking.

If you're familiar with the basic ideas of unification from H-M type
systems, or logic languages like Prolog, this is the same concept. If
you're not, you might want to read a tutorial on how H-M type
inference works, or perhaps this blog post on
[unification in the Chalk project].

[Unification in the Chalk project]: http://smallcultfollowing.com/babysteps/blog/2017/03/25/unification-in-chalk-part-1/

All told, the inference context stores five kinds of inference variables
(as of <!-- date-check --> March 2023):

- Type variables, which come in three varieties:
  - General type variables (the most common). These can be unified with any
    type.
  - Integral type variables, which can only be unified with an integral type,
    and arise from an integer literal expression like `22`.
  - Float type variables, which can only be unified with a float type, and
    arise from a float literal expression like `22.0`.
- Region variables, which represent lifetimes, and arise all over the place.
- Const variables, which represent constants.

All the type variables work in much the same way: you can create a new
type variable, and what you get is `Ty<'tcx>` representing an
unresolved type `?T`. Then later you can apply the various operations
that the inferencer supports, such as equality or subtyping, and it
will possibly **instantiate** (or **bind**) that `?T` to a specific
value as a result.

The region variables work somewhat differently, and are described
below in a separate section.

## Enforcing equality / subtyping

The most basic operations you can perform in the type inferencer is
**equality**, which forces two types `T` and `U` to be the same. The
recommended way to add an equality constraint is to use the `at`
method, roughly like so:

```rust,ignore
infcx.at(...).eq(t, u);
```

The first `at()` call provides a bit of context, i.e. why you are
doing this unification, and in what environment, and the `eq` method
performs the actual equality constraint.

When you equate things, you force them to be precisely equal. Equating
returns an `InferResult` – if it returns `Err(err)`, then equating
failed, and the enclosing `TypeError` will tell you what went wrong.

The success case is perhaps more interesting. The "primary" return
type of `eq` is `()` – that is, when it succeeds, it doesn't return a
value of any particular interest. Rather, it is executed for its
side-effects of constraining type variables and so forth. However, the
actual return type is not `()`, but rather `InferOk<()>`. The
`InferOk` type is used to carry extra trait obligations – your job is
to ensure that these are fulfilled (typically by enrolling them in a
fulfillment context). See the [trait chapter] for more background on that.

[trait chapter]: traits/resolution.html

You can similarly enforce subtyping through `infcx.at(..).sub(..)`. The same
basic concepts as above apply.

## "Trying" equality

Sometimes you would like to know if it is *possible* to equate two
types without error.  You can test that with `infcx.can_eq` (or
`infcx.can_sub` for subtyping). If this returns `Ok`, then equality
is possible – but in all cases, any side-effects are reversed.

Be aware, though, that the success or failure of these methods is always
**modulo regions**. That is, two types `&'a u32` and `&'b u32` will
return `Ok` for `can_eq`, even if `'a != 'b`.  This falls out from the
"two-phase" nature of how we solve region constraints.

## Snapshots

As described in the previous section on `can_eq`, often it is useful
to be able to do a series of operations and then roll back their
side-effects. This is done for various reasons: one of them is to be
able to backtrack, trying out multiple possibilities before settling
on which path to take. Another is in order to ensure that a series of
smaller changes take place atomically or not at all.

To allow for this, the inference context supports a `snapshot` method.
When you call it, it will start recording changes that occur from the
operations you perform. When you are done, you can either invoke
`rollback_to`, which will undo those changes, or else `confirm`, which
will make them permanent. Snapshots can be nested as long as you follow
a stack-like discipline.

Rather than use snapshots directly, it is often helpful to use the
methods like `commit_if_ok` or `probe` that encapsulate higher-level
patterns.

## Subtyping obligations

One thing worth discussing is subtyping obligations. When you force
two types to be a subtype, like `?T <: i32`, we can often convert those
into equality constraints. This follows from Rust's rather limited notion
of subtyping: so, in the above case, `?T <: i32` is equivalent to `?T = i32`.

However, in some cases we have to be more careful. For example, when
regions are involved. So if you have `?T <: &'a i32`, what we would do
is to first "generalize" `&'a i32` into a type with a region variable:
`&'?b i32`, and then unify `?T` with that (`?T = &'?b i32`). We then
relate this new variable with the original bound:

```text
&'?b i32 <: &'a i32
```

This will result in a region constraint (see below) of `'?b: 'a`.

One final interesting case is relating two unbound type variables,
like `?T <: ?U`.  In that case, we can't make progress, so we enqueue
an obligation `Subtype(?T, ?U)` and return it via the `InferOk`
mechanism. You'll have to try again when more details about `?T` or
`?U` are known.

## Region constraints

Regions are inferenced somewhat differently from types. Rather than
eagerly unifying things, we simply collect constraints as we go, but
make (almost) no attempt to solve regions. These constraints have the
form of an "outlives" constraint:

```text
'a: 'b
```

Actually the code tends to view them as a subregion relation, but it's the same
idea:

```text
'b <= 'a
```

(There are various other kinds of constraints, such as "verifys"; see
the [`region_constraints`] module for details.)

There is one case where we do some amount of eager unification. If you have an
equality constraint between two regions

```text
'a = 'b
```

we will record that fact in a unification table. You can then use
[`opportunistic_resolve_var`] to convert `'b` to `'a` (or vice
versa). This is sometimes needed to ensure termination of fixed-point
algorithms.

[`region_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/region_constraints/index.html
[`opportunistic_resolve_var`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/region_constraints/struct.RegionConstraintCollector.html#method.opportunistic_resolve_var

## Solving region constraints

Region constraints are only solved at the very end of
typechecking, once all other constraints are known and
all other obligations have been proven. There are two
ways to solve region constraints right now: lexical and
non-lexical. Eventually there will only be one.

An exception here is the leak-check which is used during trait solving
and relies on region constraints containing higher-ranked regions. Region
constraints in the root universe (i.e. not arising from a `for<'a>`) must
not influence the trait system, as these regions are all erased during
codegen.

To solve **lexical** region constraints, you invoke
[`resolve_regions_and_report_errors`].  This "closes" the region
constraint process and invokes the [`lexical_region_resolve`] code. Once
this is done, any further attempt to equate or create a subtyping
relationship will yield an ICE.

The NLL solver (actually, the MIR type-checker) does things slightly
differently. It uses canonical queries for trait solving which use
[`take_and_reset_region_constraints`] at the end. This extracts all of the
outlives constraints added during the canonical query. This is required
as the NLL solver must not only know *what* regions outlive each other,
but also *where*. Finally, the NLL solver invokes [`get_region_var_infos`],
providing all region variables to the solver.

[`resolve_regions_and_report_errors`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_trait_selection/traits/struct.ObligationCtxt.html#method.resolve_regions_and_report_errors
[`lexical_region_resolve`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/lexical_region_resolve/index.html
[`take_and_reset_region_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/struct.InferCtxt.html#method.take_and_reset_region_constraints
[`get_region_var_infos`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/struct.InferCtxt.html#method.get_region_var_infos

## Lexical region resolution

Lexical region resolution is done by initially assigning each region
variable to an empty value. We then process each outlives constraint
repeatedly, growing region variables until a fixed-point is reached.
Region variables can be grown using a least-upper-bound relation on
the region lattice in a fairly straightforward fashion.
