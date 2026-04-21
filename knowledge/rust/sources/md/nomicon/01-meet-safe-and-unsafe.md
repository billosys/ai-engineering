# Meet Safe and Unsafe

![safe and unsafe](img/safeandunsafe.svg)

It would be great to not have to worry about low-level implementation details.
Who could possibly care how much space the empty tuple occupies? Sadly, it
sometimes matters and we need to worry about it. The most common reason
developers start to care about implementation details is performance, but more
importantly, these details can become a matter of correctness when interfacing
directly with hardware, operating systems, or other languages.

When implementation details start to matter in a safe programming language,
programmers usually have three options:

* fiddle with the code to encourage the compiler/runtime to perform an optimization
* adopt a more unidiomatic or cumbersome design to get the desired implementation
* rewrite the implementation in a language that lets you deal with those details

For that last option, the language programmers tend to use is *C*. This is often
necessary to interface with systems that only declare a C interface.

Unfortunately, C is incredibly unsafe to use (sometimes for good reason),
and this unsafety is magnified when trying to interoperate with another
language. Care must be taken to ensure C and the other language agree on
what's happening, and that they don't step on each other's toes.

So what does this have to do with Rust?

Well, unlike C, Rust is a safe programming language.

But, like C, Rust is an unsafe programming language.

More accurately, Rust *contains* both a safe and unsafe programming language.

Rust can be thought of as a combination of two programming languages: *Safe
Rust* and *Unsafe Rust*. Conveniently, these names mean exactly what they say:
Safe Rust is Safe. Unsafe Rust is, well, not. In fact, Unsafe Rust lets us
do some *really* unsafe things. Things the Rust authors will implore you not to
do, but we'll do anyway.

Safe Rust is the *true* Rust programming language. If all you do is write Safe
Rust, you will never have to worry about type-safety or memory-safety. You will
never endure a dangling pointer, a use-after-free, or any other kind of
Undefined Behavior (a.k.a. UB).

The standard library also gives you enough utilities out of the box that you'll
be able to write high-performance applications and libraries in pure idiomatic
Safe Rust.

But maybe you want to talk to another language. Maybe you're writing a
low-level abstraction not exposed by the standard library. Maybe you're
*writing* the standard library (which is written entirely in Rust). Maybe you
need to do something the type-system doesn't understand and just *frob some dang
bits*. Maybe you need Unsafe Rust.

Unsafe Rust is exactly like Safe Rust with all the same rules and semantics.
It just lets you do some *extra* things that are Definitely Not Safe
(which we will define in the next section).

The value of this separation is that we gain the benefits of using an unsafe
language like C — low level control over implementation details — without most
of the problems that come with trying to integrate it with a completely
different safe language.

There are still some problems — most notably, we must become aware of properties
that the type system assumes and audit them in any code that interacts with
Unsafe Rust. That's the purpose of this book: to teach you about these assumptions
and how to manage them.


---

# How Safe and Unsafe Interact

What's the relationship between Safe Rust and Unsafe Rust? How do they
interact?

The separation between Safe Rust and Unsafe Rust is controlled with the
`unsafe` keyword, which acts as an interface from one to the other. This is
why we can say Safe Rust is a safe language: all the unsafe parts are kept
exclusively behind the `unsafe` boundary. If you wish, you can even toss
`#![forbid(unsafe_code)]` into your code base to statically guarantee that
you're only writing Safe Rust.

The `unsafe` keyword has two uses: to declare the existence of contracts the
compiler can't check, and to declare that a programmer has checked that these
contracts have been upheld.

You can use `unsafe` to indicate the existence of unchecked contracts on
_functions_ and _trait declarations_. On functions, `unsafe` means that
users of the function must check that function's documentation to ensure
they are using it in a way that maintains the contracts the function
requires. On trait declarations, `unsafe` means that implementors of the
trait must check the trait documentation to ensure their implementation
maintains the contracts the trait requires.

You can use `unsafe` on a block to declare that all unsafe actions performed
within are verified to uphold the contracts of those operations. For instance,
the index passed to [`slice::get_unchecked`][get_unchecked] is in-bounds.

You can use `unsafe` on a trait implementation to declare that the implementation
upholds the trait's contract. For instance, that a type implementing [`Send`] is
really safe to move to another thread.

The standard library has a number of unsafe functions, including:

* [`slice::get_unchecked`][get_unchecked], which performs unchecked indexing,
  allowing memory safety to be freely violated.
* [`mem::transmute`][transmute] reinterprets some value as having a given type,
  bypassing type safety in arbitrary ways (see [conversions] for details).
* Every raw pointer to a sized type has an [`offset`][ptr_offset] method that
  invokes Undefined Behavior if the passed offset is not ["in bounds"][ptr_offset].
