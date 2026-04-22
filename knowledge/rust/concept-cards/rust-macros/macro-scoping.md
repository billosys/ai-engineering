---
concept: Macro Scoping
slug: macro-scoping
category: macro-system
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Scoping"
extraction_confidence: high
aliases:
  - "macro scope"
  - "macro visibility"
  - "macro import"
  - "macro export"
  - "#[macro_use]"
  - "#[macro_export]"
  - "$crate"
prerequisites:
  - macro-rules
extends: []
related:
  - macro-hygiene
contrasts_with: []
answers_questions:
  - "How are macros scoped in Rust?"
  - "How do you export a macro from a module?"
  - "How do you import macros from an external crate?"
  - "What is #[macro_use]?"
  - "What is #[macro_export]?"
  - "What is $crate?"
---

# Quick Definition

Macros in Rust have unusual scoping: they are visible in sub-modules (unlike regular items) but only after their definition point (textual order matters). `#[macro_use]` exports macros from modules or imports them from external crates. `#[macro_export]` makes macros available to other crates. The special variable `$crate` provides an absolute path to the defining crate.

# Core Definition

Macro scoping differs from regular Rust item scoping in two key ways:

1. **Visible in sub-modules**: Unlike regular items, macros defined at a scope level remain visible in all subsequent sub-modules at the same level.
2. **Textual order dependent**: Macros are only accessible after their definition point. Code before the `macro_rules!` definition cannot use the macro.

However, macros do not "leak" out of their defining scope -- a macro defined inside a module is not visible outside that module unless explicitly exported.

For cross-module and cross-crate visibility:
- **`#[macro_use]`** on a module exports its macros to the containing scope.
- **`#[macro_use]`** on `extern crate` imports macros from an external crate (effectively hoisted to the top of the module).
- **`#[macro_export]`** makes a macro available for import by other crates, ignoring all visibility modifiers.
- **`$crate`** is a special substitution variable that always expands to an absolute path prefix to the containing crate.

An important subtlety: the textual-order dependency applies to macro *definitions* but not to macro *references within other macros*. A macro can reference another macro that is defined later, as long as the referencing macro is not invoked until after the referenced macro is defined.

# Prerequisites

- **macro-rules** -- Scoping rules apply to `macro_rules!` definitions

# Key Properties

1. **Visible in sub-modules**: Macros propagate down into child modules, unlike regular items.
2. **Textual order**: Macros are only visible after their definition point.
3. **No upward leaking**: Macros defined inside a module are not visible outside it without `#[macro_use]`.
4. **`#[macro_use]` on modules**: Exports a module's macros to the parent scope.
5. **`#[macro_use]` on extern crate**: Imports macros from an external crate; effectively hoisted to the top of the module.
6. **`#[macro_export]`**: Makes a macro available for cross-crate import, ignoring visibility.
7. **Selective import**: `#[macro_use(X)]` imports only the macro `X`.
8. **`$crate` variable**: Always expands to an absolute path to the defining crate, enabling reliable cross-crate macro use.
9. **Late resolution**: Macros referenced within other macros are resolved at expansion time, not definition time.
10. **Function scoping**: Scoping rules also apply within functions, with inner blocks creating their own scopes.

# Construction / Recognition

## Textual order dependency

```rust
mod a {
    // X!(); // undefined -- before definition
}
macro_rules! X { () => {}; }
mod b {
    X!(); // defined -- after definition
}
```

## Exporting from a module with `#[macro_use]`

```rust
#[macro_use]
mod b {
    macro_rules! X { () => {}; }
    X!(); // defined
}
mod c {
    X!(); // defined -- exported by #[macro_use]
}
```

## Cross-crate export and import

Defining crate (`macs`):
```rust
mod macros {
    #[macro_export] macro_rules! X { () => { Y!(); } }
    #[macro_export] macro_rules! Y { () => {} }
}
// X! and Y! are exported despite `macros` being private
```

Consuming crate:
```rust
#[macro_use] extern crate macs;
X!(); // available
```

## Selective import

```rust
#[macro_use(X)] extern crate macs;
// X! is available, Y! is not
```

## Using `$crate` for absolute paths

