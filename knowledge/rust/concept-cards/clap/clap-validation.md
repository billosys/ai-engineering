---
concept: Clap Validation
slug: clap-validation
category: builder-api
subcategory: argument-constraints
tier: intermediate

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Validation"

extraction_confidence: high

aliases:
  - "argument validation"
  - "clap constraints"
  - "argument conflicts"
  - "conditional requirements"

prerequisites:
  - arg
  - command
  - clap-builder-api

extends:
  - arg-group

related:
  - clap-error-handling
  - value-parser
  - arg-action

contrasts_with: []

answers_questions:
  - "How do I make two clap arguments mutually exclusive?"
  - "How do I require one argument when another is present?"
  - "How do I express conditional argument requirements in clap?"
  - "What validation constraints does clap provide for arguments?"
---

## Quick Definition

Clap validation encompasses the set of declarative constraints on arguments -- conflicts, requirements, conditional requirements, and exclusivity -- that clap checks automatically during parsing, producing structured errors when constraints are violated.

## Core Definition

Clap provides a comprehensive set of validation methods on `Arg` that express inter-argument constraints declaratively. These include `conflicts_with` / `conflicts_with_all` for mutual exclusion, `requires` / `requires_if` / `requires_ifs` for conditional presence requirements, `required_unless_present` / `required_unless_present_all` / `required_unless_present_any` for fallback requirements, `required_if_eq` / `required_if_eq_any` / `required_if_eq_all` for value-conditional requirements, and `exclusive` for arguments that must appear alone. Conflicting rules take precedence over being required by default, and conflict definitions are two-way (defining `A.conflicts_with(B)` is sufficient without also defining `B.conflicts_with(A)`). All arguments implicitly conflict with themselves (Section 8 and Arg methods in clap_builder).

## Prerequisites

- **Arg** -- Validation constraints are methods on the `Arg` type; you must understand argument definition to use them
- **Command** -- Validation operates during `Command` parsing; the `Command::error` method enables custom post-parsing validation
- **Builder API** -- Validation methods use the builder pattern, chaining constraint calls onto `Arg` definitions

## Key Properties

1. `conflicts_with(name)` makes two arguments mutually exclusive; presence of both yields `ErrorKind::ArgumentConflict`
2. `conflicts_with_all(names)` extends conflict to multiple arguments at once
3. `exclusive(true)` makes an argument conflict with every other argument
4. `requires(name)` demands another argument be present when this argument is used
5. `requires_if(val, name)` conditionally requires another argument only when this argument has a specific value
6. `required_unless_present(name)` makes this argument required unless the named argument is present
7. `required_if_eq(name, val)` makes this argument required when another argument has a specific value
8. Conflict rules are two-way: only one side needs to declare the conflict
9. Conflicting rules take precedence over `required` settings
10. The `ignore_case` setting affects value comparisons in conditional requirements like `required_if_eq`

## Construction / Recognition

### To Add Mutual Exclusion Between Arguments

1. Choose which argument to define the conflict on (only one side is needed)
2. Call `.conflicts_with("other_arg_name")` on the `Arg` builder
3. For multiple conflicts, use `.conflicts_with_all(["arg_a", "arg_b"])`
4. For total exclusivity, use `.exclusive(true)` instead

### To Add Conditional Requirements

1. Use `.requires("other")` to require `other` whenever this arg is present
2. Use `.requires_if("value", "other")` to require `other` only when this arg equals `"value"`
3. Use `.required_unless_present("fallback")` to make this arg required unless `fallback` is present
4. Use `.required_if_eq("trigger", "value")` to make this arg required when `trigger` equals `"value"`

## Context & Application

Argument validation is critical for building robust CLIs with complex inter-argument relationships. Common patterns include mutually exclusive flags (e.g., `--verbose` vs `--quiet`), option dependencies (e.g., `--output` requires `--format`), and conditional requirements (e.g., `--password` required unless `--token` is present). Clap's declarative validation produces user-friendly error messages automatically, including suggestions, without requiring manual post-parsing checks. For validation that cannot be expressed declaratively, `Command::error` provides custom post-parsing validation that integrates with clap's error formatting.

