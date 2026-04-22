---
concept: Rust OOP Patterns
slug: rust-oop-patterns
category: design-patterns
subcategory: object-oriented-patterns
tier: intermediate
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Object-Oriented Programming Features"
chapter_number: 18
pdf_page: null
section: "OOP Characteristics, Trait Objects, State Pattern, Type-State Pattern"
extraction_confidence: high
aliases:
  - "OOP in Rust"
  - "trait objects"
  - "dynamic dispatch"
  - "static dispatch"
  - "dyn keyword"
  - "state pattern"
  - "type-state pattern"
  - "duck typing"
  - "polymorphism"
  - "encapsulation"
prerequisites:
  - rust-smart-pointers
extends: []
related:
  - rust-smart-pointers
  - rust-async-await
contrasts_with: []
answers_questions:
  - "Is Rust an object-oriented language?"
  - "What are trait objects in Rust?"
  - "How does dynamic dispatch work in Rust?"
  - "What is the difference between static and dynamic dispatch?"
  - "How does Rust achieve polymorphism without inheritance?"
  - "How do I implement the state pattern in Rust?"
  - "What is the type-state pattern and how does it differ from the traditional state pattern?"
  - "How does encapsulation work in Rust?"
  - "Why doesn't Rust have inheritance?"
  - "What is dyn compatibility (object safety)?"
  - "How do trait objects compare to generics with trait bounds?"
---

# Quick Definition

Rust supports many object-oriented concepts -- encapsulation via `pub`, polymorphism via trait objects (`dyn Trait`) and generics, and code reuse via default trait method implementations -- but deliberately omits inheritance. Trait objects enable runtime polymorphism through dynamic dispatch at the cost of some performance, while generics provide compile-time polymorphism via static dispatch. The chapter demonstrates two approaches to the state pattern: a traditional OOP version using trait objects, and an idiomatic Rust version that encodes states as distinct types, catching invalid state transitions at compile time.

# Core Definition

**OOP Characteristics in Rust**: The Gang of Four defines objects as packaging "both data and the procedures that operate on that data." By this definition, "Rust is object oriented: Structs and enums have data, and `impl` blocks provide methods." Encapsulation is supported through `pub` visibility -- "by default everything else is private." Regarding inheritance, "There is no way to define a struct that inherits the parent object's fields and method implementations without using a macro." Rust provides alternatives: default trait method implementations for code reuse, and trait objects for polymorphism.

**Polymorphism Without Inheritance**: "Rust instead uses generics to abstract over different possible types and trait bounds to impose constraints on what those types must provide. This is sometimes called bounded parametric polymorphism." Inheritance is rejected because it "is often at risk of sharing more code than necessary" and can make designs "less flexible."

**Trait Objects**: "A trait object points to both an instance of a type implementing our specified trait and a table used to look up trait methods on that type at runtime." Created with `dyn` keyword: `Box<dyn Draw>`. "Trait objects aren't as generally useful as objects in other languages: Their specific purpose is to allow abstraction across common behavior." A key difference from generics: "A generic type parameter can be substituted with only one concrete type at a time, whereas trait objects allow for multiple concrete types to fill in for the trait object at runtime."

**Static vs. Dynamic Dispatch**: With generics, the compiler performs _monomorphization_ -- "the compiler generates nongeneric implementations of functions and methods for each concrete type" (static dispatch). With trait objects, "Rust must use dynamic dispatch. The compiler doesn't know all the types that might be used with the code that's using trait objects, so it doesn't know which method implemented on which type to call. Instead, at runtime, Rust uses the pointers inside the trait object to know which method to call." Dynamic dispatch "prevents the compiler from choosing to inline a method's code, which in turn prevents some optimizations."

**State Pattern (Traditional OOP Style)**: The state pattern "defines a set of states a value can have internally. The states are represented by a set of state objects, and the value's behavior changes based on its state." Implemented in Rust with a `State` trait and `Box<dyn State>`. State transitions consume the old state via `self: Box<Self>` parameter and return a new boxed state. The `Post` struct wraps the state in `Option<Box<dyn State>>` to allow `take()` for ownership transfer. Each state struct implements the `State` trait independently -- "The request_review method on Post is the same no matter its state value. Each state is responsible for its own rules."

