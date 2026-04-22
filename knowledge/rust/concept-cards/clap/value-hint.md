---
concept: ValueHint
slug: value-hint
category: builder-api
subcategory: value-conversion
tier: intermediate
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Value Parsers"
extraction_confidence: high
aliases:
  - "ValueHint"
  - "value hint"
  - "Arg::value_hint"
  - "shell completion hint"
prerequisites:
  - arg
extends: []
related:
  - shell-completions
  - value-parser
  - possible-value
contrasts_with: []
answers_questions:
  - "How do I provide shell completion hints for clap arguments?"
  - "What ValueHint variants are available and which shells support them?"
  - "How do I tell the shell that an argument expects a file path or URL?"
---

# Quick Definition

`ValueHint` is an enum that provides shells with hints on how to complete an argument's value. Set via `Arg::value_hint`, it tells completion scripts whether an argument expects a file path, directory, URL, hostname, username, or other semantic type, enabling richer tab-completion behavior.

# Core Definition

`ValueHint` is an enum that "provide[s] shell with hint on how to complete an argument." It is set on an argument via `Arg::value_hint` and is used by the `clap_complete` crate for completion script generation. The enum provides semantic categories for argument values such as file paths, directories, executables, commands, usernames, hostnames, URLs, and email addresses. Shell support varies: zsh supports all hints, fish supports most (with caveats for positional arguments), and the dynamic completer supports path-related hints (Clap Documentation, Section 4: Value Parsers).

# Prerequisites

- **arg** — `ValueHint` is set on an `Arg` via `Arg::value_hint`; understanding argument definition is needed

# Key Properties

1. Set via `Arg::value_hint(ValueHint::FilePath)` — does not affect parsing, only completion
2. `AnyPath` — suggests any file system path (file or directory)
3. `FilePath` — suggests file paths only
4. `DirPath` — suggests directory paths only
5. `ExecutablePath` — suggests executable files
6. `CommandName` — suggests command names (from PATH)
7. `CommandString` — suggests command strings (command with potential arguments)
8. `CommandWithArguments` — suggests full commands with arguments
9. `Username` — suggests system usernames
10. `Hostname` — suggests hostnames
11. `Url` — suggests URLs
12. `EmailAddress` — suggests email addresses
13. Requires the `clap_complete` crate to generate completion scripts that use these hints

# Construction / Recognition

## To Set a ValueHint on an Argument

1. Import `ValueHint`: `use clap::builder::ValueHint;`
2. Chain on an `Arg`: `.value_hint(ValueHint::FilePath)`
3. Generate completion scripts using `clap_complete` to see the hints in action

## Shell Support Matrix

1. **zsh**: Supports all hint variants
2. **fish**: Supports `AnyPath`, `FilePath`, `DirPath`, `ExecutablePath` (partial), `CommandName`, `CommandString` (partial), `Username`, `Hostname`. Does not support `CommandWithArguments`, `Url`, `EmailAddress`. Only works for named arguments (e.g., `-o` or `--opt`), not positional arguments.
3. **dynamic completer**: Supports `AnyPath`, `FilePath`, `DirPath`, `ExecutablePath`

# Context & Application

`ValueHint` improves the user experience of CLI tools by enabling intelligent tab completion. Without hints, shells can only complete based on file listing or nothing at all. With hints, a `--config` argument can suggest only files, a `--host` argument can suggest known hostnames, and a `--user` argument can suggest system users.

**Typical contexts:**

- File path arguments: `--config`, `--input`, `--output` with `ValueHint::FilePath`
- Directory arguments: `--dir`, `--prefix` with `ValueHint::DirPath`
- URL arguments: `--url`, `--endpoint` with `ValueHint::Url`
- Hostname arguments: `--host`, `--server` with `ValueHint::Hostname`

**Important:** `ValueHint` is purely a completion-time hint. It does not validate or parse the argument value at runtime. Pair it with an appropriate `ValueParser` (e.g., `PathBufValueParser`) for runtime validation.

# Examples

**Example** (Section 4, ValueHint enum doc): The source provides the shell support matrix as its primary documentation. Typical usage pattern (synthesized from API context):

```rust
use clap::{Arg, builder::ValueHint};

Arg::new("config")
    .long("config")
    .value_hint(ValueHint::FilePath)
    .value_parser(clap::value_parser!(std::path::PathBuf))

Arg::new("host")
    .long("host")
    .value_hint(ValueHint::Hostname)
    .value_parser(clap::builder::NonEmptyStringValueParser::new())
```

# Relationships

## Builds Upon

- **arg** — `ValueHint` is set on an `Arg` as a property

## Enables

- (none directly)

## Related

- **shell-completions** — `ValueHint` feeds into completion script generation via `clap_complete`
- **value-parser** — `ValueHint` is orthogonal to `ValueParser`; hints affect completion, parsers affect validation
- **possible-value** — Both influence completion behavior: `PossibleValue` for enumerated choices, `ValueHint` for semantic categories

## Contrasts With

- (none)

# Common Errors

- **Error**: Setting `ValueHint::FilePath` and assuming it validates that the path exists.
  **Correction**: `ValueHint` only affects shell completions, not runtime validation. Pair with `PathBufValueParser` or a custom validator for runtime checks.

- **Error**: Using `ValueHint` on positional arguments and expecting fish completions to work.
  **Correction**: Fish completions currently only support `ValueHint` on named arguments (e.g., `-o` or `--opt`), not positional arguments.

# Common Confusions

- **Confusion**: Thinking `ValueHint` replaces `ValueParser` for argument type handling.
  **Clarification**: They serve different purposes. `ValueParser` handles runtime parsing and type conversion. `ValueHint` provides hints to shell completion systems. Both can (and often should) be used together on the same argument.

- **Confusion**: Assuming all shells support all hint variants equally.
  **Clarification**: Support varies significantly. Zsh supports all variants; fish has partial support and does not work with positional arguments; the dynamic completer only supports path-related hints.

# Source Reference

Section 4: Value Parsers, from `repos/clap/clap_builder/src/builder/value_hint.rs`, line 3. Covers the `ValueHint` enum definition with the complete shell support matrix.

# Verification Notes

- Enum variants and shell support table: Directly from the source documentation
- The fish positional argument limitation: Noted in the source as a footnote
- Confidence: HIGH — the source provides an explicit enum definition with a detailed support matrix
- Cross-references: `arg`, `shell-completions`, `value-parser`, `possible-value` are planned or extracted by other agents
- Uncertainties: Specific usage examples are synthesized from the API context, as the source provides only the enum definition and support table
