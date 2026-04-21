# Specifying Dependencies

Your crates can depend on other libraries from [crates.io] or other
registries, `git` repositories, or subdirectories on your local file system.
You can also temporarily override the location of a dependency --- for example,
to be able to test out a bug fix in the dependency that you are working on
locally. You can have different dependencies for different platforms, and
dependencies that are only used during development. Let's take a look at how
to do each of these.

## Specifying dependencies from crates.io

Cargo is configured to look for dependencies on [crates.io] by default. Only
the name and a version string are required in this case. In [the cargo
guide](../guide/index.md), we specified a dependency on the `time` crate:

```toml
[dependencies]
time = "0.1.12"
```

The version string `"0.1.12"` is called a [version requirement](#version-requirement-syntax).
It specifies a range of versions that can be selected from when [resolving dependencies](resolver.md).
In this case, `"0.1.12"` represents the version range `>=0.1.12, <0.2.0`.
An update is allowed if it is within that range.
In this case, if we ran `cargo update time`, cargo should
update us to version `0.1.13` if it is the latest `0.1.z` release, but would not
update us to `0.2.0`.

## Version requirement syntax

### Default requirements

**Default requirements** specify a minimum version with the ability to update to [SemVer] compatible versions.
Versions are considered compatible if their left-most non-zero major/minor/patch component is the same.
This is different from [SemVer] which considers all pre-1.0.0 packages to be incompatible.

`1.2.3` is an example of a default requirement.

```notrust
1.2.3  :=  >=1.2.3, <2.0.0
1.2    :=  >=1.2.0, <2.0.0
1      :=  >=1.0.0, <2.0.0
0.2.3  :=  >=0.2.3, <0.3.0
0.2    :=  >=0.2.0, <0.3.0
0.0.3  :=  >=0.0.3, <0.0.4
0.0    :=  >=0.0.0, <0.1.0
0      :=  >=0.0.0, <1.0.0
```

### Caret requirements

**Caret requirements** are the default version requirement strategy. 
This version strategy allows [SemVer] compatible updates.
They are specified as version requirements with a leading caret (`^`).

`^1.2.3` is an example of a caret requirement.

Leaving off the caret is a simplified equivalent syntax to using caret requirements.
While caret requirements are the default, it is recommended to use the
simplified syntax when possible.

`log = "^1.2.3"` is exactly equivalent to `log = "1.2.3"`.

### Tilde requirements

**Tilde requirements** specify a minimal version with some ability to update.
If you specify a major, minor, and patch version or only a major and minor
version, only patch-level changes are allowed. If you only specify a major
version, then minor- and patch-level changes are allowed.

`~1.2.3` is an example of a tilde requirement.

```notrust
~1.2.3  := >=1.2.3, <1.3.0
~1.2    := >=1.2.0, <1.3.0
~1      := >=1.0.0, <2.0.0
```

### Wildcard requirements

**Wildcard requirements** allow for any version where the wildcard is
positioned.

`*`, `1.*` and `1.2.*` are examples of wildcard requirements.

```notrust
*     := >=0.0.0
1.*   := >=1.0.0, <2.0.0
1.2.* := >=1.2.0, <1.3.0
```

> **Note**: [crates.io] does not allow bare `*` versions.

### Comparison requirements

**Comparison requirements** allow manually specifying a version range or an
exact version to depend on.

Here are some examples of comparison requirements:

```notrust
>= 1.2.0
> 1
< 2
= 1.2.3
```

<span id="multiple-requirements"></span>
### Multiple version requirements

As shown in the examples above, multiple version requirements can be
separated with a comma, e.g., `>= 1.2, < 1.5`.
All requirements must be satisfied,
so non-overlapping requirements like `<1.2, ^1.2.2` result in no matching versions.

### Pre-releases

Version requirements exclude [pre-release versions](manifest.md#the-version-field), such as `1.0.0-alpha`,
unless specifically asked for.
For example, if `1.0.0-alpha` of package
`foo` is published, then a requirement of `foo = "1.0"` will *not* match, and
will return an error. The pre-release must be specified, such as `foo =
"1.0.0-alpha"`.
Similarly [`cargo install`] will avoid pre-releases unless
explicitly asked to install one.

Cargo allows "newer" pre-releases to be used automatically. For example, if
`1.0.0-beta` is published, then a requirement `foo = "1.0.0-alpha"` will allow
updating to the `beta` version. Note that this only works on the same release
version, `foo = "1.0.0-alpha"` will not allow updating to `foo = "1.0.1-alpha"`
or `foo = "1.0.1-beta"`.

Cargo will also upgrade automatically to semver-compatible released versions
from prereleases. The requirement `foo = "1.0.0-alpha"` will allow updating to
`foo = "1.0.0"` as well as `foo = "1.2.0"`.

Beware that pre-release versions can be unstable, and as such care should be
taken when using them. Some projects may choose to publish breaking changes
between pre-release versions. It is recommended to not use pre-release
dependencies in a library if your library is not also a pre-release. Care
should also be taken when updating your `Cargo.lock`, and be prepared if a
pre-release update causes issues.

[`cargo install`]: ../commands/cargo-install.md

### Version metadata

[Version metadata](manifest.md#the-version-field), such as `1.0.0+21AF26D3`,
is ignored and should not be used in version requirements.

> **Recommendation:** When in doubt, use the default version requirement operator.
>
> In rare circumstances, a package with a "public dependency"
> (re-exports the dependency or interoperates with it in its public API)
> that is compatible with multiple semver-incompatible versions
> (e.g. only uses a simple type that hasn't changed between releases, like an `Id`)
> may support users choosing which version of the "public dependency" to use.
> In this case, a version requirement like `">=0.4, <2"` may be of interest.
> *However* users of the package will likely run into errors and need to
> manually select a version of the "public dependency" via `cargo update` if
> they also depend on it as Cargo might pick different versions of the "public
> dependency" when [resolving dependency versions](resolver.md)  (see
> [#10599]).
>
> Avoid constraining the upper bound of a version to be anything less than the
> next semver incompatible version
> (e.g. avoid `">=2.0, <2.4"`, `"2.0.*"`, or `~2.0`),
> as other packages in the dependency tree may
> require a newer version, leading to an unresolvable error (see [#9029]).
> Consider whether controlling the version in your [`Cargo.lock`] would be more
> appropriate.
>
> In some instances this won't matter or the benefits might outweigh the cost, including:
> - When no one else depends on your package; e.g. it only has a `[[bin]]`
> - When depending on a pre-release package and wishing to avoid breaking
>   changes, then a fully specified `"=1.2.3-alpha.3"` might be warranted (see
>   [#2222])
> - When a library re-exports a proc-macro but the proc-macro generates code that
>   calls into the re-exporting library, then a fully specified `=1.2.3` might be
>   warranted to ensure the proc-macro isn't newer than the re-exporting library
>   and generating code that uses parts of the API that don't exist within the
>   current version

[`Cargo.lock`]: ../guide/cargo-toml-vs-cargo-lock.md
[#2222]: https://github.com/rust-lang/cargo/issues/2222
[#9029]: https://github.com/rust-lang/cargo/issues/9029
[#10599]: https://github.com/rust-lang/cargo/issues/10599

## Specifying dependencies from other registries

To specify a dependency from a registry other than [crates.io] set the `registry` key
to the name of the registry to use:

```toml
[dependencies]
some-crate = { version = "1.0", registry = "my-registry" }
```

where `my-registry` is the registry name configured in `.cargo/config.toml` file.
See the [registries documentation] for more information.

> **Note**: [crates.io] does not allow packages to be published with
> dependencies on code published outside of [crates.io].

[registries documentation]: registries.md

## Specifying dependencies from `git` repositories

To depend on a library located in a `git` repository, the minimum information
you need to specify is the location of the repository with the `git` key:

```toml
[dependencies]
regex = { git = "https://github.com/rust-lang/regex.git" }
```

Cargo fetches the `git` repository at that location and traverses the file tree to find
`Cargo.toml` file for the requested crate anywhere inside the `git` repository. 
For example, `regex-lite` and `regex-syntax` are members of `rust-lang/regex` repo
and can be referred to by the repo's root URL (`https://github.com/rust-lang/regex.git`)
regardless of where in the file tree they reside.

```toml
regex-lite   = { git = "https://github.com/rust-lang/regex.git" }
regex-syntax = { git = "https://github.com/rust-lang/regex.git" }
```

The above rule does not apply to [`path` dependencies](#specifying-path-dependencies).

### Choice of commit

Cargo assumes that we intend to use the latest commit on the default branch to build
our package if we only specify the repo URL, as in the examples above.

You can combine the `git` key with the `rev`, `tag`, or `branch` keys to be more specific about
which commit to use. Here's an example of using the latest commit on a branch named `next`:

```toml
[dependencies]
regex = { git = "https://github.com/rust-lang/regex.git", branch = "next" }
```

Anything that is not a branch or a tag falls under `rev` key. This can be a commit
hash like `rev = "4c59b707"`, or a named reference exposed by the remote
repository such as `rev = "refs/pull/493/head"`. 

What references are available for the `rev` key varies by where the repo is hosted.  
GitHub exposes a reference to the most recent commit of every pull request as in the example above.
Other git hosts may provide something equivalent under a different naming scheme.

**More `git` dependency examples:**

```toml
# .git suffix can be omitted if the host accepts such URLs - both examples work the same
regex = { git = "https://github.com/rust-lang/regex" }
regex = { git = "https://github.com/rust-lang/regex.git" }

# a commit with a particular tag
regex = { git = "https://github.com/rust-lang/regex.git", tag = "1.10.3" }

# a commit by its SHA1 hash
regex = { git = "https://github.com/rust-lang/regex.git", rev = "0c0990399270277832fbb5b91a1fa118e6f63dba" }

# HEAD commit of PR 493
regex = { git = "https://github.com/rust-lang/regex.git", rev = "refs/pull/493/head" }

# INVALID EXAMPLES

# specifying the commit after # ignores the commit ID and generates a warning
regex = { git = "https://github.com/rust-lang/regex.git#4c59b70" }

# git and path cannot be used at the same time
regex = { git = "https://github.com/rust-lang/regex.git#4c59b70", path = "../regex" }
```

Cargo locks the commits of `git` dependencies in `Cargo.lock` file at the time of their addition
and checks for updates only when you run `cargo update` command.

### The role of the `version` key

The `version` key always implies that the package is available in a registry,
regardless of the presence of `git` or `path` keys.

The `version` key does _not_ affect which commit is used when Cargo retrieves the `git` dependency,
but Cargo checks the version information in the dependency's `Cargo.toml` file 
against the `version` key and raises an error if the check fails.

In this example, Cargo retrieves the HEAD commit of the branch called `next` from Git and checks if the crate's version
is compatible with `version = "1.10.3"`:

```toml
[dependencies]
regex = { version = "1.10.3", git = "https://github.com/rust-lang/regex.git", branch = "next" }
```

`version`, `git`, and `path` keys are considered separate locations for resolving the dependency. 
See [Multiple locations](#multiple-locations) section below for detailed explanations.

> **Note**: [crates.io] does not allow packages to be published with
> dependencies on code published outside of [crates.io] itself
> ([dev-dependencies] are ignored). See the [Multiple
> locations](#multiple-locations) section for a fallback alternative for `git`
> and `path` dependencies.

### Git submodules

When cloning a `git` dependency,
Cargo automatically fetches its submodules recursively
so that all required code is available for the build.

To skip fetching submodules unrelated to the build,
you can set [`submodule.<name>.update = none`][submodule-update] in the dependency repo's `.gitmodules`.
This requires write access to the repo and will disable submodule updates more generally.

[submodule-update]: https://git-scm.com/docs/gitmodules#Documentation/gitmodules.txt-submodulenameupdate

### Accessing private Git repositories

See [Git Authentication](../appendix/git-authentication.md) for help with Git authentication for private repos.

## Specifying path dependencies

Over time, our `hello_world` package from [the guide](../guide/index.md) has
grown significantly in size! It’s gotten to the point that we probably want to
split out a separate crate for others to use. To do this Cargo supports **path
dependencies** which are typically sub-crates that live within one repository.
Let’s start by making a new crate inside of our `hello_world` package:

```console
# inside of hello_world/
$ cargo new hello_utils
```

This will create a new folder `hello_utils` inside of which a `Cargo.toml` and
`src` folder are ready to be configured. To tell Cargo about this, open
up `hello_world/Cargo.toml` and add `hello_utils` to your dependencies:

```toml
[dependencies]
hello_utils = { path = "hello_utils" }
```

This tells Cargo that we depend on a crate called `hello_utils` which is found
in the `hello_utils` folder, relative to the `Cargo.toml` file it’s written in.

The next `cargo build` will automatically build `hello_utils` and
all of its dependencies.

### No local path traversal

The local paths must point to the exact folder with the dependency's `Cargo.toml`.
Unlike with `git` dependencies, Cargo does not traverse local paths.
For example, if `regex-lite` and `regex-syntax` are members of a
locally cloned `rust-lang/regex` repo, they have to be referred to by the full path:

```toml
# git key accepts the repo root URL and Cargo traverses the tree to find the crate
[dependencies]
regex-lite   = { git = "https://github.com/rust-lang/regex.git" }
regex-syntax = { git = "https://github.com/rust-lang/regex.git" }

# path key requires the member name to be included in the local path
[dependencies]
regex-lite   = { path = "../regex/regex-lite" }
regex-syntax = { path = "../regex/regex-syntax" }
```

### Local paths in published crates

Crates that use dependencies specified with only a path are not
permitted on [crates.io].

If we wanted to publish our `hello_world` crate,
we would need to publish a version of `hello_utils` to [crates.io] as a separate crate
and specify its version in the dependencies line of `hello_world`:

```toml
[dependencies]
hello_utils = { path = "hello_utils", version = "0.1.0" }
```

The use of `path` and `version` keys together is explained in the [Multiple locations](#multiple-locations) section.

> **Note**: [crates.io] does not allow packages to be published with
> dependencies on code outside of [crates.io], except for [dev-dependencies].
> See the [Multiple locations](#multiple-locations) section
> for a fallback alternative for `git` and `path` dependencies.

## Multiple locations

It is possible to specify both a registry version and a `git` or `path`
location. The `git` or `path` dependency will be used locally (in which case
the `version` is checked against the local copy), and when published to a
registry like [crates.io], it will use the registry version. Other
combinations are not allowed. Examples:

```toml
[dependencies]
# Uses `my-bitflags` when used locally, and uses
# version 1.0 from crates.io when published.
bitflags = { path = "my-bitflags", version = "1.0" }

# Uses the given git repo when used locally, and uses
# version 1.0 from crates.io when published.
smallvec = { git = "https://github.com/servo/rust-smallvec.git", version = "1.0" }

# Note: if a version doesn't match, Cargo will fail to compile!
```

One example where this can be useful is when you have split up a library into
multiple packages within the same workspace. You can then use `path`
dependencies to point to the local packages within the workspace to use the
local version during development, and then use the [crates.io] version once it
is published. This is similar to specifying an
[override](overriding-dependencies.md), but only applies to this one
dependency declaration.

## Platform specific dependencies

Platform-specific dependencies take the same format, but are listed under a
`target` section. Normally Rust-like [`#[cfg]`
syntax](../../reference/conditional-compilation.html) will be used to define
these sections:

```toml
[target.'cfg(windows)'.dependencies]
winhttp = "0.4.0"

[target.'cfg(unix)'.dependencies]
openssl = "1.0.1"

[target.'cfg(target_arch = "x86")'.dependencies]
native-i686 = { path = "native/i686" }

[target.'cfg(target_arch = "x86_64")'.dependencies]
native-x86_64 = { path = "native/x86_64" }
```

Like with Rust, the syntax here supports the `not`, `any`, and `all` operators
to combine various cfg name/value pairs.

If you want to know which cfg targets are available on your platform, run
`rustc --print=cfg` from the command line. If you want to know which `cfg`
targets are available for another platform, such as 64-bit Windows,
run `rustc --print=cfg --target=x86_64-pc-windows-msvc`.

Unlike in your Rust source code, you cannot use
`[target.'cfg(feature = "fancy-feature")'.dependencies]` to add dependencies
based on optional features. Use [the `[features]` section](features.md)
instead:

```toml
[dependencies]
foo = { version = "1.0", optional = true }
bar = { version = "1.0", optional = true }

[features]
fancy-feature = ["foo", "bar"]
```

The same applies to `cfg(debug_assertions)`, `cfg(test)` and `cfg(proc_macro)`.
These values will not work as expected and will always have the default value
returned by `rustc --print=cfg`.
There is currently no way to add dependencies based on these configuration values.

In addition to `#[cfg]` syntax, Cargo also supports listing out the full target
the dependencies would apply to:

```toml
[target.x86_64-pc-windows-gnu.dependencies]
winhttp = "0.4.0"

[target.i686-unknown-linux-gnu.dependencies]
openssl = "1.0.1"
```

### Custom target specifications

If you’re using a custom target specification (such as `--target
foo/bar.json`), use the base filename without the `.json` extension:

```toml
[target.bar.dependencies]
winhttp = "0.4.0"

[target.my-special-i686-platform.dependencies]
openssl = "1.0.1"
native = { path = "native/i686" }
```

> **Note**: Custom target specifications are not usable on the stable channel.

## Development dependencies

You can add a `[dev-dependencies]` section to your `Cargo.toml` whose format
is equivalent to `[dependencies]`:

```toml
[dev-dependencies]
tempdir = "0.3"
```

Dev-dependencies are not used when compiling
a package for building, but are used for compiling tests, examples, and
benchmarks.

These dependencies are *not* propagated to other packages which depend on this
package.

You can also have target-specific development dependencies by using
`dev-dependencies` in the target section header instead of `dependencies`. For
example:

```toml
[target.'cfg(unix)'.dev-dependencies]
mio = "0.0.1"
```

> **Note**: When a package is published, only dev-dependencies that specify a
> `version` will be included in the published crate. For most use cases,
> dev-dependencies are not needed when published, though some users (like OS
> packagers) may want to run tests within a crate, so providing a `version` if
> possible can still be beneficial.

## Build dependencies

You can depend on other Cargo-based crates for use in your build scripts.
Dependencies are declared through the `build-dependencies` section of the
manifest:

```toml
[build-dependencies]
cc = "1.0.3"
```


You can also have target-specific build dependencies by using
`build-dependencies` in the target section header instead of `dependencies`. For
example:

```toml
[target.'cfg(unix)'.build-dependencies]
cc = "1.0.3"
```

In this case, the dependency will only be built when the host platform matches the
specified target.

The build script **does not** have access to the dependencies listed
in the `dependencies` or `dev-dependencies` section. Build
dependencies will likewise not be available to the package itself
unless listed under the `dependencies` section as well. A package
itself and its build script are built separately, so their
dependencies need not coincide. Cargo is kept simpler and cleaner by
using independent dependencies for independent purposes.

## Choosing features

If a package you depend on offers conditional features, you can
specify which to use:

```toml
[dependencies.awesome]
version = "1.3.5"
default-features = false # do not include the default features, and optionally
                         # cherry-pick individual features
features = ["secure-password", "civet"]
```

More information about features can be found in the [features
chapter](features.md#dependency-features).

## Renaming dependencies in `Cargo.toml`

When writing a `[dependencies]` section in `Cargo.toml` the key you write for a
dependency typically matches up to the name of the crate you import from in the
code. For some projects, though, you may wish to reference the crate with a
different name in the code regardless of how it's published on crates.io. For
example you may wish to:

* Avoid the need to  `use foo as bar` in Rust source.
* Depend on multiple versions of a crate.
* Depend on crates with the same name from different registries.

To support this Cargo supports a `package` key in the `[dependencies]` section
of which package should be depended on:

```toml
[package]
name = "mypackage"
version = "0.0.1"

[dependencies]
foo = "0.1"
bar = { git = "https://github.com/example/project.git", package = "foo" }
baz = { version = "0.1", registry = "custom", package = "foo" }
```

In this example, three crates are now available in your Rust code:

```rust,ignore
extern crate foo; // crates.io
extern crate bar; // git repository
extern crate baz; // registry `custom`
```

All three of these crates have the package name of `foo` in their own
`Cargo.toml`, so we're explicitly using the `package` key to inform Cargo that
we want the `foo` package even though we're calling it something else locally.
The `package` key, if not specified, defaults to the name of the dependency
being requested.

Note that if you have an optional dependency like:

```toml
[dependencies]
bar = { version = "0.1", package = 'foo', optional = true }
```

you're depending on the crate `foo` from crates.io, but your crate has a `bar`
feature instead of a `foo` feature. That is, names of features take after the
name of the dependency, not the package name, when renamed.

Enabling transitive dependencies works similarly, for example we could add the
following to the above manifest:

```toml
[features]
log-debug = ['bar/log-debug'] # using 'foo/log-debug' would be an error!
```

## Inheriting a dependency from a workspace

Dependencies can be inherited from a workspace by specifying the
dependency in the workspace's [`[workspace.dependencies]`][workspace.dependencies] table.
After that, add it to the `[dependencies]` table with `workspace = true`.

Along with the `workspace` key, dependencies can also include these keys:
- [`optional`][optional]: Note that the`[workspace.dependencies]` table is not allowed to specify `optional`.
- [`features`][features]: These are additive with the features declared in the `[workspace.dependencies]`

Other than `optional` and `features`, inherited dependencies cannot use any other
dependency key (such as `version` or `default-features`).

Dependencies in the `[dependencies]`, `[dev-dependencies]`, `[build-dependencies]`, and
`[target."...".dependencies]` sections support the ability to reference the
`[workspace.dependencies]` definition of dependencies.

```toml
[package]
name = "bar"
version = "0.2.0"

[dependencies]
regex = { workspace = true, features = ["unicode"] }

[build-dependencies]
cc.workspace = true

[dev-dependencies]
rand = { workspace = true, optional = true }
```


[SemVer]: https://semver.org
[crates.io]: https://crates.io/
[dev-dependencies]: #development-dependencies
[workspace.dependencies]: workspaces.md#the-dependencies-table
[optional]: features.md#optional-dependencies
[features]: features.md


---

# Overriding Dependencies

The desire to override a dependency can arise through a number of scenarios.
Most of them, however, boil down to the ability to work with a crate before
it's been published to [crates.io]. For example:

* A crate you're working on is also used in a much larger application you're
  working on, and you'd like to test a bug fix to the library inside of the
  larger application.
* An upstream crate you don't work on has a new feature or a bug fix on the
  master branch of its git repository which you'd like to test out.
* You're about to publish a new major version of your crate, but you'd like to
  do integration testing across an entire package to ensure the new major
  version works.
* You've submitted a fix to an upstream crate for a bug you found, but you'd
  like to immediately have your application start depending on the fixed
  version of the crate to avoid blocking on the bug fix getting merged.

These scenarios can be solved with the [`[patch]` manifest
section](#the-patch-section).

This chapter walks through a few different use cases, and includes details
on the different ways to override a dependency.

* Example use cases
    * [Testing a bugfix](#testing-a-bugfix)
    * [Working with an unpublished minor version](#working-with-an-unpublished-minor-version)
        * [Overriding repository URL](#overriding-repository-url)
    * [Prepublishing a breaking change](#prepublishing-a-breaking-change)
    * [Using `[patch]` with multiple versions](#using-patch-with-multiple-versions)
* Reference
    * [The `[patch]` section](#the-patch-section)
    * [The `[replace]` section](#the-replace-section)
    * [`paths` overrides](#paths-overrides)

> **Note**: See also specifying a dependency with [multiple locations], which
> can be used to override the source for a single dependency declaration in a
> local package.

## Testing a bugfix

Let's say you're working with the [`uuid` crate] but while you're working on it
you discover a bug. You are, however, quite enterprising so you decide to also
try to fix the bug! Originally your manifest will look like:

[`uuid` crate]: https://crates.io/crates/uuid

```toml
[package]
name = "my-library"
version = "0.1.0"

[dependencies]
uuid = "1.0"
```

First thing we'll do is to clone the [`uuid` repository][uuid-repository]
locally via:

```console
$ git clone https://github.com/uuid-rs/uuid.git
```

Next we'll edit the manifest of `my-library` to contain:

```toml
[patch.crates-io]
uuid = { path = "../path/to/uuid" }
```

Here we declare that we're *patching* the source `crates-io` with a new
dependency. This will effectively add the local checked out version of `uuid` to
the crates.io registry for our local package.

Next up we need to ensure that our lock file is updated to use this new version
of `uuid` so our package uses the locally checked out copy instead of one from
crates.io. The way `[patch]` works is that it'll load the dependency at
`../path/to/uuid` and then whenever crates.io is queried for versions of `uuid`
it'll *also* return the local version.

This means that the version number of the local checkout is significant and will
affect whether the patch is used. Our manifest declared `uuid = "1.0"` which
means we'll only resolve to `>= 1.0.0, < 2.0.0`, and Cargo's greedy resolution
algorithm also means that we'll resolve to the maximum version within that
range. Typically this doesn't matter as the version of the git repository will
already be greater or match the maximum version published on crates.io, but it's
important to keep this in mind!

In any case, typically all you need to do now is:

```console
$ cargo build
   Compiling uuid v1.0.0 (.../uuid)
   Compiling my-library v0.1.0 (.../my-library)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

And that's it! You're now building with the local version of `uuid` (note the
path in parentheses in the build output). If you don't see the local path version getting
built then you may need to run `cargo update uuid --precise $version` where
`$version` is the version of the locally checked out copy of `uuid`.

Once you've fixed the bug you originally found the next thing you'll want to do
is to likely submit that as a pull request to the `uuid` crate itself. Once
you've done this then you can also update the `[patch]` section. The listing
inside of `[patch]` is just like the `[dependencies]` section, so once your pull
request is merged you could change your `path` dependency to:

```toml
[patch.crates-io]
uuid = { git = 'https://github.com/uuid-rs/uuid.git' }
```

[uuid-repository]: https://github.com/uuid-rs/uuid

## Working with an unpublished minor version

Let's now shift gears a bit from bug fixes to adding features. While working on
`my-library` you discover that a whole new feature is needed in the `uuid`
crate. You've implemented this feature, tested it locally above with `[patch]`,
and submitted a pull request. Let's go over how you continue to use and test it
before it's actually published.

Let's also say that the current version of `uuid` on crates.io is `1.0.0`, but
since then the master branch of the git repository has updated to `1.0.1`. This
branch includes your new feature you submitted previously. To use this
repository we'll edit our `Cargo.toml` to look like

```toml
[package]
name = "my-library"
version = "0.1.0"

[dependencies]
uuid = "1.0.1"

[patch.crates-io]
uuid = { git = 'https://github.com/uuid-rs/uuid.git' }
```

Note that our local dependency on `uuid` has been updated to `1.0.1` as it's
what we'll actually require once the crate is published. This version doesn't
exist on crates.io, though, so we provide it with the `[patch]` section of the
manifest.

Now when our library is built it'll fetch `uuid` from the git repository and
resolve to 1.0.1 inside the repository instead of trying to download a version
from crates.io. Once 1.0.1 is published on crates.io the `[patch]` section can
be deleted.

It's also worth noting that `[patch]` applies *transitively*. Let's say you use
`my-library` in a larger package, such as:

```toml
[package]
name = "my-binary"
version = "0.1.0"

[dependencies]
my-library = { git = 'https://example.com/git/my-library' }
uuid = "1.0"

[patch.crates-io]
uuid = { git = 'https://github.com/uuid-rs/uuid.git' }
```

Remember that `[patch]` is applicable *transitively* but can only be defined at
the *top level* so the consumers of `my-library` have to repeat the `[patch]` section
if necessary. Here, though, the new `uuid` crate applies to *both* our dependency on
`uuid` and the `my-library -> uuid` dependency. The `uuid` crate will be resolved to
one version for this entire crate graph, 1.0.1, and it'll be pulled from the git
repository.

### Overriding repository URL

In case the dependency you want to override isn't loaded from `crates.io`,
you'll have to change a bit how you use `[patch]`. For example, if the
dependency is a git dependency, you can override it to a local path with:

```toml
[patch."https://github.com/your/repository"]
my-library = { path = "../my-library/path" }
```

And that's it!

## Prepublishing a breaking change

Let's take a look at working with a new major version of a crate, typically
accompanied with breaking changes. Sticking with our previous crates, this
means that we're going to be creating version 2.0.0 of the `uuid` crate. After
we've submitted all changes upstream we can update our manifest for
`my-library` to look like:

```toml
[dependencies]
uuid = "2.0"

[patch.crates-io]
uuid = { git = "https://github.com/uuid-rs/uuid.git", branch = "2.0.0" }
```

And that's it! Like with the previous example the 2.0.0 version doesn't actually
exist on crates.io but we can still put it in through a git dependency through
the usage of the `[patch]` section. As a thought exercise let's take another
look at the `my-binary` manifest from above again as well:

```toml
[package]
name = "my-binary"
version = "0.1.0"

[dependencies]
my-library = { git = 'https://example.com/git/my-library' }
uuid = "1.0"

[patch.crates-io]
uuid = { git = 'https://github.com/uuid-rs/uuid.git', branch = '2.0.0' }
```

Note that this will actually resolve to two versions of the `uuid` crate. The
`my-binary` crate will continue to use the 1.x.y series of the `uuid` crate but
the `my-library` crate will use the `2.0.0` version of `uuid`. This will allow you
to gradually roll out breaking changes to a crate through a dependency graph
without being forced to update everything all at once.

## Using `[patch]` with multiple versions

You can patch in multiple versions of the same crate with the `package` key
used to rename dependencies. For example let's say that the `serde` crate has
a bugfix that we'd like to use to its `1.*` series but we'd also like to
prototype using a `2.0.0` version of serde we have in our git repository. To
configure this we'd do:

```toml
[patch.crates-io]
serde = { git = 'https://github.com/serde-rs/serde.git' }
serde2 = { git = 'https://github.com/example/serde.git', package = 'serde', branch = 'v2' }
```

The first `serde = ...` directive indicates that serde `1.*` should be used
from the git repository (pulling in the bugfix we need) and the second `serde2
= ...` directive indicates that the `serde` package should also be pulled from
the `v2` branch of `https://github.com/example/serde`. We're assuming here
that `Cargo.toml` on that branch mentions version `2.0.0`.

Note that when using the `package` key the `serde2` identifier here is actually
ignored. We simply need a unique name which doesn't conflict with other patched
crates.

## The `[patch]` section

The `[patch]` section of `Cargo.toml` can be used to override dependencies
with other copies. The syntax is similar to the
[`[dependencies]`][dependencies] section:

```toml
[patch.crates-io]
foo = { git = 'https://github.com/example/foo.git' }
bar = { path = 'my/local/bar' }

[dependencies.baz]
git = 'https://github.com/example/baz.git'

[patch.'https://github.com/example/baz']
baz = { git = 'https://github.com/example/patched-baz.git', branch = 'my-branch' }
```

> **Note**: The `[patch]` table can also be specified as a [configuration
> option](config.md), such as in a `.cargo/config.toml` file or a CLI option
> like `--config 'patch.crates-io.rand.path="rand"'`. This can be useful for
> local-only changes that you don't want to commit, or temporarily testing a
> patch.

The `[patch]` table is made of dependency-like sub-tables. Each key after
`[patch]` is a URL of the source that is being patched, or the name of a
registry. The name `crates-io` may be used to override the default registry
[crates.io]. The first `[patch]` in the example above demonstrates overriding
[crates.io], and the second `[patch]` demonstrates overriding a git source.

Each entry in these tables is a normal dependency specification, the same as
found in the `[dependencies]` section of the manifest. The dependencies listed
in the `[patch]` section are resolved and used to patch the source at the
URL specified. The above manifest snippet patches the `crates-io` source (e.g.
crates.io itself) with the `foo` crate and `bar` crate. It also
patches the `https://github.com/example/baz` source with a `my-branch` that
comes from elsewhere.

Sources can be patched with versions of crates that do not exist, and they can
also be patched with versions of crates that already exist. If a source is
patched with a crate version that already exists in the source, then the
source's original crate is replaced.

Cargo only looks at the patch settings in the `Cargo.toml` manifest at the
root of the workspace. Patch settings defined in dependencies will be
ignored.

## The `[replace]` section

> **Note**: `[replace]` is deprecated. You should use the
> [`[patch]`](#the-patch-section) table instead.

This section of Cargo.toml can be used to override dependencies with other
copies. The syntax is similar to the `[dependencies]` section:

```toml
[replace]
"foo:0.1.0" = { git = 'https://github.com/example/foo.git' }
"bar:1.0.2" = { path = 'my/local/bar' }
```

Each key in the `[replace]` table is a [package ID
specification](pkgid-spec.md), which allows arbitrarily choosing a node in the
dependency graph to override (the 3-part version number is required). The
value of each key is the same as the `[dependencies]` syntax for specifying
dependencies, except that you can't specify features. Note that when a crate
is overridden the copy it's overridden with must have both the same name and
version, but it can come from a different source (e.g., git or a local path).

Cargo only looks at the replace settings in the `Cargo.toml` manifest at the
root of the workspace. Replace settings defined in dependencies will be
ignored.

## `paths` overrides

Sometimes you're only temporarily working on a crate and you don't want to have
to modify `Cargo.toml` like with the `[patch]` section above. For this use
case Cargo offers a much more limited version of overrides called **path
overrides**.

Path overrides are specified through [`.cargo/config.toml`](config.md) instead of
`Cargo.toml`. Inside of `.cargo/config.toml` you'll specify a key called `paths`:

```toml
paths = ["/path/to/uuid"]
```

This array should be filled with directories that contain a `Cargo.toml`. In
this instance, we’re just adding `uuid`, so it will be the only one that’s
overridden. This path can be either absolute or relative to the directory that
contains the `.cargo` folder.

Path overrides are more restricted than the `[patch]` section, however, in
that they cannot change the structure of the dependency graph. When a
path replacement is used then the previous set of dependencies
must all match exactly to the new `Cargo.toml` specification. For example this
means that path overrides cannot be used to test out adding a dependency to a
crate. Instead, `[patch]` must be used in that situation. As a result, usage of a
path override is typically isolated to quick bug fixes rather than larger
changes.

> **Note**: using a local configuration to override paths will only work for
> crates that have been published to [crates.io]. You cannot use this feature
> to tell Cargo how to find local unpublished crates.


[crates.io]: https://crates.io/
[multiple locations]: specifying-dependencies.md#multiple-locations
[dependencies]: specifying-dependencies.md


---

# Source Replacement

This document is about redirecting communication with [registries]
or repositories of [git-based dependencies] to another data source, such as a
server mirroring the original registry or an exact local copy.

If you want to patch individual dependencies, see [overriding dependencies] section of this
documentation. If you want to control how Cargo makes network requests, see [`[http]`](config.md#http)
and [`[net]`](config.md#net) configuration.

A *source* is a provider that contains crates that may be included as
dependencies for a package. Cargo supports the ability to **replace one source
with another** to express strategies such as:

* Vendoring --- custom sources can be defined which represent crates on the local
  filesystem. These sources are subsets of the source that they're replacing and
  can be checked into packages if necessary.

* Mirroring --- sources can be replaced with an equivalent version which acts as a
  cache for crates.io itself.

Cargo has a core assumption about source replacement that the source code is
exactly the same from both sources. Note that this also means that
a replacement source is not allowed to have crates which are not present in the
original source.

As a consequence, source replacement is not appropriate for situations such as
patching a dependency or a private registry. Cargo supports patching
dependencies through the usage of [the `[patch]` key][overriding
dependencies], and private registry support is described in [the Registries
chapter][registries].

When using source replacement, running commands that need to
contact the registry directly[^1] requires passing the `--registry` option. This helps avoid
any ambiguity about which registry to contact, and will use the authentication
token for the specified registry.

[^1]: Examples of such commands are in [Publishing Commands].

[Publishing Commands]: ../commands/publishing-commands.md
[overriding dependencies]: overriding-dependencies.md
[registries]: registries.md

## Configuration

Configuration of replacement sources is done through [`.cargo/config.toml`][config]
and the full set of available keys are:

```toml
# The `source` table is where all keys related to source-replacement
# are stored.
[source]

# Under the `source` table are a number of other tables whose keys are a
# name for the relevant source. For example this section defines a new
# source, called `my-vendor-source`, which comes from a directory
# located at `vendor` relative to the directory containing this `.cargo/config.toml`
# file
[source.my-vendor-source]
directory = "vendor"

# The crates.io default source for crates is available under the name
# "crates-io", and here we use the `replace-with` key to indicate that it's
# replaced with our source above.
#
# The `replace-with` key can also reference an alternative registry name
# defined in the `[registries]` table.
[source.crates-io]
replace-with = "my-vendor-source"

# Each source has its own table where the key is the name of the source
[source.the-source-name]

# Indicate that `the-source-name` will be replaced with `another-source`,
# defined elsewhere
replace-with = "another-source"

# Several kinds of sources can be specified (described in more detail below):
registry = "https://example.com/path/to/index"
local-registry = "path/to/registry"
directory = "path/to/vendor"

# Git sources can optionally specify a branch/tag/rev as well
git = "https://example.com/path/to/repo"
# branch = "master"
# tag = "v1.0.1"
# rev = "313f44e8"
```

[config]: config.md

## Registry Sources

A "registry source" is one that works like crates.io itself. It's an index
that conforms to the specification at https://doc.rust-lang.org/cargo/reference/registry-index.html
with a configuration file indicating where to download crates from.

Registry sources can use [either git or sparse HTTP protocol][protocols]:

```toml
# Git protocol
registry = "ssh://git@example.com/path/to/index.git"

# Sparse HTTP protocol  
registry = "sparse+https://example.com/path/to/index"

# HTTPS git protocol
registry = "https://example.com/path/to/index"
```

[protocols]: registries.md#registry-protocols

[crates.io index]: registry-index.md

## Local Registry Sources

A "local registry source" is intended to be a subset of another registry
source, but available on the local filesystem (aka vendoring). Local registries
are downloaded ahead of time, typically sync'd with a `Cargo.lock`, and are
made up of a set of `*.crate` files and an index like the normal registry is.

The primary way to manage and create local registry sources is through the
[`cargo-local-registry`][cargo-local-registry] subcommand,
[available on crates.io][cargo-local-registry] and can be installed with
`cargo install cargo-local-registry`.

[cargo-local-registry]: https://crates.io/crates/cargo-local-registry

Local registries are contained within one directory and contain a number of
`*.crate` files downloaded from crates.io as well as an `index` directory with
the same format as the crates.io-index project (populated with just entries for
the crates that are present).

## Directory Sources

A "directory source" is similar to a local registry source where it contains a
number of crates available on the local filesystem, suitable for vendoring
dependencies. Directory sources are primarily managed by the `cargo vendor`
subcommand.

Directory sources are distinct from local registries though in that they contain
the unpacked version of `*.crate` files, making it more suitable in some
situations to check everything into source control. A directory source is just a
directory containing a number of other directories which contain the source code
for crates (the unpacked version of `*.crate` files). Currently no restriction
is placed on the name of each directory.

Each crate in a directory source also has an associated metadata file indicating
the checksum of each file in the crate to protect against accidental
modifications.

## Git sources

Git sources represent repositories used by [git-based dependencies]. They're
used to specify which git-based dependencies should be replaced with alternative sources.

Git sources are *not* related to the [git registries][protocols],
and can't be used to replace registry sources.

[git-based dependencies]: specifying-dependencies.md#specifying-dependencies-from-git-repositories


---

# Dependency Resolution

One of Cargo's primary tasks is to determine the versions of dependencies to
use based on the version requirements specified in each package. This process
is called "dependency resolution" and is performed by the "resolver". The
result of the resolution is stored in the [`Cargo.lock` file] which "locks" the
dependencies to specific versions, and keeps them fixed over time.
The [`cargo tree`] command can be used to visualize the result of the
resolver.

[`Cargo.lock` file]: ../guide/cargo-toml-vs-cargo-lock.md
[dependency specifications]: specifying-dependencies.md
[dependency specification]: specifying-dependencies.md
[`cargo tree`]: ../commands/cargo-tree.md

## Constraints and Heuristics

In many cases there is no single "best" dependency resolution.
The resolver operates under various constraints and heuristics to find a generally applicable resolution.
To understand how these interact, it is helpful to have a coarse understanding of how dependency resolution works.

This pseudo-code approximates what Cargo's resolver does:
```rust
pub fn resolve(workspace: &[Package], policy: Policy) -> Option<ResolveGraph> {
    let dep_queue = Queue::new(workspace);
    let resolved = ResolveGraph::new();
    resolve_next(dep_queue, resolved, policy)
}

fn resolve_next(dep_queue: Queue, resolved: ResolveGraph, policy: Policy) -> Option<ResolveGraph> {
    let Some(dep_spec) = policy.pick_next_dep(&mut dep_queue) else {
        // Done
        return Some(resolved);
    };

    if let Some(resolved) = policy.try_unify_version(dep_spec, resolved.clone()) {
        return Some(resolved);
    }

    let dep_versions = dep_spec.lookup_versions()?;
    let mut dep_versions = policy.filter_versions(dep_spec, dep_versions);
    while let Some(dep_version) = policy.pick_next_version(&mut dep_versions) {
        if policy.needs_version_unification(&dep_version, &resolved) {
            continue;
        }

        let mut dep_queue = dep_queue.clone();
        dep_queue.enqueue(&dep_version.dependencies);
        let mut resolved = resolved.clone();
        resolved.register(dep_version);
        if let Some(resolved) = resolve_next(dep_queue, resolved, policy) {
            return Some(resolved);
        }
    }

    // No valid solution found, backtrack and `pick_next_version`
    None
}
```

Key steps:
- Walking dependencies (`pick_next_dep`):
  The order dependencies are walked can affect
  how related version requirements for the same dependency get resolved, see unifying versions,
  and how much the resolver backtracks, affecting resolver performance,
- Unifying versions (`try_unify_version`, `needs_version_unification`):
  Cargo reuses versions where possible to reduce build times and allow types from common dependencies to be passed between APIs.
  If multiple versions would have been unified if it wasn't for conflicts in their [dependency specifications], Cargo will backtrack, erroring if no solution is found, rather than selecting multiple versions.
  A [dependency specification] or Cargo may decide that a version is undesirable,
  preferring to backtrack or error rather than use it.
- Preferring versions (`pick_next_version`):
  Cargo may decide that it should prefer a specific version,
  falling back to the next version when backtracking.

### Version numbers

Generally, Cargo prefers the highest version currently available.

For example, if you had a package in the resolve graph with:
```toml
[dependencies]
bitflags = "*"
```
If at the time the `Cargo.lock` file is generated, the greatest version of
`bitflags` is `1.2.1`, then the package will use `1.2.1`.

For an example of a possible exception, see [Rust version](#rust-version).

### Version requirements

Package specify what versions they support, rejecting all others, through
[version requirements].

For example, if you had a package in the resolve graph with:
```toml
[dependencies]
bitflags = "1.0"  # meaning `>=1.0.0,<2.0.0`
```
If at the time the `Cargo.lock` file is generated, the greatest version of
`bitflags` is `1.2.1`, then the package will use `1.2.1` because it is the
greatest within the compatibility range. If `2.0.0` is published, it will
still use `1.2.1` because `2.0.0` is considered incompatible.

[version requirements]: specifying-dependencies.md#version-requirement-syntax

### SemVer compatibility

Cargo assumes packages follow [SemVer] and will unify dependency versions if they are
[SemVer] compatible according to the [Caret version requirements].
If two compatible versions cannot be unified because of conflicting version requirements,
Cargo will error.

See the [SemVer Compatibility] chapter for guidance on what is considered a
"compatible" change.

Examples:

The following two packages will have their dependencies on `bitflags` unified because any version picked will be compatible with each other.
```toml
# Package A
[dependencies]
bitflags = "1.0"  # meaning `>=1.0.0,<2.0.0`

# Package B
[dependencies]
bitflags = "1.1"  # meaning `>=1.1.0,<2.0.0`
```

The following packages will error because the version requirements conflict, selecting two distinct compatible versions.
```toml
# Package A
[dependencies]
log = "=0.4.11"

# Package B
[dependencies]
log = "=0.4.8"
```

The following two packages will not have their dependencies on `rand` unified because only incompatible versions are available for each.
Instead, two different versions (e.g. 0.6.5 and 0.7.3) will be resolved and built.
This can lead to potential problems, see the [Version-incompatibility hazards] section for more details.
```toml
# Package A
[dependencies]
rand = "0.7"  # meaning `>=0.7.0,<0.8.0`

# Package B
[dependencies]
rand = "0.6"  # meaning `>=0.6.0,<0.7.0`
```

Generally, the following two packages will not have their dependencies unified because incompatible versions are available that satisfy the version requirements:
Instead, two different versions (e.g. 0.6.5 and 0.7.3) will be resolved and built.
The application of other constraints or heuristics may cause these to be unified,
picking one version (e.g. 0.6.5).
```toml
# Package A
[dependencies]
rand = ">=0.6,<0.8.0"

# Package B
[dependencies]
rand = "0.6"  # meaning `>=0.6.0,<0.7.0`
```

[SemVer]: https://semver.org/
[SemVer Compatibility]: semver.md
[Caret version requirements]: specifying-dependencies.md#default-requirements
[Version-incompatibility hazards]: #version-incompatibility-hazards

#### Version-incompatibility hazards

When multiple versions of a crate appear in the resolve graph, this can cause
problems when types from those crates are exposed by the crates using them.
This is because the types and items are considered different by the Rust
compiler, even if they have the same name. Libraries should take care when
publishing a SemVer-incompatible version (for example, publishing `2.0.0`
after `1.0.0` has been in use), particularly for libraries that are widely
used.

The "[semver trick]" is a workaround for this problem of publishing a breaking
change while retaining compatibility with older versions. The linked page goes
into detail about what the problem is and how to address it. In short, when a
library wants to publish a SemVer-breaking release, publish the new release,
and also publish a point release of the previous version that reexports the
types from the newer version.

These incompatibilities usually manifest as a compile-time error, but
sometimes they will only appear as a runtime misbehavior. For example, let's
say there is a common library named `foo` that ends up appearing with both
version `1.0.0` and `2.0.0` in the resolve graph. If [`downcast_ref`] is used
on an object created by a library using version `1.0.0`, and the code calling
`downcast_ref` is downcasting to a type from version `2.0.0`, the downcast
will fail at runtime.

It is important to make sure that if you have multiple versions of a library
that you are properly using them, especially if it is ever possible for the
types from different versions to be used together. The [`cargo tree
-d`][`cargo tree`] command can be used to identify duplicate versions and
where they come from. Similarly, it is important to consider the impact on the
ecosystem if you publish a SemVer-incompatible version of a popular library.

[semver trick]: https://github.com/dtolnay/semver-trick
[`downcast_ref`]: ../../std/any/trait.Any.html#method.downcast_ref

### Lock file

Cargo gives the highest priority to versions contained in the [`Cargo.lock` file], when used.
This is intended to balance reproducible builds with adjusting to changes in the manifest.

For example, if you had a package in the resolve graph with:
```toml
[dependencies]
bitflags = "*"
```
If at the time your `Cargo.lock` file is generated, the greatest version of
`bitflags` is `1.2.1`, then the package will use `1.2.1` and recorded in the `Cargo.lock` file.

By the time Cargo next runs, `bitflags` `1.3.5` is out.
When resolving dependencies,
`1.2.1` will still be used because it is present in your `Cargo.lock` file.

The package is then edited to:
```toml
[dependencies]
bitflags = "1.3.0"
```
`bitflags` `1.2.1` does not match this version requirement and so that entry in your `Cargo.lock` file is ignored and version `1.3.5` will now be used and recorded in your `Cargo.lock` file.

### Rust version

To support developing software with a minimum supported [Rust version],
the resolver can take into account a dependency version's compatibility with your Rust version.
This is controlled by the config field [`resolver.incompatible-rust-versions`].

With the `fallback` setting, the resolver will prefer packages with a Rust version that is
less than or equal to your own Rust version.
For example, you are using Rust 1.85 to develop the following package:
```toml
[package]
name = "my-cli"
rust-version = "1.62"

[dependencies]
clap = "4.0"  # resolves to 4.0.32
```
The resolver would pick version 4.0.32 because it has a Rust version of 1.60.0.
- 4.0.0 is not picked because it is a [lower version number](#version-numbers) despite it also having a Rust version of 1.60.0.
- 4.5.20 is not picked because it is incompatible with `my-cli`'s Rust version of 1.62 despite having a much [higher version](#version-numbers) and it has a Rust version of 1.74.0 which is compatible with your 1.85 toolchain.

If a version requirement does not include a Rust version compatible dependency version,
the resolver won't error but will instead pick a version, even if its potentially suboptimal.
For example, you change the dependency on `clap`:
```toml
[package]
name = "my-cli"
rust-version = "1.62"

[dependencies]
clap = "4.2"  # resolves to 4.5.20
```
No version of `clap` matches that [version requirement](#version-requirements)
that is compatible with Rust version 1.62.
The resolver will then pick an incompatible version, like 4.5.20 despite it having a Rust version of 1.74.

When the resolver selects a dependency version of a package,
it does not know all the workspace members that will eventually have a transitive dependency on that version
and so it cannot take into account only the Rust versions relevant for that dependency.
The resolver has heuristics to find a "good enough" solution when workspace members have different Rust versions.
This applies even for packages in a workspace without a Rust version.

When a workspace has members with different Rust versions,
the resolver may pick a lower dependency version than necessary.
For example, you have the following workspace members:
```toml
[package]
name = "a"
rust-version = "1.62"

[package]
name = "b"

[dependencies]
clap = "4.2"  # resolves to 4.5.20
```
Though package `b` does not have a Rust version and could use a higher version like 4.5.20,
4.0.32 will be selected because of package `a`'s Rust version of 1.62.

Or the resolver may pick too high of a version.
For example, you have the following workspace members:
```toml
[package]
name = "a"
rust-version = "1.62"

[dependencies]
clap = "4.2"  # resolves to 4.5.20

[package]
name = "b"

[dependencies]
clap = "4.5"  # resolves to 4.5.20
```
Though each package has a version requirement for `clap` that would meet its own Rust version,
because of [version unification](#version-numbers),
the resolver will need to pick one version that works in both cases and that would be a version like 4.5.20.

[Rust version]: rust-version.md
[`resolver.incompatible-rust-versions`]: config.md#resolverincompatible-rust-versions

### Features

For the purpose of generating `Cargo.lock`, the resolver builds the dependency
graph as-if all [features] of all [workspace] members are enabled. This
ensures that any optional dependencies are available and properly resolved
with the rest of the graph when features are added or removed with the
[`--features` command-line flag](features.md#command-line-feature-options).
The resolver runs a second time to determine the actual features used when
*compiling* a crate, based on the features selected on the command-line.

Dependencies are resolved with the union of all features enabled on them. For
example, if one package depends on the [`im`] package with the [`serde`
dependency] enabled and another package depends on it with the [`rayon`
dependency] enabled, then `im` will be built with both features enabled, and
the `serde` and `rayon` crates will be included in the resolve graph. If no
packages depend on `im` with those features, then those optional dependencies
will be ignored, and they will not affect resolution.

When building multiple packages in a workspace (such as with `--workspace` or
multiple `-p` flags), the features of the dependencies of all of those
packages are unified. If you have a circumstance where you want to avoid that
unification for different workspace members, you will need to build them via
separate `cargo` invocations.

The resolver will skip over versions of packages that are missing required
features. For example, if a package depends on version `^1` of [`regex`] with
the [`perf` feature], then the oldest version it can select is `1.3.0`,
because versions prior to that did not contain the `perf` feature. Similarly,
if a feature is removed from a new release, then packages that require that
feature will be stuck on the older releases that contain that feature. It is
discouraged to remove features in a SemVer-compatible release. Beware that
optional dependencies also define an implicit feature, so removing an optional
dependency or making it non-optional can cause problems, see [removing an
optional dependency].

[`im`]: https://crates.io/crates/im
[`perf` feature]: https://github.com/rust-lang/regex/blob/1.3.0/Cargo.toml#L56
[`rayon` dependency]: https://github.com/bodil/im-rs/blob/v15.0.0/Cargo.toml#L47
[`regex`]: https://crates.io/crates/regex
[`serde` dependency]: https://github.com/bodil/im-rs/blob/v15.0.0/Cargo.toml#L46
[features]: features.md
[removing an optional dependency]: semver.md#cargo-remove-opt-dep
[workspace]: workspaces.md

#### Feature resolver version 2

When `resolver = "2"` is specified in `Cargo.toml` (see [resolver
versions](#resolver-versions) below), a different feature resolver is used
which uses a different algorithm for unifying features. The version `"1"`
resolver will unify features for a package no matter where it is specified.
The version `"2"` resolver will avoid unifying features in the following
situations:

* Features for target-specific dependencies are not enabled if the target is
  not currently being built. For example:

  ```toml
  [dependencies.common]
  version = "1.0"
  features = ["f1"]

  [target.'cfg(windows)'.dependencies.common]
  version = "1.0"
  features = ["f2"]
  ```

  When building this example for a non-Windows platform, the `f2` feature will
  *not* be enabled.

* Features enabled on [build-dependencies] or proc-macros will not be unified
  when those same dependencies are used as a normal dependency. For example:

  ```toml
  [dependencies]
  log = "0.4"

  [build-dependencies]
  log = {version = "0.4", features=['std']}
  ```

  When building the build script, the `log` crate will be built with the `std`
  feature. When building the library of your package, it will not enable the
  feature.

* Features enabled on [dev-dependencies] will not be unified when those same
  dependencies are used as a normal dependency, unless those dev-dependencies
  are currently being built. For example:

  ```toml
  [dependencies]
  serde = {version = "1.0", default-features = false}

  [dev-dependencies]
  serde = {version = "1.0", features = ["std"]}
  ```

  In this example, the library will normally link against `serde` without the
  `std` feature. However, when built as a test or example, it will include the
  `std` feature. For example, `cargo test` or `cargo build --all-targets` will
  unify these features. Note that dev-dependencies in dependencies are always
  ignored, this is only relevant for the top-level package or workspace
  members.

[build-dependencies]: specifying-dependencies.md#build-dependencies
[dev-dependencies]: specifying-dependencies.md#development-dependencies
[resolver-field]: features.md#resolver-versions

### `links`

The [`links` field] is used to ensure only one copy of a native library is
linked into a binary. The resolver will attempt to find a graph where there is
only one instance of each `links` name. If it is unable to find a graph that
satisfies that constraint, it will return an error.

For example, it is an error if one package depends on [`libgit2-sys`] version
`0.11` and another depends on `0.12`, because Cargo is unable to unify those,
but they both link to the `git2` native library. Due to this requirement, it
is encouraged to be very careful when making SemVer-incompatible releases with
the `links` field if your library is in common use.

[`links` field]: manifest.md#the-links-field
[`libgit2-sys`]: https://crates.io/crates/libgit2-sys

### Yanked versions

[Yanked releases][yank] are those that are marked that they should not be
used. When the resolver is building the graph, it will ignore all yanked
releases unless they already exist in the `Cargo.lock` file or are explicitly
requested by the [`--precise`] flag of `cargo update` (nightly only).

[yank]: publishing.md#cargo-yank
[`--precise`]: ../commands/cargo-update.md#option-cargo-update---precise

## Dependency updates

Dependency resolution is automatically performed by all Cargo commands that
need to know about the dependency graph. For example, [`cargo build`] will run
the resolver to discover all the dependencies to build. After the first time
it runs, the result is stored in the `Cargo.lock` file. Subsequent commands
will run the resolver, keeping dependencies locked to the versions in
`Cargo.lock` *if it can*.

If the dependency list in `Cargo.toml` has been modified, for example changing
the version of a dependency from `1.0` to `2.0`, then the resolver will select
a new version for that dependency that matches the new requirements. If that
new dependency introduces new requirements, those new requirements may also
trigger additional updates. The `Cargo.lock` file will be updated with the new
result. The `--locked` or `--frozen` flags can be used to change this behavior
to prevent automatic updates when requirements change, and return an error
instead.

[`cargo update`] can be used to update the entries in `Cargo.lock` when new
versions are published. Without any options, it will attempt to update all
packages in the lock file. The `-p` flag can be used to target the update for
a specific package, and other flags such as `--recursive` or `--precise` can
be used to control how versions are selected.

[`cargo build`]: ../commands/cargo-build.md
[`cargo update`]: ../commands/cargo-update.md

## Overrides

Cargo has several mechanisms to override dependencies within the graph. The
[Overriding Dependencies] chapter goes into detail on how to use overrides.
The overrides appear as an overlay to a registry, replacing the patched
version with the new entry. Otherwise, resolution is performed like normal.

[Overriding Dependencies]: overriding-dependencies.md

## Dependency kinds

There are three kinds of dependencies in a package: normal, [build], and
[dev][dev-dependencies]. For the most part these are all treated the same from
the perspective of the resolver. One difference is that dev-dependencies for
non-workspace members are always ignored, and do not influence resolution.

[Platform-specific dependencies] with the `[target]` table are resolved as-if
all platforms are enabled. In other words, the resolver ignores the platform
or `cfg` expression.

[build]: specifying-dependencies.md#build-dependencies
[dev-dependencies]: specifying-dependencies.md#development-dependencies
[Platform-specific dependencies]: specifying-dependencies.md#platform-specific-dependencies

### dev-dependency cycles

Usually the resolver does not allow cycles in the graph, but it does allow
them for [dev-dependencies]. For example, project "foo" has a dev-dependency
on "bar", which has a normal dependency on "foo" (usually as a "path"
dependency). This is allowed because there isn't really a cycle from the
perspective of the build artifacts. In this example, the "foo" library is
built (which does not need "bar" because "bar" is only used for tests), and
then "bar" can be built depending on "foo", then the "foo" tests can be built
linking to "bar".

Beware that this can lead to confusing errors. In the case of building library
unit tests, there are actually two copies of the library linked into the final
test binary: the one that was linked with "bar", and the one built that
contains the unit tests. Similar to the issues highlighted in the
[Version-incompatibility hazards] section, the types between the two are not
compatible. Be careful when exposing types of "foo" from "bar" in this
situation, since the "foo" unit tests won't treat them the same as the local
types.

If possible, try to split your package into multiple packages and restructure
it so that it remains strictly acyclic.

## Resolver versions

Different resolver behavior can be specified through the resolver
version in `Cargo.toml` like this:

```toml
[package]
name = "my-package"
version = "1.0.0"
resolver = "2"
```
- `"1"` (default)
- `"2"` ([`edition = "2021"`](manifest.md#the-edition-field) default): Introduces changes in [feature
unification](#features). See the [features chapter][features-2] for more
details.
- `"3"` ([`edition = "2024"`](manifest.md#the-edition-field) default, requires Rust 1.84+): Change the default for [`resolver.incompatible-rust-versions`] from `allow` to `fallback`

The resolver is a global option that affects the entire workspace. The
`resolver` version in dependencies is ignored, only the value in the top-level
package will be used. If using a [virtual workspace], the version should be
specified in the `[workspace]` table, for example:

```toml
[workspace]
members = ["member1", "member2"]
resolver = "2"
```

> **MSRV:** Requires 1.51+

[virtual workspace]: workspaces.md#virtual-workspace
[features-2]: features.md#feature-resolver-version-2

## Recommendations

The following are some recommendations for setting the version within your
package, and for specifying dependency requirements. These are general
guidelines that should apply to common situations, but of course some
situations may require specifying unusual requirements.

* Follow the [SemVer guidelines] when deciding how to update your version
  number, and whether or not you will need to make a SemVer-incompatible
  version change.
* Use caret requirements for dependencies, such as `"1.2.3"`, for most
  situations. This ensures that the resolver can be maximally flexible in
  choosing a version while maintaining build compatibility.
  * Specify all three components with the version you are currently using.
    This helps set the minimum version that will be used, and ensures that
    other users won't end up with an older version of the dependency that
    might be missing something that your package requires.
  * Avoid `*` requirements, as they are not allowed on [crates.io], and they
    can pull in SemVer-breaking changes during a normal `cargo update`.
  * Avoid overly broad version requirements. For example, `>=2.0.0` can pull
    in any SemVer-incompatible version, like version `5.0.0`, which can result
    in broken builds in the future.
  * Avoid overly narrow version requirements if possible. For example, if you
    specify a tilde requirement like `bar="~1.3"`, and another package
    specifies a requirement of `bar="1.4"`, this will fail to resolve, even
    though minor releases should be compatible.
* Try to keep the dependency versions up-to-date with the actual minimum
  versions that your library requires. For example, if you have a requirement
  of `bar="1.0.12"`, and then in a future release you start using new features
  added in the `1.1.0` release of "bar", update your dependency requirement to
  `bar="1.1.0"`.

  If you fail to do this, it may not be immediately obvious because Cargo can
  opportunistically choose the newest version when you run a blanket `cargo
  update`. However, if another user depends on your library, and runs `cargo
  update your-library`, it will *not* automatically update "bar" if it is
  locked in their `Cargo.lock`. It will only update "bar" in that situation if
  the dependency declaration is also updated. Failure to do so can cause
  confusing build errors for the user using `cargo update your-library`.
* If two packages are tightly coupled, then an `=` dependency requirement may
  help ensure that they stay in sync. For example, a library with a companion
  proc-macro library will sometimes make assumptions between the two libraries
  that won't work well if the two are out of sync (and it is never expected to
  use the two libraries independently). The parent library can use an `=`
  requirement on the proc-macro, and re-export the macros for easy access.
* `0.0.x` versions can be used for packages that are permanently unstable.

In general, the stricter you make the dependency requirements, the more likely
it will be for the resolver to fail. Conversely, if you use requirements that
are too loose, it may be possible for new versions to be published that will
break the build.

[SemVer guidelines]: semver.md
[crates.io]: https://crates.io/

## Troubleshooting

The following illustrates some problems you may experience, and some possible
solutions.

### Why was a dependency included?

Say you see dependency `rand` in the `cargo check` output but don't think it's needed and want to understand why it's being pulled in.

You can run
```console
$ cargo tree --workspace --target all --all-features --invert rand
rand v0.8.5
└── ...

rand v0.8.5
└── ...
```

### Why was that feature on this dependency enabled?

You might identify that it was an activated feature that caused `rand` to show up.  **To figure out which package activated the feature, you can add the `--edges features`**
```console
$ cargo tree --workspace --target all --all-features --edges features --invert rand
rand v0.8.5
└── ...

rand v0.8.5
└── ...
```

### Unexpected dependency duplication

You see multiple instances of `rand` when you run
```console
$ cargo tree --workspace --target all --all-features --duplicates
rand v0.7.3
└── ...

rand v0.8.5
└── ...
```

The resolver algorithm has converged on a solution that includes two copies of a
dependency when one would suffice. For example:

```toml
# Package A
[dependencies]
rand = "0.7"

# Package B
[dependencies]
rand = ">=0.6"  # note: open requirements such as this are discouraged
```

In this example, Cargo may build two copies of the `rand` crate, even though a
single copy at version `0.7.3` would meet all requirements. This is because the
resolver's algorithm favors building the latest available version of `rand` for
Package B, which is `0.8.5` at the time of this writing, and that is
incompatible with Package A's specification. The resolver's algorithm does not
currently attempt to "deduplicate" in this situation.

The use of open-ended version requirements like `>=0.6` is discouraged in Cargo.
But, if you run into this situation, the [`cargo update`] command with the
`--precise` flag can be used to manually remove such duplications.

[`cargo update`]: ../commands/cargo-update.md

### Why wasn't a newer version selected?

Say you noticed that the latest version of a dependency wasn't selected when you ran:
```console
$ cargo update
```
You can enable some extra logging to see why this happened:
```console
$ env CARGO_LOG=cargo::core::resolver=trace cargo update
```
**Note:** Cargo log targets and levels may change over time.

### SemVer-breaking patch release breaks the build

Sometimes a project may inadvertently publish a point release with a
SemVer-breaking change. When users update with `cargo update`, they will pick
up this new release, and then their build may break. In this situation, it is
recommended that the project should [yank] the release, and either remove the
SemVer-breaking change, or publish it as a new SemVer-major version increase.

If the change happened in a third-party project, if possible try to
(politely!) work with the project to resolve the issue.

While waiting for the release to be yanked, some workarounds depend on the
circumstances:

* If your project is the end product (such as a binary executable), just avoid
  updating the offending package in `Cargo.lock`. This can be done with the
  `--precise` flag in [`cargo update`].
* If you publish a binary on [crates.io], then you can temporarily add an `=`
  requirement to force the dependency to a specific good version.
  * Binary projects can alternatively recommend users to use the `--locked`
    flag with [`cargo install`] to use the original `Cargo.lock` that contains
    the known good version.
* Libraries may also consider publishing a temporary new release with stricter
  requirements that avoid the troublesome dependency. You may want to consider
  using range requirements (instead of `=`) to avoid overly-strict
  requirements that may conflict with other packages using the same
  dependency. Once the problem has been resolved, you can publish another
  point release that relaxes the dependency back to a caret requirement.
* If it looks like the third-party project is unable or unwilling to yank the
  release, then one option is to update your code to be compatible with the
  changes, and update the dependency requirement to set the minimum version to
  the new release. You will also need to consider if this is a SemVer-breaking
  change of your own library, for example if it exposes types from the
  dependency.

[`cargo install`]: ../commands/cargo-install.md
