# Example: Implementing Vec

To bring everything together, we're going to write `std::Vec` from scratch.
We will limit ourselves to stable Rust. In particular we won't use any
intrinsics that could make our code a little bit nicer or efficient because
intrinsics are permanently unstable. Although many intrinsics *do* become
stabilized elsewhere (`std::ptr` and `std::mem` consist of many intrinsics).

Ultimately this means our implementation may not take advantage of all
possible optimizations, though it will be by no means *naive*. We will
definitely get into the weeds over nitty-gritty details, even
when the problem doesn't *really* merit it.

You wanted advanced. We're gonna go advanced.


---

# Layout

First off, we need to come up with the struct layout. A Vec has three parts:
a pointer to the allocation, the size of the allocation, and the number of
elements that have been initialized.

Naively, this means we just want this design:

<!-- ignore: simplified code -->
```rust,ignore
pub struct Vec<T> {
    ptr: *mut T,
    cap: usize,
    len: usize,
}
```

And indeed this would compile. Unfortunately, it would be too strict. The
compiler will give us too strict variance. So a `&Vec<&'static str>`
couldn't be used where a `&Vec<&'a str>` was expected. See [the chapter
on ownership and lifetimes][ownership] for all the details on variance.

As we saw in the ownership chapter, the standard library uses `Unique<T>` in place of
`*mut T` when it has a raw pointer to an allocation that it owns. Unique is unstable,
so we'd like to not use it if possible, though.

As a recap, Unique is a wrapper around a raw pointer that declares that:

* We are covariant over `T`
* We may own a value of type `T` (this is not relevant for our example here, but see 
  [the chapter on PhantomData][phantom-data] on why the real `std::vec::Vec<T>` needs this)
* We are Send/Sync if `T` is Send/Sync
* Our pointer is never null (so `Option<Vec<T>>` is null-pointer-optimized)

We can implement all of the above requirements in stable Rust. To do this, instead
of using `Unique<T>` we will use [`NonNull<T>`][NonNull], another wrapper around a
raw pointer, which gives us two of the above properties, namely it is covariant
over `T` and is declared to never be null. By implementing Send/Sync if `T` is,
we get the same results as using `Unique<T>`:

```rust
use std::ptr::NonNull;

pub struct Vec<T> {
    ptr: NonNull<T>,
    cap: usize,
    len: usize,
}

unsafe impl<T: Send> Send for Vec<T> {}
unsafe impl<T: Sync> Sync for Vec<T> {}
# fn main() {}
```

[ownership]: ../ownership.html
[phantom-data]: ../phantom-data.md
[NonNull]: ../../std/ptr/struct.NonNull.html


---

# Allocating Memory

Using `NonNull` throws a wrench in an important feature of Vec (and indeed all of
the std collections): creating an empty Vec doesn't actually allocate at all. This
is not the same as allocating a zero-sized memory block, which is not allowed by
the global allocator (it results in undefined behavior!). So if we can't allocate,
but also can't put a null pointer in `ptr`, what do we do in `Vec::new`? Well, we
just put some other garbage in there!

This is perfectly fine because we already have `cap == 0` as our sentinel for no
allocation. We don't even need to handle it specially in almost any code because
we usually need to check if `cap > len` or `len > 0` anyway. The recommended
Rust value to put here is `mem::align_of::<T>()`. `NonNull` provides a convenience
for this: `NonNull::dangling()`. There are quite a few places where we'll
want to use `dangling` because there's no real allocation to talk about but
`null` would make the compiler do bad things.

So:

<!-- ignore: explanation code -->
```rust,ignore
use std::mem;

impl<T> Vec<T> {
    pub fn new() -> Self {
        assert!(mem::size_of::<T>() != 0, "We're not ready to handle ZSTs");
        Vec {
            ptr: NonNull::dangling(),
            len: 0,
            cap: 0,
        }
    }
}
# fn main() {}
```

I slipped in that assert there because zero-sized types will require some
special handling throughout our code, and I want to defer the issue for now.
Without this assert, some of our early drafts will do some Very Bad Things.

Next we need to figure out what to actually do when we *do* want space. For that,
we use the global allocation functions [`alloc`][alloc], [`realloc`][realloc],
and [`dealloc`][dealloc] which are available in stable Rust in
[`std::alloc`][std_alloc]. These functions are expected to become deprecated in
favor of the methods of [`std::alloc::Global`][Global] after this type is stabilized.

We'll also need a way to handle out-of-memory (OOM) conditions. The standard
library provides a function [`alloc::handle_alloc_error`][handle_alloc_error],
which will abort the program in a platform-specific manner.
The reason we abort and don't panic is because unwinding can cause allocations
to happen, and that seems like a bad thing to do when your allocator just came
back with "hey I don't have any more memory".

Of course, this is a bit silly since most platforms don't actually run out of
memory in a conventional way. Your operating system will probably kill the
application by another means if you legitimately start using up all the memory.
The most likely way we'll trigger OOM is by just asking for ludicrous quantities
of memory at once (e.g. half the theoretical address space). As such it's
*probably* fine to panic and nothing bad will happen. Still, we're trying to be
like the standard library as much as possible, so we'll just kill the whole
program.

Okay, now we can write growing. Roughly, we want to have this logic:

```text
if cap == 0:
    allocate()
    cap = 1
else:
    reallocate()
    cap *= 2
