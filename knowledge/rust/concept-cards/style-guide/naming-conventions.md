---
# === CORE IDENTIFICATION ===
concept: Naming Conventions
slug: naming-conventions

# === CLASSIFICATION ===
category: style
subcategory: core-rules
tier: foundational

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Other Style Advice"
chapter_number: 5
pdf_page: null
section: "Names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust naming rules"
  - "Rust identifier conventions"
  - "CamelCase and snake_case in Rust"
  - "Rust naming style"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-style-guide
extends: []
related:
  - formatting-conventions
  - cargo-toml-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What naming convention should I use for types in Rust?"
  - "What naming convention should I use for functions in Rust?"
  - "What naming convention should I use for constants in Rust?"
  - "What naming convention should I use for enum variants in Rust?"
  - "How should I name struct fields in Rust?"
  - "What naming convention do Rust macros use?"
  - "What should I do when a name conflicts with a reserved word in Rust?"
  - "Should I prefer expression-oriented style in Rust?"
---

# Quick Definition

Rust naming conventions mandate `UpperCamelCase` for types and enum variants, `snake_case` for functions, methods, local variables, struct fields, and macros, and `SCREAMING_SNAKE_CASE` for constants and immutable statics. These conventions are enforced by compiler lints and are a fundamental part of idiomatic Rust.

# Core Definition

The Rust Style Guide defines a clear, consistent naming scheme for all identifiers (Ch. 5: Other Style Advice):

- **Types** shall be `UpperCamelCase`
- **Enum variants** shall be `UpperCamelCase`
- **Struct fields** shall be `snake_case`
- **Function and method names** shall be `snake_case`
- **Local variables** shall be `snake_case`
- **Macro names** shall be `snake_case`
- **Constants** (`const`s and immutable `static`s) shall be `SCREAMING_SNAKE_CASE`

For reserved word conflicts: "When a name is forbidden because it is a reserved word (such as `crate`), either use a raw identifier (`r#crate`) or use a trailing underscore (`crate_`). Don't misspell the word (`krate`)." (Ch. 5: Names).

The guide also recommends an expression-oriented programming style: "Prefer to use Rust's expression oriented nature where possible" (Ch. 5: Expressions). This means using expressions that return values rather than imperative assignment patterns.

For modules, the guide advises: "Avoid `#[path]` annotations where possible" (Ch. 5: Modules).

# Prerequisites

- **rust-style-guide** -- understanding the overall style guide and its purpose

# Key Properties

1. **UpperCamelCase for types**: All struct, enum, trait, and type alias names use CamelCase with an initial capital
2. **UpperCamelCase for enum variants**: Variants follow the same convention as type names
3. **snake_case for functions and methods**: All function and method names use lowercase with underscores
4. **snake_case for variables**: Local variables and struct fields use lowercase with underscores
5. **snake_case for macros**: Declarative and procedural macro names use lowercase with underscores
6. **SCREAMING_SNAKE_CASE for constants**: Both `const` items and immutable `static` items use all-caps with underscores
7. **Raw identifiers for reserved words**: Use `r#keyword` or `keyword_` suffix, never misspelling
8. **Expression-oriented style**: Prefer `let x = if y { 1 } else { 0 };` over mutable assignment patterns
9. **No #[path] annotations**: Avoid explicit module path annotations where file system layout suffices

# Construction / Recognition

## Applying Naming Conventions:
1. For a new struct, enum, trait, or type alias: use `UpperCamelCase` (e.g., `HashMap`, `Vec`, `MyStruct`)
2. For a new function or method: use `snake_case` (e.g., `get_value`, `push_back`, `is_empty`)
3. For a new constant or immutable static: use `SCREAMING_SNAKE_CASE` (e.g., `MAX_SIZE`, `DEFAULT_PORT`)
4. For a new local variable or struct field: use `snake_case` (e.g., `item_count`, `file_path`)
5. For a new macro: use `snake_case` (e.g., `vec!`, `println!`, `my_macro!`)

## Handling Reserved Word Conflicts:
1. Try a raw identifier first: `r#type`, `r#crate`, `r#match`
2. Alternatively, append an underscore: `type_`, `crate_`, `match_`
3. Never misspell: avoid `typ`, `krate`, `mtch`

## Recognizing Convention Violations:
- A function named `GetValue` or `getValue` violates the `snake_case` rule
- A struct named `my_struct` or `MY_STRUCT` violates the `UpperCamelCase` rule
- A constant named `maxSize` or `max_size` violates the `SCREAMING_SNAKE_CASE` rule
- The Rust compiler emits warnings for many of these violations by default

# Context & Application

