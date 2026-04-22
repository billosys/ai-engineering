---
concept: API Predictability Guidelines
slug: api-predictability-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "05-predictability"
chapter_number: 5
pdf_page: null
section: "Predictability"
extraction_confidence: high
aliases:
  - "rust predictability guidelines"
  - "rust api predictability"
  - "C-SMART-PTR C-CONV-SPECIFIC C-METHOD C-NO-OUT C-OVERLOAD C-DEREF C-CTOR"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-naming-guidelines
  - api-interoperability-guidelines
  - api-flexibility-guidelines
contrasts_with: []
answers_questions:
  - "Why shouldn't smart pointers have inherent methods?"
  - "Where should conversion methods live?"
  - "When should a function be a method?"
  - "Why should Rust functions avoid out-parameters?"
  - "What are the rules for operator overloading?"
  - "When is it appropriate to implement Deref?"
  - "How should constructors be designed in Rust?"
---

# Quick Definition

The Predictability chapter of the Rust API Guidelines defines 7 guidelines (C-SMART-PTR, C-CONV-SPECIFIC, C-METHOD, C-NO-OUT, C-OVERLOAD, C-DEREF, C-CTOR) ensuring that crates enable legible code that acts how it looks. The central principle is that APIs should avoid surprising behavior: methods resolve as expected, operators behave mathematically, constructors follow conventions, and data flows through return values rather than out-parameters.

# Core Definition

**C-SMART-PTR** -- Smart pointers do not add inherent methods. Functions on smart pointers like `Box` take the smart pointer as a named parameter (not `self`) to avoid ambiguity with methods on the inner type accessed through Deref. For example, `Box::into_raw(b)` is a static function, not `b.into_raw()`, because the latter would be confusable with a method on the inner type `T`.

**C-CONV-SPECIFIC** -- Conversions live on the most specific type involved. Between two types, one is usually more "specific" (provides additional invariants). For example, `str` is more specific than `&[u8]` because it guarantees UTF-8. Place conversions on the more specific type: `str` provides both `as_bytes` and `from_utf8`. Prefer `to_`/`as_`/`into_` over `from_` because they are more ergonomic and chainable.

**C-METHOD** -- Functions with a clear receiver are methods. Prefer `impl Foo { pub fn frob(&self, w: widget) }` over `pub fn frob(foo: &Foo, w: widget)`. Methods have advantages: no import needed, autoborrowing, discoverability via rustdoc's "what can I do with type T," and concise self notation conveying ownership.

**C-NO-OUT** -- Functions do not take out-parameters. Prefer `fn foo() -> (Bar, Bar)` over `fn foo(output: &mut Bar) -> Bar`. Tuples and structs as return types are efficiently compiled without heap allocation. The exception is when the function modifies data the caller already owns, such as `fn read(&mut self, buf: &mut [u8])`.

**C-OVERLOAD** -- Operator overloads are unsurprising. Implement `Mul` only for operations resembling multiplication with expected properties like associativity. Operators come with strong user expectations.

**C-DEREF** -- Only smart pointers implement Deref and DerefMut. The Deref traits are used implicitly by the compiler for method resolution, specifically designed for smart pointers. Standard library examples: Box, String (smart pointer to str), Rc, Arc, Cow.

**C-CTOR** -- Constructors are static, inherent methods. The primary constructor is `new`, which may take arguments (like `Box::new(value)`). I/O types may use domain-specific names (`File::open`, `TcpStream::connect`). Secondary constructors can be suffixed `_with_foo`. Conversion constructors use `from_` prefix (for cases where `From<T>` is insufficient: unsafe conversions, additional arguments, or ambiguous bit representations). Both `Default` and `new()` should exist when reasonable and have the same behavior.

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework

# Key Properties

1. Smart pointer methods use static function syntax (`Box::into_raw(b)`) to avoid ambiguity with Deref-forwarded methods
2. Conversions live on the more specific type to avoid polluting generic types with endless conversion methods
3. Methods are preferred over free functions for discoverability, autoborrowing, and self notation
4. Return values (including tuples/structs) are preferred over out-parameters because they are efficiently compiled
5. Operator overloads must respect mathematical properties users expect (associativity, etc.)
6. Deref/DerefMut are reserved for smart pointers because the compiler uses them implicitly for method resolution
7. Constructor naming follows a hierarchy: `new` (primary), `_with_foo` (secondary), `from_` (conversion), domain-specific (I/O types)

# Construction / Recognition

## Applying the Predictability Guidelines:
1. **Smart pointers** (C-SMART-PTR): If your type implements Deref, do not add inherent methods that take `self`. Use associated functions with named parameters instead
2. **Conversion placement** (C-CONV-SPECIFIC): Identify which type is more specific. Place both directions of conversion on that type. Prefer `to_`/`as_`/`into_` (called on the specific type) over `from_` for ergonomics
3. **Methods vs functions** (C-METHOD): If an operation has a clear primary type, make it a method on that type. Use free functions only when there is no clear receiver
4. **Return values** (C-NO-OUT): Return multiple values as tuples or structs. Only use `&mut` parameters when modifying caller-owned data (like buffers)
5. **Operators** (C-OVERLOAD): Only implement std::ops traits when the operation genuinely resembles the mathematical operator
6. **Deref** (C-DEREF): Only implement Deref if your type is genuinely a smart pointer providing transparent access to an inner type
7. **Constructors** (C-CTOR): Use `new` for the primary constructor, `_with_foo` for variants, `from_` for conversions that cannot use `From<T>`, and domain names for I/O resources

