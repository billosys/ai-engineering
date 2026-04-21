# Rustdoc internals

This page describes [`rustdoc`]'s passes and modes.
For an overview of `rustdoc`, see the ["Rustdoc overview" chapter](./rustdoc.md).

[`rustdoc`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc

## From crate to clean

In [`core.rs`] are two central items: the [`rustdoc::core::DocContext`]
`struct`, and the [`rustdoc::core::run_global_ctxt`] function.
The latter is where `rustdoc` calls out to `rustc` to compile a crate to the point where
`rustdoc` can take over.
The former is a state container used when crawling through a crate to gather its documentation.

The main process of crate crawling is done in [`clean/mod.rs`] through several
functions with names that start with `clean_`.
Each function accepts an `hir`
or `ty` data structure, and outputs a `clean` structure used by `rustdoc`.
For example, [this function for converting lifetimes]:

```rust,ignore
fn clean_lifetime<'tcx>(lifetime: &hir::Lifetime, cx: &mut DocContext<'tcx>) -> Lifetime {
    if let Some(
        rbv::ResolvedArg::EarlyBound(did)
        | rbv::ResolvedArg::LateBound(_, _, did)
        | rbv::ResolvedArg::Free(_, did),
    ) = cx.tcx.named_bound_var(lifetime.hir_id)
        && let Some(lt) = cx.args.get(&did).and_then(|arg| arg.as_lt())
    {
        return lt.clone();
    }
    Lifetime(lifetime.ident.name)
}
```

Also, `clean/mod.rs` defines the types for the "cleaned" [Abstract Syntax Tree
(`AST`)][ast] used later to render documentation pages.
Each usually accompanies a
`clean_*` function that takes some [`AST`][ast] or [High-Level Intermediate
Representation (`HIR`)][hir] type from `rustc` and converts it into the appropriate "cleaned" type.
"Big" items like modules or associated items may
have some extra processing in its `clean` function, but for the most part these
`impl`s are straightforward conversions.
The "entry point" to this module is
[`clean::utils::krate`][ck0], which is called by [`run_global_ctxt`].

The first step in [`clean::utils::krate`][ck1] is to invoke
[`visit_ast::RustdocVisitor`] to process the module tree into an intermediate [`visit_ast::Module`].
This is the step that actually crawls the
[`rustc_middle::hir::Crate`], normalizing various aspects of name resolution, such as:

  * handling `#[doc(inline)]` and `#[doc(no_inline)]`
  * handling import globs and cycles, so there are no duplicates or infinite
    directory trees
  * inlining public `use` exports of private items, or showing a "Reexport"
    line in the module page
  * inlining items with `#[doc(hidden)]` if the base item is hidden but the
  * showing `#[macro_export]`-ed macros at the crate root, regardless of whether
    they're defined as a reexport or not

After this step, `clean::krate` invokes [`clean_doc_module`], which actually
converts the `HIR` items to the cleaned [`AST`][ast].
This is also the step where cross-crate inlining is performed,
which requires converting `rustc_middle` data structures into the cleaned [`AST`][ast].

The other major thing that happens in `clean/mod.rs` is the collection of doc
comments and `#[doc=""]` attributes into a separate field of the [`Attributes`]
`struct`, present on anything that gets hand-written documentation.
This makes it easier to collect this documentation later in the process.

The primary output of this process is a [`clean::types::Crate`] with a tree of [`Item`]s
which describe the publicly-documentable items in the target crate.

[`Attributes`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/clean/types/struct.Attributes.html
[`clean_doc_module`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/clean/fn.clean_doc_module.html
[`clean::types::Crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/clean/types/struct.Crate.html
[`clean/mod.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/clean/mod.rs
[`core.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/core.rs
[`Item`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/clean/types/struct.Item.html
[`run_global_ctxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/core/fn.run_global_ctxt.html
[`rustc_middle::hir::Crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/hir/struct.Crate.html
[`rustdoc::core::DocContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/core/struct.DocContext.html
[`rustdoc::core::run_global_ctxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/core/fn.run_global_ctxt.html
[`visit_ast::Module`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/visit_ast/struct.Module.html
[`visit_ast::RustdocVisitor`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/visit_ast/struct.RustdocVisitor.html
[ast]: ./ast-validation.md
[ck0]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/clean/utils/fn.krate.html#
[ck1]: https://doc.rust-lang.org/nightly/nightly-rustc/src/rustdoc/clean/utils.rs.html#31-77
[hir]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/index.html
[this function for converting lifetimes]: https://doc.rust-lang.org/nightly/nightly-rustc/src/rustdoc/clean/mod.rs.html#256-267

### Passes Anything But a Gas Station (or: [Hot Potato](https://www.youtube.com/watch?v=WNFBIt5HxdY))

Before moving on to the next major step, a few important "passes" occur over
the cleaned [`AST`][ast].
Several of these passes are `lint`s and reports, but some of them mutate or generate new items.

These are all implemented in the [`librustdoc/passes`] directory, one file per pass.
By default, all of these passes are run on a crate, but the ones
regarding dropping private/hidden items can be bypassed by passing
`--document-private-items` to `rustdoc`.
Note that, unlike the previous set of [`AST`][ast]
transformations, the passes are run on the _cleaned_ crate.

Here is the list of passes as of <!-- date-check --> March 2023:

- `calculate-doc-coverage` calculates information used for the `--show-coverage`
  flag.

- `check-doc-test-visibility` runs `doctest` visibility–related `lint`s.
  This pass runs before `strip-private`,
  which is why it needs to be separate from `run-lints`.

- `collect-intra-doc-links` resolves [intra-doc links](https://doc.rust-lang.org/nightly/rustdoc/write-documentation/linking-to-items-by-name.html).

- `collect-trait-impls` collects `trait` `impl`s for each item in the crate.
  For example, if we define a `struct` that implements a `trait`,
  this pass will note that the `struct` implements that `trait`.

- `propagate-doc-cfg` propagates `#[doc(cfg(...))]` to child items.

- `run-lints` runs some of `rustdoc`'s `lint`s, defined in `passes/lint`.
  This is the last pass to run.

  - `bare_urls` detects links that are not linkified, e.g., in Markdown such as
    `Go to https://example.com/.` It suggests wrapping the link with angle brackets:
    `Go to <https://example.com/>.` to linkify it.
    This is the code behind the <!-- date-check: may 2022 --> `rustdoc::bare_urls` `lint`.

  - `check_code_block_syntax` validates syntax inside Rust code blocks
    (<code>```rust</code>)

  - `html_tags` detects invalid `HTML` (like an unclosed `<span>`)
    in doc comments.

- `strip-hidden` and `strip-private` strip all `doc(hidden)` and private items
  from the output.
  `strip-private` implies `strip-priv-imports`.
  Basically, the goal is to remove items that are not relevant for public documentation.
  This pass is skipped when `--document-hidden-items` is passed.

- `strip-priv-imports` strips all private import statements (`use`, `extern
  crate`) from a crate.
  This is necessary because `rustdoc` will handle *public*
  imports by either inlining the item's documentation to the module or creating
  a "Reexports" section with the import in it.
  The pass ensures that all of these imports are actually relevant to documentation.
  It is technically only run when `--document-private-items` is passed, but `strip-private`
  accomplishes the same thing.

- `strip-private` strips all private items from a crate which cannot be seen
  externally.
  This pass is skipped when `--document-private-items` is passed.

There is also a [`stripper`] module in `librustdoc/passes`, but it is a
collection of utility functions for the `strip-*` passes and is not a pass itself.

[`librustdoc/passes`]: https://github.com/rust-lang/rust/tree/HEAD/src/librustdoc/passes
[`stripper`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/passes/stripper/index.html

## From clean to HTML

This is where the "second phase" in `rustdoc` begins.
This phase primarily lives
in the [`librustdoc/formats`] and [`librustdoc/html`] folders, and it all starts with
[`formats::renderer::run_format`].
This code is responsible for setting up a type that
`impl FormatRenderer`, which for `HTML` is [`Context`].

This structure contains methods that get called by `run_format` to drive the
doc rendering, which includes:

* `init` generates `static.files`, as well as search index and `src/`
* `item` generates the item `HTML` files themselves
* `after_krate` generates other global resources like `all.html`

In `item`, the "page rendering" occurs, via a mixture of [Askama] templates
and manual `write!()` calls, starting in [`html/layout.rs`].
The parts that have not been converted to templates occur within a series of `std::fmt::Display`
implementations and functions that pass around a `&mut std::fmt::Formatter`.

The parts that actually generate `HTML` from the items and documentation start
with [`print_item`] defined in [`html/render/print_item.rs`], which switches out
to one of several `item_*` functions based on kind of `Item` being rendered.

Depending on what kind of rendering code you're looking for, you'll probably
find it either in [`html/render/mod.rs`] for major items like "what sections
should I print for a `struct` page" or [`html/format.rs`] for smaller component
pieces like "how should I print a where clause as part of some other item".

Whenever `rustdoc` comes across an item that should print hand-written
documentation alongside, it calls out to [`html/markdown.rs`] which interfaces
with the Markdown parser.
This is exposed as a series of types that wrap a
string of Markdown, and implement `fmt::Display` to emit `HTML` text.
It takes special care to enable certain features like footnotes and tables and add
syntax highlighting to Rust code blocks (via `html/highlight.rs`) before
running the Markdown parser.
There's also a function [`find_codes`] which is
called by `find_testable_codes` that specifically scans for Rust code blocks so
the test-runner code can find all the `doctest`s in the crate.

[`find_codes`]: https://doc.rust-lang.org/nightly/nightly-rustc/src/rustdoc/html/markdown.rs.html#749-818
[`formats::renderer::run_format`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/formats/renderer/fn.run_format.html
[`html/format.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/format.rs
[`html/layout.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/layout.rs
[`html/markdown.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/markdown.rs
[`html/render/mod.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/render/mod.rs
[`html/render/print_item.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/render/print_item.rs
[`librustdoc/formats`]: https://github.com/rust-lang/rust/tree/HEAD/src/librustdoc/formats
[`librustdoc/html`]: https://github.com/rust-lang/rust/tree/HEAD/src/librustdoc/html
[`print_item`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/html/render/print_item/fn.print_item.html
[Askama]: https://docs.rs/askama/latest/askama/

### From Soup to Nuts (or: ["An Unbroken Thread Stretches From Those First `Cell`s To Us"][video])

[video]: https://www.youtube.com/watch?v=hOLAGYmUQV0

It's important to note that `rustdoc` can ask the compiler for type information
directly, even during `HTML` generation.
This [didn't used to be the case], and
a lot of `rustdoc`'s architecture was designed around not doing that, but a
`TyCtxt` is now passed to `formats::renderer::run_format`, which is used to
run generation for both `HTML` and the (unstable as of <!-- date-check --> Nov 2025) JSON format.

This change has allowed other changes to remove data from the "clean" [`AST`][ast]
that can be easily derived from `TyCtxt` queries, and we'll usually accept
PRs that remove fields from "clean" (it's been soft-deprecated), but this
is complicated from two other constraints that `rustdoc` runs under:

* Docs can be generated for crates that don't actually pass type checking.
  This is used for generating docs that cover mutually-exclusive platform
  configurations, such as `libstd` having a single package of docs that
  cover all supported operating systems.
  This means `rustdoc` has to be able to generate docs from `HIR`.
* Docs can inline across crates.
  Since crate metadata doesn't contain `HIR`,
  it must be possible to generate inlined docs from the `rustc_middle` data.

The "clean" [`AST`][ast] acts as a common output format for both input formats.
There is also some data in clean that doesn't correspond directly to `HIR`, such as
synthetic `impl`s for auto traits and blanket `impl`s generated by the `collect-trait-impls` pass.

Some additional data is stored in `html::render::context::{Context, SharedContext}`.
These two types serve as
ways to segregate `rustdoc`'s data for an eventual future with multithreaded doc
generation, as well as just keeping things organized:

* [`Context`] stores data used for generating the current page, such as its
  path, a list of `HTML` IDs that have been used (to avoid duplicate `id=""`),
  and the pointer to `SharedContext`.
* [`SharedContext`] stores data that does not vary by page, such as the `tcx`
  pointer, and a list of all types.

[`Context`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/html/render/context/struct.Context.html
[didn't used to be the case]: https://github.com/rust-lang/rust/pull/80090
[`SharedContext`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/html/render/context/struct.SharedContext.html

## Other tricks up its sleeve

All this describes the process for generating `HTML` documentation from a Rust
crate, but there are couple other major modes that `rustdoc` runs in.
It can also be run on a standalone Markdown file, or it can run `doctest`s on Rust code or
standalone Markdown files.
For the former, it shortcuts straight to
`html/markdown.rs`, optionally including a mode which inserts a Table of
Contents to the output `HTML`.

For the latter, `rustdoc` runs a similar partial-compilation to get relevant
documentation in `test.rs`, but instead of going through the full clean and
render process, it runs a much simpler crate walk to grab *just* the hand-written documentation.
Combined with the aforementioned
"`find_testable_code`" in `html/markdown.rs`, it builds up a collection of
tests to run before handing them off to the test runner.
One notable location in `test.rs` is the function `make_test`, which is where hand-written
`doctest`s get transformed into something that can be executed.

Some extra reading about `make_test` can be found
[here](https://quietmisdreavus.net/code/2018/02/23/how-the-doctests-get-made/).

## Testing locally

Some features of the generated `HTML` documentation might require local
storage to be used across pages, which doesn't work well without an `HTTP` server.
To test these features locally, you can run a local `HTTP` server, like this:

```console
$ ./x doc library
# The documentation has been generated into `build/[YOUR ARCH]/doc`.
$ python3 -m http.server -d build/[YOUR ARCH]/doc
```

Now you can browse your documentation just like you would if it was hosted on the internet.
For example, the url for `std` will be `rust/std/`.

## See also

- The [`rustdoc` api docs]
- [An overview of `rustdoc`](./rustdoc.md)
- [The rustdoc user guide]

[`rustdoc` api docs]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc/
[The rustdoc user guide]: https://doc.rust-lang.org/nightly/rustdoc/


---

# Rustdoc search

Rustdoc Search is two programs: `search_index.rs`
and `search.js`. The first generates a nasty JSON
file with a full list of items and function signatures
in the crates in the doc bundle, and the second reads
it, turns it into some in-memory structures, and
scans them linearly to search.

## Search index format

`search.js` calls this Raw, because it turns it into
a more normal object tree after loading it.
For space savings, it's also written without newlines or spaces.

```json
[
    [ "crate_name", {
        // name
        "n": ["function_name", "Data"],
        // type
        "t": "HF",
        // parent module
        "q": [[0, "crate_name"]],
        // parent type
        "i": [2, 0],
        // type dictionary
        "p": [[1, "i32"], [1, "str"], [5, "Data", 0]],
        // function signature
        "f": "{{gb}{d}}`", // [[3, 1], [2]]
        // impl disambiguator
        "b": [],
        // deprecated flag
        "c": "OjAAAAAAAAA=", // empty bitmap
        // empty description flag
        "e": "OjAAAAAAAAA=", // empty bitmap
        // aliases
        "a": [["get_name", 0]],
        // description shards
        "D": "g", // 3
        // inlined re-exports
        "r": [],
    }]
]
```

[`src/librustdoc/html/static/js/rustdoc.d.ts`]
defines an actual schema in a TypeScript `type`.

| Key | Name                 | Description  |
| --- | -------------------- | ------------ |
| `n` | Names                | Item names   |
| `t` | Item Type            | One-char item type code |
| `q` | Parent module        | `Map<index, path>` |
| `i` | Parent type          | list of indexes |
| `f` | Function signature   | [encoded](#i-f-and-p) |
| `b` | Impl disambiguator   | `Map<index, string>` |
| `c` | Deprecation flag     | [roaring bitmap](#roaring-bitmaps) |
| `e` | Description is empty | [roaring bitmap](#roaring-bitmaps) |
| `p` | Type dictionary      | `[[item type, path]]` |
| `a` | Alias                | `Map<string, index>` |
| `D` | description shards   | [encoded](#how-descriptions-are-stored) |

The above index defines a crate called `crate_name`
with a free function called `function_name` and a struct called `Data`,
with the type signature `Data, i32 -> str`,
and an alias, `get_name`, that equivalently refers to `function_name`.

[`src/librustdoc/html/static/js/rustdoc.d.ts`]: https://github.com/rust-lang/rust/blob/2f92f050e83bf3312ce4ba73c31fe843ad3cbc60/src/librustdoc/html/static/js/rustdoc.d.ts#L344-L390

The search index needs to fit the needs of the `rustdoc` compiler,
the `search.js` frontend,
and also be compact and fast to decode.
It makes a lot of compromises:

* The `rustdoc` compiler runs on one crate at a time,
  so each crate has an essentially separate search index.
  It [merges] them by having each crate on one line
  and looking at the first quoted string.
* Names in the search index are given
  in their original case and with underscores.
  When the search index is loaded,
  `search.js` stores the original names for display,
  but also folds them to lowercase and strips underscores for search.
  You'll see them called `normalized`.
* The `f` array stores types as offsets into the `p` array.
  These types might actually be from another crate,
  so `search.js` has to turn the numbers into names and then
  back into numbers to deduplicate them if multiple crates in the
  same index mention the same types.
* It's a JSON file, but not designed to be human-readable.
  Browsers already include an optimized JSON decoder,
  so this saves on `search.js` code and performs better for small crates,
  but instead of using objects like normal JSON formats do,
  it tries to put data of the same type next to each other
  so that the sliding window used by [DEFLATE] can find redundancies.
  Where `search.js` does its own compression,
  it's designed to save memory when the file is finally loaded,
  not just size on disk or network transfer.

[merges]: https://github.com/rust-lang/rust/blob/79b710c13968a1a48d94431d024d2b1677940866/src/librustdoc/html/render/write_shared.rs#L151-L164
[DEFLATE]: https://en.wikipedia.org/wiki/Deflate

### Parallel arrays and indexed maps

Abstractly, Rustdoc Search data is a table, stored in column-major form.
Most data in the index represents a set of parallel arrays
(the "columns") which refer to the same data if they're at the same position.

For example,
the above search index can be turned into this table:

|   | n | t | [d] | q | i | f | b | c |
|---|---|---|-----|---|---|---|---|---|
| 0 | `crate_name`    | `D` | Documentation | NULL | 0 | NULL | NULL | 0 |
| 1 | `function_name` | `H` | This function gets the name of an integer with Data | `crate_name` | 2 | `{{gb}{d}}` | NULL | 0 |
| 2 | `Data` | `F` | The data struct | `crate_name` | 0 | `` ` `` | NULL | 0 |

[d]: #how-descriptions-are-stored

The crate row is implied in most columns, since its type is known (it's a crate),
it can't have a parent (crates form the root of the module tree),
its name is specified as the map key,
and function-specific data like the impl disambiguator can't apply either.
However, it can still have a description and it can still be deprecated.
The crate, therefore, has a primary key of `0`.

The above code doesn't use `c`, which holds deprecated indices,
or `b`, which maps indices to strings.
If `crate_name::function_name` used both, it might look like this.

```json
        "b": [[0, "impl-Foo-for-Bar"]],
        "c": "OjAAAAEAAAAAAAIAEAAAABUAbgZYCQ==",
```

This attaches a disambiguator to index 1 and marks it deprecated.

The advantage of this layout is that these APIs often have implicit structure
that DEFLATE can take advantage of,
but that rustdoc can't assume.
Like how names are usually CamelCase or snake_case,
but descriptions aren't.
It also makes it easier to use a sparse data for things like boolean flags.

`q` is a Map from *the first applicable* ID to a parent module path.
This is a weird trick, but it makes more sense in pseudo-code:

```rust
let mut parent_module = "";
for (i, entry) in search_index.iter().enumerate() {
    if q.contains(i) {
        parent_module = q.get(i);
    }
    // ... do other stuff with `entry` ...
}
```

This is valid because everything has a parent module
(even if it's just the crate itself),
and is easy to assemble because the rustdoc generator sorts by path
before serializing.
Doing this allows rustdoc to not only make the search index smaller,
but reuse the same string representing the parent path across multiple in-memory items.

### Representing sparse columns

#### VLQ Hex

This format is, as far as I know, used nowhere other than rustdoc.
It follows this grammar:

```ebnf
VLQHex = { VHItem | VHBackref }
VHItem = VHNumber | ( '{', {VHItem}, '}' )
VHNumber = { '@' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' }, ( '`' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k ' | 'l' | 'm' | 'n' | 'o' )
VHBackref = ( '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | ':' | ';' | '<' | '=' | '>' | '?' )
```

A VHNumber is a variable-length, self-terminating base16 number
(terminated because the last hexit is lowercase while all others are uppercase).
The sign bit is represented using [zig-zag encoding].

This alphabet is chosen because the characters can be turned into hexits by
masking off the last four bits of the ASCII encoding.

A major feature of this encoding, as with all of the "compression" done in rustdoc,
is that it can remain in its compressed format *even in memory at runtime*.
This is why `HBackref` is only used at the top level,
and why we don't just use [Flate] for everything: the decoder in search.js
will reuse the entire decoded object whenever a backref is seen,
saving decode work and memory.

[zig-zag encoding]: https://en.wikipedia.org/wiki/Variable-length_quantity#Zigzag_encoding
[Flate]: https://en.wikipedia.org/wiki/Deflate

#### Roaring Bitmaps

Flag-style data, such as deprecation and empty descriptions,
are stored using the [standard Roaring Bitmap serialization format with runs].
The data is then base64 encoded when writing it.

As a brief overview: a roaring bitmap is a chunked array of bits,
described in [this paper].
A chunk can either be a list of integers, a bitfield, or a list of runs.
In any case, the search engine has to base64 decode it,
and read the chunk index itself,
but the payload data stays as-is.

All roaring bitmaps in rustdoc currently store a flag for each item index.
The crate is item 0, all others start at 1.

[standard Roaring Bitmap serialization format with runs]: https://github.com/RoaringBitmap/RoaringFormatSpec
[this paper]: https://arxiv.org/pdf/1603.06549.pdf

### How descriptions are stored

The largest amount of data,
and the main thing Rustdoc Search deals with that isn't
actually used for searching, is descriptions.
In a SERP table, this is what appears on the rightmost column.

> | item type | item path             | ***description*** (this part)                       |
> | --------- | --------------------- | --------------------------------------------------- |
> | function  | my_crate::my_function | This function gets the name of an integer with Data |

When someone runs a search in rustdoc for the first time, their browser will
work through a "sandwich workload" of three steps:

1. Download the search-index.js and search.js files (a network bottleneck).
2. Perform the actual search (a CPU and memory bandwidth bottleneck).
3. Download the description data (another network bottleneck).

Reducing the amount of data downloaded here will almost always increase latency,
by delaying the decision of what to download behind other work and/or adding
data dependencies where something can't be downloaded without first downloading
something else. In this case, we can't start downloading descriptions until
after the search is done, because that's what allows it to decide *which*
descriptions to download (it needs to sort the results then truncate to 200).

To do this, two columns are stored in the search index, building on both
Roaring Bitmaps and on VLQ Hex.

* `e` is an index of **e**mpty descriptions. It's a [roaring bitmap] of
  each item (the crate itself is item 0, the rest start at 1).
* `D` is a shard list, stored in [VLQ hex] as flat list of integers.
  Each integer gives you the number of descriptions in the shard.
  As the decoder walks the index, it checks if the description is empty.
  if it's not, then it's in the "current" shard. When all items are
  exhausted, it goes on to the next shard.

Inside each shard is a newline-delimited list of descriptions,
wrapped in a JSONP-style function call.

[roaring bitmap]: #roaring-bitmaps
[VLQ hex]: #vlq-hex

### `i`, `f`, and `p`

`i` and `f` both index into `p`, the array of parent items.

`i` is just a one-indexed number
(not zero-indexed because `0` is used for items that have no parent item).
It's different from `q` because `q` represents the parent *module or crate*,
which everything has,
while `i`/`q` are used for *type and trait-associated items* like methods.

`f`, the function signatures, use a [VLQ hex] tree.
A number is either a one-indexed reference into `p`,
a negative number representing a generic,
or zero for null.

(the internal object representation also uses negative numbers,
even after decoding,
to represent generics).

For example, `{{gb}{d}}` is equivalent to the json `[[3, 1], [2]]`.
Because of zigzag encoding, `` ` `` is +0, `a` is -0 (which is not used),
`b` is +1, and `c` is -1.

## Searching by name

Searching by name works by looping through the search index
and running these functions on each:

* [`editDistance`] is always used to determine a match
  (unless quotes are specified, which would use simple equality instead).
  It computes the number of swaps, inserts, and removes needed to turn
  the query name into the entry name.
  For example, `foo` has zero distance from itself,
  but a distance of 1 from `ofo` (one swap) and `foob` (one insert).
  It is checked against an heuristic threshold, and then,
  if it is within that threshold, the distance is stored for ranking.
* [`String.prototype.indexOf`] is always used to determine a match.
  If it returns anything other than -1, the result is added,
  even if `editDistance` exceeds its threshold,
  and the index is stored for ranking.
* [`checkPath`] is used if, and only if, a parent path is specified
  in the query. For example, `vec` has no parent path, but `vec::vec` does.
  Within checkPath, editDistance and indexOf are used,
  and the path query has its own heuristic threshold, too.
  If it's not within the threshold, the entry is rejected,
  even if the first two pass.
  If it's within the threshold, the path distance is stored
  for ranking.
* [`checkType`] is used only if there's a type filter,
  like the struct in `struct:vec`. If it fails,
  the entry is rejected.

If all four criteria pass
(plus the crate filter, which isn't technically part of the query),
the results are sorted by [`sortResults`].

[`editDistance`]: https://github.com/rust-lang/rust/blob/79b710c13968a1a48d94431d024d2b1677940866/src/librustdoc/html/static/js/search.js#L137
[`String.prototype.indexOf`]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf
[`checkPath`]: https://github.com/rust-lang/rust/blob/79b710c13968a1a48d94431d024d2b1677940866/src/librustdoc/html/static/js/search.js#L1814
[`checkType`]: https://github.com/rust-lang/rust/blob/79b710c13968a1a48d94431d024d2b1677940866/src/librustdoc/html/static/js/search.js#L1787
[`sortResults`]: https://github.com/rust-lang/rust/blob/79b710c13968a1a48d94431d024d2b1677940866/src/librustdoc/html/static/js/search.js#L1229

## Searching by type

Searching by type can be divided into two phases,
and the second phase has two sub-phases.

* Turn names in the query into numbers.
* Loop over each entry in the search index:
   * Quick rejection using a bloom filter.
   * Slow rejection using a recursive type unification algorithm.

In the names->numbers phase, if the query has only one name in it,
the editDistance function is used to find a near match if the exact match fails,
but if there's multiple items in the query,
non-matching items are treated as generics instead.
This means `hahsmap` will match hashmap on its own, but `hahsmap, u32`
is going to match the same things `T, u32` matches
(though rustdoc will detect this particular problem and warn about it).

Then, when actually looping over each item,
the bloom filter will probably reject entries that don't have every
type mentioned in the query.
For example, the bloom query allows a query of `i32 -> u32` to match
a function with the type `i32, u32 -> bool`,
but unification will reject it later.

The unification filter ensures that:

* Bag semantics are respected. If you query says `i32, i32`,
  then the function has to mention *two* i32s, not just one.
* Nesting semantics are respected. If your query says `vec<option>`,
  then `vec<option<i32>>` is fine, but `option<vec<i32>>` *is not* a match.
* The division between return type and parameter is respected.
  `i32 -> u32` and `u32 -> i32` are completely different.

The bloom filter checks none of these things,
and, on top of that, can have false positives.
But it's fast and uses very little memory, so the bloom filter helps.

## Re-exports

[Re-export inlining] allows the same item to be found by multiple names.
Search supports this by giving the same item multiple entries and tracking a canonical path
for any items where that differs from the given path.

For example, this sample index has a single struct exported from two paths:

```json
[
    [ "crate_name", {
        "doc": "Documentation",
        "n": ["Data", "Data"],
        "t": "FF",
        "d": ["The data struct", "The data struct"],
        "q": [[0, "crate_name"], [1, "crate_name::submodule"]],
        "i": [0, 0],
        "p": [],
        "f": "``",
        "b": [],
        "c": [],
        "a": [],
        "r": [[0, 1]],
    }]
]
```

The important part of this example is the `r` array,
which indicates that path entry 1 in the `q` array is
the canonical path for item 0.
That is, `crate_name::Data` has a canonical path of `crate_name::submodule::Data`.

This might sound like a strange design, since it has the duplicate data.
It's done that way because inlining can happen across crates,
which are compiled separately and might not all be present in the docs.

```json
[
  [ "crate_name", ... ],
  [ "crate_name_2", { "q": [[0, "crate_name::submodule"], [5, "core::option"]], ... }]
]
```

In the above example, a canonical path actually comes from a dependency,
and another one comes from an inlined standard library item:
the canonical path isn't even in the index!
The canonical path might also be private.
In either case, it's never shown to the user, and is only used for deduplication.

Associated types, like methods, store them differently.
These types are connected with an entry in `p` (their "parent")
and each one has an optional third tuple element:

    "p": [[5, "Data", 0, 1]]

That's:

- 5: It's a struct
- "Data": Its name
- 0: Its display path, "crate_name"
- 1: Its canonical path, "crate_name::submodule"

In both cases, the canonical path might not be public at all,
or it might be from another crate that isn't in the docs,
so it's never shown to the user, but is used for deduplication.

[Re-export inlining]: https://doc.rust-lang.org/nightly/rustdoc/write-documentation/re-exports.html

## Testing the search engine

While the generated UI is tested using `rustdoc-gui` tests, the
primary way the search engine is tested is the `rustdoc-js` and
`rustdoc-js-std` tests. They run in NodeJS.

A `rustdoc-js` test has a `.rs` and `.js` file, with the same name.
The `.rs` file specifies the hypothetical library crate to run
the searches on (make sure you mark anything you need to find as `pub`).
The `.js` file specifies the actual searches.
The `rustdoc-js-std` tests are the same, but don't require an `.rs`
file, since they use the standard library.

The `.js` file is like a module (except the loader takes care of
`exports` for you). It uses these variables:

|      Name      |              Type              | Description
| -------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------
| `FILTER_CRATE` | `string`                       | Only include results from the given crate. In the GUI, this is the "Results in <kbd>crate</kbd>" drop-down menu.
| `EXPECTED`     | `[ResultsTable]\|ResultsTable` | List of tests to run, specifying what the hypothetical user types into the search box and sees in the tabs
| `PARSED`       | `[ParsedQuery]\|ParsedQuery`   | List of parser tests to run, without running an actual search

`FILTER_CRATE` can be left out (equivalent to searching "all crates"), but you
have to specify `EXPECTED` or `PARSED`.



By default, the test fails if any of the results specified in the test case are
not found after running the search, or if the results found after running the
search don't appear in the same order that they do in the test.
The actual search results may, however, include results that aren't in the test.
To override this, specify any of the following magic comments.
Put them on their own line, without indenting.

* `// exact-check`: If search results appear that aren't part of the test case,
  then fail.
* `// ignore-order`: Allow search results to appear in any order.
* `// should-fail`: Used to write negative tests.

Standard library tests usually shouldn't specify `// exact-check`, since we
want the libs team to be able to add new items without causing unrelated
tests to fail, but standalone tests will use it more often.

The `ResultsTable` and `ParsedQuery` types are specified in
[`rustdoc.d.ts`](https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/static/js/rustdoc.d.ts).

For example, imagine we needed to fix a bug where a function named
`constructor` couldn't be found. To do this, write two files:

```rust
// tests/rustdoc-js/constructor_search.rs
// The test case needs to find this result.
pub fn constructor(_input: &str) -> i32 { 1 }
```

```js
// tests/rustdoc-js/constructor_search.js
// exact-check
// Since this test runs against its own crate,
// new items should not appear in the search results.
const EXPECTED = [
  // This first test targets name-based search.
  {
    query: "constructor",
    others: [
      { path: "constructor_search", name: "constructor" },
    ],
    in_args: [],
    returned: [],
  },
  // This test targets the second tab.
  {
    query: "str",
    others: [],
    in_args: [
      { path: "constructor_search", name: "constructor" },
    ],
    returned: [],
  },
  // This test targets the third tab.
  {
    query: "i32",
    others: [],
    in_args: [],
    returned: [
      { path: "constructor_search", name: "constructor" },
    ],
  },
  // This test targets advanced type-driven search.
  {
    query: "str -> i32",
    others: [
      { path: "constructor_search", name: "constructor" },
    ],
    in_args: [],
    returned: [],
  },
]
```

If the [`//@ revisions`] directive is used, the JS file will
have access to a variable called `REVISION`.

```js
const EXPECTED = [
  // This first test targets name-based search.
  {
    query: "constructor",
    others: REVISION === "has_constructor" ?
      [
        { path: "constructor_search", name: "constructor" },
      ] :
      [],
    in_args: [],
    returned: [],
  },
];
```

[`//@ revisions`]: ../tests/compiletest.md#revisions


---

# The `rustdoc-html` test suite

This page is about the test suite named `rustdoc-html` used to test the HTML output of `rustdoc`.
For other rustdoc-specific test suites, see [Rustdoc test suites].

Each test file in this test suite is simply a Rust source file `file.rs` sprinkled with
so-called *directives* located inside normal Rust code comments.
These come in two flavors: *Compiletest* and *HtmlDocCk*.

To learn more about the former, read [Compiletest directives].
For the latter, continue reading.

Internally, [`compiletest`] invokes the supplementary checker script [`htmldocck.py`].

[Rustdoc test suites]: ../tests/compiletest.md#rustdoc-test-suites
[`compiletest`]: ../tests/compiletest.md
[`htmldocck.py`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/htmldocck.py

## HtmlDocCk Directives

Directives to HtmlDocCk are assertions that place constraints on the generated HTML.
They look similar to those given to `compiletest` in that they take the form of `//@` comments
but ultimately, they are completely distinct and processed by different programs.

[XPath] is used to query parts of the HTML document tree.

**Introductory example**:

```rust,ignore (illustrative)
//@ has file/type.Alias.html
//@ has - '//*[@class="rust item-decl"]//code' 'type Alias = Option<i32>;'
pub type Alias = Option<i32>;
```

Here, we check that documentation generated for crate `file` contains a page for the
public type alias `Alias` where the code block that is found at the top contains the
expected rendering of the item.
The `//*[@class="rust item-decl"]//code` is an XPath expression.

Conventionally, you place these directives directly above the thing they are meant to test.
Technically speaking however, they don't need to be as HtmlDocCk only looks for the directives.

All directives take a `PATH` argument.
To avoid repetition, `-` can be passed to it to re-use the previous `PATH` argument.
Since the path contains the name of the crate, it is conventional to add a
`#![crate_name = "foo"]` attribute to the crate root to shorten the resulting path.

All arguments take the form of shell-style (single or double) quoted strings,
with the exception of `COUNT` and the special `-` form of `PATH`.

All directives (except `files`) can be *negated* by putting a `!` in front of their name.
Before you add negated directives, please read about [their caveats](#caveats).

Similar to shell commands,
directives can extend across multiple lines if their last char is `\`.
In this case, the start of the next line should be `//`, with no `@`.

Similar to compiletest directives, besides a space you can also use a colon `:` to separate
the directive name and the arguments, however a space is preferred for HtmlDocCk directives.

Use the special string `{{channel}}` in XPaths, `PATTERN` arguments and [snapshot files](#snapshot)
if you'd like to refer to the URL `https://doc.rust-lang.org/CHANNEL` where `CHANNEL` refers to the
current release channel (e.g, `stable` or `nightly`).

Listed below are all possible directives:

[XPath]: https://en.wikipedia.org/wiki/XPath

### `has`

> Usage 1: `//@ has PATH`

Check that the file given by `PATH` exists.

> Usage 2: `//@ has PATH XPATH PATTERN`

Checks that the text of each element / attribute / text selected by `XPATH` in the
whitespace-normalized[^1] file given by `PATH` matches the
(also whitespace-normalized) string `PATTERN`.

**Tip**: If you'd like to avoid whitespace normalization and/or if you'd like to match with a regex,
use `matches` instead.

### `hasraw`

> Usage: `//@ hasraw PATH PATTERN`

Checks that the contents of the whitespace-normalized[^1] file given by `PATH`
matches the (also whitespace-normalized) string `PATTERN`.

**Tip**: If you'd like to avoid whitespace normalization and / or if you'd like to match with a
regex, use `matchesraw` instead.

### `matches`

> Usage: `//@ matches PATH XPATH PATTERN`

Checks that the text of each element / attribute / text selected by `XPATH` in the
file given by `PATH` matches the Python-flavored[^2] regex `PATTERN`.

### `matchesraw`

> Usage: `//@ matchesraw PATH PATTERN`

Checks that the contents of the file given by `PATH` matches the
Python-flavored[^2] regex `PATTERN`.

### `count`

> Usage: `//@ count PATH XPATH COUNT`

Checks that there are exactly `COUNT` matches for `XPATH` within the file given by `PATH`.

### `snapshot`

> Usage: `//@ snapshot NAME PATH XPATH`

Checks that the element / text selected by `XPATH` in the file given by `PATH` matches the
pre-recorded subtree or text (the "snapshot") in file `FILE_STEM.NAME.html` where `FILE_STEM`
is the file stem of the test file.

Pass the `--bless` option to `compiletest` to accept the current subtree/text as expected.
This will overwrite the aforementioned file (or create it if it doesn't exist).
It will automatically normalize the channel-dependent URL `https://doc.rust-lang.org/CHANNEL` to
the special string `{{channel}}`.

### `has-dir`

> Usage: `//@ has-dir PATH`

Checks for the existence of the directory given by `PATH`.

### `files`

> Usage: `//@ files PATH ENTRIES`

Checks that the directory given by `PATH` contains exactly `ENTRIES`.
`ENTRIES` is a Python-like list of strings inside a quoted string.

**Example**: `//@ files "foo/bar" '["index.html", "sidebar-items.js"]'`

[^1]: Whitespace normalization means that all spans of consecutive whitespace are replaced with a single space.
[^2]: They are Unicode aware (flag `UNICODE` is set), match case-sensitively and in single-line mode.

## Compiletest Directives (Brief)

As mentioned in the introduction, you also have access to [compiletest directives].
Most importantly, they allow you to register auxiliary crates and
to pass flags to the `rustdoc` binary under test.
It's *strongly recommended* to read that chapter if you don't know anything about them yet.

Here are some details that are relevant to this test suite specifically:

* While you can use both `//@ compile-flags` and `//@ doc-flags` to pass flags to `rustdoc`,
  prefer to user the latter to show intent.
  The former is meant for `rustc`.
* Add `//@ build-aux-docs` to the test file that has auxiliary crates to not only compile the
  auxiliaries with `rustc` but to also document them with `rustdoc`.

## Caveats

Testing for the absence of an element or a piece of text is quite fragile and not very future proof.

It's not unusual that the *shape* of the generated HTML document tree changes from time to time.
This includes for example renamings of CSS classes.

Whenever that happens, *positive* checks will either continue to match the intended element /
attribute / text (if their XPath expression is general / loose enough) and
thus continue to test the correct thing or they won't in which case they would fail thereby
forcing the author of the change to look at them.

Compare that to *negative* checks (e.g., `//@ !has PATH XPATH PATTERN`) which won't fail if their
XPath expression "no longer" matches.
The author who changed "the shape" thus won't get notified and
as a result someone else can unintentionally reintroduce `PATTERN` into the generated docs without
the original negative check failing.

**Note**: Please avoid the use of *negated* checks!

**Tip**: If you can't avoid it, please **always** pair it with an analogous positive check in the
immediate vicinity, so people changing "the shape" have a chance to notice and to update the
negated check!

## Limitations

HtmlDocCk uses the XPath implementation from the Python standard library.
This leads to several limitations:

* All `XPATH` arguments must start with `//` due to a flaw in the implementation.
* Many XPath features (functions, axies, etc.) are not supported.
* Only well-formed HTML can be parsed (hopefully rustdoc doesn't output mismatched tags).

Furthmore, compiletest [revisions] are not supported.

[revisions]: ../tests/compiletest.md#revisions
[compiletest directives]: ../tests/directives.md


---

# The `rustdoc-gui` test suite

> **FIXME**: This section is a stub. Please help us flesh it out!

This page is about the test suite named `rustdoc-gui` used to test the "GUI" of `rustdoc` (i.e., the HTML/JS/CSS as rendered in a browser).
For other rustdoc-specific test suites, see [Rustdoc test suites].

These use a NodeJS-based tool called [`browser-UI-test`] that uses [puppeteer] to run tests in a headless browser and check rendering and interactivity. For information on how to write this form of test, see [`tests/rustdoc-gui/README.md`][rustdoc-gui-readme] as well as [the description of the `.goml` format][goml-script]

[Rustdoc test suites]: ../tests/compiletest.md#rustdoc-test-suites
[`browser-UI-test`]: https://github.com/GuillaumeGomez/browser-UI-test/
[puppeteer]: https://pptr.dev/
[rustdoc-gui-readme]: https://github.com/rust-lang/rust/blob/HEAD/tests/rustdoc-gui/README.md
[goml-script]: https://github.com/GuillaumeGomez/browser-UI-test/blob/main/goml-script.md


---

# The `rustdoc-json` test suite

This page is specifically about the test suite named `rustdoc-json`, which tests rustdoc's [json output].
For other test suites used for testing rustdoc, see [§Rustdoc test suites](../tests/compiletest.md#rustdoc-test-suites).

Tests are run with compiletest, and have access to the usual set of [directives](../tests/directives.md).
Frequently used directives here are:

- [`//@ aux-build`][aux-build] to have dependencies.
- `//@ edition: 2021` (or some other edition).
- `//@ compile-flags: --document-hidden-items` to enable [document private items].

Each crate's json output is checked by 2 programs: [jsondoclint](#jsondocck) and [jsondocck](#jsondocck).

## jsondoclint

[jsondoclint] checks that all [`Id`]s exist in the `index` (or `paths`).
This makes sure there are no dangling [`Id`]s.

<!-- TODO: It does some more things too?
Also, talk about how it works
 -->

## jsondocck

[jsondocck] processes directives given in comments, to assert that the values in the output are expected.
It's a lot like [htmldocck](./rustdoc-html-test-suite.md) in that way.

It uses [JSONPath] as a query language, which takes a path, and returns a *list* of values that that path is said to match to.

### Directives

- `//@ has <path>`: Checks `<path>` exists, i.e. matches at least 1 value.
- `//@ !has <path>`: Checks `<path>` doesn't exist, i.e. matches 0 values.
- `//@ has <path> <value>`: Check `<path>` exists, and at least 1 of the matches is equal to the given `<value>`
- `//@ !has <path> <value>`: Checks `<path>` exists, but none of the matches equal the given `<value>`.
- `//@ is <path> <value>`: Check `<path>` matches exactly one value, and it's equal to the given `<value>`.
- `//@ is <path> <value> <value>...`: Check that `<path>` matches to exactly every given `<value>`.
   Ordering doesn't matter here.
- `//@ !is <path> <value>`: Check `<path>` matches exactly one value, and that value is not equal to the given `<value>`.
- `//@ count <path> <number>`: Check that `<path>` matches to `<number>` of values.
- `//@ set <name> = <path>`: Check that `<path>` matches exactly one value, and store that value to the variable called `<name>`.

These are defined in [`directive.rs`].

### Values

Values can be either JSON values, or variables.

- JSON values are JSON literals, e.g. `true`, `"string"`, `{"key": "value"}`.
  These often need to be quoted using `'`, to be processed as 1 value.
  See [§Argument splitting](#argument-splitting)
- Variables can be used to store the value in one path, and use it in later queries.
  They are set with the `//@ set <name> = <path>` directive, and accessed with `$<name>`

  ```rust
  //@ set foo = $some.path
  //@ is $.some.other.path $foo
  ```

### Argument splitting

Arguments to directives are split using the [shlex] crate, which implements POSIX shell escaping.
This is because both `<path>` and `<value>` arguments to [directives](#directives) frequently have both
whitespace and quote marks.

To use the `@ is` with a `<path>` of `$.index[?(@.docs == "foo")].some.field` and a value of `"bar"` [^why_quote], you'd write:

```rust
//@ is '$.is[?(@.docs == "foo")].some.field' '"bar"'
```

[^why_quote]: The value needs to be `"bar"` *after* shlex splitting, because we
    it needs to be a JSON string value.

[json output]: https://doc.rust-lang.org/nightly/rustdoc/unstable-features.html#json-output
[jsondocck]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/jsondocck
[jsondoclint]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/jsondoclint
[aux-build]: ../tests/compiletest.md#building-auxiliary-crates
[`Id`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustdoc_json_types/struct.Id.html
[document private items]: https://doc.rust-lang.org/nightly/rustdoc/command-line-arguments.html#--document-private-items-show-items-that-are-not-public
[`directive.rs`]: https://github.com/rust-lang/rust/blob/HEAD/src/tools/jsondocck/src/directive.rs
[shlex]: https://docs.rs/shlex/1.3.0/shlex/index.html
[JSONPath]: https://www.rfc-editor.org/rfc/rfc9535.html