```rust
#[macro_export]
macro_rules! my_macro {
    () => { $crate::some_function() };
}
```

`$crate` always resolves to the crate where the macro is defined.

# Context & Application

The unusual scoping rules for macros often surprise Rust programmers. A common piece of advice is to place all macros that should be accessible "crate wide" at the very top of the root module, before any other modules. This ensures they are available consistently.

The `$crate` mechanism is particularly important for library authors exporting macros. Because crates can be renamed by consumers, using `$crate` ensures the macro always references the correct crate regardless of renaming. However, `$crate` does not work for referencing other macros (`$crate::Y!` is not valid), meaning there is currently no way to guarantee a specific macro will be available when imported by another crate.

It is recommended to always use absolute paths to non-macro names in exported macros, including names in the standard library, to avoid conflicts.

# Examples

**Late resolution of macro references** (from "Scoping" section):

```rust
mod a {
    // X!(); // undefined
}
macro_rules! X { () => { Y!(); }; }
mod b {
    // X!(); // defined, but Y! is undefined at this point
}
macro_rules! Y { () => {}; }
mod c {
    X!(); // defined, and so is Y! (resolved at expansion time)
}
```

`X!` references `Y!`, which is defined after `X!`. This works because macro references are resolved at expansion time, not definition time. `X!()` in `mod c` works because `Y!` is defined before `mod c`.

**Function-level scoping** (from "Scoping" section):

```rust
macro_rules! X {
    () => { Y!() };
}

fn a() {
    macro_rules! Y { () => {"Hi!"} }
    assert_eq!(X!(), "Hi!");
    {
        assert_eq!(X!(), "Hi!");
        macro_rules! Y { () => {"Bye!"} }
        assert_eq!(X!(), "Bye!");
    }
    assert_eq!(X!(), "Hi!");
}
```

Macros can be shadowed within inner scopes, and the shadowing is unwound when the scope exits.

**`#[macro_use]` on extern crate is hoisted** (from "Import/Export" section):

```rust
mod a {
    // X!(); // defined! (hoisted from extern crate below)
}
macro_rules! Y { () => {}; }
mod b {
    X!(); // defined, and so is Y!
}
#[macro_use] extern crate macs;
```

Unlike local `macro_rules!`, `#[macro_use]` on `extern crate` is effectively hoisted to the top of the module.

# Relationships

## Builds Upon

- **macro-rules** -- Scoping applies to `macro_rules!` definitions

## Related

- **macro-hygiene** -- Hygiene interacts with scoping for identifier resolution

# Common Errors

1. **Using a macro before its definition**: Macros are only visible after their `macro_rules!` definition in textual order.
2. **Expecting macros to be visible outside their module**: Without `#[macro_use]`, macros don't escape their defining module.
3. **Using `$crate` to reference other macros**: `$crate::Y!` is not valid. There is no way to create a cross-crate macro reference.
4. **`#[macro_use]` on extern crate in a non-root module**: You can only `#[macro_use]` an external crate from the root module.

# Common Confusions

- **Confusion**: Expecting macros to follow the same scoping rules as functions and types.
  **Clarification**: Macros are visible in sub-modules (unlike regular items) but only after their definition point (unlike regular items which can be used before they're defined in the file). These rules are "somewhat unintuitive."
- **Confusion**: Thinking `#[macro_export]` respects `pub` visibility.
  **Clarification**: `#[macro_export]` ignores all visibility modifiers. A macro inside a private module can be exported to other crates.
- **Confusion**: Believing `#[macro_use]` on `extern crate` follows textual order.
  **Clarification**: Unlike local macros, `#[macro_use]` on `extern crate` is effectively hoisted to the top of the module, making imported macros available even before the `extern crate` declaration.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Scoping" and "Import/Export."

# Verification Notes

- Scoping rules with module examples: directly from the source with exact code samples
- `#[macro_use]` and `#[macro_export]` behavior: directly from "Import/Export" section
- `$crate` variable and its limitations: directly from "Import/Export" section
- Hoisting behavior of `#[macro_use]` on extern crate: directly from the source
- Function-level scoping: directly from the source
- Confidence: HIGH -- comprehensive treatment with many illustrative examples
