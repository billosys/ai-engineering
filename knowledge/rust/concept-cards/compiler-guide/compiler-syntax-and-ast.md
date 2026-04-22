---
# === CORE IDENTIFICATION ===
concept: Compiler Syntax and AST
slug: compiler-syntax-and-ast

# === CLASSIFICATION ===
category: compiler-internals
subcategory: frontend
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Syntax and the AST"
chapter_number: 13
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust lexer"
  - "Rust parser"
  - "rustc_lexer"
  - "rustc_parse"
  - "AST"
  - "Abstract Syntax Tree"
  - "macro expansion"
  - "macro hygiene"
  - "name resolution"
  - "MBE"
  - "Macros By Example"
  - "procedural macros"
  - "proc macros"
  - "feature gates"
  - "AST validation"
  - "lang items"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-hir
  - compiler-mir
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Rust compiler lex and parse source code into an AST?"
  - "What is a NodeId and why is it problematic for incremental compilation?"
  - "How does macro expansion work in the Rust compiler?"
  - "What is macro hygiene and how are the three expansion hierarchies structured?"
  - "What is the difference between Macros By Example (MBE) and procedural macros?"
  - "How does name resolution work in Rust -- what are namespaces and ribs?"
  - "What is AST validation and when does it run?"
  - "How do feature gates control access to unstable language features?"
  - "What are lang items and how does the compiler use them?"
  - "How does the #[test] attribute transform the crate structure?"
  - "How does the panic machinery work across core and std?"
---

# Quick Definition

The front-end of the Rust compiler transforms raw UTF-8 source code into an Abstract Syntax Tree (AST) through lexing (breaking text into tokens) and parsing (structuring tokens into a tree). The AST then undergoes macro expansion -- an iterative process that resolves macro invocations, integrates their output into the tree, and tracks hygiene information across three hierarchies. Following expansion, name resolution assigns meaning to identifiers across separate namespaces (types, values, macros), and AST validation checks structural constraints. Feature-gate checking ensures unstable features are only used on nightly with explicit opt-in.

# Core Definition

**Lexing** is split between two crates: `rustc_lexer` is a hand-written lexer that breaks `&str` into raw token chunks, and `Lexer` (in `rustc_parse`) adds `Span` information and interns identifiers. **Parsing** (in `rustc_parse`) converts the token stream into the AST, defined in `rustc_ast`. Every AST node receives a `NodeId` -- an identifier unique within a crate, but fragile under insertion/deletion, making it unsuitable for incremental compilation.

**Macro expansion** is driven by `MacroExpander::fully_expand_fragment`, which operates iteratively: (1) resolve imports, (2) collect macro invocations, (3) dequeue and attempt to resolve each one, (4) if resolved, run the expander function to produce tokens or AST fragments and integrate them back. Three sub-passes run on each freshly expanded fragment: `InvocationCollector` assigns `NodeId`s and collects new macro calls; `DefCollector` creates def paths and `DefId`s; `BuildReducedGraphVisitor` puts names into modules. If no progress is made in an iteration, it is a compilation error (with recovery via `ExprKind::Err`).

**Macro hygiene** prevents name collisions through three hierarchies, all rooted at `ExpnId::root`: the *expansion order hierarchy* tracks when a macro invocation appears in the output of another macro; the *macro definition hierarchy* tracks when macro definitions are revealed during expansion, using `SyntaxContext` chains manipulated by `SyntaxContext::apply_mark`; and the *call-site hierarchy* tracks the source location of invocations via `ExpnData::call_site`. A `Span` is a compact representation of a code location plus `SyntaxContext`, and an `Ident` is an interned `Symbol` plus `Span`.

**Macros By Example (MBE)** use an NFA-based regex parser (similar to Earley parsing). The parser matches the token stream against matchers from macro rules, calling back to the normal Rust parser to bind metavariables like `$mvar:ident`. Exactly one rule must match. **Procedural macros** are compiled third-party crates whose annotated functions receive a stable `TokenStream` and return a new one; the unstable internal `TokenStream` is converted via C ABI in `rustc_expand::proc_macro`.

**Name resolution** occurs in two phases: during macro expansion (resolving imports and macro names in `rustc_resolve::macros`) and after full expansion (resolving all names in `rustc_resolve::late`). Names live in separate namespaces (types, values, macros), and visibility is tracked through a stack of `Rib`s -- each `Rib` is pushed when the set of visible names potentially changes (block boundaries, `let` bindings, macro expansion borders).

