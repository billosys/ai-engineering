# What are Editions?

In May 2015, the [release of Rust 1.0](https://blog.rust-lang.org/2015/05/15/Rust-1.0.html) established "[stability without stagnation](https://blog.rust-lang.org/2014/10/30/Stability.html)" as a core Rust axiom. Since then, Rust has committed to a pivotal rule: once a feature is [released through stable](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html), contributors will continue to support that feature for all future releases.

However, there are times when it's useful to make backwards-incompatible changes to the language. A common example is the introduction of a new keyword. For instance, early versions of Rust didn't feature the `async` and `await` keywords.

If Rust had suddenly introduced these new keywords, some code would have broken: `let async = 1;` would no longer work.

Rust uses **editions** to solve this problem. When there are backwards-incompatible changes, they are pushed into the next edition. Since editions are opt-in, existing crates won't use the changes unless they explicitly migrate into the new edition. For example, the latest version of Rust doesn't treat `async` as a keyword unless edition 2018 or later is chosen.

Each crate chooses its edition [within its `Cargo.toml` file](https://doc.rust-lang.org/cargo/reference/manifest.html#the-edition-field). When creating a new crate with Cargo, it will automatically select the newest stable edition.

## Editions do not split the ecosystem

When creating editions, there is one most consequential rule: crates in one edition **must** seamlessly interoperate with those compiled with other editions.

In other words, each crate can decide when to migrate to a new edition independently. This decision is 'private' - it won't affect other crates in the ecosystem.

For Rust, this required compatibility implies some limits on the kinds of changes that can be featured in an edition. As a result, changes found in new Rust editions tend to be 'skin deep'. All Rust code - regardless of edition - will ultimately compile down to the same internal representation within the compiler.

## Edition migration is easy and largely automated

Rust aims to make upgrading to a new edition an easy process. When a new edition releases, crate authors may use [automatic migration tooling within `cargo`](https://doc.rust-lang.org/cargo/commands/cargo-fix.html) to migrate. Cargo will then make minor changes to the code to make it compatible with the new version.

For example, when migrating to Rust 2018, anything named `async` will now use the equivalent [raw identifier syntax](https://doc.rust-lang.org/rust-by-example/compatibility/raw_identifiers.html): `r#async`.

Cargo's automatic migrations aren't perfect: there may still be corner cases where manual changes are required. It aims to avoid changes to semantics that could affect the correctness or performance of the code.

## What this guide covers

In addition to tooling, this Rust Edition Guide also covers the changes that are part of each edition. It describes each change and links to additional details, if available. It also covers corner cases or tricky details crate authors should be aware of.

Crate authors should find:

- An overview of editions
- A migration guide for specific editions
- A quick troubleshooting reference when automated tooling isn't working.


---

# Creating a new project

A new project created with Cargo is configured to use the latest edition by
default:

```console
$ cargo new foo
    Creating binary (application) `foo` package
note: see more `Cargo.toml` keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
$ cat foo/Cargo.toml
[package]
name = "foo"
version = "0.1.0"
edition = "2024"

[dependencies]
```

That `edition = "2024"` setting configures your package to be built using the
Rust 2024 edition. No further configuration needed!

You can use the `--edition <YEAR>` option of `cargo new` to create the project
using some specific edition. For example, creating a new project to use the
Rust 2018 edition could be done like this:

```console
$ cargo new --edition 2018 foo
    Creating binary (application) `foo` package
note: see more `Cargo.toml` keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
$ cat foo/Cargo.toml
[package]
name = "foo"
version = "0.1.0"
edition = "2018"

[dependencies]
```

Don't worry about accidentally using an invalid year for the edition; the
`cargo new` invocation will not accept an invalid edition year value:

```console
$ cargo new --edition 2019 foo
error: invalid value '2019' for '--edition <YEAR>'
  [possible values: 2015, 2018, 2021, 2024]

  tip: a similar value exists: '2021'

For more information, try '--help'.
```

You can change the value of the `edition` key by simply editing the
`Cargo.toml` file. For example, to cause your package to be built using the
Rust 2015 edition, you would set the key as in the following example:

```toml
[package]
name = "foo"
version = "0.1.0"
edition = "2015"

[dependencies]
```


---

# Transitioning an existing project to a new edition

Rust includes tooling to automatically transition a project from one edition to the next.
It will update your source code so that it is compatible with the next edition.
Briefly, the steps to update to the next edition are:

1. Run `cargo update` to update your dependencies to the latest versions.
2. Run `cargo fix --edition`
3. Edit `Cargo.toml` and set the `edition` field to the next edition, for example `edition = "2024"`
4. Run `cargo build` or `cargo test` to verify the fixes worked.
5. Run `cargo fmt` to reformat your project.

The following sections dig into the details of these steps, and some of the issues you may encounter along the way.

> It's our intention that the migration to new editions is as smooth an
> experience as possible. If it's difficult for you to upgrade to the latest edition,
> we consider that a bug. If you run into problems with this process, please
> [file a bug report](https://github.com/rust-lang/rust/issues/new/choose). Thank you!

## Starting the migration

As an example, let's take a look at transitioning from the 2015 edition to the 2018 edition.
The steps are essentially the same when transitioning to other editions like 2021.

Imagine we have a crate that has this code in `src/lib.rs`:

```rust
trait Foo {
    fn foo(&self, i32);
}
```

This code uses an anonymous parameter, that `i32`. This is [not
supported in Rust 2018](../rust-2018/trait-system/no-anon-params.md), and
so this would fail to compile. Let's get this code up to date!

## Updating your dependencies

Before we get started, it is recommended to update your dependencies. Some dependencies, particularly some proc-macros or dependencies that do build-time code generation, may have compatibility issues with newer editions. New releases may have been made since you last updated which may fix these issues. Run the following:

```console
cargo update
```

After updating, you may want to run your tests to verify everything is working. If you are using a source control tool such as `git`, you may want to commit these changes separately to keep a logical separation of commits.

## Updating your code to be compatible with the new edition

Your code may or may not use features that are incompatible with the new edition.
In order to help transition to the next edition, Cargo includes the [`cargo fix`] subcommand to automatically update your source code.
To start, let's run it:

```console
cargo fix --edition
```

This will check your code, and automatically fix any issues that it can.
Let's look at `src/lib.rs` again:

```rust
trait Foo {
    fn foo(&self, _: i32);
}
```

It's re-written our code to introduce a parameter name for that `i32` value.
In this case, since it had no name, `cargo fix` will replace it with `_`,
which is conventional for unused variables.

`cargo fix` can't always fix your code automatically.
If `cargo fix` can't fix something, it will print the warning that it cannot fix
to the console. If you see one of these warnings, you'll have to update your code manually.
See the [Advanced migration strategies] chapter for more on working with the migration process, and read the chapters in this guide which explain which changes are needed.
If you have problems, please seek help at the [user's forums](https://users.rust-lang.org/).

## Enabling the new edition to use new features

In order to use some new features, you must explicitly opt in to the new
edition. Once you're ready to continue, change your `Cargo.toml` to add the new
`edition` key/value pair. For example:

```toml
[package]
name = "foo"
version = "0.1.0"
edition = "2018"
```

If there's no `edition` key, Cargo will default to Rust 2015. But in this case,
we've chosen `2018`, and so our code will compile with Rust 2018!

## Testing your code in the new edition

The next step is to test your project on the new edition.
Run your project tests to verify that everything still works, such as running [`cargo test`].
If new warnings are issued, you may want to consider running `cargo fix` again (without the `--edition` flag) to apply any suggestions given by the compiler.

At this point, you may still need to do some manual changes. For example, the automatic migration does not update doctests, and build-time code generation or macros may need manual updating. See the [advanced migrations chapter] for more information.

Congrats! Your code is now valid in both Rust 2015 and Rust 2018!

[advanced migrations chapter]: advanced-migrations.md

## Reformatting with rustfmt

If you use [rustfmt] to automatically maintain formatting within your project, then you should consider reformatting using the new formatting rules of the new edition.

Before reformatting, if you are using a source control tool such as `git`, you may want to commit all the changes you have made up to this point before taking this step. It can be useful to put formatting changes in a separate commit, because then you can see which changes are just formatting versus other code changes, and also possibly ignore the formatting changes in `git blame`.

```console
cargo fmt
```

See the [style editions chapter] for more information.

[rustfmt]: https://github.com/rust-lang/rustfmt
[style editions chapter]: ../rust-2024/rustfmt-style-edition.md

## Migrating to an unstable edition

After an edition is released, there is roughly a three year window before the next edition.
During that window, new features may be added to the next edition, which will only be available on the [nightly channel].
If you want to help test those new features before they are stabilized, you can use the nightly channel to try them out.

The steps are roughly similar to the stable channel:

1. Install the most recent nightly: `rustup update nightly`.
2. Run `cargo +nightly fix --edition`.
3. Edit `Cargo.toml` and place `cargo-features = ["edition20xx"]` at the top (above `[package]`), and change the edition field to say `edition = "20xx"` where `20xx` is the edition you are upgrading to.
4. Run `cargo +nightly check` to verify it now works in the new edition.

> **⚠ Caution**: Features implemented in the next edition may not have automatic migrations implemented with `cargo fix`, and the features themselves may not be finished.
> When possible, this guide should contain information about which features are implemented
> on nightly along with more information about their status.
> A few months before the edition is stabilized, all of the new features should be fully implemented, and the [Rust Blog] will announce a call for testing.

[`cargo fix`]: ../../cargo/commands/cargo-fix.html
[`cargo test`]: ../../cargo/commands/cargo-test.html
[Advanced migration strategies]: advanced-migrations.md
[nightly channel]: ../../book/appendix-07-nightly-rust.html
[Rust Blog]: https://blog.rust-lang.org/


---

# Advanced migration strategies

## How migrations work

[`cargo fix --edition`][`cargo fix`] works by running the equivalent of [`cargo check`] on your project with special [lints] enabled which will detect code that may not compile in the next edition.
These lints include instructions on how to modify the code to make it compatible on both the current and the next edition.
`cargo fix` applies these changes to the source code, and then runs `cargo check` again to verify that the fixes work.
If the fixes fail, then it will back out the changes and display a warning.

Changing the code to be simultaneously compatible with both the current and next edition makes it easier to incrementally migrate the code.
If the automated migration does not completely succeed, or requires manual help, you can iterate while staying on the original edition before changing `Cargo.toml` to use the next edition.

The lints that `cargo fix --edition` apply are part of a [lint group].
For example, when migrating from 2018 to 2021, Cargo uses the `rust-2021-compatibility` group of lints to fix the code.
Check the [Partial migration](#partial-migration-with-broken-code) section below for tips on using individual lints to help with migration.

`cargo fix` may run `cargo check` multiple times.
For example, after applying one set of fixes, this may trigger new warnings which require further fixes.
Cargo repeats this until no new warnings are generated.

## Migrating multiple configurations

`cargo fix` can only work with a single configuration at a time.
If you use [Cargo features] or [conditional compilation], then you may need to run `cargo fix` multiple times with different flags.

For example, if you have code that uses `#[cfg]` attributes to include different code for different platforms, you may need to run `cargo fix` with the `--target` option to fix for different targets.
This may require moving your code between machines if you don't have cross-compiling available.

Similarly, if you have conditions on Cargo features, like `#[cfg(feature = "my-optional-thing")]`, it is recommended to use the `--all-features` flag to allow `cargo fix` to migrate all the code behind those feature gates.
If you want to migrate feature code individually, you can use the `--features` flag to migrate one at a time.

## Migrating a large project or workspace

You can migrate a large project incrementally to make the process easier if you run into problems.

In a [Cargo workspace], each package defines its own edition, so the process naturally involves migrating one package at a time.

Within a [Cargo package], you can either migrate the entire package at once, or migrate individual [Cargo targets] one at a time.
For example, if you have multiple binaries, tests, and examples, you can use specific target selection flags with `cargo fix --edition` to migrate just that one target.
By default, `cargo fix` uses `--all-targets`.

For even more advanced cases, you can specify the edition for each individual target in `Cargo.toml` like this:

```toml
[[bin]]
name = "my-binary"
edition = "2018"
```

This usually should not be required, but is an option if you have a lot of targets and are having difficulty migrating them all together.

## Partial migration with broken code

Sometimes the fixes suggested by the compiler may fail to work.
When this happens, Cargo will report a warning indicating what happened and what the error was.
However, by default it will automatically back out the changes it made.
It can be helpful to keep the code in the broken state and manually resolve the issue.
Some of the fixes may have been correct, and the broken fix may be *mostly* correct, but just need minor tweaking.

In this situation, use the `--broken-code` option with `cargo fix` to tell Cargo not to back out the changes.
Then, you can go manually inspect the error and investigate what is needed to fix it.

Another option to incrementally migrate a project is to apply individual fixes separately, one at a time.
You can do this by adding the individual lints as warnings, and then either running `cargo fix` (without the `--edition` flag) or using your editor or IDE to apply its suggestions if it supports "Quick Fixes".

For example, the 2018 edition uses the [`keyword-idents`] lint to fix any conflicting keywords.
You can add `#![warn(keyword_idents)]` to the top of each crate (like at the top of `src/lib.rs` or `src/main.rs`).
Then, running `cargo fix` will apply just the suggestions for that lint.

You can see the list of lints enabled for each edition in the [lint group] page, or run the `rustc -Whelp` command.

## Migrating macros

Some macros may require manual work to fix them for the next edition.
For example, `cargo fix --edition` may not be able to automatically fix a macro that generates syntax that does not work in the next edition.

This may be a problem for both [proc macros] and `macro_rules`-style macros.
`macro_rules` macros can sometimes be automatically updated if the macro is used within the same crate, but there are several situations where it cannot.
Proc macros in general cannot be automatically fixed at all.

For example, if we migrate a crate containing this (contrived) macro `foo` from 2015 to 2018, `foo` would not be automatically fixed.

```rust
#[macro_export]
macro_rules! foo {
    () => {
        let dyn = 1;
        println!("it is {}", dyn);
    };
}
```

When this macro is defined in a 2015 crate, it can be used from a crate of any other edition due to macro hygiene (discussed below).
In 2015, `dyn` is a normal identifier and can be used without restriction.

However, in 2018, `dyn` is no longer a valid identifier.
When using `cargo fix --edition` to migrate to 2018, Cargo won't display any warnings or errors at all.
However, `foo` won't work when called from any crate.

If you have macros, you are encouraged to make sure you have tests that fully cover the macro's syntax.
You may also want to test the macros by importing and using them in crates from multiple editions, just to ensure it works correctly everywhere.
If you run into issues, you'll need to read through the chapters of this guide to understand how the code can be changed to work across all editions.

### Macro hygiene

Macros use a system called "edition hygiene" where the tokens within a macro are marked with which edition they come from.
This allows external macros to be called from crates of varying editions without needing to worry about which edition it is called from.

Let's take a closer look at the example above that defines a `macro_rules` macro using `dyn` as an identifier.
If that macro was defined in a crate using the 2015 edition, then that macro works fine, even if it were called from a 2018 crate where `dyn` is a keyword and that would normally be a syntax error.
The `let dyn = 1;` tokens are marked as being from 2015, and the compiler will remember that wherever that code gets expanded.
The parser looks at the edition of the tokens to know how to interpret it.

The problem arises when changing the edition to 2018 in the crate where it is defined.
Now, those tokens are tagged with the 2018 edition, and those will fail to parse.
However, since we never called the macro from our crate, `cargo fix --edition` never had a chance to inspect the macro and fix it.

<!-- TODO: hopefully someday, the reference will have chapters on how expansion works, and this can link there for actual details. -->

## Documentation tests

At this time, `cargo fix` is not able to update [documentation tests].
After updating the edition in `Cargo.toml`, you should run `cargo test` to ensure everything still passes.
If your documentation tests use syntax that is not supported in the new edition, you will need to update them manually.

In rare cases, you can manually set the edition for each test.
For example, you can use the [`edition2018` annotation][rustdoc-annotation] on the triple backticks to tell `rustdoc` which edition to use.

## Generated code

Another area where the automated fixes cannot apply is if you have a build script which generates Rust code at compile time (see [Code generation] for an example).
In this situation, if you end up with code that doesn't work in the next edition, you will need to manually change the build script to generate code that is compatible.

## Migrating non-Cargo projects

If your project is not using Cargo as a build system, it may still be possible to make use of the automated lints to assist migrating to the next edition.
You can enable the migration lints as described above by enabling the appropriate [lint group].
For example, you can use the `#![warn(rust_2021_compatibility)]` attribute or the `-Wrust-2021-compatibility` or `--force-warns=rust-2021-compatibility` [CLI flag].

The next step is to apply those lints to your code.
There are several options here:

* Manually read the warnings and apply the suggestions recommended by the compiler.
* Use an editor or IDE that supports automatically applying suggestions.
  For example, [Visual Studio Code] with the [Rust Analyzer extension] has the ability to use the "Quick Fix" links to automatically apply suggestions.
  Many other editors and IDEs have similar functionality.
* Write a migration tool using the [`rustfix`] library.
  This is the library that Cargo uses internally to take the [JSON messages] from the compiler and modify the source code.
  Check the [`examples` directory][rustfix-examples] for examples of how to use the library.

## Writing idiomatic code in a new edition

Editions are not only about new features and removing old ones.
In any programming language, idioms change over time, and Rust is no exception.
While old code will continue to compile, it might be written with different idioms today.

For example, in Rust 2015, external crates must be listed with `extern crate` like this:

```rust,ignore
// src/lib.rs
extern crate rand;
```

In Rust 2018, it is [no longer necessary](../rust-2018/path-changes.md#no-more-extern-crate) to include these items.

`cargo fix` has the `--edition-idioms` option to automatically transition some of these idioms to the new syntax.

> **Warning**: The current *"idiom lints"* are known to have some problems.
> They may make incorrect suggestions which may fail to compile.
> The current lints are:
> * Edition 2018:
>     * [`unused-extern-crates`]
>     * [`explicit-outlives-requirements`]
> * Edition 2021 does not have any idiom lints.
>
> The following instructions are recommended only for the intrepid who are willing to work through a few compiler/Cargo bugs!
> If you run into problems, you can try the `--broken-code` option [described above](#partial-migration-with-broken-code) to make as much progress as possible, and then resolve the remaining issues manually.

With that out of the way, we can instruct Cargo to fix our code snippet with:

```console
cargo fix --edition-idioms
```

Afterwards, the line with `extern crate rand;` in `src/lib.rs` will be removed.

We're now more idiomatic, and we didn't have to fix our code manually!

[`cargo check`]: ../../cargo/commands/cargo-check.html
[`cargo fix`]: ../../cargo/commands/cargo-fix.html
[`explicit-outlives-requirements`]:  ../../rustc/lints/listing/allowed-by-default.html#explicit-outlives-requirements
[`keyword-idents`]: ../../rustc/lints/listing/allowed-by-default.html#keyword-idents
[`rustfix`]: https://crates.io/crates/rustfix
[`unused-extern-crates`]: ../../rustc/lints/listing/allowed-by-default.html#unused-extern-crates
[Cargo features]: ../../cargo/reference/features.html
[Cargo package]: ../../cargo/reference/manifest.html#the-package-section
[Cargo targets]: ../../cargo/reference/cargo-targets.html
[Cargo workspace]: ../../cargo/reference/workspaces.html
[CLI flag]: ../../rustc/lints/levels.html#via-compiler-flag
[Code generation]: ../../cargo/reference/build-script-examples.html#code-generation
[conditional compilation]: ../../reference/conditional-compilation.html
[documentation tests]: ../../rustdoc/documentation-tests.html
[JSON messages]: ../../rustc/json.html
[lint group]: ../../rustc/lints/groups.html
[lints]: ../../rustc/lints/index.html
[proc macros]: ../../reference/procedural-macros.html
[Rust Analyzer extension]: https://marketplace.visualstudio.com/items?itemName=matklad.rust-analyzer
[rustdoc-annotation]: ../../rustdoc/documentation-tests.html#attributes
[rustfix-examples]: https://github.com/rust-lang/cargo/tree/master/crates/rustfix/examples
[Visual Studio Code]: https://code.visualstudio.com/
