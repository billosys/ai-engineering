# Implementing Arc and Mutex

Knowing the theory is all fine and good, but the *best* way to understand
something is to use it. To better understand atomics and interior mutability,
we'll be implementing versions of the standard library's `Arc` and `Mutex` types.

TODO: Write `Mutex` chapters.


---

# Implementing Arc

In this section, we'll be implementing a simpler version of `std::sync::Arc`.
Similarly to [the implementation of `Vec` we made earlier](../vec/vec.md), we won't be
taking advantage of as many optimizations, intrinsics, or unstable code as the
standard library may.

This implementation is loosely based on the standard library's implementation
(technically taken from `alloc::sync` in 1.49, as that's where it's actually
implemented), but it will not support weak references at the moment as they
make the implementation slightly more complex.

Please note that this section is very work-in-progress at the moment.


---

# Layout

Let's start by making the layout for our implementation of `Arc`.

An `Arc<T>` provides thread-safe shared ownership of a value of type `T`,
allocated in the heap. Sharing implies immutability in Rust, so we don't need to
design anything that manages access to that value, right? Although interior
mutability types like Mutex allow Arc's users to create shared mutability, Arc
itself doesn't need to concern itself with these issues.

However there _is_ one place where Arc needs to concern itself with mutation:
destruction. When all the owners of the Arc go away, we need to be able to
`drop` its contents and free its allocation. So we need a way for an owner to
know if it's the _last_ owner, and the simplest way to do that is with a count
of the owners -- Reference Counting.

Unfortunately, this reference count is inherently shared mutable state, so Arc
_does_ need to think about synchronization. We _could_ use a Mutex for this, but
that's overkill. Instead, we'll use atomics. And since everyone already needs a
pointer to the T's allocation, we might as well put the reference count in that
same allocation.

Naively, it would look something like this:

```rust
use std::sync::atomic;

pub struct Arc<T> {
    ptr: *mut ArcInner<T>,
}

pub struct ArcInner<T> {
    rc: atomic::AtomicUsize,
    data: T,
}
```

This would compile, however it would be incorrect. First of all, the compiler
will give us too strict variance. For example, an `Arc<&'static str>` couldn't
be used where an `Arc<&'a str>` was expected. More importantly, it will give
incorrect ownership information to the drop checker, as it will assume we don't
own any values of type `T`. As this is a structure providing shared ownership of
a value, at some point there will be an instance of this structure that entirely
owns its data. See [the chapter on ownership and lifetimes](../ownership.md) for
all the details on variance and drop check.

To fix the first problem, we can use `NonNull<T>`. Note that `NonNull<T>` is a
wrapper around a raw pointer that declares that:

* We are covariant over `T`
* Our pointer is never null

To fix the second problem, we can include a `PhantomData` marker containing an
`ArcInner<T>`. This will tell the drop checker that we have some notion of
ownership of a value of `ArcInner<T>` (which itself contains some `T`).

With these changes we get our final structure:

```rust
use std::marker::PhantomData;
use std::ptr::NonNull;
use std::sync::atomic::AtomicUsize;

pub struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
    phantom: PhantomData<ArcInner<T>>,
}

pub struct ArcInner<T> {
    rc: AtomicUsize,
    data: T,
}
```


---

# Base Code

Now that we've decided the layout for our implementation of `Arc`, let's create
some basic code.

## Constructing the Arc

We'll first need a way to construct an `Arc<T>`.

