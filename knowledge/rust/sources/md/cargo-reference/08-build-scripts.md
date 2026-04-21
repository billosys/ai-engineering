# Build Scripts

Some packages need to compile third-party non-Rust code, for example C
libraries. Other packages need to link to C libraries which can either be
located on the system or possibly need to be built from source. Others still
need facilities for functionality such as code generation before building (think
parser generators).

Cargo does not aim to replace other tools that are well-optimized for these
tasks, but it does integrate with them with custom build scripts. Placing a
file named `build.rs` in the root of a package will cause Cargo to compile
that script and execute it just before building the package.

```rust,ignore
// Example custom build script.
fn main() {
    // Tell Cargo that if the given file changes, to rerun this build script.
    println!("cargo::rerun-if-changed=src/hello.c");
    // Use the `cc` crate to build a C file and statically link it.
    cc::Build::new()
        .file("src/hello.c")
        .compile("hello");
}
```

Some example use cases of build scripts are:

* Building a bundled C library.
* Finding a C library on the host system.
* Generating a Rust module from a specification.
* Performing any platform-specific configuration needed for the crate.

The sections below describe how build scripts work, and the [examples
chapter](build-script-examples.md) shows a variety of examples on how to write
scripts.

> Note: The [`package.build` manifest key](manifest.md#the-build-field) can be
> used to change the name of the build script, or disable it entirely.

## Life Cycle of a Build Script

Just before a package is built, Cargo will compile a build script into an
executable (if it has not already been built). It will then run the script,
which may perform any number of tasks. The script may communicate with Cargo
by printing specially formatted commands prefixed with `cargo::` to stdout.

The build script will be rebuilt if any of its source files or dependencies
change.

By default, Cargo will re-run the build script if any of the files in the
package changes. Typically it is best to use the `rerun-if` commands,
described in the [change detection](#change-detection) section below, to
narrow the focus of what triggers a build script to run again.

Once the build script successfully finishes executing, the rest of the package
will be compiled. Scripts should exit with a non-zero exit code to halt the
build if there is an error, in which case the build script's output will be
displayed on the terminal.

## Inputs to the Build Script

When the build script is run, there are a number of inputs to the build script,
all passed in the form of [environment variables][build-env].

In addition to environment variables, the build script’s current directory is
the root directory of the build script’s package.

[build-env]: environment-variables.md#environment-variables-cargo-sets-for-build-scripts

> **Note:** When checking [configuration options] like `target_os` or `target_arch`
> in a build script, do not use the `cfg!` macro or `#[cfg]` attribute, these
> check the **host** machine (where the build script runs), not the **target**
> platform you're compiling for. This distinction matters when cross-compiling.
>
> Instead, read the corresponding [`CARGO_CFG_*`][build-env] environment variables,
> which correctly reflect the target's configuration. For a typed API, consider
> using the [`build-rs`] crate. See the [build script examples] for more details.

[configuration options]: ../../reference/conditional-compilation.html
[`build-rs`]: https://crates.io/crates/build-rs
[build script examples]: build-script-examples.md#conditional-compilation

## Outputs of the Build Script

Build scripts may save any output files or intermediate artifacts in the
directory specified in the [`OUT_DIR` environment variable][build-env]. Scripts
should not modify any files outside of that directory.

> **Note:** Cargo does not clean or reset `OUT_DIR` between builds. The contents
> of this directory may persist across rebuilds, even if the build script is
> re-run. This behavior is intentional to support incremental builds, such as
> native code compilation.
>
>Build scripts should not rely on `OUT_DIR` being empty, as its contents may
>persist across rebuilds. If a script requires a clean directory, it is currently
>responsible for managing or cleaning up any files or subdirectories it creates.
>Future improvements in this area are being discussed (see
>[#16427](https://github.com/rust-lang/cargo/issues/16427) and
>[#9661](https://github.com/rust-lang/cargo/issues/9661)).

Build scripts communicate with Cargo by printing to stdout. Cargo will
interpret each line that starts with `cargo::` as an instruction that will
influence compilation of the package. All other lines are ignored.

> The order of `cargo::` instructions printed by the build script *may*
> affect the order of arguments that `cargo` passes to `rustc`. In turn, the
> order of arguments passed to `rustc` may affect the order of arguments passed
> to the linker. Therefore, you will want to pay attention to the order of the
> build script's instructions. For example, if object `foo` needs to link against
> library `bar`, you may want to make sure that library `bar`'s
> [`cargo::rustc-link-lib`](#rustc-link-lib) instruction appears *after*
> instructions to link object `foo`.

The output of the script is hidden from the terminal during normal
compilation. If you would like to see the output directly in your terminal,
invoke Cargo as "very verbose" with the `-vv` flag. This only happens when the
build script is run. If Cargo determines nothing has changed, it will not
re-run the script, see [change detection](#change-detection) below for more.

All the lines printed to stdout by a build script are written to a file like
`target/debug/build/<pkg>/output` (the precise location may depend on your
configuration). The stderr output is also saved in that same directory.

The following is a summary of the instructions that Cargo recognizes, with each
one detailed below.

* [`cargo::rerun-if-changed=PATH`](#rerun-if-changed) --- Tells Cargo when to
  re-run the script.
* [`cargo::rerun-if-env-changed=VAR`](#rerun-if-env-changed) --- Tells Cargo when
  to re-run the script.
* [`cargo::rustc-link-arg=FLAG`](#rustc-link-arg) --- Passes custom flags to a
  linker for benchmarks, binaries, `cdylib` crates, examples, and tests.
* [`cargo::rustc-link-arg-cdylib=FLAG`](#rustc-cdylib-link-arg) --- Passes custom
  flags to a linker for cdylib crates.
* [`cargo::rustc-link-arg-bin=BIN=FLAG`](#rustc-link-arg-bin) --- Passes custom
  flags to a linker for the binary `BIN`.
* [`cargo::rustc-link-arg-bins=FLAG`](#rustc-link-arg-bins) --- Passes custom
  flags to a linker for binaries.
* [`cargo::rustc-link-arg-tests=FLAG`](#rustc-link-arg-tests) --- Passes custom
  flags to a linker for tests.
* [`cargo::rustc-link-arg-examples=FLAG`](#rustc-link-arg-examples) --- Passes custom
  flags to a linker for examples.
* [`cargo::rustc-link-arg-benches=FLAG`](#rustc-link-arg-benches) --- Passes custom
  flags to a linker for benchmarks.
* [`cargo::rustc-link-lib=LIB`](#rustc-link-lib) --- Adds a library to
  link.
* [`cargo::rustc-link-search=[KIND=]PATH`](#rustc-link-search) --- Adds to the
  library search path.
* [`cargo::rustc-flags=FLAGS`](#rustc-flags) --- Passes certain flags to the
  compiler.
* [`cargo::rustc-cfg=KEY[="VALUE"]`](#rustc-cfg) --- Enables compile-time `cfg`
  settings.
* [`cargo::rustc-check-cfg=CHECK_CFG`](#rustc-check-cfg) -- Register custom `cfg`s as
  expected for compile-time checking of configs. 
* [`cargo::rustc-env=VAR=VALUE`](#rustc-env) --- Sets an environment variable.
- [`cargo::error=MESSAGE`](#cargo-error) --- Displays an error on the terminal.
* [`cargo::warning=MESSAGE`](#cargo-warning) --- Displays a warning on the
  terminal.
* [`cargo::metadata=KEY=VALUE`](#the-links-manifest-key) --- Metadata, used by `links`
  scripts.

> **MSRV:** 1.77 is required for `cargo::KEY=VALUE` syntax.
> To support older versions, use the `cargo:KEY=VALUE` syntax.

### `cargo::rustc-link-arg=FLAG` {#rustc-link-arg}

The `rustc-link-arg` instruction tells Cargo to pass the [`-C link-arg=FLAG`
option][link-arg] to the compiler, but only when building supported targets
(benchmarks, binaries, `cdylib` crates, examples, and tests). Its usage is
highly platform specific. It is useful to set the shared library version or
linker script.

[link-arg]: ../../rustc/codegen-options/index.md#link-arg

### `cargo::rustc-link-arg-cdylib=FLAG` {#rustc-cdylib-link-arg}

The `rustc-link-arg-cdylib` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building a
`cdylib` library target. Its usage is highly platform specific. It is useful
to set the shared library version or the runtime-path.

For historical reasons, the `cargo::rustc-cdylib-link-arg` form is an alias
for `cargo::rustc-link-arg-cdylib`, and has the same meaning.

### `cargo::rustc-link-arg-bin=BIN=FLAG` {#rustc-link-arg-bin}

The `rustc-link-arg-bin` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building
the binary target with name `BIN`. Its usage is highly platform specific. It is useful
to set a linker script or other linker options.

### `cargo::rustc-link-arg-bins=FLAG` {#rustc-link-arg-bins}

The `rustc-link-arg-bins` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building a
binary target. Its usage is highly platform specific. It is useful
to set a linker script or other linker options.

### `cargo::rustc-link-arg-tests=FLAG` {#rustc-link-arg-tests}

The `rustc-link-arg-tests` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building a
tests target.

### `cargo::rustc-link-arg-examples=FLAG` {#rustc-link-arg-examples}

The `rustc-link-arg-examples` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building an examples
target.

### `cargo::rustc-link-arg-benches=FLAG` {#rustc-link-arg-benches}

The `rustc-link-arg-benches` instruction tells Cargo to pass the [`-C
link-arg=FLAG` option][link-arg] to the compiler, but only when building a benchmark
target.

### `cargo::rustc-link-lib=LIB` {#rustc-link-lib}

The `rustc-link-lib` instruction tells Cargo to link the given library using
the compiler's [`-l` flag][option-link]. This is typically used to link a
native library using [FFI].

The `LIB` string is passed directly to rustc, so it supports any syntax that
`-l` does. \
Currently the fully supported syntax for `LIB` is `[KIND[:MODIFIERS]=]NAME[:RENAME]`.

The `-l` flag is only passed to the library target of the package, unless
there is no library target, in which case it is passed to all targets. This is
done because all other targets have an implicit dependency on the library
target, and the given library to link should only be included once. This means
that if a package has both a library and a binary target, the *library* has
access to the symbols from the given lib, and the binary should access them
through the library target's public API.

The optional `KIND` may be one of `dylib`, `static`, or `framework`. See the
[rustc book][option-link] for more detail.

[option-link]: ../../rustc/command-line-arguments.md#option-l-link-lib
[FFI]: ../../nomicon/ffi.md

### `cargo::rustc-link-search=[KIND=]PATH` {#rustc-link-search}

The `rustc-link-search` instruction tells Cargo to pass the [`-L`
flag][option-search] to the compiler to add a directory to the library search
path.

The optional `KIND` may be one of `dependency`, `crate`, `native`,
`framework`, or `all`. See the [rustc book][option-search] for more detail.

These paths are also added to the [dynamic library search path environment
variable](environment-variables.md#dynamic-library-paths) if they are within
the `OUT_DIR`. Depending on this behavior is discouraged since this makes it
difficult to use the resulting binary. In general, it is best to avoid
creating dynamic libraries in a build script (using existing system libraries
is fine).

[option-search]: ../../rustc/command-line-arguments.md#option-l-search-path

### `cargo::rustc-flags=FLAGS` {#rustc-flags}

The `rustc-flags` instruction tells Cargo to pass the given space-separated
flags to the compiler. This only allows the `-l` and `-L` flags, and is
equivalent to using [`rustc-link-lib`](#rustc-link-lib) and
[`rustc-link-search`](#rustc-link-search).

### `cargo::rustc-cfg=KEY[="VALUE"]` {#rustc-cfg}

The `rustc-cfg` instruction tells Cargo to pass the given value to the
[`--cfg` flag][option-cfg] to the compiler. This may be used for compile-time
detection of features to enable [conditional compilation]. Custom cfgs
must either be expected using the [`cargo::rustc-check-cfg`](#rustc-check-cfg)
instruction or usage will need to allow the [`unexpected_cfgs`][unexpected-cfgs]
lint to avoid unexpected cfgs warnings.

Note that this does *not* affect Cargo's dependency resolution. This cannot be
used to enable an optional dependency, or enable other Cargo features.

Be aware that [Cargo features] use the form `feature="foo"`. `cfg` values
passed with this flag are not restricted to that form, and may provide just a
single identifier, or any arbitrary key/value pair. For example, emitting
`cargo::rustc-cfg=abc` will then allow code to use `#[cfg(abc)]` (note the lack
of `feature=`). Or an arbitrary key/value pair may be used with an `=` symbol
like `cargo::rustc-cfg=my_component="foo"`. The key should be a Rust
identifier, the value should be a string.

[cargo features]: features.md
[conditional compilation]: ../../reference/conditional-compilation.md
[option-cfg]: ../../rustc/command-line-arguments.md#option-cfg
[unexpected-cfgs]: ../../rustc/lints/listing/warn-by-default.md#unexpected-cfgs

### `cargo::rustc-check-cfg=CHECK_CFG` {#rustc-check-cfg}

Add to the list of expected config names and values that is used when checking
the _reachable_ cfg expressions with the [`unexpected_cfgs`][unexpected-cfgs] lint.

The syntax of `CHECK_CFG` mirrors the `rustc` [`--check-cfg` flag][option-check-cfg], see
[Checking conditional configurations][checking-conditional-configurations] for more details.

The instruction can be used like this:

```rust,no_run
// build.rs
println!("cargo::rustc-check-cfg=cfg(foo, values(\"bar\"))");
if foo_bar_condition {
    println!("cargo::rustc-cfg=foo=\"bar\"");
}
```

Note that all possible cfgs should be defined, regardless of which cfgs are
currently enabled. This includes all possible values of a given cfg name.

It is recommended to group the `cargo::rustc-check-cfg` and
[`cargo::rustc-cfg`][option-cfg] instructions as closely as possible in order to
avoid typos, missing check-cfg, stale cfgs...

See also the
[conditional compilation][conditional-compilation-example] example.

> **MSRV:** Respected as of 1.80

[checking-conditional-configurations]: ../../rustc/check-cfg.html
[option-check-cfg]: ../../rustc/command-line-arguments.md#option-check-cfg
[conditional-compilation-example]: build-script-examples.md#conditional-compilation

### `cargo::rustc-env=VAR=VALUE` {#rustc-env}

The `rustc-env` instruction tells Cargo to set the given environment variable
when compiling the package. The value can be then retrieved by the [`env!`
macro][env-macro] in the compiled crate. This is useful for embedding
additional metadata in crate's code, such as the hash of git HEAD or the
unique identifier of a continuous integration server.

See also the [environment variables automatically included by
Cargo][env-cargo].

> **Note**: These environment variables are also set when running an
> executable with `cargo run` or `cargo test`. However, this usage is
> discouraged since it ties the executable to Cargo's execution environment.
> Normally, these environment variables should only be checked at compile-time
> with the `env!` macro.

[env-macro]: ../../std/macro.env.html
[env-cargo]: environment-variables.md#environment-variables-cargo-sets-for-crates

### `cargo::error=MESSAGE` {#cargo-error}

The `error` instruction tells Cargo to display an error after the build script
has finished running, and then fail the build.

 > Note: Build script libraries should carefully consider if they want to
 > use `cargo::error` versus returning a `Result`. It may be better to return
 > a `Result`, and allow the caller to decide if the error is fatal or not.
 > The caller can then decide whether or not to display the `Err` variant
 > using `cargo::error`.

> **MSRV:** Respected as of 1.84

### `cargo::warning=MESSAGE` {#cargo-warning}

The `warning` instruction tells Cargo to display a warning after the build
script has finished running. Warnings are only shown for `path` dependencies
(that is, those you're working on locally), so for example warnings printed
out in [crates.io] crates are not emitted by default, unless the build fails.
The `-vv` "very verbose" flag may be used to have Cargo display warnings for
all crates.

## Build Dependencies

Build scripts are also allowed to have dependencies on other Cargo-based crates.
Dependencies are declared through the `build-dependencies` section of the
manifest.

```toml
[build-dependencies]
cc = "1.0.46"
```

The build script **does not** have access to the dependencies listed in the
`dependencies` or `dev-dependencies` section (they’re not built yet!). Also,
build dependencies are not available to the package itself unless also
explicitly added in the `[dependencies]` table.

It is recommended to carefully consider each dependency you add, weighing
against the impact on compile time, licensing, maintenance, etc. Cargo will
attempt to reuse a dependency if it is shared between build dependencies and
normal dependencies. However, this is not always possible, for example when
cross-compiling, so keep that in consideration of the impact on compile time.

## Change Detection

When rebuilding a package, Cargo does not necessarily know if the build script
needs to be run again. By default, it takes a conservative approach of always
re-running the build script if any file within the package is changed (or the
list of files controlled by the [`exclude` and `include` fields]). For most
cases, this is not a good choice, so it is recommended that every build script
emit at least one of the `rerun-if` instructions (described below). If these
are emitted, then Cargo will only re-run the script if the given value has
changed. If Cargo is re-running the build scripts of your own crate or a
dependency and you don't know why, see ["Why is Cargo rebuilding my code?" in the
FAQ](../faq.md#why-is-cargo-rebuilding-my-code).

[`exclude` and `include` fields]: manifest.md#the-exclude-and-include-fields

### `cargo::rerun-if-changed=PATH` {#rerun-if-changed}

The `rerun-if-changed` instruction tells Cargo to re-run the build script if
the file at the given path has changed. Currently, Cargo only uses the
filesystem last-modified "mtime" timestamp to determine if the file has
changed. It compares against an internal cached timestamp of when the build
script last ran.

If the path points to a directory, it will scan the entire directory for
any modifications.

If the build script inherently does not need to re-run under any circumstance,
then emitting `cargo::rerun-if-changed=build.rs` is a simple way to prevent it
from being re-run (otherwise, the default if no `rerun-if` instructions are
emitted is to scan the entire package directory for changes). Cargo
automatically handles whether or not the script itself needs to be recompiled,
and of course the script will be re-run after it has been recompiled.
Otherwise, specifying `build.rs` is redundant and unnecessary.

### `cargo::rerun-if-env-changed=NAME` {#rerun-if-env-changed}

The `rerun-if-env-changed` instruction tells Cargo to re-run the build script
if the value of an environment variable of the given name has changed.

Note that the environment variables here are intended for global environment
variables like `CC` and such, it is not possible to use this for environment
variables like `TARGET` that [Cargo sets for build scripts][build-env]. The
environment variables in use are those received by `cargo` invocations, not
those received by the executable of the build script.

As of 1.46, using [`env!`][env-macro] and [`option_env!`][option-env-macro] in
source code will automatically detect changes and trigger rebuilds.
`rerun-if-env-changed` is no longer needed for variables already referenced by
these macros.

[option-env-macro]: ../../std/macro.option_env.html

## The `links` Manifest Key

The `package.links` key may be set in the `Cargo.toml` manifest to declare
that the package links with the given native library. The purpose of this
manifest key is to give Cargo an understanding about the set of native
dependencies that a package has, as well as providing a principled system of
passing metadata between package build scripts.

```toml
[package]
# ...
links = "foo"
```

This manifest states that the package links to the `libfoo` native library.
When using the `links` key, the package must have a build script, and the
build script should use the [`rustc-link-lib` instruction](#rustc-link-lib) to
link the library.

Primarily, Cargo requires that there is at most one package per `links` value.
In other words, it is forbidden to have two packages link to the same native
library. This helps prevent duplicate symbols between crates. Note, however,
that there are [conventions in place](#-sys-packages) to alleviate this.

Build scripts can generate an arbitrary set of metadata in the form of
key-value pairs. This metadata is set with the `cargo::metadata=KEY=VALUE`
instruction.

The metadata is passed to the build scripts of **dependent** packages. For
example, if the package `foo` depends on `bar`, which links `baz`, then if 
`bar` generates `key=value` as part of its build script metadata, then the
build script of `foo` will have the environment variables `DEP_BAZ_KEY=value`
(note that the value of the `links` key is used and the case change for `key`).
See the ["Using another `sys` crate"][using-another-sys] for an example of 
how this can be used.

Note that metadata is only passed to immediate dependents, not transitive
dependents.

> **MSRV:** 1.77 is required for `cargo::metadata=KEY=VALUE`.
> To support older versions, use `cargo:KEY=VALUE` (unsupported directives are assumed to be metadata keys).

[using-another-sys]: build-script-examples.md#using-another-sys-crate

## `*-sys` Packages

Some Cargo packages that link to system libraries have a naming convention of
having a `-sys` suffix. Any package named `foo-sys` should provide two major
pieces of functionality:

* The library crate should link to the native library `libfoo`. This will often
  probe the current system for `libfoo` before resorting to building from
  source.
* The library crate should provide **declarations** for types and functions in
  `libfoo`, but **not** higher-level abstractions.

The set of `*-sys` packages provides a common set of dependencies for linking
to native libraries. There are a number of benefits earned from having this
convention of native-library-related packages:

* Common dependencies on `foo-sys` alleviates the rule about one package per
  value of `links`.
* Other `-sys` packages can take advantage of the `DEP_LINKS_KEY=value`
  environment variables to better integrate with other packages. See the
  ["Using another `sys` crate"][using-another-sys] example.
* A common dependency allows centralizing logic on discovering `libfoo` itself
  (or building it from source).
* These dependencies are easily [overridable](#overriding-build-scripts).

It is common to have a companion package without the `-sys` suffix that
provides a safe, high-level abstractions on top of the sys package. For
example, the [`git2` crate] provides a high-level interface to the
[`libgit2-sys` crate].

[`git2` crate]: https://crates.io/crates/git2
[`libgit2-sys` crate]: https://crates.io/crates/libgit2-sys

## Overriding Build Scripts

If a manifest contains a `links` key, then Cargo supports overriding the build
script specified with a custom library. The purpose of this functionality is to
prevent running the build script in question altogether and instead supply the
metadata ahead of time.

To override a build script, place the following configuration in any acceptable [`config.toml`](config.md) file.

```toml
[target.x86_64-unknown-linux-gnu.foo]
rustc-link-lib = ["foo"]
rustc-link-search = ["/path/to/foo"]
rustc-flags = "-L /some/path"
rustc-cfg = ['key="value"']
rustc-env = {key = "value"}
rustc-cdylib-link-arg = ["…"]
metadata_key1 = "value"
metadata_key2 = "value"
```

With this configuration, if a package declares that it links to `foo` then the
build script will **not** be compiled or run, and the metadata specified will
be used instead.

The `warning`, `rerun-if-changed`, and `rerun-if-env-changed` keys should not
be used and will be ignored.

## Jobserver

Cargo and `rustc` use the [jobserver protocol], developed for GNU make, to
coordinate concurrency across processes. It is essentially a semaphore that
controls the number of jobs running concurrently. The concurrency may be set
with the `--jobs` flag, which defaults to the number of logical CPUs.

Each build script inherits one job slot from Cargo, and should endeavor to
only use one CPU while it runs. If the script wants to use more CPUs in
parallel, it should use the [`jobserver` crate] to coordinate with Cargo.

As an example, the [`cc` crate] may enable the optional `parallel` feature
which will use the jobserver protocol to attempt to build multiple C files
at the same time.

[`cc` crate]: https://crates.io/crates/cc
[`jobserver` crate]: https://crates.io/crates/jobserver
[jobserver protocol]: http://make.mad-scientist.net/papers/jobserver-implementation/
[crates.io]: https://crates.io/


---

# Build Script Examples

The following sections illustrate some examples of writing build scripts.

Some common build script functionality can be found via crates on [crates.io].
Check out the [`build-dependencies`
keyword](https://crates.io/keywords/build-dependencies) to see what is
available. The following is a sample of some popular crates[^†]:

* [`bindgen`](https://crates.io/crates/bindgen) --- Automatically generate Rust
  FFI bindings to C libraries.
* [`cc`](https://crates.io/crates/cc) --- Compiles C/C++/assembly.
* [`pkg-config`](https://crates.io/crates/pkg-config) --- Detect system
  libraries using the `pkg-config` utility.
* [`cmake`](https://crates.io/crates/cmake) --- Runs the `cmake` build tool to build a native library.
* [`autocfg`](https://crates.io/crates/autocfg),
  [`rustc_version`](https://crates.io/crates/rustc_version),
  [`version_check`](https://crates.io/crates/version_check) --- These crates
  provide ways to implement conditional compilation based on the current
  `rustc` such as the version of the compiler.

[^†]: This list is not an endorsement. Evaluate your dependencies to see which
is right for your project.

## Code generation

Some Cargo packages need to have code generated just before they are compiled
for various reasons. Here we’ll walk through a simple example which generates a
library call as part of the build script.

First, let’s take a look at the directory structure of this package:

```text
.
├── Cargo.toml
├── build.rs
└── src
    └── main.rs

1 directory, 3 files
```

Here we can see that we have a `build.rs` build script and our binary in
`main.rs`. This package has a basic manifest:

```toml
# Cargo.toml

[package]
name = "hello-from-generated-code"
version = "0.1.0"
edition = "2024"
```

Let’s see what’s inside the build script:

```rust,no_run
// build.rs

use std::env;
use std::fs;
use std::path::Path;

fn main() {
    let out_dir = env::var_os("OUT_DIR").unwrap();
    let dest_path = Path::new(&out_dir).join("hello.rs");
    fs::write(
        &dest_path,
        "pub fn message() -> &'static str {
            \"Hello, World!\"
        }
        "
    ).unwrap();
    println!("cargo::rerun-if-changed=build.rs");
}
```

There’s a couple of points of note here:

* The script uses the `OUT_DIR` environment variable to discover where the
  output files should be located. It can use the process’ current working
  directory to find where the input files should be located, but in this case we
  don’t have any input files.
* In general, build scripts should not modify any files outside of `OUT_DIR`.
  It may seem fine on the first blush, but it does cause problems when you use
  such crate as a dependency, because there's an *implicit* invariant that
  sources in `.cargo/registry` should be immutable. `cargo` won't allow such
  scripts when packaging.
  * Sometimes, projects want to check in a generated file, and treat it as
    source code. However, in this case, the file shouldn't be generated from
    `build.rs`. Instead, have a test or similar which checks that the file
    precisely matches the generated version *and fails if the result doesn't
    match*, and run that test as part of your CI. (The test can generate a
    temporary file to compare to, and if you want to update the generated file,
    you can replace the checked-in file with that temporary file.)
* This script is relatively simple as it just writes out a small generated file.
  One could imagine that other more complex operations could take place such as
  generating a Rust module from a C header file or another language definition,
  for example.
* The [`rerun-if-changed` instruction](build-scripts.md#rerun-if-changed)
  tells Cargo that the build script only needs to re-run if the build script
  itself changes. Without this line, Cargo will automatically run the build
  script if any file in the package changes. If your code generation uses some
  input files, this is where you would print a list of each of those files.

Next, let’s peek at the library itself:

```rust,ignore
// src/main.rs

include!(concat!(env!("OUT_DIR"), "/hello.rs"));

fn main() {
    println!("{}", message());
}
```

This is where the real magic happens. The library is using the rustc-defined
[`include!` macro][include-macro] in combination with the
[`concat!`][concat-macro] and [`env!`][env-macro] macros to include the
generated file (`hello.rs`) into the crate’s compilation.

Using the structure shown here, crates can include any number of generated files
from the build script itself.

[include-macro]: ../../std/macro.include.html
[concat-macro]: ../../std/macro.concat.html
[env-macro]: ../../std/macro.env.html

## Building a native library

Sometimes it’s necessary to build some native C or C++ code as part of a
package. This is another excellent use case of leveraging the build script to
build a native library before the Rust crate itself. As an example, we’ll create
a Rust library which calls into C to print “Hello, World!”.

Like above, let’s first take a look at the package layout:

```text
.
├── Cargo.toml
├── build.rs
└── src
    ├── hello.c
    └── main.rs

1 directory, 4 files
```

Pretty similar to before! Next, the manifest:

```toml
# Cargo.toml

[package]
name = "hello-world-from-c"
version = "0.1.0"
edition = "2024"
```

For now we’re not going to use any build dependencies, so let’s take a look at
the build script now:

```rust,no_run
// build.rs

use std::process::Command;
use std::env;
use std::path::Path;

fn main() {
    let out_dir = env::var("OUT_DIR").unwrap();

    // Note that there are a number of downsides to this approach, the comments
    // below detail how to improve the portability of these commands.
    Command::new("gcc").args(&["src/hello.c", "-c", "-fPIC", "-o"])
                       .arg(&format!("{}/hello.o", out_dir))
                       .status().unwrap();
    Command::new("ar").args(&["crus", "libhello.a", "hello.o"])
                      .current_dir(&Path::new(&out_dir))
                      .status().unwrap();

    println!("cargo::rustc-link-search=native={}", out_dir);
    println!("cargo::rustc-link-lib=static=hello");
    println!("cargo::rerun-if-changed=src/hello.c");
}
```

This build script starts out by compiling our C file into an object file (by
invoking `gcc`) and then converting this object file into a static library (by
invoking `ar`). The final step is feedback to Cargo itself to say that our
output was in `out_dir` and the compiler should link the crate to `libhello.a`
statically via the `-l static=hello` flag.

Note that there are a number of drawbacks to this hard-coded approach:

* The `gcc` command itself is not portable across platforms. For example it’s
  unlikely that Windows platforms have `gcc`, and not even all Unix platforms
  may have `gcc`. The `ar` command is also in a similar situation.
* These commands do not take cross-compilation into account. If we’re cross
  compiling for a platform such as Android it’s unlikely that `gcc` will produce
  an ARM executable.

Not to fear, though, this is where a `build-dependencies` entry would help!
The Cargo ecosystem has a number of packages to make this sort of task much
easier, portable, and standardized. Let's try the [`cc`
crate](https://crates.io/crates/cc) from [crates.io]. First, add it to the
`build-dependencies` in `Cargo.toml`:

```toml
[build-dependencies]
cc = "1.0"
```

And rewrite the build script to use this crate:

```rust,ignore
// build.rs

fn main() {
    cc::Build::new()
        .file("src/hello.c")
        .compile("hello");
    println!("cargo::rerun-if-changed=src/hello.c");
}
```

The [`cc` crate] abstracts a range of build script requirements for C code:

* It invokes the appropriate compiler (MSVC for windows, `gcc` for MinGW, `cc`
  for Unix platforms, etc.).
* It takes the `TARGET` variable into account by passing appropriate flags to
  the compiler being used.
* Other environment variables, such as `OPT_LEVEL`, `DEBUG`, etc., are all
  handled automatically.
* The stdout output and `OUT_DIR` locations are also handled by the `cc`
  library.

Here we can start to see some of the major benefits of farming as much
functionality as possible out to common build dependencies rather than
duplicating logic across all build scripts!

Back to the case study though, let’s take a quick look at the contents of the
`src` directory:

```c
// src/hello.c

#include <stdio.h>

void hello() {
    printf("Hello, World!\n");
}
```

```rust,ignore
// src/main.rs

// Note the lack of the `#[link]` attribute. We’re delegating the responsibility
// of selecting what to link over to the build script rather than hard-coding
// it in the source file.
unsafe extern { fn hello(); }

fn main() {
    unsafe { hello(); }
}
```

And there we go! This should complete our example of building some C code from a
Cargo package using the build script itself. This also shows why using a build
dependency can be crucial in many situations and even much more concise!

We’ve also seen a brief example of how a build script can use a crate as a
dependency purely for the build process and not for the crate itself at runtime.

[`cc` crate]: https://crates.io/crates/cc

## Linking to system libraries

This example demonstrates how to link a system library and how the build
script is used to support this use case.

Quite frequently a Rust crate wants to link to a native library provided on
the system to bind its functionality or just use it as part of an
implementation detail. This is quite a nuanced problem when it comes to
performing this in a platform-agnostic fashion. It is best, if possible, to
farm out as much of this as possible to make this as easy as possible for
consumers.

For this example, we will be creating a binding to the system's zlib library.
This is a library that is commonly found on most Unix-like systems that
provides data compression. This is already wrapped up in the [`libz-sys`
crate], but for this example, we'll do an extremely simplified version. Check
out [the source code][libz-source] for the full example.

To make it easy to find the location of the library, we will use the
[`pkg-config` crate]. This crate uses the system's `pkg-config` utility to
discover information about a library. It will automatically tell Cargo what is
needed to link the library. This will likely only work on Unix-like systems
with `pkg-config` installed. Let's start by setting up the manifest:

```toml
# Cargo.toml

[package]
name = "libz-sys"
version = "0.1.0"
edition = "2024"
links = "z"

[build-dependencies]
pkg-config = "0.3.16"
```

Take note that we included the `links` key in the `package` table. This tells
Cargo that we are linking to the `libz` library. See ["Using another sys
crate"](#using-another-sys-crate) for an example that will leverage this.

The build script is fairly simple:

```rust,ignore
// build.rs

fn main() {
    pkg_config::Config::new().probe("zlib").unwrap();
    println!("cargo::rerun-if-changed=build.rs");
}
```

Let's round out the example with a basic FFI binding:

```rust,ignore
// src/lib.rs

use std::os::raw::{c_uint, c_ulong};

unsafe extern "C" {
    pub fn crc32(crc: c_ulong, buf: *const u8, len: c_uint) -> c_ulong;
}

#[test]
fn test_crc32() {
    let s = "hello";
    unsafe {
        assert_eq!(crc32(0, s.as_ptr(), s.len() as c_uint), 0x3610a686);
    }
}
```

Run `cargo build -vv` to see the output from the build script. On a system
with `libz` already installed, it may look something like this:

```text
[libz-sys 0.1.0] cargo::rustc-link-search=native=/usr/lib
[libz-sys 0.1.0] cargo::rustc-link-lib=z
[libz-sys 0.1.0] cargo::rerun-if-changed=build.rs
```

Nice! `pkg-config` did all the work of finding the library and telling Cargo
where it is.

It is not unusual for packages to include the source for the library, and
build it statically if it is not found on the system, or if a feature or
environment variable is set. For example, the real [`libz-sys` crate] checks the
environment variable `LIBZ_SYS_STATIC` or the `static` feature to build it
from source instead of using the system library. Check out [the
source][libz-source] for a more complete example.

[`libz-sys` crate]: https://crates.io/crates/libz-sys
[`pkg-config` crate]: https://crates.io/crates/pkg-config
[libz-source]: https://github.com/rust-lang/libz-sys

## Using another `sys` crate

When using the `links` key, crates may set metadata that can be read by other
crates that depend on it. This provides a mechanism to communicate information
between crates. In this example, we'll be creating a C library that makes use
of zlib from the real [`libz-sys` crate].

If you have a C library that depends on zlib, you can leverage the [`libz-sys`
crate] to automatically find it or build it. This is great for cross-platform
support, such as Windows where zlib is not usually installed. `libz-sys` [sets
the `include`
metadata](https://github.com/rust-lang/libz-sys/blob/3c594e677c79584500da673f918c4d2101ac97a1/build.rs#L156)
to tell other packages where to find the header files for zlib. Our build
script can read that metadata with the `DEP_Z_INCLUDE` environment variable.
Here's an example:

```toml
# Cargo.toml

[package]
name = "z_user"
version = "0.1.0"
edition = "2024"

[dependencies]
libz-sys = "1.0.25"

[build-dependencies]
cc = "1.0.46"
```

Here we have included `libz-sys` which will ensure that there is only one
`libz` used in the final library, and give us access to it from our build
script:

```rust,ignore
// build.rs

fn main() {
    let mut cfg = cc::Build::new();
    cfg.file("src/z_user.c");
    if let Some(include) = std::env::var_os("DEP_Z_INCLUDE") {
        cfg.include(include);
    }
    cfg.compile("z_user");
    println!("cargo::rerun-if-changed=src/z_user.c");
}
```

With `libz-sys` doing all the heavy lifting, the C source code may now include
the zlib header, and it should find the header, even on systems where it isn't
already installed.

```c
// src/z_user.c

#include "zlib.h"

// … rest of code that makes use of zlib.
```
## Reading target configuration

When a build script needs to make decisions based on the target platform, it should read the `CARGO_CFG_*` environment
variables rather than using `cfg!` or `#[cfg]` attributes. This is because
the build script is compiled for and runs on the *host* machine, while
`CARGO_CFG_*` variables reflect the *target* platform, an important distinction
when cross-compiling.
```rust,ignore
// build.rs

fn main() {
    // reads the TARGET configuration
    let target_os = std::env::var("CARGO_CFG_TARGET_OS").unwrap();

    if target_os == "windows" {
        println!("cargo::rustc-link-lib=userenv");
    } else if target_os == "linux" {
        println!("cargo::rustc-link-lib=pthread");
    }
}
```

Note that some configuration values may contain multiple values separated by
commas (for example, `CARGO_CFG_TARGET_FAMILY` may be `unix,wasm`). When
checking these values, be sure to handle this appropriately.

For a more convenient, typed API, consider using the [`build-rs`] crate
which handles these details for you.

[`build-rs`]: https://crates.io/crates/build-rs

## Conditional compilation

A build script may emit [`rustc-cfg` instructions] which can enable conditions
that can be checked at compile time. In this example, we'll take a look at how
the [`openssl` crate] uses this to support multiple versions of the OpenSSL
library.

The [`openssl-sys` crate] implements building and linking the OpenSSL library.
It supports multiple different implementations (like LibreSSL) and multiple
versions. It makes use of the `links` key so that it may pass information to
other build scripts. One of the things it passes is the `version_number` key,
which is the version of OpenSSL that was detected. The code in the build
script looks something [like
this](https://github.com/sfackler/rust-openssl/blob/dc72a8e2c429e46c275e528b61a733a66e7877fc/openssl-sys/build/main.rs#L216):

```rust,ignore
println!("cargo::metadata=version_number={openssl_version:x}");
```

This instruction causes the `DEP_OPENSSL_VERSION_NUMBER` environment variable
to be set in any crates that directly depend on `openssl-sys`.

The `openssl` crate, which provides the higher-level interface, specifies
`openssl-sys` as a dependency. The `openssl` build script can read the
version information generated by the `openssl-sys` build script with the
`DEP_OPENSSL_VERSION_NUMBER` environment variable. It uses this to generate
some [`cfg`
values](https://github.com/sfackler/rust-openssl/blob/dc72a8e2c429e46c275e528b61a733a66e7877fc/openssl/build.rs#L18-L36):

```rust,ignore
// (portion of build.rs)

println!("cargo::rustc-check-cfg=cfg(ossl101,ossl102)");
println!("cargo::rustc-check-cfg=cfg(ossl110,ossl110g,ossl111)");

if let Ok(version) = env::var("DEP_OPENSSL_VERSION_NUMBER") {
    let version = u64::from_str_radix(&version, 16).unwrap();

    if version >= 0x1_00_01_00_0 {
        println!("cargo::rustc-cfg=ossl101");
    }
    if version >= 0x1_00_02_00_0 {
        println!("cargo::rustc-cfg=ossl102");
    }
    if version >= 0x1_01_00_00_0 {
        println!("cargo::rustc-cfg=ossl110");
    }
    if version >= 0x1_01_00_07_0 {
        println!("cargo::rustc-cfg=ossl110g");
    }
    if version >= 0x1_01_01_00_0 {
        println!("cargo::rustc-cfg=ossl111");
    }
}
```

These `cfg` values can then be used with the [`cfg` attribute] or the [`cfg`
macro] to conditionally include code. For example, SHA3 support was added in
OpenSSL 1.1.1, so it is [conditionally
excluded](https://github.com/sfackler/rust-openssl/blob/dc72a8e2c429e46c275e528b61a733a66e7877fc/openssl/src/hash.rs#L67-L85)
for older versions:

```rust,ignore
// (portion of openssl crate)

#[cfg(ossl111)]
pub fn sha3_224() -> MessageDigest {
    unsafe { MessageDigest(ffi::EVP_sha3_224()) }
}
```

Of course, one should be careful when using this, since it makes the resulting
binary even more dependent on the build environment. In this example, if the
binary is distributed to another system, it may not have the exact same shared
libraries, which could cause problems.

[`cfg` attribute]: ../../reference/conditional-compilation.md#the-cfg-attribute
[`cfg` macro]: ../../std/macro.cfg.html
[`rustc-cfg` instructions]: build-scripts.md#rustc-cfg
[`openssl` crate]: https://crates.io/crates/openssl
[`openssl-sys` crate]: https://crates.io/crates/openssl-sys

[crates.io]: https://crates.io/
