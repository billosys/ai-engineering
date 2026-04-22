---
# === CORE IDENTIFICATION ===
concept: Rustdoc Command-Line Arguments
slug: rustdoc-cli

# === CLASSIFICATION ===
category: documentation
subcategory: tool-configuration
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "Command-line arguments"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustdoc flags"
  - "rustdoc options"
  - "rustdoc command-line flags"
  - "cargo doc options"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustdoc
extends: []
related:
  - rustdoc-lints
  - doc-tests
  - rustdoc-advanced-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What command-line arguments does rustdoc accept?"
  - "How do I generate documentation for private items?"
  - "How do I set the output directory for rustdoc?"
  - "How do I control the crate name in generated documentation?"
  - "How do I run documentation tests with rustdoc?"
  - "How do I add custom CSS or HTML to rustdoc output?"
  - "How do I set the Rust edition for rustdoc and doctests?"
  - "How do I add a custom theme to rustdoc output?"
  - "How do I specify the target triple for documentation?"
  - "How do I pass configuration flags to rustdoc?"
---

# Quick Definition

Rustdoc accepts a comprehensive set of command-line arguments to control documentation generation, including output location, crate metadata, private item visibility, edition selection, documentation testing, custom theming, HTML injection, and cross-compilation targeting. Many of these flags mirror `rustc` options since rustdoc performs partial compilation.

# Core Definition

The `rustdoc` command-line interface provides stable flags for controlling every aspect of documentation generation. The flags fall into several categories: (1) output control (`-o`/`--out-dir`, `--crate-name`, `--crate-version`), (2) visibility (`--document-private-items`), (3) compilation context (`-L`, `--extern`, `--cfg`, `--check-cfg`, `-C`/`--codegen`, `--sysroot`, `--edition`, `--target`), (4) testing (`--test`, `--test-args`, `--test-run-directory`, `--test-runtool`), (5) HTML/CSS customization (`--html-in-header`, `--html-before-content`, `--html-after-content`, `--extend-css`, `--theme`, `--check-theme`, `--default-theme`), and (6) Markdown rendering (`--markdown-css`, `--markdown-playground-url`, `--markdown-no-toc`). Some flags are deprecated: `--passes`, `--no-defaults`, and `-r`/`--input-format`.

As noted in Ch. 2: "Some of `rustdoc`'s flags are unstable; this page only shows stable options, `--help` will show them all."

# Prerequisites

- **rustdoc** -- Understanding what rustdoc is and its basic usage

# Key Properties

1. **Output control**: `-o`/`--out-dir` sets the output directory (default: `doc/`); `--crate-name` overrides the inferred crate name; `--crate-version` adds a version string to the sidebar
2. **Private items**: `--document-private-items` includes all non-public items (shown with a lock icon) except `#[doc(hidden)]` items
3. **Edition**: `--edition` controls both how source code is parsed and how doctests are compiled (default: 2015)
4. **Test execution**: `--test` runs code examples as tests; `--test-args` passes options to the test runner; `--test-runtool` specifies a wrapper program (e.g., valgrind)
5. **HTML injection**: `--html-in-header`, `--html-before-content`, and `--html-after-content` insert custom HTML at specific points in the rendered output
6. **Theming**: `--theme` adds custom CSS themes (name derived from filename); `--check-theme` verifies a theme implements the same CSS rules as the built-in `light` theme; `--default-theme` sets the initial theme
7. **Cross-compilation**: `--target` generates documentation for a different target triple, subject to the same cross-compilation constraints as `rustc`
8. **Stdin input**: Specifying `-` as the input reads source code from standard input
9. **Response files**: `@path` loads command-line options from a file (one per line, UTF-8 encoded)

# Construction / Recognition

## Common Invocation Patterns:

```bash
# Basic documentation generation
$ rustdoc src/lib.rs --crate-name mycrate -o target/doc

# Document private items
$ rustdoc src/lib.rs --document-private-items

# Run documentation tests
$ rustdoc src/lib.rs --test
$ rustdoc src/lib.rs --test --test-args ignored

# Run doctests under valgrind
$ rustdoc src/lib.rs --test-runtool valgrind

# Set edition and target
$ rustdoc src/lib.rs --edition 2021 --target x86_64-pc-windows-gnu

# Add custom theme and HTML
$ rustdoc src/lib.rs --theme /path/to/custom.css --html-in-header header.html

# Verify custom theme compatibility
$ rustdoc --check-theme /path/to/custom.css

# Render standalone Markdown with playground links
$ rustdoc README.md --markdown-playground-url https://play.rust-lang.org/

# Pass configuration flags
$ rustdoc src/lib.rs --cfg feature="foo"
$ rustdoc src/lib.rs --check-cfg='cfg(my_cfg, values("foo", "bar"))'
```

