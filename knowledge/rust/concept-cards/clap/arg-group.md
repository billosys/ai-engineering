---
# === CORE IDENTIFICATION ===
concept: ArgGroup
slug: arg-group

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clap::ArgGroup"
  - "clap_builder::ArgGroup"
  - "argument group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arg
  - command
extends: []
related:
  - clap-validation
  - arg-matches
  - clap-builder-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ArgGroup in clap?"
  - "How do I make a set of arguments mutually exclusive?"
  - "How do I require at least one argument from a set?"
  - "How do I find out which argument in a group was used?"
  - "What is the difference between ArgGroup::required and ArgGroup::multiple?"
---

# Quick Definition

`ArgGroup` specifies a logical grouping of arguments for validation purposes -- ensuring that at most one (or at least one) argument from a set is present, and establishing conflict and requirement rules that apply to the group as a whole.

# Core Definition

The source documents `ArgGroup` as specifying "a logical group of arguments." You can use it for: "applying validation to an entire group, like `ArgGroup::multiple`; validate relationships between an argument and a group, like conflicts or requirements; check which argument in a group was specified on the command-line." The source explicitly distinguishes this from visual grouping: "For visually grouping arguments in help, see instead `Arg::help_heading`" (arg_group.rs, line 5).

An `ArgGroup` is added to a `Command` via `.group()`. By default, a group allows at most one of its member arguments to be present (`multiple(false)`). When `required(true)` is set, at least one member must be present. The combination of `required(true)` and the default `multiple(false)` enforces "exactly one" semantics.

# Prerequisites

- **arg** -- ArgGroup groups `Arg` instances by name; understanding Arg is required to use groups.
- **command** -- ArgGroups are added to a `Command` via `.group()`.

# Key Properties

1. Created with `ArgGroup::new(name)` where the name uniquely identifies the group
2. Arguments are added to the group via `.arg("name")` or `.args(["name1", "name2"])`
3. `multiple(false)` (the default) means at most one argument from the group can be used
4. `multiple(true)` allows any number of arguments from the group to be used
5. `required(true)` means at least one argument from the group must be present
6. The combination `required(true)` + `multiple(false)` enforces "exactly one" semantics
7. The group name can be used in `ArgMatches::contains_id()` to check if any group member was used
8. `ArgMatches::get_one::<Id>(group_name)` returns the name of which argument in the group was used
9. Groups support `.requires()`, `.requires_all()`, `.conflicts_with()`, and `.conflicts_with_all()` for inter-group and group-to-argument relationship rules
10. Group names can be referenced in other arguments' `.requires()` and `.conflicts_with()` calls

# Construction / Recognition

## To Create a Mutually Exclusive Group:
1. Define the individual arguments and add them to the command
2. Create `ArgGroup::new("group_name")`
3. Add argument names with `.args(["arg1", "arg2", "arg3"])`
4. Set `.required(true)` if at least one must be present
5. Add to the command with `Command::new("prog").group(group)`
6. The default `multiple(false)` ensures mutual exclusivity

## To Create an "At Least One" Group:
1. Follow the same steps but add `.multiple(true)`
2. This allows multiple arguments from the group to be used simultaneously
3. Combined with `.required(true)`, this means "one or more"

## To Check Which Group Member Was Used:
1. Use `matches.contains_id("group_name")` to test if any member was used
2. Use `matches.get_one::<Id>("group_name")` to get the ID of the specific argument used

# Context & Application

ArgGroup is clap's primary mechanism for expressing "choose one" and "at least one" constraints across arguments. It is especially useful for versioning workflows (e.g., choose either `--major`, `--minor`, `--patch`, or `--set-ver`) and mutually exclusive mode selection.

**Typical use cases:**
- **Mutually exclusive options**: Only one of several alternatives may be chosen (default behavior)
- **Required alternatives**: At least one of several options must be provided (`required(true)`)
- **Conditional requirements**: If any argument from the group is used, another argument must also be present (`.requires()`)
- **Group-level conflicts**: If any argument from the group is used, another argument must not be present (`.conflicts_with()`)

**Design note:** Groups operate on argument names (strings), not `Arg` references. This means the arguments must first be added to the `Command`; the group references them by name. The group itself is also identifiable by name in `ArgMatches`.

# Examples