These naming conventions are among the most universally applied rules in the Rust ecosystem. The Rust compiler itself enforces them through lints (`non_camel_case_types`, `non_snake_case`, `non_upper_case_globals`), meaning violations produce compiler warnings by default. Following these conventions is essential for idiomatic Rust code and is expected by virtually all Rust libraries, frameworks, and code review processes.

The expression-oriented style advice applies broadly: Rust's `if`, `match`, `loop`, and block expressions all return values, enabling a more functional style that avoids mutable variables and reduces the chance of uninitialized-variable bugs.

# Examples

**Example 1** (Ch. 5): Expression-oriented style:
```rust
// Preferred: expression-oriented
let x = if y { 1 } else { 0 };

// Avoid: imperative assignment
let x;
if y {
    x = 1;
} else {
    x = 0;
}
```

**Example 2**: Naming convention summary by category:
```rust
// Types: UpperCamelCase
struct MyStruct { ... }
enum Color { Red, Green, Blue }
trait Drawable { ... }
type Result<T> = std::result::Result<T, MyError>;

// Functions, methods, variables, fields: snake_case
fn calculate_total(item_count: u32) -> u32 { ... }
let file_path = "/tmp/data.txt";

// Constants: SCREAMING_SNAKE_CASE
const MAX_RETRIES: u32 = 3;
static DEFAULT_NAME: &str = "unnamed";

// Macros: snake_case
macro_rules! my_macro { ... }
```

**Example 3**: Handling reserved word conflicts:
```rust
// Using raw identifiers
let r#type = "keyword";
fn r#match(input: &str) -> bool { ... }

// Using trailing underscore
let type_ = "keyword";
fn match_(input: &str) -> bool { ... }

// WRONG: Don't misspell
// let typ = "keyword";  // Avoid this
// fn mtch(input: &str) -> bool { ... }  // Avoid this
```

# Relationships

## Builds Upon
- **rust-style-guide** -- naming conventions are part of the overall style guide

## Enables
- Consistent, readable code across the entire Rust ecosystem
- Compiler lint enforcement through `non_camel_case_types`, `non_snake_case`, and `non_upper_case_globals`

## Related
- **formatting-conventions** -- the complementary set of visual formatting rules
- **cargo-toml-conventions** -- naming is also relevant in Cargo.toml key names

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `camelCase` (lower initial) for type names, following Java or JavaScript conventions.
  **Correction**: Rust types use `UpperCamelCase` (also called PascalCase). The first letter must be uppercase: `HashMap`, not `hashMap`.

- **Error**: Using `SCREAMING_SNAKE_CASE` for mutable statics.
  **Correction**: The guide specifies `SCREAMING_SNAKE_CASE` for "constants (`const`s and immutable `static`s)." Mutable statics (`static mut`) are a different category, though in practice `SCREAMING_SNAKE_CASE` is commonly used for all statics.

- **Error**: Misspelling identifiers to avoid reserved word conflicts (e.g., `krate` for `crate`, `typ` for `type`).
  **Correction**: Use raw identifiers (`r#crate`, `r#type`) or trailing underscores (`crate_`, `type_`). Misspelling harms readability and searchability.

# Common Confusions

- **Confusion**: Thinking enum variants follow a different convention than types.
  **Clarification**: Both types and enum variants use `UpperCamelCase`. An enum variant like `Color::DarkBlue` follows the same convention as a struct name like `DarkBlue`.

- **Confusion**: Thinking macro names should use `UpperCamelCase` because macros are "like types."
  **Clarification**: Macro names use `snake_case`, following the same convention as functions. This is true for both declarative macros (`macro_rules!`) and procedural macros (though derive macros follow type naming since they are used as type-level attributes).

- **Confusion**: Thinking `snake_case` means no abbreviations or acronyms are allowed.
  **Clarification**: The convention specifies the casing pattern, not word choice. Abbreviations and acronyms are acceptable when clear (e.g., `tcp_stream`, `io_error`). For `UpperCamelCase`, acronyms are typically capitalized as words: `TcpStream`, not `TCPStream`.

# Source Reference

Chapter 5: Other Style Advice -- sections on Expressions, Names, and Modules. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 5 -- the naming rules are quoted verbatim from the "Names" section
- Expression style: Directly from Ch. 5 -- "Prefer to use Rust's expression oriented nature where possible"
- Reserved word handling: Directly quoted from Ch. 5 -- "either use a raw identifier (`r#crate`) or use a trailing underscore (`crate_`). Don't misspell the word (`krate`)."
- Confidence rationale: HIGH -- the rules are explicit and unambiguous
- Uncertainties: The guide does not cover all naming edge cases (e.g., acronym handling in CamelCase); additional conventions come from RFC 430
- Cross-reference status: rust-style-guide, formatting-conventions are in this extraction set
