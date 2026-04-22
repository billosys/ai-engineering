---
# === CORE IDENTIFICATION ===
concept: Cargo Registries
slug: cargo-registries

# === CLASSIFICATION ===
category: build-system
subcategory: package-distribution
tier: advanced

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "12-registries"
chapter_number: 12
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "crate registry"
  - "crates.io"
  - "alternative registry"
  - "private registry"
  - "registry index"
  - "registry web API"
  - "sparse registry"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-build-cache
  - cargo-home
extends: []
related:
  - cargo-external-tools
  - cargo-publishing
  - cargo-dependencies
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure and use an alternative registry?"
  - "How do I publish a crate to a private registry?"
  - "What is the difference between git and sparse registry protocols?"
  - "How does registry authentication work in Cargo?"
  - "What credential providers does Cargo support?"
  - "What is the registry index format?"
  - "How are crate files organized in the registry index?"
  - "What is the registry Web API and what endpoints does it expose?"
  - "How do I restrict which registries a package can be published to?"
  - "How do I run my own registry?"
---

# Quick Definition

Cargo registries are servers that host crate packages and their metadata. The default registry is crates.io. Registries consist of an index (searchable metadata for all crates) and optionally a web API for publishing. Cargo supports two index protocols: `git` (clones the entire index repository) and `sparse` (fetches individual metadata files over HTTP). Authentication uses configurable credential providers that can store tokens in OS keychains, plain text files, or custom backends. The registry web API exposes endpoints for publishing, yanking, owner management, and search.

# Core Definition

The source states: "Cargo installs crates and fetches dependencies from a 'registry'. The default registry is crates.io. A registry contains an 'index' which contains a searchable list of available crates. A registry may also provide a web API to support publishing new crates directly from Cargo." (Ch. 12).

Alternative registries are configured in `.cargo/config.toml` under the `[registries]` table with an index URL. Dependencies from alternate registries use the `registry` key in `Cargo.toml`. The `sparse+` URL prefix selects the sparse protocol; otherwise the git protocol is used.

For authentication, the source states: "Using alternative registries with authentication requires a credential provider to be configured to avoid unknowingly storing unencrypted credentials on disk." Cargo includes built-in providers (`cargo:token`, `cargo:wincred`, `cargo:macos-keychain`, `cargo:libsecret`, `cargo:token-from-stdout`) and supports external credential plugins via a JSON-based stdin/stdout protocol.

The index format stores one file per package, organized in a tiered directory structure (1-char names in `1/`, 2-char in `2/`, 3-char in `3/{first-char}/`, 4+ chars in `{first-two}/{second-two}/`). Each line in a package file is a JSON object describing one published version.

# Prerequisites

- **Cargo Build Cache** -- understanding where downloaded and compiled crate artifacts are stored
- **Cargo Home** -- registry data (index, cache, sources) is stored in the Cargo home directory

# Key Properties

1. **Default registry**: crates.io; configurable via `registry.default` in config
2. **Alternative registry config**: `[registries.my-registry] = { index = "..." }` in `.cargo/config.toml`
3. **Two protocols**: `git` (clones full index repo) and `sparse` (individual HTTP requests, `sparse+` prefix)
4. **Sparse protocol advantages**: Saves significant time and bandwidth by only downloading relevant metadata
5. **Publishing restriction**: `package.publish` in `Cargo.toml` can restrict which registries are allowed
6. **crates.io restriction**: crates.io does not accept packages that depend on crates from other registries
7. **Credential providers**: Ordered list in `registry.global-credential-providers`; later entries have higher precedence
8. **Built-in providers**: `cargo:token` (plain text), `cargo:wincred`, `cargo:macos-keychain`, `cargo:libsecret`, `cargo:token-from-stdout`
9. **Credential plugin protocol**: JSON messages over stdin/stdout with version negotiation, login/get/logout operations
10. **Index directory structure**: Tiered by package name length (1/, 2/, 3/x/, ab/cd/)
11. **Index JSON per version**: Each line is a JSON object with name, version, deps, checksum, features, yanked status
12. **Schema versioning**: `v` field in index entries (v1 for base, v2 for `features2` with `dep:` and `pkg?/feat` syntax)
13. **Web API endpoints**: Publish (`PUT /api/v1/crates/new`), Yank (`DELETE .../{version}/yank`), Unyank, Owners (list/add/remove), Search (`GET /api/v1/crates`)

