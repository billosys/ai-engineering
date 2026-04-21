# Command-line Arguments

Command-line flags are documented in the [rustc book][cli-docs]. All *stable*
flags should be documented there. Unstable flags should be documented in the
[unstable book].

See the [forge guide for new options] for details on the *procedure* for
adding a new command-line argument.

## Guidelines

- Flags should be orthogonal to each other. For example, if we'd have a
  json-emitting variant of multiple actions `foo` and `bar`, an additional
  `--json` flag is better than adding `--foo-json` and `--bar-json`.
- Avoid flags with the `no-` prefix. Instead, use the [`parse_bool`] function,
  such as `-C embed-bitcode=no`.
- Consider the behavior if the flag is passed multiple times. In some
  situations, the values should be accumulated (in order!). In other
  situations, subsequent flags should override previous flags (for example,
  the lint-level flags). And some flags (like `-o`) should generate an error
  if it is too ambiguous what multiple flags would mean.
- Always give options a long descriptive name, if only for more understandable
  compiler scripts.
- The `--verbose` flag is for adding verbose information to `rustc`
  output. For example, using it with the `--version`
  flag gives information about the hashes of the compiler code.
- Experimental flags and options must be guarded behind the `-Z
  unstable-options` flag.

[cli-docs]: https://doc.rust-lang.org/rustc/command-line-arguments.html
[forge guide for new options]: https://forge.rust-lang.org/compiler/proposals-and-stabilization.html#compiler-flags
[unstable book]: https://doc.rust-lang.org/nightly/unstable-book/
[`parse_bool`]: https://github.com/rust-lang/rust/blob/e5335592e78354e33d798d20c04bcd677c1df62d/src/librustc_session/options.rs#L307-L313


---

# `rustc_driver` and `rustc_interface`

## `rustc_driver`

The [`rustc_driver`] is essentially `rustc`'s `main` function.
It acts as the glue for running the various phases of the compiler in the correct order,
using the interface defined in the [`rustc_interface`] crate. Where possible, using [`rustc_driver`] rather than [`rustc_interface`] is recommended.

The main entry point of [`rustc_driver`] is [`rustc_driver::run_compiler`][rd_rc].
This builder accepts the same command-line args as rustc as well as an implementation of [`Callbacks`] and a couple of other optional options.
[`Callbacks`] is a `trait` that allows for custom compiler configuration,
as well as allowing custom code to run after different phases of the compilation.

## `rustc_interface`

The [`rustc_interface`] crate provides a low level API to external users for manually driving the compilation process,
allowing third parties to effectively use `rustc`'s internals as a library for analyzing a crate or for ad hoc emulating of the compiler for cases where [`rustc_driver`] is not flexible enough (i.e. `rustdoc` compiling code and serving output).

The main entry point of [`rustc_interface`] ([`rustc_interface::run_compiler`][i_rc]) takes a configuration variable for the compiler
and a `closure` taking a yet unresolved [`Compiler`].
[`run_compiler`][i_rc] creates a `Compiler` from the configuration and passes it to the `closure`.
Inside the `closure` you can use the `Compiler` to call various functions to compile a crate and get the results.
You can see a minimal example of how to use [`rustc_interface`] [here][example].

You can see an example of how to use the various functions using [`rustc_interface`] needs by looking at the `rustc_driver` implementation,
specifically [`rustc_driver_impl::run_compiler`][rdi_rc]
(not to be confused with [`rustc_interface::run_compiler`][i_rc]).

> **Warning:** By its very nature, the internal compiler APIs are always going
> to be unstable. That said, we do try not to break things unnecessarily.


