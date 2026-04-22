---
concept: Syntax Extension
slug: syntax-extension
category: compilation
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Syntax Extensions"
extraction_confidence: high
aliases:
  - "syntax extensions"
  - "compiler extensions"
prerequisites:
  - token-tree
extends: []
related:
  - macro-rules
  - macro-expansion
contrasts_with: []
answers_questions:
  - "What are syntax extensions in Rust?"
  - "How do macros relate to syntax extensions?"
  - "What forms can syntax extensions take in Rust?"
  - "Where can macros appear in Rust code?"
---

# Quick Definition

Syntax extensions are the general mechanism in Rust that macros are built on. They are parsed as part of the AST and can only appear in specific syntactic positions. The `$name!($arg)` form is the one available to user-defined macros, where `$arg` is always a single non-leaf token tree.

# Core Definition

Before the compiler constructs its semantic understanding of a Rust program, it processes syntax extensions found in the AST. There are several syntax extension forms in Rust:

1. `#[$arg]` -- e.g., `#[derive(Clone)]`, `#[no_mangle]` (attributes)
2. `#![$arg]` -- e.g., `#![allow(dead_code)]` (inner attributes)
3. `$name ! $arg` -- e.g., `println!("Hi!")`, `concat!("a", "b")` (the macro invocation form)
4. `$name ! $arg0 $arg1` -- e.g., `macro_rules! dummy { () => {}; }` (used only by `macro_rules!` itself)

The third form is the one available for user-defined macros. Not everything of the form `$name! $arg` is necessarily a macro -- it is a generic syntax extension form. For example, `format_args!` is a compiler built-in syntax extension, not a macro.

The argument to a syntax extension invocation is always a single non-leaf token tree (`(...)`, `[...]`, or `{...}`). The parser does not attempt to understand the contents of this token tree -- it simply remembers the tokens it contains.

# Prerequisites

- **token-tree** -- The input to every syntax extension is a single non-leaf token tree; understanding token trees is essential to understanding how the parser handles macro arguments.

# Key Properties

1. **Parsed into the AST**: Syntax extensions are part of the abstract syntax tree, not a separate pre-processing phase.
2. **Single token tree argument**: The argument is always a single non-leaf token tree (`(...)`, `[...]`, or `{...}`).
3. **Parser-opaque contents**: The parser does not interpret the contents of the argument token tree.
4. **Position-restricted**: Macros can only appear where explicitly supported in the grammar.
5. **Multiple forms exist**: Attributes, bang-macros, and `macro_rules!` are all syntax extension forms.

# Construction / Recognition

## Valid macro positions

Macros can appear in place of:
- Patterns
- Statements
- Expressions
- Items
- `impl` items

## Invalid macro positions

Macros cannot appear in place of:
- Identifiers
- Match arms
- Struct fields
- Types (unstable feature `type_macros` exists)

## How the parser sees macro invocations

```text
bitflags! { ... }    -->  bitflags! [black-box-token-tree]
lazy_static! { ... } -->  lazy_static! [black-box-token-tree]
vec![RED, GREEN]     -->  vec! [black-box-token-tree]
println!("Hi!")      -->  println! [black-box-token-tree]
```

The parser sees each invocation as `$name!` followed by a single opaque token tree.

# Context & Application

Understanding syntax extensions is important because it explains why macros have the constraints they do. Since macros are parsed into the AST:

- They can only appear in specific syntactic positions
- They can only expand to AST node types the parser expects at that position
- They cannot expand to incomplete or syntactically invalid constructs

This is fundamentally different from C/C++ macros, which operate at the token level before parsing and can therefore produce arbitrary token sequences (including syntactically invalid ones).

The fact that the parser treats macro arguments as opaque token trees is what allows macros like `bitflags!` and `lazy_static!` to accept domain-specific syntax -- the parser doesn't try to understand the contents, it just records the tokens for later processing by the macro expander.

# Examples

**Various syntax extension invocations** (from "Macros in the AST" section):

```rust
bitflags! {
    flags Color: u8 {
        const RED    = 0b0001,
        const GREEN  = 0b0010,
        const BLUE   = 0b0100,
        const BRIGHT = 0b1000,
    }
}

lazy_static! {
    static ref FIB_100: u32 = {
        fn fib(a: u32) -> u32 {
            match a {
                0 => 0,
                1 => 1,
                a => fib(a-1) + fib(a-2)
            }
        }
        fib(100)
    };
}

fn main() {
    let colors = vec![RED, GREEN, BLUE];
    println!("Hello, World!");
}
```

The parser sees all of these as `$name!` followed by an opaque token tree:

```text
bitflags! [box]
lazy_static! [box]
vec! [box]
println! [box]
```

# Relationships

## Enables

- **macro-rules** -- `macro_rules!` is the primary user-facing syntax extension form
- **macro-expansion** -- Syntax extensions are expanded after AST construction

## Related

- **token-tree** -- The argument to every syntax extension is a token tree

# Common Errors

1. **Attempting to use a macro in an unsupported position**: e.g., trying to use a macro as a struct field name or match arm, which will fail because macros are not supported in those positions.
2. **Confusing syntax extension forms**: Not all `$name!` invocations are `macro_rules!` macros -- some are compiler built-ins like `format_args!`.

# Common Confusions

- **Confusion**: Thinking macros are a pre-processing step like in C/C++.
  **Clarification**: Rust macros are parsed as part of the AST and processed after AST construction. They cannot produce syntactically invalid code.
- **Confusion**: Believing macros can appear anywhere in Rust code.
  **Clarification**: Macros can only appear in the specific positions listed above (patterns, statements, expressions, items, impl items). There is "absolutely, definitely no way" to use macros in other positions.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Syntax Extensions" and "Macros in the AST."

# Verification Notes

- Syntax extension forms: directly enumerated in the source
- Valid/invalid positions: directly listed in the source
- The characterization of parser-opaque token trees is explicit in the source ("the parser does not assume anything about [the token tree]; it remembers the tokens it contains, but doesn't try to understand them")
- Confidence: HIGH -- explicit and detailed treatment in the source
