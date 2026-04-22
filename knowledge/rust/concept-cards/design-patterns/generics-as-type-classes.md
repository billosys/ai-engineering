---
concept: Generics as Type Classes
slug: generics-as-type-classes
category: functional-programming
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Functional Usage of Rust"
chapter_number: 4
pdf_page: null
section: "Generics as Type Classes"
extraction_confidence: high
aliases:
  - "type class constraints"
  - "monomorphization"
  - "generic type specialization"
  - "type-state via generics"
prerequisites:
  - ownership
extends: []
related:
  - builder-pattern
  - strategy-pattern
  - newtype-pattern
  - imperative-vs-declarative
contrasts_with: []
answers_questions:
  - "How do Rust generics differ from C++ templates or Java generics?"
  - "What is monomorphization and how does it relate to type classes?"
  - "How can generic type parameters create different impl blocks for different types?"
  - "What is the type-state pattern in Rust?"
---

# Quick Definition

Rust's generic type system is modeled after functional languages like Haskell rather than C++ templates or Java generics. Each distinct generic parameter creates a genuinely different type (monomorphization), and different concrete types can have different `impl` blocks. This allows "split APIs" where methods are available only for specific type parameter values, turning runtime checks into compile-time guarantees.

# Core Definition

Rust's type system is designed more like functional languages (like Haskell) rather than imperative languages (like Java and C++). A key part of this is the way generic types work. In C++ and Java, generic types are a meta-programming construct for the compiler -- `vector<int>` and `vector<char>` are just two different copies of the same boilerplate code. In Rust, a generic type parameter creates what is known in functional languages as a "type class constraint", and each different parameter filled in by an end user actually changes the type. `Vec<isize>` and `Vec<char>` are two different types, recognized as distinct by all parts of the type system. This is called **monomorphization**, where different types are created from **polymorphic** code. This special behavior requires `impl` blocks to specify generic parameters, and different values for the generic type cause different types that can have different `impl` blocks.

# Prerequisites

- **Ownership** -- understanding Rust's ownership model helps appreciate why compile-time type distinctions matter for safety

# Key Properties

1. `Vec<isize>` and `Vec<char>` are genuinely different types, not just different copies of the same template code
2. Different concrete generic types can have entirely different `impl` blocks with different methods
3. A generic `impl<P: ProtoKind> FileDownloadRequest<P>` provides methods for all variants, while `impl FileDownloadRequest<Nfs>` provides methods only for the NFS variant
4. Calling a method that does not exist on a particular generic instantiation is a compile-time error, not a runtime check
5. This eliminates the need for `Option` return types or runtime checks when protocol-specific behavior is known at compile time
6. The pattern can model "type states" where an object gains and loses API based on an internal state or invariant
7. The disadvantage is increased binary size due to monomorphization generating code for each concrete type

# Construction / Recognition

## To Apply This Pattern:
1. Identify a type that has multiple variants with both shared and variant-specific behavior
2. Create a trait that represents the variance (e.g., `ProtoKind`)
3. Make the main struct generic over that trait: `struct FileDownloadRequest<P: ProtoKind>`
4. Put shared methods in a generic `impl<P: ProtoKind>` block
5. Put variant-specific methods in concrete `impl` blocks (e.g., `impl FileDownloadRequest<Nfs>`)
6. Keep the trait and its implementations private to prevent external implementations if needed

## Example Structure:
```rust
use std::path::{Path, PathBuf};

mod proto_trait {
    pub(crate) trait ProtoKind {
        type AuthInfo;
        fn auth_info(&self) -> Self::AuthInfo;
    }

    pub struct Nfs { /* fields */ }
    pub struct Bootp();

    impl ProtoKind for Nfs {
        type AuthInfo = super::nfs::AuthInfo;
        fn auth_info(&self) -> Self::AuthInfo { /* ... */ }
    }
    impl ProtoKind for Bootp {
        type AuthInfo = super::bootp::AuthInfo;
        fn auth_info(&self) -> Self::AuthInfo { /* ... */ }
    }
}

struct FileDownloadRequest<P: ProtoKind> {
    file_name: PathBuf,
    protocol: P,
}

// Shared methods for all protocol types
impl<P: ProtoKind> FileDownloadRequest<P> {
    fn file_path(&self) -> &Path { &self.file_name }
    fn auth_info(&self) -> P::AuthInfo { self.protocol.auth_info() }
}

// NFS-only methods
impl FileDownloadRequest<Nfs> {
    fn mount_point(&self) -> &Path { self.protocol.mount_point() }
}
```