# Construction / Recognition

## Configuring an Alternative Registry:
```toml
# .cargo/config.toml
[registries]
my-registry = { index = "sparse+https://my-intranet:8080/index/" }
```

## Using a Dependency from an Alternative Registry:
```toml
# Cargo.toml
[dependencies]
other-crate = { version = "1.0", registry = "my-registry" }
```

## Publishing to an Alternative Registry:
```bash
cargo login --registry=my-registry
cargo publish --registry=my-registry
```

## Restricting Publishing Targets:
```toml
# Cargo.toml
[package]
publish = ["my-registry"]   # only allow publishing to my-registry
# publish = false            # prevent all publishing
```

## Recommended Credential Provider Configuration:
```toml
# ~/.cargo/config.toml
[registry]
global-credential-providers = ["cargo:token", "cargo:libsecret",
                                "cargo:macos-keychain", "cargo:wincred"]
```

## Index Directory Structure:
```
index/
├── config.json              # dl URL, api URL, auth-required
├── 1/                       # 1-char package names
├── 2/                       # 2-char package names
├── 3/
│   └── s/                   # 3-char: 3/{first-char}/
│       └── syn              # one JSON line per version
├── ca/
│   └── rg/
│       └── cargo            # 4+ char: {first-two}/{second-two}/
└── se/
    └── rd/
        └── serde
```

# Context & Application

The registry system is the backbone of Rust's package ecosystem. The sparse protocol (stabilized and now default for crates.io) was a major improvement over the git protocol, which required cloning the entire index (hundreds of megabytes for crates.io). For organizations running private registries, the chapter provides comprehensive implementation guidance covering the index format, authentication flow, and web API contract. The credential provider system balances security (OS keychain integration) with flexibility (custom plugins, environment variables). A minimal registry needs only a git repo for the index and a file server for `.crate` files; a full-featured registry additionally implements the web API for publishing. The index format's careful versioning (the `v` field and `features2` separation) demonstrates backward compatibility design, allowing older Cargo versions to work with newer index entries.

# Examples

**Example 1** (Ch. 12): Sparse vs git protocol selection:
> "If the registry index URL starts with `sparse+`, Cargo uses the sparse protocol. Otherwise Cargo uses the `git` protocol."
> "Since Cargo only downloads the metadata for relevant crates, the sparse protocol can save significant time and bandwidth."

**Example 2** (Ch. 12): Index config.json for crates.io:
```javascript
{"dl": "https://crates.io/api/v1/crates", "api": "https://crates.io"}
```
The `dl` key supports markers: `{crate}`, `{version}`, `{prefix}`, `{lowerprefix}`, `{sha256-checksum}`.

**Example 3** (Ch. 12): Publish API body format:
> "32-bit unsigned little-endian integer of the length of JSON data. Metadata of the package as a JSON object. 32-bit unsigned little-endian integer of the length of the `.crate` file. The `.crate` file."

**Example 4** (Ch. 12): Credential provider communication flow:
> 1. Cargo spawns the credential process
> 2. Provider sends hello: `{"v": [1]}`
> 3. Cargo sends request: `{"v": 1, "kind": "get", "operation": "read", "registry": {...}}`
> 4. Provider responds: `{"token": "...", "cache": "session", "operation_independent": true}`
> 5. Cargo closes stdin; provider exits

