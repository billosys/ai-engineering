# How to build and run the compiler

<div class="warning">

For `profile = "library"` users, or users who use `download-rustc = true | "if-unchanged"`, please be advised that
the `./x test library/std` flow where `download-rustc` is active (i.e. no compiler changes) is currently broken.
This is tracked in <https://github.com/rust-lang/rust/issues/142505>.
Only the `./x test` flow is affected in this
case, `./x {check,build} library/std` should still work.

In the short-term, you may need to disable `download-rustc` for `./x test library/std`.
This can be done either by:

1. `./x test library/std --set rust.download-rustc=false`
2. Or set `rust.download-rustc = false` in `bootstrap.toml`.

Unfortunately that will require building the stage 1 compiler.
The bootstrap team is working on this, but
implementing a maintainable fix is taking some time.

</div>


The compiler is built using a tool called `x.py`.
You will need to have Python installed to run it.

## Quick Start

For a less in-depth quick-start of getting the compiler running, see [quickstart](./quickstart.md).


## Get the source code

The main repository is [`rust-lang/rust`][repo].
This contains the compiler,
the standard library (including `core`, `alloc`, `test`, `proc_macro`, etc),
and a bunch of tools (e.g. `rustdoc`, the bootstrapping infrastructure, etc).

[repo]: https://github.com/rust-lang/rust

The very first step to work on `rustc` is to clone the repository:

```bash
git clone https://github.com/rust-lang/rust.git
cd rust
```

### Partial clone the repository

Due to the size of the repository, cloning on a slower internet connection can take a long time,
and requires disk space to store the full history of every file and directory.
Instead, it is possible to tell git to perform a _partial clone_, which will only fully retrieve
the current file contents, but will automatically retrieve further file contents when you, e.g.,
jump back in the history.
All git commands will continue to work as usual, at the price of requiring an internet connection
to visit not-yet-loaded points in history.

```bash
git clone --filter='blob:none' https://github.com/rust-lang/rust.git
cd rust
```

> **NOTE**: [This link](https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/)
> describes this type of checkout in more detail, and also compares it to other modes, such as
> shallow cloning.

### Shallow clone the repository

An older alternative to partial clones is to use shallow clone the repository instead.
To do so, you can use the `--depth N` option with the `git clone` command.
This instructs `git` to perform a "shallow clone", cloning the repository but truncating it to
the last `N` commits.

Passing `--depth 1` tells `git` to clone the repository but truncate the history to the latest
commit that is on the `main` branch, which is usually fine for browsing the source code or
building the compiler.

```bash
git clone --depth 1 https://github.com/rust-lang/rust.git
cd rust
```

