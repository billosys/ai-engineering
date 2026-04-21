# Background topics

This section covers a numbers of common compiler terms that arise in
this guide. We try to give the general definition while providing some
Rust-specific context.

<a id="cfg"></a>

## What is a control-flow graph?

A control-flow graph (CFG) is a common term from compilers. If you've ever
used a flow-chart, then the concept of a control-flow graph will be
pretty familiar to you. It's a representation of your program that
clearly exposes the underlying control flow.

A control-flow graph is structured as a set of **basic blocks**
connected by edges. The key idea of a basic block is that it is a set
of statements that execute "together" – that is, whenever you branch
to a basic block, you start at the first statement and then execute
all the remainder. Only at the end of the block is there the
possibility of branching to more than one place (in MIR, we call that
final statement the **terminator**):

```mir
bb0: {
    statement0;
    statement1;
    statement2;
    ...
    terminator;
}
```

Many expressions that you are used to in Rust compile down to multiple
basic blocks. For example, consider an if statement:

```rust,ignore
a = 1;
if some_variable {
    b = 1;
} else {
    c = 1;
}
d = 1;
```

This would compile into four basic blocks in MIR. In textual form, it looks like
this:

```mir
BB0: {
    a = 1;
    if some_variable {
        goto BB1;
    } else {
        goto BB2;
    }
}

BB1: {
    b = 1;
    goto BB3;
}

BB2: {
    c = 1;
    goto BB3;
}

BB3: {
    d = 1;
    ...
}
```

In graphical form, it looks like this:

```
                BB0
       +--------------------+
       | a = 1;             |
       +--------------------+
             /       \
  if some_variable   else
           /           \
     BB1  /             \  BB2
    +-----------+   +-----------+
    | b = 1;    |   | c = 1;    |
    +-----------+   +-----------+
            \          /
             \        /
              \ BB3  /
            +----------+
            | d = 1;   |
            | ...      |
            +----------+
```

When using a control-flow graph, a loop simply appears as a cycle in
the graph, and the `break` keyword translates into a path out of that
cycle.

<a id="dataflow"></a>

## What is a dataflow analysis?

