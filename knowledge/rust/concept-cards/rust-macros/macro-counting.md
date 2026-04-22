---
concept: Macro Counting Techniques
slug: macro-counting
category: macro-building-blocks
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "04-building-blocks"
chapter_number: 4
pdf_page: null
section: "Counting"
extraction_confidence: high
aliases:
  - "count_tts"
  - "counting tokens"
  - "macro token counting"
  - "compile-time counting"
prerequisites:
  - macro-rules
  - macro-repetition
  - repetition-replacement
  - token-tree
extends:
  - macro-repetition
related:
  - repetition-replacement
  - tt-muncher
  - push-down-accumulation
contrasts_with: []
answers_questions:
  - "How do you count the number of tokens in a macro input?"
  - "What are the trade-offs between different counting approaches?"
  - "How do you get a compile-time constant count from a macro?"
  - "Why does counting in macros crash the compiler with large inputs?"
---

# Quick Definition

Counting tokens in `macro_rules!` is surprisingly difficult. The source presents four techniques with different trade-offs: repetition with replacement (simple but limited to ~500 tokens), recursion (extendable but hits recursion limits), slice length (handles 10,000+ tokens but not `const`), and enum counting (produces `const` but only works with distinct identifiers).

# Core Definition

"Counting things in a macro is a surprisingly tricky task." The source presents four approaches:

1. **Repetition with replacement**: Uses `replace_expr!` to map each token to `1usize` and sums them. Simple but produces a deeply unbalanced AST that crashes the compiler around 500 tokens.

2. **Recursion**: Peels off one token at a time, adding `1usize +` at each step. Hits the recursion limit trivially, but can be extended by matching multiple tokens per step (up to ~1,200 tokens with batches of 20).

3. **Slice length**: Constructs an array of unit values and calls `.len()`. Works up to 10,000+ tokens but cannot produce a constant expression.

4. **Enum counting**: Creates a hidden enum with one variant per identifier plus a sentinel, then uses the sentinel's discriminant as the count. Produces a constant but only works with distinct, non-keyword identifiers.

# Prerequisites

- **macro_rules!** -- all counting techniques use declarative macros
- **Macro repetition** -- most techniques operate on repetition-matched sequences
- **Repetition replacement** -- the `replace_expr!` helper is used by two of the four techniques
- **Token trees** -- tokens are captured as `tt` for counting

# Key Properties

1. No single technique is optimal for all cases -- each has distinct limitations
2. Repetition with replacement: `0usize $(+ replace_expr!($tts 1usize))*` -- crashes at ~500 tokens
3. Recursion: `1usize + count_tts!($($tail)*)` -- hits recursion limit, extendable with multi-token matching
4. Slice length: `<[()]>::len(&[$(replace_expr!($tts ())),*])` -- scales to 10,000+ but not `const`
5. Enum counting: creates `enum { variants..., __Last }` -- produces `const` but requires distinct identifiers
6. The compiler has performance problems with large numbers of untyped integer literals -- always use explicitly typed `usize` literals

# Construction / Recognition

## To Construct (recommended approach -- slice length):
1. Define `replace_expr!`: `macro_rules! replace_expr { ($_t:tt $sub:expr) => {$sub}; }`
2. Define the counter: `macro_rules! count_tts { ($($tts:tt)*) => {<[()]>::len(&[$(replace_expr!($tts ())),*])}; }`
3. Use: `count_tts!(a b c)` evaluates to `3usize`

## To Construct (constant result -- enum counting):
1. Define `count_idents!` with a hidden enum whose last variant serves as the count
2. Use: `const N: u32 = count_idents!(A, B, C);` evaluates to `3`

## To Recognise:
1. Macros named `count_tts`, `count_idents`, or similar
2. Patterns that sum `1usize` values in a repetition
3. Array construction with `.len()` calls inside macros

# Context & Application

Counting is needed whenever a macro must know the length of its input -- for example, to declare a fixed-size array, compute an index, or generate numbered variants. The choice of technique depends on whether a constant is needed, how large the input might be, and whether inputs are identifiers or arbitrary tokens.

