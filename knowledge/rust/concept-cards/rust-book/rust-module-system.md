---
concept: Rust Module System
slug: rust-module-system
category: language-fundamentals
subcategory: code-organization
tier: foundational
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "07 - Packages, Crates, and Modules"
chapter_number: 7
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "modules"
  - "crates"
  - "packages"
  - "module system"
  - "use keyword"
  - "pub keyword"
  - "mod keyword"
  - "module paths"
  - "re-exporting"
  - "pub use"
prerequisites:
  - rust-structs
  - rust-enums-and-matching
extends: []
related:
  - rust-structs
  - rust-enums-and-matching
contrasts_with: []
answers_questions:
  - "What is the difference between a package, crate, and module?"
  - "What is a crate root?"
  - "How do I declare and organize modules?"
  - "What are absolute and relative paths in the module system?"
  - "How does the pub keyword work with modules, functions, structs, and enums?"
  - "How do I bring paths into scope with use?"
  - "What is idiomatic use path style for functions vs. types?"
  - "How does pub use re-exporting work?"
  - "How do I separate modules into different files?"
  - "What is the super keyword for?"
  - "Why are struct fields private but enum variants public by default?"
---

# Quick Definition

Rust's module system controls code organization, scope, and privacy through four interconnected features: packages (Cargo feature for building/testing/sharing crates), crates (a tree of modules producing a library or executable), modules and `use` (controlling organization, scope, and privacy of paths), and paths (naming items like structs, functions, or modules). All items are private by default; the `pub` keyword exposes them, and the `use` keyword creates shortcuts to reduce path repetition.

# Core Definition

A **crate** is the smallest compilation unit the Rust compiler considers. It comes in two forms: **binary crates** compile to executables and must have a `main` function, while **library crates** define shared functionality without `main`. The **crate root** is the source file the compiler starts from -- conventionally `src/main.rs` for binary crates and `src/lib.rs` for library crates.

A **package** is a bundle of one or more crates described by a `Cargo.toml` file. A package must contain at least one crate and can have at most one library crate but any number of binary crates. Additional binary crates are placed in `src/bin/`, each file becoming a separate binary crate.

**Modules** are declared with `mod` and organize code within a crate. The compiler looks for a module's code in three places: inline (curly braces replacing the semicolon), in `src/module_name.rs`, or in `src/module_name/mod.rs` (older style). Submodules follow the same pattern within the parent module's directory. The entire module hierarchy forms the **module tree**, rooted at the implicit `crate` module.

**Paths** refer to items in the module tree. An **absolute path** starts from `crate` (for the current crate) or the crate name (for external crates). A **relative path** starts from the current module using an identifier, `self`, or `super` (parent module, analogous to `..` in filesystems). Paths use `::` as the separator.

**Privacy**: All items (functions, methods, structs, enums, modules, constants) are **private to parent modules by default**. Child modules can see items in their ancestor modules, but parent modules cannot see private items in child modules. The `pub` keyword makes items public. Key asymmetry: making a **module** public does not make its contents public; each item must be individually marked `pub`. For **structs**, each field is independently public or private. For **enums**, making the enum `pub` makes all variants public (since enums with private variants would be useless).

**`use`** creates shortcuts to paths within a scope. Idiomatic style: bring a function's parent module into scope (so calls show the module name), but bring structs, enums, and other types directly. When two types share a name, use parent modules or the `as` keyword to disambiguate. `use` only applies to the scope where it appears.

**`pub use`** re-exports a name, making it available to external code as if defined in the re-exporting scope. This allows the internal module structure to differ from the public API structure.

**Nested paths** combine multiple `use` statements sharing a common prefix: `use std::{cmp::Ordering, io};`. Using `self` in a nested path brings the prefix itself into scope: `use std::io::{self, Write};`. The **glob operator** (`*`) imports all public items from a path.

**Separating modules into files**: Use `mod module_name;` (with semicolon) to tell the compiler to load the module from a file. The `mod` declaration is needed only once; all other files reference the module via paths. File locations mirror the module tree structure.

# Prerequisites

- **Structs** (Ch. 5): Understanding struct field privacy and how `pub` applies per-field
- **Enums** (Ch. 6): Understanding why enum variants are all-public when the enum is public

# Key Properties

1. A package contains at most one library crate but any number of binary crates
2. `src/main.rs` is the binary crate root; `src/lib.rs` is the library crate root (by convention)
3. The compiler looks for module code inline, in `src/name.rs`, or in `src/name/mod.rs`
4. All items are private to parent modules by default; child modules can see ancestor items
5. Making a module `pub` does not make its contents `pub`; each item needs its own `pub`
6. Struct fields are individually public or private; structs with private fields need a public constructor
7. Enum variants are all public when the enum is `pub`
8. Absolute paths start with `crate` (current crate) or the crate name (external crate)
9. `super` starts a relative path from the parent module, like `..` in a filesystem
10. Idiomatic `use`: bring the parent module for functions, bring the full path for types
11. `pub use` re-exports items, decoupling internal structure from the public API
12. `mod` declarations load a file once; other files reference via paths, not additional `mod` statements

# Construction / Recognition

## Setting Up Packages and Crates

1. Run `cargo new my-project` to create a package with a binary crate (`src/main.rs`)
2. Add `src/lib.rs` for a library crate alongside the binary crate
3. Place additional binary crates in `src/bin/`, one file per binary
4. Add external crate dependencies in `Cargo.toml`

## Organizing with Modules

