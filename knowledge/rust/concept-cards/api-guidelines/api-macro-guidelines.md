---
concept: API Macro Guidelines
slug: api-macro-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "03-macros"
chapter_number: 3
pdf_page: null
section: "Macros"
extraction_confidence: high
aliases:
  - "rust macro guidelines"
  - "macro design guidelines"
  - "C-EVOCATIVE C-MACRO-ATTR C-ANYWHERE C-MACRO-VIS C-MACRO-TY"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-naming-guidelines
  - api-documentation-guidelines
contrasts_with: []
answers_questions:
  - "How should macro input syntax be designed?"
  - "Should macros support attributes and derive?"
  - "What scope limitations should macros avoid?"
  - "How should macros handle visibility specifiers?"
  - "What type fragments should macros accept?"
---

# Quick Definition

The Macros chapter of the Rust API Guidelines defines 5 guidelines (C-EVOCATIVE, C-MACRO-ATTR, C-ANYWHERE, C-MACRO-VIS, C-MACRO-TY) for designing well-behaved macros. The central principle is that macros should feel like natural Rust: their input syntax should mirror existing Rust syntax, and their output should compose with the full range of Rust features including attributes, visibility, and arbitrary scopes.

# Core Definition

**C-EVOCATIVE** -- Input syntax is evocative of the output. Macro input syntax should mirror existing Rust syntax where possible. Use keywords and punctuation similar to what will be produced in the output. If the macro declares a struct, preface the name with `struct`. If declaring constants, use semicolons (not commas) to match Rust's constant syntax. "Aim to keep input syntax familiar and cohesive with the rest of your users' code."

**C-MACRO-ATTR** -- Macros compose well with attributes. Macros that produce multiple output items should support adding attributes to any one of those items (e.g., putting items behind `#[cfg(windows)]`). Macros that produce a struct or enum should support attributes so the output can be used with derive (e.g., `#[derive(Default, Serialize)]`).

**C-ANYWHERE** -- Item macros work anywhere that items are allowed. Rust allows items at the module level or within tighter scopes like functions. Item macros should work equally well in all such places. Test suites should include invocations in at least module scope and function scope. A common failure mode is macros that use `super::` paths which break inside function scope because `super` refers to the containing module, not the function.

**C-MACRO-VIS** -- Item macros support visibility specifiers. Follow Rust syntax: private by default, public if `pub` is specified. Users should be able to write both `struct PrivateFlags` and `pub struct PublicFlags` within the macro invocation.

**C-MACRO-TY** -- Type fragments are flexible. If a macro accepts `$t:ty`, it should work with all type forms: primitives (`u8`, `&str`), relative paths (`m::Data`), absolute paths (`::base::Data`), upward relative paths (`super::Data`), and generics (`Vec<String>`). A common failure mode is macros that wrap the type in a module, breaking relative path resolution.

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework

# Key Properties

1. Macro input should use Rust keywords (`struct`, `const`) and punctuation (semicolons) that match the output
2. Attribute support enables `#[cfg(...)]` gating and `#[derive(...)]` on macro-generated items
3. Scope independence means macros work at module level and inside functions
4. Visibility support follows Rust's default-private convention
5. Type fragment flexibility ensures macros accept all forms of Rust type syntax
6. The `super::` path is the most common source of scope-related breakage in macros

# Construction / Recognition

## Designing a Well-Behaved Macro:
1. **Syntax** (C-EVOCATIVE): Mirror Rust syntax in the macro input. If generating structs, use the `struct` keyword. If generating constants, use semicolons. Avoid ad-hoc keywords (e.g., `flags` instead of `struct`)
2. **Attributes** (C-MACRO-ATTR): Allow `#[...]` attributes before each item the macro produces. Pass through outer attributes to the generated output items
3. **Scope testing** (C-ANYWHERE): Test the macro in at least two scopes -- module level and inside a function. Watch for `super::` paths that break in function scope
4. **Visibility** (C-MACRO-VIS): Accept an optional visibility modifier (e.g., `$vis:vis`) and apply it to generated items. Default to private when no modifier is given
5. **Type flexibility** (C-MACRO-TY): Test type fragments with primitives, relative paths, absolute paths, `super::` paths, and generic types. Avoid wrapping types in modules that break relative path resolution

