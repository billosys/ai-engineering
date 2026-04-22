---
# === CORE IDENTIFICATION ===
concept: API Future Proofing Guidelines
slug: api-future-proofing-guidelines

# === CLASSIFICATION ===
category: api-design
subcategory: future-proofing
tier: advanced

# === PROVENANCE ===
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "10-future-proofing"
chapter_number: 10
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C-SEALED"
  - "C-STRUCT-PRIVATE"
  - "C-STRUCT-BOUNDS"
  - "C-NEWTYPE-HIDE"
  - "sealed trait pattern"
  - "API evolution guidelines"
  - "non-breaking changes"
  - "trait bound guidelines"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - api-guidelines-overview
  - api-type-safety-guidelines
extends: []
related:
  - api-predictability-guidelines
  - api-flexibility-guidelines
  - api-interoperability-guidelines
  - api-dependability-guidelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the sealed trait pattern and when should I use it?"
  - "Why should struct fields be private by default?"
  - "How do newtypes help encapsulate implementation details?"
  - "Why should data structures avoid duplicating derived trait bounds?"
  - "What makes adding a trait bound to a data structure a breaking change?"
  - "When is impl Trait better than a newtype for hiding return types?"
  - "What are the exceptions where trait bounds on structs are required?"
  - "How can I add methods to a trait without breaking downstream code?"
---

# Quick Definition

Rust APIs should be designed to allow non-breaking evolution. Four guidelines govern this: seal traits that should only be implemented internally (C-SEALED), keep struct fields private (C-STRUCT-PRIVATE), use newtypes or `impl Trait` to hide implementation details in return types (C-NEWTYPE-HIDE), and avoid putting derived trait bounds on generic data structures (C-STRUCT-BOUNDS). These patterns preserve the ability to make changes in future releases without breaking downstream code.

# Core Definition

The Rust API Guidelines define four conventions for future-proof API design.

**C-SEALED**: "Some traits are only meant to be implemented within the crate that defines them. In such cases, we can retain the ability to make changes to the trait in a non-breaking way by using the sealed trait pattern." The pattern uses a private supertrait `private::Sealed` that cannot be named by downstream crates, guaranteeing all implementations exist only in the defining crate. This allows adding methods to the trait in non-breaking releases.

**C-STRUCT-PRIVATE**: "Making a field public is a strong commitment: it pins down a representation choice, and prevents the type from providing any validation or maintaining any invariants on the contents of the field, since clients can mutate it arbitrarily." The guideline recommends getter/setter methods unless the struct is a passive C-style data structure.

**C-NEWTYPE-HIDE**: "A newtype can be used to hide representation details while making precise promises to the client." Instead of exposing `Enumerate<Skip<I>>` as a return type, wrap it in `MyTransformResult<I>` implementing `Iterator`. The source notes that `impl Trait` (Rust 1.26+) is a more concise alternative but with limitations -- it cannot express combinations like `Debug + Clone + Iterator`.

**C-STRUCT-BOUNDS**: "Generic data structures should not use trait bounds that can be derived or do not otherwise add semantic value." Adding a trait bound to a data structure is a breaking change because all consumers must satisfy it. Deriving more traits via `#[derive]` is not a breaking change. The source lists specific traits that should never appear as bounds on data structures: `Clone`, `PartialEq`, `PartialOrd`, `Debug`, `Display`, `Default`, `Error`, `Serialize`, `Deserialize`, `DeserializeOwned`.

# Prerequisites

- **API Guidelines Overview** -- understanding the overall API Guidelines framework
- **API Type Safety Guidelines** -- C-NEWTYPE-HIDE builds on the newtype pattern from C-NEWTYPE

# Key Properties

