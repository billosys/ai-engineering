---
concept: Rust Smart Pointers
slug: rust-smart-pointers
category: language-semantics
subcategory: memory-management
tier: intermediate
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Smart Pointers"
chapter_number: 15
pdf_page: null
section: "Box<T>, Deref, Drop, Rc<T>, RefCell<T>, Reference Cycles, Weak<T>"
extraction_confidence: high
aliases:
  - "smart pointers"
  - "Box"
  - "Rc"
  - "RefCell"
  - "Deref trait"
  - "Drop trait"
  - "deref coercion"
  - "interior mutability"
  - "reference counting"
  - "Weak"
  - "reference cycles"
prerequisites: []
extends: []
related:
  - rust-concurrency
  - rust-oop-patterns
contrasts_with: []
answers_questions:
  - "What are smart pointers in Rust?"
  - "When should I use Box<T>?"
  - "How does the Deref trait work?"
  - "What is deref coercion?"
  - "How does the Drop trait work?"
  - "What is Rc<T> and when do I use it?"
  - "What is RefCell<T> and interior mutability?"
  - "What is the difference between Box<T>, Rc<T>, and RefCell<T>?"
  - "How do reference cycles cause memory leaks?"
  - "How does Weak<T> prevent reference cycles?"
  - "How do I enable recursive types in Rust?"
  - "Can I call drop explicitly?"
---

# Quick Definition

Smart pointers are data structures that act like pointers but have additional metadata and capabilities. Unlike references, which only borrow data, smart pointers often own the data they point to. Smart pointers are implemented as structs that implement the `Deref` and `Drop` traits. The most common smart pointers in the standard library are `Box<T>` (heap allocation), `Rc<T>` (reference counting for multiple ownership), and `RefCell<T>` (runtime-checked borrowing for interior mutability).

# Core Definition

**Smart Pointers vs. References**: "Smart pointers are data structures that act like a pointer but also have additional metadata and capabilities." While "references only borrow data, in many cases smart pointers own the data they point to." Smart pointers are "usually implemented using structs" and implement the `Deref` and `Drop` traits.

**`Box<T>`**: "The most straightforward smart pointer is a box, whose type is written `Box<T>`. Boxes allow you to store data on the heap rather than the stack." Boxes are used when: (1) you have a type whose size cannot be known at compile time, (2) you have a large amount of data and want to transfer ownership without copying, or (3) you want to own a value that implements a particular trait. Boxes enable recursive types by providing indirection: "Because a `Box<T>` is a pointer, Rust always knows how much space a `Box<T>` needs: A pointer's size doesn't change based on the amount of data it's pointing to."

**`Deref` Trait**: Implementing `Deref` "allows you to customize the behavior of the dereference operator `*`." The trait requires implementing a `deref` method that "borrows `self` and returns a reference to the inner data." When you write `*y`, Rust actually runs `*(y.deref())`. _Deref coercion_ "converts a reference to a type that implements the `Deref` trait into a reference to another type" -- for example, `&String` to `&str`. It is resolved at compile time with no runtime penalty. Rust performs deref coercion in three cases: `&T` to `&U` when `T: Deref<Target=U>`, `&mut T` to `&mut U` when `T: DerefMut<Target=U>`, and `&mut T` to `&U` when `T: Deref<Target=U>`. Immutable references never coerce to mutable references.

**`Drop` Trait**: "The `Drop` trait lets you customize what happens when a value is about to go out of scope." You implement a `drop` method that "takes a mutable reference to `self`." Variables are dropped in reverse order of creation. You cannot call the `Drop` trait's `drop` method manually -- Rust prevents this to avoid double free errors. Instead, use `std::mem::drop` to force early cleanup.

**`Rc<T>`**: "The `Rc<T>` type keeps track of the number of references to a value to determine whether or not the value is still in use." Used when "a single value might have multiple owners," such as graph data structures. `Rc::clone` only increments the reference count (not a deep copy). `Rc<T>` provides only immutable access and is "only for use in single-threaded scenarios." Use `Rc::strong_count` and `Rc::weak_count` to inspect reference counts.

**`RefCell<T>` and Interior Mutability**: "Interior mutability is a design pattern in Rust that allows you to mutate data even when there are immutable references to that data." With `RefCell<T>`, borrowing rules "are enforced at runtime" rather than compile time -- "if you break these rules, your program will panic and exit." `RefCell<T>` is also "only for use in single-threaded scenarios." Use `borrow()` for immutable access (returns `Ref<T>`) and `borrow_mut()` for mutable access (returns `RefMut<T>`). The common pattern `Rc<RefCell<T>>` enables multiple owners of mutable data.