* All FFI (Foreign Function Interface) functions are `unsafe` to call because the
  other language can do arbitrary operations that the Rust compiler can't check.

As of Rust 1.29.2, the standard library defines the following unsafe traits
(there are others, but they are not stabilized yet and some of them may never
be):

* [`Send`] is a marker trait (a trait with no API) that promises implementors
  are safe to send (move) to another thread.
* [`Sync`] is a marker trait that promises threads can safely share implementors
  through a shared reference.
* [`GlobalAlloc`] allows customizing the memory allocator of the whole program.

Much of the Rust standard library also uses Unsafe Rust internally. These
implementations have generally been rigorously manually checked, so the Safe Rust
interfaces built on top of these implementations can be assumed to be safe.

The need for all of this separation boils down to a single fundamental property
of Safe Rust, the *soundness property*:

**No matter what, Safe Rust can't cause Undefined Behavior.**

The design of the safe/unsafe split means that there is an asymmetric trust
relationship between Safe and Unsafe Rust. Safe Rust inherently has to
trust that any Unsafe Rust it touches has been written correctly.
On the other hand, Unsafe Rust cannot trust Safe Rust without care.

As an example, Rust has the [`PartialOrd`] and [`Ord`] traits to differentiate
between types which can "just" be compared, and those that provide a "total"
ordering (which basically means that comparison behaves reasonably).

[`BTreeMap`] doesn't really make sense for partially-ordered types, and so it
requires that its keys implement `Ord`. However, `BTreeMap` has Unsafe Rust code
inside of its implementation. Because it would be unacceptable for a sloppy `Ord`
implementation (which is Safe to write) to cause Undefined Behavior, the Unsafe
code in BTreeMap must be written to be robust against `Ord` implementations which
aren't actually total — even though that's the whole point of requiring `Ord`.

The Unsafe Rust code just can't trust the Safe Rust code to be written correctly.
That said, `BTreeMap` will still behave completely erratically if you feed in
values that don't have a total ordering. It just won't ever cause Undefined
Behavior.

One may wonder, if `BTreeMap` cannot trust `Ord` because it's Safe, why can it
trust *any* Safe code? For instance `BTreeMap` relies on integers and slices to
be implemented correctly. Those are safe too, right?

The difference is one of scope. When `BTreeMap` relies on integers and slices,
it's relying on one very specific implementation. This is a measured risk that
can be weighed against the benefit. In this case there's basically zero risk;
if integers and slices are broken, *everyone* is broken. Also, they're maintained
by the same people who maintain `BTreeMap`, so it's easy to keep tabs on them.

On the other hand, `BTreeMap`'s key type is generic. Trusting its `Ord` implementation
means trusting every `Ord` implementation in the past, present, and future.
Here the risk is high: someone somewhere is going to make a mistake and mess up
their `Ord` implementation, or even just straight up lie about providing a total
ordering because "it seems to work". When that happens, `BTreeMap` needs to be
prepared.

The same logic applies to trusting a closure that's passed to you to behave
correctly.

This problem of unbounded generic trust is the problem that `unsafe` traits
exist to resolve. The `BTreeMap` type could theoretically require that keys
implement a new trait called `UnsafeOrd`, rather than `Ord`, that might look
like this:

```rust
use std::cmp::Ordering;

unsafe trait UnsafeOrd {
    fn cmp(&self, other: &Self) -> Ordering;
}
```

Then, a type would use `unsafe` to implement `UnsafeOrd`, indicating that
they've ensured their implementation maintains whatever contracts the
trait expects. In this situation, the Unsafe Rust in the internals of
`BTreeMap` would be justified in trusting that the key type's `UnsafeOrd`
implementation is correct. If it isn't, it's the fault of the unsafe trait
implementation, which is consistent with Rust's safety guarantees.

The decision of whether to mark a trait `unsafe` is an API design choice. A
safe trait is easier to implement, but any unsafe code that relies on it must
defend against incorrect behavior. Marking a trait `unsafe` shifts this
responsibility to the implementor. Rust has traditionally avoided marking
traits `unsafe` because it makes Unsafe Rust pervasive, which isn't desirable.

`Send` and `Sync` are marked unsafe because thread safety is a *fundamental
property* that unsafe code can't possibly hope to defend against in the way it
could defend against a buggy `Ord` implementation. Similarly, `GlobalAlloc`
is keeping accounts of all the memory in the program and other things like
`Box` or `Vec` that build on top of it. If it does something weird (giving the same
chunk of memory to another request when it is still in use), there's no chance
to detect that and do anything about it.

The decision of whether to mark your own traits `unsafe` depends on the same
sort of consideration. If `unsafe` code can't reasonably expect to defend
against a broken implementation of the trait, then marking the trait `unsafe` is
a reasonable choice.

