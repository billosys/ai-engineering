# Dataflow Analysis

If you work on the MIR, you will frequently come across various flavors of
[dataflow analysis][wiki]. `rustc` uses dataflow to find uninitialized
variables, determine what variables are live across a generator `yield`
statement, and compute which `Place`s are borrowed at a given point in the
control-flow graph. Dataflow analysis is a fundamental concept in modern
compilers, and knowledge of the subject will be helpful to prospective
contributors.

However, this documentation is not a general introduction to dataflow analysis.
It is merely a description of the framework used to define these analyses in
`rustc`. It assumes that the reader is familiar with the core ideas as well as
some basic terminology, such as "transfer function", "fixpoint" and "lattice".
If you're unfamiliar with these terms, or if you want a quick refresher,
[*Static Program Analysis*] by Anders Møller and Michael I. Schwartzbach is an
excellent, freely available textbook. For those who prefer audiovisual
learning, we previously recommended a series of short lectures
by the Goethe University Frankfurt on YouTube, but it has since been deleted.
See [this PR][pr-1295] for the context and [this comment][pr-1295-comment]
for the alternative lectures.

## Defining a Dataflow Analysis

A dataflow analysis is defined by the [`Analysis`] trait. In addition to the
type of the dataflow state, this trait defines the initial value of that state
at entry to each block, as well as the direction of the analysis, either
forward or backward. The domain of your dataflow analysis must be a [lattice][]
(strictly speaking a join-semilattice) with a well-behaved `join` operator. See
documentation for the [`lattice`] module, as well as the [`JoinSemiLattice`]
trait, for more information.

### Transfer Functions and Effects

The dataflow framework in `rustc` allows each statement (and terminator) inside
a basic block to define its own transfer function. For brevity, these
individual transfer functions are known as "effects". Each effect is applied
successively in dataflow order, and together they define the transfer function
for the entire basic block. It's also possible to define an effect for
particular outgoing edges of some terminators (e.g.
[`apply_call_return_effect`] for the `success` edge of a `Call`
terminator). Collectively, these are referred to as "per-edge effects".

### "Before" Effects

Observant readers of the documentation may notice that there are actually *two*
possible effects for each statement and terminator, the "before" effect and the
unprefixed (or "primary") effect. The "before" effects are applied immediately
before the unprefixed effect **regardless of the direction of the analysis**.
In other words, a backward analysis will apply the "before" effect and then the
"primary" effect when computing the transfer function for a basic block, just
like a forward analysis.

The vast majority of analyses should use only the unprefixed effects: Having
multiple effects for each statement makes it difficult for consumers to know
where they should be looking. However, the "before" variants can be useful in
some scenarios, such as when the effect of the right-hand side of an assignment
statement must be considered separately from the left-hand side.

### Convergence

Your analysis must converge to "fixpoint", otherwise it will run forever.
Converging to fixpoint is just another way of saying "reaching equilibrium".
In order to reach equilibrium, your analysis must obey some laws. One of the
laws it must obey is that the bottom value[^bottom-purpose] joined with some
other value equals the second value. Or, as an equation:

> *bottom* join *x* = *x*

Another law is that your analysis must have a "top value" such that

> *top* join *x* = *top*

Having a top value ensures that your semilattice has a finite height, and the
law state above ensures that once the dataflow state reaches top, it will no
longer change (the fixpoint will be top).

[^bottom-purpose]: The bottom value's primary purpose is as the initial dataflow
    state. Each basic block's entry state is initialized to bottom before the
    analysis starts.

## A Brief Example

This section provides a brief example of a simple data-flow analysis at a high
level. It doesn't explain everything you need to know, but hopefully it will
make the rest of this page clearer.

Let's say we want to do a simple analysis to find if `mem::transmute` may have
been called by a certain point in the program. Our analysis domain will just
be a `bool` that records whether `transmute` has been called so far. The bottom
value will be `false`, since by default `transmute` has not been called. The top
value will be `true`, since our analysis is done as soon as we determine that
`transmute` has been called. Our join operator will just be the boolean OR (`||`)
operator. We use OR and not AND because of this case:

```rust
# unsafe fn example(some_cond: bool) {
let x = if some_cond {
    std::mem::transmute::<i32, u32>(0_i32) // transmute was called!
} else {
    1_u32 // transmute was not called
};

// Has transmute been called by this point? We conservatively approximate that
// as yes, and that is why we use the OR operator.
println!("x: {}", x);
# }
```

## Inspecting the Results of a Dataflow Analysis

Once you have constructed an analysis, you must call `iterate_to_fixpoint`
which will return a `Results`, which contains the dataflow state at fixpoint
upon entry of each block. Once you have a `Results`, you can inspect the
dataflow state at fixpoint at any point in the CFG. If you only need the state
at a few locations (e.g., each `Drop` terminator) use a [`ResultsCursor`]. If
you need the state at *every* location, a [`ResultsVisitor`] will be more
efficient.

```text
                         Analysis
                            |
                            | iterate_to_fixpoint()
                            |
                         Results
                         /     \
 into_results_cursor(…) /       \  visit_with(…)
                       /         \
               ResultsCursor  ResultsVisitor
```

For example, the following code uses a [`ResultsVisitor`]...


```rust,ignore
// Assuming `MyVisitor` implements `ResultsVisitor<FlowState = MyAnalysis::Domain>`...
let mut my_visitor = MyVisitor::new();

// inspect the fixpoint state for every location within every block in RPO.
let results = MyAnalysis::new()
    .iterate_to_fixpoint(tcx, body, None);
results.visit_with(body, &mut my_visitor);`
```

whereas this code uses [`ResultsCursor`]:

```rust,ignore
let mut results = MyAnalysis::new()
    .iterate_to_fixpoint(tcx, body, None);
    .into_results_cursor(body);

// Inspect the fixpoint state immediately before each `Drop` terminator.
for (bb, block) in body.basic_blocks().iter_enumerated() {
    if let TerminatorKind::Drop { .. } = block.terminator().kind {
        results.seek_before_primary_effect(body.terminator_loc(bb));
        let state = results.get();
        println!("state before drop: {:#?}", state);
    }
}
```

### Graphviz Diagrams

When the results of a dataflow analysis are not what you expect, it often helps
to visualize them. This can be done with the `-Z dump-mir` flags described in
[Debugging MIR]. Start with `-Z dump-mir=F -Z dump-mir-dataflow`, where `F` is
either "all" or the name of the MIR body you are interested in.

These `.dot` files will be saved in your `mir_dump` directory and will have the
[`NAME`] of the analysis (e.g. `maybe_inits`) as part of their filename. Each
visualization will display the full dataflow state at entry and exit of each
block, as well as any changes that occur in each statement and terminator.  See
the example below:

![A graphviz diagram for a dataflow analysis](../img/dataflow-graphviz-example.png)

["gen-kill" problems]: https://en.wikipedia.org/wiki/Data-flow_analysis#Bit_vector_problems
[*Static Program Analysis*]: https://cs.au.dk/~amoeller/spa/
[Debugging MIR]: ./debugging.md
[`Analysis`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.Analysis.html
[`GenKillAnalysis`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.GenKillAnalysis.html
[`JoinSemiLattice`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/lattice/trait.JoinSemiLattice.html
[`NAME`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.Analysis.html#associatedconstant.NAME
[`ResultsCursor`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/struct.ResultsCursor.html
[`ResultsVisitor`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.ResultsVisitor.html
[`apply_call_return_effect`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.Analysis.html#tymethod.apply_call_return_effect
[`into_engine`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/trait.Analysis.html#method.into_engine
[`lattice`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/lattice/index.html
[pr-1295]: https://github.com/rust-lang/rustc-dev-guide/pull/1295
[pr-1295-comment]: https://github.com/rust-lang/rustc-dev-guide/pull/1295#issuecomment-1118131294
[lattice]: https://en.wikipedia.org/wiki/Lattice_(order)
[wiki]: https://en.wikipedia.org/wiki/Data-flow_analysis#Basic_principles


---

# Drop elaboration

## Dynamic drops

According to the [reference][reference-drop]:

> When an initialized variable or temporary goes out of scope, its destructor
> is run, or it is dropped. Assignment also runs the destructor of its
> left-hand operand, if it's initialized. If a variable has been partially
> initialized, only its initialized fields are dropped.

When building the MIR, the `Drop` and `DropAndReplace` terminators represent
places where drops may occur. However, in this phase, the presence of these
terminators does not guarantee that a destructor will run. That's because the
target of a drop may be uninitialized (usually because it has been moved from)
before the terminator is reached. In general, we cannot know at compile-time whether a
variable is initialized.

```rust
let mut y = vec![];

{
    let x = vec![1, 2, 3];
    if std::process::id() % 2 == 0 {
        y = x; // conditionally move `x` into `y`
    }
} // `x` goes out of scope here. Should it be dropped?
```

In these cases, we need to keep track of whether a variable is initialized
*dynamically*. The rules are laid out in detail in [RFC 320: Non-zeroing
dynamic drops][RFC 320].

## Drop obligations

From the RFC:

> When a local variable becomes initialized, it establishes a set of "drop
> obligations": a set of structural paths (e.g. a local `a`, or a path to a
> field `b.f.y`) that need to be dropped.
>
> The drop obligations for a local variable x of struct-type `T` are computed
> from analyzing the structure of `T`. If `T` itself implements `Drop`, then `x` is a
> drop obligation. If `T` does not implement `Drop`, then the set of drop
> obligations is the union of the drop obligations of the fields of `T`.

When a structural path is moved from (and thus becomes uninitialized), any drop
obligations for that path or its descendants (`path.f`, `path.f.g.h`, etc.) are
released. Types with `Drop` implementations do not permit moves from individual
fields, so there is no need to track initializedness through them.

When a local variable goes out of scope (`Drop`), or when a structural path is
overwritten via assignment (`DropAndReplace`), we check for any drop
obligations for that variable or path.  Unless that obligation has been
released by this point, its associated `Drop` implementation will be called.
For `enum` types, only fields corresponding to the "active" variant need to be
dropped. When processing drop obligations for such types, we first check the
discriminant to determine the active variant. All drop obligations for variants
besides the active one are ignored.

Here are a few interesting types to help illustrate these rules:

```rust
struct NoDrop(u8); // No `Drop` impl. No fields with `Drop` impls.

struct NeedsDrop(Vec<u8>); // No `Drop` impl but has fields with `Drop` impls.

struct ThinVec(*const u8); // Custom `Drop` impl. Individual fields cannot be moved from.

impl Drop for ThinVec {
    fn drop(&mut self) { /* ... */ }
}

