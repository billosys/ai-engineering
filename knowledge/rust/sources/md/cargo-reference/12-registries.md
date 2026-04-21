# Registries

Cargo installs crates and fetches dependencies from a "registry". The default
registry is [crates.io]. A registry contains an "index" which contains a
searchable list of available crates. A registry may also provide a web API to
support publishing new crates directly from Cargo.

> Note: If you are interested in mirroring or vendoring an existing registry,
> take a look at [Source Replacement].

If you are implementing a registry server, see [Running a Registry] for more
details about the protocol between Cargo and a registry.

If you're using a registry that requires authentication, see [Registry Authentication].
If you are implementing a credential provider, see [Credential Provider Protocol]
for details.

## Using an Alternate Registry

To use a registry other than [crates.io], the name and index URL of the
registry must be added to a [`.cargo/config.toml` file][config]. The `registries`
table has a key for each registry, for example:

```toml
[registries]
my-registry = { index = "https://my-intranet:8080/git/index" }
```

The `index` key should be a URL to a git repository with the registry's index or a
Cargo sparse registry URL with the `sparse+` prefix.

A crate can then depend on a crate from another registry by specifying the
`registry` key and a value of the registry's name in that dependency's entry
in `Cargo.toml`:

```toml
# Sample Cargo.toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2024"

[dependencies]
other-crate = { version = "1.0", registry = "my-registry" }
```

As with most config values, the index may be specified with an environment
variable instead of a config file. For example, setting the following
environment variable will accomplish the same thing as defining a config file:

```ignore
CARGO_REGISTRIES_MY_REGISTRY_INDEX=https://my-intranet:8080/git/index
```

> Note: [crates.io] does not accept packages that depend on crates from other
> registries.

## Publishing to an Alternate Registry

If the registry supports web API access, then packages can be published
directly to the registry from Cargo. Several of Cargo's commands such as
[`cargo publish`] take a `--registry` command-line flag to indicate which
registry to use. For example, to publish the package in the current directory:

1. `cargo login --registry=my-registry`

    This only needs to be done once. You must enter the secret API token
    retrieved from the registry's website. Alternatively the token may be
    passed directly to the `publish` command with the `--token` command-line
    flag or an environment variable with the name of the registry such as
    `CARGO_REGISTRIES_MY_REGISTRY_TOKEN`.

2. `cargo publish --registry=my-registry`

Instead of always passing the `--registry` command-line option, the default
registry may be set in [`.cargo/config.toml`][config] with the `registry.default`
key. For example:

```toml
[registry]
default = "my-registry"
```

Setting the `package.publish` key in the `Cargo.toml` manifest restricts which
registries the package is allowed to be published to. This is useful to
prevent accidentally publishing a closed-source package to [crates.io]. The
value may be a list of registry names, for example:

```toml
[package]
# ...
publish = ["my-registry"]
```

The `publish` value may also be `false` to restrict all publishing, which is
the same as an empty list.

The authentication information saved by [`cargo login`] is stored in the
`credentials.toml` file in the Cargo home directory (default `$HOME/.cargo`). It
has a separate table for each registry, for example:

```toml
[registries.my-registry]
token = "854DvwSlUwEHtIo3kWy6x7UCPKHfzCmy"
```

## Registry Protocols
Cargo supports two remote registry protocols: `git` and `sparse`. If the registry
index URL starts with `sparse+`, Cargo uses the sparse protocol. Otherwise
Cargo uses the `git` protocol.

The `git` protocol stores index metadata in a git repository and requires Cargo to clone
the entire repo.

The `sparse` protocol fetches individual metadata files using plain HTTP requests.
Since Cargo only downloads the metadata for relevant crates, the `sparse` protocol can
save significant time and bandwidth.

The [crates.io] registry supports both protocols. The protocol for crates.io is
controlled via the [`registries.crates-io.protocol`] config key.

[Source Replacement]: source-replacement.md
[Running a Registry]: running-a-registry.md
[Credential Provider Protocol]: credential-provider-protocol.md
[Registry Authentication]: registry-authentication.md
[`cargo publish`]: ../commands/cargo-publish.md
[`cargo package`]: ../commands/cargo-package.md
[`cargo login`]: ../commands/cargo-login.md
[config]: config.md
[crates.io]: https://crates.io/
[`registries.crates-io.protocol`]: config.md#registriescrates-ioprotocol


---

# Registry Authentication
Cargo authenticates to registries with credential providers. These
credential providers are external executables or built-in providers that Cargo
uses to store and retrieve credentials.

Using alternative registries with authentication *requires* a credential provider to be configured
to avoid unknowingly storing unencrypted credentials on disk. For historical reasons, public
(non-authenticated) registries do not require credential provider configuration, and the `cargo:token`
provider is used if no providers are configured.