1. Declare modules in the crate root with `mod module_name;`
2. Place module code in `src/module_name.rs` or inline with curly braces
3. Declare submodules in parent module files with `mod submodule_name;`
4. Place submodule code in `src/parent_module/submodule_name.rs`
5. Use `pub mod` and `pub fn`/`pub struct` to expose items through the module tree
6. Use `pub use` in the crate root to create a flat public API from a nested internal structure

## Using Paths and use Statements

1. Use absolute paths (`crate::module::item`) for stability when code moves
2. Use `super::` to reference parent module items (useful for tightly coupled code)
3. Use `use crate::module::submodule;` then call `submodule::function()` (idiomatic for functions)
4. Use `use std::collections::HashMap;` then `HashMap::new()` (idiomatic for types)
5. Use `as` to rename imports: `use std::io::Result as IoResult;`
6. Use nested paths: `use std::{cmp::Ordering, io};`

# Context & Application

The module system is how Rust manages growing projects. It provides encapsulation (private by default), namespacing (modules create scopes), and code organization (files mirror the module tree). The privacy system is fundamental to Rust's safety guarantees -- it controls which code can access which data and functions, which is particularly important for maintaining invariants in unsafe code.

The distinction between packages and crates matters for the ecosystem: packages are the unit Cargo manages (building, testing, publishing to crates.io), while crates are the unit the compiler processes. A common pattern is having both a library and binary crate in one package, where the binary is a thin wrapper calling into the library's public API.

Re-exporting with `pub use` is a powerful technique for API design: the internal module structure can be organized for development convenience, while `pub use` in the crate root creates a flat, user-friendly public API. This is commonly used in production Rust libraries.

# Examples

**Example 1** (Sec. 7.2-7.3): Module tree with paths and privacy:
```rust
// src/lib.rs
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();
    // Relative path
    front_of_house::hosting::add_to_waitlist();
}
```

**Example 2** (Sec. 7.3): Struct fields vs. enum variants privacy:
```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,       // public field
        seasonal_fruit: String,  // private field
    }
    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {  // constructor needed
            Breakfast { toast: String::from(toast), seasonal_fruit: String::from("peaches") }
        }
    }
    pub enum Appetizer {
        Soup,    // automatically public
        Salad,   // automatically public
    }
}
```

**Example 3** (Sec. 7.4): Re-exporting with pub use:
```rust
// Without pub use: external code uses restaurant::front_of_house::hosting::add_to_waitlist()
// With pub use:
pub use crate::front_of_house::hosting;
// Now external code uses: restaurant::hosting::add_to_waitlist()
```

# Relationships

## Builds Upon
- **rust-structs** -- struct field privacy is controlled by the module system
- **rust-enums-and-matching** -- enum variant visibility rules differ from struct fields

## Enables
- **rust-error-handling** -- organizing error types and propagation across module boundaries
- **rust-collections** -- `use std::collections::HashMap;` demonstrates the `use` keyword for standard library types

## Related
- **rust-structs** -- `pub` controls per-field visibility in structs
- **rust-enums-and-matching** -- all enum variants are public when the enum is public

## Contrasts With
(none)

# Common Errors

- **Error**: Adding `pub` to a module but not to the items inside it, then wondering why they are still inaccessible.
  **Correction**: Making a module public only allows referencing the module itself. Each function, struct, or other item within must also be marked `pub` to be accessible.

- **Error**: Using `mod module_name;` in multiple files (treating it like an include/import statement).
  **Correction**: `mod` declares a module and loads its file exactly once, in the file that owns that position in the module tree. Other files reference the module's items via paths and `use`, not additional `mod` declarations.

- **Error**: Expecting to construct a struct with private fields from outside the module.
  **Correction**: If a struct has any private fields, it cannot be constructed directly outside its module. The module must provide a public associated function (constructor) like `Breakfast::summer()`.

# Common Confusions

- **Confusion**: Thinking `mod` is like `import` or `#include` from other languages.
  **Clarification**: `mod` declares that a module exists and tells the compiler where to find its code. It is a declaration, not an import. `use` is the keyword that brings paths into scope (closer to import). A `mod` declaration is needed only once per module in the tree.

- **Confusion**: Assuming struct fields and enum variants have the same default visibility.
  **Clarification**: Struct fields are private by default even when the struct is `pub` -- each field needs its own `pub`. Enum variants are all automatically public when the enum is `pub`, because private variants would make the enum largely unusable.

- **Confusion**: Thinking `use` brings items into scope globally.
  **Clarification**: `use` only creates a shortcut in the scope where it appears. If a function is moved to a child module, the parent's `use` statement does not apply there. The child module needs its own `use` or must use `super::` to access the parent's shortcut.

# Source Reference

Chapter 7: Packages, Crates, and Modules. Section 7.1: Packages and Crates (definitions, binary vs. library, crate root conventions). Section 7.2: Defining Modules to Control Scope and Privacy (modules cheat sheet, module tree, inline vs. file modules). Section 7.3: Paths for Referring to an Item in the Module Tree (absolute/relative paths, pub keyword, super, struct/enum public visibility rules). Section 7.4: Bringing Paths into Scope with the use Keyword (idiomatic use, as keyword, pub use re-exporting, nested paths, glob operator). Section 7.5: Separating Modules into Different Files (file layout, mod declarations, alternate file paths).

# Verification Notes

- Definition source: Direct synthesis from Chapter 7 source (1060 lines)
- Key Properties: All items directly stated in the source text
- Confidence rationale: HIGH -- the chapter provides comprehensive, explicit coverage of the entire module system
- Uncertainties: None; all rules are clearly specified in the source
- Cross-reference status: Related slugs reference cards in this rust-book extraction set
