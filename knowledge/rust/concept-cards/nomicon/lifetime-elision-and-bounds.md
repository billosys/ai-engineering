---
concept: Lifetime Elision and Bounds
slug: lifetime-elision-and-bounds
category: unsafe-rust
subcategory: ownership-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Ownership and Lifetimes"
chapter_number: 3
pdf_page: null
section: "Lifetime Elision / Unbounded Lifetimes / Higher-Rank Trait Bounds"
extraction_confidence: high
aliases:
  - "lifetime elision rules"
  - "unbounded lifetimes"
  - "HRTBs"
  - "higher-rank trait bounds"
  - "for<'a>"
  - "elision rules"
prerequisites:
  - ownership-and-lifetimes
extends:
  - ownership-and-lifetimes
related:
  - subtyping-and-variance
  - type-conversions
contrasts_with: []
answers_questions:
  - "What are the three lifetime elision rules?"
  - "What is an unbounded lifetime and how do they arise?"
  - "What does for<'a> mean in Rust?"
  - "When are HRTBs needed?"
  - "Why is an unbounded lifetime more powerful than 'static?"
  - "How do you bound an unbounded lifetime?"
---

# Quick Definition

Lifetime elision rules allow common lifetime patterns to be written without explicit annotations. Unbounded lifetimes arise from unsafe code (mainly dereferencing raw pointers) and are more powerful than `'static`. Higher-Rank Trait Bounds (HRTBs) use `for<'a>` syntax to express that a bound must hold for all possible lifetime choices.

# Core Definition

**Lifetime elision** makes common patterns ergonomic by inferring lifetime annotations. There are three rules (Ch. 3, "Lifetime Elision"):

1. Each elided lifetime in input position becomes a distinct lifetime parameter
2. If there is exactly one input lifetime position (elided or not), it is assigned to all elided output lifetimes
3. If multiple input lifetime positions exist but one is `&self` or `&mut self`, the `self` lifetime is assigned to all elided output lifetimes

If none of these rules apply, eliding an output lifetime is an error. Lifetime positions are anywhere you can write a lifetime: `&'a T`, `&'a mut T`, `T<'a>`. Input positions are function arguments; output positions are return types. For `impl` headers, all types are input.

**Unbounded lifetimes** arise when unsafe code produces references "out of thin air," most commonly by dereferencing a raw pointer. "Such a lifetime becomes as big as context demands. This is in fact more powerful than simply becoming `'static`, because for instance `&'static &'a T` will fail to typecheck, but the unbound lifetime will perfectly mold into `&'a &'a T` as needed." (Ch. 3, "Unbounded Lifetimes"). Output lifetimes that don't derive from inputs are unbounded. The easiest way to avoid them is to use lifetime elision at the function boundary, which forces all output lifetimes to derive from inputs.