# Context & Application

Most Rust developers interact with rustdoc through `cargo doc`, which sets many of these flags automatically (crate name, output path, library paths, edition). Direct use of rustdoc flags is relevant when customizing documentation builds, running doctests in special environments (emulators, valgrind), adding custom branding via HTML/CSS injection, cross-compiling documentation for different targets, or building documentation pipelines in CI. The `--document-private-items` flag is particularly useful for internal documentation of libraries where maintainers need to see all items.

# Examples

**Example 1** (Ch. 2): Documenting private items:
```rust
pub fn public() {} // documented
mod private {      // not documented by default
    pub fn unreachable() {} // not documented by default
}
```
Running `rustdoc src/lib.rs --document-private-items` includes all non-public items with a lock icon.

**Example 2** (Ch. 2): Adding a custom theme:
```bash
$ rustdoc src/lib.rs --theme /path/to/your/custom-theme.css
```
> "The theme's name is determined by its filename; a theme file named `custom-theme.css` will add a theme named `custom-theme` to the documentation."

**Example 3** (Ch. 2): Running doctests with a wrapper program:
```bash
$ rustdoc src/lib.rs --test-runtool path/to/runner \
    --test-runtool-arg --do-thing \
    --test-runtool-arg --do-other-thing
```
The wrapper receives the runtool args followed by the path to the doctest executable.

**Example 4** (Ch. 2): Verbose version output:
```text
$ rustdoc --verbose --version
rustdoc 1.17.0 (56124baa9 2017-04-24)
binary: rustdoc
commit-hash: hash
commit-date: date
host: host-tuple
release: 1.17.0
LLVM version: 3.9
```

**Example 5** (Ch. 2): Reading options from a response file:
> "If you specify `@path` on the command-line, then it will open `path` and read command line options from it. These options are one per line; a blank line indicates an empty option."

# Relationships

## Builds Upon
- **rustdoc** -- these flags control rustdoc's behavior

## Enables
- **doc-tests** -- `--test`, `--test-args`, and `--test-runtool` control documentation test execution
- **rustdoc-advanced-features** -- some advanced features are activated via command-line flags

## Related
- **rustdoc-lints** -- lints complement CLI flags for documentation quality control
- **rustdoc-advanced-features** -- `#[cfg(doc)]` interacts with `--cfg` and `--target` flags

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting `--crate-name` when invoking rustdoc directly, resulting in the crate being named after the source file (e.g., "lib").
  **Correction**: Always pass `--crate-name mycrate` when calling `rustdoc` directly. `cargo doc` handles this automatically.

- **Error**: Using `--check-theme` alongside other flags expecting normal documentation output.
  **Correction**: "`--check-theme` is a separate mode in `rustdoc`. When `rustdoc` sees the `--check-theme` flag, it discards all other flags and only performs the CSS rule comparison operation."

- **Error**: Passing `--markdown-css` when generating documentation from Rust source files.
  **Correction**: "When rendering Rust files, this flag is ignored." Use `--extend-css` or `--theme` instead for Rust source documentation.

# Common Confusions

- **Confusion**: Thinking `--default-theme` permanently changes the theme for all users.
  **Clarification**: It only sets the initial theme for users whose browsers have not remembered a previous selection from the on-page theme picker. The set of available themes is not stable across rustdoc versions.

- **Confusion**: Conflating `-L`/`--library-path` with `--extern`.
  **Clarification**: `--library-path` provides directories to search for dependencies. `--extern` specifies the exact location of a specific named dependency. The former is a search path; the latter is a precise mapping.

- **Confusion**: Thinking `--edition` only affects source parsing.
  **Clarification**: The `--edition` flag controls both how the source code is interpreted and how doctests are compiled. As with `rustc`, the default edition is 2015.

# Source Reference

Chapter 2: Command-line arguments -- all stable flags documented in full. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 2 -- each flag documented with usage examples
- Confidence rationale: HIGH -- every flag has explicit documentation with examples
- Uncertainties: The chapter notes that some unstable flags exist but are not documented here
- Cross-reference status: rustdoc, rustdoc-lints, rustdoc-advanced-features are in this extraction set; doc-tests from Agent B