```

But Rust's only supported allocator API is so low level that we'll need to do a
fair bit of extra work. We also need to guard against some special
conditions that can occur with really large allocations or empty allocations.

In particular, `ptr::offset` will cause us a lot of trouble, because it has
the semantics of LLVM's GEP inbounds instruction. If you're fortunate enough to
not have dealt with this instruction, here's the basic story with GEP: alias
analysis, alias analysis, alias analysis. It's super important to an optimizing
compiler to be able to reason about data dependencies and aliasing.

As a simple example, consider the following fragment of code:

<!-- ignore: simplified code -->
```rust,ignore
*x *= 7;
*y *= 3;
```

If the compiler can prove that `x` and `y` point to different locations in
memory, the two operations can in theory be executed in parallel (by e.g.
loading them into different registers and working on them independently).
However the compiler can't do this in general because if x and y point to
the same location in memory, the operations need to be done to the same value,
and they can't just be merged afterwards.

When you use GEP inbounds, you are specifically telling LLVM that the offsets
you're about to do are within the bounds of a single "allocated" entity. The
ultimate payoff being that LLVM can assume that if two pointers are known to
point to two disjoint objects, all the offsets of those pointers are *also*
known to not alias (because you won't just end up in some random place in
memory). LLVM is heavily optimized to work with GEP offsets, and inbounds
offsets are the best of all, so it's important that we use them as much as
possible.

So that's what GEP's about, how can it cause us trouble?

The first problem is that we index into arrays with unsigned integers, but
GEP (and as a consequence `ptr::offset`) takes a signed integer. This means
that half of the seemingly valid indices into an array will overflow GEP and
actually go in the wrong direction! As such we must limit all allocations to
`isize::MAX` elements. This actually means we only need to worry about
byte-sized objects, because e.g. `> isize::MAX` `u16`s will truly exhaust all of
the system's memory. However in order to avoid subtle corner cases where someone
reinterprets some array of `< isize::MAX` objects as bytes, std limits all
allocations to `isize::MAX` bytes.

On all 64-bit targets that Rust currently supports we're artificially limited
to significantly less than all 64 bits of the address space (modern x64
platforms only expose 48-bit addressing), so we can rely on just running out of
memory first. However on 32-bit targets, particularly those with extensions to
use more of the address space (PAE x86 or x32), it's theoretically possible to
successfully allocate more than `isize::MAX` bytes of memory.

However since this is a tutorial, we're not going to be particularly optimal
here, and just unconditionally check, rather than use clever platform-specific
`cfg`s.

The other corner-case we need to worry about is empty allocations. There will
be two kinds of empty allocations we need to worry about: `cap = 0` for all T,
and `cap > 0` for zero-sized types.

These cases are tricky because they come
down to what LLVM means by "allocated". LLVM's notion of an
allocation is significantly more abstract than how we usually use it. Because
LLVM needs to work with different languages' semantics and custom allocators,
it can't really intimately understand allocation. Instead, the main idea behind
allocation is "doesn't overlap with other stuff". That is, heap allocations,
stack allocations, and globals don't randomly overlap. Yep, it's about alias
analysis. As such, Rust can technically play a bit fast and loose with the notion of
an allocation as long as it's *consistent*.

Getting back to the empty allocation case, there are a couple of places where
we want to offset by 0 as a consequence of generic code. The question is then:
is it consistent to do so? For zero-sized types, we have concluded that it is
indeed consistent to do a GEP inbounds offset by an arbitrary number of
elements. This is a runtime no-op because every element takes up no space,
and it's fine to pretend that there's infinite zero-sized types allocated
at `0x01`. No allocator will ever allocate that address, because they won't
allocate `0x00` and they generally allocate to some minimal alignment higher
than a byte. Also generally the whole first page of memory is
protected from being allocated anyway (a whole 4k, on many platforms).

However what about for positive-sized types? That one's a bit trickier. In
principle, you can argue that offsetting by 0 gives LLVM no information: either
there's an element before the address or after it, but it can't know which.
However we've chosen to conservatively assume that it may do bad things. As
such we will guard against this case explicitly.

*Phew*

Ok with all the nonsense out of the way, let's actually allocate some memory:

<!-- ignore: simplified code -->
```rust,ignore
use std::alloc::{self, Layout};

