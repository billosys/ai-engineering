---
concept: Macros by Example (Declarative Macros)
slug: reference-macros-by-example
category: language-specification
subcategory: macros
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Macros"
chapter_number: 3
pdf_page: null
section: "Macro invocation / Macros by example"
extraction_confidence: high
aliases:
  - "macro_rules!"
  - "declarative macros"
  - "macros by example"
  - "metavariables"
  - "fragment specifiers"
  - "macro repetitions"
  - "macro hygiene"
  - "macro scoping"
  - "$crate"
  - "macro_export"
  - "macro_use"
  - "follow-set ambiguity"
prerequisites:
  - rust-reference-overview
  - lexical-structure-input-and-keywords
  - lexical-structure-tokens-and-literals
extends: []
related:
  - reference-procedural-macros
contrasts_with:
  - reference-procedural-macros
answers_questions:
  - "How are macro invocations structured in Rust?"
  - "Where can macros be invoked?"
  - "How do macro_rules! matchers and transcribers work?"
  - "What are the fragment specifier types?"
  - "How do macro repetitions work?"
  - "What is textual scope vs path-based scope for macros?"
  - "How does macro_export make macros available?"
  - "What is macro hygiene for declarative macros?"
  - "What does $crate refer to?"
  - "What are the follow-set ambiguity restrictions?"
  - "How does macro name resolution work?"
---

# Quick Definition

Declarative macros (`macro_rules!`) define syntax extensions by pattern matching: each macro has one or more rules with a matcher (pattern) and transcriber (replacement). Matchers bind Rust syntax fragments to metavariables using fragment specifiers (`expr`, `ty`, `ident`, `tt`, etc.). Macros have mixed-site hygiene, two scoping mechanisms (textual and path-based), and are subject to follow-set ambiguity restrictions that ensure forward compatibility with language evolution.

# Core Definition

## Macro Invocation

A macro invocation has the form `SimplePath ! DelimTokenTree` -- a path, an exclamation mark, and a delimited token tree using `()`, `[]`, or `{}`. Macros may be invoked in expressions, statements, patterns, types, items (including associated items), `macro_rules` transcribers, and external blocks. When used as an item or statement, a semicolon is required at the end unless curly braces are used. Visibility qualifiers are never allowed before a macro invocation.

Macro name resolution uses two kinds of scope: **textual scope** and **path-based scope**. When invoked by an unqualified identifier, textual scope is tried first; if nothing is found, path-based scope is tried. When qualified with a path (e.g., `self::my_macro!()`), only path-based scope is used.

## Matchers and Transcribers

Each `macro_rules!` definition has one or more rules. The macro expander tries each rule in order and **transcribes the first successful match** -- if this results in an error, future matches are not tried. **No lookahead is performed**: the compiler must unambiguously determine how to parse the invocation one token at a time, or it is an error. The outer delimiters of the matcher match any pair of delimiters (so matcher `(())` matches `{()}` but not `{{}}`). The `$` character cannot be matched or transcribed literally.

## Metavariables and Fragment Specifiers

In the matcher, `$name:fragment_specifier` binds a syntax fragment to a metavariable. The 15 fragment specifiers are:

- `block` -- a block expression
- `expr` -- an expression (2024+ includes underscore and const block expressions)
- `expr_2021` -- an expression excluding underscore and const block expressions (backward compatibility)
- `ident` -- an identifier or keyword (except `_`), raw identifier, or `$crate`
- `item` -- an item
- `lifetime` -- a lifetime token
- `literal` -- an optional `-` followed by a literal expression
- `meta` -- the contents of an attribute
- `pat` -- a pattern (2021+ includes top-level or-patterns)
- `pat_param` -- a pattern without top-level or-patterns
- `path` -- a TypePath-style path
- `stmt` -- a statement without trailing semicolon
- `tt` -- a single token or a delimited token tree
- `ty` -- a type
- `vis` -- a possibly empty visibility qualifier

**Fragment forwarding**: When a matched fragment is forwarded to another macro, the second macro sees an opaque AST and can only match it with the same fragment specifier type. Exceptions: `ident`, `lifetime`, and `tt` fragments can be matched by literal tokens in the second macro.

The `$crate` metavariable refers to the crate defining the macro and can be used at the start of paths to reference items not in scope at the invocation site. It must use a fully qualified module path when referring to non-macro items (e.g., `$crate::inner::foo()`).

## Repetitions

Repetitions use the syntax `$( ... ) separator? operator` where the operator is `*` (zero or more), `+` (one or more), or `?` (zero or one). The separator can be any token except a delimiter or repetition operator; `;` and `,` are most common. `?` cannot be used with a separator. Nested repetitions are permitted.

In transcribers: (1) metavariables must appear in the same nesting order and kind of repetitions as in the matcher; (2) each repetition must contain at least one metavariable to determine expansion count; (3) multiple metavariables in the same repetition must bind the same number of fragments.