As an aside, while `Send` and `Sync` are `unsafe` traits, they are *also*
automatically implemented for types when such derivations are provably safe
to do. `Send` is automatically derived for all types composed only of values
whose types also implement `Send`. `Sync` is automatically derived for all
types composed only of values whose types also implement `Sync`. This minimizes
the pervasive unsafety of making these two traits `unsafe`. And not many people
are going to *implement* memory allocators (or use them directly, for that
matter).

This is the balance between Safe and Unsafe Rust. The separation is designed to
make using Safe Rust as ergonomic as possible, but requires extra effort and
care when writing Unsafe Rust. The rest of this book is largely a discussion
of the sort of care that must be taken, and what contracts Unsafe Rust must uphold.

[`Send`]: ../std/marker/trait.Send.html
[`Sync`]: ../std/marker/trait.Sync.html
[`GlobalAlloc`]: ../std/alloc/trait.GlobalAlloc.html
[conversions]: conversions.html
[ptr_offset]: ../std/primitive.pointer.html#method.offset
[get_unchecked]: ../std/primitive.slice.html#method.get_unchecked
[transmute]: ../std/mem/fn.transmute.html
[`PartialOrd`]: ../std/cmp/trait.PartialOrd.html
[`Ord`]: ../std/cmp/trait.Ord.html
[`BTreeMap`]: ../std/collections/struct.BTreeMap.html


---

# What Unsafe Rust Can Do

The only things that are different in Unsafe Rust are that you can:

* Dereference raw pointers
* Call `unsafe` functions (including C functions, compiler intrinsics, and the raw allocator)
* Implement `unsafe` traits
* Access or modify mutable statics
* Access fields of `union`s

That's it. The reason these operations are relegated to Unsafe is that misusing
any of these things will cause the ever dreaded Undefined Behavior. Invoking
Undefined Behavior gives the compiler full rights to do arbitrarily bad things
to your program. You definitely *should not* invoke Undefined Behavior.

Unlike C, Undefined Behavior is pretty limited in scope in Rust. All the core
language cares about is preventing the following things:

* Dereferencing (using the `*` operator on) dangling or unaligned pointers (see below)
* Breaking the [pointer aliasing rules][]
* Calling a function with the wrong call ABI or unwinding from a function with the wrong unwind ABI.
* Causing a [data race][race]
* Executing code compiled with [target features][] that the current thread of execution does
  not support
* Producing invalid values (either alone or as a field of a compound type such
  as `enum`/`struct`/array/tuple):
  * a `bool` that isn't 0 or 1
  * an `enum` with an invalid discriminant
  * a null `fn` pointer
  * a `char` outside the ranges [0x0, 0xD7FF] and [0xE000, 0x10FFFF]
  * a `!` (all values are invalid for this type)
  * an integer (`i*`/`u*`), floating point value (`f*`), or raw pointer read from
    [uninitialized memory][], or uninitialized memory in a `str`.
  * a reference/`Box` that is dangling, unaligned, or points to an invalid value.
  * a wide reference, `Box`, or raw pointer that has invalid metadata:
    * `dyn Trait` metadata is invalid if it is not a pointer to a vtable for
      `Trait` that matches the actual dynamic trait the pointer or reference points to
    * slice metadata is invalid if the length is not a valid `usize`
      (i.e., it must not be read from uninitialized memory)
  * a type with custom invalid values that is one of those values, such as a
    [`NonNull`] that is null. (Requesting custom invalid values is an unstable
    feature, but some stable libstd types, like `NonNull`, make use of it.)

For a more detailed explanation about "Undefined Behavior", you may refer to
[the reference][behavior-considered-undefined].

"Producing" a value happens any time a value is assigned, passed to a
function/primitive operation or returned from a function/primitive operation.

A reference/pointer is "dangling" if it is null or not all of the bytes it
points to are part of the same allocation (so in particular they all have to be
part of *some* allocation). The span of bytes it points to is determined by the
pointer value and the size of the pointee type. As a consequence, if the span is
empty, "dangling" is the same as "null". Note that slices and strings point
to their entire range, so it's important that the length metadata is never too
large (in particular, allocations and therefore slices and strings cannot be
bigger than `isize::MAX` bytes). If for some reason this is too cumbersome,
consider using raw pointers.

That's it. That's all the causes of Undefined Behavior baked into Rust. Of
course, unsafe functions and traits are free to declare arbitrary other
constraints that a program must maintain to avoid Undefined Behavior. For
instance, the allocator APIs declare that deallocating unallocated memory is
Undefined Behavior.

However, violations of these constraints generally will just transitively lead to one of
the above problems. Some additional constraints may also derive from compiler
intrinsics that make special assumptions about how code can be optimized. For instance,
Vec and Box make use of intrinsics that require their pointers to be non-null at all times.