**Example 1** (arg_group.rs, line 5): Mutually exclusive required group -- only one allowed:
```rust
use clap::{Command, arg, ArgGroup, error::ErrorKind};

let result = Command::new("cmd")
    .arg(arg!(--"set-ver" <ver> "set the version manually"))
    .arg(arg!(--major "auto increase major"))
    .arg(arg!(--minor "auto increase minor"))
    .arg(arg!(--patch "auto increase patch"))
    .group(ArgGroup::new("vers")
        .args(["set-ver", "major", "minor", "patch"])
        .required(true))
    .try_get_matches_from(vec!["cmd", "--major", "--patch"]);

// Two args from the group = error
assert!(result.is_err());
assert_eq!(result.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```

**Example 2** (arg_group.rs, line 5): Checking which group member was used:
```rust
use clap::{Command, arg, ArgGroup, Id};

let matches = Command::new("cmd")
    .arg(arg!(--"set-ver" <ver> "set the version manually"))
    .arg(arg!(--major "auto increase major"))
    .arg(arg!(--minor "auto increase minor"))
    .arg(arg!(--patch "auto increase patch"))
    .group(ArgGroup::new("vers")
        .args(["set-ver", "major", "minor", "patch"])
        .required(true))
    .try_get_matches_from(vec!["cmd", "--major"])
    .unwrap();

assert!(matches.contains_id("vers"));
assert_eq!(
    matches.get_one::<Id>("vers").expect("`vers` is required").as_str(),
    "major"
);
```

**Example 3** (arg_group.rs, line 419): Group with conflict rules:
```rust
use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};

let result = Command::new("myprog")
    .arg(Arg::new("flag").short('f').action(ArgAction::SetTrue))
    .arg(Arg::new("color").short('c').action(ArgAction::SetTrue))
    .arg(Arg::new("debug").short('d').action(ArgAction::SetTrue))
    .group(ArgGroup::new("req_flags")
        .args(["flag", "color"])
        .conflicts_with("debug"))
    .try_get_matches_from(vec!["myprog", "-c", "-d"]);

assert!(result.is_err());
assert_eq!(result.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```

# Relationships

## Builds Upon
- **arg** -- Groups reference `Arg` names
- **command** -- Groups are added to a `Command` via `.group()`

## Enables
- **clap-validation** -- Groups are a primary validation mechanism in clap

## Related
- **arg-matches** -- Group membership can be queried in `ArgMatches`
- **clap-builder-api** -- ArgGroup is part of the builder pattern API

## Contrasts With
- **arg** -- Individual argument definition vs. group-level validation

# Common Errors

- **Error**: Setting `required(true)` but forgetting that `multiple(false)` (the default) limits to exactly one argument.
  **Correction**: If you want "at least one, possibly more," also set `.multiple(true)`.

- **Error**: Adding group members by `Arg` reference instead of by name string.
  **Correction**: `ArgGroup::args()` takes string names, not `Arg` instances. Use the same name string passed to `Arg::new()`.

- **Error**: Using an ArgGroup for visual grouping in help output.
  **Correction**: ArgGroup is for validation only. For visual grouping in help, use `Arg::help_heading()`.

# Common Confusions

- **Confusion**: Believing `required(true)` alone means "exactly one."
  **Clarification**: `required(true)` means "at least one." Combined with the default `multiple(false)`, it becomes "exactly one" because the default already prevents more than one.

- **Confusion**: Thinking group conflicts are one-directional.
  **Clarification**: Like `Arg::conflicts_with`, group conflicts are bidirectional -- defining `group.conflicts_with("debug")` means using any group member AND `debug` is an error, regardless of which side defines the conflict.

- **Confusion**: Assuming the group name must match one of its member argument names.
  **Clarification**: The group name is an independent identifier. It can be anything unique, and it serves as its own ID in `ArgMatches`.

# Source Reference

Section 2: Arguments (Arg), from `clap_builder/src/builder/arg_group.rs`. Struct definition at line 5. Impl blocks: Builder (line 77), Reflection (line 516). Key methods: `new` (79), `arg` (112), `args` (146), `multiple` (195), `required` (267), `requires` (320), `conflicts_with` (419).

# Verification Notes

- Definition: Directly quoted from the struct-level documentation at line 5
- Mutual exclusivity: Demonstrated by the first example from source, which shows `ArgumentConflict` when two group members are used
- Group querying: The `get_one::<Id>` pattern is from the source's own example
- Visual grouping distinction: Explicitly stated in source ("For visually grouping arguments in help, see instead Arg::help_heading")
- Confidence: HIGH -- the struct is well-documented with clear examples covering all major use cases
- Cross-references: All slugs verified against planned extractions
