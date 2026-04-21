# The Manifest Format

The `Cargo.toml` file for each package is called its *manifest*. It is written
in the [TOML] format. It contains metadata that is needed to compile the package. Checkout
the `cargo locate-project` section for more detail on how cargo finds the manifest file.

Every manifest file consists of the following sections:

* [`cargo-features`](unstable.md) --- Unstable, nightly-only features.
* [`[package]`](#the-package-section) --- Defines a package.
  * [`name`](#the-name-field) --- The name of the package.
  * [`version`](#the-version-field) --- The version of the package.
  * [`authors`](#the-authors-field) --- The authors of the package.
  * [`edition`](#the-edition-field) --- The Rust edition.
  * [`rust-version`](rust-version.md) --- The minimal supported Rust version.
  * [`description`](#the-description-field) --- A description of the package.
  * [`documentation`](#the-documentation-field) --- URL of the package documentation.
  * [`readme`](#the-readme-field) --- Path to the package's README file.
  * [`homepage`](#the-homepage-field) --- URL of the package homepage.
  * [`repository`](#the-repository-field) --- URL of the package source repository.
  * [`license`](#the-license-and-license-file-fields) --- The package license.
  * [`license-file`](#the-license-and-license-file-fields) --- Path to the text of the license.
  * [`keywords`](#the-keywords-field) --- Keywords for the package.
  * [`categories`](#the-categories-field) --- Categories of the package.
  * [`workspace`](#the-workspace-field) --- Path to the workspace for the package.
  * [`build`](#the-build-field) --- Path to the package build script.
  * [`links`](#the-links-field) --- Name of the native library the package links with.
  * [`exclude`](#the-exclude-and-include-fields) --- Files to exclude when publishing.
  * [`include`](#the-exclude-and-include-fields) --- Files to include when publishing.
  * [`publish`](#the-publish-field) --- Can be used to prevent publishing the package.
  * [`metadata`](#the-metadata-table) --- Extra settings for external tools.
  * [`default-run`](#the-default-run-field) --- The default binary to run by [`cargo run`].
  * [`autolib`](cargo-targets.md#target-auto-discovery) --- Disables library auto discovery.
  * [`autobins`](cargo-targets.md#target-auto-discovery) --- Disables binary auto discovery.
  * [`autoexamples`](cargo-targets.md#target-auto-discovery) --- Disables example auto discovery.
  * [`autotests`](cargo-targets.md#target-auto-discovery) --- Disables test auto discovery.
  * [`autobenches`](cargo-targets.md#target-auto-discovery) --- Disables bench auto discovery.
  * [`resolver`](resolver.md#resolver-versions) --- Sets the dependency resolver to use.
* Target tables: (see [configuration](cargo-targets.md#configuring-a-target) for settings)
  * [`[lib]`](cargo-targets.md#library) --- Library target settings.
  * [`[[bin]]`](cargo-targets.md#binaries) --- Binary target settings.
  * [`[[example]]`](cargo-targets.md#examples) --- Example target settings.
  * [`[[test]]`](cargo-targets.md#tests) --- Test target settings.
  * [`[[bench]]`](cargo-targets.md#benchmarks) --- Benchmark target settings.
* Dependency tables:
  * [`[dependencies]`](specifying-dependencies.md) --- Package library dependencies.
  * [`[dev-dependencies]`](specifying-dependencies.md#development-dependencies) --- Dependencies for examples, tests, and benchmarks.
  * [`[build-dependencies]`](specifying-dependencies.md#build-dependencies) --- Dependencies for build scripts.
  * [`[target]`](specifying-dependencies.md#platform-specific-dependencies) --- Platform-specific dependencies.
* [`[badges]`](#the-badges-section) --- Badges to display on a registry.
* [`[features]`](features.md) --- Conditional compilation features.
* [`[lints]`](#the-lints-section) --- Configure linters for this package.
* [`[hints]`](#the-hints-section) --- Provide hints for compiling this package.
* [`[patch]`](overriding-dependencies.md#the-patch-section) --- Override dependencies.
* [`[replace]`](overriding-dependencies.md#the-replace-section) --- Override dependencies (deprecated).
* [`[profile]`](profiles.md) --- Compiler settings and optimizations.
* [`[workspace]`](workspaces.md) --- The workspace definition.

## The `[package]` section

The first section in a `Cargo.toml` is `[package]`.

```toml
[package]
name = "hello_world" # the name of the package
version = "0.1.0"    # the current version, obeying semver
```

The only field required by Cargo is [`name`](#the-name-field). If publishing to
a registry, the registry may require additional fields. See the notes below and
[the publishing chapter][publishing] for requirements for publishing to
[crates.io].

### The `name` field

The package name is an identifier used to refer to the package. It is used
when listed as a dependency in another package, and as the default name of
inferred lib and bin targets.

The name must use only [alphanumeric] characters or `-` or `_`, and cannot be empty.

Note that [`cargo new`] and [`cargo init`] impose some additional restrictions on
the package name, such as enforcing that it is a valid Rust identifier and not
a keyword. [crates.io] imposes even more restrictions, such as:

- Only ASCII characters are allowed.
- Do not use reserved names.
- Do not use special Windows names such as "nul".
- Use a maximum of 64 characters of length.

[alphanumeric]: ../../std/primitive.char.html#method.is_alphanumeric

### The `version` field

The `version` field is formatted according to the [SemVer] specification:

Versions must have three numeric parts,
the major version, the minor version, and the patch version.

A pre-release part can be added after a dash such as `1.0.0-alpha`.
The pre-release part may be separated with periods to distinguish separate
components. Numeric components will use numeric comparison while
everything else will be compared lexicographically.
For example, `1.0.0-alpha.11` is higher than `1.0.0-alpha.4`.

A metadata part can be added after a plus, such as `1.0.0+21AF26D3`.
This is for informational purposes only and is generally ignored by Cargo.

Cargo bakes in the concept of [Semantic Versioning](https://semver.org/),
so versions are considered [compatible](semver.md) if their left-most non-zero major/minor/patch component is the same.
See the [Resolver] chapter for more information on how Cargo uses versions to
resolve dependencies.

This field is optional and defaults to `0.0.0`.  The field is required for publishing packages.

> **MSRV:** Before 1.75, this field was required

[SemVer]: https://semver.org
[Resolver]: resolver.md
[SemVer compatibility]: semver.md

### The `authors` field

> **Warning**: This field is deprecated

The optional `authors` field lists in an array the people or organizations that are considered
the "authors" of the package. An optional email address may be included within angled brackets at
the end of each author entry.

```toml
[package]
# ...
authors = ["Graydon Hoare", "Fnu Lnu <no-reply@rust-lang.org>"]
```

This field is surfaced in package metadata and in the `CARGO_PKG_AUTHORS`
environment variable within `build.rs` for backwards compatibility.

### The `edition` field

The `edition` key is an optional key that affects which [Rust Edition] your package
is compiled with. Setting the `edition` key in `[package]` will affect all
targets/crates in the package, including test suites, benchmarks, binaries,
examples, etc.

```toml
[package]
# ...
edition = '2024'
```

Most manifests have the `edition` field filled in automatically by [`cargo new`]
with the latest stable edition. By default `cargo new` creates a manifest with
the 2024 edition currently.

If the `edition` field is not present in `Cargo.toml`, then the 2015 edition is
assumed for backwards compatibility. Note that all manifests
created with [`cargo new`] will not use this historical fallback because they
will have `edition` explicitly specified to a newer value.

### The `rust-version` field

The `rust-version` field tells cargo what version of the
Rust toolchain you support for your package.
See [the Rust version chapter](rust-version.md) for more detail.

### The `description` field

The description is a short blurb about the package. [crates.io] will display
this with your package. This should be plain text (not Markdown).

```toml
[package]
# ...
description = "A short description of my package"
```

> **Note**: [crates.io] requires the `description` to be set.

### The `documentation` field

The `documentation` field specifies a URL to a website hosting the crate's
documentation. If no URL is specified in the manifest file, [crates.io] will
automatically link your crate to the corresponding [docs.rs] page when the
documentation has been built and is available (see [docs.rs queue]).

```toml
[package]
# ...
documentation = "https://docs.rs/bitflags"
```

[docs.rs queue]: https://docs.rs/releases/queue

### The `readme` field

The `readme` field should be the path to a file in the package root (relative
to this `Cargo.toml`) that contains general information about the package.
This file will be transferred to the registry when you publish. [crates.io]
will interpret it as Markdown and render it on the crate's page.

```toml
[package]
# ...
readme = "README.md"
```

If no value is specified for this field, and a file named `README.md`,
`README.txt` or `README` exists in the package root, then the name of that
file will be used. You can suppress this behavior by setting this field to
`false`. If the field is set to `true`, a default value of `README.md` will
be assumed.

### The `homepage` field

The `homepage` field should be a URL to a site that is the home page for your
package.

```toml
[package]
# ...
homepage = "https://serde.rs"
```

A value should only be set for `homepage` if there is a dedicated website for
the crate other than the source repository or API documentation. Do not make
`homepage` redundant with either the `documentation` or `repository` values.

### The `repository` field

The `repository` field should be a URL to the source repository for your
package.

```toml
[package]
# ...
repository = "https://github.com/rust-lang/cargo"
```

### The `license` and `license-file` fields

The `license` field contains the name of the software license that the package
is released under. The `license-file` field contains the path to a file
containing the text of the license (relative to this `Cargo.toml`).

[crates.io] interprets the `license` field as an [SPDX 2.3 license
expression][spdx-2.3-license-expressions]. The name must be a known license
from the [SPDX license list 3.20][spdx-license-list-3.20]. See the [SPDX site]
for more information.

SPDX license expressions support AND and OR operators to combine multiple
licenses.[^slash]

```toml
[package]
# ...
license = "MIT OR Apache-2.0"
```

Using `OR` indicates the user may choose either license. Using `AND` indicates
the user must comply with both licenses simultaneously. The `WITH` operator
indicates a license with a special exception. Some examples:

* `MIT OR Apache-2.0`
* `LGPL-2.1-only AND MIT AND BSD-2-Clause`
* `GPL-2.0-or-later WITH Bison-exception-2.2`

If a package is using a nonstandard license, then the `license-file` field may
be specified in lieu of the `license` field.

```toml
[package]
# ...
license-file = "LICENSE.txt"
```

> **Note**: [crates.io] requires either `license` or `license-file` to be set.

[^slash]: Previously multiple licenses could be separated with a `/`, but that
usage is deprecated.

### The `keywords` field

The `keywords` field is an array of strings that describe this package. This
can help when searching for the package on a registry, and you may choose any
words that would help someone find this crate.

```toml
[package]
# ...
keywords = ["gamedev", "graphics"]
```

> **Note**: [crates.io] allows a maximum of 5 keywords. Each keyword must be
> ASCII text, have at most 20 characters, start with an alphanumeric character,
> and only contain letters, numbers, `_`, `-` or `+`.

### The `categories` field

The `categories` field is an array of strings of the categories this package
belongs to.

```toml
categories = ["command-line-utilities", "development-tools::cargo-plugins"]
```

> **Note**: [crates.io] has a maximum of 5 categories. Each category should
> match one of the strings available at <https://crates.io/category_slugs>, and
> must match exactly.

### The `workspace` field

The `workspace` field can be used to configure the workspace that this package
will be a member of. If not specified this will be inferred as the first
Cargo.toml with `[workspace]` upwards in the filesystem. Setting this is
useful if the member is not inside a subdirectory of the workspace root.

```toml
[package]
# ...
workspace = "path/to/workspace/root"
```

This field cannot be specified if the manifest already has a `[workspace]`
table defined. That is, a crate cannot both be a root crate in a workspace
(contain `[workspace]`) and also be a member crate of another workspace
(contain `package.workspace`).

For more information, see the [workspaces chapter](workspaces.md).

### The `build` field

The `build` field specifies a file in the package root which is a [build
script] for building native code. More information can be found in the [build
script guide][build script].

[build script]: build-scripts.md

```toml
[package]
# ...
build = "build.rs"
```

The default is `"build.rs"`, which loads the script from a file named
`build.rs` in the root of the package. Use `build = "custom_build_name.rs"` to
specify a path to a different file or `build = false` to disable automatic
detection of the build script.

### The `links` field

The `links` field specifies the name of a native library that is being linked
to. More information can be found in the [`links`][links] section of the build
script guide.

[links]: build-scripts.md#the-links-manifest-key

For example, a crate that links a native library called "git2" (e.g. `libgit2.a`
on Linux) may specify:

```toml
[package]
# ...
links = "git2"
```

### The `exclude` and `include` fields

The `exclude` and `include` fields can be used to explicitly specify which
files are included when packaging a project to be [published][publishing],
and certain kinds of change tracking (described below).
The patterns specified in the `exclude` field identify a set of files that are
not included, and the patterns in `include` specify files that are explicitly
included.

```toml
[package]
# ...
exclude = ["/ci", "images/", ".*"]
```

```toml
[package]
# ...
include = ["/src", "COPYRIGHT", "/examples", "!/examples/big_example"]
```

> **Note:** Run [`cargo package --list`][`cargo package`]
> to verify which files will be included in the package.

The default if neither field is specified is to include all files from the
root of the package, except for the exclusions listed below.

If `include` is not specified, then the following files will be excluded:

* If the package is not in a git repository, all "hidden" files starting with
  a dot will be skipped.
* If the package is in a git repository, any files that are ignored by the
  [gitignore] rules of the repository and global git configuration will be
  skipped.

If `include` is specified,
gitignore rules of the repository and global git configuration are not applied.

Regardless of whether `exclude` or `include` is specified, the following files
are always excluded:

* Any sub-packages will be skipped (any subdirectory that contains a
  `Cargo.toml` file).
* A directory named `target` in the root of the package will be skipped.

The following files are always included:

* The `Cargo.toml` file of the package itself is always included, it does not
  need to be listed in `include`.
* A minimized `Cargo.lock` is automatically included.
  See [`cargo package`] for more information.
* If a [`license-file`](#the-license-and-license-file-fields) is specified, it
  is always included.

The options are mutually exclusive; setting `include` will override an
`exclude`. If you need to have exclusions to a set of `include` files, use the
`!` operator described below.

The patterns should be [gitignore]-style patterns. Briefly:

- `foo` matches any file or directory with the name `foo` anywhere in the
  package. This is equivalent to the pattern `**/foo`.
- `/foo` matches any file or directory with the name `foo` only in the root of
  the package.
- `foo/` matches any *directory* with the name `foo` anywhere in the package.
- Common glob patterns like `*`, `?`, and `[]` are supported:
  - `*` matches zero or more characters except `/`.  For example, `*.html`
    matches any file or directory with the `.html` extension anywhere in the
    package.
  - `?` matches any character except `/`. For example, `foo?` matches `food`,
    but not `foo`.
  - `[]` allows for matching a range of characters. For example, `[ab]`
    matches either `a` or `b`. `[a-z]` matches letters a through z.
- `**/` prefix matches in any directory. For example, `**/foo/bar` matches the
  file or directory `bar` anywhere that is directly under directory `foo`.
- `/**` suffix matches everything inside. For example, `foo/**` matches all
  files inside directory `foo`, including all files in subdirectories below
  `foo`.
- `/**/` matches zero or more directories. For example, `a/**/b` matches
  `a/b`, `a/x/b`, `a/x/y/b`, and so on.
- `!` prefix negates a pattern. For example, a pattern of `src/*.rs` and
  `!foo.rs` would match all files with the `.rs` extension inside the `src`
  directory, except for any file named `foo.rs`.

The include/exclude list is also used for change tracking in some situations.
For targets built with `rustdoc`, it is used to determine the list of files to
track to determine if the target should be rebuilt. If the package has a
[build script] that does not emit any `rerun-if-*` directives, then the
include/exclude list is used for tracking if the build script should be re-run
if any of those files change.

[gitignore]: https://git-scm.com/docs/gitignore

### The `publish` field

The `publish` field can be used to control which registries names the package
may be published to:
```toml
[package]
# ...
publish = ["some-registry-name"]
```

To prevent a package from being published to a registry (like crates.io) by mistake,
for instance to keep a package private in a company,
you can omit the [`version`](#the-version-field) field.
If you'd like to be more explicit, you can disable publishing:
```toml
[package]
# ...
publish = false
```

If publish array contains a single registry, `cargo publish` command will use
it when `--registry` flag is not specified.

### The `metadata` table

Cargo by default will warn about unused keys in `Cargo.toml` to assist in
detecting typos and such. The `package.metadata` table, however, is completely
ignored by Cargo and will not be warned about. This section can be used for
tools which would like to store package configuration in `Cargo.toml`. For
example:

```toml
[package]
name = "..."
# ...

# Metadata used when generating an Android APK, for example.
[package.metadata.android]
package-name = "my-awesome-android-app"
assets = "path/to/static"
```

You'll need to look in the documentation for your tool to see how to use this field.
For Rust Projects that use `package.metadata` tables, see:
- [docs.rs](https://docs.rs/about/metadata)

There is a similar table at the workspace level at
[`workspace.metadata`][workspace-metadata]. While cargo does not specify a
format for the content of either of these tables, it is suggested that
external tools may wish to use them in a consistent fashion, such as referring
to the data in `workspace.metadata` if data is missing from `package.metadata`,
if that makes sense for the tool in question.

[workspace-metadata]: workspaces.md#the-metadata-table

### The `default-run` field

The `default-run` field in the `[package]` section of the manifest can be used
to specify a default binary picked by [`cargo run`]. For example, when there is
both `src/bin/a.rs` and `src/bin/b.rs`:

```toml
[package]
default-run = "a"
```

## The `[lints]` section

Override the default level of lints from different tools by assigning them to a new level in a
table, for example:
```toml
[lints.rust]
unsafe_code = "forbid"
```

This is short-hand for:
```toml
[lints.rust]
unsafe_code = { level = "forbid", priority = 0 }
```

`level` corresponds to the [lint levels](https://doc.rust-lang.org/rustc/lints/levels.html) in `rustc`:
- `forbid`
- `deny`
- `warn`
- `allow`

`priority` is a signed integer that controls which lints or lint groups override other lint groups:
- lower (particularly negative) numbers have lower priority, being overridden
  by higher numbers, and show up first on the command-line to tools like
  `rustc`

To know which table under `[lints]` a particular lint belongs under, it is the part before `::` in the lint
name.  If there isn't a `::`, then the tool is `rust`.  For example a warning
about `unsafe_code` would be `lints.rust.unsafe_code` but a lint about
`clippy::enum_glob_use` would be `lints.clippy.enum_glob_use`.

For example:
```toml
[lints.rust]
unsafe_code = "forbid"

[lints.clippy]
enum_glob_use = "deny"
```

Generally, these will only affect local development of the current package.
Cargo only applies these to the current package and not to dependencies.
As for dependents, Cargo suppresses lints from non-path dependencies with features like
[`--cap-lints`](../../rustc/lints/levels.html#capping-lints).

> **MSRV:** Respected as of 1.74

## The `[hints]` section

The `[hints]` section allows specifying hints for compiling this package. Cargo
will respect these hints by default when compiling this package, though the
top-level package being built can override these values through the `[profile]`
mechanism. Hints are, by design, always safe for Cargo to ignore; if Cargo
encounters a hint it doesn't understand, or a hint it understands but with a
value it doesn't understand, it will warn, but not error. As a result,
specifying hints in a crate does not impact the MSRV of the crate.

Individual hints may have an associated unstable feature gate that you need to
pass in order to apply the configuration they specify, but if you don't specify
that unstable feature gate, you will again get only a warning, not an error.

There are no stable hints at this time. See the [hint-mostly-unused
documentation](unstable.md#profile-hint-mostly-unused-option) for information
on an unstable hint.

> **MSRV:** Respected as of 1.90.

## The `[badges]` section

The `[badges]` section is for specifying status badges that can be displayed
on a registry website when the package is published.

> Note: [crates.io] previously displayed badges next to a crate on its
> website, but that functionality has been removed. Packages should place
> badges in its README file which will be displayed on [crates.io] (see [the
> `readme` field](#the-readme-field)).

```toml
[badges]
# The `maintenance` table indicates the status of the maintenance of
# the crate. This may be used by a registry, but is currently not
# used by crates.io. See https://github.com/rust-lang/crates.io/issues/2437
# and https://github.com/rust-lang/crates.io/issues/2438 for more details.
#
# The `status` field is required. Available options are:
# - `actively-developed`: New features are being added and bugs are being fixed.
# - `passively-maintained`: There are no plans for new features, but the maintainer intends to
#   respond to issues that get filed.
# - `as-is`: The crate is feature complete, the maintainer does not intend to continue working on
#   it or providing support, but it works for the purposes it was designed for.
# - `experimental`: The author wants to share it with the community but is not intending to meet
#   anyone's particular use case.
# - `looking-for-maintainer`: The current maintainer would like to transfer the crate to someone
#   else.
# - `deprecated`: The maintainer does not recommend using this crate (the description of the crate
#   can describe why, there could be a better solution available or there could be problems with
#   the crate that the author does not want to fix).
# - `none`: Displays no badge on crates.io, since the maintainer has not chosen to specify
#   their intentions, potential crate users will need to investigate on their own.
maintenance = { status = "..." }
```

## Dependency sections

See the [specifying dependencies page](specifying-dependencies.md) for
information on the `[dependencies]`, `[dev-dependencies]`,
`[build-dependencies]`, and target-specific `[target.*.dependencies]` sections.

## The `[profile.*]` sections

The `[profile]` tables provide a way to customize compiler settings such as
optimizations and debug settings. See [the Profiles chapter](profiles.md) for
more detail.



[`cargo init`]: ../commands/cargo-init.md
[`cargo new`]: ../commands/cargo-new.md
[`cargo package`]: ../commands/cargo-package.md
[`cargo run`]: ../commands/cargo-run.md
[crates.io]: https://crates.io/
[docs.rs]: https://docs.rs/
[publishing]: publishing.md
[Rust Edition]: ../../edition-guide/index.html
[spdx-2.3-license-expressions]: https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/
[spdx-license-list-3.20]: https://github.com/spdx/license-list-data/tree/v3.20
[SPDX site]: https://spdx.org
[TOML]: https://toml.io/


---

# Cargo Targets

Cargo packages consist of *targets* which correspond to source files which can
be compiled into a crate. Packages can have [library](#library),
[binary](#binaries), [example](#examples), [test](#tests), and
[benchmark](#benchmarks) targets. The list of targets can be configured in the
`Cargo.toml` manifest, often [inferred automatically](#target-auto-discovery)
by the [directory layout][package layout] of the source files.

See [Configuring a target](#configuring-a-target) below for details on
configuring the settings for a target.

## Library

The library target defines a "library" that can be used and linked by other
libraries and executables. The filename defaults to `src/lib.rs`, and the name
of the library defaults to the name of the package, with any dashes replaced
with underscores. A package can have only one library. The settings for the
library can be [customized] in the `[lib]` table in `Cargo.toml`.

```toml
# Example of customizing the library in Cargo.toml.
[lib]
crate-type = ["cdylib"]
bench = false
```

## Binaries

Binary targets are executable programs that can be run after being compiled.
A binary's source can be `src/main.rs` and/or stored in the [`src/bin/`
directory][package layout]. For `src/main.rs`, the default binary name is the
package name. The settings for each binary can be [customized] in the`[[bin]]`
tables in `Cargo.toml`.

Binaries can use the public API of the package's library. They are also linked
with the [`[dependencies]`][dependencies] defined in `Cargo.toml`.

You can run individual binaries with the [`cargo run`] command with the `--bin
<bin-name>` option. [`cargo install`] can be used to copy the executable to a
common location.

```toml
# Example of customizing binaries in Cargo.toml.
[[bin]]
name = "cool-tool"
test = false
bench = false

[[bin]]
name = "frobnicator"
required-features = ["frobnicate"]
```

## Examples

Files located under the [`examples` directory][package layout] are example
uses of the functionality provided by the library. When compiled, they are
placed in the [`target/debug/examples` directory][build cache].

Examples can use the public API of the package's library. They are also linked
with the [`[dependencies]`][dependencies] and
[`[dev-dependencies]`][dev-dependencies] defined in `Cargo.toml`.

By default, examples are executable binaries (with a `main()` function). You
can specify the [`crate-type` field](#the-crate-type-field) to make an example
be compiled as a library:

```toml
[[example]]
name = "foo"
crate-type = ["staticlib"]
```

You can run individual executable examples with the [`cargo run`] command with
the `--example <example-name>` option. Library examples can be built with
[`cargo build`] with the `--example <example-name>` option. [`cargo install`]
with the `--example <example-name>` option can be used to copy executable
binaries to a common location. Examples are compiled by [`cargo test`] by
default to protect them from bit-rotting. Set [the `test`
field](#the-test-field) to `true` if you have `#[test]` functions in the
example that you want to run with [`cargo test`].

## Tests

There are two styles of tests within a Cargo project:

* *Unit tests* which are functions marked with the [`#[test]`
  attribute][test-attribute] located within your library or binaries (or any
  target enabled with [the `test` field](#the-test-field)). These tests have
  access to private APIs located within the target they are defined in.
* *Integration tests* which is a separate executable binary, also containing
  `#[test]` functions, which is linked with the project's library and has
  access to its *public* API.

Tests are run with the [`cargo test`] command. By default, Cargo and `rustc`
use the [libtest harness] which is responsible for collecting functions
annotated with the [`#[test]` attribute][test-attribute] and executing them in
parallel, reporting the success and failure of each test. See [the `harness`
field](#the-harness-field) if you want to use a different harness or test
strategy.

> **Note**: There is another special style of test in Cargo:
> [documentation tests][documentation examples].
> They are handled by `rustdoc` and have a slightly different execution model.
> For more information, please see [`cargo test`][cargo-test-documentation-tests].

[libtest harness]: ../../rustc/tests/index.html
[cargo-test-documentation-tests]: ../commands/cargo-test.md#documentation-tests

### Integration tests

Files located under the [`tests` directory][package layout] are integration
tests. When you run [`cargo test`], Cargo will compile each of these files as
a separate crate, and execute them.

Integration tests can use the public API of the package's library. They are
also linked with the [`[dependencies]`][dependencies] and
[`[dev-dependencies]`][dev-dependencies] defined in `Cargo.toml`.

If you want to share code among multiple integration tests, you can place it
in a separate module such as `tests/common/mod.rs` and then put `mod common;`
in each test to import it.

Each integration test results in a separate executable binary, and [`cargo
test`] will run them serially. In some cases this can be inefficient, as it
can take longer to compile, and may not make full use of multiple CPUs when
running the tests. If you have a lot of integration tests, you may want to
consider creating a single integration test, and split the tests into multiple
modules. The libtest harness will automatically find all of the `#[test]`
annotated functions and run them in parallel. You can pass module names to
[`cargo test`] to only run the tests within that module.

Binary targets are automatically built if there is an integration test. This
allows an integration test to execute the binary to exercise and test its
behavior. The `CARGO_BIN_EXE_<name>` [environment variable] is set when the
integration test is built and run so that it can use the [`env` macro] or [`var` function]
to locate the executable.

[environment variable]: environment-variables.md#environment-variables-cargo-sets-for-crates
[`env` macro]: ../../std/macro.env.html
[`var` function]: ../../std/env/fn.var.html

## Benchmarks

Benchmarks provide a way to test the performance of your code using the
[`cargo bench`] command. They follow the same structure as [tests](#tests),
with each benchmark function annotated with the `#[bench]` attribute.
Similarly to tests:

* Benchmarks are placed in the [`benches` directory][package layout].
* Benchmark functions defined in libraries and binaries have access to the
  *private* API within the target they are defined in. Benchmarks in the
  `benches` directory may use the *public* API.
* [The `bench` field](#the-bench-field) can be used to define which targets
  are benchmarked by default.
* [The `harness` field](#the-harness-field) can be used to disable the
  built-in harness.

> **Note**: The [`#[bench]`
> attribute](../../unstable-book/library-features/test.html) is currently
> unstable and only available on the [nightly channel]. There are some
> packages available on [crates.io](https://crates.io/keywords/benchmark) that
> may help with running benchmarks on the stable channel, such as
> [Criterion](https://crates.io/crates/criterion).

## Configuring a target

All of the  `[lib]`, `[[bin]]`, `[[example]]`, `[[test]]`, and `[[bench]]`
sections in `Cargo.toml` support similar configuration for specifying how a
target should be built. The double-bracket sections like `[[bin]]` are
[array-of-table of TOML](https://toml.io/en/v1.0.0-rc.3#array-of-tables),
which means you can write more than one `[[bin]]` section to make several
executables in your crate. You can only specify one library, so `[lib]` is a
normal TOML table.

The following is an overview of the TOML settings for each target, with each
field described in detail below.

```toml
[lib]
name = "foo"           # The name of the target.
path = "src/lib.rs"    # The source file of the target.
test = true            # Is tested by default.
doctest = true         # Documentation examples are tested by default.
bench = true           # Is benchmarked by default.
doc = true             # Is documented by default.
proc-macro = false     # Set to `true` for a proc-macro library.
harness = true         # Use libtest harness.
crate-type = ["lib"]   # The crate types to generate.
required-features = [] # Features required to build this target (N/A for lib).
```

### The `name` field

The `name` field specifies the name of the target, which corresponds to the
filename of the artifact that will be generated. For a library, this is the
crate name that dependencies will use to reference it.

For the library target, this defaults to the name of the package , with any
dashes replaced with underscores. For the default binary (`src/main.rs`),
it also defaults to the name of the package, with no replacement for dashes.
For [auto discovered](#target-auto-discovery) targets, it defaults to the
directory or file name.

This is required for all targets except `[lib]`.

### The `path` field

The `path` field specifies where the source for the crate is located, relative
to the `Cargo.toml` file.

If not specified, the [inferred path](#target-auto-discovery) is used based on
the target name.

### The `test` field

The `test` field indicates whether or not the target is tested by default by
[`cargo test`]. The default is `true` for lib, bins, and tests.

> **Note**: Examples are built by [`cargo test`] by default to ensure they
> continue to compile, but they are not *tested* by default. Setting `test =
> true` for an example will also build it as a test and run any
> [`#[test]`][test-attribute] functions defined in the example.

### The `doctest` field

The `doctest` field indicates whether or not [documentation examples] are
tested by default by [`cargo test`]. This is only relevant for libraries, it
has no effect on other sections. The default is `true` for the library.

### The `bench` field

The `bench` field indicates whether or not the target is benchmarked by
default by [`cargo bench`]. The default is `true` for lib, bins, and
benchmarks.

### The `doc` field

The `doc` field indicates whether or not the target is included in the
documentation generated by [`cargo doc`] by default. The default is `true` for
libraries and binaries.

> **Note**: The binary will be skipped if its name is the same as the lib
> target.

### The `plugin` field

This option is deprecated and unused.

### The `proc-macro` field

The `proc-macro` field indicates that the library is a [procedural macro]
([reference][proc-macro-reference]). This is only valid for the `[lib]`
target.

### The `harness` field

The `harness` field indicates that the [`--test` flag] will be passed to
`rustc` which will automatically include the libtest library which is the
driver for collecting and running tests marked with the [`#[test]`
attribute][test-attribute] or benchmarks with the `#[bench]` attribute. The
default is `true` for all targets.

If set to `false`, then you are responsible for defining a `main()` function
to run tests and benchmarks.

Tests have the [`cfg(test)` conditional expression][cfg-test] enabled whether
or not the harness is enabled.

### The `crate-type` field

The `crate-type` field defines the [crate types] that will be generated by the
target. It is an array of strings, allowing you to specify multiple crate
types for a single target. This can only be specified for libraries and
examples. Binaries, tests, and benchmarks are always the "bin" crate type. The
defaults are:

Target | Crate Type
-------|-----------
Normal library | `"lib"`
Proc-macro library | `"proc-macro"`
Example | `"bin"`

The available options are `bin`, `lib`, `rlib`, `dylib`, `cdylib`,
`staticlib`, and `proc-macro`. You can read more about the different crate
types in the [Rust Reference Manual][crate types].

### The `required-features` field

The `required-features` field specifies which [features] the target needs in
order to be built. If any of the required features are not enabled, the
target will be skipped. This is only relevant for the `[[bin]]`, `[[bench]]`,
`[[test]]`, and `[[example]]` sections, it has no effect on `[lib]`.

```toml
[features]
# ...
postgres = []
sqlite = []
tools = []

[[bin]]
name = "my-pg-tool"
required-features = ["postgres", "tools"]
```

### The `edition` field

The `edition` field defines the [Rust edition] the target will use. If not
specified, it defaults to the [`edition` field][package-edition] for the
`[package]`.

> **Note:** This field is deprecated and will be removed in a future Edition

## Target auto-discovery

By default, Cargo automatically determines the targets to build based on the
[layout of the files][package layout] on the filesystem. The target
configuration tables, such as `[lib]`, `[[bin]]`, `[[test]]`, `[[bench]]`, or
`[[example]]`, can be used to add additional targets that don't follow the
standard directory layout.

The automatic target discovery can be disabled so that only manually
configured targets will be built. Setting the keys `autolib`, `autobins`, `autoexamples`,
`autotests`, or `autobenches` to `false` in the `[package]` section will
disable auto-discovery of the corresponding target type.

```toml
[package]
# ...
autolib = false
autobins = false
autoexamples = false
autotests = false
autobenches = false
```

Disabling automatic discovery should only be needed for specialized
situations. For example, if you have a library where you want a *module* named
`bin`, this would present a problem because Cargo would usually attempt to
compile anything in the `bin` directory as an executable. Here is a sample
layout of this scenario:

```text
├── Cargo.toml
└── src
    ├── lib.rs
    └── bin
        └── mod.rs
```

To prevent Cargo from inferring `src/bin/mod.rs` as an executable, set
`autobins = false` in `Cargo.toml` to disable auto-discovery:

```toml
[package]
# …
autobins = false
```

> **Note**: For packages with the 2015 edition, the default for auto-discovery
> is `false` if at least one target is manually defined in `Cargo.toml`.
> Beginning with the 2018 edition, the default is always `true`.

> **MSRV:** Respected as of 1.27 for `autobins`, `autoexamples`, `autotests`, and `autobenches`

> **MSRV:** Respected as of 1.83 for `autolib`

[Build cache]: build-cache.md
[Rust Edition]: ../../edition-guide/index.html
[`--test` flag]: ../../rustc/command-line-arguments.html#option-test
[`cargo bench`]: ../commands/cargo-bench.md
[`cargo build`]: ../commands/cargo-build.md
[`cargo doc`]: ../commands/cargo-doc.md
[`cargo install`]: ../commands/cargo-install.md
[`cargo run`]: ../commands/cargo-run.md
[`cargo test`]: ../commands/cargo-test.md
[cfg-test]: ../../reference/conditional-compilation.html#test
[crate types]: ../../reference/linkage.html
[crates.io]: https://crates.io/
[customized]: #configuring-a-target
[dependencies]: specifying-dependencies.md
[dev-dependencies]: specifying-dependencies.md#development-dependencies
[documentation examples]: ../../rustdoc/documentation-tests.html
[features]: features.md
[nightly channel]: ../../book/appendix-07-nightly-rust.html
[package layout]: ../guide/project-layout.md
[package-edition]: manifest.md#the-edition-field
[proc-macro-reference]: ../../reference/procedural-macros.html
[procedural macro]: ../../book/ch19-06-macros.html
[test-attribute]: ../../reference/attributes/testing.html#the-test-attribute


---

# Rust Version

The `rust-version` field is an optional key that tells cargo what version of the
Rust toolchain you support for your package.

```toml
[package]
# ...
rust-version = "1.56"
```

The Rust version must be a bare version number with at least one component; it
cannot include semver operators or pre-release identifiers. Compiler pre-release
identifiers such as -nightly will be ignored while checking the Rust version.

> **MSRV:** Respected as of 1.56

## Uses

**Diagnostics:**

When your package is compiled on an unsupported toolchain, Cargo will report that as an error to the user. This makes the support expectations clear and avoids reporting a less direct diagnostic like invalid syntax or missing functionality
in the standard library. This affects all [Cargo targets](cargo-targets.md) in the
package, including binaries, examples, test suites, benchmarks, etc.
A user can opt-in to an unsupported build of a package with the `--ignore-rust-version` flag.


**Development aid:**

`cargo add` will auto-select the dependency's version requirement to be the latest version compatible with your `rust-version`.
If that isn't the latest version, `cargo add` will inform users so they can make the choice on whether to keep it or update your `rust-version`.

The [resolver](resolver.md#rust-version) may take Rust version into account when picking dependencies.

Other tools may also take advantage of it, like `cargo clippy`'s
[`incompatible_msrv` lint](https://rust-lang.github.io/rust-clippy/stable/index.html#incompatible_msrv).

> **Note:** The `rust-version` may be ignored using the `--ignore-rust-version` option.

## Support Expectations

These are general expectations; some packages may document when they do not follow these.

**Complete:**

All functionality, including binaries and API, are available on the supported Rust versions under every [feature](features.md).

**Verified:**

A package's functionality is verified on its supported Rust versions, including automated testing.
See also our
[Rust version CI guide](../guide/continuous-integration.md#verifying-rust-version).

**Patchable:**

When licenses allow it,
users can [override their local dependency](overriding-dependencies.md) with a fork of your package.
In this situation, Cargo may load the entire workspace for the patched dependency which should work on the supported Rust versions, even if other packages in the workspace have different supported Rust versions.

**Dependency Support:**

In support of the above,
it is expected that each dependency's version-requirement supports at least one version compatible with your `rust-version`.
However,
it is **not** expected that the dependency specification excludes versions incompatible with your `rust-version`.
In fact, supporting both allows you to balance the needs of users that support older Rust versions with those that don't.

## Setting and Updating Rust Version

What Rust versions to support is a trade off between
- Costs for the maintainer in not using newer features of the Rust toolchain or their dependencies
- Costs to users who would benefit from a package using newer features of a toolchain, e.g. reducing build times by migrating to a feature in the standard library from a polyfill
- Availability of a package to users supporting older Rust versions

> **Note:** [Changing `rust-version`](semver.md#env-new-rust) is assumed to be a minor incompatibility

> **Recommendation:** Choose a policy for what Rust versions to support and when that is changed so users can compare it with their own policy and,
> if it isn't compatible,
> decide whether the loss of general improvements or the risk of a blocking bug that won't be fixed is acceptable or not.
>
> The simplest policy to support is to always use the latest Rust version.
>
> Depending on your risk profile, the next simplest approach is to continue to support old major or minor versions of your package that support older Rust versions.

### Selecting supported Rust versions

Users of your package are most likely to track their supported Rust versions to:
- Their Rust toolchain vendor's support policy, e.g. The Rust Project or a Linux distribution
  - Note: the Rust Project only offers bug fixes and security updates for the latest version.
- A fixed schedule for users to re-verify their packages with the new toolchain, e.g. the first release of the year, every 5 releases.

In addition, users are unlikely to be using the new Rust version immediately but need time to notice and re-verify or might not be aligned on the exact same schedule..

Example version policies:
- "N-2", meaning "latest version with a 2 release grace window for updating"
- Every even release with a 2 release grace window for updating
- Every version from this calendar year with a one year grace window for updating

> **Note:** To find the minimum `rust-version` compatible with your project as-is, you can use third-party tools like [`cargo-msrv`](https://crates.io/crates/cargo-msrv).

### Update timeline

When your policy specifies you no longer need to support a Rust version, you can update `rust-version` immediately or when needed.

By allowing `rust-version` to drift from your policy,
you offer users more of a grace window for upgrading.
However, this is too unpredictable to be relied on for aligning with the Rust version users track.

The further `rust-version` drifts from your specified policy,
the more likely users are to infer a policy you did not intend,
leading to frustration at the unmet expectations.

When drift is allowed,
there is the question of what is "justifiable enough" to drop supported Versions.
Each person can come to a reasonably different justification;
working through that discussion can be frustrating for the involved parties.
This will disempower those who would want to avoid that type of conflict,
which is particularly the case for new or casual contributors who either
feel that they are not in a position to raise the question or
that the conflict may hurt the chance of their change being merged.

### Multiple Policies in a Workspace

Cargo allows supporting multiple policies within one workspace.

Verifying specific packages under specific Rust versions can get complicated.
Tools like [`cargo-hack`](https://crates.io/crates/cargo-hack) can help.

For any dependency shared across policies,
the lowest common versions must be used as Cargo
[unifies SemVer-compatible versions](resolver.md#semver-compatibility),
potentially limiting access to features of the shared dependency for the workspace member with the higher `rust-version`.

To allow users to patch a dependency on one of your workspace members,
every package in the workspace would need to be loadable in the oldest Rust version supported by the workspace.

When using [`incompatible-rust-versions = "fallback"`](config.md#resolverincompatible-rust-versions),
the Rust version of one package can affect dependency versions selected for another package with a different Rust version.
See the [resolver](resolver.md#rust-version) chapter for more details.

### One or More Policies

One way to mitigate the downsides of supporting older Rust versions is to apply your policy to older major or minor versions of your package that you continue to support.
You likely still need a policy for what Rust versions the development branch support compared to the release branches for those major or minor versions.

Only updating the development branch when "needed"' can help reduce the number of supported release branches.

There is the question of what can be backported into these release branches.
By backporting new functionality between minor versions,
the next available version would be missing it which could be considered a breaking change, violating SemVer.
Backporting changes also comes with the risk of introducing bugs.

Supporting older versions comes at a cost.
This cost is dependent on the risk and impact of bugs within the package and what is acceptable for backporting.
Creating the release branches on-demand and putting the backport burden on the community are ways to balance this cost.

There is not yet a way for dependency management tools to report that a non-latest version is still supported,
shifting the responsibility to users to notice this in documentation.

For example, a Rust version support policy could look like:
- The development branch tracks to the latest stable release from the Rust Project, updated when needed
  - The minor version will be raised when changing `rust-version`
- The project supports every version for this calendar year, with another year grace window
  - The last minor version that supports a supported Rust version will receive community provided bug fixes
  - Fixes must be backported to all supported minor releases between the development branch and the needed supported Rust version
