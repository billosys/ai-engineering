# High-Level Compiler Architecture

The remaining parts of this guide discuss how the compiler works. They go
through everything from high-level structure of the compiler to how each stage
of compilation works. They should be friendly to both readers interested in the
end-to-end process of compilation _and_ readers interested in learning about a
specific system they wish to contribute to. If anything is unclear, feel free
to file an issue on the [rustc-dev-guide
repo](https://github.com/rust-lang/rustc-dev-guide/issues) or contact the compiler
team, as detailed in [this chapter from Part 1](./compiler-team.md).

In this part, we will look at the high-level architecture of the compiler. In
particular, we will look at three overarching design choices that impact the
whole compiler: the query system, incremental compilation, and interning.


---

# Overview of the compiler

This chapter is about the overall process of compiling a program -- how everything fits together.

The Rust compiler is special in two ways: it does things to your code that
other compilers don't do (e.g. borrow-checking) and it has a lot of
unconventional implementation choices (e.g. queries).
We will talk about these in turn in this chapter, and in the rest of the guide, we will look at the
individual pieces in more detail.

## What the compiler does to your code

So first, let's look at what the compiler does to your code.
For now, we will avoid mentioning how the compiler implements these steps except as needed.

### Invocation

Compilation begins when a user writes a Rust source program in text and invokes
the `rustc` compiler on it.
The work that the compiler needs to perform is defined by command-line options.
For example, it is possible to enable nightly
features (`-Z` flags), perform `check`-only builds, or emit the LLVM
Intermediate Representation (`LLVM-IR`) rather than executable machine code.
The `rustc` executable call may be indirect through the use of `cargo`.

Command line argument parsing occurs in the [`rustc_driver`].
This crate defines the compile configuration that is requested by the user and passes it
to the rest of the compilation process as a [`rustc_interface::Config`].

### Lexing and parsing

The raw Rust source text is analyzed by a low-level *lexer* located in [`rustc_lexer`].
At this stage, the source text is turned into a stream of
atomic source code units known as _tokens_.
 The `lexer` supports the Unicode character encoding.

The token stream passes through a higher-level lexer located in
[`rustc_parse`] to prepare for the next stage of the compile process.
The [`Lexer`] `struct` is used at this stage to perform a set of validations
and turn strings into interned symbols (_interning_ is discussed later).
[String interning] is a way of storing only one immutable copy of each distinct string value.

The lexer has a small interface and doesn't depend directly on the diagnostic
infrastructure in `rustc`.
Instead it provides diagnostics as plain data which
are emitted in [`rustc_parse::lexer`] as real diagnostics.
The `lexer` preserves full fidelity information for both IDEs and procedural macros
(sometimes referred to as "proc-macros").

The *parser* [translates the token stream from the `lexer` into an Abstract Syntax
Tree (AST)][parser].
It uses a recursive descent (top-down) approach to syntax analysis.
The crate entry points for the `parser` are the
[`Parser::parse_crate_mod`][parse_crate_mod] and [`Parser::parse_mod`][parse_mod]
methods found in [`rustc_parse::parser::Parser`].
The external module parsing
entry point is [`rustc_expand::module::parse_external_mod`][parse_external_mod].
And the macro-`parser` entry point is [`Parser::parse_nonterminal`][parse_nonterminal].

Parsing is performed with a set of [`parser`] utility methods including [`bump`],
[`check`], [`eat`], [`expect`], [`look_ahead`].

Parsing is organized by semantic construct.
Separate `parse_*` methods can be found in the [`rustc_parse`][rustc_parse_parser_dir] directory.
The source file name follows the construct name.
For example, the following files are found in the `parser`:

- [`expr.rs`](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_parse/src/parser/expr.rs)
- [`pat.rs`](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_parse/src/parser/pat.rs)
- [`ty.rs`](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_parse/src/parser/ty.rs)
- [`stmt.rs`](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_parse/src/parser/stmt.rs)

This naming scheme is used across many compiler stages.
You will find either a file or directory with the same name across the parsing, lowering, type
checking, [Typed High-level Intermediate Representation (`THIR`)][thir] lowering, and
[Mid-level Intermediate Representation (`MIR`)][mir] building sources.

Macro-expansion, `AST`-validation, name-resolution, and early linting also take
place during the lexing and parsing stage.

The [`rustc_ast::ast`]::{[`Crate`], [`Expr`], [`Pat`], ...} `AST` nodes are
returned from the parser while the standard [`Diag`] API is used for error handling.
Generally Rust's compiler will try to recover from errors
by parsing a superset of Rust's grammar, while also emitting an error type.

### `AST` lowering

Next the `AST` is converted into [High-Level Intermediate Representation
(`HIR`)][hir], a more compiler-friendly representation of the `AST`.
This process is called "lowering" and involves a lot of desugaring (the expansion and
formalizing of shortened or abbreviated syntax constructs) of things like loops and `async fn`.

We then use the `HIR` to do [*type inference*] (the process of automatic
detection of the type of an expression), [*trait solving*] (the process of
pairing up an impl with each reference to a `trait`), and [*type checking*].
Type checking is the process of converting the types found in the `HIR` ([`hir::Ty`]),
which represent what the user wrote, into the internal representation used by
the compiler ([`Ty<'tcx>`]).
It's called type checking because the information
is used to verify the type safety, correctness and coherence of the types used in the program.

### `MIR` lowering

The `HIR` is further lowered to `MIR`
(used for [borrow checking]) by constructing the `THIR`  (an even more desugared `HIR` used for
pattern and exhaustiveness checking) to convert into `MIR`.

We do [many optimizations on the MIR][mir-opt] because it is generic and that
improves later code generation and compilation speed.
It is easier to do some optimizations at `MIR` level than at `LLVM-IR` level.
For example LLVM doesn't seem
to be able to optimize the pattern the [`simplify_try`] `MIR`-opt looks for.

Rust code is also [_monomorphized_] during code generation, which means making
copies of all the generic code with the type parameters replaced by concrete types.
To do this, we need to collect a list of what concrete types to generate code for.
This is called _monomorphization collection_ and it happens at the `MIR` level.

[_monomorphized_]: https://en.wikipedia.org/wiki/Monomorphization

### Code generation

We then begin what is simply called _code generation_ or _codegen_.
The [code generation stage][codegen] is when higher-level representations of source are
turned into an executable binary.
Since `rustc` uses LLVM for code generation,
the first step is to convert the `MIR` to `LLVM-IR`.
This is where the `MIR` is actually monomorphized.
The `LLVM-IR` is passed to LLVM, which does a lot more
optimizations on it, emitting machine code which is basically assembly code
with additional low-level types and annotations added (e.g. an ELF object or
`WASM`).
The different libraries/binaries are then linked together to produce the final binary.

[*trait solving*]: traits/resolution.md
[*type checking*]: hir-typeck/summary.md
[*type inference*]: type-inference.md
[`bump`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.bump
[`check`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.check
[`Crate`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_ast/ast/struct.Crate.html
[`diag`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html
[`eat`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.eat
[`expect`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.expect
[`Expr`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_ast/ast/struct.Expr.html
[`hir::Ty`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/struct.Ty.html
[`look_ahead`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.look_ahead
[`Parser`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html
[`Pat`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_ast/ast/struct.Pat.html
[`rustc_ast::ast`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_ast/index.html
[`rustc_driver`]: rustc-driver/intro.md
[`rustc_interface::Config`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/struct.Config.html
[`rustc_lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lexer/index.html
[`rustc_parse::lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/lexer/index.html
[`rustc_parse::parser::Parser`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html
[`rustc_parse`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html
[`simplify_try`]: https://github.com/rust-lang/rust/pull/66282
[`Lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/lexer/struct.Lexer.html
[`Ty<'tcx>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[borrow checking]: borrow-check.md
[codegen]: backend/codegen.md
[hir]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/index.html
[lex]: the-parser.md
[mir-opt]: mir/optimizations.md
[mir]: mir/index.md
[parse_crate_mod]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.parse_crate_mod
[parse_external_mod]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/module/fn.parse_external_mod.html
[parse_mod]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.parse_mod
[parse_nonterminal]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html#method.parse_nonterminal
[parser]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html
[rustc_parse_parser_dir]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_parse/src/parser
[String interning]: https://en.wikipedia.org/wiki/String_interning
[thir]: ./thir.md

## How it does it

Now that we have a high-level view of what the compiler does to your code,
let's take a high-level view of _how_ it does all that stuff.
There are a lot of constraints and conflicting goals that the compiler needs to
satisfy/optimize for.
For example,

- Compilation speed: how fast is it to compile a program?
  More/better compile-time analyses often means compilation is slower.
  - Also, we want to support incremental compilation, so we need to take that into account.
    How can we keep track of what work needs to be redone and
    what can be reused if the user modifies their program?
    - Also we can't store too much stuff in the incremental cache because
      it would take a long time to load from disk and it could take a lot
      of space on the user's system...
- Compiler memory usage: while compiling a program, we don't want to use more memory than we need.
- Program speed: how fast is your compiled program?
  More/better compile-time analyses often means the compiler can do better optimizations.
- Program size: how large is the compiled binary?
  Similar to the previous point.
- Compiler compilation speed: how long does it take to compile the compiler?
  This impacts contributors and compiler maintenance.
- Implementation complexity: building a compiler is one of the hardest
  things a person/group can do, and Rust is not a very simple language, so how
  do we make the compiler's code base manageable?
- Compiler correctness: the binaries produced by the compiler should do what
  the input programs says they do, and should continue to do so despite the
  tremendous amount of change constantly going on.
- Integration: a number of other tools need to use the compiler in
  various ways (e.g. `cargo`, `clippy`, `Miri`) that must be supported.
- Compiler stability: the compiler should not crash or fail ungracefully on the stable channel.
- Rust stability: the compiler must respect Rust's stability guarantees by not
  breaking programs that previously compiled despite the many changes that are
  always going on to its implementation.
- Limitations of other tools: `rustc` uses LLVM in its backend, and LLVM has some
  strengths we leverage and some aspects we need to work around.

So, as you continue your journey through the rest of the guide, keep these things in mind.
They will often inform decisions that we make.

### Intermediate representations

As with most compilers, `rustc` uses some intermediate representations (IRs) to
facilitate computations.
In general, working directly with the source code is extremely inconvenient and error-prone.
Source code is designed to be human-friendly while at
the same time being unambiguous, but it's less convenient for doing something
like, say, type checking.

Instead most compilers, including `rustc`, build some sort of IR out of the
source code which is easier to analyze.
`rustc` has a few IRs, each optimized for different purposes:

- Token stream: the lexer produces a stream of tokens directly from the source code.
  This stream of tokens is easier for the parser to deal with than raw text.
- Abstract Syntax Tree (`AST`): the abstract syntax tree is built from the stream
  of tokens produced by the lexer.
  It represents pretty much exactly what the user wrote.
  It helps to do some syntactic sanity
  checking (e.g. checking that a type is expected where the user wrote one).
- High-level IR (HIR): This is a sort of desugared `AST`.
  It's still close to what the user wrote syntactically, but it includes some implicit things
  such as some elided lifetimes, etc. This IR is amenable to type checking.
- Typed `HIR` (THIR) _formerly High-level Abstract IR (HAIR)_: This is an
  intermediate between `HIR` and MIR.
  It is like the `HIR` but it is fully typed
  and a bit more desugared (e.g. method calls and implicit dereferences are
  made fully explicit).
  As a result, it is easier to lower to `MIR` from `THIR`  than from HIR.
- Middle-level IR (`MIR`): This IR is basically a Control-Flow Graph (CFG).
  A CFG is a type of diagram that shows the basic blocks of a program and how control
  flow can go between them.
  Likewise, `MIR` also has a bunch of basic blocks with
  simple typed statements inside them (e.g. assignment, simple computations,
  etc) and control flow edges to other basic blocks (e.g., calls, dropping
  values).
  `MIR` is used for borrow checking and other
  important dataflow-based checks, such as checking for uninitialized values.
  It is also used for a series of optimizations and for constant evaluation (via `Miri`).
  Because `MIR` is still generic, we can do a lot of analyses here more
  efficiently than after monomorphization.
- `LLVM-IR`: This is the standard form of all input to the LLVM compiler.
  `LLVM-IR` is a sort of typed assembly language with lots of annotations.
  It's
  a standard format that is used by all compilers that use LLVM (e.g. the clang
  C compiler also outputs `LLVM-IR`).
  `LLVM-IR` is designed to be easy for other
  compilers to emit and also rich enough for LLVM to run a bunch of optimizations on it.

One other thing to note is that many values in the compiler are _interned_.
This is a performance and memory optimization in which we allocate the values in
a special allocator called an _[arena]_.
Then, we pass around references to the values allocated in the arena.
This allows us to make
sure that identical values (e.g. types in your program) are only allocated once
and can be compared cheaply by comparing pointers.
Many of the intermediate representations are interned.

[arena]: https://en.wikipedia.org/wiki/Region-based_memory_management

### Queries

The first big implementation choice is Rust's use of the _query_ system in its compiler.
The Rust compiler _is not_ organized as a series of passes over the code which execute sequentially.
The Rust compiler does this to make
incremental compilation possible -- that is, if the user makes a change to
their program and recompiles, we want to do as little redundant work as
possible to output the new binary.

In `rustc`, all the major steps above are organized as a bunch of queries that call each other.
For example, there is a query to ask for the type of something
and another to ask for the optimized `MIR` of a function.
These queries can call each other and are all tracked through the query system.
The results of the queries are cached on disk so that the compiler can tell which queries' results
changed from the last compilation and only redo those.
This is how incremental compilation works.

In principle, for the query-fied steps, we do each of the above for each item individually.
For example, we will take the `HIR` for a function and use queries
to ask for the `LLVM-IR` for that HIR.
This drives the generation of optimized
`MIR`, which drives the borrow checker, which drives the generation of `MIR`, and so on.

... except that this is very over-simplified.
In fact, some queries are not
cached on disk, and some parts of the compiler have to run for all code anyway
for correctness even if the code is dead code (e.g. the borrow checker). For
example, [currently the `mir_borrowck` query is first executed on all functions
of a crate.][passes] Then the codegen backend invokes the
`collect_and_partition_mono_items` query, which first recursively requests the
`optimized_mir` for all reachable functions, which in turn runs `mir_borrowck`
for that function and then creates codegen units.
This kind of split will need
to remain to ensure that unreachable functions still have their errors emitted.

[passes]: https://github.com/rust-lang/rust/blob/e69c7306e2be08939d95f14229e3f96566fb206c/compiler/rustc_interface/src/passes.rs#L791

Moreover, the compiler wasn't originally built to use a query system; the query
system has been retrofitted into the compiler, so parts of it are not query-fied yet.
Also, LLVM isn't our code, so that isn't querified either.
The plan is to eventually query-fy all of the steps listed in the previous section,
but as of <!-- date-check --> November 2022, only the steps between `HIR` and
`LLVM-IR` are query-fied.
That is, lexing, parsing, name resolution, and macro
expansion are done all at once for the whole program.

One other thing to mention here is the all-important "typing context",
[`TyCtxt`], which is a giant struct that is at the center of all things.
(Note that the name is mostly historic.
This is _not_ a "typing context" in the sense of `Γ` or `Δ` from type theory.
The name is retained because that's what the name of the struct is in the source code.) All
queries are defined as methods on the [`TyCtxt`] type, and the in-memory query
cache is stored there too.
In the code, there is usually a variable called `tcx` which is a handle on the typing context.
You will also see lifetimes with
the name `'tcx`, which means that something is tied to the lifetime of the
[`TyCtxt`] (usually it is stored or interned there).

[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html

For more information about queries in the compiler, see [the queries chapter][queries].

[queries]: ./query.md

### `ty::Ty`

Types are really important in Rust, and they form the core of a lot of compiler analyses.
The main type (in the compiler) that represents types (in the user's
program) is [`rustc_middle::ty::Ty`][ty].
This is so important that we have a whole chapter
on [`ty::Ty`][ty], but for now, we just want to mention that it exists and is the way
`rustc` represents types!

Also note that the [`rustc_middle::ty`] module defines the [`TyCtxt`] struct we mentioned before.

[ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html
[`rustc_middle::ty`]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_middle/ty/index.html

### Parallelism

Compiler performance is a problem that we would like to improve on (and are always working on).
One aspect of that is parallelizing `rustc` itself.

Currently, there is only one part of rustc that is parallel by default:
[code generation](./parallel-rustc.md#Codegen).

However, the rest of the compiler is still not yet parallel.
There have been lots of efforts spent on this, but it is generally a hard problem.
The current approach is to turn [`RefCell`]s into [`Mutex`]s -- that is, we
switch to thread-safe internal mutability.
However, there are ongoing
challenges with lock contention, maintaining query-system invariants under
concurrency, and the complexity of the code base.
One can try out the current work by enabling parallel compilation in `bootstrap.toml`.
It's still early days,
but there are already some promising performance improvements.

[`RefCell`]: https://doc.rust-lang.org/std/cell/struct.RefCell.html
[`Mutex`]: https://doc.rust-lang.org/std/sync/struct.Mutex.html

### Bootstrapping

`rustc` itself is written in Rust.
So how do we compile the compiler? We use an older compiler to compile the newer compiler.
This is called [_bootstrapping_].

Bootstrapping has a lot of interesting implications.
For example, it means that one of the major users of Rust is the Rust compiler, so we are
constantly testing our own software ("eating our own dogfood").

For more details on bootstrapping, see [the bootstrapping section of the guide][rustc-bootstrap].

[_bootstrapping_]: https://en.wikipedia.org/wiki/Bootstrapping_(compilers)
[rustc-bootstrap]: building/bootstrapping/intro.md

<!--
# Unresolved Questions

- Does LLVM ever do optimizations in debug builds?
- How do I explore phases of the compile process in my own sources (lexer,
  parser, HIR, etc)? - e.g., `cargo rustc -- -Z unpretty=hir-tree` allows you to
  view `HIR` representation
- What is the main source entry point for `X`?
- Where do phases diverge for cross-compilation to machine code across different platforms?
-->

# References

- Command line parsing
  - Guide: [The Rustc Driver and Interface](rustc-driver/intro.md)
  - Driver definition: [`rustc_driver`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/)
  - Main entry point: [`rustc_session::config::build_session_options`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/config/fn.build_session_options.html)
- Lexical Analysis: Lex the user program to a stream of tokens
  - Guide: [Lexing and Parsing](the-parser.md)
  - Lexer definition: [`rustc_lexer`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lexer/index.html)
  - Main entry point: [`rustc_lexer::Cursor::advance_token`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lexer/struct.Cursor.html#method.advance_token)
- Parsing: Parse the stream of tokens to an Abstract Syntax Tree (AST)
  - Guide: [Lexing and Parsing](the-parser.md)
  - Guide: [Macro Expansion](macro-expansion.md)
  - Guide: [Name Resolution](name-resolution.md)
  - Parser definition: [`rustc_parse`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html)
  - Main entry points:
    - [Entry point for first file in crate](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/passes/fn.parse.html)
    - [Entry point for outline module parsing](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/module/fn.parse_external_mod.html)
    - [Entry point for macro fragments][parse_nonterminal]
  - `AST` definition: [`rustc_ast`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/index.html)
  - Feature gating: [Feature Gate Checking](feature-gate-check.md)
  - Early linting: **TODO**
- The High Level Intermediate Representation (HIR)
  - Guide: [The HIR](hir.md)
  - Guide: [Identifiers in the HIR](hir.md#identifiers-in-the-hir)
  - Guide: [The `HIR` Map](hir.md#the-hir-map)
  - Guide: [Lowering `AST` to `HIR`](./hir/lowering.md)
  - How to view `HIR` representation for your code `cargo rustc -- -Z unpretty=hir-tree`
  - Rustc `HIR` definition: [`rustc_hir`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/index.html)
  - Main entry point: **TODO**
  - Late linting: **TODO**
- Type Inference
  - Guide: [Type Inference](type-inference.md)
  - Guide: [The ty Module: Representing Types](ty.md) (semantics)
  - Main entry point (type inference): [`InferCtxtBuilder::enter`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_infer/infer/struct.InferCtxtBuilder.html#method.enter)
  - Main entry point (type checking bodies): [the `typeck` query](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.typeck)
    - These two functions can't be decoupled.
- The Mid Level Intermediate Representation (MIR)
  - Guide: [The `MIR` (Mid level IR)](mir/index.md)
  - Definition: [`rustc_middle/src/mir`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/mir/index.html)
  - Definition of sources that manipulates the MIR: [`rustc_mir_build`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_build/index.html), [`rustc_mir_dataflow`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_dataflow/index.html), [`rustc_mir_transform`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/index.html)
- The Borrow Checker
  - Guide: [MIR Borrow Check](borrow-check.md)
  - Definition: [`rustc_borrowck`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/index.html)
  - Main entry point: [`mir_borrowck` query](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_borrowck/fn.mir_borrowck.html)
- `MIR` Optimizations
  - Guide: [MIR Optimizations](mir/optimizations.md)
  - Definition: [`rustc_mir_transform`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/index.html)
  - Main entry point: [`optimized_mir` query](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_mir_transform/fn.optimized_mir.html)
- Code Generation
  - Guide: [Code Generation](backend/codegen.md)
  - Generating Machine Code from `LLVM-IR` with LLVM - **TODO: reference?**
  - Main entry point: [`rustc_codegen_ssa::base::codegen_crate`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/fn.codegen_crate.html)
    - This monomorphizes and produces `LLVM-IR` for one codegen unit.
      It then starts a background thread to run LLVM, which must be joined later.
    - Monomorphization happens lazily via [`FunctionCx::monomorphize`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/struct.FunctionCx.html#method.monomorphize) and [`rustc_codegen_ssa::base::codegen_instance `](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/fn.codegen_instance.html)


---

# High-level overview of the compiler source

Now that we have [seen what the compiler does][orgch],
let's take a look at the structure of the [`rust-lang/rust`] repository,
where the rustc source code lives.

[`rust-lang/rust`]: https://github.com/rust-lang/rust

> You may find it helpful to read the ["Overview of the compiler"][orgch]
> chapter, which introduces how the compiler works, before this one.

[orgch]: ./overview.md

## Workspace structure

The [`rust-lang/rust`] repository consists of a single large cargo workspace
containing the compiler, the standard libraries ([`core`], [`alloc`], [`std`],
[`proc_macro`], [`etc`]), and [`rustdoc`], along with the build system and a
bunch of tools and submodules for building a full Rust distribution.

The repository consists of three main directories:

- [`compiler/`] contains the source code for `rustc`. It consists of many crates
  that together make up the compiler.
  
- [`library/`] contains the standard libraries ([`core`], [`alloc`], [`std`],
  [`proc_macro`], [`test`]), as well as the Rust runtime ([`backtrace`], [`rtstartup`],
  [`lang_start`]).
  
- [`tests/`] contains the compiler tests.
  
- [`src/`] contains the source code for [`rustdoc`], [`clippy`], [`cargo`], the build system,
  language docs, etc.

[`alloc`]: https://github.com/rust-lang/rust/tree/HEAD/library/alloc
[`backtrace`]: https://github.com/rust-lang/backtrace-rs/
[`cargo`]: https://github.com/rust-lang/cargo
[`clippy`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/clippy
[`compiler/`]: https://github.com/rust-lang/rust/tree/HEAD/compiler
[`core`]: https://github.com/rust-lang/rust/tree/HEAD/library/core
[`etc`]: https://github.com/rust-lang/rust/tree/HEAD/src/etc
[`lang_start`]: https://github.com/rust-lang/rust/blob/HEAD/library/std/src/rt.rs
[`library/`]: https://github.com/rust-lang/rust/tree/HEAD/library
[`proc_macro`]: https://github.com/rust-lang/rust/tree/HEAD/library/proc_macro
[`rtstartup`]: https://github.com/rust-lang/rust/tree/HEAD/library/rtstartup
[`rust-lang/rust`]: https://github.com/rust-lang/rust
[`rustdoc`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc
[`src/`]: https://github.com/rust-lang/rust/tree/HEAD/src
[`std`]: https://github.com/rust-lang/rust/tree/HEAD/library/std
[`test`]: https://github.com/rust-lang/rust/tree/HEAD/library/test
[`tests/`]: https://github.com/rust-lang/rust/tree/HEAD/tests

## Compiler

The compiler is implemented in the various [`compiler/`] crates.
The [`compiler/`] crates all have names starting with `rustc_*`. These are a
collection of around 50 interdependent crates ranging in size from tiny to
huge. There is also the `rustc` crate which is the actual binary (i.e. the
`main` function); it doesn't actually do anything besides calling the
[`rustc_driver`] crate, which drives the various parts of compilation in other
crates.

The dependency order of these crates is complex, but roughly it is
something like this:

1. `rustc` (the binary) calls [`rustc_driver::main`][main].
1. [`rustc_driver`] depends on a lot of other crates, but the main one is
   [`rustc_interface`].
1. [`rustc_interface`] depends on most of the other compiler crates. It is a
   fairly generic interface for driving the whole compilation.
1. Most of the other `rustc_*` crates depend on [`rustc_middle`], which defines
   a lot of central data structures in the compiler.
1. [`rustc_middle`] and most of the other crates depend on a handful of crates
   representing the early parts of the compiler (e.g. the parser), fundamental
   data structures (e.g. [`Span`]), or error reporting:
   [`rustc_data_structures`], [`rustc_span`], [`rustc_errors`], etc.

[`rustc_data_structures`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/index.html
[`rustc_driver`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/index.html
[`rustc_errors`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/index.html
[`rustc_interface`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/index.html
[`rustc_middle`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/index.html
[`rustc_span`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/index.html
[`Span`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html
[main]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/fn.main.html

You can see the exact dependencies by running `cargo tree`,
just like you would for any other Rust package:

```console
cargo tree --package rustc_driver
```

One final thing: [`src/llvm-project`] is a submodule for our fork of LLVM.
During bootstrapping, LLVM is built and the [`compiler/rustc_llvm`] crate
contains Rust wrappers around LLVM (which is written in C++), so that the
compiler can interface with it.

Most of this book is about the compiler, so we won't have any further
explanation of these crates here.

[`compiler/rustc_llvm`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_llvm
[`src/llvm-project`]: https://github.com/rust-lang/rust/tree/HEAD/src/
[`Cargo.toml`]: https://github.com/rust-lang/rust/blob/HEAD/Cargo.toml

### Big picture

The dependency structure of the compiler is influenced by two main factors:

1. Organization. The compiler is a _huge_ codebase; it would be an impossibly
   large crate. In part, the dependency structure reflects the code structure
   of the compiler.
2. Compile-time. By breaking the compiler into multiple crates, we can take
   better advantage of incremental/parallel compilation using cargo. In
   particular, we try to have as few dependencies between crates as possible so
   that we don't have to rebuild as many crates if you change one.

At the very bottom of the dependency tree are a handful of crates that are used
by the whole compiler (e.g. [`rustc_span`]). The very early parts of the
compilation process (e.g. [parsing and the Abstract Syntax Tree (`AST`)][parser]) 
depend on only these.

After the [`AST`][parser] is constructed and other early analysis is done, the
compiler's [query system][query] gets set up. The query system is set up in a
clever way using function pointers. This allows us to break dependencies
between crates, allowing more parallel compilation. The query system is defined
in [`rustc_middle`], so nearly all subsequent parts of the compiler depend on
this crate. It is a really large crate, leading to long compile times. Some
efforts have been made to move stuff out of it with varying success. Another
side-effect is that sometimes related functionality gets scattered across
different crates. For example, linting functionality is found across earlier
parts of the crate, [`rustc_lint`], [`rustc_middle`], and other places.

Ideally there would be fewer, more cohesive crates, with incremental and
parallel compilation making sure compile times stay reasonable. However,
incremental and parallel compilation haven't gotten good enough for that yet,
so breaking things into separate crates has been our solution so far.

At the top of the dependency tree is [`rustc_driver`] and [`rustc_interface`]
which is an unstable wrapper around the query system helping drive various
stages of compilation. Other consumers of the compiler may use this interface
in different ways (e.g. [`rustdoc`] or maybe eventually `rust-analyzer`). The
[`rustc_driver`] crate first parses command line arguments and then uses
[`rustc_interface`] to drive the compilation to completion.

[parser]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html
[`rustc_lint`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/index.html
[query]: ./query.md

## rustdoc

The bulk of [`rustdoc`] is in [`librustdoc`]. However, the [`rustdoc`] binary
itself is [`src/tools/rustdoc`], which does nothing except call [`rustdoc::main`].

There is also `JavaScript` and `CSS` for the docs in [`src/tools/rustdoc-js`]
and [`src/tools/rustdoc-themes`]. The type definitions for `--output-format=json`
are in a separate crate in [`src/rustdoc-json-types`].

You can read more about [`rustdoc`] in [this chapter][rustdoc-chapter].

[`librustdoc`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/index.html
[`rustdoc::main`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/fn.main.html
[`src/tools/rustdoc-js`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc-js
[`src/tools/rustdoc-themes`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc-themes
[`src/tools/rustdoc`]:  https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc
[`src/rustdoc-json-types`]: https://github.com/rust-lang/rust/tree/HEAD/src/rustdoc-json-types
[rustdoc-chapter]: ./rustdoc.md

## Tests

The test suite for all of the above is in [`tests/`]. You can read more
about the test suite [in this chapter][testsch].

The test harness is in [`src/tools/compiletest/`][`compiletest/`].

[`tests/`]: https://github.com/rust-lang/rust/tree/HEAD/tests
[testsch]: ./tests/intro.md

## Build System

There are a number of tools in the repository just for building the compiler,
standard library, [`rustdoc`], etc, along with testing, building a full Rust
distribution, etc.

One of the primary tools is [`src/bootstrap/`]. You can read more about
bootstrapping [in this chapter][bootstch]. The process may also use other tools
from [`src/tools/`], such as [`tidy/`] or [`compiletest/`].

[`compiletest/`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest
[`src/bootstrap/`]: https://github.com/rust-lang/rust/tree/HEAD/src/bootstrap
[`src/tools/`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools
[`tidy/`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/tidy
[bootstch]: ./building/bootstrapping/intro.md

## Standard library

This code is fairly similar to most other Rust crates except that it must be
built in a special way because it can use unstable ([`nightly`]) features.
The standard library is sometimes referred to as [`libstd or the "standard facade"`].

[`libstd or the "standard facade"`]: https://rust-lang.github.io/rfcs/0040-libstd-facade.html
[`nightly`]: https://doc.rust-lang.org/nightly/nightly-rustc/

## Other

There are a lot of other things in the `rust-lang/rust` repo that are related
to building a full Rust distribution. Most of the time you don't need to worry about them.

These include:
- [`src/ci`]: The CI configuration. This actually quite extensive because we
  run a lot of tests on a lot of platforms.
- [`src/doc`]: Various documentation, including submodules for a few books.
- [`src/etc`]: Miscellaneous utilities.
- And more...

[`src/ci`]: https://github.com/rust-lang/rust/tree/HEAD/src/ci
[`src/doc`]: https://github.com/rust-lang/rust/tree/HEAD/src/doc
[`src/etc`]: https://github.com/rust-lang/rust/tree/HEAD/src/etc


---

# Memory management in rustc

Generally rustc tries to be pretty careful how it manages memory.
The compiler allocates _a lot_ of data structures throughout compilation,
and if we are not careful, it will take a lot of time and space to do so.

One of the main way the compiler manages this is using [arena]s and [interning].

[arena]: https://en.wikipedia.org/wiki/Region-based_memory_management
[interning]: https://en.wikipedia.org/wiki/String_interning

## Arenas and  Interning

Since A LOT of data structures are created during compilation, for performance
reasons, we allocate them from a global memory pool.
Each are allocated once from a long-lived *arena*.
This is called _arena allocation_.
This system reduces allocations/deallocations of memory.
It also allows for easy comparison of types (more on types [here](./ty.md)) for equality:
for each interned type `X`, we implemented [`PartialEq` for X][peqimpl],
so we can just compare pointers.
The [`CtxtInterners`] type contains a bunch of maps of interned types and the arena itself.

[`CtxtInterners`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.CtxtInterners.html#structfield.arena
[peqimpl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Ty.html#implementations

### Example: `ty::TyKind`

Taking the example of [`ty::TyKind`] which represents a type in the compiler (you
can read more [here](./ty.md)).  Each time we want to construct a type, the
compiler doesn’t naively allocate from the buffer.  Instead, we check if that
type was already constructed. If it was, we just get the same pointer we had
before, otherwise we make a fresh pointer. With this schema if we want to know
if two types are the same, all we need to do is compare the pointers which is
efficient. [`ty::TyKind`] should never be constructed on the stack, and it would be unusable
if done so.
You always allocate them from this arena and you always intern them so they are
unique.

At the beginning of the compilation we make a buffer and each time we need to allocate a type we use
some of this memory buffer. If we run out of space we get another one. The lifetime of that buffer
is `'tcx`. Our types are tied to that lifetime, so when compilation finishes all the memory related
to that buffer is freed and our `'tcx` references would be invalid.

In addition to types, there are a number of other arena-allocated data structures that you can
allocate, and which are found in this module. Here are a few examples:

- [`GenericArgs`], allocated with [`mk_args`] – this will intern a slice of types, often used
to specify the values to be substituted for generics args (e.g. `HashMap<i32, u32>` would be
represented as a slice `&'tcx [tcx.types.i32, tcx.types.u32]`).
- [`TraitRef`], typically passed by value – a **trait reference** consists of a reference to a trait
  along with its various type parameters (including `Self`), like `i32: Display` (here, the def-id
  would reference the `Display` trait, and the args would contain `i32`). Note that `def-id` is
  defined and discussed in depth in the [`AdtDef and DefId`][adtdefid] section.
- [`Predicate`] defines something the trait system has to prove (see [traits] module).

[`GenericArgs`]: ./ty-module/generic-arguments.md#the-genericargs-type
[adtdefid]: ./ty-module/generic-arguments.md#adtdef-and-defid
[`TraitRef`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TraitRef.html
[`AdtDef` and `DefId`]: ./ty.md#adts-representation
[`def-id`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html
[`GenericArgs`]: ./generic_arguments.html#GenericArgs
[`mk_args`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.mk_args
[adtdefid]: ./ty-module/generic-arguments.md#adtdef-and-defid
[`Predicate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.Predicate.html
[`TraitRef`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/type.TraitRef.html
[`ty::TyKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/sty/type.TyKind.html
[traits]: ./traits/resolution.md

## The `tcx` and how it uses lifetimes

The typing context (`tcx`) is the central data structure in the compiler. It is the context that
you use to perform all manner of queries. The `struct` [`TyCtxt`] defines a reference to this shared
context:

```rust,ignore
tcx: TyCtxt<'tcx>
//          ----
//          |
//          arena lifetime
```

As you can see, the `TyCtxt` type takes a lifetime parameter. When you see a reference with a
lifetime like `'tcx`, you know that it refers to arena-allocated data (or data that lives as long as
the arenas, anyhow).

[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html

### A Note On Lifetimes

The Rust compiler is a fairly large program containing lots of big data
structures (e.g. the [Abstract Syntax Tree (AST)][ast], [High-Level Intermediate
Representation (`HIR`)][hir], and the type system) and as such, arenas and
references are heavily relied upon to minimize unnecessary memory use. This
manifests itself in the way people can plug into the compiler (i.e. the
[driver](./rustc-driver/intro.md)), preferring a "push"-style API (callbacks) instead
of the more Rust-ic "pull" style (think the `Iterator` trait).

Thread-local storage and interning are used a lot through the compiler to reduce
duplication while also preventing a lot of the ergonomic issues due to many
pervasive lifetimes. The [`rustc_middle::ty::tls`][tls] module is used to access these
thread-locals, although you should rarely need to touch it.

[ast]: ./ast-validation.md
[hir]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/index.html
[tls]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/tls/index.html


---

# Serialization in rustc

rustc has to [serialize] and deserialize various data during compilation.
Specifically:

- "Crate metadata", consisting mainly of query outputs, are serialized
  from a binary format into `rlib` and `rmeta` files that are output when
  compiling a library crate. These `rlib` and `rmeta` files are then
  deserialized by the crates which depend on that library.
- Certain query outputs are serialized in a binary format to
  [persist incremental compilation results].
- [`CrateInfo`] is serialized to `JSON` when the `-Z no-link` flag is used, and
  deserialized from `JSON` when the `-Z link-only` flag is used.

[`CrateInfo`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/struct.CrateInfo.html
[persist incremental compilation results]: queries/incremental-compilation-in-detail.md#the-real-world-how-persistence-makes-everything-complicated
[serialize]: https://en.wikipedia.org/wiki/Serialization

## The `Encodable` and `Decodable` traits

The [`rustc_serialize`] crate defines two traits for types which can be serialized:

```rust,ignore
pub trait Encodable<S: Encoder> {
    fn encode(&self, s: &mut S) -> Result<(), S::Error>;
}

pub trait Decodable<D: Decoder>: Sized {
    fn decode(d: &mut D) -> Result<Self, D::Error>;
}
```

It also defines implementations of these for various common standard library
[primitive types](https://doc.rust-lang.org/std/#primitives) such as integer
types, floating point types, `bool`, `char`, `str`, etc.

For types that are constructed from those types, `Encodable` and `Decodable`
are usually implemented by [derives]. These generate implementations that
forward deserialization to the fields of the struct or enum. For a
struct those impls look something like this:

```rust,ignore
#![feature(rustc_private)]
extern crate rustc_serialize;
use rustc_serialize::{Decodable, Decoder, Encodable, Encoder};

struct MyStruct {
    int: u32,
    float: f32,
}

impl<E: Encoder> Encodable<E> for MyStruct {
    fn encode(&self, s: &mut E) -> Result<(), E::Error> {
        s.emit_struct("MyStruct", 2, |s| {
            s.emit_struct_field("int", 0, |s| self.int.encode(s))?;
            s.emit_struct_field("float", 1, |s| self.float.encode(s))
        })
    }
}

impl<D: Decoder> Decodable<D> for MyStruct {
    fn decode(s: &mut D) -> Result<MyStruct, D::Error> {
        s.read_struct("MyStruct", 2, |d| {
            let int = d.read_struct_field("int", 0, Decodable::decode)?;
            let float = d.read_struct_field("float", 1, Decodable::decode)?;

            Ok(MyStruct { int, float })
        })
    }
}
```
[`rustc_serialize`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_serialize/index.html

## Encoding and Decoding arena allocated types

rustc has a lot of [arena allocated types].
Deserializing these types isn't possible without access to the arena that they need to be allocated on.
The [`TyDecoder`] and [`TyEncoder`] traits are subtraits of [`Decoder`] and [`Encoder`] that allow access to a [`TyCtxt`].

Types which contain `arena` allocated types can then bound the type parameter of their
[`Encodable`] and [`Decodable`] implementations with these traits.
For example

```rust,ignore
impl<'tcx, D: TyDecoder<'tcx>> Decodable<D> for MyStruct<'tcx> {
    /* ... */
}
```

The [`TyEncodable`] and [`TyDecodable`] [derive macros][derives] will expand to such
an implementation.

Decoding the actual `arena` allocated type is harder, because some of the
implementations can't be written due to the [orphan rules]. To work around this,
the [`RefDecodable`] trait is defined in [`rustc_middle`]. This can then be
implemented for any type. The `TyDecodable` macro will call `RefDecodable` to
decode references, but various generic code needs types to actually be
`Decodable` with a specific decoder.

For interned types instead of manually implementing `RefDecodable`, using a new
type wrapper, like [`ty::Predicate`] and manually implementing `Encodable` and
`Decodable` may be simpler.

[`Decodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_serialize/trait.Decodable.html
[`Decoder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_serialize/trait.Decoder.html
[`Encodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_serialize/trait.Encodable.html
[`Encoder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_serialize/trait.Encoder.html
[`RefDecodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/codec/trait.RefDecodable.html
[`rustc_middle`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/index.html
[`ty::Predicate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/predicate/struct.Predicate.html
[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html
[`TyDecodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_macros/derive.TyDecodable.html
[`TyDecoder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/codec/trait.TyDecoder.html
[`TyEncodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_macros/derive.TyEncodable.html
[`TyEncoder`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/codec/trait.TyEncoder.html
[arena allocated types]: memory.md
[derives]: #derive-macros
[orphan rules]:https://doc.rust-lang.org/reference/items/implementations.html#orphan-rules

## Derive macros

The [`rustc_macros`] crate defines various derives to help implement `Decodable`
and `Encodable`.

- The `Encodable` and `Decodable` macros generate implementations that apply to
  all `Encoders` and `Decoders`. These should be used in crates that don't
  depend on [`rustc_middle`], or that have to be serialized by a type that does
  not implement `TyEncoder`.
- [`MetadataEncodable`] generates implementations that
  only allow decoding by [`rustc_metadata::rmeta::encoder::EncodeContext`].
- [`BlobDecodable`] and [`LazyDecodable`] serve as the decoding counterparts to
  `MetadataEncodable`. They generate implementations that decode with the
  metadata blob decoders in `rustc_metadata::rmeta`; use `BlobDecodable` when
  the type has no lazy metadata handles, and `LazyDecodable` when it does.
- `TyEncodable` and `TyDecodable` generate implementation that apply to any
  `TyEncoder` or `TyDecoder`. These should be used for types that are only
  serialized in crate metadata and/or the incremental cache, which is most
  serializable types in `rustc_middle`.

[`BlobDecodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_macros/derive.BlobDecodable.html
[`LazyDecodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_macros/derive.LazyDecodable.html
[`MetadataEncodable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_macros/derive.MetadataEncodable.html
[`rustc_macros`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_macros
[`rustc_metadata::rmeta`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/index.html
[`rustc_metadata::rmeta::encoder::EncodeContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/encoder/struct.EncodeContext.html
[`rustc_middle`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_middle

## Shorthands

`Ty` can be deeply recursive, if each `Ty` was encoded naively then crate
metadata would be very large. To handle this, each `TyEncoder` has a cache of
locations in its output where it has serialized types. If a type being encoded
is in the cache, then instead of serializing the type as usual, the byte offset
within the file being written is encoded instead. A similar scheme is used for
`ty::Predicate`.

## `LazyValue<T>`

Crate metadata is initially loaded before the `TyCtxt<'tcx>` is created, so
some deserialization needs to be deferred from the initial loading of metadata.
The [`LazyValue<T>`] type wraps the (relative) offset in the crate metadata
where a `T` has been serialized. There are also some variants, [`LazyArray<T>`]
and [`LazyTable<I, T>`].

The `LazyArray<[T]>` and `LazyTable<I, T>` types provide some functionality over
`Lazy<Vec<T>>` and `Lazy<HashMap<I, T>>`:

- It's possible to encode a `LazyArray<T>` directly from an `Iterator`, without
  first collecting into a `Vec<T>`.
- Indexing into a `LazyTable<I, T>` does not require decoding entries other
  than the one being read.

**note**: `LazyValue<T>` does not cache its value after being deserialized the
first time. Instead the query system itself is the main way of caching these
results.

[`LazyArray<T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html
[`LazyTable<I, T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html
[`LazyValue<T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html

## Specialization

A few types, most notably `DefId`, need to have different implementations for
different `Encoder`s. This is currently handled by ad-hoc specializations, for
example: `DefId` has a `default` implementation of `Encodable<E>` and a
specialized one for `Encodable<CacheEncoder>`.


---

# Parallel compilation

<div class="warning">
As of <!-- date-check --> November 2024,
the parallel front-end is undergoing significant changes,
so this page contains quite a bit of outdated information.

Tracking issue: <https://github.com/rust-lang/rust/issues/113349>
</div>

As of <!-- date-check --> November 2024, most of the rust compiler is now
parallelized.

- The codegen part is executed concurrently by default.
  You can use the `-C
  codegen-units=n` option to control the number of concurrent tasks.
- The parts after HIR lowering to codegen such as type checking, borrowing
  checking, and mir optimization are parallelized in the nightly version.
  Currently, they are executed in serial by default, and parallelization is
  manually enabled by the user using the `-Z threads = n` option.
- Other parts, such as lexical parsing, HIR lowering, and macro expansion, are
  still executed in serial mode.

<div class="warning">
The following sections are kept for now but are quite outdated.
</div>

---

[codegen]: backend/codegen.md

## Code generation

During monomorphization the compiler splits up all the code to
be generated into smaller chunks called _codegen units_.
These are then generated by independent instances of LLVM running in parallel.
At the end, the linker
is run to combine all the codegen units together into one binary.
This process occurs in the [`rustc_codegen_ssa::base`] module.

[`rustc_codegen_ssa::base`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/index.html

## Data structures

The underlying thread-safe data-structures used in the parallel compiler
can be found in the [`rustc_data_structures::sync`] module.
These data structures
are implemented differently depending on whether `parallel-compiler` is true.

| data structure                   | parallel                                            | non-parallel |
| -------------------------------- | --------------------------------------------------- | ------------ |
| Lock\<T> | (parking_lot::Mutex\<T>) | (std::cell::RefCell) |
| RwLock\<T> | (parking_lot::RwLock\<T>) | (std::cell::RefCell) |
| ReadGuard | parking_lot::RwLockReadGuard | std::cell::Ref |
| MappedReadGuard | parking_lot::MappedRwLockReadGuard | std::cell::Ref |
| WriteGuard | parking_lot::RwLockWriteGuard | std::cell::RefMut |
| MappedWriteGuard | parking_lot::MappedRwLockWriteGuard | std::cell::RefMut |
| LockGuard | parking_lot::MutexGuard | std::cell::RefMut |

- These thread-safe data structures are interspersed during compilation which
  can cause lock contention resulting in degraded performance as the number of
  threads increases beyond 4. So we audit the use of these data structures
  which leads to either a refactoring so as to reduce the use of shared state,
  or the authoring of persistent documentation covering the specific of the
  invariants, the atomicity, and the lock orderings.

- On the other hand, we still need to figure out what other invariants
  during compilation might not hold in parallel compilation.

[`rustc_data_structures::sync`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/sync/index.html

### WorkerLocal

[`WorkerLocal`] is a special data structure implemented for parallel compilers.
It holds worker-locals values for each thread in a thread pool.
You can only
access the worker local value through the `Deref` `impl` on the thread pool it
was constructed on.
It panics otherwise.

`WorkerLocal` is used to implement the `Arena` allocator in the parallel
environment, which is critical in parallel queries.
Its implementation is
located in the [`rustc_data_structures::sync::worker_local`] module.
However,
in the non-parallel compiler, it is implemented as `(OneThread<T>)`, whose `T`
can be accessed directly through `Deref::deref`.

[`rustc_data_structures::sync::worker_local`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/sync/worker_local/index.html
[`WorkerLocal`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/sync/worker_local/struct.WorkerLocal.html

## Parallel iterator

The parallel iterators provided by the [`rayon`] crate are easy ways to
implement parallelism.
In the current implementation of the parallel compiler,
we use [a custom fork of `rayon`][rustc-rayon] to run tasks in parallel.

Some iterator functions are implemented to run loops in parallel
when `parallel-compiler` is true.

| Function(Omit `Send` and `Sync`)                             | Introduction                                                 | Owning Module              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- |
| **par_iter**<T: IntoParallelIterator>(t: T) -> T::Iter       | generate a parallel iterator                                 | rustc_data_structure::sync |
| **par_for_each_in**<T: IntoParallelIterator>(t: T, for_each: impl Fn(T::Item)) | generate a parallel iterator and run `for_each` on each element | rustc_data_structure::sync |
| **Map::par_body_owners**(self, f: impl Fn(LocalDefId))       | run `f` on all hir owners in the crate                       | rustc_middle::hir::map     |
| **Map::par_for_each_module**(self, f: impl Fn(LocalDefId))   | run `f` on all modules and sub modules in the crate          | rustc_middle::hir::map     |
| **ModuleItems::par_items**(&self, f: impl Fn(ItemId))        | run `f` on all items in the module                           | rustc_middle::hir          |
| **ModuleItems::par_trait_items**(&self, f: impl Fn(TraitItemId)) | run `f` on all trait items in the module                     | rustc_middle::hir          |
| **ModuleItems::par_impl_items**(&self, f: impl Fn(ImplItemId)) | run `f` on all impl items in the module                      | rustc_middle::hir          |
| **ModuleItems::par_foreign_items**(&self, f: impl Fn(ForeignItemId)) | run `f` on all foreign items in the module                   | rustc_middle::hir          |

There are a lot of loops in the compiler which can possibly be parallelized
using these functions. As of <!-- date-check--> August 2022, scenarios where
the parallel iterator function has been used are as follows:

| caller                                                  | scenario                                                     | callee                   |
| ------------------------------------------------------- | ------------------------------------------------------------ | ------------------------ |
| rustc_metadata::rmeta::encoder::prefetch_mir            | Prefetch queries which will be needed later by metadata encoding | par_iter                 |
| rustc_monomorphize::collector::collect_crate_mono_items | Collect monomorphized items reachable from non-generic items | par_for_each_in          |
| rustc_interface::passes::analysis                       | Check the validity of the match statements                   | Map::par_body_owners     |
| rustc_interface::passes::analysis                       | MIR borrow check                                             | Map::par_body_owners     |
| rustc_typeck::check::typeck_item_bodies                 | Type check                                                   | Map::par_body_owners     |
| rustc_interface::passes::hir_id_validator::check_crate  | Check the validity of hir                                    | Map::par_for_each_module |
| rustc_interface::passes::analysis                       | Check the validity of loops body, attributes, naked functions, unstable abi, const bodys | Map::par_for_each_module |
| rustc_interface::passes::analysis                       | Liveness and intrinsic checking of MIR                       | Map::par_for_each_module |
| rustc_interface::passes::analysis                       | Deathness checking                                           | Map::par_for_each_module |
| rustc_interface::passes::analysis                       | Privacy checking                                             | Map::par_for_each_module |
| rustc_lint::late::check_crate                           | Run per-module lints                                         | Map::par_for_each_module |
| rustc_typeck::check_crate                               | Well-formedness checking                                         | Map::par_for_each_module |

There are still many loops that have the potential to use parallel iterators.

## Query system

The query model has some properties that make it actually feasible to evaluate
multiple queries in parallel without too much effort:

- All data a query provider can access is via the query context, so
  the query context can take care of synchronizing access.
- Query results are required to be immutable so they can safely be used by
  different threads concurrently.

When a query `foo` is evaluated, the cache table for `foo` is locked.

- If there already is a result, we can clone it, release the lock and
  we are done.
- If there is no cache entry and no other active query invocation computing the
  same result, we mark the key as being "in progress", release the lock and
  start evaluating.
- If there *is* another query invocation for the same key in progress, we
  release the lock, and just block the thread until the other invocation has
  computed the result we are waiting for.
  **Cycle error detection** in the parallel
  compiler requires more complex logic than in single-threaded mode.
  When
  worker threads in parallel queries stop making progress due to interdependence,
  the compiler uses an extra thread *(named deadlock handler)* to detect, remove and
  report the cycle error.

The parallel query feature still has implementation to do, most of which is
related to the previous `Data Structures` and `Parallel Iterators`.
See [this open feature tracking issue][tracking].

## Rustdoc

As of <!-- date-check--> November 2022, there are still a number of steps to
complete before `rustdoc` rendering can be made parallel (see a open discussion
of [parallel `rustdoc`][parallel-rustdoc]).

## Resources

Here are some resources that can be used to learn more:

- [This IRLO thread by alexchricton about performance][irlo1]
- [This IRLO thread by Zoxc, one of the pioneers of the effort][irlo0]
- [This list of interior mutability in the compiler by nikomatsakis][imlist]

[`rayon`]: https://crates.io/crates/rayon
[imlist]: https://github.com/nikomatsakis/rustc-parallelization/blob/master/interior-mutability-list.md
[irlo0]: https://internals.rust-lang.org/t/parallelizing-rustc-using-rayon/6606
[irlo1]: https://internals.rust-lang.org/t/help-test-parallel-rustc/11503
[monomorphization]: backend/monomorph.md
[parallel-rustdoc]: https://github.com/rust-lang/rust/issues/82741
[rustc-rayon]: https://github.com/rust-lang/rustc-rayon
[tracking]: https://github.com/rust-lang/rust/issues/48685
