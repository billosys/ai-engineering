r[memory]
# Memory model

> [!WARNING]
> The memory model of Rust is incomplete and not fully decided.

r[memory.bytes]
## Bytes

r[memory.bytes.intro]
The most basic unit of memory in Rust is a byte.

> [!NOTE]
> While bytes are typically lowered to hardware bytes, Rust uses an "abstract" notion of bytes that can make distinctions which are absent in hardware, such as being uninitialized, or storing part of a pointer. Those distinctions can affect whether your program has undefined behavior, so they still have tangible impact on how compiled Rust programs behave.

r[memory.bytes.contents]
Each byte may have one of the following values:

r[memory.bytes.init]
* An initialized byte containing a `u8` value and optional [provenance][std::ptr#provenance],

r[memory.bytes.uninit]
* An uninitialized byte.

> [!NOTE]
> The above list is not yet guaranteed to be exhaustive.


---

r[alloc]
# Memory allocation and lifetime

r[alloc.static]
The _items_ of a program are those functions, modules, and types that have their
value calculated at compile-time and stored uniquely in the memory image of the
rust process. Items are neither dynamically allocated nor freed.

r[alloc.dynamic]
The _heap_ is a general term that describes boxes.  The lifetime of an
allocation in the heap depends on the lifetime of the box values pointing to
it. Since box values may themselves be passed in and out of frames, or stored
in the heap, heap allocations may outlive the frame they are allocated within.
An allocation in the heap is guaranteed to reside at a single location in the
heap for the whole lifetime of the allocation - it will never be relocated as
a result of moving a box value.


---

r[variable]
# Variables

r[variable.intro]
A _variable_ is a component of a stack frame, either a named function parameter,
an anonymous [temporary](expressions.md#temporaries), or a named local
variable.

r[variable.local]
A _local variable_ (or *stack-local* allocation) holds a value directly,
allocated within the stack's memory. The value is a part of the stack frame.

r[variable.local-mut]
Local variables are immutable unless declared otherwise. For example:
`let mut x = ...`.

r[variable.param-mut]
Function parameters are immutable unless declared with `mut`. The `mut` keyword
applies only to the following parameter. For example: `|mut x, y|` and
`fn f(mut x: Box<i32>, y: Box<i32>)` declare one mutable variable `x` and one
immutable variable `y`.

r[variable.init]
Local variables are not initialized when allocated. Instead, the entire frame
worth of local variables are allocated, on frame-entry, in an uninitialized
state. Subsequent statements within a function may or may not initialize the
local variables. Local variables can be used only after they have been
initialized through all reachable control flow paths.

In this next example, `init_after_if` is initialized after the [`if` expression]
while `uninit_after_if` is not because it is not initialized in the `else` case.

```rust
# fn random_bool() -> bool { true }
fn initialization_example() {
    let init_after_if: ();
    let uninit_after_if: ();

    if random_bool() {
        init_after_if = ();
        uninit_after_if = ();
    } else {
        init_after_if = ();
    }

    init_after_if; // ok
    // uninit_after_if; // err: use of possibly uninitialized `uninit_after_if`
}
```

[`if` expression]: expressions/if-expr.md#if-expressions