impl<T> Vec<T> {
    fn grow(&mut self) {
        let (new_cap, new_layout) = if self.cap == 0 {
            (1, Layout::array::<T>(1))
        } else {
            // This can't overflow since self.cap <= isize::MAX.
            let new_cap = 2 * self.cap;
            (new_cap, Layout::array::<T>(new_cap))
        };

        // `Layout::array` checks that the number of bytes allocated is
        // in 1..=isize::MAX and will error otherwise.  An allocation of
        // 0 bytes isn't possible thanks to the above condition.
        let new_layout = new_layout.expect("Allocation too large");

        let new_ptr = if self.cap == 0 {
            unsafe { alloc::alloc(new_layout) }
        } else {
            let old_layout = Layout::array::<T>(self.cap).unwrap();
            let old_ptr = self.ptr.as_ptr() as *mut u8;
            unsafe { alloc::realloc(old_ptr, old_layout, new_layout.size()) }
        };

        // If allocation fails, `new_ptr` will be null, in which case we abort.
        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };
        self.cap = new_cap;
    }
}
# fn main() {}
```

[Global]: ../../std/alloc/struct.Global.html
[handle_alloc_error]: ../../alloc/alloc/fn.handle_alloc_error.html
[alloc]: ../../alloc/alloc/fn.alloc.html
[realloc]: ../../alloc/alloc/fn.realloc.html
[dealloc]: ../../alloc/alloc/fn.dealloc.html
[std_alloc]: ../../alloc/alloc/index.html


---

# Push and Pop

Alright. We can initialize. We can allocate. Let's actually implement some
functionality! Let's start with `push`. All it needs to do is check if we're
full to grow, unconditionally write to the next index, and then increment our
length.

To do the write we have to be careful not to evaluate the memory we want to write
to. At worst, it's truly uninitialized memory from the allocator. At best it's the
bits of some old value we popped off. Either way, we can't just index to the memory
and dereference it, because that will evaluate the memory as a valid instance of
T. Worse, `foo[idx] = x` will try to call `drop` on the old value of `foo[idx]`!

The correct way to do this is with `ptr::write`, which just blindly overwrites the
target address with the bits of the value we provide. No evaluation involved.

For `push`, if the old len (before push was called) is 0, then we want to write
to the 0th index. So we should offset by the old len.

<!-- ignore: simplified code -->
```rust,ignore
pub fn push(&mut self, elem: T) {
    if self.len == self.cap { self.grow(); }

    unsafe {
        ptr::write(self.ptr.as_ptr().add(self.len), elem);
    }

    // Can't fail, we'll OOM first.
    self.len += 1;
}
```

Easy! How about `pop`? Although this time the index we want to access is
initialized, Rust won't just let us dereference the location of memory to move
the value out, because that would leave the memory uninitialized! For this we
need `ptr::read`, which just copies out the bits from the target address and
interprets it as a value of type T. This will leave the memory at this address
logically uninitialized, even though there is in fact a perfectly good instance
of T there.

For `pop`, if the old len is 1, for example, we want to read out of the 0th
index. So we should offset by the new len.

<!-- ignore: simplified code -->
```rust,ignore
pub fn pop(&mut self) -> Option<T> {
    if self.len == 0 {
        None
    } else {
        self.len -= 1;
        unsafe {
            Some(ptr::read(self.ptr.as_ptr().add(self.len)))
        }
    }
}
```


---

# Deallocating

Next we should implement Drop so that we don't massively leak tons of resources.
The easiest way is to just call `pop` until it yields None, and then deallocate
our buffer. Note that calling `pop` is unneeded if `T: !Drop`. In theory we can
ask Rust if `T` `needs_drop` and omit the calls to `pop`. However in practice
LLVM is *really* good at removing simple side-effect free code like this, so I
wouldn't bother unless you notice it's not being stripped (in this case it is).

We must not call `alloc::dealloc` when `self.cap == 0`, as in this case we
haven't actually allocated any memory.

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Drop for Vec<T> {
    fn drop(&mut self) {
        if self.cap != 0 {
            while let Some(_) = self.pop() { }
            let layout = Layout::array::<T>(self.cap).unwrap();
            unsafe {
                alloc::dealloc(self.ptr.as_ptr() as *mut u8, layout);
            }
        }
    }
}
```


---

# Deref

Alright! We've got a decent minimal stack implemented. We can push, we can
pop, and we can clean up after ourselves. However there's a whole mess of
functionality we'd reasonably want. In particular, we have a proper array, but
none of the slice functionality. That's actually pretty easy to solve: we can
implement `Deref<Target=[T]>`. This will magically make our Vec coerce to, and
behave like, a slice in all sorts of conditions.

All we need is `slice::from_raw_parts`. It will correctly handle empty slices
for us. Later once we set up zero-sized type support it will also Just Work
for those too.

<!-- ignore: simplified code -->
```rust,ignore
use std::ops::Deref;

impl<T> Deref for Vec<T> {
    type Target = [T];
    fn deref(&self) -> &[T] {
        unsafe {
            std::slice::from_raw_parts(self.ptr.as_ptr(), self.len)
        }
    }
}
```

And let's do DerefMut too:

<!-- ignore: simplified code -->
```rust,ignore
use std::ops::DerefMut;

impl<T> DerefMut for Vec<T> {
    fn deref_mut(&mut self) -> &mut [T] {
        unsafe {
            std::slice::from_raw_parts_mut(self.ptr.as_ptr(), self.len)
        }
    }
}
```

Now we have `len`, `first`, `last`, indexing, slicing, sorting, `iter`,
`iter_mut`, and all other sorts of bells and whistles provided by slice. Sweet!


---

# Insert and Remove

Something *not* provided by slice is `insert` and `remove`, so let's do those
next.

Insert needs to shift all the elements at the target index to the right by one.
To do this we need to use `ptr::copy`, which is our version of C's `memmove`.
This copies some chunk of memory from one location to another, correctly
handling the case where the source and destination overlap (which will
definitely happen here).

If we insert at index `i`, we want to shift the `[i .. len]` to `[i+1 .. len+1]`
using the old len.

<!-- ignore: simplified code -->
```rust,ignore
pub fn insert(&mut self, index: usize, elem: T) {
    // Note: `<=` because it's valid to insert after everything
    // which would be equivalent to push.
    assert!(index <= self.len, "index out of bounds");
    if self.len == self.cap { self.grow(); }

    unsafe {
        // ptr::copy(src, dest, len): "copy from src to dest len elems"
        ptr::copy(
            self.ptr.as_ptr().add(index),
            self.ptr.as_ptr().add(index + 1),
            self.len - index,
        );
        ptr::write(self.ptr.as_ptr().add(index), elem);
    }

    self.len += 1;
}
```

Remove behaves in the opposite manner. We need to shift all the elements from
`[i+1 .. len + 1]` to `[i .. len]` using the *new* len.

<!-- ignore: simplified code -->
```rust,ignore
pub fn remove(&mut self, index: usize) -> T {
    // Note: `<` because it's *not* valid to remove after everything
    assert!(index < self.len, "index out of bounds");
    unsafe {
        self.len -= 1;
        let result = ptr::read(self.ptr.as_ptr().add(index));
        ptr::copy(
            self.ptr.as_ptr().add(index + 1),
            self.ptr.as_ptr().add(index),
            self.len - index,
        );
        result
    }
}
```


---

# IntoIter

Let's move on to writing iterators. `iter` and `iter_mut` have already been
written for us thanks to The Magic of Deref. However there's two interesting
iterators that Vec provides that slices can't: `into_iter` and `drain`.

IntoIter consumes the Vec by-value, and can consequently yield its elements
by-value. In order to enable this, IntoIter needs to take control of Vec's
allocation.