Rust is otherwise quite permissive with respect to other dubious operations.
Rust considers it "safe" to:

* Deadlock
* Have a [race condition][race]
* Leak memory
* Overflow integers (with the built-in operators such as `+` etc.)
* Abort the program
* Delete the production database

For more detailed information, you may refer to [the reference][behavior-not-considered-unsafe].

However any program that actually manages to do such a thing is *probably*
incorrect. Rust provides lots of tools to make these things rare, but
these problems are considered impractical to categorically prevent.

[pointer aliasing rules]: references.html
[uninitialized memory]: uninitialized.html
[race]: races.html
[target features]: ../reference/attributes/codegen.html#the-target_feature-attribute
[`NonNull`]: ../std/ptr/struct.NonNull.html
[behavior-considered-undefined]: ../reference/behavior-considered-undefined.html
[behavior-not-considered-unsafe]: ../reference/behavior-not-considered-unsafe.html


---

# Working with Unsafe

Rust generally only gives us the tools to talk about Unsafe Rust in a scoped and
binary manner. Unfortunately, reality is significantly more complicated than
that. For instance, consider the following toy function:

```rust
fn index(idx: usize, arr: &[u8]) -> Option<u8> {
    if idx < arr.len() {
        unsafe {
            Some(*arr.get_unchecked(idx))
        }
    } else {
        None
    }
}
```

This function is safe and correct. We check that the index is in bounds, and if
it is, index into the array in an unchecked manner. We say that such a correct
unsafely implemented function is *sound*, meaning that safe code cannot cause
Undefined Behavior through it (which, remember, is the single fundamental
property of Safe Rust).

But even in such a trivial function, the scope of the unsafe block is
questionable. Consider changing the `<` to a `<=`:

```rust
fn index(idx: usize, arr: &[u8]) -> Option<u8> {
    if idx <= arr.len() {
        unsafe {
            Some(*arr.get_unchecked(idx))
        }
    } else {
        None
    }
}
```

This program is now *unsound*, Safe Rust can cause Undefined Behavior, and yet
*we only modified safe code*. This is the fundamental problem of safety: it's
non-local. The soundness of our unsafe operations necessarily depends on the
state established by otherwise "safe" operations.

Safety is modular in the sense that opting into unsafety doesn't require you
to consider arbitrary other kinds of badness. For instance, doing an unchecked
index into a slice doesn't mean you suddenly need to worry about the slice being
null or containing uninitialized memory. Nothing fundamentally changes. However
safety *isn't* modular in the sense that programs are inherently stateful and
your unsafe operations may depend on arbitrary other state.

This non-locality gets much worse when we incorporate actual persistent state.
Consider a simple implementation of `Vec`:

```rust
use std::ptr;

// Note: This definition is naive. See the chapter on implementing Vec.
pub struct Vec<T> {
    ptr: *mut T,
    len: usize,
    cap: usize,
}

// Note this implementation does not correctly handle zero-sized types.
// See the chapter on implementing Vec.
impl<T> Vec<T> {
    pub fn push(&mut self, elem: T) {
        if self.len == self.cap {
            // not important for this example
            self.reallocate();
        }
        unsafe {
            ptr::write(self.ptr.add(self.len), elem);
            self.len += 1;
        }
    }
    # fn reallocate(&mut self) { }
}

# fn main() {}
```

This code is simple enough to reasonably audit and informally verify. Now consider
adding the following method:

<!-- ignore: simplified code -->
```rust,ignore
fn make_room(&mut self) {
    // grow the capacity
    self.cap += 1;
}
```

This code is 100% Safe Rust but it is also completely unsound. Changing the
capacity violates the invariants of Vec (that `cap` reflects the allocated space
in the Vec). This is not something the rest of Vec can guard against. It *has*
to trust the capacity field because there's no way to verify it.

Because it relies on invariants of a struct field, this `unsafe` code
does more than pollute a whole function: it pollutes a whole *module*.
Generally, the only bullet-proof way to limit the scope of unsafe code is at the
module boundary with privacy.

However this works *perfectly*. The existence of `make_room` is *not* a
problem for the soundness of Vec because we didn't mark it as public. Only the
module that defines this function can call it. Also, `make_room` directly
accesses the private fields of Vec, so it can only be written in the same module
as Vec.

It is therefore possible for us to write a completely safe abstraction that
relies on complex invariants. This is *critical* to the relationship between
Safe Rust and Unsafe Rust.

We have already seen that Unsafe code must trust *some* Safe code, but shouldn't
trust *generic* Safe code. Privacy is important to unsafe code for similar reasons:
it prevents us from having to trust all the safe code in the universe from messing
with our trusted state.

Safety lives!
