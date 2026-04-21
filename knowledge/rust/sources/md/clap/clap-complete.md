# Crate Documentation

**Version:** 4.5.65

**Format Version:** 55

# Module `clap_complete`

## Quick Start

- For generating at compile-time, see [`generate_to`]
- For generating at runtime, see [`generate`]

[`Shell`] is a convenience `enum` for an argument value type that implements `Generator`
for each natively-supported shell type.

## Example

```rust,no_run
use clap::{Command, Arg, ValueHint, value_parser, ArgAction};
use clap_complete::aot::{generate, Generator, Shell};
use std::io;

fn build_cli() -> Command {
    Command::new("example")
        .arg(Arg::new("file")
            .help("some input file")
            .value_hint(ValueHint::AnyPath))
        .arg(Arg::new("generator")
            .long("generate")
            .action(ArgAction::Set)
            .value_parser(value_parser!(Shell)))
}

fn print_completions<G: Generator>(generator: G, cmd: &mut Command) {
    generate(generator, cmd, cmd.get_name().to_string(), &mut io::stdout());
}

fn main() {
    let matches = build_cli().get_matches();

    if let Some(generator) = matches.get_one::<Shell>("generator").copied() {
        let mut cmd = build_cli();
        eprintln!("Generating completion file for {generator}...");
        print_completions(generator, &mut cmd);
    }
}
```
<!-- omit in TOC -->
# clap_complete

> **Shell completion generation for `clap`**

[![Crates.io](https://img.shields.io/crates/v/clap_complete?style=flat-square)](https://crates.io/crates/clap_complete)
[![Crates.io](https://img.shields.io/crates/d/clap_complete?style=flat-square)](https://crates.io/crates/clap_complete)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)](https://github.com/clap-rs/clap/blob/clap_complete-v4.5.65/LICENSE-APACHE)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/clap-rs/clap/blob/clap_complete-v4.5.65/LICENSE-MIT)

Dual-licensed under [Apache 2.0](LICENSE-APACHE) or [MIT](LICENSE-MIT).

1. [About](#about)
2. [API Reference](https://docs.rs/clap_complete)
3. [Questions & Discussions](https://github.com/clap-rs/clap/discussions)
4. [CONTRIBUTING](https://github.com/clap-rs/clap/blob/clap_complete-v4.5.65/clap_complete/CONTRIBUTING.md)
5. [Sponsors](https://github.com/clap-rs/clap/blob/clap_complete-v4.5.65/README.md#sponsors)

## About

### Related Projects

- [clap_complete_nushell](https://crates.io/crates/clap_complete_nushell) for [nushell](https://www.nushell.sh/) shell completion support

## Modules

## Module `aot`

Prebuilt completions

## Quick Start

- For generating at compile-time, see [`generate_to`]
- For generating at runtime, see [`generate`]

[`Shell`] is a convenience `enum` for an argument value type that implements `Generator`
for each natively-supported shell type.

To customize completions, see

- [`ValueHint`]
- [`ValueEnum`][clap::ValueEnum]

## Example

```rust,no_run
use clap::{Command, Arg, ValueHint, value_parser, ArgAction};
use clap_complete::{generate, Generator, Shell};
use std::io;

fn build_cli() -> Command {
    Command::new("example")
         .arg(Arg::new("file")
             .help("some input file")
                .value_hint(ValueHint::AnyPath),
        )
       .arg(
           Arg::new("generator")
               .long("generate")
               .action(ArgAction::Set)
               .value_parser(value_parser!(Shell)),
       )
}

fn print_completions<G: Generator>(generator: G, cmd: &mut Command) {
    generate(generator, cmd, cmd.get_name().to_string(), &mut io::stdout());
}

fn main() {
    let matches = build_cli().get_matches();

    if let Some(generator) = matches.get_one::<Shell>("generator").copied() {
        let mut cmd = build_cli();
        eprintln!("Generating completion file for {generator}...");
        print_completions(generator, &mut cmd);
    }
}
```

```rust
pub mod aot { /* ... */ }
```

### Re-exports

#### Re-export `ValueHint`

```rust
pub use clap::ValueHint;
```

#### Re-export `generator::*`

```rust
pub use generator::*;
```

#### Re-export `shells::*`

```rust
pub use shells::*;
```

## Module `generator`

Deprecated, see [`aot`]

```rust
pub mod generator { /* ... */ }
```

### Re-exports

#### Re-export `generate`

```rust
pub use crate::aot::generate;
```

#### Re-export `generate_to`

```rust
pub use crate::aot::generate_to;
```

#### Re-export `utils`

```rust
pub use crate::aot::utils;
```

#### Re-export `Generator`

```rust
pub use crate::aot::Generator;
```

## Module `shells`

Deprecated, see [`aot`]

```rust
pub mod shells { /* ... */ }
```

### Re-exports

#### Re-export `Bash`

```rust
pub use crate::aot::Bash;
```

#### Re-export `Elvish`

```rust
pub use crate::aot::Elvish;
```

#### Re-export `Fish`

```rust
pub use crate::aot::Fish;
```

#### Re-export `PowerShell`

```rust
pub use crate::aot::PowerShell;
```

#### Re-export `Shell`

```rust
pub use crate::aot::Shell;
```

#### Re-export `Zsh`

```rust
pub use crate::aot::Zsh;
```

## Re-exports

### Re-export `ValueHint`

```rust
pub use clap::ValueHint;
```

### Re-export `generate`

Deprecated, see [`aot::generate`]

```rust
pub use aot::generate;
```

### Re-export `generate_to`

Deprecated, see [`aot::generate_to`]

```rust
pub use aot::generate_to;
```

### Re-export `Generator`

Deprecated, see [`aot::Generator`]

```rust
pub use aot::Generator;
```

### Re-export `Shell`

Deprecated, see [`aot::Shell`]

```rust
pub use aot::Shell;
```