**Choosing Between Smart Pointers**: "`Rc<T>` enables multiple owners of the same data; `Box<T>` and `RefCell<T>` have single owners. `Box<T>` allows immutable or mutable borrows checked at compile time; `Rc<T>` allows only immutable borrows checked at compile time; `RefCell<T>` allows immutable or mutable borrows checked at runtime."

**Reference Cycles and `Weak<T>`**: "Rust allows memory leaks by using `Rc<T>` and `RefCell<T>`: It's possible to create references where items refer to each other in a cycle." Strong references (`Rc::clone`) express ownership; weak references (`Rc::downgrade`) do not. `Weak<T>` references "don't express an ownership relationship, and their count doesn't affect when an `Rc<T>` instance is cleaned up." Call `upgrade()` on a `Weak<T>` to get `Option<Rc<T>>` -- returns `None` if the value has been dropped. Tree structures commonly use `Rc<T>` for parent-to-child (ownership) and `Weak<T>` for child-to-parent (non-ownership).

# Prerequisites

General understanding of Rust ownership, borrowing, and references (Chapter 4) is assumed. Knowledge of traits (Chapter 10) is helpful for understanding `Deref` and `Drop`.

# Key Properties

1. Smart pointers implement both `Deref` (pointer-like behavior) and `Drop` (cleanup on scope exit)
2. `Box<T>` stores data on the heap; the pointer itself lives on the stack
3. `Box<T>` enables recursive types through indirection (fixed pointer size)
4. Deref coercion happens at compile time with zero runtime cost
5. `DerefMut` enables mutable deref coercion; mutable-to-immutable coercion is allowed, but not the reverse
6. `Drop::drop` is called automatically in reverse order of creation; manual calls are forbidden
7. `std::mem::drop` (in the prelude) forces early cleanup of a value
8. `Rc::clone` only increments the reference count, not a deep copy
9. `Rc<T>` is single-threaded only; `Arc<T>` is the thread-safe equivalent
10. `RefCell<T>` enforces borrowing rules at runtime; violations cause panics, not compiler errors
11. `Rc<RefCell<T>>` enables multiple owners with interior mutability
12. `Weak<T>` prevents reference cycles; `upgrade()` returns `Option<Rc<T>>`
13. `Rc<T>` instances are cleaned up when `strong_count` reaches 0; `weak_count` has no effect on cleanup
14. Reference cycles with `Rc<T>` and `RefCell<T>` cause memory leaks (values never dropped)

# Construction / Recognition

## Smart Pointer Comparison Table

| Smart Pointer | Ownership | Borrow Checking | Mutability | Thread Safety |
|---------------|-----------|----------------|------------|---------------|
| `Box<T>` | Single | Compile time | Immutable or mutable | Send + Sync (if T is) |
| `Rc<T>` | Multiple | Compile time | Immutable only | Single-threaded only |
| `RefCell<T>` | Single | Runtime | Interior mutability | Single-threaded only |
| `Rc<RefCell<T>>` | Multiple | Runtime | Interior mutability | Single-threaded only |
| `Arc<T>` | Multiple | Compile time | Immutable only | Thread-safe |
| `Weak<T>` | Non-owning | N/A | N/A | Matches Rc/Arc |

## Recursive Type with Box

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}
```

## Deref Coercion Chain

`&MyBox<String>` -> `&String` -> `&str` (each step calls `deref()`)

## Interior Mutability Pattern

```rust
use std::cell::RefCell;
let data = RefCell::new(vec![1, 2, 3]);
data.borrow_mut().push(4);       // mutable borrow at runtime
println!("{:?}", data.borrow()); // immutable borrow at runtime
```

## Tree with Weak<T> for Parent References

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,       // non-owning
    children: RefCell<Vec<Rc<Node>>>,   // owning
}
```

# Context & Application

