---
concept: Procedural Macros
slug: reference-procedural-macros
category: language-specification
subcategory: macros
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Macros"
chapter_number: 3
pdf_page: null
section: "Procedural macros"
extraction_confidence: high
aliases:
  - "proc macros"
  - "proc_macro attribute"
  - "derive macros"
  - "attribute macros"
  - "function-like procedural macros"
  - "proc_macro_derive"
  - "proc_macro_attribute"
  - "TokenStream"
  - "proc macro hygiene"
  - "derive macro helper attributes"
prerequisites:
  - rust-reference-overview
  - lexical-structure-tokens-and-literals
  - reference-macros-by-example
extends: []
related:
  - reference-macros-by-example
contrasts_with:
  - reference-macros-by-example
answers_questions:
  - "What are the three kinds of procedural macros?"
  - "How do function-like procedural macros work?"
  - "How do derive macros work?"
  - "How do attribute macros work?"
  - "What is the proc_macro crate and what does it provide?"
  - "How do procedural macro token trees differ from macro_rules token trees?"
  - "What happens when tokens are passed between declarative and procedural macros?"
  - "Are procedural macros hygienic?"
  - "What are derive macro helper attributes?"
  - "Where must procedural macros be defined?"
---

# Quick Definition

Procedural macros are compile-time functions that transform token streams, defined in dedicated `proc-macro` crate types. They come in three flavors: function-like (`custom!(...)`, replacing the invocation), derive (`#[derive(Custom)]`, appending items after the target), and attribute (`#[custom_attr]`, replacing the annotated item). Unlike declarative macros, procedural macros are unhygienic and operate on a different token representation via the `proc_macro` crate's `TokenStream` type.

# Core Definition

## Procedural Macro Fundamentals

Procedural macros allow creating syntax extensions as the execution of a function. They run code at compile time that operates over Rust syntax, consuming and producing Rust syntax. They must be defined in the root of a crate with crate type `proc-macro` (specified via `[lib] proc-macro = true` in Cargo.toml). **Macros may not be used from the crate where they are defined** -- they can only be used when imported into another crate.

As functions, proc macros must either return syntax, panic, or loop endlessly. Panics are caught by the compiler and converted to compiler errors. Endless loops hang the compiler. Proc macros have two error reporting mechanisms: panicking, and emitting a `compile_error!` macro invocation. They run with the same resources as the compiler (stdin, stdout, stderr, file system access), giving them the same security concerns as Cargo build scripts.

## The `proc_macro` Crate

The compiler-provided `proc_macro` crate contains the `TokenStream` type -- the primary interface. Token streams are roughly equivalent to `Vec<TokenTree>` where a `TokenTree` is a lexical token (`Ident`, `Punct`, `Literal`, or `Group`). `TokenStream` is cheap to clone. All tokens have an associated `Span` -- an opaque value representing source location, primarily used for error reporting. Spans cannot be modified but can be copied from one token to another.

## Three Flavors

### Function-like Macros (`#[proc_macro]`)

Defined by applying the `proc_macro` attribute to a `pub fn(TokenStream) -> TokenStream` in the crate root with Rust ABI. The function receives the token tree inside the invocation delimiters and its output replaces the entire invocation. Function-like proc macros can be invoked in: statements, expressions, patterns, type expressions, item positions (including `extern` blocks), inherent and trait implementations, and trait definitions.

### Derive Macros (`#[proc_macro_derive]`)

Defined by applying `proc_macro_derive(Name)` to a `pub fn(TokenStream) -> TokenStream`. The input is the token stream of the struct, enum, or union to which `#[derive(Name)]` is applied. The output must be a (possibly empty) set of items that are **appended after** the input item within the same module or block -- the original item is not replaced.

Derive macros can declare **helper attributes** via `#[proc_macro_derive(Name, attributes(helper))]`. These helper attributes become available on the item and its fields/variants when the derive is applied. Helper attributes are inert -- they are visible to any macro but their purpose is to be consumed by the declaring derive macro. Helper attributes come into scope for attributes applied lexically after the derive invocation on the same item, and for attributes on fields and variants inside the item.

### Attribute Macros (`#[proc_macro_attribute]`)

Defined by applying `proc_macro_attribute` to a `pub fn(TokenStream, TokenStream) -> TokenStream`. The first `TokenStream` is the delimited token tree following the attribute name (empty if the attribute has no arguments). The second is the rest of the item including other attributes. The item is **replaced** by the zero or more items in the returned stream. Attribute macros can be used on: items, items in `extern` blocks, inherent and trait implementations, and trait definitions.

## Procedural Macro Hygiene

