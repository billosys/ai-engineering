# Testing the compiler

The Rust project runs a wide variety of different tests, orchestrated by the
build system (`./x test`). This section gives a brief overview of the different
testing tools. Subsequent chapters dive into [running tests](running.md) and
[adding new tests](adding.md).

## Kinds of tests

There are several kinds of tests to exercise things in the Rust distribution.
Almost all of them are driven by `./x test`, with some exceptions noted below.

### Compiletest

The main test harness for testing the compiler itself is a tool called
[compiletest].

[compiletest] supports running different styles of tests, organized into *test
suites*. A *test mode* may provide common presets/behavior for a set of *test
suites*. [compiletest]-supported tests are located in the [`tests`] directory.

The [Compiletest chapter][compiletest] goes into detail on how to use this tool.

> Example: `./x test tests/ui`

[compiletest]: compiletest.md
[`tests`]: https://github.com/rust-lang/rust/tree/HEAD/tests

### Package tests

The standard library and many of the compiler packages include typical Rust
`#[test]` unit tests, integration tests, and documentation tests. You can pass a
path to `./x test` for almost any package in the `library/` or `compiler/`
directory, and `x` will essentially run `cargo test` on that package.

Examples:

| Command                                   | Description                           |
|-------------------------------------------|---------------------------------------|
| `./x test library/std`                    | Runs tests on `std` only              |
| `./x test library/core`                   | Runs tests on `core` only             |
| `./x test compiler/rustc_data_structures` | Runs tests on `rustc_data_structures` |

The standard library relies very heavily on documentation tests to cover its
functionality. However, unit tests and integration tests can also be used as
needed. Almost all of the compiler packages have doctests disabled.

All standard library and compiler unit tests are placed in separate `tests` file
(which is enforced in [tidy][tidy-unit-tests]). This ensures that when the test
file is changed, the crate does not need to be recompiled. For example:

```rust,ignore
#[cfg(test)]
mod tests;
```

If it wasn't done this way, and you were working on something like `core`, that
would require recompiling the entire standard library, and the entirety of
`rustc`.

`./x test` includes some CLI options for controlling the behavior with these
package tests:

* `--doc` — Only runs documentation tests in the package.
* `--all-targets` — Run all tests *except* documentation tests.
* `--tests` — Only runs unit and integration tests

[tidy-unit-tests]: https://github.com/rust-lang/rust/blob/HEAD/src/tools/tidy/src/unit_tests.rs

### Tidy

