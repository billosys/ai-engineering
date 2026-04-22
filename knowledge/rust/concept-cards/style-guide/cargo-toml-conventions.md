---
# === CORE IDENTIFICATION ===
concept: Cargo.toml Conventions
slug: cargo-toml-conventions

# === CLASSIFICATION ===
category: style
subcategory: cargo
tier: intermediate

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Cargo.toml Conventions"
chapter_number: 6
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo.toml formatting"
  - "Cargo.toml style"
  - "Cargo manifest conventions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-style-guide
extends:
  - formatting-conventions
related:
  - naming-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I format my Cargo.toml file?"
  - "What order should sections appear in Cargo.toml?"
  - "How should I order keys within the [package] section?"
  - "Should I quote key names in Cargo.toml?"
  - "How should I format dependency tables in Cargo.toml?"
  - "What format should the authors list use in Cargo.toml?"
  - "How should I write the license field in Cargo.toml?"
  - "How should arrays and tables be formatted in Cargo.toml?"
---

# Quick Definition

The Rust Style Guide defines formatting and metadata conventions for `Cargo.toml` files: use the same line width (100 chars) and indentation (4 spaces) as Rust code, version-sort keys within sections, put `[package]` first with `name` and `version` at the top, use bare key names, and follow specific rules for arrays, tables, and metadata fields like `authors`, `license`, and `description`.

# Core Definition

The `Cargo.toml` conventions extend the Rust formatting rules to the project manifest file (Ch. 6: Cargo.toml Conventions).

**Formatting conventions**: "Use the same line width and indentation as Rust code" -- meaning 100-character lines and 4-space indentation. Key formatting rules include:

- "Put a blank line between the last key-value pair in a section and the header of the next section. Do not place a blank line between section headers and the key-value pairs in that section, or between key-value pairs in a section."
- "Version-sort key names within each section, with the exception of the `[package]` section."
- For `[package]`: "Put the `[package]` section at the top of the file; put the `name` and `version` keys in that order at the top of that section, followed by the remaining keys other than `description` in order, followed by the `description` at the end of that section."
- "Don't use quotes around any standard key names; use bare keys."
- "Put a single space both before and after the `=` between a key and value."

For arrays: "put the entire list on the same line as the key, if it fits. Otherwise, use block indentation" with trailing commas, matching the Rust code style.

For tables: "write the entire table using curly braces and commas on the same line as the key if it fits. If the entire table does not fit on the same line as the key, separate it out into a separate section with key-value pairs."

**Metadata conventions**: The guide specifies standards for specific fields:
- **authors**: "strings that each contain an author name followed by an email address in angle brackets: `Full Name <email@address>`"
- **license**: "must contain a valid SPDX expression" (with `/` permitted in place of ` OR ` by convention)
- **homepage**: "must consist of a single URL, including the scheme"
- **description**: "wrap text at 80 columns. Don't start the description field with the name of the crate"; first sentence on its own line summarizing the crate

# Prerequisites

- **rust-style-guide** -- understanding the overall style guide context

# Key Properties

1. **Same line width and indentation as code**: 100 characters, 4 spaces
2. **[package] section first**: Always at the top of the file
3. **name and version first in [package]**: These two keys lead, in that order
4. **description last in [package]**: Placed at the end of the `[package]` section
5. **Version-sorted keys**: All sections except `[package]` have keys sorted by version-sort
6. **Bare key names**: No quotes around standard TOML key names
7. **Single space around `=`**: `key = "value"`, not `key="value"` or `key =  "value"`
8. **Blank lines between sections only**: Blank line before the next section header, but not within a section
9. **Inline tables for short dependencies**: `crate1 = { path = "crate1", version = "1.2.3" }`
10. **Separate sections for long dependencies**: Use `[dependencies.long_name]` with key-value pairs on separate lines
11. **SPDX license expressions**: Valid SPDX names required (e.g., `MIT`, `Apache-2.0`, `MIT/Apache-2.0`)
12. **Author format**: `Full Name <email@address>` -- no bare emails or names without emails

# Construction / Recognition

## Formatting a [package] Section:
1. Place `[package]` as the first section in the file
2. Put `name` first, then `version`
3. Add remaining keys (edition, authors, license, etc.) in version-sorted order
4. Place `description` last in the section
5. Leave a blank line before the next section header

## Formatting Dependencies:
1. For short dependencies: use inline table syntax on one line
2. For long dependencies: break into a separate `[dependencies.crate_name]` section
3. Version-sort dependency names within the `[dependencies]` section

## Formatting Arrays:
1. If the array fits on one line: `features = ["feature1", "feature2"]`
2. If it doesn't fit: use block indent with trailing commas and closing bracket on its own line

