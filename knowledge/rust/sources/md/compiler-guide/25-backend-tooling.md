# Libraries and metadata

When the compiler sees a reference to an external crate, it needs to load some
information about that crate.
This chapter gives an overview of that process,
and the supported file formats for crate libraries.

## Libraries

A crate dependency can be loaded from an `rlib`, `dylib`, or `rmeta` file.
A key point of these file formats is that they contain `rustc`-specific
[*metadata*](#metadata).
This metadata allows the compiler to discover enough
information about the external crate to understand the items it contains,
which macros it exports, and *much* more.

### rlib

An `rlib` is an [archive file], which is similar to a tar file.
This file format is specific to `rustc`, and may change over time.
This file contains:

* Object code, which is the result of code generation.
  This is used during regular linking.
  There is a separate `.o` file for each [codegen unit].
  The codegen step can be skipped with the [`-C linker-plugin-lto`][linker-plugin-lto] CLI option,
  which means each `.o` file will only contain LLVM bitcode.
* [LLVM bitcode], which is a binary representation of LLVM's intermediate
  representation, which is embedded as a section in the `.o` files.
  This can be used for [Link Time Optimization] (LTO).
  This can be removed with the
  [`-C embed-bitcode=no`][embed-bitcode] CLI option to improve compile times
  and reduce disk space if LTO is not needed.
* `rustc` [metadata], in a file named `lib.rmeta`.
* A symbol table, which is essentially a list of symbols with offsets to the
  object files that contain that symbol.
  This is pretty standard for archive files.

[archive file]: https://en.wikipedia.org/wiki/Ar_(Unix)
[LLVM bitcode]: https://llvm.org/docs/BitCodeFormat.html
[Link Time Optimization]: https://llvm.org/docs/LinkTimeOptimization.html
[codegen unit]: ../backend/codegen.md
[embed-bitcode]: https://doc.rust-lang.org/rustc/codegen-options/index.html#embed-bitcode
[linker-plugin-lto]: https://doc.rust-lang.org/rustc/codegen-options/index.html#linker-plugin-lto

### dylib

A `dylib` is a platform-specific shared library.
It includes the `rustc` [metadata] in a special link section called `.rustc`.

### rmeta

An `rmeta` file is a custom binary format that contains the [metadata] for the crate.
This file can be used for fast "checks" of a project by skipping all code
generation (as is done with `cargo check`), collecting enough information for
documentation (as is done with `cargo doc`), or for [pipelining](#pipelining).
This file is created if the [`--emit=metadata`][emit] CLI option is used.

`rmeta` files do not support linking, since they do not contain compiled object files.

[emit]: https://doc.rust-lang.org/rustc/command-line-arguments.html#option-emit

## Metadata

The metadata contains a wide swath of different elements.
This guide will not go into detail about every field it contains.
You are encouraged to browse the
[`CrateRoot`] definition to get a sense of the different elements it contains.
Everything about metadata encoding and decoding is in the [`rustc_metadata`] package.

Here are a few highlights of things it contains:

* The version of the `rustc` compiler.
  The compiler will refuse to load files from any other version.
* The [Strict Version Hash](#strict-version-hash) (SVH).
  This helps ensure the correct dependency is loaded.
* The [Stable Crate Id](#stable-crate-id).
  This is a hash used to identify crates.
* Information about all the source files in the library.
  This can be used for a variety of things, such as diagnostics pointing to sources in a
  dependency.
* Information about exported macros, traits, types, and items.
  Generally,
  anything that's needed to be known when a path references something inside a crate dependency.
* Encoded [MIR].
  This is optional, and only encoded if needed for code generation.
  `cargo check` skips this for performance reasons.

[`CrateRoot`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.CrateRoot.html
[`rustc_metadata`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/index.html
[MIR]: ../mir/index.md

### Strict Version Hash

The Strict Version Hash ([SVH], also known as the "crate hash") is a 64-bit
hash that is used to ensure that the correct crate dependencies are loaded.
It is possible for a directory to contain multiple copies of the same dependency
built with different settings, or built from different sources.
The crate loader will skip any crates that have the wrong SVH.

The SVH is also used for the [incremental compilation] session filename,
though that usage is mostly historic.

The hash includes a variety of elements:

* Hashes of the HIR nodes.
* All of the upstream crate hashes.
* All of the source filenames.
* Hashes of certain command-line flags (like `-C metadata` via the [Stable
  Crate Id](#stable-crate-id), and all CLI options marked with `[TRACKED]`).

See [`compute_hir_hash`] for where the hash is actually computed.

[SVH]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_data_structures/svh/struct.Svh.html
[incremental compilation]: ../queries/incremental-compilation.md
[`compute_hir_hash`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_lowering/fn.compute_hir_hash.html

### Stable Crate Id

The [`StableCrateId`] is a 64-bit hash used to identify different crates with
potentially the same name.
It is a hash of the crate name and all the
[`-C metadata`] CLI options computed in [`StableCrateId::new`].
It is used in a variety of places, such as symbol name mangling, crate loading, and
much more.

By default, all Rust symbols are mangled and incorporate the stable crate id.
This allows multiple versions of the same crate to be included together.
Cargo automatically generates `-C metadata` hashes based on a variety of factors, like
the package version, source, and target kind (a lib and test can have the same
crate name, so they need to be disambiguated).

[`StableCrateId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/def_id/struct.StableCrateId.html
[`StableCrateId::new`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/def_id/struct.StableCrateId.html#method.new
[`-C metadata`]: https://doc.rust-lang.org/rustc/codegen-options/index.html#metadata

## Crate loading

Crate loading can have quite a few subtle complexities.
During [name resolution], when an external crate is referenced (via an `extern crate` or
path), the resolver uses the [`CStore`] which is responsible for finding
the crate libraries and loading the [metadata] for them.
After the dependency is loaded, the `CStore` will provide the information the resolver needs
to perform its job (such as expanding macros, resolving paths, etc.).

To load each external crate, the `CStore` uses a [`CrateLocator`] to
actually find the correct files for one specific crate.
There is some great documentation in the [`locator`] module that goes into detail on how loading
works, and I strongly suggest reading it to get the full picture.

The location of a dependency can come from several different places.
Direct dependencies are usually passed with `--extern` flags, and the loader can look
at those directly.
Direct dependencies often have references to their own dependencies, which need to be loaded, too.
These are usually found by
scanning the directories passed with the `-L` flag for any file whose metadata
contains a matching crate name and [SVH](#strict-version-hash).
The loader will also look at the [sysroot] to find dependencies.

As crates are loaded, they are kept in the [`CStore`] with the crate metadata
wrapped in the [`CrateMetadata`] struct.
After resolution and expansion, the
`CStore` will make its way into the [`GlobalCtxt`] for the rest of the compilation.

[name resolution]: ../name-resolution.md
[`CrateLocator`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/locator/struct.CrateLocator.html
[`locator`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/locator/index.html
[`CStore`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/creader/struct.CStore.html
[`CrateMetadata`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/decoder/struct.CrateMetadata.html
[`GlobalCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.GlobalCtxt.html
[sysroot]: ../building/bootstrapping/what-bootstrapping-does.md#what-is-a-sysroot

## Pipelining

One trick to improve compile times is to start building a crate as soon as the
metadata for its dependencies is available.
For a library, there is no need to wait for the code generation of dependencies to finish.
Cargo implements this technique by telling `rustc` to emit an [`rmeta`](#rmeta) file for each
dependency as well as an [`rlib`](#rlib).
As early as it can, `rustc` will
save the `rmeta` file to disk before it continues to the code generation phase.
The compiler sends a JSON message to let the build tool know that it
can start building the next crate if possible.

The [crate loading](#crate-loading) system is smart enough to know when it
sees an `rmeta` file to use that if the `rlib` is not there (or has only been partially written).

This pipelining isn't possible for binaries, because the linking phase will
require the code generation of all its dependencies.
In the future, it may be
possible to further improve this scenario by splitting linking into a separate
command (see [#64191]).

[#64191]: https://github.com/rust-lang/rust/issues/64191

[metadata]: #metadata


---

# Profile-guided optimization

`rustc` supports doing profile-guided optimization (PGO).
This chapter describes what PGO is and how the support for it is
implemented in `rustc`.

## What is profiled-guided optimization?

The basic concept of PGO is to collect data about the typical execution of
a program (e.g. which branches it is likely to take) and then use this data
to inform optimizations such as inlining, machine-code layout,
register allocation, etc.

There are different ways of collecting data about a program's execution.
One is to run the program inside a profiler (such as `perf`) and another
is to create an instrumented binary, that is, a binary that has data
collection built into it, and run that.
The latter usually provides more accurate data.

## How is PGO implemented in `rustc`?

`rustc` current PGO implementation relies entirely on LLVM.
LLVM actually [supports multiple forms][clang-pgo] of PGO:

[clang-pgo]: https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization

- Sampling-based PGO where an external profiling tool like `perf` is used
  to collect data about a program's execution.
- GCOV-based profiling, where code coverage infrastructure is used to collect
  profiling information.
- Front-end based instrumentation, where the compiler front-end (e.g. Clang)
  inserts instrumentation intrinsics into the LLVM IR it generates (but see the
  [^note-instrument-coverage]"Note").
- IR-level instrumentation, where LLVM inserts the instrumentation intrinsics
  itself during optimization passes.

`rustc` supports only the last approach, IR-level instrumentation, mainly
because it is almost exclusively implemented in LLVM and needs little
maintenance on the Rust side. Fortunately, it is also the most modern approach,
yielding the best results.

So, we are dealing with an instrumentation-based approach, i.e. profiling data
is generated by a specially instrumented version of the program that's being
optimized. Instrumentation-based PGO has two components: a compile-time
component and run-time component, and one needs to understand the overall
workflow to see how they interact.

[^note-instrument-coverage]: Note: `rustc` now supports front-end-based coverage
instrumentation, via the experimental option
[`-C instrument-coverage`](./llvm-coverage-instrumentation.md), but using these
coverage results for PGO has not been attempted at this time.

### Overall workflow

Generating a PGO-optimized program involves the following four steps:

1. Compile the program with instrumentation enabled (e.g. `rustc -C profile-generate main.rs`)
2. Run the instrumented program (e.g. `./main`) which generates a `default-<id>.profraw` file
3. Convert the `.profraw` file into a `.profdata` file using LLVM's `llvm-profdata` tool.
4. Compile the program again, this time making use of the profiling data
   (e.g. `rustc -C profile-use=merged.profdata main.rs`)

### Compile-time aspects

Depending on which step in the above workflow we are in, two different things
can happen at compile time:

#### Create binaries with instrumentation

As mentioned above, the profiling instrumentation is added by LLVM.
`rustc` instructs LLVM to do so [by setting the appropriate][pgo-gen-passmanager]
flags when creating LLVM `PassManager`s:

```C
	// `PMBR` is an `LLVMPassManagerBuilderRef`
    unwrap(PMBR)->EnablePGOInstrGen = true;
    // Instrumented binaries have a default output path for the `.profraw` file
    // hard-coded into them:
    unwrap(PMBR)->PGOInstrGen = PGOGenPath;
```

`rustc` also has to make sure that some of the symbols from LLVM's profiling
runtime are not removed [by marking the with the right export level][pgo-gen-symbols].

[pgo-gen-passmanager]: https://github.com/rust-lang/rust/blob/1.34.1/src/rustllvm/PassWrapper.cpp#L412-L416
[pgo-gen-symbols]:https://github.com/rust-lang/rust/blob/1.34.1/src/librustc_codegen_ssa/back/symbol_export.rs#L212-L225


#### Compile binaries where optimizations make use of profiling data

In the final step of the workflow described above, the program is compiled
again, with the compiler using the gathered profiling data in order to drive
optimization decisions. `rustc` again leaves most of the work to LLVM here,
basically [just telling][pgo-use-passmanager] the LLVM `PassManagerBuilder`
where the profiling data can be found:

```C
	unwrap(PMBR)->PGOInstrUse = PGOUsePath;
```

[pgo-use-passmanager]: https://github.com/rust-lang/rust/blob/1.34.1/src/rustllvm/PassWrapper.cpp#L417-L420

LLVM does the rest (e.g. setting branch weights, marking functions with
`cold` or `inlinehint`, etc).


### Runtime aspects

Instrumentation-based approaches always also have a runtime component, i.e.
once we have an instrumented program, that program needs to be run in order
to generate profiling data, and collecting and persisting this profiling
data needs some infrastructure in place.

In the case of LLVM, these runtime components are implemented in
[compiler-rt][compiler-rt-profile] and statically linked into any instrumented
binaries.
The `rustc` version of this can be found in `library/profiler_builtins` which
basically packs the C code from `compiler-rt` into a Rust crate.

In order for `profiler_builtins` to be built, `profiler = true` must be set
in `rustc`'s `bootstrap.toml`.

[compiler-rt-profile]: https://github.com/llvm/llvm-project/tree/main/compiler-rt/lib/profile

## Testing PGO

Since the PGO workflow spans multiple compiler invocations most testing happens
in [run-make tests][rmake-tests] (the relevant tests have `pgo` in their name).
There is also a [codegen test][codegen-test] that checks that some expected
instrumentation artifacts show up in LLVM IR.

[rmake-tests]: https://github.com/rust-lang/rust/tree/HEAD/tests/run-make
[codegen-test]: https://github.com/rust-lang/rust/blob/HEAD/tests/codegen-llvm/pgo-instrumentation.rs

## Additional information

Clang's documentation contains a good overview on [PGO in LLVM][llvm-pgo].

[llvm-pgo]: https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization


---

# LLVM source-based code coverage

`rustc` supports detailed source-based code and test coverage analysis
with a command line option (`-C instrument-coverage`) that instruments Rust
libraries and binaries with additional instructions and data, at compile time.

The coverage instrumentation injects calls to the LLVM intrinsic instruction
[`llvm.instrprof.increment`][llvm-instrprof-increment] at code branches
(based on a MIR-based control flow analysis), and LLVM converts these to
instructions that increment static counters, when executed.
The LLVM coverage instrumentation also requires a [Coverage Map] that encodes source metadata,
mapping counter IDs--directly and indirectly--to the file locations (with
start and end line and column).

Rust libraries, with or without coverage instrumentation, can be linked into instrumented binaries.
When the program is executed and cleanly terminates,
LLVM libraries write the final counter values to a file (`default.profraw` or
a custom file set through environment variable `LLVM_PROFILE_FILE`).

Developers use existing LLVM coverage analysis tools to decode `.profraw`
files, with corresponding Coverage Maps (from matching binaries that produced
them), and generate various reports for analysis, for example:

![Screenshot of sample `llvm-cov show` result, for function add_quoted_string](img/llvm-cov-show-01.png)

Detailed instructions and examples are documented in the
[rustc book][rustc-book-instrument-coverage].

[llvm-instrprof-increment]: https://llvm.org/docs/LangRef.html#llvm-instrprof-increment-intrinsic
[coverage map]: https://llvm.org/docs/CoverageMappingFormat.html
[rustc-book-instrument-coverage]: https://doc.rust-lang.org/nightly/rustc/instrument-coverage.html

## Recommended `bootstrap.toml` settings

When working on the coverage instrumentation code, it is usually necessary to
**enable the profiler runtime** by setting `profiler = true` in `[build]`.
This allows the compiler to produce instrumented binaries, and makes it possible
to run the full coverage test suite.

Enabling debug assertions in the compiler and in LLVM is recommended, but not mandatory.

```toml
# Similar to the "compiler" profile, but also enables debug assertions in LLVM.
# These assertions can detect malformed coverage mappings in some cases.
profile = "codegen"

# IMPORTANT: This tells the build system to build the LLVM profiler runtime.
# Without it, the compiler can't produce coverage-instrumented binaries,
# and many of the coverage tests will be skipped.
build.profiler = true

# Enable debug assertions in the compiler.
rust.debug-assertions = true
```

## Rust symbol mangling

`-C instrument-coverage` automatically enables Rust symbol mangling `v0` (as
if the user specified `-C symbol-mangling-version=v0` option when invoking
`rustc`) to ensure consistent and reversible name mangling.
This has two important benefits:

1. LLVM coverage tools can analyze coverage over multiple runs, including some
   changes to source code; so mangled names must be consistent across compilations.
2. LLVM coverage reports can report coverage by function, and even separates
   out the coverage counts of each unique instantiation of a generic function,
   if invoked with multiple type substitution variations.

## The LLVM profiler runtime

Coverage data is only generated by running the executable Rust program.
`rustc` statically links coverage-instrumented binaries with LLVM runtime code
([compiler-rt][compiler-rt-profile]) that implements program hooks
(such as an `exit` hook) to write the counter values to the `.profraw` file.

In the `rustc` source tree,
`library/profiler_builtins` bundles the LLVM `compiler-rt` code into a Rust library crate.
Note that when building `rustc`,
`profiler_builtins` is only included when `build.profiler = true` is set in `bootstrap.toml`.

When compiling with `-C instrument-coverage`,
[`CStore::postprocess()`][crate-loader-postprocess] dynamically loads
`profiler_builtins` by calling `inject_profiler_runtime()`.

[compiler-rt-profile]: https://github.com/llvm/llvm-project/tree/main/compiler-rt/lib/profile
[crate-loader-postprocess]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/creader/struct.CStore.html#method.postprocess

## Testing coverage instrumentation

[(See also the compiletest documentation for the `tests/coverage`
test suite.)](./tests/compiletest.md#coverage-tests)

Coverage instrumentation in the MIR is validated by a `mir-opt` test:
[`tests/mir-opt/coverage/instrument_coverage.rs`].

Coverage instrumentation in LLVM IR is validated by the [`tests/coverage`]
test suite in `coverage-map` mode.
These tests compile a test program to LLVM IR assembly, and then
use the [`src/tools/coverage-dump`] tool to extract and pretty-print the
coverage mappings that would be embedded in the final binary.

End-to-end testing of coverage instrumentation and coverage reporting is
performed by the [`tests/coverage`] test suite in `coverage-run` mode,
and by the [`tests/coverage-run-rustdoc`] test suite.
These tests compile and run a test program with coverage
instrumentation, then use LLVM tools to convert the coverage data into a
human-readable coverage report.

> Tests in `coverage-run` mode have an implicit `//@ needs-profiler-runtime`
> directive, so they will be skipped if the profiler runtime has not been
> [enabled in `bootstrap.toml`](#recommended-configtoml-settings).

Finally, the [`tests/codegen-llvm/instrument-coverage/testprog.rs`] test compiles a simple Rust program
with `-C instrument-coverage` and compares the compiled program's LLVM IR to
expected LLVM IR instructions and structured data for a coverage-enabled
program, including various checks for Coverage Map-related metadata and the LLVM
intrinsic calls to increment the runtime counters.

Expected results for the `coverage`, `coverage-run-rustdoc`,
and `mir-opt` tests can be refreshed by running:

```shell
./x test coverage --bless
./x test coverage-run-rustdoc --bless
./x test tests/mir-opt --bless
```

[`tests/mir-opt/coverage/instrument_coverage.rs`]: https://github.com/rust-lang/rust/blob/HEAD/tests/mir-opt/coverage/instrument_coverage.rs
[`tests/coverage`]: https://github.com/rust-lang/rust/tree/HEAD/tests/coverage
[`src/tools/coverage-dump`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/coverage-dump
[`tests/coverage-run-rustdoc`]: https://github.com/rust-lang/rust/tree/HEAD/tests/coverage-run-rustdoc
[`tests/codegen-llvm/instrument-coverage/testprog.rs`]: https://github.com/rust-lang/rust/blob/HEAD/tests/mir-opt/coverage/instrument_coverage.rs


---

# Sanitizers support

The rustc compiler contains support for following sanitizers:

* [AddressSanitizer][clang-asan] a faster memory error detector.
  Can detect out-of-bounds access to heap, stack, and globals, use after free, use
  after return, double free, invalid free, memory leaks.
* [ControlFlowIntegrity][clang-cfi] LLVM Control Flow Integrity (CFI) provides
  forward-edge control flow protection.
* [Hardware-assisted AddressSanitizer][clang-hwasan]  a tool similar to
  AddressSanitizer but based on partial hardware assistance.
* [KernelControlFlowIntegrity][clang-kcfi] LLVM Kernel Control Flow Integrity
  (KCFI) provides forward-edge control flow protection for operating systems kernels.
* [LeakSanitizer][clang-lsan] a run-time memory leak detector.
* [MemorySanitizer][clang-msan] a detector of uninitialized reads.
* [ThreadSanitizer][clang-tsan] a fast data race detector.

## How to use the sanitizers?

To enable a sanitizer compile with `-Z sanitizer=...` option, where value is one
of `address`, `cfi`, `hwaddress`, `kcfi`, `leak`, `memory` or `thread`.
For more details on how to use sanitizers,
please refer to the sanitizer flag in [The Unstable Book].

[The Unstable Book]: https://doc.rust-lang.org/unstable-book

## How are sanitizers implemented in rustc?

The implementation of sanitizers (except CFI) relies almost entirely on LLVM.
The rustc is an integration point for LLVM compile time instrumentation passes
and runtime libraries.
Highlight of the most important aspects of the implementation:

*  The sanitizer runtime libraries are part of the [compiler-rt] project, and
   [will be built][sanitizer-build] on [supported targets][sanitizer-targets]
   when enabled in `bootstrap.toml`:

   ```toml
   build.sanitizers = true
   ```

   The runtimes are [placed into target libdir][sanitizer-copy].

*  During LLVM code generation, the functions intended for instrumentation are
   [marked][sanitizer-attribute] with appropriate LLVM attribute:
   `SanitizeAddress`, `SanitizeHWAddress`, `SanitizeMemory`, or `SanitizeThread`.
   By default, all functions are instrumented, but this
   behaviour can be changed with `#[sanitize(xyz = "on|off|<other>")]`.

*  The decision whether to perform instrumentation or not is possible only at a
   function granularity.
   In the cases were those decision differ between
   functions, it might be necessary to inhibit inlining, both at [MIR
   level][inline-mir] and [LLVM level][inline-llvm].

*  The LLVM IR generated by rustc is instrumented by [dedicated LLVM
   passes][sanitizer-pass], different for each sanitizer.
   Instrumentation passes are invoked after optimization passes.

*  When producing an executable, the sanitizer specific runtime library is
   [linked in][sanitizer-link].
   The libraries are searched for in the target libdir.
   First, the search is relative to the overridden system root, and subsequently,
   it is relative to the default system root.
   Fall-back to the default system root
   ensures that sanitizer runtimes remain available when using sysroot overrides
   constructed by cargo `-Z build-std` or xargo.

[compiler-rt]: https://github.com/llvm/llvm-project/tree/main/compiler-rt
[sanitizer-build]: https://github.com/rust-lang/rust/blob/1ead4761e9e2f056385768614c23ffa7acb6a19e/src/bootstrap/src/core/build_steps/llvm.rs#L958-L1031
[sanitizer-targets]: https://github.com/rust-lang/rust/blob/1ead4761e9e2f056385768614c23ffa7acb6a19e/src/bootstrap/src/core/build_steps/llvm.rs#L1073-L1111
[sanitizer-copy]: https://github.com/rust-lang/rust/blob/1ead4761e9e2f056385768614c23ffa7acb6a19e/src/bootstrap/src/core/build_steps/compile.rs#L637-L676
[sanitizer-attribute]: https://github.com/rust-lang/rust/blob/1.55.0/compiler/rustc_codegen_llvm/src/attributes.rs#L42-L58
[inline-mir]: https://github.com/rust-lang/rust/blob/1.55.0/compiler/rustc_mir/src/transform/inline.rs#L314-L316
[inline-llvm]: https://github.com/rust-lang/llvm-project/blob/9330ec5a4c1df5fc1fa62f993ed6a04da68cb040/llvm/include/llvm/IR/Attributes.td#L225-L241
[sanitizer-pass]: https://github.com/rust-lang/rust/blob/1.55.0/compiler/rustc_codegen_llvm/src/back/write.rs#L660-L678
[sanitizer-link]: https://github.com/rust-lang/rust/blob/1.55.0/compiler/rustc_codegen_ssa/src/back/link.rs#L1053-L1089

## Testing sanitizers

Sanitizers are validated by code generation tests in
[`tests/codegen-llvm/sanitize*.rs`][test-cg] and end-to-end functional tests in
[`tests/ui/sanitizer/`][test-ui] directory.

Testing sanitizer functionality requires the sanitizer runtimes (built when
`build.sanitizer = true` in `bootstrap.toml`) and target providing support for particular a sanitizer.
When a sanitizer is unsupported on a given target, sanitizer tests will be ignored.
This behaviour is controlled by compiletest `needs-sanitizer-*` directives.

[test-cg]: https://github.com/rust-lang/rust/tree/HEAD/tests/codegen-llvm
[test-ui]: https://github.com/rust-lang/rust/tree/HEAD/tests/ui/sanitizer

## Enabling a sanitizer on a new target

To enable a sanitizer on a new target which is already supported by LLVM:

1. Include the sanitizer in the list of `supported_sanitizers` in [the target
   definition][target-definition].
   `rustc --target .. -Zsanitizer=..` should now recognize the sanitizer as supported.
2. [Build the runtime for the target and include it in the libdir.][sanitizer-targets]
3. [Teach compiletest that your target now supports the sanitizer.][compiletest-definition]
   Tests marked with `needs-sanitizer-*` should now run on the target.
4. Run tests `./x test --force-rerun tests/ui/sanitize/` to verify.
5. [--enable-sanitizers in the CI configuration][ci-configuration] to build and
   distribute the sanitizer runtime as part of the release process.

[target-definition]: https://github.com/rust-lang/rust/blob/1.55.0/compiler/rustc_target/src/spec/x86_64_unknown_linux_gnu.rs#L10-L11
[compiletest-definition]: https://github.com/rust-lang/rust/blob/1.55.0/src/tools/compiletest/src/util.rs#L87-L116
[ci-configuration]: https://github.com/rust-lang/rust/blob/1.55.0/src/ci/docker/host-x86_64/dist-x86_64-linux/Dockerfile#L94

## Additional Information

* [Sanitizers project page](https://github.com/google/sanitizers/wiki/)
* [AddressSanitizer in Clang][clang-asan]
* [ControlFlowIntegrity in Clang][clang-cfi]
* [Hardware-assisted AddressSanitizer][clang-hwasan]
* [KernelControlFlowIntegrity in Clang][clang-kcfi]
* [LeakSanitizer in Clang][clang-lsan]
* [MemorySanitizer in Clang][clang-msan]
* [ThreadSanitizer in Clang][clang-tsan]

[clang-asan]: https://clang.llvm.org/docs/AddressSanitizer.html
[clang-cfi]: https://clang.llvm.org/docs/ControlFlowIntegrity.html
[clang-hwasan]: https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html
[clang-kcfi]: https://clang.llvm.org/docs/ControlFlowIntegrity.html#fsanitize-kcfi
[clang-lsan]: https://clang.llvm.org/docs/LeakSanitizer.html
[clang-msan]: https://clang.llvm.org/docs/MemorySanitizer.html
[clang-tsan]: https://clang.llvm.org/docs/ThreadSanitizer.html
