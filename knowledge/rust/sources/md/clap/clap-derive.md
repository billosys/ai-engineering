# Crate Documentation

**Version:** 4.5.49

**Format Version:** 55

# Module `clap_derive`

# `clap_derive`

Macro implementation for clap's derives.

[docs.rs](https://docs.rs/clap)
- [Derive Tutorial](https://docs.rs/clap/latest/clap/_derive/_tutorial/index.html)
- [Derive Reference](https://docs.rs/clap/latest/clap/_derive/index.html)

## License

Licensed under either of

* Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
* MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/license/mit>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual-licensed as above, without any additional terms or
conditions.

See [CONTRIBUTING](CONTRIBUTING.md) for more details.

## Macros

### Procedural Macro `ValueEnum`

**Attributes:**

- `Other("#[attr = ProcMacroDerive {trait_name: \"ValueEnum\", helper_attrs: [\"clap\",\n\"value\"]}]")`

Generates the `ValueEnum` impl.

```rust
pub #[proc_macro_derive]
// Helpers: #[clap], #[value]
pub fn ValueEnum(/* ... */) -> /* ... */ {
    /* ... */
}
```

### Procedural Macro `Parser`

**Attributes:**

- `Other("#[attr = ProcMacroDerive {trait_name: \"Parser\", helper_attrs: [\"clap\",\n\"structopt\", \"command\", \"arg\", \"group\"]}]")`

Generates the `Parser` implementation.

This is far less verbose than defining the `clap::Command` struct manually,
receiving an instance of `clap::ArgMatches` from conducting parsing, and then
implementing a conversion code to instantiate an instance of the user
context struct.

```rust
pub #[proc_macro_derive]
// Helpers: #[clap], #[structopt], #[command], #[arg], #[group]
pub fn Parser(/* ... */) -> /* ... */ {
    /* ... */
}
```

### Procedural Macro `Subcommand`

**Attributes:**

- `Other("#[attr = ProcMacroDerive {trait_name: \"Subcommand\", helper_attrs: [\"clap\",\n\"command\", \"arg\", \"group\"]}]")`

Generates the `Subcommand` impl.

```rust
pub #[proc_macro_derive]
// Helpers: #[clap], #[command], #[arg], #[group]
pub fn Subcommand(/* ... */) -> /* ... */ {
    /* ... */
}
```

### Procedural Macro `Args`

**Attributes:**

- `Other("#[attr = ProcMacroDerive {trait_name: \"Args\", helper_attrs: [\"clap\",\n\"command\", \"arg\", \"group\"]}]")`

Generates the `Args` impl.

```rust
pub #[proc_macro_derive]
// Helpers: #[clap], #[command], #[arg], #[group]
pub fn Args(/* ... */) -> /* ... */ {
    /* ... */
}
```

