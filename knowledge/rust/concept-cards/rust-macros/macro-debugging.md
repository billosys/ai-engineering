---
concept: Macro Debugging
slug: macro-debugging
category: macro-system
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Debugging"
extraction_confidence: high
aliases:
  - "trace_macros!"
  - "log_syntax!"
  - "--pretty expanded"
  - "macro debugging tools"
prerequisites:
  - macro-rules
  - macro-expansion
extends: []
related:
  - macro-matcher
  - metavariable
  - macro-repetition
contrasts_with: []
answers_questions:
  - "How do you debug macros in Rust?"
  - "What is trace_macros!?"
  - "What is log_syntax!?"
  - "How do you see the expanded output of a macro?"
  - "How do you debug recursive macros?"
---

# Quick Definition

Rust provides three primary tools for debugging macros: `trace_macros!` (dumps every macro invocation before expansion), `log_syntax!` (outputs tokens passed to it at compile time), and `--pretty expanded` (shows the fully expanded source code). The first two require the nightly compiler.

# Core Definition

The `rustc` compiler provides several tools for debugging macros:

**`trace_macros!`** is a compiler directive that instructs it to dump every macro invocation prior to expansion. It can be turned on and off to trace only specific sections of code:
- `trace_macros!(true);` enables tracing
- `trace_macros!(false);` disables tracing
- Can also be enabled from the command line with `-Z trace-macros`
- Requires nightly compiler (`#![feature(trace_macros)]`)

**`log_syntax!`** causes the compiler to output all tokens passed to it at compile time. It provides more targeted debugging than `trace_macros!`:
- Requires nightly compiler (`#![feature(log_syntax)]`)
- Useful for seeing exactly what tokens are present at a specific point in expansion

**`--pretty expanded`** shows the fully expanded source code after all macros have been processed:
- Invoked with `rustc -Z unstable-options --pretty expanded file.rs`
- Shows what the compiler actually compiles after expansion
- Available options can be listed with `rustc -Z unstable-options --help -v`

# Prerequisites

- **macro-rules** -- These tools debug `macro_rules!` definitions
- **macro-expansion** -- Understanding expansion is necessary to interpret debugging output

# Key Properties

1. **`trace_macros!`**: Shows every macro invocation with its arguments before expansion.
2. **`log_syntax!`**: Outputs tokens at compile time; more targeted than `trace_macros!`.
3. **`--pretty expanded`**: Shows the fully expanded source code.
4. **Nightly required**: `trace_macros!` and `log_syntax!` require the nightly compiler.
5. **Toggleable**: `trace_macros!` can be turned on and off to trace only specific code regions.
6. **Invaluable for recursion**: `trace_macros!` is particularly useful for debugging deeply recursive macros.

# Construction / Recognition

## Using `trace_macros!`

```rust
#![feature(trace_macros)]

macro_rules! each_tt {
    () => {};
    ($_tt:tt $($rest:tt)*) => { each_tt!($($rest)*); };
}

each_tt!(foo bar baz quux);
trace_macros!(true);
each_tt!(spim wak plee whum);
trace_macros!(false);
each_tt!(trom qlip winp xod);
```

Output:
```text
each_tt! { spim wak plee whum }
each_tt! { wak plee whum }
each_tt! { plee whum }
each_tt! { whum }
each_tt! {  }
```

Only the middle invocation is traced; the first and third are outside the trace region.

## Using `log_syntax!`

```rust
#![feature(log_syntax)]

macro_rules! sing {
    () => {};
    ($tt:tt $($rest:tt)*) => { log_syntax!($tt); sing!($($rest)*); };
}

sing! {
    ^ < @ < . @ *
    '\x08' '{' '"' _ # ' '
    - @ '$' && / _ %
    ! ( '\t' @ | = >
    ; '\x08' '\'' + '$' ? '\x7f'
    , # '"' ~ | ) '\x07'
}
```

Each token is output individually at compile time.

## Using `--pretty expanded`

