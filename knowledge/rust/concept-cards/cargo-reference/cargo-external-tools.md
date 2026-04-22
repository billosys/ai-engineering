---
# === CORE IDENTIFICATION ===
concept: Cargo External Tools
slug: cargo-external-tools

# === CLASSIFICATION ===
category: build-system
subcategory: tooling-integration
tier: advanced

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "11-external-tools"
chapter_number: 11
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "custom subcommands"
  - "cargo subcommand"
  - "JSON messages"
  - "cargo message format"
  - "cargo metadata"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-build-cache
extends: []
related:
  - cargo-registries
  - cargo-build-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a custom Cargo subcommand?"
  - "What JSON messages does Cargo emit during a build?"
  - "How do I parse Cargo's structured build output?"
  - "What is the format of compiler-message, compiler-artifact, and build-script-executed messages?"
  - "How do I integrate Cargo with an IDE or external build system?"
  - "What information does cargo metadata provide?"
  - "How does Cargo resolve custom subcommand names?"
  - "How do custom subcommands receive arguments?"
---

# Quick Definition

Cargo supports integration with external tools through three facilities: `cargo metadata` for querying package structure and dependencies as JSON, `--message-format=json` for receiving structured compiler messages, artifact notifications, and build script output during a build, and custom subcommands where `cargo foo` automatically invokes an executable named `cargo-foo` found on `$PATH`. These mechanisms enable IDEs, build systems, and third-party tools to work with Cargo programmatically.

# Core Definition

The source states: "One of the goals of Cargo is simple integration with third-party tools, like IDEs and other build systems. To make integration easier, Cargo has several facilities." (Ch. 11). These facilities are:

1. **`cargo metadata`**: Outputs package structure and dependency information in JSON. "The format is stable and versioned. When calling `cargo metadata`, you should pass `--format-version` flag explicitly to avoid forward incompatibility hazard."

2. **`--message-format=json`**: Emits JSON objects (one per line) during builds, including compiler errors/warnings, produced artifacts, and build script results. The `reason` field distinguishes message types: `compiler-message`, `compiler-artifact`, `build-script-executed`, and `build-finished`.

3. **Custom subcommands**: "Cargo is designed to be extensible with new subcommands without having to modify Cargo itself. This is achieved by translating a cargo invocation of the form cargo `(?<command>[^ ]+)` into an invocation of an external tool `cargo-${command}`."

# Prerequisites

- **Cargo Build Cache** -- understanding where build artifacts are produced for interpreting artifact messages

# Key Properties

1. **cargo metadata is stable and versioned**: Always pass `--format-version` to avoid forward incompatibility
2. **cargo_metadata crate**: Rust library for parsing both `cargo metadata` and `--message-format=json` output
3. **JSON one-per-line format**: Each line is a complete JSON object; the `reason` field identifies the message type
4. **compiler-message**: Contains the rustc diagnostic with package ID, manifest path, and target info
5. **compiler-artifact**: Includes profile settings, enabled features, generated filenames, executable path, and `fresh` flag
6. **build-script-executed**: Contains parsed build script output (linked libs, paths, cfgs, env vars, out_dir)
7. **build-finished**: Signals end of Cargo's JSON output; `success` boolean indicates build result
8. **Custom subcommand resolution**: Executables named `cargo-${command}` in `$PATH` directories
9. **$CARGO_HOME/bin priority**: Cargo defaults to prioritizing `$CARGO_HOME/bin` over `$PATH`
10. **Subcommand arguments**: First argument is the filename, second is the subcommand name, then user arguments
11. **Help integration**: `cargo help foo` invokes `cargo-foo foo --help`
12. **CARGO environment variable**: Custom subcommands can use `$CARGO` to call back to Cargo

# Construction / Recognition

## JSON Message Types During Build:
```javascript
// compiler-message: compiler diagnostics
{"reason": "compiler-message", "package_id": "file:///path#0.1.0",
 "manifest_path": "/path/Cargo.toml", "target": {...}, "message": {...}}

// compiler-artifact: compiled output
{"reason": "compiler-artifact", "package_id": "file:///path#0.1.0",
 "profile": {"opt_level": "0", "debuginfo": 2, ...},
 "features": ["feat1"], "filenames": ["/path/libfoo.rlib"],
 "executable": null, "fresh": true}

// build-script-executed: build.rs output
{"reason": "build-script-executed", "package_id": "file:///path#0.1.0",
 "linked_libs": ["foo", "static=bar"],
 "linked_paths": ["/some/path"], "cfgs": ["cfg1"],
 "env": [["KEY", "value"]], "out_dir": "/path/in/target"}

// build-finished: end of build
{"reason": "build-finished", "success": true}
```

## Custom Subcommand Pattern:
```bash
# Installing a custom subcommand
cargo install cargo-expand

# Cargo translates "cargo expand" into invoking "cargo-expand"
cargo expand

# Help integration
cargo help expand  # invokes: cargo-expand expand --help
```

