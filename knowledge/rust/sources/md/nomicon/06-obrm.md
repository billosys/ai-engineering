# The Perils Of Ownership Based Resource Management (OBRM)

OBRM (AKA RAII: Resource Acquisition Is Initialization) is something you'll
interact with a lot in Rust. Especially if you use the standard library.

Roughly speaking the pattern is as follows: to acquire a resource, you create an
object that manages it. To release the resource, you simply destroy the object,
and it cleans up the resource for you. The most common "resource" this pattern
manages is simply *memory*. `Box`, `Rc`, and basically everything in
`std::collections` is a convenience to enable correctly managing memory. This is
particularly important in Rust because we have no pervasive GC to rely on for
memory management. Which is the point, really: Rust is about control. However we
are not limited to just memory. Pretty much every other system resource like a
thread, file, or socket is exposed through this kind of API.


---

# Constructors

There is exactly one way to create an instance of a user-defined type: name it,
and initialize all its fields at once:

```rust
struct Foo {
    a: u8,
    b: u32,
    c: bool,
}

enum Bar {
    X(u32),
    Y(bool),
}

struct Unit;

let foo = Foo { a: 0, b: 1, c: false };
let bar = Bar::X(0);
let empty = Unit;
```

That's it. Every other way you make an instance of a type is just calling a
totally vanilla function that does some stuff and eventually bottoms out to The
One True Constructor.

Unlike C++, Rust does not come with a slew of built-in kinds of constructor.
There are no Copy, Default, Assignment, Move, or whatever constructors. The
reasons for this are varied, but it largely boils down to Rust's philosophy of
*being explicit*.

Move constructors are meaningless in Rust because we don't enable types to
"care" about their location in memory. Every type must be ready for it to be
blindly memcopied to somewhere else in memory. This means pure on-the-stack-but-
still-movable intrusive linked lists are simply not happening in Rust (safely).

Assignment and copy constructors similarly don't exist because move semantics
are the only semantics in Rust. At most `x = y` just moves the bits of y into
the x variable. Rust does provide two facilities for providing C++'s copy-
oriented semantics: `Copy` and `Clone`. Clone is our moral equivalent of a copy
constructor, but it's never implicitly invoked. You have to explicitly call
`clone` on an element you want to be cloned. Copy is a special case of Clone
where the implementation is just "copy the bits". Copy types *are* implicitly
cloned whenever they're moved, but because of the definition of Copy this just
means not treating the old copy as uninitialized -- a no-op.