Given:
```rust
macro_rules! S {
    ($e:expr) => { String::from($e) };
}

fn main() {
    let world = S!("World");
    println!("Hello, {}!", world);
}
```

Compile with:
```shell
rustc -Z unstable-options --pretty expanded hello.rs
```

Output shows `S!("World")` expanded to `String::from("World")` and `println!` expanded to its full `::std::io::_print(...)` implementation.

# Context & Application

Debugging macros can be notoriously difficult because the code you write is not the code the compiler sees. These three tools address different debugging needs:

- **`trace_macros!`** is best for understanding recursive macro behavior -- you can see each step of the recursion with its arguments. This is "particularly invaluable when debugging deeply recursive macros."
- **`log_syntax!`** is best for targeted inspection of specific tokens at specific points during expansion.
- **`--pretty expanded`** is best for seeing the final result of all macro expansion, useful when the expanded code itself causes compiler errors.

In practice, a common debugging workflow is:
1. Use `trace_macros!` to verify the macro is being invoked with the expected arguments at each step
2. Use `log_syntax!` to inspect specific captures or intermediate values
3. Use `--pretty expanded` to see the final expanded code and diagnose type errors or other issues in the expansion

# Examples

**`trace_macros!` for recursive macro** (from "Debugging" section):

```rust
#![feature(trace_macros)]

macro_rules! each_tt {
    () => {};
    ($_tt:tt $($rest:tt)*) => { each_tt!($($rest)*); };
}

trace_macros!(true);
each_tt!(spim wak plee whum);
trace_macros!(false);
```

Output shows each recursive step:
```text
each_tt! { spim wak plee whum }
each_tt! { wak plee whum }
each_tt! { plee whum }
each_tt! { whum }
each_tt! {  }
```

**`--pretty expanded` output** (from "Debugging" section):

```rust
fn main() {
    let world = String::from("World");
    ::std::io::_print(::std::fmt::Arguments::new_v1(
        {
            static __STATIC_FMTSTR: &'static [&'static str]
                = &["Hello, ", "!\n"];
            __STATIC_FMTSTR
        },
        &match (&world,) {
             (__arg0,) => [
                ::std::fmt::ArgumentV1::new(__arg0, ::std::fmt::Display::fmt)
            ],
        }
    ));
}
```

This shows both the `S!` macro expansion and the `println!` macro expansion.

# Relationships

## Builds Upon

- **macro-expansion** -- Debugging tools reveal the expansion process

## Related

- **macro-rules** -- All three tools apply to `macro_rules!` macros
- **macro-matcher** -- `trace_macros!` shows what arguments are matched at each step
- **macro-repetition** -- Trace output reveals how repetitions are processed step by step

# Common Errors

1. **Forgetting `#![feature(...)]`**: `trace_macros!` and `log_syntax!` are unstable features and require their respective feature gates on nightly.
2. **Leaving trace enabled**: Forgetting to add `trace_macros!(false)` results in verbose output for all subsequent macro invocations.
3. **Using `--pretty expanded` on stable**: The `-Z` flags require nightly or unstable options.

# Common Confusions

- **Confusion**: Thinking `trace_macros!` shows the expanded output.
  **Clarification**: `trace_macros!` shows the macro invocation (name and arguments) before expansion, not the result of expansion. Use `--pretty expanded` to see expansion results.
- **Confusion**: Expecting these tools to work on stable Rust.
  **Clarification**: `trace_macros!` and `log_syntax!` require the nightly compiler. The `--pretty expanded` flag also requires `-Z unstable-options`. There is also the `cargo-expand` tool (a third-party crate) that provides a stable alternative for viewing expanded output.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," section "Debugging."

# Verification Notes

- `trace_macros!` example and output: directly from the source
- `log_syntax!` example: directly from the source
- `--pretty expanded` example and output: directly from the source
- The characterization of `trace_macros!` as "particularly invaluable" for recursive macros: direct quote
- Confidence: HIGH -- all three tools are demonstrated with complete examples and output in the source