## Scoping

**Textual scope**: Based on source order, like `let` bindings. A macro enters scope after its `macro_rules!` definition and exits when its surrounding scope (typically a module) closes. Can span child modules and even across files. Multiple definitions of the same macro shadow previous ones. Textual scope shadows path-based scope.

**Path-based scope**: Achieved via `#[macro_export]` (makes the macro available from the crate root with `pub` visibility) or `pub use` re-exports. By default, macros have no path-based scope. Macros have an implicit visibility of `pub(crate)`; `#[macro_export]` changes this to `pub`.

**`macro_use` attribute**: On modules, extends the macro's textual scope beyond the module. On `extern crate`, imports exported macros into the `macro_use` prelude (not textual scope), where they can be shadowed by other names. `macro_use` on `extern crate self` is not allowed.

**`macro_export` attribute**: Exports the macro from the crate root for path-based resolution and cross-crate use. The `local_inner_macros` option adds implicit `$crate::` to single-segment macro invocations within the macro body (discouraged in new code).

## Hygiene

Declarative macros have **mixed-site hygiene**: loop labels, block labels, and local variables are looked up at the **definition site**, while other symbols (functions, types, etc.) are looked up at the **invocation site**. Labels and local variables defined in macro expansion are not shared between separate invocations of the same macro.

## Follow-Set Ambiguity Restrictions

To ensure forward compatibility, metavariables must be followed by specific tokens:
- `expr`, `stmt`: only `=>`, `,`, or `;`
- `pat_param`: only `=>`, `,`, `=`, `|`, `if`, or `in`
- `pat`: only `=>`, `,`, `=`, `if`, or `in` (pre-2021: also `|`)
- `path`, `ty`: only `=>`, `,`, `=`, `|`, `;`, `:`, `>`, `>>`, `[`, `{`, `as`, `where`, or a `block` metavariable
- `vis`: only `,`, a non-raw `priv` identifier, tokens that can begin a type, or `ident`/`ty`/`path` metavariables
- All other specifiers: no restrictions

# Prerequisites

- **rust-reference-overview** -- grammar notation for reading formal productions
- **lexical-structure-input-and-keywords** -- keywords and identifiers used in macro definitions
- **lexical-structure-tokens-and-literals** -- token tree structure, `tt` fragment meaning

# Key Properties

1. Macro expansion tries rules in order; the first successful match is used and errors do not fall through to subsequent rules
2. No lookahead is performed -- ambiguous invocations are compilation errors
3. The 15 fragment specifiers cover all major Rust syntax categories
4. Fragment forwarding produces opaque ASTs except for `ident`, `lifetime`, and `tt`
5. Textual scope takes priority over path-based scope for unqualified macro invocations
6. `#[macro_export]` promotes a macro from `pub(crate)` to `pub` and places it in the crate root
7. Mixed-site hygiene: local variables use definition site, functions/types use invocation site
8. `$crate` enables cross-crate macro correctness by referring to the defining crate
9. Follow-set restrictions on `expr`, `stmt`, `pat`, `path`, and `ty` prevent future language changes from breaking existing macros
10. Repetition metavariables in transcribers must match the same nesting structure as in matchers

# Construction / Recognition

## Writing a Declarative Macro

1. Define rules with `macro_rules! name { (matcher) => { transcriber }; ... }`
2. Use fragment specifiers to bind syntax fragments: `$x:expr`, `$name:ident`, etc.
3. Use repetitions for variable-length input: `$( $item:expr ),*`
4. Choose the most specific fragment specifier possible (e.g., `pat_param` over `pat` if top-level or-patterns are not needed)
5. Ensure follow tokens after metavariables comply with the follow-set restrictions
6. Use `$crate::` for reliable cross-crate references to items in the defining crate
7. Apply `#[macro_export]` to make the macro available outside the crate

## Resolving Macro Scope Issues

1. For unqualified invocation failures: check that the `macro_rules!` definition appears textually before the invocation
2. For path-based invocation: ensure `#[macro_export]` is applied or the macro is re-exported with `pub use`
3. For cross-crate use: either use path-based import (`use crate::macro_name`) or `#[macro_use] extern crate`
4. Remember: textual bindings shadow path-based bindings

# Context & Application

Declarative macros are Rust's primary mechanism for syntactic abstraction within the language itself. They operate at the token level and are expanded before semantic analysis, making them powerful for code generation, DSLs, and boilerplate reduction. The Reference perspective focuses on the formal rules -- the grammar, scoping semantics, hygiene model, and forward-compatibility constraints -- rather than practical usage patterns.

The follow-set restrictions are a key design decision: they sacrifice some macro expressiveness to ensure that future Rust syntax extensions (like new expression forms starting with `[`) cannot silently change the meaning of existing macros. This is why `$i:expr [,]` is rejected even though it would be unambiguous today.

