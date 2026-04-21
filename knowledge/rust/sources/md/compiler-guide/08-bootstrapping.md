# Bootstrapping the compiler

[*Bootstrapping*][boot] is the process of using a compiler to compile itself.
More accurately, it means using an older compiler to compile a newer version
of the same compiler.

This raises a chicken-and-egg paradox: where did the first compiler come from?
It must have been written in a different language. In Rust's case it was
[written in OCaml][ocaml-compiler]. However, it was abandoned long ago, and the
only way to build a modern version of rustc is with a slightly less modern
version.

This is exactly how `x.py` works: it downloads the current beta release of
rustc, then uses it to compile the new compiler.

In this section, we give a high-level overview of
[what Bootstrap does](./what-bootstrapping-does.md), followed by a high-level
introduction to [how Bootstrap does it](./how-bootstrap-does-it.md).

Additionally, see [debugging bootstrap](./debugging-bootstrap.md) to learn
about debugging methods.

[boot]: https://en.wikipedia.org/wiki/Bootstrapping_(compilers)
[ocaml-compiler]: https://github.com/rust-lang/rust/tree/ef75860a0a72f79f97216f8aaa5b388d98da6480/src/boot


---

# What Bootstrapping does

[*Bootstrapping*][boot] is the process of using a compiler to compile itself.
More accurately, it means using an older compiler to compile a newer version of the same compiler.

This raises a chicken-and-egg paradox: where did the first compiler come from?
It must have been written in a different language.
In Rust's case, it was [written in OCaml][ocaml-compiler].
However, it was abandoned long ago, and the
only way to build a modern version of `rustc` is with a slightly less modern version.

This is exactly how [`./x.py`] works: it downloads the current beta release of
`rustc`, then uses it to compile the new compiler.

[`./x.py`]: https://github.com/rust-lang/rust/blob/HEAD/x.py

Note that this documentation mostly covers user-facing information.
See [bootstrap/README.md][bootstrap-internals] to read about bootstrap internals.

[bootstrap-internals]: https://github.com/rust-lang/rust/blob/HEAD/src/bootstrap/README.md

## Stages of bootstrapping

### Overview

- Stage 0: the pre-compiled compiler and standard library
- Stage 1: from current code, by an earlier compiler
- Stage 2: the truly current compiler
- Stage 3: the same-result test

Compiling `rustc` is done in stages.
Here's a diagram, adapted from Jynn
Nelson's [talk on bootstrapping][rustconf22-talk] at RustConf 2022, with
detailed explanations below.

The `A`, `B`, `C`, and `D` show the ordering of the stages of bootstrapping.
<span style="background-color: lightblue; color: black">Blue</span> nodes are
downloaded, <span style="background-color: yellow; color: black">yellow</span>
nodes are built with the `stage0` compiler, and <span style="background-color:
lightgreen; color: black">green</span> nodes are built with the `stage1` compiler.

[rustconf22-talk]: https://www.youtube.com/watch?v=oUIjG-y4zaA

```mermaid
graph TD
    s0c["stage0 compiler (1.86.0-beta.1)"]:::downloaded -->|A| s0l("stage0 std (1.86.0-beta.1)"):::downloaded;
    s0c & s0l --- stepb[ ]:::empty;
    stepb -->|B| s0ca["stage0 compiler artifacts (1.87.0-dev)"]:::with-s0c;
    s0ca -->|copy| s1c["stage1 compiler (1.87.0-dev)"]:::with-s0c;
    s1c -->|C| s1l("stage1 std (1.87.0-dev)"):::with-s1c;
    s1c & s1l --- stepd[ ]:::empty;
    stepd -->|D| s1ca["stage1 compiler artifacts (1.87.0-dev)"]:::with-s1c;
    s1ca -->|copy| s2c["stage2 compiler"]:::with-s1c;

    classDef empty width:0px,height:0px;
    classDef downloaded fill: lightblue;
    classDef with-s0c fill: yellow;
    classDef with-s1c fill: lightgreen;
```

### Stage 0: the pre-compiled compiler

The stage0 compiler is by default the very recent _beta_ `rustc` compiler and its
associated dynamic libraries, which `./x.py` will download for you.
(You can also configure `./x.py` to change stage0 to something else.)

The precompiled stage0 compiler is then used only to compile [`src/bootstrap`] and [`compiler/rustc`]
with precompiled stage0 std.

Note that to build the stage1 compiler we use the precompiled stage0 compiler and std.
Therefore, to use a compiler with a std that is freshly built from the tree, you need to
build the stage2 compiler.

There are two concepts at play here: a compiler (with its set of dependencies) and its
'target' or 'object' libraries (`std` and `rustc`).
Both are staged, but in a staggered manner.