1. **Sealed trait pattern**: A private supertrait prevents external implementations while allowing internal trait evolution
2. **Sealed traits still have breaking changes**: "Removing a public method or changing the signature of a public method in a sealed trait are still breaking changes"
3. **Private fields preserve invariants**: Public fields prevent validation and allow arbitrary mutation
4. **Newtypes hide representation**: Wrapping complex return types lets the implementation change without breaking callers
5. **impl Trait as alternative**: More concise than newtypes but cannot express trait combinations like `Debug + Clone + Iterator`
6. **Trait bounds on structs are breaking**: Every consumer must satisfy added bounds; deriving more traits is not breaking
7. **Forbidden bounds list**: Clone, PartialEq, PartialOrd, Debug, Display, Default, Error, Serialize, Deserialize, DeserializeOwned
8. **Three exceptions for struct bounds**: (1) the struct refers to an associated type on the trait, (2) the bound is `?Sized`, (3) the struct has a `Drop` impl that requires the bound
9. **Grey area for semantic bounds**: Non-derivable bounds like `Read` or `Write` "may communicate the intended behavior of the type better" but still limit extensibility
10. **Document sealed traits**: "It should be documented in rustdoc that the trait is sealed and not meant to be implemented outside of the current crate"

# Construction / Recognition

## Sealed trait pattern (C-SEALED):
```rust
/// This trait is sealed and cannot be implemented for types outside this crate.
pub trait TheTrait: private::Sealed {
    fn public_method(&self);

    #[doc(hidden)]
    fn private_method(&self);
}

impl TheTrait for usize { /* ... */ }

mod private {
    pub trait Sealed {}
    impl Sealed for usize {}
}
```

## Newtype to hide return type (C-NEWTYPE-HIDE):
```rust
pub struct MyTransformResult<I>(Enumerate<Skip<I>>);

impl<I: Iterator> Iterator for MyTransformResult<I> {
    type Item = (usize, I::Item);
    fn next(&mut self) -> Option<Self::Item> {
        self.0.next()
    }
}

pub fn my_transform<I: Iterator>(input: I) -> MyTransformResult<I> {
    MyTransformResult(input.skip(3).enumerate())
}
```

## impl Trait alternative (C-NEWTYPE-HIDE):
```rust
pub fn my_transform<I: Iterator>(input: I) -> impl Iterator<Item = (usize, I::Item)> {
    input.skip(3).enumerate()
}
```

## Correct vs incorrect struct bounds (C-STRUCT-BOUNDS):
```rust
// Correct: no bounds on the struct
#[derive(Clone, Debug, PartialEq)]
struct Good<T> { /* ... */ }

// Incorrect: duplicates derived trait bounds
#[derive(Clone, Debug, PartialEq)]
struct Bad<T: Clone + Debug + PartialEq> { /* ... */ }
```

## Why bounds matter -- adding PartialOrd (C-STRUCT-BOUNDS):
```rust
// Non-breaking change:
#[derive(Clone, Debug, PartialEq, PartialOrd)]
struct Good<T> { /* ... */ }

// Breaking change (new PartialOrd bound required of all consumers):
#[derive(Clone, Debug, PartialEq, PartialOrd)]
struct Bad<T: Clone + Debug + PartialEq + PartialOrd> { /* ... */ }
```

# Context & Application

These guidelines address one of the most challenging aspects of library design: evolving APIs without breaking downstream code. The sealed trait pattern (C-SEALED) is widely used in the Rust ecosystem -- the source cites `serde_json::value::Index` and `byteorder::ByteOrder` as real-world examples. The C-STRUCT-BOUNDS guideline has particular practical importance because it is easy to accidentally add bounds that seem harmless but create breaking changes when you derive additional traits later. The `impl Trait` feature (Rust 1.26+) has partially superseded C-NEWTYPE-HIDE for simple cases, but the source notes it is "probably great for internal APIs" while newtypes remain important for public APIs where you need to express additional trait bounds on the return type.

# Examples

**Example 1** (Ch. 10, C-SEALED): The sealed trait mechanism explained:
> "The empty private `Sealed` supertrait cannot be named by downstream crates, so we are guaranteed that implementations of `Sealed` (and therefore `TheTrait`) only exist in the current crate. We are free to add methods to `TheTrait` in a non-breaking release."

**Example 2** (Ch. 10, C-STRUCT-PRIVATE): Why public fields are a strong commitment:
> "Making a field public is a strong commitment: it pins down a representation choice, and prevents the type from providing any validation or maintaining any invariants on the contents of the field."

**Example 3** (Ch. 10, C-NEWTYPE-HIDE): Hiding `Enumerate<Skip<I>>` behind `MyTransformResult<I>`:
> "The client does not know how the result iterator is constructed or represented, which means the representation can change in the future without breaking client code."

