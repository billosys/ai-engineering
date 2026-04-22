---
# === CORE IDENTIFICATION ===
concept: Macro Indexing
slug: macro-indexing

# === CLASSIFICATION ===
category: macro-system
subcategory: advanced-patterns
tier: advanced

# === PROVENANCE ===
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "02-practical-introduction"
chapter_number: 2
pdf_page: null
section: "Indexing and Shuffling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "macro subscript patterns"
  - "index operator in macros"
  - "macro sliding window"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-rules
  - macro-substitution
  - macro-hygiene
extends: []
related:
  - macro-invocation-design
  - incremental-macro-development
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a macro expansion support subscript/index syntax like a[n-1]?"
  - "How do I implement a sliding window over previous values in macro-generated code?"
  - "How does the Index trait interact with macro-generated code?"
  - "Why do macros need wrapper types for custom indexing behavior?"
---

# Quick Definition

Macro indexing is a technique for making macro-generated code support subscript syntax (like `a[n-1]`) by implementing the `Index` trait on a wrapper type in the macro expansion. The macro captures the sequence and index identifiers, then generates a wrapper struct with an `Index` implementation that translates logical indices into physical array positions.

# Core Definition

When a macro's invocation syntax includes index expressions like `a[n-1]`, the expansion must provide a context where `a[n-1]` is a valid Rust expression. Since Rust's subscript syntax `a[i]` desugars to `*a.index(i)` via the `Index` trait, the macro generates:

1. A wrapper type (e.g., `IndexOffset`) that borrows a fixed-size array and stores an offset.
2. An `Index<usize>` implementation that translates the user-visible index (e.g., `n-1`) into the correct physical position in the underlying sliding-window buffer.
3. A local `let` binding that creates an instance of the wrapper, so the captured identifier (`$seq`) refers to something indexable.

This allows the recurrence expression `$recur` (which contains `a[n-1] + a[n-2]`) to compile without modification.

# Prerequisites

