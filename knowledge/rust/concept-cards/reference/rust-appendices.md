---
concept: Reference Appendices
slug: rust-appendices
category: reference
subcategory: appendices
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Appendices"
chapter_number: 21
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Rust glossary"
  - "Rust keyword index"
  - "Rust operator precedence"
  - "Rust syntax index"
  - "Rust influences"
  - "macro follow-set ambiguity"
prerequisites: []
extends: []
related:
  - rust-unsafety-reference
  - rust-linkage
contrasts_with: []
answers_questions:
  - "What are the formal definitions of common Rust terms (DST, soundness, turbofish, etc.)?"
  - "What languages influenced Rust's design?"
  - "What is the formal specification for macro follow-set ambiguity rules?"
  - "What are all the keywords, operators, and syntactic forms in Rust?"
  - "What are the FIRST, LAST, and FOLLOW set rules for macro matchers?"
---

# Quick Definition

The Reference appendices provide the Rust glossary (defining ~40 terms), a comprehensive syntax index (keywords, operators, expressions, items, types, patterns), the formal specification for macro follow-set ambiguity rules (FIRST/LAST/FOLLOW sets), and a catalog of Rust's design influences from other programming languages.

# Core Definition

**Glossary** (~40 terms): The glossary provides canonical definitions for fundamental Rust concepts. Key entries include:

- **ABI (Application Binary Interface)**: Defines how compiled code interacts -- calling conventions (argument passing, return values, stack cleanup) and unwinding behavior (e.g., `"C-unwind"` allows unwinding, `"C"` does not)
- **Blanket implementation**: `impl<T> Foo for T` where a type appears uncovered. `impl<T> Bar<Vec<T>> for Vec<T>` is NOT a blanket impl because `T` is covered by `Vec`
- **Dispatch**: Static vs. dynamic dispatch. Rust supports dynamic dispatch via trait objects
- **DST (Dynamically Sized Type)**: A type without statically known size or alignment
- **Dyn-compatible traits** (formerly "object safe"): Traits usable in `dyn Trait` types, following specific rules
- **Entity**: A language construct referable via a path -- types, items, generic parameters, variable bindings, loop labels, lifetimes, fields, attributes, lints
- **Fundamental type constructors**: `&`, `&mut`, `Box`, `Pin` -- blanket impls over these are breaking changes; when `T` is local, these wrapping `T` are also local
- **Inhabited/Uninhabited**: A type is inhabited if it has constructors; `!` and `enum Never {}` are uninhabited
- **Local type/trait**: Defined in the current crate. `struct Foo` is local but `Vec<Foo>` is not. Type aliases do not affect locality
- **Nominal types**: Types referable by path -- enums, structs, unions, trait object types
- **Scrutinee**: The expression matched on in `match` expressions
- **Size**: How much memory to allocate, OR offset between successive array elements. Always a multiple of alignment, including zero
- **Sound/Unsound**: Sound unsafe code means no safe caller can trigger UB; unsound means safe code can cause UB
- **Turbofish**: `::< >` syntax for generic arguments in expressions, required to disambiguate from comparison operators

**Syntax Index**: Comprehensive tables covering:
- All keywords with their uses (including reserved keywords like `abstract`, `become`, `box`, `yield`)
- All operators and punctuation with usage contexts
- Comment types, token forms, macro syntax, attribute syntax
- Expression forms, item forms, type expression forms, pattern forms

**Macro Follow-Set Ambiguity** (formal specification from RFC 550): Defines FIRST(M), LAST(M), and FOLLOW(M) sets for macro matchers with three invariants that valid matchers must satisfy:
1. For successive token sequences, FOLLOW of the first must contain FIRST of the second
2. Separated complex NTs must use separator tokens from the FOLLOW set
3. Unseparated repeating (`*`/`+`) complex NTs must have FOLLOW containing FIRST (currently unenforced)

Follow sets for fragment specifiers: `pat` -> `{=>  , = | if in}`, `expr`/`stmt` -> `{=> , ;}`, `ty`/`path` -> `{{ [ , => : = > >> ; | as where}` plus block NTs.

**Influences**: Design elements drawn from SML/OCaml (ADTs, pattern matching, type inference), C++ (references, RAII, move semantics, memory model), Haskell (typeclasses, type families), Erlang (message passing, thread failure), Swift (optional bindings), Scheme (hygienic macros), C# (attributes), Ruby (closure syntax), and others.

# Prerequisites

Broad familiarity with Rust syntax and concepts. The macro follow-set specification requires understanding of formal language theory (sets, grammars, tokens).

# Key Properties

1. The glossary distinguishes "blanket implementation" (`impl<T> Foo for T`) from non-blanket (all type parameters covered)
2. Fundamental type constructors (`&`, `&mut`, `Box`, `Pin`) cannot cover other types for orphan rule purposes
3. A type's size may be zero and can change between compiler versions and target platforms
4. "Dyn-compatible" is the new terminology for "object safe" traits
5. The turbofish (`::< >`) is required because without it, expressions like `f(a<b, c>d)` would be ambiguous
6. FOLLOW sets for macro fragment specifiers are carefully restricted to prevent future syntax additions from breaking existing macros
7. The third macro matcher invariant (unseparated repetition FIRST/FOLLOW) is currently unenforced due to historical oversight
8. Reserved keywords (`abstract`, `become`, `box`, `do`, `final`, `gen`, `macro`, `override`, `priv`, `try`, `typeof`, `unsized`, `virtual`, `yield`) cannot be used as identifiers
9. Rust's algebraic data types and pattern matching come from ML (SML, OCaml); its RAII, move semantics, and memory model from C++
10. The `safe` keyword (for extern block functions and statics) and `unsafe` keyword (9 uses) are both indexed in the syntax table

