# Debugging the compiler

This chapter contains a few tips to debug the compiler.
These tips aim to be useful no matter what you are working on.
Some of the other chapters have
advice about specific parts of the compiler (e.g. the [Queries Debugging and
Testing chapter](./incrcomp-debugging.html) or the [LLVM Debugging
chapter](./backend/debugging.md)).

## Configuring the compiler

By default, rustc is built without most debug information.
To enable debug info,
set `rust.debug = true` in your bootstrap.toml.

Setting `rust.debug = true` turns on many different debug options (e.g., `debug-assertions`,
`debug-logging`, etc.) which can be individually tweaked if you want to, but many people
simply set `rust.debug = true`.

If you want to use GDB to debug rustc, please set `bootstrap.toml` with options:

```toml
rust.debug = true
rust.debuginfo-level = 2
```

> NOTE:
> This will use a lot of disk space
> (upwards of <!-- date-check Aug 2022 --> 35GB),
> and will take a lot more compile time.
> With `debuginfo-level = 1` (the default when `debug = true`),
> you will be able to track the execution path,
> but will lose the symbol information for debugging.

The default configuration will enable `symbol-mangling-version` v0.
This requires at least GDB v10.2,
otherwise you need to disable new symbol-mangling-version in `bootstrap.toml`.

```toml
rust.new-symbol-mangling = false
```

> See the comments in `bootstrap.example.toml` for more info.

You will need to rebuild the compiler after changing any configuration option.

## Suppressing the ICE file

By default, if rustc encounters an Internal Compiler Error (ICE) it will dump the ICE contents to an
ICE file within the current working directory named `rustc-ice-<timestamp>-<pid>.txt`.
If this is not desirable, you can prevent the ICE file from being created with `RUSTC_ICE=0`.

## Getting a backtrace
[getting-a-backtrace]: #getting-a-backtrace

When you have an ICE (panic in the compiler), you can set
`RUST_BACKTRACE=1` to get the stack trace of the `panic!` like in normal Rust programs.
IIRC backtraces **don't work** on MinGW, sorry.
If you have trouble or the backtraces are full of `unknown`,
you might want to find some way to use Linux, Mac, or MSVC on Windows.

In the default configuration (without `debug` set to `true`), you don't have line numbers
enabled, so the backtrace looks like this:

```text
stack backtrace:
   0: std::sys::imp::backtrace::tracing::imp::unwind_backtrace
   1: std::sys_common::backtrace::_print
   2: std::panicking::default_hook::{{closure}}
   3: std::panicking::default_hook
   4: std::panicking::rust_panic_with_hook
   5: std::panicking::begin_panic
   (~~~~ LINES REMOVED BY ME FOR BREVITY ~~~~)
  32: rustc_typeck::check_crate
  33: <std::thread::local::LocalKey<T>>::with
  34: <std::thread::local::LocalKey<T>>::with
  35: rustc::ty::context::TyCtxt::create_and_enter
  36: rustc_driver::driver::compile_input
  37: rustc_driver::run_compiler
```

If you set `debug = true`, you will get line numbers for the stack trace.
Then the backtrace will look like this:

```text
stack backtrace:
   (~~~~ LINES REMOVED BY ME FOR BREVITY ~~~~)
             at /home/user/rust/compiler/rustc_typeck/src/check/cast.rs:110
   7: rustc_typeck::check::cast::CastCheck::check
             at /home/user/rust/compiler/rustc_typeck/src/check/cast.rs:572
             at /home/user/rust/compiler/rustc_typeck/src/check/cast.rs:460
             at /home/user/rust/compiler/rustc_typeck/src/check/cast.rs:370
   (~~~~ LINES REMOVED BY ME FOR BREVITY ~~~~)
  33: rustc_driver::driver::compile_input
             at /home/user/rust/compiler/rustc_driver/src/driver.rs:1010
             at /home/user/rust/compiler/rustc_driver/src/driver.rs:212
  34: rustc_driver::run_compiler
             at /home/user/rust/compiler/rustc_driver/src/lib.rs:253
```

## `-Z` flags

The compiler has a bunch of `-Z *` flags.
These are unstable flags that are only enabled on nightly.
Many of them are useful for debugging.
To get a full listing of `-Z` flags, use `-Z help`.

One useful flag is `-Z verbose-internals`, which generally enables printing more
info that could be useful for debugging.

Right below you can find elaborate explainers on a selected few.

### Getting a backtrace for errors
[getting-a-backtrace-for-errors]: #getting-a-backtrace-for-errors

If you want to get a backtrace to the point where the compiler emits an
error message, you can pass the `-Z treat-err-as-bug=n`, which will make
the compiler panic on the `nth` error.
If you leave off `=n`, the compiler will
assume `1` for `n` and thus panic on the first error it encounters.

For example:

```bash
$ cat error.rs
```

```rust
fn main() {
    1 + ();
}
```

```
$ rustc +stage1 error.rs
error[E0277]: cannot add `()` to `{integer}`
 --> error.rs:2:7
  |
2 |       1 + ();
  |         ^ no implementation for `{integer} + ()`
  |
  = help: the trait `Add<()>` is not implemented for `{integer}`

error: aborting due to previous error
```

Now, where does the error above come from?

```
$ RUST_BACKTRACE=1 rustc +stage1 error.rs -Z treat-err-as-bug
error[E0277]: the trait bound `{integer}: std::ops::Add<()>` is not satisfied
 --> error.rs:2:7
  |
2 |     1 + ();
  |       ^ no implementation for `{integer} + ()`
  |
  = help: the trait `std::ops::Add<()>` is not implemented for `{integer}`

error: internal compiler error: unexpected panic

note: the compiler unexpectedly panicked. this is a bug.

note: we would appreciate a bug report: https://github.com/rust-lang/rust/blob/HEAD/CONTRIBUTING.md#bug-reports

note: rustc 1.24.0-dev running on x86_64-unknown-linux-gnu

note: run with `RUST_BACKTRACE=1` for a backtrace

thread 'rustc' panicked at 'encountered error with `-Z treat_err_as_bug',
/home/user/rust/compiler/rustc_errors/src/lib.rs:411:12
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose
backtrace.
stack backtrace:
  (~~~ IRRELEVANT PART OF BACKTRACE REMOVED BY ME ~~~)
   7: rustc::traits::error_reporting::<impl rustc::infer::InferCtxt<'a, 'tcx>>
             ::report_selection_error
             at /home/user/rust/compiler/rustc_middle/src/traits/error_reporting.rs:823
   8: rustc::traits::error_reporting::<impl rustc::infer::InferCtxt<'a, 'tcx>>
             ::report_fulfillment_errors
             at /home/user/rust/compiler/rustc_middle/src/traits/error_reporting.rs:160
             at /home/user/rust/compiler/rustc_middle/src/traits/error_reporting.rs:112
   9: rustc_typeck::check::FnCtxt::select_obligations_where_possible
             at /home/user/rust/compiler/rustc_typeck/src/check/mod.rs:2192
  (~~~ IRRELEVANT PART OF BACKTRACE REMOVED BY ME ~~~)
  36: rustc_driver::run_compiler
             at /home/user/rust/compiler/rustc_driver/src/lib.rs:253