[`compiler/rustc`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc
[`src/bootstrap`]: https://github.com/rust-lang/rust/tree/HEAD/src/bootstrap

### Stage 1: from current code, by an earlier compiler

The rustc source code is then compiled with the `stage0` compiler to produce the `stage1` compiler.

### Stage 2: the truly current compiler

We then rebuild the compiler using `stage1` compiler with in-tree std to produce the `stage2`
compiler.

The `stage1` compiler itself was built by precompiled `stage0` compiler and std
and hence not by the source in your working directory.
This means that the ABI
generated by the `stage0` compiler may not match the ABI that would have been made
by the `stage1` compiler, which can cause problems for dynamic libraries, tests
and tools using `rustc_private`.

Note that the `proc_macro` crate avoids this issue with a `C` FFI layer called
`proc_macro::bridge`, allowing it to be used with `stage1`.

The `stage2` compiler is the one distributed with `rustup` and all other install methods.
However, it takes a very long time to build because one must first
build the new compiler with an older compiler and then use that to build the new
compiler with itself.

For development, you usually only want to use `--stage 1` flag to build things.
See [Building the compiler](../how-to-build-and-run.html#building-the-compiler).

### Stage 3: the same-result test

Stage 3 is optional.
To sanity check our new compiler, we can build the libraries with the `stage2` compiler.
The result ought to be identical to before, unless something has broken.

### Building the stages

The script [`./x`] tries to be helpful and pick the stage you most likely meant for each subcommand.
Here are some `x` commands with their default stages:

- `check`: `--stage 1`
- `clippy`: `--stage 1`
- `doc`: `--stage 1`
- `build`: `--stage 1`
- `test`: `--stage 1`
- `dist`: `--stage 2`
- `install`: `--stage 2`
- `bench`: `--stage 2`

You can always override the stage by passing `--stage N` explicitly.

For more information about stages, [see below](#understanding-stages-of-bootstrap).

[`./x`]: https://github.com/rust-lang/rust/blob/HEAD/x

## Complications of bootstrapping

Since the build system uses the current beta compiler to build a `stage1`
bootstrapping compiler, the compiler source code can't use some features until
they reach beta (because otherwise the beta compiler doesn't support them).
On the other hand, for [compiler intrinsics][intrinsics] and internal features, the
features _have_ to be used.
Additionally, the compiler makes heavy use of `nightly` features (`#![feature(...)]`).
How can we resolve this problem?

There are two methods used:

1. The build system sets `--cfg bootstrap` when building with `stage0`, so we
   can use `cfg(not(bootstrap))` to only use features when built with `stage1`.
   Setting `--cfg bootstrap` in this way is used for features that were just
   stabilized, which require `#![feature(...)]` when built with `stage0`, but not for `stage1`.
2. The build system sets `RUSTC_BOOTSTRAP=1`.
   This special variable means to
   _break the stability guarantees_ of Rust: allowing use of `#![feature(...)]`
   with a compiler that's not `nightly`.
   _Setting `RUSTC_BOOTSTRAP=1` should never be used except when bootstrapping the compiler._

[boot]: https://en.wikipedia.org/wiki/Bootstrapping_(compilers)
[intrinsics]: ../../appendix/glossary.md#intrinsic
[ocaml-compiler]: https://github.com/rust-lang/rust/tree/ef75860a0a72f79f97216f8aaa5b388d98da6480/src/boot

## Understanding stages of bootstrap

### Overview

This is a detailed look into the separate bootstrap stages.

The convention `./x` uses is that:

- A `--stage N` flag means to run the stage N compiler (`stageN/rustc`).
- A "stage N artifact" is a build artifact that is _produced_ by the stage N compiler.
- The stage N+1 compiler is assembled from stage N *artifacts*. This process is
  called _uplifting_.

#### Build artifacts

Anything you can build with `./x` is a _build artifact_.
Build artifacts include, but are not limited to:

- binaries, like `stage0-rustc/rustc-main`
- shared objects, like `stage0-sysroot/rustlib/libstd-6fae108520cf72fe.so`
- [rlib] files, like `stage0-sysroot/rustlib/libstd-6fae108520cf72fe.rlib`
- HTML files generated by rustdoc, like `doc/std`

[rlib]: ../../serialization.md

#### Examples

- `./x test tests/ui` means to build the `stage1` compiler and run `compiletest` on it.
  If you're working on the compiler, this is normally the test command you want.
- `./x test --stage 0 library/std` means to run tests on the standard library
  without building `rustc` from source ('build with `stage0`, then test the artifacts').
  If you're working on the standard library, this is normally the test command you want.
- `./x build --stage 0` means to build with the stage0 `rustc`.
- `./x doc --stage 1` means to document using the stage0 `rustdoc`.

#### Examples of what *not* to do

- `./x test --stage 0 tests/ui` is not useful: it runs tests on the _beta_
  compiler and doesn't build `rustc` from source.
  Use `test tests/ui` instead,
  which builds `stage1` from source.
- `./x test --stage 0 compiler/rustc` builds the compiler but runs no tests:
  it's running `cargo test -p rustc`, but `cargo` doesn't understand Rust's tests.
  You shouldn't need to use this; use `test` instead (without arguments).
- `./x build --stage 0 compiler/rustc` builds the compiler, but does not build
  `libstd` or even `libcore`.
  Most of the time, you'll want `./x build library`
  instead, which allows compiling programs without needing to define lang items.

### Building vs. running

In short, _stage 0 uses the `stage0` compiler to create `stage0` artifacts which
will later be uplifted to be the stage1 compiler_.

In each stage besides 0, two major steps are performed:

1. `std` is compiled by the stage N compiler.
2. That `std` is linked to programs built by the stage N compiler, including the
   stage N artifacts (stage N+1 compiler).

This is somewhat intuitive if one thinks of the stage N artifacts as "just"
another program we are building with the stage N compiler: `build --stage N
compiler/rustc` is linking the stage N artifacts to the `std` built by the stage N compiler.

### Stages and `std`

Note that there are two `std` libraries in play here:

1. The library _linked_ to `stageN/rustc`, which was built by stage N-1 (stage N-1 `std`)
2. The library _used to compile programs_ with `stageN/rustc`, which was built
   by stage N (stage N `std`).

Stage N `std` is pretty much necessary for any useful work with the stage N compiler.
Without it, you can only compile programs with `#![no_core]` -- not terribly useful!

The reason these need to be different is because they aren't necessarily
ABI-compatible: there could be new layout optimizations, changes to `MIR`, or
other changes to Rust metadata on `nightly` that aren't present in beta.

This is also where `--keep-stage 1 library/std` comes into play.
Since most changes to the compiler don't actually change the ABI, once you've produced a
`std` in `stage1`, you can probably just reuse it with a different compiler.
If the ABI hasn't changed, you're good to go; no need to spend time recompiling that `std`.
The flag `--keep-stage` simply instructs the build script to assume
the previous compile is fine and copies those artifacts into the appropriate
place, skipping the `cargo` invocation.

### Cross-compiling rustc

*Cross-compiling* is the process of compiling code that will run on another architecture.
For instance, you might want to build an ARM version of rustc using an x86 machine.
Building `stage2` `std` is different when you are cross-compiling.

This is because `./x` uses the following logic: if `HOST` and `TARGET` are the
same, it will reuse `stage1` `std` for `stage2`!
This is sound because `stage1`
`std` was compiled with the `stage1` compiler, i.e. a compiler using the source
code you currently have checked out.
So it should be identical (and therefore
ABI-compatible) to the `std` that `stage2/rustc` would compile.

However, when cross-compiling, `stage1` `std` will only run on the host.
So, the `stage2` compiler has to recompile `std` for the target.

(See in the table how `stage2` only builds non-host `std` targets).

### What is a 'sysroot'?

When you build a project with `cargo`, the build artifacts for dependencies are
normally stored in `target/debug/deps`.
This only contains dependencies `cargo`
knows about; in particular, it doesn't have the standard library.
Where do `std` or `proc_macro` come from?
They come from the **sysroot**, the root of a number
of directories where the compiler loads build artifacts at runtime.
The `sysroot` doesn't just store the standard library, though - it includes anything
that needs to be loaded at runtime.
That includes (but is not limited to):

- Libraries `libstd`/`libtest`/`libproc_macro`.
- Compiler crates themselves, when using `rustc_private`.
  In-tree, these are always present; out-of-tree, you need to install `rustc-dev` with `rustup`.
- Shared object file `libLLVM.so` for the LLVM project.
  In-tree, this is either built from source or downloaded from CI; out-of-tree, you need to install
  `llvm-tools-preview` with `rustup`.

All the artifacts listed so far are *compiler* runtime dependencies.
You can see them with `rustc --print sysroot`:

```
$ ls $(rustc --print sysroot)/lib
libchalk_derive-0685d79833dc9b2b.so  libstd-25c6acf8063a3802.so
libLLVM-11-rust-1.50.0-nightly.so    libtest-57470d2aa8f7aa83.so
librustc_driver-4f0cc9f50e53f0ba.so  libtracing_attributes-e4be92c35ab2a33b.so
librustc_macros-5f0ec4a119c6ac86.so  rustlib
```

There are also runtime dependencies for the standard library!
These are in `lib/rustlib/`, not `lib/` directly.

```
$ ls $(rustc --print sysroot)/lib/rustlib/x86_64-unknown-linux-gnu/lib | head -n 5
libaddr2line-6c8e02b8fedc1e5f.rlib
libadler-9ef2480568df55af.rlib
liballoc-9c4002b5f79ba0e1.rlib
libcfg_if-512eb53291f6de7e.rlib
libcompiler_builtins-ef2408da76957905.rlib
```

Directory `lib/rustlib/` includes libraries like `hashbrown` and `cfg_if`, which
are not part of the public API of the standard library, but are used to implement it.
Also,`lib/rustlib/` is part of the search path for linkers, but
`lib` will never be part of the search path.

#### `-Z force-unstable-if-unmarked`

Since `lib/rustlib/` is part of the search path we have to be careful about
which crates are included in it.
In particular, all crates except for the
standard library are built with the flag `-Z force-unstable-if-unmarked`, which
means that you have to use `#![feature(rustc_private)]` in order to load it (as
opposed to the standard library, which is always available).

The `-Z force-unstable-if-unmarked` flag has a variety of purposes to help
enforce that the correct crates are marked as `unstable`.
It was introduced primarily to allow rustc and the standard library to link to arbitrary crates on
crates.io which do not themselves use `staged_api`.
`rustc` also relies on this
flag to mark all of its crates as `unstable` with the `rustc_private` feature so
that each crate does not need to be carefully marked with `unstable`.

This flag is automatically applied to all of `rustc` and the standard library by
the bootstrap scripts.
This is needed because the compiler and all of its
dependencies are shipped in `sysroot` to all users.

This flag has the following effects:

- Marks the crate as "`unstable`" with the `rustc_private` feature if it is not
  itself marked as `stable` or `unstable`.
- Allows these crates to access other forced-unstable crates without any need for attributes.
  Normally, a crate would need a `#![feature(rustc_private)]`
  attribute to use other `unstable` crates.
  However, that would make it
  impossible for a crate from crates.io to access its own dependencies since
  that crate won't have a `feature(rustc_private)` attribute, but *everything*
  is compiled with `-Z force-unstable-if-unmarked`.

Code which does not use `-Z force-unstable-if-unmarked` should include the
`#![feature(rustc_private)]` crate attribute to access these forced-unstable crates.
This is needed for things which link `rustc` itself, such as `Miri` or `clippy`.

You can find more discussion about sysroots in:
- The [rustdoc PR] explaining why it uses `extern crate` for dependencies loaded from `sysroot`
- [Discussions about sysroot on
  Zulip](https://rust-lang.zulipchat.com/#narrow/stream/182449-t-compiler.2Fhelp/topic/deps.20in.20sysroot/)
- [Discussions about building rustdoc out of
  tree](https://rust-lang.zulipchat.com/#narrow/stream/182449-t-compiler.2Fhelp/topic/How.20to.20create.20an.20executable.20accessing.20.60rustc_private.60.3F)

[rustdoc PR]: https://github.com/rust-lang/rust/pull/76728

## Passing flags to commands invoked by `bootstrap`

Conveniently `./x` allows you to pass stage-specific flags to `rustc` and
`cargo` when bootstrapping.
The `RUSTFLAGS_BOOTSTRAP` environment variable is
passed as `RUSTFLAGS` to the bootstrap stage (`stage0`), and
`RUSTFLAGS_NOT_BOOTSTRAP` is passed when building artifacts for later stages.
`RUSTFLAGS` will work, but also affects the build of `bootstrap` itself, so it
will be rare to want to use it.
Finally, `MAGIC_EXTRA_RUSTFLAGS` bypasses the
`cargo` cache to pass flags to rustc without recompiling all dependencies.

- `RUSTDOCFLAGS`, `RUSTDOCFLAGS_BOOTSTRAP` and `RUSTDOCFLAGS_NOT_BOOTSTRAP` are
  analogous to `RUSTFLAGS`, but for `rustdoc`.
- `CARGOFLAGS` will pass arguments to cargo itself (e.g. `--timings`).
  `CARGOFLAGS_BOOTSTRAP` and `CARGOFLAGS_NOT_BOOTSTRAP` work analogously to `RUSTFLAGS_BOOTSTRAP`.
- `--test-args` will pass arguments through to the test runner.
  For `tests/ui`,
  this is `compiletest`.
  For unit tests and doc tests, this is the `libtest` runner.

Most test runners accept `--help`,
which you can use to find out the options accepted by the runner.

## Environment Variables

During bootstrapping, there are a bunch of compiler-internal environment variables that are used.
If you are trying to run an intermediate version of
`rustc`, sometimes you may need to set some of these environment variables manually.
Otherwise, you get an error like the following:

```text
thread 'main' panicked at 'RUSTC_STAGE was not set: NotPresent', library/core/src/result.rs:1165:5
```

If `./stageN/bin/rustc` gives an error about environment variables, that usually
means something is quite wrong -- such as you're trying to compile `rustc` or
`std` or something which depends on environment variables.
In the unlikely case that you actually need to invoke `rustc` in such a situation, you can tell the
bootstrap shim to print all `env` variables by adding `-vvv` to your `x` command.

Finally, bootstrap makes use of the [cc-rs crate] which has [its own
method][env-vars] of configuring `C` compilers and `C` flags via environment variables.

[cc-rs crate]: https://github.com/rust-lang/cc-rs
[env-vars]: https://docs.rs/cc/latest/cc/#external-configuration-via-environment-variables

## Clarification of build command's `stdout`

In this part, we will investigate the build command's `stdout` in an action
(similar, but more detailed and complete documentation compare to topic above).
When you execute `x build --dry-run` command, the build output will be something like the following:

```text
Building stage0 library artifacts (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu)
Copying stage0 library from stage0 (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu / x86_64-unknown-linux-gnu)
Building stage0 compiler artifacts (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu)
Copying stage0 rustc from stage0 (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu / x86_64-unknown-linux-gnu)
Assembling stage1 compiler (x86_64-unknown-linux-gnu)
Building stage1 library artifacts (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu)
Copying stage1 library from stage1 (x86_64-unknown-linux-gnu -> x86_64-unknown-linux-gnu / x86_64-unknown-linux-gnu)
Building stage1 tool rust-analyzer-proc-macro-srv (x86_64-unknown-linux-gnu)
Building rustdoc for stage1 (x86_64-unknown-linux-gnu)
```

### Building stage0 {std,compiler} artifacts

These steps use the provided (downloaded, usually) compiler to compile the local
Rust source into libraries we can use.

### Copying stage0 \{std,rustc\}

This copies the library and compiler artifacts from `cargo` into
`stage0-sysroot/lib/rustlib/{target-triple}/lib`

### Assembling stage1 compiler

This copies the libraries we built in "building `stage0` ... artifacts" into the
`stage1` compiler's `lib/` directory.
These are the host libraries that the compiler itself uses to run.
These aren't actually used by artifacts the new compiler generates.
This step also copies the `rustc` and `rustdoc` binaries we generated into `build/$HOST/stage/bin`.

The `stage1/bin/rustc` is a fully functional compiler built with stage0 (precompiled) compiler and std.
To use a compiler built entirely from source with the in-tree compiler and std, you need to build the
stage2 compiler, which is compiled using the stage1 (in-tree) compiler and std.


---

# How Bootstrap does it

The core concept in Bootstrap is a build [`Step`],  which are chained together
by [`Builder::ensure`]. [`Builder::ensure`] takes a [`Step`] as input, and runs
the [`Step`] if and only if it has not already been run. Let's take a closer
look at [`Step`].

## Synopsis of [`Step`]

A [`Step`] represents a granular collection of actions involved in the process
of producing some artifact. It can be thought of like a rule in Makefiles.
The [`Step`] trait is defined as:

```rs,no_run
pub trait Step: 'static + Clone + Debug + PartialEq + Eq + Hash {
    type Output: Clone;

    const DEFAULT: bool = false;
    const ONLY_HOSTS: bool = false;

    // Required methods
    fn run(self, builder: &Builder<'_>) -> Self::Output;
    fn should_run(run: ShouldRun<'_>) -> ShouldRun<'_>;

    // Provided method
    fn make_run(_run: RunConfig<'_>) { ... }
}
```

- `run` is the function that is responsible for doing the work.
  [`Builder::ensure`] invokes `run`.
- `should_run` is the command-line interface, which determines if an invocation
  such as `x build foo` should run a given [`Step`]. In a "default" context
  where no paths are provided, then `make_run` is called directly.
- `make_run` is invoked only for things directly asked via the CLI and not
  for steps which are dependencies of other steps.

## The entry points

There's a couple of preliminary steps before core Bootstrap code is reached:

1. Shell script or `make`: [`./x`](https://github.com/rust-lang/rust/blob/HEAD/x) or [`./x.ps1`](https://github.com/rust-lang/rust/blob/HEAD/x.ps1) or `make`
2. Convenience wrapper script: [`x.py`](https://github.com/rust-lang/rust/blob/HEAD/x.py)
3. [`src/bootstrap/bootstrap.py`](https://github.com/rust-lang/rust/blob/HEAD/src/bootstrap/bootstrap.py)
4. [`src/bootstrap/src/bin/main.rs`](https://github.com/rust-lang/rust/blob/HEAD/src/bootstrap/src/bin/main.rs)

See [src/bootstrap/README.md](https://github.com/rust-lang/rust/blob/HEAD/src/bootstrap/README.md)
for a more specific description of the implementation details.

[`Step`]: https://doc.rust-lang.org/nightly/nightly-rustc/bootstrap/core/builder/trait.Step.html
[`Builder::ensure`]: https://doc.rust-lang.org/nightly/nightly-rustc/bootstrap/core/builder/struct.Builder.html#method.ensure


---

# Writing tools in Bootstrap

There are three types of tools you can write in bootstrap:

- **`Mode::ToolBootstrap`**

  Use this for tools that don’t need anything from the in-tree compiler and can run with the stage0 `rustc`.
  The output is placed in the "bootstrap-tools" directory.
  This mode is for general-purpose tools built entirely with the stage0 compiler,
  including target libraries, and it only works for stage 0.

- **`Mode::ToolStd`**

  Use this for tools that rely on the locally built std.
  The output goes into the "stageN-tools" directory.
  This mode is rarely used, mainly for `compiletest` which requires `libtest`.

- **`Mode::ToolRustcPrivate`**

  Use this for tools that use the `rustc_private` mechanism,
  and thus depend on the locally built `rustc` and its rlib artifacts.
  This is more complex than the other modes,
  because the tool must be built with the same compiler used for `rustc`,
  and placed in the "stageN-tools" directory.
  When you choose `Mode::ToolRustcPrivate`,
  `ToolBuild` implementation takes care of this automatically.
  If you need to use the builder’s compiler for something specific,
  you can get it from `ToolBuildResult`, which is returned by the tool's [`Step`].

Regardless of the tool type,
you must return `ToolBuildResult` from the tool’s [`Step`] implementation,
and use `ToolBuild` inside it.

[`Step`]: https://doc.rust-lang.org/nightly/nightly-rustc/bootstrap/core/builder/trait.Step.html


---

# Debugging bootstrap

There are two main ways of debugging (and profiling bootstrap). The first is through println logging, and the second is through the `tracing` feature.

## `println` logging

Bootstrap has extensive unstructured logging. Most of it is gated behind the `--verbose` flag (pass `-vv` for even more detail).

If you want to see verbose output of executed Cargo commands and other kinds of detailed logs, pass `-v` or `-vv` when invoking bootstrap. Note that the logs are unstructured and may be overwhelming.

```
$ ./x dist rustc --dry-run -vv
learning about cargo
running: RUSTC_BOOTSTRAP="1" "/home/jyn/src/rust2/build/x86_64-unknown-linux-gnu/stage0/bin/cargo" "metadata" "--format-version" "1" "--no-deps" "--manifest-path" "/home/jyn/src/rust2/Cargo.toml" (failure_mode=Exit) (created at src/bootstrap/src/core/metadata.rs:81:25, executed at src/bootstrap/src/core/metadata.rs:92:50)
running: RUSTC_BOOTSTRAP="1" "/home/jyn/src/rust2/build/x86_64-unknown-linux-gnu/stage0/bin/cargo" "metadata" "--format-version" "1" "--no-deps" "--manifest-path" "/home/jyn/src/rust2/library/Cargo.toml" (failure_mode=Exit) (created at src/bootstrap/src/core/metadata.rs:81:25, executed at src/bootstrap/src/core/metadata.rs:92:50)
...
```

## `tracing` in bootstrap

Bootstrap has a conditional `tracing` feature, which provides the following features:
- It enables structured logging using [`tracing`][tracing] events and spans.
- It generates a [Chrome trace file] that can be used to visualize the hierarchy and durations of executed steps and commands.
  - You can open the generated `chrome-trace.json` file using Chrome, on the `chrome://tracing` tab, or e.g. using [Perfetto].
- It generates [GraphViz] graphs that visualize the dependencies between executed steps.
  - You can open the generated `step-graph-*.dot` file using e.g. [xdot] to visualize the step graph, or use e.g. `dot -Tsvg` to convert the GraphViz file to an SVG file.
- It generates a command execution summary, which shows which commands were executed, how many of their executions were cached, and what commands were the slowest to run.
  - The generated `command-stats.txt` file is in a simple human-readable format.

The structured logs will be written to standard error output (`stderr`), while the other outputs will be stored in files in the `<build-dir>/bootstrap-trace/<pid>` directory. For convenience, bootstrap will also create a symlink to the latest generated trace output directory at `<build-dir>/bootstrap-trace/latest`.

> Note that if you execute bootstrap with `--dry-run`, the tracing output directory might change. Bootstrap will always print a path where the tracing output files were stored at the end of its execution.

[tracing]: https://docs.rs/tracing/0.1.41/tracing/index.html
[Chrome trace file]: https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/
[Perfetto]: https://ui.perfetto.dev/
[GraphViz]: https://graphviz.org/doc/info/lang.html
[xdot]: https://github.com/jrfonseca/xdot.py

### Enabling `tracing` output

To enable the conditional `tracing` feature, run bootstrap with the `BOOTSTRAP_TRACING` environment variable.

[tracing_subscriber filter]: https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html

```bash
$ BOOTSTRAP_TRACING=trace ./x build library --stage 1
```

Example output[^unstable]:

```
$ BOOTSTRAP_TRACING=trace ./x build library --stage 1 --dry-run
Building bootstrap
    Finished `dev` profile [unoptimized] target(s) in 0.05s
15:56:52.477  INFO > tool::LibcxxVersionTool {target: x86_64-unknown-linux-gnu} (builder/mod.rs:1715)
15:56:52.575  INFO > compile::Assemble {target_compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }} (builder/mod.rs:1715)
15:56:52.575  INFO > tool::Compiletest {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu} (builder/mod.rs:1715)
15:56:52.576  INFO  > tool::ToolBuild {build_compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu, tool: "compiletest", path: "src/tools/compiletest", mode: ToolBootstrap, source_type: InTree, extra_features: [], allow_features: "internal_output_capture", cargo_args: [], artifact_kind: Binary} (builder/mod.rs:1715)
15:56:52.576  INFO   > builder::Libdir {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu} (builder/mod.rs:1715)
15:56:52.576  INFO    > compile::Sysroot {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, force_recompile: false} (builder/mod.rs:1715)
15:56:52.578  INFO > compile::Assemble {target_compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }} (builder/mod.rs:1715)
15:56:52.578  INFO > tool::Compiletest {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu} (builder/mod.rs:1715)
15:56:52.578  INFO  > tool::ToolBuild {build_compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu, tool: "compiletest", path: "src/tools/compiletest", mode: ToolBootstrap, source_type: InTree, extra_features: [], allow_features: "internal_output_capture", cargo_args: [], artifact_kind: Binary} (builder/mod.rs:1715)
15:56:52.578  INFO   > builder::Libdir {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, target: x86_64-unknown-linux-gnu} (builder/mod.rs:1715)
15:56:52.578  INFO    > compile::Sysroot {compiler: Compiler { stage: 0, host: x86_64-unknown-linux-gnu, forced_compiler: false }, force_recompile: false} (builder/mod.rs:1715)
    Finished `release` profile [optimized] target(s) in 0.11s
Tracing/profiling output has been written to <src-root>/build/bootstrap-trace/latest
Build completed successfully in 0:00:00
```

[^unstable]: This output is always subject to further changes.

#### Controlling tracing output

The environment variable `BOOTSTRAP_TRACING` accepts a [`tracing_subscriber` filter][tracing-env-filter]. If you set `BOOTSTRAP_TRACING=trace`, you will enable all logs, but that can be overwhelming. You can thus use the filter to reduce the amount of data logged.

There are two orthogonal ways to control which kind of tracing logs you want:

1. You can specify the log **level**, e.g. `debug` or `trace`.
   - If you select a level, all events/spans with an equal or higher priority level will be shown.
2. You can also control the log **target**, e.g. `bootstrap` or `bootstrap::core::config` or a custom target like `CONFIG_HANDLING` or `STEP`.
    - Custom targets are used to limit what kinds of spans you are interested in, as the `BOOTSTRAP_TRACING=trace` output can be quite verbose. Currently, you can use the following custom targets:
        - `CONFIG_HANDLING`: show spans related to config handling.
        - `STEP`: show all executed steps. Executed commands have `info` event level.
        - `COMMAND`: show all executed commands. Executed commands have `trace` event level.
        - `IO`: show performed I/O operations. Executed commands have `trace` event level.
            - Note that many I/O are currently not being traced.

You can of course combine them (custom target logs are typically gated behind `TRACE` log level additionally):

```bash
$ BOOTSTRAP_TRACING=CONFIG_HANDLING=trace,STEP=info,COMMAND=trace ./x build library --stage 1
```

[tracing-env-filter]: https://docs.rs/tracing-subscriber/0.3.19/tracing_subscriber/filter/struct.EnvFilter.html

Note that the level that you specify using `BOOTSTRAP_TRACING` also has an effect on the spans that will be recorded in the Chrome trace file.

##### FIXME(#96176): specific tracing for `compiler()` vs `compiler_for()`

The additional targets `COMPILER` and `COMPILER_FOR` are used to help trace what
`builder.compiler()` and `builder.compiler_for()` does. They should be removed
if [#96176][cleanup-compiler-for] is resolved.

[cleanup-compiler-for]: https://github.com/rust-lang/rust/issues/96176

### Using `tracing` in bootstrap

Both `tracing::*` macros and the `tracing::instrument` proc-macro attribute need to be gated behind `tracing` feature. Examples:

```rs
#[cfg(feature = "tracing")]
use tracing::instrument;

struct Foo;

impl Step for Foo {
    type Output = ();

    #[cfg_attr(feature = "tracing", instrument(level = "trace", name = "Foo::should_run", skip_all))]
    fn should_run(run: ShouldRun<'_>) -> ShouldRun<'_> {
        trace!(?run, "entered Foo::should_run");

        todo!()
    }

    fn run(self, builder: &Builder<'_>) -> Self::Output {
        trace!(?run, "entered Foo::run");

        todo!()
    }    
}
```

For `#[instrument]`, it's recommended to:

- Gate it behind `trace` level for fine-granularity, possibly `debug` level for core functions.
- Explicitly pick an instrumentation name via `name = ".."` to distinguish between e.g. `run` of different steps.
- Take care to not cause diverging behavior via tracing, e.g. building extra things only when tracing infra is enabled.

### rust-analyzer integration?

Unfortunately, because bootstrap is a `rust-analyzer.linkedProjects`, you can't ask r-a to check/build bootstrap itself with `tracing` feature enabled to get relevant completions, due to lack of support as described in <https://github.com/rust-lang/rust-analyzer/issues/8521>.


---

# `cfg(bootstrap)` in compiler dependencies

The rust compiler uses some external crates that can run into cyclic dependencies with the compiler itself: the compiler needs an updated crate to build, but the crate needs an updated compiler. This page describes how `#[cfg(bootstrap)]` can be used to break this cycle.

## Enabling `#[cfg(bootstrap)]`

Usually the use of `#[cfg(bootstrap)]` in an external crate causes a warning:

```
warning: unexpected `cfg` condition name: `bootstrap`
 --> src/main.rs:1:7
  |
1 | #[cfg(bootstrap)]
  |       ^^^^^^^^^
  |
  = help: expected names are: `docsrs`, `feature`, and `test` and 31 more
  = help: consider using a Cargo feature instead
  = help: or consider adding in `Cargo.toml` the `check-cfg` lint config for the lint:
           [lints.rust]
           unexpected_cfgs = { level = "warn", check-cfg = ['cfg(bootstrap)'] }
  = help: or consider adding `println!("cargo::rustc-check-cfg=cfg(bootstrap)");` to the top of the `build.rs`
  = note: see <https://doc.rust-lang.org/nightly/rustc/check-cfg/cargo-specifics.html> for more information about checking conditional configuration
  = note: `#[warn(unexpected_cfgs)]` on by default
```

This warning can be silenced by adding these lines to the project's `Cargo.toml`:

```toml
[lints.rust]
unexpected_cfgs = { level = "warn", check-cfg = ['cfg(bootstrap)'] }
```

Now `#[cfg(bootstrap)]` can be used in the crate just like it can be in the compiler: when the bootstrap compiler is used, code annotated with `#[cfg(bootstrap)]` is compiled, otherwise code annotated with `#[cfg(not(bootstrap))]` is compiled.

## The update dance

As a concrete example we'll use a change where the `#[naked]` attribute was made into an unsafe attribute, which caused a cyclic dependency with the `compiler-builtins` crate.

### Step 1: accept the new behavior in the compiler ([#139797](https://github.com/rust-lang/rust/pull/139797))

In this example it is possible to accept both the old and new behavior at the same time by disabling an error.

### Step 2: update the crate ([#821](https://github.com/rust-lang/compiler-builtins/pull/821))

Now in the crate, use `#[cfg(bootstrap)]` to use the old behavior, or `#[cfg(not(bootstrap))]` to use the new behavior.

### Step 3: update the crate version used by the compiler ([#139934](https://github.com/rust-lang/rust/pull/139934))

For `compiler-builtins` this meant a version bump, in other cases it may be a git submodule update.

### Step 4: remove the old behavior from the compiler ([#139753](https://github.com/rust-lang/rust/pull/139753))

The updated crate can now be used. In this example that meant that the old behavior could be removed.