enum MaybeDrop {
    Yes(NeedsDrop),
    No(NoDrop),
}
```

## Drop elaboration

One valid model for these rules is to keep a boolean flag (a "drop flag") for
every structural path that is used at any point in the function. This flag is
set when its path is initialized and is cleared when the path is moved from.
When a `Drop` occurs, we check the flags for every obligation associated with
the target of the `Drop` and call the associated `Drop` impl for those that are
still applicable.

This process—transforming the newly built MIR with its imprecise `Drop` and
`DropAndReplace` terminators into one with drop flags—is known as drop
elaboration. When a MIR statement causes a variable to become initialized (or
uninitialized), drop elaboration inserts code that sets (or clears) the drop
flag for that variable. It wraps `Drop` terminators in conditionals that check
the newly inserted drop flags.

Drop elaboration also splits `DropAndReplace` terminators into a `Drop` of the
target and a write of the newly dropped place. This is somewhat unrelated to what
we've discussed above.

Once this is complete, `Drop` terminators in the MIR correspond to a call to
the "drop glue" or "drop shim" for the type of the dropped place. The drop
glue for a type calls the `Drop` impl for that type (if one exists), and then
recursively calls the drop glue for all fields of that type.

## Drop elaboration in `rustc`

The approach described above is more expensive than necessary. One can imagine
a few optimizations:

- Only paths that are the target of a `Drop` (or have the target as a prefix)
  need drop flags.
- Some variables are known to be initialized (or uninitialized) when they are
  dropped. These do not need drop flags.
- If a set of paths are only dropped or moved from via a shared prefix, those
  paths can share a single drop flag.

A subset of these are implemented in `rustc`.

In the compiler, drop elaboration is split across several modules. The pass
itself is defined [here][drops-transform], but the [main logic][drops] is
defined elsewhere since it is also used to build [drop shims][drops-shim].

Drop elaboration designates each `Drop` in the newly built MIR as one of four
kinds:

- `Static`, the target is always initialized.
- `Dead`, the target is always **un**initialized.
- `Conditional`, the target is either wholly initialized or wholly
  uninitialized. It is not partly initialized.
- `Open`, the target may be partly initialized.

For this, it uses a pair of dataflow analyses, `MaybeInitializedPlaces` and
`MaybeUninitializedPlaces`. If a place is in one but not the other, then the
initializedness of the target is known at compile-time (`Dead` or `Static`).
In this case, drop elaboration does not add a flag for the target. It simply
removes (`Dead`) or preserves (`Static`) the `Drop` terminator.

For `Conditional` drops, we know that the initializedness of the variable as a
whole is the same as the initializedness of its fields. Therefore, once we
generate a drop flag for the target of that drop, it's safe to call the drop
glue for that target.

### `Open` drops

`Open` drops are the most complex, since we need to break down a single `Drop`
terminator into several different ones, one for each field of the target whose
type has drop glue (`Ty::needs_drop`). We cannot call the drop glue for the
target itself because that requires all fields of the target to be initialized.
Remember, variables whose type has a custom `Drop` impl do not allow `Open`
drops because their fields cannot be moved from.

This is accomplished by recursively categorizing each field as `Dead`,
`Static`, `Conditional` or `Open`. Fields whose type does not have drop glue
are automatically `Dead` and need not be considered during the recursion. When
we reach a field whose kind is not `Open`, we handle it as we did above. If the
field is also `Open`, the recursion continues.

It's worth noting how we handle `Open` drops of enums. Inside drop elaboration,
each variant of the enum is treated like a field, with the invariant that only
one of those "variant fields" can be initialized at any given time. In the
general case, we do not know which variant is the active one, so we will have
to call the drop glue for the enum (which checks the discriminant) or check the
discriminant ourselves as part of an elaborated `Open` drop. However, in
certain cases (within a `match` arm, for example) we do know which variant of
an enum is active. This information is encoded in the `MaybeInitializedPlaces`
and `MaybeUninitializedPlaces` dataflow analyses by marking all places
corresponding to inactive variants as uninitialized.

### Cleanup paths

TODO: Discuss drop elaboration and unwinding.

## Aside: drop elaboration and const-eval

In Rust, functions that are eligible for evaluation at compile-time must be
marked explicitly using the `const` keyword. This includes implementations  of
the `Drop` trait, which may or may not be `const`. Code that is eligible for
compile-time evaluation may only call `const` functions, so any calls to
non-const `Drop` implementations in such code must be forbidden.

A call to a `Drop` impl is encoded as a `Drop` terminator in the MIR. However,
as we discussed above, a `Drop` terminator in newly built MIR does not
necessarily result in a call to `Drop::drop`. The drop target may be
uninitialized at that point. This means that checking for non-const `Drop`s on
the newly built MIR can result in spurious errors. Instead, we wait until after
drop elaboration runs, which eliminates `Dead` drops (ones where the target is
known to be uninitialized) to run these checks.

[RFC 320]: https://rust-lang.github.io/rfcs/0320-nonzeroing-dynamic-drop.html
[reference-drop]: https://doc.rust-lang.org/reference/destructors.html
[drops]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_mir_transform/src/elaborate_drops.rs
[drops-shim]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_mir_transform/src/shim.rs
[drops-transform]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_mir_transform/src/elaborate_drops.rs


---

# MIR borrow check

The borrow check is Rust's "secret sauce" – it is tasked with
enforcing a number of properties:

- That all variables are initialized before they are used.
- That you can't move the same value twice.
- That you can't move a value while it is borrowed.
- That you can't access a place while it is mutably borrowed (except through
  the reference).
- That you can't mutate a place while it is immutably borrowed.
- etc

The borrow checker operates on the MIR. An older implementation operated on the
HIR. Doing borrow checking on MIR has several advantages:

- The MIR is *far* less complex than the HIR; the radical desugaring
  helps prevent bugs in the borrow checker. (If you're curious, you
  can see
  [a list of bugs that the MIR-based borrow checker fixes here][47366].)
- Even more importantly, using the MIR enables ["non-lexical lifetimes"][nll],
  which are regions derived from the control-flow graph.

[47366]: https://github.com/rust-lang/rust/issues/47366
[nll]: https://rust-lang.github.io/rfcs/2094-nll.html

### Major phases of the borrow checker

The borrow checker source is found in
[the `rustc_borrowck` crate][b_c]. The main entry point is
the [`mir_borrowck`] query.

[b_c]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/index.html
[`mir_borrowck`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/fn.mir_borrowck.html

- We first create a **local copy** of the MIR. In the coming steps,
  we will modify this copy in place to modify the types and things to
  include references to the new regions that we are computing.
- We then invoke [`replace_regions_in_mir`] to modify our local MIR.
  Among other things, this function will replace all of the [regions](./appendix/glossary.md#region)
  in the MIR with fresh [inference variables](./appendix/glossary.md#inf-var).
- Next, we perform a number of
  [dataflow analyses](./appendix/background.md#dataflow) that
  compute what data is moved and when.
- We then do a [second type check](borrow-check/type-check.md) across the MIR:
  the purpose of this type check is to determine all of the constraints between
  different regions.
- Next, we do [region inference](borrow-check/region-inference.md), which computes
  the values of each region — basically, the points in the control-flow graph where
  each lifetime must be valid according to the constraints we collected.
- At this point, we can compute the "borrows in scope" at each point.
- Finally, we do a second walk over the MIR, looking at the actions it
  does and reporting errors. For example, if we see a statement like
  `*a + 1`, then we would check that the variable `a` is initialized
  and that it is not mutably borrowed, as either of those would
  require an error to be reported. Doing this check requires the results of all
  the previous analyses.

[`replace_regions_in_mir`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/nll/fn.replace_regions_in_mir.html


---

# Tracking moves and initialization

Part of the borrow checker's job is to track which variables are
"initialized" at any given point in time -- this also requires
figuring out where moves occur and tracking those.

## Initialization and moves

From a user's perspective, initialization -- giving a variable some
value -- and moves -- transferring ownership to another place -- might
seem like distinct topics. Indeed, our borrow checker error messages
often talk about them differently. But **within the borrow checker**,
they are not nearly as separate. Roughly speaking, the borrow checker
tracks the set of "initialized places" at any point in the source
code. Assigning to a previously uninitialized local variable adds it
to that set; moving from a local variable removes it from that set.

Consider this example:

```rust,ignore
fn foo() {
    let a: Vec<u32>;

    // a is not initialized yet

    a = vec![22];

    // a is initialized here

    std::mem::drop(a); // a is moved here

    // a is no longer initialized here

    let l = a.len(); //~ ERROR
}
```

Here you can see that `a` starts off as uninitialized; once it is
assigned, it becomes initialized. But when `drop(a)` is called, that
moves `a` into the call, and hence it becomes uninitialized again.

## Subsections

To make it easier to peruse, this section is broken into a number of
subsections:

- [Move paths](./moves-and-initialization/move-paths.md) the
  *move path* concept that we use to track which local variables (or parts of
  local variables, in some cases) are initialized.
- TODO *Rest not yet written* =)


---

# Move paths

In reality, it's not enough to track initialization at the granularity
of local variables. Rust also allows us to do moves and initialization
at the field granularity:

```rust,ignore
fn foo() {
    let a: (Vec<u32>, Vec<u32>) = (vec![22], vec![44]);

    // a.0 and a.1 are both initialized

    let b = a.0; // moves a.0

    // a.0 is not initialized, but a.1 still is

    let c = a.0; // ERROR
    let d = a.1; // OK
}
```

To handle this, we track initialization at the granularity of a **move
path**. A [`MovePath`] represents some location that the user can
initialize, move, etc. So e.g. there is a move-path representing the
local variable `a`, and there is a move-path representing `a.0`.  Move
paths roughly correspond to the concept of a [`Place`] from MIR, but
they are indexed in ways that enable us to do move analysis more
efficiently.

[`MovePath`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePath.html
[`Place`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.Place.html

## Move path indices

Although there is a [`MovePath`] data structure, they are never referenced
directly.  Instead, all the code passes around *indices* of type
[`MovePathIndex`]. If you need to get information about a move path, you use
this index with the [`move_paths` field of the `MoveData`][move_paths]. For
example, to convert a [`MovePathIndex`] `mpi` into a MIR [`Place`], you might
access the [`MovePath::place`] field like so:

```rust,ignore
move_data.move_paths[mpi].place
```

[move_paths]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MoveData.html#structfield.move_paths
[`MovePath::place`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePath.html#structfield.place
[`MovePathIndex`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePathIndex.html

## Building move paths

One of the first things we do in the MIR borrow check is to construct
the set of move paths. This is done as part of the
[`MoveData::gather_moves`] function. This function uses a MIR visitor
called [`MoveDataBuilder`] to walk the MIR and look at how each [`Place`]
within is accessed. For each such [`Place`], it constructs a
corresponding [`MovePathIndex`]. It also records when/where that
particular move path is moved/initialized, but we'll get to that in a
later section.

[`MoveDataBuilder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/builder/struct.MoveDataBuilder.html
[`MoveData::gather_moves`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MoveData.html#method.gather_moves

### Illegal move paths

We don't actually create a move-path for **every** [`Place`] that gets
used.  In particular, if it is illegal to move from a [`Place`], then
there is no need for a [`MovePathIndex`]. Some examples:

- You cannot move an individual element of an array, so if we have e.g. `foo: [String; 3]`,
  there would be no move-path for `foo[1]`.
- You cannot move from inside of a borrowed reference, so if we have e.g. `foo: &String`,
  there would be no move-path for `*foo`.

These rules are enforced by the [`move_path_for`] function, which
converts a [`Place`] into a [`MovePathIndex`] -- in error cases like
those just discussed, the function returns an `Err`. This in turn
means we don't have to bother tracking whether those places are
initialized (which lowers overhead).

[`move_path_for`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/builder/struct.MoveDataBuilder.html#method.move_path_for

## Projections

Instead of using [`PlaceElem`], projections in move paths are stored as [`MoveSubPath`]s.
Projections that can't be moved out of and projections that can be skipped are not represented.

Subslice projections of arrays (produced by slice patterns) are special; they're turned into
multiple [`ConstantIndex`] subpaths, one for each element in the subslice.

[`PlaceElem`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/type.PlaceElem.html
[`MoveSubPath`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/enum.MoveSubPath.html
[`ConstantIndex`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/enum.MoveSubPath.html#variant.ConstantIndex

## Looking up a move-path

If you have a [`Place`] and you would like to convert it to a [`MovePathIndex`], you
can do that using the [`MovePathLookup`] structure found in the [`rev_lookup`] field
of [`MoveData`]. There are two different methods:

[`MoveData`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MoveData.html
[`MovePathLookup`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePathLookup.html
[`rev_lookup`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MoveData.html#structfield.rev_lookup

- [`find_local`], which takes a [`mir::Local`] representing a local
  variable. This is the easier method, because we **always** create a
  [`MovePathIndex`] for every local variable.
- [`find`], which takes an arbitrary [`Place`]. This method is a bit
  more annoying to use, precisely because we don't have a
  [`MovePathIndex`] for **every** [`Place`] (as we just discussed in
  the "illegal move paths" section). Therefore, [`find`] returns a
  [`LookupResult`] indicating the closest path it was able to find
  that exists (e.g., for `foo[1]`, it might return just the path for
  `foo`).

[`find`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePathLookup.html#method.find
[`find_local`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MovePathLookup.html#method.find_local
[`mir::Local`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.Local.html
[`LookupResult`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/enum.LookupResult.html

## Cross-references

As we noted above, move-paths are stored in a big vector and
referenced via their [`MovePathIndex`]. However, within this vector,
they are also structured into a tree. So for example if you have the
[`MovePathIndex`] for `a.b.c`, you can go to its parent move-path
`a.b`. You can also iterate over all children paths: so, from `a.b`,
you might iterate to find the path `a.b.c` (here you are iterating
just over the paths that are **actually referenced** in the source,
not all **possible** paths that could have been referenced). These
references are used for example in the
[`find_in_move_path_or_its_descendants`] function, which determines
whether a move-path (e.g., `a.b`) or any child of that move-path
(e.g.,`a.b.c`) matches a given predicate.

[`Place`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.Place.html
[`find_in_move_path_or_its_descendants`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/move_paths/struct.MoveData.html#method.find_in_move_path_or_its_descendants


---

# The MIR type-check

A key component of the borrow check is the
[MIR type-check](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/type_check/index.html).
This check walks the MIR and does a complete "type check" -- the same
kind you might find in any other language. In the process of doing
this type-check, we also uncover the region constraints that apply to
the program.

TODO -- elaborate further? Maybe? :)

## User types

At the start of MIR type-check, we replace all regions in the body with new unconstrained regions.
However, this would cause us to accept the following program:
```rust
fn foo<'a>(x: &'a u32) {
    let y: &'static u32 = x;
}
```
By erasing the lifetimes in the type of `y` we no longer know that it is supposed to be `'static`,
ignoring the intentions of the user.

To deal with this we remember all places where the user explicitly mentioned a type during
HIR type-check as [`CanonicalUserTypeAnnotations`][annot].

There are two different annotations we care about:
- explicit type ascriptions, e.g. `let y: &'static u32` results in `UserType::Ty(&'static u32)`.
- explicit generic arguments, e.g. `x.foo<&'a u32, Vec<String>>`
results in `UserType::TypeOf(foo_def_id, [&'a u32, Vec<String>])`.

As we do not want the region inference from the HIR type-check to influence MIR typeck,
we store the user type right after lowering it from the HIR.
This means that it may still contain inference variables,
which is why we are using **canonical** user type annotations.
We replace all inference variables with existential bound variables instead.
Something like `let x: Vec<_>` would therefore result in `exists<T> UserType::Ty(Vec<T>)`.

A pattern like `let Foo(x): Foo<&'a u32>` has a user type `Foo<&'a u32>` but
the actual type of `x` should only be `&'a u32`. For this, we use a [`UserTypeProjection`][proj].

In the MIR, we deal with user types in two slightly different ways.

Given a MIR local corresponding to a variable in a pattern which has an explicit type annotation,
we require the type of that local to be equal to the type of the [`UserTypeProjection`][proj].
This is directly stored in the [`LocalDecl`][decl].

We also constrain the type of scrutinee expressions, e.g. the type of `x` in `let _: &'a u32 = x;`.
Here `T_x` only has to be a subtype of the user type, so we instead use
[`StatementKind::AscribeUserType`][stmt] for that.

Note that we do not directly use the user type as the MIR typechecker
doesn't really deal with type and const inference variables. We instead store the final
[`inferred_type`][inf] from the HIR type-checker. During MIR typeck, we then replace its regions
with new nll inference vars and relate it with the actual `UserType` to get the correct region
constraints again.

After the MIR type-check, all user type annotations get discarded, as they aren't needed anymore.

[annot]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.CanonicalUserTypeAnnotation.html
[proj]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.UserTypeProjection.html
[decl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.LocalDecl.html
[stmt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/enum.StatementKind.html#variant.AscribeUserType
[inf]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.CanonicalUserTypeAnnotation.html#structfield.inferred_ty

---

# Drop Check

We generally require the type of locals to be well-formed whenever the
local is used. This includes proving the where-bounds of the local and
also requires all regions used by it to be live.

The only exception to this is when implicitly dropping values when they
go out of scope. This does not necessarily require the value to be live:

```rust
fn main() {
    let x = vec![];
    {
        let y = String::from("I am temporary");
        x.push(&y);
    }
    // `x` goes out of scope here, after the reference to `y`
    // is invalidated. This means that while dropping `x` its type
    // is not well-formed as it contain regions which are not live.
}
```

This is only sound if dropping the value does not try to access any dead
region. We check this by requiring the type of the value to be
drop-live.
The requirements for which are computed in `fn dropck_outlives`.

The rest of this section uses the following type definition for a type
which requires its region parameter to be live:

```rust
struct PrintOnDrop<'a>(&'a str);
impl<'a> Drop for PrintOnDrop<'_> {
    fn drop(&mut self) {
        println!("{}", self.0);
    }
}
```

## How values are dropped

At its core, a value of type `T` is dropped by executing its "drop
glue". Drop glue is compiler generated and first calls `<T as
Drop>::drop` and then recursively calls the drop glue of any recursively
owned values.

- If `T` has an explicit `Drop` impl, call `<T as Drop>::drop`.
- Regardless of whether `T` implements `Drop`, recurse into all values
  *owned* by `T`:
    - references, raw pointers, function pointers, function items, trait
      objects[^traitobj], and scalars do not own anything.
    - tuples, slices, and arrays consider their elements to be owned.
      For arrays of length zero we do not own any value of the element
      type.
    - all fields (of all variants) of ADTs are considered owned. We
      consider all variants for enums. The exception here is
      `ManuallyDrop<U>` which is not considered to own `U`.
      `PhantomData<U>` also does not own anything.
      closures and generators own their captured upvars.

Whether a type has drop glue is returned by [`fn
Ty::needs_drop`](https://github.com/rust-lang/rust/blob/320b412f9c55bf480d26276ff0ab480e4ecb29c0/compiler/rustc_middle/src/ty/util.rs#L1086-L1108).

### Partially dropping a local

For types which do not implement `Drop` themselves, we can also
partially move parts of the value before dropping the rest. In this case
only the drop glue for the not-yet moved values is called, e.g.

```rust
fn main() {
    let mut x = (PrintOnDrop("third"), PrintOnDrop("first"));
    drop(x.1);
    println!("second")
}
```

During MIR building we assume that a local may get dropped whenever it
goes out of scope *as long as its type needs drop*. Computing the exact
drop glue for a variable happens **after** borrowck in the
`ElaborateDrops` pass. This means that even if some part of the local
have been dropped previously, dropck still requires this value to be
live. This is the case even if we completely moved a local.

```rust
fn main() {
    let mut x;
    {
        let temp = String::from("I am temporary");
        x = PrintOnDrop(&temp);
        drop(x);
    }
} //~ ERROR `temp` does not live long enough.
```

It should be possible to add some amount of drop elaboration before
borrowck, allowing this example to compile. There is an unstable feature
to move drop elaboration before const checking:
[#73255](https://github.com/rust-lang/rust/issues/73255). Such a feature
gate does not exist for doing some drop elaboration before borrowck,
although there's a [relevant
MCP](https://github.com/rust-lang/compiler-team/issues/558).

[^traitobj]: you can consider trait objects to have a builtin `Drop`
implementation which directly uses the `drop_in_place` provided by the
vtable. This `Drop` implementation requires all its generic parameters
to be live.

### `dropck_outlives`

There are two distinct "liveness" computations that we perform:

* a value `v` is *use-live* at location `L` if it may be "used" later; a
  *use* here is basically anything that is not a *drop*
* a value `v` is *drop-live* at location `L` if it maybe dropped later

When things are *use-live*, their entire type must be valid at `L`. When
they are *drop-live*, all regions that are required by dropck must be
valid at `L`.  The values dropped in the MIR are *places*.

The constraints computed by `dropck_outlives` for a type closely match
the generated drop glue for that type. Unlike drop glue,
`dropck_outlives` cares about the types of owned values, not the values
itself. For a value of type `T`

- if `T` has an explicit `Drop`, require all generic arguments to be
  live, unless they are marked with `#[may_dangle]` in which case they
  are fully ignored
- regardless of whether `T` has an explicit `Drop`, recurse into all
  types *owned* by `T`
    - references, raw pointers, function pointers, function items, trait
      objects[^traitobj], and scalars do not own anything.
    - tuples, slices and arrays consider their element type to be owned.
      **For arrays we currently do not check whether their length is
      zero**.
    - all fields (of all variants) of ADTs are considered owned. The
      exception here is `ManuallyDrop<U>` which is not considered to own
      `U`. **We consider `PhantomData<U>` to own `U`**.
    - closures and generators own their captured upvars.

The sections marked in bold are cases where `dropck_outlives` considers
types to be owned which are ignored by `Ty::needs_drop`. We only rely on
`dropck_outlives` if `Ty::needs_drop` for the containing local returned
`true`.This means liveness requirements can change depending on whether
a type is contained in a larger local. **This is inconsistent, and
should be fixed: an example [for
arrays](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=8b5f5f005a03971b22edb1c20c5e6cbe)
and [for
`PhantomData`](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=44c6e2b1fae826329fd54c347603b6c8).**[^core]

One possible way these inconsistencies can be fixed is by MIR building
to be more pessimistic, probably by making `Ty::needs_drop` weaker, or
alternatively, changing `dropck_outlives` to be more precise, requiring
fewer regions to be live.

[^core]: This is the core assumption of [#110288](https://github.com/rust-lang/rust/issues/110288) and [RFC 3417](https://github.com/rust-lang/rfcs/pull/3417).


---

# Region inference (NLL)

The MIR-based region checking code is located in [the `rustc_mir::borrow_check`
module][nll].

[nll]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/index.html

The MIR-based region analysis consists of two major functions:

- [`replace_regions_in_mir`], invoked first, has two jobs:
  - First, it finds the set of regions that appear within the
    signature of the function (e.g., `'a` in `fn foo<'a>(&'a u32) {
    ... }`). These are called the "universal" or "free" regions – in
    particular, they are the regions that [appear free][fvb] in the
    function body.
  - Second, it replaces all the regions from the function body with
    fresh inference variables. This is because (presently) those
    regions are the results of lexical region inference and hence are
    not of much interest. The intention is that – eventually – they
    will be "erased regions" (i.e., no information at all), since we
    won't be doing lexical region inference at all.
- [`compute_regions`], invoked second: this is given as argument the
  results of move analysis. It has the job of computing values for all
  the inference variables that `replace_regions_in_mir` introduced.
  - To do that, it first runs the [MIR type checker]. This is
    basically a normal type-checker but specialized to MIR, which is
    much simpler than full Rust, of course. Running the MIR type
    checker will however create various [constraints][cp] between region
    variables, indicating their potential values and relationships to
    one another.
  - After this, we perform [constraint propagation][cp] by creating a
    [`RegionInferenceContext`] and invoking its [`solve`]
    method.
  - The [NLL RFC] also includes fairly thorough (and hopefully readable)
    coverage.

[cp]: ./region-inference/constraint-propagation.md
[fvb]: ../appendix/background.md#free-vs-bound
[`replace_regions_in_mir`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/nll/fn.replace_regions_in_mir.html
[`compute_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/nll/fn.compute_regions.html
[`RegionInferenceContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html
[`solve`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.solve
[NLL RFC]: https://rust-lang.github.io/rfcs/2094-nll.html
[MIR type checker]: ./type-check.md

## Universal regions

The [`UniversalRegions`] type represents a collection of _universal_ regions
corresponding to some MIR `DefId`. It is constructed in
[`replace_regions_in_mir`] when we replace all regions with fresh inference
variables. [`UniversalRegions`] contains indices for all the free regions in
the given MIR along with any relationships that are _known_ to hold between
them (e.g. implied bounds, where clauses, etc.).

For example, given the MIR for the following function:

```rust
fn foo<'a>(x: &'a u32) {
    // ...
}
```

we would create a universal region for `'a` and one for `'static`. There may
also be some complications for handling closures, but we will ignore those for
the moment.

TODO: write about _how_ these regions are computed.

[`UniversalRegions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/universal_regions/struct.UniversalRegions.html

<a id="region-variables"></a>

## Region variables

The value of a region can be thought of as a **set**. This set contains all
points in the MIR where the region is valid along with any regions that are
outlived by this region (e.g. if `'a: 'b`, then `end('b)` is in the set for
`'a`); we call the domain of this set a `RegionElement`. In the code, the value
for all regions is maintained in [the `rustc_borrowck::region_infer` module][ri].
For each region we maintain a set storing what elements are present in its value (to make this
efficient, we give each kind of element an index, the `RegionElementIndex`, and
use sparse bitsets).

[ri]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_borrowck/src/region_infer

The kinds of region elements are as follows:

- Each **[`location`]** in the MIR control-flow graph: a location is just
  the pair of a basic block and an index. This identifies the point
  **on entry** to the statement with that index (or the terminator, if
  the index is equal to `statements.len()`).
- There is an element `end('a)` for each universal region `'a`,
  corresponding to some portion of the caller's (or caller's caller,
  etc) control-flow graph.
- Similarly, there is an element denoted `end('static)` corresponding
  to the remainder of program execution after this function returns.
- There is an element `!1` for each placeholder region `!1`. This
  corresponds (intuitively) to some unknown set of other elements –
  for details on placeholders, see the section
  [placeholders and universes](region-inference/placeholders-and-universes.md).

## Constraints

Before we can infer the value of regions, we need to collect
constraints on the regions. The full set of constraints is described
in [the section on constraint propagation][cp], but the two most
common sorts of constraints are:

1. Outlives constraints. These are constraints that one region outlives another
   (e.g. `'a: 'b`). Outlives constraints are generated by the [MIR type
   checker].
2. Liveness constraints. Each region needs to be live at points where it can be
   used.

## Inference Overview

So how do we compute the contents of a region? This process is called _region
inference_. The high-level idea is pretty simple, but there are some details we
need to take care of.

Here is the high-level idea: we start off each region with the MIR locations we
know must be in it from the liveness constraints. From there, we use all of the
outlives constraints computed from the type checker to _propagate_ the
constraints: for each region `'a`, if `'a: 'b`, then we add all elements of
`'b` to `'a`, including `end('b)`. This all happens in
[`propagate_constraints`].

Then, we will check for errors. We first check that type tests are satisfied by
calling [`check_type_tests`]. This checks constraints like `T: 'a`. Second, we
check that universal regions are not "too big". This is done by calling
[`check_universal_regions`]. This checks that for each region `'a` if `'a`
contains the element `end('b)`, then we must already know that `'a: 'b` holds
(e.g. from a where clause). If we don't already know this, that is an error...
well, almost. There is some special handling for closures that we will discuss
later.

### Example

Consider the following example:

```rust,ignore
fn foo<'a, 'b>(x: &'a usize) -> &'b usize {
    x
}
```

Clearly, this should not compile because we don't know if `'a` outlives `'b`
(if it doesn't then the return value could be a dangling reference).

Let's back up a bit. We need to introduce some free inference variables (as is
done in [`replace_regions_in_mir`]). This example doesn't use the exact regions
produced, but it (hopefully) is enough to get the idea across.

```rust,ignore
fn foo<'a, 'b>(x: &'a /* '#1 */ usize) -> &'b /* '#3 */ usize {
    x // '#2, location L1
}
```

Some notation: `'#1`, `'#3`, and `'#2` represent the universal regions for the
argument, return value, and the expression `x`, respectively. Additionally, I
will call the location of the expression `x` `L1`.

So now we can use the liveness constraints to get the following starting points:

Region  | Contents
--------|----------
'#1     |
'#2     | `L1`
'#3     | `L1`

Now we use the outlives constraints to expand each region. Specifically, we
know that `'#2: '#3` ...

Region  | Contents
--------|----------
'#1     | `L1`
'#2     | `L1, end('#3) // add contents of '#3 and end('#3)`
'#3     | `L1`

... and `'#1: '#2`, so ...

Region  | Contents
--------|----------
'#1     | `L1, end('#2), end('#3) // add contents of '#2 and end('#2)`
'#2     | `L1, end('#3)`
'#3     | `L1`

Now, we need to check that no regions were too big (we don't have any type
tests to check in this case). Notice that `'#1` now contains `end('#3)`, but
we have no `where` clause or implied bound to say that `'a: 'b`... that's an
error!

### Some details

The [`RegionInferenceContext`] type contains all of the information needed to
do inference, including the universal regions from [`replace_regions_in_mir`] and
the constraints computed for each region. It is constructed just after we
compute the liveness constraints.

Here are some of the fields of the struct:

- [`constraints`]: contains all the outlives constraints.
- [`liveness_constraints`]: contains all the liveness constraints.
- [`universal_regions`]: contains the `UniversalRegions` returned by
  [`replace_regions_in_mir`].
- [`universal_region_relations`]: contains relations known to be true about
  universal regions. For example, if we have a where clause that `'a: 'b`, that
  relation is assumed to be true while borrow checking the implementation (it
  is checked at the caller), so `universal_region_relations` would contain `'a:
  'b`.
- [`type_tests`]: contains some constraints on types that we must check after
  inference (e.g. `T: 'a`).
- [`closure_bounds_mapping`]: used for propagating region constraints from
  closures back out to the creator of the closure.

[`constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.constraints
[`liveness_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.liveness_constraints
[`location`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/struct.Location.html
[`universal_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.universal_regions
[`universal_region_relations`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.universal_region_relations
[`type_tests`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.type_tests
[`closure_bounds_mapping`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.closure_bounds_mapping

TODO: should we discuss any of the others fields? What about the SCCs?

Ok, now that we have constructed a `RegionInferenceContext`, we can do
inference. This is done by calling the [`solve`] method on the context. This
is where we call [`propagate_constraints`] and then check the resulting type
tests and universal regions, as discussed above.

[`propagate_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.propagate_constraints
[`check_type_tests`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.check_type_tests
[`check_universal_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.check_universal_regions


---

# Constraint propagation

The main work of the region inference is **constraint propagation**,
which is done in the [`propagate_constraints`] function.  There are
three sorts of constraints that are used in NLL, and we'll explain how
`propagate_constraints` works by "layering" those sorts of constraints
on one at a time (each of them is fairly independent from the others):

- liveness constraints (`R live at E`), which arise from liveness;
- outlives constraints (`R1: R2`), which arise from subtyping;
- [member constraints][m_c] (`member R_m of [R_c...]`), which arise from impl Trait.

[`propagate_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.propagate_constraints
[m_c]: ./member-constraints.md

In this chapter, we'll explain the "heart" of constraint propagation,
covering both liveness and outlives constraints.

## Notation and high-level concepts

Conceptually, region inference is a "fixed-point" computation. It is
given some set of constraints `{C}` and it computes a set of values
`Values: R -> {E}` that maps each region `R` to a set of elements
`{E}` (see [here][riv] for more notes on region elements):

- Initially, each region is mapped to an empty set, so `Values(R) =
  {}` for all regions `R`.
- Next, we process the constraints repeatedly until a fixed-point is reached:
  - For each constraint C:
    - Update `Values` as needed to satisfy the constraint

[riv]: ../region-inference.md#region-variables

As a simple example, if we have a liveness constraint `R live at E`,
then we can apply `Values(R) = Values(R) union {E}` to make the
constraint be satisfied. Similarly, if we have an outlives constraints
`R1: R2`, we can apply `Values(R1) = Values(R1) union Values(R2)`.
(Member constraints are more complex and we discuss them [in this section][m_c].)

In practice, however, we are a bit more clever. Instead of applying
the constraints in a loop, we can analyze the constraints and figure
out the correct order to apply them, so that we only have to apply
each constraint once in order to find the final result.

Similarly, in the implementation, the `Values` set is stored in the
`scc_values` field, but they are indexed not by a *region* but by a
*strongly connected component* (SCC). SCCs are an optimization that
avoids a lot of redundant storage and computation.  They are explained
in the section on outlives constraints.

## Liveness constraints

A **liveness constraint** arises when some variable whose type
includes a region R is live at some [point] P. This simply means that
the value of R must include the point P. Liveness constraints are
computed by the MIR type checker.

[point]: ../../appendix/glossary.md#point

A liveness constraint `R live at E` is satisfied if `E` is a member of
`Values(R)`. So to "apply" such a constraint to `Values`, we just have
to compute `Values(R) = Values(R) union {E}`.

The liveness values are computed in the type-check and passed to the
region inference upon creation in the `liveness_constraints` argument.
These are not represented as individual constraints like `R live at E`
though; instead, we store a (sparse) bitset per region variable (of
type [`LivenessValues`]). This way we only need a single bit for each
liveness constraint.

[`liveness_constraints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.liveness_constraints
[`LivenessValues`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/values/struct.LivenessValues.html

One thing that is worth mentioning: All lifetime parameters are always
considered to be live over the entire function body. This is because
they correspond to some portion of the *caller's* execution, and that
execution clearly includes the time spent in this function, since the
caller is waiting for us to return.

## Outlives constraints

An outlives constraint `'a: 'b` indicates that the value of `'a` must
be a **superset** of the value of `'b`. That is, an outlives
constraint `R1: R2` is satisfied if `Values(R1)` is a superset of
`Values(R2)`. So to "apply" such a constraint to `Values`, we just
have to compute `Values(R1) = Values(R1) union Values(R2)`.

One observation that follows from this is that if you have `R1: R2`
and `R2: R1`, then `R1 = R2` must be true. Similarly, if you have:

```txt
R1: R2
R2: R3
R3: R4
R4: R1
```

then `R1 = R2 = R3 = R4` follows. We take advantage of this to make things
much faster, as described shortly.

In the code, the set of outlives constraints is given to the region
inference context on creation in a parameter of type
[`OutlivesConstraintSet`]. The constraint set is basically just a list of `'a:
'b` constraints.

### The outlives constraint graph and SCCs

In order to work more efficiently with outlives constraints, they are
[converted into the form of a graph][graph-fn], where the nodes of the
graph are region variables (`'a`, `'b`) and each constraint `'a: 'b`
induces an edge `'a -> 'b`. This conversion happens in the
[`RegionInferenceContext::new`] function that creates the inference
context.

[`OutlivesConstraintSet`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/constraints/struct.OutlivesConstraintSet.html
[graph-fn]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/constraints/struct.OutlivesConstraintSet.html#method.graph
[`RegionInferenceContext::new`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.new

When using a graph representation, we can detect regions that must be equal
by looking for cycles. That is, if you have a constraint like

```txt
'a: 'b
'b: 'c
'c: 'd
'd: 'a
```

then this will correspond to a cycle in the graph containing the
elements `'a...'d`.

Therefore, one of the first things that we do in propagating region
values is to compute the **strongly connected components** (SCCs) in
the constraint graph. The result is stored in the [`constraint_sccs`]
field. You can then easily find the SCC that a region `r` is a part of
by invoking `constraint_sccs.scc(r)`.

Working in terms of SCCs allows us to be more efficient: if we have a
set of regions `'a...'d` that are part of a single SCC, we don't have
to compute/store their values separately. We can just store one value
**for the SCC**, since they must all be equal.

If you look over the region inference code, you will see that a number
of fields are defined in terms of SCCs. For example, the
[`scc_values`] field stores the values of each SCC. To get the value
of a specific region `'a` then, we first figure out the SCC that the
region is a part of, and then find the value of that SCC.

[`constraint_sccs`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.constraint_sccs
[`scc_values`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#structfield.scc_values

When we compute SCCs, we not only figure out which regions are a
member of each SCC, we also figure out the edges between them. So for example
consider this set of outlives constraints:

```txt
'a: 'b
'b: 'a

'a: 'c

'c: 'd
'd: 'c
```

Here we have two SCCs: S0 contains `'a` and `'b`, and S1 contains `'c`
and `'d`.  But these SCCs are not independent: because `'a: 'c`, that
means that `S0: S1` as well. That is -- the value of `S0` must be a
superset of the value of `S1`. One crucial thing is that this graph of
SCCs is always a DAG -- that is, it never has cycles. This is because
all the cycles have been removed to form the SCCs themselves.

### Applying liveness constraints to SCCs

The liveness constraints that come in from the type-checker are
expressed in terms of regions -- that is, we have a map like
`Liveness: R -> {E}`.  But we want our final result to be expressed
in terms of SCCs -- we can integrate these liveness constraints very
easily just by taking the union:

```txt
for each region R:
  let S be the SCC that contains R
  Values(S) = Values(S) union Liveness(R)
```

In the region inferencer, this step is done in [`RegionInferenceContext::new`].

### Applying outlives constraints

Once we have computed the DAG of SCCs, we use that to structure out
entire computation. If we have an edge `S1 -> S2` between two SCCs,
that means that `Values(S1) >= Values(S2)` must hold. So, to compute
the value of `S1`, we first compute the values of each successor `S2`.
Then we simply union all of those values together. To use a
quasi-iterator-like notation:

```txt
Values(S1) =
  s1.successors()
    .map(|s2| Values(s2))
    .union()
```

In the code, this work starts in the [`propagate_constraints`]
function, which iterates over all the SCCs. For each SCC `S1`, we
compute its value by first computing the value of its
successors. Since SCCs form a DAG, we don't have to be concerned about
cycles, though we do need to keep a set around to track whether we
have already processed a given SCC or not. For each successor `S2`, once
we have computed `S2`'s value, we can union those elements into the
value for `S1`. (Although we have to be careful in this process to
properly handle [higher-ranked
placeholders](./placeholders-and-universes.md). Note that the value
for `S1` already contains the liveness constraints, since they were
added in [`RegionInferenceContext::new`].

Once that process is done, we now have the "minimal value" for `S1`,
taking into account all of the liveness and outlives
constraints. However, in order to complete the process, we must also
consider [member constraints][m_c], which are described in [a later
section][m_c].


---

# Universal regions

"Universal regions" is the name that the code uses to refer to "named
lifetimes" -- e.g., lifetime parameters and `'static`. The name
derives from the fact that such lifetimes are "universally quantified"
(i.e., we must make sure the code is true for all values of those
lifetimes). It is worth spending a bit of discussing how lifetime
parameters are handled during region inference. Consider this example:

```rust,ignore
fn foo<'a, 'b>(x: &'a u32, y: &'b u32) -> &'b u32 {
  x
}
```

This example is intended not to compile, because we are returning `x`,
which has type `&'a u32`, but our signature promises that we will
return a `&'b u32` value. But how are lifetimes like `'a` and `'b`
integrated into region inference, and how this error wind up being
detected?

## Universal regions and their relationships to one another

Early on in region inference, one of the first things we do is to
construct a [`UniversalRegions`] struct. This struct tracks the
various universal regions in scope on a particular function.  We also
create a [`UniversalRegionRelations`] struct, which tracks their
relationships to one another. So if you have e.g. `where 'a: 'b`, then
the [`UniversalRegionRelations`] struct would track that `'a: 'b` is
known to hold (which could be tested with the [`outlives`] function).

[`UniversalRegions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/universal_regions/struct.UniversalRegions.html
[`UniversalRegionRelations`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/type_check/free_region_relations/struct.UniversalRegionRelations.html
[`outlives`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/type_check/free_region_relations/struct.UniversalRegionRelations.html#method.outlives

## Everything is a region variable

One important aspect of how NLL region inference works is that **all
lifetimes** are represented as numbered variables. This means that the
only variant of [`region_kind::RegionKind`] that we use is the [`ReVar`]
variant. These region variables are broken into two major categories,
based on their index:

[`region_kind::RegionKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/region_kind/enum.RegionKind.html
[`ReVar`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_type_ir/region_kind/enum.RegionKind.html#variant.ReVar

- 0..N: universal regions -- the ones we are discussing here. In this
  case, the code must be correct with respect to any value of those
  variables that meets the declared relationships.
- N..M: existential regions -- inference variables where the region
  inferencer is tasked with finding *some* suitable value.

In fact, the universal regions can be further subdivided based on
where they were brought into scope (see the [`RegionClassification`]
type). These subdivisions are not important for the topics discussed
here, but become important when we consider [closure constraint
propagation](./closure-constraints.md), so we discuss them there.

[`RegionClassification`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/universal_regions/enum.RegionClassification.html#variant.Local

## Universal lifetimes as the elements of a region's value

As noted previously, the value that we infer for each region is a set
`{E}`. The elements of this set can be points in the control-flow
graph, but they can also be an element `end('a)` corresponding to each
universal lifetime `'a`. If the value for some region `R0` includes
`end('a`), then this implies that `R0` must extend until the end of `'a`
in the caller.

## The "value" of a universal region

During region inference, we compute a value for each universal region
in the same way as we compute values for other regions. This value
represents, effectively, the **lower bound** on that universal region
-- the things that it must outlive. We now describe how we use this
value to check for errors.

## Liveness and universal regions

All universal regions have an initial liveness constraint that
includes the entire function body. This is because lifetime parameters
are defined in the caller and must include the entirety of the
function call that invokes this particular function. In addition, each
universal region `'a` includes itself (that is, `end('a)`) in its
liveness constraint (i.e., `'a` must extend until the end of
itself). In the code, these liveness constraints are setup in
[`init_free_and_bound_regions`].

[`init_free_and_bound_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.init_free_and_bound_regions

## Propagating outlives constraints for universal regions

So, consider the first example of this section:

```rust,ignore
fn foo<'a, 'b>(x: &'a u32, y: &'b u32) -> &'b u32 {
  x
}
```

Here, returning `x` requires that `&'a u32 <: &'b u32`, which gives
rise to an outlives constraint `'a: 'b`. Combined with our default liveness
constraints we get:

```txt
'a live at {B, end('a)} // B represents the "function body"
'b live at {B, end('b)}
'a: 'b
```

When we process the `'a: 'b` constraint, therefore, we will add
`end('b)` into the value for `'a`, resulting in a final value of `{B,
end('a), end('b)}`.

## Detecting errors

Once we have finished constraint propagation, we then enforce a
constraint that if some universal region `'a` includes an element
`end('b)`, then `'a: 'b` must be declared in the function's bounds. If
not, as in our example, that is an error. This check is done in the
[`check_universal_regions`] function, which simply iterates over all
universal regions, inspects their final value, and tests against the
declared [`UniversalRegionRelations`].

[`check_universal_regions`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/region_infer/struct.RegionInferenceContext.html#method.check_universal_regions


---

# Member constraints

A member constraint `'m member of ['c_1..'c_N]` expresses that the
region `'m` must be *equal* to some **choice regions** `'c_i` (for some `i`).
These constraints cannot be expressed by users, but they
arise from `impl Trait` due to its lifetime capture rules.
Consider a function such as the following:

```rust,ignore
fn make(a: &'a u32, b: &'b u32) -> impl Trait<'a, 'b> { .. }
```

Here, the true return type (often called the "hidden type") is only
permitted to capture the lifetimes `'a` or `'b`.
You can kind of see
this more clearly by desugaring that `impl Trait` return type into its
more explicit form:

```rust,ignore
type MakeReturn<'x, 'y> = impl Trait<'x, 'y>;
fn make(a: &'a u32, b: &'b u32) -> MakeReturn<'a, 'b> { .. }
```

Here, the idea is that the hidden type must be some type that could
have been written in place of the `impl Trait<'x, 'y>` -- but clearly
such a type can only reference the regions `'x` or `'y` (or
`'static`!), as those are the only names in scope.
This limitation is
then translated into a restriction to only access `'a` or `'b` because
we are returning `MakeReturn<'a, 'b>`, where `'x` and `'y` have been
replaced with `'a` and `'b` respectively.

## Detailed example

To help us explain member constraints in more detail, let's spell out
the `make` example in a bit more detail.
First off, let's assume that you have some dummy trait:

```rust,ignore
trait Trait<'a, 'b> { }
impl<T> Trait<'_, '_> for T { }
```

and this is the `make` function (in desugared form):

```rust,ignore
type MakeReturn<'x, 'y> = impl Trait<'x, 'y>;
fn make(a: &'a u32, b: &'b u32) -> MakeReturn<'a, 'b> {
  (a, b)
}
```

What happens in this case is that the return type will be `(&'0 u32, &'1 u32)`,
where `'0` and `'1` are fresh region variables.
We will have the following region constraints:

```txt
'0 live at {L}
'1 live at {L}
'a: '0
'b: '1
'0 member of ['a, 'b, 'static]
'1 member of ['a, 'b, 'static]
```

Here the "liveness set" `{L}` corresponds to that subset of the body
where `'0` and `'1` are live -- basically the point from where the
return tuple is constructed to where it is returned (in fact, `'0` and
`'1` might have slightly different liveness sets, but that's not very
interesting to the point we are illustrating here).

The `'a: '0` and `'b: '1` constraints arise from subtyping.
When we construct the `(a, b)` value, it will be assigned type `(&'0 u32, &'1
u32)` -- the region variables reflect that the lifetimes of these
references could be made smaller.
For this value to be created from `a` and `b`, however, we do require that:

```txt
(&'a u32, &'b u32) <: (&'0 u32, &'1 u32)
```

which means in turn that `&'a u32 <: &'0 u32` and hence that `'a: '0`
(and similarly that `&'b u32 <: &'1 u32`, `'b: '1`).

Note that if we ignore member constraints, the value of `'0` would be
inferred to some subset of the function body (from the liveness
constraints, which we did not write explicitly).
It would never become
`'a`, because there is no need for it too -- we have a constraint that
`'a: '0`, but that just puts a "cap" on how *large* `'0` can grow to become.
Since we compute the *minimal* value that we can, we are happy
to leave `'0` as being just equal to the liveness set.
This is where member constraints come in.

## Choices are always lifetime parameters

At present, the "choice" regions from a member constraint are always lifetime
parameters from the current function. As of <!-- date-check --> March 2026,
this falls out from the placement of impl Trait, though in the future it may not
be the case.
We take some advantage of this fact, as it simplifies the current code.
In particular, we don't have to consider a case like `'0 member of ['1,
'static]`, in which the value of both `'0` and `'1` are being inferred and hence
changing.
See [rust-lang/rust#61773][#61773] for more information.

[#61773]: https://github.com/rust-lang/rust/issues/61773

## Applying member constraints

Member constraints are a bit more complex than other forms of constraints.
This is because they have a "or" quality to them -- that
is, they describe multiple choices that we must select from. E.g., in
our example constraint `'0 member of ['a, 'b, 'static]`, it might be
that `'0` is equal to `'a`, `'b`, *or* `'static`.
How can we pick the correct one?
What we currently do is to look for a *minimal choice*
-- if we find one, then we will grow `'0` to be equal to that minimal choice.
To find that minimal choice, we take two factors into
consideration: lower and upper bounds.

### Lower bounds

The *lower bounds* are those lifetimes that `'0` *must outlive* --
i.e., that `'0` must be larger than. In fact, when it comes time to
apply member constraints, we've already *computed* the lower bounds of
`'0` because we computed its minimal value (or at least, the lower
bounds considering everything but member constraints).

Let `LB` be the current value of `'0`.
We know then that `'0: LB` must hold, whatever the final value of `'0` is.
Therefore, we can rule out
any choice `'choice` where `'choice: LB` does not hold.

Unfortunately, in our example, this is not very helpful.
The lower bound for `'0` will just be the liveness set `{L}`, and we know that
all the lifetime parameters outlive that set.
So we are left with the same set of choices here.
(But in other examples, particularly those
with different variance, lower bound constraints may be relevant.)

### Upper bounds

The *upper bounds* are those lifetimes that *must outlive* `'0` --
i.e., that `'0` must be *smaller* than. In our example, this would be
`'a`, because we have the constraint that `'a: '0`.
In more complex examples, the chain may be more indirect.

We can use upper bounds to rule out members in a very similar way to
lower bounds.
If UB is some upper bound, then we know that `UB:
'0` must hold, so we can rule out any choice `'choice` where `UB:
'choice` does not hold.

In our example, we would be able to reduce our choice set from `['a,
'b, 'static]` to just `['a]`.
This is because `'0` has an upper bound
of `'a`, and neither `'a: 'b` nor `'a: 'static` is known to hold.

(For notes on how we collect upper bounds in the implementation, see
[the section below](#collecting).)

### Minimal choice

After applying lower and upper bounds, we can still sometimes have
multiple possibilities.
For example, imagine a variant of our example
using types with the opposite variance.
In that case, we would have the constraint `'0: 'a` instead of `'a: '0`.
Hence the current value of `'0` would be `{L, 'a}`.
Using this as a lower bound, we would be
able to narrow down the member choices to `['a, 'static]` because `'b:
'a` is not known to hold (but `'a: 'a` and `'static: 'a` do hold).
We would not have any upper bounds, so that would be our final set of choices.

In that case, we apply the **minimal choice** rule -- basically, if
one of our choices if smaller than the others, we can use that.
In this case, we would opt for `'a` (and not `'static`).

This choice is consistent with the general 'flow' of region
propagation, which always aims to compute a minimal value for the
region being inferred.
However, it is somewhat arbitrary.

<a id="collecting"></a>

### Collecting upper bounds in the implementation

In practice, computing upper bounds is a bit inconvenient, because our
data structures are setup for the opposite.
What we do is to compute
the **reverse SCC graph** (we do this lazily and cache the result) --
that is, a graph where `'a: 'b` induces an edge `SCC('b) -> SCC('a)`.
Like the normal SCC graph, this is a DAG.
We can then do a depth-first search starting from `SCC('0)` in this graph.
This will take us to all the SCCs that must outlive `'0`.

One wrinkle is that, as we walk the "upper bound" SCCs, their values
will not yet have been fully computed.
However, we **have** already
applied their liveness constraints, so we have some information about
their value.
In particular, for any regions representing lifetime
parameters, their value will contain themselves (i.e., the initial
value for `'a` includes `'a` and the value for `'b` contains `'b`).
So we can collect all of the lifetime parameters that are reachable,
which is precisely what we are interested in.


---

# Placeholders and universes

From time to time we have to reason about regions that we can't
concretely know. For example, consider this program:

```rust,ignore
// A function that needs a static reference
fn foo(x: &'static u32) { }

fn bar(f: for<'a> fn(&'a u32)) {
       // ^^^^^^^^^^^^^^^^^^^ a function that can accept **any** reference
    let x = 22;
    f(&x);
}

fn main() {
    bar(foo);
}
```

This program ought not to type-check: `foo` needs a static reference
for its argument, and `bar` wants to be given a function that
accepts **any** reference (so it can call it with something on its
stack, for example). But *how* do we reject it and *why*?

## Subtyping and Placeholders

When we type-check `main`, and in particular the call `bar(foo)`, we
are going to wind up with a subtyping relationship like this one:

```text
fn(&'static u32) <: for<'a> fn(&'a u32)
----------------    -------------------
the type of `foo`   the type `bar` expects
```

We handle this sort of subtyping by taking the variables that are
bound in the supertype and replacing them with
[universally quantified](../../appendix/background.md#quantified)
representatives, denoted like `!1` here. We call these regions "placeholder
regions" – they represent, basically, "some unknown region".

Once we've done that replacement, we have the following relation:

```text
fn(&'static u32) <: fn(&'!1 u32)
```

The key idea here is that this unknown region `'!1` is not related to
any other regions. So if we can prove that the subtyping relationship
is true for `'!1`, then it ought to be true for any region, which is
what we wanted.

So let's work through what happens next. To check if two functions are
subtypes, we check if their arguments have the desired relationship
(fn arguments are [contravariant](../../appendix/background.md#variance), so
we swap the left and right here):

```text
&'!1 u32 <: &'static u32
```

According to the basic subtyping rules for a reference, this will be
true if `'!1: 'static`. That is – if "some unknown region `!1`" outlives `'static`.
Now, this *might* be true – after all, `'!1` could be `'static` –
but we don't *know* that it's true. So this should yield up an error (eventually).

## What is a universe?

In the previous section, we introduced the idea of a placeholder
region, and we denoted it `!1`. We call this number `1` the **universe
index**. The idea of a "universe" is that it is a set of names that
are in scope within some type or at some point. Universes are formed
into a tree, where each child extends its parents with some new names.
So the **root universe** conceptually contains global names, such as
the lifetime `'static` or the type `i32`. In the compiler, we also
put generic type parameters into this root universe (in this sense,
there is not just one root universe, but one per item). So consider
this function `bar`:

```rust,ignore
struct Foo { }

fn bar<'a, T>(t: &'a T) {
    ...
}
```

Here, the root universe would consist of the lifetimes `'static` and
`'a`.  In fact, although we're focused on lifetimes here, we can apply
the same concept to types, in which case the types `Foo` and `T` would
be in the root universe (along with other global types, like `i32`).
Basically, the root universe contains all the names that
[appear free](../../appendix/background.md#free-vs-bound) in the body of `bar`.

Now let's extend `bar` a bit by adding a variable `x`:

```rust,ignore
fn bar<'a, T>(t: &'a T) {
    let x: for<'b> fn(&'b u32) = ...;
}
```

Here, the name `'b` is not part of the root universe. Instead, when we
"enter" into this `for<'b>` (e.g., by replacing it with a placeholder), we will create
a child universe of the root, let's call it U1:

```text
U0 (root universe)
│
└─ U1 (child universe)
```

The idea is that this child universe U1 extends the root universe U0
with a new name, which we are identifying by its universe number:
`!1`.

Now let's extend `bar` a bit by adding one more variable, `y`:

```rust,ignore
fn bar<'a, T>(t: &'a T) {
    let x: for<'b> fn(&'b u32) = ...;
    let y: for<'c> fn(&'c u32) = ...;
}
```

When we enter *this* type, we will again create a new universe, which
we'll call `U2`. Its parent will be the root universe, and U1 will be
its sibling:

```text
U0 (root universe)
│
├─ U1 (child universe)
│
└─ U2 (child universe)
```

This implies that, while in U2, we can name things from U0 or U2, but
not U1.

**Giving existential variables a universe.** Now that we have this
notion of universes, we can use it to extend our type-checker and
things to prevent illegal names from leaking out. The idea is that we
give each inference (existential) variable – whether it be a type or
a lifetime – a universe. That variable's value can then only
reference names visible from that universe. So for example if a
lifetime variable is created in U0, then it cannot be assigned a value
of `!1` or `!2`, because those names are not visible from the universe
U0.

**Representing universes with just a counter.** You might be surprised
to see that the compiler doesn't keep track of a full tree of
universes. Instead, it just keeps a counter – and, to determine if
one universe can see another one, it just checks if the index is
greater. For example, U2 can see U0 because 2 >= 0. But U0 cannot see
U2, because 0 >= 2 is false.

How can we get away with this? Doesn't this mean that we would allow
U2 to also see U1? The answer is that, yes, we would, **if that
question ever arose**.  But because of the structure of our type
checker etc, there is no way for that to happen. In order for
something happening in the universe U1 to "communicate" with something
happening in U2, they would have to have a shared inference variable X
in common. And because everything in U1 is scoped to just U1 and its
children, that inference variable X would have to be in U0. And since
X is in U0, it cannot name anything from U1 (or U2). This is perhaps easiest
to see by using a kind of generic "logic" example:

```text
exists<X> {
   forall<Y> { ... /* Y is in U1 ... */ }
   forall<Z> { ... /* Z is in U2 ... */ }
}
```

Here, the only way for the two foralls to interact would be through X,
but neither Y nor Z are in scope when X is declared, so its value
cannot reference either of them.

## Universes and placeholder region elements

But where does that error come from?  The way it happens is like this.
When we are constructing the region inference context, we can tell
from the type inference context how many placeholder variables exist
(the `InferCtxt` has an internal counter). For each of those, we
create a corresponding universal region variable `!n` and a "region
element" `placeholder(n)`. This corresponds to "some unknown set of other
elements". The value of `!n` is `{placeholder(n)}`.

At the same time, we also give each existential variable a
**universe** (also taken from the `InferCtxt`). This universe
determines which placeholder elements may appear in its value: For
example, a variable in universe U3 may name `placeholder(1)`, `placeholder(2)`, and
`placeholder(3)`, but not `placeholder(4)`. Note that the universe of an inference
variable controls what region elements **can** appear in its value; it
does not say region elements **will** appear.

## Placeholders and outlives constraints

In the region inference engine, outlives constraints have the form:

```text
V1: V2 @ P
```

where `V1` and `V2` are region indices, and hence map to some region
variable (which may be universally or existentially quantified). The
`P` here is a "point" in the control-flow graph; it's not important
for this section. This variable will have a universe, so let's call
those universes `U(V1)` and `U(V2)` respectively. (Actually, the only
one we are going to care about is `U(V1)`.)

When we encounter this constraint, the ordinary procedure is to start
a DFS from `P`. We keep walking so long as the nodes we are walking
are present in `value(V2)` and we add those nodes to `value(V1)`. If
we reach a return point, we add in any `end(X)` elements. That part
remains unchanged.

But then *after that* we want to iterate over the placeholder `placeholder(x)`
elements in V2 (each of those must be visible to `U(V2)`, but we
should be able to just assume that is true, we don't have to check
it). We have to ensure that `value(V1)` outlives each of those
placeholder elements.

Now there are two ways that could happen. First, if `U(V1)` can see
the universe `x` (i.e., `x <= U(V1)`), then we can just add `placeholder(x)`
to `value(V1)` and be done. But if not, then we have to approximate:
we may not know what set of elements `placeholder(x)` represents, but we
should be able to compute some sort of **upper bound** B for it –
some region B that outlives `placeholder(x)`. For now, we'll just use
`'static` for that (since it outlives everything) – in the future, we
can sometimes be smarter here (and in fact we have code for doing this
already in other contexts). Moreover, since `'static` is in the root
universe U0, we know that all variables can see it – so basically if
we find that `value(V2)` contains `placeholder(x)` for some universe `x`
that `V1` can't see, then we force `V1` to `'static`.

## Extending the "universal regions" check

After all constraints have been propagated, the NLL region inference
has one final check, where it goes over the values that wound up being
computed for each universal region and checks that they did not get
'too large'. In our case, we will go through each placeholder region
and check that it contains *only* the `placeholder(u)` element it is known to
outlive. (Later, we might be able to know that there are relationships
between two placeholder regions and take those into account, as we do
for universal regions from the fn signature.)

Put another way, the "universal regions" check can be considered to be
checking constraints like:

```text
{placeholder(1)}: V1
```

where `{placeholder(1)}` is like a constant set, and V1 is the variable we
made to represent the `!1` region.

## Back to our example

OK, so far so good. Now let's walk through what would happen with our
first example:

```text
fn(&'static u32) <: fn(&'!1 u32) @ P  // this point P is not imp't here
```

The region inference engine will create a region element domain like this:

```text
{ CFG; end('static); placeholder(1) }
  ---  ------------  ------- from the universe `!1`
  |    'static is always in scope
  all points in the CFG; not especially relevant here
```

It will always create two universal variables, one representing
`'static` and one representing `'!1`. Let's call them Vs and V1. They
will have initial values like so:

```text
Vs = { CFG; end('static) } // it is in U0, so can't name anything else
V1 = { placeholder(1) }
```

From the subtyping constraint above, we would have an outlives constraint like

```text
'!1: 'static @ P
```

To process this, we would grow the value of V1 to include all of Vs:

```text
Vs = { CFG; end('static) }
V1 = { CFG; end('static), placeholder(1) }
```

At that point, constraint propagation is complete, because all the
outlives relationships are satisfied. Then we would go to the "check
universal regions" portion of the code, which would test that no
universal region grew too large.

In this case, `V1` *did* grow too large – it is not known to outlive
`end('static)`, nor any of the CFG – so we would report an error.

## Another example

What about this subtyping relationship?

```text
for<'a> fn(&'a u32, &'a u32)
    <:
for<'b, 'c> fn(&'b u32, &'c u32)
```

Here we would replace the bound region in the supertype with a placeholder, as before, yielding:

```text
for<'a> fn(&'a u32, &'a u32)
    <:
fn(&'!1 u32, &'!2 u32)
```

then we instantiate the variable on the left-hand side with an
existential in universe U2, yielding the following (`?n` is a notation
for an existential variable):

```text
fn(&'?3 u32, &'?3 u32)
    <:
fn(&'!1 u32, &'!2 u32)
```

Then we break this down further:

```text
&'!1 u32 <: &'?3 u32
&'!2 u32 <: &'?3 u32
```

and even further, yield up our region constraints:

```text
'!1: '?3
'!2: '?3
```

Note that, in this case, both `'!1` and `'!2` have to outlive the
variable `'?3`, but the variable `'?3` is not forced to outlive
anything else. Therefore, it simply starts and ends as the empty set
of elements, and hence the type-check succeeds here.

(This should surprise you a little. It surprised me when I first realized it.
We are saying that if we are a fn that **needs both of its arguments to have
the same region**, we can accept being called with **arguments with two
distinct regions**. That seems intuitively unsound. But in fact, it's fine, as
I tried to explain in [this issue][ohdeargoditsallbroken] on the Rust issue
tracker long ago.  The reason is that even if we get called with arguments of
two distinct lifetimes, those two lifetimes have some intersection (the call
itself), and that intersection can be our value of `'a` that we use as the
common lifetime of our arguments. -nmatsakis)

[ohdeargoditsallbroken]: https://github.com/rust-lang/rust/issues/32330#issuecomment-202536977

## Final example

Let's look at one last example. We'll extend the previous one to have
a return type:

```text
for<'a> fn(&'a u32, &'a u32) -> &'a u32
    <:
for<'b, 'c> fn(&'b u32, &'c u32) -> &'b u32
```

Despite seeming very similar to the previous example, this case is going to get
an error. That's good: the problem is that we've gone from a fn that promises
to return one of its two arguments, to a fn that is promising to return the
first one. That is unsound. Let's see how it plays out.

First, we replace the bound region in the supertype with a placeholder:

```text
for<'a> fn(&'a u32, &'a u32) -> &'a u32
    <:
fn(&'!1 u32, &'!2 u32) -> &'!1 u32
```

Then we instantiate the subtype with existentials (in U2):

```text
fn(&'?3 u32, &'?3 u32) -> &'?3 u32
    <:
fn(&'!1 u32, &'!2 u32) -> &'!1 u32
```

And now we create the subtyping relationships:

```text
&'!1 u32 <: &'?3 u32 // arg 1
&'!2 u32 <: &'?3 u32 // arg 2
&'?3 u32 <: &'!1 u32 // return type
```

And finally the outlives relationships. Here, let V1, V2, and V3 be the
variables we assign to `!1`, `!2`, and `?3` respectively:

```text
V1: V3
V2: V3
V3: V1
```

Those variables will have these initial values:

```text
V1 in U1 = {placeholder(1)}
V2 in U2 = {placeholder(2)}
V3 in U2 = {}
```

Now because of the `V3: V1` constraint, we have to add `placeholder(1)` into `V3` (and
indeed it is visible from `V3`), so we get:

```text
V3 in U2 = {placeholder(1)}
```

then we have this constraint `V2: V3`, so we wind up having to enlarge
`V2` to include `placeholder(1)` (which it can also see):

```text
V2 in U2 = {placeholder(1), placeholder(2)}
```

Now constraint propagation is done, but when we check the outlives
relationships, we find that `V2` includes this new element `placeholder(1)`,
so we report an error.


---

# Propagating closure constraints

When we are checking the type tests and universal regions, we may come
across a constraint that we can't prove yet if we are in a closure
body! However, the necessary constraints may actually hold (we just
don't know it yet). Thus, if we are inside a closure, we just collect
all the constraints we can't prove yet and return them. Later, when we
are borrow check the MIR node that created the closure, we can also
check that these constraints hold. At that time, if we can't prove
they hold, we report an error.

## How this is implemented

While borrow-checking a closure inside of `RegionInferenceContext::solve` we separately try to propagate type-outlives and region-outlives constraints to the parent if we're unable to prove them locally.

### Region-outlive constraints

If `RegionInferenceContext::check_universal_regions` fails to prove some outlives constraint `'longer_fr: 'shorter_fr`, we try to propagate it in `fn try_propagate_universal_region_error`. Both these universal regions are either local to the closure or an external region.

In case `'longer_fr` is a local universal region, we search for the largest external region `'fr_minus` which is outlived by `'longer_fr`, i.e. `'longer_fr: 'fr_minus`. In case there are multiple such regions, we pick the `mutual_immediate_postdominator`: the fixpoint of repeatedly computing the GLB of all GLBs, see [TransitiveRelation::postdom_upper_bound](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/transitive_relation/struct.TransitiveRelation.html#method.postdom_upper_bound) for more details.

If `'fr_minus` exists we require it to outlive all non-local upper bounds of `'shorter_fr`. There will always be at least one non-local upper bound `'static`.

### Type-outlive constraints

Type-outlives constraints are proven in `check_type_tests`. This happens after computing the outlives graph, which is now immutable.

For all type tests we fail to prove via `fn eval_verify_bound` inside of the closure we call `try_promote_type_test`. A `TypeTest` represents a type-outlives bound `generic_kind: lower_bound` together with a `verify_bound`. If the `VerifyBound` holds for the `lower_bound`, the constraint is satisfied. `try_promote_type_test`  does not care about the ` verify_bound`.

It starts by calling `fn try_promote_type_test_subject`. This function takes the `GenericKind` and tries to transform it to a `ClosureOutlivesSubject`  which is no longer references anything local to the closure. This is done by replacing all free regions in that type with either `'static`  or region parameters which are equal to that free region. This operation fails if the `generic_kind` contains a region which cannot be replaced.

We then promote the `lower_bound` into the context of the caller. If the lower bound is equal to a placeholder, we replace it with `'static`

We then look at all universal regions `uv` which are required to be outlived by `lower_bound`, i.e. for which borrow checking added region constraints. For each of these we then emit a `ClosureOutlivesRequirement` for all non-local universal regions which are known to outlive `uv`.

As we've already built the region graph of the closure at this point and separately check that it is consistent, we are also able to assume the outlive constraints `uv: lower_bound` here.

So if we have a type-outlives bounds we can't prove, e.g. `T: 'local_infer`, we use the region graph to go to universal variables `'a` with `'a: local_infer`. In case `'a` are local, we then use the assumed outlived constraints to go to non-local ones.

We then store the list of promoted type tests in the `BorrowCheckResults`.
We then apply them in while borrow-checking its parent in `TypeChecker::prove_closure_bounds`.

TODO: explain how exactly that works :3


---

# Reporting region errors

TODO: we should discuss how to generate errors from the results of these analyses.


---

# Two-phase borrows

Two-phase borrows are a more permissive version of mutable borrows that allow
nested method calls such as `vec.push(vec.len())`. Such borrows first act as
shared borrows in a "reservation" phase and can later be "activated" into a
full mutable borrow.

Only certain implicit mutable borrows can be two-phase, any `&mut` or `ref mut`
in the source code is never a two-phase borrow. The cases where we generate a
two-phase borrow are:

1. The autoref borrow when calling a method with a mutable reference receiver.
2. A mutable reborrow in function arguments.
3. The implicit mutable borrow in an overloaded compound assignment operator.

To give some examples:

```rust,edition2018
// In the source code

// Case 1:
let mut v = Vec::new();
v.push(v.len());
let r = &mut Vec::new();
r.push(r.len());

// Case 2:
std::mem::replace(r, vec![1, r.len()]);

// Case 3:
let mut x = std::num::Wrapping(2);
x += x;
```

Expanding these enough to show the two-phase borrows:

```rust,ignore
// Case 1:
let mut v = Vec::new();
let temp1 = &two_phase v;
let temp2 = v.len();
Vec::push(temp1, temp2);
let r = &mut Vec::new();
let temp3 = &two_phase *r;
let temp4 = r.len();
Vec::push(temp3, temp4);

// Case 2:
let temp5 = &two_phase *r;
let temp6 = vec![1, r.len()];
std::mem::replace(temp5, temp6);

// Case 3:
let mut x = std::num::Wrapping(2);
let temp7 = &two_phase x;
let temp8 = x;
std::ops::AddAssign::add_assign(temp7, temp8);
```

Whether a borrow can be two-phase is tracked by a flag on the [`AutoBorrow`]
after type checking, which is then [converted] to a [`BorrowKind`] during MIR
construction.

Each two-phase borrow is assigned to a temporary that is only used once. As
such we can define:

* The point where the temporary is assigned to is called the *reservation*
  point of the two-phase borrow.
* The point where the temporary is used, which is effectively always a
  function call, is called the *activation* point.

The activation points are found using the [`GatherBorrows`] visitor. The
[`BorrowData`] then holds both the reservation and activation points for the
borrow.

[`AutoBorrow`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/adjustment/enum.AutoBorrow.html
[converted]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_build/thir/cx/expr/trait.ToBorrowKind.html#method.to_borrow_kind
[`BorrowKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/enum.BorrowKind.html
[`GatherBorrows`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/borrow_set/struct.GatherBorrows.html
[`BorrowData`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/borrow_set/struct.BorrowData.html

## Checking two-phase borrows

Two-phase borrows are treated as if they were mutable borrows with the
following exceptions:

1. At every location in the MIR we [check] if any two-phase borrows are
   activated at this location. If a live two phase borrow is activated at a
   location, then we check that there are no borrows that conflict with the
   two-phase borrow.
2. At the reservation point we error if there are conflicting live *mutable*
   borrows. And lint if there are any conflicting shared borrows.
3. Between the reservation and the activation point, the two-phase borrow acts
   as a shared borrow. We determine (in [`is_active`]) if we're at such a point
   by using the [`Dominators`] for the MIR graph.
4. After the activation point, the two-phase borrow acts as a mutable borrow.

[check]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/struct.MirBorrowckCtxt.html#method.check_activations
[`Dominators`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/graph/dominators/struct.Dominators.html
[`is_active`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/path_utils/fn.is_active.html


---

# Closure Capture Inference

This section describes how rustc handles closures. Closures in Rust are
effectively "desugared" into structs that contain the values they use (or
references to the values they use) from their creator's stack frame. rustc has
the job of figuring out which values a closure uses and how, so it can decide
whether to capture a given variable by shared reference, mutable reference, or
by move. rustc also has to figure out which of the closure traits ([`Fn`][fn],
[`FnMut`][fn_mut], or [`FnOnce`][fn_once]) a closure is capable of
implementing.

[fn]: https://doc.rust-lang.org/std/ops/trait.Fn.html
[fn_mut]:https://doc.rust-lang.org/std/ops/trait.FnMut.html
[fn_once]: https://doc.rust-lang.org/std/ops/trait.FnOnce.html

Let's start with a few examples:

### Example 1

To start, let's take a look at how the closure in the following example is desugared:

```rust
fn closure(f: impl Fn()) {
    f();
}

fn main() {
    let x: i32 = 10;
    closure(|| println!("Hi {}", x));  // The closure just reads x.
    println!("Value of x after return {}", x);
}
```

Let's say the above is the content of a file called `immut.rs`. If we compile
`immut.rs` using the following command. The [`-Z dump-mir=all`][dump-mir] flag will cause
`rustc` to generate and dump the [MIR][mir] to a directory called `mir_dump`.
```console
> rustc +stage1 immut.rs -Z dump-mir=all
```

[mir]: ./mir/index.md
[dump-mir]: ./mir/passes.md

After we run this command, we will see a newly generated directory in our
current working directory called `mir_dump`, which will contain several files.
If we look at file `rustc.main.-------.mir_map.0.mir`, we will find, among
other things, it also contains this line:

```rust,ignore
_4 = &_1;
_3 = [closure@immut.rs:7:13: 7:36] { x: move _4 };
```

Note that in the MIR examples in this chapter, `_1` is `x`.

Here in first line `_4 = &_1;`, the `mir_dump` tells us that `x` was borrowed
as an immutable reference.  This is what we would hope as our closure just
reads `x`.

### Example 2

Here is another example:

```rust
fn closure(mut f: impl FnMut()) {
    f();
}

fn main() {
    let mut x: i32 = 10;
    closure(|| {
        x += 10;  // The closure mutates the value of x
        println!("Hi {}", x)
    });
    println!("Value of x after return {}", x);
}
```

```rust,ignore
_4 = &mut _1;
_3 = [closure@mut.rs:7:13: 10:6] { x: move _4 };
```
This time along, in the line `_4 = &mut _1;`, we see that the borrow is changed to mutable borrow.
Fair enough! The closure increments `x` by 10.

### Example 3

One more example:

```rust
fn closure(f: impl FnOnce()) {
    f();
}

fn main() {
    let x = vec![21];
    closure(|| {
        drop(x);  // Makes x unusable after the fact.
    });
    // println!("Value of x after return {:?}", x);
}
```

```rust,ignore
_6 = [closure@move.rs:7:13: 9:6] { x: move _1 }; // bb16[3]: scope 1 at move.rs:7:13: 9:6
```
Here, `x` is directly moved into the closure and the access to it will not be permitted after the
closure.

## Inferences in the compiler

Now let's dive into rustc code and see how all these inferences are done by the compiler.

Let's start with defining a term that we will be using quite a bit in the rest of the discussion -
*upvar*. An **upvar** is a variable that is local to the function where the closure is defined. So,
in the above examples, **x** will be an upvar to the closure. They are also sometimes referred to as
the *free variables* meaning they are not bound to the context of the closure.
[`compiler/rustc_passes/src/upvars.rs`][upvars] defines a query called *upvars_mentioned*
for this purpose.

[upvars]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_passes/upvars/index.html

Other than lazy invocation, one other thing that distinguishes a closure from a
normal function is that it can use the upvars. It borrows these upvars from its surrounding
context; therefore the compiler has to determine the upvar's borrow type. The compiler starts with
assigning an immutable borrow type and lowers the restriction (that is, changes it from
**immutable** to **mutable** to **move**) as needed, based on the usage. In the Example 1 above, the
closure only uses the variable for printing but does not modify it in any way and therefore, in the
`mir_dump`, we find the borrow type for the upvar `x` to be immutable.  In example 2, however, the
closure modifies `x` and increments it by some value.  Because of this mutation, the compiler, which
started off assigning `x` as an immutable reference type, has to adjust it as a mutable reference.
Likewise in the third example, the closure drops the vector and therefore this requires the variable
`x` to be moved into the closure. Depending on the borrow kind, the closure has to implement the
appropriate trait: `Fn` trait for immutable borrow, `FnMut` for mutable borrow,
and `FnOnce` for move semantics.

Most of the code related to the closure is in the
[`compiler/rustc_hir_typeck/src/upvar.rs`][upvar] file and the data structures are
declared in the file [`compiler/rustc_middle/src/ty/mod.rs`][ty].

[upvar]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/upvar/index.html
[ty]:https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/index.html

Before we go any further, let's discuss how we can examine the flow of control through the rustc
codebase. For closures specifically, set the `RUSTC_LOG` env variable as below and collect the
output in a file:

```console
> RUSTC_LOG=rustc_hir_typeck::upvar rustc +stage1 -Z dump-mir=all \
    <.rs file to compile> 2> <file where the output will be dumped>
```

This uses the stage1 compiler and enables `debug!` logging for the
`rustc_hir_typeck::upvar` module.

The other option is to step through the code using lldb or gdb.

1. `rust-lldb build/host/stage1/bin/rustc test.rs`
2. In lldb:
    1. `b upvar.rs:134`  // Setting the breakpoint on a certain line in the upvar.rs file
    2. `r`  // Run the program until it hits the breakpoint

Let's start with [`upvar.rs`][upvar]. This file has something called
the [`euv::ExprUseVisitor`] which walks the source of the closure and
invokes a callback for each upvar that is borrowed, mutated, or moved.

[`euv::ExprUseVisitor`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/expr_use_visitor/struct.ExprUseVisitor.html

```rust
fn main() {
    let mut x = vec![21];
    let _cl = || {
        let y = x[0];  // 1.
        x[0] += 1;  // 2.
    };
}
```

In the above example, our visitor will be called twice, for the lines marked 1 and 2, once for a
shared borrow and another one for a mutable borrow. It will also tell us what was borrowed.

The callbacks are defined by implementing the [`Delegate`] trait. The
[`InferBorrowKind`][ibk] type implements `Delegate` and keeps a map that
records for each upvar which mode of capture was required. The modes of capture
can be `ByValue` (moved) or `ByRef` (borrowed). For `ByRef` borrows, the possible
[`BorrowKind`]s are `ImmBorrow`, `UniqueImmBorrow`, `MutBorrow` as defined in the
[`compiler/rustc_middle/src/ty/mod.rs`][middle_ty].

[`BorrowKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/enum.BorrowKind.html
[middle_ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/index.html

`Delegate` defines a few different methods (the different callbacks):
**consume** for *move* of a variable, **borrow** for a *borrow* of some kind
(shared or mutable), and **mutate** when we see an *assignment* of something.

All of these callbacks have a common argument *cmt* which stands for Category,
Mutability and Type and is defined in
[`compiler/rustc_hir_typeck/src/expr_use_visitor.rs`][cmt]. Borrowing from the code
comments, "`cmt` is a complete categorization of a value indicating where it
originated and how it is located, as well as the mutability of the memory in
which the value is stored". Based on the callback (consume, borrow etc.), we
will call the relevant `adjust_upvar_borrow_kind_for_<something>` and pass the
`cmt` along. Once the borrow type is adjusted, we store it in the table, which
basically says what borrows were made for each closure.

```rust,ignore
self.tables
    .borrow_mut()
    .upvar_capture_map
    .extend(delegate.adjust_upvar_captures);
```

[`Delegate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/expr_use_visitor/trait.Delegate.html
[ibk]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/upvar/struct.InferBorrowKind.html
[cmt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir_typeck/expr_use_visitor/index.html


---

# Async closures/"coroutine-closures"

Please read [RFC 3668](https://rust-lang.github.io/rfcs/3668-async-closures.html) to understand the general motivation of the feature. This is a very technical and somewhat "vertical" chapter; ideally we'd split this and sprinkle it across all the relevant chapters, but for the purposes of understanding async closures *holistically*, I've put this together all here in one chapter.

## Coroutine-closures -- a technical deep dive

Coroutine-closures are a generalization of async closures, being special syntax for closure expressions which return a coroutine, notably one that is allowed to capture from the closure's upvars.

For now, the only usable kind of coroutine-closure is the async closure, and supporting async closures is the extent of this PR. We may eventually support `gen || {}`, etc., and most of the problems and curiosities described in this document apply to all coroutine-closures in general.

As a consequence of the code being somewhat general, this document may flip between calling them "async closures" and "coroutine-closures". The future that is returned by the async closure will generally be called the "coroutine" or the "child coroutine".

### HIR

Async closures (and in the future, other coroutine flavors such as `gen`) are represented in HIR as a `hir::Closure`.
The closure-kind of the `hir::Closure` is `ClosureKind::CoroutineClosure(_)`[^k1], which wraps an async block, which is also represented in HIR as a `hir::Closure`.
The closure-kind of the async block is `ClosureKind::Closure(CoroutineKind::Desugared(_, CoroutineSource::Closure))`[^k2].

[^k1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_ast_lowering/src/expr.rs#L1147>

[^k2]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_ast_lowering/src/expr.rs#L1117>

Like `async fn`, when lowering an async closure's body, we need to unconditionally move all of the closures arguments into the body so they are captured. This is handled by `lower_coroutine_body_with_moved_arguments`[^l1]. The only notable quirk with this function is that the async block we end up generating as a capture kind of `CaptureBy::ByRef`[^l2]. We later force all of the *closure args* to be captured by-value[^l3], but we don't want the *whole* async block to act as if it were an `async move`, since that would defeat the purpose of the self-borrowing of an async closure.

[^l1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_ast_lowering/src/item.rs#L1096-L1100>

[^l2]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_ast_lowering/src/item.rs#L1276-L1279>

[^l3]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_hir_typeck/src/upvar.rs#L250-L256>

### `rustc_middle::ty` Representation

For the purposes of keeping the implementation mostly future-compatible (i.e. with gen `|| {}` and `async gen || {}`), most of this section calls async closures "coroutine-closures".

The main thing that this PR introduces is a new `TyKind` called `CoroutineClosure`[^t1] and corresponding variants on other relevant enums in typeck and borrowck (`UpvarArgs`, `DefiningTy`, `AggregateKind`).

[^t1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_type_ir/src/ty_kind.rs#L163-L168>

We introduce a new `TyKind` instead of generalizing the existing `TyKind::Closure` due to major representational differences in the type. The major differences between `CoroutineClosure`s can be explored by first inspecting the `CoroutineClosureArgsParts`, which is the "unpacked" representation of the coroutine-closure's generics.

#### Similarities to closures

Like a closure, we have `parent_args`, a `closure_kind_ty`, and a `tupled_upvars_ty`. These represent the same thing as their closure counterparts; namely: the generics inherited from the body that the closure is defined in, the maximum "calling capability" of the closure (i.e. must it be consumed to be called, like `FnOnce`, or can it be called by-ref), and the captured upvars of the closure itself.

#### The signature

A traditional closure has a `fn_sig_as_fn_ptr_ty` which it uses to represent the signature of the closure. In contrast, we store the signature of a coroutine closure in a somewhat "exploded" way, since coroutine-closures have *two* signatures depending on what `AsyncFn*` trait you call it with (see below sections).

Conceptually, the coroutine-closure may be thought as containing several different signature types depending on whether it is being called by-ref or by-move.

To conveniently recreate both of these signatures, the `signature_parts_ty` stores all of the relevant parts of the coroutine returned by this coroutine-closure. This signature parts type will have the general shape of `fn(tupled_inputs, resume_ty) -> (return_ty, yield_ty)`, where `resume_ty`, `return_ty`, and `yield_ty` are the respective types for the *coroutine* returned by the coroutine-closure[^c1].

[^c1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_type_ir/src/ty_kind/closure.rs#L221-L229>

The compiler mainly deals with the `CoroutineClosureSignature` type[^c2], which is created by extracting the relevant types out of the `fn()` ptr type described above, and which exposes methods that can be used to construct the *coroutine* that the coroutine-closure ultimately returns.

[^c2]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_type_ir/src/ty_kind/closure.rs#L362>

#### The data we need to carry along to construct a `Coroutine` return type

Along with the data stored in the signature, to construct a `TyKind::Coroutine` to return, we also need to store the "witness" of the coroutine.

So what about the upvars of the `Coroutine` that is returned? Well, for `AsyncFnOnce` (i.e. call-by-move), this is simply the same upvars that the coroutine returns. But for `AsyncFnMut`/`AsyncFn`, the coroutine that is returned from the coroutine-closure borrows data from the coroutine-closure with a given "environment" lifetime[^c3]. This corresponds to the `&self` lifetime[^c4] on the `AsyncFnMut`/`AsyncFn` call signature, and the GAT lifetime of the `ByRef`[^c5].

[^c3]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_type_ir/src/ty_kind/closure.rs#L447-L455>

[^c4]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/library/core/src/ops/async_function.rs#L36>

[^c5]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/library/core/src/ops/async_function.rs#L30>

#### Actually getting the coroutine return type(s)

To most easily construct the `Coroutine` that a coroutine-closure returns, you can use the `to_coroutine_given_kind_and_upvars`[^helper] helper on `CoroutineClosureSignature`, which can be acquired from the `CoroutineClosureArgs`.

[^helper]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_type_ir/src/ty_kind/closure.rs#L419>

Most of the args to that function will be components that you can get out of the `CoroutineArgs`, except for the `goal_kind: ClosureKind` which controls which flavor of coroutine to return based off of the `ClosureKind` passed in -- i.e. it will prepare the by-ref coroutine if `ClosureKind::Fn | ClosureKind::FnMut`, and the by-move coroutine if `ClosureKind::FnOnce`.

### Trait Hierarchy

We introduce a parallel hierarchy of `Fn*` traits that are implemented for . The motivation for the introduction was covered in a blog post: [Async Closures](https://hackmd.io/@compiler-errors/async-closures).

All currently-stable callable types (i.e., closures, function items, function pointers, and `dyn Fn*` trait objects) automatically implement `AsyncFn*() -> T` if they implement `Fn*() -> Fut` for some output type `Fut`, and `Fut` implements `Future<Output = T>`[^tr1].

[^tr1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_next_trait_solver/src/solve/assembly/structural_traits.rs#L404-L409>

Async closures implement `AsyncFn*` as their bodies permit; i.e. if they end up using upvars in a way that is compatible (i.e. if they consume or mutate their upvars, it may affect whether they implement `AsyncFn` and `AsyncFnMut`...)

#### Lending

We may in the future move `AsyncFn*` onto a more general set of `LendingFn*` traits; however, there are some concrete technical implementation details that limit our ability to use `LendingFn` ergonomically in the compiler today. These have to do with:

- Closure signature inference.
- Limitations around higher-ranked trait bounds.
- Shortcomings with error messages.

These limitations, plus the fact that the underlying trait should have no effect on the user experience of async closures and async `Fn` trait bounds, leads us to `AsyncFn*` for now. To ensure we can eventually move to these more general traits, the precise `AsyncFn*` trait definitions (including the associated types) are left as an implementation detail.

#### When do async closures implement the regular `Fn*` traits?

We mention above that "regular" callable types can implement `AsyncFn*`, but the reverse question exists of "can async closures implement `Fn*` too"? The short answer is "when it's valid", i.e. when the coroutine that would have been returned from `AsyncFn`/`AsyncFnMut` does not actually have any upvars that are "lent" from the parent coroutine-closure.

See the "follow-up: when do..." section below for an elaborated answer. The full answer describes a pretty interesting and hopefully thorough heuristic that is used to ensure that most async closures "just work".

### Tale of two bodies...

When async closures are called with `AsyncFn`/`AsyncFnMut`, they return a coroutine that borrows from the closure. However, when they are called via `AsyncFnOnce`, we consume that closure, and cannot return a coroutine that borrows from data that is now dropped.

To work around this limitation, we synthesize a separate by-move MIR body for calling `AsyncFnOnce::call_once` on a coroutine-closure that can be called by-ref.

This body operates identically to the "normal" coroutine returned from calling the coroutine-closure, except for the fact that it has a different set of upvars, since we must *move* the captures from the parent coroutine-closure into the child coroutine.

#### Synthesizing the by-move body

When we want to access the by-move body of the coroutine returned by a coroutine-closure, we can do so via the `coroutine_by_move_body_def_id`[^b1] query.

[^b1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_mir_transform/src/coroutine/by_move_body.rs#L1-L70>

This query synthesizes a new MIR body by copying the MIR body of the coroutine and inserting additional derefs and field projections[^b2] to preserve the semantics of the body.

[^b2]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_mir_transform/src/coroutine/by_move_body.rs#L131-L195>

Since we've synthesized a new def id, this query is also responsible for feeding a ton of other relevant queries for the MIR body. This query is `ensure()`d[^b3] during the `mir_promoted` query, since it operates on the *built* mir of the coroutine.

[^b3]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_mir_transform/src/lib.rs#L339-L342>

### Closure signature inference

The closure signature inference algorithm for async closures is a bit more complicated than the inference algorithm for "traditional" closures. Like closures, we iterate through all of the clauses that may be relevant (for the expectation type passed in)[^deduce1].

To extract a signature, we consider two situations:
* Projection predicates with `AsyncFnOnce::Output`, which we will use to extract the inputs and output type for the closure. This corresponds to the situation that there was a `F: AsyncFn*() -> T` bound[^deduce2].
* Projection predicates with `FnOnce::Output`, which we will use to extract the inputs. For the output, we also try to deduce an output by looking for relevant `Future::Output` projection predicates. This corresponds to the situation that there was an `F: Fn*() -> T, T: Future<Output = U>` bound.[^deduce3]
    * If there is no `Future` bound, we simply use a fresh infer var for the output. This corresponds to the case where one can pass an async closure to a combinator function like `Option::map`.[^deduce4]

[^deduce1]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_hir_typeck/src/closure.rs#L345-L362>

[^deduce2]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_hir_typeck/src/closure.rs#L486-L487>

[^deduce3]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_hir_typeck/src/closure.rs#L517-L534>

[^deduce4]: <https://github.com/rust-lang/rust/blob/5ca0e9fa9b2f92b463a0a2b0b34315e09c0b7236/compiler/rustc_hir_typeck/src/closure.rs#L575-L590>

We support the latter case simply to make it easier for users to simply drop-in `async || {}` syntax, even when they're calling an API that was designed before first-class `AsyncFn*` traits were available.

#### Calling a closure before its kind has been inferred

We defer[^call1] the computation of a coroutine-closure's "kind" (i.e. its maximum calling mode: `AsyncFnOnce`/`AsyncFnMut`/`AsyncFn`) until the end of typeck. However, since we want to be able to call that coroutine-closure before the end of typeck, we need to come up with the return type of the coroutine-closure before that.

[^call1]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_hir_typeck/src/callee.rs#L169-L210>

Unlike regular closures, whose return type does not change depending on what `Fn*` trait we call it with, coroutine-closures *do* end up returning different coroutine types depending on the flavor of `AsyncFn*` trait used to call it. 

Specifically, while the def-id of the returned coroutine does not change, the upvars[^call2] (which are either borrowed or moved from the parent coroutine-closure) and the coroutine-kind[^call3] are dependent on the calling mode.

[^call2]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_type_ir/src/ty_kind/closure.rs#L574-L576>

[^call3]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_type_ir/src/ty_kind/closure.rs#L554-L563>

We introduce a `AsyncFnKindHelper` trait which allows us to defer the question of "does this coroutine-closure support this calling mode"[^helper1] via a trait goal, and "what are the tupled upvars of this calling mode"[^helper2] via an associated type, which can be computed by appending the input types of the coroutine-closure to either the upvars or the "by ref" upvars computed during upvar analysis.

[^helper1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/library/core/src/ops/async_function.rs#L135-L144>

[^helper2]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/library/core/src/ops/async_function.rs#L146-L154>

#### Ok, so why?

This seems a bit roundabout and complex, and I admit that it is. But let's think of the "do nothing" alternative -- we could instead mark all `AsyncFn*` goals as ambiguous until upvar analysis, at which point we would know exactly what to put into the upvars of the coroutine we return. However, this is actually *very* detrimental to inference in the program, since it means that programs like this would not be valid:

```rust,ignore
let c = async || -> String { .. };
let s = c().await;
// ^^^ If we can't project `<{c} as AsyncFn>::call()` to a coroutine, then the `IntoFuture::into_future` call inside of the `.await` stalls, and the type of `s` is left unconstrained as an infer var.
s.as_bytes();
// ^^^ That means we can't call any methods on the awaited return of a coroutine-closure, like... at all!
```

So *instead*, we use this alias (in this case, a projection: `AsyncFnKindHelper::Upvars<'env, ...>`) to delay the computation of the *tupled upvars* and give us something to put in its place, while still allowing us to return a `TyKind::Coroutine` (which is a rigid type) and we may successfully confirm the built-in traits we need (in our case, `Future`), since the `Future` implementation doesn't depend on the upvars at all.

### Upvar analysis

By and large, the upvar analysis for coroutine-closures and their child coroutines proceeds like normal upvar analysis. However, there are several interesting bits that happen to account for async closures' special natures:

#### Forcing all inputs to be captured

Like async fn, all input arguments are captured. We explicitly force[^f1] all of these inputs to be captured by move so that the future coroutine returned by async closures does not depend on whether the input is *used* by the body or not, which would impart an interesting semver hazard.

[^f1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_hir_typeck/src/upvar.rs#L250-L259>

#### Computing the by-ref captures

For a coroutine-closure that supports `AsyncFn`/`AsyncFnMut`, we must also compute the relationship between the captures of the coroutine-closure and its child coroutine. Specifically, the coroutine-closure may `move` a upvar into its captures, but the coroutine may only borrow that upvar.

We compute the "`coroutine_captures_by_ref_ty`" by looking at all of the child coroutine's captures and comparing them to the corresponding capture of the parent coroutine-closure[^br1]. This `coroutine_captures_by_ref_ty` ends up being represented as a `for<'env> fn() -> captures...` type, with the additional binder lifetime representing the "`&self`" lifetime of calling `AsyncFn::async_call` or `AsyncFnMut::async_call_mut`. We instantiate that binder later when actually calling the methods.

[^br1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_hir_typeck/src/upvar.rs#L375-L471>

Note that not every by-ref capture from the parent coroutine-closure results in a "lending" borrow. See the **Follow-up: When do async closures implement the regular `Fn*` traits?** section below for more details, since this intimately influences whether or not the coroutine-closure is allowed to implement the `Fn*` family of traits.

#### By-move body + `FnOnce` quirk

There are several situations where the closure upvar analysis ends up inferring upvars for the coroutine-closure's child coroutine that are too relaxed, and end up resulting in borrow-checker errors. This is best illustrated via examples. For example, given:

```rust
fn force_fnonce<T: async FnOnce()>(t: T) -> T { t }

let x = String::new();
let c = force_fnonce(async move || {
    println!("{x}");
});
```

`x` will be moved into the coroutine-closure, but the coroutine that is returned would only borrow `&x`. However, since `force_fnonce` forces the coroutine-closure to `AsyncFnOnce`, which is not *lending*, we must force the capture to happen by-move[^bm1].

Similarly:

```rust
let x = String::new();
let y = String::new();
let c = async move || {
    drop(y);
    println!("{x}");
};
```

`x` will be moved into the coroutine-closure, but the coroutine that is returned would only borrow `&x`. However, since we also capture `y` and drop it, the coroutine-closure is forced to be `AsyncFnOnce`. We must also force the capture of `x` to happen by-move. To determine this situation in particular, since unlike the last example the coroutine-kind's closure-kind has not yet been constrained, we must analyze the body of the coroutine-closure to see if how all of the upvars are used, to determine if they've been used in a way that is "consuming" -- i.e. that would force it to `FnOnce`[^bm2].

[^bm1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_hir_typeck/src/upvar.rs#L211-L248>

[^bm2]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_hir_typeck/src/upvar.rs#L532-L539>

#### Follow-up: When do async closures implement the regular `Fn*` traits?

Well, first of all, all async closures implement `FnOnce` since they can always be called *at least once*.

For `Fn`/`FnMut`, the detailed answer involves answering a related question: is the coroutine-closure lending? Because if it is, then it cannot implement the non-lending `Fn`/`FnMut` traits.

Determining when the coroutine-closure must *lend* its upvars is implemented in the `should_reborrow_from_env_of_parent_coroutine_closure` helper function[^u1]. Specifically, this needs to happen in two places:

[^u1]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_hir_typeck/src/upvar.rs#L1818-L1860>

1.  Are we borrowing data owned by the parent closure? We can determine if that is the case by checking if the parent capture is by-move, EXCEPT if we apply a deref projection, which means we're reborrowing a reference that we captured by-move.

```rust
let x = &1i32; // Let's call this lifetime `'1`.
let c = async move || {
    println!("{:?}", *x);
    // Even though the inner coroutine borrows by ref, we're only capturing `*x`,
    // not `x`, so the inner closure is allowed to reborrow the data for `'1`.
};
```

2. If a coroutine is mutably borrowing from a parent capture, then that mutable borrow cannot live for longer than either the parent *or* the borrow that we have on the original upvar. Therefore we always need to borrow the child capture with the lifetime of the parent coroutine-closure's env.

```rust
let mut x = 1i32;
let c = async || {
    x = 1;
    // The parent borrows `x` for some `&'1 mut i32`.
    // However, when we call `c()`, we implicitly autoref for the signature of
    // `AsyncFnMut::async_call_mut`. Let's call that lifetime `'call`. Since
    // the maximum that `&'call mut &'1 mut i32` can be reborrowed is `&'call mut i32`,
    // the inner coroutine should capture w/ the lifetime of the coroutine-closure.
};
```

If either of these cases apply, then we should capture the borrow with the lifetime of the parent coroutine-closure's env. Luckily, if this function is not correct, then the program is not unsound, since we still borrowck and validate the choices made from this function -- the only side-effect is that the user may receive unnecessary borrowck errors.

### Instance resolution

If a coroutine-closure has a closure-kind of `FnOnce`, then its `AsyncFnOnce::call_once` and `FnOnce::call_once` implementations resolve to the coroutine-closure's body[^res1], and the `Future::poll` of the coroutine that gets returned resolves to the body of the child closure.

[^res1]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_ty_utils/src/instance.rs#L351>

If a coroutine-closure has a closure-kind of `FnMut`/`Fn`, then the same applies to `AsyncFn` and the corresponding `Future` implementation of the coroutine that gets returned.[^res1] However, we use a MIR shim to generate the implementation of `AsyncFnOnce::call_once`/`FnOnce::call_once`[^res2], and `Fn::call`/`FnMut::call_mut` instances if they exist[^res3].

[^res2]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_ty_utils/src/instance.rs#L341-L349>

[^res3]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_ty_utils/src/instance.rs#L312-L326>

This is represented by the `ConstructCoroutineInClosureShim`[^i1]. The `receiver_by_ref` bool will be true if this is the instance of `Fn::call`/`FnMut::call_mut`.[^i2] The coroutine that all of these instances returns corresponds to the by-move body we will have synthesized by this point.[^i3]

[^i1]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_middle/src/ty/instance.rs#L129-L134>

[^i2]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_middle/src/ty/instance.rs#L136-L141>

[^i3]: <https://github.com/rust-lang/rust/blob/07cbbdd69363da97075650e9be24b78af0bcdd23/compiler/rustc_middle/src/ty/instance.rs#L841>

### Borrow-checking

It turns out that borrow-checking async closures is pretty straightforward. After adding a new `DefiningTy::CoroutineClosure`[^bck1] variant, and teaching borrowck how to generate the signature of the coroutine-closure[^bck2], borrowck proceeds totally fine.

One thing to note is that we don't borrow-check the synthetic body we make for by-move coroutines, since by construction (and the validity of the by-ref coroutine body it was derived from) it must be valid.

[^bck1]: <https://github.com/rust-lang/rust/blob/705cfe0e966399e061d64dd3661bfbc57553ed87/compiler/rustc_borrowck/src/universal_regions.rs#L110-L115>

[^bck2]: <https://github.com/rust-lang/rust/blob/7c7bb7dc017545db732f5cffec684bbaeae0a9a0/compiler/rustc_borrowck/src/universal_regions.rs#L743-L790>
