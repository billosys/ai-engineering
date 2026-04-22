---
concept: Deref Polymorphism
slug: deref-polymorphism
category: anti-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Anti-patterns"
chapter_number: 3
pdf_page: null
section: "Deref polymorphism"
extraction_confidence: high
aliases:
  - "Deref inheritance"
  - "Deref for method delegation"
  - "fake inheritance via Deref"
prerequisites:
  - ownership
extends: []
related:
  - newtype-pattern
  - strategy-pattern
contrasts_with: []
answers_questions:
  - "Why is using Deref to emulate inheritance an anti-pattern in Rust?"
  - "What are the problems with Deref polymorphism?"
  - "How should I delegate methods to an inner type in Rust?"
---

# Quick Definition

Misusing the `Deref` trait to emulate struct inheritance from OO languages like Java or C++. By implementing `Deref<Target = Foo>` for `Bar`, the dot operator's implicit dereferencing makes `Foo`'s methods callable on `Bar`. While this saves boilerplate, it is surprising, does not create true subtyping, and breaks trait-based generic programming.

# Core Definition

The `Deref` trait is designed for the implementation of custom pointer types -- its intention is to take a pointer-to-`T` to a `T`, not to convert between different types. However, because the dot operator performs implicit dereferencing, implementing `Deref` for a wrapper struct with an inner type as the `Target` causes the inner type's methods to appear on the wrapper. This anti-pattern uses this mechanism to emulate inheritance: a `Bar` struct contains a `Foo` field, implements `Deref<Target = Foo>`, and thus gains access to all of `Foo`'s methods. The result is subtly different from inheritance in OO languages: there is no subtyping, traits implemented by `Foo` are not automatically implemented for `Bar`, and `self` in delegated methods refers to `Foo`, not `Bar`.

# Prerequisites

- **Ownership and composition** -- understanding that Rust uses composition (structs containing other structs) rather than inheritance

# Key Properties

1. The `Deref` trait is intended for custom pointer types (e.g., `Box<T>`, `Rc<T>`), not for type conversion between unrelated structs
2. The dot operator performs implicit dereferencing, which is why `Foo`'s methods become callable on `Bar`
3. This does NOT introduce subtyping -- `Bar` is not a subtype of `Foo`
4. Traits implemented by `Foo` are NOT automatically implemented for `Bar`, breaking generic programming with trait bounds
5. In delegated methods, `self` refers to `Foo` (the deref target), not `Bar` -- unlike OO inheritance where `self`/`this` refers to the subclass
6. Only single inheritance is supported (one `Deref` target); there is no notion of interfaces, class-based privacy, or other inheritance features
7. The mechanism is completely implicit, making code surprising to readers

# Construction / Recognition

## To Recognize This Anti-Pattern:
1. Look for `impl Deref for StructA` where `type Target = StructB` and `StructB` is not a smart pointer target
2. Check if `StructA` contains a field of type `StructB` and the `deref()` method returns a reference to that field
3. Note if the purpose is to make `StructB`'s methods callable on `StructA` (method delegation)

## The Anti-Pattern (Java-style inheritance emulation):
```rust
use std::ops::Deref;

struct Foo {}
impl Foo {
    fn m(&self) { /* ... */ }
}

struct Bar { f: Foo }
impl Deref for Bar {
    type Target = Foo;
    fn deref(&self) -> &Foo { &self.f }
}

fn main() {
    let b = Bar { f: Foo {} };
    b.m(); // calls Foo::m via implicit deref
}
```

## Better Alternatives:
1. **Explicit delegation** -- write facade methods that forward to the inner type
2. **Traits** -- define shared behavior as traits and implement them for each type
3. **Delegation crates** -- use crates like `delegate` or `ambassador` to reduce boilerplate

# Context & Application

Rust tries to strike a careful balance between explicit and implicit mechanisms, favouring explicit conversions between types. Automatic dereferencing in the dot operator is a case where ergonomics strongly favour an implicit mechanism, but the intention is that this is limited to degrees of indirection (pointer-to-value), not conversion between arbitrary types. There is no struct inheritance in Rust by design. The source notes that there are ongoing discussions about adding a delegation or inheritance mechanism to Rust (referencing RFC issue #349 and blog posts from 2015), but these have not reached stable Rust.

# Examples

**Example 1** (Ch. 3, "Deref polymorphism", Java comparison):

The source shows the Java equivalent being emulated:
```java
class Foo { void m() { ... } }
class Bar extends Foo {}
public static void main(String[] args) {
    Bar b = new Bar();
    b.m();  // inherited from Foo
}
```

In Rust, `Bar` contains a `Foo` field and implements `Deref<Target = Foo>`, making `b.m()` work through implicit deref. However, unlike Java, `Bar` is NOT a subtype of `Foo` -- you cannot pass a `Bar` where a `&Foo` is expected in generic contexts with trait bounds.

**Example 2** (Ch. 3, "Advantages"): The explicit delegation alternative that the anti-pattern avoids:
```rust
impl Bar {
    fn m(&self) {
        self.f.m()
    }
}
```
This is more boilerplate but is explicit, unsurprising, and works correctly with traits and generics.

# Relationships

## Builds Upon
- The `Deref` trait and Rust's dot-operator auto-dereferencing mechanism

## Enables
- Understanding of when `Deref` is used correctly (smart pointers, the "collections are smart pointers" idiom)

## Related
- **newtype-pattern** -- newtypes often need method delegation; Deref polymorphism is the wrong way to achieve it
- **strategy-pattern** -- when the API between types does not change but behavior does, strategy is a better fit

## Contrasts With
- Correct use of `Deref` for smart pointer types (`Box<T>`, `Rc<T>`, `Arc<T>`)

# Common Errors

- **Error**: Implementing `Deref` for a newtype wrapper to expose all inner methods, then being surprised that trait impls on the inner type don't apply to the wrapper.
  **Correction**: Implement the necessary traits directly on the wrapper type, or use delegation crates to generate forwarding impls.

- **Error**: Assuming `self` in a deref-delegated method refers to the outer type.
  **Correction**: `self` refers to the `Deref::Target` type. If the method needs access to the outer struct's fields, deref polymorphism cannot provide it.

# Common Confusions

- **Confusion**: Thinking Deref polymorphism and OO inheritance are equivalent.
  **Clarification**: They differ in critical ways: no subtyping, no automatic trait inheritance, `self` semantics differ, and only single "inheritance" is supported. The experience will be subtly surprising to programmers used to Java or C++ inheritance.

- **Confusion**: Thinking the "collections are smart pointers" idiom (e.g., `Vec<T>` implementing `Deref<Target = [T]>`) is the same anti-pattern.
  **Clarification**: That idiom is considered acceptable because `Vec<T>` IS a smart pointer over a slice -- it manages ownership of heap-allocated data and provides transparent access to the underlying slice. This is the intended use of `Deref`.

# Source Reference

Chapter 3: Anti-patterns, "Deref polymorphism" section. The anti-pattern is described with a Java comparison, Rust code example, detailed advantages/disadvantages, discussion of Deref's intended purpose, and references to RFC #349 and delegation crates.

# Verification Notes

- Definition source: Paraphrased from the Description and Discussion subsections
- Key Properties: All from explicit statements in the source, including the disadvantages section
- Confidence rationale: HIGH -- the source provides extensive explanation, code examples, and nuanced discussion
- Uncertainties: The status of RFC #349 and future inheritance mechanisms in Rust
- Cross-reference status: `newtype-pattern` and `strategy-pattern` reference cards from other extraction agents
