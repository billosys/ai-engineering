---
# === CORE IDENTIFICATION ===
concept: Documentation Tests
slug: doc-tests

# === CLASSIFICATION ===
category: documentation
subcategory: testing
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "Documentation tests"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "doctests"
  - "doc tests"
  - "documentation examples as tests"
  - "rustdoc --test"
  - "cargo test --doc"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - writing-documentation-sections
  - doc-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does rustdoc run code examples as tests?"
  - "How do I hide boilerplate code in doc test examples?"
  - "What preprocessing does rustdoc apply to doc tests?"
  - "What are the doc test attributes (ignore, should_panic, no_run, compile_fail)?"
  - "How do I use the ? operator in doc tests?"
  - "How does doc test merging work in edition 2024?"
  - "What is the standalone_crate attribute for doc tests?"
  - "How do I test documentation for macros?"
  - "What is #[cfg(doctest)] used for?"
  - "How do I specify an edition for a doc test?"
---

# Quick Definition

Rustdoc compiles and runs code examples in documentation comments as tests, ensuring examples stay correct as code evolves. Doc tests are preprocessed -- rustdoc wraps them in `fn main()`, injects `extern crate`, and applies common `allow` attributes. Lines prefixed with `# ` are hidden from rendered output but included in compilation. Code block attributes (`ignore`, `should_panic`, `no_run`, `compile_fail`, `edition2024`) control test behavior. Starting in edition 2024, compatible doc tests are merged into a single compilation unit for performance.

# Core Definition

Documentation tests are one of Rust's distinguishing features: every fenced code block in a doc comment is, by default, compiled and executed as a test. This ensures documentation examples are always up to date.

Rustdoc preprocesses each example before compiling:

1. Common `allow` attributes are inserted (`unused_variables`, `unused_assignments`, `unused_mut`, `unused_attributes`, `dead_code`)
2. Attributes from `#![doc(test(attr(...)))]` are added
3. Leading `#![foo]` attributes are kept as crate attributes
4. If no `extern crate` is present and `test(no_crate_inject)` is not set, `extern crate <mycrate>;` is inserted
5. If no `fn main` is present, the code is wrapped in `fn main() { your_code }`

Lines starting with `# ` (hash-space) are hidden from rendered documentation but included during compilation, allowing clean examples with hidden setup/teardown code.

Code block attributes control behavior:
- **`ignore`**: Skip compilation and execution entirely
- **`should_panic`**: Must compile and panic during execution
- **`no_run`**: Compile but do not execute (for network, I/O, or UB examples)
- **`compile_fail`**: Must fail to compile
- **`edition2015`/`edition2018`/`edition2021`/`edition2024`**: Compile with a specific edition
- **`standalone_crate`**: Do not merge with other doc tests (edition 2024+)
- **`ignore-<target>`**: Skip for specific targets (e.g., `ignore-x86_64`)

# Prerequisites

- **doc-comments** -- doc tests live inside `///` and `//!` doc comments

# Key Properties

1. **Automatic `fn main()` wrapping**: If the example doesn't contain `fn main`, rustdoc wraps it automatically.
2. **Hidden lines with `# `**: Lines prefixed with `# ` are compiled but not shown in rendered docs. Essential for hiding error-handling boilerplate.
3. **`?` operator support**: Since Rust 1.34.0, you can use `?` without an explicit `fn main()` if you add `# Ok::<(), ErrorType>(())` at the end.
4. **Escape hatch with `##`**: Two consecutive `#` symbols prevent line hiding -- `## ` renders as `# ` in the output.
5. **Doc test merging (2024+)**: Compatible doc tests are merged into one compilation unit for dramatically faster testing (e.g., sysinfo crate: 4.59s wall time vs. much longer without merging).
6. **`#[cfg(doctest)]`**: Items annotated with this only exist when rustdoc collects tests, useful for attaching compile_fail tests to dummy structs or testing README files.
7. **Custom CSS classes**: Code blocks can use `custom,{class=language-c}` to render as non-Rust code with custom styling.
8. **Target-specific ignoring**: `ignore-x86_64`, `ignore-windows` etc. skip doc tests for specific targets (since Rust 1.88.0).

# Construction / Recognition

## Basic Doc Test:
```rust
/// # Examples
///
/// ```
/// let x = 5;
/// assert_eq!(x, 5);
/// ```
pub fn my_function() {}
```

## Hiding Boilerplate:
```rust
/// ```
/// # fn main() -> Result<(), std::num::ParseIntError> {
/// let fortytwo = "42".parse::<u32>()?;
/// println!("{} + 10 = {}", fortytwo, fortytwo+10);
/// # Ok(())
/// # }
/// ```
```

## Using `?` Without Explicit main (Rust 1.34+):
```rust
/// ```
/// use std::io;
/// let mut input = String::new();
/// io::stdin().read_line(&mut input)?;
/// # Ok::<(), io::Error>(())
/// ```
```

## Doc Test Attributes:
```rust
/// ```should_panic
/// assert!(false);
/// ```