# Construction / Recognition

## Using the Glossary

The glossary is a definitional reference, not a learning resource. Use it to:
1. Verify precise definitions when writing documentation
2. Resolve ambiguity about terms like "blanket implementation" vs "inherent implementation"
3. Understand the orphan rule implications of "local type," "uncovered type," and "fundamental type constructor"
4. Distinguish "inhabited" from "uninhabited" types

## Using Macro Follow-Set Rules

To verify a macro matcher is valid:
1. Compute FIRST and LAST sets for each sub-matcher
2. Verify all three invariants hold
3. Pay special attention to fragment specifier follow sets (e.g., `$ty:ty` can only be followed by `{`, `[`, `,`, `=>`, `:`, `=`, `>`, `>>`, `;`, `|`, `as`, `where`, or block NTs)

Invalid: `($ty:ty < foo ,)` because `<` is not in FOLLOW(`ty`)
Valid: `($ty:ty , foo <)` because `,` is in FOLLOW(`ty`)

# Context & Application

The appendices serve as reference material rather than conceptual content, but they contain information found nowhere else in the Reference. The glossary's definitions of "blanket implementation," "fundamental type constructor," "local type," and "uncovered type" are essential for understanding Rust's orphan rules and coherence system. The macro follow-set specification is the authoritative source for understanding why certain macro patterns are rejected by the compiler and how Rust prevents future syntax additions from breaking existing macros (the "macro future-proofing" design from RFC 550).

The influences section documents Rust's intentional design as a synthesis language rather than a novel one -- understanding the source languages helps predict Rust's behavior and idioms.

# Examples

**Example 1** (Blanket vs. non-blanket implementation):
```rust
// Blanket impl: T appears uncovered
impl<T> Display for MyWrapper<T> where T: Display { /* ... */ }

// NOT a blanket impl: all T instances covered by Vec
// impl<T> Bar<Vec<T>> for Vec<T> { }
```

**Example 2** (Macro follow-set validation):
```rust
// VALID: `,` is in FOLLOW(ty)
macro_rules! ok { ($ty:ty , $rest:expr) => { $rest } }

// INVALID: `<` is not in FOLLOW(ty)
// macro_rules! bad { ($ty:ty < $rest:expr) => { $rest } }
// ERROR: `$ty:ty` is followed by `<`, which is not allowed
```

**Example 3** (Turbofish disambiguation):
```rust
let ok_num = Ok::<_, ()>(5);
let vec = [1, 2, 3].iter().map(|n| n * 2).collect::<Vec<_>>();
// Without `::`, `collect<Vec<_>>()` would parse ambiguously
```

# Relationships

## Builds Upon
(none -- appendices are standalone reference material)

## Enables
- Understanding orphan rules and coherence (via glossary definitions)
- Writing correct macro matchers (via follow-set specification)
- Understanding Rust's design philosophy (via influences)

## Related
- **rust-unsafety-reference** -- glossary defines "undefined behavior," "sound," "unsound"
- **rust-linkage** -- glossary cross-references crate types

## Contrasts With
(none)

# Common Errors

- **Error**: Writing a macro matcher where a fragment specifier is followed by a token not in its FOLLOW set.
  **Correction**: Check FOLLOW sets: `pat` allows `=> , = | if in`; `expr`/`stmt` allow `=> , ;`; `ty`/`path` allow `{ [ , => : = > >> ; | as where` plus block NTs. Other fragment specifiers (`tt`, `ident`, `block`, `item`, `literal`, `meta`, `lifetime`) allow ANYTOKEN.

- **Error**: Assuming `Vec<LocalType>` is a "local type" for orphan rule purposes.
  **Correction**: Only the struct/enum/union itself is local, not its use as a generic argument. `Vec<Foo>` is NOT local even if `Foo` is. However, `&Foo`, `&mut Foo`, `Box<Foo>`, and `Pin<Foo>` ARE local when `Foo` is, because these are fundamental type constructors.

# Common Confusions

- **Confusion**: Thinking "dyn compatible" and "object safe" are different concepts.
  **Clarification**: "Dyn-compatible" is the new terminology for what was previously called "object safe." They refer to the same set of trait rules for `dyn Trait` usage.

- **Confusion**: Believing the macro follow-set invariants are all enforced.
  **Clarification**: The third invariant (unseparated repetition `*`/`+` requiring FOLLOW to contain FIRST) is currently unenforced due to historical oversight. Macros violating it may become invalid in future editions.

- **Confusion**: Assuming a type's size is fixed across compiler versions.
  **Clarification**: The glossary explicitly states that size "can change depending on compiler version (as new optimizations are made) and target platform." Only types with explicit `repr` guarantees have stable sizes.

# Source Reference

Chapter 21 (Appendices, 1061 lines): Grammar summary, syntax index (keywords, operators/punctuation, comments, tokens, macros, attributes, expressions, items, type expressions, patterns with full cross-reference links), macro follow-set ambiguity formal specification (RFC 550: definitions, matcher invariants, FIRST/LAST/FOLLOW formal definitions and examples), influences (12 source languages), glossary (~40 terms).

# Verification Notes

- Definition source: Direct extraction from Chapter 21 (1061 lines), selectively covering the most reference-valuable content
- Key Properties: Items 1-10 synthesized from glossary entries, syntax tables, and formal specification
- Confidence rationale: HIGH -- appendix content is definitional and well-structured
- Uncertainties: The third macro matcher invariant may be enforced in a future edition (tracking issue open); the influences list may not be exhaustive
- Cross-reference status: Related slugs reference cards in the reference extraction set
