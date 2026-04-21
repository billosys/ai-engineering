# Basics for hacking on Clippy

This document explains the basics for hacking on Clippy. Besides others, this
includes how to build and test Clippy. For a more in depth description on the
codebase take a look at [Adding Lints] or [Common Tools].

[Adding Lints]: adding_lints.md
[Common Tools]: common_tools_writing_lints.md

- [Basics for hacking on Clippy](#basics-for-hacking-on-clippy)
  - [Get the Code](#get-the-code)
  - [Building and Testing](#building-and-testing)
  - [`cargo dev`](#cargo-dev)
  - [lintcheck](#lintcheck)
  - [PR](#pr)
  - [Common Abbreviations](#common-abbreviations)
  - [Install from source](#install-from-source)

## Get the Code

First, make sure you have checked out the latest version of Clippy. If this is
your first time working on Clippy, create a fork of the repository and clone it
afterwards with the following command:

```bash
git clone git@github.com:<your-username>/rust-clippy
```

If you've already cloned Clippy in the past, update it to the latest version:

```bash
# If the upstream remote has not been added yet
git remote add upstream https://github.com/rust-lang/rust-clippy
# upstream has to be the remote of the rust-lang/rust-clippy repo
git fetch upstream
# make sure that you are on the master branch
git checkout master
# rebase your master branch on the upstream master
git rebase upstream/master
# push to the master branch of your fork
git push
```

## Building and Testing

You can build and test Clippy like every other Rust project:

```bash
cargo build  # builds Clippy
cargo test   # tests Clippy
```

Since Clippy's test suite is pretty big, there are some commands that only run a
subset of Clippy's tests:

```bash
# only run UI tests
cargo uitest
# only run UI tests starting with `test_`
TESTNAME="test_" cargo uitest
# only run dogfood tests
cargo dev dogfood
```

If the output of a [UI test] differs from the expected output, you can update
the reference file with:

```bash
cargo bless
```

For example, this is necessary if you fix a typo in an error message of a lint,
or if you modify a test file to add a test case.

> _Note:_ This command may update more files than you intended. In that case
> only commit the files you wanted to update.

[UI test]: https://rustc-dev-guide.rust-lang.org/tests/adding.html#ui-test-walkthrough

## `cargo dev`

Clippy has some dev tools to make working on Clippy more convenient. These tools
can be accessed through the `cargo dev` command. Available tools are listed
below. To get more information about these commands, just call them with
`--help`.

```bash
# formats the whole Clippy codebase and all tests
cargo dev fmt
# register or update lint names/groups/...
cargo dev update_lints
# create a new lint and register it
cargo dev new_lint
# deprecate a lint and attempt to remove code relating to it
cargo dev deprecate
# automatically formatting all code before each commit
cargo dev setup git-hook
# (experimental) Setup Clippy to work with RustRover
cargo dev setup intellij
# runs the `dogfood` tests
cargo dev dogfood
```

More about [intellij] command usage and reasons.

[intellij]: https://github.com/rust-lang/rust-clippy/blob/master/CONTRIBUTING.md#rustrover

## lintcheck

`cargo lintcheck` will build and run Clippy on a fixed set of crates and
generate a log of the results.  You can `git diff` the updated log against its
previous version and see what impact your lint made on a small set of crates.
If you add a new lint, please audit the resulting warnings and make sure there
are no false positives and that the suggestions are valid.

Refer to the tools [README] for more details.

[README]: https://github.com/rust-lang/rust-clippy/blob/master/lintcheck/README.md

## PR

We follow a rustc no merge-commit policy. See
<https://rustc-dev-guide.rust-lang.org/contributing.html#opening-a-pr>.

## Common Abbreviations

| Abbreviation | Meaning                                |
|--------------|----------------------------------------|
| UB           | Undefined Behavior                     |
| FP           | False Positive                         |
| FN           | False Negative                         |
| ICE          | Internal Compiler Error                |
| AST          | Abstract Syntax Tree                   |
| MIR          | Mid-Level Intermediate Representation  |
| HIR          | High-Level Intermediate Representation |
| TCX          | Type context                           |

This is a concise list of abbreviations that can come up during Clippy
development. An extensive general list can be found in the [rustc-dev-guide
glossary][glossary]. Always feel free to ask if an abbreviation or meaning is
unclear to you.

## Install from source

If you are hacking on Clippy and want to install it from source, do the
following:

From the Clippy project root, run the following command to build the Clippy
binaries and copy them into the toolchain directory. This will create a new
toolchain called `clippy` by default, see `cargo dev setup toolchain --help`
for other options.

```terminal
cargo dev setup toolchain
```

Now you may run `cargo +clippy clippy` in any project using the new toolchain.

```terminal
cd my-project
cargo +clippy clippy
```

...or `clippy-driver`

```terminal
clippy-driver +clippy <filename>
```

If you no longer need the toolchain it can be uninstalled using `rustup`:

```terminal
rustup toolchain uninstall clippy
```

> **DO NOT** install using `cargo install --path . --force` since this will
> overwrite rustup
> [proxies](https://rust-lang.github.io/rustup/concepts/proxies.html). That is,
> `~/.cargo/bin/cargo-clippy` and `~/.cargo/bin/clippy-driver` should be hard or
> soft links to `~/.cargo/bin/rustup`. You can repair these by running `rustup
> update`.

[glossary]: https://rustc-dev-guide.rust-lang.org/appendix/glossary.html


---

# Adding a new lint

You are probably here because you want to add a new lint to Clippy. If this is
the first time you're contributing to Clippy, this document guides you through
creating an example lint from scratch.

To get started, we will create a lint that detects functions called `foo`,
because that's clearly a non-descriptive name.

- [Adding a new lint](#adding-a-new-lint)
  - [Setup](#setup)
  - [Getting Started](#getting-started)
    - [Defining Our Lint](#defining-our-lint)
      - [Standalone](#standalone)
      - [Specific Type](#specific-type)
      - [Tests Location](#tests-location)
  - [Testing](#testing)
    - [Cargo lints](#cargo-lints)
  - [Rustfix tests](#rustfix-tests)
  - [Testing manually](#testing-manually)
  - [Lint declaration](#lint-declaration)
  - [Lint registration](#lint-registration)
  - [Lint passes](#lint-passes)
  - [Emitting a lint](#emitting-a-lint)
  - [Adding the lint logic](#adding-the-lint-logic)
  - [Specifying the lint's minimum supported Rust version (MSRV)](#specifying-the-lints-minimum-supported-rust-version-msrv)
  - [Author lint](#author-lint)
  - [Print HIR lint](#print-hir-lint)
  - [Documentation](#documentation)
  - [Running rustfmt](#running-rustfmt)
  - [Debugging](#debugging)
  - [Conflicting lints](#conflicting-lints)
  - [PR Checklist](#pr-checklist)
  - [Adding configuration to a lint](#adding-configuration-to-a-lint)
  - [Cheat Sheet](#cheat-sheet)

## Setup

See the [Basics](basics.md#get-the-code) documentation.

## Getting Started

There is a bit of boilerplate code that needs to be set up when creating a new
lint. Fortunately, you can use the Clippy dev tools to handle this for you. We
are naming our new lint `foo_functions` (lints are generally written in snake
case), and we don't need type information, so it will have an early pass type
(more on this later). If you're unsure if the name you chose fits the lint,
take a look at our [lint naming guidelines][lint_naming].

## Defining Our Lint
To get started, there are two ways to define our lint.

### Standalone
Command: `cargo dev new_lint --name=foo_functions --pass=early --category=pedantic`
(category will default to nursery if not provided)

This command will create a new file: `clippy_lints/src/foo_functions.rs`, as well
as [register the lint](#lint-registration).

### Specific Type
Command: `cargo dev new_lint --name=foo_functions --type=functions --category=pedantic`

This command will create a new file: `clippy_lints/src/{type}/foo_functions.rs`.

Notice how this command has a `--type` flag instead of `--pass`. Unlike a standalone
definition, this lint won't be registered in the traditional sense. Instead, you will
call your lint from within the type's lint pass, found in `clippy_lints/src/{type}/mod.rs`.

A "type" is just the name of a directory in `clippy_lints/src`, like `functions` in
the example command. These are groupings of lints with common behaviors, so if your
lint falls into one, it would be best to add it to that type.

### Tests Location
Both commands will create a file: `tests/ui/foo_functions.rs`. For cargo lints,
two project hierarchies (fail/pass) will be created by default under `tests/ui-cargo`.

Next, we'll open up these files and add our lint!

## Testing

Let's write some tests first that we can execute while we iterate on our lint.

Clippy uses UI tests for testing. UI tests check that the output of Clippy is
exactly as expected. Each test is just a plain Rust file that contains the code
we want to check. The output of Clippy is compared against a `.stderr` file.
Note that you don't have to create this file yourself, we'll get to generating
the `.stderr` files further down.

We start by opening the test file created at `tests/ui/foo_functions.rs`.

Update the file with some examples to get started:

```rust
#![allow(unused)]
#![warn(clippy::foo_functions)]

// Impl methods
struct A;
impl A {
    pub fn fo(&self) {}
    pub fn foo(&self) {}
    //~^ foo_functions
    pub fn food(&self) {}
}

// Default trait methods
trait B {
    fn fo(&self) {}
    fn foo(&self) {}
    //~^ foo_functions
    fn food(&self) {}
}

// Plain functions
fn fo() {}
fn foo() {}
//~^ foo_functions
fn food() {}

fn main() {
    // We also don't want to lint method calls
    foo();
    let a = A;
    a.foo();
}
```

Note that we are adding comment annotations with the name of our lint to mark
lines where we expect an error. Except for very specific situations
(`//@check-pass`), at least one error marker must be present in a test file for
it to be accepted.

Once we have implemented our lint we can run `TESTNAME=foo_functions cargo
uibless` to generate the `.stderr` file. If our lint makes use of structured
suggestions then this command will also generate the corresponding `.fixed`
file.

While we are working on implementing our lint, we can keep running the UI test.
That allows us to check if the output is turning into what we want by checking the
`.stderr` file that gets updated on every test run.

Once we have implemented our lint running `TESTNAME=foo_functions cargo uitest`
should pass on its own. When we commit our lint, we need to commit the generated
 `.stderr` and if applicable `.fixed` files, too. In general, you should only
 commit files changed by `cargo bless` for the specific lint you are creating/editing.

> _Note:_ you can run multiple test files by specifying a comma separated list:
> `TESTNAME=foo_functions,test2,test3`.

### Cargo lints

For cargo lints, the process of testing differs in that we are interested in the
`Cargo.toml` manifest file. We also need a minimal crate associated with that
manifest.

If our new lint is named e.g. `foo_categories`, after running `cargo dev
new_lint --name=foo_categories --type=cargo --category=cargo` we will find by
default two new crates, each with its manifest file:

* `tests/ui-cargo/foo_categories/fail/Cargo.toml`: this file should cause the
  new lint to raise an error.
* `tests/ui-cargo/foo_categories/pass/Cargo.toml`: this file should not trigger
  the lint.

If you need more cases, you can copy one of those crates (under
`foo_categories`) and rename it.

The process of generating the `.stderr` file is the same, and prepending the
`TESTNAME` variable to `cargo uitest` works too.

## Rustfix tests

If the lint you are working on is making use of structured suggestions, the test
will create a `.fixed` file by running [rustfix] for that test.
Rustfix will apply the suggestions
from the lint to the code of the test file and compare that to the contents of a
`.fixed` file.

Use `cargo bless` to automatically generate the `.fixed` file while running
the tests.

[rustfix]: https://github.com/rust-lang/cargo/tree/master/crates/rustfix

## Testing manually

Manually testing against an example file can be useful if you have added some
`println!`s and the test suite output becomes unreadable. To try Clippy with
your local modifications, run the following from the Clippy directory:

```bash
cargo dev lint input.rs
```

To run Clippy on an existing project rather than a single file you can use

```bash
cargo dev lint /path/to/project
```

Or set up a rustup toolchain that points to the local Clippy binaries

```bash
cargo dev setup toolchain

# Then in `/path/to/project` you can run
cargo +clippy clippy
```

## Lint declaration

Let's start by opening the new file created in the `clippy_lints` crate at
`clippy_lints/src/foo_functions.rs`. That's the crate where all the lint code
is. This file has already imported some initial things we will need:

```rust
use rustc_lint::{EarlyLintPass, EarlyContext};
use rustc_session::declare_lint_pass;
use rustc_ast::ast::*;
```

The next step is to update the lint declaration. Lints are declared using the
[`declare_clippy_lint!`][declare_clippy_lint] macro, and we just need to update
the auto-generated lint declaration to have a real description, something like
this:

```rust
declare_clippy_lint! {
    /// ### What it does
    ///
    /// ### Why is this bad?
    ///
    /// ### Example
    /// ```rust
    /// // example code
    /// ```
    #[clippy::version = "1.29.0"]
    pub FOO_FUNCTIONS,
    pedantic,
    "function named `foo`, which is not a descriptive name"
}
```

* The section of lines prefixed with `///` constitutes the lint documentation
  section. This is the default documentation style and will be displayed [like
  this][example_lint_page]. To render and open this documentation locally in a
  browser, run `cargo dev serve`.
* The `#[clippy::version]` attribute will be rendered as part of the lint
  documentation. The value should be set to the current Rust version that the
  lint is developed in, it can be retrieved by running `rustc -vV` in the
  rust-clippy directory. The version is listed under *release*. (Use the version
  without the `-nightly`) suffix.
* `FOO_FUNCTIONS` is the name of our lint. Be sure to follow the [lint naming
  guidelines][lint_naming] here when naming your lint. In short, the name should
  state the thing that is being checked for and read well when used with
  `allow`/`warn`/`deny`.
* `pedantic` sets the lint level to `Allow`. The exact mapping can be found
  [here][category_level_mapping]
* The last part should be a text that explains what exactly is wrong with the
  code

The rest of this file contains an empty implementation for our lint pass, which
in this case is `EarlyLintPass` and should look like this:

```rust
// clippy_lints/src/foo_functions.rs

// .. imports and lint declaration ..

declare_lint_pass!(FooFunctions => [FOO_FUNCTIONS]);

impl EarlyLintPass for FooFunctions {}
```

[declare_clippy_lint]: https://github.com/rust-lang/rust-clippy/blob/557f6848bd5b7183f55c1e1522a326e9e1df6030/clippy_lints/src/lib.rs#L60
[example_lint_page]: https://rust-lang.github.io/rust-clippy/master/index.html#redundant_closure
[lint_naming]: https://rust-lang.github.io/rfcs/0344-conventions-galore.html#lints
[category_level_mapping]: ../index.html

## Lint registration

When using `cargo dev new_lint`, the lint is automatically registered and
nothing more has to be done.

When declaring a new lint by hand and `cargo dev update_lints` is used, the lint
pass may have to be registered manually in the `register_lints` function in
`clippy_lints/src/lib.rs`:

```rust,ignore
store.register_early_pass(|| Box::new(foo_functions::FooFunctions));
```

As one may expect, there is a corresponding `register_late_pass` method
available as well. Without a call to one of `register_early_pass` or
`register_late_pass`, the lint pass in question will not be run.

One reason that `cargo dev update_lints` does not automate this step is that
multiple lints can use the same lint pass, so registering the lint pass may
already be done when adding a new lint. Another reason that this step is not
automated is that the order that the passes are registered determines the order
the passes actually run, which in turn affects the order that any emitted lints
are output in.

## Lint passes

Writing a lint that only checks for the name of a function means that we only
have to deal with the AST and don't have to deal with the type system at all.
This is good, because it makes writing this particular lint less complicated.

We have to make this decision with every new Clippy lint. It boils down to using
either [`EarlyLintPass`][early_lint_pass] or [`LateLintPass`][late_lint_pass].

`EarlyLintPass` runs before type checking and
[HIR](https://rustc-dev-guide.rust-lang.org/hir.html) lowering, while `LateLintPass`
runs after these stages, providing access to type information. The `cargo dev new_lint` command
defaults to the recommended `LateLintPass`, but you can specify `--pass=early` if your lint
only needs AST level analysis.

Since we don't need type information for checking the function name, we used
`--pass=early` when running the new lint automation and all the imports were
added accordingly.

[early_lint_pass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.EarlyLintPass.html
[late_lint_pass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html

## Emitting a lint

With UI tests and the lint declaration in place, we can start working on the
implementation of the lint logic.

Let's start by implementing the `EarlyLintPass` for our `FooFunctions`:

```rust,ignore
impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        // TODO: Emit lint here
    }
}
```

We implement the [`check_fn`][check_fn] method from the
[`EarlyLintPass`][early_lint_pass] trait. This gives us access to various
information about the function that is currently being checked. More on that in
the next section. Let's worry about the details later and emit our lint for
*every* function definition first.

Depending on how complex we want our lint message to be, we can choose from a
variety of lint emission functions. They can all be found in
[`clippy_utils/src/diagnostics.rs`][diagnostics].

`span_lint_and_help` seems most appropriate in this case. It allows us to
provide an extra help message, and we can't really suggest a better name
automatically. This is how it looks:

```rust,ignore
impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        span_lint_and_help(
            cx,
            FOO_FUNCTIONS,
            span,
            "function named `foo`",
            None,
            "consider using a more meaningful name"
        );
    }
}
```

Running our UI test should now produce output that contains the lint message.

According to [the rustc-dev-guide], the text should be matter of fact and avoid
capitalization and periods, unless multiple sentences are needed. When code or
an identifier must appear in a message or label, it should be surrounded with
single grave accents \`.

[check_fn]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.EarlyLintPass.html#method.check_fn
[diagnostics]: https://github.com/rust-lang/rust-clippy/blob/master/clippy_utils/src/diagnostics.rs
[the rustc-dev-guide]: https://rustc-dev-guide.rust-lang.org/diagnostics.html

## Adding the lint logic

Writing the logic for your lint will most likely be different from our example,
so this section is kept rather short.

Using the [`check_fn`][check_fn] method gives us access to [`FnKind`][fn_kind]
that has the [`FnKind::Fn`] variant. It provides access to the name of the
function/method via an [`Ident`][ident].

With that we can expand our `check_fn` method to:

```rust
impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        if is_foo_fn(fn_kind) {
            span_lint_and_help(
                cx,
                FOO_FUNCTIONS,
                span,
                "function named `foo`",
                None,
                "consider using a more meaningful name"
            );
        }
    }
}
```

We separate the lint conditional from the lint emissions because it makes the
code a bit easier to read. In some cases this separation would also allow to
write some unit tests (as opposed to only UI tests) for the separate function.

In our example, `is_foo_fn` looks like:

```rust
// use statements, impl EarlyLintPass, check_fn, ..

fn is_foo_fn(fn_kind: FnKind<'_>) -> bool {
    match fn_kind {
        FnKind::Fn(_, _, Fn { ident, .. }) => {
            // check if `fn` name is `foo`
            ident.name.as_str() == "foo"
        }
        // ignore closures
        FnKind::Closure(..) => false
    }
}
```

Now we should also run the full test suite with `cargo test`. At this point
running `cargo test` should produce the expected output. Remember to run `cargo
bless` to update the `.stderr` file.

`cargo test` (as opposed to `cargo uitest`) will also ensure that our lint
implementation is not violating any Clippy lints itself.

That should be it for the lint implementation. Running `cargo test` should now
pass.

[fn_kind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/visit/enum.FnKind.html
[`FnKind::Fn`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/visit/enum.FnKind.html#variant.Fn
[ident]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Ident.html

## Specifying the lint's minimum supported Rust version (MSRV)

Sometimes a lint makes suggestions that require a certain version of Rust. For
example, the `manual_strip` lint suggests using `str::strip_prefix` and
`str::strip_suffix` which is only available after Rust 1.45. In such cases, you
need to ensure that the MSRV configured for the project is >= the MSRV of the
required Rust feature. If multiple features are required, just use the one with
a lower MSRV.

First, add an MSRV alias for the required feature in [`clippy_utils::msrvs`].
This can be accessed later as `msrvs::STR_STRIP_PREFIX`, for example.

```rust
msrv_aliases! {
    ..
    1,45,0 { STR_STRIP_PREFIX }
}
```

In order to access the project-configured MSRV, you need to have an `msrv` field
in the LintPass struct, and a constructor to initialize the field. The `msrv`
value is passed to the constructor in `clippy_lints/lib.rs`.

```rust
pub struct ManualStrip {
    msrv: Msrv,
}

impl ManualStrip {
    pub fn new(conf: &'static Conf) -> Self {
        Self { msrv: conf.msrv }
    }
}
```

The project's MSRV can then be matched against the feature MSRV in the LintPass
using the `Msrv::meets` method.

``` rust
if !self.msrv.meets(cx, msrvs::STR_STRIP_PREFIX) {
    return;
}
```

Early lint passes should instead use `MsrvStack` coupled with
`extract_msrv_attr!()`

Once the `msrv` is added to the lint, a relevant test case should be added to
the lint's test file, `tests/ui/manual_strip.rs` in this example. It should
have a case for the version below the MSRV and one with the same contents but
for the MSRV version itself.

```rust,ignore
...

#[clippy::msrv = "1.44"]
fn msrv_1_44() {
    /* something that would trigger the lint */
}

#[clippy::msrv = "1.45"]
fn msrv_1_45() {
    /* something that would trigger the lint */
}
```

As a last step, the lint should be added to the lint documentation. This is done
in `clippy_config/src/conf.rs`:

```rust
define_Conf! {
    #[lints(
        allow_attributes,
        allow_attributes_without_reason,
        ..
        <the newly added lint name>,
        ..
        unused_trait_names,
        use_self,
    )]
    msrv: Msrv = Msrv::default(),
    ...
}
```

[`clippy_utils::msrvs`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_config/msrvs/index.html

Afterwards update the documentation for the book as described in [Adding configuration to a lint](#adding-configuration-to-a-lint).

## Author lint

If you have trouble implementing your lint, there is also the internal `author`
lint to generate Clippy code that detects the offending pattern. It does not
work for all the Rust syntax, but can give a good starting point.

The quickest way to use it, is the [Rust playground:
play.rust-lang.org][author_example]. Put the code you want to lint into the
editor and add the `#[clippy::author]` attribute above the item. Then run Clippy
via `Tools -> Clippy` and you should see the generated code in the output below.

[Here][author_example] is an example on the playground.

If the command was executed successfully, you can copy the code over to where
you are implementing your lint.

[author_example]: https://play.rust-lang.org/?version=nightly&mode=debug&edition=2024&gist=9a12cb60e5c6ad4e3003ac6d5e63cf55

## Print HIR lint

To implement a lint, it's helpful to first understand the internal
representation that rustc uses. Clippy has the `#[clippy::dump]` attribute that
prints the [_High-Level Intermediate Representation (HIR)_] of the item,
statement, or expression that the attribute is attached to. To attach the
attribute to expressions you often need to enable
`#![feature(stmt_expr_attributes)]`.

[Here][print_hir_example] you can find an example, just select _Tools_ and run
_Clippy_.

[_High-Level Intermediate Representation (HIR)_]: https://rustc-dev-guide.rust-lang.org/hir.html
[print_hir_example]: https://play.rust-lang.org/?version=nightly&mode=debug&edition=2024&gist=daf14db3a7f39ca467cd1b86c34b9afb

## Documentation

The final thing before submitting our PR is to add some documentation to our
lint declaration.

Please document your lint with a doc comment akin to the following:

```rust
declare_clippy_lint! {
    /// ### What it does
    /// Checks for ... (describe what the lint matches).
    ///
    /// ### Why is this bad?
    /// Supply the reason for linting the code.
    ///
    /// ### Example
    ///
    /// ```rust,ignore
    /// // A short example of code that triggers the lint
    /// ```
    ///
    /// Use instead:
    /// ```rust,ignore
    /// // A short example of improved code that doesn't trigger the lint
    /// ```
    #[clippy::version = "1.29.0"]
    pub FOO_FUNCTIONS,
    pedantic,
    "function named `foo`, which is not a descriptive name"
}
```

If the lint is in the `restriction` group because it lints things that are not
necessarily “bad” but are more of a style choice, then replace the
“Why is this bad?” section heading with “Why restrict this?”, to avoid writing
“Why is this bad? It isn't, but ...”.

Once your lint is merged, this documentation will show up in the [lint
list][lint_list].

[lint_list]: https://rust-lang.github.io/rust-clippy/master/index.html

## Running rustfmt

[Rustfmt] is a tool for formatting Rust code according to style guidelines. Your
code has to be formatted by `rustfmt` before a PR can be merged. Clippy uses
nightly `rustfmt` in the CI.

It can be installed via `rustup`:

```bash
rustup component add rustfmt --toolchain=nightly
```

Use `cargo dev fmt` to format the whole codebase. Make sure that `rustfmt` is
installed for the nightly toolchain.

[Rustfmt]: https://github.com/rust-lang/rustfmt

## Debugging

If you want to debug parts of your lint implementation, you can use the [`dbg!`]
macro anywhere in your code. Running the tests should then include the debug
output in the `stdout` part.

[`dbg!`]: https://doc.rust-lang.org/std/macro.dbg.html

## Conflicting lints

There are several lints that deal with the same pattern but suggest different approaches. In other words, some lints
may suggest modifications that go in the opposite direction to what some other lints already propose for the same
code, creating conflicting diagnostics.

When you are creating a lint that ends up in this scenario, the following tips should be encouraged to guide
classification:

* The only case where they should be in the same category is if that category is `restriction`. For example,
`semicolon_inside_block` and `semicolon_outside_block`.
* For all the other cases, they should be in different categories with different levels of allowance. For example,
`implicit_return` (restriction, allow) and `needless_return` (style, warn).

For lints that are in different categories, it is also recommended that at least one of them should be in the
`restriction` category. The reason for this is that the `restriction` group is the only group where we don't
recommend to enable the entire set, but cherry pick lints out of.

## PR Checklist

Before submitting your PR make sure you followed all the basic requirements:

<!-- Sync this with `.github/PULL_REQUEST_TEMPLATE` -->

- \[ ] Followed [lint naming conventions][lint_naming]
- \[ ] Added passing UI tests (including committed `.stderr` file)
- \[ ] `cargo test` passes locally
- \[ ] Executed `cargo dev update_lints`
- \[ ] Added lint documentation
- \[ ] Run `cargo dev fmt`

## Adding configuration to a lint

Clippy supports the configuration of lints values using a `clippy.toml` file which is searched for in:

1. The directory specified by the `CLIPPY_CONF_DIR` environment variable, or
2. The directory specified by the
[CARGO_MANIFEST_DIR](https://doc.rust-lang.org/cargo/reference/environment-variables.html) environment variable, or
3. The current directory.

Adding a configuration to a lint can be useful for
thresholds or to constrain some behavior that can be seen as a false positive
for some users. Adding a configuration is done in the following steps:

1. Adding a new configuration entry to [`clippy_config::conf`] like this:

   ```rust,ignore
   /// Lint: LINT_NAME.
   ///
   /// <The configuration field doc comment>
   (configuration_ident: Type = DefaultValue),
   ```

   The doc comment is automatically added to the documentation of the listed
   lints. The default value will be formatted using the `Debug` implementation
   of the type.
2. Adding the configuration value to the lint impl struct:
    1. This first requires the definition of a lint impl struct. Lint impl
       structs are usually generated with the `declare_lint_pass!` macro. This
       struct needs to be defined manually to add some kind of metadata to it:
       ```rust
       // Generated struct definition
       declare_lint_pass!(StructName => [
           LINT_NAME
       ]);

       // New manual definition struct
       pub struct StructName {}

       impl_lint_pass!(StructName => [
           LINT_NAME
       ]);
       ```

    2. Next add the configuration value and a corresponding creation method like
       this:
       ```rust
       pub struct StructName {
           configuration_ident: Type,
       }

       // ...

       impl StructName {
           pub fn new(conf: &'static Conf) -> Self {
               Self {
                   configuration_ident: conf.configuration_ident,
               }
           }
       }
       ```
3. Passing the configuration value to the lint impl struct:

   First find the struct construction in the [`clippy_lints` lib file]. The
   configuration value is now cloned or copied into a local value that is then
   passed to the impl struct like this:

   ```rust,ignore
   // Default generated registration:
   store.register_*_pass(|| box module::StructName);

   // New registration with configuration value
   store.register_*_pass(move || box module::StructName::new(conf));
   ```

   Congratulations the work is almost done. The configuration value can now be
   accessed in the linting code via `self.configuration_ident`.

4. Adding tests:
    1. The default configured value can be tested like any normal lint in
       [`tests/ui`].
    2. The configuration itself will be tested separately in [`tests/ui-toml`].
       Simply add a new subfolder with a fitting name. This folder contains a
       `clippy.toml` file with the configuration value and a rust file that
       should be linted by Clippy. The test can otherwise be written as usual.

5. Update [Lint Configuration](../lint_configuration.md)

   Run `cargo bless --test config-metadata` to generate documentation changes for the book.

[`clippy_config::conf`]: https://github.com/rust-lang/rust-clippy/blob/master/clippy_config/src/conf.rs
[`clippy_lints` lib file]: https://github.com/rust-lang/rust-clippy/blob/master/clippy_lints/src/lib.rs
[`tests/ui`]: https://github.com/rust-lang/rust-clippy/blob/master/tests/ui
[`tests/ui-toml`]: https://github.com/rust-lang/rust-clippy/blob/master/tests/ui-toml

## Cheat Sheet

Here are some pointers to things you are likely going to need for every lint:

* [Clippy utils][utils] - Various helper functions. Maybe the function you need
  is already in here ([`implements_trait`], [`snippet`], etc)
* [Clippy diagnostics][diagnostics]
* [Let chains][let-chains]
* [`from_expansion`][from_expansion] and
  [`in_external_macro`][in_external_macro]
* [`Span`][span]
* [`Applicability`][applicability]
* [Common tools for writing lints](common_tools_writing_lints.md) helps with
  common operations
* [The rustc-dev-guide][rustc-dev-guide] explains a lot of internal compiler
  concepts
* [The nightly rustc docs][nightly_docs] which has been linked to throughout
  this guide

For `EarlyLintPass` lints:

* [`EarlyLintPass`][early_lint_pass]
* [`rustc_ast::ast`][ast]

For `LateLintPass` lints:

* [`LateLintPass`][late_lint_pass]
* [`Ty::TyKind`][ty]

While most of Clippy's lint utils are documented, most of rustc's internals lack
documentation currently. This is unfortunate, but in most cases you can probably
get away with copying things from existing similar lints. If you are stuck,
don't hesitate to ask on [Zulip] or in the issue/PR.

[utils]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/index.html
[`implements_trait`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/ty/fn.implements_trait.html
[`snippet`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/source/fn.snippet.html
[let-chains]: https://github.com/rust-lang/rust/pull/94927
[from_expansion]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html#method.from_expansion
[in_external_macro]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html#method.in_external_macro
[span]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html
[applicability]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/enum.Applicability.html
[rustc-dev-guide]: https://rustc-dev-guide.rust-lang.org/
[nightly_docs]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/
[ast]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast/ast/index.html
[ty]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/sty/index.html
[Zulip]: https://rust-lang.zulipchat.com/#narrow/stream/clippy


---

# Define New Lints

The first step in the journey of a new lint is the definition
and registration of the lint in Clippy's codebase.
We can use the Clippy dev tools to handle this step since setting up the
lint involves some boilerplate code.

#### Lint types

A lint type is the category of items and expressions in which your lint focuses on.

As of the writing of this documentation update, there are 11 _types_ of lints
besides the numerous standalone lints living under `clippy_lints/src/`:

- `cargo`
- `casts`
- `functions`
- `loops`
- `matches`
- `methods`
- `misc_early`
- `operators`
- `transmute`
- `types`
- `unit_types`

These types group together lints that share some common behaviors. For instance,
`functions` groups together lints that deal with some aspects of functions in
Rust, like definitions, signatures and attributes.

For more information, feel free to compare the lint files under any category
with [All Clippy lints][all_lints] or ask one of the maintainers.

## Lint name

A good lint name is important, make sure to check the [lint naming
guidelines][lint_naming]. Don't worry, if the lint name doesn't fit, a Clippy
team member will alert you in the PR process.

---

We'll name our example lint that detects functions named "foo" `foo_functions`.
Check the [lint naming guidelines][lint_naming] to see why this name makes
sense.

## Add and Register the Lint

Now that a name is chosen, we shall register `foo_functions` as a lint to the
codebase. There are two ways to register a lint.

### Standalone

If you believe that this new lint is a standalone lint (that doesn't belong to
any specific [type](#lint-types) like `functions` or `loops`), you can run the
following command in your Clippy project:

```sh
$ cargo dev new_lint --name=lint_name --pass=late --category=pedantic
```

There are two things to note here:

1. `--pass`: We set `--pass=late` in this command to do a late lint pass. The
   alternative is an `early` lint pass. We will discuss this difference in the
   [Lint Passes] chapter.
2. `--category`: If not provided, the `category` of this new lint will default
   to `nursery`.

The `cargo dev new_lint` command will create a new file:
`clippy_lints/src/foo_functions.rs` as well as [register the
lint](#lint-registration).

Overall, you should notice that the following files are modified or created:

```sh
$ git status
On branch foo_functions
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CHANGELOG.md
	modified:   clippy_lints/src/lib.register_lints.rs
	modified:   clippy_lints/src/lib.register_pedantic.rs
	modified:   clippy_lints/src/lib.rs

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	clippy_lints/src/foo_functions.rs
	tests/ui/foo_functions.rs
```


### Specific Type

> **Note**: Lint types are listed in the ["Lint types"](#lint-types) section

If you believe that this new lint belongs to a specific type of lints,
you can run `cargo dev new_lint` with a `--type` option.

Since our `foo_functions` lint is related to function calls, one could
argue that we should put it into a group of lints that detect some behaviors
of functions, we can put it in the `functions` group.

Let's run the following command in your Clippy project:

```sh
$ cargo dev new_lint --name=foo_functions --type=functions --category=pedantic
```

This command will create, among other things, a new file:
`clippy_lints/src/{type}/foo_functions.rs`.
In our case, the path will be `clippy_lints/src/functions/foo_functions.rs`.

Notice how this command has a `--type` flag instead of `--pass`. Unlike a standalone
definition, this lint won't be registered in the traditional sense. Instead, you will
call your lint from within the type's lint pass, found in `clippy_lints/src/{type}/mod.rs`.

A _type_ is just the name of a directory in `clippy_lints/src`, like `functions` in
the example command. Clippy groups together some lints that share common behaviors,
so if your lint falls into one, it would be best to add it to that type.

Overall, you should notice that the following files are modified or created:

```sh
$ git status
On branch foo_functions
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CHANGELOG.md
	modified:   clippy_lints/src/declared_lints.rs
	modified:   clippy_lints/src/functions/mod.rs

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	clippy_lints/src/functions/foo_functions.rs
	tests/ui/foo_functions.rs
```


## The `declare_clippy_lint` macro

After `cargo dev new_lint`, you should see a macro with the name
`declare_clippy_lint`. It will be in the same file if you defined a standalone
lint, and it will be in `mod.rs` if you defined a type-specific lint.

The macro looks something like this:

```rust
declare_clippy_lint! {
    /// ### What it does
    ///
    /// // Describe here what does the lint do.
    ///
    /// Triggers when detects...
    ///
    /// ### Why is this bad?
    ///
    /// // Describe why this pattern would be bad
    ///
    /// It can lead to...
    ///
    /// ### Example
    /// ```rust
    /// // example code where Clippy issues a warning
    /// ```
    /// Use instead:
    /// ```rust
    /// // example code which does not raise Clippy warning
    /// ```
    #[clippy::version = "1.70.0"] // <- In which version was this implemented, keep it up to date!
    pub LINT_NAME, // <- The lint name IN_ALL_CAPS
    pedantic, // <- The lint group
    "default lint description" // <- A lint description, e.g. "A function has an unit return type."
}
```

## Lint registration

If we run the `cargo dev new_lint` command for a new lint, the lint will be
automatically registered and there is nothing more to do.

However, sometimes we might want to declare a new lint by hand. In this case,
we'd use `cargo dev update_lints` command afterwards.

When a lint is manually declared, we might need to register the lint pass
manually in the `register_lints` function in `clippy_lints/src/lib.rs`:

```rust
store.register_late_pass(|_| Box::new(foo_functions::FooFunctions));
```

As you might have guessed, where there's something late, there is something
early: in Clippy there is a `register_early_pass` method as well. More on early
vs. late passes in the [Lint Passes] chapter.

Without a call to one of `register_early_pass` or `register_late_pass`, the lint
pass in question will not be run.


[all_lints]: https://rust-lang.github.io/rust-clippy/master/
[lint_naming]: https://rust-lang.github.io/rfcs/0344-conventions-galore.html#lints
[Lint Passes]: lint_passes.md


---

# Testing

Developing lints for Clippy is a Test-Driven Development (TDD) process because
our first task before implementing any logic for a new lint is to write some test cases.

## Develop Lints with Tests

When we develop Clippy, we enter a complex and chaotic realm full of
programmatic issues, stylistic errors, illogical code and non-adherence to convention.
Tests are the first layer of order we can leverage to define when and where
we want a new lint to trigger or not.

Moreover, writing tests first help Clippy developers to find a balance for
the first iteration of and further enhancements for a lint.
With test cases on our side, we will not have to worry about over-engineering
a lint on its first version nor missing out some obvious edge cases of the lint.
This approach empowers us to iteratively enhance each lint.

## Clippy UI Tests

We use **UI tests** for testing in Clippy. These UI tests check that the output
of Clippy is exactly as we expect it to be. Each test is just a plain Rust file
that contains the code we want to check.

The output of Clippy is compared against a `.stderr` file. Note that you don't
have to create this file yourself. We'll get to generating the `.stderr` files
with the command [`cargo bless`](#cargo-bless) (seen later on).

### Write Test Cases

Let us now think about some tests for our imaginary `foo_functions` lint. We
start by opening the test file `tests/ui/foo_functions.rs` that was created by
`cargo dev new_lint`.

Update the file with some examples to get started:

```rust
#![warn(clippy::foo_functions)] // < Add this, so the lint is guaranteed to be enabled in this file

// Impl methods
struct A;
impl A {
    pub fn fo(&self) {}
    pub fn foo(&self) {}
    //~^ foo_functions
    pub fn food(&self) {}
}

// Default trait methods
trait B {
    fn fo(&self) {}
    fn foo(&self) {}
    //~^ foo_functions
    fn food(&self) {}
}

// Plain functions
fn fo() {}
fn foo() {}
//~^ foo_functions
fn food() {}

fn main() {
    // We also don't want to lint method calls
    foo();
    let a = A;
    a.foo();
}
```

Without actual lint logic to emit the lint when we see a `foo` function name,
this test will fail, because we expect errors at lines marked with
`//~^ foo_functions`. However, we can now run the test with the following command:

```sh
$ TESTNAME=foo_functions cargo uitest
```

Clippy will compile and it will fail complaining it didn't receive any errors:

```
...Clippy warnings and test outputs...
error: diagnostic code `clippy::foo_functions` not found on line 8
 --> tests/ui/foo_functions.rs:9:10
  |
9 |     //~^ foo_functions
  |          ^^^^^^^^^^^^^ expected because of this pattern
  |

error: diagnostic code `clippy::foo_functions` not found on line 16
  --> tests/ui/foo_functions.rs:17:10
   |
17 |     //~^ foo_functions
   |          ^^^^^^^^^^^^^ expected because of this pattern
   |

error: diagnostic code `clippy::foo_functions` not found on line 23
  --> tests/ui/foo_functions.rs:24:6
   |
24 | //~^ foo_functions
   |      ^^^^^^^^^^^^^ expected because of this pattern
   |

```

This is normal. After all, we wrote a bunch of Rust code but we haven't really
implemented any logic for Clippy to detect `foo` functions and emit a lint.

As we gradually implement our lint logic, we will keep running this UI test command.
Clippy will begin outputting information that allows us to check if the output is
turning into what we want it to be.

### Example output

As our `foo_functions` lint is tested, the output would look something like this:

```
failures:
---- compile_test stdout ----
normalized stderr:
error: function called "foo"
  --> tests/ui/foo_functions.rs:6:12
   |
LL |     pub fn foo(&self) {}
   |            ^^^
   |
   = note: `-D clippy::foo-functions` implied by `-D warnings`
error: function called "foo"
  --> tests/ui/foo_functions.rs:13:8
   |
LL |     fn foo(&self) {}
   |        ^^^
error: function called "foo"
  --> tests/ui/foo_functions.rs:19:4
   |
LL | fn foo() {}
   |    ^^^
error: aborting due to 3 previous errors
```

Note the *failures* label at the top of the fragment, we'll get rid of it
(saving this output) in the next section.

> _Note:_ You can run multiple test files by specifying a comma separated list:
> `TESTNAME=foo_functions,bar_methods,baz_structs`.

### `cargo bless`

Once we are satisfied with the output, we need to run this command to
generate or update the `.stderr` file for our lint:

```sh
$ TESTNAME=foo_functions cargo uibless
```

This writes the emitted lint suggestions and fixes to the `.stderr` file, with
the reason for the lint, suggested fixes, and line numbers, etc.

Running `TESTNAME=foo_functions cargo uitest` should pass then. When we commit
our lint, we need to commit the generated `.stderr` files, too.

In general, you should only commit files changed by `cargo bless` for the
specific lint you are creating/editing.

> _Note:_ If the generated `.stderr`, and `.fixed` files are empty,
> they should be removed.

## `toml` Tests

Some lints can be configured through a `clippy.toml` file. Those configuration
values are tested in `tests/ui-toml`.

To add a new test there, create a new directory and add the files:

- `clippy.toml`: Put here the configuration value you want to test.
- `lint_name.rs`: A test file where you put the testing code, that should see a
  different lint behavior according to the configuration set in the
  `clippy.toml` file.

The potential `.stderr` and `.fixed` files can again be generated with `cargo
bless`.

## Cargo Lints

The process of testing is different for Cargo lints in that now we are
interested in the `Cargo.toml` manifest file. In this case, we also need a
minimal crate associated with that manifest. Those tests are generated in
`tests/ui-cargo`.

Imagine we have a new example lint that is named `foo_categories`, we can run:

```sh
$ cargo dev new_lint --name=foo_categories --pass=late --category=cargo
```

After running `cargo dev new_lint` we will find by default two new crates,
each with its manifest file:

* `tests/ui-cargo/foo_categories/fail/Cargo.toml`: this file should cause the
  new lint to raise an error.
* `tests/ui-cargo/foo_categories/pass/Cargo.toml`: this file should not trigger
  the lint.

If you need more cases, you can copy one of those crates (under
`foo_categories`) and rename it.

The process of generating the `.stderr` file is the same as for other lints
and prepending the `TESTNAME` variable to `cargo uitest` works for Cargo lints too.

## Rustfix Tests

If the lint you are working on is making use of structured suggestions,
[`rustfix`] will apply the suggestions from the lint to the test file code and
compare that to the contents of a `.fixed` file.

Structured suggestions tell a user how to fix or re-write certain code that has
been linted with [`span_lint_and_sugg`].

Should `span_lint_and_sugg` be used to generate a suggestion, but not all
suggestions lead to valid code, you can use the `//@no-rustfix` comment on top
of the test file, to not run `rustfix` on that file.

We'll talk about suggestions more in depth in a [later chapter](emitting_lints.md).

Use `cargo bless` to automatically generate the `.fixed` file after running
the tests.

[`rustfix`]: https://github.com/rust-lang/cargo/tree/master/crates/rustfix
[`span_lint_and_sugg`]: https://doc.rust-lang.org/beta/nightly-rustc/clippy_utils/diagnostics/fn.span_lint_and_sugg.html

## Testing Manually

Manually testing against an example file can be useful if you have added some
`println!`s and the test suite output becomes unreadable.

To try Clippy with your local modifications, run from the working copy root.

```sh
$ cargo dev lint input.rs
```


---

# Lint passes

Before working on the logic of a new lint, there is an important decision
that every Clippy developer must make: to use
[`EarlyLintPass`][early_lint_pass] or [`LateLintPass`][late_lint_pass].

In short, the `LateLintPass` has access to type and symbol information while the
`EarlyLintPass` doesn't. If you don't need access to type information, use the
`EarlyLintPass`.

Let us expand on these two traits more below.

## `EarlyLintPass`

If you examine the documentation on [`EarlyLintPass`][early_lint_pass] closely,
you'll see that every method defined for this trait utilizes a
[`EarlyContext`][early_context]. In `EarlyContext`'s documentation, it states:

> Context for lint checking of the AST, after expansion, before lowering to HIR.

Voilà. `EarlyLintPass` works only on the Abstract Syntax Tree (AST) level.
And AST is generated during the [lexing and parsing][lexing_and_parsing] phase
of code compilation. Therefore, it doesn't know what a symbol means or information about types, and it should
be our trait choice for a new lint if the lint only deals with syntax-related issues.

While linting speed has not been a concern for Clippy,
the `EarlyLintPass` is faster, and it should be your choice
if you know for sure a lint does not need type information.

As a reminder, run the following command to generate boilerplate for lints
that use `EarlyLintPass`:

```sh
$ cargo dev new_lint --name=<your_new_lint> --pass=early --category=<your_category_choice>
```

### Example for `EarlyLintPass`

Take a look at the following code:

```rust
let x = OurUndefinedType;
x.non_existing_method();
```

From the AST perspective, both lines are "grammatically" correct.
The assignment uses a `let` and ends with a semicolon. The invocation
of a method looks fine, too. As programmers, we might raise a few
questions already, but the parser is okay with it. This is what we
mean when we say `EarlyLintPass` deals with only syntax on the AST level.

Alternatively, think of the `foo_functions` lint we mentioned in
the [Define New Lints](defining_lints.md) chapter.

We want the `foo_functions` lint to detect functions with `foo` as their name.
Writing a lint that only checks for the name of a function means that we only
work with the AST and don't have to access the type system at all (the type system is where
`LateLintPass` comes into the picture).

## `LateLintPass`

In contrast to `EarlyLintPass`, `LateLintPass` contains type information.

If you examine the documentation on [`LateLintPass`][late_lint_pass] closely,
you see that every method defined in this trait utilizes a
[`LateContext`][late_context].

In `LateContext`'s documentation we will find methods that
deal with type-checking, which do not exist in `EarlyContext`, such as:

- [`maybe_typeck_results`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/context/struct.LateContext.html#method.maybe_typeck_results)
- [`typeck_results`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/context/struct.LateContext.html#method.typeck_results)

### Example for `LateLintPass`

Let us take a look with the following example:

```rust
let x = OurUndefinedType;
x.non_existing_method();
```

These two lines of code are syntactically correct code from the perspective
of the AST. We have an assignment and invoke a method on the variable that
is of a type. Grammatically, everything is in order for the parser.

However, going down a level and looking at the type information,
the compiler will notice that both `OurUndefinedType` and `non_existing_method()`
**are undefined**.

As Clippy developers, to access such type information, we must implement
`LateLintPass` on our lint.
When you browse through Clippy's lints, you will notice that almost every lint
is implemented in a `LateLintPass`, specifically because we often need to check
not only for syntactic issues but also type information.

Another limitation of the `EarlyLintPass` is that the nodes are only identified
by their position in the AST. This means that you can't just get an `id` and
request a certain node. For most lints that is fine, but we have some lints
that require the inspection of other nodes, which is easier at the HIR level.
In these cases, `LateLintPass` is the better choice.

As a reminder, run the following command to generate boilerplate for lints
that use `LateLintPass`:

```sh
$ cargo dev new_lint --name=<your_new_lint> --pass=late --category=<your_category_choice>
```

[early_context]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/context/struct.EarlyContext.html
[early_lint_pass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.EarlyLintPass.html
[late_context]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/context/struct.LateContext.html
[late_lint_pass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html
[lexing_and_parsing]: https://rustc-dev-guide.rust-lang.org/overview.html#lexing-and-parsing


---

# Emitting a lint

Once we have [defined a lint](defining_lints.md), written [UI
tests](writing_tests.md) and chosen [the lint pass](lint_passes.md) for the lint,
we can begin the implementation of the lint logic so that we can emit it and
gradually work towards a lint that behaves as expected.

Note that we will not go into concrete implementation of a lint logic in this
chapter. We will go into details in later chapters as well as in two examples of
real Clippy lints.

To emit a lint, we must implement a pass (see [Lint Passes](lint_passes.md)) for
the lint that we have declared. In this example we'll implement a "late" lint,
so take a look at the [LateLintPass][late_lint_pass] documentation, which
provides an abundance of methods that we can implement for our lint.

```rust
pub trait LateLintPass<'tcx>: LintPass {
    // Trait methods
}
```

By far the most common method used for Clippy lints is [`check_expr`
method][late_check_expr], this is because Rust is an expression language and,
more often than not, the lint we want to work on must examine expressions.

> _Note:_ If you don't fully understand what expressions are in Rust, take a
> look at the official documentation on [expressions][rust_expressions]

Other common ones include the [`check_fn` method][late_check_fn] and the
[`check_item` method][late_check_item].

### Emitting a lint

Inside the trait method that we implement, we can write down the lint logic and
emit the lint with suggestions.

Clippy's [diagnostics] provides quite a few diagnostic functions that we can use
to emit lints. Take a look at the documentation to pick one that suits your
lint's needs the best. Some common ones you will encounter in the Clippy
repository includes:

- [`span_lint`]: Emits a lint without providing any other information
- [`span_lint_and_note`]: Emits a lint and adds a note
- [`span_lint_and_help`]: Emits a lint and provides a helpful message
- [`span_lint_and_sugg`]: Emits a lint and provides a suggestion to fix the code
- [`span_lint_and_then`]: Like `span_lint`, but allows for a lot of output
  customization.

```rust
impl<'tcx> LateLintPass<'tcx> for LintName {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx Expr<'_>)  {
        // Imagine that `some_lint_expr_logic` checks for requirements for emitting the lint
        if some_lint_expr_logic(expr) {
            span_lint_and_help(
                cx, // < The context
                LINT_NAME, // < The name of the lint in ALL CAPS
                expr.span, // < The span to lint
                "message on why the lint is emitted",
                None, // < An optional help span (to highlight something in the lint)
                "message that provides a helpful suggestion",
            );
        }
    }
}
```

> Note: The message should be matter of fact and avoid capitalization and
> punctuation. If multiple sentences are needed, the messages should probably be
> split up into an error + a help / note / suggestion message.

## Suggestions: Automatic fixes

Some lints know what to change in order to fix the code. For example, the lint
[`range_plus_one`][range_plus_one] warns for ranges where the user wrote `x..y +
1` instead of using an [inclusive range][inclusive_range] (`x..=y`). The fix to
this code would be changing the `x..y + 1` expression to `x..=y`. **This is
where suggestions come in**.

A suggestion is a change that the lint provides to fix the issue it is linting.
The output looks something like this (from the example earlier):

```text
error: an inclusive range would be more readable
  --> tests/ui/range_plus_minus_one.rs:37:14
   |
LL |     for _ in 1..1 + 1 {}
   |              ^^^^^^^^ help: use: `1..=1`
```

**Not all suggestions are always right**, some of them require human
supervision, that's why we have [Applicability][applicability].

Applicability indicates confidence in the correctness of the suggestion, some
are always right (`Applicability::MachineApplicable`), but we use
`Applicability::MaybeIncorrect` and others when talking about a suggestion that
may be incorrect.

### Example

The same lint `LINT_NAME` but that emits a suggestion would look something like this:

```rust
impl<'tcx> LateLintPass<'tcx> for LintName {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx Expr<'_>)  {
        // Imagine that `some_lint_expr_logic` checks for requirements for emitting the lint
        if some_lint_expr_logic(expr) {
            span_lint_and_sugg( // < Note this change
                cx,
                LINT_NAME,
                span,
                "message on why the lint is emitted",
                "use",
                format!("foo + {} * bar", snippet(cx, expr.span, "<default>")), // < Suggestion
                Applicability::MachineApplicable,
            );
        }
    }
}
```

Suggestions generally use the [`format!`][format_macro] macro to interpolate the
old values with the new ones. To get code snippets, use one of the `snippet*`
functions from `clippy_utils::source`.

## How to choose between notes, help messages and suggestions

Notes are presented separately from the main lint message, they provide useful
information that the user needs to understand why the lint was activated. They
are the most helpful when attached to a span.

Examples:

### Notes

```text
error: calls to `std::mem::forget` with a reference instead of an owned value. Forgetting a reference does nothing.
  --> tests/ui/drop_forget_ref.rs:10:5
   |
10 |     forget(&SomeStruct);
   |     ^^^^^^^^^^^^^^^^^^^
   |
   = note: `-D clippy::forget-ref` implied by `-D warnings`
note: argument has type &SomeStruct
  --> tests/ui/drop_forget_ref.rs:10:12
   |
10 |     forget(&SomeStruct);
   |            ^^^^^^^^^^^
```

### Help Messages

Help messages are specifically to help the user. These are used in situation
where you can't provide a specific machine applicable suggestion. They can also
be attached to a span.

Example:

```text
error: constant division of 0.0 with 0.0 will always result in NaN
  --> tests/ui/zero_div_zero.rs:6:25
   |
6  |     let other_f64_nan = 0.0f64 / 0.0;
   |                         ^^^^^^^^^^^^
   |
   = help: consider using `f64::NAN` if you would like a constant representing NaN
```

### Suggestions

Suggestions are the most helpful, they are changes to the source code to fix the
error. The magic in suggestions is that tools like `rustfix` can detect them and
automatically fix your code.

Example:

```text
error: This `.fold` can be more succinctly expressed as `.any`
--> tests/ui/methods.rs:390:13
    |
390 |     let _ = (0..3).fold(false, |acc, x| acc || x > 2);
    |                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ help: try: `.any(|x| x > 2)`
    |
```

### Snippets

Snippets are pieces of the source code (as a string), they are extracted
generally using the [`snippet`][snippet_fn] function.

For example, if you want to know how an item looks (and you know the item's
span), you could use `snippet(cx, span, "..")`.

## Final: Run UI Tests to Emit the Lint

Now, if we run our [UI test](writing_tests.md), we should see that Clippy now
produces output that contains the lint message we designed.

The next step is to implement the logic properly, which is a detail that we will
cover in the next chapters.

[diagnostics]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/diagnostics/index.html
[late_check_expr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html#method.check_expr
[late_check_fn]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html#method.check_fn
[late_check_item]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html#method.check_item
[late_lint_pass]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/trait.LateLintPass.html
[rust_expressions]: https://doc.rust-lang.org/reference/expressions.html
[`span_lint`]: https://doc.rust-lang.org/beta/nightly-rustc/clippy_utils/diagnostics/fn.span_lint.html
[`span_lint_and_note`]: https://doc.rust-lang.org/beta/nightly-rustc/clippy_utils/diagnostics/fn.span_lint_and_note.html
[`span_lint_and_help`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/diagnostics/fn.span_lint_and_help.html
[`span_lint_and_sugg`]: https://doc.rust-lang.org/nightly/nightly-rustc/clippy_utils/diagnostics/fn.span_lint_and_sugg.html
[`span_lint_and_then`]: https://doc.rust-lang.org/beta/nightly-rustc/clippy_utils/diagnostics/fn.span_lint_and_then.html
[range_plus_one]: https://rust-lang.github.io/rust-clippy/master/index.html#range_plus_one
[inclusive_range]: https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html
[applicability]: https://doc.rust-lang.org/beta/nightly-rustc/rustc_errors/enum.Applicability.html
[snippet_fn]: https://doc.rust-lang.org/beta/nightly-rustc/clippy_utils/source/fn.snippet.html
[format_macro]: https://doc.rust-lang.org/std/macro.format.html