## Writing Metadata:
1. Authors: `authors = ["Full Name <email@address>"]`
2. License: `license = "MIT"` or `license = "MIT/Apache-2.0"`
3. Homepage: `homepage = "https://example.org/"` (include scheme)
4. Description: wrap at 80 columns, don't start with the crate name, first sentence summarizes

# Context & Application

These conventions ensure that `Cargo.toml` files across the Rust ecosystem are consistently formatted and contain well-structured metadata. The formatting rules align with the same principles as Rust code formatting -- consistent indentation, predictable ordering, and clean diffs. The metadata conventions ensure that crate information on crates.io is professional and useful: valid SPDX licenses enable automated license checking, properly formatted author lists enable attribution, and well-written descriptions help users find and evaluate crates.

# Examples

**Example 1** (Ch. 6): Block-indented array for features:
```toml
some_feature = [
    "another_feature",
    "yet_another_feature",
    "some_dependency?/some_feature",
]
```

**Example 2** (Ch. 6): Inline table vs. separate section for dependencies:
```toml
[dependencies]
crate1 = { path = "crate1", version = "1.2.3" }

[dependencies.extremely_long_crate_name_goes_here]
path = "extremely_long_path_name_goes_right_here"
version = "4.5.6"
```

**Example 3**: Well-formatted [package] section following all conventions:
```toml
[package]
name = "my-awesome-crate"
version = "0.1.0"
authors = ["Jane Doe <jane@example.com>"]
edition = "2024"
license = "MIT/Apache-2.0"
homepage = "https://example.org/my-awesome-crate/"
repository = "https://github.com/example/my-awesome-crate"
description = """
A fast and ergonomic library for parsing configuration files.
Supports TOML, YAML, and JSON formats with a unified API.
"""

[dependencies]
serde = { version = "1.0", features = ["derive"] }
toml = "0.8"
```

**Example 4**: Author format rules:
```toml
# Correct
authors = ["Full Name <email@address>"]
authors = ["Alice Smith <alice@example.com>", "Bob Jones <bob@example.com>"]

# Wrong: bare email
# authors = ["alice@example.com"]

# Wrong: name without email
# authors = ["Alice Smith"]
```

# Relationships

## Builds Upon
- **rust-style-guide** -- Cargo.toml conventions are part of the overall style guide
- **formatting-conventions** -- inherits line width (100 chars), indentation (4 spaces), and block indent rules

## Enables
- Consistent, professional crate metadata across the Rust ecosystem
- Automated tooling for Cargo.toml formatting

## Related
- **naming-conventions** -- naming principles apply to crate names and feature names

## Contrasts With
- None within this source

# Common Errors

- **Error**: Placing `description` in the middle of the `[package]` section.
  **Correction**: The `description` field should be the last key in the `[package]` section, after all other keys.

- **Error**: Quoting standard key names like `"name"` or `"version"`.
  **Correction**: Use bare keys for standard TOML key names. Only use quoted keys for non-standard key names that require quoting.

- **Error**: Using a non-SPDX license identifier like `"BSD"` instead of `"BSD-3-Clause"`.
  **Correction**: The license field must contain a valid SPDX expression. Use the exact SPDX identifier (e.g., `"MIT"`, `"Apache-2.0"`, `"BSD-3-Clause"`).

- **Error**: Putting blank lines between key-value pairs within the same section.
  **Correction**: "Do not place a blank line between section headers and the key-value pairs in that section, or between key-value pairs in a section." Blank lines go only between sections.

# Common Confusions

- **Confusion**: Thinking `[package]` keys should be alphabetically sorted like other sections.
  **Clarification**: The `[package]` section has a special ordering: `name` first, `version` second, remaining keys in version-sorted order, and `description` last. Other sections use standard version-sorting.

- **Confusion**: Thinking inline table syntax is always preferred over separate sections.
  **Clarification**: Inline tables are for dependencies that fit on one line. When the table is too long, break it into a separate section with `[dependencies.crate_name]`. The choice is based on line length, not preference.

- **Confusion**: Thinking the `/` in license expressions (e.g., `MIT/Apache-2.0`) is non-standard.
  **Clarification**: While SPDX uses ` OR `, the Rust ecosystem accepts `/` as a conventional shorthand by "widespread convention." Both forms are acceptable.

# Source Reference

Chapter 6: Cargo.toml Conventions -- sections on "Formatting conventions" and "Metadata conventions." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 6 with key rules quoted verbatim
- Metadata rules: Directly from Ch. 6 "Metadata conventions" section for authors, license, homepage, and description
- Confidence rationale: HIGH -- the source provides explicit, unambiguous rules
- Uncertainties: The guide does not cover all possible Cargo.toml sections (e.g., `[profile]`, `[workspace]`)
- Cross-reference status: rust-style-guide, formatting-conventions, naming-conventions are in this extraction set
