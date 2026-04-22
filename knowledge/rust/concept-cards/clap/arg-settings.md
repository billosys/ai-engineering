---
# === CORE IDENTIFICATION ===
concept: ArgSettings
slug: arg-settings

# === CLASSIFICATION ===
category: builder-api
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Arguments (Arg)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "clap::ArgSettings"
  - "clap_builder::ArgSettings"
  - "argument settings"
  - "per-argument settings"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arg
extends: []
related:
  - arg-action
  - arg-types
  - command-settings
  - clap-builder-api
contrasts_with:
  - command-settings

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ArgSettings in clap?"
  - "How do ArgSettings relate to the Arg builder methods?"
  - "What is the difference between ArgSettings and the Arg builder methods that accept bool?"
  - "How do I check if an ArgSettings flag is set on an argument?"
---

# Quick Definition

`ArgSettings` is an internal enum representing boolean configuration flags on an individual `Arg`. These settings are the underlying mechanism behind many `Arg` builder methods that accept a `bool` parameter, such as `.required(true)` or `.hide(true)`.

# Core Definition

The source documents `ArgSettings` as: "Various settings that apply to arguments and may be set, unset, and checked via getter/setter methods `Arg::setting`, `Arg::unset_setting`, and `Arg::is_set`. This is what the `Arg` methods which accept a `bool` use internally" (arg_settings.rs, line 34).

In practice, `ArgSettings` is a low-level API. Most users never interact with it directly because the `Arg` builder methods provide a higher-level interface to the same underlying flags. For example, calling `Arg::required(true)` internally sets the corresponding `ArgSettings` flag.

# Prerequisites

- **arg** -- ArgSettings are per-argument configuration flags applied to `Arg` instances.

# Key Properties

1. `ArgSettings` is an enum where each variant represents a boolean flag
2. Settings are set via `Arg::setting(ArgSettings::Variant)` and unset via `Arg::unset_setting(ArgSettings::Variant)`
3. Settings are checked via `Arg::is_set(ArgSettings::Variant)`
4. Most settings have a corresponding `Arg` builder method that is the preferred API (e.g., `Arg::required(true)` instead of `Arg::setting(ArgSettings::Required)`)
5. The settings cover concerns like: whether the argument is required, hidden, global, allows hyphen values, requires equals sign, etc.
6. This is an internal-facing API -- the builder methods on `Arg` are the idiomatic way to configure arguments

# Construction / Recognition

## To Use ArgSettings Directly (Low-Level):
1. Import `ArgSettings` from `clap`
2. Call `arg.setting(ArgSettings::Required)` to set a flag
3. Call `arg.unset_setting(ArgSettings::Required)` to clear a flag
4. Call `arg.is_set(ArgSettings::Required)` to check a flag

## To Use the Preferred Higher-Level API:
1. Call the corresponding builder method: `arg.required(true)` instead of `arg.setting(ArgSettings::Required)`
2. The builder methods are more readable, self-documenting, and provide the same functionality
3. The builder methods also return `Self` for chaining, making them composable in the builder pattern

## To Recognize ArgSettings in Code:
1. Look for `ArgSettings::` usage in `.setting()` or `.unset_setting()` calls
2. In most codebases, you will see the builder methods instead
3. ArgSettings may appear in lower-level code that programmatically inspects or modifies argument configuration

# Context & Application

`ArgSettings` provides the underlying bitflag mechanism for per-argument boolean configuration. While it exists as a public API, the clap documentation and examples consistently prefer the higher-level builder methods on `Arg`.

**When you might use ArgSettings directly:**
- Programmatically iterating over settings to inspect argument configuration
- Writing generic code that needs to check or toggle settings without knowing the specific builder method
- Interfacing with internal clap APIs or writing extensions

**The corresponding builder methods are preferred because:**
- They are self-documenting (`.required(true)` vs `.setting(ArgSettings::Required)`)
- They accept `bool` so the setting can be toggled dynamically
- They chain fluently in the builder pattern
- The clap documentation consistently uses them in examples

**Relationship to CommandSettings:** Just as `ArgSettings` controls per-argument flags, `AppSettings` (see `command-settings`) controls per-command flags. Both follow the same pattern of an internal enum behind higher-level builder methods.

# Examples

**Example 1** (arg_settings.rs, line 34): Low-level setting/checking:
```rust
use clap::{Arg, ArgSettings};

let arg = Arg::new("config")
    .setting(ArgSettings::Required);

assert!(arg.is_set(ArgSettings::Required));
```

**Example 2**: Preferred builder method equivalent:
```rust
use clap::Arg;

let arg = Arg::new("config")
    .required(true);
```

**Example 3**: Checking and unsetting:
```rust
use clap::{Arg, ArgSettings};

let mut arg = Arg::new("config").required(true);
assert!(arg.is_set(ArgSettings::Required));

arg = arg.unset_setting(ArgSettings::Required);
assert!(!arg.is_set(ArgSettings::Required));
```

# Relationships

## Builds Upon
- **arg** -- ArgSettings are configuration flags on `Arg` instances

## Related
- **arg-action** -- Some actions implicitly set certain argument settings
- **arg-types** -- Certain settings only apply to specific argument kinds (e.g., index settings for positionals)
- **command-settings** -- The command-level equivalent (`AppSettings`) follows the same pattern
- **clap-builder-api** -- ArgSettings is part of the builder API internals

## Contrasts With
- **command-settings** -- Per-command settings vs. per-argument settings

# Common Errors

- **Error**: Using `Arg::setting(ArgSettings::...)` when the builder method exists and is more readable.
  **Correction**: Prefer `.required(true)` over `.setting(ArgSettings::Required)`. The builder methods are the idiomatic API.

- **Error**: Expecting `ArgSettings` to cover all `Arg` configuration.
  **Correction**: ArgSettings only covers boolean flags. Configuration like `short`, `long`, `action`, `value_parser`, `num_args`, and `default_value` are not settings -- they are full builder methods with their own state.

# Common Confusions

- **Confusion**: Believing `ArgSettings` must be used to configure arguments.
  **Clarification**: Almost all users should use the builder methods on `Arg` (e.g., `.required(true)`, `.hide(true)`, `.global(true)`). `ArgSettings` is the internal representation that these methods use under the hood.

- **Confusion**: Thinking `ArgSettings` and `AppSettings` are interchangeable or combinable.
  **Clarification**: `ArgSettings` applies to individual `Arg` instances. `AppSettings` applies to `Command` instances. They are separate enums for separate scopes.

- **Confusion**: Assuming all `Arg` builder methods correspond to an `ArgSettings` variant.
  **Clarification**: Only the boolean-toggle methods (like `required`, `hide`, `global`, `allow_hyphen_values`) have `ArgSettings` counterparts. Methods like `action`, `value_parser`, `short`, `long` do not.

# Source Reference

Section 2: Arguments (Arg), from `clap_builder/src/builder/arg_settings.rs`. Enum definition at line 34. The enum references `Arg::setting`, `Arg::unset_setting`, and `Arg::is_set` as the getter/setter methods.

# Verification Notes

- Definition: Directly quoted from the enum-level documentation at line 34
- Builder method relationship: Explicitly stated in source as "This is what the Arg methods which accept a bool use internally"
- Variant details: The source provides the enum definition but the individual variants are sparse in documentation in the extracted section; the key insight is the relationship to builder methods
- Confidence: MEDIUM -- the enum is briefly documented and its role is clear, but the individual variant documentation was limited in the extracted section; the concept is primarily useful as context for understanding the Arg builder API
- Cross-references: All slugs verified against planned extractions