IntoIter needs to be DoubleEnded as well, to enable reading from both ends.
Reading from the back could just be implemented as calling `pop`, but reading
from the front is harder. We could call `remove(0)` but that would be insanely
expensive. Instead we're going to just use ptr::read to copy values out of
either end of the Vec without mutating the buffer at all.

To do this we're going to use a very common C idiom for array iteration. We'll
make two pointers; one that points to the start of the array, and one that
points to one-element past the end. When we want an element from one end, we'll
read out the value pointed to at that end and move the pointer over by one. When
the two pointers are equal, we know we're done.

Note that the order of read and offset are reversed for `next` and `next_back`
For `next_back` the pointer is always after the element it wants to read next,
while for `next` the pointer is always at the element it wants to read next.
To see why this is, consider the case where every element but one has been
yielded.

The array looks like this:

```text
          S  E
[X, X, X, O, X, X, X]
```

If E pointed directly at the element it wanted to yield next, it would be
indistinguishable from the case where there are no more elements to yield.

Although we don't actually care about it during iteration, we also need to hold
onto the Vec's allocation information in order to free it once IntoIter is
dropped.

So we're going to use the following struct:

<!-- ignore: simplified code -->
```rust,ignore
pub struct IntoIter<T> {
    buf: NonNull<T>,
    cap: usize,
    start: *const T,
    end: *const T,
}
```

And this is what we end up with for initialization:

<!-- ignore: simplified code -->
```rust,ignore
impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>;
    fn into_iter(self) -> IntoIter<T> {
        // Make sure not to drop Vec since that would free the buffer
        let vec = ManuallyDrop::new(self);

        // Can't destructure Vec since it's Drop
        let ptr = vec.ptr;
        let cap = vec.cap;
        let len = vec.len;

        IntoIter {
            buf: ptr,
            cap,
            start: ptr.as_ptr(),
            end: if cap == 0 {
                // can't offset off this pointer, it's not allocated!
                ptr.as_ptr()
            } else {
                unsafe { ptr.as_ptr().add(len) }
            },
        }
    }
}
```

Here's iterating forward:

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Iterator for IntoIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                let result = ptr::read(self.start);
                self.start = self.start.offset(1);
                Some(result)
            }
        }
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        let len = (self.end as usize - self.start as usize)
                  / mem::size_of::<T>();
        (len, Some(len))
    }
}
```

And here's iterating backwards.

<!-- ignore: simplified code -->
```rust,ignore
impl<T> DoubleEndedIterator for IntoIter<T> {
    fn next_back(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                self.end = self.end.offset(-1);
                Some(ptr::read(self.end))
            }
        }
    }
}
```

Because IntoIter takes ownership of its allocation, it needs to implement Drop
to free it. However it also wants to implement Drop to drop any elements it
contains that weren't yielded.

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Drop for IntoIter<T> {
    fn drop(&mut self) {
        if self.cap != 0 {
            // drop any remaining elements
            for _ in &mut *self {}
            let layout = Layout::array::<T>(self.cap).unwrap();
            unsafe {
                alloc::dealloc(self.buf.as_ptr() as *mut u8, layout);
            }
        }
    }
}
```


---

# RawVec

We've actually reached an interesting situation here: we've duplicated the logic
for specifying a buffer and freeing its memory in Vec and IntoIter. Now that
we've implemented it and identified *actual* logic duplication, this is a good
time to perform some logic compression.

We're going to abstract out the `(ptr, cap)` pair and give them the logic for
allocating, growing, and freeing:

<!-- ignore: simplified code -->
```rust,ignore
struct RawVec<T> {
    ptr: NonNull<T>,
    cap: usize,
}

unsafe impl<T: Send> Send for RawVec<T> {}
unsafe impl<T: Sync> Sync for RawVec<T> {}

impl<T> RawVec<T> {
    fn new() -> Self {
        assert!(mem::size_of::<T>() != 0, "TODO: implement ZST support");
        RawVec {
            ptr: NonNull::dangling(),
            cap: 0,
        }
    }

    fn grow(&mut self) {
        // This can't overflow because we ensure self.cap <= isize::MAX.
        let new_cap = if self.cap == 0 { 1 } else { 2 * self.cap };

        // Layout::array checks that the number of bytes is <= usize::MAX,
        // but this is redundant since old_layout.size() <= isize::MAX,
        // so the `unwrap` should never fail.
        let new_layout = Layout::array::<T>(new_cap).unwrap();

        // Ensure that the new allocation doesn't exceed `isize::MAX` bytes.
        assert!(new_layout.size() <= isize::MAX as usize, "Allocation too large");

        let new_ptr = if self.cap == 0 {
            unsafe { alloc::alloc(new_layout) }
        } else {
            let old_layout = Layout::array::<T>(self.cap).unwrap();
            let old_ptr = self.ptr.as_ptr() as *mut u8;
            unsafe { alloc::realloc(old_ptr, old_layout, new_layout.size()) }
        };

        // If allocation fails, `new_ptr` will be null, in which case we abort.
        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };
        self.cap = new_cap;
    }
}

impl<T> Drop for RawVec<T> {
    fn drop(&mut self) {
        if self.cap != 0 {
            let layout = Layout::array::<T>(self.cap).unwrap();
            unsafe {
                alloc::dealloc(self.ptr.as_ptr() as *mut u8, layout);
            }
        }
    }
}
```

And change Vec as follows:

<!-- ignore: simplified code -->
```rust,ignore
pub struct Vec<T> {
    buf: RawVec<T>,
    len: usize,
}

impl<T> Vec<T> {
    fn ptr(&self) -> *mut T {
        self.buf.ptr.as_ptr()
    }

    fn cap(&self) -> usize {
        self.buf.cap
    }

    pub fn new() -> Self {
        Vec {
            buf: RawVec::new(),
            len: 0,
        }
    }

    // push/pop/insert/remove largely unchanged:
    // * `self.ptr.as_ptr() -> self.ptr()`
    // * `self.cap -> self.cap()`
    // * `self.grow() -> self.buf.grow()`
}

impl<T> Drop for Vec<T> {
    fn drop(&mut self) {
        while let Some(_) = self.pop() {}
        // deallocation is handled by RawVec
    }
}
```