- **Typical contexts**: Recursive data structures (linked lists, trees, graphs), shared ownership scenarios, mock objects in testing, GUI component hierarchies.
- **Common applications**: `Box<T>` for heap allocation and trait objects; `Rc<T>` for graph structures where nodes have multiple parents; `RefCell<T>` for interior mutability when the compiler cannot prove correctness; `Weak<T>` for back-references in tree/graph structures that would otherwise create reference cycles.
- **Design guideline**: Prefer `Box<T>` when single ownership and compile-time checking suffice. Use `Rc<T>` only when multiple ownership is genuinely needed. Resort to `RefCell<T>` only when compile-time borrow checking is too conservative for a known-safe pattern. For multithreaded contexts, use `Arc<T>` and `Mutex<T>` instead of `Rc<T>` and `RefCell<T>`.

# Examples

**Example 1** -- Recursive type with `Box<T>` (Ch. 15, "Enabling Recursive Types with Boxes"):
```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}
use List::{Cons, Nil};
let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
```

**Example 2** -- Multiple ownership with `Rc<T>` (Ch. 15, "Sharing Data"):
```rust
use std::rc::Rc;
enum List {
    Cons(i32, Rc<List>),
    Nil,
}
let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
let b = Cons(3, Rc::clone(&a));  // a and b share ownership
let c = Cons(4, Rc::clone(&a));  // a, b, and c share ownership
```

**Example 3** -- Interior mutability with `Rc<RefCell<T>>` (Ch. 15, "Allowing Multiple Owners of Mutable Data"):
```rust
use std::cell::RefCell;
use std::rc::Rc;
let value = Rc::new(RefCell::new(5));
*value.borrow_mut() += 10;  // mutate through immutable Rc
println!("{}", value.borrow()); // prints: 15
```

**Example 4** -- Early drop with `std::mem::drop` (Ch. 15, "Dropping a Value Early"):
```rust
let c = CustomSmartPointer { data: String::from("some data") };
drop(c);  // forces c to be dropped immediately
// c is no longer usable here
```

# Relationships

## Builds Upon
No direct prerequisite cards in this batch.

## Enables
- **rust-concurrency** -- `Arc<T>` and `Mutex<T>` are the thread-safe counterparts of `Rc<T>` and `RefCell<T>`
- **rust-oop-patterns** -- trait objects (`Box<dyn Trait>`) rely on `Box<T>` and `Deref`

## Related
- **rust-concurrency** -- introduces `Arc<T>` as the thread-safe `Rc<T>` and `Mutex<T>` as the thread-safe `RefCell<T>`
- **rust-oop-patterns** -- uses `Box<dyn Trait>` for trait objects and dynamic dispatch

## Contrasts With
No direct contrasts within this batch.

# Common Errors

- **Error**: Trying to call the `Drop` trait's `drop` method directly on a value (e.g., `c.drop()`).
  **Correction**: Use `std::mem::drop(c)` instead. Rust forbids explicit `drop` calls to prevent double free errors.

- **Error**: Using `Rc<T>` in multithreaded code, getting `` `Rc<T>` cannot be sent between threads safely ``.
  **Correction**: Use `Arc<T>` for thread-safe reference counting. `Rc<T>` is designed for single-threaded use only.

- **Error**: Creating two mutable borrows from `RefCell<T>` in the same scope, causing a runtime panic.
  **Correction**: Ensure only one `borrow_mut()` is active at a time. The runtime panic message will be `already borrowed: BorrowMutError`.

# Common Confusions

- **Confusion**: `Rc::clone` performs a deep copy like `Clone::clone` typically does.
  **Clarification**: `Rc::clone` only increments the reference count, which is very cheap. Use the `Rc::clone(&value)` convention (not `value.clone()`) to visually distinguish reference count increments from deep copies.

- **Confusion**: `RefCell<T>` bypasses Rust's borrowing rules entirely.
  **Clarification**: `RefCell<T>` enforces the same borrowing rules (one mutable XOR many immutable) but checks them at runtime instead of compile time. Violations cause panics rather than compiler errors.

- **Confusion**: Using `Weak<T>` directly to access data.
  **Clarification**: You must call `upgrade()` on a `Weak<T>` to get an `Option<Rc<T>>`. The value may have been dropped, so you must handle the `None` case.

# Source Reference

The Rust Programming Language, Chapter 15: Smart Pointers -- Box<T>, Deref trait, Drop trait, Rc<T>, RefCell<T>, reference cycles, and Weak<T>.

# Verification Notes

- Definition source: Direct from Chapter 15 of The Rust Programming Language
- Confidence rationale: High -- concepts are well-documented with extensive code examples and clear explanations
- Uncertainties: None significant; these are stable, core library types
- Cross-reference status: Related cards (rust-concurrency, rust-oop-patterns) verified against planned card slugs
