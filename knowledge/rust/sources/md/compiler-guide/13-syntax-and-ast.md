# Source Code Representation

This part describes the process of taking raw source code from the user and
transforming it into various forms that the compiler can work with easily.
These are called _intermediate representations (IRs)_.

This process starts with compiler understanding what the user has asked for:
parsing the command line arguments given and determining what it is to compile.
After that, the compiler transforms the user input into a series of IRs that
look progressively less like what the user wrote.


---

# Syntax and the AST

Working directly with source code is very inconvenient and error-prone.
Thus, before we do anything else, we convert raw source code into an
[Abstract Syntax Tree (AST)][AST].
It turns out that doing this involves a lot of work,
including [lexing, parsing], [macro expansion], [name resolution], conditional
compilation, [feature-gate checking], and [validation] of the [AST].
In this chapter, we take a look at all of these steps.

Notably, there isn't always a clean ordering between these tasks.
For example, macro expansion relies on name resolution to resolve the names of macros and imports.
And parsing requires macro expansion, which in turn may require parsing the output of the macro.

[AST]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html
[macro expansion]: ./macro-expansion.md
[feature-gate checking]: ./feature-gate-check.md
[lexing, parsing]: ./the-parser.md
[name resolution]: ./name-resolution.md
[validation]: ./ast-validation.md


---

# Lexing and parsing

The very first thing the compiler does is take the program (in UTF-8 Unicode text)
and turn it into a data format the compiler can work with more conveniently than strings.
This happens in two stages: Lexing and Parsing.

  1. _Lexing_ takes strings and turns them into streams of [tokens]. For
  example, `foo.bar + buz` would be turned into the tokens `foo`, `.`, `bar`,
  `+`, and `buz`. This is implemented in [`rustc_lexer`][lexer].

[tokens]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/token/index.html
[lexer]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lexer/index.html

  2. _Parsing_ takes streams of tokens and turns them into a structured form
  which is easier for the compiler to work with, usually called an [*Abstract
  Syntax Tree* (AST)][ast] . 

## The AST

The AST mirrors the structure of a Rust program in memory, using a `Span` to
link a particular AST node back to its source text. The AST is defined in
[`rustc_ast`][rustc_ast], along with some definitions for tokens and token
streams, data structures/traits for mutating ASTs, and shared definitions for
other AST-related parts of the compiler (like the lexer and
macro-expansion).

Every node in the AST has its own [`NodeId`], including top-level items
such as structs, but also individual statements and expressions. A [`NodeId`]
is an identifier number that uniquely identifies an AST node within a crate.

However, because they are absolute within a crate, adding or removing a single
node in the AST causes all the subsequent [`NodeId`]s to change. This renders
[`NodeId`]s pretty much useless for incremental compilation, where you want as
few things as possible to change.

[`NodeId`]s are used in all the `rustc` bits that operate directly on the AST,
like macro expansion and name resolution (more on these over the next couple chapters).