> **NOTE**: A shallow clone limits which `git` commands can be run.
> If you intend to work on and contribute to the compiler, it is
> generally recommended to fully clone the repository [as shown above](#get-the-source-code),
> or to perform a [partial clone](#partial-clone-the-repository) instead.
>
> For example, `git bisect` and `git blame` require access to the commit history,
> so they don't work if the repository was cloned with `--depth 1`.

## What is `x.py`?

`x.py` is the build tool for the `rust` repository.
It can build docs, run tests, and build the compiler and standard library.

This chapter focuses on the basics to be productive, but
if you want to learn more about `x.py`, [read this chapter][bootstrap].

[bootstrap]: ./bootstrapping/intro.md

Also, using `x` rather than `x.py` is recommended as:

> `./x` is the most likely to work on every system (on Unix it runs the shell script
> that does python version detection, on Windows it will probably run the
> powershell script - certainly less likely to break than `./x.py` which often just
> opens the file in an editor).[^1]

(You can find the platform related scripts around the `x.py`, like `x.ps1`)

Notice that this is not absolute.
For instance, using Nushell in VSCode on Win10,
typing `x` or `./x` still opens `x.py` in an editor rather than invoking the program.

In the rest of this guide, we use `x` rather than `x.py` directly.
The following command:

```bash
./x check
```

could be replaced by:

```bash
./x.py check
```

### Running `x.py`

The `x.py` command can be run directly on most Unix systems in the following format:

```sh
./x <subcommand> [flags]
```

This is how the documentation and examples assume you are running `x.py`.
Some alternative ways are:

```sh
# On a Unix shell if you don't have the necessary `python3` command
./x <subcommand> [flags]

# In Windows Powershell (if powershell is configured to run scripts)
./x <subcommand> [flags]
./x.ps1 <subcommand> [flags]

# On the Windows Command Prompt (if .py files are configured to run Python)
x.py <subcommand> [flags]

# You can also run Python yourself, e.g.:
python x.py <subcommand> [flags]
```

On Windows, the Powershell commands may give you an error that looks like this:
```
PS C:\Users\vboxuser\rust> ./x
./x : File C:\Users\vboxuser\rust\x.ps1 cannot be loaded because running scripts is disabled on this system. For more
information, see about_Execution_Policies at https://go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ ./x
+ ~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

You can avoid this error by allowing powershell to run local scripts:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Running `x.py` slightly more conveniently

There is a binary that wraps `x.py` called `x` in `src/tools/x`.
All it does is run `x.py`, but it can be installed system-wide and run from any subdirectory
of a checkout.
It also looks up the appropriate version of `python` to use.

You can install it with `cargo install --path src/tools/x`.

To clarify that this is another global installed binary util, which is
similar to the one declared in section [What is `x.py`](#what-is-xpy), but
it works as an independent process to execute the `x.py` rather than calling the
shell to run the platform related scripts.

## Create a `bootstrap.toml`

To start, run `./x setup` and select the `compiler` defaults.
This will do some initialization and create a `bootstrap.toml` for you with reasonable defaults.
If you use a different default (which
you'll likely want to do if you want to contribute to an area of rust other than the compiler, such
as rustdoc), make sure to read information about that default (located in `src/bootstrap/defaults`)
as the build process may be different for other defaults.

Alternatively, you can write `bootstrap.toml` by hand.
See `bootstrap.example.toml` for all the available settings and what they do.
See `src/bootstrap/defaults` for common settings to change.

If you have already built `rustc` and you change settings related to LLVM, then you may have to
execute `./x clean --all` for subsequent configuration changes to take effect.
Note that `./x clean` will not cause a rebuild of LLVM.

## Common `x` commands

Here are the basic invocations of the `x` commands most commonly used when
working on `rustc`, `std`, `rustdoc`, and other tools.

| Command     | When to use it                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------ |
| `./x check` | Quick check to see if most things compile; [rust-analyzer can run this automatically for you][rust-analyzer] |
| `./x build` | Builds `rustc`, `std`, and `rustdoc`                                                                         |
| `./x test`  | Runs all tests                                                                                               |
| `./x fmt`   | Formats all code                                                                                             |

As written, these commands are reasonable starting points.
However, there are additional options and arguments for each of them that are worth learning for
serious development work.
In particular, `./x build` and `./x test`
provide many ways to compile or test a subset of the code, which can save a lot of time.

Also, note that `x` supports all kinds of path suffixes for `compiler`, `library`,
and `src/tools` directories.
So, you can simply run `x test tidy` instead of `x test src/tools/tidy`.
Or, `x build std` instead of `x build library/std`.

[rust-analyzer]: suggested.html#configuring-rust-analyzer-for-rustc

See the chapters on [testing](../tests/running.md) and [rustdoc](../rustdoc.md) for more details.

### Building the compiler

Note that building will require a relatively large amount of storage space.
You may want to have upwards of 10 or 15 gigabytes available to build the compiler.

Once you've created a `bootstrap.toml`, you are now ready to run `x`.
There are a lot of options here, but let's start with what is
probably the best "go to" command for building a local compiler:

```console
./x build library
```

What this command does is:
- Build `rustc` using the stage0 compiler and stage0 `std`.
- Build `library` (the standard libraries) with the stage1 compiler that was just built.
- Assemble a working stage1 sysroot, containing the stage1 compiler and stage1 standard libraries.

This final product (stage1 compiler + libs built using that compiler)
is what you need to build other Rust programs (unless you use `#![no_std]` or `#![no_core]`).

You will probably find that building the stage1 `std` is a bottleneck for you,
but fear not, there is a (hacky) workaround...
see [the section on avoiding rebuilds for std][keep-stage].

[keep-stage]: ./suggested.md#faster-rebuilds-with---keep-stage-std

Sometimes you don't need a full build.
When doing some kind of "type-based refactoring", like renaming a method, or changing the
signature of some function, you can use `./x check` instead for a much faster build.

Note that this whole command just gives you a subset of the full `rustc` build.
The **full** `rustc` build (what you get with `./x build
--stage 2 rustc`) has quite a few more steps:

- Build `rustc` with the stage1 compiler.
  - The resulting compiler here is called the "stage2" compiler, which uses stage1 std from the previous command.
- Build `librustdoc` and a bunch of other things with the stage2 compiler.

You almost never need to do this.

### Build specific components

If you are working on the standard library, you probably don't need to build
every other default component.
Instead, you can build a specific component by providing its name, like this:

```bash
./x build --stage 1 library
```

If you choose the `library` profile when running `x setup`, you can omit `--stage 1` (it's the
default).

## Creating a rustup toolchain

Once you have successfully built `rustc`, you will have created a bunch
of files in your `build` directory.
In order to actually run the resulting `rustc`, we recommend creating rustup toolchains.
The first command listed below creates the stage1 toolchain, which was built in the
steps above, with the name `stage1`.
The second command creates the stage2 toolchain using the stage1 compiler.
This will be needed in the future
if running the entire test suite, but will not be built in this page.
Building stage2 is done with the same `./x build` command as for stage1,
specifying that the stage is 2 instead.

```bash
rustup toolchain link stage1 build/host/stage1
rustup toolchain link stage2 build/host/stage2
```

Now you can run the `rustc` you built with via the toolchain.
If you run with `-vV`, you should see a version number ending in `-dev`, indicating a build from
your local environment:

```bash
$ rustc +stage1 -vV
rustc 1.48.0-dev
binary: rustc
commit-hash: unknown
commit-date: unknown
host: x86_64-unknown-linux-gnu
release: 1.48.0-dev
LLVM version: 11.0
```

The rustup toolchain points to the specified toolchain compiled in your `build` directory,
so the rustup toolchain will be updated whenever `x build` or `x test` are run for
that toolchain/stage.

**Note:** the toolchain we've built does not include `cargo`.
 In this case, `rustup` will
fall back to using `cargo` from the installed `nightly`, `beta`, or `stable` toolchain
(in that order).
 If you need to use unstable `cargo` flags, be sure to run
`rustup install nightly` if you haven't already.
 See the
[rustup documentation on custom toolchains](https://rust-lang.github.io/rustup/concepts/toolchains.html#custom-toolchains).

**Note:** rust-analyzer and IntelliJ Rust plugin use a component called
`rust-analyzer-proc-macro-srv` to work with proc macros.
If you intend to use a
custom toolchain for a project (e.g. via `rustup override set stage1`), you may
want to build this component:

```bash
./x build proc-macro-srv-cli
```

## Building targets for cross-compilation

To produce a compiler that can cross-compile for other targets,
pass any number of `target` flags to `x build`.
For example, if your host platform is `x86_64-unknown-linux-gnu`
and your cross-compilation target is `wasm32-wasip1`, you can build with:

```bash
./x build --target x86_64-unknown-linux-gnu,wasm32-wasip1
```

Note that if you want the resulting compiler to be able to build crates that
involve proc macros or build scripts, you must be sure to explicitly build target support for the
host platform (in this case, `x86_64-unknown-linux-gnu`).

If you want to always build for other targets without needing to pass flags to `x build`,
you can configure this in the `[build]` section of your `bootstrap.toml` like so:

```toml
build.target = ["x86_64-unknown-linux-gnu", "wasm32-wasip1"]
```

Note that building for some targets requires having external dependencies installed
(e.g. building musl targets requires a local copy of musl).
Any target-specific configuration (e.g. the path to a local copy of musl)
will need to be provided by your `bootstrap.toml`.
Please see `bootstrap.example.toml` for information on target-specific configuration keys.

For examples of the complete configuration necessary to build a target, please visit
[the rustc book](https://doc.rust-lang.org/rustc/platform-support.html),
select any target under the "Platform Support" heading on the left,
and see the section related to building a compiler for that target.
For targets without a corresponding page in the rustc book,
it may be useful to [inspect the Dockerfiles](../tests/docker.md)
that the Rust infrastructure itself uses to set up and configure cross-compilation.

If you have followed the directions from the prior section on creating a rustup toolchain,
then once you have built your compiler you will be able to use it to cross-compile like so:

```bash
cargo +stage1 build --target wasm32-wasip1
```

## Other `x` commands

Here are a few other useful `x` commands.
We'll cover some of them in detail in other sections:

- Building things:
  - `./x build` – builds everything using the stage 1 compiler,
    not just up to `std`
  - `./x build --stage 2` – builds everything with the stage 2 compiler including `rustdoc`
- Running tests (see the [section on running tests](../tests/running.html) for more details):
  - `./x test library/std` – runs the unit tests and integration tests from `std`
  - `./x test tests/ui` – runs the `ui` test suite
  - `./x test tests/ui/const-generics` - runs all the tests in
    the `const-generics/` subdirectory of the `ui` test suite
  - `./x test tests/ui/const-generics/const-types.rs` - runs
    the single test `const-types.rs` from the `ui` test suite

### Cleaning out build directories

Sometimes you need to start fresh, but this is normally not the case.
If you need to run this then bootstrap is most likely not acting right and
you should file a bug as to what is going wrong.
If you do need to clean everything up then you only need to run one command!

```bash
./x clean
```

`rm -rf build` works too, but then you have to rebuild LLVM, which can take
a long time even on fast computers.

## Remarks on disk space

Building the compiler (especially if beyond stage 1) can require significant amounts of free disk
space, possibly around 100GB.
This is compounded if you have a separate build directory for
rust-analyzer (e.g. `build-rust-analyzer`). This is easy to hit with dev-desktops which have a [set
disk
quota](https://github.com/rust-lang/simpleinfra/blob/8a59e4faeb75a09b072671c74a7cb70160ebef50/ansible/roles/dev-desktop/defaults/main.yml#L7)
for each user, but this also applies to local development as well.
Occasionally, you may need to:

- Remove `build/` directory.
- Remove `build-rust-analyzer/` directory (if you have a separate rust-analyzer build directory).
- Uninstall unnecessary toolchains if you use `cargo-bisect-rustc`.
  You can check which toolchains are installed with `rustup toolchain list`.

[^1]: issue[#1707](https://github.com/rust-lang/rustc-dev-guide/issues/1707)


---

# Quickstart

This is a quickstart guide about getting the compiler running. For more
information on the individual steps, see the other pages in this chapter.

First, clone the repository:

```sh
git clone https://github.com/rust-lang/rust.git
cd rust
```

When building the compiler, we don't use `cargo` directly, instead we use a
wrapper called "x". It is invoked with `./x`.

We need to create a configuration for the build. Use `./x setup` to create a
good default.

```sh
./x setup
```

Then, we can build the compiler. Use `./x build` to build the compiler, standard
library and a few tools. You can also `./x check` to just check it. All these
commands can take specific components/paths as arguments, for example `./x check
compiler` to just check the compiler.

```sh
./x build
```

> When doing a change to the compiler that does not affect the way it compiles
the standard library (so for example, a change to an error message), use
`--keep-stage-std 1` to avoid recompiling it.

After building the compiler and standard library, you now have a working
compiler toolchain. You can use it with rustup by linking it.

```sh
rustup toolchain link stage1 build/host/stage1
```

Now you have a toolchain called `stage1` linked to your build. You can use it to
test the compiler.

```sh
rustc +stage1 testfile.rs
```

After doing a change, you can run the compiler test suite with `./x test`.

`./x test` runs the full test suite, which is slow and rarely what you want.
Usually, `./x test tests/ui` is what you want after a compiler change, testing
all [UI tests](../tests/ui.md) that invoke the compiler on a specific test file
and check the output.

```sh
./x test tests/ui
```

Use `--bless` if you've made a change and want to update the `.stderr` files
with the new output.

Congrats, you are now ready to make a change to the compiler! If you have more
questions, [the full chapter](./how-to-build-and-run.md) might contain the
answers, and if it doesn't, feel free to ask for help on
[Zulip](https://rust-lang.zulipchat.com/#narrow/stream/182449-t-compiler.2Fhelp).

If you use VSCode, Vim, Emacs, Helix or Zed, `./x setup` will ask you if you want to
set up the editor config. For more information, check out [suggested
workflows](./suggested.md).


---

# Prerequisites

## Dependencies

See [the `rust-lang/rust` INSTALL](https://github.com/rust-lang/rust/blob/HEAD/INSTALL.md#dependencies).

## Hardware

You will need an internet connection to build. The bootstrapping process
involves updating git submodules and downloading a beta compiler. It doesn't
need to be super fast, but that can help.

There are no strict hardware requirements, but building the compiler is
computationally expensive, so a beefier machine will help, and I wouldn't
recommend trying to build on a Raspberry Pi! We recommend the following.
* 30GB+ of free disk space. Otherwise, you will have to keep
  clearing incremental caches. More space is better, the compiler is a bit of a
  hog; it's a problem we are aware of.
* 8GB+ RAM
* 2+ cores. Having more cores really helps. 10 or 20 or more is not too many!

Beefier machines will lead to much faster builds. If your machine is not very
powerful, a common strategy is to only use `./x check` on your local machine
and let the CI build test your changes when you push to a PR branch.

Building the compiler takes more than half an hour on my moderately powerful
laptop. We suggest downloading LLVM from CI so you don't have to build it from source
([see here][config]).

Like `cargo`, the build system will use as many cores as possible. Sometimes
this can cause you to run low on memory. You can use `-j` to adjust the number
of concurrent jobs. If a full build takes more than ~45 minutes to an hour, you
are probably spending most of the time swapping memory in and out; try using
`-j1`.

If you don't have too much free disk space, you may want to turn off
incremental compilation ([see here][config]). This will make compilation take
longer (especially after a rebase), but will save a ton of space from the
incremental caches.

[config]: ./how-to-build-and-run.md#create-a-bootstraptoml


---

# Suggested workflows

The full bootstrapping process takes quite a while.
Here are some suggestions to make your life easier.

## Installing a pre-push hook

CI will automatically fail your build if it doesn't pass `tidy`, our internal
tool for ensuring code quality.
If you'd like, you can install a [Git
hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) that will
automatically run `./x test tidy` on each push, to ensure your code is up to par.
If the hook fails then run `./x test tidy --bless` and commit the changes.
If you decide later that the pre-push behavior is undesirable, you can delete
the `pre-push` file in `.git/hooks`.

A prebuilt git hook lives at [`src/etc/pre-push.sh`].
 It can be copied into your `.git/hooks` folder as `pre-push` (without the `.sh` extension!).

You can also install the hook as a step of running `./x setup`!

## Config extensions

When working on different tasks, you might need to switch between different bootstrap configurations.
Sometimes you may want to keep an old configuration for future use.
But saving raw config values in
random files and manually copying and pasting them can quickly become messy, especially if you have a
long history of different configurations.

To simplify managing multiple configurations, you can create config extensions.

For example, you can create a simple config file named `cross.toml`:

```toml
[build]
build = "x86_64-unknown-linux-gnu"
host = ["i686-unknown-linux-gnu"]
target = ["i686-unknown-linux-gnu"]


[llvm]
download-ci-llvm = false

[target.x86_64-unknown-linux-gnu]
llvm-config = "/path/to/llvm-19/bin/llvm-config"
```

Then, include this in your `bootstrap.toml`:

```toml
include = ["cross.toml"]
```

You can also include extensions within extensions recursively.

**Note:** In the `include` field, the overriding logic follows a right-to-left order.
For example,
in `include = ["a.toml", "b.toml"]`, extension `b.toml` overrides `a.toml`.
Also, parent extensions always override the inner ones.

## Configuring `rust-analyzer` for `rustc`

### Checking the "library" tree

Checking the "library" tree requires a stage1 compiler, which can be a heavy process on some computers.
For this reason, bootstrap has a flag called `--skip-std-check-if-no-download-rustc` that skips checking the
"library" tree if `rust.download-rustc` isn't available.
If you want to avoid putting a heavy load on your computer
with `rust-analyzer`, you can add the `--skip-std-check-if-no-download-rustc` flag to your `./x check` command in
the `rust-analyzer` configuration.

### Project-local rust-analyzer setup

`rust-analyzer` can help you check and format your code whenever you save a file.
By default, `rust-analyzer` runs the `cargo check` and `rustfmt` commands,
but you can override these commands to use more adapted versions of these tools
when hacking on `rustc`.
With custom setup, `rust-analyzer` can use `./x check`
to check the sources, and the stage 0 rustfmt to format them.

The default `rust-analyzer.check.overrideCommand` command line will check all
the crates and tools in the repository.
If you are working on a specific part,
you can override the command to only check the part you are working on to save checking time.
For example, if you are working on the compiler, you can override
the command to `x check compiler --json-output` to only check the compiler part.
You can run `x check --help --verbose` to see the available parts.

Running `./x setup editor` will prompt you to create a project-local LSP config
file for one of the supported editors.
You can also create the config file as a step of running `./x setup`.

### Using a separate build directory for rust-analyzer

By default, when rust-analyzer runs a check or format command, it will share
the same build directory as manual command-line builds.
This can be inconvenient for two reasons:
- Each build will lock the build directory and force the other to wait, so it
  becomes impossible to run command-line builds while rust-analyzer is running
  commands in the background.
- There is an increased risk of one of the builds deleting previously-built
  artifacts due to conflicting compiler flags or other settings, forcing
  additional rebuilds in some cases.

To avoid these problems:
- Add `--build-dir=build-rust-analyzer` to all of the custom `x` commands in
  your editor's rust-analyzer configuration.
  (Feel free to choose a different directory name if desired.)
- Modify the `rust-analyzer.rustfmt.overrideCommand` setting so that it points
  to the copy of `rustfmt` in that other build directory.
- Modify the `rust-analyzer.procMacro.server` setting so that it points to the
  copy of `rust-analyzer-proc-macro-srv` in that other build directory.

Using separate build directories for command-line builds and rust-analyzer
requires extra disk space.

### Visual Studio Code

Selecting `vscode` in `./x setup editor` will prompt you to create a
`.vscode/settings.json` file which will configure Visual Studio code.
The recommended `rust-analyzer` settings live at [`src/etc/rust_analyzer_settings.json`].

If running `./x check` on save is inconvenient, in VS Code you can use a [Build Task] instead:

```JSON
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "./x check",
            "command": "./x check",
            "type": "shell",
            "problemMatcher": "$rustc",
            "presentation": { "clear": true },
            "group": { "kind": "build", "isDefault": true }
        }
    ]
}
```

[Build Task]: https://code.visualstudio.com/docs/editor/tasks


### Neovim

For Neovim users, there are a few options:

1. The easiest way is using [neoconf.nvim][neoconf.nvim] but it uses the
   deprecated `require('lspconfig')` API which displays a warning on neovim 0.11+.
2. Using `coc.nvim` is another option but it requires node.js to be installed.
3. Using a custom script to load rust-analyzer settings.

#### neoconf.nvim

[neoconf.nvim][neoconf.nvim] allows for project-local configuration
files with the native LSP. The steps for how to use it are below. Note that they require
rust-analyzer to already be configured with Neovim. Steps for this can be
[found here][r-a nvim lsp].

1. First install the plugin.
   This can be done by following the steps in the README.
2. Run `./x setup editor`, and select `vscode` to create a `.vscode/settings.json` file.
   `neoconf` is able to read and update
   rust-analyzer settings automatically when the project is opened when this file is detected.

#### coc.nvim

If you're using `coc.nvim`, you can run `./x setup editor` and select `vim` to
create a `.vim/coc-settings.json`.
The settings can be edited with `:CocLocalConfig`.
The recommended settings live at [`src/etc/rust_analyzer_settings.json`].

#### Custom LSP settings

If you're running neovim 0.11+, you can configure rust-analyzer with just
[nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) and a custom script.

1. Make sure [rust-analyzer LSP][r-a nvim lsp] is set up
2. Create `$HOME/.config/nvim/after/plugged/rust_analyzer.lua` with the following content:

```lua
-- Capture the default functions from nvim-lspconfig/lsp/rust_analyzer.lua before overriding it.
-- This file is in after/plugin to guarantee nvim-lspconfig has been initialised already.
local default_root_dir = vim.lsp.config["rust_analyzer"].root_dir
local default_before_init = vim.lsp.config["rust_analyzer"].before_init

vim.lsp.config("rust_analyzer", {
    cmd = { "rust-analyzer" },
    filetypes = { "rust" },
    -- To support rust-lang/rust, we need to detect when we're in the rust repo and use the git root
    -- instead of cargo project root.
    root_dir = function(bufnr, on_dir)
        local git_root = vim.fs.root(bufnr, { ".git" })
        if git_root then
            if vim.uv.fs_stat(vim.fs.joinpath(git_root, "src/etc/rust_analyzer_zed.json")) then
                on_dir(git_root)
                return
            end
        end
        -- For anything that doesn't match rust-lang/rust, fallback to default root_dir
        default_root_dir(bufnr, on_dir)
    end,
    before_init = function(init_params, config)
        -- When inside rust-lang/rust, we need to use the special rust-analyzer settings.
        local settings = vim.fs.joinpath(config.root_dir, "src/etc/rust_analyzer_zed.json")
        if vim.uv.fs_stat(settings) then
            local file = io.open(settings)
            -- nvim 0.12+ supports comments otherwise you'll need content:gsub("//[^\n]*", "").
            local json = vim.json.decode(file:read("*a"), { skip_comments = true })
            file:close()
            config.settings["rust-analyzer"] = vim.tbl_deep_extend(
                "force", -- Overwrite with the special settings when there is a conflict.
                config.settings["rust-analyzer"] or {},
                json.lsp["rust-analyzer"].initialization_options
            )
        end
        default_before_init(init_params, config)
    end,
})

vim.lsp.enable("rust_analyzer")
```

If you would like to use the build task that is described above, you may either
make your own command in your config, or you can install a plugin such as
[overseer.nvim](https://github.com/stevearc/overseer.nvim) that can [read VSCode's `task.json`
files](https://github.com/stevearc/overseer.nvim/blob/master/doc/guides.md#vs-code-tasks),
and follow the same instructions as above.

[neoconf.nvim]: https://github.com/folke/neoconf.nvim/
[r-a nvim lsp]: https://rust-analyzer.github.io/book/other_editors.html#nvim-lsp

### Emacs

Emacs provides support for rust-analyzer with project-local configuration
through [Eglot](https://www.gnu.org/software/emacs/manual/html_node/eglot/).
Steps for setting up Eglot with rust-analyzer can be [found
here](https://rust-analyzer.github.io/manual.html#eglot).
Having set up Emacs & Eglot for Rust development in general, you can run
`./x setup editor` and select `emacs`, which will prompt you to create
`.dir-locals.el` with the recommended configuration for Eglot.
The recommended settings live at [`src/etc/rust_analyzer_eglot.el`].
For more information on project-specific Eglot configuration, consult [the
manual](https://www.gnu.org/software/emacs/manual/html_node/eglot/Project_002dspecific-configuration.html).

### Helix

Helix comes with built-in LSP and rust-analyzer support.
It can be configured through `languages.toml`, as described
[here](https://docs.helix-editor.com/languages.html).
You can run `./x setup editor` and select `helix`, which will prompt you to
create `languages.toml` with the recommended configuration for Helix.
The recommended settings live at [`src/etc/rust_analyzer_helix.toml`].

### Zed

Zed comes with built-in LSP and rust-analyzer support.
It can be configured through `.zed/settings.json`, as described
[here](https://zed.dev/docs/configuring-languages).
Selecting `zed` in `./x setup editor` will prompt you to create a `.zed/settings.json`
file which will configure Zed with the recommended configuration.
The recommended `rust-analyzer` settings live at [`src/etc/rust_analyzer_zed.json`].

## Check, check, and check again

When doing simple refactoring, it can be useful to run `./x check` continuously.
If you set up `rust-analyzer` as described above, this will be
done for you every time you save a file.
Here you are just checking that the
compiler can **build**, but often that is all you need (e.g., when renaming a
method).
You can then run `./x build` when you actually need to run tests.

In fact, it is sometimes useful to put off tests even when you are not 100% sure the code will work.
You can then keep building up refactoring commits and only run the tests at some later time.
You can then use `git bisect` to track down **precisely** which commit caused the problem.
A nice side-effect of this style
is that you are left with a fairly fine-grained set of commits at the end, all
of which build and pass tests.
This often helps reviewing.

## Configuring `rustup` to use nightly

Some parts of the bootstrap process uses pinned, nightly versions of tools like rustfmt.
To make things like `cargo fmt` work correctly in your repo,
[install a nightly toolchain] with rustup, then run this command:

```console
cd <path to rustc repo>
rustup override set nightly
```

Don't forget to do this for all directories you have [setup a worktree for].
You may need to use the
pinned nightly version from `src/stage0`, but often the normal `nightly` channel will work.

**Note** see [the section on vscode] for how to configure it with this real
rustfmt `x` uses, and [the section on rustup] for how to setup `rustup`
toolchain for your bootstrapped compiler

**Note** This does _not_ allow you to build `rustc` with cargo directly.
You still have to use `x` to work on the compiler or standard library, this just
lets you use `cargo fmt`.

[install a nightly toolchain]: https://rust-lang.github.io/rustup/concepts/channels.html?highlight=nightl#working-with-nightly-rust
[setup a worktree for]: ./suggested.md#working-on-multiple-branches-at-the-same-time
[the section on vscode]: suggested.md#configuring-rust-analyzer-for-rustc
[the section on rustup]: how-to-build-and-run.md?highlight=rustup#creating-a-rustup-toolchain

## Faster Builds with CI-rustc

If you are not working on the compiler, you often don't need to build the compiler tree.
For example, you can skip building the compiler and only build the `library` tree or the
tools under `src/tools`.
To achieve that, you have to enable this by setting the `download-rustc`
option in your configuration.
This tells bootstrap to use the latest nightly compiler for `stage > 0`
steps, meaning it will have two precompiled compilers: stage0 compiler and `download-rustc` compiler
for `stage > 0` steps.
This way, it will never need to build the in-tree compiler.
As a result, your build time will be significantly reduced by not building the in-tree compiler.

## Faster rebuilds with `--keep-stage-std`

Sometimes just checking whether the compiler builds is not enough.
A common example is that you need to add a `debug!` statement to inspect the value of
some state or better understand the problem.
In that case, you don't really need a full build.
By bypassing bootstrap's cache invalidation, you can often get
these builds to complete very fast (e.g., around 30 seconds). The only catch is
this requires a bit of fudging and may produce compilers that don't work (but
that is easily detected and fixed).

The sequence of commands you want is as follows:

- Initial build: `./x build library`
- Subsequent builds: `./x build library --keep-stage-std=1`
  - Note that we added the `--keep-stage-std=1` flag here

As mentioned, the effect of `--keep-stage-std=1` is that we just _assume_ that the
old standard library can be re-used.
If you are editing the compiler, this is
often true: you haven't changed the standard library, after all.
But sometimes, it's not true: for example, if you are editing the "metadata" part of
the compiler, which controls how the compiler encodes types and other states
into the `rlib` files, or if you are editing things that wind up in the metadata
(such as the definition of the MIR).

**The TL;DR is that you might get weird behavior from a compile when using
`--keep-stage-std=1`** -- for example, strange [ICEs](../appendix/glossary.html#ice)
or other panics.
In that case, you should simply remove the `--keep-stage-std=1` from the command and rebuild.
That ought to fix the problem.

You can also use `--keep-stage-std=1` when running tests.
Something like this:

- Initial test run: `./x test tests/ui`
- Subsequent test run: `./x test tests/ui --keep-stage-std=1`

## Using incremental compilation

You can further enable the `--incremental` flag to save additional time in subsequent rebuilds:

```bash
./x test tests/ui --incremental --test-args issue-1234
```

If you don't want to include the flag with every command, you can enable it in the `bootstrap.toml`:

```toml
[rust]
incremental = true
```

Note that incremental compilation will use more disk space than usual.
If disk space is a concern for you, you might want to check the size of the `build`
directory from time to time.

## Fine-tuning optimizations

Setting `optimize = false` makes the compiler too slow for tests.
However, to improve the test cycle, you can disable optimizations selectively only for the
crates you'll have to rebuild
([source](https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler/topic/incremental.20compilation.20question/near/202712165)).
For example, when working on `rustc_mir_build`, the `rustc_mir_build` and
`rustc_driver` crates take the most time to incrementally rebuild.
You could therefore set the following in the root `Cargo.toml`:

```toml
[profile.release.package.rustc_mir_build]
opt-level = 0
[profile.release.package.rustc_driver]
opt-level = 0
```

## Working on multiple branches at the same time

Working on multiple branches in parallel can be a little annoying, since
building the compiler on one branch will cause the old build and the incremental
compilation cache to be overwritten.
One solution would be to have multiple
clones of the repository, but that would mean storing the Git metadata multiple
times, and having to update each clone individually.

Fortunately, Git has a better solution called [worktrees].
This lets you create multiple "working trees", which all share the same Git database.
Moreover,
because all of the worktrees share the same object database, if you update a
branch (e.g. `main`) in any of them, you can use the new commits from any of the
worktrees.
One caveat, though, is that submodules do not get shared.
They will still be cloned multiple times.

[worktrees]: https://git-scm.com/docs/git-worktree

Given you are inside the root directory for your Rust repository, you can create
a "linked working tree" in a new "rust2" directory by running the following command:

```bash
git worktree add ../rust2
```

Creating a new worktree for a new branch based on `main` looks like:

```bash
git worktree add -b my-feature ../rust2 main
```

You can then use that rust2 folder as a separate workspace for modifying and building `rustc`!

## Working with nix

Several nix configurations are defined in `src/tools/nix-dev-shell`.

If you're using direnv, you can create a symbolic link to `src/tools/nix-dev-shell/envrc-flake` or `src/tools/nix-dev-shell/envrc-shell`

```bash
ln -s ./src/tools/nix-dev-shell/envrc-flake ./.envrc # Use flake
```
or
```bash
ln -s ./src/tools/nix-dev-shell/envrc-shell ./.envrc # Use nix-shell
```

If you're using the flake, make sure to also update it with the following command:

```
nix flake update --flake ./src/tools/nix-dev-shell
```

The shell creates a command named `x` that runs the `./x.py` script with all dependencies
set up correctly.

### Note

Note that when using nix on a not-NixOS distribution, it may be necessary to set
**`build.patch-binaries-for-nix = true` in `bootstrap.toml`**. Bootstrap tries to detect
whether it's running in nix and enable patching automatically, but this
detection can have false negatives.

You can also use your nix shell to manage `bootstrap.toml`:

```nix
let
  config = pkgs.writeText "rustc-config" ''
    # Your bootstrap.toml content goes here
  ''
pkgs.mkShell {
  /* ... */
  # This environment variable tells bootstrap where our bootstrap.toml is.
  RUST_BOOTSTRAP_CONFIG = config;
}
```

## Shell Completions

If you use Bash, Zsh, Fish or PowerShell, you can find automatically-generated shell
completion scripts for `x.py` in
[`src/etc/completions`](https://github.com/rust-lang/rust/tree/HEAD/src/etc/completions).

You can use `source ./src/etc/completions/x.py.<extension>` to load completions
for your shell of choice, or `& .\src\etc\completions\x.py.ps1` for PowerShell.
Adding this to your shell's startup script (e.g. `.bashrc`) will automatically
load this completion.

[`src/etc/rust_analyzer_settings.json`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/rust_analyzer_settings.json
[`src/etc/rust_analyzer_eglot.el`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/rust_analyzer_eglot.el
[`src/etc/rust_analyzer_helix.toml`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/rust_analyzer_helix.toml
[`src/etc/rust_analyzer_zed.json`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/rust_analyzer_zed.json
[`src/etc/pre-push.sh`]: https://github.com/rust-lang/rust/blob/HEAD/src/etc/pre-push.sh


---

# Build distribution artifacts

You might want to build and package up the compiler for distribution.
You’ll want to run this command to do it:

```bash
./x dist
```

# Install from source

You might want to prefer installing Rust (and tools configured in your configuration)
by building from source. If so, you want to run this command:

```bash
./x install
```

   Note: If you are testing out a modification to a compiler, you might
   want to build the compiler (with `./x build`) then create a toolchain as
   discussed in [here][create-rustup-toolchain].

   For example, if the toolchain you created is called "foo", you would then
   invoke it with `rustc +foo ...` (where ... represents the rest of the arguments).

Instead of installing Rust (and tools in your config file) globally, you can set `DESTDIR`
environment variable to change the installation path. If you want to set installation paths
more dynamically, you should prefer [install options] in your config file to achieve that.

[create-rustup-toolchain]: ./how-to-build-and-run.md#creating-a-rustup-toolchain
[install options]: https://github.com/rust-lang/rust/blob/f7c8928f035370be33463bb7f1cd1aeca2c5f898/config.example.toml#L422-L442

---

# Building documentation

This chapter describes how to build documentation of toolchain components,
like the standard library (std) or the compiler (rustc).

- Document everything

  This uses `rustdoc` from the beta toolchain,
  so will produce (slightly) different output to stage 1 rustdoc,
  as rustdoc is under active development:

  ```bash
  ./x doc
  ```

  If you want to be sure the documentation looks the same as on CI:

  ```bash
  ./x doc --stage 1
  ```

  This ensures that (current) rustdoc gets built,
  then that is used to document the components.

- Much like running individual tests or building specific components,
  you can build just the documentation you want:

  ```bash
  ./x doc src/doc/book
  ./x doc src/doc/nomicon
  ./x doc compiler library
  ```

  See [the nightly docs index page](https://doc.rust-lang.org/nightly/) for a full list of books.

- Document internal rustc items

  Compiler documentation is not built by default.
  To create it by default with `x doc`, modify `bootstrap.toml`:

  ```toml
  build.compiler-docs = true
  ```

  Note that when enabled,
  documentation for internal compiler items will also be built.

  NOTE: The documentation for the compiler is found at [this link].

[this link]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/


---

# Rustdoc overview

`rustdoc` lives in-tree with the compiler and standard library.
This chapter is about how it works.
For information about Rustdoc's features and how to use them, see
the [Rustdoc book](https://doc.rust-lang.org/nightly/rustdoc/).
For more details about how rustdoc works, see the ["Rustdoc internals" chapter][Rustdoc internals].

[Rustdoc internals]: ./rustdoc-internals.md

`rustdoc` uses `rustc` internals (and, of course, the standard library), so you
will have to build the compiler and `std` once before you can build `rustdoc`.

Rustdoc is implemented entirely within the crate [`librustdoc`][rd].
It runs the compiler up to the point where we have an internal representation of a
crate (HIR) and the ability to run some queries about the types of items.
[HIR] and [queries] are discussed in the linked chapters.

[HIR]: ./hir.md
[queries]: ./query.md
[rd]: https://github.com/rust-lang/rust/tree/HEAD/src/librustdoc

`librustdoc` performs two major steps after that to render a set of documentation:

* "Clean" the AST into a form that's more suited to creating documentation (and
  slightly more resistant to churn in the compiler).
* Use this cleaned AST to render a crate's documentation, one page at a time.

Naturally, there's more than just this, and those descriptions simplify out
lots of details, but that's the high-level overview.

(Side note: `librustdoc` is a library crate!
The `rustdoc` binary is created using the project in [`src/tools/rustdoc`][bin].
Note that literally all that does is call the `main()` that's in this crate's `lib.rs`, though.)

[bin]: https://github.com/rust-lang/rust/tree/HEAD/src/tools/rustdoc

## Cheat sheet

* Run `./x setup tools` before getting started.
  This will configure `x` with nice settings for developing rustdoc and other tools, including
  downloading a copy of rustc rather than building it.
* Use `./x check rustdoc` to quickly check for compile errors.
* Use `./x build library rustdoc` to make a usable rustdoc you can run on other projects.
  * Add `library/test` to be able to use `rustdoc --test`.
  * Run `rustup toolchain link stage2 build/host/stage2` to add a
    custom toolchain called `stage2` to your rustup environment.
    After running that, `cargo +stage2 doc` in any directory will build with
    your locally-compiled rustdoc.
* Use `./x doc library` to use this rustdoc to generate the standard library docs.
  * The completed docs will be available in `build/host/doc` (under `core`, `alloc`, and `std`).
  * If you want to copy those docs to a webserver, copy all of
    `build/host/doc`, since that's where the CSS, JS, fonts, and landing page are.
  * For frontend debugging, disable the `rust.docs-minification` option in [`bootstrap.toml`].
* Use `./x test tests/rustdoc*` to run the tests using a stage1 rustdoc.
  * See [Rustdoc internals] for more information about tests.
* Use `./x test tidy --extra-checks=js` to run rustdoc’s JavaScript checks (`eslint`, `es-check`, and `tsc`).
> **Note:** `./x test tidy` already runs these checks automatically when JS/TS sources changed; `--extra-checks=js` forces them explicitly.

### JavaScript CI checks

Rustdoc’s JavaScript and TypeScript are checked during CI by `eslint`, `es-check`, and `tsc` (not by compiletest).
These run as part of the `tidy` job.

```console
./x test tidy --extra-checks=js
```

The `--extra-checks=js` flag enables the frontend linting that runs in CI.

[`bootstrap.toml`]: ./building/how-to-build-and-run.md

## Code structure

All paths in this section are relative to `src/librustdoc/` in the rust-lang/rust repository.

* Most of the HTML printing code is in `html/format.rs` and `html/render/mod.rs`.
  It's in a bunch of functions returning `impl std::fmt::Display`.
* The data types that get rendered by the functions mentioned above are defined in `clean/types.rs`.
  The functions responsible for creating them from the `HIR` and the `rustc_middle::ty` IR
  live in `clean/mod.rs`.
* The bits specific to using rustdoc as a test harness are in `doctest.rs`.
* The Markdown renderer is loaded up in `html/markdown.rs`, including functions
  for extracting doctests from a given block of Markdown.
* Frontend CSS and JavaScript are stored in `html/static/`.
  * Re.
    JavaScript, type annotations are written using [TypeScript-flavored JSDoc]
comments and an external `.d.ts` file.
    This way, the code itself remains plain, valid JavaScript.
    We only use `tsc` as a linter.

[TypeScript-flavored JSDoc]: https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html

## Tests

`rustdoc`'s integration tests are split across several test suites.
See [Rustdoc tests suites](tests/compiletest.md#rustdoc-test-suites) for more details.

## Constraints

We try to make rustdoc work reasonably well with JavaScript disabled, and when browsing local files.
We have [a list of supported browsers].

Supporting local files (`file:///` URLs) brings some surprising restrictions.
Certain browser features that require secure origins, like `localStorage` and
Service Workers, don't work reliably.
We can still use such features, but we should make sure pages are still usable without them.

Rustdoc [does not type-check function bodies][platform-specific docs].
This works by [overriding the built-in queries for typeck][override queries],
by [silencing name resolution errors], and by [not resolving opaque types].
This comes with several caveats: in particular, rustdoc *cannot* run any parts of the compiler that
require type-checking bodies;
for example, it cannot generate `.rlib` files or run most lints.
We want to move away from this model eventually, but we need some alternative for
[the people using it][async-std];
see [various][zulip stop accepting broken code]
[previous][rustdoc meeting 2024-07-08] [Zulip][compiler meeting 2023-01-26] [discussions][notriddle rfc].
For examples of code that breaks if this hack is removed, see
[`tests/rustdoc-ui/error-in-impl-trait`].

[platform-specific docs]: https://doc.rust-lang.org/rustdoc/advanced-features.html#interactions-between-platform-specific-docs
[override queries]: https://github.com/rust-lang/rust/blob/52bf0cf795dfecc8b929ebb1c1e2545c3f41d4c9/src/librustdoc/core.rs#L299-L323
[silencing name resolution errors]: https://github.com/rust-lang/rust/blob/52bf0cf795dfecc8b929ebb1c1e2545c3f41d4c9/compiler/rustc_resolve/src/late.rs#L4517
[not resolving opaque types]: https://github.com/rust-lang/rust/blob/52bf0cf795dfecc8b929ebb1c1e2545c3f41d4c9/compiler/rustc_hir_analysis/src/check/check.rs#L188-L194
[async-std]: https://github.com/rust-lang/rust/issues/75100
[rustdoc meeting 2024-07-08]: https://rust-lang.zulipchat.com/#narrow/channel/393423-t-rustdoc.2Fmeetings/topic/meeting.202024-07-08/near/449969836
[compiler meeting 2023-01-26]: https://rust-lang.zulipchat.com/#narrow/channel/238009-t-compiler.2Fmeetings/topic/.5Bweekly.5D.202023-01-26/near/323755789
[zulip stop accepting broken code]: https://rust-lang.zulipchat.com/#narrow/stream/266220-rustdoc/topic/stop.20accepting.20broken.20code
[notriddle rfc]: https://rust-lang.zulipchat.com/#narrow/channel/266220-t-rustdoc/topic/Pre-RFC.3A.20stop.20accepting.20broken.20code
[`tests/rustdoc-ui/error-in-impl-trait`]: https://github.com/rust-lang/rust/tree/163cb4ea3f0ae3bc7921cc259a08a7bf92e73ee6/tests/rustdoc-ui/error-in-impl-trait
[a list of supported browsers]: https://rust-lang.github.io/rfcs/1985-tiered-browser-support.html#supported-browsers

## Multiple runs, same output directory

Rustdoc can be run multiple times for varying inputs, with its output set to the same directory.
That's how cargo produces documentation for dependencies of the current crate.
It can also be done manually if a user wants a big
documentation bundle with all of the docs they care about.

HTML is generated independently for each crate, but there is some cross-crate
information that we update as we add crates to the output directory:

 - `crates<SUFFIX>.js` holds a list of all crates in the output directory.
 - `search-index<SUFFIX>.js` holds a list of all searchable items.
 - For each trait, there is a file under `implementors/.../trait.TraitName.js`
   containing a list of implementors of that trait.
   The implementors may be in
   different crates than the trait, and the JS file is updated as we discover new ones.

## Use cases

There are a few major use cases for rustdoc that you should keep in mind when working on it:

### Standard library docs

These are published at <https://doc.rust-lang.org/std> as part of the Rust release process.
Stable releases are also uploaded to specific versioned URLs like
<https://doc.rust-lang.org/1.57.0/std/>.
Beta and nightly docs are published to
<https://doc.rust-lang.org/beta/std/> and <https://doc.rust-lang.org/nightly/std/>.
The docs are uploaded with the [promote-release
tool](https://github.com/rust-lang/promote-release) and served from S3 with CloudFront.

The standard library docs contain five crates: alloc, core, proc_macro, std, and test.

### docs.rs

When crates are published to crates.io, docs.rs automatically builds
and publishes their documentation, for instance at <https://docs.rs/serde/latest/serde/>.
It always builds with the current nightly
rustdoc, so any changes you land in rustdoc are "insta-stable" in that they will
have an immediate public effect on docs.rs.
Old documentation is only sometimes rebuilt, so
you will see some variation in UI when browsing old releases in docs.rs.
Crate authors can request rebuilds, which will be run with the latest rustdoc.

Docs.rs performs some transformations on rustdoc's output in order to save
storage and display a navigation bar at the top.
In particular, certain static
files, like main.js and rustdoc.css, may be shared across multiple invocations
of the same version of rustdoc.
Others, like crates.js and sidebar-items.js, are different for different invocations.
Still others, like fonts, will never change.
These categories are distinguished using the `SharedResource` enum in
`src/librustdoc/html/render/write_shared.rs`

Documentation on docs.rs is always generated for a single crate at a time, so
the search and sidebar functionality don't include dependencies of the current crate.

### Locally generated docs

Crate authors can run `cargo doc --open` in crates they have checked out locally to see the docs.
This is useful to check that the docs they are writing are useful and display correctly.
It can also be useful for people to view documentation on crates they aren't authors of, but want to
use.
In both cases, people may use `--document-private-items` Cargo flag to
see private methods, fields, and so on, which are normally not displayed.

By default, `cargo doc` will generate documentation for a crate and all of its dependencies.
That can result in a very large documentation bundle, with a large (and slow) search corpus.
The Cargo flag `--no-deps` inhibits that behavior and generates docs for just the crate.

### Self-hosted project docs

Some projects host their own documentation.
This is easy to do by locally generating docs, and simply copying them to a web server.
Rustdoc's HTML output can be extensively customized by flags.
Users can add a theme, set the default theme, and inject arbitrary HTML.
See `rustdoc --help` for details.


---

# Adding a new target

These are a set of steps to add support for a new target.
There are numerous end states and paths to get there, so not all sections may be
relevant to your desired goal.

See also the associated documentation in the [target tier policy].

[target tier policy]: https://doc.rust-lang.org/rustc/target-tier-policy.html#adding-a-new-target

## Specifying a new LLVM

For very new targets, you may need to use a different fork of LLVM
than what is currently shipped with Rust.
In that case, navigate to the `src/llvm-project` git submodule (you might need to run `./x
check` at least once so the submodule is updated), check out the
appropriate commit for your fork, then commit that new submodule
reference in the main Rust repository.

An example would be:

```
cd src/llvm-project
git remote add my-target-llvm some-llvm-repository
git checkout my-target-llvm/my-branch
cd ..
git add llvm-project
git commit -m 'Use my custom LLVM'
```

### Using pre-built LLVM

If you have a local LLVM checkout that is already built, you may be
able to configure Rust to treat your build as the system LLVM to avoid redundant builds.

You can tell Rust to use a pre-built version of LLVM using the `target` section of `bootstrap.toml`:

```toml
[target.x86_64-unknown-linux-gnu]
llvm-config = "/path/to/llvm/llvm-7.0.1/bin/llvm-config"
```

If you are attempting to use a system LLVM, we have observed the following paths
before, though they may be different from your system:

- `/usr/bin/llvm-config-8`
- `/usr/lib/llvm-8/bin/llvm-config`

Note that you need to have the LLVM `FileCheck` tool installed, which is used for codegen tests.
This tool is normally built with LLVM, but if you use your
own preinstalled LLVM, you will need to provide `FileCheck` in some other way.
On Debian-based systems, you can install the `llvm-N-tools` package (where `N`
is the LLVM version number, e.g. `llvm-8-tools`). Alternately, you can specify
the path to `FileCheck` with the `llvm-filecheck` config item in `bootstrap.toml`
or you can disable codegen test with the `rust.codegen-tests` item in `bootstrap.toml`.

## Creating a target specification

You should start with a target JSON file.
You can see the specification for an existing target using `--print target-spec-json`:

```
rustc -Z unstable-options --target=wasm32-unknown-unknown --print target-spec-json
```

Save that JSON to a file and modify it as appropriate for your target.

### Adding a target specification

Once you have filled out a JSON specification and been able to compile
somewhat successfully, you can copy the specification into the compiler itself.

You will need to add a line to the big table inside of the
`supported_targets` macro in the `rustc_target::spec` module.
You will then add a corresponding file for your new target containing a `target` function.

Look for existing targets to use as examples.

To use this target in bootstrap, we need to explicitly add the target triple to
the `STAGE0_MISSING_TARGETS` list in `src/bootstrap/src/core/sanity.rs`.
This is necessary because the default bootstrap compiler (typically a beta compiler)
does not recognize the new target we just added.
Therefore, it should be added to
`STAGE0_MISSING_TARGETS` so that the bootstrap is aware that this target is not
yet supported by the stage0 compiler.

```diff
const STAGE0_MISSING_TARGETS: &[&str] = &[
+   "NEW_TARGET_TRIPLE"
];
```

## Patching crates

You may need to make changes to crates that the compiler depends on,
such as [`libc`][] or [`cc`][].
If so, you can use Cargo's [`[patch]`][patch] ability.
For example, if you want to use an unreleased version of `libc`, you can add it to the top-level
`Cargo.toml` file:

```diff
diff --git a/Cargo.toml b/Cargo.toml
index 1e83f05e0ca..4d0172071c1 100644
--- a/Cargo.toml
+++ b/Cargo.toml
@@ -113,6 +113,8 @@ cargo-util = { path = "src/tools/cargo/crates/cargo-util" }
 [patch.crates-io]
+libc = { git = "https://github.com/rust-lang/libc", rev = "0bf7ce340699dcbacabdf5f16a242d2219a49ee0" }

 # See comments in `src/tools/rustc-workspace-hack/README.md` for what's going on
 # here
 rustc-workspace-hack = { path = 'src/tools/rustc-workspace-hack' }
```

After this, run `cargo update -p libc` to update the lockfiles.

Beware that if you patch to a local `path` dependency, this will enable
warnings for that dependency.
Some dependencies are not warning-free, and due
to the `rust.deny-warnings` setting in `bootstrap.toml`, the build may suddenly start to fail.
To work around warnings, you may want to:
- Modify the dependency to remove the warnings
- Or for local development purposes, suppress the warnings by setting `rust.deny-warnings = false` in bootstrap.toml.

[`libc`]: https://crates.io/crates/libc
[`cc`]: https://crates.io/crates/cc
[patch]: https://doc.rust-lang.org/stable/cargo/reference/overriding-dependencies.html#the-patch-section

## Cross-compiling

Once you have a target specification in JSON and in the code, you can cross-compile `rustc`:

```
DESTDIR=/path/to/install/in \
./x install -i --stage 1 --host aarch64-apple-darwin.json --target aarch64-apple-darwin \
compiler/rustc library/std
```

If your target specification is already available in the bootstrap
compiler, you can use it instead of the JSON file for both arguments.

## Promoting a target from tier 2 (target) to tier 2 (host)

There are two levels of tier 2 targets:
- Targets that are only cross-compiled (`rustup target add`)
- Targets that [have a native toolchain][tier2-native] (`rustup toolchain install`)

[tier2-native]: https://doc.rust-lang.org/nightly/rustc/target-tier-policy.html#tier-2-with-host-tools

For an example of promoting a target from cross-compiled to native,
see [#75914](https://github.com/rust-lang/rust/pull/75914).


---

# Optimized build of the compiler

There are multiple additional build configuration options and techniques that can be used to compile a
build of `rustc` that is as optimized as possible (for example when building `rustc` for a Linux
distribution).
The status of these configuration options for various Rust targets is tracked [here].
This page describes how you can use these approaches when building `rustc` yourself.

[here]: https://github.com/rust-lang/rust/issues/103595

## Link-time optimization

Link-time optimization is a powerful compiler technique that can increase program performance.
To enable (Thin-)LTO when building `rustc`, set the `rust.lto` config option to `"thin"`
in `bootstrap.toml`:

```toml
rust.lto = "thin"
```

> Note that LTO for `rustc` is currently supported and tested only for
> the `x86_64-unknown-linux-gnu` target. Other targets *may* work, but no guarantees are provided.
> Notably, LTO-optimized `rustc` currently produces [miscompilations] on Windows.

[miscompilations]: https://github.com/rust-lang/rust/issues/109114

Enabling LTO on Linux has [produced] speed-ups by up to 10%.

[produced]: https://github.com/rust-lang/rust/pull/101403#issuecomment-1288190019

## Memory allocator

Using a different memory allocator for `rustc` can provide significant performance benefits.
If you want to enable the `jemalloc` allocator, you can set the `rust.jemalloc` option to `true`
in `bootstrap.toml`:

```toml
rust.jemalloc = true
```

> Note that this option is currently only supported for Linux and macOS targets.

## Codegen units

Reducing the amount of codegen units per `rustc` crate can produce a faster build of the compiler.
You can modify the number of codegen units for `rustc` and `libstd` in `bootstrap.toml` with the
following options:

```toml
rust.codegen-units = 1
rust.codegen-units-std = 1
```

## Instruction set

By default, `rustc` is compiled for a generic (and conservative) instruction set architecture
(depending on the selected target), to make it support as many CPUs as possible.
If you want to compile `rustc` for a specific instruction set architecture,
you can set the `target_cpu` compiler option in `RUSTFLAGS`:

```bash
RUSTFLAGS="-C target_cpu=x86-64-v3" ./x build ...
```

If you also want to compile LLVM for a specific instruction set, you can set `llvm` flags
in `bootstrap.toml`:

```toml
llvm.cxxflags = "-march=x86-64-v3"
llvm.cflags = "-march=x86-64-v3"
```

## Profile-guided optimization

Applying profile-guided optimizations (or more generally, feedback-directed optimizations) can
produce a large increase to `rustc` performance, by up to 15% ([1], [2]).
However, these techniques
are not simply enabled by a configuration option, but rather they require a complex build workflow
that compiles `rustc` multiple times and profiles it on selected benchmarks.

There is a tool called `opt-dist` that is used to optimize `rustc` with [PGO] (profile-guided
optimizations) and [BOLT] (a post-link binary optimizer) for builds distributed to end users.
You can examine the tool, which is located in `src/tools/opt-dist`, and build a custom PGO build
workflow based on it, or try to use it directly.
Note that the tool is currently quite hardcoded to
the way we use it in Rust's continuous integration workflows, and it might require some custom
changes to make it work in a different environment.

[1]: https://blog.rust-lang.org/inside-rust/2020/11/11/exploring-pgo-for-the-rust-compiler.html#final-numbers-and-a-benchmarking-plot-twist
[2]: https://github.com/rust-lang/rust/pull/96978

[PGO]: https://doc.rust-lang.org/rustc/profile-guided-optimization.html

[BOLT]: https://github.com/llvm/llvm-project/blob/main/bolt/README.md

To use the tool, you will need to provide some external dependencies:

- A Python3 interpreter (for executing `x.py`).
- Compiled LLVM toolchain, with the `llvm-profdata` binary.
  Optionally, if you want to use BOLT,
  the `llvm-bolt` and `merge-fdata` binaries have to be available in the toolchain.

These dependencies are provided to `opt-dist` by an implementation of the [`Environment`] struct.
It specifies directories where will the PGO/BOLT pipeline take place, and also external dependencies
like Python or LLVM.

Here is an example of how can `opt-dist` be used locally (outside of CI):

1. Enable metrics in your `bootstrap.toml` file, because `opt-dist` expects it to be enabled:
   ```toml
   build.metrics = true
   ```
2. Build the tool with the following command:
    ```bash
    ./x build tools/opt-dist
    ```
3. Run the tool with the `local` mode and provide necessary parameters:
    ```bash
    ./build/host/stage1-tools-bin/opt-dist local \
      --target-triple <target> \ # select target, e.g. "x86_64-unknown-linux-gnu"
      --checkout-dir <path>    \ # path to rust checkout, e.g. "."
      --llvm-dir <path>        \ # path to built LLVM toolchain, e.g. "/foo/bar/llvm/install"
      -- python3 x.py dist       # pass the actual build command
    ```
    You can run `--help` to see further parameters that you can modify.

[`Environment`]: https://github.com/rust-lang/rust/blob/ee451f8faccf3050c76cdcd82543c917b40c7962/src/tools/opt-dist/src/environment.rs#L5

> Note: if you want to run the actual CI pipeline, instead of running `opt-dist` locally,
> you can execute `cargo run --manifest-path src/ci/citool/Cargo.toml run-local dist-x86_64-linux`.


---

# crates.io dependencies

The Rust compiler supports building with some dependencies from `crates.io`.

Rust Forge has [official policy for vetting new dependencies].

## Permitted dependencies

The `tidy` tool has [a list of crates that are allowed].
To add a dependency that is not already in the compiler, you will need to add it to the list.

[a list of crates that are allowed]: https://github.com/rust-lang/rust/blob/9d1b2106e23b1abd32fce1f17267604a5102f57a/src/tools/tidy/src/deps.rs#L73
[official policy for vetting new dependencies]: https://forge.rust-lang.org/compiler/third-party-out-of-tree#third-party-crates