Procedural macros are **unhygienic** -- their output behaves as if written inline at the invocation site. This means output is affected by and affects external items and imports. Macro authors must use absolute paths (e.g., `::std::option::Option` instead of `Option`) and unlikely-to-clash names (e.g., `__internal_foo` instead of `foo`) to ensure macros work across contexts.

## Token Representation Differences

Declarative and procedural macros use different token tree definitions:

**`macro_rules` tokens** include: delimited groups, multi-character operators (`+=`), literals (without negation), identifiers/keywords, lifetimes, and metavariable substitutions.

**Procedural macro tokens** include: delimited groups, single punctuation characters (not multi-character operators), single quote `'`, literals (with negation support for numbers), and identifiers/keywords. Lifetimes are not a single token but a `'` plus an identifier.

**Conversions when passing to a proc macro**: Multi-character operators are broken into single characters. Lifetimes become `'` + identifier. `$crate` becomes a single identifier. Other metavariable substitutions become their underlying token streams, possibly wrapped in `Group` with `Delimiter::None` to preserve parsing priorities (`tt` and `ident` are never wrapped).

**Conversions when emitting from a proc macro**: Punctuation characters are glued into multi-character operators. `'` joined with identifiers become lifetimes. Negative literals become two tokens (possibly wrapped in `Delimiter::None` group).

**Doc comments**: Neither macro system supports doc comment tokens -- they are always converted to `#[doc = r"string"]` attribute token streams before being passed to macros.

# Prerequisites

- **rust-reference-overview** -- crate structure (proc macros must be in the crate root)
- **lexical-structure-tokens-and-literals** -- token types and their representations
- **reference-macros-by-example** -- declarative macros for comparison; token conversion rules reference both systems

# Key Properties

1. Proc macros must be defined in the root of a `proc-macro` crate type and cannot be used from the defining crate
2. Function-like proc macros replace the invocation; derive macros append items; attribute macros replace the annotated item
3. Procedural macros are unhygienic -- output is as if written inline at the invocation site
4. The `TokenStream` type is cheap to clone and is the primary interface
5. Multi-character operators are broken into single `Punct` tokens when passed to proc macros
6. Lifetimes are split into `'` + identifier when passed to proc macros, and reassembled when emitted
7. `$crate` becomes a single identifier token when passed to proc macros
8. Derive macro helper attributes are inert and scoped to the item and its inner attributes/fields
9. Attribute macros receive two token streams: the attribute arguments and the annotated item
10. Proc macros have the same security surface as build scripts (file system, network access)

# Construction / Recognition

## Creating a Procedural Macro

1. Create a separate crate with `[lib] proc-macro = true` in Cargo.toml
2. Add `extern crate proc_macro; use proc_macro::TokenStream;`
3. Define a public function in the crate root with the appropriate attribute:
   - `#[proc_macro]` for function-like: `pub fn name(input: TokenStream) -> TokenStream`
   - `#[proc_macro_derive(Name)]` for derive: `pub fn name(input: TokenStream) -> TokenStream`
   - `#[proc_macro_attribute]` for attribute: `pub fn name(attr: TokenStream, item: TokenStream) -> TokenStream`
4. Use absolute paths in generated code for hygiene safety
5. The function must use Rust ABI (no `extern "C"` or other ABIs) and no other qualifiers (not `async`, not `unsafe`)

## Choosing the Right Flavor

1. **Function-like**: When you need custom syntax that replaces the invocation entirely
2. **Derive**: When you need to generate implementations or companion items for a struct/enum/union without modifying it
3. **Attribute**: When you need to transform or wrap an existing item

# Context & Application

Procedural macros represent Rust's most powerful metaprogramming mechanism. They can perform arbitrary computation at compile time, including file I/O, network access, and code generation. The Reference perspective focuses on the formal rules governing their definition, invocation, and token handling.

The token conversion rules between declarative and procedural macros are a critical interoperability concern. When a `macro_rules!` macro forwards tokens to a proc macro (or vice versa), the conversions described above ensure consistent behavior but can produce surprising results -- for example, the operator `+=` arriving as two separate `Punct` tokens (`+` and `=`).

The unhygienic nature of procedural macros is a significant difference from declarative macros. While `macro_rules!` macros have mixed-site hygiene that prevents accidental variable capture, proc macros must manually ensure name isolation. This is why `syn` and `quote` (popular proc macro libraries) default to using absolute paths.

The requirement that proc macros live in a separate crate is a compile-time architecture constraint: the proc macro code must be compiled and executed before the crate that uses it can be compiled. This creates a dependency ordering that affects build parallelism and crate organization.

# Examples

**Example 1** (Function-like Procedural Macro):
```rust,ignore
// In proc-macro crate:
#[proc_macro]
pub fn make_answer(_item: TokenStream) -> TokenStream {
    "fn answer() -> u32 { 42 }".parse().unwrap()
}

// In user crate:
make_answer!();
fn main() { println!("{}", answer()); } // prints 42
```

