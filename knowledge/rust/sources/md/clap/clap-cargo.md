# Crate Documentation

**Version:** 0.18.3

**Format Version:** 55

# Module `clap_cargo`

**clap-cargo**: Re-usable CLI flags for `cargo` plugins

## Examples

```rust,no_run
# #[cfg(feature = "clap")] {
# #[cfg(feature = "cargo_metadata")] {
use clap::Parser;

// ...
#[derive(Debug, Parser)]
#[command(styles = clap_cargo::style::CLAP_STYLING)]
struct Cli {
    #[command(flatten)]
    manifest: clap_cargo::Manifest,
    #[command(flatten)]
    workspace: clap_cargo::Workspace,
    #[command(flatten)]
    features: clap_cargo::Features,
}

let cli = // ...
# Cli::parse_from(["app"]);
let mut metadata = cli.manifest.metadata();
cli.features.forward_metadata(&mut metadata);
let metadata = metadata.exec().unwrap();
let (selected, excluded) = cli.workspace.partition_packages(&metadata);
# }
# }
```

## Relevant crates

Other crates that might be useful for cargo plugins:
* [escargot][escargot] for wrapping `cargo-build`, `carg-run`, `cargo-test`, etc.
* [cargo_metadata][cargo_metadata] for getting crate information.
* [clap-verbosity][clap-verbosity] for adding logging to your CLI.

[escargot]: https://crates.io/crates/escargot
[cargo_metadata]: https://crates.io/crates/cargo_metadata
[clap-verbosity]: https://crates.io/crates/clap-verbosity-flag

## Modules

## Module `style`

**Attributes:**

- `Other("#[allow(missing_docs)]")`
- `Other("#[allow(unused_qualifications)]")`
- `Other("#[allow(unreachable_pub)]")`

```rust
pub mod style { /* ... */ }
```

### Constants and Statics

#### Constant `NOP`

```rust
pub const NOP: anstyle::Style = _;
```

#### Constant `HEADER`

```rust
pub const HEADER: anstyle::Style = _;
```

#### Constant `USAGE`

```rust
pub const USAGE: anstyle::Style = _;
```

#### Constant `LITERAL`

```rust
pub const LITERAL: anstyle::Style = _;
```

#### Constant `PLACEHOLDER`

```rust
pub const PLACEHOLDER: anstyle::Style = _;
```

#### Constant `ERROR`

```rust
pub const ERROR: anstyle::Style = annotate_snippets::renderer::DEFAULT_ERROR_STYLE;
```

#### Constant `WARN`

```rust
pub const WARN: anstyle::Style = annotate_snippets::renderer::DEFAULT_WARNING_STYLE;
```

#### Constant `NOTE`

```rust
pub const NOTE: anstyle::Style = annotate_snippets::renderer::DEFAULT_NOTE_STYLE;
```

#### Constant `GOOD`

```rust
pub const GOOD: anstyle::Style = _;
```

#### Constant `VALID`

```rust
pub const VALID: anstyle::Style = _;
```

#### Constant `INVALID`

```rust
pub const INVALID: anstyle::Style = annotate_snippets::renderer::DEFAULT_WARNING_STYLE;
```

#### Constant `TRANSIENT`

```rust
pub const TRANSIENT: anstyle::Style = annotate_snippets::renderer::DEFAULT_HELP_STYLE;
```

#### Constant `CONTEXT`

```rust
pub const CONTEXT: anstyle::Style = annotate_snippets::renderer::DEFAULT_CONTEXT_STYLE;
```

#### Constant `UPDATE_ADDED`

```rust
pub const UPDATE_ADDED: anstyle::Style = NOTE;
```

#### Constant `UPDATE_REMOVED`

```rust
pub const UPDATE_REMOVED: anstyle::Style = ERROR;
```

#### Constant `UPDATE_UPGRADED`

```rust
pub const UPDATE_UPGRADED: anstyle::Style = GOOD;
```

#### Constant `UPDATE_DOWNGRADED`

```rust
pub const UPDATE_DOWNGRADED: anstyle::Style = WARN;
```

#### Constant `UPDATE_UNCHANGED`

```rust
pub const UPDATE_UNCHANGED: anstyle::Style = _;
```

#### Constant `DEP_NORMAL`

```rust
pub const DEP_NORMAL: anstyle::Style = _;
```

#### Constant `DEP_BUILD`

```rust
pub const DEP_BUILD: anstyle::Style = _;
```

#### Constant `DEP_DEV`

```rust
pub const DEP_DEV: anstyle::Style = _;
```

#### Constant `DEP_FEATURE`

```rust
pub const DEP_FEATURE: anstyle::Style = _;
```

#### Constant `CLAP_STYLING`

**Attributes:**

- `Other("#[<cfg>(feature = \"clap\")]")`

For use with
[`clap::Command::styles`](https://docs.rs/clap/latest/clap/struct.Command.html#method.styles)

```rust
pub const CLAP_STYLING: clap::builder::styling::Styles = _;
```

## Re-exports

### Re-export `features::*`

```rust
pub use features::*;
```

### Re-export `manifest::*`

```rust
pub use manifest::*;
```

### Re-export `workspace::*`

```rust
pub use workspace::*;
```