[`NodeId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/node_id/struct.NodeId.html

## Parsing

The parser is defined in [`rustc_parse`][rustc_parse], along with a
high-level interface to the lexer and some validation routines that run after
macro expansion. In particular, the [`rustc_parse::parser`][parser] contains
the parser implementation.

The main entrypoint to the parser is via the various `parse_*` functions and others in
[rustc_parse][rustc_parse]. They let you do things like turn a [`SourceFile`][sourcefile]
(e.g. the source in a single file) into a token stream, create a parser from
the token stream, and then execute the parser to get a [`Crate`] (the root AST
node).

To minimize the amount of copying that is done,
both [`Lexer`] and [`Parser`] have lifetimes which bind them to the parent [`ParseSess`].
This contains all the information needed while parsing, as well as the [`SourceMap`] itself.

Note that while parsing, we may encounter macro definitions or invocations.
We set these aside to be expanded (see [Macro Expansion](./macro-expansion.md)).
Expansion itself may require parsing the output of a macro, which may reveal more macros to be expanded, and so on.

## More on lexical analysis

Code for lexical analysis is split between two crates:

- [`rustc_lexer`] crate is responsible for breaking a `&str` into chunks
  constituting tokens. Although it is popular to implement lexers as generated
  finite state machines, the lexer in [`rustc_lexer`] is hand-written.

- [`Lexer`] integrates [`rustc_lexer`] with data structures specific to
  `rustc`. Specifically, it adds `Span` information to tokens returned by
  [`rustc_lexer`] and interns identifiers.

[`Crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/struct.Crate.html
[`Parser`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/struct.Parser.html
[`ParseSess`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.ParseSess.html
[`rustc_lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lexer/index.html
[`SourceMap`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/source_map/struct.SourceMap.html
[`Lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/lexer/struct.Lexer.html
[ast module]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/index.html
[ast]: ./ast-validation.md
[parser]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/index.html
[rustc_ast]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/index.html
[rustc_errors]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/index.html
[rustc_parse]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/index.html
[sourcefile]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.SourceFile.html
[visit module]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/visit/index.html


---

# Macro expansion

Rust has a very powerful macro system.
In the previous chapter, we saw how
the parser sets aside macros to be expanded (using temporary [placeholders]).
This chapter is about the process of expanding those macros iteratively until
we have a complete [*Abstract Syntax Tree* (AST)][ast] for our crate with no
unexpanded macros (or a compile error).

[ast]: ./ast-validation.md
[placeholders]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/placeholders/index.html

First, we discuss the algorithm that expands and integrates macro output into ASTs.
Next, we take a look at how hygiene data is collected.
Finally, we look at the specifics of expanding different types of macros.

Many of the algorithms and data structures described below are in [`rustc_expand`],
with fundamental data structures in [`rustc_expand::base`][base].

Also of note, `cfg` and `cfg_attr` are treated specially from other macros, and are
handled in [`rustc_expand::config`][cfg].

[`rustc_expand`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/index.html
[base]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/index.html
[cfg]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/config/index.html

## Expansion and AST Integration

Firstly, expansion happens at the crate level.
Given a raw source code for
a crate, the compiler will produce a massive AST with all macros expanded, all
modules inlined, etc. The primary entry point for this process is the
[`MacroExpander::fully_expand_fragment`][fef] method.
With few exceptions, we
use this method on the whole crate (see ["Eager Expansion"](#eager-expansion)
below for more detailed discussion of edge case expansion issues).

[`rustc_builtin_macros`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_builtin_macros/index.html
[reb]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/build/index.html

At a high level, [`fully_expand_fragment`][fef] works in iterations.
We keep a
queue of unresolved macro invocations (i.e. macros we haven't found the
definition of yet).
We repeatedly try to pick a macro from the queue, resolve it, expand it, and integrate it back.
If we can't make progress in an iteration, this represents a compile error.
 Here is the [algorithm][original]:

[fef]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/struct.MacroExpander.html#method.fully_expand_fragment
[original]: https://github.com/rust-lang/rust/pull/53778#issuecomment-419224049

1. Initialize a `queue` of unresolved macros.
2. Repeat until `queue` is empty (or we make no progress, which is an error):
   1. [Resolve](./name-resolution.md) imports in our partially built crate as
      much as possible.
   2. Collect as many macro [`Invocation`s][inv] as possible from our
      partially built crate (`fn`-like, attributes, derives) and add them to the queue.
   3. Dequeue the first element and attempt to resolve it.
   4. If it's resolved:
      1. Run the macro's expander function that consumes a [`TokenStream`] or
         AST and produces a [`TokenStream`] or [`AstFragment`] (depending on
         the macro kind).
         (A [`TokenStream`] is a collection of [`TokenTree`s][tt],
         each of which are a token (punctuation, identifier, or literal) or a
         delimited group (anything inside `()`/`[]`/`{}`)).
         - At this point, we know everything about the macro itself and can
           call [`set_expn_data`] to fill in its properties in the global
           data; that is the [hygiene] data associated with [`ExpnId`] (see
           [Hygiene][hybelow] below).
      2. Integrate that piece of AST into the currently-existing though
         partially-built AST.
         This is essentially where the "token-like mass"
         becomes a proper set-in-stone AST with side-tables.
         It happens as follows:
         - If the macro produces tokens (e.g. a proc macro), we parse into
           an AST, which may produce parse errors.
         - During expansion, we create [`SyntaxContext`]s (hierarchy 2) (see
           [Hygiene][hybelow] below).
         - These three passes happen one after another on every AST fragment
           freshly expanded from a macro:
           - [`NodeId`]s are assigned by [`InvocationCollector`].
             This also collects new macro calls from this new AST piece and
             adds them to the queue.
           - ["Def paths"][defpath] are created and [`DefId`]s are
             assigned to them by [`DefCollector`].
           - Names are put into modules (from the resolver's point of
             view) by [`BuildReducedGraphVisitor`].
      3. After expanding a single macro and integrating its output, continue
         to the next iteration of [`fully_expand_fragment`][fef].
   5. If it's not resolved:
      1. Put the macro back in the queue.
      2. Continue to next iteration...

[`AstFragment`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/enum.AstFragment.html
[`BuildReducedGraphVisitor`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/build_reduced_graph/struct.BuildReducedGraphVisitor.html
[`DefCollector`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/def_collector/struct.DefCollector.html
[`DefId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html
[`ExpnId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnId.html
[`InvocationCollector`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/struct.InvocationCollector.html
[`NodeId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/node_id/struct.NodeId.html
[`set_expn_data`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.LocalExpnId.html#method.set_expn_data
[`SyntaxContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html
[`TokenStream`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/tokenstream/struct.TokenStream.html
[defpath]: hir.md#identifiers-in-the-hir
[hybelow]: #hygiene-and-hierarchies
[hygiene]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/index.html
[inv]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/struct.Invocation.html
[tt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/tokenstream/enum.TokenTree.html

### Error Recovery

If we make no progress in an iteration we have reached a compilation error
(e.g. an undefined macro). We attempt to recover from failures (i.e.
unresolved macros or imports) with the intent of generating diagnostics.
Failure recovery happens by expanding unresolved macros into
[`ExprKind::Err`][err] and allows compilation to continue past the first error
so that `rustc` can report more errors than just the original failure.

[err]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/enum.ExprKind.html#variant.Err

### Name Resolution

Notice that name resolution is involved here: we need to resolve imports and
macro names in the above algorithm.
This is done in [`rustc_resolve::macros`][mresolve], which resolves macro paths, validates
those resolutions, and reports various errors (e.g. "not found", "found, but
it's unstable", "expected x, found y").
However, we don't try to resolve other names yet.
This happens later, as we will see in the chapter: [Name Resolution](./name-resolution.md).

[mresolve]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/macros/index.html

### Eager Expansion

_Eager expansion_ means we expand the arguments of a macro invocation before
the macro invocation itself.
This is implemented only for a few special
built-in macros that expect literals; expanding arguments first for some of
these macro results in a smoother user experience.
As an example, consider the following:

```rust,ignore
macro bar($i: ident) { $i }
macro foo($i: ident) { $i }

foo!(bar!(baz));
```

A lazy-expansion would expand `foo!` first.
An eager-expansion would expand `bar!` first.

Eager-expansion is not a generally available feature of Rust.
Implementing eager-expansion more generally would be challenging, so we implement it for a
few special built-in macros for the sake of user-experience.
The built-in macros are implemented in [`rustc_builtin_macros`], along with some other
early code generation facilities like injection of standard library imports or
generation of test harness.
There are some additional helpers for building AST fragments in [`rustc_expand::build`][reb].
Eager-expansion generally performs a subset of the things that lazy (normal) expansion does.
It is done by invoking [`fully_expand_fragment`][fef] on only part of a crate (as opposed
to the whole crate, like we normally do).

### Other Data Structures

Here are some other notable data structures involved in expansion and integration:
- [`ResolverExpand`] - a `trait` used to break crate dependencies.
  This allows the resolver services to be used in [`rustc_ast`], despite [`rustc_resolve`] and
  pretty much everything else depending on [`rustc_ast`].
- [`ExtCtxt`]/[`ExpansionData`] - holds various intermediate expansion infrastructure data.
- [`Annotatable`] - a piece of AST that can be an attribute target, almost the same
  thing as [`AstFragment`] except for types and patterns that can be produced by
  macros but cannot be annotated with attributes.
- [`MacResult`] - a "polymorphic" AST fragment, something that can turn into
  a different [`AstFragment`] depending on its [`AstFragmentKind`] (i.e. an item,
  expression, pattern, etc).

[`AstFragment`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/enum.AstFragment.html
[`rustc_ast`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/index.html
[`rustc_resolve`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/index.html
[`ResolverExpand`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.ResolverExpand.html
[`ExtCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/struct.ExtCtxt.html
[`ExpansionData`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/struct.ExpansionData.html
[`Annotatable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/enum.Annotatable.html
[`MacResult`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.MacResult.html
[`AstFragmentKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/expand/enum.AstFragmentKind.html

## Hygiene and Hierarchies

If you have ever used the C/C++ preprocessor macros, you know that there are some
annoying and hard-to-debug gotchas!
For example, consider the following C code:

```c
#define DEFINE_FOO struct Bar {int x;}; struct Foo {Bar bar;};

// Then, somewhere else
struct Bar {
    ...
};

DEFINE_FOO
```

Most people avoid writing C like this – and for good reason: it doesn't compile.
The `struct Bar` defined by the macro clashes names with the `struct Bar` defined in the code.
Consider also the following example:

```c
#define DO_FOO(x) {\
    int y = 0;\
    foo(x, y);\
    }

// Then elsewhere
int y = 22;
DO_FOO(y);
```

Do you see the problem?
We wanted to generate a call `foo(22, 0)`, but instead
we got `foo(0, 0)` because the macro defined its own `y`!

These are both examples of _macro hygiene_ issues.
_Hygiene_ relates to how to handle names defined _within a macro_.
In particular, a hygienic macro system prevents errors due to names introduced within a macro.
Rust macros are hygienic in that they do not allow one to write the sorts of bugs above.

At a high level, hygiene within the Rust compiler is accomplished by keeping
track of the context where a name is introduced and used.
We can then disambiguate names based on that context.
Future iterations of the macro system
will allow greater control to the macro author to use that context.
For example,
a macro author may want to introduce a new name to the context where the macro was called.
Alternately, the macro author may be defining a variable for use
only within the macro (i.e. it should not be visible outside the macro).

[code_dir]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_expand/src/mbe
[code_mp]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/mbe/macro_parser
[code_mr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/mbe/macro_rules
[code_parse_int]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/mbe/macro_parser/struct.TtParser.html#method.parse_tt
[parsing]: ./the-parser.html

The context is attached to AST nodes.
All AST nodes generated by macros have context attached.
Additionally, there may be other nodes that have context
attached, such as some desugared syntax (non-macro-expanded nodes are
considered to just have the "root" context, as described below).
Throughout the compiler, we use [`rustc_span::Span`s][span] to refer to code locations.
This struct also has hygiene information attached to it, as we will see later.

[span]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html

Because macros invocations and definitions can be nested, the syntax context of
a node must be a hierarchy.
For example, if we expand a macro and there is
another macro invocation or definition in the generated output, then the syntax
context should reflect the nesting.

However, it turns out that there are actually a few types of context we may
want to track for different purposes.
Thus, there are not just one but _three_
expansion hierarchies that together comprise the hygiene information for a crate.

All of these hierarchies need some sort of "macro ID" to identify individual
elements in the chain of expansions.
This ID is [`ExpnId`].
All macros receive an integer ID, assigned continuously starting from 0 as we discover new macro
calls.
All hierarchies start at [`ExpnId::root`][rootid], which is its own parent.

The [`rustc_span::hygiene`][hy] crate contains all of the hygiene-related algorithms
(with the exception of some hacks in [`Resolver::resolve_crate_root`][hacks])
and structures related to hygiene and expansion that are kept in global data.

The actual hierarchies are stored in [`HygieneData`][hd].
This is a global piece of data containing hygiene and expansion info that can be accessed from
any [`Ident`] without any context.


[`ExpnId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnId.html
[rootid]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnId.html#method.root
[hd]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.HygieneData.html
[hy]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/index.html
[hacks]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/struct.Resolver.html#method.resolve_crate_root
[`Ident`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Ident.html

### The Expansion Order Hierarchy

The first hierarchy tracks the order of expansions, i.e., when a macro
invocation is in the output of another macro.

Here, the children in the hierarchy will be the "innermost" tokens.
The [`ExpnData`] struct itself contains a subset of properties from both macro
definition and macro call available through global data.
[`ExpnData::parent`][edp] tracks the child-to-parent link in this hierarchy.

[`ExpnData`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnData.html
[edp]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnData.html#structfield.parent

For example:

```rust,ignore
macro_rules! foo { () => { println!(); } }

fn main() { foo!(); }
```

In this code, the AST nodes that are finally generated would have hierarchy
`root -> id(foo) -> id(println)`.

### The Macro Definition Hierarchy

The second hierarchy tracks the order of macro definitions, i.e., when we are
expanding one macro another macro definition is revealed in its output.
This one is a bit tricky and more complex than the other two hierarchies.

[`SyntaxContext`][sc] represents a whole chain in this hierarchy via an ID.
[`SyntaxContextData`][scd] contains data associated with the given
[`SyntaxContext`][sc]; mostly it is a cache for results of filtering that chain in different ways.
 [`SyntaxContextData::parent`][scdp] is the child-to-parent
link here, and [`SyntaxContextData::outer_expns`][scdoe] are individual elements in the chain.
The "chaining-operator" is [`SyntaxContext::apply_mark`][am] in compiler code.

A [`Span`][span], mentioned above, is actually just a compact representation of
a code location and [`SyntaxContext`][sc].
Likewise, an [`Ident`] is just an interned
[`Symbol`] + `Span` (i.e. an interned string + hygiene data).

[`Symbol`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Symbol.html
[scd]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContextData.html
[scdp]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContextData.html#structfield.parent
[sc]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html
[scdoe]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContextData.html#structfield.outer_expn
[am]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html#method.apply_mark

For built-in macros, we use the context:
[`SyntaxContext::empty().apply_mark(expn_id)`], and such macros are
considered to be defined at the hierarchy root.
We do the same for `proc macro`s because we haven't implemented cross-crate hygiene yet.

[`SyntaxContext::empty().apply_mark(expn_id)`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html#method.apply_mark

If the token had context `X` before being produced by a macro then after being
produced by the macro it has context `X -> macro_id`.
Here are some examples:

Example 0:

```rust,ignore
macro m() { ident }

m!();
```

Here `ident` which initially has context [`SyntaxContext::root`][scr] has
context `ROOT -> id(m)` after it's produced by `m`.

[scr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.SyntaxContext.html#method.root

Example 1:

```rust,ignore
macro m() { macro n() { ident } }

m!();
n!();
```

In this example the `ident` has context `ROOT` initially, then `ROOT -> id(m)`
after the first expansion, then `ROOT -> id(m) -> id(n)`.

Example 2:

Note that these chains are not entirely determined by their last element, in
other words [`ExpnId`] is not isomorphic to [`SyntaxContext`][sc].

```rust,ignore
macro m($i: ident) { macro n() { ($i, bar) } }

m!(foo);
```

After all expansions, `foo` has context `ROOT -> id(n)` and `bar` has context
`ROOT -> id(m) -> id(n)`.

Currently this hierarchy for tracking macro definitions is subject to the
so-called ["context transplantation hack"][hack]. Modern (i.e. experimental)
macros have stronger hygiene than the legacy "Macros By Example" (MBE)
system which can result in weird interactions between the two.
The hack is intended to make things "just work" for now.

[`ExpnId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnId.html
[hack]: https://github.com/rust-lang/rust/pull/51762#issuecomment-401400732

### The Call-site Hierarchy

The third and final hierarchy tracks the location of macro invocations.

In this hierarchy [`ExpnData::call_site`][callsite] is the `child -> parent` link.

[callsite]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/hygiene/struct.ExpnData.html#structfield.call_site

Here is an example:

```rust,ignore
macro bar($i: ident) { $i }
macro foo($i: ident) { $i }

foo!(bar!(baz));
```

For the `baz` AST node in the final output, the expansion-order hierarchy is
`ROOT -> id(foo) -> id(bar) -> baz`, while the call-site hierarchy is `ROOT -> baz`.

### Macro Backtraces

Macro backtraces are implemented in [`rustc_span`] using the hygiene machinery
in [`rustc_span::hygiene`][hy].

[`rustc_span`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/index.html

## Producing Macro Output

Above, we saw how the output of a macro is integrated into the AST for a crate,
and we also saw how the hygiene data for a crate is generated.
But how do we actually produce the output of a macro?
It depends on the type of macro.

There are two types of macros in Rust:
  1. `macro_rules!` macros (a.k.a.
     "Macros By Example" (MBE)), and,
  2. procedural macros (proc macros); including custom derives.

During the parsing phase, the normal Rust parser will set aside the contents of
macros and their invocations.
Later, macros are expanded using these portions of the code.

Some important data structures/interfaces here:
- [`SyntaxExtension`] - a lowered macro representation, contains its expander
  function, which transforms a [`TokenStream`] or AST into another
  [`TokenStream`] or AST + some additional data like stability, or a list of
  unstable features allowed inside the macro.
- [`SyntaxExtensionKind`] - expander functions may have several different
  signatures (take one token stream, or two, or a piece of AST, etc).
  This is an `enum` that lists them.
- [`BangProcMacro`]/[`TTMacroExpander`]/[`AttrProcMacro`]/[`MultiItemModifier`] -
  `trait`s representing the expander function signatures.

[`SyntaxExtension`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/struct.SyntaxExtension.html
[`SyntaxExtensionKind`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/enum.SyntaxExtensionKind.html
[`BangProcMacro`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.BangProcMacro.html
[`TTMacroExpander`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.TTMacroExpander.html
[`AttrProcMacro`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.AttrProcMacro.html
[`MultiItemModifier`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/base/trait.MultiItemModifier.html

## Macros By Example

MBEs have their own parser distinct from the Rust parser.
When macros are expanded, we may invoke the MBE parser to parse and expand a macro.
 The MBE parser, in turn, may call the Rust parser when it needs to bind a
metavariable (e.g. `$my_expr`) while parsing the contents of a macro
invocation.
The code for macro expansion is in [`compiler/rustc_expand/src/mbe/`][code_dir].

### Example

```rust,ignore
macro_rules! printer {
    (print $mvar:ident) => {
        println!("{}", $mvar);
    };
    (print twice $mvar:ident) => {
        println!("{}", $mvar);
        println!("{}", $mvar);
    };
}
```

Here `$mvar` is called a _metavariable_.
Unlike normal variables, rather than
binding to a value _at runtime_, a metavariable binds _at compile time_ to a tree of _tokens_.
A _token_ is a single "unit" of the grammar, such as an
identifier (e.g. `foo`) or punctuation (e.g. `=>`). There are also other
special tokens, such as `EOF`, which itself indicates that there are no more tokens.
There are token trees resulting from the paired parentheses-like
characters (`(`...`)`, `[`...`]`, and `{`...`}`) – they include the open and
close and all the tokens in between (Rust requires that parentheses-like characters be balanced).
Having macro expansion operate on token streams
rather than the raw bytes of a source-file abstracts away a lot of complexity.
The macro expander (and much of the rest of the compiler) doesn't consider
the exact line and column of some syntactic construct in the code; it considers
which constructs are used in the code.
Using tokens allows us to care about _what_ without worrying about _where_.
For more information about tokens, see the [Parsing][parsing] chapter of this book.

```rust,ignore
printer!(print foo); // `foo` is a variable
```

The process of expanding the macro invocation into the syntax tree
`println!("{}", foo)` and then expanding the syntax tree into a call to
`Display::fmt` is one common example of _macro expansion_.

### The MBE parser

There are two parts to MBE expansion done by the macro parser:
  1. parsing the definition, and,
  2. parsing the invocations.

We think of the MBE parser as a nondeterministic finite automaton (NFA) based
regex parser since it uses an algorithm similar in spirit to the [Earley
parsing algorithm](https://en.wikipedia.org/wiki/Earley_parser).
The macro parser is defined in [`compiler/rustc_expand/src/mbe/macro_parser.rs`][code_mp].

The interface of the macro parser is as follows (this is slightly simplified):

```rust,ignore
fn parse_tt(
    &mut self,
    parser: &mut Cow<'_, Parser<'_>>,
    matcher: &[MatcherLoc]
) -> ParseResult
```

We use these items in macro parser:

- a `parser` variable is a reference to the state of a normal Rust parser,
  including the token stream and parsing session.
  The token stream is what we are about to ask the MBE parser to parse.
  We will consume the raw stream of
  tokens and output a binding of metavariables to corresponding token trees.
  The parsing session can be used to report parser errors.
- a `matcher` variable is a sequence of [`MatcherLoc`]s that we want to match the token stream
  against.
  They're converted from the original token trees in the macro's definition before matching.

[`MatcherLoc`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/mbe/macro_parser/enum.MatcherLoc.html

In the analogy of a regex parser, the token stream is the input and we are
matching it against the pattern defined by matcher.
Using our examples, the
token stream could be the stream of tokens containing the inside of the example
invocation `print foo`, while matcher might be the sequence of token (trees) `print $mvar:ident`.

The output of the parser is a [`ParseResult`], which indicates which of three cases has occurred:

- **Success**: the token stream matches the given matcher and we have produced a
  binding from metavariables to the corresponding token trees.
- **Failure**: the token stream does not match matcher and results in an error
  message such as "No rule expected token ...".
- **Error**: some fatal error has occurred _in the parser_.
  For example, this happens if there is more than one pattern match, since that indicates the
  macro is ambiguous.

The full interface is defined [here][code_parse_int].

The macro parser does pretty much exactly the same as a normal regex parser
with one exception: in order to parse different types of metavariables, such as
`ident`, `block`, `expr`, etc., the macro parser must call back to the normal
Rust parser.

The code to parse macro definitions is in [`compiler/rustc_expand/src/mbe/macro_rules.rs`][code_mr].
For more information about the macro parser's implementation, see the comments in
[`compiler/rustc_expand/src/mbe/macro_parser.rs`][code_mp].

Using our example, we would try to match the token stream `print foo` from the invocation against
the matchers `print $mvar:ident` and `print twice $mvar:ident` that we previously extracted from the
rules in the macro definition.
When the macro parser comes to a place in the current matcher where
it needs to match a _non-terminal_ (e.g. `$mvar:ident`), it calls back to the normal Rust parser to
get the contents of that non-terminal.
In this case, the Rust parser would look for an `ident`
token, which it finds (`foo`) and returns to the macro parser.
Then, the macro parser continues parsing.

Note that exactly one of the matchers from the various rules should match the invocation; if there is
more than one match, the parse is ambiguous, while if there are no matches at all, there is a syntax
error.

Assuming exactly one rule matches, macro expansion will then *transcribe* the right-hand side of the
rule, substituting the values of any matches it captured when matching against the left-hand side.

## Procedural Macros

Procedural macros are also expanded during parsing.
However, rather than having a parser in the compiler, proc macros are implemented as custom,
third-party crates.
The compiler will compile the proc macro crate and
specially annotated functions in them (i.e. the proc macro itself), passing
them a stream of tokens.
A proc macro can then transform the token stream and
output a new token stream, which is synthesized into the AST.

The token stream type used by proc macros is _stable_, so `rustc` does not use it internally.
The compiler's (unstable) token stream is defined in
[`rustc_ast::tokenstream::TokenStream`][rustcts].
This is converted into the stable [`proc_macro::TokenStream`][stablets] and back in
[`rustc_expand::proc_macro`][pm] and [`rustc_expand::proc_macro_server`][pms].
Since the Rust ABI is currently unstable, we use the C ABI for this conversion.

[tsmod]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/tokenstream/index.html
[rustcts]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/tokenstream/struct.TokenStream.html
[stablets]: https://doc.rust-lang.org/proc_macro/struct.TokenStream.html
[pm]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/proc_macro/index.html
[pms]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/proc_macro_server/index.html
[`ParseResult`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/mbe/macro_parser/enum.ParseResult.html

<!-- TODO(rylev): more here. [#1160](https://github.com/rust-lang/rustc-dev-guide/issues/1160) -->

### Custom Derive

Custom derives are a special type of proc macro.

### Macros By Example and Macros 2.0

There is an legacy and mostly undocumented effort to improve the MBE system
by giving it more hygiene-related features, better scoping and visibility
rules, etc. Internally this uses the same machinery as today's MBEs with some
additional syntactic sugar and are allowed to be in namespaces.

<!-- TODO(rylev): more? [#1160](https://github.com/rust-lang/rustc-dev-guide/issues/1160) -->


---

# Name resolution

In the previous chapters, we saw how the [*Abstract Syntax Tree* (`AST`)][ast]
is built with all macros expanded. We saw how doing that requires doing some
name resolution to resolve imports and macro names. In this chapter, we show
how this is actually done and more.

[ast]: ./ast-validation.md

In fact, we don't do full name resolution during macro expansion -- we only
resolve imports and macros at that time. This is required to know what to even
expand. Later, after we have the whole AST, we do full name resolution to
resolve all names in the crate. This happens in [`rustc_resolve::late`][late].
Unlike during macro expansion, in this late expansion, we only need to try to
resolve a name once, since no new names can be added. If we fail to resolve a
name, then it is a compiler error.

Name resolution is complex. There are different namespaces (e.g.
macros, values, types, lifetimes), and names may be valid at different (nested)
scopes. Also, different types of names can fail resolution differently, and
failures can happen differently at different scopes. For example, in a module
scope, failure means no unexpanded macros and no unresolved glob imports in
that module. On the other hand, in a function body scope, failure requires that a
name be absent from the block we are in, all outer scopes, and the global
scope.

[late]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/late/index.html

## Basics

In our programs we refer to variables, types, functions, etc, by giving them
a name. These names are not always unique. For example, take this valid Rust
program:

```rust
type x = u32;
let x: x = 1;
let y: x = 2;
```

How do we know on line 3 whether `x` is a type (`u32`) or a value (1)? These
conflicts are resolved during name resolution. In this specific case, name
resolution defines that type names and variable names live in separate
namespaces and therefore can co-exist.

The name resolution in Rust is a two-phase process. In the first phase, which runs
during `macro` expansion, we build a tree of modules and resolve imports. Macro
expansion and name resolution communicate with each other via the
[`ResolverAstLoweringExt`] trait.

The input to the second phase is the syntax tree, produced by parsing input
files and expanding `macros`. This phase produces links from all the names in the
source to relevant places where the name was introduced. It also generates
helpful error messages, like typo suggestions, traits to import or lints about
unused items.

A successful run of the second phase ([`Resolver::resolve_crate`]) creates kind
of an index the rest of the compilation may use to ask about the present names
(through the `hir::lowering::Resolver` interface).

The name resolution lives in the [`rustc_resolve`] crate, with the bulk in
`lib.rs` and some helpers or symbol-type specific logic in the other modules.

[`Resolver::resolve_crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/struct.Resolver.html#method.resolve_crate
[`ResolverAstLoweringExt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/trait.ResolverAstLoweringExt.html
[`rustc_resolve`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/index.html

## Namespaces

Different kind of symbols live in different namespaces ‒ e.g. types don't
clash with variables. This usually doesn't happen, because variables start with
lower-case letter while types with upper-case one, but this is only a
convention. This is legal Rust code that will compile (with warnings):

```rust
type x = u32;
let x: x = 1;
let y: x = 2; // See? x is still a type here.
```

To cope with this, and with slightly different scoping rules for these
namespaces, the resolver keeps them separated and builds separate structures for
them.

In other words, when the code talks about namespaces, it doesn't mean the module
hierarchy, it's types vs. values vs. macros.

## Scopes and ribs

A name is visible only in certain area in the source code. This forms a
hierarchical structure, but not necessarily a simple one ‒ if one scope is
part of another, it doesn't mean a name visible in the outer scope is also
visible in the inner scope, or that it refers to the same thing.

To cope with that, the compiler introduces the concept of [`Rib`]s. This is
an abstraction of a scope. Every time the set of visible names potentially changes,
a new [`Rib`] is pushed onto a stack. The places where this can happen include for
example:

[`Rib`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/late/struct.Rib.html

* The obvious places ‒ curly braces enclosing a block, function boundaries,
  modules.
* Introducing a `let` binding ‒ this can shadow another binding with the same
  name.
* Macro expansion border ‒ to cope with macro hygiene.

When searching for a name, the stack of [`ribs`] is traversed from the innermost
outwards. This helps to find the closest meaning of the name (the one not
shadowed by anything else). The transition to outer [`Rib`] may also affect
what names are usable ‒ if there are nested functions (not closures),
the inner one can't access parameters and local bindings of the outer one,
even though they should be visible by ordinary scoping rules. An example:

[`ribs`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/late/struct.LateResolutionVisitor.html#structfield.ribs

```rust
fn do_something<T: Default>(val: T) { // <- New rib in both types and values (1)
    // `val` is accessible, as is the helper function
    // `T` is accessible
   let helper = || { // New rib on the block (2)
        // `val` is accessible here
    }; // End of (2), new rib on `helper` (3)
    // `val` is accessible, `helper` variable shadows `helper` function
    fn helper() { // <- New rib in both types and values (4)
        // `val` is not accessible here, (4) is not transparent for locals
        // `T` is not accessible here
    } // End of (4)
    let val = T::default(); // New rib (5)
    // `val` is the variable, not the parameter here
} // End of (5), (3) and (1)
```

Because the rules for different namespaces are a bit different, each namespace
has its own independent [`Rib`] stack that is constructed in parallel to the others.
In addition, there's also a [`Rib`] stack for local labels (e.g. names of loops or
blocks), which isn't a full namespace in its own right.

## Overall strategy

To perform the name resolution of the whole crate, the syntax tree is traversed
top-down and every encountered name is resolved. This works for most kinds of
names, because at the point of use of a name it is already introduced in the [`Rib`]
hierarchy.

There are some exceptions to this. Items are bit tricky, because they can be
used even before encountered ‒ therefore every block needs to be first scanned
for items to fill in its [`Rib`].

Other, even more problematic ones, are imports which need recursive fixed-point
resolution and macros, that need to be resolved and expanded before the rest of
the code can be processed.

Therefore, the resolution is performed in multiple stages.

## Speculative crate loading

To give useful errors, rustc suggests importing paths into scope if they're
not found. How does it do this? It looks through every module of every crate
and looks for possible matches. This even includes crates that haven't yet
been loaded!

Eagerly loading crates to include import suggestions that haven't yet been
loaded is called _speculative crate loading_, because any errors it encounters
shouldn't be reported: [`rustc_resolve`] decided to load them, not the user. The function
that does this is [`lookup_import_candidates`] and lives in
[`rustc_resolve::diagnostics`].

[`rustc_resolve`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/index.html
[`lookup_import_candidates`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/struct.Resolver.html#method.lookup_import_candidates
[`rustc_resolve::diagnostics`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_resolve/diagnostics/index.html

To tell the difference between speculative loads and loads initiated by the
user, [`rustc_resolve`] passes around a `record_used` parameter, which is `false` when
the load is speculative.

## TODO: [#16](https://github.com/rust-lang/rustc-dev-guide/issues/16)

This is a result of the first pass of learning the code. It is definitely
incomplete and not detailed enough. It also might be inaccurate in places.
Still, it probably provides useful first guidepost to what happens in there.

* What exactly does it link to and how is that published and consumed by
  following stages of compilation?
* Who calls it and how it is actually used.
* Is it a pass and then the result is only used, or can it be computed
  incrementally?
* The overall strategy description is a bit vague.
* Where does the name `Rib` come from?
* Does this thing have its own tests, or is it tested only as part of some e2e
  testing?


---

# Attributes

Attributes come in two types: *inert* (or *built-in*) and *active* (*non-builtin*).

## Builtin/inert attributes

These attributes are defined in the compiler itself, in
[`compiler/rustc_feature/src/builtin_attrs.rs`][builtin_attrs].

Examples include `#[allow]` and `#[macro_use]`.

[builtin_attrs]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_feature/builtin_attrs/index.html

These attributes have several important characteristics:
* They are always in scope, and do not participate in typical path-based resolution.
* They cannot be renamed. For example, `use allow as foo` will compile, but writing `#[foo]` will
  produce an error.
* They are 'inert', meaning they are left as-is by the macro expansion code.
  As a result, any behavior comes as a result of the compiler explicitly checking for their presence.
  For example, lint-related code explicitly checks for `#[allow]`, `#[warn]`, `#[deny]`, and
  `#[forbid]`, rather than the behavior coming from the expansion of the attributes themselves.

## 'Non-builtin'/'active' attributes

These attributes are defined by a crate - either the standard library, or a proc-macro crate.

**Important**: Many non-builtin attributes, such as `#[derive]`, are still considered part of the
core Rust language. However, they are **not** called 'builtin attributes', since they have a
corresponding definition in the standard library.

Definitions of non-builtin attributes take two forms:

1. Proc-macro attributes, defined via a function annotated with `#[proc_macro_attribute]` in a
   proc-macro crate.
2. AST-based attributes, defined in the standard library. These attributes have special 'stub'
   macros defined in places like [`library/core/src/macros/mod.rs`][core_macros].

[core_macros]:  https://github.com/rust-lang/rust/blob/HEAD/library/core/src/macros/mod.rs

These definitions exist to allow the macros to participate in typical path-based resolution - they
can be imported, re-exported, and renamed just like any other item definition. However, the body of
the definition is empty. Instead, the macro is annotated with the `#[rustc_builtin_macro]`
attribute, which tells the compiler to run a corresponding function in `rustc_builtin_macros`.

All non-builtin attributes have the following characteristics:
* Like all other definitions (e.g. structs), they must be brought into scope via an import.
  Many standard library attributes are included in the prelude - this is why writing `#[derive]`
  works without an import.
* They participate in macro expansion. The implementation of the macro may leave the attribute
  target unchanged, modify the target, produce new AST nodes, or remove the target entirely.


---

# The `#[test]` attribute



Many Rust programmers rely on a built-in attribute called `#[test]`. All
you have to do is mark a function and include some asserts like so:


```rust,ignore
#[test]
fn my_test() {
    assert!(2+2 == 4);
}
```

When this program is compiled using `rustc --test` or `cargo test`, it will
produce an executable that can run this, and any other test function. This
method of testing allows tests to live alongside code in an organic way. You
can even put tests inside private modules:

```rust,ignore
mod my_priv_mod {
    fn my_priv_func() -> bool {}

    #[test]
    fn test_priv_func() {
        assert!(my_priv_func());
    }
}
```

Private items can thus be easily tested without worrying about how to expose
them to any sort of external testing apparatus. This is key to the
ergonomics of testing in Rust. Semantically, however, it's rather odd.
How does any sort of `main` function invoke these tests if they're not visible?
What exactly is `rustc --test` doing?

`#[test]` is implemented as a syntactic transformation inside the compiler's
[`rustc_ast`][rustc_ast]. Essentially, it's a fancy [`macro`] that
rewrites the crate in 3 steps:

## Step 1: Re-Exporting

As mentioned earlier, tests can exist inside private modules, so we need a
way of exposing them to the main function, without breaking any existing
code. To that end, [`rustc_ast`][rustc_ast] will create local modules called
`__test_reexports` that recursively reexport tests. This expansion translates
the above example into:

```rust,ignore
mod my_priv_mod {
    fn my_priv_func() -> bool {}

    pub fn test_priv_func() {
        assert!(my_priv_func());
    }

    pub mod __test_reexports {
        pub use super::test_priv_func;
    }
}
```

Now, our test can be accessed as
`my_priv_mod::__test_reexports::test_priv_func`. For deeper module
structures, `__test_reexports` will reexport modules that contain tests, so a
test at `a::b::my_test` becomes
`a::__test_reexports::b::__test_reexports::my_test`. While this process seems
pretty safe, what happens if there is an existing `__test_reexports` module?
The answer: nothing.

To explain, we need to understand how Rust's [Abstract Syntax Tree][ast]
represents [identifiers][Ident]. The name of every function, variable, module,
etc. is not stored as a string, but rather as an opaque [Symbol][Symbol] which
is essentially an ID number for each identifier. The compiler keeps a separate
hashtable that allows us to recover the human-readable name of a Symbol when
necessary (such as when printing a syntax error). When the compiler generates
the `__test_reexports` module, it generates a new [Symbol][Symbol] for the
identifier, so while the compiler-generated `__test_reexports` may share a name
with your hand-written one, it will not share a [Symbol][Symbol]. This
technique prevents name collision during code generation and is the foundation
of Rust's [`macro`] hygiene.

## Step 2: Harness generation

Now that our tests are accessible from the root of our crate, we need to do
something with them using [`rustc_ast`][ast] generates a module like so:

```rust,ignore
#[main]
pub fn main() {
    extern crate test;
    test::test_main_static(&[&path::to::test1, /*...*/]);
}
```

Here `path::to::test1` is a constant of type [`test::TestDescAndFn`][tdaf].

While this transformation is simple, it gives us a lot of insight into how
tests are actually run. The tests are aggregated into an array and passed to
a test runner called `test_main_static`. We'll come back to exactly what
[`TestDescAndFn`][tdaf] is, but for now, the key takeaway is that there is a crate
called [`test`][test] that is part of Rust core, that implements all of the
runtime for testing. [`test`][test]'s interface is unstable, so the only stable way
to interact with it is through the `#[test]` macro.

## Step 3: Test object generation

If you've written tests in Rust before, you may be familiar with some of the
optional attributes available on test functions. For example, a test can be
annotated with `#[should_panic]` if we expect the test to cause a panic. It
looks something like this:

```rust,ignore
#[test]
#[should_panic]
fn foo() {
    panic!("intentional");
}
```

This means our tests are more than just simple functions, they have
configuration information as well. `test` encodes this configuration data into
a `struct` called [`TestDesc`]. For each test function in a crate,
[`rustc_ast`][rustc_ast] will parse its attributes and generate a [`TestDesc`]
instance. It then combines the [`TestDesc`] and test function into the
predictably named [`TestDescAndFn`][tdaf] `struct`, that [`test_main_static`]
operates on.
For a given test, the generated [`TestDescAndFn`][tdaf] instance looks like so:

```rust,ignore
self::test::TestDescAndFn{
  desc: self::test::TestDesc{
    name: self::test::StaticTestName("foo"),
    ignore: false,
    should_panic: self::test::ShouldPanic::Yes,
    allow_fail: false,
  },
  testfn: self::test::StaticTestFn(||
    self::test::assert_test_result(::crate::__test_reexports::foo())),
}
```

Once we've constructed an array of these test objects, they're passed to the
test runner via the harness generated in Step 2.

## Inspecting the generated code

On `nightly` `rustc`, there's an unstable flag called `unpretty` that you can use
to print out the module source after [`macro`] expansion:

```bash
$ rustc my_mod.rs -Z unpretty=hir
```

[`macro`]: ./macro-expansion.md
[`TestDesc`]: https://doc.rust-lang.org/test/struct.TestDesc.html
[ast]: ./ast-validation.md
[Ident]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Ident.html
[rustc_ast]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_ast
[Symbol]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Symbol.html
[test]: https://doc.rust-lang.org/test/index.html
[tdaf]: https://doc.rust-lang.org/test/struct.TestDescAndFn.html
[`test_main_static`]: https://doc.rust-lang.org/test/fn.test_main_static.html


---

# Panicking in Rust

## Step 1: Invocation of the `panic!` macro.

There are actually two panic macros - one defined in `core`, and one defined in `std`.
This is due to the fact that code in `core` can panic. `core` is built before `std`,
but we want panics to use the same machinery at runtime, whether they originate in `core`
or `std`.

### core definition of panic!

The `core` `panic!` macro eventually makes the following call (in `library/core/src/panicking.rs`):

```rust
// NOTE This function never crosses the FFI boundary; it's a Rust-to-Rust call
extern "Rust" {
    #[lang = "panic_impl"]
    fn panic_impl(pi: &PanicInfo<'_>) -> !;
}

let pi = PanicInfo::internal_constructor(Some(&fmt), location);
unsafe { panic_impl(&pi) }
```

Actually resolving this goes through several layers of indirection:

1. In `compiler/rustc_middle/src/middle/weak_lang_items.rs`, `panic_impl` is
   declared as 'weak lang item', with the symbol `rust_begin_unwind`. This is
   used in `rustc_hir_analysis/src/collect.rs` to set the actual symbol name to
   `rust_begin_unwind`.

   Note that `panic_impl` is declared in an `extern "Rust"` block,
   which means that core will attempt to call a foreign symbol called `rust_begin_unwind`
   (to be resolved at link time)

2. In `library/std/src/panicking.rs`, we have this definition:

```rust
/// Entry point of panic from the core crate.
#[cfg(not(test))]
#[panic_handler]
#[unwind(allowed)]
pub fn begin_panic_handler(info: &PanicInfo<'_>) -> ! {
    ...
}
```

The special `panic_handler` attribute is resolved via `compiler/rustc_middle/src/middle/lang_items`.
The `extract` function converts the `panic_handler` attribute to a `panic_impl` lang item.

Now, we have a matching `panic_handler` lang item in the `std`. This function goes
through the same process as the `extern { fn panic_impl }` definition in `core`, ending
up with a symbol name of `rust_begin_unwind`. At link time, the symbol reference in `core`
will be resolved to the definition of `std` (the function called `begin_panic_handler` in the
Rust source).

Thus, control flow will pass from core to std at runtime. This allows panics from `core`
to go through the same infrastructure that other panics use (panic hooks, unwinding, etc)

### std implementation of panic!

This is where the actual panic-related logic begins. In `library/std/src/panicking.rs`,
control passes to `rust_panic_with_hook`. This method is responsible
for invoking the global panic hook, and checking for double panics. Finally,
we call `__rust_start_panic`, which is provided by the panic runtime.

The call to `__rust_start_panic` is very weird - it is passed a `*mut &mut dyn PanicPayload`,
converted to an `usize`. Let's break this type down:

1. `PanicPayload` is an internal trait. It is implemented for `PanicPayload`
(a wrapper around the user-supplied payload type), and has a method
`fn take_box(&mut self) -> *mut (dyn Any + Send)`.
This method takes the user-provided payload (`T: Any + Send`),
boxes it, and converts the box to a raw pointer.

2. When we call `__rust_start_panic`, we have an `&mut dyn PanicPayload`.
However, this is a fat pointer (twice the size of a `usize`).
To pass this to the panic runtime across an FFI boundary, we take a mutable
reference *to this mutable reference* (`&mut &mut dyn PanicPayload`), and convert it to a raw
pointer (`*mut &mut dyn PanicPayload`). The outer raw pointer is a thin pointer, since it points to
a `Sized` type (a mutable reference). Therefore, we can convert this thin pointer into a `usize`,
which is suitable for passing across an FFI boundary.

Finally, we call `__rust_start_panic` with this `usize`. We have now entered the panic runtime.

## Step 2: The panic runtime

Rust provides two panic runtimes: `panic_abort` and `panic_unwind`. The user chooses
between them at build time via their `Cargo.toml`

`panic_abort` is extremely simple: its implementation of `__rust_start_panic` just aborts,
as you would expect.

`panic_unwind` is the more interesting case.

In its implementation of `__rust_start_panic`, we take the `usize`, convert
it back to a `*mut &mut dyn PanicPayload`, dereference it, and call `take_box`
on the `&mut dyn PanicPayload`. At this point, we have a raw pointer to the payload
itself (a `*mut (dyn Send + Any)`): that is, a raw pointer to the actual value
provided by the user who called `panic!`.

At this point, the platform-independent code ends. We now call into
platform-specific unwinding logic (e.g `unwind`). This code is
responsible for unwinding the stack, running any 'landing pads' associated
with each frame (currently, running destructors), and transferring control
to the `catch_unwind` frame.

Note that all panics either abort the process or get caught by some call to `catch_unwind`.
In particular, in std's [runtime service],
the call to the user-provided `main` function is wrapped in `catch_unwind`.


[runtime service]: https://github.com/rust-lang/rust/blob/HEAD/library/std/src/rt.rs


---

# AST validation

_AST validation_ is a separate AST pass that visits each
item in the tree and performs simple checks. This pass
doesn't perform any complex analysis, type checking or
name resolution.

Before performing any validation, the compiler first expands
the macros. Then this pass performs validations to check
that each AST item is in the correct state. And when this pass
is done, the compiler runs the crate resolution pass.

## Validations

Validations are defined in `AstValidator` type, which 
itself is located in `rustc_ast_passes` crate. This
type implements various simple checks which emit errors
when certain language rules are broken.

In addition, `AstValidator` implements `Visitor` trait
that defines how to visit AST items (which can be functions,
traits, enums, etc).

For each item, visitor performs specific checks. For
example, when visiting a function declaration,
`AstValidator` checks that the function has:

* no more than `u16::MAX` parameters;
* c-variadic argument goes the last in the declaration;
* documentation comments aren't applied to function parameters;
* and other validations.


---

# Feature Gate Checking

For the how-to steps to add, remove, rename, or stabilize feature gates,
see [Feature gates][feature-gates].

Feature gates prevent usage of unstable language and library features without a
nightly-only `#![feature(...)]` opt-in.
This chapter documents the implementation
of feature gating: where gates are defined, how they are enabled, and how usage is verified.

<!-- date-check: Feb 2026 -->

## Feature Definitions

All feature gate definitions are located in the `rustc_feature` crate:

- **Unstable features** are declared in [`rustc_feature/src/unstable.rs`] via
  the `declare_features!` macro.
  This associates features with issue numbers and tracking metadata.
- **Accepted features** (stabilized) are listed in [`rustc_feature/src/accepted.rs`].
- **Removed features** (explicitly disallowed) are listed in [`rustc_feature/src/removed.rs`].
- **Gated built-in attributes and cfgs** are declared in [`rustc_feature/src/builtin_attrs.rs`].

The [`rustc_feature::Features`] type represents the **active feature set** for a crate.
Helpers like `enabled`, `incomplete`, and `internal` are used during compilation to check status.

## Collecting Features

Before AST validation or expansion, `rustc` collects crate-level
`#![feature(...)]` attributes to build the active `Features` set.

- The collection happens in [`rustc_expand/src/config.rs`] in [`features`].
- Each `#![feature]` entry is classified against the `unstable`, `accepted`, and `removed` tables:
  - **Removed** features cause an immediate error.
  - **Accepted** features are recorded but do not require nightly.
    On stable/beta, `maybe_stage_features` in
    [`rustc_ast_passes/src/feature_gate.rs`] emits the non-nightly
    diagnostic and lists stable features, which is where the "already
    stabilized" messaging comes from.
  - **Unstable** features are recorded as enabled.
  - Unknown features are treated as **library features** and validated later.
- With `-Z allow-features=...`, any **unstable** or **unknown** feature
  not in the allowlist is rejected.
- [`RUSTC_BOOTSTRAP`] feeds into `UnstableFeatures::from_environment`.
  This variable controls whether the compiler is treated as "nightly", allowing
  feature gates to be bypassed during bootstrapping or explicitly disabled (`-1`).

## Parser Gating

Some syntax is detected and gated during parsing.
The parser records spans for
later checking to keep diagnostics consistent and deferred until after parsing.

- [`rustc_session/src/parse.rs`] defines [`GatedSpans`] and the `gate` method.
- The parser uses it in [`rustc_parse/src/parser/*`] when it encounters
  syntax that requires a gate (e.g., `async for`, `yield`, experimental patterns).

## Checking Pass

The central logic lives in [`rustc_ast_passes/src/feature_gate.rs`], primarily
in `check_crate` and its AST visitor.

### `check_crate`

`check_crate` performs high-level validation:

- `maybe_stage_features`: Rejects `#![feature]` on stable/beta.
- `check_incompatible_features`: Ensures incompatible feature combinations
  (declared in `rustc_feature::INCOMPATIBLE_FEATURES`) are not used together.
- `check_new_solver_banned_features`: Bans features incompatible with
  compiler mode for the next trait solver.
- **Parser-gated spans**: Processes the `GatedSpans` recorded during parsing
  (see [Checking `GatedSpans`](#checking-gatedspans)).

### Checking `GatedSpans`

`check_crate` iterates over `sess.psess.gated_spans`:

- The `gate_all!` macro emits diagnostics for each gated span if the feature is not enabled.
- Some gates have extra logic (e.g., `yield` can be allowed by `coroutines` or
  `gen_blocks`).
- Legacy gates (e.g., `box_patterns`, `try_blocks`) may use a separate path that
  emits future-incompatibility warnings instead of hard errors.

### AST Visitor

A `PostExpansionVisitor` walks the expanded AST to check constructs that are
easier to validate after expansion.

- The visitor uses helper macros (`gate!`, `gate_alt!`, `gate_multi!`) to check:
  1. Is the feature enabled?
  2. Does `span.allows_unstable` permit it (for internal compiler macros)?
- Examples include `trait_alias`, `decl_macro`, `extern types`, and various `impl Trait` forms.

## Attributes and `cfg`

Beyond syntax, rustc also gates attributes and `cfg` options.

### Built-in attributes

- [`rustc_ast_passes::check_attribute`] inspects attributes against `BUILTIN_ATTRIBUTE_MAP`.
- If the attribute is `AttributeGate::Gated` and the feature isn’t enabled,
  `feature_err` is emitted.

### `cfg` options

- [`rustc_attr_parsing/src/attributes/cfg.rs`] defines `gate_cfg` and uses
  [`rustc_feature::find_gated_cfg`] to reject gated `cfg`s.
- `gate_cfg` respects `Span::allows_unstable`, allowing internal compiler
  macros to bypass `cfg` gates when marked with `#[allow_internal_unstable]`.
- The gated cfg list is defined in [`rustc_feature/src/builtin_attrs.rs`].

## Diagnostics

Diagnostic helpers are located in [`rustc_session/src/parse.rs`].

- `feature_err` and `feature_warn` emit standardized diagnostics, attaching the
  tracking issue number where possible.
- `Span::allows_unstable` in [`rustc_span/src/lib.rs`] checks if a span originates
  from a macro marked with `#[allow_internal_unstable]`.
  This allows internal
  macros to use unstable features on stable channels while enforcing gates for user code.

[`rustc_feature/src/unstable.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_feature/src/unstable.rs
[`rustc_feature/src/removed.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_feature/src/removed.rs
[`rustc_feature/src/accepted.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_feature/src/accepted.rs
[`rustc_feature/src/builtin_attrs.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_feature/src/builtin_attrs.rs
[`rustc_feature::Features`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_feature/struct.Features.html
[`rustc_expand/src/config.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_expand/src/config.rs
[`features`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_expand/config/fn.features.html
[`RUSTC_BOOTSTRAP`]: https://doc.rust-lang.org/beta/unstable-book/compiler-environment-variables/RUSTC_BOOTSTRAP.html
[`rustc_session/src/parse.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_session/src/parse.rs
[`GatedSpans`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.GatedSpans.html
[`rustc_ast_passes/src/feature_gate.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_ast_passes/src/feature_gate.rs
[`rustc_parse/src/parser/*`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/parser/index.html
[`rustc_ast_passes::check_attribute`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_passes/feature_gate/fn.check_attribute.html
[`rustc_attr_parsing/src/attributes/cfg.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_attr_parsing/src/attributes/cfg.rs
[`rustc_feature::find_gated_cfg`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_feature/fn.find_gated_cfg.html
[`rustc_span/src/lib.rs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_span/src/lib.rs
[feature-gates]: ./feature-gates.md


---

# Lang items

The compiler has certain pluggable operations; that is, functionality that isn't hard-coded into
the language, but is implemented in libraries, with a special marker to tell the compiler it
exists. The marker is the attribute `#[lang = "..."]`, and there are various different values of
`...`, i.e. various different 'lang items'.

Many such lang items can be implemented only in one sensible way, such as `add` (`trait
core::ops::Add`) or `future_trait` (`trait core::future::Future`). Others can be overridden to
achieve some specific goals; for example, you can control your binary's entrypoint.

Features provided by lang items include:

- overloadable operators via traits: the traits corresponding to the
  `==`, `<`, dereference (`*`), `+`, etc. operators are all
  marked with lang items; those specific four are `eq`, `ord`,
  `deref`, and `add` respectively.
- panicking and stack unwinding; the `eh_personality`, `panic` and
  `panic_bounds_checks` lang items.
- the traits in `std::marker` used to indicate properties of types used by the compiler;
  lang items `send`, `sync` and `copy`.
- the special marker types used for variance indicators found in
  `core::marker`; lang item `phantom_data`.

Lang items are loaded lazily by the compiler; e.g. if one never uses `Box`
then there is no need to define functions for `exchange_malloc` and
`box_free`. `rustc` will emit an error when an item is needed but not found
in the current crate or any that it depends on.

Most lang items are defined by the `core` library, but if you're trying to build an
executable with `#![no_std]`, you'll still need to define a few lang items that are
usually provided by `std`.

## Retrieving a language item

You can retrieve lang items by calling [`tcx.lang_items()`].

Here's a small example of retrieving the `trait Sized {}` language item:

```rust
// Note that in case of `#![no_core]`, the trait is not available.
if let Some(sized_trait_def_id) = tcx.lang_items().sized_trait() {
    // do something with `sized_trait_def_id`
}
```

Note that `sized_trait()` returns an `Option`, not the `DefId` itself.
That's because language items are defined in the standard library, so if someone compiles with
`#![no_core]` (or for some lang items, `#![no_std]`), the lang item may not be present.
You can either:

- Give a hard error if the lang item is necessary to continue (don't panic, since this can happen in
  user code).
- Proceed with limited functionality, by just omitting whatever you were going to do with the
  `DefId`.

[`tcx.lang_items()`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.lang_items

## List of all language items

You can find language items in the following places:
- An exhaustive reference in the compiler documentation: [`rustc_hir::LangItem`]
- An auto-generated list with source locations by using ripgrep: `rg '#\[.*lang =' library/`

Note that language items are explicitly unstable and may change in any new release.

[`rustc_hir::LangItem`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/lang_items/enum.LangItem.html