Cargo also includes platform-specific providers that use the operating system to securely store
tokens. The `cargo:token` provider is also included which stores credentials in unencrypted plain
text in the [credentials](config.md#credentials) file.

## Recommended configuration
It's recommended to configure a global credential provider list in `$CARGO_HOME/config.toml`
which defaults to:
* Windows: `%USERPROFILE%\.cargo\config.toml`
* Unix: `~/.cargo/config.toml`

This recommended configuration uses the operating system provider, with a fallback to `cargo:token`
to look in Cargo's [credentials](config.md#credentials) file or environment variables:
```toml
# ~/.cargo/config.toml
[registry]
global-credential-providers = ["cargo:token", "cargo:libsecret", "cargo:macos-keychain", "cargo:wincred"]
```
*Note that later entries have higher precedence.
See [`registry.global-credential-providers`](config.md#registryglobal-credential-providers)
for more details.*

Some private registries may also recommend a registry-specific credential-provider. Check your
registry's documentation to see if this is the case.

## Built-in providers
Cargo includes several built-in credential providers. The available built-in providers
may change in future Cargo releases (though there are currently no plans to do so).

### `cargo:token`
Uses Cargo's [credentials](config.md#credentials) file to store tokens unencrypted in plain text.
When retrieving tokens, checks the `CARGO_REGISTRIES_<NAME>_TOKEN` environment variable.
If this credential provider is not listed, then the `*_TOKEN` environment variables will not work.

### `cargo:wincred`
Uses the Windows Credential Manager to store tokens.

The credentials are stored as `cargo-registry:<index-url>` in the Credential Manager
under "Windows Credentials".

### `cargo:macos-keychain`
Uses the macOS Keychain to store tokens.

The Keychain Access app can be used to view stored tokens.

### `cargo:libsecret`
Uses [libsecret](https://wiki.gnome.org/Projects/Libsecret) to store tokens.

Any password manager with libsecret support can be used to view stored tokens.
The following are a few examples (non-exhaustive):

- [GNOME Keyring](https://wiki.gnome.org/Projects/GnomeKeyring)
- [KDE Wallet Manager](https://apps.kde.org/kwalletmanager5/) (since KDE Frameworks 5.97.0)
- [KeePassXC](https://keepassxc.org/) (since 2.5.0)

### `cargo:token-from-stdout <command> <args>`
Launch a subprocess that returns a token on stdout. Newlines will be trimmed.
* The process inherits the user's stdin and stderr.
* It should exit 0 on success, and nonzero on error.
* [`cargo login`] and [`cargo logout`] are not supported and return an error if used.

The following environment variables will be provided to the executed command:

* `CARGO` --- Path to the `cargo` binary executing the command.
* `CARGO_REGISTRY_INDEX_URL` --- The URL of the registry index.
* `CARGO_REGISTRY_NAME_OPT` --- Optional name of the registry. Should not be used as a lookup key.

Arguments will be passed on to the subcommand.

[`cargo login`]: ../commands/cargo-login.md
[`cargo logout`]: ../commands/cargo-logout.md

## Credential plugins
For credential provider plugins that follow Cargo's [credential provider protocol](credential-provider-protocol.md),
the configuration value should be a string with the path to the executable (or the executable name if on the `PATH`).

For example, to install [cargo-credential-1password](https://crates.io/crates/cargo-credential-1password)
from crates.io do the following:

Install the provider with `cargo install cargo-credential-1password`

In the config, add to (or create) `registry.global-credential-providers`:
```toml
[registry]
global-credential-providers = ["cargo:token", "cargo-credential-1password --account my.1password.com"]
```

The values in `global-credential-providers` are split on spaces into path and command-line arguments. To
define a global credential provider where the path or arguments contain spaces, use
the [`[credential-alias]` table](config.md#credential-alias).


---

# Credential Provider Protocol
This document describes information for building a Cargo credential provider. For information on
setting up or using a credential provider, see [Registry Authentication](registry-authentication.md).

When using an external credential provider, Cargo communicates with the credential
provider using stdin/stdout messages passed as single lines of JSON.

Cargo will always execute the credential provider with the `--cargo-plugin` argument.
This enables a credential provider executable to have additional functionality beyond
what Cargo needs. Additional arguments are included in the JSON via the `args` field.

## JSON messages
The JSON messages in this document have newlines added for readability.
Actual messages must not contain newlines.

### Credential hello
* Sent by: credential provider
* Purpose: used to identify the supported protocols on process startup
```javascript
{
    "v":[1]
}
```

Requests sent by Cargo will include a `v` field set to one of the versions listed here.
If Cargo does not support any of the versions offered by the credential provider, it will issue an
error and shut down the credential process.

### Registry information
* Sent by: Cargo
Not a message by itself. Included in all messages sent by Cargo as the `registry` field.
```javascript
{
    // Index URL of the registry
    "index-url":"https://github.com/rust-lang/crates.io-index",
    // Name of the registry in configuration (optional)
    "name": "crates-io",
    // HTTP headers received from attempting to access an authenticated registry (optional)
    "headers": ["WWW-Authenticate: cargo"]
}
```

### Login request
* Sent by: Cargo
* Purpose: collect and store credentials
```javascript
{
    // Protocol version
    "v":1,
    // Action to perform: login
    "kind":"login",
    // Registry information (see Registry information)
    "registry":{"index-url":"sparse+https://registry-url/index/", "name": "my-registry"},
    // User-specified token from stdin or command line (optional)
    "token": "<the token value>",
    // URL that the user could visit to get a token (optional)
    "login-url": "http://registry-url/login",
    // Additional command-line args (optional)
    "args":[]
}
```

If the `token` field is set, then the credential provider should use the token provided. If
the `token` is not set, then the credential provider should prompt the user for a token.

In addition to the arguments that may be passed to the credential provider in
configuration, `cargo login` also supports passing additional command line args
via `cargo login -- <additional args>`. These additional arguments will be included
in the `args` field after any args from Cargo configuration.

### Read request
* Sent by: Cargo
* Purpose: Get the credential for reading crate information
```javascript
{
    // Protocol version
    "v":1,
    // Request kind: get credentials
    "kind":"get",
    // Action to perform: read crate information
    "operation":"read",
    // Registry information (see Registry information)
    "registry":{"index-url":"sparse+https://registry-url/index/", "name": "my-registry"},
    // Additional command-line args (optional)
    "args":[]
}
```

### Publish request
* Sent by: Cargo
* Purpose: Get the credential for publishing a crate
```javascript
{
    // Protocol version
    "v":1,
    // Request kind: get credentials
    "kind":"get",
    // Action to perform: publish crate
    "operation":"publish",
    // Crate name
    "name":"sample",
    // Crate version
    "vers":"0.1.0",
    // Crate checksum
    "cksum":"...",
    // Registry information (see Registry information)
    "registry":{"index-url":"sparse+https://registry-url/index/", "name": "my-registry"},
    // Additional command-line args (optional)
    "args":[]
}
```

### Get success response
* Sent by: credential provider
* Purpose: Gives the credential to Cargo
```javascript
{"Ok":{
    // Response kind: this was a get request
    "kind":"get",
    // Token to send to the registry
    "token":"...",
    // Cache control. Can be one of the following:
    // * "never": do not cache
    // * "session": cache for the current cargo session
    // * "expires": cache for the current cargo session until expiration
    "cache":"expires",
    // Unix timestamp (only for "cache": "expires")
    "expiration":1693942857,
    // Is the token operation independent?
    "operation_independent":true
}}
```

The `token` will be sent to the registry as the value of the `Authorization` HTTP header.

`operation_independent` indicates whether the token can be cached across different
operations (such as publishing or fetching). In general, this should be `true` unless
the provider wants to generate tokens that are scoped to specific operations.

### Login success response
* Sent by: credential provider
* Purpose: Indicates the login was successful
```javascript
{"Ok":{
    // Response kind: this was a login request
    "kind":"login"
}}
```

### Logout success response
* Sent by: credential provider
* Purpose: Indicates the logout was successful
```javascript
{"Ok":{
    // Response kind: this was a logout request
    "kind":"logout"
}}
```

### Failure response (URL not supported)
* Sent by: credential provider
* Purpose: Gives error information to Cargo
```javascript
{"Err":{
    "kind":"url-not-supported"
}}
```
Sent if the credential provider is designed
to only handle specific registry URLs and the given URL
is not supported. Cargo will attempt another provider if
available.

### Failure response (not found)
* Sent by: credential provider
* Purpose: Gives error information to Cargo
```javascript
{"Err":{
    // Error: The credential could not be found in the provider.
    "kind":"not-found"
}}
```
Sent if the credential could not be found. This is expected for
`get` requests where the credential is not available, or `logout`
requests where there is nothing found to erase.

### Failure response (operation not supported)
* Sent by: credential provider
* Purpose: Gives error information to Cargo
```javascript
{"Err":{
    // Error: The credential could not be found in the provider.
    "kind":"operation-not-supported"
}}
```
Sent if the credential provider does not support the requested operation.
If a provider only supports `get` and a `login` is requested, the
provider should respond with this error.

### Failure response (other)
* Sent by: credential provider
* Purpose: Gives error information to Cargo
```javascript
{"Err":{
    // Error: something else has failed
    "kind":"other",
    // Error message string to be displayed
    "message": "free form string error message",
    // Detailed cause chain for the error (optional)
    "caused-by": ["cause 1", "cause 2"]
}}
```

## Example communication to request a token for reading:
1. Cargo spawns the credential process, capturing stdin and stdout.
2. Credential process sends the Hello message to Cargo
    ```javascript
    { "v": [1] }
   ```
3. Cargo sends the CredentialRequest message to the credential process (newlines added for readability).
    ```javascript
    {
        "v": 1,
        "kind": "get",
        "operation": "read",
        "registry":{"index-url":"sparse+https://registry-url/index/"}
    }
    ```
4. Credential process sends the CredentialResponse to Cargo (newlines added for readability).
    ```javascript
    {
        "token": "...",
        "cache": "session",
        "operation_independent": true
    }
    ```
5. Cargo closes the stdin pipe to the credential provider and it exits.
6. Cargo uses the token for the remainder of the session (until Cargo exits) when interacting with this registry.


---

# Running a Registry

A minimal registry can be implemented by having a git repository that contains
an index, and a server that contains the compressed `.crate` files created by
[`cargo package`]. Users won't be able to use Cargo to publish to it, but this
may be sufficient for closed environments. The index format is described in
[Registry Index].

A full-featured registry that supports publishing will additionally need to
have a web API service that conforms to the API used by Cargo. The web API is
described in [Registry Web API].

Commercial and community projects are available for building and running a
registry. See <https://github.com/rust-lang/cargo/wiki/Third-party-registries>
for a list of what is available.

[Registry Web API]: registry-web-api.md
[Registry Index]: registry-index.md
[`cargo publish`]: ../commands/cargo-publish.md
[`cargo package`]: ../commands/cargo-package.md


---

# Index Format

The following defines the format of the index. New features are occasionally
added, which are only understood starting with the version of Cargo that
introduced them. Older versions of Cargo may not be able to use packages that
make use of new features. However, the format for older packages should not
change, so older versions of Cargo should be able to use them.

## Index Configuration
The root of the index contains a file named `config.json` which contains JSON
information used by Cargo for accessing the registry. This is an example of
what the [crates.io] config file looks like:

```javascript
{
    "dl": "https://crates.io/api/v1/crates",
    "api": "https://crates.io"
}
```

The keys are:
- `dl`: This is the URL for downloading crates listed in the index. The value
  may have the following markers which will be replaced with their
  corresponding value:

  - `{crate}`: The name of crate.
  - `{version}`: The crate version.
  - `{prefix}`: A directory prefix computed from the crate name. For example,
    a crate named `cargo` has a prefix of `ca/rg`. See below for details.
  - `{lowerprefix}`: Lowercase variant of `{prefix}`.
  - `{sha256-checksum}`: The crate's sha256 checksum.

  If none of the markers are present, then the value
  `/{crate}/{version}/download` is appended to the end.
- `api`: This is the base URL for the web API. This key is optional, but if it
  is not specified, commands such as [`cargo publish`] will not work. The web
  API is described below. This URL should not have a trailing slash.
- `auth-required`: indicates whether this is a private registry that requires
  all operations to be authenticated including API requests, crate downloads
  and sparse index updates.


## Download Endpoint
The download endpoint should send the `.crate` file for the requested package.
Cargo supports https, http, and file URLs, HTTP redirects, HTTP1 and HTTP2.
The exact specifics of TLS support depend on the platform that Cargo is
running on, the version of Cargo, and how it was compiled.

If `auth-required: true` is set in `config.json`, the `Authorization` header
will be included with http(s) download requests.

## Index files
The rest of the index repository contains one file for each package, where the
filename is the name of the package in lowercase. Each version of the package
has a separate line in the file. The files are organized in a tier of
directories:

- Packages with 1 character names are placed in a directory named `1`.
- Packages with 2 character names are placed in a directory named `2`.
- Packages with 3 character names are placed in the directory
  `3/{first-character}` where `{first-character}` is the first character of
  the package name.
- All other packages are stored in directories named
  `{first-two}/{second-two}` where the top directory is the first two
  characters of the package name, and the next subdirectory is the third and
  fourth characters of the package name. For example, `cargo` would be stored
  in a file named `ca/rg/cargo`.

> Note: Although the index filenames are in lowercase, the fields that contain
> package names in `Cargo.toml` and the index JSON data are case-sensitive and
> may contain upper and lower case characters.

The directory name above is calculated based on the package name converted to
lowercase; it is represented by the marker `{lowerprefix}`.  When the original
package name is used without case conversion, the resulting directory name is
represented by the marker `{prefix}`.  For example, the package `MyCrate` would
have a `{prefix}` of `My/Cr` and a `{lowerprefix}` of `my/cr`.  In general,
using `{prefix}` is recommended over `{lowerprefix}`, but there are pros and
cons to each choice.  Using `{prefix}` on case-insensitive filesystems results
in (harmless-but-inelegant) directory aliasing.  For example, `crate` and
`CrateTwo` have `{prefix}` values of `cr/at` and `Cr/at`; these are distinct on
Unix machines but alias to the same directory on Windows.  Using directories
with normalized case avoids aliasing, but on case-sensitive filesystems it's
harder to support older versions of Cargo that lack `{prefix}`/`{lowerprefix}`.
For example, nginx rewrite rules can easily construct `{prefix}` but can't
perform case-conversion to construct `{lowerprefix}`.

## Name restrictions

Registries should consider enforcing limitations on package names added to
their index. Cargo itself allows names with any [alphanumeric], `-`, or `_`
characters. [crates.io] imposes its own limitations, including the following:

- Only allows ASCII characters.
- Only alphanumeric, `-`, and `_` characters.
- First character must be alphabetic.
- Case-insensitive collision detection.
- Prevent differences of `-` vs `_`.
- Under a specific length (max 64).
- Rejects reserved names, such as Windows special filenames like "nul".

Registries should consider incorporating similar restrictions, and consider
the security implications, such as [IDN homograph
attacks](https://en.wikipedia.org/wiki/IDN_homograph_attack) and other
concerns in [UTR36](https://www.unicode.org/reports/tr36/) and
[UTS39](https://www.unicode.org/reports/tr39/).

## Version uniqueness

Indexes *must* ensure that each version only appears once for each package.
This includes ignoring SemVer build metadata.
For example, the index must *not* contain two entries with a version `1.0.7` and `1.0.7+extra`.

## JSON schema

Each line in a package file contains a JSON object that describes a published
version of the package. The following is a pretty-printed example with comments
explaining the format of the entry.

```javascript
{
    // The name of the package.
    // This must only contain alphanumeric, `-`, or `_` characters.
    "name": "foo",
    // The version of the package this row is describing.
    // This must be a valid version number according to the Semantic
    // Versioning 2.0.0 spec at https://semver.org/.
    "vers": "0.1.0",
    // Array of direct dependencies of the package.
    "deps": [
        {
            // Name of the dependency.
            // If the dependency is renamed from the original package name,
            // this is the new name. The original package name is stored in
            // the `package` field.
            "name": "rand",
            // The SemVer requirement for this dependency.
            // This must be a valid version requirement defined at
            // https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html.
            "req": "^0.6",
            // Array of features (as strings) enabled for this dependency.
            // Since Cargo 1.84, defaults to `[]` if not specified.
            "features": ["i128_support"],
            // Boolean of whether or not this is an optional dependency.
            // Since Cargo 1.84, defaults to `false` if not specified.
            "optional": false,
            // Boolean of whether or not default features are enabled.
            // Since Cargo 1.84, defaults to `true` if not specified.
            "default_features": true,
            // The target platform for the dependency.
            // If not specified or `null`, it is not a target dependency.
            // Otherwise, a string such as "cfg(windows)".
            "target": null,
            // The dependency kind.
            // "dev", "build", or "normal".
            // If not specified or `null`, it defaults to "normal".
            "kind": "normal",
            // The URL of the index of the registry where this dependency is
            // from as a string. If not specified or `null`, it is assumed the
            // dependency is in the current registry.
            "registry": null,
            // If the dependency is renamed, this is a string of the actual
            // package name. If not specified or `null`, this dependency is not
            // renamed.
            "package": null,
        }
    ],
    // A SHA256 checksum of the `.crate` file.
    "cksum": "d867001db0e2b6e0496f9fac96930e2d42233ecd3ca0413e0753d4c7695d289c",
    // Set of features defined for the package.
    // Each feature maps to an array of features or dependencies it enables.
    // Since Cargo 1.84, defaults to `{}` if not specified.
    "features": {
        "extras": ["rand/simd_support"]
    },
    // Boolean of whether or not this version has been yanked.
    "yanked": false,
    // The `links` string value from the package's manifest, or null if not
    // specified. This field is optional and defaults to null.
    "links": null,
    // An unsigned 32-bit integer value indicating the schema version of this
    // entry.
    //
    // If this is not specified, it should be interpreted as the default of 1.
    //
    // Cargo (starting with version 1.51) will ignore versions it does not
    // recognize. This provides a method to safely introduce changes to index
    // entries and allow older versions of cargo to ignore newer entries it
    // doesn't understand. Versions older than 1.51 ignore this field, and
    // thus may misinterpret the meaning of the index entry.
    //
    // The current values are:
    //
    // * 1: The schema as documented here, not including newer additions.
    //      This is honored in Rust version 1.51 and newer.
    // * 2: The addition of the `features2` field.
    //      This is honored in Rust version 1.60 and newer.
    "v": 2,
    // This optional field contains features with new, extended syntax.
    // Specifically, namespaced features (`dep:`) and weak dependencies
    // (`pkg?/feat`).
    //
    // This is separated from `features` because versions older than 1.19
    // will fail to load due to not being able to parse the new syntax, even
    // with a `Cargo.lock` file.
    //
    // Cargo will merge any values listed here with the "features" field.
    //
    // If this field is included, the "v" field should be set to at least 2.
    //
    // Registries are not required to use this field for extended feature
    // syntax, they are allowed to include those in the "features" field.
    // Using this is only necessary if the registry wants to support cargo
    // versions older than 1.19, which in practice is only crates.io since
    // those older versions do not support other registries.
    "features2": {
        "serde": ["dep:serde", "chrono?/serde"]
    }
    // The minimal supported Rust version (optional)
    // This must be a valid version requirement without an operator (e.g. no `=`)
    "rust_version": "1.60",
    // The publish time of this package version (optional).
    //
    // The format is a subset of ISO8601:
    // - `yyyy-mm-ddThh:mm:ssZ`
    // - no fractional seconds
    // - always `Z` for UTC timezone, no timezone offsets supported
    // - fields are 0-padded
    //
    // Example: 2025-11-12T19:30:12Z
    //
    // This should be the original publish time and not changed on any status changes,
    // like `yanked`.
    "pubtime": "2025-11-12T19:30:12Z"
}
```

The JSON objects should not be modified after they are added except for the
`yanked` field whose value may change at any time.

> **Note**: The index JSON format has subtle differences from the JSON format of the [Publish API] and [`cargo metadata`].
> If you are using one of those as a source to generate index entries, you are encouraged to carefully inspect the documentation differences between them.
>
> For the [Publish API], the differences are:
>
> * `deps`
>     * `name` --- When the dependency is [renamed] in `Cargo.toml`, the publish API puts the original package name in the `name` field and the aliased name in the `explicit_name_in_toml` field.
>       The index places the aliased name in the `name` field, and the original package name in the `package` field.
>     * `req` --- The Publish API field is called `version_req`.
> * `cksum` --- The publish API does not specify the checksum, it must be computed by the registry before adding to the index.
> * `features` --- Some features may be placed in the `features2` field.
>   Note: This is only a legacy requirement for [crates.io]; other registries should not need to bother with modifying the features map.
>   The `v` field indicates the presence of the `features2` field.
> * The publish API includes several other fields, such as `description` and `readme`, which don't appear in the index.
>   These are intended to make it easier for a registry to obtain the metadata about the crate to display on a website without needing to extract and parse the `.crate` file.
>   This additional information is typically added to a database on the registry server.
> * Although `rust_version` is included here, [crates.io] will ignore this field
>   and instead read it from the `Cargo.toml` contained in the `.crate` file.
>
> For [`cargo metadata`], the differences are:
>
> * `vers` --- The `cargo metadata` field is called `version`.
> * `deps`
>   * `name` --- When the dependency is [renamed] in `Cargo.toml`, `cargo metadata` puts the original package name in the `name` field and the aliased name in the `rename` field.
>     The index places the aliased name in the `name` field, and the original package name in the `package` field.
>   * `default_features` --- The `cargo metadata` field is called `uses_default_features`.
>   * `registry` --- `cargo metadata` uses a value of `null` to indicate that the dependency comes from [crates.io].
>     The index uses a value of `null` to indicate that the dependency comes from the same registry as the index.
>     When creating an index entry, a registry other than [crates.io] should translate a value of `null` to be `https://github.com/rust-lang/crates.io-index` and translate a URL that matches the current index to be `null`.
>   * `cargo metadata` includes some extra fields, such as `source` and `path`.
> * The index includes additional fields such as `yanked`, `cksum`, and `v`.

[renamed]: specifying-dependencies.md#renaming-dependencies-in-cargotoml
[Publish API]: registry-web-api.md#publish
[`cargo metadata`]: ../commands/cargo-metadata.md

## Index Protocols
Cargo supports two remote registry protocols: `git` and `sparse`. The `git` protocol
stores index files in a git repository and the `sparse` protocol fetches individual
files over HTTP.

### Git Protocol
The git protocol has no protocol prefix in the index url. For example the git index URL
for [crates.io] is `https://github.com/rust-lang/crates.io-index`.

Cargo caches the git repository on disk so that it can efficiently incrementally fetch
updates.

### Sparse Protocol
The sparse protocol uses the `sparse+` protocol prefix in the registry URL. For example,
the sparse index URL for [crates.io] is `sparse+https://index.crates.io/`.

The sparse protocol downloads each index file using an individual HTTP request. Since
this results in a large number of small HTTP requests, performance is significantly
improved with a server that supports pipelining and HTTP/2.

#### Sparse authentication
Cargo will attempt to fetch the `config.json` file before
fetching any other files. If the server responds with an HTTP 401, then Cargo will assume
that the registry requires authentication and re-attempt the request for `config.json`
with the authentication token included.

On authentication failure (or a missing authentication token) the server may include a
`www-authenticate` header with a `Cargo login_url="<URL>"` challenge to indicate where the user
can go to get a token.

Registries that require authentication must set `auth-required: true` in `config.json`.

#### Caching
Cargo caches the crate metadata files, and captures the `ETag` or `Last-Modified`
HTTP header from the server for each entry. When refreshing crate metadata, Cargo
sends the `If-None-Match` or `If-Modified-Since` header to allow the server to respond
with HTTP 304 "Not Modified" if the local cache is valid, saving time and bandwidth.
If both `ETag` and `Last-Modified` headers are present, Cargo uses the `ETag` only.

#### Cache Invalidation
If a registry is using some kind of CDN or proxy which caches access to the index files,
then it is recommended that registries implement some form of cache invalidation when
the files are updated. If these caches are not updated, then users may not be able to
access new crates until the cache is cleared.

#### Nonexistent Crates
For crates that do not exist, the registry should respond with a 404 "Not Found", 410 "Gone"
or 451 "Unavailable For Legal Reasons" code.

#### Sparse Limitations
Since the URL of the registry is stored in the lockfile, it's not recommended to offer
a registry with both protocols. Discussion about a transition plan is ongoing in issue
[#10964]. The [crates.io] registry is an exception, since Cargo internally substitutes
the equivalent git URL when the sparse protocol is used.

If a registry does offer both protocols, it's currently recommended to choose one protocol
as the canonical protocol and use [source replacement] for the other protocol.


[`cargo publish`]: ../commands/cargo-publish.md
[alphanumeric]: ../../std/primitive.char.html#method.is_alphanumeric
[crates.io]: https://crates.io/
[source replacement]: ../reference/source-replacement.md
[#10964]: https://github.com/rust-lang/cargo/issues/10964


---

# Web API

A registry may host a web API at the location defined in `config.json` to
support any of the actions listed below.

Cargo includes the `Authorization` header for requests that require
authentication. The header value is the API token. The server should respond
with a 403 response code if the token is not valid. Users are expected to
visit the registry's website to obtain a token, and Cargo can store the token
using the [`cargo login`] command, or by passing the token on the
command-line.

Responses use a 2xx response code for success.
Errors should use an appropriate response code, such as 404.
Failure
responses should have a JSON object with the following structure:

```javascript
{
    // Array of errors to display to the user.
    "errors": [
        {
            // The error message as a string.
            "detail": "error message text"
        }
    ]
}
```

If the response has this structure Cargo will display the detailed message to the user, even if the response code is 200.
If the response code indicates an error and the content does not have this structure, Cargo will display to the user a
 message intended to help debugging the server error. A server returning an `errors` object allows a registry to provide a more
detailed or user-centric error message.

For backwards compatibility, servers should ignore any unexpected query
parameters or JSON fields. If a JSON field is missing, it should be assumed to
be null. The endpoints are versioned with the `v1` component of the path, and
Cargo is responsible for handling backwards compatibility fallbacks should any
be required in the future.

Cargo sets the `User-Agent` header for all requests to the Cargo version such
as `cargo/1.32.0 (8610973aa 2019-01-02)`. This may be modified by the user in
a configuration value. Added in 1.29.

Other headers vary by endpoint and are documented below.

## Publish

- Endpoint: `/api/v1/crates/new`
- Method: PUT
- Authorization: Included
- Headers:
    - `Content-Type`: `application/octet-stream`
    - `Accept`: `application/json`
- Body: Included (see below)

The publish endpoint is used to publish a new version of a crate. The server
should validate the crate, make it available for download, and add it to the
index.

It is not required for the index to be updated before the successful response is sent.
After a successful response, Cargo will poll the index for a short period of time to identify that the new crate has been added.
If the crate does not appear in the index after a short period of time, then Cargo will display a warning letting the user know that the new crate is not yet available.

The body of the data sent by Cargo is:

- 32-bit unsigned little-endian integer of the length of JSON data.
- Metadata of the package as a JSON object.
- 32-bit unsigned little-endian integer of the length of the `.crate` file.
- The `.crate` file.

The following is a commented example of the JSON object. Some notes of some
restrictions imposed by [crates.io] are included only to illustrate some
suggestions on types of validation that may be done, and should not be
considered as an exhaustive list of restrictions [crates.io] imposes.

```javascript
{
    // The name of the package.
    "name": "foo",
    // The version of the package being published.
    "vers": "0.1.0",
    // Array of direct dependencies of the package.
    "deps": [
        {
            // Name of the dependency.
            // If the dependency is renamed from the original package name,
            // this is the original name. The new package name is stored in
            // the `explicit_name_in_toml` field.
            "name": "rand",
            // The semver requirement for this dependency.
            "version_req": "^0.6",
            // Array of features (as strings) enabled for this dependency.
            "features": ["i128_support"],
            // Boolean of whether or not this is an optional dependency.
            "optional": false,
            // Boolean of whether or not default features are enabled.
            "default_features": true,
            // The target platform for the dependency.
            // null if not a target dependency.
            // Otherwise, a string such as "cfg(windows)".
            "target": null,
            // The dependency kind.
            // "dev", "build", or "normal".
            "kind": "normal",
            // The URL of the index of the registry where this dependency is
            // from as a string. If not specified or null, it is assumed the
            // dependency is in the current registry.
            "registry": null,
            // If the dependency is renamed, this is a string of the new
            // package name. If not specified or null, this dependency is not
            // renamed.
            "explicit_name_in_toml": null,
        }
    ],
    // Set of features defined for the package.
    // Each feature maps to an array of features or dependencies it enables.
    // Cargo does not impose limitations on feature names, but crates.io
    // requires alphanumeric ASCII, `_` or `-` characters.
    "features": {
        "extras": ["rand/simd_support"]
    },
    // List of strings of the authors.
    // May be empty.
    "authors": ["Alice <a@example.com>"],
    // Description field from the manifest.
    // May be null. crates.io requires at least some content.
    "description": null,
    // String of the URL to the website for this package's documentation.
    // May be null.
    "documentation": null,
    // String of the URL to the website for this package's home page.
    // May be null.
    "homepage": null,
    // String of the content of the README file.
    // May be null.
    "readme": null,
    // String of a relative path to a README file in the crate.
    // May be null.
    "readme_file": null,
    // Array of strings of keywords for the package.
    "keywords": [],
    // Array of strings of categories for the package.
    "categories": [],
    // String of the license for the package.
    // May be null. crates.io requires either `license` or `license_file` to be set.
    "license": null,
    // String of a relative path to a license file in the crate.
    // May be null.
    "license_file": null,
    // String of the URL to the website for the source repository of this package.
    // May be null.
    "repository": null,
    // Optional object of "status" badges. Each value is an object of
    // arbitrary string to string mappings.
    // crates.io has special interpretation of the format of the badges.
    "badges": {
        "travis-ci": {
            "branch": "master",
            "repository": "rust-lang/cargo"
        }
    },
    // The `links` string value from the package's manifest, or null if not
    // specified. This field is optional and defaults to null.
    "links": null,
    // The minimal supported Rust version (optional)
    // This must be a valid version requirement without an operator (e.g. no `=`)
    "rust_version": null
}
```

A successful response includes the JSON object:

```javascript
{
    // Optional object of warnings to display to the user.
    "warnings": {
        // Array of strings of categories that are invalid and ignored.
        "invalid_categories": [],
        // Array of strings of badge names that are invalid and ignored.
        "invalid_badges": [],
        // Array of strings of arbitrary warnings to display to the user.
        "other": []
    }
}
```

## Yank

- Endpoint: `/api/v1/crates/{crate_name}/{version}/yank`
- Method: DELETE
- Authorization: Included
- Headers:
    - `Accept`: `application/json`
- Body: None

The yank endpoint will set the `yank` field of the given version of a crate to
`true` in the index.

A successful response includes the JSON object:

```javascript
{
    // Indicates the yank succeeded, always true.
    "ok": true,
}
```

## Unyank

- Endpoint: `/api/v1/crates/{crate_name}/{version}/unyank`
- Method: PUT
- Authorization: Included
- Headers:
    - `Accept`: `application/json`
- Body: None

The unyank endpoint will set the `yank` field of the given version of a crate
to `false` in the index.

A successful response includes the JSON object:

```javascript
{
    // Indicates the unyank succeeded, always true.
    "ok": true,
}
```

## Owners

Cargo does not have an inherent notion of users and owners, but it does
provide the `owner` command to assist managing who has authorization to
control a crate. It is up to the registry to decide exactly how users and
owners are handled. See the [publishing documentation] for a description of
how [crates.io] handles owners via GitHub users and teams.

### Owners: List

- Endpoint: `/api/v1/crates/{crate_name}/owners`
- Method: GET
- Authorization: Included
- Headers:
    - `Accept`: `application/json`
- Body: None

The owners endpoint returns a list of owners of the crate.

A successful response includes the JSON object:

```javascript
{
    // Array of owners of the crate.
    "users": [
        {
            // Unique unsigned 32-bit integer of the owner.
            "id": 70,
            // The unique username of the owner.
            "login": "github:rust-lang:core",
            // Name of the owner.
            // This is optional and may be null.
            "name": "Core",
        }
    ]
}
```

### Owners: Add

- Endpoint: `/api/v1/crates/{crate_name}/owners`
- Method: PUT
- Authorization: Included
- Headers:
    - `Content-Type`: `application/json`
    - `Accept`: `application/json`
- Body: Included (see below)

A PUT request will send a request to the registry to add a new owner to a
crate. It is up to the registry how to handle the request. For example,
[crates.io] sends an invite to the user that they must accept before being
added.

The request should include the following JSON object:

```javascript
{
    // Array of `login` strings of owners to add.
    "users": ["login_name"]
}
```

A successful response includes the JSON object:

```javascript
{
    // Indicates the add succeeded, always true.
    "ok": true,
    // A string to be displayed to the user.
    "msg": "user ehuss has been invited to be an owner of crate cargo"
}
```

### Owners: Remove

- Endpoint: `/api/v1/crates/{crate_name}/owners`
- Method: DELETE
- Authorization: Included
- Headers:
    - `Content-Type`: `application/json`
    - `Accept`: `application/json`
- Body: Included (see below)

A DELETE request will remove an owner from a crate. The request should include
the following JSON object:

```javascript
{
    // Array of `login` strings of owners to remove.
    "users": ["login_name"]
}
```

A successful response includes the JSON object:

```javascript
{
    // Indicates the remove succeeded, always true.
    "ok": true
    // A string to be displayed to the user. Currently ignored by cargo.
    "msg": "owners successfully removed",
}
```

## Search

- Endpoint: `/api/v1/crates`
- Method: GET
- Authorization: Not Included
- Headers:
    - `Accept`: `application/json`
- Body: None
- Query Parameters:
    - `q`: The search query string.
    - `per_page`: Number of results, default 10, max 100.

The search request will perform a search for crates, using criteria defined on
the server.

A successful response includes the JSON object:

```javascript
{
    // Array of results.
    "crates": [
        {
            // Name of the crate.
            "name": "rand",
            // The highest version available.
            "max_version": "0.6.1",
            // Textual description of the crate.
            "description": "Random number generators and other randomness functionality.\n",
        }
    ],
    "meta": {
        // Total number of results available on the server.
        "total": 119
    }
}
```

## Login

- Endpoint: `/me`

The "login" endpoint is not an actual API request. It exists solely for the
[`cargo login`] command to display a URL to instruct a user to visit in a web
browser to log in and retrieve an API token.

[`cargo login`]: ../commands/cargo-login.md
[`cargo package`]: ../commands/cargo-package.md
[`cargo publish`]: ../commands/cargo-publish.md
[alphanumeric]: ../../std/primitive.char.html#method.is_alphanumeric
[config]: config.md
[crates.io]: https://crates.io/
[publishing documentation]: publishing.md#cargo-owner
