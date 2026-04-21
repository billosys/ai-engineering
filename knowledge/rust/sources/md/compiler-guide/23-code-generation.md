# Code generation

Code generation (or "codegen") is the part of the compiler
that actually generates an executable binary.
Usually, rustc uses LLVM for code generation,
but there is also support for [Cranelift] and [GCC].
The key is that rustc doesn't implement codegen itself.
It's worth noting, though, that in the Rust source code,
many parts of the backend have `codegen` in their names
(there are no hard boundaries).

[Cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[GCC]: https://github.com/rust-lang/rustc_codegen_gcc

> NOTE: If you are looking for hints on how to debug code generation bugs,
> please see [this section of the debugging chapter][debugging].

[debugging]: ./debugging.md

## What is LLVM?

[LLVM](https://llvm.org) is "a collection of modular and reusable compiler and
toolchain technologies". In particular, the LLVM project contains a pluggable
compiler backend (also called "LLVM"), which is used by many compiler projects,
including the `clang` C compiler and our beloved `rustc`.

LLVM takes input in the form of LLVM IR. It is basically assembly code with
additional low-level types and annotations added. These annotations are helpful
for doing optimizations on the LLVM IR and outputted machine code. The end
result of all this is (at long last) something executable (e.g. an ELF object,
an EXE, or wasm).

There are a few benefits to using LLVM:

- We don't have to write a whole compiler backend. This reduces implementation
  and maintenance burden.
- We benefit from the large suite of advanced optimizations that the LLVM
  project has been collecting.
- We can automatically compile Rust to any of the platforms for which LLVM has
  support. For example, as soon as LLVM added support for wasm, voila! rustc,
  clang, and a bunch of other languages were able to compile to wasm! (Well,
  there was some extra stuff to be done, but we were 90% there anyway).
- We and other compiler projects benefit from each other. For example, when the
  [Spectre and Meltdown security vulnerabilities][spectre] were discovered,
  only LLVM needed to be patched.

[spectre]: https://meltdownattack.com/

## Running LLVM, linking, and metadata generation

Once LLVM IR for all of the functions and statics, etc is built, it is time to
start running LLVM and its optimization passes. LLVM IR is grouped into
"modules". Multiple "modules" can be codegened at the same time to aid in
multi-core utilization. These "modules" are what we refer to as _codegen
units_. These units were established way back during monomorphization
collection phase.

Once LLVM produces objects from these modules, these objects are passed to the
linker along with, optionally, the metadata object and an archive or an
executable is produced.

It is not necessarily the codegen phase described above that runs the
optimizations. With certain kinds of LTO, the optimization might happen at the
linking time instead. It is also possible for some optimizations to happen
before objects are passed on to the linker and some to happen during the
linking.

This all happens towards the very end of compilation. The code for this can be
found in [`rustc_codegen_ssa::back`][ssaback] and
[`rustc_codegen_llvm::back`][llvmback]. Sadly, this piece of code is not
really well-separated into LLVM-dependent code; the [`rustc_codegen_ssa`][ssa]
contains a fair amount of code specific to the LLVM backend.

Once these components are done with their work you end up with a number of
files in your filesystem corresponding to the outputs you have requested.

[ssa]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/index.html
[ssaback]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/back/index.html
[llvmback]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_llvm/back/index.html


---

# Updating LLVM

Rust supports building against multiple LLVM versions:

* Tip-of-tree for the current LLVM development branch is usually supported within a few days.
  PRs for such fixes are tagged with `llvm-main`.
* The latest released major version is always supported.
* The one or two preceding major versions are usually supported in the sense that they are expected
  to build successfully and pass most tests.
  However, fixes for miscompilations often do not get
  backported to past LLVM versions, so using rustc with older versions of LLVM comes with an
  increased risk of soundness bugs.
  We strongly recommend using the latest version of LLVM.

By default, Rust uses its own fork in the [rust-lang/llvm-project repository].
This fork is based on a `release/$N.x` branch of the upstream project, where
`$N` is either the latest released major version, or the current major version
in release candidate phase.
The fork is never based on the `main` development branch.

Our LLVM fork only accepts:

* Backports of changes that have already landed upstream.
* Workarounds for build issues affecting our CI environment.

With the exception of one grandfathered-in patch for SGX enablement, we do not
accept functional patches that have not been upstreamed first.

There are three types of LLVM updates, with different procedures:

* Backports while the current major LLVM version is supported.
* Backports while the current major LLVM version is no longer supported (or
  the change is not eligible for upstream backport).
* Update to a new major LLVM version.

## Backports (upstream supported)

While the current major LLVM version is supported upstream, fixes should be
backported upstream first, and the release branch then merged back into the Rust fork.

1. Make sure the bugfix is in upstream LLVM.
2. If this hasn't happened already, request a backport to the upstream release branch.
   If you have LLVM commit access, follow the [backport process].
   Otherwise, open an issue requesting the backport.
   Continue once the backport has been approved and merged.
3. Identify the branch that rustc is currently using.
   The `src/llvm-project` submodule is always pinned to a branch of the
   [rust-lang/llvm-project repository].
4. Fork the rust-lang/llvm-project repository.
5. Check out the appropriate branch (typically named `rustc/a.b-yyyy-mm-dd`).
6. Add a remote for the upstream repository using
   `git remote add upstream https://github.com/llvm/llvm-project.git` and
   fetch it using `git fetch upstream`.
7. Merge the `upstream/release/$N.x` branch.
8. Push this branch to your fork.
9. Send a Pull Request to rust-lang/llvm-project to the same branch as before.
   Be sure to reference the Rust and/or LLVM issue that you're fixing in the PR description.
10. Wait for the PR to be merged.
11. Send a PR to rust-lang/rust updating the `src/llvm-project` submodule with your bugfix.
    This can be done locally with `git submodule update --remote src/llvm-project` typically.
12. Wait for PR to be merged.

An example PR: [#59089](https://github.com/rust-lang/rust/pull/59089)

## Backports (upstream not supported)

Upstream LLVM releases are only supported for two to three months after the GA release.
Once upstream backports are no longer accepted, changes should be
cherry-picked directly to our fork.

1. Make sure the bugfix is in upstream LLVM.
2. Identify the branch that rustc is currently using.
   The `src/llvm-project` submodule is always pinned to a branch of the
   [rust-lang/llvm-project repository].
3. Fork the rust-lang/llvm-project repository.
4. Check out the appropriate branch (typically named `rustc/a.b-yyyy-mm-dd`).
5. Add a remote for the upstream repository using
   `git remote add upstream https://github.com/llvm/llvm-project.git` and
   fetch it using `git fetch upstream`.
6. Cherry-pick the relevant commit(s) using `git cherry-pick -x`.
7. Push this branch to your fork.
8. Send a Pull Request to rust-lang/llvm-project to the same branch as before.
   Be sure to reference the Rust and/or LLVM issue that you're fixing in the PR description.
9. Wait for the PR to be merged.
10. Send a PR to rust-lang/rust updating the `src/llvm-project` submodule with your bugfix.
    This can be done locally with `git submodule update --remote src/llvm-project` typically.
11. Wait for PR to be merged.

An example PR: [#59089](https://github.com/rust-lang/rust/pull/59089)

## New LLVM Release Updates


Unlike bugfixes,
updating to a new release of LLVM typically requires a lot more work.
This is where we can't reasonably cherry-pick commits backwards,
so we need to do a full update.
There's a lot of stuff to do here,
so let's go through each in detail.

1. LLVM announces that its latest release version has branched.
   This will show up as a branch in the [llvm/llvm-project repository],
   typically named `release/$N.x`,
   where `$N` is the version of LLVM that's being released.

1. Create a new branch in the [rust-lang/llvm-project repository]
   from this `release/$N.x` branch,
   and name it `rustc/a.b-yyyy-mm-dd`,
   where `a.b` is the current version number of LLVM in-tree at the time of the branch,
   and the remaining part is the current date.

1. Apply Rust-specific patches to the llvm-project repository.
   All features and bugfixes are upstream,
   but there's often some weird build-related patches that don't make sense to upstream.
   These patches are typically the latest patches in the
   rust-lang/llvm-project branch that rustc is currently using.

1. Build the new LLVM in the `rust` repository.
   To do this,
   you'll want to update the `src/llvm-project` repository to your branch,
   and the revision you've created.
   It's also typically a good idea to update `.gitmodules` with the new
   branch name of the LLVM submodule.
   Make sure you've committed changes to
   `src/llvm-project` to ensure submodule updates aren't reverted.
   Some commands you should execute are:

   * `./x build src/llvm-project` - test that LLVM still builds
   * `./x build` - build the rest of rustc

   You'll likely need to update [`llvm-wrapper/*.cpp`][`llvm-wrapper`]
   to compile with updated LLVM bindings.
   Note that you should use `#ifdef` and such to ensure
   that the bindings still compile on older LLVM versions.

   Note that `profile = "compiler"` and other defaults set by `./x setup`
   download LLVM from CI instead of building it from source.
   You should disable this temporarily to make sure your changes are being used.
   This is done by having the following setting in `bootstrap.toml`:

   ```toml
   llvm.download-ci-llvm = false
   ```

1. Test for regressions across other platforms.
   LLVM often has at least one bug
   for non-tier-1 architectures, so it's good to do some more testing before
   sending this to bors!
   If you're low on resources you can send the PR as-is
   now to bors, though, and it'll get tested anyway.

   Ideally, build LLVM and test it on a few platforms:

   * Linux
   * macOS
   * Windows

   Afterwards, run some docker containers that CI also does:

   * `./src/ci/docker/run.sh wasm32`
   * `./src/ci/docker/run.sh arm-android`
   * `./src/ci/docker/run.sh dist-various-1`
   * `./src/ci/docker/run.sh dist-various-2`
   * `./src/ci/docker/run.sh armhf-gnu`

1. Prepare a PR to `rust-lang/rust`.
   Work with maintainers of
   `rust-lang/llvm-project` to get your commit in a branch of that repository,
   and then you can send a PR to `rust-lang/rust`.
   You'll change at least
   `src/llvm-project` and will likely also change [`llvm-wrapper`] as well.

   <!-- date-check: March 2026 -->
   > For prior art, here are some previous LLVM updates:
   > - [LLVM 17](https://github.com/rust-lang/rust/pull/115959)
   > - [LLVM 18](https://github.com/rust-lang/rust/pull/120055)
   > - [LLVM 19](https://github.com/rust-lang/rust/pull/127513)
   > - [LLVM 20](https://github.com/rust-lang/rust/pull/135763)
   > - [LLVM 21](https://github.com/rust-lang/rust/pull/143684)
   > - [LLVM 22](https://github.com/rust-lang/rust/pull/150722)

   Note that sometimes it's easiest to land [`llvm-wrapper`] compatibility as a PR
   before actually updating `src/llvm-project`.
   This way,
   while you're working through LLVM issues,
   others interested in trying out the new LLVM can benefit from work you've done
   to update the C++ bindings.

1. Over the next few months,
   LLVM will continually push commits to its `release/a.b` branch.
   We will often want to have those bug fixes as well.
   The merge process for that is to use `git merge` itself to merge LLVM's
   `release/a.b` branch with the branch created in step 2.
   This is typically done multiple times when necessary while LLVM's release branch is baking.

1. LLVM then announces the release of version `a.b`.

1. After LLVM's official release,
   we follow the process of creating a new branch on the rust-lang/llvm-project repository again,
   this time with a new date.
   It is only then that the PR to update Rust to use that version is merged.

   The commit history of `rust-lang/llvm-project`
   should look much cleaner as a `git rebase` is done,
   where just a few Rust-specific commits are stacked on top of stock LLVM's release branch.

### Caveats and gotchas

Ideally the above instructions are pretty smooth, but here's some caveats to
keep in mind while going through them:

* LLVM bugs are hard to find, don't hesitate to ask for help!
  Bisection is definitely your friend here
  (yes LLVM takes forever to build, yet bisection is still your friend).
  Note that you can make use of [Dev Desktops],
  which is an initiative to provide the contributors with remote access to powerful hardware.
* If you've got general questions, [wg-llvm] can help you out.
* Creating branches is a privileged operation on GitHub, so you'll need someone
  with write access to create the branches for you most likely.


[rust-lang/llvm-project repository]: https://github.com/rust-lang/llvm-project
[llvm/llvm-project repository]: https://github.com/llvm/llvm-project
[`llvm-wrapper`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_llvm/llvm-wrapper
[wg-llvm]: https://rust-lang.zulipchat.com/#narrow/stream/187780-t-compiler.2Fwg-llvm
[Dev Desktops]: https://forge.rust-lang.org/infra/docs/dev-desktop.html
[backport process]: https://llvm.org/docs/GitHub.html#backporting-fixes-to-the-release-branches


---

## Debugging LLVM

> NOTE: If you are looking for info about code generation, please see [this
> chapter][codegen] instead.

[codegen]: ./codegen.md

This section is about debugging compiler bugs in code generation (e.g. why the
compiler generated some piece of code or crashed in LLVM).
LLVM is a big project that probably needs to have its own debugging document,
but following are some tips that are important in a rustc context.

### Minimize the example

As a general rule, compilers generate lots of information from analyzing code.
Thus, a useful first step is usually to find a minimal example.
One way to do this is to

1. create a new crate that reproduces the issue (e.g. adding whatever crate is
at fault as a dependency, and using it from there)

2. minimize the crate by removing external dependencies; that is, moving
everything relevant to the new crate

3. further minimize the issue by making the code shorter (there are tools that
help with this like `creduce`)

For more discussion on methodology for steps 2 and 3 above, there is an
[epic blog post][mcve-blog] from pnkfelix specifically about Rust program minimization.

[mcve-blog]: https://blog.pnkfx.org/blog/2019/11/18/rust-bug-minimization-patterns/

### Enable LLVM internal checks

The official compilers (including nightlies) have LLVM assertions disabled,
which means that LLVM assertion failures can show up as compiler crashes (not
ICEs but "real" crashes) and other sorts of weird behavior.
If you are encountering these, it is a good idea to try using a compiler with LLVM
assertions enabled - either an "alt" nightly or a compiler you build yourself
by setting `llvm.assertions = true` in your bootstrap.toml - and see whether anything turns up.

The rustc build process builds the LLVM tools into `build/host/llvm/bin`.
They can be called directly.
These tools include:
 * [`llc`], which compiles bitcode (`.bc` files) to executable code; this can be used to
   replicate LLVM backend bugs.
 * [`opt`], a bitcode transformer that runs LLVM optimization passes.
 * [`bugpoint`], which reduces large test cases to small, useful ones.
 * and many others, some of which are referenced in the text below.

[`llc`]: https://llvm.org/docs/CommandGuide/llc.html
[`opt`]: https://llvm.org/docs/CommandGuide/opt.html
[`bugpoint`]: https://llvm.org/docs/Bugpoint.html

By default, the Rust build system does not check for changes to the LLVM source code or
its build configuration settings.
So, if you need to rebuild the LLVM that is linked
into `rustc`, first delete the file `.llvm-stamp`, which should be located
in `build/host/llvm/`.

The default rustc compilation pipeline has multiple codegen units, which is
hard to replicate manually and means that LLVM is called multiple times in
parallel.  If you can get away with it (i.e. if it doesn't make your bug
disappear), passing `-C codegen-units=1` to rustc will make debugging easier.

### Get your hands on raw LLVM input

For rustc to generate LLVM IR, you need to pass the `--emit=llvm-ir` flag.
If you are building via cargo,
use the `RUSTFLAGS` environment variable (e.g. `RUSTFLAGS='--emit=llvm-ir'`).
This causes rustc to spit out LLVM IR into the target directory.

`cargo llvm-ir [options] path` spits out the LLVM IR for a particular function at `path`.
(`cargo install cargo-asm` installs `cargo asm` and `cargo llvm-ir`).
`--build-type=debug` emits code for debug builds.
There are also other useful options.
Also, debug info in LLVM IR can clutter the output a lot:
`RUSTFLAGS="-C debuginfo=0"` is really useful.

`RUSTFLAGS="-C save-temps"` outputs LLVM bitcode at
different stages during compilation, which is sometimes useful.
The output LLVM bitcode will be in `.bc` files in the compiler's output directory, set via the
`--out-dir DIR` argument to `rustc`.

 * If you are hitting an assertion failure or segmentation fault from the LLVM
   backend when invoking `rustc` itself, it is a good idea to try passing each
   of these `.bc` files to the `llc` command, and see if you get the same failure.
   (LLVM developers often prefer a bug reduced to a `.bc` file over one
   that uses a Rust crate for its minimized reproduction.)

 * To get human readable versions of the LLVM bitcode, one just needs to convert
   the bitcode (`.bc`) files to `.ll` files using `llvm-dis`, which should be in
   the target local compilation of rustc.


Note that rustc emits different IR depending on whether `-O` is enabled, even
without LLVM's optimizations, so if you want to play with the IR rustc emits,
you should:

```bash
$ rustc +local my-file.rs --emit=llvm-ir -O -C no-prepopulate-passes \
    -C codegen-units=1
$ OPT=build/$TRIPLE/llvm/bin/opt
$ $OPT -S -O2 < my-file.ll > my
```

If you just want to get the LLVM IR during the LLVM pipeline, to e.g. see which
IR causes an optimization-time assertion to fail, or to see when LLVM performs
a particular optimization, you can pass the rustc flag `-C
llvm-args=-print-after-all`, and possibly add `-C
llvm-args='-filter-print-funcs=EXACT_FUNCTION_NAME` (e.g.  `-C
llvm-args='-filter-print-funcs=_ZN11collections3str21_$LT$impl$u20$str$GT$\
7replace17hbe10ea2e7c809b0bE'`).

That produces a lot of output into standard error, so you'll want to pipe that to some file.
Also, if you are using neither `-filter-print-funcs` nor `-C
codegen-units=1`, then, because the multiple codegen units run in parallel, the
printouts will mix together and you won't be able to read anything.

 * One caveat to the aforementioned methodology: the `-print` family of options
   to LLVM only prints the IR unit that the pass runs on (e.g., just a
   function), and does not include any referenced declarations, globals,
   metadata, etc. This means you cannot in general feed the output of `-print`
   into `llc` to reproduce a given problem.

 * Within LLVM itself, calling `F.getParent()->dump()` at the beginning of
   `SafeStackLegacyPass::runOnFunction` will dump the whole module, which
   may provide better basis for reproduction.
   (However, you should be able to get that same dump from the `.bc` files dumped by
   `-C save-temps`.)

If you want just the IR for a specific function (say, you want to see why it
causes an assertion or doesn't optimize correctly), you can use `llvm-extract`,
e.g.

```bash
$ ./build/$TRIPLE/llvm/bin/llvm-extract \
    -func='_ZN11collections3str21_$LT$impl$u20$str$GT$7replace17hbe10ea2e7c809b0bE' \
    -S \
    < unextracted.ll \
    > extracted.ll
```

### Investigate LLVM optimization passes

If you are seeing incorrect behavior due to an optimization pass, a very handy
LLVM option is `-opt-bisect-limit`, which takes an integer denoting the index
value of the highest pass to run.
Index values for taken passes are stable
from run to run; by coupling this with software that automates bisecting the
search space based on the resulting program, an errant pass can be quickly determined.
When an `-opt-bisect-limit` is specified, all runs are displayed
to standard error, along with their index and output indicating if the
pass was run or skipped.  Setting the limit to an index of -1 (e.g.,
`RUSTFLAGS="-C llvm-args=-opt-bisect-limit=-1"`) will show all passes and
their corresponding index values.

If you want to play with the optimization pipeline, you can use the [`opt`] tool
from `./build/host/llvm/bin/` with the LLVM IR emitted by rustc.

When investigating the implementation of LLVM itself, you should be
aware of its [internal debug infrastructure][llvm-debug].
This is provided in LLVM Debug builds, which you enable for rustc
LLVM builds by changing this setting in the bootstrap.toml:
```
# Indicates whether the LLVM assertions are enabled or not
llvm.assertions = true

# Indicates whether the LLVM build is a Release or Debug build
llvm.optimize = false
```
The quick summary is:
 * Setting `assertions=true` enables coarse-grain debug messaging.
   * beyond that, setting `optimize=false` enables fine-grain debug messaging.
 * `LLVM_DEBUG(dbgs() << msg)` in LLVM is like `debug!(msg)` in `rustc`.
 * The `-debug` option turns on all messaging; it is like setting the
   environment variable `RUSTC_LOG=debug` in `rustc`.
 * The `-debug-only=<pass1>,<pass2>` variant is more selective; it is like
   setting the environment variable `RUSTC_LOG=path1,path2` in `rustc`.

[llvm-debug]: https://llvm.org/docs/ProgrammersManual.html#the-llvm-debug-macro-and-debug-option

### Getting help and asking questions

If you have some questions, head over to the [rust-lang Zulip] and
specifically the `#t-compiler/wg-llvm` channel.

[rust-lang Zulip]: https://rust-lang.zulipchat.com/

### Compiler options to know and love

The `-C help` and `-Z help` compiler switches will list out a variety
of interesting options you may find useful.
Here are a few of the most common that pertain to LLVM development (some of them are employed in the
tutorial above):

- The `--emit llvm-ir` option emits a `<filename>.ll` file with LLVM IR in textual format
    - The `--emit llvm-bc` option emits in bytecode format (`<filename>.bc`)
- Passing `-C llvm-args=<foo>` allows passing pretty much all the
  options that tools like llc and opt would accept;
  e.g. `-C llvm-args=-print-before-all` to print IR before every LLVM
  pass.
- The `-C no-prepopulate-passes` will avoid pre-populate the LLVM pass
  manager with a list of passes.
  This will allow you to view the LLVM
  IR that rustc generates, not the LLVM IR after optimizations.
- The `-C passes=val` option allows you to supply a space separated list of extra LLVM passes to run
- The `-C save-temps` option saves all temporary output files during compilation
- The `-Z print-llvm-passes` option will print out LLVM optimization passes being run
- The `-Z time-llvm-passes` option measures the time of each LLVM pass
- The `-Z verify-llvm-ir` option will verify the LLVM IR for correctness
- The `-Z no-parallel-backend` will disable parallel compilation of distinct compilation units
- The `-Z llvm-time-trace` option will output a Chrome profiler compatible JSON file
  which contains details and timings for LLVM passes.
- The `-C llvm-args=-opt-bisect-limit=<index>` option allows for bisecting LLVM optimizations.

### Filing LLVM bug reports

When filing an LLVM bug report, you will probably want some sort of minimal
working example that demonstrates the problem.
The Godbolt compiler explorer is really helpful for this.

1. Once you have some LLVM IR for the problematic code (see above), you can
create a minimal working example with Godbolt.
Go to [llvm.godbolt.org](https://llvm.godbolt.org).

2. Choose `LLVM-IR` as programming language.

3. Use `llc` to compile the IR to a particular target as is:
    - There are some useful flags: `-mattr` enables target features, `-march=`
      selects the target, `-mcpu=` selects the CPU, etc.
    - Commands like `llc -march=help` output all architectures available, which
      is useful because sometimes the Rust arch names and the LLVM names do not match.
    - If you have compiled rustc yourself somewhere, in the target directory
      you have binaries for `llc`, `opt`, etc.

4. If you want to optimize the LLVM-IR, you can use `opt` to see how the LLVM
   optimizations transform it.

5. Once you have a godbolt link demonstrating the issue, it is pretty easy to
   fill in an LLVM bug.
   Just visit their [github issues page][llvm-issues].

[llvm-issues]: https://github.com/llvm/llvm-project/issues

### Porting bug fixes from LLVM

Once you've identified the bug as an LLVM bug, you will sometimes
find that it has already been reported and fixed in LLVM, but we haven't
gotten the fix yet (or perhaps you are familiar enough with LLVM to fix it yourself).

In that case, we can sometimes opt to port the fix for the bug
directly to our own LLVM fork, so that rustc can use it more easily.
Our fork of LLVM is maintained in [rust-lang/llvm-project].
Once you've landed the fix there, you'll also need to land a PR modifying
our submodule commits -- ask around on Zulip for help.

[rust-lang/llvm-project]: https://github.com/rust-lang/llvm-project/


---

# Backend Agnostic Codegen

[`rustc_codegen_ssa`]
provides an abstract interface for all backends to implement,
namely LLVM, [Cranelift], and [GCC].

[Cranelift]: https://github.com/rust-lang/rustc_codegen_cranelift
[GCC]: https://github.com/rust-lang/rustc_codegen_gcc
[`rustc_codegen_ssa`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/index.html

Below is some background information on the refactoring that created this
abstract interface.

## Refactoring of `rustc_codegen_llvm`
by Denis Merigoux, October 23rd 2018

### State of the code before the refactoring

All the code related to the compilation of MIR into LLVM IR was contained
inside the `rustc_codegen_llvm` crate. Here is the breakdown of the most
important elements:
* the `back` folder (7,800 LOC) implements the mechanisms for creating the
  different object files and archive through LLVM, but also the communication
  mechanisms for parallel code generation;
* the `debuginfo` (3,200 LOC) folder contains all code that passes debug
  information down to LLVM;
* the `llvm` (2,200 LOC) folder defines the FFI necessary to communicate with
  LLVM using the C++ API;
* the `mir` (4,300 LOC) folder implements the actual lowering from MIR to LLVM
  IR;
* the `base.rs` (1,300 LOC) file contains some helper functions but also the
  high-level code that launches the code generation and distributes the work.
* the `builder.rs` (1,200 LOC) file contains all the functions generating
  individual LLVM IR instructions inside a basic block;
* the `common.rs` (450 LOC) contains various helper functions and all the
  functions generating LLVM static values;
* the `type_.rs` (300 LOC) defines most of the type translations to LLVM IR.

The goal of this refactoring is to separate inside this crate code that is
specific to the LLVM from code that can be reused for other rustc backends. For
instance, the `mir` folder is almost entirely backend-specific but it relies
heavily on other parts of the crate. The separation of the code must not affect
the logic of the code nor its performance.

For these reasons, the separation process involves two transformations that
have to be done at the same time for the resulting code to compile:

1. replace all the LLVM-specific types by generics inside function signatures
   and structure definitions;
2. encapsulate all functions calling the LLVM FFI inside a set of traits that
   will define the interface between backend-agnostic code and the backend.

While the LLVM-specific code will be left in `rustc_codegen_llvm`, all the new
traits and backend-agnostic code will be moved in `rustc_codegen_ssa` (name
suggestion by @eddyb).

### Generic types and structures

@irinagpopa started to parametrize the types of `rustc_codegen_llvm` by a
generic `Value` type, implemented in LLVM by a reference `&'ll Value`. This
work has been extended to all structures inside the `mir` folder and elsewhere,
as well as for LLVM's `BasicBlock` and `Type` types.

The two most important structures for the LLVM codegen are `CodegenCx` and
`Builder`. They are parametrized by multiple lifetime parameters and the type
for `Value`.

```rust,ignore
struct CodegenCx<'ll, 'tcx> {
  /* ... */
}

struct Builder<'a, 'll, 'tcx> {
  cx: &'a CodegenCx<'ll, 'tcx>,
  /* ... */
}
```

`CodegenCx` is used to compile one codegen-unit that can contain multiple
functions, whereas `Builder` is created to compile one basic block.

The code in `rustc_codegen_llvm` has to deal with multiple explicit lifetime
parameters, that correspond to the following:
* `'tcx` is the longest lifetime, that corresponds to the original `TyCtxt`
  containing the program's information;
* `'a` is a short-lived reference of a `CodegenCx` or another object inside a
  struct;
* `'ll` is the lifetime of references to LLVM objects such as `Value` or
  `Type`.

Although there are already many lifetime parameters in the code, making it
generic uncovered situations where the borrow-checker was passing only due to
the special nature of the LLVM objects manipulated (they are extern pointers).
For instance, an additional lifetime parameter had to be added to
`LocalAnalyser` in `analyse.rs`, leading to the definition:

```rust,ignore
struct LocalAnalyzer<'mir, 'a, 'tcx> {
  /* ... */
}
```

However, the two most important structures `CodegenCx` and `Builder` are not
defined in the backend-agnostic code. Indeed, their content is highly specific
of the backend and it makes more sense to leave their definition to the backend
implementor than to allow just a narrow spot via a generic field for the
backend's context.

### Traits and interface

Because they have to be defined by the backend, `CodegenCx` and `Builder` will
be the structures implementing all the traits defining the backend's interface.
These traits are defined in the folder `rustc_codegen_ssa/traits` and all the
backend-agnostic code is parametrized by them. For instance, let us explain how
a function in `base.rs` is parametrized:

```rust,ignore
pub fn codegen_instance<'a, 'tcx, Bx: BuilderMethods<'a, 'tcx>>(
    cx: &'a Bx::CodegenCx,
    instance: Instance<'tcx>
) {
    /* ... */
}
```

In this signature, we have the two lifetime parameters explained earlier and
the master type `Bx` which satisfies the trait `BuilderMethods` corresponding
to the interface satisfied by the `Builder` struct. The `BuilderMethods`
defines an associated type `Bx::CodegenCx` that itself satisfies the
`CodegenMethods` traits implemented by the struct `CodegenCx`.

On the trait side, here is an example with part of the definition of
`BuilderMethods` in `traits/builder.rs`:

```rust,ignore
pub trait BuilderMethods<'a, 'tcx>:
    HasCodegen<'tcx>
    + DebugInfoBuilderMethods<'tcx>
    + ArgTypeMethods<'tcx>
    + AbiBuilderMethods<'tcx>
    + IntrinsicCallMethods<'tcx>
    + AsmBuilderMethods<'tcx>
{
    fn new_block<'b>(
        cx: &'a Self::CodegenCx,
        llfn: Self::Function,
        name: &'b str
    ) -> Self;
    /* ... */
    fn cond_br(
        &mut self,
        cond: Self::Value,
        then_llbb: Self::BasicBlock,
        else_llbb: Self::BasicBlock,
    );
    /* ... */
}
```

Finally, a master structure implementing the `ExtraBackendMethods` trait is
used for high-level codegen-driving functions like `codegen_crate` in
`base.rs`. For LLVM, it is the empty `LlvmCodegenBackend`.
`ExtraBackendMethods` should be implemented by the same structure that
implements the `CodegenBackend` defined in
`rustc_codegen_utils/codegen_backend.rs`.

During the traitification process, certain functions have been converted from
methods of a local structure to methods of `CodegenCx` or `Builder` and a
corresponding `self` parameter has been added. Indeed, LLVM stores information
internally that it can access when called through its API. This information
does not show up in a Rust data structure carried around when these methods are
called. However, when implementing a Rust backend for `rustc`, these methods
will need information from `CodegenCx`, hence the additional parameter (unused
in the LLVM implementation of the trait).

### State of the code after the refactoring

The traits offer an API which is very similar to the API of LLVM. This is not
the best solution since LLVM has a very special way of doing things: when
adding another backend, the traits definition might be changed in order to
offer more flexibility.

However, the current separation between backend-agnostic and LLVM-specific code
has allowed the reuse of a significant part of the old `rustc_codegen_llvm`.
Here is the new LOC breakdown between backend-agnostic (BA) and LLVM for the
most important elements:

* `back` folder: 3,800 (BA) vs 4,100 (LLVM);
* `mir` folder: 4,400 (BA) vs 0 (LLVM);
* `base.rs`: 1,100 (BA) vs 250 (LLVM);
* `builder.rs`: 1,400 (BA) vs 0 (LLVM);
* `common.rs`: 350 (BA) vs 350 (LLVM);

The `debuginfo` folder has been left almost untouched by the splitting and is
specific to LLVM. Only its high-level features have been traitified.

The new `traits` folder has 1500 LOC only for trait definitions. Overall, the
27,000 LOC-sized old `rustc_codegen_llvm` code has been split into the new
18,500 LOC-sized new `rustc_codegen_llvm` and the 12,000 LOC-sized
`rustc_codegen_ssa`. We can say that this refactoring allowed the reuse of
approximately 10,000 LOC that would otherwise have had to be duplicated between
the multiple backends of `rustc`.

The refactored version of `rustc`'s backend introduced no regression over the
test suite nor in performance benchmark, which is in coherence with the nature
of the refactoring that used only compile-time parametricity (no trait
objects).


---

# Implicit caller location

Approved in [RFC 2091], this feature enables the accurate reporting of caller location during panics
initiated from functions like `Option::unwrap`, `Result::expect`, and `Index::index`. This feature
adds the [`#[track_caller]`][attr-reference] attribute for functions, the
[`caller_location`][intrinsic] intrinsic, and the stabilization-friendly
[`core::panic::Location::caller`][wrapper] wrapper.

## Motivating example

Take this example program:

```rust
fn main() {
    let foo: Option<()> = None;
    foo.unwrap(); // this should produce a useful panic message!
}
```

Prior to Rust 1.42, panics like this `unwrap()` printed a location in core:

```
$ rustc +1.41.0 example.rs; example.exe
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value',...core\macros\mod.rs:15:40
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace.
```

As of 1.42, we get a much more helpful message:

```
$ rustc +1.42.0 example.rs; example.exe
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value', example.rs:3:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

These error messages are achieved through a combination of changes to `panic!` internals to make use
of `core::panic::Location::caller` and a number of `#[track_caller]` annotations in the standard
library which propagate caller information.

## Reading caller location

Previously, `panic!` made use of the `file!()`, `line!()`, and `column!()` macros to construct a
[`Location`] pointing to where the panic occurred. These macros couldn't be given an overridden
location, so functions which intentionally invoked `panic!` couldn't provide their own location,
hiding the actual source of error.

Internally, `panic!()` now calls [`core::panic::Location::caller()`][wrapper] to find out where it
was expanded. This function is itself annotated with `#[track_caller]` and wraps the
[`caller_location`][intrinsic] compiler intrinsic implemented by rustc. This intrinsic is easiest
explained in terms of how it works in a `const` context.

## Caller location in `const`

There are two main phases to returning the caller location in a const context: walking up the stack
to find the right location and allocating a const value to return.

### Finding the right `Location`

In a const context we "walk up the stack" from where the intrinsic is invoked, stopping when we
reach the first function call in the stack which does *not* have the attribute. This walk is in
[`InterpCx::find_closest_untracked_caller_location()`][const-find-closest].

Starting at the bottom, we iterate up over stack [`Frame`][const-frame]s in the
[`InterpCx::stack`][const-stack], calling
[`InstanceKind::requires_caller_location`][requires-location] on the
[`Instance`s from each `Frame`][frame-instance]. We stop once we find one that returns `false` and
return the span of the *previous* frame which was the "topmost" tracked function.

### Allocating a static `Location`

Once we have a `Span`, we need to allocate static memory for the `Location`, which is performed by
the [`TyCtxt::const_caller_location()`][const-location-query] query. Internally this calls
[`InterpCx::alloc_caller_location()`][alloc-location] and results in a unique
[memory kind][location-memory-kind] (`MemoryKind::CallerLocation`). The SSA codegen backend is able
to emit code for these same values, and we use this code there as well.

Once our `Location` has been allocated in static memory, our intrinsic returns a reference to it.

## Generating code for `#[track_caller]` callees

To generate efficient code for a tracked function and its callers, we need to provide the same
behavior from the intrinsic's point of view without having a stack to walk up at runtime. We invert
the approach: as we grow the stack down we pass an additional argument to calls of tracked functions
rather than walking up the stack when the intrinsic is called. That additional argument can be
returned wherever the caller location is queried.

The argument we append is of type `&'static core::panic::Location<'static>`. A reference was chosen
to avoid unnecessary copying because a pointer is a third the size of
`std::mem::size_of::<core::panic::Location>() == 24` at time of writing.

When generating a call to a function which is tracked, we pass the location argument the value of
[`FunctionCx::get_caller_location`][fcx-get].

If the calling function is tracked, `get_caller_location` returns the local in
[`FunctionCx::caller_location`][fcx-location] which was populated by the current caller's caller.
In these cases the intrinsic "returns" a reference which was actually provided in an argument to its
caller.

If the calling function is not tracked, `get_caller_location` allocates a `Location` static from
the current `Span` and returns a reference to that.

We more efficiently achieve the same behavior as a loop starting from the bottom by passing a single
`&Location` value through the `caller_location` fields of multiple `FunctionCx`s as we grow the
stack downward.

### Codegen examples

What does this transformation look like in practice? Take this example which uses the new feature:

```rust
#![feature(track_caller)]
use std::panic::Location;

#[track_caller]
fn print_caller() {
    println!("called from {}", Location::caller());
}

fn main() {
    print_caller();
}
```

Here `print_caller()` appears to take no arguments, but we compile it to something like this:

```rust
#![feature(panic_internals)]
use std::panic::Location;

fn print_caller(caller: &Location) {
    println!("called from {}", caller);
}

fn main() {
    print_caller(&Location::internal_constructor(file!(), line!(), column!()));
}
```

### Dynamic dispatch

In codegen contexts we have to modify the callee ABI to pass this information down the stack, but
the attribute expressly does *not* modify the type of the function. The ABI change must be
transparent to type checking and remain sound in all uses.

Direct calls to tracked functions will always know the full codegen flags for the callee and can
generate appropriate code. Indirect callers won't have this information and it's not encoded in
the type of the function pointer they call, so we generate a [`ReifyShim`] around the function
whenever taking a pointer to it. This shim isn't able to report the actual location of the indirect
call (the function's definition site is reported instead), but it prevents miscompilation and is
probably the best we can do without modifying fully-stabilized type signatures.

> *Note:* We always emit a [`ReifyShim`] when taking a pointer to a tracked function. While the
> constraint here is imposed by codegen contexts, we don't know during MIR construction of the shim
> whether we'll be called in a const context (safe to ignore shim) or in a codegen context (unsafe
> to ignore shim). Even if we did know, the results from const and codegen contexts must agree.

## The attribute

The `#[track_caller]` attribute is checked alongside other codegen attributes to ensure the
function:

* has the `"Rust"` ABI (as opposed to e.g., `"C"`)
* is not a closure
* is not `#[naked]`

If the use is valid, we set [`CodegenFnAttrsFlags::TRACK_CALLER`][attrs-flags]. This flag influences
the return value of [`InstanceKind::requires_caller_location`][requires-location] which is in turn
used in both const and codegen contexts to ensure correct propagation.

### Traits

When applied to trait method implementations, the attribute works as it does for regular functions.

When applied to a trait method prototype, the attribute applies to all implementations of the
method. When applied to a default trait method implementation, the attribute takes effect on
that implementation *and* any overrides.

Examples:

```rust
#![feature(track_caller)]

macro_rules! assert_tracked {
    () => {{
        let location = std::panic::Location::caller();
        assert_eq!(location.file(), file!());
        assert_ne!(location.line(), line!(), "line should be outside this fn");
        println!("called at {}", location);
    }};
}

trait TrackedFourWays {
    /// All implementations inherit `#[track_caller]`.
    #[track_caller]
    fn blanket_tracked();

    /// Implementors can annotate themselves.
    fn local_tracked();

    /// This implementation is tracked (overrides are too).
    #[track_caller]
    fn default_tracked() {
        assert_tracked!();
    }

    /// Overrides of this implementation are tracked (it is too).
    #[track_caller]
    fn default_tracked_to_override() {
        assert_tracked!();
    }
}

/// This impl uses the default impl for `default_tracked` and provides its own for
/// `default_tracked_to_override`.
impl TrackedFourWays for () {
    fn blanket_tracked() {
        assert_tracked!();
    }

    #[track_caller]
    fn local_tracked() {
        assert_tracked!();
    }

    fn default_tracked_to_override() {
        assert_tracked!();
    }
}

fn main() {
    <() as TrackedFourWays>::blanket_tracked();
    <() as TrackedFourWays>::default_tracked();
    <() as TrackedFourWays>::default_tracked_to_override();
    <() as TrackedFourWays>::local_tracked();
}
```

## Background/History

Broadly speaking, this feature's goal is to improve common Rust error messages without breaking
stability guarantees, requiring modifications to end-user source, relying on platform-specific
debug-info, or preventing user-defined types from having the same error-reporting benefits.

Improving the output of these panics has been a goal of proposals since at least mid-2016 (see
[non-viable alternatives] in the approved RFC for details). It took two more years until RFC 2091
was approved, much of its [rationale] for this feature's design having been discovered through the
discussion around several earlier proposals.

The design in the original RFC limited itself to implementations that could be done inside the
compiler at the time without significant refactoring. However in the year and a half between the
approval of the RFC and the actual implementation work, a [revised design] was proposed and written
up on the tracking issue. During the course of implementing that, it was also discovered that an
implementation was possible without modifying the number of arguments in a function's MIR, which
would simplify later stages and unlock use in traits.

Because the RFC's implementation strategy could not readily support traits, the semantics were not
originally specified. They have since been implemented following the path which seemed most correct
to the author and reviewers.

[RFC 2091]: https://github.com/rust-lang/rfcs/blob/master/text/2091-inline-semantic.md
[attr-reference]: https://doc.rust-lang.org/reference/attributes/codegen.html#the-track_caller-attribute
[intrinsic]: https://doc.rust-lang.org/nightly/core/intrinsics/fn.caller_location.html
[wrapper]: https://doc.rust-lang.org/nightly/core/panic/struct.Location.html#method.caller
[non-viable alternatives]: https://github.com/rust-lang/rfcs/blob/master/text/2091-inline-semantic.md#non-viable-alternatives
[rationale]: https://github.com/rust-lang/rfcs/blob/master/text/2091-inline-semantic.md#rationale
[revised design]: https://github.com/rust-lang/rust/issues/47809#issuecomment-443538059
[attrs-flags]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/middle/codegen_fn_attrs/struct.CodegenFnAttrFlags.html#associatedconstant.TRACK_CALLER
[`ReifyShim`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/enum.InstanceKind.html#variant.ReifyShim
[`Location`]: https://doc.rust-lang.org/core/panic/struct.Location.html
[const-find-closest]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.InterpCx.html#method.find_closest_untracked_caller_location
[requires-location]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/instance/enum.InstanceKind.html#method.requires_caller_location
[alloc-location]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.InterpCx.html#method.alloc_caller_location
[fcx-location]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/struct.FunctionCx.html#structfield.caller_location
[const-location-query]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/struct.TyCtxt.html#method.const_caller_location
[location-memory-kind]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/enum.MemoryKind.html#variant.CallerLocation
[const-frame]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.Frame.html
[const-stack]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.InterpCx.html#structfield.stack
[fcx-get]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/mir/struct.FunctionCx.html#method.get_caller_location
[frame-instance]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_const_eval/interpret/struct.Frame.html#structfield.instance