**Example 2** (Derive Macro with Helper Attribute):
```rust,ignore
// In proc-macro crate:
#[proc_macro_derive(WithHelperAttr, attributes(helper))]
pub fn derive_with_helper(_item: TokenStream) -> TokenStream {
    TokenStream::new()
}

// In user crate:
#[derive(WithHelperAttr)]
struct Struct {
    #[helper] field: (),  // helper attribute consumed by derive macro
}
```

**Example 3** (Attribute Macro):
```rust,ignore
// In proc-macro crate:
#[proc_macro_attribute]
pub fn show_streams(attr: TokenStream, item: TokenStream) -> TokenStream {
    println!("attr: \"{attr}\"");
    println!("item: \"{item}\"");
    item
}

// In user crate:
#[show_streams(bar)]
fn invoke() {}
// Compiler output during compilation:
//   attr: "bar"
//   item: "fn invoke() {}"
```

**Example 4** (Token Conversion): When `$crate::my_macro!(a += b)` is passed to a proc macro, the proc macro sees: the identifier for `$crate`, `::`, identifier `my_macro`, `!`, `(`, identifier `a`, punct `+`, punct `=`, identifier `b`, `)`. The `+=` is split into two punctuation tokens.

# Relationships

## Builds Upon
- **rust-reference-overview** -- crate type system, module structure
- **lexical-structure-tokens-and-literals** -- token types that proc macros operate on
- **reference-macros-by-example** -- declarative macro tokens for understanding conversion rules

## Enables
(none in this extraction set)

## Related
- **reference-macros-by-example** -- the other macro system with different hygiene and token models

## Contrasts With
- **reference-macros-by-example** -- declarative macros use pattern matching; proc macros use arbitrary code. Declarative macros have mixed-site hygiene; proc macros are unhygienic. Declarative macros see multi-character operators as single tokens; proc macros see individual punctuation characters.

# Common Errors

- **Error**: Defining a procedural macro and trying to use it in the same crate.
  **Correction**: Proc macros can only be used from other crates. Move the macro definition to a separate `proc-macro` crate.

- **Error**: Using relative paths (e.g., `Option` instead of `::std::option::Option`) in generated code.
  **Correction**: Since proc macros are unhygienic, relative paths resolve at the invocation site where different items may be in scope. Always use absolute paths in generated code.

- **Error**: Expecting a derive macro's output to replace the original struct/enum.
  **Correction**: Derive macro output is **appended after** the original item, not substituted for it. The original item remains unchanged. Only attribute macros replace their target.

# Common Confusions

- **Confusion**: Thinking proc macros operate on ASTs like compiler plugins.
  **Clarification**: Proc macros operate on **token streams**, not ASTs. `TokenStream` is a flat sequence of tokens. Libraries like `syn` parse token streams into AST-like structures, but the proc macro interface itself is token-level.

- **Confusion**: Thinking multi-character operators (like `+=`, `->`, `::`) arrive as single tokens in proc macros.
  **Clarification**: Multi-character operators are broken into individual `Punct` tokens when passed to proc macros. The `Spacing` field on `Punct` indicates whether the next character is also punctuation (enabling reconstruction of multi-character operators). When emitted back, adjacent punctuation is glued back into multi-character operators.

- **Confusion**: Thinking derive macro helper attributes are active attributes that trigger behavior.
  **Clarification**: Helper attributes are **inert** -- they do not trigger any behavior on their own. They exist so the derive macro can inspect them when processing the token stream. They are visible to all macros but only meaningful to the declaring derive macro.

# Source Reference

Chapter 3 (Macros): Procedural macros -- definition requirements (crate type, root location, cannot self-use), security model (same resources as compiler). The `proc_macro` crate -- `TokenStream` type, `Span` type, `TokenTree` variants. Function-like macros -- `#[proc_macro]` attribute, signature, invocation positions. Derive macros -- `#[proc_macro_derive]` attribute, input/output semantics (append not replace), helper attributes (declaration, scope, inert nature). Attribute macros -- `#[proc_macro_attribute]` attribute, two-argument signature, invocation positions, replacement semantics. Hygiene -- unhygienic nature, absolute path recommendation. Token conversion -- detailed rules for passing between declarative and procedural macro systems, `Delimiter::None` wrapping, doc comment conversion.

# Verification Notes

- Definition source: Direct synthesis from Ch. 3, procedural macros section (407 lines)
- Key Properties: All items directly from normative text; token conversion rules are detailed and verbatim
- Confidence rationale: HIGH -- formal definitions with explicit rules and examples
- Uncertainties: The `Span` API is described as opaque; its exact capabilities may evolve
- Cross-reference status: All slugs reference cards in this Reference extraction set