## Examples

**Example 1** (Arg conflicts_with, Section 8): Mutual exclusion between `--config` and `--debug`:
```rust
let res = Command::new("prog")
    .arg(Arg::new("cfg")
        .action(ArgAction::Set)
        .conflicts_with("debug")
        .long("config"))
    .arg(Arg::new("debug")
        .long("debug")
        .action(ArgAction::SetTrue))
    .try_get_matches_from(vec!["prog", "--debug", "--config", "file.conf"]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```

**Example 2** (Arg requires): `--config` requires `input` to be present:
```rust
let res = Command::new("prog")
    .arg(Arg::new("cfg")
        .action(ArgAction::Set)
        .requires("input")
        .long("config"))
    .arg(Arg::new("input"))
    .try_get_matches_from(vec!["prog", "--config", "file.conf"]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```

**Example 3** (Arg exclusive): An exclusive argument that conflicts with all others:
```rust
let res = Command::new("prog")
    .arg(Arg::new("exclusive")
        .action(ArgAction::Set)
        .exclusive(true)
        .long("exclusive"))
    .arg(Arg::new("debug").long("debug"))
    .arg(Arg::new("input"))
    .try_get_matches_from(vec!["prog", "--exclusive", "file.conf", "file.txt"]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```

## Relationships

### Builds Upon

- **Arg** -- All validation methods are defined on the `Arg` type
- **Command** -- `Command::error` enables custom post-parsing validation

### Enables

- **clap-error-handling** -- Validation failures produce structured `Error` values with specific `ErrorKind` variants

### Related

- **ArgGroup** -- Groups provide collective validation (require one of several args, conflict as a group)
- **ValueParser** -- Value-level validation (type checking, range checking) complements argument-level validation

### Contrasts With

- **ValueParser** -- ValueParser validates individual values; argument validation validates inter-argument relationships

## Common Errors

- **Error**: Defining conflicts on both sides (both `A.conflicts_with(B)` and `B.conflicts_with(A)`)
  **Correction**: Only one side needs the conflict definition; it is automatically two-way

- **Error**: Expecting `required(true)` to override `conflicts_with`
  **Correction**: Conflicting rules take precedence over required settings

- **Error**: Using `requires` when meaning `required_if_eq` (always requiring vs. conditionally requiring)
  **Correction**: `requires` always requires the other arg when this arg is present; `required_if_eq` makes *this* arg required when *another* arg has a specific value

## Common Confusions

- **Confusion**: Believing `conflicts_with` only works in one direction
  **Clarification**: Conflict rules are automatically two-way; defining on one side is sufficient

- **Confusion**: Confusing `requires` with `required_unless_present` -- they have opposite semantics
  **Clarification**: `requires("B")` on A means "if A is present, B must also be present." `required_unless_present("B")` on A means "A is required unless B is present"

- **Confusion**: Thinking `exclusive(true)` is the same as `conflicts_with_all` with all other args listed
  **Clarification**: While functionally similar, `exclusive(true)` is simpler and automatically covers all present and future arguments

## Source Reference

Clap Documentation, Section 8: "Validation" (clap-source-docs). Primary content from `repos/clap/clap_builder/src/builder/arg.rs` methods: `required`, `requires`, `exclusive`, `conflicts_with`, `conflicts_with_all`, `required_unless_present`, `required_unless_present_all`, `required_if_eq`, `required_if_eq_any`, `required_if_eq_all`, `requires_if`, `requires_ifs`. Additional content from `Command::error` for custom post-parsing validation.

## Verification Notes

- Definition: Synthesized from multiple Arg method documentation entries in the source
- Key Properties: All items directly documented in source method docs
- Examples: Directly from source code examples in Arg method documentation
- Confidence: HIGH -- extensive explicit documentation with numerous code examples for every validation method
- Cross-references: `arg`, `command`, `clap-builder-api`, `arg-group` verified against other agents' planned extractions
- Uncertainties: Section 8 header content is sparse (mainly styling functions); the actual validation methods are documented in the Arg section but are categorized under validation concepts