```

Cool, now I have a backtrace for the error!

### Debugging delayed bugs

The `-Z eagerly-emit-delayed-bugs` option makes it easy to debug delayed bugs.
It turns them into normal errors, i.e. makes them visible. This can be used in
combination with `-Z treat-err-as-bug` to stop at a particular delayed bug and get a backtrace.

### Getting the error creation location

`-Z track-diagnostics` can help figure out where errors are emitted.
It uses `#[track_caller]` for this and prints its location alongside the error:

```
$ RUST_BACKTRACE=1 rustc +stage1 error.rs -Z track-diagnostics
error[E0277]: cannot add `()` to `{integer}`
 --> src\error.rs:2:7
  |
2 |     1 + ();
  |       ^ no implementation for `{integer} + ()`
-Ztrack-diagnostics: created at compiler/rustc_trait_selection/src/traits/error_reporting/mod.rs:638:39
  |
  = help: the trait `Add<()>` is not implemented for `{integer}`
  = help: the following other types implement trait `Add<Rhs>`:
            <&'a f32 as Add<f32>>
            <&'a f64 as Add<f64>>
            <&'a i128 as Add<i128>>
            <&'a i16 as Add<i16>>
            <&'a i32 as Add<i32>>
            <&'a i64 as Add<i64>>
            <&'a i8 as Add<i8>>
            <&'a isize as Add<isize>>
          and 48 others

For more information about this error, try `rustc --explain E0277`.
```

This is similar but different to `-Z treat-err-as-bug`:
- it will print the locations for all errors emitted
- it does not require a compiler built with debug symbols
- you don't have to read through a big stack trace.

## Getting logging output

The compiler uses the [`tracing`] crate for logging.

[`tracing`]: https://docs.rs/tracing

For details see [the guide section on tracing](./tracing.md)

## Narrowing (Bisecting) Regressions

The [cargo-bisect-rustc][bisect] tool can be used as a quick and easy way to
find exactly which PR caused a change in `rustc` behavior.
It automatically downloads `rustc` PR artifacts and tests them against a project you provide
until it finds the regression.
You can then look at the PR to get more context on *why* it was changed.
 See [this tutorial][bisect-tutorial] on how to use it.

[bisect]: https://github.com/rust-lang/cargo-bisect-rustc
[bisect-tutorial]: https://rust-lang.github.io/cargo-bisect-rustc/tutorial.html

## Downloading Artifacts from Rust's CI

The [rustup-toolchain-install-master][rtim] tool by kennytm can be used to
download the artifacts produced by Rust's CI for a specific SHA1 -- this
basically corresponds to the successful landing of some PR -- and then sets
them up for your local use.
This also works for artifacts produced by `@bors try`.
This is helpful when you want to examine the resulting build of a PR
without doing the build yourself.

[rtim]: https://github.com/kennytm/rustup-toolchain-install-master

## `#[rustc_*]` TEST attributes

The compiler defines a whole lot of internal (perma-unstable) attributes some of which are useful
for debugging by dumping extra compiler-internal information.
These are prefixed with `rustc_` and
are gated behind the internal feature `rustc_attrs` (enabled via e.g. `#![feature(rustc_attrs)]`).

For a complete and up to date list, see [`builtin_attrs`].
More specifically, the ones marked `TEST`.
Here are some notable ones:

| Attribute | Description |
|----------------|-------------|
| `rustc_dump_def_parents` | Dumps the chain of `DefId` parents of certain definitions. |
| `rustc_dump_def_path` | Dumps the [`def_path_str`] of an item. |
| `rustc_dump_hidden_type_of_opaques` | Dumps the [hidden type of each opaque types][opaq] in the crate. |
| `rustc_dump_inferred_outlives` | Dumps implied bounds of an item. More precisely, the [`inferred_outlives_of`] an item. |
| `rustc_dump_item_bounds` | Dumps the [`item_bounds`] of an item. |
| `rustc_dump_layout` | [See this section](#debugging-type-layouts). |
| `rustc_dump_object_lifetime_defaults` | Dumps the [object lifetime defaults] of an item. |
| `rustc_dump_predicates` | Dumps the [`predicates_of`] an item. |
| `rustc_dump_symbol_name` | Dumps the mangled & demangled [`symbol_name`] of an item. |
| `rustc_dump_variances` | Dumps the [variances] of an item. |
| `rustc_dump_vtable` | Dumps the vtable layout of an impl, or a type alias of a dyn type. |
| `rustc_regions` | Dumps NLL closure region requirements. |

Right below you can find elaborate explainers on a selected few.

[`builtin_attrs`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_feature/src/builtin_attrs.rs
[`def_path_str`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.def_path_str
[`inferred_outlives_of`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.inferred_outlives_of
[`item_bounds`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.item_bounds
[`predicates_of`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.predicates_of
[`symbol_name`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.symbol_name
[object lifetime defaults]: https://doc.rust-lang.org/reference/lifetime-elision.html#default-trait-object-lifetimes
[opaq]: ./opaque-types-impl-trait-inference.md
[variances]: ./variance.md

### Formatting Graphviz output (.dot files)
[formatting-graphviz-output]: #formatting-graphviz-output

Some compiler options for debugging specific features yield graphviz graphs -
e.g. the `#[rustc_mir(borrowck_graphviz_postflow="suffix.dot")]` attribute
on a function dumps various borrow-checker dataflow graphs in conjunction with
`-Zdump-mir-dataflow`.

These all produce `.dot` files. To view these files, install graphviz (e.g.
`apt-get install graphviz`) and then run the following commands:

```bash
$ dot -T pdf maybe_init_suffix.dot > maybe_init_suffix.pdf
$ firefox maybe_init_suffix.pdf # Or your favorite pdf viewer
```

### Debugging type layouts

The internal attribute `#[rustc_dump_layout(...)]` can be used to dump the
[`Layout`] of the type it is attached to.
For example:

```rust
#![feature(rustc_attrs)]

#[rustc_dump_layout(debug)]
type T<'a> = &'a u32;
```

Will emit the following:

```text
error: layout_of(&u32) = Layout {
           size: Size(8 bytes),
           align: AbiAlign {
               abi: Align(8 bytes),
           },
           backend_repr: Scalar(
               Initialized {
                   value: Pointer(
                       AddressSpace(
                           0,
                       ),
                   ),
                   valid_range: 1..=18446744073709551615,
               },
           ),
           fields: Primitive,
           largest_niche: Some(
               Niche {
                   offset: Size(0 bytes),
                   value: Pointer(
                       AddressSpace(
                           0,
                       ),
                   ),
                   valid_range: 1..=18446744073709551615,
               },
           ),
           uninhabited: false,
           variants: Single {
               index: 0,
           },
           max_repr_align: None,
           unadjusted_abi_align: Align(8 bytes),
           randomization_seed: 281492156579847,
       }
 --> src/lib.rs:4:1
  |
4 | type T<'a> = &'a u32;
  | ^^^^^^^^^^^^^^^^^^^^^

error: aborting due to previous error
```

[`Layout`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_public/abi/struct.Layout.html


## Configuring CodeLLDB for debugging `rustc`

If you are using VSCode, and have edited your `bootstrap.toml` to request debugging
level 1 or 2 for the parts of the code you're interested in, then you should be
able to use the [CodeLLDB] extension in VSCode to debug it.

Here is a sample `launch.json` file, being used to run a stage 1 compiler direct
from the directory where it is built (does not have to be "installed"):

```javascript
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
      {
        "type": "lldb",
        "request": "launch",
        "name": "Launch",
        "args": [],  // array of string command-line arguments to pass to compiler
        "program": "${workspaceFolder}/build/host/stage1/bin/rustc",
        "windows": {  // applicable if using windows
            "program": "${workspaceFolder}/build/host/stage1/bin/rustc.exe"
        },
        "cwd": "${workspaceFolder}",  // current working directory at program start
        "stopOnEntry": false,
        "sourceLanguages": ["rust"]
      }
    ]
  }
```

[CodeLLDB]: https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb


---

# Using tracing to debug the compiler

The compiler has a lot of [`debug!`] (or `trace!`) calls, which print out logging information
at many points.
These are very useful to at least narrow down the location of
a bug if not to find it entirely, or just to orient yourself as to why the
compiler is doing a particular thing.

[`debug!`]: https://docs.rs/tracing/0.1/tracing/macro.debug.html

To see the logs, you need to set the `RUSTC_LOG` environment variable to your log filter.
The full syntax of the log filters can be found in the [rustdoc
of `tracing-subscriber`](https://docs.rs/tracing-subscriber/0.2.24/tracing_subscriber/filter/struct.EnvFilter.html#directives).

## Environment variables

This is an overview of the environment variables rustc accepts to customize its tracing output.
The definition of these can mostly be found in `compiler/rustc_log/src/lib.rs`.

|  Name                     | Usage                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `RUSTC_LOG`               | Tracing filters (see the rest of this page)                                                                             |
| `RUSTC_LOG_COLOR`         | `always`, `never` or `auto`.                                                                                            |
| `RUSTC_LOG_ENTRY_EXIT`    | if set and not '0', log span entry/exit.                                                                                |
| `RUSTC_LOG_THREAD_IDS`    | if set and equal to '1', also log thread ids.                                                                           |
| `RUSTC_LOG_BACKTRACE`     | Capture and print a backtrace if a trace is emitted with a target that matches the provided string value.               |
| `RUSTC_LOG_LINES`         | If `1`, indents log lines based on depth.                                                                               |
| `RUSTC_LOG_FORMAT_JSON`   | If `1`, outputs logs as JSON. The exact parameters can be found in `rustc_log/src/lib.rs` but the format is *UNSTABLE*. |
| `RUSTC_LOG_OUTPUT_TARGET` | If provided, logs go to the provided file name instead of stderr.                                                       |




## Function level filters

Lots of functions in rustc are annotated with

```
#[instrument(level = "debug", skip(self))]
fn foo(&self, bar: Type) {}
```

which allows you to use

```
RUSTC_LOG=[foo]
```

to do the following all at once

* log all function calls to `foo`
* log the arguments (except for those in the `skip` list)
* log everything (from anywhere else in the compiler) until the function returns

### I don't want everything

Depending on the scope of the function, you may not want to log everything in its body.
As an example: the `do_mir_borrowck` function will dump hundreds of lines even for trivial
code being borrowchecked.

Since you can combine all filters, you can add a crate/module path, e.g.

```
RUSTC_LOG=rustc_borrowck[do_mir_borrowck]
```

### I don't want all calls

If you are compiling libcore, you likely don't want *all* borrowck dumps, but only one
for a specific function.
You can filter function calls by their arguments by regexing them.

```
RUSTC_LOG=[do_mir_borrowck{id=\.\*from_utf8_unchecked\.\*}]
```

will only give you the logs of borrowchecking `from_utf8_unchecked`.
Note that you will
still get a short message per ignored `do_mir_borrowck`, but none of the things inside those calls.
This helps you in looking through the calls that are happening and helps you adjust
your regex if you mistyped it.

## Query level filters

Every [query](query.md) is automatically tagged with a logging span so that
you can display all log messages during the execution of the query.
For example, if you want to log everything during type checking:

```
RUSTC_LOG=[typeck]
```

The query arguments are included as a tracing field which means that you can
filter on the debug display of the arguments.
For example, the `typeck` query has an argument `key: LocalDefId` of what is being checked.
You can use a regex to match on that `LocalDefId` to log type checking for a specific function:

```
RUSTC_LOG=[typeck{key=.*name_of_item.*}]
```

Different queries have different arguments.
You can find a list of queries and their arguments in
[`rustc_middle/src/query/mod.rs`](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_middle/src/query/mod.rs#L18).

## Broad module level filters

You can also use filters similar to the `log` crate's filters, which will enable
everything within a specific module.
This is often too verbose and too unstructured,
so it is recommended to use function level filters.

Your log filter can be just `debug` to get all `debug!` output and
higher (e.g., it will also include `info!`), or `path::to::module` to get *all*
output (which will include `trace!`) from a particular module, or
`path::to::module=debug` to get `debug!` output and higher from a particular module.

For example, to get the `debug!` output and higher for a specific module, you
can run the compiler with `RUSTC_LOG=path::to::module=debug rustc my-file.rs`.
All `debug!` output will then appear in standard error.

Note that you can use a partial path and the filter will still work.
For example, if you want to see `info!` output from only
`rustdoc::passes::collect_intra_doc_links`, you could use
`RUSTDOC_LOG=rustdoc::passes::collect_intra_doc_links=info` *or* you could use
`RUSTDOC_LOG=rustdoc::passes::collect_intra=info`.

If you are developing rustdoc, use `RUSTDOC_LOG` instead.
If you are developing Miri, use `MIRI_LOG` instead.
You get the idea :)

See the [`tracing`] crate's docs, and specifically the docs for [`debug!`] to
see the full syntax you can use.
(Note: unlike the compiler, the [`tracing`]
crate and its examples use the `RUSTC_LOG` environment variable.
rustc, rustdoc,
and other tools set custom environment variables.)

**Note that unless you use a very strict filter, the logger will emit a lot of
output, so use the most specific module(s) you can (comma-separated if
multiple)**. It's typically a good idea to pipe standard error to a file and
look at the log output with a text editor.

So, to put it together:

```bash
# This puts the output of all debug calls in `rustc_middle/src/traits` into
# standard error, which might fill your console backscroll.
$ RUSTC_LOG=rustc_middle::traits=debug rustc +stage1 my-file.rs

# This puts the output of all debug calls in `rustc_middle/src/traits` in
# `traits-log`, so you can then see it with a text editor.
$ RUSTC_LOG=rustc_middle::traits=debug rustc +stage1 my-file.rs 2>traits-log

# Not recommended! This will show the output of all `debug!` calls
# in the Rust compiler, and there are a *lot* of them, so it will be
# hard to find anything.
$ RUSTC_LOG=debug rustc +stage1 my-file.rs 2>all-log

# This will show the output of all `info!` calls in `rustc_codegen_ssa`.
#
# There's an `info!` statement in `codegen_instance` that outputs
# every function that is codegen'd. This is useful to find out
# which function triggers an LLVM assertion, and this is an `info!`
# log rather than a `debug!` log so it will work on the official
# compilers.
$ RUSTC_LOG=rustc_codegen_ssa=info rustc +stage1 my-file.rs

# This will show all logs in `rustc_codegen_ssa` and `rustc_resolve`.
$ RUSTC_LOG=rustc_codegen_ssa,rustc_resolve rustc +stage1 my-file.rs

# This will show the output of all `info!` calls made by rustdoc
# or any rustc library it calls.
$ RUSTDOC_LOG=info rustdoc +stage1 my-file.rs

# This will only show `debug!` calls made by rustdoc directly,
# not any `rustc*` crate.
$ RUSTDOC_LOG=rustdoc=debug rustdoc +stage1 my-file.rs
```

## Log colors

By default, rustc (and other tools, like rustdoc and Miri) will be smart about
when to use ANSI colors in the log output.
If they are outputting to a terminal,
they will use colors, and if they are outputting to a file or being piped
somewhere else, they will not.
However, it's hard to read log output in your
terminal unless you have a very strict filter, so you may want to pipe the
output to a pager like `less`.
But then there won't be any colors, which makes it hard to pick out what you're looking for!

You can override whether to have colors in log output with the `RUSTC_LOG_COLOR`
environment variable (or `RUSTDOC_LOG_COLOR` for rustdoc, or `MIRI_LOG_COLOR`
for Miri, etc.). There are three options: `auto` (the default), `always`, and
`never`.
So, if you want to enable colors when piping to `less`, use something similar to this command:

```bash
# The `-R` switch tells less to print ANSI colors without escaping them.
$ RUSTC_LOG=debug RUSTC_LOG_COLOR=always rustc +stage1 ... | less -R
```

Note that `MIRI_LOG_COLOR` will only color logs that come from Miri, not logs
from rustc functions that Miri calls.
Use `RUSTC_LOG_COLOR` to color logs from rustc.

## How to keep or remove `debug!` and `trace!` calls from the resulting binary

While calls to `error!`, `warn!` and `info!` are included in every build of the compiler,
calls to `debug!` and `trace!` are only included in the program if
`rust.debug-logging=true` is turned on in bootstrap.toml (it is
turned off by default), so if you don't see `DEBUG` logs, especially
if you run the compiler with `RUSTC_LOG=rustc rustc some.rs` and only see
`INFO` logs, make sure that `rust.debug-logging=true` is turned on in your bootstrap.toml.

## Logging etiquette and conventions

Because calls to `debug!` are removed by default, in most cases, don't worry
about the performance of adding "unnecessary" calls to `debug!` and leaving them in code you
commit - they won't slow down the performance of what we ship.

That said, there can also be excessive tracing calls, especially
when they are redundant with other calls nearby or in functions called from here.
There is no perfect balance to hit here, and it is left to the reviewer's
discretion to decide whether to let you leave `debug!` statements in, or whether to ask
you to remove them before merging.

It may be preferable to use `trace!` over `debug!` for very noisy logs.

A loosely followed convention is to use `#[instrument(level = "debug")]`
([also see the attribute's documentation](https://docs.rs/tracing-attributes/0.1.17/tracing_attributes/attr.instrument.html))
in favour of `debug!("foo(...)")` at the start of a function `foo`.
Within functions, prefer `debug!(?variable.field)` over `debug!("xyz = {:?}", variable.field)`
and `debug!(bar = ?var.method(arg))` over `debug!("bar = {:?}", var.method(arg))`.
The documentation for this syntax can be found [here](https://docs.rs/tracing/0.1.28/tracing/#recording-fields).

One thing to be **careful** of is **expensive** operations in logs.

If in the module `rustc::foo` you have a statement

```Rust
debug!(x = ?random_operation(tcx));
```

Then if someone runs a debug `rustc` with `RUSTC_LOG=rustc::foo`, then
`random_operation()` will run.
`RUSTC_LOG` filters that do not enable this debug statement will not execute `random_operation`.

This means that you should not put anything too expensive or likely to crash
there - that would annoy anyone who wants to use logging for that module.
No-one will know it until someone tries to use logging to find *another* bug.

[`tracing`]: https://docs.rs/tracing


---

# Profiling the compiler

This section talks about how to profile the compiler and find out where it spends its time.

Depending on what you're trying to measure, there are several different approaches:

- If you want to see if a PR improves or regresses compiler performance,
  see the [rustc-perf chapter](tests/perf.md) for requesting a benchmarking run.

- If you want a medium-to-high level overview of where `rustc` is spending its time:
  - The `-Z self-profile` flag and [measureme](https://github.com/rust-lang/measureme) tools offer a query-based approach to profiling.
    See [their docs](https://github.com/rust-lang/measureme/blob/master/summarize/README.md) for more information.

- If you want function level performance data or even just more details than the above approaches:
  - Consider using a native code profiler such as [perf](profiling/with-perf.md)
  - or [tracy](https://github.com/nagisa/rust_tracy_client) for a nanosecond-precision,
    full-featured graphical interface.

- If you want a nice visual representation of the compile times of your crate graph,
  you can use [cargo's `--timings` flag](https://doc.rust-lang.org/nightly/cargo/reference/timings.html),
  e.g. `cargo build --timings`.
  You can use this flag on the compiler itself with `CARGOFLAGS="--timings" ./x build`

- If you want to profile memory usage, you can use various tools depending on what operating system
  you are using.
  - For Windows, read our [WPA guide](profiling/wpa-profiling.md).

## Optimizing rustc's bootstrap times with `cargo-llvm-lines`

Using [cargo-llvm-lines](https://github.com/dtolnay/cargo-llvm-lines) you can count the
number of lines of LLVM IR across all instantiations of a generic function.
Since most of the time compiling rustc is spent in LLVM, the idea is that by
reducing the amount of code passed to LLVM, compiling rustc gets faster.

To use `cargo-llvm-lines` together with somewhat custom rustc build process, you can use
`-C save-temps` to obtain required LLVM IR.
The option preserves temporary work products created during compilation.
Among those is LLVM IR that represents an input to the
optimization pipeline; ideal for our purposes.
It is stored in files with `*.no-opt.bc` extension in LLVM bitcode format.

Example usage:
```
cargo install cargo-llvm-lines
# On a normal crate you could now run `cargo llvm-lines`, but `x` isn't normal :P

# Do a clean before every run, to not mix in the results from previous runs.
./x clean
env RUSTFLAGS=-Csave-temps ./x build --stage 0 compiler/rustc

# Single crate, e.g., rustc_middle. (Relies on the glob support of your shell.)
# Convert unoptimized LLVM bitcode into a human readable LLVM assembly accepted by cargo-llvm-lines.
for f in build/x86_64-unknown-linux-gnu/stage0-rustc/x86_64-unknown-linux-gnu/release/deps/rustc_middle-*.no-opt.bc; do
  ./build/x86_64-unknown-linux-gnu/llvm/bin/llvm-dis "$f"
done
cargo llvm-lines --files ./build/x86_64-unknown-linux-gnu/stage0-rustc/x86_64-unknown-linux-gnu/release/deps/rustc_middle-*.ll > llvm-lines-middle.txt

# Specify all crates of the compiler.
for f in build/x86_64-unknown-linux-gnu/stage0-rustc/x86_64-unknown-linux-gnu/release/deps/*.no-opt.bc; do
  ./build/x86_64-unknown-linux-gnu/llvm/bin/llvm-dis "$f"
done
cargo llvm-lines --files ./build/x86_64-unknown-linux-gnu/stage0-rustc/x86_64-unknown-linux-gnu/release/deps/*.ll > llvm-lines.txt
```

Example output for the compiler:
```
  Lines            Copies          Function name
  -----            ------          -------------
  45207720 (100%)  1583774 (100%)  (TOTAL)
   2102350 (4.7%)   146650 (9.3%)  core::ptr::drop_in_place
    615080 (1.4%)     8392 (0.5%)  std::thread::local::LocalKey<T>::try_with
    594296 (1.3%)     1780 (0.1%)  hashbrown::raw::RawTable<T>::rehash_in_place
    592071 (1.3%)     9691 (0.6%)  core::option::Option<T>::map
    528172 (1.2%)     5741 (0.4%)  core::alloc::layout::Layout::array
    466854 (1.0%)     8863 (0.6%)  core::ptr::swap_nonoverlapping_one
    412736 (0.9%)     1780 (0.1%)  hashbrown::raw::RawTable<T>::resize
    367776 (0.8%)     2554 (0.2%)  alloc::raw_vec::RawVec<T,A>::grow_amortized
    367507 (0.8%)      643 (0.0%)  rustc_query_system::dep_graph::graph::DepGraph<K>::with_task_impl
    355882 (0.8%)     6332 (0.4%)  alloc::alloc::box_free
    354556 (0.8%)    14213 (0.9%)  core::ptr::write
    354361 (0.8%)     3590 (0.2%)  core::iter::traits::iterator::Iterator::fold
    347761 (0.8%)     3873 (0.2%)  rustc_middle::ty::context::tls::set_tlv
    337534 (0.7%)     2377 (0.2%)  alloc::raw_vec::RawVec<T,A>::allocate_in
    331690 (0.7%)     3192 (0.2%)  hashbrown::raw::RawTable<T>::find
    328756 (0.7%)     3978 (0.3%)  rustc_middle::ty::context::tls::with_context_opt
    326903 (0.7%)      642 (0.0%)  rustc_query_system::query::plumbing::try_execute_query
```

Since this doesn't seem to work with incremental compilation or `./x check`,
you will be compiling rustc _a lot_.
I recommend changing a few settings in `bootstrap.toml` to make it bearable:
```
# A debug build takes _a third_ as long on my machine,
# but compiling more than stage0 rustc becomes unbearably slow.
rust.optimize = false

# We can't use incremental anyway, so we disable it for a little speed boost.
rust.incremental = false
# We won't be running it, so no point in compiling debug checks.
rust.debug = false

# Using a single codegen unit gives less output, but is slower to compile.
rust.codegen-units = 0  # num_cpus
```

The llvm-lines output is affected by several options.
`rust.optimize = false` increases it from 2.1GB to 3.5GB and `codegen-units = 0` to 4.1GB.

MIR optimizations have little impact.
Compared to the default `RUSTFLAGS="-Z
mir-opt-level=1"`, level 0 adds 0.3GB and level 2 removes 0.2GB.
As of <!-- date-check --> July 2022,
inlining happens in LLVM and GCC codegen backends,
missing only in the Cranelift one.


---

# Profiling with perf

This is a guide for how to profile rustc with [perf](https://perf.wiki.kernel.org/index.php/Main_Page).

## Initial steps

- Get a clean checkout of rust-lang/rust
- Set the following settings in your `bootstrap.toml`:
  - `rust.debuginfo-level = 1` - enables line debuginfo
  - `rust.jemalloc = false` - lets you do memory use profiling with valgrind
  - leave everything else the defaults
- Run `./x build` to get a full build
- Make a rustup toolchain pointing to that result
  - see [the "build and run" section for instructions][b-a-r]

[b-a-r]: ../building/how-to-build-and-run.html#toolchain

## Gathering a perf profile

perf is an excellent tool on linux that can be used to gather and
analyze all kinds of information. Mostly it is used to figure out
where a program spends its time. It can also be used for other sorts
of events, though, like cache misses and so forth.

### The basics

The basic `perf` command is this:

```bash
perf record -F99 --call-graph dwarf XXX
```

The `-F99` tells perf to sample at 99 Hz, which avoids generating too
much data for longer runs (why 99 Hz you ask? It is often chosen
because it is unlikely to be in lockstep with other periodic
activity). The `--call-graph dwarf` tells perf to get call-graph
information from debuginfo, which is accurate. The `XXX` is the
command you want to profile. So, for example, you might do:

```bash
perf record -F99 --call-graph dwarf cargo +<toolchain> rustc
```

to run `cargo` -- here `<toolchain>` should be the name of the toolchain
you made in the beginning. But there are some things to be aware of:

- You probably don't want to profile the time spend building
  dependencies. So something like `cargo build; cargo clean -p $C` may
  be helpful (where `$C` is the crate name)
    - Though usually I just do `touch src/lib.rs` and rebuild instead. =)
- You probably don't want incremental messing about with your
  profile. So something like `CARGO_INCREMENTAL=0` can be helpful.

In case to avoid the issue of `addr2line xxx/elf: could not read first record` when reading
collected data from `cargo`, you may need use the latest version of `addr2line`:

```bash
cargo install addr2line --features="bin"
```

### Gathering a perf profile from a `perf.rust-lang.org` test

Often we want to analyze a specific test from `perf.rust-lang.org`.
The easiest way to do that is to use the [rustc-perf][rustc-perf]
benchmarking suite, this approach is described [here](with-rustc-perf.md).

Instead of using the benchmark suite CLI, you can also profile the benchmarks manually. First,
you need to clone the [rustc-perf][rustc-perf] repository:

```bash
$ git clone https://github.com/rust-lang/rustc-perf
```

and then find the source code of the test that you want to profile. Sources for the tests
are found in [the `collector/compile-benchmarks` directory][compile-time dir]
and [the `collector/runtime-benchmarks` directory][runtime dir]. So let's
go into the directory of a specific test; we'll use `clap-rs` as an example:

[rustc-perf]: https://github.com/rust-lang/rustc-perf
[compile-time dir]: https://github.com/rust-lang/rustc-perf/tree/master/collector/compile-benchmarks
[runtime dir]: https://github.com/rust-lang/rustc-perf/tree/master/collector/runtime-benchmarks

```bash
cd collector/compile-benchmarks/clap-3.1.6
```

In this case, let's say we want to profile the `cargo check`
performance. In that case, I would first run some basic commands to
build the dependencies:

```bash
# Setup: first clean out any old results and build the dependencies:
cargo +<toolchain> clean
CARGO_INCREMENTAL=0 cargo +<toolchain> check
```

(Again, `<toolchain>` should be replaced with the name of the
toolchain we made in the first step.)

Next: we want record the execution time for *just* the clap-rs crate,
running cargo check. I tend to use `cargo rustc` for this, since it
also allows me to add explicit flags, which we'll do later on.

```bash
touch src/lib.rs
CARGO_INCREMENTAL=0 perf record -F99 --call-graph dwarf cargo rustc --profile check --lib
```

Note that final command: it's a doozy! It uses the `cargo rustc`
command, which executes rustc with (potentially) additional options;
the `--profile check` and `--lib` options specify that we are doing a
`cargo check` execution, and that this is a library (not a binary).

At this point, we can use `perf` tooling to analyze the results. For example:

```bash
perf report
```

will open up an interactive TUI program. In simple cases, that can be
helpful. For more detailed examination, the [`perf-focus` tool][pf]
can be helpful; it is covered below.

**A note of caution.** Each of the rustc-perf tests is its own special
  snowflake. In particular, some of them are not libraries, in which
  case you would want to do `touch src/main.rs` and avoid passing
  `--lib`. I'm not sure how best to tell which test is which to be
  honest.

### Gathering NLL data

If you want to profile an NLL run, you can just pass extra options to
the `cargo rustc` command, like so:

```bash
touch src/lib.rs
CARGO_INCREMENTAL=0 perf record -F99 --call-graph dwarf cargo rustc --profile check --lib -- -Z borrowck=mir
```

[pf]: https://github.com/nikomatsakis/perf-focus

## Analyzing a perf profile with `perf focus`

Once you've gathered a perf profile, we want to get some information
about it. For this, I personally use [perf focus][pf]. It's a kind of
simple but useful tool that lets you answer queries like:

- "how much time was spent in function F" (no matter where it was called from)
- "how much time was spent in function F when it was called from G"
- "how much time was spent in function F *excluding* time spent in G"
- "what functions does F call and how much time does it spend in them"

To understand how it works, you have to know just a bit about
perf. Basically, perf works by *sampling* your process on a regular
basis (or whenever some event occurs). For each sample, perf gathers a
backtrace. `perf focus` lets you write a regular expression that tests
which functions appear in that backtrace, and then tells you which
percentage of samples had a backtrace that met the regular
expression. It's probably easiest to explain by walking through how I
would analyze NLL performance.

### Installing `perf-focus`

You can install perf-focus using `cargo install`:

```bash
cargo install perf-focus
```

### Example: How much time is spent in MIR borrowck?

Let's say we've gathered the NLL data for a test. We'd like to know
how much time it is spending in the MIR borrow-checker. The "main"
function of the MIR borrowck is called `do_mir_borrowck`, so we can do
this command:

```bash
$ perf focus '{do_mir_borrowck}'
Matcher    : {do_mir_borrowck}
Matches    : 228
Not Matches: 542
Percentage : 29%
```

The `'{do_mir_borrowck}'` argument is called the **matcher**. It
specifies the test to be applied on the backtrace. In this case, the
`{X}` indicates that there must be *some* function on the backtrace
that meets the regular expression `X`. In this case, that regex is
just the name of the function we want (in fact, it's a subset of the name;
the full name includes a bunch of other stuff, like the module
path). In this mode, perf-focus just prints out the percentage of
samples where `do_mir_borrowck` was on the stack: in this case, 29%.

**A note about c++filt.** To get the data from `perf`, `perf focus`
  currently executes `perf script` (perhaps there is a better
  way...). I've sometimes found that `perf script` outputs C++ mangled
  names. This is annoying. You can tell by running `perf script |
  head` yourself — if you see names like `5rustc6middle` instead of
  `rustc::middle`, then you have the same problem. You can solve this
  by doing:

```bash
perf script | c++filt | perf focus --from-stdin ...
```

This will pipe the output from `perf script` through `c++filt` and
should mostly convert those names into a more friendly format. The
`--from-stdin` flag to `perf focus` tells it to get its data from
stdin, rather than executing `perf focus`. We should make this more
convenient (at worst, maybe add a `c++filt` option to `perf focus`, or
just always use it — it's pretty harmless).

### Example: How much time does MIR borrowck spend solving traits?

Perhaps we'd like to know how much time MIR borrowck spends in the
trait checker. We can ask this using a more complex regex:

```bash
$ perf focus '{do_mir_borrowck}..{^rustc::traits}'
Matcher    : {do_mir_borrowck},..{^rustc::traits}
Matches    : 12
Not Matches: 1311
Percentage : 0%
```

Here we used the `..` operator to ask "how often do we have
`do_mir_borrowck` on the stack and then, later, some function whose
name begins with `rustc::traits`?" (basically, code in that module). It
turns out the answer is "almost never" — only 12 samples fit that
description (if you ever see *no* samples, that often indicates your
query is messed up).

If you're curious, you can find out exactly which samples by using the
`--print-match` option. This will print out the full backtrace for
each sample. The `|` at the front of the line indicates the part that
the regular expression matched.

### Example: Where does MIR borrowck spend its time?

Often we want to do more "explorational" queries. Like, we know that
MIR borrowck is 29% of the time, but where does that time get spent?
For that, the `--tree-callees` option is often the best tool. You
usually also want to give `--tree-min-percent` or
`--tree-max-depth`. The result looks like this:

```bash
$ perf focus '{do_mir_borrowck}' --tree-callees --tree-min-percent 3
Matcher    : {do_mir_borrowck}
Matches    : 577
Not Matches: 746
Percentage : 43%

Tree
| matched `{do_mir_borrowck}` (43% total, 0% self)
: | rustc_borrowck::nll::compute_regions (20% total, 0% self)
: : | rustc_borrowck::nll::type_check::type_check_internal (13% total, 0% self)
: : : | core::ops::function::FnOnce::call_once (5% total, 0% self)
: : : : | rustc_borrowck::nll::type_check::liveness::generate (5% total, 3% self)
: : : | <rustc_borrowck::nll::type_check::TypeVerifier<'a, 'b, 'tcx> as rustc::mir::visit::Visitor<'tcx>>::visit_mir (3% total, 0% self)
: | rustc::mir::visit::Visitor::visit_mir (8% total, 6% self)
: | <rustc_borrowck::MirBorrowckCtxt<'cx, 'tcx> as rustc_mir_dataflow::DataflowResultsConsumer<'cx, 'tcx>>::visit_statement_entry (5% total, 0% self)
: | rustc_mir_dataflow::do_dataflow (3% total, 0% self)
```

What happens with `--tree-callees` is that

- we find each sample matching the regular expression
- we look at the code that occurs *after* the regex match and try
  to build up a call tree

The `--tree-min-percent 3` option says "only show me things that take
more than 3% of the time". Without this, the tree often gets really
noisy and includes random stuff like the innards of
malloc. `--tree-max-depth` can be useful too, it just limits how many
levels we print.

For each line, we display the percent of time in that function
altogether ("total") and the percent of time spent in **just that
function and not some callee of that function** (self). Usually
"total" is the more interesting number, but not always.

### Relative percentages

By default, all in perf-focus are relative to the **total program
execution**. This is useful to help you keep perspective — often as
we drill down to find hot spots, we can lose sight of the fact that,
in terms of overall program execution, this "hot spot" is actually not
important. It also ensures that percentages between different queries
are easily compared against one another.

That said, sometimes it's useful to get relative percentages, so `perf
focus` offers a `--relative` option. In this case, the percentages are
listed only for samples that match (vs all samples). So for example we
could get our percentages relative to the borrowck itself
like so:

```bash
$ perf focus '{do_mir_borrowck}' --tree-callees --relative --tree-max-depth 1 --tree-min-percent 5
Matcher    : {do_mir_borrowck}
Matches    : 577
Not Matches: 746
Percentage : 100%

Tree
| matched `{do_mir_borrowck}` (100% total, 0% self)
: | rustc_borrowck::nll::compute_regions (47% total, 0% self) [...]
: | rustc::mir::visit::Visitor::visit_mir (19% total, 15% self) [...]
: | <rustc_borrowck::MirBorrowckCtxt<'cx, 'tcx> as rustc_mir_dataflow::DataflowResultsConsumer<'cx, 'tcx>>::visit_statement_entry (13% total, 0% self) [...]
: | rustc_mir_dataflow::do_dataflow (8% total, 1% self) [...]
```

Here you see that `compute_regions` came up as "47% total" — that
means that 47% of `do_mir_borrowck` is spent in that function. Before,
we saw 20% — that's because `do_mir_borrowck` itself is only 43% of
the total time (and `.47 * .43 = .20`).


---

# Profiling on Windows

## Introducing WPR and WPA

High-level performance analysis (including memory usage) can be performed with the Windows
Performance Recorder (WPR) and Windows Performance Analyzer (WPA).
As the names suggest, WPR is for recording system statistics (in the form of event trace log a.k.a.
ETL files), while WPA is for analyzing these ETL files.

WPR collects system wide statistics, so it won't just record things relevant to rustc but also
everything else that's running on the machine.
During analysis, we can filter to just the things we find interesting.

These tools are quite powerful but also require a bit of learning
before we can successfully profile the Rust compiler.

Here we will explore how to use WPR and WPA for analyzing the Rust compiler as well as provide
links to useful "profiles" (i.e., settings files that tweak the defaults for WPR and WPA) that are
specifically designed to make analyzing rustc easier.

### Installing WPR and WPA

You can install WPR and WPA as part of the Windows Performance Toolkit which itself is an option as
part of downloading the Windows Assessment and Deployment Kit (ADK).
You can download the ADK
installer [here](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-install).
Make sure to select the Windows Performance Toolkit (you don't need to select anything else).

## Recording

In order to perform system analysis, you'll first need to record your system with WPR.
Open WPR and at the bottom of the window select the "profiles" of the things you want to record.
For looking
into memory usage of the rustc bootstrap process, we'll want to select the following items:

* CPU usage
* VirtualAlloc usage

You might be tempted to record "Heap usage" as well, but this records every single heap allocation
and can be very, very expensive.
For high-level analysis, it might be best to leave that turned off.

Now we need to get our setup ready to record.
For memory usage analysis, it is best to record the
stage 2 compiler build with a stage 1 compiler build with debug symbols.
Having symbols in the
compiler we're using to build rustc will aid our analysis greatly by allowing WPA to resolve Rust
symbols correctly.
Unfortunately, the stage 0 compiler does not have symbols turned on,
which is why we'll need to build a stage 1 compiler,
and then a stage 2 compiler ourselves.

To do this, make sure you have set `rust.debuginfo-level = 1` in your `bootstrap.toml` file.
This tells rustc to generate debug information which includes stack frames when bootstrapping.

Now you can build the stage 1 compiler: `x build --stage 1 -i library` or however
else you want to build the stage 1 compiler.

Now that the stage 1 compiler is built, we can record the stage 2 build.
Go back to WPR, click the
"start" button and build the stage 2 compiler (e.g., `x build --stage=2 -i library`).
When this process finishes, stop the recording.

Click the Save button and once that process is complete, click the "Open in WPA" button which
appears.

> Note: The trace file is fairly large so it can take WPA some time to finish opening the file.

## Analysis

Now that our ETL file is open in WPA, we can analyze the results.
First, we'll want to apply the
pre-made "profile" which will put WPA into a state conducive to analyzing rustc bootstrap.
Download
the profile [here](https://github.com/wesleywiser/rustc-bootstrap-wpa-analysis/releases/download/1/rustc.generic.wpaProfile).
Select the "Profiles" menu at the top, then "apply" and then choose the downloaded profile.

You should see something resembling the following:

![WPA with profile applied](../img/wpa-initial-memory.png)

Next, we will need to tell WPA to load and process debug symbols so that it can properly demangle
the Rust stack traces.
To do this, click "Trace" and then choose "Load Symbols".
This step can take a while.

Once WPA has loaded symbols for rustc, we can expand the rustc.exe node and begin drilling down
into the stack with the largest allocations.

To do that, we'll expand the `[Root]` node in the "Commit Stack" column and continue expanding
until we find interesting stack frames.

> Tip: After selecting the node you want to expand, press the right arrow key. This will expand the
node and put the selection on the next largest node in the expanded set.
You can continue pressing the right arrow key until you reach an interesting frame.

![WPA with expanded stack](../img/wpa-stack.png)

In this sample, you can see calls through codegen are allocating ~30gb of memory in total
throughout this profile.

## Other Analysis Tabs

The profile also includes a few other tabs which can be helpful:

- System Configuration
    - General information about the system the capture was recorded on.
- rustc Build Processes
    - A flat list of relevant processes such as rustc.exe, cargo.exe, link.exe etc.
    - Each process lists its command line arguments.
    - Useful for figuring out what a specific rustc process was working on.
- rustc Build Process Tree
    - Timeline showing when processes started and exited.
- rustc CPU Analysis
    - Contains charts preconfigured to show hotspots in rustc.
    - These charts are designed to support analyzing where rustc is spending its time.
- rustc Memory Analysis
    - Contains charts preconfigured to show where rustc is allocating memory.


---

# Profiling with rustc-perf

The [Rust benchmark suite][rustc-perf] provides a comprehensive way of profiling and benchmarking
the Rust compiler.
You can find instructions on how to use the suite in its [manual][rustc-perf-readme].

However, using the suite manually can be a bit cumbersome.
To make this easier for `rustc` contributors,
the compiler build system (`bootstrap`) also provides built-in integration with the benchmarking suite,
which will download and build the suite for you, build a local compiler toolchain and let you profile it using a simplified command-line interface.

You can use the `./x perf <command> [options]` command to use this integration.

You can use normal bootstrap flags for this command, such as `--stage 1` or `--stage 2`, for example to modify the stage of the created sysroot. It might also be useful to configure `bootstrap.toml` to better support profiling, e.g. set `rust.debuginfo-level = 1` to add source line information to the built compiler.

`x perf` currently supports the following commands:
- `benchmark <id>`: Benchmark the compiler and store the results under the passed `id`.
- `compare <baseline> <modified>`: Compare the benchmark results of two compilers with the two passed `id`s.
- `eprintln`: Just run the compiler and capture its `stderr` output.
  Note that the compiler normally does not print
  anything to `stderr`, so you might want to add some `eprintln!` calls to get any output.
- `samply`: Profile the compiler using the [samply][samply] sampling profiler.
- `cachegrind`: Use [Cachegrind][cachegrind] to generate a detailed simulated trace of the compiler's execution.

> You can find a more detailed description of the profilers in the [`rustc-perf` manual][rustc-perf-readme-profilers].

You can use the following options for the `x perf` command, which mirror the corresponding options of the
`profile_local` and `bench_local` commands that you can use in the suite:

- `--include`: Select benchmarks which should be profiled/benchmarked.
- `--profiles`: Select profiles (`Check`, `Debug`, `Opt`, `Doc`) which should be profiled/benchmarked.
- `--scenarios`: Select scenarios (`Full`, `IncrFull`, `IncrPatched`, `IncrUnchanged`) which should be profiled/benchmarked.

## Example profiling diff for external crates
It can be of interest to generate a local diff for two commits of the compiler for external crates.
To start, in the `rustc-perf` repo, build the collector, which runs the Rust compiler benchmarks as follows.
```
cargo build --release -p collector
```
The collector can then be run using cargo, specifying the collector binary.
It expects the following arguments:
- `<PROFILE>`: Profiler selection for how performance should be measured.
  For this example, we will use Cachegrind.
- `<RUSTC>`: The Rust compiler revision to benchmark, specified as a commit SHA from `rust-lang/rust`.
Optional arguments allow running profiles and scenarios as described above.
More information regarding the mandatory and
optional arguments can be found in the [rustc-perf-readme-profilers].

Then, for the case of generating a profile diff for the crate `serve_derive-1.0.136`, for two commits `<SHA1>` and `<SHA2>` from the `rust-lang/rust` repository,
run the following in the `rustc-perf` repo:
```
cargo run --release --bin collector profile_local cachegrind +<SHA1> --rustc2 +<SHA2> --exact-match serde_derive-1.0.136 --profiles Check --scenarios IncrUnchanged
```


[samply]: https://github.com/mstange/samply
[cachegrind]: https://www.cs.cmu.edu/afs/cs.cmu.edu/project/cmt-40/Nice/RuleRefinement/bin/valgrind-3.2.0/docs/html/cg-manual.html
[rustc-perf]: https://github.com/rust-lang/rustc-perf
[rustc-perf-readme]: https://github.com/rust-lang/rustc-perf/blob/master/collector/README.md
[rustc-perf-readme-profilers]: https://github.com/rust-lang/rustc-perf/blob/master/collector/README.md#profiling-local-builds