While Rust provides a `Default` trait for specifying the moral equivalent of a
default constructor, it's incredibly rare for this trait to be used. This is
because variables [aren't implicitly initialized][uninit]. Default is basically
only useful for generic programming. In concrete contexts, a type will provide a
static `new` method for any kind of "default" constructor. This has no relation
to `new` in other languages and has no special meaning. It's just a naming
convention.

TODO: talk about "placement new"?

[uninit]: uninitialized.html


---

# Destructors

What the language *does* provide is full-blown automatic destructors through the
`Drop` trait, which provides the following method:

<!-- ignore: function header -->
```rust,ignore
fn drop(&mut self);
```

This method gives the type time to somehow finish what it was doing.

**After `drop` is run, Rust will recursively try to drop all of the fields
of `self`.**

This is a convenience feature so that you don't have to write "destructor
boilerplate" to drop children. If a struct has no special logic for being
dropped other than dropping its children, then it means `Drop` doesn't need to
be implemented at all!

**There is no stable way to prevent this behavior in Rust 1.0.**

Note that taking `&mut self` means that even if you could suppress recursive
Drop, Rust will prevent you from e.g. moving fields out of self. For most types,
this is totally fine.

For instance, a custom implementation of `Box` might write `Drop` like this:

```rust
#![feature(ptr_internals, allocator_api)]

use std::alloc::{Allocator, Global, GlobalAlloc, Layout};
use std::mem;
use std::ptr::{drop_in_place, NonNull, Unique};

struct Box<T>{ ptr: Unique<T> }

impl<T> Drop for Box<T> {
    fn drop(&mut self) {
        unsafe {
            drop_in_place(self.ptr.as_ptr());
            let c: NonNull<T> = self.ptr.into();
            Global.deallocate(c.cast(), Layout::new::<T>())
        }
    }
}
# fn main() {}
```

and this works fine because when Rust goes to drop the `ptr` field it just sees
a [Unique] that has no actual `Drop` implementation. Similarly nothing can
use-after-free the `ptr` because when drop exits, it becomes inaccessible.

However this wouldn't work:

```rust
#![feature(allocator_api, ptr_internals)]

use std::alloc::{Allocator, Global, GlobalAlloc, Layout};
use std::ptr::{drop_in_place, Unique, NonNull};
use std::mem;

struct Box<T>{ ptr: Unique<T> }

impl<T> Drop for Box<T> {
    fn drop(&mut self) {
        unsafe {
            drop_in_place(self.ptr.as_ptr());
            let c: NonNull<T> = self.ptr.into();
            Global.deallocate(c.cast(), Layout::new::<T>());
        }
    }
}

struct SuperBox<T> { my_box: Box<T> }

impl<T> Drop for SuperBox<T> {
    fn drop(&mut self) {
        unsafe {
            // Hyper-optimized: deallocate the box's contents for it
            // without `drop`ing the contents
            let c: NonNull<T> = self.my_box.ptr.into();
            Global.deallocate(c.cast::<u8>(), Layout::new::<T>());
        }
    }
}
# fn main() {}
```

After we deallocate the `box`'s ptr in SuperBox's destructor, Rust will
happily proceed to tell the box to Drop itself and everything will blow up with
use-after-frees and double-frees.

Note that the recursive drop behavior applies to all structs and enums
regardless of whether they implement Drop. Therefore something like

```rust
struct Boxy<T> {
    data1: Box<T>,
    data2: Box<T>,
    info: u32,
}
```

will have the destructors of its `data1` and `data2` fields called whenever it "would" be
dropped, even though it itself doesn't implement Drop. We say that such a type
*needs Drop*, even though it is not itself Drop.

Similarly,

```rust
enum Link {
    Next(Box<Link>),
    None,
}
```

will have its inner Box field dropped if and only if an instance stores the
Next variant.

In general this works really nicely because you don't need to worry about
adding/removing drops when you refactor your data layout. Still there's
certainly many valid use cases for needing to do trickier things with
destructors.

The classic safe solution to overriding recursive drop and allowing moving out
of Self during `drop` is to use an Option:

```rust
#![feature(allocator_api, ptr_internals)]

use std::alloc::{Allocator, GlobalAlloc, Global, Layout};
use std::ptr::{drop_in_place, Unique, NonNull};
use std::mem;

struct Box<T>{ ptr: Unique<T> }

impl<T> Drop for Box<T> {
    fn drop(&mut self) {
        unsafe {
            drop_in_place(self.ptr.as_ptr());
            let c: NonNull<T> = self.ptr.into();
            Global.deallocate(c.cast(), Layout::new::<T>());
        }
    }
}

struct SuperBox<T> { my_box: Option<Box<T>> }

impl<T> Drop for SuperBox<T> {
    fn drop(&mut self) {
        unsafe {
            // Hyper-optimized: deallocate the box's contents for it
            // without `drop`ing the contents. Need to set the `box`
            // field as `None` to prevent Rust from trying to Drop it.
            let my_box = self.my_box.take().unwrap();
            let c: NonNull<T> = my_box.ptr.into();
            Global.deallocate(c.cast(), Layout::new::<T>());
            mem::forget(my_box);
        }
    }
}
# fn main() {}
```

However this has fairly odd semantics: you are saying that a field that *should*
always be Some *may* be None, just because of what happens in the destructor. Of
course this conversely makes a lot of sense: you can call arbitrary methods on
self during the destructor, and this should prevent you from ever doing so after
deinitializing the field. Not that it will prevent you from producing any other
arbitrarily invalid state in there.

On balance this is an ok choice. Certainly what you should reach for by default.
However, in the future we expect there to be a first-class way to announce that
a field shouldn't be automatically dropped.

[Unique]: phantom-data.html


---

# Leaking

Ownership-based resource management is intended to simplify composition. You
acquire resources when you create the object, and you release the resources when
it gets destroyed. Since destruction is handled for you, it means you can't
forget to release the resources, and it happens as soon as possible! Surely this
is perfect and all of our problems are solved.

Everything is terrible and we have new and exotic problems to try to solve.

Many people like to believe that Rust eliminates resource leaks. In practice,
this is basically true. You would be surprised to see a Safe Rust program
leak resources in an uncontrolled way.

However from a theoretical perspective this is absolutely not the case, no
matter how you look at it. In the strictest sense, "leaking" is so abstract as
to be unpreventable. It's quite trivial to initialize a collection at the start
of a program, fill it with tons of objects with destructors, and then enter an
infinite event loop that never refers to it. The collection will sit around
uselessly, holding on to its precious resources until the program terminates (at
which point all those resources would have been reclaimed by the OS anyway).

We may consider a more restricted form of leak: failing to drop a value that is
unreachable. Rust also doesn't prevent this. In fact Rust *has a function for
doing this*: `mem::forget`. This function consumes the value it is passed *and
then doesn't run its destructor*.

In the past `mem::forget` was marked as unsafe as a sort of lint against using
it, since failing to call a destructor is generally not a well-behaved thing to
do (though useful for some special unsafe code). However this was generally
determined to be an untenable stance to take: there are many ways to fail to
call a destructor in safe code. The most famous example is creating a cycle of
reference-counted pointers using interior mutability.

It is reasonable for safe code to assume that destructor leaks do not happen, as
any program that leaks destructors is probably wrong. However *unsafe* code
cannot rely on destructors to be run in order to be safe. For most types this
doesn't matter: if you leak the destructor then the type is by definition
inaccessible, so it doesn't matter, right? For instance, if you leak a `Box<u8>`
then you waste some memory but that's hardly going to violate memory-safety.

However where we must be careful with destructor leaks are *proxy* types. These
are types which manage access to a distinct object, but don't actually own it.
Proxy objects are quite rare. Proxy objects you'll need to care about are even
rarer. However we'll focus on three interesting examples in the standard
library:

* `vec::Drain`
* `Rc`
* `thread::scoped::JoinGuard`

## Drain

`drain` is a collections API that moves data out of the container without
consuming the container. This enables us to reuse the allocation of a `Vec`
after claiming ownership over all of its contents. It produces an iterator
(Drain) that returns the contents of the Vec by-value.

Now, consider Drain in the middle of iteration: some values have been moved out,
and others haven't. This means that part of the Vec is now full of logically
uninitialized data! We could backshift all the elements in the Vec every time we
remove a value, but this would have pretty catastrophic performance
consequences.

Instead, we would like Drain to fix the Vec's backing storage when it is
dropped. It should run itself to completion, backshift any elements that weren't
removed (drain supports subranges), and then fix Vec's `len`. It's even
unwinding-safe! Easy!

Now consider the following:

<!-- ignore: simplified code -->
```rust,ignore
let mut vec = vec![Box::new(0); 4];

{
    // start draining, vec can no longer be accessed
    let mut drainer = vec.drain(..);

    // pull out two elements and immediately drop them
    drainer.next();
    drainer.next();

    // get rid of drainer, but don't call its destructor
    mem::forget(drainer);
}

// Oops, vec[0] was dropped, we're reading a pointer into free'd memory!
println!("{}", vec[0]);
```

This is pretty clearly Not Good. Unfortunately, we're kind of stuck between a
rock and a hard place: maintaining consistent state at every step has an
enormous cost (and would negate any benefits of the API). Failing to maintain
consistent state gives us Undefined Behavior in safe code (making the API
unsound).

So what can we do? Well, we can pick a trivially consistent state: set the Vec's
len to be 0 when we start the iteration, and fix it up if necessary in the
destructor. That way, if everything executes like normal we get the desired
behavior with minimal overhead. But if someone has the *audacity* to
mem::forget us in the middle of the iteration, all that does is *leak even more*
(and possibly leave the Vec in an unexpected but otherwise consistent state).
Since we've accepted that mem::forget is safe, this is definitely safe. We call
leaks causing more leaks a *leak amplification*.

## Rc

Rc is an interesting case because at first glance it doesn't appear to be a
proxy value at all. After all, it manages the data it points to, and dropping
all the Rcs for a value will drop that value. Leaking an Rc doesn't seem like it
would be particularly dangerous. It will leave the refcount permanently
incremented and prevent the data from being freed or dropped, but that seems
just like Box, right?

Nope.

Let's consider a simplified implementation of Rc:

<!-- ignore: simplified code -->
```rust,ignore
struct Rc<T> {
    ptr: *mut RcBox<T>,
}

struct RcBox<T> {
    data: T,
    ref_count: usize,
}

impl<T> Rc<T> {
    fn new(data: T) -> Self {
        unsafe {
            // Wouldn't it be nice if heap::allocate worked like this?
            let ptr = heap::allocate::<RcBox<T>>();
            ptr::write(ptr, RcBox {
                data,
                ref_count: 1,
            });
            Rc { ptr }
        }
    }

    fn clone(&self) -> Self {
        unsafe {
            (*self.ptr).ref_count += 1;
        }
        Rc { ptr: self.ptr }
    }
}

impl<T> Drop for Rc<T> {
    fn drop(&mut self) {
        unsafe {
            (*self.ptr).ref_count -= 1;
            if (*self.ptr).ref_count == 0 {
                // drop the data and then free it
                ptr::read(self.ptr);
                heap::deallocate(self.ptr);
            }
        }
    }
}
```

This code contains an implicit and subtle assumption: `ref_count` can fit in a
`usize`, because there can't be more than `usize::MAX` Rcs in memory. However
this itself assumes that the `ref_count` accurately reflects the number of Rcs
in memory, which we know is false with `mem::forget`. Using `mem::forget` we can
overflow the `ref_count`, and then get it down to 0 with outstanding Rcs. Then
we can happily use-after-free the inner data. Bad Bad Not Good.

This can be solved by just checking the `ref_count` and doing *something*. The
standard library's stance is to just abort, because your program has become
horribly degenerate. Also *oh my gosh* it's such a ridiculous corner case.

## thread::scoped::JoinGuard

> Note: This API has already been removed from std, for more information
> you may refer [issue #24292](https://github.com/rust-lang/rust/issues/24292).
>
> This section remains here because we think this example is still
> important, regardless of whether it is part of std or not.

The thread::scoped API intended to allow threads to be spawned that reference
data on their parent's stack without any synchronization over that data by
ensuring the parent joins the thread before any of the shared data goes out
of scope.

<!-- ignore: simplified code -->
```rust,ignore
pub fn scoped<'a, F>(f: F) -> JoinGuard<'a>
    where F: FnOnce() + Send + 'a
```

Here `f` is some closure for the other thread to execute. Saying that
`F: Send + 'a` is saying that it closes over data that lives for `'a`, and it
either owns that data or the data was Sync (implying `&data` is Send).

Because JoinGuard has a lifetime, it keeps all the data it closes over
borrowed in the parent thread. This means the JoinGuard can't outlive
the data that the other thread is working on. When the JoinGuard *does* get
dropped it blocks the parent thread, ensuring the child terminates before any
of the closed-over data goes out of scope in the parent.

Usage looked like:

<!-- ignore: simplified code -->
```rust,ignore
let mut data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
{
    let mut guards = vec![];
    for x in &mut data {
        // Move the mutable reference into the closure, and execute
        // it on a different thread. The closure has a lifetime bound
        // by the lifetime of the mutable reference `x` we store in it.
        // The guard that is returned is in turn assigned the lifetime
        // of the closure, so it also mutably borrows `data` as `x` did.
        // This means we cannot access `data` until the guard goes away.
        let guard = thread::scoped(move || {
            *x *= 2;
        });
        // store the thread's guard for later
        guards.push(guard);
    }
    // All guards are dropped here, forcing the threads to join
    // (this thread blocks here until the others terminate).
    // Once the threads join, the borrow expires and the data becomes
    // accessible again in this thread.
}
// data is definitely mutated here.
```

In principle, this totally works! Rust's ownership system perfectly ensures it!
...except it relies on a destructor being called to be safe.

<!-- ignore: simplified code -->
```rust,ignore
let mut data = Box::new(0);
{
    let guard = thread::scoped(|| {
        // This is at best a data race. At worst, it's also a use-after-free.
        *data += 1;
    });
    // Because the guard is forgotten, expiring the loan without blocking this
    // thread.
    mem::forget(guard);
}
// So the Box is dropped here while the scoped thread may or may not be trying
// to access it.
```

Dang. Here the destructor running was pretty fundamental to the API, and it had
to be scrapped in favor of a completely different design.
