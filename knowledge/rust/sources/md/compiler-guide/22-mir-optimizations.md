# From MIR to binaries

All of the preceding chapters of this guide have one thing in common:
we never generated any executable machine code at all!
With this chapter, all of that changes.

So far,
we've shown how the compiler can take raw source code in text format
and transform it into [MIR].
We have also shown how the compiler does various
analyses on the code to detect things like type or lifetime errors.
Now, we will finally take the MIR and produce some executable machine code.

[MIR]: ./mir/index.md

> NOTE: This part of a compiler is often called the _backend_.
> The term is a bit overloaded because in the compiler source,
> it usually refers to the "codegen backend" (i.e. LLVM, Cranelift, or GCC).
> Usually, when you see the word "backend"  in this part,
> we are referring to the "codegen backend".

So what do we need to do?

1. First, we need to collect the set of things to generate code for.
   In particular,
   we need to find out which concrete types to substitute for generic ones,
   since we need to generate code for the concrete types.
   Generating code for the concrete types
   (i.e. emitting a copy of the code for each concrete type) is called _monomorphization_,
   so the process of collecting all the concrete types is called _monomorphization collection_.
2. Next, we need to actually lower the MIR to a codegen IR
   (usually LLVM IR) for each concrete type we collected.
3. Finally, we need to invoke the codegen backend,
   which runs a bunch of optimization passes,
   generates executable code,
   and links together an executable binary.

[codegen1]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/fn.codegen_crate.html

The code for codegen is actually a bit complex due to a few factors:

- Support for multiple codegen backends (LLVM, Cranelift, and GCC).
  We try to share as much backend code between them as possible,
  so a lot of it is generic over the codegen implementation.
  This means that there are often a lot of layers of abstraction.
- Codegen happens asynchronously in another thread for performance.
- The actual codegen is done by a third-party library (either of the 3 backends).

Generally, the [`rustc_codegen_ssa`][ssa] crate contains backend-agnostic code,
while the [`rustc_codegen_llvm`][llvm] crate contains code specific to LLVM codegen.

[ssa]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/index.html
[llvm]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_llvm/index.html

At a very high level, the entry point is
[`rustc_codegen_ssa::base::codegen_crate`][codegen1].
This function starts the process discussed in the rest of this chapter.


---

# MIR optimizations

MIR optimizations are optimizations run on the [MIR][mir] to produce better MIR
before codegen. This is important for two reasons: first, it makes the final
generated executable code better, and second, it means that LLVM has less work
to do, so compilation is faster. Note that since MIR is generic (not
[monomorphized][monomorph] yet), these optimizations are particularly
effective; we can optimize the generic version, so all of the monomorphizations
are cheaper!

[mir]: ../mir/index.md
[monomorph]: ../appendix/glossary.md#mono

MIR optimizations run after borrow checking. We run a series of optimization
passes over the MIR to improve it. Some passes are required to run on all code,
some passes don't actually do optimizations but only check stuff, and some
passes are only turned on in `release` mode.

The [`optimized_mir`][optmir] [query] is called to produce the optimized MIR
for a given [`DefId`][defid]. This query makes sure that the borrow checker has
run and that some validation has occurred. Then, it [steals][steal] the MIR,
optimizes it, and returns the improved MIR.

[optmir]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/fn.optimized_mir.html
[query]: ../query.md
[defid]: ../appendix/glossary.md#def-id
[steal]: ../mir/passes.md#stealing

## Quickstart for adding a new optimization

1. Make a Rust source file in `tests/mir-opt` that shows the code you want to
   optimize. This should be kept simple, so avoid `println!` or other formatting
   code if it's not necessary for the optimization. The reason for this is that
   `println!`, `format!`, etc. generate a lot of MIR that can make it harder to
   understand what the optimization does to the test.

2. Run `./x test --bless tests/mir-opt/<your-test>.rs` to generate a MIR
   dump. Read [this README][mir-opt-test-readme] for instructions on how to dump
   things.

3. Commit the current working directory state. The reason you should commit the
   test output before you implement the optimization is so that you (and your
   reviewers) can see a before/after diff of what the optimization changed.

