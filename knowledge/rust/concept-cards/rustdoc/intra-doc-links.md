---
# === CORE IDENTIFICATION ===
concept: Intra-Doc Links
slug: intra-doc-links

# === CLASSIFICATION ===
category: documentation
subcategory: linking
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "Linking to items by name"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "intra-doc linking"
  - "linking to items by name"
  - "path-based doc links"
  - "rustdoc link resolution"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - doc-reexports
  - doc-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I link to other items in Rust documentation?"
  - "What link syntaxes does rustdoc support for intra-doc links?"
  - "How do I disambiguate between items with the same name in different namespaces?"
  - "What disambiguator prefixes are available (struct@, fn@, macro@, etc.)?"
  - "How are intra-doc links resolved when items are re-exported?"
  - "Can I link to generic types like Vec<T>?"
  - "How do I link to a specific section of another item's documentation?"
  - "What happens when an intra-doc link cannot be resolved?"
---

# Quick Definition

Intra-doc links allow Rust documentation to link to other items using their Rust path rather than manual URLs. All standard Markdown link syntaxes work: `[Bar]`, `[bar](Bar)`, `[bar][b]` with `[b]: Bar`, and `` [`Bar`] `` (backticks are stripped). When names are ambiguous across namespaces (type, value, macro), disambiguators like `struct@Foo`, `fn@Foo`, `Foo()`, or `foo!` are used. Links are resolved in the scope of the module where the item is defined, even after re-export.

# Core Definition

Rustdoc can directly link to other items using their Rust path as a link target, without requiring manual HTML URLs. This is called "intra-doc linking." The feature supports all Markdown link syntaxes:

```rust
/// This struct is not [Bar]
/// This struct is also not [bar](Bar)
/// This struct is also not [bar][b]
///
/// [b]: Bar
/// This struct is also not [`Bar`]
```

Unlike standard Markdown, `[bar][Bar]` syntax works without needing a `[Bar]: ...` reference link definition. Backticks around link text are stripped, so `` [`Option`] `` links to `Option` and renders as code.

Links can reference anything in scope: types, functions, constants, modules, traits, associated items, and primitives. Paths support `Self`, `self`, `super`, and `crate`. Generic types like `Vec<T>` resolve as if written `` [`Vec<T>`](Vec) ``. URL fragment specifiers work for linking to sections: `[positional parameters]: std::fmt#formatting-parameters`.

When a name exists in multiple namespaces (type, value, macro), rustdoc warns and requires a disambiguator prefix (`struct@`, `enum@`, `trait@`, `fn@`, `macro@`, etc.) or suffix (`()` for functions, `!` for macros).

# Prerequisites

- **doc-comments** -- intra-doc links are written inside doc comments

# Key Properties

1. **All Markdown link syntaxes work**: `[Name]`, `[text](Name)`, `[text][ref]` with `[ref]: Name`, and `` [`Name`] ``
2. **No reference definition needed**: `[bar][Bar]` works without a `[Bar]: ...` line, unlike standard Markdown
3. **Backticks are stripped**: `` [`Option`] `` links to `Option` and renders the text as inline code
4. **Scope-based resolution**: Links resolve in the module where the doc comment is defined, even after re-export
5. **Disambiguators for namespaces**: Available prefixes: `struct`, `enum`, `trait`, `union`, `mod`/`module`, `const`/`constant`, `fn`/`function`, `field`, `variant`, `method`, `derive`, `type`, `value`, `macro`, `tyalias`/`typealias`, `prim`/`primitive`
6. **Function/macro suffix disambiguators**: `foo()` for functions, `foo!` for macros (with optional `()`, `{}`, or `[]`)
7. **Automatic trait vs. derive disambiguation**: When both a trait and a derive proc-macro have the same name (e.g., `Clone`), rustdoc automatically links to the trait
8. **Fragment specifiers**: `std::fmt#formatting-parameters` links to a section within another item's docs
9. **Re-export additional docs**: Documentation added on a re-export resolves in the re-export's scope, not the original item's scope
10. **Silent ignore for non-Rust links**: Links containing `/` or `[]` are ignored and produce no warnings

# Construction / Recognition

## Basic Intra-Doc Links:
```rust
/// See [`Vec`] for a growable array.
/// Also check out [HashMap](std::collections::HashMap).
/// The [standard library](std) has many useful types.
pub fn example() {}
```

## Disambiguators:
```rust
/// See also: [`Foo`](struct@Foo)
struct Bar;

/// This is different from [`Foo`](fn@Foo)
struct Foo {}

fn Foo() {}
```