## Common Failure Pattern (C-ANYWHERE):
```rust
macro_rules! broken {
    ($m:ident :: $t:ident) => {
        pub struct $t;
        pub mod $m { pub use super::$t; }
    }
}
broken!(m::T); // Works at module scope
fn g() {
    broken!(m::U); // Fails: super::U refers to containing module, not g
}
```

## Common Failure Pattern (C-MACRO-TY):
```rust
macro_rules! broken {
    ($m:ident => $t:ty) => {
        pub mod $m { pub struct Wrapper($t); }
    }
}
broken!(a => u8); // Works
broken!(c => S); // Fails: S not found inside generated module
```

# Context & Application

Macros are one of Rust's most powerful features but also one of the easiest to misuse. Because macros can define arbitrary input syntax, there is a temptation to create novel DSLs that feel alien to Rust users. These guidelines push back toward familiarity: macro input should look like Rust, and macro output should behave like hand-written Rust.

The practical effect is that well-designed macros compose with the rest of the language. Users can apply attributes, control visibility, use them in any scope, and pass any type -- the same things they can do with regular Rust items.

# Examples

**Example 1** (C-EVOCATIVE): The `bitflags!` macro uses `struct` keyword and semicolons to match Rust syntax:
```rust
bitflags! {
    struct S: u32 {
        const C = 0b000100;
        const D = 0b001000;
    }
}
```
This is preferred over omitting `struct` or using an ad-hoc keyword like `flags`, and over using commas instead of semicolons (since ordinary constants use semicolons).

**Example 2** (C-MACRO-ATTR): Supporting `#[cfg(...)]` on individual items and `#[derive(...)]` on the outer type:
```rust
bitflags! {
    #[derive(Default, Serialize)]
    struct Flags: u8 {
        #[cfg(windows)]
        const ControlCenter = 0b001;
        #[cfg(unix)]
        const Terminal = 0b010;
    }
}
```

**Example 3** (C-MACRO-VIS): Supporting both private and public visibility:
```rust
bitflags! {
    struct PrivateFlags: u8 { const A = 0b0001; }
}
bitflags! {
    pub struct PublicFlags: u8 { const C = 0b0100; }
}
```

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories

## Enables
- Well-behaved macros that integrate seamlessly with attributes, visibility, and scoping
- Macros that users can adopt without learning custom syntax

## Related
- **api-naming-guidelines** -- C-CASE applies to macro names (`snake_case!`)
- **api-documentation-guidelines** -- macros need documentation and examples too

## Contrasts With
- Macros with ad-hoc DSL syntax that diverges from Rust conventions
- Macros that only work at module scope or only with absolute paths

# Common Errors

- **Error**: Using commas between constant declarations in a macro that generates constants.
  **Correction**: Use semicolons to match Rust's constant declaration syntax, since constants in Rust are followed by semicolons.

- **Error**: Using `super::` paths in macro-generated modules without testing inside function scope.
  **Correction**: `super::` inside a function refers to the containing module, not the function. Test macros in both module and function scope to catch this.

- **Error**: Wrapping a type fragment `$t:ty` inside a generated module, breaking relative path resolution.
  **Correction**: If the macro generates a module, relative type paths like `S` will not resolve inside it. Design the macro to avoid this or require absolute paths.

# Common Confusions

- **Confusion**: Thinking macro syntax should be maximally concise rather than familiar.
  **Clarification**: The goal is to mirror Rust syntax, even if it is slightly more verbose. Users should recognize the structure (struct declarations, const statements) without learning a new language.

- **Confusion**: Thinking `#[derive(...)]` support comes automatically from macros.
  **Clarification**: The macro must explicitly pass through outer attributes to the generated items. Without this, users cannot apply derive to macro-generated types.

# Source Reference

Chapter 3: Macros. All 5 guidelines (C-EVOCATIVE, C-MACRO-ATTR, C-ANYWHERE, C-MACRO-VIS, C-MACRO-TY) are covered with examples primarily from the `bitflags!` macro and demonstrations of common failure modes.

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit statements and code examples in each section
- Confidence: HIGH -- the macro guidelines are concrete with clear examples and failure demonstrations
- Uncertainties: None -- the guidelines and their examples are unambiguous
- Cross-reference status: All slugs reference cards in this extraction set