4. Implement a new optimization in [`compiler/rustc_mir_transform/src`].
   The fastest and easiest way to do this is to

   1. pick a small optimization (such as [`remove_storage_markers`]) and copy it
      to a new file,
   2. add your optimization to one of the lists in the
      [`run_optimization_passes()`] function,
   3. and then start modifying the copied optimization.

5. Rerun `./x test --bless tests/mir-opt/<your-test>.rs` to regenerate the
   MIR dumps. Look at the diffs to see if they are what you expect.

6. Run `./x test tests/ui` to see if your optimization broke anything.

7. If there are issues with your optimization, experiment with it a bit and
   repeat steps 5 and 6.

8. Commit and open a PR. You can do this at any point, even if things aren't
   working yet, so that you can ask for feedback on the PR. Open a "WIP" PR
   (just prefix your PR title with `[WIP]` or otherwise note that it is a
   work in progress) in that case.

   Make sure to commit the blessed test output as well! It's necessary for CI to
   pass and it's very helpful to reviewers.

If you have any questions along the way, feel free to ask in
`#t-compiler/wg-mir-opt` on Zulip.

[mir-opt-test-readme]: https://github.com/rust-lang/rust/blob/HEAD/tests/mir-opt/README.md
[`compiler/rustc_mir_transform/src`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_mir_transform/src
[`remove_storage_markers`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_mir_transform/src/remove_storage_markers.rs
[`run_optimization_passes()`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/fn.run_optimization_passes.html

## Defining optimization passes

The list of passes run and the order in which they are run is defined by the
[`run_optimization_passes`][rop] function. It contains an array of passes to
run.  Each pass in the array is a struct that implements the [`MirPass`] trait.
The array is an array of `&dyn MirPass` trait objects. Typically, a pass is
implemented in its own module of the [`rustc_mir_transform`][trans] crate.

[rop]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/fn.run_optimization_passes.html
[`MirPass`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/pass_manager/trait.MirPass.html
[trans]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/index.html

Some examples of passes are:
- `CleanupPostBorrowck`: Remove some of the info that is only needed for
  analyses, rather than codegen.
- `ConstProp`: Does [constant propagation][constprop].

You can see the ["Implementors" section of the `MirPass` rustdocs][impl] for more examples.

[impl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/pass_manager/trait.MirPass.html#implementors
[constprop]: https://en.wikipedia.org/wiki/Constant_folding#Constant_propagation

## MIR optimization levels

MIR optimizations can come in various levels of readiness. Experimental
optimizations may cause miscompilations, or slow down compile times.
These passes are still included in nightly builds to gather feedback and make it easier to modify
the pass. To enable working with slow or otherwise experimental optimization passes,
you can specify the `-Z mir-opt-level` debug flag. You can find the
definitions of the levels in the [compiler MCP]. If you are developing a MIR pass and
want to query whether your optimization pass should run, you can check the
current level using [`tcx.sess.opts.unstable_opts.mir_opt_level`][mir_opt_level].

[compiler MCP]: https://github.com/rust-lang/compiler-team/issues/319
[mir_opt_level]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/config/struct.UnstableOptions.html#structfield.mir_opt_level


---

# MIR Debugging

The `-Z dump-mir` flag can be used to dump a text representation of the MIR.
The following optional flags, used in combination with `-Z dump-mir`, enable
additional output formats, including:

* `-Z dump-mir-graphviz` - dumps a `.dot` file that represents MIR as a
control-flow graph
* `-Z dump-mir-dataflow` - dumps a `.dot` file showing the [dataflow state] at
  each point in the control-flow graph

`-Z dump-mir=F` is a handy compiler option that will let you view the MIR for
each function at each stage of compilation. `-Z dump-mir` takes a **filter** `F`
which allows you to control which functions and which passes you are
interested in. For example:

```bash
> rustc -Z dump-mir=foo ...
```

This will dump the MIR for any function whose name contains `foo`; it
will dump the MIR both before and after every pass. Those files will
be created in the `mir_dump` directory. There will likely be quite a
lot of them!

```bash
> cat > foo.rs
fn main() {
    println!("Hello, world!");
}
^D
> rustc -Z dump-mir=main foo.rs
> ls mir_dump/* | wc -l
     161
```

The files have names like `rustc.main.000-000.CleanEndRegions.after.mir`. These
names have a number of parts:

```text
rustc.main.000-000.CleanEndRegions.after.mir
      ---- --- --- --------------- ----- either before or after
      |    |   |   name of the pass
      |    |   index of dump within the pass (usually 0, but some passes dump intermediate states)
      |    index of the pass
      def-path to the function etc being dumped
```

You can also make more selective filters. For example, `main & CleanEndRegions`
will select for things that reference *both* `main` and the pass
`CleanEndRegions`:

```bash
> rustc -Z dump-mir='main & CleanEndRegions' foo.rs
> ls mir_dump
rustc.main.000-000.CleanEndRegions.after.mir	rustc.main.000-000.CleanEndRegions.before.mir
```
<!--- TODO: Change NoLandingPads. [#1232](https://github.com/rust-lang/rustc-dev-guide/issues/1232) -->
Filters can also have `|` parts to combine multiple sets of
`&`-filters. For example `main & CleanEndRegions | main &
NoLandingPads` will select *either* `main` and `CleanEndRegions` *or*
`main` and `NoLandingPads`:

```bash
> rustc -Z dump-mir='main & CleanEndRegions | main & NoLandingPads' foo.rs
> ls mir_dump
rustc.main-promoted[0].002-000.NoLandingPads.after.mir
rustc.main-promoted[0].002-000.NoLandingPads.before.mir
rustc.main-promoted[0].002-006.NoLandingPads.after.mir
rustc.main-promoted[0].002-006.NoLandingPads.before.mir
rustc.main-promoted[1].002-000.NoLandingPads.after.mir
rustc.main-promoted[1].002-000.NoLandingPads.before.mir
rustc.main-promoted[1].002-006.NoLandingPads.after.mir
rustc.main-promoted[1].002-006.NoLandingPads.before.mir
rustc.main.000-000.CleanEndRegions.after.mir
rustc.main.000-000.CleanEndRegions.before.mir
rustc.main.002-000.NoLandingPads.after.mir
rustc.main.002-000.NoLandingPads.before.mir
rustc.main.002-006.NoLandingPads.after.mir
rustc.main.002-006.NoLandingPads.before.mir
```

(Here, the `main-promoted[0]` files refer to the MIR for "promoted constants"
that appeared within the `main` function.)

The `-Z unpretty=mir-cfg` flag can be used to create a graphviz MIR
control-flow diagram for the whole crate:

![A control-flow diagram](mir_cfg.svg)

TODO: anything else?

[dataflow state]: ./dataflow.html#graphviz-diagrams


---

# Constant Evaluation

Constant evaluation is the process of computing values at compile time. For a
specific item (constant/static/array length) this happens after the MIR for the
item is borrow-checked and optimized. In many cases trying to const evaluate an
item will trigger the computation of its MIR for the first time.

Prominent examples are:

* The initializer of a `static`
* Array length
    * needs to be known to reserve stack or heap space
* Enum variant discriminants
    * needs to be known to prevent two variants from having the same
      discriminant
* Patterns
    * need to be known to check for overlapping patterns

Additionally constant evaluation can be used to reduce the workload or binary
size at runtime by precomputing complex operations at compile time and only
storing the result.

All uses of constant evaluation can either be categorized as "influencing the type system"
(array lengths, enum variant discriminants, const generic parameters), or as solely being
done to precompute expressions to be used at runtime.

Constant evaluation can be done by calling the `const_eval_*` functions of `TyCtxt`.
They're the wrappers of the `const_eval` query.

* `const_eval_global_id_for_typeck` evaluates a constant to a valtree,
  so the result value can be further inspected by the compiler.
* `const_eval_global_id` evaluate a constant to an "opaque blob" containing its final value;
  this is only useful for codegen backends and the CTFE evaluator engine itself.
* `eval_static_initializer` specifically computes the initial values of a static.
  Statics are special; all other functions do not represent statics correctly
  and have thus assertions preventing their use on statics.

The `const_eval_*` functions use a [`ParamEnv`](./typing-parameter-envs.md) of environment
in which the constant is evaluated (e.g. the function within which the constant is used)
and a [`GlobalId`]. The `GlobalId` is made up of an `Instance` referring to a constant
or static or of an `Instance` of a function and an index into the function's `Promoted` table.

Constant evaluation returns an [`EvalToValTreeResult`] for type system constants
or [`EvalToConstValueResult`] with either the error, or a representation of the
evaluated constant: a [valtree](mir/index.md#valtrees) or a [MIR constant
value](mir/index.md#mir-constant-values), respectively.

[`GlobalId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/struct.GlobalId.html
[`EvalToConstValueResult`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/error/type.EvalToConstValueResult.html
[`EvalToValTreeResult`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/error/type.EvalToValTreeResult.html


---

# Interpreter

The interpreter is a virtual machine for executing MIR without compiling to
machine code.
It is usually invoked via `tcx.const_eval_*` functions.
The interpreter is shared between the compiler (for compile-time function
evaluation, CTFE) and the tool [Miri](https://github.com/rust-lang/miri/), which
uses the same virtual machine to detect Undefined Behavior in (unsafe) Rust
code.

If you start out with a constant:

```rust
const FOO: usize = 1 << 12;
```

rustc doesn't actually invoke anything until the constant is either used or
placed into metadata.

Once you have a use-site like:

```rust,ignore
type Foo = [u8; FOO - 42];
```

The compiler needs to figure out the length of the array before being able to
create items that use the type (locals, constants, function arguments, ...).

To obtain the (in this case empty) parameter environment, one can call
`let param_env = tcx.param_env(length_def_id);`.
The `GlobalId` needed is

```rust,ignore
let gid = GlobalId {
    promoted: None,
    instance: Instance::mono(length_def_id),
};
```

Invoking `tcx.const_eval(param_env.and(gid))` will now trigger the creation of
the MIR of the array length expression.
The MIR will look something like this:

```mir
Foo::{{constant}}#0: usize = {
    let mut _0: usize;
    let mut _1: (usize, bool);

    bb0: {
        _1 = CheckedSub(const FOO, const 42usize);
        assert(!move (_1.1: bool), "attempt to subtract with overflow") -> bb1;
    }

    bb1: {
        _0 = move (_1.0: usize);
        return;
    }
}
```

Before the evaluation, a virtual memory location (in this case essentially a
`vec![u8; 4]` or `vec![u8; 8]`) is created for storing the evaluation result.

At the start of the evaluation, `_0` and `_1` are
`Operand::Immediate(Immediate::Scalar(ScalarMaybeUndef::Undef))`.
This is quite
a mouthful: [`Operand`] can represent either data stored somewhere in the
[interpreter memory](#memory) (`Operand::Indirect`), or (as an optimization)
immediate data stored in-line.
And [`Immediate`] can either be a single
(potentially uninitialized) [scalar value][`Scalar`] (integer or thin pointer),
or a pair of two of them.
In our case, the single scalar value is *not* (yet) initialized.

When the initialization of `_1` is invoked, the value of the `FOO` constant is
required, and triggers another call to `tcx.const_eval_*`, which will not be shown
here.
If the evaluation of FOO is successful, `42` will be subtracted from its
value `4096` and the result stored in `_1` as
`Operand::Immediate(Immediate::ScalarPair(Scalar::Raw { data: 4054, .. },
Scalar::Raw { data: 0, .. })`.
The first part of the pair is the computed value,
the second part is a bool that's true if an overflow happened.
A `Scalar::Raw`
also stores the size (in bytes) of this scalar value; we are eliding that here.

The next statement asserts that said boolean is `0`.
In case the assertion
fails, its error message is used for reporting a compile-time error.

Since it does not fail, `Operand::Immediate(Immediate::Scalar(Scalar::Raw {
data: 4054, .. }))` is stored in the virtual memory it was allocated before the
evaluation.
`_0` always refers to that location directly.

After the evaluation is done, the return value is converted from [`Operand`] to
[`ConstValue`] by [`op_to_const`]: the former representation is geared towards
what is needed *during* const evaluation, while [`ConstValue`] is shaped by the
needs of the remaining parts of the compiler that consume the results of const
evaluation.
As part of this conversion, for types with scalar values, even if
the resulting [`Operand`] is `Indirect`, it will return an immediate
`ConstValue::Scalar(computed_value)` (instead of the usual `ConstValue::Indirect`).
This makes using the result much more efficient and also more convenient, as no
further queries need to be executed in order to get at something as simple as a
`usize`.

Future evaluations of the same constants will not actually invoke
the interpreter, but just use the cached result.

[`Operand`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/operand/enum.Operand.html
[`Immediate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/enum.Immediate.html
[`ConstValue`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/consts/enum.ConstValue.html
[`Scalar`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/enum.Scalar.html
[`op_to_const`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/const_eval/eval_queries/fn.op_to_const.html

## Datastructures

The interpreter's outside-facing datastructures can be found in
[rustc_middle/src/mir/interpret](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_middle/src/mir/interpret).
This is mainly the error enum and the [`ConstValue`] and [`Scalar`] types.
A `ConstValue` can be either `Scalar` (a single `Scalar`, i.e., integer or thin
pointer), `Slice` (to represent byte slices and strings, as needed for pattern
matching) or `Indirect`, which is used for anything else and refers to a virtual
allocation.
These allocations can be accessed via the methods on `tcx.interpret_interner`.
A `Scalar` is either some `Raw` integer or a pointer;
see [the next section](#memory) for more on that.

If you are expecting a numeric result, you can use `eval_usize` (panics on
anything that can't be represented as a `u64`) or `try_eval_usize` which results
in an `Option<u64>` yielding the `Scalar` if possible.

## Memory

To support any kind of pointers, the interpreter needs to have a "virtual memory" that the
pointers can point to.
This is implemented in the [`Memory`] type.
In the simplest model, every global variable, stack variable and every dynamic
allocation corresponds to an [`Allocation`] in that memory.
(Actually using an
allocation for every MIR stack variable would be very inefficient; that's why we
have `Operand::Immediate` for stack variables that are both small and never have
their address taken.
But that is purely an optimization.)

Such an `Allocation` is basically just a sequence of `u8` storing the value of
each byte in this allocation.
(Plus some extra data, see below.)  Every
`Allocation` has a globally unique `AllocId` assigned in `Memory`.
With that, a
[`Pointer`] consists of a pair of an `AllocId` (indicating the allocation) and
an offset into the allocation (indicating which byte of the allocation the
pointer points to).
It may seem odd that a `Pointer` is not just an integer
address, but remember that during const evaluation, we cannot know at which
actual integer address the allocation will end up -- so we use `AllocId` as
symbolic base addresses, which means we need a separate offset.
(As an aside,
it turns out that pointers at run-time are
[more than just integers, too](https://rust-lang.github.io/unsafe-code-guidelines/glossary.html#pointer-provenance).)

These allocations exist so that references and raw pointers have something to
point to.
There is no global linear heap in which things are allocated, but each
allocation (be it for a local variable, a static or a (future) heap allocation)
gets its own little memory with exactly the required size.
So if you have a
pointer to an allocation for a local variable `a`, there is no possible (no
matter how unsafe) operation that you can do that would ever change said pointer
to a pointer to a different local variable `b`.
Pointer arithmetic on `a` will only ever change its offset; the `AllocId` stays the same.

This, however, causes a problem when we want to store a `Pointer` into an
`Allocation`: we cannot turn it into a sequence of `u8` of the right length!
`AllocId` and offset together are twice as big as a pointer "seems" to be.
This is what the `relocation` field of `Allocation` is for: the byte offset of the
`Pointer` gets stored as a bunch of `u8`, while its `AllocId` gets stored
out-of-band.
The two are reassembled when the `Pointer` is read from memory.
The other bit of extra data an `Allocation` needs is `undef_mask` for keeping
track of which of its bytes are initialized.

### Global memory and exotic allocations

`Memory` exists only during evaluation; it gets destroyed when the
final value of the constant is computed.
In case that constant contains any
pointers, those get "interned" and moved to a global "const eval memory" that is
part of `TyCtxt`.
These allocations stay around for the remaining computation
and get serialized into the final output (so that dependent crates can use
them).

Moreover, to also support function pointers, the global memory in `TyCtxt` can
also contain "virtual allocations": instead of an `Allocation`, these contain an
`Instance`.
That allows a `Pointer` to point to either normal data or a
function, which is needed to be able to evaluate casts from function pointers to
raw pointers.

Finally, the [`GlobalAlloc`] type used in the global memory also contains a
variant `Static` that points to a particular `const` or `static` item.
This is needed to support circular statics, where we need to have a `Pointer` to a
`static` for which we cannot yet have an `Allocation` as we do not know the
bytes of its value.

[`Memory`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.Memory.html
[`Allocation`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/struct.Allocation.html
[`Pointer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/struct.Pointer.html
[`GlobalAlloc`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/interpret/enum.GlobalAlloc.html

### Pointer values vs Pointer types

One common cause of confusion in the interpreter is that being a pointer *value* and having
a pointer *type* are entirely independent properties.
By "pointer value", we
refer to a `Scalar::Ptr` containing a `Pointer` and thus pointing somewhere into
the interpreter's virtual memory.
This is in contrast to `Scalar::Raw`, which is just some concrete integer.

However, a variable of pointer or reference *type*, such as `*const T` or `&T`,
does not have to have a pointer *value*: it could be obtained by casting or
transmuting an integer to a pointer.
And similarly, when casting or transmuting a reference to some
actual allocation to an integer, we end up with a pointer *value*
(`Scalar::Ptr`) at integer *type* (`usize`).
 This is a problem because we
cannot meaningfully perform integer operations such as division on pointer
values.

## Interpretation

Although the main entry point to constant evaluation is the `tcx.const_eval_*`
functions, there are additional functions in
[rustc_const_eval/src/const_eval](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/index.html)
that allow accessing the fields of a `ConstValue` (`Indirect` or otherwise).
You should
never have to access an `Allocation` directly except for translating it to the
compilation target (at the moment just LLVM).

The interpreter starts by creating a virtual stack frame for the current constant that is
being evaluated.
There's essentially no difference between a constant and a
function with no arguments, except that constants do not allow local (named)
variables at the time of writing this guide.

A stack frame is defined by the `Frame` type in
[rustc_const_eval/src/interpret/eval_context.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_const_eval/src/interpret/eval_context.rs)
and contains all the local variables memory (`None` at the start of evaluation).
Each frame refers to the
evaluation of either the root constant or subsequent calls to `const fn`.
The evaluation of another constant simply calls `tcx.const_eval_*`, which produce an
entirely new and independent stack frame.

The frames are just a `Vec<Frame>`, there's no way to actually refer to a
`Frame`'s memory even if horrible shenanigans are done via unsafe code.
The only memory that can be referred to are `Allocation`s.

The interpreter now calls the `step` method (in
[rustc_const_eval/src/interpret/step.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_const_eval/src/interpret/step.rs)
) until it either returns an error or has no further statements to execute.
Each statement will now initialize or modify the locals or the virtual memory
referred to by a local.
This might require evaluating other constants or
statics, which just recursively invokes `tcx.const_eval_*`.


---

# Monomorphization

As you probably know, Rust has a very expressive type system that has extensive
support for generic types. But of course, assembly is not generic, so we need
to figure out the concrete types of all the generics before the code can
execute.

Different languages handle this problem differently. For example, in some
languages, such as Java, we may not know the most precise type of value until
runtime. In the case of Java, this is ok because (almost) all variables are
reference values anyway (i.e. pointers to a heap allocated object). This
flexibility comes at the cost of performance, since all accesses to an object
must dereference a pointer.

Rust takes a different approach: it _monomorphizes_ all generic types. This
means that compiler stamps out a different copy of the code of a generic
function for each concrete type needed. For example, if I use a `Vec<u64>` and
a `Vec<String>` in my code, then the generated binary will have two copies of
the generated code for `Vec`: one for `Vec<u64>` and another for `Vec<String>`.
The result is fast programs, but it comes at the cost of compile time (creating
all those copies can take a while) and binary size (all those copies might take
a lot of space).

Monomorphization is the first step in the backend of the Rust compiler.

## Collection

First, we need to figure out what concrete types we need for all the generic
things in our program. This is called _collection_, and the code that does this
is called the _monomorphization collector_.

Take this example:

```rust
fn banana() {
   peach::<u64>();
}

fn main() {
    banana();
}
```

The monomorphization collector will give you a list of `[main, banana,
peach::<u64>]`. These are the functions that will have machine code generated
for them. Collector will also add things like statics to that list.

See [the collector rustdocs][collect] for more info.

[collect]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_monomorphize/collector/index.html

The monomorphization collector is run just before MIR lowering and codegen.
[`rustc_codegen_ssa::base::codegen_crate`][codegen1] calls the
[`collect_and_partition_mono_items`][mono] query, which does monomorphization
collection and then partitions them into [codegen
units](../appendix/glossary.md#codegen-unit).

## Codegen Unit (CGU) partitioning

For better incremental build times, the CGU partitioner creates two CGU for each source level
modules. One is for "stable" i.e. non-generic code and the other is more volatile code i.e.
monomorphized/specialized instances.

For dependencies, consider Crate A and Crate B, such that Crate B depends on Crate A.
The following table lists different scenarios for a function in Crate A that might be used by one
or more modules in Crate B.

| Crate A function | Behavior |
| - | - |
| Non-generic function | Crate A function doesn't appear in any codegen units of Crate B |
| Non-generic `#[inline]` function |  Crate A function appears within a single CGU  of Crate B, and exists even after post-inlining stage|
| Generic function |  Regardless of inlining, all monomorphized (specialized) functions <br> from Crate A appear within a single codegen unit for Crate B. <br> The codegen unit exists even after the post inlining stage.|
| Generic `#[inline]` function |   - same - |

For more details about the partitioner read the module level [documentation].

[mono]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_monomorphize/partitioning/fn.collect_and_partition_mono_items.html
[codegen1]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/fn.codegen_crate.html
[documentation]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_monomorphize/partitioning/index.html


---

# Lowering MIR to a Codegen IR

Now that we have a list of symbols to generate from the collector, we need to
generate some sort of codegen IR. In this chapter, we will assume LLVM IR,
since that's what rustc usually uses. The actual monomorphization is performed
as we go, while we do the translation.

Recall that the backend is started by
[`rustc_codegen_ssa::base::codegen_crate`][codegen1]. Eventually, this reaches
[`rustc_codegen_ssa::mir::codegen_mir`][codegen2], which does the lowering from
MIR to LLVM IR.

[codegen1]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/fn.codegen_crate.html
[codegen2]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/fn.codegen_mir.html

The code is split into modules which handle particular MIR primitives:

- [`rustc_codegen_ssa::mir::block`][mirblk] will deal with translating
  blocks and their terminators.  The most complicated and also the most
  interesting thing this module does is generating code for function calls,
  including the necessary unwinding handling IR.
- [`rustc_codegen_ssa::mir::statement`][mirst] translates MIR statements.
- [`rustc_codegen_ssa::mir::operand`][mirop] translates MIR operands.
- [`rustc_codegen_ssa::mir::place`][mirpl] translates MIR place references.
- [`rustc_codegen_ssa::mir::rvalue`][mirrv] translates MIR r-values.

[mirblk]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/block/index.html
[mirst]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/statement/index.html
[mirop]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/operand/index.html
[mirpl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/place/index.html
[mirrv]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/rvalue/index.html

Before a function is translated a number of simple and primitive analysis
passes will run to help us generate simpler and more efficient LLVM IR. An
example of such an analysis pass would be figuring out which variables are
SSA-like, so that we can translate them to SSA directly rather than relying on
LLVM's `mem2reg` for those variables. The analysis can be found in
[`rustc_codegen_ssa::mir::analyze`][mirana].

[mirana]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/analyze/index.html

Usually a single MIR basic block will map to a LLVM basic block, with very few
exceptions: intrinsic or function calls and less basic MIR statements like
`assert` can result in multiple basic blocks. This is a perfect lede into the
non-portable LLVM-specific part of the code generation. Intrinsic generation is
fairly easy to understand as it involves very few abstraction levels in between
and can be found in [`rustc_codegen_llvm::intrinsic`][llvmint].

[llvmint]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_llvm/intrinsic/index.html

Everything else will use the [builder interface][builder]. This is the code that gets
called in the [`rustc_codegen_ssa::mir::*`][ssamir] modules discussed above.

[builder]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_llvm/builder/index.html
[ssamir]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/index.html

> TODO: discuss how constants are generated