## Distinguishing `from_` Constructors from `From<T>` (C-CTOR):
- `from_` can be unsafe; From cannot (e.g., `Box::from_raw`)
- `from_` can take extra arguments for disambiguation (e.g., `u64::from_str_radix`)
- From is only appropriate when the source type alone determines the encoding (not for raw bit reinterpretation like `u64::from_be`)

# Context & Application

Predictability means code reads the way it behaves. When users see `boxed_str.chars()`, they know it is a method on `str` accessed through Deref. When they see `Box::into_raw(boxed_str)`, the static call syntax signals this is a method on `Box` itself. When they see `fn foo() -> (A, B)`, they know data flows through return values. These conventions reduce the gap between reading code and understanding it.

The Deref guideline is particularly important: misusing Deref for non-smart-pointer types (sometimes called the "Deref polymorphism anti-pattern") creates confusion because the compiler silently inserts dereferences during method resolution.

# Examples

**Example 1** (C-SMART-PTR): `Box::into_raw` takes `Box<T>` as a named parameter:
```rust
impl<T> Box<T> where T: ?Sized {
    fn into_raw(b: Box<T>) -> *mut T { /* ... */ }
}
let ptr = Box::into_raw(boxed_str);
```
If this were `fn into_raw(self)`, then `boxed_str.into_raw()` would be ambiguous with methods on the inner type.

**Example 2** (C-CONV-SPECIFIC): `str` is more specific than `&[u8]` because it guarantees UTF-8. So `str` provides both `as_bytes` (str to bytes) and `from_utf8` (bytes to str). This avoids polluting `&[u8]` with str-specific conversion methods.

**Example 3** (C-NO-OUT): Prefer returning a tuple:
```rust
fn foo() -> (Bar, Bar)
```
Over using an out-parameter:
```rust
fn foo(output: &mut Bar) -> Bar
```
Exception: `fn read(&mut self, buf: &mut [u8]) -> io::Result<usize>` reuses a caller-owned buffer.

**Example 4** (C-CTOR): Constructor naming examples from the standard library:
- `Box::new(value)` -- primary constructor with argument
- `File::open(path)` -- domain-specific I/O constructor
- `Mmap::open_with_offset(...)` -- secondary constructor with `_with_` suffix
- `std::io::Error::from_raw_os_error(code)` -- conversion constructor that cannot use `From` because the source (an integer) is ambiguous

**Example 5** (C-DEREF): Standard library Deref implementations: `Box<T>`, `String` (derefs to `str`), `Rc<T>`, `Arc<T>`, `Cow<'a, T>`. These are all smart pointers providing transparent access to an inner value.

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories

## Enables
- Code that reads the way it behaves, reducing bugs from misunderstanding
- Clear ownership semantics visible from function signatures
- Unambiguous method resolution on smart pointer types

## Related
- **api-naming-guidelines** -- C-CONV (as_/to_/into_ naming) relates to C-CONV-SPECIFIC (where conversions live)
- **api-interoperability-guidelines** -- C-CONV-TRAITS (From/Into) relates to C-CTOR (from_ constructors)
- **api-flexibility-guidelines** -- C-GENERIC relates to accepting flexible parameters in methods

## Contrasts With
- C-style APIs using out-parameters for multiple return values
- Languages where Deref-like operator overloading is commonly used for non-pointer types
- Java-style static factory patterns without the `new` convention

# Common Errors

- **Error**: Adding inherent methods with `self` receiver to a smart pointer type.
  **Correction**: Use associated functions with named parameters (e.g., `Box::into_raw(b)` not `b.into_raw()`). This avoids ambiguity with Deref-forwarded methods.

- **Error**: Implementing Deref for a non-smart-pointer type to get "inheritance-like" method forwarding.
  **Correction**: Deref is reserved for smart pointers. Use explicit delegation, a trait, or composition instead.

- **Error**: Using out-parameters to return multiple values.
  **Correction**: Return a tuple or struct. Compound return types are efficiently compiled without heap allocation.

# Common Confusions

- **Confusion**: Thinking `from_` constructors and `From<T>` impls are interchangeable.
  **Clarification**: `from_` constructors serve three cases where `From<T>` cannot: unsafe construction (Box::from_raw), additional disambiguation arguments (u64::from_str_radix), and ambiguous bit representations (u64::from_be, String::from_utf8).

- **Confusion**: Thinking the `new` constructor should always take no arguments.
  **Clarification**: `new` may take arguments -- `Box::new(value)` is the standard example. It is the "primary method of instantiating a type" regardless of arity.

- **Confusion**: Thinking methods are always better than free functions.
  **Clarification**: Methods are preferred when there is a clear receiver. Some operations (like conversion functions between two equally specific types) may be better as free functions.

# Source Reference

Chapter 5: Predictability. All 7 guidelines (C-SMART-PTR, C-CONV-SPECIFIC, C-METHOD, C-NO-OUT, C-OVERLOAD, C-DEREF, C-CTOR) are covered with examples from the standard library (Box, str, Vec, File, TcpStream) and ecosystem crates (TempDir, Mmap).

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit rationale in each section
- Confidence: HIGH -- the predictability guidelines are concrete with clear code examples
- Uncertainties: None -- the guidelines are unambiguous
- Cross-reference status: All slugs reference cards in this extraction set