[`Compiler`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/struct.Compiler.html
[`rustc_driver`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/
[`rustc_interface`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/index.html
[`Callbacks`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/trait.Callbacks.html
[example]: https://github.com/rust-lang/rustc-dev-guide/blob/main/examples/rustc-interface-example.rs
[i_rc]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/fn.run_compiler.html
[rd_rc]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/fn.run_compiler.html
[rdi_rc]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver_impl/fn.run_compiler.html


---

# External `rustc_driver`s

## `rustc_private`

### Overview

The `rustc_private` feature allows external crates to use compiler internals.

### Using `rustc_private` with Official Toolchains

When using the `rustc_private` feature with official Rust toolchains distributed via rustup, you need to install two additional components:

1. **`rustc-dev`**: Provides compiler libraries
2. **`llvm-tools`**: Provides LLVM libraries required for linking

#### Installation Steps

Install both components using rustup:

```text
rustup component add rustc-dev llvm-tools
```

#### Common Error

Without the `llvm-tools` component, you'll encounter linking errors like:

```text
error: linking with `cc` failed: exit status: 1
  |
  = note: rust-lld: error: unable to find library -lLLVM-{version}
```

### Using `rustc-private` with Custom Toolchains

For custom-built toolchains or environments not using rustup, additional configuration is typically required:

#### Requirements

- LLVM libraries must be available in your system's library search paths
- The LLVM version must match the one used to build your Rust toolchain

#### Troubleshooting Steps

1. Verify LLVM is installed and accessible
2. Ensure that library paths are set:
   ```sh
   export LD_LIBRARY_PATH=/path/to/llvm/lib:$LD_LIBRARY_PATH
   ```
3. Ensure your LLVM version is compatible with your Rust toolchain

### Configuring `rust-analyzer` for out-of-tree projects

When developing out-of-tree projects that use `rustc_private` crates, you can configure `rust-analyzer` to recognize these crates.

#### Configuration Steps

1. Configure `rust-analyzer.rustc.source` to `"discover"` in your editor settings.  
   For VS Code, add to `rust_analyzer_settings.json`:
   ```json
   {
       "rust-analyzer.rustc.source": "discover"
   }
   ```

2. Add the following to the `Cargo.toml` of every crate that uses `rustc_private`:
   ```toml
   [package.metadata.rust-analyzer]
   rustc_private = true
   ```

This configuration allows `rust-analyzer` to properly recognize and provide IDE support for `rustc_private` crates in out-of-tree projects. 

### Getting Specific Nightly Documentation for `rustc_private`

The nightly-rustc internal crates' documentation is only available for the latest nightly. If you depend on compiler internals from an older nightly, you may want to refer to the internal documentation from that particular nightly. The only way to do this is to generate the documentation locally. For example, to get documentation for `nightly-2025-11-08`:

Get the Git commit hash for that nightly:

```sh
rustup toolchain install nightly-2025-11-08
rustc +nightly-2025-11-08 --version --verbose
```

The output will include a `commit-hash` line identifying the exact source revision. Check out `rust-lang/rust` at that commit, then follow the steps in [compiler documentation](../building/compiler-documenting.md).


### Additional Resources

- [GitHub Issue #137421] explains that `rustc_private` linker failures often occur because `llvm-tools` is not installed

[GitHub Issue #137421]: https://github.com/rust-lang/rust/issues/137421


---

# Example: Type checking through `rustc_driver`

[`rustc_driver`] allows you to interact with Rust code at various stages of compilation.

## Getting the type of an expression

To get the type of an expression, use the [`after_analysis`] callback to get a [`TyCtxt`].

```rust
{{#include ../../examples/rustc-driver-interacting-with-the-ast.rs}}
```
[`after_analysis`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver/trait.Callbacks.html#method.after_analysis
[`rustc_driver`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_driver
[`TyCtxt`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html


---

# Example: Getting diagnostic through `rustc_interface`

The [`rustc_interface`] allows you to intercept diagnostics that would
otherwise be printed to stderr.

## Getting diagnostics

To get diagnostics from the compiler,
configure [`rustc_interface::Config`] to output diagnostic to a buffer,
and run [`TyCtxtEnsureOk::typeck`] for each item.

```rust
{{#include ../../examples/rustc-interface-getting-diagnostics.rs}}
```

[`rustc_interface`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/index.html
[`rustc_interface::Config`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/struct.Config.html
[`TyCtxtEnsureOk::typeck`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/query/struct.TyCtxtEnsureOk.html#method.typeck