Calling `mount_point()` on a `FileDownloadRequest<Bootp>` is a compile-time error.

# Context & Application

The source motivates this pattern with a lab storage server that must handle both BOOTP (PXE boot) and NFS (remote mount) protocols. Without generics, protocol-specific methods would need to return `Option` and callers would need runtime checks even when the protocol is statically known. With generics, the type system enforces correct usage at compile time. This pattern is used throughout the Rust ecosystem: `Vec<u8>` has special methods not available on other `Vec<T>` types; iterators can convert to `BinaryHeap` only if the element type implements `Ord`; the `embedded-hal` crate uses it to statically verify device pin configurations; and the `hyper` HTTP library uses it for pluggable connector APIs.

# Examples

**Example 1** (Ch. 4, "Generics as Type Classes"): The naive approach without generics uses an enum for authentication and `Option<PathBuf>` for the mount point:

```rust
struct FileDownloadRequest {
    file_name: PathBuf,
    authentication: AuthInfo,
    mount_point: Option<PathBuf>,
}
```

Every caller of `mount_point()` must check for `None` and write code to handle it, even if they know only NFS requests are ever used in a given code path.

**Example 2** (Ch. 4, compile-time error): With the generic approach, attempting to call `mount_point()` on a BOOTP request:

```rust
let mut socket = crate::bootp::listen()?;
while let Some(request) = socket.next_request()? {
    match request.mount_point().as_ref() { // COMPILE ERROR
        "/secure" => socket.send("Access denied"),
        _ => {}
    }
}
```

The type `FileDownloadRequest<Bootp>` does not implement `mount_point()`, so this fails at compile time rather than at runtime.

# Relationships

## Builds Upon
- Rust's trait system and generic type parameters

## Enables
- The "type-state" pattern (objects gain/lose API based on generic state parameter)
- Compile-time protocol enforcement in library APIs

## Related
- **builder-pattern** -- if a type needs a "split API" due to construction or partial initialization, the builder pattern may be more appropriate
- **strategy-pattern** -- if the API between types does not change, only the behavior, the strategy pattern is a better fit
- **newtype-pattern** -- newtypes can serve a similar role of creating distinct types for compile-time enforcement
- **imperative-vs-declarative** -- this pattern reflects the functional language influence on Rust's type system

## Contrasts With
- C++ templates (code duplication without distinct types in the type system)
- Java generics (type erasure -- generic types are not distinct at runtime)

# Common Errors

- **Error**: Making the protocol trait public, allowing external code to create new protocol implementations that bypass intended constraints.
  **Correction**: The source keeps the trait module private (`mod proto_trait`) and only re-exports the concrete types, preventing external implementations.

- **Error**: Using this pattern when only behavior changes but the API stays the same.
  **Correction**: If all variants have the same methods with different implementations, use the strategy pattern (trait objects or generic trait bounds) instead.

# Common Confusions

- **Confusion**: Thinking this is just "generics" as in other languages.
  **Clarification**: Rust generics create genuinely distinct types through monomorphization. This enables different `impl` blocks per concrete type, which is not possible with C++ templates or Java generics in the same way.

- **Confusion**: Thinking the increased binary size from monomorphization is always a significant problem.
  **Clarification**: The source notes this as a disadvantage but expresses hope that compiler implementation will improve. In practice, the compile-time safety benefits usually outweigh the binary size cost.

# Source Reference

Chapter 4: Functional Usage of Rust, "Generics as Type Classes" section. The source provides a complete worked example with the BOOTP/NFS protocol scenario, advantages/disadvantages, alternatives (Builder and Strategy patterns), and references to standard library and ecosystem usage including embedded-hal, hyper, and the type-state pattern.

# Verification Notes

- Definition source: Direct quotation from the Description subsection, paragraphs 1-3
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides extensive explanation with a complete code example, advantages/disadvantages, alternatives, and ecosystem references
- Uncertainties: None for the definition
- Cross-reference status: `builder-pattern`, `strategy-pattern`, and `newtype-pattern` reference cards from other extraction agents; `imperative-vs-declarative` is a sibling card in this extraction set