# Context & Application

The JSON message interface is essential for IDE integration (rust-analyzer, IntelliJ Rust) and CI tooling. The `compiler-artifact` message is particularly useful because it provides the exact paths of generated files, enabling downstream tools to locate binaries, libraries, and other outputs without guessing. The `fresh` field indicates whether a compilation step was actually executed or used cached results, which is valuable for build performance analysis. The `build-finished` message is important for tools that need to distinguish Cargo's JSON output from subsequent program output (e.g., from `cargo run`). Custom subcommands power the Cargo plugin ecosystem (cargo-edit, cargo-expand, cargo-watch, cargo-clippy, etc.) and the source encourages using the CLI interface rather than linking to Cargo as a library since "Cargo as a library is unstable."

# Examples

**Example 1** (Ch. 11): Querying package metadata safely:
> "The format is stable and versioned. When calling `cargo metadata`, you should pass `--format-version` flag explicitly to avoid forward incompatibility hazard."

**Example 2** (Ch. 11): Limitation of `--message-format=json`:
> "`--message-format=json` only controls Cargo and Rustc's output. This cannot control the output of other tools, e.g. `cargo run --message-format=json`, or arbitrary output from procedural macros."
> "A possible workaround in these situations is to only interpret a line as JSON if it starts with `{`."

**Example 3** (Ch. 11): Build-finished message purpose:
> "This message lets a tool know that Cargo will not produce additional JSON messages, but there may be additional output that may be generated afterwards (such as the output generated by the program executed by `cargo run`)."

**Example 4** (Ch. 11): Why not to link Cargo as a library:
> "Cargo as a library is unstable: the API may change without deprecation" and "versions of the linked Cargo library may be different from the Cargo binary."
> "Instead, it is encouraged to use the CLI interface to drive Cargo."

**Example 5** (Ch. 11): Custom subcommand argument passing:
> "When Cargo invokes a custom subcommand, the first argument to the subcommand will be the filename of the custom subcommand, as usual. The second argument will be the subcommand name itself."

# Relationships

## Builds Upon
- **Cargo Build Cache** -- artifact messages reference paths within the target directory structure

## Enables
- IDE integration with structured compiler output
- CI pipeline tooling with machine-readable build results
- The Cargo plugin ecosystem through custom subcommands

## Related
- **cargo-registries** -- Package IDs in JSON messages can reference registry URLs
- **cargo-build-performance** -- the `fresh` field in artifact messages indicates cache hits

## Contrasts With
- None within this source

# Common Errors

- **Error**: Not passing `--format-version` to `cargo metadata`.
  **Correction**: "You should pass `--format-version` flag explicitly to avoid forward incompatibility hazard."

- **Error**: Expecting `--message-format=json` to capture output from `cargo run` or proc macros.
  **Correction**: "This cannot control the output of other tools." Use the `build-finished` message to know when Cargo's JSON output ends.

- **Error**: Expecting custom subcommand to receive only user-provided arguments.
  **Correction**: The first argument is the executable filename and the second is the subcommand name. User arguments start from the third position.

- **Error**: Linking to the `cargo` crate as a library for stable integration.
  **Correction**: "Cargo as a library is unstable: the API may change without deprecation." Use the CLI interface and `cargo metadata` instead.

# Common Confusions

- **Confusion**: Thinking JSON messages are emitted on stderr.
  **Clarification**: "The output goes to stdout in the JSON object per line format." Compiler diagnostics that would normally go to stderr are wrapped in JSON on stdout when using `--message-format=json`.

- **Confusion**: Thinking `package_id` has always been a Package ID Specification.
  **Clarification**: "MSRV: 1.77 is required for `package_id` to be a Package ID Specification. Before that, it was opaque."

- **Confusion**: Thinking custom subcommands must be installed with `cargo install`.
  **Clarification**: Any executable named `cargo-${command}` in `$PATH` will work. It can be a shell script, Python script, or any other executable.

- **Confusion**: Thinking `$PATH` takes priority over `$CARGO_HOME/bin` for subcommands.
  **Clarification**: "Cargo defaults to prioritizing external tools in `$CARGO_HOME/bin` over `$PATH`. Users can override this precedence by adding `$CARGO_HOME/bin` to `$PATH`."

# Source Reference

Chapter 11: External Tools -- sections "Information about package structure," "JSON messages" (compiler messages, artifact messages, build script output, build finished), and "Custom subcommands." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 11 -- "One of the goals of Cargo is simple integration with third-party tools, like IDEs and other build systems"
- Confidence rationale: HIGH -- the source provides complete JSON schemas for all message types and clear documentation of the subcommand mechanism
- Uncertainties: "There is experimental nightly-only support for JSON output for tests" which may change the message format
- Cross-reference status: All slugs reference cards within this extraction set or related extraction sets