This is pretty simple, as we just need to box the `ArcInner<T>` and get a
`NonNull<T>` pointer to it.

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Arc<T> {
    pub fn new(data: T) -> Arc<T> {
        // We start the reference count at 1, as that first reference is the
        // current pointer.
        let boxed = Box::new(ArcInner {
            rc: AtomicUsize::new(1),
            data,
        });
        Arc {
            // It is okay to call `.unwrap()` here as we get a pointer from
            // `Box::into_raw` which is guaranteed to not be null.
            ptr: NonNull::new(Box::into_raw(boxed)).unwrap(),
            phantom: PhantomData,
        }
    }
}
```

## Send and Sync

Since we're building a concurrency primitive, we'll need to be able to send it
across threads. Thus, we can implement the `Send` and `Sync` marker traits. For
more information on these, see [the section on `Send` and
`Sync`](../send-and-sync.md).

This is okay because:
* You can only get a mutable reference to the value inside an `Arc` if and only
  if it is the only `Arc` referencing that data (which only happens in `Drop`)
* We use atomics for the shared mutable reference counting

<!-- ignore: simplified code -->
```rust,ignore
unsafe impl<T: Sync + Send> Send for Arc<T> {}
unsafe impl<T: Sync + Send> Sync for Arc<T> {}
```

We need to have the bound `T: Sync + Send` because if we did not provide those
bounds, it would be possible to share values that are thread-unsafe across a
thread boundary via an `Arc`, which could possibly cause data races or
unsoundness.

For example, if those bounds were not present, `Arc<Rc<u32>>` would be `Sync` or
`Send`, meaning that you could clone the `Rc` out of the `Arc` to send it across
a thread (without creating an entirely new `Rc`), which would create data races
as `Rc` is not thread-safe.

## Getting the `ArcInner`

To dereference the `NonNull<T>` pointer into a `&T`, we can call
`NonNull::as_ref`. This is unsafe, unlike the typical `as_ref` function, so we
must call it like this:

<!-- ignore: simplified code -->
```rust,ignore
unsafe { self.ptr.as_ref() }
```

We'll be using this snippet a few times in this code (usually with an associated
`let` binding).

This unsafety is okay because while this `Arc` is alive, we're guaranteed that
the inner pointer is valid.

## Deref

Alright. Now we can make `Arc`s (and soon will be able to clone and destroy them correctly), but how do we get
to the data inside?

What we need now is an implementation of `Deref`.

We'll need to import the trait:

<!-- ignore: simplified code -->
```rust,ignore
use std::ops::Deref;
```

And here's the implementation:

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Deref for Arc<T> {
    type Target = T;

    fn deref(&self) -> &T {
        let inner = unsafe { self.ptr.as_ref() };
        &inner.data
    }
}
```

Pretty simple, eh? This simply dereferences the `NonNull` pointer to the
`ArcInner<T>`, then gets a reference to the data inside.

## Code

Here's all the code from this section:

<!-- ignore: simplified code -->
```rust,ignore
use std::ops::Deref;

impl<T> Arc<T> {
    pub fn new(data: T) -> Arc<T> {
        // We start the reference count at 1, as that first reference is the
        // current pointer.
        let boxed = Box::new(ArcInner {
            rc: AtomicUsize::new(1),
            data,
        });
        Arc {
            // It is okay to call `.unwrap()` here as we get a pointer from
            // `Box::into_raw` which is guaranteed to not be null.
            ptr: NonNull::new(Box::into_raw(boxed)).unwrap(),
            phantom: PhantomData,
        }
    }
}

unsafe impl<T: Sync + Send> Send for Arc<T> {}
unsafe impl<T: Sync + Send> Sync for Arc<T> {}


impl<T> Deref for Arc<T> {
    type Target = T;

    fn deref(&self) -> &T {
        let inner = unsafe { self.ptr.as_ref() };
        &inner.data
    }
}
```


---

# Cloning

Now that we've got some basic code set up, we'll need a way to clone the `Arc`.

Basically, we need to:

1. Increment the atomic reference count
2. Construct a new instance of the `Arc` from the inner pointer

First, we need to get access to the `ArcInner`:

<!-- ignore: simplified code -->
```rust,ignore
let inner = unsafe { self.ptr.as_ref() };
```

We can update the atomic reference count as follows:

<!-- ignore: simplified code -->
```rust,ignore
let old_rc = inner.rc.fetch_add(1, Ordering::???);
```

But what ordering should we use here? We don't really have any code that will
need atomic synchronization when cloning, as we do not modify the internal value
while cloning. Thus, we can use a Relaxed ordering here, which implies no
happens-before relationship but is atomic. When `Drop`ping the Arc, however,
we'll need to atomically synchronize when decrementing the reference count. This
is described more in [the section on the `Drop` implementation for
`Arc`](arc-drop.md). For more information on atomic relationships and Relaxed
ordering, see [the section on atomics](../atomics.md).