**AST validation** (in `AstValidator`) runs after macro expansion but before name resolution, performing simple structural checks (e.g., parameter count limits, c-variadic argument placement). **Feature-gate checking** ensures `#![feature(...)]` attributes are validated against unstable/accepted/removed tables, with parser-gated spans checked after parsing and a `PostExpansionVisitor` checking expanded AST constructs. **Lang items** are compiler-pluggable operations marked with `#[lang = "..."]` that connect language constructs (operators, panicking, marker traits) to library implementations.

# Prerequisites

General understanding of how compilers transform source code through successive representations. Familiarity with Rust's macro system at the user level.

# Key Properties

1. **Hand-written lexer**: `rustc_lexer` is not a generated finite state machine but a manually implemented lexer that breaks `&str` into token chunks
2. **NodeId fragility**: Every AST node gets a `NodeId` unique within the crate, but adding or removing any node shifts all subsequent IDs, making them unsuitable for incremental compilation
3. **Iterative macro expansion**: Expansion loops until no unresolved macros remain or no progress can be made; it interleaves with name resolution since macros need import resolution to find their definitions
4. **Three hygiene hierarchies**: Expansion order (nesting of macro outputs), macro definition (nesting of macro definitions, tracked via `SyntaxContext`), and call-site (source location of invocations)
5. **SyntaxContext chaining**: When a token is produced by macro `m`, its context becomes `old_context -> id(m)`, building chains that disambiguate identically named items from different macro scopes
6. **MBE uses NFA-based parsing**: The macro-by-example parser operates like a nondeterministic finite automaton, calling back to the Rust parser for metavariable binding
7. **Stable proc macro interface**: Proc macros use a stable `TokenStream` type (distinct from the compiler's internal `TokenStream`), converted via C ABI boundary
8. **Two-phase name resolution**: Import and macro resolution happens during expansion; full name resolution happens after expansion is complete
9. **Rib-based scoping**: Each namespace maintains an independent stack of `Rib`s representing nested scopes; inner functions (not closures) create opaque ribs that block access to outer locals
10. **Feature gates as a three-table system**: Features are classified as unstable (active), accepted (stabilized), or removed, with `#![feature(...)]` attributes checked against all three tables

# Construction / Recognition

## Lexing and Parsing flow:
1. `rustc_lexer` breaks source `&str` into raw tokens
2. `Lexer` in `rustc_parse` adds `Span` information and interns identifiers
3. `Parser` converts the token stream into an `ast::Crate` (the root AST node)
4. Macro definitions and invocations are set aside during parsing for later expansion

## Macro expansion algorithm:
1. Initialize queue of unresolved macro invocations
2. Loop: resolve imports, collect invocations, dequeue and resolve
3. If resolved: run expander, parse output if needed, create `SyntaxContext`, assign `NodeId`s, create `DefId`s, build module graph
4. If not resolved: re-queue; if no progress overall, error (with recovery)

## Name resolution:
1. Phase 1 (during expansion): resolve imports and macro names via `rustc_resolve::macros`
2. Phase 2 (post-expansion): resolve all names via `rustc_resolve::late`, traversing the AST top-down through `Rib` stacks

# Context & Application

The AST stage is the entry point of the compiler pipeline. Source code -> tokens -> AST -> (macro expansion + name resolution + validation + feature gating) -> ready for lowering to HIR. Understanding this stage is essential for:

- Contributing to the parser or macro expander
- Debugging macro hygiene issues (which hierarchy is relevant, how `SyntaxContext` chains form)
- Understanding why `NodeId` is replaced by `DefId` and `HirId` in later stages
- Adding new syntax or feature gates
- Working with proc macros or custom derives at the compiler level

# Examples

**Example 1** (Ch. 13, "Hygiene -- Expansion Order Hierarchy"):
```rust,ignore
macro_rules! foo { () => { println!(); } }
fn main() { foo!(); }
```
The final AST nodes have hierarchy `root -> id(foo) -> id(println)`.

**Example 2** (Ch. 13, "Hygiene -- Macro Definition Hierarchy"):
```rust,ignore
macro m() { macro n() { ident } }
m!();
n!();
```
After expansion, `ident` has SyntaxContext `ROOT -> id(m) -> id(n)`.

**Example 3** (Ch. 13, "Macros By Example"):
```rust,ignore
macro_rules! printer {
    (print $mvar:ident) => { println!("{}", $mvar); };
    (print twice $mvar:ident) => {
        println!("{}", $mvar);
        println!("{}", $mvar);
    };
}
printer!(print foo); // Matches first arm, expands to println!("{}", foo)
```

**Example 4** (Ch. 13, "Ribs and Scoping"):
```rust,ignore
fn do_something<T: Default>(val: T) { // Rib 1
    let helper = || { /* val accessible */ }; // Rib 2
    fn helper() { /* val NOT accessible -- opaque rib */ } // Rib 4
    let val = T::default(); // Rib 5 -- shadows parameter
}
```

**Example 5** (Ch. 13, "The #[test] attribute"): The `#[test]` attribute works as a syntactic transformation that (1) creates `__test_reexports` modules to expose private tests, (2) generates a `main` function calling `test::test_main_static`, and (3) produces `TestDescAndFn` instances encoding test metadata like `should_panic`.

# Relationships

## Builds Upon
(none -- this is the first stage of the compiler pipeline)

## Enables
- **compiler-hir** -- the fully expanded, name-resolved AST is lowered to HIR via `rustc_ast_lowering`
- **rustdoc-internals** -- rustdoc starts from the compiler's HIR, which is derived from this AST stage

## Related
- **compiler-mir** -- several stages downstream; MIR is built from THIR which is built from HIR which is lowered from AST

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Attempting to use `NodeId` for incremental compilation or cross-compilation-session identity.
  **Correction**: `NodeId`s are fragile -- adding or removing any AST node shifts subsequent IDs. Use `DefId` (stable across compilations) or `HirId` (stable within a crate) instead, which are assigned during lowering.

- **Error**: Writing ambiguous macro rules where more than one arm matches an invocation.
  **Correction**: The MBE parser requires exactly one matching arm. Multiple matches produce an ambiguity error. Rewrite rules to be mutually exclusive, typically by making distinguishing tokens appear earlier in the pattern.

- **Error**: Expecting proc macros to have access to the compiler's internal `TokenStream` type.
  **Correction**: Proc macros use the stable `proc_macro::TokenStream`. The compiler converts between the internal and stable representations via C ABI in `rustc_expand::proc_macro`.

# Common Confusions

- **Confusion**: Macro expansion and name resolution are separate, sequential phases.
  **Clarification**: They are interleaved. Macro expansion requires name resolution to find macro definitions and imports, while name resolution needs macro expansion to reveal new names. The iterative `fully_expand_fragment` algorithm handles this mutual dependency.

- **Confusion**: Rust macros are textual substitution like C preprocessor macros.
  **Clarification**: Rust macros operate on token trees (not raw text) and implement three levels of hygiene tracking to prevent name collisions. A macro-introduced binding cannot shadow or be shadowed by user code in ways that cause silent bugs.

- **Confusion**: The three hygiene hierarchies serve the same purpose.
  **Clarification**: They track different things: expansion order tracks nesting of macro outputs; macro definition hierarchy tracks nesting of macro definitions (for resolving which names are visible); call-site hierarchy tracks where invocations appear in source (for error reporting and backtrace generation).

# Source Reference

Chapter 13 of the Rust Compiler Dev Guide (1535 lines). Covers: source code representation overview, lexing (`rustc_lexer`, `Lexer`), parsing (`rustc_parse`, `Parser`, `NodeId`), macro expansion algorithm (`fully_expand_fragment`, error recovery, eager expansion), hygiene and the three hierarchies (`ExpnId`, `SyntaxContext`, `Span`), MBE parsing (NFA-based, metavariable binding, `ParseResult`), procedural macros (stable `TokenStream`, C ABI conversion), name resolution (two phases, namespaces, `Rib`s, speculative crate loading), attributes (builtin/inert vs active/non-builtin), the `#[test]` attribute (re-exporting, harness generation, test object generation), panic machinery (`core`-to-`std` bridge, panic runtimes), AST validation (`AstValidator`), feature-gate checking (definitions, collection, parser gating, `PostExpansionVisitor`), and lang items.

# Verification Notes

- Definition source: Directly extracted from Chapter 13 sections on lexing, parsing, macro expansion, hygiene, name resolution, AST validation, feature gates, and lang items
- Key Properties: All derived from explicit descriptions and code examples in the source text
- Confidence rationale: HIGH -- official compiler team documentation; core compiler pipeline concepts
- Uncertainties: Some hygiene details (e.g., "context transplantation hack" for MBE/modern macro interactions) are described as interim solutions subject to change
- Cross-reference status: Directly enables the HIR card; referenced by MIR and rustdoc cards