[*Static Program Analysis*](https://cs.au.dk/~amoeller/spa/) by Anders Møller
and Michael I. Schwartzbach is an incredible resource!

_Dataflow analysis_ is a type of static analysis that is common in many
compilers. It describes a general technique, rather than a particular analysis.

The basic idea is that we can walk over a [control-flow graph (CFG)](#cfg) and
keep track of what some value could be. At the end of the walk, we might have
shown that some claim is true or not necessarily true (e.g. "this variable must
be initialized"). `rustc` tends to do dataflow analyses over the MIR, since MIR
is already a CFG.

For example, suppose we want to check that `x` is initialized before it is used
in this snippet:

```rust,ignore
fn foo() {
    let mut x;

    if some_cond {
        x = 1;
    }

    dbg!(x);
}
```

A CFG for this code might look like this:

```txt
 +------+
 | Init | (A)
 +------+
    |   \
    |   if some_cond
  else    \ +-------+
    |      \| x = 1 | (B)
    |       +-------+
    |      /
 +---------+
 | dbg!(x) | (C)
 +---------+
```

We can do the dataflow analysis as follows: we will start off with a flag `init`
which indicates if we know `x` is initialized. As we walk the CFG, we will
update the flag. At the end, we can check its value.

So first, in block (A), the variable `x` is declared but not initialized, so
`init = false`. In block (B), we initialize the value, so we know that `x` is
initialized. So at the end of (B), `init = true`.

Block (C) is where things get interesting. Notice that there are two incoming
edges, one from (A) and one from (B), corresponding to whether `some_cond` is true or not.
But we cannot know that! It could be the case the `some_cond` is always true,
so that `x` is actually always initialized. It could also be the case that
`some_cond` depends on something random (e.g. the time), so `x` may not be
initialized. In general, we cannot know statically (due to [Rice's
Theorem][rice]).  So what should the value of `init` be in block (C)?

[rice]: https://en.wikipedia.org/wiki/Rice%27s_theorem

Generally, in dataflow analyses, if a block has multiple parents (like (C) in
our example), its dataflow value will be some function of all its parents (and
of course, what happens in (C)).  Which function we use depends on the analysis
we are doing.

In this case, we want to be able to prove definitively that `x` must be
initialized before use. This forces us to be conservative and assume that
`some_cond` might be false sometimes. So our "merging function" is "and". That
is, `init = true` in (C) if `init = true` in (A) _and_ in (B) (or if `x` is
initialized in (C)). But this is not the case; in particular, `init = false` in
(A), and `x` is not initialized in (C).  Thus, `init = false` in (C); we can
report an error that "`x` may not be initialized before use".

There is definitely a lot more that can be said about dataflow analyses. There is an
extensive body of research literature on the topic, including a lot of theory.
We only discussed a forwards analysis, but backwards dataflow analysis is also
useful. For example, rather than starting from block (A) and moving forwards,
we might have started with the usage of `x` and moved backwards to try to find
its initialization.

<a id="quantified"></a>

## What is "universally quantified"? What about "existentially quantified"?

In math, a predicate may be _universally quantified_ or _existentially
quantified_:

- _Universal_ quantification:
  - the predicate holds if it is true for all possible inputs.
  - Traditional notation: ∀x: P(x). Read as "for all x, P(x) holds".
- _Existential_ quantification:
  - the predicate holds if there is any input where it is true, i.e., there
    only has to be a single input.
  - Traditional notation: ∃x: P(x). Read as "there exists x such that P(x) holds".

In Rust, they come up in type checking and trait solving. For example,

```rust,ignore
fn foo<T>()
```
This function claims that the function is well-typed for all types `T`: `∀ T: well_typed(foo)`.

Another example:

```rust,ignore
fn foo<'a>(_: &'a usize)
```
This function claims that for any lifetime `'a` (determined by the
caller), it is well-typed: `∀ 'a: well_typed(foo)`.

Another example:

```rust,ignore
fn foo<F>()
where for<'a> F: Fn(&'a u8)
```
This function claims that it is well-typed for all types `F` such that for all
lifetimes `'a`, `F: Fn(&'a u8)`: `∀ F: ∀ 'a: (F: Fn(&'a u8)) => well_typed(foo)`.

One more example:

```rust,ignore
fn foo(_: dyn Debug)
```
This function claims that there exists some type `T` that implements `Debug`
such that the function is well-typed: `∃ T:  (T: Debug) and well_typed(foo)`.

<a id="variance"></a>

## What is a de Bruijn Index?

[De Bruijn indices][wikideb] are a way of representing, using only integers,
which variables are bound in which binders. They were originally invented for
use in lambda calculus evaluation (see [this Wikipedia article][wikideb] for
more). In `rustc`, we use de Bruijn indices to [represent generic types][sub].

[wikideb]: https://en.wikipedia.org/wiki/De_Bruijn_index
[sub]: ../ty-module/generic-arguments.md

Here is a basic example of how de Bruijn indices might be used for closures (we
don't actually do this in `rustc` though!):

```rust,ignore
|x| {
    f(x) // de Bruijn index of `x` is 1 because `x` is bound 1 level up

    |y| {
        g(x, y) // index of `x` is 2 because it is bound 2 levels up
                // index of `y` is 1 because it is bound 1 level up
    }
}
```

## What are co- and contra-variance?

Check out the subtyping chapter from the
[Rust Nomicon](https://doc.rust-lang.org/nomicon/subtyping.html).

See the [variance](../variance.html) chapter of this guide for more info on how
the type checker handles variance.

<a id="free-vs-bound"></a>

## What is a "free region" or a "free variable"? What about "bound region"?

Let's describe the concepts of free vs bound in terms of program
variables, since that's the thing we're most familiar with.

- Consider this expression, which creates a closure: `|a, b| a + b`.
  Here, the `a` and `b` in `a + b` refer to the arguments that the closure will
  be given when it is called. We say that the `a` and `b` there are **bound** to
  the closure, and that the closure signature `|a, b|` is a **binder** for the
  names `a` and `b` (because any references to `a` or `b` within refer to the
  variables that it introduces).
- Consider this expression: `a + b`. In this expression, `a` and `b` refer to
  local variables that are defined *outside* of the expression. We say that
  those variables **appear free** in the expression (i.e., they are **free**,
  not **bound** (tied up)).

So there you have it: a variable "appears free" in some
expression/statement/whatever if it refers to something defined
outside of that expressions/statement/whatever. Equivalently, we can
then refer to the "free variables" of an expression – which is just
the set of variables that "appear free".

So what does this have to do with regions? Well, we can apply the
analogous concept to type and regions. For example, in the type `&'a
u32`, `'a` appears free.  But in the type `for<'a> fn(&'a u32)`, it
does not.

# Further Reading About Compilers

> Thanks to `mem`, `scottmcm`, and `Levi` on the official Discord for the
> recommendations, and to `tinaun` for posting a link to a [twitter thread from
> Graydon Hoare](https://web.archive.org/web/20181230012554/https://twitter.com/graydon_pub/status/1039615569132118016)
> which had some more recommendations!
>
> Other sources: https://gcc.gnu.org/wiki/ListOfCompilerBooks
>
> If you have other suggestions, please feel free to open an issue or PR.

## Books
- [Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/tapl/)
- [Programming Language Pragmatics](https://www.cs.rochester.edu/~scott/pragmatics/)
- [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl/)
- [Compilers: Principles, Techniques, and Tools, 2nd Edition](https://www.pearson.com/us/higher-education/program/Aho-Compilers-Principles-Techniques-and-Tools-2nd-Edition/PGM167067.html)
- [Garbage Collection: Algorithms for Automatic Dynamic Memory Management](https://www.cs.kent.ac.uk/people/staff/rej/gcbook/)
- [Linkers and Loaders](https://www.amazon.com/Linkers-Kaufmann-Software-Engineering-Programming/dp/1558604960) (There are also free versions of this, but the version we had linked seems to be offline at the moment.)
- [Advanced Compiler Design and Implementation](https://www.goodreads.com/book/show/887908.Advanced_Compiler_Design_and_Implementation)
- [Building an Optimizing Compiler](https://www.goodreads.com/book/show/2063103.Building_an_Optimizing_Compiler)
- [Crafting Interpreters](http://www.craftinginterpreters.com/)

## Courses
- [University of Oregon Programming Languages Summer School archive](https://www.cs.uoregon.edu/research/summerschool/archives.html)

## Wikis
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [Esoteric Programming Languages](https://esolangs.org/wiki/Main_Page)
- [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/index.html)
- [nLab](https://ncatlab.org/nlab/show/HomePage)

## Misc Papers and Blog Posts
- [Programming in Martin-Löf's Type Theory](https://www.cse.chalmers.se/research/group/logic/book/)
- [Polymorphism, Subtyping, and Type Inference in MLsub](https://dl.acm.org/doi/10.1145/3093333.3009882)


---

# Glossary

Term                                           | Meaning
-----------------------------------------------|--------
<span id="1zst">1-ZST</span>                   |  A *one-aligned [zero-sized type](#zst)*. A type of size zero with an [alignment][size-align] of one.
<span id="arena">arena, arena allocation</span> |  An _arena_ is a large memory buffer from which other memory allocations are made. This style of allocation is called _arena allocation_. See [this chapter](../memory.md) for more info.
<span id="afidt">AFIDT</span>                  |  Short for _async function in `dyn Trait`_. See also [AFIT](#afit).
<span id="afit">AFIT</span>                    |  Short for _async function in trait_. They desugar to [RPITITs](#rpitit).
<span id="ast">AST</span>                      |  The _abstract syntax tree_ (an [IR](#ir)) produced by the parser; reflects the surface / user syntax very closely.
<span id="apit">APIT</span>                    |  Short for _argument-position `impl Trait`_. Also known as universial `impl Trait` (as opposed to existential) or anonymous type parameter. ([see the reference](https://doc.rust-lang.org/reference/types/impl-trait.html#anonymous-type-parameters)).
<span id="atpit">ATPIT</span>                  |  Short for _associated-type-position `impl Trait`_. Also known as [ITIAT](#itiat).
<span id="binder">binder</span>                |  A _binder_ is a place where a variable or type is declared; for example, the `<T>` is a binder for the type parameter `T` in `fn foo<T>(..)`, `for<'a>` is a binder for the lifetime parameter `'a` and `\|a\| …` is a binder for the parameter `a`. See [the background chapter for more](./background.md#free-vs-bound).
<span id="body">body</span>                    |  The definition of a function or constant that contains "executable code".
<span id="body-id">`BodyId`</span>             |  An identifier that refers to a specific [body](#body) in the crate. See [the HIR chapter for more](../hir.md#identifiers-in-the-hir).
<span id="bound-var">bound variable</span>     |  A _bound variable_ is one that is declared within an expression or term (in the general sense). For example, the variable `a` is bound within the closure expression `\|a\| a * 2` and lifetime variable `'a` is bound within the type expression `for<'a> fn(&'a str) -> bool`. See [the background chapter for more](./background.md#free-vs-bound)
<span id="codegen">codegen</span>              |  Short for _code generation_. The code to translate MIR into LLVM IR.
<span id="codegen-unit">codegen unit</span>    |  When we produce LLVM IR, we group the Rust code into a number of codegen units (sometimes abbreviated as CGUs). Each of these units is processed by LLVM independently from one another, enabling parallelism. They are also the unit of incremental re-use. ([see more](../backend/codegen.md))
<span id="completeness">completeness</span>    |  A technical term in type theory, it means that every type-safe program also type-checks. Having both soundness and completeness is very hard, and usually soundness is more important. (see "soundness").
<span id="cfg">control-flow graph, CFG</span>  |  A representation of the control-flow of a program; see [the background chapter for more](./background.md#cfg)
<span id="ctfe">CTFE</span>                    |  Short for _compile-time function evaluation_, this is the ability of the compiler to evaluate `const fn`s at compile time. This is part of the compiler's constant evaluation system. ([see more](../const-eval.md))
<span id="cx">`cx`</span>                      |  We tend to use _cx_ as an abbreviation for _context_. See also `tcx`, `infcx`, etc.
<span id="ctxt">`ctxt`</span>                  |  We also use _ctxt_ as an abbreviation for _context_, e.g. [`TyCtxt`](#TyCtxt). See also [cx](#cx) or [tcx](#tcx).
<span id="dag">DAG</span>                      |  A _directed acyclic graph_ is used during compilation to keep track of dependencies between queries. ([see more](../queries/incremental-compilation.md))
<span id="data-flow">data-flow analysis</span> |  A static analysis that figures out what properties are true at each point in the control-flow of a program; see [the background chapter for more](./background.md#dataflow).
<span id="debruijn">de Bruijn index</span>     |  A technique for describing which binder a variable is bound by using only integers. It has the benefit that it is invariant under variable renaming. ([see more](./background.md#what-is-a-debruijn-index))
<span id="def-id">`DefId`</span>               |  An index identifying a definition (see `rustc_middle/src/hir/def_id.rs`). Uniquely identifies a `DefPath`. See [the HIR chapter for more](../hir.md#identifiers-in-the-hir).
<span id="discriminant">discriminant</span>    |  The underlying value associated with an enum variant or generator state to indicate it as "active" (but not to be confused with its ["variant index"](#variant-idx)). At runtime, the discriminant of the active variant is encoded in the [tag](#tag).
<span id="double-ptr">double pointer</span>    |  A pointer with additional metadata. See [fat pointer](#fat-ptr) for more.
<span id="drop-glue">drop glue</span>          |  (Internal) compiler-generated instructions that handle calling the destructors (`Drop`) for data types.
<span id="dst">DST</span>                      |  Short for *dynamically-sized type*, this is a type for which the compiler cannot statically know the size in memory (e.g. `str` or `[u8]`). Such types don't implement `Sized` and cannot be allocated on the stack. They can only occur as the last field in a struct. They can only be used behind a pointer (e.g. `&str` or `&[u8]`).
<span id="ebl">early-bound lifetime</span>     |  A lifetime / region that is substituted at its definition site. Bound in an item's `Generics` and substituted/instantiated using a `GenericArgs`. Contrast with **late-bound lifetime**. ([see more](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/region_kind/enum.RegionKind.html#bound-regions))
<span id="effect">effects</span>               |  Right now only means const traits and `~const` bounds. ([see more](../effects.md))
<span id="empty-type">empty type</span>        |  See [uninhabited type](#ut).
<span id="fat-ptr">fat pointer</span>          |  A two word value carrying the address of some value, along with some further information necessary to put the value to use. Rust includes two kinds of _fat pointers_: references to slices, and trait objects. A reference to a slice carries the starting address of the slice and its length. A trait object carries a value's address and a pointer to the trait's implementation appropriate to that value. "Fat pointers" are also known as "wide pointers", and "double pointers".
<span id="free-var">free variable</span>       |  A _free variable_ is one that is not bound within an expression or term (in the general sense); see [the background chapter for more](./background.md#free-vs-bound)
<span id="gac">GAC</span>                      |  A _generic associated constant_, an associated constant with (own) generic parameters or a where-clause. Part of feature [`generic_const_items`] (GCI).
<span id="gat">GAT</span>                      |  A _generic associated type_, an associated type that has (own) generic parameters or a where-clause. Introduced in [RFC 1598].
<span id="generics">generics</span>            |  The list of generic parameters defined on an item. There are three kinds of generic parameters: Type, lifetime and const parameters.
<span id="hir">HIR</span>                      |  The _high-level [IR](#ir)_, created by lowering / desugaring the AST. ([see more](../hir.md))
<span id="hir-id">`HirId`</span>               |  Identifies a particular node in the HIR by combining a def-id with an "intra-definition offset". See [the HIR chapter for more](../hir.md#identifiers-in-the-hir).
<span id="iac">IAC</span>                      |  A (more often than not type-level) _inherent associated constant_, an associated constant in an inherent impl `impl Type { … }`. Often mentioned in the context of feature [`min_generic_const_items`] (mGCA, MGCA). An IGAC is an inherent [GAC](#gac).
<span id="iat">IAT</span>                      |  An _inherent associated type_, an associated type defined in an inherent impl `impl Type { … }`. An IGAT is an inherent [GAT](#gat), a generic IAT.
<span id="ice">ICE</span>                      |  Short for _internal compiler error_, this is when the compiler crashes.
<span id="ich">ICH</span>                      |  Short for _incremental compilation hash_, these are used as fingerprints for things such as HIR and crate metadata, to check if changes have been made. This is useful in incremental compilation to see if part of a crate has changed and should be recompiled.
<span id="infcx">`infcx`</span>                |  The type inference context (`InferCtxt`). (see `rustc_middle::infer`)
<span id="inf-var">inference variable, infer var </span> |  When doing type, region, const inference, an _inference variable_ is a kind of special type/region that represents what you are trying to infer. Think of X in algebra. For example, if we are trying to infer the type of a variable in a program, we create an inference variable to represent that unknown type.
<span id="intern">intern</span>                |  Interning refers to storing certain frequently-used constant data, such as strings, and then referring to the data by an identifier (e.g. a `Symbol`) rather than the data itself, to reduce memory usage and number of allocations. See [this chapter](../memory.md) for more info.
<span id="interpreter">interpreter</span>      |  The heart of const evaluation, running MIR code at compile time. ([see more](../const-eval/interpret.md))
<span id="intrinsic">intrinsic</span>          |  Intrinsics are special functions that are implemented in the compiler itself but exposed (often unstably) to users. They do magical and dangerous things. (See [`std::intrinsics`](https://doc.rust-lang.org/std/intrinsics/index.html))
<span id="ir">IR</span>                        |  Short for _intermediate representation_, a general term in compilers. During compilation, the code is transformed from raw source (ASCII text) to various IRs. In Rust, these are primarily HIR, MIR, and LLVM IR. Each IR is well-suited for some set of computations. For example, MIR is well-suited for the borrow checker, and LLVM IR is well-suited for codegen because LLVM accepts it.
<span id="irlo">IRLO, irlo</span>              |  Sometimes used as an abbreviation for [internals.rust-lang.org](https://internals.rust-lang.org).
<span id="item">item</span>                    |  A kind of "definition" in the language, such as a static, const, use statement, module, struct, etc. Concretely, this corresponds to the `Item` type.
<span id="item-sig">item signature</span>      |  The type signature / annotation / ascription of an item (e.g., struct, function). Often mentioned in the context of type inference since they are a place where we don't perform inference contrary to types in [bodies](#body).
<span id="itiat">ITIAT</span>                  |  Short for _`impl Trait` in associated type_. Also known as [ATPIT](#atpit).
<span id="lang-item">lang item</span>          |  Items that represent concepts intrinsic to the language itself, such as special built-in traits like `Sync` and `Send`; or traits representing operations such as `Add`; or functions that are called by the compiler. ([see more](https://doc.rust-lang.org/1.9.0/book/lang-items.html))
<span id="lbl">late-bound lifetime</span>      |  A lifetime / region that is substituted at its call site. Bound in a HRTB and substituted by specific functions in the compiler, such as `liberate_late_bound_regions`. Contrast with **early-bound lifetime**. ([see more](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/region_kind/enum.RegionKind.html#bound-regions))
<span id="local-crate">local crate</span>      |  The crate currently being compiled. This is in contrast to "upstream crates" which refer to dependencies of the local crate.
<span id="lowering">lowering</span>            |  The act of converting a higher-level [IR](#ir) to a lower-level one. E.g., AST lowering (from [AST](#ast) to [HIR](#hir)) or HIR ty lowering (from HIR to [middle ty IR](#middle-ty-ir)).
<span id="lta">LTA</span>                      |  A _lazy type alias_, a type alias that gets "properly" represented as an alias in the [middle ty IR](#middle-ty-ir); contrary to (eager) type aliases whose reference sites get expanded to the underlying aliased type (the RHS of the type alias after instantiation) during HIR ty lowering, its reference sites get [lowered](#lowering) to an [`AliasTy`].
<span id="lto">LTO</span>                      |  Short for *link-time optimizations*, this is a set of optimizations offered by LLVM that occur just before the final binary is linked. These include optimizations like removing functions that are never used in the final program, for example. _ThinLTO_ is a variant of LTO that aims to be a bit more scalable and efficient, but possibly sacrifices some optimizations. You may also read issues in the Rust repo about "FatLTO", which is the loving nickname given to non-Thin LTO. LLVM documentation: [here][lto] and [here][thinlto].
<span id="llvm">[LLVM]</span>                  |  (actually not an acronym :P) an open-source compiler backend. It accepts LLVM IR and outputs native binaries. Various languages (e.g. Rust) can then implement a compiler front-end that outputs LLVM IR and use LLVM to compile to all the platforms LLVM supports.
<span id="memoization">memoization</span>      |  The process of storing the results of (pure) computations (such as pure function calls) to avoid having to repeat them in the future. This is typically a trade-off between execution speed and memory usage.
<span id="middle-ty-ir">middle ty IR</span>    |  The collection of types defined in module [`rustc_middle::ty`] used by the type checker and the trait solver. They essentially form an [IR](#ir).
<span id="mir">MIR</span>                      |  The _mid-level [IR](#ir)_ that is created after type-checking for use by borrowck and codegen. ([see more](../mir/index.md))
<span id="miri">Miri</span>                    |  A tool to detect Undefined Behavior in (unsafe) Rust code. ([see more](https://github.com/rust-lang/miri))
<span id="mono">monomorphization</span>        |  The process of taking generic implementations of types and functions and instantiating them with concrete types. For example, in the code we might have `Vec<T>`, but in the final executable, we will have a copy of the `Vec` code for every concrete type used in the program (e.g. a copy for `Vec<usize>`, a copy for `Vec<MyStruct>`, etc).
<span id="normalize">normalize</span>          |  A general term for converting to a more canonical form, but in the case of rustc typically refers to [associated type normalization](../traits/goals-and-clauses.md#normalizeprojection---type).
<span id="newtype">newtype</span>              |  A wrapper around some other type (e.g., `struct Foo(T)` is a "newtype" for `T`). This is commonly used in Rust to give a stronger type for indices.
<span id="niche">niche</span>                  |  Invalid bit patterns for a type _that can be used_ for layout optimizations. Some types cannot have certain bit patterns. For example, the `NonZero*` integers or the reference `&T` cannot be represented by a 0 bitstring. This means the compiler can perform layout optimizations by taking advantage of the invalid "niche value". An example application for this is the [*Discriminant elision on `Option`-like enums*](https://rust-lang.github.io/unsafe-code-guidelines/layout/enums.html#discriminant-elision-on-option-like-enums), which allows using a type's niche as the ["tag"](#tag) for an `enum` without requiring a separate field.
<span id="nll">NLL</span>                      |  Short for [non-lexical lifetimes](../borrow-check/region-inference.md), this is an extension to Rust's borrowing system to make it be based on the control-flow graph.
<span id="node-id">node-id or `NodeId`</span>  |  An index identifying a particular node in the AST or HIR; gradually being phased out and replaced with `HirId`. See [the HIR chapter for more](../hir.md#identifiers-in-the-hir).
<span id="obligation">obligation</span>        |  Something that must be proven by the trait system. ([see more](../traits/resolution.md))
<span id="placeholder">placeholder</span>      |  **NOTE: skolemization is deprecated by placeholder** a way of handling subtyping around "for-all" types (e.g., `for<'a> fn(&'a u32)`) as well as solving higher-ranked trait bounds (e.g., `for<'a> T: Trait<'a>`). See [the chapter on placeholder and universes](../borrow-check/region-inference/placeholders-and-universes.md) for more details.
<span id="point">point</span>                  |  Used in the NLL analysis to refer to some particular location in the MIR; typically used to refer to a node in the control-flow graph.
<span id="projection">projection</span>        |  A general term for a "relative path", e.g. `x.f` is a "field projection", and `T::Item` is an ["associated type projection"](../traits/goals-and-clauses.md#trait-ref).
<span id="pc">promoted constants</span>        |  Constants extracted from a function and lifted to static scope; see [this section](../mir/index.md#promoted) for more details.
<span id="provider">provider</span>            |  The function that executes a query. ([see more](../query.md))
<span id="quantified">quantified</span>        |  In math or logic, existential and universal quantification are used to ask questions like "is there any type T for which is true?" or "is this true for all types T?"; see [the background chapter for more](./background.md#quantified).
<span id="query">query</span>                  |  A sub-computation during compilation. Query results can be cached in the current session or to disk for incremental compilation. ([see more](../query.md))
<span id="recovery">recovery</span>            |  Recovery refers to handling invalid syntax during parsing (e.g. a missing comma) and continuing to parse the AST. This avoid showing spurious errors to the user (e.g. showing 'missing field' errors when the struct definition contains errors).
<span id="region">region</span>                |  Another term for "lifetime" often used in the literature and in the borrow checker.
<span id="rib">rib</span>                      |  A data structure in the name resolver that keeps track of a single scope for names. ([see more](../name-resolution.md))
<span id="rpit">RPIT</span>                    |  Short for _return-position `impl Trait`_. An existential `impl Trait` (as opposed to universial) like [TAITs](#tait) and [ATPIT](#atpit). ([see the reference](https://doc.rust-lang.org/reference/types/impl-trait.html#abstract-return-types)).
<span id="rpitit">RPITIT</span>                |  Short for _return-position `impl Trait` in trait_. Unlike [RPIT](#rpit), this is desugared to a generic associated type ([GAT](#gat)). Introduced in [RFC 3425]. ([see more](../return-position-impl-trait-in-trait.md))
<span id="rustbuild">rustbuild 👎</span>          |  A **deprecated** term for the part of bootstrap that is written in Rust
<span id="scrutinee">scrutinee</span>          |  A scrutinee is the expression that is matched on in `match` expressions and similar pattern matching constructs. For example, in `match x { A => 1, B => 2 }`, the expression `x` is the scrutinee.
<span id="sess">`sess`</span>                  |  The compiler _session_, which stores global data used throughout compilation
<span id="side-tables">side tables</span>      |  Because the [AST](#ast) and HIR are immutable once created, we often carry extra information about them in the form of hashtables, indexed by the id of a particular node.
<span id="sigil">sigil</span>                  |  Like a keyword but composed entirely of non-alphanumeric tokens. For example, `&` is a sigil for references.
<span id="soundness">soundness</span>          |  A technical term in type theory. Roughly, if a type system is sound, then a program that type-checks is type-safe. That is, one can never (in safe rust) force a value into a variable of the wrong type. (see "completeness").
<span id="span">span</span>                    |  A location in the user's source code, used for error reporting primarily. These are like a file-name/line-number/column tuple on steroids: they carry a start/end point, and also track macro expansions and compiler desugaring. All while being packed into a few bytes (really, it's an index into a table). See the [`Span`] datatype for more.
<span id="subst">subst 👎</span>               |  The act of _substituting_ the generic parameters inside of a type, constant expression, etc. with concrete generic arguments by supplying [substs](#substs). Nowadays referred to as _instantiating_ in the compiler.
<span id="substs">substs 👎</span>             |  The _substitutions_ for a given generic item (e.g. the `i32`, `u32` in `HashMap<i32, u32>`). Nowadays referred to as the list of _generic arguments_ in the compiler (but note that strictly speaking these two concepts differ, see the literature).
<span id="sysroot">sysroot</span>              |  The directory for build artifacts that are loaded by the compiler at runtime. ([see more](../building/bootstrapping/what-bootstrapping-does.html#what-is-a-sysroot))
<span id="tag">tag</span>                      |  The "tag" of an enum/generator encodes the [discriminant](#discriminant) of the active variant/state.  Tags can either be "direct" (simply storing the discriminant in a field) or use a ["niche"](#niche).
<span id="tait">TAIT</span>                    |  Short for _type-alias `impl Trait`_. Introduced in [RFC 2515].
<span id="tcx">`tcx`</span>                    |  Standard variable name for the "typing context" (`TyCtxt`), main data structure of the compiler. ([see more](../ty.md))
<span id="lifetime-tcx">`'tcx`</span>          |  The lifetime of the allocation arenas used by `TyCtxt`. Most data interned during a compilation session will use this lifetime with the exception of HIR data which uses the `'hir` lifetime. ([see more](../ty.md))
<span id="token">token</span>                  |  The smallest unit of parsing. Tokens are produced after lexing ([see more](../the-parser.md)).
<span id="tls">[TLS]</span>                    |  _Thread-local storage_. Variables may be defined so that each thread has its own copy (rather than all threads sharing the variable). This has some interactions with LLVM. Not all platforms support TLS.
<span id="trait-ref">trait reference, trait ref </span> |  The name of a trait along with a suitable list of generic arguments. ([see more](../traits/goals-and-clauses.md#trait-ref))
<span id="trans">trans 👎</span>                  |  Short for _translation_, the code to translate MIR into LLVM IR. **Renamed to** [codegen](#codegen).
<span id="ty">`Ty`</span>                      |  The internal representation of a type. ([see more](../ty.md))
<span id="tyctxt">`TyCtxt`</span>              |  The data structure often referred to as [`tcx`](#tcx) in code which provides access to session data and the query system.
<span id="ufcs">UFCS 👎</span>                 |  Short for _universal function call syntax_, this is an unambiguous syntax for calling a method. **Term no longer in use!** Prefer _fully-qualified path / syntax_. ([see more](../hir-typeck/summary.md), [see the reference](https://doc.rust-lang.org/reference/expressions/call-expr.html#disambiguating-function-calls))
<span id="ut">uninhabited type</span>          |  A type which has _no_ values. This is not the same as a ZST, which has exactly 1 value. An example of an uninhabited type is `enum Foo {}`, which has no variants, and so, can never be created. The compiler can treat code that deals with uninhabited types as dead code, since there is no such value to be manipulated. `!` (the never type) is an uninhabited type. Uninhabited types are also called _empty types_.
<span id="upvar">upvar</span>                  |  A variable captured by a closure from outside the closure.
<span id="variance">variance</span>            |  Determines how changes to a generic parameter affect subtyping; for example, if `T` is a subtype of `U`, then `Vec<T>` is a subtype `Vec<U>` because `Vec` is _covariant_ in its generic parameter. See [the background chapter](./background.md#variance) for a more general explanation. See the [variance chapter](../variance.md) for an explanation of how type checking handles variance.
<span id="variant-idx">variant index</span>    |  In an enum, identifies a variant by assigning them indices starting at 0. This is purely internal and not to be confused with the ["discriminant"](#discriminant) which can be overwritten by the user (e.g. `enum Bool { True = 42, False = 0 }`).
<span id="wf">well-formedness, wfness, wf</span> |  Semantically: An expression that evaluates to meaningful result. In type systems: A type related construct which follows rules of the type system.
<span id="wide-ptr">wide pointer</span>        |  A pointer with additional metadata. See [fat pointer](#fat-ptr) for more.
<span id="zst">ZST</span>                      |  *Zero-sized type*. A type whose values have size 0 bytes. Since `2^0 = 1`, such types can have exactly one value. For example, `()` (unit) is a ZST. `struct Foo;` is also a ZST. The compiler can do some nice optimizations around ZSTs.

See also <https://doc.rust-lang.org/reference/glossary.html#glossary>.

[LLVM]: https://llvm.org/
[RFC 1598]: https://rust-lang.github.io/rfcs/1598-generic_associated_types.html
[RFC 2515]: https://rust-lang.github.io/rfcs/2515-type_alias_impl_trait.html
[RFC 3425]: https://rust-lang.github.io/rfcs/3425-return-position-impl-trait-in-traits.html
[TLS]: https://llvm.org/docs/LangRef.html#thread-local-storage-models
[`AliasTy`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.AliasTy.html
[`Span`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html
[`generic_const_items`]: https://github.com/rust-lang/rust/issues/113521
[`min_generic_const_items`]: https://github.com/rust-lang/rust/issues/132980
[`rustc_middle::ty`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/index.html
[lto]: https://llvm.org/docs/LinkTimeOptimization.html
[size-align]: https://doc.rust-lang.org/reference/type-layout.html#size-and-alignment
[thinlto]: https://clang.llvm.org/docs/ThinLTO.html


---

# Code Index

rustc has a lot of important data structures.
This is an attempt to give some guidance on where to learn more
about some of the key data structures of the compiler.

Item            |  Kind    | Short description           | Chapter            | Declaration
----------------|----------|-----------------------------|--------------------|-------------------
`BodyId` | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | [compiler/rustc_hir/src/hir.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.BodyId.html)
`Compiler` | struct | Represents a compiler session and can be used to drive a compilation. | [The Rustc Driver and Interface] | [compiler/rustc_interface/src/interface.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/struct.Compiler.html)
`ast::Crate` | struct | A syntax-level representation of a parsed crate | [The parser] | [compiler/rustc_ast/src/ast.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/struct.Crate.html)
`hir::Crate` | struct | A more abstract, compiler-friendly form of a crate's AST | [The Hir] | [compiler/rustc_middle/src/hir/mod.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/hir/struct.Crate.html)
`DefId` | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | [compiler/rustc_hir/src/def_id.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html)
`Diag` | struct | A struct for a compiler diagnostic, such as an error or lint | [Emitting Diagnostics] | [compiler/rustc_errors/src/diagnostic.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html)
`DocContext` | struct | A state container used by rustdoc when crawling through a crate to gather its documentation | [Rustdoc] | [src/librustdoc/core.rs](https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/core.rs)
`HirId` | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | [compiler/rustc_hir_id/src/lib.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/struct.HirId.html)
`Lexer` | struct | This is the lexer used during parsing. It consumes characters from the raw source code being compiled and produces a series of tokens for use by the rest of the parser | [The parser] |  [compiler/rustc_parse/src/lexer/mod.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/lexer/struct.Lexer.html)
`NodeId` | struct | One of four types of HIR node identifiers. Being phased out | [Identifiers in the HIR] | [compiler/rustc_ast/src/ast.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/node_id/struct.NodeId.html)
`ParamEnv` | struct | Information about generic parameters or `Self`, useful for working with associated or generic items | [Parameter Environment] | [compiler/rustc_middle/src/ty/mod.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.ParamEnv.html)
`ParseSess` | struct | This struct contains information about a parsing session | [The parser] | [compiler/rustc_session/src/parse/parse.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.ParseSess.html)
`Rib` | struct | Represents a single scope of names | [Name resolution] | [compiler/rustc_resolve/src/lib.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/late/struct.Rib.html)
`Session` | struct | The data associated with a compilation session | [The parser], [The Rustc Driver and Interface] | [compiler/rustc_session/src/session.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/struct.Session.html)
`SourceFile` | struct | Part of the `SourceMap`. Maps AST nodes to their source code for a single source file. Was previously called FileMap | [The parser] | [compiler/rustc_span/src/lib.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.SourceFile.html)
`SourceMap` | struct | Maps AST nodes to their source code. It is composed of `SourceFile`s. Was previously called CodeMap | [The parser] | [compiler/rustc_span/src/source_map.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/source_map/struct.SourceMap.html)
`Span` | struct  | A location in the user's source code, used for error reporting primarily | [Emitting Diagnostics] | [compiler/rustc_span/src/span_encoding.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html)
`rustc_ast::token_stream::TokenStream` | struct | An abstract sequence of tokens, organized into `TokenTree`s | [The parser], [Macro expansion] | [compiler/rustc_ast/src/tokenstream.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/tokenstream/struct.TokenStream.html)
`TraitDef` | struct | This struct contains a trait's definition with type information | [The `ty` modules] |  [compiler/rustc_middle/src/ty/trait_def.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/trait_def/struct.TraitDef.html)
`TraitRef` | struct | The combination of a trait and its input types (e.g. `P0: Trait<P1...Pn>`) | [Trait Solving: Goals and Clauses]  |  [compiler/rustc_middle/src/ty/sty.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TraitRef.html)
`Ty<'tcx>` | struct | This is the internal representation of a type used for type checking | [Type checking] | [compiler/rustc_middle/src/ty/mod.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html)
`TyCtxt<'tcx>` | struct | The "typing context". This is the central data structure in the compiler. It is the context that you use to perform all manner of queries | [The `ty` modules] | [compiler/rustc_middle/src/ty/context.rs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html)

[The HIR]: ../hir.html
[Identifiers in the HIR]: ../hir.html#hir-id
[The parser]: ../the-parser.html
[The Rustc Driver and Interface]: ../rustc-driver/intro.html
[Type checking]: ../hir-typeck/summary.html
[The `ty` modules]: ../ty.html
[Rustdoc]: ../rustdoc.html
[Emitting Diagnostics]: ../diagnostics.html
[Macro expansion]: ../macro-expansion.html
[Name resolution]: ../name-resolution.html
[Parameter Environment]: ../typing-parameter-envs.html
[Trait Solving: Goals and Clauses]: ../traits/goals-and-clauses.html#domain-goals


---

# Compiler Lecture Series

These are videos where various experts explain different parts of the compiler:

## General
- [January 2019: Tom Tromey discusses debugging support in rustc](https://www.youtube.com/watch?v=elBxMRSNYr4)
- [June 2019: Responsive compilers - Nicholas Matsakis - PLISS 2019](https://www.youtube.com/watch?v=N6b44kMS6OM)
- [June 2019: Things I Learned (TIL) - Nicholas Matsakis - PLISS 2019](https://www.youtube.com/watch?v=LIYkT3p5gTs)
- [October 2022: Rustc Explore](https://www.youtube.com/playlist?list=PL85XCvVPmGQj3-MujOJ0jcoSqQ6Yi6Rkk)

## Rust Analyzer
- [January 2019: How Salsa Works](https://www.youtube.com/watch?v=_muY4HjSqVw)
- [January 2019: Salsa In More Depth](https://www.youtube.com/watch?v=i_IhACacPRY)
- [January 2019: Rust analyzer guide](https://www.youtube.com/watch?v=ANKBNiSWyfc)
- [February 2019: Rust analyzer syntax trees](https://www.youtube.com/watch?v=DGAuLWdCCAI)
- [March 2019: rust-analyzer type-checker overview by flodiebold](https://www.youtube.com/watch?v=Lmp3P9WNL8o)
- [March 2019: RLS 2.0, Salsa, and Name Resolution](https://www.youtube.com/watch?v=Xr-rBqLr-G4)

## Type System
- [July 2015: Felix Klock - Rust: A type system you didn't know you wanted - Curry On](https://www.youtube.com/watch?v=Q7lQCgnNWU0)
- [November 2016: Felix Klock - Subtyping in Rust and Clarke's Third Law](https://www.youtube.com/watch?v=fI4RG_uq-WU)
- [February 2019: Universes and Lifetimes](https://www.youtube.com/watch?v=iV1Z0xYXkck)
- [April 2019: Representing types in rustc](https://www.youtube.com/watch?v=c01TsOsr3-c)
- [March 2019: RFC #2229 Disjoint Field Capture plan](https://www.youtube.com/watch?v=UTXOptVMuIc)

## Closures
- [October 2018: closures and upvar capture](https://www.youtube.com/watch?v=fMopdkn5-Xw)
- [October 2018: blitzerr closure upvar tys](https://www.youtube.com/watch?v=pLmVhSB-z4s)
- [January 2019: Convert Closure Upvar Representation to Tuples with blitzerr](https://www.youtube.com/watch?v=2QCuNtISoYc)

## Chalk
- [July 2018: Coherence in Chalk by Sunjay Varma - Bay Area Rust Meetup](https://www.youtube.com/watch?v=rZqS4bLPL24)
- [March 2019: rustc-chalk integration overview](https://www.youtube.com/watch?v=MBWtbDifPeU)
- [April 2019: How the chalk-engine crate works](https://www.youtube.com/watch?v=Ny2928cGDoM)
- [May 2019: How the chalk-engine crate works 2](https://www.youtube.com/watch?v=hmV66tB79LM)

## Polonius
- [March 2019: Polonius-rustc walkthrough](https://www.youtube.com/watch?v=i5KdU0ieb_A)
- [May 2019: Polonius WG: Initialization and move tracking](https://www.youtube.com/watch?v=ilv9V-328HI)

## Miri
- [March 2019: oli-obk on miri and constant evaluation](https://www.youtube.com/watch?v=5Pm2C1YXrvM)

## Async
- [February 2019: async-await implementation plans](https://www.youtube.com/watch?v=xe2_whJWBC0)
- [April 2019: async-await region inferencer](https://www.youtube.com/watch?v=hlOxfkUDLPQ)

## Code Generation
- [January 2019: Cranelift](https://www.youtube.com/watch?v=9OIA7DTFQWU)
- [December 2024: LLVM Developers' Meeting - Rust ❤️ LLVM](https://www.youtube.com/watch?v=Kqz-umsAnk8)


---

# Rust Bibliography

This is a reading list of material relevant to Rust.
It includes prior research that has - at one time or another - influenced the design of
Rust, as well as publications about Rust.

## Type system

* [Alias burying](https://dl.acm.org/doi/10.1002/spe.370) - We tried something similar and abandoned it.
* [External uniqueness is unique enough](https://lirias.kuleuven.be/retrieve/35835)
* [Macros that work together](https://www.cs.utah.edu/plt/publications/jfp12-draft-fcdf.pdf)
* [Making ad-hoc polymorphism less ad hoc](https://dl.acm.org/doi/10.1145/75277.75283)
* [Region based memory management in Cyclone](https://www.cs.umd.edu/projects/cyclone/papers/cyclone-regions.pdf)
* [Region Based Memory Management](https://www.cs.ucla.edu/~palsberg/tba/papers/tofte-talpin-iandc97.pdf)
* [Safe manual memory management in Cyclone](https://www.cs.umd.edu/projects/PL/cyclone/scp.pdf)
* [Skolem Normal Form](https://en.wikipedia.org/wiki/Skolem_normal_form)
* [Traits: composable units of behavior](http://scg.unibe.ch/archive/papers/Scha03aTraits.pdf)
* [Uniqueness and Reference Immutability for Safe Parallelism](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/msr-tr-2012-79.pdf)

## Concurrency

* [A Java fork/join calamity](https://web.archive.org/web/20190904045322/http://www.coopsoft.com/ar/CalamityArticle.html) - critique of Java's fork/join library, particularly its application of work stealing to non-strict computation
* [Algorithms for scalable synchronization of shared-memory multiprocessors](https://www.cs.rochester.edu/u/scott/papers/1991_TOCS_synch.pdf)
* [Balanced work stealing for time-sharing multicores](https://web.njit.edu/~dingxn/papers/BWS.pdf)
* [Contention aware scheduling](https://www.blagodurov.net/files/a8-blagodurov.pdf)
* [Dynamic circular work stealing deque](https://patents.google.com/patent/US7346753B2/en) - The Chase/Lev deque
* [Epoch-based reclamation](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-579.pdf).
* [Language support for fast and reliable message-based communication in singularity OS](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/04/singsharp.pdf)
* [Non-blocking steal-half work queues](https://www.cs.bgu.ac.il/%7Ehendlerd/papers/p280-hendler.pdf)
* [Reagents: expressing and composing fine-grained concurrency](https://aturon.github.io/academic/reagents.pdf)
* [Scheduling multithreaded computations by work stealing](https://www.lri.fr/~cecile/ENSEIGNEMENT/IPAR/Exposes/cilk1.pdf)
* [Scheduling techniques for concurrent systems](https://www.stanford.edu/~ouster/cgi-bin/papers/coscheduling.pdf)
* [Singularity: rethinking the software stack](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/osr2007_rethinkingsoftwarestack.pdf)
* [The data locality of work stealing](http://www.aladdin.cs.cmu.edu/papers/pdfs/y2000/locality_spaa00.pdf)
* [Thread scheduling for multiprogramming multiprocessors](https://dl.acm.org/doi/10.1145/277651.277678)
* [Three layer cake for shared-memory programming](https://dl.acm.org/doi/10.1145/1953611.1953616)
* [Work-first and help-first scheduling policies for async-finish task parallelism](https://dl.acm.org/doi/10.1109/IPDPS.2009.5161079) - More general than fully-strict work stealing

## Others

* [Composing High-Performance Memory Allocators](https://people.cs.umass.edu/~emery/pubs/berger-pldi2001.pdf)
* [Crash-only software](https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea.pdf)
* [Reconsidering Custom Memory Allocation](https://people.cs.umass.edu/~emery/pubs/berger-oopsla2002.pdf)

## Papers *about* Rust

* [GPU Programming in Rust: Implementing High Level Abstractions in a Systems Level
  Language](https://ieeexplore.ieee.org/document/6650903).
  Early GPU work by Eric Holk.
* [Parallel closures: a new twist on an old
  idea](https://www.usenix.org/conference/hotpar12/parallel-closures-new-twist-old-idea)
  - not exactly about Rust, but by nmatsakis
* [Patina: A Formalization of the Rust Programming
  Language](https://dada.cs.washington.edu/research/tr/2015/03/UW-CSE-15-03-02.pdf).
  Early formalization of a subset of the type system, by Eric Reed.
* [Experience Report: Developing the Servo Web Browser Engine using
  Rust](https://arxiv.org/abs/1505.07383).
  By Lars Bergstrom.
* [Implementing a Generic Radix Trie in
  Rust](https://michaelsproul.github.io/rust_radix_paper/rust-radix-sproul.pdf).
  Undergrad paper by Michael Sproul.
* [Reenix: Implementing a Unix-Like Operating System in
  Rust](https://scialex.github.io/reenix.pdf).
  Undergrad paper by Alex Light.
* [Evaluation of performance and productivity metrics of potential programming languages in the HPC environment](https://github.com/1wilkens/thesis-ba).
  Bachelor's thesis by Florian Wilkens.
  Compares C, Go and Rust.
* [Nom, a byte oriented, streaming, zero copy, parser combinators library
  in Rust](http://spw15.langsec.org/papers/couprie-nom.pdf).
  By Geoffroy Couprie, research for VLC.
* [Graph-Based Higher-Order Intermediate
  Representation](https://compilers.cs.uni-saarland.de/papers/lkh15_cgo.pdf).
  An experimental IR implemented in Impala, a Rust-like language.
* [Code Refinement of Stencil Codes](https://compilers.cs.uni-saarland.de/papers/ppl14_web.pdf).
  Another paper using Impala.
* [Parallelization in Rust with fork-join and
  friends](http://publications.lib.chalmers.se/records/fulltext/219016/219016.pdf).
  Linus Farnstrand's master's thesis.
* [Session Types for Rust](https://munksgaard.me/papers/laumann-munksgaard-larsen.pdf).
  Philip Munksgaard's master's thesis.
  Research for Servo.
* [Ownership is Theft: Experiences Building an Embedded OS in Rust - Amit Levy, et. al.](https://amitlevy.com/papers/tock-plos2015.pdf)
* [You can't spell trust without Rust](https://faultlore.com/blah/papers/thesis.pdf).
  Aria Beingessner's master's thesis.
* [Rust-Bio: a fast and safe bioinformatics library](https://rust-bio.github.io/).
  Johannes Köster
* [Safe, Correct, and Fast Low-Level Networking](https://csperkins.org/research/thesis-msci-clipsham.pdf).
  Robert Clipsham's master's thesis.
* [Formalizing Rust traits](https://open.library.ubc.ca/cIRcle/collections/ubctheses/24/items/1.0220521).
  Jonatan Milewski's master's thesis.
* [Rust as a Language for High Performance GC Implementation](https://dl.acm.org/doi/pdf/10.1145/3241624.2926707)
* [Simple Verification of Rust Programs via Functional Purification](https://github.com/Kha/electrolysis).
  Sebastian Ullrich's master's thesis.
* [Writing parsers like it is 2017](http://spw17.langsec.org/papers/chifflier-parsing-in-2017.pdf) Pierre Chifflier and Geoffroy Couprie for the Langsec Workshop
* [The Case for Writing a Kernel in Rust](https://www.tockos.org/assets/papers/rust-kernel-apsys2017.pdf)
* [RustBelt: Securing the Foundations of the Rust Programming Language](https://plv.mpi-sws.org/rustbelt/popl18/)
* [Oxide: The Essence of Rust](https://arxiv.org/abs/1903.00982).
  By Aaron Weiss, Olek Gierczak, Daniel Patterson, Nicholas D.
  Matsakis, and Amal Ahmed.


---

# Humor in Rust

What's a project without a sense of humor? And frankly some of these are
enlightening?

- [Weird exprs test](https://github.com/rust-lang/rust/blob/HEAD/tests/ui/expr/weird-exprs.rs)
- [Ferris Rap](https://fitzgen.com/2018/12/13/rust-raps.html)
- [The Genesis of Generic Germination](https://github.com/rust-lang/rust/pull/53645#issue-210543221)
- [The Bastion of the Turbofish test](https://github.com/rust-lang/rust/blob/79d8a0fcefa5134db2a94739b1d18daa01fc6e9f/src/test/ui/bastion-of-the-turbofish.rs)
- [Rust Koans](https://users.rust-lang.org/t/rust-koans/2408)
- [`break rust;`](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=0ab2bd6a9d722e0f05a95e2a5dcf89cc)
- [The Nomicon Intro](https://doc.rust-lang.org/stable/nomicon/)
- [`rustc-ty` renaming punfest](https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler/topic/rustc-ty.20naming.20bikeshed.20.2F.20punfest.20%28was.3A.20design.20meeting.202.2E.2E.2E/near/189906455)
- [try using their name "ferris" instead](https://github.com/rust-lang/rust/pull/91476)
- [Forbid pineapple on pizza](https://github.com/rust-lang/rust/pull/70645)