The slice length approach is the preferred method for non-constant counts due to its scalability. For constant counts, enum counting works but is limited to distinct identifiers. The recursive approach with multi-token batching offers a middle ground for moderate-sized inputs.

# Examples

**Example 1** (Ch. 4, "Counting -- Repetition with replacement"):

```rust
macro_rules! replace_expr {
    ($_t:tt $sub:expr) => {$sub};
}

macro_rules! count_tts {
    ($($tts:tt)*) => {0usize $(+ replace_expr!($tts 1usize))*};
}

fn main() {
    assert_eq!(count_tts!(0 1 2), 3);
}
// Expands to: 0usize + 1usize + 1usize + 1usize
```

**Example 2** (Ch. 4, "Counting -- Recursion"): Multi-token batching to extend the recursion limit:

```rust
macro_rules! count_tts {
    ($_a:tt $_b:tt $_c:tt $_d:tt $_e:tt
     $_f:tt $_g:tt $_h:tt $_i:tt $_j:tt
     $($tail:tt)*)
        => {10usize + count_tts!($($tail)*)};
    ($_a:tt $($tail:tt)*)
        => {1usize + count_tts!($($tail)*)};
    () => {0usize};
}
// Works up to ~1,200 tokens with batches of 10 and 20
```

**Example 3** (Ch. 4, "Counting -- Slice length"):

```rust
macro_rules! count_tts {
    ($($tts:tt)*) => {<[()]>::len(&[$(replace_expr!($tts ())),*])};
}
// Works up to 10,000+ tokens, but result is not const
```

**Example 4** (Ch. 4, "Counting -- Enum counting"):

```rust
macro_rules! count_idents {
    ($($idents:ident),* $(,)*) => {
        {
            #[allow(dead_code, non_camel_case_types)]
            enum Idents { $($idents,)* __CountIdentsLast }
            const COUNT: u32 = Idents::__CountIdentsLast as u32;
            COUNT
        }
    };
}

const COUNT: u32 = count_idents!(A, B, C);
assert_eq!(COUNT, 3);
```

# Relationships

## Builds Upon
- **macro-repetition** -- all techniques use repetition matching
- **repetition-replacement** -- the `replace_expr!` helper is used by two techniques

## Enables
- Complex macros that need to know input length at compile time

## Related
- **tt-muncher** -- the recursive counting approach is a simple TT muncher
- **push-down-accumulation** -- the abacus counter (provisional pattern) uses accumulation for counting

## Contrasts With
- None explicitly -- the four techniques are alternatives to each other, not to an external pattern

# Common Errors

- **Error**: Using untyped integer literals (`0`, `1`) in counting macros, causing slow type inference.
  **Correction**: "As of `rustc` 1.2, the compiler has *grevious* performance problems when large numbers of integer literals of unknown type must undergo inference." Always use `0usize`, `1usize`, etc.

- **Error**: Using enum counting with duplicate identifiers.
  **Correction**: Enum counting requires all identifiers to be distinct. If the sentinel name `__CountIdentsLast` appears in the input, the macro fails with a duplicate variant error. This approach "is *not* hygienic."

# Common Confusions

- **Confusion**: Thinking any counting technique can produce a `const` result.
  **Clarification**: Only enum counting produces a true constant. Slice length "can probably go much higher" but "*cannot* be used to produce a constant expression" -- the result "still cannot be used in constant positions (such as the value of `const`s, or a fixed array's size)."

- **Confusion**: Expecting the simple repetition-with-replacement approach to scale.
  **Clarification**: It "will likely *crash the compiler* with inputs of around 500 or so tokens" because the output forms a deeply unbalanced binary AST that overflows the parser's stack.

# Source Reference

Chapter 4: Building Blocks, "Counting" section. Four subsections present the techniques: "Repetition with replacement," "Recursion," "Slice length," and "Enum counting." Each includes working code and discusses limitations.

# Verification Notes

- Definition source: Direct quotation from "Counting" section opening and each subsection
- Key Properties: All from explicit statements in the source, including specific token limits
- Confidence rationale: HIGH -- the source presents four well-defined techniques with clear trade-off analysis
- Uncertainties: The specific token limits (~500, ~1,200, 10,000+) and const-expression limitations may have changed in newer Rust versions
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