Thus, the code becomes this:

<!-- ignore: simplified code -->
```rust,ignore
let old_rc = inner.rc.fetch_add(1, Ordering::Relaxed);
```

We'll need to add another import to use `Ordering`:

```rust
use std::sync::atomic::Ordering;
```

However, we have one problem with this implementation right now. What if someone
decides to `mem::forget` a bunch of Arcs? The code we have written so far (and
will write) assumes that the reference count accurately portrays how many Arcs
are in memory, but with `mem::forget` this is false. Thus, when more and more
Arcs are cloned from this one without them being `Drop`ped and the reference
count being decremented, we can overflow! This will cause use-after-free which
is **INCREDIBLY BAD!**

To handle this, we need to check that the reference count does not go over some
arbitrary value (below `usize::MAX`, as we're storing the reference count as an
`AtomicUsize`), and do *something*.

The standard library's implementation decides to just abort the program (as it
is an incredibly unlikely case in normal code and if it happens, the program is
probably incredibly degenerate) if the reference count reaches `isize::MAX`
(about half of `usize::MAX`) on any thread, on the assumption that there are
probably not about 2 billion threads (or about **9 quintillion** on some 64-bit
machines) incrementing the reference count at once. This is what we'll do.

It's pretty simple to implement this behavior:

<!-- ignore: simplified code -->
```rust,ignore
if old_rc >= isize::MAX as usize {
    std::process::abort();
}
```

Then, we need to return a new instance of the `Arc`:

<!-- ignore: simplified code -->
```rust,ignore
Self {
    ptr: self.ptr,
    phantom: PhantomData
}
```

Now, let's wrap this all up inside the `Clone` implementation:

<!-- ignore: simplified code -->
```rust,ignore
use std::sync::atomic::Ordering;

impl<T> Clone for Arc<T> {
    fn clone(&self) -> Arc<T> {
        let inner = unsafe { self.ptr.as_ref() };
        // Using a relaxed ordering is alright here as we don't need any atomic
        // synchronization here as we're not modifying or accessing the inner
        // data.
        let old_rc = inner.rc.fetch_add(1, Ordering::Relaxed);

        if old_rc >= isize::MAX as usize {
            std::process::abort();
        }

        Self {
            ptr: self.ptr,
            phantom: PhantomData,
        }
    }
}
```


---

# Dropping

We now need a way to decrease the reference count and drop the data once it is
low enough, otherwise the data will live forever on the heap.

To do this, we can implement `Drop`.

Basically, we need to:

1. Decrement the reference count
2. If there is only one reference remaining to the data, then:
3. Atomically fence the data to prevent reordering of the use and deletion of
   the data
4. Drop the inner data

First, we'll need to get access to the `ArcInner`:

<!-- ignore: simplified code -->
```rust,ignore
let inner = unsafe { self.ptr.as_ref() };
```

Now, we need to decrement the reference count. To streamline our code, we can
also return if the returned value from `fetch_sub` (the value of the reference
count before decrementing it) is not equal to `1` (which happens when we are not
the last reference to the data).

<!-- ignore: simplified code -->
```rust,ignore
if inner.rc.fetch_sub(1, Ordering::Release) != 1 {
    return;
}
```

We then need to create an atomic fence to prevent reordering of the use of the
data and deletion of the data. As described in [the standard library's
implementation of `Arc`][3]:
> This fence is needed to prevent reordering of use of the data and deletion of
> the data. Because it is marked `Release`, the decreasing of the reference
> count synchronizes with this `Acquire` fence. This means that use of the data
> happens before decreasing the reference count, which happens before this
> fence, which happens before the deletion of the data.
>
> As explained in the [Boost documentation][1],
>
> > It is important to enforce any possible access to the object in one
> > thread (through an existing reference) to *happen before* deleting
> > the object in a different thread. This is achieved by a "release"
> > operation after dropping a reference (any access to the object
> > through this reference must obviously happened before), and an
> > "acquire" operation before deleting the object.
>
> In particular, while the contents of an Arc are usually immutable, it's
> possible to have interior writes to something like a `Mutex<T>`. Since a Mutex
> is not acquired when it is deleted, we can't rely on its synchronization logic
> to make writes in thread A visible to a destructor running in thread B.
>
> Also note that the Acquire fence here could probably be replaced with an
> Acquire load, which could improve performance in highly-contended situations.
> See [2].
>
> [1]: https://www.boost.org/doc/libs/1_55_0/doc/html/atomic/usage_examples.html
> [2]: https://github.com/rust-lang/rust/pull/41714
[3]: https://github.com/rust-lang/rust/blob/e1884a8e3c3e813aada8254edfa120e85bf5ffca/library/alloc/src/sync.rs#L1440-L1467