And finally we can really simplify IntoIter:

<!-- ignore: simplified code -->
```rust,ignore
pub struct IntoIter<T> {
    _buf: RawVec<T>, // we don't actually care about this. Just need it to live.
    start: *const T,
    end: *const T,
}

// next and next_back literally unchanged since they never referred to the buf

impl<T> Drop for IntoIter<T> {
    fn drop(&mut self) {
        // only need to ensure all our elements are read;
        // buffer will clean itself up afterwards.
        for _ in &mut *self {}
    }
}

impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>;
    fn into_iter(self) -> IntoIter<T> {
        // need to use ptr::read to unsafely move the buf out since it's
        // not Copy, and Vec implements Drop (so we can't destructure it).
        let buf = unsafe { ptr::read(&self.buf) };
        let len = self.len;
        mem::forget(self);

        IntoIter {
            start: buf.ptr.as_ptr(),
            end: if buf.cap == 0 {
                // can't offset off of a pointer unless it's part of an allocation
                buf.ptr.as_ptr()
            } else {
                unsafe { buf.ptr.as_ptr().add(len) }
            },
            _buf: buf,
        }
    }
}
```

Much better.


---

# Drain

Let's move on to Drain. Drain is largely the same as IntoIter, except that
instead of consuming the Vec, it borrows the Vec and leaves its allocation
untouched. For now we'll only implement the "basic" full-range version.

<!-- ignore: simplified code -->
```rust,ignore
use std::marker::PhantomData;

struct Drain<'a, T: 'a> {
    // Need to bound the lifetime here, so we do it with `&'a mut Vec<T>`
    // because that's semantically what we contain. We're "just" calling
    // `pop()` and `remove(0)`.
    vec: PhantomData<&'a mut Vec<T>>,
    start: *const T,
    end: *const T,
}

impl<'a, T> Iterator for Drain<'a, T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end {
            None
```

-- wait, this is seeming familiar. Let's do some more compression. Both
IntoIter and Drain have the exact same structure, let's just factor it out.

<!-- ignore: simplified code -->
```rust,ignore
struct RawValIter<T> {
    start: *const T,
    end: *const T,
}

impl<T> RawValIter<T> {
    // unsafe to construct because it has no associated lifetimes.
    // This is necessary to store a RawValIter in the same struct as
    // its actual allocation. OK since it's a private implementation
    // detail.
    unsafe fn new(slice: &[T]) -> Self {
        RawValIter {
            start: slice.as_ptr(),
            end: if slice.len() == 0 {
                // if `len = 0`, then this is not actually allocated memory.
                // Need to avoid offsetting because that will give wrong
                // information to LLVM via GEP.
                slice.as_ptr()
            } else {
                slice.as_ptr().add(slice.len())
            }
        }
    }
}

// Iterator and DoubleEndedIterator impls identical to IntoIter.
```

And IntoIter becomes the following:

<!-- ignore: simplified code -->
```rust,ignore
pub struct IntoIter<T> {
    _buf: RawVec<T>, // we don't actually care about this. Just need it to live.
    iter: RawValIter<T>,
}

impl<T> Iterator for IntoIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> { self.iter.next() }
    fn size_hint(&self) -> (usize, Option<usize>) { self.iter.size_hint() }
}

impl<T> DoubleEndedIterator for IntoIter<T> {
    fn next_back(&mut self) -> Option<T> { self.iter.next_back() }
}

impl<T> Drop for IntoIter<T> {
    fn drop(&mut self) {
        for _ in &mut *self {}
    }
}

impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>;
    fn into_iter(self) -> IntoIter<T> {
        unsafe {
            let iter = RawValIter::new(&self);

            let buf = ptr::read(&self.buf);
            mem::forget(self);

            IntoIter {
                iter,
                _buf: buf,
            }
        }
    }
}
```

Note that I've left a few quirks in this design to make upgrading Drain to work
with arbitrary subranges a bit easier. In particular we *could* have RawValIter
drain itself on drop, but that won't work right for a more complex Drain.
We also take a slice to simplify Drain initialization.

Alright, now Drain is really easy:

<!-- ignore: simplified code -->
```rust,ignore
use std::marker::PhantomData;

pub struct Drain<'a, T: 'a> {
    vec: PhantomData<&'a mut Vec<T>>,
    iter: RawValIter<T>,
}

impl<'a, T> Iterator for Drain<'a, T> {
    type Item = T;
    fn next(&mut self) -> Option<T> { self.iter.next() }
    fn size_hint(&self) -> (usize, Option<usize>) { self.iter.size_hint() }
}

impl<'a, T> DoubleEndedIterator for Drain<'a, T> {
    fn next_back(&mut self) -> Option<T> { self.iter.next_back() }
}

impl<'a, T> Drop for Drain<'a, T> {
    fn drop(&mut self) {
        for _ in &mut *self {}
    }
}