- Understanding of `macro_rules!` substitution (how captures appear in expansions)
- Familiarity with Rust's `Index` trait and how subscript syntax desugars
- Knowledge of macro hygiene (captured identifiers must share the caller's syntax context)

# Key Properties

1. **Trait-based desugaring**: Rust's `a[i]` syntax calls `Index::index(&a, i)`. By implementing `Index` on a custom type, macro-generated code can define arbitrary indexing behavior.
2. **Sliding window pattern**: The `IndexOffset` wrapper maps logical indices (the user's `n-1`, `n-2`) to physical positions in a fixed-size circular buffer using wrapping arithmetic: `real_index = (index - offset + window_size)`.
3. **Borrow scoping**: The wrapper borrows the iterator's memory buffer (`&self.mem`). This borrow must expire before the buffer can be mutated (to shuffle in the new value). The chapter uses a block `{ let n = ...; let a = ...; $recur }` to limit the borrow's scope.
4. **Identity capture for hygiene**: The identifier used for indexing (`a`) must be captured as `$seq:ident` from the invocation, not hardcoded in the expansion. This ensures the `a` in the user's `a[n-1]` and the `a` defined via `let $seq = IndexOffset { ... }` share the same syntax context.
5. **Shuffle-down mutation**: After computing the new value, the sliding window is updated by swapping elements down one position and inserting the new value, allowing the same fixed-size buffer to be reused for unbounded sequences.

# Construction / Recognition

**The wrapper type with Index implementation:**

```rust,ignore
struct IndexOffset<'a> {
    slice: &'a [$sty; MEM_SIZE],
    offset: usize,
}

impl<'a> Index<usize> for IndexOffset<'a> {
    type Output = $sty;

    #[inline(always)]
    fn index<'b>(&'b self, index: usize) -> &'b $sty {
        use std::num::Wrapping;

        let index = Wrapping(index);
        let offset = Wrapping(self.offset);
        let window = Wrapping(MEM_SIZE);

        let real_index = index - offset + window;
        &self.slice[real_index.0]
    }
}
```

**Binding the captured identifier to the wrapper:**

```rust,ignore
let next_val = {
    let $ind = self.pos;                                    // n = current position
    let $seq = IndexOffset { slice: &self.mem, offset: $ind }; // a = window wrapper
    $recur                                                  // a[n-1] + a[n-2]
};
```

**The shuffle-down after computing the new value:**

```rust,ignore
{
    use std::mem::swap;
    let mut swap_tmp = next_val;
    for i in (0..MEM_SIZE).rev() {
        swap(&mut swap_tmp, &mut self.mem[i]);
    }
}
```

# Context & Application

This technique is applicable whenever a macro needs to provide custom subscript semantics. The `recurrence!` macro uses it so that the user can write natural mathematical notation like `a[n-1] + a[n-2]` in the recurrence expression. Without this technique, the user would need to manually manage array indexing with offset calculations, defeating the purpose of the macro.

The pattern generalizes: any macro that wants to let users write `identifier[expression]` with custom semantics can generate a local type implementing `Index`. This is a form of "operator overloading via code generation."

# Examples

**Fibonacci sequence:**

```rust,ignore
let fib = recurrence![a[n]: u64 = 0, 1 ... a[n-1] + a[n-2]];
```

Here `a[n-1]` accesses the (n-1)th element of the sequence. With `n = 5`, `MEM_SIZE = 2`, and `offset = 5`, the index computation for `a[4]` is: `Wrapping(4) - Wrapping(5) + Wrapping(2) = Wrapping(1)`, which correctly accesses `self.mem[1]`.

**Factorial sequence (different identifiers):**

```rust,ignore
for e in recurrence!(f[i]: f64 = 1.0 ... f[i-1] * i as f64).take(10) {
    println!("{}", e)
}
```

This uses `f` and `i` instead of `a` and `n`, demonstrating that the captured identifiers are fully generic.

# Relationships

- **macro-substitution**: The `$seq`, `$ind`, `$sty`, and `$recur` captures are all substituted into the generated `IndexOffset` code.
- **macro-hygiene**: The need to capture `a` and `n` as identifiers (rather than hardcoding them) arises directly from hygiene -- identifiers from different syntax contexts do not resolve to each other.
- **macro-invocation-design**: The choice to use `a[n]` subscript syntax in the invocation drives the need for this entire technique.
- **incremental-macro-development**: The indexing machinery is developed as plain Rust first, then integrated into the macro.

# Common Errors

1. **Forgetting to scope the borrow**: If the `IndexOffset` wrapper (which borrows `&self.mem`) is not confined to a block, the subsequent mutation of `self.mem` for shuffling will fail with a borrow-checker error.
2. **Hardcoding the wrapper's array size**: Using a literal like `2` instead of `MEM_SIZE` makes the macro work only for sequences with exactly 2 initial values.
3. **Hardcoding identifier names**: Using literal `a` and `n` instead of `$seq` and `$ind` causes hygiene failures -- the identifiers in the expansion are in a different syntax context than those in the invocation.

# Common Confusions

- **Why not just use a slice?**: A plain slice does not provide the offset translation needed. The user writes `a[n-1]` meaning "the (n-1)th element of the sequence," but the physical buffer only holds the last `MEM_SIZE` elements. The `IndexOffset` wrapper bridges this gap.
- **Wrapping arithmetic**: The use of `std::num::Wrapping` is necessary because when `n` is small (e.g., position 2 with offset 2), `index - offset` would underflow for unsigned integers. Wrapping arithmetic produces the correct result via modular arithmetic.
- **Why does `--pretty expanded` compile but the macro doesn't?**: The expanded text looks identical, but hygiene means the identifiers are in different syntax contexts. Capturing them as `$seq:ident` and `$ind:ident` solves this.

# Source Reference

The Little Book of Rust Macros, Chapter 2 "Macros, A Practical Introduction", "Indexing and Shuffling" section and "Being Hygienic" section. The technique spans lines 390-1305 of the source text.

# Verification Notes

Confidence: high. The indexing pattern is thoroughly explained and demonstrated with working code in the source. The `IndexOffset` wrapper, its `Index` implementation, and the hygiene fix are all explicitly presented.