**Type-State Pattern (Idiomatic Rust)**: Rather than runtime state objects, "encode the states into different types" -- `DraftPost`, `PendingReviewPost`, and `Post`. State transitions consume one type and return another: `DraftPost::request_review(self) -> PendingReviewPost`. The `content` method exists only on `Post` (published), so "if we try to get a draft post's content, we'll get a compiler error telling us the method doesn't exist." This makes "invalid states and transitions into compile-time errors."

# Prerequisites

- **rust-smart-pointers** -- `Box<dyn Trait>` (trait objects) requires understanding `Box<T>` and the `Deref` trait

# Key Properties

1. Rust supports encapsulation (`pub`), polymorphism (traits), but not inheritance
2. Default trait method implementations serve as Rust's alternative to code reuse via inheritance
3. Trait objects (`Box<dyn Trait>`) enable heterogeneous collections of different types implementing the same trait
4. Dynamic dispatch uses a vtable at runtime; static dispatch (generics) uses monomorphization at compile time
5. Dynamic dispatch prevents inlining and some optimizations; static dispatch has no runtime cost
6. Generics constrain a container to one concrete type; trait objects allow mixing types at runtime
7. `dyn` keyword is required for trait objects to distinguish from static dispatch
8. Trait objects have dyn compatibility (object safety) rules restricting which traits can be used
9. Traditional state pattern uses `Box<dyn State>` with `Option::take()` for ownership-safe state transitions
10. `self: Box<Self>` parameter in trait methods consumes the boxed state, enabling state transitions
11. Type-state pattern encodes states as distinct types, making invalid transitions a compile-time error
12. Type-state transitions consume the old type (`self`) and return a new type, using Rust's ownership system

# Construction / Recognition

## Trait Object vs. Generic

```rust
// Trait object: heterogeneous, dynamic dispatch
struct Screen {
    components: Vec<Box<dyn Draw>>,  // can mix Button, TextField, etc.
}

// Generic: homogeneous, static dispatch
struct Screen<T: Draw> {
    components: Vec<T>,  // all elements must be the same type
}
```

## Dispatch Comparison

| Approach | Dispatch | Type Mixing | Performance | Flexibility |
|----------|----------|-------------|-------------|-------------|
| Generics + trait bounds | Static (compile time) | One type per instantiation | Optimal (inlining) | Known types at compile time |
| `dyn Trait` | Dynamic (runtime) | Multiple types in one collection | vtable overhead | Extensible at runtime |

## Traditional State Pattern Structure

```rust
trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
    fn content<'a>(&self, post: &'a Post) -> &'a str { "" }
}
struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}
struct Draft;
struct PendingReview;
struct Published;
```

## Type-State Pattern Structure

```rust
struct DraftPost { content: String }
struct PendingReviewPost { content: String }
struct Post { content: String }

impl DraftPost {
    fn request_review(self) -> PendingReviewPost { /* ... */ }
}
impl PendingReviewPost {
    fn approve(self) -> Post { /* ... */ }
}
impl Post {
    fn content(&self) -> &str { &self.content }
}
// DraftPost and PendingReviewPost have NO content() method
```

# Context & Application

- **Typical contexts**: GUI frameworks with heterogeneous component lists, plugin systems, workflow engines, state machines.
- **Common applications**: Building extensible libraries where users define new types that conform to a trait; implementing state machines for business workflows (e.g., blog post draft/review/publish); creating heterogeneous collections of drawable components.
- **Design guidelines**: Prefer generics with trait bounds when all types are known at compile time (better performance via monomorphization). Use trait objects when you need heterogeneous collections or the set of types is open-ended. Consider the type-state pattern when invalid state transitions should be compile-time errors. Use the traditional state pattern when states need to change at runtime and encapsulation of state logic is more important than compile-time guarantees.
- **Rust vs. OOP tradeoff**: "Even though Rust is capable of implementing object-oriented design patterns, other patterns, such as encoding state into the type system, are also available in Rust. These patterns have different trade-offs."

# Examples

**Example 1** -- Trait object for heterogeneous drawing (Ch. 18, "Using Trait Objects"):
```rust
pub trait Draw {
    fn draw(&self);
}
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();  // dynamic dispatch
        }
    }
}
```

