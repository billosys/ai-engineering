---
concept: RAII with Guards
slug: raii-guards
category: behavioural-pattern
subcategory: null
tier: advanced
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Behavioural Patterns"
extraction_confidence: high
aliases:
  - "RAII guard"
  - "resource guard"
  - "mutex guard pattern"
  - "scope guard"
prerequisites:
  - finalisation-in-destructors
extends:
  - finalisation-in-destructors
related:
  - newtype-pattern
  - clone-to-satisfy-borrow-checker
contrasts_with: []
answers_questions:
  - "How does RAII work in Rust with guards?"
  - "How does the borrow checker enforce resource safety with RAII guards?"
  - "Why does MutexGuard implement Deref?"
  - "How do RAII guards prevent use-after-free errors at compile time?"
---

# Quick Definition

RAII (Resource Acquisition Is Initialisation) with guards extends the basic RAII pattern by using a guard object that mediates all access to a resource, combined with Rust's borrow checker to statically prevent use-after-finalisation errors. The guard acquires the resource in its constructor and releases it in its destructor (`Drop`), while `Deref` provides ergonomic access.

# Core Definition

"RAII stands for 'Resource Acquisition is Initialisation' which is a terrible name. The essence of the pattern is that resource initialisation is done in the constructor of an object and finalisation in the destructor. This pattern is extended in Rust by using a RAII object as a guard of some resource and relying on the type system to ensure that access is always mediated by the guard object." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "RAII with guards")

# Prerequisites

- **Finalisation in destructors** -- RAII guards build directly on the idiom of using `Drop` for resource cleanup; understanding destructor-based finalisation is essential

# Key Properties

1. Resource initialisation happens in the constructor (e.g., `Mutex::lock` acquires the OS mutex and returns a `MutexGuard`)
2. Resource finalisation happens in the destructor (`Drop::drop` releases the OS mutex)
3. The guard object contains a reference to the underlying resource
4. All access to the resource is mediated through the guard
5. The borrow checker ensures references to the resource cannot outlive the guard
6. Implementing `Deref` makes the guard ergonomic (treat it like a pointer to the inner type)
7. `Deref` is not a core part of the pattern -- a `get` method works just as well
8. The lifetime of the returned reference from `deref` matches the lifetime of `self`, enforcing the safety invariant
9. This is a compile-time guarantee, not a runtime check

# Construction / Recognition

## To Implement an RAII Guard:
1. Create a resource type (e.g., `Mutex<T>`) that owns the underlying resource
2. Create a guard type (e.g., `MutexGuard<'a, T>`) that holds a reference to the resource data
3. Implement a method on the resource that returns the guard (e.g., `lock(&self) -> MutexGuard<T>`)
4. In the constructor method, acquire the resource (e.g., lock the OS mutex)
5. Implement `Drop` for the guard to release the resource (e.g., unlock the OS mutex)
6. Optionally implement `Deref` for ergonomic access: `fn deref(&self) -> &T { self.data }`
7. The borrow checker automatically prevents the guard (and thus resource access) from outliving the resource

## To Recognize the Pattern:
1. Look for a type that wraps access to a resource and implements `Drop`
2. Check for a constructor method that acquires a resource and returns a guard
3. Look for `Deref` implementation on the guard type
4. Verify that the guard holds a lifetime-bounded reference to the resource

# Context & Application

The canonical example is `MutexGuard` from the standard library. The source presents a simplified version: `Mutex<T>` holds the data, `MutexGuard<'a, T>` holds a reference `data: &'a T`. Calling `lock()` acquires the OS mutex and returns a `MutexGuard`. When the guard goes out of scope, `Drop::drop` unlocks the mutex. Implementing `Deref` means `xx.foo()` works directly on the guarded data.

The source explains the key Rust-specific insight: "The core aim of the borrow checker is to ensure that references to data do not outlive that data. The RAII guard pattern works because the guard object contains a reference to the underlying resource and only exposes such references. Rust ensures that the guard cannot outlive the underlying resource and that references to the resource mediated by the guard cannot outlive the guard."

Without lifetime elision, `deref` has the signature `fn deref<'a>(&'a self) -> &'a T`, which makes explicit that the returned reference has the same lifetime as the guard itself.

# Examples

**Example 1** (Ch. 2, "RAII with guards" -- MutexGuard): A simplified `MutexGuard<'a, T>` holds `data: &'a T`. `Mutex::lock` returns a guard, `Drop` for the guard unlocks the mutex, and `Deref` allows treating the guard as a `&T`. In the function `baz`, the guard `xx` provides access to `Foo`'s methods, and "the borrow checker ensures we can't store a reference to the underlying Foo which will outlive the guard xx."

**Example 2** (Ch. 2, "RAII with guards" -- Deref Lifetime): The source shows `deref` without lifetime elision: `fn deref<'a>(&'a self) -> &'a T`. "The returned reference to the resource has the same lifetime as `self` (`'a`). The borrow checker therefore ensures that the lifetime of the reference to `T` is shorter than the lifetime of `self`."

# Relationships

## Builds Upon
- **finalisation-in-destructors** -- RAII guards extend the basic destructor finalisation idiom with a guard wrapper and borrow checker integration

## Enables
- None explicitly

## Related
- **newtype-pattern** -- both wrap an inner type; RAII guards wrap for resource management while newtypes wrap for type safety
- **clone-to-satisfy-borrow-checker** -- developers sometimes clone unnecessarily when the borrow checker prevents them from holding references alongside guards; understanding RAII guards helps avoid this anti-pattern

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Trying to store a reference to the guarded data that outlives the guard.
  **Correction**: The borrow checker prevents this at compile time. Restructure code so the guard lives at least as long as any reference to the guarded data.

- **Error**: Thinking `Deref` is required for the RAII guard pattern.
  **Correction**: "Implementing `Deref` is not a core part of this pattern, it only makes using the guard object more ergonomic. Implementing a `get` method on the guard works just as well."

# Common Confusions

- **Confusion**: Thinking RAII guards provide only runtime safety (like C++ RAII).
  **Clarification**: In Rust, RAII guards provide compile-time safety via the borrow checker. The guard's lifetime is tracked statically, preventing use-after-finalisation errors before the program runs.

- **Confusion**: Thinking the pattern only applies to mutexes.
  **Clarification**: While `MutexGuard` is the canonical example, the pattern applies to any resource requiring guarded access: file handles, database connections, GPU resources, or any scoped exclusive access pattern.

# Source Reference

Chapter 2: Design Patterns, "RAII with guards" section under Behavioural Patterns. Includes a simplified `MutexGuard` implementation, discussion of borrow checker integration, lifetime analysis of `deref`, and a "See also" linking to the "Finalisation in destructors" idiom, cppreference.com RAII page, and Wikipedia.

# Verification Notes

- Definition source: Direct quotation from the "Description" subsection of "RAII with guards"
- Key Properties: Derived from the example code, the "Discussion" subsection, and the lifetime analysis
- Confidence rationale: HIGH -- the source provides a complete (simplified) implementation with detailed explanation of the borrow checker interaction
- Uncertainties: None for the pattern itself; the source notes the Rust style guide entry for RAII is "currently just a placeholder"
- Cross-reference status: finalisation-in-destructors is from Agent 1 (idioms); newtype-pattern is in this extraction set; clone-to-satisfy-borrow-checker is from Agent 5