The mixed-site hygiene model is simpler than full hygiene (as in Scheme macros) but more principled than C preprocessor textual substitution. It prevents accidental variable capture while allowing macros to refer to items visible at the call site.

# Examples

**Example 1** (Basic Macro with Repetition):
```rust
macro_rules! vec_of_strings {
    ( $( $s:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push(String::from($s)); )*
            v
        }
    };
}
let v = vec_of_strings!["hello", "world"];
```

**Example 2** (Hygiene -- Mixed-Site Lookup):
```rust
let x = 1;
fn func() { unreachable!("never called") }

macro_rules! check {
    () => {
        assert_eq!(x, 1); // x from definition site
        func();           // func from invocation site
    };
}

{
    let x = 2;            // This x is NOT seen by the macro
    fn func() {}          // This func IS seen by the macro
    check!();
}
```

**Example 3** (Scoping -- Textual vs Path-Based):
```rust,ignore
use lazy_static::lazy_static; // Path-based import

macro_rules! lazy_static {    // Textual definition
    (lazy) => {};
}

lazy_static!{lazy}            // Textual lookup wins
self::lazy_static!{}          // Path-based lookup ignores textual, finds import
```

**Example 4** ($crate for Cross-Crate References):
```rust
pub mod inner {
    #[macro_export]
    macro_rules! call_foo {
        () => { $crate::inner::foo() };
    }
    pub fn foo() {}
}
```

# Relationships

## Builds Upon
- **rust-reference-overview** -- grammar notation
- **lexical-structure-tokens-and-literals** -- token trees, literal tokens

## Enables
(none in this extraction set -- enables downstream use of macro-generated code)

## Related
- **reference-procedural-macros** -- the other macro system; proc macros see different token representations

## Contrasts With
- **reference-procedural-macros** -- declarative macros use pattern matching on token trees; procedural macros use arbitrary Rust code operating on token streams. Declarative macros have mixed-site hygiene; procedural macros are unhygienic.

# Common Errors

- **Error**: Expecting macro rules to fall through on error (like match arms).
  **Correction**: The macro expander takes the first successful match. If transcription of that match produces an error, subsequent rules are NOT tried. Order rules from most specific to most general.

- **Error**: Forwarding a matched `expr` fragment to another macro that expects to match it literally.
  **Correction**: Forwarded fragments (except `ident`, `lifetime`, `tt`) are opaque ASTs. The receiving macro can only match them with the same fragment specifier. Use `tt` if literal token matching is needed in the second macro.

- **Error**: Using `$i:expr` followed by `[` in a matcher.
  **Correction**: Follow-set restrictions require `expr` to be followed only by `=>`, `,`, or `;`. Use a different fragment specifier or restructure the matcher.

# Common Confusions

- **Confusion**: Thinking `$crate` is always available or refers to the invoking crate.
  **Clarification**: `$crate` refers to the crate where the macro is **defined**, not where it is invoked. It is only available inside `macro_rules!` definitions and enables reliable cross-crate item references.

- **Confusion**: Thinking textual and path-based scope are the same thing.
  **Clarification**: Textual scope is based on source order (like `let` bindings). Path-based scope uses the module system. A macro can have textual scope without path-based scope (the default), or both (with `#[macro_export]`). Textual scope shadows path-based scope for unqualified invocations.

- **Confusion**: Believing `macro_rules!` macros are hygienic like Scheme macros.
  **Clarification**: They have **mixed-site** hygiene: local variables and labels use the definition site (hygienic), but item-level names (functions, types, modules) use the invocation site (unhygienic for items). This means a macro can accidentally shadow or reference unintended items at the call site.

# Source Reference

Chapter 3 (Macros): Macro invocation -- syntax, positions, name resolution. Macros by example -- `macro_rules!` syntax, matchers and transcribers, no-lookahead rule, fragment forwarding. Metavariables -- 15 fragment specifiers with detailed definitions, `$crate`, edition-specific changes (2021 `pat`, 2024 `expr`). Repetitions -- operators, separators, nesting rules, transcription constraints. Scoping -- textual scope (source order, shadowing, cross-file), path-based scope (`macro_export`, `use` re-exports, visibility). `macro_use` and `macro_export` attributes with all sub-rules. Hygiene -- mixed-site model, `$crate` semantics, visibility constraints. Follow-set ambiguity restrictions -- per-specifier follow token requirements.

# Verification Notes

- Definition source: Direct synthesis from Ch. 3, sections on macro invocation (122 lines) and macros by example (740+ lines)
- Key Properties: All items are directly from normative text; fragment specifier list and follow-set restrictions are verbatim
- Confidence rationale: HIGH -- formal grammar productions and explicit normative rules
- Uncertainties: None significant; the `local_inner_macros` feature is discouraged but not deprecated
- Cross-reference status: All slugs reference cards in this Reference extraction set