**Example 2** -- Extending the library with a user-defined type (Ch. 18, "Implementing the Trait"):
```rust
struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}
impl Draw for SelectBox {
    fn draw(&self) { /* render select box */ }
}
// Can be added to Screen alongside Button:
let screen = Screen {
    components: vec![
        Box::new(SelectBox { width: 75, height: 10, options: vec![] }),
        Box::new(Button { width: 50, height: 10, label: String::from("OK") }),
    ],
};
```

**Example 3** -- State pattern with trait objects (Ch. 18, "Implementing an Object-Oriented Design Pattern"):
```rust
impl Post {
    pub fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review());
        }
    }
}
impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {})
    }
    // approve returns self (no-op for Draft)
}
```

**Example 4** -- Type-state pattern encoding state transitions as types (Ch. 18, "Encoding States and Behavior as Types"):
```rust
let mut post = Post::new();         // returns DraftPost
post.add_text("hello");
let post = post.request_review();   // consumes DraftPost, returns PendingReviewPost
let post = post.approve();          // consumes PendingReviewPost, returns Post
println!("{}", post.content());     // only Post has content()
// post.add_text("more");           // ERROR: Post has no add_text method
```

# Relationships

## Builds Upon
- **rust-smart-pointers** -- `Box<dyn Trait>` for trait objects; `Deref` coercion for method dispatch

## Enables
No directly enabled cards within this batch.

## Related
- **rust-smart-pointers** -- `Box<T>` is the primary pointer type for trait objects
- **rust-async-await** -- async trait objects use `Box<dyn Future>`, connecting these concepts

## Contrasts With
No direct contrasts within this batch.

# Common Errors

- **Error**: Using a type that does not implement the required trait as a trait object, getting "the trait `Draw` is not implemented for `String`."
  **Correction**: Only types that implement the trait can be used as trait objects. Implement the trait on the type, or use a type that already implements it.

- **Error**: In the traditional state pattern, trying to move `state` out of `&self` without using `Option::take()`.
  **Correction**: Wrap the state in `Option<Box<dyn State>>` and use `self.state.take()` to move the value out, leaving `None` temporarily. Then assign the new state back.

- **Error**: Using `self` instead of `self: Box<Self>` for state transition methods, preventing ownership transfer.
  **Correction**: State transition methods should take `self: Box<Self>` to consume the boxed state. This ensures the old state is invalidated and the new state is returned.

# Common Confusions

- **Confusion**: Rust is not object-oriented because it lacks inheritance.
  **Clarification**: By the Gang of Four definition (objects = data + methods), Rust is object-oriented. It supports encapsulation and polymorphism but deliberately replaces inheritance with trait-based composition, which avoids the tight coupling and "diamond problem" of traditional inheritance.

- **Confusion**: Trait objects and generics with trait bounds are interchangeable.
  **Clarification**: Generics use static dispatch (monomorphized at compile time, one concrete type per instantiation). Trait objects use dynamic dispatch (vtable lookup at runtime, multiple types in one collection). Generics are faster but less flexible; trait objects are more flexible but have runtime overhead.

- **Confusion**: The type-state pattern and the traditional state pattern solve the same problem equally well.
  **Clarification**: The type-state pattern catches invalid state transitions at compile time but requires API changes (methods return new types, requiring re-binding). The traditional state pattern encapsulates state internally but pushes error detection to runtime or logic bugs. Choose based on whether compile-time safety or internal encapsulation is more important.

# Source Reference

The Rust Programming Language, Chapter 18: Object-Oriented Programming Features -- OOP Characteristics, Trait Objects, Dynamic Dispatch, the State Pattern (traditional and type-state variants).

# Verification Notes

- Definition source: Direct from Chapter 18 of The Rust Programming Language
- Confidence rationale: High -- trait objects, dynamic dispatch, and the state pattern are well-documented with complete code examples
- Uncertainties: Dyn compatibility (object safety) rules are mentioned but not fully enumerated in this chapter; the reference provides complete rules
- Cross-reference status: Related cards verified against planned card slugs (rust-smart-pointers, rust-async-await)