Tidy is a custom tool used for validating source code style and formatting
conventions, such as rejecting long lines. There is more information in the
[section on coding conventions](../conventions.md#formatting) or the [Tidy Readme].

> Examples: `./x test tidy`

[Tidy Readme]: https://github.com/rust-lang/rust/blob/HEAD/src/tools/tidy/Readme.md


### Formatting

Rustfmt is integrated with the build system to enforce uniform style across the
compiler. The formatting check is automatically run by the Tidy tool mentioned
above.

Examples:

| Command                 | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| `./x fmt --check`       | Checks formatting and exits with an error if formatting is needed. |
| `./x fmt`               | Runs rustfmt across the entire codebase.                           |
| `./x test tidy --bless` | First runs rustfmt to format the codebase, then runs tidy checks.  |

### Book documentation tests

All of the books that are published have their own tests, primarily for
validating that the Rust code examples pass. Under the hood, these are
essentially using `rustdoc --test` on the markdown files. The tests can be run
by passing a path to a book to `./x test`.

> Example: `./x test src/doc/book`

### Documentation link checker

Links across all documentation is validated with a link checker tool,
and it can be invoked so:

```console
./x test linkchecker
```

This requires building all of the documentation, which might take a while.

### `distcheck`

`distcheck` verifies that the source distribution tarball created by the build
system will unpack, build, and run all tests.

```console
./x test distcheck
```

### Tool tests

Packages that are included with Rust have all of their tests run as well. This
includes things such as cargo, clippy, rustfmt, miri, bootstrap (testing the
Rust build system itself), etc.

Most of the tools are located in the [`src/tools`] directory. To run the tool's
tests, just pass its path to `./x test`.

> Example: `./x test src/tools/cargo`

Usually these tools involve running `cargo test` within the tool's directory.

If you want to run only a specified set of tests, append `--test-args
FILTER_NAME` to the command.

> Example: `./x test src/tools/miri --test-args padding`

In CI, some tools are allowed to fail. Failures send notifications to the
corresponding teams, and is tracked on the [toolstate website]. More information
can be found in the [toolstate documentation].

[`src/tools`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/
[toolstate documentation]: https://forge.rust-lang.org/infra/toolstate.html
[toolstate website]: https://rust-lang-nursery.github.io/rust-toolstate/

### Ecosystem testing

Rust tests integration with real-world code to catch regressions and make
informed decisions about the evolution of the language. There are several kinds
of ecosystem tests, including Crater. See the [Ecosystem testing
chapter](ecosystem.md) for more details.

### Performance testing

A separate infrastructure is used for testing and tracking performance of the
compiler. See the [Performance testing chapter](perf.md) for more details.

### Codegen backend testing

See [Codegen backend testing](./codegen-backend-tests/intro.md).

## Miscellaneous information

There are some other useful testing-related info at [Misc info](misc.md).

## Further reading

The following blog posts may also be of interest:

- brson's classic ["How Rust is tested"][howtest]

[howtest]: https://brson.github.io/2017/07/10/how-rust-is-tested


---

# Running tests

You can run the entire test collection using `x`.
But note that running the *entire* test collection is almost never what you want to do during local
development because it takes a really long time.
For local development, see the subsection after on how to run a subset of tests.

<div class="warning">

Running plain `./x test` will build the stage 1 compiler and then run the whole test suite.
This not only includes `tests/`, but also `library/`, `compiler/`,
`src/tools/` package tests and more.

You usually only want to run a subset of the test suites (or even a smaller set
of tests than that) which you expect will exercise your changes.
PR CI exercises a subset of test collections, and merge queue CI will exercise all of the test
collection.

</div>

```text
./x test
```

The test results are cached and previously successful tests are `ignored` during testing.
The stdout/stderr contents as well as a timestamp file for every test
can be found under `build/<target-tuple>/test/` for the given
`<target-tuple>`. To force-rerun a test (e.g. in case the test runner fails to
notice a change) you can use the `--force-rerun` CLI option.

> **Note on requirements of external dependencies**
>
> Some test suites may require external dependencies. This is especially true of
> debuginfo tests. Some debuginfo tests require a Python-enabled gdb. You can
> test if your gdb install supports Python by using the `python` command from
> within gdb. Once invoked you can type some Python code (e.g. `print("hi")`)
> followed by return and then `CTRL+D` to execute it. If you are building gdb
> from source, you will need to configure with
> `--with-python=<path-to-python-binary>`.

## Running a subset of the test suites

When working on a specific PR, you will usually want to run a smaller set of tests.
For example, a good "smoke test" that can be used after modifying rustc
to see if things are generally working correctly would be to exercise the `ui`
test suite ([`tests/ui`]):

```text
./x test tests/ui
```

Of course, the choice of test suites is somewhat arbitrary, and may not suit the task you are doing.
For example, if you are hacking on debuginfo, you may be better off with the debuginfo test suite:

```text
./x test tests/debuginfo
```

If you only need to test a specific subdirectory of tests for any given test
suite, you can pass that directory as a filter to `./x test`:

```text
./x test tests/ui/const-generics
```

> **Note for MSYS2**
>
> On MSYS2 the paths seem to be strange and `./x test` neither recognizes
> `tests/ui/const-generics` nor `tests\ui\const-generics`. In that case, you can
> workaround it by using e.g. `./x test ui
> --test-args="tests/ui/const-generics"`.

Likewise, you can test a single file by passing its path:

```text
./x test tests/ui/const-generics/const-test.rs
```

`x` doesn't support running a single tool test by passing its path yet.
You'll have to use the `--test-args` argument as described
[below](#running-an-individual-test).

```text
./x test src/tools/miri --test-args tests/fail/uninit/padding-enum.rs
```

### Run only the tidy script

```text
./x test tidy
```

### Run tests on the standard library

```text
./x test --stage 0 library/std
```

Note that this only runs tests on `std`;
if you want to test `core` or other crates, you have to specify those explicitly.

### Run the tidy script and tests on the standard library

```text
./x test --stage 0 tidy library/std
```

### Run tests on the standard library using a stage 1 compiler

```text
./x test --stage 1 library/std
```

By listing which test suites you want to run,
you avoid having to run tests for components you did not change at all.

<div class="warning">

Note that bors only runs the tests with the full stage 2 build;
therefore, while the tests **usually** work fine with stage 1, there are some limitations.

</div>

### Run all tests using a stage 2 compiler

```text
./x test --stage 2
```

<div class="warning">
You almost never need to do this;
CI will run these tests for you.
</div>

## Run unit tests on the compiler/library

You may want to run unit tests on a specific file with following:

```text
./x test compiler/rustc_data_structures/src/thin_vec/tests.rs
```

But unfortunately, it's impossible.
You should invoke the following instead:

```text
./x test compiler/rustc_data_structures/ --test-args thin_vec
```

## Running an individual test

Another common thing that people want to do is to run an **individual test**,
often the test they are trying to fix.
As mentioned earlier, you may pass the
full file path to achieve this, or alternatively one may invoke `x` with the `--test-args` option:

```text
./x test tests/ui --test-args issue-1234
```

Under the hood, the test runner invokes the standard Rust test runner (the same
one you get with `#[test]`), so this command would wind up filtering for tests
that include "issue-1234" in the name.
Thus, `--test-args` is a good way to run a collection of related tests.

## Passing arguments to `rustc` when running tests

It can sometimes be useful to run some tests with specific compiler arguments,
without using `RUSTFLAGS` (during development of unstable features, with `-Z` flags, for example).

This can be done with `./x test`'s `--compiletest-rustc-args` option, to pass
additional arguments to the compiler when building the tests.

## Editing and updating the reference files

If you have changed the compiler's output intentionally, or you are making a new
test, you can pass `--bless` to the test subcommand.

As an example, if some tests in `tests/ui` are failing, you can run this command:

```text
./x test tests/ui --bless
```

It automatically adjusts the `.stderr`, `.stdout`, or `.fixed` files of all `test/ui` tests.
Of course you can also target just specific tests with the `--test-args your_test_name` flag,
just like when running the tests without the `--bless` flag.

## Configuring test running

There are a few options for running tests:

* `bootstrap.toml` has the `rust.verbose-tests` option. If `false`, each test will
  print a single dot (the default).
  If `true`, the name of every test will be printed.
  This is equivalent to the `--quiet` option in the [Rust test
  harness](https://doc.rust-lang.org/rustc/tests/).
* The environment variable `RUST_TEST_THREADS` can be set to the number of
  concurrent threads to use for testing.

## Passing `--pass $mode`

Pass UI tests now have three modes, `check-pass`, `build-pass` and `run-pass`.
When `--pass $mode` is passed, these tests will be forced to run under the given
`$mode` unless the directive `//@ ignore-pass` exists in the test file.
For example, you can run all the tests in `tests/ui` as `check-pass`:

```text
./x test tests/ui --pass check
```

By passing `--pass $mode`, you can reduce the testing time.
For each mode, please see [Controlling pass/fail
expectations](ui.md#controlling-passfail-expectations).

## Running tests with different "compare modes"

UI tests may have different output depending on certain "modes" that the compiler is in.
For example, when using the Polonius mode, a test `foo.rs` will
first look for expected output in `foo.polonius.stderr`, falling back to the
usual `foo.stderr` if not found.
The following will run the UI test suite in Polonius mode:

```text
./x test tests/ui --compare-mode=polonius
```

See [Compare modes](compiletest.md#compare-modes) for more details.

## Running tests manually

Sometimes it's easier and faster to just run the test by hand.
Most tests are just `.rs` files, so after [creating a rustup
toolchain](../building/how-to-build-and-run.md#creating-a-rustup-toolchain), you
can do something like:

```text
rustc +stage1 tests/ui/issue-1234.rs
```

This is much faster, but doesn't always work.
For example, some tests include
directives that specify specific compiler flags, or which rely on other crates,
and they may not run the same without those options.

## Running tests on a remote machine

Tests may be run on a remote machine (e.g. to test builds for a different
architecture).
This is done using `remote-test-client` on the build machine to
send test programs to `remote-test-server` running on the remote machine.
`remote-test-server` executes the test programs and sends the results back to the build machine.
`remote-test-server` provides *unauthenticated remote code
execution* so be careful where it is used.

To do this, first build `remote-test-server` for the remote machine
(using RISC-V as an example):

```text
./x build src/tools/remote-test-server --target riscv64gc-unknown-linux-gnu
```

The binary will be created at `./build/host/stage2-tools/$TARGET_ARCH/release/remote-test-server`.
Copy this over to the remote machine.

On the remote machine, run the `remote-test-server` with the `--bind
0.0.0.0:12345` flag (and optionally `--verbose` flag).
Output should look like this:

```console
$ ./remote-test-server --verbose --bind 0.0.0.0:12345
starting test server
listening on 0.0.0.0:12345!
```

Note that binding the server to 0.0.0.0 will allow all hosts able to reach your
machine to execute arbitrary code on your machine.
We strongly recommend either
setting up a firewall to block external access to port 12345, or to use a more
restrictive IP address when binding.

You can test if the `remote-test-server` is working by connecting to it and sending `ping\n`.
It should reply `pong`:

```console
$ nc $REMOTE_IP 12345
ping
pong
```

To run tests using the remote runner, set the `TEST_DEVICE_ADDR` environment
variable then use `x` as usual.
For example, to run `ui` tests for a RISC-V machine with the IP address `1.2.3.4` use

```text
export TEST_DEVICE_ADDR="1.2.3.4:12345"
./x test tests/ui --target riscv64gc-unknown-linux-gnu
```

If `remote-test-server` was run with the verbose flag, output on the test
machine may look something like

```text
[...]
run "/tmp/work/test1007/a"
run "/tmp/work/test1008/a"
run "/tmp/work/test1009/a"
run "/tmp/work/test1010/a"
run "/tmp/work/test1011/a"
run "/tmp/work/test1012/a"
run "/tmp/work/test1013/a"
run "/tmp/work/test1014/a"
run "/tmp/work/test1015/a"
run "/tmp/work/test1016/a"
run "/tmp/work/test1017/a"
run "/tmp/work/test1018/a"
[...]
```

Tests are built on the machine running `x` not on the remote machine.
Tests which fail to build unexpectedly (or `ui` tests producing incorrect build
output) may fail without ever running on the remote machine.

There is a default timeout of 30 minutes in case the `remote-test-server`
cannot be reached by the `x` command. This timeout can be modified by using the
`TEST_DEVICE_CONNECT_TIMEOUT_SECONDS` environment variable.

## Testing on emulators

Some platforms are tested via an emulator for architectures that aren't readily available.
For architectures where the standard library is well supported and
the host operating system supports TCP/IP networking, see the above instructions
for testing on a remote machine (in this case the remote machine is emulated).

There is also a set of tools for orchestrating running the tests within the emulator.
Platforms such as `arm-android` and `arm-unknown-linux-gnueabihf` are
set up to automatically run the tests under emulation on GitHub Actions.
The following will take a look at how a target's tests are run under emulation.

The Docker image for [armhf-gnu] includes [QEMU] to emulate the ARM CPU architecture.
Included in the Rust tree are the tools [remote-test-client] and
[remote-test-server] which are programs for sending test programs and libraries
to the emulator, and running the tests within the emulator, and reading the results.
The Docker image is set up to launch `remote-test-server` and the
build tools use `remote-test-client` to communicate with the server to
coordinate running tests (see [src/bootstrap/src/core/build_steps/test.rs]).

To run on the iOS/tvOS/watchOS/visionOS simulator, we can similarly treat it as a "remote" machine.
A curious detail here is that the network is shared between
the simulator instance and the host macOS, so we can use the local loopback address `127.0.0.1`.
Something like the following should work:

```sh
# Build the test server for the iOS simulator:
./x build src/tools/remote-test-server --target aarch64-apple-ios-sim

# If you already have a simulator instance open, copy the device UUID from:
xcrun simctl list devices booted
UDID=01234567-89AB-CDEF-0123-456789ABCDEF

# Alternatively, create and boot a new simulator instance:
xcrun simctl list runtimes
xcrun simctl list devicetypes
UDID=$(xcrun simctl create $CHOSEN_DEVICE_TYPE $CHOSEN_RUNTIME)
xcrun simctl boot $UDID
# See https://nshipster.com/simctl/ for details.

# Spawn the runner on port 12345:
xcrun simctl spawn $UDID ./build/host/stage2-tools/aarch64-apple-ios-sim/release/remote-test-server -v --bind 127.0.0.1:12345

# In a new terminal, run tests via the runner:
export TEST_DEVICE_ADDR="127.0.0.1:12345"
./x test --host='' --target aarch64-apple-ios-sim --skip tests/debuginfo
# FIXME(madsmtm): Allow debuginfo tests to work (maybe needs `.dSYM` folder to be copied to the target?).
```

[armhf-gnu]: https://github.com/rust-lang/rust/tree/HEAD/src/ci/docker/host-x86_64/armhf-gnu/Dockerfile
[QEMU]: https://www.qemu.org/
[remote-test-client]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/remote-test-client
[remote-test-server]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/remote-test-server
[src/bootstrap/src/core/build_steps/test.rs]: https://github.com/rust-lang/rust/blob/HEAD/src/bootstrap/src/core/build_steps/test.rs

## Testing tests on wasi (wasm32-wasip1)

Some tests are specific to wasm targets.
To run theste tests, you have to pass `--target wasm32-wasip1` to `x test`.
Additionally, you need the wasi sdk.
Follow the install instructions from the [wasi sdk repository] to get a sysroot on your computer.
On the [wasm32-wasip1 target support page] a minimum version is specified that your sdk must be able to build.
Some cmake commands that take a while and give a lot of very concerning c++ warnings...
Then, in `bootstrap.toml`, point to the sysroot like so:

```toml
[target.wasm32-wasip1]
wasi-root = "<wasi-sdk location>/build/sysroot/install/share/wasi-sysroot"
```

In my case I git-cloned it next to my rust folder, so it was `../wasi-sdk/build/....`
Now, tests should just run, you don't have to set up anything else.

[wasi sdk repository]: https://github.com/WebAssembly/wasi-sdk
[wasm32-wasip1 target support page]: https://github.com/rust-lang/rust/blob/HEAD/src/doc/rustc/src/platform-support/wasm32-wasip1.md#building-the-target.


[`tests/ui`]: https://github.com/rust-lang/rust/tree/HEAD/tests/ui


---

# Testing with Docker

The [`src/ci/docker`] directory includes [Docker] image definitions for Linux-based jobs executed on GitHub Actions (non-Linux jobs run outside Docker).
You can run these jobs on your local development machine, which can be
helpful to test environments different from your local system.
You will need to install Docker on a Linux, Windows, or macOS system (typically Linux
will be much faster than Windows or macOS because the latter use virtual
machines to emulate a Linux environment).

Jobs running in CI are configured through a set of bash scripts, and it is not always trivial to reproduce their behavior locally.
If you want to run a CI job locally in the simplest way possible, you can use a provided helper `citool` that tries to replicate what happens on CI as closely as possible:

```bash
cargo run --manifest-path src/ci/citool/Cargo.toml run-local <job-name>
# For example:
cargo run --manifest-path src/ci/citool/Cargo.toml run-local dist-x86_64-linux-alt
```

If the above script does not work for you, you would like to have more control of the Docker image execution, or you want to understand what exactly happens during Docker job execution, then continue reading below.

## The `run.sh` script
The [`src/ci/docker/run.sh`] script is used to build a specific Docker image, run it,
build Rust within the image, and either run tests or prepare a set of archives designed for distribution.
The script will mount your local Rust source tree in read-only mode, and an `obj` directory in read-write mode.
All the compiler artifacts will be stored in the `obj` directory.
The shell will start out in the `obj`directory.
From there, it will execute `../src/ci/run.sh` which starts the build as defined by the Docker image.

You can run `src/ci/docker/run.sh <image-name>` directly.
A few important notes regarding the `run.sh` script:
- When executed on CI, the script expects that all submodules are checked out.
  If some submodule that is accessed by the job is not available, the build will result in an error.
  You should thus make sure that you have all required submodules checked out locally.
  You can either do that manually through git, or set `build.submodules = true` in your `bootstrap.toml` and run a command such as `x build` to let bootstrap download the most important submodules
  Note that this might not be enough for the given CI job that you are trying to execute though.
- `<image-name>` corresponds to a single directory located in one of the `src/ci/docker/host-*` directories.
  Note that image name does not necessarily correspond to a job name, as some jobs execute the same image, but with different environment variables or Docker build arguments
  This is a part of the complexity that makes it difficult to run CI jobs locally.
- If you are executing a "dist" job (job beginning with `dist-`), you should set the `DEPLOY=1` environment variable.
- If you are executing an "alternative dist" job (job beginning with `dist-` and ending with `-alt`), you should set the `DEPLOY_ALT=1` environment variable.
- Some of the std tests require IPv6 support.
  Docker on Linux seems to have it disabled by default.
  Run the commands in [`enable-docker-ipv6.sh`] to enable IPv6 before creating the container.
  This only needs to be done once.

### Interactive mode

Sometimes, it can be useful to build a specific Docker image, and then run custom commands inside it, so that you can experiment with how the given system behaves.
You can do that using an interactive mode, which will
start a bash shell in the container, using `src/ci/docker/run.sh --dev <image-name>`.

When inside the Docker container, you can run individual commands to do specific tasks.
For example, you can run `../x test tests/ui` to just run UI tests.

Some additional notes about using the interactive mode:

- The container will be deleted automatically when you exit the shell, however
  the build artifacts persist in the `obj` directory.
  If you are switching between different Docker images, the artifacts from previous environments
  stored in the `obj` directory may confuse the build system.
  Sometimes you will need to delete parts or all of the `obj` directory before building
  inside the container.
- The container is bare-bones, with only a minimal set of packages.
  You may want to install some things like `apt install less vim`.
- You can open multiple shells in the container.
  First you need the container
  name (a short hash), which is displayed in the shell prompt, or you can run
  `docker container ls` outside of the container to list the available containers.
  With the container name, run `docker exec -it <CONTAINER>
  /bin/bash` where `<CONTAINER>` is the container name like `4ba195e95cef`.

[Docker]: https://www.docker.com/
[`src/ci/docker`]: https://github.com/rust-lang/rust/tree/HEAD/src/ci/docker
[`src/ci/docker/run.sh`]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/docker/run.sh
[`src/ci/run.sh`]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/run.sh
[`enable-docker-ipv6.sh`]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/scripts/enable-docker-ipv6.sh


---

# Testing with CI

The primary goal of our CI system is to ensure that the `main` branch of
`rust-lang/rust` is always in a valid state by passing our test suite.

From a high-level point of view, when you open a pull request at
`rust-lang/rust`, the following will happen:

- A small [subset](#pull-request-builds) of tests and checks are run after each push to the PR.
  This should help catch common errors.
- When the PR is approved, the [bors] bot enqueues the PR into a [merge queue].
- Once the PR gets to the front of the queue, bors will create a merge commit
  and run the [full test suite](#auto-builds) on it.
  The merge commit either contains only one specific PR or it can be a ["rollup"](#rollups) which
  combines multiple PRs together, to reduce CI costs and merge delays.
- Once the whole test suite finishes, two things can happen.
  Either CI fails with an error that needs to be addressed by the developer, or CI succeeds and
  the merge commit is then pushed to the `main` branch.

If you want to modify what gets executed on CI, see [Modifying CI jobs](#modifying-ci-jobs).

## CI workflow

<!-- date-check: Oct 2024 -->

Our CI is primarily executed on [GitHub Actions], with a single workflow defined
in [`.github/workflows/ci.yml`], which contains a bunch of steps that are
unified for all CI jobs that we execute.
When a commit is pushed to a corresponding branch or a PR, the workflow executes the
[`src/ci/citool`] crate, which dynamically generates the specific CI jobs that should be executed.
This script uses the [`jobs.yml`] file as an
input, which contains a declarative configuration of all our CI jobs.

> Almost all build steps shell out to separate scripts. This keeps the CI fairly
> platform independent (i.e., we are not overly reliant on GitHub Actions).
> GitHub Actions is only relied on for bootstrapping the CI process and for
> orchestrating the scripts that drive the process.

In essence, all CI jobs run `./x test`, `./x dist` or some other command with
different configurations, across various operating systems, targets, and platforms.
There are two broad categories of jobs that are executed, `dist` and non-`dist` jobs.

- Dist jobs build a full release of the compiler for a specific platform,
  including all the tools we ship through rustup.
  Those builds are then uploaded
  to the `rust-lang-ci2` S3 bucket and are available to be locally installed
  with the [rustup-toolchain-install-master] tool.
  The same builds are also used
  for actual releases: our release process basically consists of copying those
  artifacts from `rust-lang-ci2` to the production endpoint and signing them.
- Non-dist jobs run our full test suite on the platform, and the test suite of
  all the tools we ship through rustup;
  The amount of stuff we test depends on
  the platform (for example some tests are run only on Tier 1 platforms), and
  some quicker platforms are grouped together on the same builder to avoid wasting CI resources.

Based on an input event (usually a push to a branch), we execute one of three
kinds of builds (sets of jobs).

1. PR builds
2. Auto builds
3. Try builds

[rustup-toolchain-install-master]: https://github.com/kennytm/rustup-toolchain-install-master

### Pull Request builds

After each push to a pull request, a set of `pr` jobs are executed.
Currently, these execute the `x86_64-gnu-llvm-X`, `x86_64-gnu-tools`, `pr-check-1`, `pr-check-2`
and `tidy` jobs, all running on Linux.
These execute a relatively short
(~40 minutes) and lightweight test suite that should catch common issues.
More specifically, they run a set of lints, they try to perform a cross-compile check
build to Windows mingw (without producing any artifacts), and they test the
compiler using a *system* version of LLVM.
Unfortunately, it would take too many
resources to run the full test suite for each commit on every PR.

> **Note on doc comments**
>
> Note that PR CI as of Oct 2024 <!-- datecheck --> by default does not try to
> run `./x doc xxx`. This means that if you have any broken intradoc links that
> would lead to `./x doc xxx` failing, it will happen very late into the full
> merge queue CI pipeline.
>
> Thus, it is a good idea to run `./x doc xxx` locally for any doc comment
> changes to help catch these early.

PR jobs are defined in the `pr` section of [`jobs.yml`].
Their results can be observed
directly on the PR, in the "CI checks" section at the bottom of the PR page.

### Auto builds

Before a commit can be merged into the `main` branch, it needs to pass our complete test suite.
We call this an `auto` build.
This build runs tens of CI jobs that exercise various tests across operating systems and targets.
The full test suite is quite slow;
it can take several hours until all the `auto` CI jobs finish.

Most platforms only run the build steps, some run a restricted set of tests;
only a subset run the full suite of tests (see Rust's [platform tiers]).

Auto jobs are defined in the `auto` section of [`jobs.yml`].
They are executed on the [`automation/bors/auto`][auto] branch under the `rust-lang/rust` repository,
and the final result will be reported via a comment made by bors on the corresponding PR.
The live results can be seen on [the GitHub Actions workflows page].

At any given time, at most a single `auto` build is being executed.
Find out more in [Merging PRs serially with bors](#merging-prs-serially-with-bors).

Normally, when an auto job fails, the whole CI workflow immediately ends.
However, it can be useful to
create auto jobs that are "non-blocking", or optional, to test them on CI for some time before blocking
merges on them.
This can be useful if those jobs can be flaky.

To do that, prefix such a job with `optional-`, and set `continue_on_error: true` for it in [`jobs.yml`].

[platform tiers]: https://forge.rust-lang.org/release/platform-support.html#rust-platform-support
[auto]: https://github.com/rust-lang/rust/tree/automation/bors/auto

### Try builds

Sometimes we want to run a subset of the test suite on CI for a given PR, or
build a set of compiler artifacts from that PR, without attempting to merge it.
We call this a "try build".
A try build is started after a user with the proper
permissions posts a PR comment with the `@bors try` command.

There are several use-cases for try builds:

- Run a set of performance benchmarks using our [rustc-perf] benchmark suite.
  For this, a working compiler build is needed, which can be generated with a
  try build that runs the [dist-x86_64-linux] CI job, which builds an optimized
  version of the compiler on Linux (this job is currently executed by default
  when you start a try build).
  To create a try build and schedule it for a
  performance benchmark, you can use the `@bors try @rust-timer queue` command combination.
- Check the impact of the PR across the Rust ecosystem, using a [Crater](crater.md) run.
  Again, a working compiler build is needed for this, which can be produced by
  the [dist-x86_64-linux] CI job.
- Run a specific CI job (e.g. Windows tests) on a PR, to quickly test if it
  passes the test suite executed by that job.

By default, if you send a comment with `@bors try`, the jobs defined in the `try` section of
[`jobs.yml`] will be executed.
We call this mode a "fast try build".
Such a try build will not execute any tests, and it will allow compilation warnings.
It is useful when you want to
get an optimized toolchain as fast as possible, for a Crater run or performance benchmarks,
even if it might not be working fully correctly.

The CI job executed in fast try builds has a special suffix (`-quick`),
to distinguish it from a full build of the default try job.
If you want to do the full build instead,
specify its job name in a job pattern (explained below).

If you want to run custom CI jobs in a try build and make sure that they pass all tests and do
not produce any compilation warnings, you can select CI jobs to be executed by specifying a *job pattern*,
which can be used in one of two ways:
- You can add a set of `try-job: <job pattern>` directives to the PR description (described below) and then
  simply run `@bors try`.
  CI will read these directives and run the jobs that you have specified.
  This is
  useful if you want to rerun the same set of try jobs multiple times, after incrementally modifying a PR.
- You can specify the job pattern using the `jobs` parameter of the try command: `@bors try jobs=<job pattern>`.
  This is useful for one-off try builds with specific jobs.
  Note that the `jobs` parameter has a higher priority than the PR description directives.
  - There can also be multiple patterns specified, e.g. `@bors try jobs=job1,job2,job3`.

Each job pattern can either be an exact name of a job or a glob pattern that matches multiple jobs,
for example `*msvc*` or `*-alt`.
You can start at most 20 jobs in a single try build.
When using
glob patterns in the PR description, you can optionally wrap them in backticks (`` ` ``) to avoid GitHub rendering
the pattern as Markdown if it contains e.g. an asterisk. Note that this escaping will not work when using
the `@bors jobs=` parameter.

The job pattern needs to match one or more jobs defined in the `auto` or `optional` sections
of [`jobs.yml`]:

- `auto` jobs are executed before a commit is merged into the `main` branch.
- `optional` jobs are executed only when explicitly requested via a try build.
  They are typically used for tier 2 and tier 3 targets.

One reason to do a try build is to do a perf run, as described above, with `@rust-timer queue`.
This perf build then compares against some commit on main.
With `@bors try parent=<sha>` you can base your try build and subsequent perf run on a specific commit on `main`,
to help make the perf comparison as fair as possible.

> **Using `try-job` PR description directives**
>
> 1. Identify which set of try-jobs you would like to exercise. You can
>    find the name of the CI jobs in [`jobs.yml`].
>
> 2. Amend PR description to include a set of patterns (usually at the end
>    of the PR description), for example:
>
>    ```text
>    This PR fixes #123456.
>
>    try-job: x86_64-msvc
>    try-job: test-various
>    try-job: `*-alt`
>    ```
>
>    Each `try-job` pattern must be on its own line.
>
> 3. Run the prescribed try jobs with `@bors try`. As aforementioned, this
>    requires the user to either (1) have `try` permissions or (2) be delegated
>    with `try` permissions by `@bors delegate=try` by someone who has `try`
>    permissions.
>
> Note that this is usually easier to do than manually edit [`jobs.yml`].
> However, it can be less flexible because you cannot adjust the set of tests
> that are exercised this way.

Try builds are executed on the [`automation/bors/try`][try] branch under the `rust-lang/rust` repository and
their results can be seen on [the GitHub Actions workflows page],
although usually you will be notified of the result by a comment made by bors on
the corresponding PR.

Multiple try builds can execute concurrently across different PRs, but there can be at most
a single try build running on a single PR at any given time.

[rustc-perf]: https://github.com/rust-lang/rustc-perf
[try]: https://github.com/rust-lang/rust/tree/automation/bors/try

### Modifying CI jobs

If you want to modify what gets executed on our CI, you can simply modify the
`pr`, `auto` or `try` sections of the [`jobs.yml`] file.

You can also modify what gets executed temporarily, for example to test a
particular platform or configuration that is challenging to test locally (for
example, if a Windows build fails, but you don't have access to a Windows machine).
Don't hesitate to use CI resources in such situations.

You can perform an arbitrary CI job in two ways:
- Use the [try build](#try-builds) functionality, and specify the CI jobs that
  you want to be executed in try builds in your PR description.
- Modify the [`pr`](#pull-request-builds) section of `jobs.yml` to specify which
  CI jobs should be executed after each push to your PR.
  This might be faster than repeatedly starting try builds.

To modify the jobs executed after each push to a PR, you can simply copy one of
the job definitions from the `auto` section to the `pr` section.
For example, the `x86_64-msvc` job is responsible for running the 64-bit MSVC tests.
You can copy it to the `pr` section to cause it to be executed after a commit is pushed
to your PR, like this:

```yaml
pr:
  ...
  - image: x86_64-gnu-tools
    <<: *job-linux-16c
  # this item was copied from the `auto` section
  # vvvvvvvvvvvvvvvvvv
  - image: x86_64-msvc
    env:
      RUST_CONFIGURE_ARGS: --build=x86_64-pc-windows-msvc --enable-profiler
      SCRIPT: make ci-msvc
    <<: *job-windows-8c
```

Then you can commit the file and push it to your PR branch on GitHub.
GitHub Actions should then execute this CI job after each push to your PR.

<div class="warning">

**After you have finished your experiments, don't forget to remove any changes
you have made to `jobs.yml`, if they were supposed to be temporary!**

A good practice is to prefix `[WIP]` in PR title while still running try jobs
and `[DO NOT MERGE]` in the commit that modifies the CI jobs for testing purposes.
</div>

Although you are welcome to use CI, just be conscious that this is a shared
resource with limited concurrency.
Try not to enable too many jobs at once;
one or two should be sufficient in most cases.

## Merging PRs serially with bors

CI services usually test the last commit of a branch merged with the last commit
in `main`, and while that’s great to check if the feature works in isolation,
it doesn’t provide any guarantee the code is going to work once it’s merged.
Breakages like these usually happen when another, incompatible PR is merged
after the build happened.

To ensure a `main` branch that works all the time, we forbid manual merges.
Instead, all PRs have to be approved through our bot, [bors].
All the approved PRs are put in a [merge queue]
(sorted by priority and creation date) and are automatically tested one at the time.
If all the builders are green, the PR is merged, otherwise the failure is
recorded and the PR will have to be re-approved again.

Bors doesn’t interact with CI services directly, but it works by pushing the
merge commit it wants to test to specific branches (like `automation/bors/auto` or `automation/bors/try`),
which are configured to execute CI checks.
Bors then detects the outcome of the build by listening for either Commit Statuses or Check Runs.
Since the merge commit is
based on the latest `main` and only one can be tested at the same time, when
the results are green, `main` is fast-forwarded to that merge commit.

Unfortunately, testing a single PR at a time, combined with our long CI (~2
hours for a full run), means we can’t merge a lot of PRs in a single day, and a
single failure greatly impacts our throughput.
The maximum number of PRs we can merge in a day is around ~10.

The long CI run times, and requirement for a large builder pool, is largely due
to the fact that full release artifacts are built in the `dist-` builders.
This is worth it because these release artifacts:

- Allow perf testing even at a later date.
- Allow bisection when bugs are discovered later.
- Ensure release quality since if we're always releasing, we can catch problems early.

### Rollups

Some PRs don’t need the full test suite to be executed: trivial changes like
typo fixes or README improvements *shouldn’t* break the build, and testing every
single one of them for 2+ hours would be wasteful.
To solve this, we regularly create a "rollup", a PR where we merge several pending trivial PRs so
they can be tested together.
Rollups are created manually by a team member using
the "create a rollup" button on the [merge queue].
The team member uses their judgment to decide if a PR is risky or not.

## Docker

All CI jobs, except those on macOS and Windows, are executed inside that
platform’s custom [Docker container].
This has a lot of advantages for us:

- The build environment is consistent regardless of the changes of the
  underlying image (switching from the trusty image to xenial was painless for us).
- We can use ancient build environments to ensure maximum binary compatibility,
  for example [using older CentOS releases][dist-x86_64-linux] on our Linux builders.
- We can avoid reinstalling tools (like QEMU or the Android emulator) every time,
  thanks to Docker image caching.
- Users can run the same tests in the same environment locally by just running this command:

      cargo run --manifest-path src/ci/citool/Cargo.toml run-local <job-name>

  This is helpful for debugging failures.
  Note that there are only Linux Docker images available locally due to licensing and
  other restrictions.

The Docker images prefixed with `dist-` are used for building artifacts while
those without that prefix run tests and checks.

We also run tests for less common architectures (mainly Tier 2 and Tier 3 platforms) in CI.
Since those platforms are not x86, we either run everything
inside QEMU, or we just cross-compile if we don’t want to run the tests for that platform.

These builders are running on a special pool of builders set up and maintained for us by GitHub.

[Docker container]: https://github.com/rust-lang/rust/tree/HEAD/src/ci/docker

## Caching

Our CI workflow uses various caching mechanisms, mainly for two things:

### Docker images caching

The Docker images we use to run most of the Linux-based builders take a *long* time to fully build.
To speed up the build, we cache them using [Docker registry
caching], with the intermediate artifacts being stored on [ghcr.io].
We also push the built Docker images to ghcr, so that they can be reused by other tools
(rustup) or by developers running the Docker build locally (to speed up their build).

Since we test multiple, diverged branches (`main`, `beta` and `stable`), we
can’t rely on a single cache for the images, otherwise builds on a branch would
override the cache for the others.
Instead, we store the images under different
tags, identifying them with a custom hash made from the contents of all the
Dockerfiles and related scripts.

The CI calculates a hash key, so that the cache of a Docker image is
invalidated if one of the following changes:

- Dockerfile
- Files copied into the Docker image in the Dockerfile
- The architecture of the GitHub runner (x86 or ARM)

[ghcr.io]: https://github.com/rust-lang/rust/pkgs/container/rust-ci
[Docker registry caching]: https://docs.docker.com/build/cache/backends/registry/

### LLVM caching with Sccache

We build some C/C++ stuff in various CI jobs, and we rely on [Sccache] to cache
the intermediate LLVM artifacts.
Sccache is a distributed ccache developed by
Mozilla, which can use an object storage bucket as the storage backend.

With Sccache there's no need to calculate the hash key ourselves.
Sccache invalidates the cache automatically when it detects changes to relevant inputs,
such as the source code, the version of the compiler, and important environment variables.
So we just pass the Sccache wrapper on top of Cargo and Sccache does the rest.

We store the persistent artifacts on the S3 bucket, `rust-lang-ci-sccache2`.
So when the CI runs, if Sccache sees that LLVM is being compiled with the same C/C++
compiler and the LLVM source code is the same, Sccache retrieves the individual
compiled translation units from S3.

[sccache]: https://github.com/mozilla/sccache

## Custom tooling around CI

During the years, we developed some custom tooling to improve our CI experience.

### Rust Log Analyzer to show the error message in PRs

The build logs for `rust-lang/rust` are huge, and it’s not practical to find
what caused the build to fail by looking at the logs.
We therefore developed a bot called [Rust Log Analyzer][rla] (RLA) that
receives the build logs on failure, and extracts the error message automatically,
posting it on the PR thread.

The bot is not hardcoded to look for error strings, but was trained with a bunch
of build failures to recognize which lines are common between builds and which are not.
While the generated snippets can be weird sometimes, the bot is pretty
good at identifying the relevant lines, even if it’s an error we've never seen before.

[rla]: https://github.com/rust-lang/rust-log-analyzer

### Toolstate to support allowed failures

The `rust-lang/rust` repo doesn’t only test the compiler on its CI, but also a
variety of tools and documentation.
Some documentation is pulled in via git submodules.
If we blocked merging rustc PRs on the documentation being fixed, we
would be stuck in a chicken-and-egg problem, because the documentation's CI
would not pass since updating it would need the not-yet-merged version of rustc
to test against (and we usually require CI to be passing).

To avoid the problem, submodules are allowed to fail, and their status is
recorded in [rust-toolstate].
When a submodule breaks, a bot automatically pings
the maintainers so they know about the breakage, and it records the failure on
the toolstate repository.
The release process will then ignore broken tools on
nightly, removing them from the shipped nightlies.

While tool failures are allowed most of the time, they’re automatically
forbidden a week before a release: we don’t care if tools are broken on nightly
but they must work on beta and stable, so they also need to work on nightly a
few days before we promote nightly to beta.

More information is available in the [toolstate documentation].

[rust-toolstate]: https://rust-lang-nursery.github.io/rust-toolstate
[toolstate documentation]: https://forge.rust-lang.org/infra/toolstate.html

## Public CI dashboard

To monitor the Rust CI, you can have a look at the [public dashboard] maintained by the infra team.

These are some useful panels from the dashboard:

- Pipeline duration: check how long the auto builds take to run.
- Top slowest jobs: check which jobs are taking the longest to run.
- Change in median job duration: check what jobs are slowest than before. Useful
  to detect regressions.
- Top failed jobs: check which jobs are failing the most.

To learn more about the dashboard, see the [Datadog CI docs].

[Datadog CI docs]: https://docs.datadoghq.com/continuous_integration/
[public dashboard]: https://p.datadoghq.com/sb/3a172e20-e9e1-11ed-80e3-da7ad0900002-b5f7bb7e08b664a06b08527da85f7e30

## Determining the CI configuration

If you want to determine which `bootstrap.toml` settings are used in CI for a
particular job, it is probably easiest to just look at the build log.
To do this:

1. Go to [the Rust CI successful workflow runs page][workflow runs]
   and click on the most recent one.
2. Choose the job you are interested in on the left-hand side.
3. Click on the gear icon and choose "View raw logs"
4. Search for the string "Configure the build"
5. All of the build settings are listed on the line with the text, `build.configure-args`

[GitHub Actions]: https://github.com/rust-lang/rust/actions
[`jobs.yml`]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/github-actions/jobs.yml
[`.github/workflows/ci.yml`]: https://github.com/rust-lang/rust/blob/HEAD/.github/workflows/ci.yml
[`src/ci/citool`]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/citool
[bors]: https://github.com/rust-lang/bors
[merge queue]: https://bors.rust-lang.org/queue/rust
[dist-x86_64-linux]: https://github.com/rust-lang/rust/blob/HEAD/src/ci/docker/host-x86_64/dist-x86_64-linux/Dockerfile
[the GitHub Actions workflows page]: https://github.com/rust-lang/rust/actions
[workflow runs]: https://github.com/rust-lang/rust/actions?query=branch%3Aautomation%2Fbors%2Fauto+is%3Asuccess


---

# Adding new tests

**In general, we expect every PR that fixes a bug in rustc to come accompanied
by a regression test of some kind.** This test should fail in `main` but pass
after the PR.
These tests are really useful for preventing us from repeating the
mistakes of the past.

The first thing to decide is which kind of test to add.
This will depend on the nature of the change and what you want to exercise.
Here are some rough guidelines:

- The majority of compiler tests are done with [compiletest].
  - The majority of compiletest tests are [UI](ui.md) tests in the [`tests/ui`]
    directory.
- Changes to the standard library are usually tested within the standard library
  itself.
  - The majority of standard library tests are written as doctests, which
    illustrate and exercise typical API behavior.
  - Additional [unit tests](intro.md#package-tests) should go in
    `library/${crate}/tests` (where `${crate}` is usually `std`).
  - Tests for the `alloc` or `core` crates must go in separate crates: `alloctests` or `coretests` respectively.
    - NOTE: That when adding unit tests for unstable features the `#![feature(...)]`
      declaration must be added to `library/${crate}tests/tests/lib.rs` and not to
      `library/${crate}tests/lib.rs`.
- If the code is part of an isolated system, and you are not testing compiler
  output, consider using a [unit or integration test](intro.md#package-tests).
- Need to run rustdoc?
  Prefer a `rustdoc` or `rustdoc-ui` test.
  Occasionally you'll need `rustdoc-js` as well.
- Other compiletest test suites are generally used for special purposes:
  - Need to run gdb or lldb?
    Use the `debuginfo` test suite.
  - Need to inspect LLVM IR or MIR IR?
    Use the `codegen` or `mir-opt` test suites.
  - Need to inspect the resulting binary in some way?
    Or if all the other test suites are too limited for your purposes?
    Then use `run-make`.
    - Use `run-make-cargo` if you need to exercise in-tree `cargo` in conjunction
      with in-tree `rustc`.
  - Check out the [compiletest] chapter for more specialized test suites.

After deciding on which kind of test to add, see [best
practices](best-practices.md) for guidance on how to author tests that are easy
to work with that stand the test of time (i.e. if a test fails or need to be
modified several years later, how can we make it easier for them?).

[compiletest]: compiletest.md
[`tests/ui`]: https://github.com/rust-lang/rust/tree/HEAD/tests/ui/

## UI test walkthrough

The following is a basic guide for creating a [UI test](ui.md), which is one of
the most common compiler tests.
For this tutorial, we'll be adding a test for an async error message.

### Step 1: Add a test file

The first step is to create a Rust source file somewhere in the [`tests/ui`]
tree.
When creating a test, do your best to find a good location and name (see
[Test organization](ui.md#test-organization) for more).
Since naming is the
hardest part of development, everything should be downhill from here!

Let's place our async test at `tests/ui/async-await/await-without-async.rs`:

```rust,ignore
// Provide diagnostics when the user writes `await` in a non-`async` function.
//@ edition:2018

async fn foo() {}

fn bar() {
    foo().await
}

fn main() {}
```

A few things to notice about our test:

- The top should start with a short comment that [explains what the test is
  for](#explanatory_comment).
- The `//@ edition:2018` comment is called a [directive](directives.md) which
  provides instructions to compiletest on how to build the test.
  Here we need to
  set the edition for `async` to work (the default is edition 2015).
- Following that is the source of the test.
  Try to keep it succinct and to the point.
  This may require some effort if you are trying to minimize an example
  from a bug report.
- We end this test with an empty `fn main` function.
  This is because the default
  for UI tests is a `bin` crate-type, and we don't want the "main not found"
  error in our test.
  Alternatively, you could add `#![crate_type="lib"]`.

### Step 2: Generate the expected output

The next step is to create the expected output snapshots from the compiler.
This can be done with the `--bless` option:

```sh
./x test tests/ui/async-await/await-without-async.rs --bless
```

This will build the compiler (if it hasn't already been built), compile the
test, and place the output of the compiler in a file called
`tests/ui/async-await/await-without-async.stderr`.

However, this step will fail!
You should see an error message, something like this:

> error: /rust/tests/ui/async-await/await-without-async.rs:7: unexpected
> error: '7:10: 7:16: `await` is only allowed inside `async` functions and
> blocks E0728'

This is because the stderr contains errors which were not matched by error
annotations in the source file.

### Step 3: Add error annotations

Every error needs to be annotated with a comment in the source with the text of
the error.
In this case, we can add the following comment to our test file:

```rust,ignore
fn bar() {
    foo().await
    //~^ ERROR `await` is only allowed inside `async` functions and blocks
}
```

The `//~^` squiggle caret comment tells compiletest that the error belongs to
the *previous* line (more on this in the [Error
annotations](ui.md#error-annotations) section).

Save that, and run the test again:

```sh
./x test tests/ui/async-await/await-without-async.rs
```

It should now pass, yay!

### Step 4: Review the output

Somewhat hand-in-hand with the previous step, you should inspect the `.stderr`
file that was created to see if it looks like how you expect.
If you are adding a new diagnostic message,
now would be a good time to also consider how readable the message looks overall,
particularly for people new to Rust.

Our example `tests/ui/async-await/await-without-async.stderr` file should look
like this:

```text
error[E0728]: `await` is only allowed inside `async` functions and blocks
  --> $DIR/await-without-async.rs:7:10
   |
LL | fn bar() {
   |    --- this is not `async`
LL |     foo().await
   |          ^^^^^^ only allowed inside `async` functions and blocks

error: aborting due to previous error

For more information about this error, try `rustc --explain E0728`.
```

You may notice some things look a little different than the regular compiler
output.

- The `$DIR` removes the path information which will differ between systems.
- The `LL` values replace the line numbers.
  That helps avoid small changes in the source from triggering large diffs.
  See the [Normalization](ui.md#normalization) section for more.

Around this stage, you may need to iterate over the last few steps a few times
to tweak your test, re-bless the test, and re-review the output.

### Step 5: Check other tests

Sometimes when adding or changing a diagnostic message, this will affect other
tests in the test suite.
The final step before posting a PR is to check if you
have affected anything else.
Running the UI suite is usually a good start:

```sh
./x test tests/ui
```

If other tests start failing, you may need to investigate what has changed and
if the new output makes sense.

You may also need to re-bless the output with the `--bless` flag.

<a id="explanatory_comment"></a>

## Comment explaining what the test is about

The first comment of a test file should **summarize the point of the test**, and
highlight what is important about it.
If there is an issue number associated with the test, include the issue number.

This comment doesn't have to be super extensive.
Just something like the following might be enough:
"Regression test for #18060: match arms were matching in the wrong order".

These comments are very useful to others later on when your test breaks, since
they often can highlight what the problem is.
They are also useful if for some
reason the tests need to be refactored, since they let others know which parts
of the test were important.
Often a test must be rewritten because it no longer
tests what it was meant to test, and then it's useful to know what it *was*
meant to test exactly.


---

# Best practices for writing tests

This chapter describes best practices related to authoring and modifying tests.
We want to make sure the tests we author are easy to understand and modify, even
several years later, without needing to consult the original author and perform
a bunch of git archeology.

It's good practice to review the test that you authored by pretending that you
are a different contributor who is looking at the test that failed several years
later without much context (this also helps yourself even a few days or months later!).
Then ask yourself: how can I make my life and their lives easier?

To help put this into perspective, let's start with an aside on how to write a
test that makes the life of another contributor as hard as possible.

> **Aside: Simple Test Sabotage Field Manual**
>
> To make the life of another contributor as hard as possible, one might:
>
> - Name the test after an issue number alone without any other context, e.g.
>   `issue-123456.rs`.
> - Have no comments at all on what the test is trying to exercise, no links to
>   relevant context.
> - Include a test that is massive (that can otherwise be minimized) and
>   contains non-essential pieces which distracts from the core thing the test
>   is actually trying to test.
> - Include a bunch of unrelated syntax errors and other errors which are not
>   critical to what the test is trying to check.
> - Weirdly format the snippets.
> - Include a bunch of unused and unrelated features.
> - Have e.g. `ignore-windows` [compiletest directives] but don't offer any
>   explanation as to *why* they are needed.

## Test naming

Make it easy for the reader to immediately understand what the test is
exercising, instead of having to type in the issue number and dig through github
search for what the test is trying to exercise.
This has an additional benefit
of making the test possible to be filtered via `--test-args` as a collection of related tests.

- Name the test after what it's trying to exercise or prevent regressions of.
- Keep it concise.
- Avoid using issue numbers alone as test names.
- Avoid starting the test name with `issue-xxxxx` prefix as it degrades auto-completion.

> **Avoid using only issue numbers as test names**
>
> Prefer including them as links or `#123456` in test comments instead. Or if it
> makes sense to include the issue number, also include brief keywords like
> `macro-external-span-ice-123956.rs`.
>
> ```text
> tests/ui/typeck/issue-123456.rs                              // bad
> tests/ui/typeck/issue-123456-asm-macro-external-span-ice.rs  // bad (for tab completion)
> tests/ui/typeck/asm-macro-external-span-ice-123456.rs        // good
> tests/ui/typeck/asm-macro-external-span-ice.rs               // good
> ```
>
> `issue-123456.rs` does not tell you immediately anything about what the test
> is actually exercising meaning you need to do additional searching. Including
> the issue number in the test name as a prefix makes tab completion less useful
> (if you `ls` a test directory and get a bunch of `issue-xxxxx` prefixes). We
> can link to the issue in a test comment.
>
> ```rs
> //! Check that `asm!` macro including nested macros that come from external
> //! crates do not lead to a codepoint boundary assertion ICE.
> //!
> //! Regression test for <https://github.com/rust-lang/rust/issues/123456>.
> ```
>
> One exception to this rule is [crash tests]: there it is canonical that
> tests are named only after issue numbers because its purpose is to track
> snippets from which issues no longer ICE/crash, and they would either be
> removed or converted into proper ui/other tests in the fix PRs.

## Test organization

- For most test suites, try to find a semantically meaningful subdirectory to home the test.
    - E.g. for an implementation of RFC 2093 specifically, we can group a
      collection of tests under `tests/ui/rfc-2093-infer-outlives/`.
      For the directory name, include what the RFC is about.
- For the [`run-make`]/`run-make-support` test suites, each `rmake.rs` must
  be contained within an immediate subdirectory under `tests/run-make/` or
  `tests/run-make-cargo/` respectively.
  Further nesting is not presently supported.
  Avoid using _only_ an issue number for the test name as well.

## Test descriptions

To help other contributors understand what the test is about if their changes
lead to the test failing, we should make sure a test has sufficient docs about
its intent/purpose, links to relevant context (including issue numbers or other discussions)
and possibly relevant resources (e.g. it can be helpful to link to
Win32 APIs for specific behavior).

**Synopsis of a test with good comments**

```rust,ignore
//! Brief summary of what the test is exercising.
//! Example: Regression test for #123456: make sure coverage attribute don't ICE
//!     when applied to non-items.
//!
//! Optional: Remarks on related tests/issues, external APIs/tools, crash
//!     mechanism, how it's fixed, FIXMEs, limitations, etc.
//! Example: This test is like `tests/attrs/linkage.rs`, but this test is
//!     specifically checking `#[coverage]` which exercises a different code
//!     path. The ICE was triggered during attribute validation when we tried
//!     to construct a `def_path_str` but only emitted the diagnostic when the
//!     platform is windows, causing an ICE on unix.
//!
//! Links to relevant issues and discussions. Examples below:
//! Regression test for <https://github.com/rust-lang/rust/issues/123456>.
//! See also <https://github.com/rust-lang/rust/issues/101345>.
//! See discussion at <https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler/topic/123456-example-topic>.
//! See [`clone(2)`].
//!
//! [`clone(2)`]: https://man7.org/linux/man-pages/man2/clone.2.html

//@ ignore-windows
// Reason: (why is this test ignored for windows? why not specifically
// windows-gnu or windows-msvc?)

// Optional: Summary of test cases: What positive cases are checked?
// What negative cases are checked? Any specific quirks?

fn main() {
    #[coverage]
    //~^ ERROR coverage attribute can only be applied to function items.
    let _ = {
        // Comment highlighting something that deserves reader attention.
        fn foo() {}
    };
}
```

For how much context/explanation is needed, it is up to the author and reviewer's discretion.
A good rule of thumb is non-trivial things exercised in
the test deserves some explanation to help other contributors to understand.
This may include remarks on:

- How an ICE can get triggered if it's quite elaborate.
- Related issues and tests (e.g. this test is like another test but is kept
  separate because...).
- Platform-specific behaviors.
- Behavior of external dependencies and APIs: syscalls, linkers, tools,
  environments and the like.

## Test content

- Try to make sure the test is as minimal as possible.
- Minimize non-critical code and especially minimize unnecessary syntax and type
  errors which can clutter stderr snapshots.
- Use `#![allow(...)]` or `#![expect(...)]` to suppress unrelated warnings.
- Where possible, use semantically meaningful names (e.g. `fn
  bare_coverage_attributes() {}`).

## Flaky tests

All tests need to strive to be reproducible and reliable.
Flaky tests are the worst kind of tests, arguably even worse than not having the test in the first
place.

- Flaky tests can fail in completely unrelated PRs which can confuse other
  contributors and waste their time trying to figure out if test failure is related.
- Flaky tests provide no useful information from its test results other than
  it's flaky and not reliable: if a test passed but it's flakey, did I just get lucky?
  If a test is flakey but it failed, was it just spurious?
- Flaky tests degrade confidence in the whole test suite.
  If a test suite can
  randomly spuriously fail due to flaky tests, did the whole test suite pass or
  did I just get lucky/unlucky?
- Flaky tests can randomly fail in full CI, wasting previous full CI resources.

## Compiletest directives

See [compiletest directives] for a listing of directives.

- For `ignore-*`/`needs-*`/`only-*` directives, unless extremely obvious,
  provide a brief remark on why the directive is needed. E.g. `"//@ ignore-wasi
  (wasi codegens the main symbol differently)"`.
- When using `//@ ignore-auxiliary`, specify the corresponding main test files,
  e.g. ``//@ ignore-auxiliary (used by `./foo.rs`)``.

## FileCheck best practices

See [LLVM FileCheck guide][FileCheck] for details.

- Avoid matching on specific register numbers or basic block numbers unless
  they're special or critical for the test.
  Consider using patterns to match them where suitable.

> **TODO**
>
> Pending concrete advice.

[compiletest]: ./compiletest.md
[compiletest directives]: ./directives.md
[`run-make`]: ./compiletest.md#run-make-tests
[FileCheck]: https://llvm.org/docs/CommandGuide/FileCheck.html
[crash tests]: ./compiletest.md#crash-tests


---

# Compiletest

## Introduction

`compiletest` is the main test harness of the Rust test suite.
It allows test authors to organize large numbers of tests (the Rust compiler has many
thousands), efficient test execution (parallel execution is supported), and
allows the test author to configure behavior and expected results of both
individual and groups of tests.

> **Note for macOS users**
>
> For macOS users, `SIP` (System Integrity Protection) [may consistently check
> the compiled binary by sending network requests to Apple][zulip], so you may
> get a huge performance degradation when running tests.
>
> You can resolve it by tweaking the following settings: `Privacy & Security ->
> Developer Tools -> Add Terminal (Or VsCode, etc.)`.

[zulip]: https://rust-lang.zulipchat.com/#narrow/stream/182449-t-compiler.2Fhelp/topic/.E2.9C.94.20Is.20there.20any.20performance.20issue.20for.20MacOS.3F

`compiletest` may check test code for compile-time or run-time success/failure.

Tests are typically organized as a Rust source file with annotations in comments
before and/or within the test code.
These comments serve to direct `compiletest`
on if or how to run the test, what behavior to expect, and more.
See [directives](directives.md) and the test suite documentation below for more details
on these annotations.

See the [Adding new tests](adding.md) and [Best practices](best-practices.md)
chapters for a tutorial on creating a new test and advice on writing a good
test, and the [Running tests](running.md) chapter on how to run the test suite.

Arguments can be passed to compiletest using `--test-args` or by placing them after `--`, e.g.
- `x test --test-args --force-rerun`
- `x test -- --force-rerun`

Additionally, bootstrap accepts several common arguments directly, e.g.

`x test --no-capture --force-rerun --run --pass`.

Compiletest itself tries to avoid running tests when the artifacts that are
involved (mainly the compiler) haven't changed.
You can use `x test --test-args
--force-rerun` to rerun a test even when none of the inputs have changed.

## Test suites

All of the tests are in the [`tests`] directory.
The tests are organized into "suites", with each suite in a separate subdirectory.
Each test suite behaves a
little differently, with different compiler behavior and different checks for correctness.
For example, the [`tests/incremental`] directory contains tests for incremental compilation.
The various suites are defined in
[`src/tools/compiletest/src/common.rs`] in the `pub enum Mode` declaration.

The following test suites are available, with links for more information:

[`tests`]: https://github.com/rust-lang/rust/blob/HEAD/tests
[`src/tools/compiletest/src/common.rs`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest/src/common.rs

### Compiler-specific test suites

| Test suite                                | Purpose                                                                                                             |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [`ui`](ui.md)                             | Check the stdout/stderr snapshots from the compilation and/or running the resulting executable                      |
| `ui-fulldeps`                             | `ui` tests which require a linkable build of `rustc` (such as using `extern crate rustc_span;` or used as a plugin) |
| [`pretty`](#pretty-printer-tests)         | Check pretty printing                                                                                               |
| [`incremental`](#incremental-tests)       | Check incremental compilation behavior                                                                              |
| [`debuginfo`](#debuginfo-tests)           | Check debuginfo generation running debuggers                                                                        |
| [`codegen-*`](#codegen-tests)             | Check code generation                                                                                               |
| [`codegen-units`](#codegen-units-tests)   | Check codegen unit partitioning                                                                                     |
| [`assembly`](#assembly-tests)             | Check assembly output                                                                                               |
| [`mir-opt`](#mir-opt-tests)               | Check MIR generation and optimizations                                                                              |
| [`coverage`](#coverage-tests)             | Check coverage instrumentation                                                                                      |
| [`coverage-run-rustdoc`](#coverage-tests) | `coverage` tests that also run instrumented doctests                                                                |
| [`crashes`](#crash-tests)               | Check that the compiler ICEs/panics/crashes on certain inputs to catch accidental fixes                             |

### General purpose test suite

[`run-make`](#run-make-tests) are general purpose tests using Rust programs.

### The build-std test suite

[`build-std`](#build-std-tests) tests that -Zbuild-std works.

### Rustdoc test suites

| Test suite                           | Purpose                                                                  |
|--------------------------------------|--------------------------------------------------------------------------|
| [`rustdoc-html`][rustdoc-html-tests]      | Check HTML output of `rustdoc`                                           |
| [`rustdoc-gui`][rustdoc-gui-tests]   | Check `rustdoc`'s GUI using a web browser                                |
| [`rustdoc-js`][rustdoc-js-tests]     | Check `rustdoc`'s search engine and index                                |
| [`rustdoc-js-std`][rustdoc-js-tests] | Check `rustdoc`'s search engine and index on the std library docs        |
| [`rustdoc-json`][rustdoc-json-tests] | Check JSON output of `rustdoc`                                           |
| `rustdoc-ui`                         | Check terminal output of `rustdoc` ([see also](ui.md))                   |

Some rustdoc-specific tests can also be found in `ui/rustdoc/`.
These tests ensure that certain lints that are emitted as part of executing rustdoc
are also run when executing rustc.
Run-make tests pertaining to rustdoc are typically named `run-make/rustdoc-*/`.

[rustdoc-html-tests]: ../rustdoc-internals/rustdoc-html-test-suite.md
[rustdoc-gui-tests]: ../rustdoc-internals/rustdoc-gui-test-suite.md
[rustdoc-js-tests]: ../rustdoc-internals/search.md#testing-the-search-engine
[rustdoc-json-tests]: ../rustdoc-internals/rustdoc-json-test-suite.md

### Pretty-printer tests

The tests in [`tests/pretty`] exercise the "pretty-printing" functionality of `rustc`.
The `-Z unpretty` CLI option for `rustc` causes it to translate the
input source into various different formats, such as the Rust source after macro expansion.

The pretty-printer tests have several [directives](directives.md) described below.
These commands can significantly change the behavior of the test, but the
default behavior without any commands is to:

1. Run `rustc -Zunpretty=normal` on the source file.
2. Run `rustc -Zunpretty=normal` on the output of the previous step.
3. The output of the previous two steps should be the same.
4. Run `rustc -Zno-codegen` on the output to make sure that it can type check
   (similar to `cargo check`).

If any of the commands above fail, then the test fails.

The directives for pretty-printing tests are:

- `pretty-mode` specifies the mode pretty-print tests should run in (that is,
  the argument to `-Zunpretty`).
  The default is `normal` if not specified.
- `pretty-compare-only` causes a pretty test to only compare the pretty-printed
  output (stopping after step 3 from above).
  It will not try to compile the expanded output to type check it.
  This is needed for a pretty-mode that does
  not expand to valid Rust, or for other situations where the expanded output cannot be compiled.
- `pp-exact` is used to ensure a pretty-print test results in specific output.
  If specified without a value, then it means the pretty-print output should
  match the original source.
  If specified with a value, as in `//@
  pp-exact:foo.pp`, it will ensure that the pretty-printed output matches the
  contents of the given file.
  Otherwise, if `pp-exact` is not specified, then
  the pretty-printed output will be pretty-printed one more time, and the output
  of the two pretty-printing rounds will be compared to ensure that the
  pretty-printed output converges to a steady state.

[`tests/pretty`]: https://github.com/rust-lang/rust/tree/HEAD/tests/pretty

### Incremental tests

The tests in [`tests/incremental`] exercise incremental compilation.
They use [`revisions` directive](#revisions) to tell compiletest to run the compiler in a
series of steps.

Compiletest starts with an empty directory with the `-C incremental` flag, and
then runs the compiler for each revision, reusing the incremental results from previous steps.

The revisions should start with:

* `bfail` — the test should fail to compile
* `bpass` — the test should compile successully
* `rpass` — the test should compile and run successfully

To make the revisions unique, you should add a suffix like `rpass1` and `rpass2`.

To simulate changing the source, compiletest also passes a `--cfg` flag with the
current revision name.

For example, this will run twice, simulating changing a function:

```rust,ignore
//@ revisions: rpass1 rpass2

#[cfg(rpass1)]
fn foo() {
    println!("one");
}

#[cfg(rpass2)]
fn foo() {
    println!("two");
}

fn main() { foo(); }
```

Incremental tests support the `forbid-output` directive to specify that a certain
substring must not appear anywhere in the compiler output.
This can be useful to ensure certain errors do not appear, but this can be fragile as error messages
change over time, and a test may no longer be checking the right thing but will still pass.

Incremental tests may use the attribute `#[rustc_clean(...)]` attribute.
This attribute compares the fingerprint from the current compilation session with the previous one.
The first revision should never have an active `rustc_clean` attribute, since it will always be dirty.

In the default mode, it asserts that the fingerprints must be the same.
The attribute takes the following arguments:

* `cfg="<cond>"` — checks the cfg condition `<cond>`, and only runs the check if the config condition evaluates to true.
  This can be used to only run the `rustc_clean` attribute in a specific revision.
* `except="<query1>,<query2>,..."` — asserts that the query results for the listed queries must be different,
  rather than the same.
* `loaded_from_disk="<query1>,<query2>,..."` — asserts that the query results for the listed queries
  were actually loaded from disk (not just marked green).
  This can be useful to ensure that a test is actually exercising the deserialization
  logic for a particular query result.
  This can be combined with `except`.

A simple example of a test using `rustc_clean` is the [hello_world test].

[`tests/incremental`]: https://github.com/rust-lang/rust/tree/7b42543/tests/incremental
[hello_world test]: https://github.com/rust-lang/rust/blob/646a3f8c15baefb98dc6e0c1c1ba3356db702d2a/tests/incremental/hello_world.rs

### Debuginfo tests

The tests in [`tests/debuginfo`] test debuginfo generation.
They build a program, launch a debugger, and issue commands to the debugger.
A single test can work with cdb, gdb, and lldb.

Most tests should have the `//@ compile-flags: -g` directive or something
similar to generate the appropriate debuginfo.

To set a breakpoint on a line, add a `// #break` comment on the line.

The debuginfo tests consist of a series of debugger commands along with
"check" lines which specify output that is expected from the debugger.

The commands are comments of the form `// $DEBUGGER-command:$COMMAND` where
`$DEBUGGER` is the debugger being used and `$COMMAND` is the debugger command to execute.

The debugger values can be:

- `cdb`
- `gdb`
- `gdbg` — GDB without Rust support (versions older than 7.11)
- `gdbr` — GDB with Rust support
- `lldb`
- `lldbg` — LLDB without Rust support
- `lldbr` — LLDB with Rust support (this no longer exists)

The command to check the output are of the form `// $DEBUGGER-check:$OUTPUT`
where `$OUTPUT` is the output to expect.

For example, the following will build the test, start the debugger, set a
breakpoint, launch the program, inspect a value, and check what the debugger prints:

```rust,ignore
//@ compile-flags: -g

//@ lldb-command: run
//@ lldb-command: print foo
//@ lldb-check: $0 = 123

fn main() {
    let foo = 123;
    b(); // #break
}

fn b() {}
```

The following [directives](directives.md) are available to disable a test based on
the debugger currently being used:

- `min-cdb-version: 10.0.18317.1001` — ignores the test if the version of cdb
  is below the given version
- `min-gdb-version: 8.2` — ignores the test if the version of gdb is below the given version
- `ignore-gdb-version: 9.2` — ignores the test if the version of gdb is equal
  to the given version
- `ignore-gdb-version: 7.11.90 - 8.0.9` — ignores the test if the version of
  gdb is in a range (inclusive)
- `min-lldb-version: 310` — ignores the test if the version of lldb is below the given version
- `rust-lldb` — ignores the test if lldb is not contain the Rust plugin.
  NOTE: The "Rust" version of LLDB doesn't exist anymore, so this will always be ignored.
  This should probably be removed.

By passing the `--debugger` option to compiletest, you can specify a single debugger to run tests with.
For example, `./x test tests/debuginfo -- --debugger gdb` will only test GDB commands.

> **Note on running lldb debuginfo tests locally**
>
> If you want to run lldb debuginfo tests locally, then currently on Windows it
> is required that:
>
> - You have Python 3.10 installed.
> - You have `python310.dll` available in your `PATH` env var. This is not
>   provided by the standard Python installer you obtain from `python.org`; you
>   need to add this to `PATH` manually.
>
> Otherwise the lldb debuginfo tests can produce crashes in mysterious ways.

[`tests/debuginfo`]: https://github.com/rust-lang/rust/tree/HEAD/tests/debuginfo

> **Note on acquiring `cdb.exe` on Windows 11**
>
> `cdb.exe` is acquired alongside a suitable "Windows 11 SDK" which is part of
> the "Desktop Development with C++" workload profile in a Visual Studio
> installer (e.g. Visual Studio 2022 installer).
>
> **HOWEVER** this is not sufficient by default alone. If you need `cdb.exe`,
> you must go to Installed Apps, find the newest "Windows Software Development
> Kit" (and yes, this can still say `Windows 10.0.22161.3233` even though the OS
> is called Windows 11). You must then click "Modify" -> "Change" and then
> selected "Debugging Tools for Windows" in order to acquire `cdb.exe`.

### Codegen tests

The tests in [`tests/codegen-llvm`] test LLVM code generation.
They compile the test with the `--emit=llvm-ir` flag to emit LLVM IR.
They then run the LLVM [FileCheck] tool.
The test is annotated with various `// CHECK` comments to check the generated code.
See the [FileCheck] documentation for a tutorial and more information.

See also the [assembly tests](#assembly-tests) for a similar set of tests.

By default, codegen tests will have `//@ needs-target-std` *implied* (that the
target needs to support std), *unless* the `#![no_std]`/`#![no_core]` attribute
was specified in the test source.
You can override this behavior and explicitly
write `//@ needs-target-std` to only run the test when target supports std, even
if the test is `#![no_std]`/`#![no_core]`.

If you need to work with `#![no_std]` cross-compiling tests, consult the
[`minicore` test auxiliary](./minicore.md) chapter.

[`tests/codegen-llvm`]: https://github.com/rust-lang/rust/tree/HEAD/tests/codegen-llvm
[FileCheck]: https://llvm.org/docs/CommandGuide/FileCheck.html


### Assembly tests

The tests in [`tests/assembly-llvm`] test LLVM assembly output.
They compile the test with the `--emit=asm` flag to emit a `.s` file with the assembly output.
They then run the LLVM [FileCheck] tool.

Each test should be annotated with the `//@ assembly-output:` directive with a
value of either `emit-asm` or `ptx-linker` to indicate the type of assembly output.

Then, they should be annotated with various `// CHECK` comments to check the assembly output.
See the [FileCheck] documentation for a tutorial and more information.

See also the [codegen tests](#codegen-tests) for a similar set of tests.

If you need to work with `#![no_std]` cross-compiling tests, consult the
[`minicore` test auxiliary](./minicore.md) chapter.

[`tests/assembly-llvm`]: https://github.com/rust-lang/rust/tree/HEAD/tests/assembly-llvm


### Codegen-units tests

The tests in [`tests/codegen-units`] test the
[monomorphization](../backend/monomorph.md) collector and CGU partitioning.

These tests work by running `rustc` with a flag to print the result of the
monomorphization collection pass, i.e., `-Zprint-mono-items`, and then special
annotations in the file are used to compare against that.

Then, the test should be annotated with comments of the form `//~ MONO_ITEM
name` where `name` is the monomorphized string printed by rustc like `fn <u32 as Trait>::foo`.

To check for CGU partitioning, a comment of the form `//~ MONO_ITEM name @@ cgu`
where `cgu` is a space separated list of the CGU names and the linkage information in brackets.
For example: `//~ MONO_ITEM static function::FOO @@ statics[Internal]`

[`tests/codegen-units`]: https://github.com/rust-lang/rust/tree/HEAD/tests/codegen-units


### Mir-opt tests

The tests in [`tests/mir-opt`] check parts of the generated MIR to make sure it
is generated correctly and is doing the expected optimizations.
Check out the [MIR Optimizations](../mir/optimizations.md) chapter for more.

Compiletest will build the test with several flags to dump the MIR output and
set a baseline for optimizations:

* `-Copt-level=1`
* `-Zdump-mir=all`
* `-Zmir-opt-level=4`
* `-Zvalidate-mir`
* `-Zdump-mir-exclude-pass-number`

The test should be annotated with `// EMIT_MIR` comments that specify files that
will contain the expected MIR output.
You can use `x test --bless` to create the initial expected files.

There are several forms the `EMIT_MIR` comment can take:

- `// EMIT_MIR $MIR_PATH.mir` — This will check that the given filename matches
  the exact output from the MIR dump.
  For example,
  `my_test.main.SimplifyCfg-elaborate-drops.after.mir` will load that file from
  the test directory, and compare it against the dump from rustc.

  Checking the "after" file (which is after optimization) is useful if you are
  interested in the final state after an optimization.
  Some rare cases may want to use the "before" file for completeness.

- `// EMIT_MIR $MIR_PATH.diff` — where `$MIR_PATH` is the filename of the MIR
  dump, such as `my_test_name.my_function.EarlyOtherwiseBranch`.
  Compiletest will diff the `.before.mir` and `.after.mir` files, and compare the diff
  output to the expected `.diff` file from the `EMIT_MIR` comment.

  This is useful if you want to see how an optimization changes the MIR.

- `// EMIT_MIR $MIR_PATH.dot` — When using specific flags that dump additional
  MIR data (e.g. `-Z dump-mir-graphviz` to produce `.dot` files), this will
  check that the output matches the given file.

By default 32 bit and 64 bit targets use the same dump files, which can be
problematic in the presence of pointers in constants or other bit width dependent things.
In that case you can add `// EMIT_MIR_FOR_EACH_BIT_WIDTH` to
your test, causing separate files to be generated for 32bit and 64bit systems.

[`tests/mir-opt`]: https://github.com/rust-lang/rust/tree/HEAD/tests/mir-opt


### `run-make` tests

The tests in [`tests/run-make`] and [`tests/run-make-cargo`] are general-purpose
tests using Rust *recipes*, which are small programs (`rmake.rs`) allowing
arbitrary Rust code such as `rustc` invocations, and is supported by a [`run_make_support`] library.
Using Rust recipes provide the ultimate in flexibility.

`run-make` tests should be used if no other test suites better suit your needs.

The `run-make-cargo` test suite additionally builds an in-tree `cargo` to support
use cases that require testing in-tree `cargo` in conjunction with in-tree `rustc`.
The `run-make` test suite does not have access to in-tree `cargo` (so it can be the
faster-to-iterate test suite).

### `build-std` tests

The tests in [`tests/build-std`] check that `-Zbuild-std` works.
This is currently just a run-make test suite with a single recipe.
The recipe generates test cases and runs them in parallel.

[`tests/build-std`]: https://github.com/rust-lang/rust/tree/HEAD/tests/build-std

#### Using Rust recipes

Each test should be in a separate directory with a `rmake.rs` Rust program,
called the *recipe*. A recipe will be compiled and executed by compiletest with
the `run_make_support` library linked in.

If you need new utilities or functionality, consider extending and improving the
[`run_make_support`] library.

Compiletest directives like `//@ only-<target>` or `//@ ignore-<target>` are
supported in `rmake.rs`, like in UI tests.
However, revisions or building auxiliary via directives are not currently supported.

`rmake.rs` and `run-make-support` may *not* use any nightly/unstable features,
as they must be compilable by a stage 0 rustc that may be a beta or even stable rustc.

By default, run-make tests print each subprocess command and its stdout/stderr.
When running with `--no-capture` on `panic=abort` test suites (such as `cg_clif`),
this can flood the terminal. Omit `--verbose-run-make-subprocess-output` to
suppress this output for passing tests — failing tests always print regardless:

```bash
./x test tests/run-make --no-capture --verbose-run-make-subprocess-output=false
```

#### Quickly check if `rmake.rs` tests can be compiled

You can quickly check if `rmake.rs` tests can be compiled without having to
build stage1 rustc by forcing `rmake.rs` to be compiled with the stage0 compiler:

```bash
$ COMPILETEST_FORCE_STAGE0=1 x test --stage 0 tests/run-make/<test-name>
```

Of course, some tests will not successfully *run* in this way.

#### Using rust-analyzer with `rmake.rs`

Like other test programs, the `rmake.rs` scripts used by run-make tests do not
have rust-analyzer integration by default.

To work around this when working on a particular test, temporarily create a
`Cargo.toml` file in the test's directory
(e.g. `tests/run-make/sysroot-crates-are-unstable/Cargo.toml`)
with these contents:

<div class="warning">

Be careful not to add this `Cargo.toml` or its `Cargo.lock` to your actual PR!

</div>

```toml
# Convince cargo that this isn't part of an enclosing workspace.
[workspace]

[package]
name = "rmake"
version = "0.1.0"
edition = "2021"

[dependencies]
run_make_support = { path = "../../../src/tools/run-make-support" }

[[bin]]
name = "rmake"
path = "rmake.rs"
```

Then add a corresponding entry to `"rust-analyzer.linkedProjects"`
(e.g. in `.vscode/settings.json`):

```json
"rust-analyzer.linkedProjects": [
  "tests/run-make/sysroot-crates-are-unstable/Cargo.toml"
],
```

[`tests/run-make`]: https://github.com/rust-lang/rust/tree/HEAD/tests/run-make
[`tests/run-make-cargo`]: https://github.com/rust-lang/rust/tree/HEAD/tests/run-make-cargo
[`run_make_support`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/run-make-support

### Coverage tests

The tests in [`tests/coverage`] are shared by multiple test modes that test
coverage instrumentation in different ways.
Running the `coverage` test suite
will automatically run each test in all of the different coverage modes.

Each mode also has an alias to run the coverage tests in just that mode:

```bash
./x test coverage # runs all of tests/coverage in all coverage modes
./x test tests/coverage # same as above

./x test tests/coverage/if.rs # runs the specified test in all coverage modes

./x test coverage-map # runs all of tests/coverage in "coverage-map" mode only
./x test coverage-run # runs all of tests/coverage in "coverage-run" mode only

./x test coverage-map -- tests/coverage/if.rs # runs the specified test in "coverage-map" mode only
```

If a particular test should not be run in one of the coverage test modes for
some reason, use the `//@ ignore-coverage-map` or `//@ ignore-coverage-run` directives.

#### `coverage-map` suite

In `coverage-map` mode, these tests verify the mappings between source code
regions and coverage counters that are emitted by LLVM.
They compile the test with `--emit=llvm-ir`, then use a custom tool ([`src/tools/coverage-dump`]) to
extract and pretty-print the coverage mappings embedded in the IR.
These tests don't require the profiler runtime, so they run in PR CI jobs and are easy to
run/bless locally.

These coverage map tests can be sensitive to changes in MIR lowering or MIR
optimizations, producing mappings that are different but produce identical coverage reports.

As a rule of thumb, any PR that doesn't change coverage-specific code should
**feel free to re-bless** the `coverage-map` tests as necessary, without
worrying about the actual changes, as long as the `coverage-run` tests still pass.

#### `coverage-run` suite

In `coverage-run` mode, these tests perform an end-to-end test of coverage reporting.
They compile a test program with coverage instrumentation, run that
program to produce raw coverage data, and then use LLVM tools to process that
data into a human-readable code coverage report.

Instrumented binaries need to be linked against the LLVM profiler runtime, so
`coverage-run` tests are **automatically skipped** unless the profiler runtime
is enabled in `bootstrap.toml`:

```toml
build.profiler = true
```

This also means that they typically don't run in PR CI jobs, though they do run
as part of the full set of CI jobs used for merging.

#### `coverage-run-rustdoc` suite

The tests in [`tests/coverage-run-rustdoc`] also run instrumented doctests and
include them in the coverage report.
This avoids having to build rustdoc when only running the main `coverage` suite.

[`tests/coverage`]: https://github.com/rust-lang/rust/tree/HEAD/tests/coverage
[`src/tools/coverage-dump`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/coverage-dump
[`tests/coverage-run-rustdoc`]: https://github.com/rust-lang/rust/tree/HEAD/tests/coverage-run-rustdoc

### Crash tests

[`tests/crashes`] serve as a collection of tests that are expected to cause the
compiler to ICE, panic or crash in some other way, so that accidental fixes are tracked.
Formerly, this was done at <https://github.com/rust-lang/glacier> but
doing it inside the rust-lang/rust testsuite is more convenient.

It is imperative that a test in the suite causes rustc to ICE, panic, or crash in some other way.
A test will "pass" if rustc exits with an exit status other than 1 or 0.

If you want to see verbose stdout/stderr, you need to set
`COMPILETEST_VERBOSE_CRASHES=1`, e.g.

```bash
$ COMPILETEST_VERBOSE_CRASHES=1 ./x test tests/crashes/999999.rs --stage 1
```

Anyone can add ["untracked" crashes] from the issue tracker.
It's strongly recommended to include test cases from several issues in a single PR.
When you do so, each issue number should be noted in the file name (`12345.rs`
should suffice) and also inside the file by means of a `//@ known-bug: #12345` directive.
Please [label][labeling] the relevant issues with `S-bug-has-test` once your PR is merged.

If you happen to fix one of the crashes, please move it to a fitting
subdirectory in `tests/ui` and give it a meaningful name.
Please add a doc comment at the top of the file explaining why this test exists.
Even better will be if you can briefly explain how the example caused rustc to crash previously,
and what was done to fix it.

Adding

```text
Fixes #NNNNN
Fixes #MMMMM
```

to the description of your pull request will ensure the corresponding tickets be closed
automatically upon merge.

Make sure that your fix actually fixes the root cause of the issue and not just a subset first.
The issue numbers can be found in the file name or the `//@
known-bug` directive inside the test file.

[`tests/crashes`]: https://github.com/rust-lang/rust/tree/HEAD/tests/crashes
["untracked" crashes]: https://github.com/rust-lang/rust/issues?q=is%3Aissue+state%3Aopen+label%3AI-ICE%2CI-crash+label%3AT-compiler+label%3AS-has-mcve+-label%3AS-bug-has-test
[labeling]: https://forge.rust-lang.org/release/issue-triaging.html#applying-and-removing-labels

## Building auxiliary crates

It is common that some tests require additional auxiliary crates to be compiled.
There are multiple [directives](directives.md) to assist with that:

- `aux-build`
- `aux-crate`
- `aux-bin`
- `aux-codegen-backend`
- `proc-macro`

`aux-build` will build a separate crate from the named source file.
The source file should be in a directory called `auxiliary` beside the test file.

```rust,ignore
//@ aux-build: my-helper.rs

extern crate my_helper;
// ... You can use my_helper.
```

The aux crate will be built as a dylib if possible (unless on a platform that
does not support them, or the `no-prefer-dynamic` header is specified in the aux file).
The `-L` flag is used to find the extern crates.

`aux-crate` is very similar to `aux-build`.
However, it uses the `--extern` flag
to link to the extern crate to make the crate be available as an extern prelude.
That allows you to specify the additional syntax of the `--extern` flag, such as
renaming a dependency.
For example, `//@ aux-crate:foo=bar.rs` will compile
`auxiliary/bar.rs` and make it available under then name `foo` within the test.
This is similar to how Cargo does dependency renaming.
It is also possible to
specify [`--extern` modifiers](https://github.com/rust-lang/rust/issues/98405).
For example, `//@ aux-crate:noprelude:foo=bar.rs`.

`aux-bin` is similar to `aux-build` but will build a binary instead of a library.
The binary will be available in `auxiliary/bin` relative to the working directory of the test.

`aux-codegen-backend` is similar to `aux-build`, but will then pass the compiled
dylib to `-Zcodegen-backend` when building the main file.
This will only work for tests in `tests/ui-fulldeps`, since it requires the use of compiler crates.

### Auxiliary proc-macro

If you want a proc-macro dependency, then you can use the `proc-macro`
directive. This directive behaves just like `aux-build`, i.e. that you should
place the proc-macro test auxiliary file under a `auxiliary` folder under the
same parent folder as the main test file.
However, it also has four additional
preset behavior compared to `aux-build` for the proc-macro test auxiliary:

1. The aux test file is built with `--crate-type=proc-macro`.
2. The aux test file is built without `-C prefer-dynamic`, i.e. it will not try
   to produce a dylib for the aux crate.
3. The aux crate is made available to the test file via extern prelude with
   `--extern <aux_crate_name>`.
   Note that since UI tests default to edition
   2015, you still need to specify `extern <aux_crate_name>` unless the main
   test file is using an edition that is 2018 or newer if you want to use the
   aux crate name in a `use` import.
4. The `proc_macro` crate is made available as an extern prelude module.
   The same edition 2015 vs newer edition distinction for `extern proc_macro;` applies.

For example, you might have a test `tests/ui/cat/meow.rs` and proc-macro
auxiliary `tests/ui/cat/auxiliary/whiskers.rs`:

```text
tests/ui/cat/
    meow.rs                 # main test file
    auxiliary/whiskers.rs   # auxiliary
```

```rs
// tests/ui/cat/meow.rs

//@ proc-macro: whiskers.rs

extern crate whiskers; // needed as ui test defaults to edition 2015

fn main() {
  whiskers::identity!();
}
```

```rs
// tests/ui/cat/auxiliary/whiskers.rs

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn identity(ts: TokenStream) -> TokenStream {
    ts
}
```

> **Note**: The `proc-macro` header currently does not work with the
> `build-aux-doc` header for rustdoc tests. In that case, you will need to use
> the `aux-build` header, and use `#![crate_type="proc_macro"]`, and `//@
> force-host` and `//@ no-prefer-dynamic` headers in the proc-macro.

## Revisions

Revisions allow a single test file to be used for multiple tests.
This is done by adding a special directive at the top of the file:

```rust,ignore
//@ revisions: foo bar baz
```

This will result in the test being compiled (and tested) three times, once with
`--cfg foo`, once with `--cfg bar`, and once with `--cfg baz`.
You can therefore use `#[cfg(foo)]` etc within the test to tweak each of these results.

You can also customize directives and expected error messages to a particular revision.
To do this, add `[revision-name]` after the `//@` for directives, and
after `//` for UI error annotations, like so:

```rust,ignore
// A flag to pass in only for cfg `foo`:
//@[foo]compile-flags: -Z verbose-internals

#[cfg(foo)]
fn test_foo() {
    let x: usize = 32_u32; //[foo]~ ERROR mismatched types
}
```

Multiple revisions can be specified in a comma-separated list, such as `//[foo,bar,baz]~^`.

In test suites that use the LLVM [FileCheck] tool, the current revision name is
also registered as an additional prefix for FileCheck directives:

```rust,ignore
//@ revisions: NORMAL COVERAGE
//@[COVERAGE] compile-flags: -Cinstrument-coverage
//@[COVERAGE] needs-profiler-runtime

// COVERAGE:   @__llvm_coverage_mapping
// NORMAL-NOT: @__llvm_coverage_mapping

// CHECK: main
fn main() {}
```

Note that not all directives have meaning when customized to a revision.
For example, the `ignore-test` directives (and all "ignore" directives) currently
only apply to the test as a whole, not to particular revisions.
The only directives that are intended to really work when customized to a revision are
error patterns and compiler flags.

<!-- date-check Feb 2026 -->
> Note that these test suites do not support revisions:
> - `codegen-units`
> - `run-make`
> - `rustdoc-html`
> - `rustdoc-json`

### Ignoring unused revision names

Normally, revision names mentioned in other directives and error annotations
must correspond to an actual revision declared in a `revisions` directive.
This is enforced by an `./x test tidy` check.

If a revision name needs to be temporarily removed from the revision list for
some reason, the above check can be suppressed by adding the revision name to an
`//@ unused-revision-names:` header instead.

Specifying an unused name of `*` (i.e. `//@ unused-revision-names: *`) will
permit any unused revision name to be mentioned.

## Compare modes

Compiletest can be run in different modes, called _compare modes_, which can be
used to compare the behavior of all tests with different compiler flags enabled.
This can help highlight what differences might appear with certain flags, and
check for any problems that might arise.

To run the tests in a different mode, you need to pass the `--compare-mode` CLI flag:

```bash
./x test tests/ui --compare-mode=chalk
```

The possible compare modes are:

- `polonius` — Runs with Polonius with `-Zpolonius`.
- `chalk` — Runs with Chalk with `-Zchalk`.
- `split-dwarf` — Runs with unpacked split-DWARF with `-Csplit-debuginfo=unpacked`.
- `split-dwarf-single` — Runs with packed split-DWARF with `-Csplit-debuginfo=packed`.

See [UI compare modes](ui.md#compare-modes) for more information about how UI
tests support different output for different modes.

In CI, compare modes are only used in one Linux builder, and only with the following settings:

- `tests/debuginfo`: Uses `split-dwarf` mode.
  This helps ensure that none of the debuginfo tests are affected when enabling split-DWARF.

Note that compare modes are separate to [revisions](#revisions).
All revisions are tested when running `./x test tests/ui`, however compare-modes must be
manually run individually via the `--compare-mode` flag.

## Parallel frontend

Compiletest can be run with the `--parallel-frontend-threads` flag to run the compiler in parallel mode.
This can be used to check that the compiler produces the same output in parallel mode as in non-parallel mode, and to check for any issues that might arise in parallel mode.

To run the tests in parallel mode, you need to pass the `--parallel-frontend-threads` CLI flag:

```bash
./x test tests/ui -- --parallel-frontend-threads=N --iteration-count=M
```

Where `N` is the number of threads to use for the parallel frontend, and `M` is the number of times to run each test in parallel mode (to increase the chances of catching any non-determinism).

Also, when running with `--parallel-frontend-threads`, the `compare-output-by-lines` directive would be implied for all tests, since the output from the parallel frontend can be non-deterministic in terms of the order of lines.

The parallel frontend is available in UI tests only at the moment, and is not currently supported in other test suites.


---

# UI tests

UI tests are a particular [test suite](compiletest.md#test-suites) of compiletest.

## Introduction

The tests in [`tests/ui`] are a collection of general-purpose tests which
primarily focus on validating the console output of the compiler, but can be
used for many other purposes.
For example, tests can also be configured to [run
the resulting program](#controlling-passfail-expectations) to verify its behavior.

For a survey of each subdirectory's purpose under `tests/ui`, consult the
[README.md](https://github.com/rust-lang/rust/tree/HEAD/tests/ui/README.md).
This is useful if you write a new test, and are looking for a category to place it in.

If you need to work with `#![no_std]` cross-compiling tests, consult the
[`minicore` test auxiliary](./minicore.md) chapter.

[`tests/ui`]: https://github.com/rust-lang/rust/blob/HEAD/tests/ui

## General structure of a test

A test consists of a Rust source file located in the `tests/ui` directory.
**Tests must be placed in the appropriate subdirectory** based on their purpose
and testing category - placing tests directly in `tests/ui` is not permitted.

Compiletest will use `rustc` to compile the test, and compare the output against
the expected output which is stored in a `.stdout` or `.stderr` file located next to the test.
See [Output comparison](#output-comparison) for more.

Additionally, errors and warnings should be annotated with comments within the source file.
See [Error annotations](#error-annotations) for more.

Compiletest [directives](directives.md) in the form of special comments prefixed
with `//@` control how the test is compiled and what the expected behavior is.

Tests are expected to fail to compile, since most tests are testing compiler errors.
You can change that behavior with a directive, see [Controlling
pass/fail expectations](#controlling-passfail-expectations).

By default, a test is built as an executable binary.
If you need a different crate type, you can use the `#![crate_type]` attribute to set it as needed.

## Output comparison

UI tests store the expected output from the compiler in `.stderr` and `.stdout`
snapshots next to the test.
You normally generate these files with the `--bless`
CLI option, and then inspect them manually to verify they contain what you expect.

The output is normalized to ignore unwanted differences, see the
[Normalization](#normalization) section.
If the file is missing, then compiletest expects the corresponding output to be empty.

A common reason to use normalization, revisions, and most of the other following tools,
is to account for platform differences.
Consider alternatives to these tools, like
e.g. using the `extern "rust-invalid"` ABI that is invalid on every platform
instead of fixing the test to use cross-compilation and testing every possibly-invalid ABI.

There can be multiple stdout/stderr files.
The general form is:

```text
*test-name*`.`*revision*`.`*compare_mode*`.`*extension*
```

- *test-name* cannot contain dots.
  This is so that the general form of test
  output filenames have a predictable form we can pattern match on in order to
  track stray test output files.
- *revision* is the [revision](#cfg-revisions) name.
  This is not included when not using revisions.
- *compare_mode* is the [compare mode](#compare-modes).
  This will only be checked when the given compare mode is active.
  If the file does not exist,
  then compiletest will check for a file without the compare mode.
- *extension* is the kind of output being checked:
  - `stderr` — compiler stderr
  - `stdout` — compiler stdout
  - `run.stderr` — stderr when running the test
  - `run.stdout` — stdout when running the test
  - `64bit.stderr` — compiler stderr with `stderr-per-bitwidth` directive on a 64-bit target
  - `32bit.stderr` — compiler stderr with `stderr-per-bitwidth` directive on a 32-bit target

A simple example would be `foo.stderr` next to a `foo.rs` test.
A more complex example would be `foo.my-revision.polonius.stderr`.

There are several [directives](directives.md) which will change how compiletest
will check for output files:

- `stderr-per-bitwidth` — checks separate output files based on the target pointer width.
  Consider using the `normalize-stderr` directive instead (see [Normalization](#normalization)).
- `dont-check-compiler-stderr` — Ignores stderr from the compiler.
- `dont-check-compiler-stdout` — Ignores stdout from the compiler.
- `compare-output-by-lines` — Some tests have non-deterministic orders of output, so we need to compare by lines.

UI tests run with `-Zdeduplicate-diagnostics=no` flag which disables rustc's
built-in diagnostic deduplication mechanism.
This means you may see some duplicate messages in the output.
This helps illuminate situations where duplicate diagnostics are being generated.

### Normalization

The compiler output is normalized to eliminate output difference between
platforms, mainly about filenames.

Compiletest makes the following replacements on the compiler output:

- The directory where the test is defined is replaced with `$DIR`.
  Example: `/path/to/rust/tests/ui/error-codes`
- The directory to the standard library source is replaced with `$SRC_DIR`.
  Example: `/path/to/rust/library`
- Line and column numbers for paths in `$SRC_DIR` are replaced with `LL:COL`.
  This helps ensure that changes to the layout of the standard library do not
  cause widespread changes to the `.stderr` files.
  Example: `$SRC_DIR/alloc/src/sync.rs:53:46`
- The base directory where the test's output goes is replaced with `$TEST_BUILD_DIR`.
  This only comes up in a few rare circumstances.
  Example: `/path/to/rust/build/x86_64-unknown-linux-gnu/test/ui`
- The real directory to the standard library source is replaced with `$SRC_DIR_REAL`.
- The real directory to the compiler source is replaced with `$COMPILER_DIR_REAL`.
- Tabs are replaced with `\t`.
- Backslashes (`\`) are converted to forward slashes (`/`) within paths (using a heuristic).
  This helps normalize differences with Windows-style paths.
- CRLF newlines are converted to LF.
- Error line annotations like `//~ ERROR some message` are removed.
- Various v0 and legacy symbol hashes are replaced with placeholders like
  `[HASH]` or `<SYMBOL_HASH>`.

Additionally, the compiler is run with the `-Z ui-testing` flag which causes
the compiler itself to apply some changes to the diagnostic output to make it
more suitable for UI testing.

For example, it will anonymize line numbers in the output (line numbers
prefixing each source line are replaced with `LL`).
In extremely rare situations, this mode can be disabled with the directive `//@
compile-flags: -Z ui-testing=no`.

When using `-Z ui-testing=no`, the `--diagnostic-width` argument should also
be set to avoid tests failing or passing depending on the width of the terminal
from which the UI test suite is being run.

Note: The line and column numbers for `-->` lines pointing to the test are *not*
normalized, and left as-is.
This ensures that the compiler continues to point to
the correct location, and keeps the stderr files readable.
Ideally all line/column information would be retained, but small changes to the source
causes large diffs, and more frequent merge conflicts and test errors.

Sometimes these built-in normalizations are not enough.
In such cases, you may
provide custom normalization rules using `normalize-*` directives, e.g.

```rust,ignore
//@ normalize-stdout: "foo" -> "bar"
//@ normalize-stderr: "foo" -> "bar"
//@ normalize-stderr-32bit: "fn\(\) \(32 bits\)" -> "fn\(\) \($$PTR bits\)"
//@ normalize-stderr-64bit: "fn\(\) \(64 bits\)" -> "fn\(\) \($$PTR bits\)"
```

This tells the test, on 32-bit platforms, whenever the compiler writes `fn() (32
bits)` to stderr, it should be normalized to read `fn() ($PTR bits)` instead.
Similar for 64-bit.
The replacement is performed by regexes using default regex flavor provided by `regex` crate.

The corresponding reference file will use the normalized output to test both
32-bit and 64-bit platforms:

```text
...
   |
   = note: source type: fn() ($PTR bits)
   = note: target type: u16 (16 bits)
...
```

Please see [`ui/transmute/main.rs`][mrs] and [`main.stderr`] for a concrete usage example.

[mrs]: https://github.com/rust-lang/rust/blob/HEAD/tests/ui/transmute/main.rs
[`main.stderr`]: https://github.com/rust-lang/rust/blob/HEAD/tests/ui/transmute/main.stderr

## Error annotations

Error annotations specify the errors that the compiler is expected to emit.
They are "attached" to the line in source where the error is located.

```rust,ignore
fn main() {
    boom  //~ ERROR cannot find value `boom` in this scope [E0425]
}
```

Although UI tests have a `.stderr` file which contains the entire compiler
output, UI tests require that errors are also annotated within the source.
This redundancy helps avoid mistakes since the `.stderr` files are usually
auto-generated.
It also helps to directly see where the error spans are expected
to point to by looking at one file instead of having to compare the `.stderr` file with the source.
Finally, they ensure that no additional unexpected errors are generated.

They have several forms, but generally are a comment with the diagnostic level
(such as `ERROR`) and a substring of the expected error output.
You don't have to write out the entire message,
but be sure to include the important part of the message to make it self-documenting.

Most error annotations need to match with the line of the diagnostic.
There are several ways to match the message with the line (see the examples below):

* `~`: Associates the error level and message with the *current* line
* `~^`: Associates the error level and message with the *previous* error annotation line.
  Each caret (`^`) that you add adds a line to this, so `~^^^`
  is three lines above the error annotation line.
* `~|`: Associates the error level and message with the *same* line as the
  *previous comment*. This is more convenient than using multiple carets when
  there are multiple messages associated with the same line.
* `~v`: Associates the error level and message with the *next* error annotation line.
  Each symbol (`v`) that you add adds a line to this, so `~vvv`
  is three lines below the error annotation line.

Example:

```rust,ignore
let _ = same_line; //~ ERROR undeclared variable
fn meow(_: [u8]) {}
//~^ ERROR unsized
//~| ERROR anonymous parameters
```

The space character between `//~` (or other variants) and the subsequent text is
negligible (i.e. there is no semantic difference between `//~ ERROR` and
`//~ERROR` although the former is more common in the codebase).

`~? <diagnostic kind>` (example being `~? ERROR`)
is used to match diagnostics _without_ line info at all,
or where the line info is outside the main test file[^main test file].
These annotations can be placed on any line in the test file.

[^main test file]: This is a file that has the `~?` annotations,
as distinct from aux files, or sources that we have no control over.

### Error annotation examples

Here are examples of error annotations on different lines of UI test source.

#### Positioned on error line

Use the `//~ ERROR` idiom:

```rust,ignore
fn main() {
    let x = (1, 2, 3);
    match x {
        (_a, _x @ ..) => {} //~ ERROR `_x @` is not allowed in a tuple
        _ => {}
    }
}
```

#### Positioned below error line

Use the `//~^` idiom with number of carets in the string to indicate the number of lines above.
In the example below, the error line is four lines above the
error annotation line so four carets are included in the annotation.

```rust,ignore
fn main() {
    let x = (1, 2, 3);
    match x {
        (_a, _x @ ..) => {}  // <- the error is on this line
        _ => {}
    }
}
//~^^^^ ERROR `_x @` is not allowed in a tuple
```

#### Use same error line as defined on error annotation line above

Use the `//~|` idiom to define the same error line as the error annotation
line above:

```rust,ignore
struct Binder(i32, i32, i32);

fn main() {
    let x = Binder(1, 2, 3);
    match x {
        Binder(_a, _x @ ..) => {}  // <- the error is on this line
        _ => {}
    }
}
//~^^^^ ERROR `_x @` is not allowed in a tuple struct
//~| ERROR this pattern has 1 field, but the corresponding tuple struct has 3 fields [E0023]
```

#### Positioned above error line

Use the `//~v` idiom with number of v's in the string to indicate the number of lines below.
This is typically used in lexer or parser tests matching on errors like unclosed
delimiter or unclosed literal happening at the end of file.

```rust,ignore
// ignore-tidy-trailing-newlines
//~v ERROR this file contains an unclosed delimiter
fn main((ؼ
```

#### Error without line information

Use `//~?` to match an error without line information.
`//~?` is precise and will not match errors if their line information is available.
It should be preferred over `//@ error-pattern`
for tests wishing to match against compiler diagnostics,
due to `//@ error-pattern` being imprecise and non-exhaustive.

```rust,ignore
//@ compile-flags: --print yyyy

//~? ERROR unknown print request: `yyyy`
```

### `error-pattern`

The `error-pattern` [directive](directives.md) can be used for runtime messages which don't
have a specific span, or, in exceptional cases, for compile time messages.

Let's think about this test:

```rust,ignore
fn main() {
    let a: *const [_] = &[1, 2, 3];
    unsafe {
        let _b = (*a)[3];
    }
}
```

We want to ensure this shows "index out of bounds", but we cannot use the `ERROR`
annotation since the runtime error doesn't have any span.
Then it's time to use the `error-pattern` directive:

```rust,ignore
//@ error-pattern: index out of bounds
fn main() {
    let a: *const [_] = &[1, 2, 3];
    unsafe {
        let _b = (*a)[3];
    }
}
```

For strict testing of compile time output, try to use the line annotations `//~` as much as
possible, including `//~?` annotations for diagnostics without spans.

If the compile time output is target dependent or too verbose, use directive
`//@ dont-require-annotations: <diagnostic-kind>` to make the line annotation checking
non-exhaustive.
Some of the compiler messages can stay uncovered by annotations in this mode.

For checking runtime output, `//@ check-run-results` may be preferable.

Only use `error-pattern` if none of the above works, such as when finding a
specific string pattern in a runtime panic output.

Line annotations `//~` and `error-pattern` are compatible and can be used in the same test.

### Diagnostic kinds (error levels)

The diagnostic kinds that you can have are:

- `ERROR`
- `WARN` (or `WARNING`)
- `NOTE`
- `HELP`
- `SUGGESTION`
- `RAW`

The `SUGGESTION` kind is used for specifying what the expected replacement text
should be for a diagnostic suggestion.
The `RAW` kind can be used for matching on lines from non-structured output sometimes emitted
by the compiler instead of or in addition to structured json.

`ERROR` and `WARN` kinds are required to be exhaustively covered by line annotations
`//~` by default.

Other kinds only need to be line-annotated if at least one annotation of that kind appears
in the test file.
For example, one `//~ NOTE` will also require all other `//~ NOTE`s in the file
to be written out explicitly.

Use directive `//@ dont-require-annotations` to opt out of exhaustive annotations.
E.g. use `//@ dont-require-annotations: NOTE` to annotate notes selectively.
Avoid using this directive for `ERROR`s and `WARN`ings, unless there's a serious reason, like
target-dependent compiler output.

Some diagnostics are never required to be line-annotated, regardless of their kind or directives,
for example secondary lines of multiline diagnostics,
or ubiquitous diagnostics like `aborting due to N previous errors`.

UI tests use the `-A unused` flag by default to ignore all unused warnings, as
unused warnings are usually not the focus of a test.
However, simple code samples often have unused warnings.
If the test is specifically testing an
unused warning, just add the appropriate `#![warn(unused)]` attribute as needed.

### `cfg` revisions

When using [revisions](compiletest.md#revisions), different messages can be
conditionally checked based on the current revision.
This is done by placing the revision cfg name in brackets like this:

```rust,ignore
//@ edition:2018
//@ revisions: mir thir
//@[thir] compile-flags: -Z thir-unsafeck

async unsafe fn f() {}

async fn g() {
    f(); //~ ERROR call to unsafe function is unsafe
}

fn main() {
    f(); //[mir]~ ERROR call to unsafe function is unsafe
}
```

In this example, the second error message is only emitted in the `mir` revision.
The `thir` revision only emits the first error.

If the `cfg` causes the compiler to emit different output, then a test can have
multiple `.stderr` files for the different outputs.
In the example above, there
would be a `.mir.stderr` and `.thir.stderr` file with the different outputs of
the different revisions.

> Note: cfg revisions also work inside the source code with `#[cfg]` attributes.
>
> By convention, the `FALSE` cfg is used to have an always-false config.

## Controlling pass/fail expectations

By default, a UI test is expected to **generate a compile error** because most
of the tests are checking for invalid input and error diagnostics.
However, you can also make UI tests where compilation is expected to succeed, and you can
even run the resulting program.
Just add one of the following [directives](directives.md):

- Pass directives:
  - `//@ check-pass` — compilation should succeed but skip codegen
    (which is expensive and isn't supposed to fail in most cases).
  - `//@ build-pass` — compilation and linking should succeed but do
    not run the resulting binary.
  - `//@ run-pass` — compilation should succeed and running the resulting
    binary should make it exit with code 0 which indicates success.
- Fail directives:
  - `//@ check-fail` — compilation should fail (the codegen phase is skipped).
    This is the default for UI tests.
  - `//@ build-fail` — compilation should fail during the codegen phase.
    This will run `rustc` twice:
    - First time is to ensure that the compile succeeds without the codegen phase
    - Second time is to ensure that the full compile fails
  - `//@ run-fail` — compilation should succeed, but running the resulting
    binary should make it exit with a code in the range `1..=127` which
    indicates regular failure.
    On targets without unwind support, crashes are also accepted.
  - `//@ run-crash` — compilation should succeed, but running the resulting
    binary should fail with a crash.
    Crashing is defined as "not exiting with a code in the range `0..=127`".
    - Example on Linux: Termination by `SIGABRT` or `SIGSEGV`.
    - Example on Windows: Exiting with the code for `STATUS_ILLEGAL_INSTRUCTION` (`0xC000001D`).
  - `//@ run-fail-or-crash` — compilation should succeed, but running the
    resulting binary should either `run-fail` or `run-crash`.
    Useful if a test crashes on some targets but just fails on others.

For `run-pass`, `run-fail`, `run-crash`, and `run-fail-or-crash` tests,
the output of the program itself is not checked by default.

If you want to check the output of running the program, include the `check-run-results` directive.
This will check for a `.run.stderr` and
`.run.stdout` files to compare against the actual output of the program.

Tests with the `*-pass` directives can be overridden with the `--pass` command-line option:

```sh
./x test tests/ui --pass check
```

The `--pass` option only affects UI tests.
Using `--pass check` can run the UI
test suite much faster (roughly twice as fast on my system), though obviously
not exercising as much.

The `ignore-pass` directive can be used to ignore the `--pass` CLI flag if the
test won't work properly with that override.


## Known bugs

The `known-bug` directive may be used for tests that demonstrate a known bug
that has not yet been fixed.
Adding tests for known bugs is helpful for several reasons, including:

1. Maintaining a functional test that can be conveniently reused when the bug is fixed.
2. Providing a sentinel that will fail if the bug is incidentally fixed.
   This can alert the developer so they know that the associated issue has been fixed
   and can possibly be closed.

This directive takes comma-separated issue numbers as arguments, or `"unknown"`:

- `//@ known-bug: #123, #456` (when the issues are on rust-lang/rust)
- `//@ known-bug: rust-lang/chalk#123456`
  (allows arbitrary text before the `#`, which is useful when the issue is on another repo)
- `//@ known-bug: unknown`
  (when there is no known issue yet; preferably open one if it does not already exist)

Do not include [error annotations](#error-annotations) in a test with `known-bug`.
The test should still include other normal directives and stdout/stderr files.


## Test organization

When deciding where to place a test file, please try to find a subdirectory that
best matches what you are trying to exercise.
Do your best to keep things organized.
Admittedly, it can be difficult as some tests can overlap different
categories, and the existing layout may not fit well.

Name the test by a concise description of what the test is checking.
Avoid including the issue number in the test name.
See [best practices](best-practices.md) for a more in-depth discussion of this.

Ideally, the test should be added to a directory that helps identify what piece
of code is being tested here (e.g.,
`tests/ui/borrowck/reject-move-out-of-borrow-via-pat.rs`)

When writing a new feature, you may want to **create a subdirectory to store
your tests**. For example, if you are implementing RFC 1234 ("Widgets"), then it
might make sense to put the tests in a directory like `tests/ui/rfc1234-widgets/`.

In other cases, there may already be a suitable directory.

Over time, the [`tests/ui`] directory has grown very fast.
There is a check in [tidy](intro.md#tidy) that will ensure none of the subdirectories has more than
1000 entries.
Having too many files causes problems because it isn't editor/IDE
friendly and the GitHub UI won't show more than 1000 entries.
However, since `tests/ui` (UI test root directory) and `tests/ui/issues` directories have more
than 1000 entries, we set a different limit for those directories.
So, please avoid putting a new test there and try to find a more relevant place.

For example, if your test is related to closures, you should put it in `tests/ui/closures`.
When you reach the limit, you could increase it by tweaking [here][ui test tidy].

[ui test tidy]: https://github.com/rust-lang/rust/blob/HEAD/src/tools/tidy/src/ui_tests.rs

## Rustfix tests

UI tests can validate that diagnostic suggestions apply correctly and that the
resulting changes compile correctly.
This can be done with the `run-rustfix` directive:

```rust,ignore
//@ run-rustfix
//@ check-pass
#![crate_type = "lib"]

pub struct not_camel_case {}
//~^ WARN `not_camel_case` should have an upper camel case name
//~| HELP convert the identifier to upper camel case
//~| SUGGESTION NotCamelCase
```

Rustfix tests should have a file with the `.fixed` extension which contains the
source file after the suggestion has been applied.

- When the test is run, compiletest first checks that the correct lint/warning is generated.
- Then, it applies the suggestion and compares against `.fixed` (they must match).
- Finally, the fixed source is compiled, and this compilation is required to succeed.

Usually when creating a rustfix test you will generate the `.fixed` file
automatically with the `x test --bless` option.

The `run-rustfix` directive will cause *all* suggestions to be applied, even if
they are not [`MachineApplicable`](../diagnostics.md#suggestions).
If this is a problem, then you can add the `rustfix-only-machine-applicable` directive in
addition to `run-rustfix`.
This should be used if there is a mixture of
different suggestion levels, and some of the non-machine-applicable ones do not apply cleanly.


## Compare modes

[Compare modes](compiletest.md#compare-modes) can be used to run all tests with
different flags from what they are normally compiled with.
In some cases, this might result in different output from the compiler.
To support this, different
output files can be saved which contain the output based on the compare mode.

For example, when using the Polonius mode, a test `foo.rs` will first look for
expected output in `foo.polonius.stderr`, falling back to the usual `foo.stderr` if not found.
This is useful as different modes can sometimes result in different diagnostics and behavior.
This can help track which tests have
differences between the modes, and to visually inspect those diagnostic differences.

If in the rare case you encounter a test that has different behavior, you can
run something like the following to generate the alternate stderr file:

```sh
./x test tests/ui --compare-mode=polonius --bless
```

Currently none of the compare modes are checked in CI for UI tests.

## `rustc_*` TEST attributes

The compiler defines several perma-unstable `#[rustc_*]` attributes gated behind
the internal feature `rustc_attrs` that dump extra compiler-internal information.
See the corresponding subsection in [compiler debugging] for more details.

They can be used in tests to more precisely, legibly, and easily test internal
compiler state in cases where it would otherwise be very hard to do the same
with "user-facing" Rust alone.
Indeed, one could say that this slightly abuses
the term "UI" (*user* interface) and turns such UI tests from black-box tests into white-box ones.
Use them carefully and sparingly.

[compiler debugging]: ../compiler-debugging.md#rustc_-test-attributes

## UI test mode preset lint levels

By default, test suites under UI test mode (`tests/ui`, `tests/ui-fulldeps`,
but not `tests/rustdoc-ui`) will specify

- `-A unused`
- `-W unused_attributes` (since these tend to be interesting for ui tests)
- `-A internal_features`
- `-A incomplete_features`
- `-A unused_parens`
- `-A unused_braces`

For more details, see [runtest].

[runtest]: https://github.com/rust-lang/rust/blob/HEAD/src/tools/compiletest/src/runtest.rs

If:

- The ui test's pass mode is below `run` (i.e. check or build).
- No compare modes are specified.

Since they can be very noisy in ui tests.

You can override them with `compile-flags` lint level flags or
in-source lint level attributes as required.

Note that the `rustfix` version will *not* have `-A unused` passed,
meaning that you may have to `#[allow(unused)]` to suppress `unused`
lints on the rustfix'd file (because we might be testing rustfix on `unused` lints themselves).


---

# Compiletest directives

<!--
FIXME(jieyouxu) completely revise this chapter.
-->

Directives are special comments that tell compiletest how to build and interpret a test.
They may also appear in `rmake.rs` [run-make tests](compiletest.md#run-make-tests).

They are normally put after the short comment that explains the point of this test.
Compiletest test suites use `//@` to signal that a comment is a directive.
For example, this test uses the `//@ compile-flags` command to specify a custom
flag to give to rustc when the test is compiled:

```rust,ignore
// Test the behavior of `0 - 1` when overflow checks are disabled.

//@ compile-flags: -C overflow-checks=off

fn main() {
    let x = 0 - 1;
    ...
}
```

Directives can be standalone (like `//@ run-pass`) or take a value (like `//@
compile-flags: -C overflow-checks=off`).

Directives are written one directive per line: you cannot write multiple
directives on the same line.
For example, if you write `//@ only-x86 only-windows`,
then `only-windows` is interpreted as a comment, not a separate directive.

## Listing of compiletest directives

The following is a list of compiletest directives.
Directives are linked to sections that describe the command in more detail if available.
This list may not be exhaustive.
Directives can generally be found by browsing the
`TestProps` structure found in [`directives.rs`] from the compiletest source.

[`directives.rs`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest/src/directives.rs

### Assembly

<!-- date-check: Oct 2024 -->

| Directive         | Explanation                   | Supported test suites | Possible values                        |
|-------------------|-------------------------------|-----------------------|----------------------------------------|
| `assembly-output` | Assembly output kind to check | `assembly`            | `emit-asm`, `bpf-linker`, `ptx-linker` |

### Auxiliary builds

See [Building auxiliary crates](compiletest.html#building-auxiliary-crates)

| Directive             | Explanation                                                                                           | Supported test suites                  | Possible values                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------|
| `aux-bin`             | Build a aux binary, made available in `auxiliary/bin` relative to test directory                      | All except `run-make`/`run-make-cargo` | Path to auxiliary `.rs` file                                       |
| `aux-build`           | Build a separate crate from the named source file                                                     | All except `run-make`/`run-make-cargo` | Path to auxiliary `.rs` file                                       |
| `aux-crate`           | Like `aux-build` but makes available as extern prelude                                                | All except `run-make`/`run-make-cargo` | `[<extern_modifiers>:]<extern_prelude_name>=<path/to/aux/file.rs>` |
| `aux-codegen-backend` | Similar to `aux-build` but pass the compiled dylib to `-Zcodegen-backend` when building the main file | `ui-fulldeps`                          | Path to codegen backend file                                       |
| `proc-macro`          | Similar to `aux-build`, but for aux forces host and don't use `-Cprefer-dynamic`[^pm].                | All except `run-make`/`run-make-cargo` | Path to auxiliary proc-macro `.rs` file                            |
| `build-aux-docs`      | Build docs for auxiliaries as well.  Note that this only works with `aux-build`, not `aux-crate`.     | All except `run-make`/`run-make-cargo` | N/A                                                                |

[^pm]: please see the [Auxiliary proc-macro section](compiletest.html#auxiliary-proc-macro) in the compiletest chapter for specifics.

### Controlling outcome expectations

See [Controlling pass/fail expectations](ui.md#controlling-passfail-expectations).

| Directive                   | Explanation                                 | Supported test suites                     | Possible values |
|-----------------------------|---------------------------------------------|-------------------------------------------|-----------------|
| `check-pass`                | Building (no codegen) should pass           | `ui`, `crashes`, `incremental`            | N/A             |
| `check-fail`                | Building (no codegen) should fail           | `ui`, `crashes`                           | N/A             |
| `build-pass`                | Building should pass                        | `ui`, `crashes`, `codegen`, `incremental` | N/A             |
| `build-fail`                | Building should fail                        | `ui`, `crashes`                           | N/A             |
| `run-pass`                  | Program must exit with code `0`             | `ui`, `crashes`, `incremental`            | N/A             |
| `run-fail`                  | Program must exit with code `1..=127`       | `ui`, `crashes`                           | N/A             |
| `run-crash`                 | Program must crash                          | `ui`                                      | N/A             |
| `run-fail-or-crash`         | Program must `run-fail` or `run-crash`      | `ui`                                      | N/A             |
| `ignore-pass`               | Ignore `--pass` flag                        | `ui`, `crashes`, `codegen`, `incremental` | N/A             |
| `dont-check-failure-status` | Don't check exact failure status (i.e. `1`) | `ui`, `incremental`                       | N/A             |
| `failure-status`            | On failure, the compiler must exit with this status code. To expect an ICE, use `//@ failure-status: 101`. | `ui`, `crashes`, `incremental`            | Any `u16`       |
| `should-fail`               | Compiletest self-test                       | All                                       | N/A             |

### Controlling output snapshots and normalizations

See [Normalization](ui.md#normalization), [Output
comparison](ui.md#output-comparison) and [Rustfix tests](ui.md#rustfix-tests) for more details.

| Directive                         | Explanation                                                                                                              | Supported test suites                        | Possible values                                                                         |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------|
| `check-run-results`               | Check run test binary `run-{pass,fail}` output snapshot                                                                  | `ui`, `crashes`, `incremental` if `run-pass` | N/A                                                                                     |
| `error-pattern`                   | Check that output contains a specific string                                                                             | `ui`, `crashes`, `incremental` if `run-pass` | String                                                                                  |
| `regex-error-pattern`             | Check that output contains a regex pattern                                                                               | `ui`, `crashes`, `incremental` if `run-pass` | Regex                                                                                   |
| `check-stdout`                    | Check `stdout` against `error-pattern`s from running test binary[^check_stdout]                                          | `ui`, `crashes`, `incremental`               | N/A                                                                                     |
| `normalize-stderr-32bit`          | Normalize actual stderr (for 32-bit platforms) with a rule `"<raw>" -> "<normalized>"` before comparing against snapshot | `ui`, `incremental`                          | `"<RAW>" -> "<NORMALIZED>"`, `<RAW>`/`<NORMALIZED>` is regex capture and replace syntax |
| `normalize-stderr-64bit`          | Normalize actual stderr (for 64-bit platforms) with a rule `"<raw>" -> "<normalized>"` before comparing against snapshot | `ui`, `incremental`                          | `"<RAW>" -> "<NORMALIZED>"`, `<RAW>`/`<NORMALIZED>` is regex capture and replace syntax |
| `normalize-stderr`                | Normalize actual stderr with a rule `"<raw>" -> "<normalized>"` before comparing against snapshot                        | `ui`, `incremental`                          | `"<RAW>" -> "<NORMALIZED>"`, `<RAW>`/`<NORMALIZED>` is regex capture and replace syntax |
| `normalize-stdout`                | Normalize actual stdout with a rule `"<raw>" -> "<normalized>"` before comparing against snapshot                        | `ui`, `incremental`                          | `"<RAW>" -> "<NORMALIZED>"`, `<RAW>`/`<NORMALIZED>` is regex capture and replace syntax |
| `dont-check-compiler-stderr`      | Don't check actual compiler stderr vs stderr snapshot                                                                    | `ui`                                         | N/A                                                                                     |
| `dont-check-compiler-stdout`      | Don't check actual compiler stdout vs stdout snapshot                                                                    | `ui`                                         | N/A                                                                                     |
| `dont-require-annotations`        | Don't require line annotations for the given diagnostic kind (`//~ KIND`) to be exhaustive                               | `ui`, `incremental`                          | `ERROR`, `WARN`, `NOTE`, `HELP`, `SUGGESTION`                                           |
| `run-rustfix`                     | Apply all suggestions via `rustfix`, snapshot fixed output, and check fixed output builds                                | `ui`                                         | N/A                                                                                     |
| `rustfix-only-machine-applicable` | `run-rustfix` but only machine-applicable suggestions                                                                    | `ui`                                         | N/A                                                                                     |
| `exec-env`                        | Env var to set when executing a test                                                                                     | `ui`, `crashes`                              | `<KEY>=<VALUE>`                                                                         |
| `unset-exec-env`                  | Env var to unset when executing a test                                                                                   | `ui`, `crashes`                              | Any env var name                                                                        |
| `stderr-per-bitwidth`             | Generate a stderr snapshot for each bitwidth                                                                             | `ui`                                         | N/A                                                                                     |
| `forbid-output`                   | Check that compile/run output does not contain a specific string                                                         | `ui`, `incremental`                          | String                                                                                  |
| `run-flags`                       | Flags passed to the test executable                                                                                      | `ui`                                         | Arbitrary flags                                                                         |
| `known-bug`                       | No error annotation needed due to known bug                                                                              | `ui`, `crashes`, `incremental`               | Issue number `#123456`                                                                  |
| `compare-output-by-lines`         | Compare the output by lines, rather than as a single string                                                              | All                                          | N/A                                                                                     |

[^check_stdout]: presently <!-- date-check: Oct 2024 --> this has a weird quirk
    where the test binary's stdout and stderr gets concatenated and then
    `error-pattern`s are matched on this combined output, which is ???
    slightly questionable to say the least.

### Controlling when tests are run

These directives are used to ignore the test in some situations, which
means the test won't be compiled or run.

* `ignore-X` where `X` is a target detail or other criteria on which to ignore the test (see below)
* `only-X` is like `ignore-X`, but will *only* run the test on that target or stage
* `ignore-auxiliary` is intended for files that *participate* in one or more other
  main test files but that `compiletest` should not try to build the file itself.
  Please backlink to which main test is actually using the auxiliary file.
* `ignore-test` always ignores the test.
  This can be used to temporarily disable
  a test if it is currently not working, but you want to keep it in-tree to re-enable it later.

Some examples of `X` in `ignore-X` or `only-X`:

- A full target triple: `aarch64-apple-ios`
- Architecture: `aarch64`, `arm`, `mips`, `wasm32`, `x86_64`, `x86`,
  ...
- OS: `android`, `emscripten`, `freebsd`, `ios`, `linux`, `macos`, `windows`,
  ...
- Environment (fourth word of the target triple): `gnu`, `msvc`, `musl`
- Pointer width: `32bit`, `64bit`
- Endianness: `endian-big`
- Stage: `stage1`, `stage2`
- Binary format: `elf`
- Channel: `stable`, `beta`
- When cross compiling: `cross-compile`
- When [remote testing] is used: `remote`
- When particular debuggers are being tested: `cdb`, `gdb`, `lldb`
- When particular debugger versions are matched: `ignore-gdb-version`
- When the [parallel frontend] is enabled: `ignore-parallel-frontend`
- Specific [compare modes]: `compare-mode-polonius`, `compare-mode-chalk`,
  `compare-mode-split-dwarf`, `compare-mode-split-dwarf-single`
- The two different test modes used by coverage tests:
  `ignore-coverage-map`, `ignore-coverage-run`
- When testing a dist toolchain: `dist`
  - This needs to be enabled with `COMPILETEST_ENABLE_DIST_TESTS=1`
- The `rustc_abi` of the target: e.g. `rustc_abi-x86_64-sse2`

The following directives will check rustc build settings and target settings:

- `needs-asm-support` — ignores if the **host** architecture doesn't have
  stable support for `asm!`.
  For tests that cross-compile to explicit targets
  via `--target`, use `needs-llvm-components` instead to ensure the appropriate
  backend is available.
- `needs-profiler-runtime` — ignores the test if the profiler runtime was not
  enabled for the target (`build.profiler = true` in `bootstrap.toml`)
- `needs-sanitizer-support` — ignores if the sanitizer support was not enabled
  for the target (`build.sanitizers = true` in `bootstrap.toml`)
- `needs-sanitizer-{address,hwaddress,leak,memory,thread}` — ignores if the
  corresponding sanitizer is not enabled for the target (AddressSanitizer,
  hardware-assisted AddressSanitizer, LeakSanitizer, MemorySanitizer or
  ThreadSanitizer respectively)
- `needs-run-enabled` — ignores if it is a test that gets executed, and running
  has been disabled.
  Running tests can be disabled with the `x test --run=never` flag, or running on fuchsia.
- `needs-unwind` — ignores if the target does not support unwinding
- `needs-rust-lld` — ignores if the rust lld support is not enabled (`rust.lld =
  true` in `bootstrap.toml`)
- `needs-threads` — ignores if the target does not have threading support
- `needs-subprocess`  — ignores if the target does not have subprocess support
- `needs-symlink` — ignores if the target does not support symlinks.
  This can be the case on Windows if the developer did not enable privileged symlink
  permissions.
- `ignore-std-debug-assertions` — ignores if std was built with debug assertions.
- `needs-std-debug-assertions` — ignores if std was not built with debug assertions.
- `ignore-std-remap-debuginfo` — ignores if std was built with remapping of it's sources.
- `needs-std-remap-debugino` — ignores if std was not built with remapping of it's sources.
- `ignore-rustc-debug-assertions` — ignores if rustc was built with debug assertions.
- `needs-rustc-debug-assertions` — ignores if rustc was not built with debug assertions.
- `needs-target-has-atomic` — ignores if target does not have support for all
  specified atomic widths, e.g. the test with `//@ needs-target-has-atomic: 8,
  16, ptr` will only run if it supports the comma-separated list of atomic widths.
- `needs-dynamic-linking` — ignores if target does not support dynamic linking
  (which is orthogonal to it being unable to create `dylib` and `cdylib` crate types)
- `needs-crate-type` — ignores if target platform does not support one or more
  of the comma-delimited list of specified crate types.
  For example,
  `//@ needs-crate-type: cdylib, proc-macro` will cause the test to be ignored
  on `wasm32-unknown-unknown` target because the target does not support the
  `proc-macro` crate type.
- `needs-target-std` — ignores if target platform does not have std support.
  - See also [`#![no_std]`/`#![no_core]` and implied `needs-target-std` for
    codegen tests](./compiletest.md#codegen-tests).
- `ignore-backends` — ignores the listed backends, separated by whitespace characters.
  Please note
  that this directive can be overriden with the `--bypass-ignore-backends=[BACKEND]` command line
  flag.
- `needs-backends` — only runs the test if current codegen backend is listed.
- `needs-offload` — ignores if our LLVM backend was not built with offload support.
- `needs-enzyme` — ignores if our Enzyme submodule was not built.

The following directives will check LLVM support:

- `exact-llvm-major-version: 19` — ignores if the llvm major version does not
  match the specified llvm major version.
- `min-llvm-version: 13.0` — ignored if the LLVM version is less than the given value
- `min-system-llvm-version: 12.0` — ignored if using a system LLVM and its
  version is less than the given value
- `max-llvm-major-version: 19` — ignored if the LLVM major version is higher
  than the given major version
- `ignore-llvm-version: 9.0` — ignores a specific LLVM version
- `ignore-llvm-version: 7.0 - 9.9.9` — ignores LLVM versions in a range (inclusive)
- `needs-llvm-components: powerpc` — ignores if the specific LLVM component was not built.
  Note: The test will fail on CI (when
  `COMPILETEST_REQUIRE_ALL_LLVM_COMPONENTS` is set) if the component does not exist.
- `needs-forced-clang-based-tests` — test is ignored unless the environment
  variable `RUSTBUILD_FORCE_CLANG_BASED_TESTS` is set, which enables building clang alongside LLVM
  - This is only set in two CI jobs ([`x86_64-gnu-debug`] and
    [`aarch64-gnu-debug`]), which only runs a subset of `run-make` tests.
    Other tests with this directive will not run at all, which is usually not what you want.

See also [Debuginfo tests](compiletest.md#debuginfo-tests) for directives for ignoring debuggers.

[remote testing]: running.md#running-tests-on-a-remote-machine
[parallel frontend]: compiletest.md#parallel-frontend
[compare modes]: ui.md#compare-modes
[`x86_64-gnu-debug`]: https://github.com/rust-lang/rust/blob/ab3dba92db355b8d97db915a2dca161a117e959c/src/ci/docker/host-x86_64/x86_64-gnu-debug/Dockerfile#L32
[`aarch64-gnu-debug`]: https://github.com/rust-lang/rust/blob/20c909ff9cdd88d33768a4ddb8952927a675b0ad/src/ci/docker/host-aarch64/aarch64-gnu-debug/Dockerfile#L32

### Affecting how tests are built

| Directive           | Explanation                                                                                  | Supported test suites                      | Possible values                                                                            |
|---------------------|----------------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------|
| `compile-flags`     | Flags passed to `rustc` when building the test or aux file                                   | All except for `run-make`/`run-make-cargo` | Any valid `rustc` flags, e.g. `-Awarnings -Dfoo`. Cannot be `-Cincremental` or `--edition` |
| `edition`           | The edition used to build the test                                                           | All except for `run-make`/`run-make-cargo` | Any valid `--edition` value                                                                |
| `rustc-env`         | Env var to set when running `rustc`                                                          | All except for `run-make`/`run-make-cargo` | `<KEY>=<VALUE>`                                                                            |
| `unset-rustc-env`   | Env var to unset when running `rustc`                                                        | All except for `run-make`/`run-make-cargo` | Any env var name                                                                           |
| `incremental`       | Proper incremental support for tests outside of incremental test suite                       | `ui`, `crashes`                            | N/A                                                                                        |
| `no-prefer-dynamic` | Don't use `-C prefer-dynamic`, don't build as a dylib via a `--crate-type=dylib` preset flag | `ui`, `crashes`                            | N/A                                                                                        |

<div class="warning">

Tests (outside of `run-make`/`run-make-cargo`) that want to use incremental tests not in the
incremental test-suite must not pass `-C incremental` via `compile-flags`, and
must instead use the `//@ incremental` directive.

Consider writing the test as a proper incremental test instead.

</div>

#### The edition directive

The `//@ edition` directive can take an exact edition, a bounded range of editions,
or a left-bounded half-open range of editions.
This affects which edition is used by `./x test` to run the test.

For example:

- A test with the `//@ edition: 2018` directive will only run under the 2018 edition.
- A test with the `//@ edition: 2015..2021` directive can be run under the 2015 and the 2018 edition,
  so the upper bound is exclusive just like in Rust
  (note that there's no equivalent to Rust's `..=` where the upper bound is inclusive).
  However, CI will only run the test with the lowest edition in the range (which is 2015 in this example).
- A test with the `//@ edition: 2018..` directive will run under 2018 edition or greater.
  However, CI will only run the test with the lowest edition in the range (which is 2018 in this example).

You can also force `./x test` to use a specific edition by passing the `-- --edition=` argument.
However, tests with the `//@ edition` directive will clamp the value passed to the argument.
For example, if we run `./x test -- --edition=2015`:

- A test with the `//@ edition: 2018` will run with the 2018 edition.
- A test with the `//@ edition: 2015..2021` will be run with the 2015 edition.
- A test with the `//@ edition: 2018..` will run with the 2018 edition.

### Rustdoc

| Directive   | Explanation                                                  | Supported test suites                   | Possible values           |
|-------------|--------------------------------------------------------------|-----------------------------------------|---------------------------|
| `doc-flags` | Flags passed to `rustdoc` when building the test or aux file | `rustdoc`, `rustdoc-js`, `rustdoc-json` | Any valid `rustdoc` flags |

<!--
**FIXME(rustdoc)**: what does `check-test-line-numbers-match` do?
Asked in
<https://rust-lang.zulipchat.com/#narrow/stream/266220-t-rustdoc/topic/What.20is.20the.20.60check-test-line-numbers-match.60.20directive.3F>.
-->

#### Test-suite-specific directives

The test suites [`rustdoc-html`][rustdoc-html-tests], [`rustdoc-js`/`rustdoc-js-std`][rustdoc-js-tests]
and [`rustdoc-json`][rustdoc-json-tests] each feature an additional set of directives whose basic
syntax resembles the one of compiletest directives but which are ultimately read and checked by
separate tools.
For more information, please read their respective chapters as linked above.

[rustdoc-html-tests]: ../rustdoc-internals/rustdoc-html-test-suite.md
[rustdoc-js-tests]: ../rustdoc-internals/search.html#testing-the-search-engine
[rustdoc-json-tests]: ../rustdoc-internals/rustdoc-json-test-suite.md

### Pretty printing

See [Pretty-printer](compiletest.md#pretty-printer-tests).

#### Misc directives

- `no-auto-check-cfg` — disable auto check-cfg (only for `--check-cfg` tests)
- [`revisions`](compiletest.md#revisions) — compile multiple times
- [`forbid-output`](compiletest.md#incremental-tests) — check that output does not contain a specified string
- [`reference`] — an annotation linking to a rule in the reference
- `disable-gdb-pretty-printers` — disable gdb pretty printers for debuginfo tests

[`reference`]: https://github.com/rust-lang/reference/blob/master/docs/authoring.md#test-rule-annotations

### Tool-specific directives

The following directives affect how certain command-line tools are invoked, in
test suites that use those tools:

- `filecheck-flags` adds extra flags when running LLVM's `FileCheck` tool.
  - Used by [codegen tests](compiletest.md#codegen-tests),
  [assembly tests](compiletest.md#assembly-tests), and
  [MIR-opt tests](compiletest.md#mir-opt-tests).
- `llvm-cov-flags` adds extra flags when running LLVM's `llvm-cov` tool.
  - Used by [coverage tests](compiletest.md#coverage-tests) in `coverage-run` mode.

### Tidy specific directives

The following directives control how the [tidy script](../conventions.md#formatting) verifies tests.

- `ignore-tidy-target-specific-tests` disables checking that the appropriate
  LLVM component is required (via a `needs-llvm-components` directive) when a
  test is compiled for a specific target (via the `--target` flag in a `compile-flag` directive).
- [`unused-revision-names`](compiletest.md#ignoring-unused-revision-names) -
      suppress tidy checks for mentioning unknown revision names.

## Substitutions

Directive values support substituting a few variables which will be replaced
with their corresponding value.
For example, if you need to pass a compiler flag
with a path to a specific file, something like the following could work:

```rust,ignore
//@ compile-flags: --remap-path-prefix={{src-base}}=/the/src
```

Where the sentinel `{{src-base}}` will be replaced with the appropriate path described below:

- `{{cwd}}`: The directory where compiletest is run from.
  This may not be the root of the checkout, so you should avoid using it where possible.
  - Examples: `/path/to/rust`, `/path/to/build/root`
- `{{src-base}}`: The directory where the test is defined.
  This is equivalent to `$DIR` for [output normalization].
  - Example: `/path/to/rust/tests/ui/error-codes`
- `{{build-base}}`: The base directory where the test's output goes.
  This is equivalent to `$TEST_BUILD_DIR` for [output normalization].
  - Example: `/path/to/rust/build/x86_64-unknown-linux-gnu/test/ui`
- `{{rust-src-base}}`: The sysroot directory where libstd/libcore/... are located
- `{{sysroot-base}}`: Path of the sysroot directory used to build the test.
  - Mainly intended for `ui-fulldeps` tests that run the compiler via API.
- `{{target-linker}}`: Linker that would be passed to `-Clinker` for this test,
  or blank if no linker override is active.
  - Mainly intended for `ui-fulldeps` tests that run the compiler via API.
- `{{target}}`: The target the test is compiling for
  - Example: `x86_64-unknown-linux-gnu`

See
[`tests/ui/argfile/commandline-argfile.rs`](https://github.com/rust-lang/rust/blob/HEAD/tests/ui/argfile/commandline-argfile.rs)
for an example of a test that uses this substitution.

[output normalization]: ui.md#normalization


## Adding a directive

One would add a new directive if there is a need to define some test property or
behavior on an individual, test-by-test basis.
A directive property serves as
the directive's backing store (holds the command's current value) at runtime.

To add a new directive property:

1. Look for the `pub struct TestProps` declaration in
   [`src/tools/compiletest/src/directives.rs`] and add the new public property to
   the end of the declaration.
2. Look for the `impl TestProps` implementation block immediately following the
   struct declaration and initialize the new property to its default value.

### Adding a new directive parser

When `compiletest` encounters a test file, it parses the file a line at a time
by calling every parser defined in the `Config` struct's implementation block,
also in [`src/tools/compiletest/src/directives.rs`] (note that the `Config` struct's
declaration block is found in [`src/tools/compiletest/src/common.rs`]).
`TestProps`'s `load_from()` method will try passing the current line of text to
each parser, which, in turn typically checks to see if the line begins with a
particular commented (`//@`) directive such as `//@ must-compile-successfully`
or `//@ failure-status`.
Whitespace after the comment marker is optional.

Parsers will override a given directive property's default value merely by being
specified in the test file as a directive or by having a parameter value
specified in the test file, depending on the directive.

Parsers defined in `impl Config` are typically named `parse_<directive-name>`
(note kebab-case `<directive-command>` transformed to snake-case `<directive_command>`).
`impl Config` also defines several 'low-level' parsers
which make it simple to parse common patterns like simple presence or not
(`parse_name_directive()`), `directive:parameter(s)`
(`parse_name_value_directive()`), optional parsing only if a particular `cfg`
attribute is defined (`has_cfg_prefix()`) and many more.
The low-level parsers
are found near the end of the `impl Config` block; be sure to look through them
and their associated parsers immediately above to see how they are used to avoid
writing additional parsing code unnecessarily.

As a concrete example, here is the implementation for the
`parse_failure_status()` parser, in [`src/tools/compiletest/src/directives.rs`]:

```diff
@@ -232,6 +232,7 @@ pub struct TestProps {
     // customized normalization rules
     pub normalize_stdout: Vec<(String, String)>,
     pub normalize_stderr: Vec<(String, String)>,
+    pub failure_status: i32,
 }

 impl TestProps {
@@ -260,6 +261,7 @@ impl TestProps {
             run_pass: false,
             normalize_stdout: vec![],
             normalize_stderr: vec![],
+            failure_status: 101,
         }
     }

@@ -383,6 +385,10 @@ impl TestProps {
             if let Some(rule) = config.parse_custom_normalization(ln, "normalize-stderr") {
                 self.normalize_stderr.push(rule);
             }
+
+            if let Some(code) = config.parse_failure_status(ln) {
+                self.failure_status = code;
+            }
         });

         for key in &["RUST_TEST_NOCAPTURE", "RUST_TEST_THREADS"] {
@@ -488,6 +494,13 @@ impl Config {
         self.parse_name_directive(line, "pretty-compare-only")
     }

+    fn parse_failure_status(&self, line: &str) -> Option<i32> {
+        match self.parse_name_value_directive(line, "failure-status") {
+            Some(code) => code.trim().parse::<i32>().ok(),
+            _ => None,
+        }
+    }
```

### Implementing the behavior change

When a test invokes a particular directive, it is expected that some behavior
will change as a result.
What behavior, obviously, will depend on the purpose of the directive.
In the case of `failure-status`, the behavior that changes is
that `compiletest` expects the failure code defined by the directive invoked in
the test, rather than the default value.

Although specific to `failure-status` (as every directive will have a different
implementation in order to invoke behavior change) perhaps it is helpful to see
the behavior change implementation of one case, simply as an example.
To implement `failure-status`, the `check_correct_failure_status()` function found
in the `TestCx` implementation block, located in
[`src/tools/compiletest/src/runtest.rs`], was modified as per below:

```diff
@@ -295,11 +295,14 @@ impl<'test> TestCx<'test> {
     }

     fn check_correct_failure_status(&self, proc_res: &ProcRes) {
-        // The value the Rust runtime returns on failure
-        const RUST_ERR: i32 = 101;
-        if proc_res.status.code() != Some(RUST_ERR) {
+        let expected_status = Some(self.props.failure_status);
+        let received_status = proc_res.status.code();
+
+        if expected_status != received_status {
             self.fatal_proc_rec(
-                &format!("failure produced the wrong error: {}", proc_res.status),
+                &format!("Error: expected failure status ({:?}) but received status {:?}.",
+                         expected_status,
+                         received_status),
                 proc_res,
             );
         }
@@ -320,7 +323,6 @@ impl<'test> TestCx<'test> {
         );

         let proc_res = self.exec_compiled_test();
-
         if !proc_res.status.success() {
             self.fatal_proc_rec("test run failed!", &proc_res);
         }
@@ -499,7 +501,6 @@ impl<'test> TestCx<'test> {
                 expected,
                 actual
             );
-            panic!();
         }
     }
```

Note the use of `self.props.failure_status` to access the directive property.
In tests which do not specify the failure status directive,
`self.props.failure_status` will evaluate to the default value of 101 at the time of this writing.
But for a test which specifies a directive of, for
example, `//@ failure-status: 1`, `self.props.failure_status` will evaluate to
1, as `parse_failure_status()` will have overridden the `TestProps` default
value, for that test specifically.

[`src/tools/compiletest/src/directives.rs`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest/src/directives.rs
[`src/tools/compiletest/src/common.rs`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest/src/common.rs
[`src/tools/compiletest/src/runtest.rs`]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/compiletest/src/runtest.rs


---

# `minicore` test auxiliary: using `core` stubs

<!-- date-check: Oct 2025 -->

[`tests/auxiliary/minicore.rs`][`minicore`] is a test auxiliary for ui/codegen/assembly test suites.
It provides `core` stubs for tests that need to
build for cross-compiled targets but do not need/want to run.

<div class="warning">

Please note that [`minicore`] is only intended for `core` items, and explicitly
**not** `std` or `alloc` items because `core` items are applicable to a wider range of tests.

</div>

A test can use [`minicore`] by specifying the `//@ add-minicore` directive.
Then, mark the test with `#![feature(no_core)]` + `#![no_std]` + `#![no_core]`,
and import the crate into the test with `extern crate minicore` (edition 2015)
or `use minicore` (edition 2018+).

## Implied compiler flags

Due to the `no_std` + `no_core` nature of these tests, `//@ add-minicore`
implies and requires that the test will be built with `-C panic=abort`.
**Unwinding panics are not supported.**

Tests will also be built with `-C force-unwind-tables=yes` to preserve CFI
directives in assembly tests.

TL;DR: `//@ add-minicore` implies two compiler flags:

1. `-C panic=abort`
2. `-C force-unwind-tables=yes`

## Adding more `core` stubs

If you find a `core` item to be missing from the [`minicore`] stub, consider
adding it to the test auxiliary if it's likely to be used or is already needed
by more than one test.

## Staying in sync with `core`

The `minicore` items must be kept up to date with `core`.
For consistent diagnostic output between using `core` and `minicore`, any `diagnostic`
attributes (e.g. `on_unimplemented`) should be replicated exactly in `minicore`.

## Example codegen test that uses `minicore`

```rust,no_run
//@ add-minicore
//@ revisions: meow bark
//@[meow] compile-flags: --target=x86_64-unknown-linux-gnu
//@[meow] needs-llvm-components: x86
//@[bark] compile-flags: --target=wasm32-unknown-unknown
//@[bark] needs-llvm-components: webassembly

#![crate_type = "lib"]
#![feature(no_core)]
#![no_std]
#![no_core]

extern crate minicore;
use minicore::*;

struct Meow;
impl Copy for Meow {} // `Copy` here is provided by `minicore`

// CHECK-LABEL: meow
#[unsafe(no_mangle)]
fn meow() {}
```

[`minicore`]: https://github.com/rust-lang/rust/tree/HEAD/tests/auxiliary/minicore.rs


---

# Ecosystem testing

Rust tests integration with real-world code in the ecosystem to catch
regressions and make informed decisions about the evolution of the language.

## Testing methods

### Crater

Crater is a tool which runs tests on many thousands of public projects. This
tool has its own separate infrastructure for running, and is not run as part of
CI. See the [Crater chapter](crater.md) for more details.

### `cargotest`

`cargotest` is a small tool which runs `cargo test` on a few sample projects
(such as `servo`, `ripgrep`, `tokei`, etc.). This runs as part of CI and ensures
there aren't any significant regressions:

```console
./x test src/tools/cargotest
```

### Large OSS Project builders

We have CI jobs that build large open-source Rust projects that are used as
regression tests in CI. Our integration jobs build the following projects:

- [Fuchsia](./ecosystem-test-jobs/fuchsia.md)
- [Rust for Linux](./ecosystem-test-jobs/rust-for-linux.md)


---

# Crater

[Crater](https://github.com/rust-lang/crater) is a tool for compiling and
running tests for _every_ crate on [crates.io](https://crates.io) (and a few on GitHub).
It is mainly used for checking the extent of breakage when implementing
potentially breaking changes and ensuring lack of breakage by running beta vs
stable compiler versions.

## When to run Crater

You should request a Crater run if your PR makes large changes to the compiler
or could cause breakage.
If you are unsure, feel free to ask your PR's reviewer.

## Requesting Crater Runs

The Rust team maintains a few machines that can be used for Crater runs
on the changes introduced by a PR.
If your PR needs a Crater run, leave a comment for the triage team in the PR thread.
Please inform the team whether you
require a "check-only" Crater run, a "build only" Crater run, or a "build-and-test" Crater run.
The difference is primarily in time;
if you're not sure, go for the build-and-test run.
If making changes that will only have an effect at compile-time
(e.g., implementing a new trait), then you only need a check run.

Your PR will be enqueued by the triage team and the results will be posted when they are ready.
Check runs will take around ~3-4 days, and the other two taking 5-6 days on average.

While Crater is really useful, it is also important to be aware of a few caveats:

- Not all code is on crates.io!
  There is a lot of code in repos on GitHub and elsewhere.
  Also, companies may not wish to publish their code.
  Thus, a successful Crater run does not mean there will be no
  breakage; you still need to be careful.

- Crater only runs Linux builds on x86_64. Thus, other architectures and platforms are not tested.
  Critically, this includes Windows.

- Many crates are not tested.
  This could be for a lot of reasons, including that
  the crate doesn't compile any more (e.g. used old nightly features), has
  broken or flaky tests, requires network access, or other reasons.

- Before Crater can be run, `@bors try` needs to succeed in building artifacts.
  This means that if your code doesn't compile, you cannot run Crater.


---

# Fuchsia integration tests

[Fuchsia](https://fuchsia.dev) is an open-source operating system with about 2
million lines of Rust code.[^loc] It has caught a large number of [regressions]
in the past and was subsequently included in CI.

## What to do if the Fuchsia job breaks?

Please contact the [fuchsia][fuchsia-ping] ping group and ask them for help.

```text
@rustbot ping fuchsia
```

## Building Fuchsia in CI

Fuchsia builds as part of the suite of bors tests that run before a pull request
is merged.

If you are worried that a pull request might break the Fuchsia builder and want
to test it out before submitting it to the bors queue, simply ask bors to run
the try job that builds the Fuchsia integration: `@bors try jobs=x86_64-fuchsia`.

## Building Fuchsia locally

Because Fuchsia uses languages other than Rust, it does not use Cargo as a build
system. It also requires the toolchain build to be configured in a [certain
way][build-toolchain].

The recommended way to build Fuchsia is to use the Docker scripts that check out
and run a Fuchsia build for you. If you've run Docker tests before, you can
simply run this command from your Rust checkout to download and build Fuchsia
using your local Rust toolchain.

```
src/ci/docker/run.sh x86_64-fuchsia
```

See the [Testing with Docker](../docker.md) chapter for more details on how to run
and debug jobs with Docker.

Note that a Fuchsia checkout is *large* – as of this writing, a checkout and
build takes 46G of space – and as you might imagine, it takes a while to
complete.

### Modifying the Fuchsia checkout

The main reason you would want to build Fuchsia locally is because you need to
investigate a regression. After running a Docker build, you'll find the Fuchsia
checkout inside the `obj/fuchsia` directory of your Rust checkout.  If you
modify the `KEEP_CHECKOUT` line in the [build-fuchsia.sh] script to
`KEEP_CHECKOUT=1`, you can change the checkout as needed and rerun the build
command above. This will reuse all the build results from before.

You can find more options to customize the Fuchsia checkout in the
[build-fuchsia.sh] script.

### Customizing the Fuchsia build

You can find more info about the options used to build Fuchsia in Rust CI in the
[build_fuchsia_from_rust_ci.sh] script invoked by [build-fuchsia.sh].

The Fuchsia build system uses [GN], a metabuild system that generates [Ninja]
files and then hands off the work of running the build to Ninja.

Fuchsia developers use `fx` to run builds and perform other development tasks.
This tool is located in `.jiri_root/bin` of the Fuchsia checkout; you may need
to add this to your `$PATH` for some workflows.

There are a few `fx` subcommands that are relevant, including:

- `fx set` accepts build arguments, writes them to `out/default/args.gn`, and
  runs GN.
- `fx build` builds the Fuchsia project using Ninja. It will automatically pick
  up changes to build arguments and rerun GN. By default it builds everything,
  but it also accepts target paths to build specific targets (see below).
- `fx clippy` runs Clippy on specific Rust targets (or all of them). We use this
  in the Rust CI build to avoid running codegen on most Rust targets. Underneath
  it invokes Ninja, just like `fx build`. The clippy results are saved in json
  files inside the build output directory before being printed.

#### Target paths

GN uses paths like the following to identify build targets:

```
//src/starnix/kernel:starnix_core
```

The initial `//` means the root of the checkout, and the remaining slashes are
directory names. The string after `:` is the _target name_ of a target defined
in the `BUILD.gn` file of that directory.

The target name can be omitted if it is the same as the directory name. In other
words, `//src/starnix/kernel` is the same as `//src/starnix/kernel:kernel`.

These target paths are used inside `BUILD.gn` files to reference dependencies,
and can also be used in `fx build`.

#### Modifying compiler flags

You can put custom compiler flags inside a GN `config` that is added to a
target. As a simple example:

```
config("everybody_loops") {
    rustflags = [ "-Zeverybody-loops" ]
}

rustc_binary("example") {
    crate_root = "src/bin.rs"
    # ...existing keys here...
    configs += [ ":everybody_loops" ]
}
```

This will add the flag `-Zeverybody-loops` to rustc when building the `example`
target. Note that you can also use [`public_configs`] for a config to be added
to every target that depends on that target.

If you want to add a flag to every Rust target in the build, you can add
rustflags to the [`//build/config:compiler`] config or to the OS-specific
configs referenced in that file. Note that `cflags` and `ldflags` are ignored on
Rust targets.

#### Running ninja and rustc commands directly

Going down one layer, `fx build` invokes `ninja`, which in turn eventually
invokes `rustc`. All build actions are run inside the out directory, which is
usually `out/default` inside the Fuchsia checkout.

You can get ninja to print the actual command it invokes by forcing that command
to fail, e.g. by adding a syntax error to one of the source files of the target.
Once you have the command, you can run it from inside the output directory.

After changing the toolchain itself, the build setting `rustc_version_string` in
`out/default/args.gn` needs to be changed so that `fx build` or `ninja` will
rebuild all the Rust targets. This can be done in a text editor and the contents
of the string do not matter, as long as it changes from one build to the next.
[build_fuchsia_from_rust_ci.sh] does this for you by hashing the toolchain
directory.

The Fuchsia website has more detailed documentation of the [build system].

#### Other tips and tricks

When using `build_fuchsia_from_rust_ci.sh` you can comment out the `fx set`
command after the initial run so it won't rerun GN each time. If you do this you
can also comment out the version_string line to save a couple seconds.

`export NINJA_PERSISTENT_MODE=1` to get faster ninja startup times after the
initial build.

## Fuchsia target support

To learn more about Fuchsia target support, see the Fuchsia chapter in [the
rustc book][platform-support].

[regressions]: https://gist.github.com/tmandry/7103eba4bd6a6fb0c439b5a90ae355fa
[build-toolchain]: https://fuchsia.dev/fuchsia-src/development/build/rust_toolchain
[build-fuchsia.sh]: https://github.com/rust-lang/rust/blob/221e2741c39515a5de6da42d8c76ee1e132c2c74/src/ci/docker/host-x86_64/x86_64-fuchsia/build-fuchsia.sh
[build_fuchsia_from_rust_ci.sh]: https://cs.opensource.google/fuchsia/fuchsia/+/main:scripts/rust/build_fuchsia_from_rust_ci.sh?q=build_fuchsia_from_rust_ci&ss=fuchsia
[platform-support]: https://doc.rust-lang.org/nightly/rustc/platform-support/fuchsia.html
[GN]: https://gn.googlesource.com/gn/+/main#gn
[Ninja]: https://ninja-build.org/
[`public_configs`]: https://gn.googlesource.com/gn/+/main/docs/reference.md#var_public_configs
[`//build/config:compiler`]: https://cs.opensource.google/fuchsia/fuchsia/+/main:build/config/BUILD.gn;l=121;drc=c26c473bef93b33117ae417893118907a026fec7
[build system]: https://fuchsia.dev/fuchsia-src/development/build/build_system
[fuchsia-ping]: ../../notification-groups/fuchsia.md

[^loc]: As of June 2024, Fuchsia had about 2 million lines of first-party Rust
code and a roughly equal amount of third-party code, as counted by tokei
(excluding comments and blanks).


---

# Rust for Linux integration tests

[Rust for Linux](https://rust-for-linux.com/) (RfL) is an effort for adding
support for the Rust programming language into the Linux kernel.

## What to do if the Rust for Linux job breaks?

If a PR breaks the Rust for Linux CI job, then:

- If the breakage was unintentional and seems spurious, then let [RfL][rfl-ping]
  know and retry.
    - If the PR is urgent and retrying doesn't fix it, then disable the CI job
      temporarily (comment out the `image: x86_64-rust-for-linux` job in
      `src/ci/github-actions/jobs.yml`).
- If the breakage was unintentional, then change the PR to resolve the breakage.
- If the breakage was intentional, then let [RfL][rfl-ping] know and discuss
  what will the kernel need to change.
    - If the PR is urgent, then disable the CI job temporarily (comment out
      the `image: x86_64-rust-for-linux` job in `src/ci/github-actions/jobs.yml`).
    - If the PR can wait a few days, then wait for RfL maintainers to provide a
      new Linux kernel commit hash with the needed changes done, and apply it to
      the PR, which would confirm the changes work (update the  `LINUX_VERSION`
      environment variable in `src/ci/docker/scripts/rfl-build.sh`).

If you need to contact the RfL developers, you can ping the [Rust for Linux][rfl-ping]
ping group to ask for help:

```text
@rustbot ping rfl
```

## Building Rust for Linux in CI

Rust for Linux builds as part of the suite of bors tests that run before a pull
request is merged.

The workflow builds a stage1 sysroot of the Rust compiler, downloads the Linux
kernel, and tries to compile several Rust for Linux drivers and examples using
this sysroot. RfL uses several unstable compiler/language features, therefore
this workflow notifies us if a given compiler change would break it.

If you are worried that a pull request might break the Rust for Linux builder
and want to test it out before submitting it to the bors queue, simply ask
bors to run the try job that builds the Rust for Linux integration:
`@bors try jobs=x86_64-rust-for-linux`.

[rfl-ping]: ../../notification-groups/rust-for-linux.md


---

# Codegen backend testing

See also the [Code generation](../../backend/codegen.md) chapter.

In addition to the primary LLVM codegen backend, the rust-lang/rust CI also runs tests of the [cranelift][cg_clif] and [GCC][cg_gcc] codegen backends in certain test jobs.

For more details on the tests involved, see:

- [Cranelift codegen backend tests](./cg_clif.md)
- [GCC codegen backend tests](./cg_gcc.md)

[cg_clif]: https://github.com/rust-lang/rustc_codegen_cranelift
[cg_gcc]: https://github.com/rust-lang/rustc_codegen_gcc


---

# Cranelift codegen backend tests

TODO: please add some more information to this page.


---

# GCC codegen backend

We run a subset of the compiler test suite with the GCC codegen backend on our CI, to help find changes that could break the integration of this backend with the compiler.

If you encounter any bugs or problems with the GCC codegen backend in general, don't hesitate to open issues on the
[`rustc_codegen_gcc` repository](https://github.com/rust-lang/rustc_codegen_gcc).

Note that the backend currently only supports the `x86_64-unknown-linux-gnu` target.

## Running into GCC backend CI errors

If you ran into an error related to tests executed with the GCC codegen backend on CI in the `x86_64-gnu-gcc` job,
you can use the following command to run UI tests locally using the GCC backend, which reproduces what happens on CI:

```bash
./x test tests/ui \
  --set 'rust.codegen-backends = ["llvm", "gcc"]' \
  --set 'rust.debug-assertions = false' \
  --test-codegen-backend gcc
```

If a different test suite has failed on CI, you will have to modify the `tests/ui` part.

To reproduce the whole CI job locally, you can run `cargo run --manifest-path src/ci/citool/Cargo.toml run-local x86_64-gnu-gcc`.
See [Testing with Docker](../docker.md) for more information.

### What to do in case of a GCC job failure?

If the GCC job test fails and it seems like the failure could be caused by the GCC backend, you can ping the [cg-gcc working group](https://github.com/orgs/rust-lang/teams/wg-gcc-backend) using `@rust-lang/wg-gcc-backend`

If fixing a compiler test that fails with the GCC backend is non-trivial, you can ignore that test when executed with `cg_gcc` using the `//@ ignore-backends: gcc` [compiletest directive](../directives.md).

## Choosing which codegen backends are built

The `rust.codegen-backends = [...]` bootstrap option affects which codegen backends will be built and
included in the sysroot of the produced `rustc`.
To use the GCC codegen backend, `"gcc"` has to be included in this array in `bootstrap.toml`:

```toml
rust.codegen-backends = ["llvm", "gcc"]
```

If you don't want to change your `bootstrap.toml` file, you can alternatively run your `x`
commands with `--set 'rust.codegen-backends=["llvm", "gcc"]'`.
For example:

```bash
./x build --set 'rust.codegen-backends=["llvm", "gcc"]'
```

The first backend in the `codegen-backends` array will determine which backend will be used as the
*default backend* of the built `rustc`.
This also determines which backend will be used to compile the
stage 1 standard library (or anything built in stage 2+).
To produce `rustc` that uses the GCC backend
by default, you can thus put `"gcc"` as the first element of this array:

```bash
./x build --set 'rust.codegen-backends=["gcc"]' library
```

## Choosing the codegen backend used in tests

To run compiler tests with the GCC codegen backend being used to build the test Rust programs, you can use the
`--test-codegen-backend` flag:

```bash
./x test tests/ui --test-codegen-backend gcc
```

Note that in order for this to work, the tested compiler must have the GCC codegen backend [available](#choosing-which-codegen-backends-are-built) in its sysroot directory.

## Downloading GCC from CI

The `gcc.download-ci-gcc` bootstrap option controls if GCC (which is a dependency of the GCC codegen backend)
will be downloaded from CI or built locally.
The default value is `true`, which will download GCC from CI
if there are no local changes to the GCC sources and the given host target is available on CI.

## Providing your own GCC

There are cases where you will want to provide your own `libgccjit.so` file.
One such case is when you want to cross-compile `rustc` to another target since GCC is not a multi-target compiler.
To support this use case, there is the bootstrap option `gcc.libgccjit-libs-dir`.
This option overrides `gcc.download-ci-gcc`, meaning `libgccjit.so` won't be downloaded or built locally by bootstrap.
The directory structure of this directory is `<host>/<target>/libgccjit.so`, for instance:

```
.
├── m68k-unknown-linux-gnu
│   └── m68k-unknown-linux-gnu
│       └── libgccjit.so
└── x86_64-unknown-linux-gnu
    ├── m68k-unknown-linux-gnu
    │   └── libgccjit.so
    └── x86_64-unknown-linux-gnu
        └── libgccjit.so
```

## Running tests of the backend itself

In addition to running the compiler's test suites using the GCC codegen backend, you can also run the test suite of the backend itself.

Now you do that using the following command:

```text
./x test rustc_codegen_gcc
```

The backend needs to be [enabled](#choosing-which-codegen-backends-are-built) for this to work.


---

# Performance testing

## rustc-perf

A lot of work is put into improving the performance of the compiler and
preventing performance regressions.

The [rustc-perf](https://github.com/rust-lang/rustc-perf) project provides
several services for testing and tracking performance.
It provides hosted infrastructure for running benchmarks as a service.
At this time, only `x86_64-unknown-linux-gnu` builds are tracked.

A "perf run" is used to compare the performance of the compiler in different
configurations for a large collection of popular crates.
Different
configurations include "fresh builds", builds with incremental compilation, etc.

The result of a perf run is a comparison between two versions of the compiler
(by their commit hashes).

You can also use `rustc-perf` to manually benchmark and profile the compiler
[locally](../profiling/with-rustc-perf.md).

### Automatic perf runs

After every PR is merged, a suite of benchmarks are run against the compiler.
The results are tracked over time on the <https://perf.rust-lang.org/> website.
Any changes are noted in a comment on the PR.

### Manual perf runs

Additionally, performance tests can be ran before a PR is merged on an as-needed basis.
You should request a perf run if your PR may affect performance,
especially if it can affect performance adversely.

To evaluate the performance impact of a PR, write this comment on the PR:

`@bors try @rust-timer queue`

> **Note**: Only users authorized to do perf runs are allowed to post this
> comment. Teams that are allowed to use it are tracked in the [Teams
> repository](https://github.com/rust-lang/team) with the `perf = true` value in
> the `[permissions]` section (and bors permissions are also required). If you
> are not on one of those teams, feel free to ask for someone to post it for you
> (either on [Zulip][perf run] or ask the assigned reviewer).

[perf run]: https://rust-lang.zulipchat.com/#narrow/channel/182449-t-compiler.2Fhelp/topic/perf.20run

This will first tell bors to do a "try" build which do a full release build for
`x86_64-unknown-linux-gnu`.
After the build finishes, it will place it in the queue to run the performance suite against it.
After the performance tests
finish, the bot will post a comment on the PR with a summary and a link to a full report.

If you want to do a perf run for an already built artifact (e.g. for a previous
try build that wasn't benchmarked yet), you can run this instead:

`@rust-timer build <commit-sha>`

You cannot benchmark the same artifact twice though.

More information about the available perf bot commands can be found
[here](https://perf.rust-lang.org/help.html).

More details about the benchmarking process itself are available in the [perf collector
documentation](https://github.com/rust-lang/rustc-perf/blob/master/collector/README.md).


---

# Miscellaneous testing-related info

## `RUSTC_BOOTSTRAP` and stability

<!-- date-check: Nov 2024 -->

This is a bootstrap/compiler implementation detail, but it can also be useful
for testing:

- `RUSTC_BOOTSTRAP=1` will "cheat" and bypass usual stability checking, allowing
  you to use unstable features and cli flags on a stable `rustc`.
- `RUSTC_BOOTSTRAP=-1` will force a given `rustc` to pretend it is a stable
  compiler, even if it's actually a nightly `rustc`. This is useful because some
  behaviors of the compiler (e.g. diagnostics) can differ depending on whether
  the compiler is nightly or not.

In `ui` tests and other test suites that support `//@ rustc-env`, you can specify

```rust,ignore
// Force unstable features to be usable on stable rustc
//@ rustc-env:RUSTC_BOOTSTRAP=1

// Or force nightly rustc to pretend it is a stable rustc
//@ rustc-env:RUSTC_BOOTSTRAP=-1
```

For `run-make`/`run-make-cargo` tests, `//@ rustc-env` is not supported. You can do
something like the following for individual `rustc` invocations.

```rust,ignore
use run_make_support::rustc;

fn main() {
    rustc()
        // Pretend that I am very stable
        .env("RUSTC_BOOTSTRAP", "-1")
        //...
        .run();
}
```