To do this, we do the following:

```rust
# use std::sync::atomic::Ordering;
use std::sync::atomic;
atomic::fence(Ordering::Acquire);
```

Finally, we can drop the data itself. We use `Box::from_raw` to drop the boxed
`ArcInner<T>` and its data. This takes a `*mut T` and not a `NonNull<T>`, so we
must convert using `NonNull::as_ptr`.

<!-- ignore: simplified code -->
```rust,ignore
unsafe { Box::from_raw(self.ptr.as_ptr()); }
```

This is safe as we know we have the last pointer to the `ArcInner` and that its
pointer is valid.

Now, let's wrap this all up inside the `Drop` implementation:

<!-- ignore: simplified code -->
```rust,ignore
impl<T> Drop for Arc<T> {
    fn drop(&mut self) {
        let inner = unsafe { self.ptr.as_ref() };
        if inner.rc.fetch_sub(1, Ordering::Release) != 1 {
            return;
        }
        // This fence is needed to prevent reordering of the use and deletion
        // of the data.
        atomic::fence(Ordering::Acquire);
        // This is safe as we know we have the last pointer to the `ArcInner`
        // and that its pointer is valid.
        unsafe { Box::from_raw(self.ptr.as_ptr()); }
    }
}
```


---

# Final Code

Here's the final code, with some added comments and re-ordered imports:

```rust
use std::marker::PhantomData;
use std::ops::Deref;
use std::ptr::NonNull;
use std::sync::atomic::{self, AtomicUsize, Ordering};

pub struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
    phantom: PhantomData<ArcInner<T>>,
}

pub struct ArcInner<T> {
    rc: AtomicUsize,
    data: T,
}

impl<T> Arc<T> {
    pub fn new(data: T) -> Arc<T> {
        // We start the reference count at 1, as that first reference is the
        // current pointer.
        let boxed = Box::new(ArcInner {
            rc: AtomicUsize::new(1),
            data,
        });
        Arc {
            // It is okay to call `.unwrap()` here as we get a pointer from
            // `Box::into_raw` which is guaranteed to not be null.
            ptr: NonNull::new(Box::into_raw(boxed)).unwrap(),
            phantom: PhantomData,
        }
    }
}

unsafe impl<T: Sync + Send> Send for Arc<T> {}
unsafe impl<T: Sync + Send> Sync for Arc<T> {}

impl<T> Deref for Arc<T> {
    type Target = T;

    fn deref(&self) -> &T {
        let inner = unsafe { self.ptr.as_ref() };
        &inner.data
    }
}

impl<T> Clone for Arc<T> {
    fn clone(&self) -> Arc<T> {
        let inner = unsafe { self.ptr.as_ref() };
        // Using a relaxed ordering is alright here as we don't need any atomic
        // synchronization here as we're not modifying or accessing the inner
        // data.
        let old_rc = inner.rc.fetch_add(1, Ordering::Relaxed);

        if old_rc >= isize::MAX as usize {
            std::process::abort();
        }

        Self {
            ptr: self.ptr,
            phantom: PhantomData,
        }
    }
}

impl<T> Drop for Arc<T> {
    fn drop(&mut self) {
        let inner = unsafe { self.ptr.as_ref() };
        if inner.rc.fetch_sub(1, Ordering::Release) != 1 {
            return;
        }
        // This fence is needed to prevent reordering of the use and deletion
        // of the data.
        atomic::fence(Ordering::Acquire);
        // This is safe as we know we have the last pointer to the `ArcInner`
        // and that its pointer is valid.
        unsafe { Box::from_raw(self.ptr.as_ptr()); }
    }
}
```