**Example 4** (Ch. 10, C-STRUCT-BOUNDS): Standard library examples of legitimate struct bounds:
> "`std::borrow::Cow` refers to an associated type on the `Borrow` trait. `std::boxed::Box` opts out of the implicit `Sized` bound. `std::io::BufWriter` requires a trait bound in its `Drop` impl."

**Example 5** (Ch. 10, C-NEWTYPE-HIDE): Limitations of `impl Trait`:
> "Returning an iterator that impls `Debug` or `Clone` or some combination of the other iterator extension traits can be problematic."

# Relationships

## Builds Upon
- **API Guidelines Overview** -- these guidelines are part of the overall API Guidelines checklist
- **API Type Safety Guidelines** -- C-NEWTYPE-HIDE extends the newtype pattern from C-NEWTYPE

## Enables
- Non-breaking API evolution over semver releases
- Adding trait methods without breaking downstream implementations
- Changing internal representations without breaking callers

## Related
- **api-predictability-guidelines** -- predictable APIs support future evolution
- **api-flexibility-guidelines** -- flexible APIs must also be evolvable
- **api-interoperability-guidelines** -- standard trait implementations interact with struct bounds
- **api-dependability-guidelines** -- dependable APIs require stable evolution strategies

## Contrasts With
- None within this source

# Common Errors

- **Error**: Adding a trait bound to a generic data structure without realizing it is a breaking change.
  **Correction**: "Generally speaking, adding a trait bound to a data structure is a breaking change because every consumer of that structure will need to start satisfying the additional bound." Only use struct bounds for the three exception cases. (C-STRUCT-BOUNDS)

- **Error**: Exposing complex iterator adapter types in public return signatures.
  **Correction**: Wrap complex return types in a newtype or use `impl Trait` so the internal representation can change freely. (C-NEWTYPE-HIDE)

- **Error**: Making struct fields public for convenience.
  **Correction**: "Consider providing getter/setter methods and hiding fields instead." Public fields pin down representation choices and prevent invariant enforcement. (C-STRUCT-PRIVATE)

- **Error**: Adding methods to an unsealed public trait, causing a breaking change.
  **Correction**: Use the sealed trait pattern with a private `Sealed` supertrait to prevent downstream implementations, enabling non-breaking method additions. (C-SEALED)

# Common Confusions

- **Confusion**: Thinking sealed traits cannot have any public methods.
  **Clarification**: Sealed traits have both public methods (callable by anyone) and `#[doc(hidden)]` methods (private to the crate). The seal only prevents external implementations, not external use.

- **Confusion**: Thinking `impl Trait` always replaces the newtype-hide pattern.
  **Clarification**: "With `impl Trait` you are limited in what you can express. For example, returning an iterator that impls `Debug` or `Clone` or some combination of the other iterator extension traits can be problematic." Newtypes remain necessary for complex public APIs.

- **Confusion**: Thinking semantically useful bounds like `Read` or `Write` on structs are as problematic as derivable bounds.
  **Clarification**: The source describes a "grey area" -- semantic bounds "may communicate the intended behavior of the type better" and are "still less problematic than including derivable traits as bounds."

- **Confusion**: Thinking all trait bounds on structs are wrong.
  **Clarification**: Three exceptions are legitimate: (1) the struct refers to an associated type on the trait, (2) the bound is `?Sized`, (3) the struct has a `Drop` impl that requires the bound.

# Source Reference

Chapter 10: Future Proofing -- guidelines C-SEALED (sealed traits protect against downstream implementations), C-STRUCT-PRIVATE (structs have private fields), C-NEWTYPE-HIDE (newtypes encapsulate implementation details), C-STRUCT-BOUNDS (data structures do not duplicate derived trait bounds). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 10 of the Rust API Guidelines
- Confidence rationale: HIGH -- the source provides detailed code examples, explicit lists of forbidden bounds, named exceptions, and real-world examples from the standard library and ecosystem
- Uncertainties: The `impl Trait` guidance notes it is "probably" appropriate for some public APIs, reflecting the feature's relative newness at time of writing
- Cross-reference status: api-guidelines-overview and api-type-safety-guidelines referenced; api-type-safety-guidelines is in this extraction set