**Example 5** (Ch. 12): Sparse protocol caching:
> "Cargo caches the crate metadata files, and captures the `ETag` or `Last-Modified` HTTP header from the server for each entry."
> Cargo sends `If-None-Match` or `If-Modified-Since` headers to allow HTTP 304 responses.

**Example 6** (Ch. 12): Running a minimal registry:
> "A minimal registry can be implemented by having a git repository that contains an index, and a server that contains the compressed `.crate` files created by `cargo package`. Users won't be able to use Cargo to publish to it, but this may be sufficient for closed environments."

# Relationships

## Builds Upon
- **Cargo Build Cache** -- downloaded crates are compiled and stored in the build cache
- **Cargo Home** -- registry index, cache, and source data are stored in `$CARGO_HOME/registry/`

## Enables
- The entire crate distribution and dependency resolution ecosystem
- Private/enterprise package hosting with alternative registries
- Secure credential management for registry access

## Related
- **cargo-external-tools** -- `cargo metadata` and JSON messages reference registry-based Package IDs
- **cargo-publishing** -- the guide-level view of publishing workflow
- **cargo-dependencies** -- dependency specs can include `registry` keys for alternative sources

## Contrasts With
- None within this source

# Common Errors

- **Error**: Publishing a crate to crates.io that depends on crates from another registry.
  **Correction**: "crates.io does not accept packages that depend on crates from other registries."

- **Error**: Using an authenticated registry without configuring a credential provider.
  **Correction**: "Using alternative registries with authentication requires a credential provider to be configured to avoid unknowingly storing unencrypted credentials on disk."

- **Error**: Assuming the index JSON format is identical to the Publish API JSON.
  **Correction**: There are subtle differences: the index uses `name` for the aliased name and `package` for the original; the Publish API uses `name` for the original and `explicit_name_in_toml` for the alias. The version requirement field is `req` in the index but `version_req` in the Publish API.

- **Error**: Creating index entries with duplicate versions differing only in build metadata.
  **Correction**: "Indexes must ensure that each version only appears once for each package. This includes ignoring SemVer build metadata." Versions `1.0.7` and `1.0.7+extra` are considered duplicates.

# Common Confusions

- **Confusion**: Thinking the sparse protocol always requires a special server.
  **Clarification**: The sparse protocol uses plain HTTP requests. Any HTTP server serving static files (with proper directory structure) can work. Performance improves with HTTP/2 and pipelining support.

- **Confusion**: Thinking index filenames are case-sensitive.
  **Clarification**: "The index filenames are in lowercase" but "the fields that contain package names in Cargo.toml and the index JSON data are case-sensitive and may contain upper and lower case characters."

- **Confusion**: Thinking `registry` value of `null` means the same thing in the index and in `cargo metadata`.
  **Clarification**: In the index, `null` means "same registry as this index." In `cargo metadata`, `null` means crates.io. When generating index entries, translate accordingly.

- **Confusion**: Thinking the index must be updated before the publish response is sent.
  **Clarification**: "It is not required for the index to be updated before the successful response is sent." Cargo polls the index briefly after publishing and warns if the crate does not appear.

# Source Reference

Chapter 12: Registries -- sections "Using an Alternate Registry," "Publishing to an Alternate Registry," "Registry Protocols," "Registry Authentication," "Credential Provider Protocol," "Running a Registry," "Index Format" (configuration, download endpoint, index files, JSON schema, index protocols), and "Web API" (publish, yank, unyank, owners, search, login). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 12 -- "Cargo installs crates and fetches dependencies from a 'registry'"
- Confidence rationale: HIGH -- the source provides exhaustive documentation of all registry components including JSON schemas, protocol details, and API specifications
- Uncertainties: Third-party registry implementations may vary in their adherence to the spec; the sparse protocol limitation regarding dual-protocol registries is noted as an ongoing discussion (#10964)
- Cross-reference status: All slugs reference cards within this extraction set or related extraction sets
