# Features

Cargo "features" provide a mechanism to express [conditional compilation] and
[optional dependencies](#optional-dependencies). A package defines a set of
named features in the `[features]` table of `Cargo.toml`, and each feature can
either be enabled or disabled. Features for the package being built can be
enabled on the command-line with flags such as `--features`. Features for
dependencies can be enabled in the dependency declaration in `Cargo.toml`.

> **Note**: New crates or versions published on crates.io are now limited to
> a maximum of 300 features. Exceptions are granted on a case-by-case basis.
> See this [blog post] for details. Participation in solution discussions is
> encouraged via the crates.io Zulip stream.

[blog post]: https://blog.rust-lang.org/2023/10/26/broken-badges-and-23k-keywords.html

See also the [Features Examples] chapter for some examples of how features can
be used.

[conditional compilation]: ../../reference/conditional-compilation.md
[Features Examples]: features-examples.md

## The `[features]` section

Features are defined in the `[features]` table in `Cargo.toml`. Each feature
specifies an array of other features or optional dependencies that it enables.
The following examples illustrate how features could be used for a 2D image
processing library where support for different image formats can be optionally
included:

```toml
[features]
# Defines a feature named `webp` that does not enable any other features.
webp = []
```

With this feature defined, [`cfg` expressions] can be used to conditionally
include code to support the requested feature at compile time. For example,
inside `lib.rs` of the package could include this:

```rust
// This conditionally includes a module which implements WEBP support.
#[cfg(feature = "webp")]
pub mod webp;
```

Cargo sets features in the package using the `rustc` [`--cfg` flag], and code
can test for their presence with the [`cfg` attribute] or the [`cfg` macro].

Features can list other features to enable. For example, the ICO image format
can contain BMP and PNG images, so when it is enabled, it should make sure
those other features are enabled, too:

```toml
[features]
bmp = []
png = []
ico = ["bmp", "png"]
webp = []
```

Feature names may include characters from the [Unicode XID standard] (which
includes most letters), and additionally allows starting with `_` or digits
`0` through `9`, and after the first character may also contain `-`, `+`, or
`.`.

> **Note**: [crates.io] imposes additional constraints on feature name syntax
> that they must only be [ASCII alphanumeric] characters or `_`, `-`, or `+`.

[crates.io]: https://crates.io/
[Unicode XID standard]: https://unicode.org/reports/tr31/
[ASCII alphanumeric]: ../../std/primitive.char.html#method.is_ascii_alphanumeric
[`--cfg` flag]: ../../rustc/command-line-arguments.md#option-cfg
[`cfg` expressions]: ../../reference/conditional-compilation.md
[`cfg` attribute]: ../../reference/conditional-compilation.md#the-cfg-attribute
[`cfg` macro]: ../../std/macro.cfg.html

## The `default` feature

By default, all features are disabled unless explicitly enabled. This can be
changed by specifying the `default` feature:

```toml
[features]
default = ["ico", "webp"]
bmp = []
png = []
ico = ["bmp", "png"]
webp = []
```

When the package is built, the `default` feature is enabled which in turn
enables the listed features. This behavior can be changed by:

* The `--no-default-features` [command-line
  flag](#command-line-feature-options) disables the default features of the
  package.
* The `default-features = false` option can be specified in a [dependency
  declaration](#dependency-features).

> **Note**: Be careful about choosing the default feature set. The default
> features are a convenience that make it easier to use a package without
> forcing the user to carefully select which features to enable for common
> use, but there are some drawbacks. Dependencies automatically enable default
> features unless `default-features = false` is specified. This can make it
> difficult to ensure that the default features are not enabled, especially
> for a dependency that appears multiple times in the dependency graph. Every
> package must ensure that `default-features = false` is specified to avoid
> enabling them.
>
> Another issue is that it can be a [SemVer incompatible
> change](#semver-compatibility) to remove a feature from the default set, so
> you should be confident that you will keep those features.

## Optional dependencies

Dependencies can be marked "optional", which means they will not be compiled
by default. For example, let's say that our 2D image processing library uses
an external package to handle GIF images. This can be expressed like this:

```toml
[dependencies]
gif = { version = "0.11.1", optional = true }
```

By default, this optional dependency implicitly defines a feature that looks
like this:

```toml
[features]
gif = ["dep:gif"]
```

This means that this dependency will only be included if the `gif`
feature is enabled.
The same `cfg(feature = "gif")` syntax can be used in the code, and the
dependency can be enabled just like any feature such as `--features gif` (see
[Command-line feature options](#command-line-feature-options) below).

In some cases, you may not want to expose a feature that has the same name
as the optional dependency.
For example, perhaps the optional dependency is an internal detail, or you
want to group multiple optional dependencies together, or you just want to use
a better name.
If you specify the optional dependency with the `dep:` prefix anywhere
in the `[features]` table, that disables the implicit feature.

> **Note**: The `dep:` syntax is only available starting with Rust 1.60.
> Previous versions can only use the implicit feature name.

For example, let's say in order to support the AVIF image format, our library
needs two other dependencies to be enabled:

```toml
[dependencies]
ravif = { version = "0.6.3", optional = true }
rgb = { version = "0.8.25", optional = true }

[features]
avif = ["dep:ravif", "dep:rgb"]
```

In this example, the `avif` feature will enable the two listed dependencies.
This also avoids creating the implicit `ravif` and `rgb` features, since we
don't want users to enable those individually as they are internal details to
our crate.

> **Note**: Another way to optionally include a dependency is to use
> [platform-specific dependencies]. Instead of using features, these are
> conditional based on the target platform.

[platform-specific dependencies]: specifying-dependencies.md#platform-specific-dependencies

## Dependency features

Features of dependencies can be enabled within the dependency declaration. The
`features` key indicates which features to enable:

```toml
[dependencies]
# Enables the `derive` feature of serde.
serde = { version = "1.0.118", features = ["derive"] }
```

The [`default` features](#the-default-feature) can be disabled using
`default-features = false`:

```toml
[dependencies]
flate2 = { version = "1.0.3", default-features = false, features = ["zlib-rs"] }
```

> **Note**: This may not ensure the default features are disabled. If another
> dependency includes `flate2` without specifying `default-features = false`,
> then the default features will be enabled. See [feature
> unification](#feature-unification) below for more details.

Features of dependencies can also be enabled in the `[features]` table. The
syntax is `"package-name/feature-name"`. For example:

```toml
[dependencies]
jpeg-decoder = { version = "0.1.20", default-features = false }

[features]
# Enables parallel processing support by enabling the "rayon" feature of jpeg-decoder.
parallel = ["jpeg-decoder/rayon"]
```

The `"package-name/feature-name"` syntax will also enable `package-name`
if it is an optional dependency. Often this is not what you want.
You can add a `?` as in `"package-name?/feature-name"` which will only enable
the given feature if something else enables the optional dependency.

> **Note**: The `?` syntax is only available starting with Rust 1.60.

For example, let's say we have added some serialization support to our
library, and it requires enabling a corresponding feature in some optional
dependencies.
That can be done like this:

```toml
[dependencies]
serde = { version = "1.0.133", optional = true }
rgb = { version = "0.8.25", optional = true }

[features]
serde = ["dep:serde", "rgb?/serde"]
```

In this example, enabling the `serde` feature will enable the serde
dependency.
It will also enable the `serde` feature for the `rgb` dependency, but only if
something else has enabled the `rgb` dependency.

## Command-line feature options

The following command-line flags can be used to control which features are
enabled:

* `--features` _FEATURES_: Enables the listed features. Multiple features may
  be separated with commas or spaces. If using spaces, be sure to use quotes
  around all the features if running Cargo from a shell (such as `--features
  "foo bar"`). If building multiple packages in a [workspace], the
  `package-name/feature-name` syntax can be used to specify features for
  specific workspace members.
* `--all-features`: Activates all features of all packages selected on the command line.
* `--no-default-features`: Does not activate the [`default`
  feature](#the-default-feature) of the selected packages.
  
**NOTE**: check the individual subcommand documentation for details. Not all flags are available for all subcommands.

[workspace]: workspaces.md

## Feature unification

Features are unique to the package that defines them. Enabling a feature on a
package does not enable a feature of the same name on other packages.

When a dependency is used by multiple packages, Cargo will use the union of
all features enabled on that dependency when building it. This helps ensure
that only a single copy of the dependency is used. See the [features section]
of the resolver documentation for more details.

For example, let's look at the [`winapi`] package which uses a [large
number][winapi-features] of features. If your package depends on a package
`foo` which enables the "fileapi" and "handleapi" features of `winapi`, and
another dependency `bar` which enables the "std" and "winnt" features of
`winapi`, then `winapi` will be built with all four of those features enabled.

![winapi features example](../images/winapi-features.svg)

[`winapi`]: https://crates.io/crates/winapi
[winapi-features]: https://github.com/retep998/winapi-rs/blob/0.3.9/Cargo.toml#L25-L431

A consequence of this is that features should be *additive*. That is, enabling
a feature should not disable functionality, and it should usually be safe to
enable any combination of features. A feature should not introduce a
[SemVer-incompatible change](#semver-compatibility).

For example, if you want to optionally support [`no_std`] environments, **do
not** use a `no_std` feature. Instead, use a `std` feature that *enables*
`std`. For example:

```rust
#![no_std]

#[cfg(feature = "std")]
extern crate std;

#[cfg(feature = "std")]
pub fn function_that_requires_std() {
    // ...
}
```

[`no_std`]: ../../reference/names/preludes.html#the-no_std-attribute
[features section]: resolver.md#features

### Mutually exclusive features

There are rare cases where features may be mutually incompatible with one
another. This should be avoided if at all possible, because it requires
coordinating all uses of the package in the dependency graph to cooperate to
avoid enabling them together. If it is not possible, consider adding a compile
error to detect this scenario. For example:

```rust,ignore
#[cfg(all(feature = "foo", feature = "bar"))]
compile_error!("feature \"foo\" and feature \"bar\" cannot be enabled at the same time");
```

Instead of using mutually exclusive features, consider some other options:

* Split the functionality into separate packages.
* When there is a conflict, [choose one feature over
  another][feature-precedence]. The [`cfg-if`] package can help with writing
  more complex `cfg` expressions.
* Architect the code to allow the features to be enabled concurrently, and use
  runtime options to control which is used. For example, use a config file,
  command-line argument, or environment variable to choose which behavior to
  enable.

[`cfg-if`]: https://crates.io/crates/cfg-if
[feature-precedence]: features-examples.md#feature-precedence

### Inspecting resolved features

In complex dependency graphs, it can sometimes be difficult to understand how
different features get enabled on various packages. The [`cargo tree`] command
offers several options to help inspect and visualize which features are
enabled. Some options to try:

* `cargo tree -e features`: This will show features in the dependency graph.
  Each feature will appear showing which package enabled it.
* `cargo tree -f "{p} {f}"`: This is a more compact view that shows a
  comma-separated list of features enabled on each package.
* `cargo tree -e features -i foo`: This will invert the tree, showing how
  features flow into the given package "foo". This can be useful because
  viewing the entire graph can be quite large and overwhelming. Use this when
  you are trying to figure out which features are enabled on a specific
  package and why. See the example at the bottom of the [`cargo tree`] page on
  how to read this.

[`cargo tree`]: ../commands/cargo-tree.md

## Feature resolver version 2

A different feature resolver can be specified with the `resolver` field in
`Cargo.toml`, like this:

```toml
[package]
name = "my-package"
version = "1.0.0"
resolver = "2"
```

See the [resolver versions] section for more detail on specifying resolver
versions.

The version `"2"` resolver avoids unifying features in a few situations where
that unification can be unwanted. The exact situations are described in the
[resolver chapter][resolver-v2], but in short, it avoids unifying in these
situations:

* Features enabled on [platform-specific dependencies] for [target architectures][target] not
  currently being built are ignored.
* [Build-dependencies] and proc-macros do not share features with normal
  dependencies.
* [Dev-dependencies] do not activate features unless building a [Cargo target][target] that
  needs them (like tests or examples).

Avoiding the unification is necessary for some situations. For example, if a
build-dependency enables a `std` feature, and the same dependency is used as a
normal dependency for a `no_std` environment, enabling `std` would break the
build.

However, one drawback is that this can increase build times because the
dependency is built multiple times (each with different features). When using
the version `"2"` resolver, it is recommended to check for dependencies that
are built multiple times to reduce overall build time. If it is not *required*
to build those duplicated packages with separate features, consider adding
features to the `features` list in the [dependency
declaration](#dependency-features) so that the duplicates end up with the same
features (and thus Cargo will build it only once). You can detect these
duplicate dependencies with the [`cargo tree --duplicates`][`cargo tree`]
command. It will show which packages are built multiple times; look for any
entries listed with the same version. See [Inspecting resolved
features](#inspecting-resolved-features) for more on fetching information on
the resolved features. For build dependencies, this is not necessary if you
are cross-compiling with the `--target` flag because build dependencies are
always built separately from normal dependencies in that scenario.

[target]: ../appendix/glossary.md#target

### Resolver version 2 command-line flags

The `resolver = "2"` setting also changes the behavior of the `--features` and
`--no-default-features` [command-line options](#command-line-feature-options).

With version `"1"`, you can only enable features for the package in the
current working directory. For example, in a workspace with packages `foo` and
`bar`, and you are in the directory for package `foo`, and ran the command
`cargo build -p bar --features bar-feat`, this would fail because the
`--features` flag only allowed enabling features on `foo`.

With `resolver = "2"`, the features flags allow enabling features for any of
the packages selected on the command-line with `-p` and `--workspace` flags.
For example:

```sh
# This command is allowed with resolver = "2", regardless of which directory
# you are in.
cargo build -p foo -p bar --features foo-feat,bar-feat

# This explicit equivalent works with any resolver version:
cargo build -p foo -p bar --features foo/foo-feat,bar/bar-feat
```

Additionally, with `resolver = "1"`, the `--no-default-features` flag only
disables the default feature for the package in the current directory. With
version "2", it will disable the default features for all workspace members.

[resolver versions]: resolver.md#resolver-versions
[build-dependencies]: specifying-dependencies.md#build-dependencies
[dev-dependencies]: specifying-dependencies.md#development-dependencies
[resolver-v2]: resolver.md#feature-resolver-version-2

## Build scripts

[Build scripts] can detect which features are enabled on the package by
inspecting the `CARGO_FEATURE_<name>` environment variable, where `<name>` is
the feature name converted to uppercase and `-` converted to `_`.

[build scripts]: build-scripts.md

## Required features

The [`required-features` field] can be used to disable specific [Cargo
targets] if a feature is not enabled. See the linked documentation for more
details.

[`required-features` field]: cargo-targets.md#the-required-features-field
[Cargo targets]: cargo-targets.md

## SemVer compatibility

Enabling a feature should not introduce a SemVer-incompatible change. For
example, the feature shouldn't change an existing API in a way that could
break existing uses. More details about what changes are compatible can be
found in the [SemVer Compatibility chapter](semver.md).

Care should be taken when adding and removing feature definitions and optional
dependencies, as these can sometimes be backwards-incompatible changes. More
details can be found in the [Cargo section](semver.md#cargo) of the SemVer
Compatibility chapter. In short, follow these rules:

* The following is usually safe to do in a minor release:
  * Add a [new feature][cargo-feature-add] or [optional dependency][cargo-dep-add].
  * [Change the features used on a dependency][cargo-change-dep-feature].
* The following should usually **not** be done in a minor release:
  * [Remove a feature][cargo-feature-remove] or [optional dependency][cargo-remove-opt-dep].
  * [Moving existing public code behind a feature][item-remove].
  * [Remove a feature from a feature list][cargo-feature-remove-another].

See the links for caveats and examples.

[cargo-change-dep-feature]: semver.md#cargo-change-dep-feature
[cargo-dep-add]: semver.md#cargo-dep-add
[cargo-feature-add]: semver.md#cargo-feature-add
[item-remove]: semver.md#item-remove
[cargo-feature-remove]: semver.md#cargo-feature-remove
[cargo-remove-opt-dep]: semver.md#cargo-remove-opt-dep
[cargo-feature-remove-another]: semver.md#cargo-feature-remove-another

## Feature documentation and discovery

You are encouraged to document which features are available in your package.
This can be done by adding [doc comments] at the top of `lib.rs`. As an
example, see the [regex crate source], which when rendered can be viewed on
[docs.rs][regex-docs-rs]. If you have other documentation, such as a user
guide, consider adding the documentation there (for example, see [serde.rs]).
If you have a binary project, consider documenting the features in the README
or other documentation for the project (for example, see [sccache]).

Clearly documenting the features can set expectations about features that are
considered "unstable" or otherwise shouldn't be used. For example, if there is
an optional dependency, but you don't want users to explicitly list that
optional dependency as a feature, exclude it from the documented list.

Documentation published on [docs.rs] can use metadata in `Cargo.toml` to
control which features are enabled when the documentation is built. See
[docs.rs metadata documentation] for more details.

> **Note**: Rustdoc has experimental support for annotating the documentation
> to indicate which features are required to use certain APIs. See the
> `doc_cfg` documentation for more details. An example is the [`syn`
> documentation], where you can see colored boxes which note which features
> are required to use it.

[docs.rs metadata documentation]: https://docs.rs/about/metadata
[docs.rs]: https://docs.rs/
[serde.rs]: https://serde.rs/feature-flags.html
[doc comments]: ../../rustdoc/how-to-write-documentation.html
[regex crate source]: https://github.com/rust-lang/regex/blob/1.4.2/src/lib.rs#L488-L583
[regex-docs-rs]: https://docs.rs/regex/1.4.2/regex/#crate-features
[sccache]: https://github.com/mozilla/sccache/blob/0.2.13/README.md#build-requirements
[`syn` documentation]: https://docs.rs/syn/1.0.54/syn/#modules

### Discovering features

When features are documented in the library API, this can make it easier for
your users to discover which features are available and what they do. If the
feature documentation for a package isn't readily available, you can look at
the `Cargo.toml` file, but sometimes it can be hard to track it down. The
crate page on [crates.io] has a link to the source repository if available.
Tools like [`cargo vendor`] or [cargo-clone-crate] can be used to download the
source and inspect it.

[`cargo vendor`]: ../commands/cargo-vendor.md
[cargo-clone-crate]: https://crates.io/crates/cargo-clone-crate

## Feature combinations

Because features are a form of conditional compilation, they require an exponential number of configurations and test cases to be 100% covered. By default, tests, docs, and other tooling such as [Clippy](https://github.com/rust-lang/rust-clippy) will only run with the default set of features.

We encourage you to consider your strategy and tooling in regards to different feature combinations --- Every project will have different requirements in conjunction with time, resources, and the cost-benefit of covering specific scenarios. Common configurations may be with / without default features, specific combinations of features, or all combinations of features.


---

# Features Examples

The following illustrates some real-world examples of features in action.

## Minimizing build times and file sizes

Some packages use features so that if the features are not enabled, it reduces
the size of the crate and reduces compile time. Some examples are:

* [`syn`] is a popular crate for parsing Rust code. Since it is so popular, it
  is helpful to reduce compile times since it affects so many projects. It has
  a [clearly documented list][syn-features] of features which can be used to
  minimize the amount of code it contains.
* [`regex`] has a [several features][regex-features] that are [well
  documented][regex-docs]. Cutting out Unicode support can reduce the
  resulting file size as it can remove some large tables.
* [`winapi`] has [a large number][winapi-features] of features that
  limit which Windows API bindings it supports.
* [`web-sys`] is another example similar to `winapi` that provides a [huge
  surface area][web-sys-features] of API bindings that are limited by using
  features.

[`winapi`]: https://crates.io/crates/winapi
[winapi-features]: https://github.com/retep998/winapi-rs/blob/0.3.9/Cargo.toml#L25-L431
[`regex`]: https://crates.io/crates/regex
[`syn`]: https://crates.io/crates/syn
[syn-features]: https://docs.rs/syn/1.0.54/syn/#optional-features
[regex-features]: https://github.com/rust-lang/regex/blob/1.4.2/Cargo.toml#L33-L101
[regex-docs]: https://docs.rs/regex/1.4.2/regex/#crate-features
[`web-sys`]: https://crates.io/crates/web-sys
[web-sys-features]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/crates/web-sys/Cargo.toml#L32-L1395

## Extending behavior

The [`serde_json`] package has a [`preserve_order` feature][serde_json-preserve_order]
which [changes the behavior][serde_json-code] of JSON maps to preserve the
order that keys are inserted. Notice that it enables an optional dependency
[`indexmap`] to implement the new behavior.

When changing behavior like this, be careful to make sure the changes are
[SemVer compatible]. That is, enabling the feature should not break code that
usually builds with the feature off.

[`serde_json`]: https://crates.io/crates/serde_json
[serde_json-preserve_order]: https://github.com/serde-rs/json/blob/v1.0.60/Cargo.toml#L53-L56
[SemVer compatible]: features.md#semver-compatibility
[serde_json-code]: https://github.com/serde-rs/json/blob/v1.0.60/src/map.rs#L23-L26
[`indexmap`]: https://crates.io/crates/indexmap

## `no_std` support

Some packages want to support both [`no_std`] and `std` environments. This is
useful for supporting embedded and resource-constrained platforms, but still
allowing extended capabilities for platforms that support the full standard
library.

The [`wasm-bindgen`] package defines a [`std` feature][wasm-bindgen-std] that
is [enabled by default][wasm-bindgen-default]. At the top of the library, it
[unconditionally enables the `no_std` attribute][wasm-bindgen-no_std]. This
ensures that `std` and the [`std` prelude] are not automatically in scope.
Then, in various places in the code ([example1][wasm-bindgen-cfg1],
[example2][wasm-bindgen-cfg2]), it uses `#[cfg(feature = "std")]` attributes
to conditionally enable extra functionality that requires `std`.

[`no_std`]: ../../reference/names/preludes.html#the-no_std-attribute
[`wasm-bindgen`]: https://crates.io/crates/wasm-bindgen
[`std` prelude]: ../../std/prelude/index.html
[wasm-bindgen-std]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L25
[wasm-bindgen-default]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L23
[wasm-bindgen-no_std]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L8
[wasm-bindgen-cfg1]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L270-L273
[wasm-bindgen-cfg2]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L67-L75

## Re-exporting dependency features

It can be convenient to re-export the features from a dependency. This allows
the user depending on the crate to control those features without needing to
specify those dependencies directly. For example, [`regex`] [re-exports the
features][regex-re-export] from the [`regex_syntax`][regex_syntax-features]
package. Users of `regex` don't need to know about the `regex_syntax` package,
but they can still access the features it contains.

[regex-re-export]: https://github.com/rust-lang/regex/blob/1.4.2/Cargo.toml#L65-L89
[regex_syntax-features]: https://github.com/rust-lang/regex/blob/1.4.2/regex-syntax/Cargo.toml#L17-L32

## Vendoring of C libraries

Some packages provide bindings to common C libraries (sometimes referred to as
["sys" crates][sys]). Sometimes these packages give you the choice to use the
C library installed on the system, or to build it from source. For example,
the [`openssl`] package has a [`vendored` feature][openssl-vendored] which
enables the corresponding `vendored` feature of [`openssl-sys`]. The
`openssl-sys` build script has some [conditional logic][openssl-sys-cfg] which
causes it to build from a local copy of the OpenSSL source code instead of
using the version from the system.

The [`curl-sys`] package is another example where the [`static-curl`
feature][curl-sys-static] causes it to build libcurl from source. Notice that
it also has a [`force-system-lib-on-osx`][curl-sys-macos] feature which forces
it [to use the system libcurl][curl-sys-macos-code], overriding the
static-curl setting.

[`openssl`]: https://crates.io/crates/openssl
[`openssl-sys`]: https://crates.io/crates/openssl-sys
[sys]: build-scripts.md#-sys-packages
[openssl-vendored]: https://github.com/sfackler/rust-openssl/blob/openssl-v0.10.31/openssl/Cargo.toml#L19
[build script]: build-scripts.md
[openssl-sys-cfg]: https://github.com/sfackler/rust-openssl/blob/openssl-v0.10.31/openssl-sys/build/main.rs#L47-L54
[`curl-sys`]: https://crates.io/crates/curl-sys
[curl-sys-static]: https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/Cargo.toml#L49
[curl-sys-macos]: https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/Cargo.toml#L52
[curl-sys-macos-code]: https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/build.rs#L15-L20

## Feature precedence

Some packages may have mutually-exclusive features. One option to handle this
is to prefer one feature over another. The [`log`] package is an example. It
has [several features][log-features] for choosing the maximum logging level at
compile-time described [here][log-docs]. It uses [`cfg-if`] to [choose a
precedence][log-cfg-if]. If multiple features are enabled, the higher "max"
levels will be preferred over the lower levels.

[`log`]: https://crates.io/crates/log
[log-features]: https://github.com/rust-lang/log/blob/0.4.11/Cargo.toml#L29-L42
[log-docs]: https://docs.rs/log/0.4.11/log/#compile-time-filters
[log-cfg-if]: https://github.com/rust-lang/log/blob/0.4.11/src/lib.rs#L1422-L1448
[`cfg-if`]: https://crates.io/crates/cfg-if

## Proc-macro companion package

Some packages have a proc-macro that is intimately tied with it. However, not
all users will need to use the proc-macro. By making the proc-macro an
optional-dependency, this allows you to conveniently choose whether or not it
is included. This is helpful, because sometimes the proc-macro version must
stay in sync with the parent package, and you don't want to force the users to
have to specify both dependencies and keep them in sync.

An example is [`serde`] which has a [`derive`][serde-derive] feature which
enables the [`serde_derive`] proc-macro. The `serde_derive` crate is very
tightly tied to `serde`, so it uses an [equals version
requirement][serde-equals] to ensure they stay in sync.

[`serde`]: https://crates.io/crates/serde
[`serde_derive`]: https://crates.io/crates/serde_derive
[serde-derive]: https://github.com/serde-rs/serde/blob/v1.0.118/serde/Cargo.toml#L34-L35
[serde-equals]: https://github.com/serde-rs/serde/blob/v1.0.118/serde/Cargo.toml#L17

## Nightly-only features

Some packages want to experiment with APIs or language features that are only
available on the Rust [nightly channel]. However, they may not want to require
their users to also use the nightly channel. An example is [`wasm-bindgen`]
which has a [`nightly` feature][wasm-bindgen-nightly] which enables an
[extended API][wasm-bindgen-unsize] that uses the [`Unsize`] marker trait that
is only available on the nightly channel at the time of this writing.

Note that at the root of the crate it uses [`cfg_attr` to enable the nightly
feature][wasm-bindgen-cfg_attr]. Keep in mind that the [`feature` attribute]
is unrelated to Cargo features, and is used to opt-in to experimental language
features.

The [`simd_support` feature][rand-simd_support] of the [`rand`] package is another example,
which relies on a dependency that only builds on the nightly channel.

[`wasm-bindgen`]: https://crates.io/crates/wasm-bindgen
[nightly channel]: ../../book/appendix-07-nightly-rust.html
[wasm-bindgen-nightly]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L27
[wasm-bindgen-unsize]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/closure.rs#L257-L269
[`Unsize`]: ../../std/marker/trait.Unsize.html
[wasm-bindgen-cfg_attr]: https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L11
[`feature` attribute]: ../../unstable-book/index.html
[`rand`]: https://crates.io/crates/rand
[rand-simd_support]: https://github.com/rust-random/rand/blob/0.7.3/Cargo.toml#L40

## Experimental features

Some packages have new functionality that they may want to experiment with,
without having to commit to the stability of those APIs. The features are
usually documented that they are experimental, and thus may change or break in
the future, even during a minor release. An example is the [`async-std`]
package, which has an [`unstable` feature][async-std-unstable], which [gates
new APIs][async-std-gate] that people can opt-in to using, but may not be
completely ready to be relied upon.

[`async-std`]: https://crates.io/crates/async-std
[async-std-unstable]: https://github.com/async-rs/async-std/blob/v1.8.0/Cargo.toml#L38-L42
[async-std-gate]: https://github.com/async-rs/async-std/blob/v1.8.0/src/macros.rs#L46