impl<T> Vec<T> {
    pub fn drain(&mut self) -> Drain<T> {
        let iter = unsafe { RawValIter::new(&self) };

        // this is a mem::forget safety thing. If Drain is forgotten, we just
        // leak the whole Vec's contents. Also we need to do this *eventually*
        // anyway, so why not do it now?
        self.len = 0;

        Drain {
            iter,
            vec: PhantomData,
        }
    }
}
```

For more details on the `mem::forget` problem, see the
[section on leaks][leaks].

[leaks]: ../leaking.html


---

# Handling Zero-Sized Types

It's time. We're going to fight the specter that is zero-sized types. Safe Rust
*never* needs to care about this, but Vec is very intensive on raw pointers and
raw allocations, which are exactly the two things that care about
zero-sized types. We need to be careful of two things:

* The raw allocator API has undefined behavior if you pass in 0 for an
  allocation size.
* raw pointer offsets are no-ops for zero-sized types, which will break our
  C-style pointer iterator.

Thankfully we abstracted out pointer-iterators and allocating handling into
`RawValIter` and `RawVec` respectively. How mysteriously convenient.

## Allocating Zero-Sized Types

So if the allocator API doesn't support zero-sized allocations, what on earth
do we store as our allocation? `NonNull::dangling()` of course! Almost every operation
with a ZST is a no-op since ZSTs have exactly one value, and therefore no state needs
to be considered to store or load them. This actually extends to `ptr::read` and
`ptr::write`: they won't actually look at the pointer at all. As such we never need
to change the pointer.

Note however that our previous reliance on running out of memory before overflow is
no longer valid with zero-sized types. We must explicitly guard against capacity
overflow for zero-sized types.

Due to our current architecture, all this means is writing 3 guards, one in each
method of `RawVec`.

<!-- ignore: simplified code -->
```rust,ignore
impl<T> RawVec<T> {
    fn new() -> Self {
        // This branch should be stripped at compile time.
        let cap = if mem::size_of::<T>() == 0 { usize::MAX } else { 0 };

        // `NonNull::dangling()` doubles as "unallocated" and "zero-sized allocation"
        RawVec {
            ptr: NonNull::dangling(),
            cap,
        }
    }

    fn grow(&mut self) {
        // since we set the capacity to usize::MAX when T has size 0,
        // getting to here necessarily means the Vec is overfull.
        assert!(mem::size_of::<T>() != 0, "capacity overflow");

        let (new_cap, new_layout) = if self.cap == 0 {
            (1, Layout::array::<T>(1).unwrap())
        } else {
            // This can't overflow because we ensure self.cap <= isize::MAX.
            let new_cap = 2 * self.cap;

            // `Layout::array` checks that the number of bytes is <= usize::MAX,
            // but this is redundant since old_layout.size() <= isize::MAX,
            // so the `unwrap` should never fail.
            let new_layout = Layout::array::<T>(new_cap).unwrap();
            (new_cap, new_layout)
        };

        // Ensure that the new allocation doesn't exceed `isize::MAX` bytes.
        assert!(new_layout.size() <= isize::MAX as usize, "Allocation too large");

        let new_ptr = if self.cap == 0 {
            unsafe { alloc::alloc(new_layout) }
        } else {
            let old_layout = Layout::array::<T>(self.cap).unwrap();
            let old_ptr = self.ptr.as_ptr() as *mut u8;
            unsafe { alloc::realloc(old_ptr, old_layout, new_layout.size()) }
        };

        // If allocation fails, `new_ptr` will be null, in which case we abort.
        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };
        self.cap = new_cap;
    }
}

impl<T> Drop for RawVec<T> {
    fn drop(&mut self) {
        let elem_size = mem::size_of::<T>();

        if self.cap != 0 && elem_size != 0 {
            unsafe {
                alloc::dealloc(
                    self.ptr.as_ptr() as *mut u8,
                    Layout::array::<T>(self.cap).unwrap(),
                );
            }
        }
    }
}
```

That's it. We support pushing and popping zero-sized types now. Our iterators
(that aren't provided by slice Deref) are still busted, though.

## Iterating Zero-Sized Types

Zero-sized offsets are no-ops. This means that our current design will always
initialize `start` and `end` as the same value, and our iterators will yield
nothing. The current solution to this is to cast the pointers to integers,
increment, and then cast them back:

<!-- ignore: simplified code -->
```rust,ignore
impl<T> RawValIter<T> {
    unsafe fn new(slice: &[T]) -> Self {
        RawValIter {
            start: slice.as_ptr(),
            end: if mem::size_of::<T>() == 0 {
                ((slice.as_ptr() as usize) + slice.len()) as *const _
            } else if slice.len() == 0 {
                slice.as_ptr()
            } else {
                slice.as_ptr().add(slice.len())
            },
        }
    }
}
```

Now we have a different bug. Instead of our iterators not running at all, our
iterators now run *forever*. We need to do the same trick in our iterator impls.
Also, our size_hint computation code will divide by 0 for ZSTs. Since we'll
basically be treating the two pointers as if they point to bytes, we'll just
map size 0 to divide by 1. Here's what `next` will be:

<!-- ignore: simplified code -->
```rust,ignore
fn next(&mut self) -> Option<T> {
    if self.start == self.end {
        None
    } else {
        unsafe {
            let result = ptr::read(self.start);
            self.start = if mem::size_of::<T>() == 0 {
                (self.start as usize + 1) as *const _
            } else {
                self.start.offset(1)
            };
            Some(result)
        }
    }
}
```

Do you see the "bug"? No one else did! The original author only noticed the
problem when linking to this page years later. This code is kind of dubious
because abusing the iterator pointers to be *counters* makes them unaligned!
Our *one job* when using ZSTs is to keep pointers aligned! *forehead slap*

Raw pointers don't need to be aligned at all times, so the basic trick of
using pointers as counters is *fine*, but they *should* definitely be aligned
when passed to `ptr::read`! This is *possibly* needless pedantry
because `ptr::read` is a noop for a ZST, but let's be a *little* more
responsible and read from `NonNull::dangling` on the ZST path.

(Alternatively you could call `read_unaligned` on the ZST path. Either is fine,
because either way we're making up a value from nothing and it all compiles
to doing nothing.)

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Iterator for RawValIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                if mem::size_of::<T>() == 0 {
                    self.start = (self.start as usize + 1) as *const _;
                    Some(ptr::read(NonNull::<T>::dangling().as_ptr()))
                } else {
                    let old_ptr = self.start;
                    self.start = self.start.offset(1);
                    Some(ptr::read(old_ptr))
                }
            }
        }
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        let elem_size = mem::size_of::<T>();
        let len = (self.end as usize - self.start as usize)
                  / if elem_size == 0 { 1 } else { elem_size };
        (len, Some(len))
    }
}

impl<T> DoubleEndedIterator for RawValIter<T> {
    fn next_back(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                if mem::size_of::<T>() == 0 {
                    self.end = (self.end as usize - 1) as *const _;
                    Some(ptr::read(NonNull::<T>::dangling().as_ptr()))
                } else {
                    self.end = self.end.offset(-1);
                    Some(ptr::read(self.end))
                }
            }
        }
    }
}
```