/// ```no_run
/// loop { println!("Hello, world"); }
/// ```

/// ```compile_fail
/// let x = 5;
/// x += 2; // shouldn't compile!
/// ```

/// ```edition2018
/// // Compiled with the 2018 edition
/// ```

/// ```ignore-x86_64,ignore-windows
/// // Skipped on x86_64 and Windows targets
/// ```
```

## Testing README via `#[cfg(doctest)]`:
```rust
#[doc = include_str!("../README.md")]
#[cfg(doctest)]
pub struct ReadmeDoctests;
```

# Context & Application

Doc tests are the primary mechanism for keeping Rust documentation honest. They run as part of `cargo test` (specifically `cargo test --doc`) and `rustdoc --test`. They are particularly valuable because:

- They catch documentation rot -- when APIs change, doc tests fail
- They serve as both documentation and regression tests
- The hidden-line mechanism lets examples be pedagogically clean while remaining compilable
- `compile_fail` tests can verify that type system guarantees hold

The edition 2024 merging feature significantly improves doc test performance for large crates, reducing compile time from O(n) separate compilations to a single merged compilation.

# Examples

**Example 1** (Ch 4): The five-step preprocessing algorithm:
> "1. Some common `allow` attributes are inserted... 2. Any attributes specified with `#![doc(test(attr(...)))]` are added. 3. Any leading `#![foo]` attributes are left intact as crate attributes. 4. If the example does not contain `extern crate`... `extern crate <mycrate>;` is inserted. 5. If the example does not contain `fn main`, the remainder of the text is wrapped in `fn main() { your_code }`."

**Example 2** (Ch 4): Hiding repeated setup code across multiple examples to explain code step by step -- each code block contains the full program but hides irrelevant lines with `# `:
```text
First, we set `x` to five:
    let x = 5;
    # let y = 6;
    # println!("{}", x + y);

Next, we set `y` to six:
    # let x = 5;
    let y = 6;
    # println!("{}", x + y);
```

**Example 3** (Ch 4): Doc test merging performance improvement in edition 2024:
> "sysinfo crate: wall-time duration: 4.59s, total compile time: 27.067s, total runtime: 3.969s"
> "Rust core library: wall-time duration: 102s, total compile time: 775.204s"

**Example 4** (Ch 4): Documenting macros with doc tests requires explicit `extern crate` and `main`:
```rust
/// ```
/// # #[macro_use] extern crate foo;
/// # fn main() {
/// panic_unless!(1 + 1 == 2, "Math is broken.");
/// # }
/// ```
```

# Relationships

## Builds Upon
- **doc-comments** -- doc tests are embedded in doc comments

## Enables
- Nothing directly -- doc tests are a terminal consumer of documentation

## Related
- **writing-documentation-sections** -- the Examples section contains doc tests
- **doc-attribute** -- `#![doc(test(attr(...)))]` and `#![doc(test(no_crate_inject))]` control doc test behavior
- **rustdoc-unstable** -- nightly features include error numbers for `compile_fail` tests

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Doc test fails with "cannot find function" because `extern crate` is missing for macros.
  **Correction**: For macro documentation, explicitly add `# #[macro_use] extern crate my_crate;` and `# fn main() { }` as hidden lines.

- **Error**: Using `?` in a doc test without a return type, causing "mismatched types" error.
  **Correction**: Either wrap in a hidden `fn main() -> Result<...>` or add `# Ok::<(), ErrorType>(())` at the end (Rust 1.34+). Write the `(())` without intermediate whitespace.

- **Error**: A doc test that depends on line numbers breaks when other tests are added (edition 2024 merging).
  **Correction**: Add the `standalone_crate` attribute to prevent the test from being merged with others.

# Common Confusions

- **Confusion**: Thinking `ignore` is the best way to skip a doc test.
  **Clarification**: `ignore` is rarely what you want. Use `text` for non-Rust code, `no_run` if it should compile but not run, or `compile_fail` if it should fail to compile. "Consider annotating it with `text` if it's not code or using `#`s to get a working example."

- **Confusion**: Thinking `# ` only works at the start of a line in the rendered output.
  **Clarification**: `# ` at the start of a doc comment line hides that entire line from the rendered documentation. The `##` escape renders as `# ` in the output, for cases where a literal `#` at the start of a line is needed.

- **Confusion**: Thinking doc tests run in the context of the crate's full private API.
  **Clarification**: Doc tests "link against only the public items of your crate." To test private items, use regular unit tests.

# Source Reference

Chapter 4: How to Write Documentation; section "Documentation tests" covering preprocessing, hiding, `?` usage, attributes, merging, macros, and `#[cfg(doctest)]`. Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- the five-step preprocessing algorithm and the complete list of code block attributes
- Confidence rationale: HIGH -- doc tests are thoroughly documented with precise semantics and numerous examples
- Uncertainties: Doc test merging behavior is edition-dependent and relatively new (2024); target-specific ignore is from Rust 1.88.0
- Cross-reference status: doc-comments, writing-documentation-sections, doc-attribute are in this extraction set