**Higher-Rank Trait Bounds (HRTBs)** use the `for<'a>` syntax to express that a bound holds for all possible lifetime choices. This is needed when a trait bound involves a lifetime that doesn't exist until the function is called. The canonical example is `Fn` trait bounds: `where for<'a> F: Fn(&'a (u8, u16)) -> &'a u8` reads as "for all choices of `'a`, F must satisfy this bound." This produces "an infinite list of trait bounds that F must satisfy." (Ch. 3, "Higher-Rank Trait Bounds")

# Prerequisites

- **ownership-and-lifetimes** -- understanding reference rules, lifetime regions, and borrow checking is essential for all three topics

# Key Properties

1. Lifetime elision has exactly three rules, applied in order
2. Elision rule 1: each elided input lifetime becomes a distinct lifetime parameter
3. Elision rule 2: a single input lifetime is assigned to all elided output lifetimes
4. Elision rule 3: `&self`/`&mut self` lifetime is assigned to all elided output lifetimes
5. If no rule applies, eliding output lifetimes is a compile error
6. For `impl` headers, all type positions are input positions
7. Unbounded lifetimes arise from dereferencing raw pointers or from `transmute`/`transmute_copy`
8. Unbounded lifetimes are more powerful than `'static` -- they mold to match any required lifetime
9. Functions with output lifetimes not derived from inputs produce unbounded lifetimes
10. `for<'a>` produces an infinite list of trait bounds -- one for each possible lifetime choice
11. HRTBs are mostly needed with `Fn` trait bounds where the lifetime is determined at call time
12. `for<'a> F: Fn(&'a T) -> &'a U` is equivalent to the natural desugaring of `F: Fn(&T) -> &U`

# Construction / Recognition

## To Apply Elision Rules

1. Count input lifetime positions in the function signature
2. If one input lifetime: assign it to all elided output lifetimes (rule 2)
3. If `&self` or `&mut self` is present: assign self's lifetime to elided outputs (rule 3)
4. Otherwise: all output lifetimes must be explicitly annotated
5. Each elided input lifetime becomes its own distinct parameter (rule 1, always applies)

## To Identify Unbounded Lifetimes

1. Look for functions that produce references from raw pointer dereferences
2. Check if output lifetimes derive from input lifetimes -- if not, they're unbounded
3. Bound them quickly: return from a function with bound lifetimes, or place in a location with a specific lifetime

## To Use HRTBs

1. Identify when a lifetime in a trait bound can't be named at the point of the bound
2. Write `where for<'a> F: Fn(&'a T) -> &'a U` instead of trying to name a specific lifetime
3. Alternatively: `where F: for<'a> Fn(&'a T) -> &'a U` (the `for<'a>` can go on either side)

# Context & Application

Lifetime elision is what makes Rust's lifetime system practical -- without it, even simple function signatures would be cluttered with lifetime annotations. The three rules capture the vast majority of real-world patterns. The Nomicon's treatment is important for unsafe code authors because elision also serves as a safety mechanism: by forcing output lifetimes to derive from inputs, elision prevents accidental unbounded lifetimes.

Unbounded lifetimes are one of the most dangerous aspects of unsafe code. The source warns: "Almost no reference is `'static`, so this is probably wrong." A function like `fn get_str<'a>(s: *const String) -> &'a str` produces a reference with an unbounded lifetime that can be molded to match any caller's context, leading to use-after-free bugs that compile without error.

HRTBs are "intense" but rarely needed outside `Fn` trait bounds, where lifetime elision provides "nice magic sugar for the common cases." Understanding them matters for unsafe code that manipulates closures or function pointers with lifetime-parameterized arguments.

# Examples

**Example 1** (Ch. 3, "Lifetime Elision"): Elision in practice:
```rust
fn substr(s: &str, until: usize) -> &str;         // elided
fn substr<'a>(s: &'a str, until: usize) -> &'a str; // expanded (rule 2)

fn get_mut(&mut self) -> &mut T;                    // elided
fn get_mut<'a>(&'a mut self) -> &'a mut T;          // expanded (rule 3)

fn frob(s: &str, t: &str) -> &str;                 // ILLEGAL (no rule applies)
```

**Example 2** (Ch. 3, "Unbounded Lifetimes"): Dangerous unbounded lifetime:
```rust
fn get_str<'a>(s: *const String) -> &'a str {
    unsafe { &*s }
}
fn main() {
    let soon_dropped = String::from("hello");
    let dangling = get_str(&soon_dropped);
    drop(soon_dropped);
    println!("Invalid str: {}", dangling); // UB: use after free
}
```

**Example 3** (Ch. 3, "Higher-Rank Trait Bounds"): HRTB for a closure bound:
```rust
impl<F> Closure<F>
    where for<'a> F: Fn(&'a (u8, u16)) -> &'a u8,
{
    fn call(&self) -> &u8 {
        (self.func)(&self.data)
    }
}
```
The `'a` lifetime cannot be named at the `impl` level -- it only exists when `call` is invoked.

# Relationships

## Builds Upon
- **ownership-and-lifetimes** -- elision, unbounded lifetimes, and HRTBs all extend the base lifetime system

## Enables
- **subtyping-and-variance** -- HRTBs interact with variance when closures take references with specific lifetimes

## Related
- **type-conversions** -- unbounded lifetimes from transmute are a type conversion hazard

## Contrasts With
(none)

# Common Errors

- **Error**: Writing a function that returns a reference derived from a raw pointer without bounding the output lifetime to an input lifetime.
  **Correction**: Use lifetime elision (tie the output to an input) or explicitly constrain the output lifetime. Unbounded lifetimes from raw pointer dereferences are almost always wrong.

- **Error**: Expecting elision to work when there are multiple input lifetimes and no `&self`.
  **Correction**: With multiple input lifetimes and no `self`, the compiler cannot determine which input lifetime to assign to the output. Annotate explicitly: `fn foo<'a, 'b>(s: &'a str, t: &'b str) -> &'a str`.

# Common Confusions

- **Confusion**: Thinking unbounded lifetimes are the same as `'static`.
  **Clarification**: Unbounded lifetimes are more powerful than `'static`. A `'static` reference cannot be placed where a shorter lifetime is needed in certain contexts (`&'static &'a T` fails), but an unbounded lifetime can mold to fit any context (`&'unbounded &'a T` works as `&'a &'a T`).

- **Confusion**: Believing HRTBs are needed frequently.
  **Clarification**: HRTBs are almost exclusively needed with `Fn` trait bounds, and even there, lifetime elision usually provides sugar that hides the HRTB. Writing `F: Fn(&T) -> &U` implicitly uses HRTBs.

- **Confusion**: Thinking lifetime elision changes semantics.
  **Clarification**: Elision is purely syntactic sugar. The elided form and the expanded form are identical -- the compiler applies the same rules mechanically.

# Source Reference

Chapter 3: Ownership and Lifetimes -- Lifetime Elision (three rules, input/output positions, examples), Unbounded Lifetimes (sources, dangers, bounding strategies), Higher-Rank Trait Bounds (for<'a> syntax, Fn trait desugaring).

# Verification Notes

- Definition source: Direct synthesis from three sections of Ch. 3 (lines 676-904 of source)
- Key Properties: Elision rules are verbatim from source; unbounded lifetime properties from explicit discussion; HRTB properties from desugaring example
- Confidence rationale: HIGH -- all three sections provide explicit rules and concrete code examples
- Uncertainties: None for the concepts themselves; the source notes HRTBs are rarely encountered outside Fn traits
- Cross-reference status: All slugs reference cards in the nomicon extraction set