And that's it. Iteration works!

One last thing we need to consider is that when our vector is dropped, it deallocates the memory that was allocated while it was alive. With ZSTs, we didn't allocate any memory; in fact, we never do. So, right now, our code has unsoundness: we're still trying to deallocate a `NonNull::dangling()` pointer that we use to simulate the ZST in our vector. This means we'd cause undefined behavior if we tried to deallocate something we never allocated (obviously, and for good reasons). To fix this, in our `RawVec`'s `Drop` trait, we're going to tweak it to ensure we only deallocate types that are sized.

```rust,ignore
impl<T> Drop for RawVec<T> {
    fn drop(&mut self) {
        println!("RawVec<T> Drop called, deallocating memory");
        if self.cap != 0 && std::mem::size_of::<T>() > 0 {
            let layout = std::alloc::Layout::array::<T>(self.cap).unwrap();
            unsafe {
                std::alloc::dealloc(self.ptr.as_ptr() as *mut _, layout);
            }
        }
    }
}
```



---

# The Final Code

```rust
use std::alloc::{self, Layout};
use std::marker::PhantomData;
use std::mem;
use std::ops::{Deref, DerefMut};
use std::ptr::{self, NonNull};

struct RawVec<T> {
    ptr: NonNull<T>,
    cap: usize,
}

unsafe impl<T: Send> Send for RawVec<T> {}
unsafe impl<T: Sync> Sync for RawVec<T> {}

impl<T> RawVec<T> {
    fn new() -> Self {
        // !0 is usize::MAX. This branch should be stripped at compile time.
        let cap = if mem::size_of::<T>() == 0 { !0 } else { 0 };

        // `NonNull::dangling()` doubles as "unallocated" and "zero-sized allocation"
        RawVec {
            ptr: NonNull::dangling(),
            cap,
        }
    }

    fn grow(&mut self) {
        // since we set the capacity to usize::MAX when T has size 0,
        // getting to here necessarily means the Vec is overfull.
        assert!(mem::size_of::<T>() != 0, "capacity overflow");

        let (new_cap, new_layout) = if self.cap == 0 {
            (1, Layout::array::<T>(1))
        } else {
            // This can't overflow since self.cap <= isize::MAX.
            let new_cap = 2 * self.cap;
            (new_cap, Layout::array::<T>(new_cap))
        };

        // `Layout::array` checks that the number of bytes allocated is
        // in 1..=isize::MAX and will error otherwise.  An allocation of
        // 0 bytes isn't possible thanks to the above condition.
        let new_layout = new_layout.expect("Allocation too large");

        let new_ptr = if self.cap == 0 {
            unsafe { alloc::alloc(new_layout) }
        } else {
            let old_layout = Layout::array::<T>(self.cap).unwrap();
            let old_ptr = self.ptr.as_ptr() as *mut u8;
            unsafe { alloc::realloc(old_ptr, old_layout, new_layout.size()) }
        };

        // If allocation fails, `new_ptr` will be null, in which case we abort.
        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };
        self.cap = new_cap;
    }
}

impl<T> Drop for RawVec<T> {
    fn drop(&mut self) {
        let elem_size = mem::size_of::<T>();

        if self.cap != 0 && elem_size != 0 {
            unsafe {
                alloc::dealloc(
                    self.ptr.as_ptr() as *mut u8,
                    Layout::array::<T>(self.cap).unwrap(),
                );
            }
        }
    }
}

pub struct Vec<T> {
    buf: RawVec<T>,
    len: usize,
}

impl<T> Vec<T> {
    fn ptr(&self) -> *mut T {
        self.buf.ptr.as_ptr()
    }

    fn cap(&self) -> usize {
        self.buf.cap
    }

    pub fn new() -> Self {
        Vec {
            buf: RawVec::new(),
            len: 0,
        }
    }
    pub fn push(&mut self, elem: T) {
        if self.len == self.cap() {
            self.buf.grow();
        }

        unsafe {
            ptr::write(self.ptr().add(self.len), elem);
        }

        // Can't overflow, we'll OOM first.
        self.len += 1;
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.len == 0 {
            None
        } else {
            self.len -= 1;
            unsafe { Some(ptr::read(self.ptr().add(self.len))) }
        }
    }

    pub fn insert(&mut self, index: usize, elem: T) {
        assert!(index <= self.len, "index out of bounds");
        if self.len == self.cap() {
            self.buf.grow();
        }

        unsafe {
            ptr::copy(
                self.ptr().add(index),
                self.ptr().add(index + 1),
                self.len - index,
            );
            ptr::write(self.ptr().add(index), elem);
        }

        self.len += 1;
    }

    pub fn remove(&mut self, index: usize) -> T {
        assert!(index < self.len, "index out of bounds");

        self.len -= 1;

        unsafe {
            let result = ptr::read(self.ptr().add(index));
            ptr::copy(
                self.ptr().add(index + 1),
                self.ptr().add(index),
                self.len - index,
            );
            result
        }
    }

    pub fn drain(&mut self) -> Drain<T> {
        let iter = unsafe { RawValIter::new(&self) };

        // this is a mem::forget safety thing. If Drain is forgotten, we just
        // leak the whole Vec's contents. Also we need to do this *eventually*
        // anyway, so why not do it now?
        self.len = 0;

        Drain {
            iter,
            vec: PhantomData,
        }
    }
}

impl<T> Drop for Vec<T> {
    fn drop(&mut self) {
        while let Some(_) = self.pop() {}
        // deallocation is handled by RawVec
    }
}

impl<T> Deref for Vec<T> {
    type Target = [T];
    fn deref(&self) -> &[T] {
        unsafe { std::slice::from_raw_parts(self.ptr(), self.len) }
    }
}

impl<T> DerefMut for Vec<T> {
    fn deref_mut(&mut self) -> &mut [T] {
        unsafe { std::slice::from_raw_parts_mut(self.ptr(), self.len) }
    }
}

impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>;
    fn into_iter(self) -> IntoIter<T> {
        let (iter, buf) = unsafe {
            (RawValIter::new(&self), ptr::read(&self.buf))
        };

        mem::forget(self);

        IntoIter {
            iter,
            _buf: buf,
        }
    }
}

struct RawValIter<T> {
    start: *const T,
    end: *const T,
}

impl<T> RawValIter<T> {
    unsafe fn new(slice: &[T]) -> Self {
        RawValIter {
            start: slice.as_ptr(),
            end: if mem::size_of::<T>() == 0 {
                ((slice.as_ptr() as usize) + slice.len()) as *const _
            } else if slice.len() == 0 {
                slice.as_ptr()
            } else {
                slice.as_ptr().add(slice.len())
            },
        }
    }
}

impl<T> Iterator for RawValIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                if mem::size_of::<T>() == 0 {
                    self.start = (self.start as usize + 1) as *const _;
                    Some(ptr::read(NonNull::<T>::dangling().as_ptr()))
                } else {
                    let old_ptr = self.start;
                    self.start = self.start.offset(1);
                    Some(ptr::read(old_ptr))
                }
            }
        }
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        let elem_size = mem::size_of::<T>();
        let len = (self.end as usize - self.start as usize)
                  / if elem_size == 0 { 1 } else { elem_size };
        (len, Some(len))
    }
}

impl<T> DoubleEndedIterator for RawValIter<T> {
    fn next_back(&mut self) -> Option<T> {
        if self.start == self.end {
            None
        } else {
            unsafe {
                if mem::size_of::<T>() == 0 {
                    self.end = (self.end as usize - 1) as *const _;
                    Some(ptr::read(NonNull::<T>::dangling().as_ptr()))
                } else {
                    self.end = self.end.offset(-1);
                    Some(ptr::read(self.end))
                }
            }
        }
    }
}

pub struct IntoIter<T> {
    _buf: RawVec<T>, // we don't actually care about this. Just need it to live.
    iter: RawValIter<T>,
}

impl<T> Iterator for IntoIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        self.iter.next()
    }
    fn size_hint(&self) -> (usize, Option<usize>) {
        self.iter.size_hint()
    }
}

impl<T> DoubleEndedIterator for IntoIter<T> {
    fn next_back(&mut self) -> Option<T> {
        self.iter.next_back()
    }
}

impl<T> Drop for IntoIter<T> {
    fn drop(&mut self) {
        for _ in &mut *self {}
    }
}

pub struct Drain<'a, T: 'a> {
    vec: PhantomData<&'a mut Vec<T>>,
    iter: RawValIter<T>,
}

impl<'a, T> Iterator for Drain<'a, T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        self.iter.next()
    }
    fn size_hint(&self) -> (usize, Option<usize>) {
        self.iter.size_hint()
    }
}

impl<'a, T> DoubleEndedIterator for Drain<'a, T> {
    fn next_back(&mut self) -> Option<T> {
        self.iter.next_back()
    }
}

impl<'a, T> Drop for Drain<'a, T> {
    fn drop(&mut self) {
        // pre-drain the iter
        for _ in &mut *self {}
    }
}
#
# fn main() {
#     tests::create_push_pop();
#     tests::iter_test();
#     tests::test_drain();
#     tests::test_zst();
#     println!("All tests finished OK");
# }
#
# mod tests {
#     use super::*;
#
#     pub fn create_push_pop() {
#         let mut v = Vec::new();
#         v.push(1);
#         assert_eq!(1, v.len());
#         assert_eq!(1, v[0]);
#         for i in v.iter_mut() {
#             *i += 1;
#         }
#         v.insert(0, 5);
#         let x = v.pop();
#         assert_eq!(Some(2), x);
#         assert_eq!(1, v.len());
#         v.push(10);
#         let x = v.remove(0);
#         assert_eq!(5, x);
#         assert_eq!(1, v.len());
#     }
#
#     pub fn iter_test() {
#         let mut v = Vec::new();
#         for i in 0..10 {
#             v.push(Box::new(i))
#         }
#         let mut iter = v.into_iter();
#         let first = iter.next().unwrap();
#         let last = iter.next_back().unwrap();
#         drop(iter);
#         assert_eq!(0, *first);
#         assert_eq!(9, *last);
#     }
#
#     pub fn test_drain() {
#         let mut v = Vec::new();
#         for i in 0..10 {
#             v.push(Box::new(i))
#         }
#         {
#             let mut drain = v.drain();
#             let first = drain.next().unwrap();
#             let last = drain.next_back().unwrap();
#             assert_eq!(0, *first);
#             assert_eq!(9, *last);
#         }
#         assert_eq!(0, v.len());
#         v.push(Box::new(1));
#         assert_eq!(1, *v.pop().unwrap());
#     }
#
#     pub fn test_zst() {
#         let mut v = Vec::new();
#         for _i in 0..10 {
#             v.push(())
#         }
#
#         let mut count = 0;
#
#         for _ in v.into_iter() {
#             count += 1
#         }
#
#         assert_eq!(10, count);
#     }
# }
```