## Function and Macro Disambiguators:
```rust
/// This is different from [`foo!()`].
fn foo() {}

/// This is different from [`foo()`]
macro_rules! foo { () => {} }
```

## Linking to Associated Items and Generics:
```rust
/// You can obtain a [`std::future::Future`] by calling [`Self::recv()`].
/// This is a version of [`Receiver<T>`] with support for [`std::future`].
pub struct AsyncReceiver<T> { /* ... */ }
```

## Fragment Specifiers:
```rust
/// This is a special implementation of [positional parameters].
///
/// [positional parameters]: std::fmt#formatting-parameters
struct MySpecialFormatter;
```

# Context & Application

Intra-doc links are the idiomatic way to cross-reference items in Rust documentation. They are superior to manual URLs because they are checked at documentation build time (broken links produce warnings), they automatically follow re-exports and refactoring, and they don't depend on the documentation output format or hosting location. They are especially useful for proc-macro crates, which must be defined in separate crates but can add re-export documentation that links to items in the main crate.

# Examples

**Example 1** (Ch 4): All four supported link syntaxes pointing to the same item:
```rust
/// This struct is not [Bar]
pub struct Foo1;

/// This struct is also not [bar](Bar)
pub struct Foo2;

/// This struct is also not [bar][b]
///
/// [b]: Bar
pub struct Foo3;

/// This struct is also not [`Bar`]
pub struct Foo4;

pub struct Bar;
```

**Example 2** (Ch 4): Disambiguating between namespaces:
> "Paths in Rust have three namespaces: type, value, and macro. Item names must be unique within their namespace, but can overlap with items in other namespaces."

Disambiguator prefixes are stripped in rendered output: `[struct@Foo]` renders as just `Foo`.

**Example 3** (Ch 4): Re-export scoping -- links resolve where defined, not where re-exported:
```rust
mod inner {
    /// Link to [f()]
    pub struct S;
    pub fn f() {}
}
pub use inner::S; // the link to `f` will still resolve correctly
```

**Example 4** (Ch 4): Fallback behavior when a link cannot resolve:
> "`[a]` and `[b][c]` will be displayed as is (ie, `[a]` and `[b][c]`) whereas `[d](e)` and `[f]` (with `[f]: g`) will be replaced by a link."

# Relationships

## Builds Upon
- **doc-comments** -- intra-doc links are embedded in doc comments

## Enables
- Nothing directly -- intra-doc links are a feature within documentation

## Related
- **doc-reexports** -- intra-doc links interact with re-export inlining and scope resolution
- **doc-attribute** -- `#[doc(hidden)]` items are not linkable via intra-doc links
- **rustdoc-lints** -- broken intra-doc links produce warnings by default

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Writing `[std::collections::HashMap]` and expecting it to work as a link without parenthetical syntax.
  **Correction**: Bare `[path::to::Item]` does work as an intra-doc link. However, if you want different display text, use `[display text](path::to::Item)`.

- **Error**: Linking to a name that exists in multiple namespaces without a disambiguator.
  **Correction**: Add a disambiguator prefix (`struct@Name`, `fn@Name`, `macro@Name`) or suffix (`Name()` for functions, `Name!` for macros).

- **Error**: Expecting links to resolve after moving an item to a different module.
  **Correction**: Links resolve in the module where the doc comment is defined. If an item is re-exported, its links still resolve in the original module. Documentation added on the re-export resolves in the re-export's scope.

# Common Confusions

- **Confusion**: Thinking intra-doc links require full paths.
  **Clarification**: Links resolve using normal Rust path resolution. You can use relative paths, `Self`, `super`, and `crate`, just like in code.

- **Confusion**: Thinking links containing `/` are intra-doc links.
  **Clarification**: Links containing `/` or `[]` are silently treated as regular Markdown links, not intra-doc links. They produce no warning even if the URL is invalid.

- **Confusion**: Thinking the disambiguator prefix appears in the rendered output.
  **Clarification**: "These prefixes will be stripped when displayed in the documentation, so `[struct@Foo]` will be rendered as `Foo`."

# Source Reference

Chapter 4: How to Write Documentation; section "Linking to items by name" covering valid links, namespaces and disambiguators, warnings, re-exports and scoping, and fallback behavior. Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- "Rustdoc is capable of directly linking to other rustdoc pages using the path of the item as a link. This is referred to as an 'intra-doc link'."
- Confidence rationale: HIGH -- comprehensive coverage with syntax examples, disambiguation rules, and edge cases
- Uncertainties: Fully-qualified syntax (e.g., `<Vec as IntoIterator>::into_iter()`) is noted as "not yet supported" per tracking issue #74563
- Cross-reference status: doc-comments, doc-reexports, doc-attribute are in this extraction set
