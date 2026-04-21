# Concurrency and Parallelism

Rust as a language doesn't *really* have an opinion on how to do concurrency or
parallelism. The standard library exposes OS threads and blocking sys-calls
because everyone has those, and they're uniform enough that you can provide
an abstraction over them in a relatively uncontroversial way. Message passing,
green threads, and async APIs are all diverse enough that any abstraction over
them tends to involve trade-offs that we weren't willing to commit to for 1.0.

However the way Rust models concurrency makes it relatively easy to design your own
concurrency paradigm as a library and have everyone else's code Just Work
with yours. Just require the right lifetimes and Send and Sync where appropriate
and you're off to the races. Or rather, off to the... not... having... races.


---

# Data Races and Race Conditions

Safe Rust guarantees an absence of data races, which are defined as:

* two or more threads concurrently accessing a location of memory
* one or more of them is a write
* one or more of them is unsynchronized

A data race has Undefined Behavior, and is therefore impossible to perform in
Safe Rust. Data races are prevented *mostly* through Rust's ownership system alone:
it's impossible to alias a mutable reference, so it's impossible to perform a
data race. Interior mutability makes this more complicated, which is largely why
we have the Send and Sync traits (see the next section for more on this).

**However Rust does not prevent general race conditions.**

This is mathematically impossible in situations where you do not control the
scheduler, which is true for the normal OS environment. If you do control
preemption, it _can be_ possible to prevent general races - this technique is
used by frameworks such as [RTIC](https://github.com/rtic-rs/rtic). However,
actually having control over scheduling is a very uncommon case.

For this reason, it is considered "safe" for Rust to get deadlocked or do
something nonsensical with incorrect synchronization: this is known as a general
race condition or resource race. Obviously such a program isn't very good, but
Rust of course cannot prevent all logic errors.

In any case, a race condition cannot violate memory safety in a Rust program on
its own. Only in conjunction with some other unsafe code can a race condition
actually violate memory safety. For instance, a correct program looks like this:

```rust,no_run
use std::thread;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;

let data = vec![1, 2, 3, 4];
// Arc so that the memory the AtomicUsize is stored in still exists for
// the other thread to increment, even if we completely finish executing
// before it. Rust won't compile the program without it, because of the
// lifetime requirements of thread::spawn!
let idx = Arc::new(AtomicUsize::new(0));
let other_idx = idx.clone();

// `move` captures other_idx by-value, moving it into this thread
thread::spawn(move || {
    // It's ok to mutate idx because this value
    // is an atomic, so it can't cause a Data Race.
    other_idx.fetch_add(10, Ordering::SeqCst);
});

// Index with the value loaded from the atomic. This is safe because we
// read the atomic memory only once, and then pass a copy of that value
// to the Vec's indexing implementation. This indexing will be correctly
// bounds checked, and there's no chance of the value getting changed
// in the middle. However our program may panic if the thread we spawned
// managed to increment before this ran. A race condition because correct
// program execution (panicking is rarely correct) depends on order of
// thread execution.
println!("{}", data[idx.load(Ordering::SeqCst)]);
```

We can cause a race condition to violate memory safety if we instead do the bound
check in advance, and then unsafely access the data with an unchecked value:

```rust,no_run
use std::thread;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;

let data = vec![1, 2, 3, 4];

let idx = Arc::new(AtomicUsize::new(0));
let other_idx = idx.clone();

// `move` captures other_idx by-value, moving it into this thread
thread::spawn(move || {
    // It's ok to mutate idx because this value
    // is an atomic, so it can't cause a Data Race.
    other_idx.fetch_add(10, Ordering::SeqCst);
});

if idx.load(Ordering::SeqCst) < data.len() {
    unsafe {
        // Incorrectly loading the idx after we did the bounds check.
        // It could have changed. This is a race condition, *and dangerous*
        // because we decided to do `get_unchecked`, which is `unsafe`.
        println!("{}", data.get_unchecked(idx.load(Ordering::SeqCst)));
    }
}
```


---

# Send and Sync

Not everything obeys inherited mutability, though. Some types allow you to
have multiple aliases of a location in memory while mutating it. Unless these types use
synchronization to manage this access, they are absolutely not thread-safe. Rust
captures this through the `Send` and `Sync` traits.

* A type is Send if it is safe to send it to another thread.
* A type is Sync if it is safe to share between threads (T is Sync if and only if `&T` is Send).

Send and Sync are fundamental to Rust's concurrency story. As such, a
substantial amount of special tooling exists to make them work right. First and
foremost, they're [unsafe traits]. This means that they are unsafe to
implement, and other unsafe code can assume that they are correctly
implemented. Since they're *marker traits* (they have no associated items like
methods), correctly implemented simply means that they have the intrinsic
properties an implementor should have. Incorrectly implementing Send or Sync can
cause Undefined Behavior.

Send and Sync are also automatically derived traits. This means that, unlike
every other trait, if a type is composed entirely of Send or Sync types, then it
is Send or Sync. Almost all primitives are Send and Sync, and as a consequence
pretty much all types you'll ever interact with are Send and Sync.

Major exceptions include:

* raw pointers are neither Send nor Sync (because they have no safety guards).
* `UnsafeCell` isn't Sync (and therefore `Cell` and `RefCell` aren't).
* `Rc` isn't Send or Sync (because the refcount is shared and unsynchronized).

`Rc` and `UnsafeCell` are very fundamentally not thread-safe: they enable
unsynchronized shared mutable state. However raw pointers are, strictly
speaking, marked as thread-unsafe as more of a *lint*. Doing anything useful
with a raw pointer requires dereferencing it, which is already unsafe. In that
sense, one could argue that it would be "fine" for them to be marked as thread
safe.

However it's important that they aren't thread-safe to prevent types that
contain them from being automatically marked as thread-safe. These types have
non-trivial untracked ownership, and it's unlikely that their author was
necessarily thinking hard about thread safety. In the case of `Rc`, we have a nice
example of a type that contains a `*mut` that is definitely not thread-safe.

Types that aren't automatically derived can simply implement them if desired:

```rust
struct MyBox(*mut u8);

unsafe impl Send for MyBox {}
unsafe impl Sync for MyBox {}
```

In the *incredibly rare* case that a type is inappropriately automatically
derived to be Send or Sync, then one can also unimplement Send and Sync:

```rust
#![feature(negative_impls)]

// I have some magic semantics for some synchronization primitive!
struct SpecialThreadToken(u8);

impl !Send for SpecialThreadToken {}
impl !Sync for SpecialThreadToken {}
```

Note that *in and of itself* it is impossible to incorrectly derive Send and
Sync. Only types that are ascribed special meaning by other unsafe code can
possibly cause trouble by being incorrectly Send or Sync.

Most uses of raw pointers should be encapsulated behind a sufficient abstraction
that Send and Sync can be derived. For instance all of Rust's standard
collections are Send and Sync (when they contain Send and Sync types) in spite
of their pervasive use of raw pointers to manage allocations and complex ownership.
Similarly, most iterators into these collections are Send and Sync because they
largely behave like an `&` or `&mut` into the collection.

## Example

[`Box`][box-doc] is implemented as its own special intrinsic type by the
compiler for [various reasons][box-is-special], but we can implement something
with similar-ish behavior ourselves to see an example of when it is sound to
implement Send and Sync. Let's call it a `Carton`.

We start by writing code to take a value allocated on the stack and transfer it
to the heap.

```rust
# pub mod libc {
#    pub use ::std::os::raw::{c_int, c_void};
#    #[allow(non_camel_case_types)]
#    pub type size_t = usize;
#    unsafe extern "C" { pub fn posix_memalign(memptr: *mut *mut c_void, align: size_t, size: size_t) -> c_int; }
# }
use std::{
    mem::{align_of, size_of},
    ptr,
    cmp::max,
};

struct Carton<T>(ptr::NonNull<T>);

impl<T> Carton<T> {
    pub fn new(value: T) -> Self {
        // Allocate enough memory on the heap to store one T.
        assert_ne!(size_of::<T>(), 0, "Zero-sized types are out of the scope of this example");
        let mut memptr: *mut T = ptr::null_mut();
        unsafe {
            let ret = libc::posix_memalign(
                (&mut memptr as *mut *mut T).cast(),
                max(align_of::<T>(), size_of::<usize>()),
                size_of::<T>()
            );
            assert_eq!(ret, 0, "Failed to allocate or invalid alignment");
        };

        // NonNull is just a wrapper that enforces that the pointer isn't null.
        let ptr = {
            // Safety: memptr is dereferenceable because we created it from a
            // reference and have exclusive access.
            ptr::NonNull::new(memptr)
                .expect("Guaranteed non-null if posix_memalign returns 0")
        };

        // Move value from the stack to the location we allocated on the heap.
        unsafe {
            // Safety: If non-null, posix_memalign gives us a ptr that is valid
            // for writes and properly aligned.
            ptr.as_ptr().write(value);
        }

        Self(ptr)
    }
}
```

This isn't very useful, because once our users give us a value they have no way
to access it. [`Box`][box-doc] implements [`Deref`][deref-doc] and
[`DerefMut`][deref-mut-doc] so that you can access the inner value. Let's do
that.

```rust
use std::ops::{Deref, DerefMut};

# struct Carton<T>(std::ptr::NonNull<T>);
#
impl<T> Deref for Carton<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        unsafe {
            // Safety: The pointer is aligned, initialized, and dereferenceable
            //   by the logic in [`Self::new`]. We require readers to borrow the
            //   Carton, and the lifetime of the return value is elided to the
            //   lifetime of the input. This means the borrow checker will
            //   enforce that no one can mutate the contents of the Carton until
            //   the reference returned is dropped.
            self.0.as_ref()
        }
    }
}

impl<T> DerefMut for Carton<T> {
    fn deref_mut(&mut self) -> &mut Self::Target {
        unsafe {
            // Safety: The pointer is aligned, initialized, and dereferenceable
            //   by the logic in [`Self::new`]. We require writers to mutably
            //   borrow the Carton, and the lifetime of the return value is
            //   elided to the lifetime of the input. This means the borrow
            //   checker will enforce that no one else can access the contents
            //   of the Carton until the mutable reference returned is dropped.
            self.0.as_mut()
        }
    }
}
```

Finally, let's think about whether our `Carton` is Send and Sync. Something can
safely be Send unless it shares mutable state with something else without
enforcing exclusive access to it. Each `Carton` has a unique pointer, so
we're good.

```rust
# struct Carton<T>(std::ptr::NonNull<T>);
// Safety: No one besides us has the raw pointer, so we can safely transfer the
// Carton to another thread if T can be safely transferred.
unsafe impl<T> Send for Carton<T> where T: Send {}
```

What about Sync? For `Carton` to be Sync we have to enforce that you can't
write to something stored in a `&Carton` while that same something could be read
or written to from another `&Carton`. Since you need an `&mut Carton` to
write to the pointer, and the borrow checker enforces that mutable
references must be exclusive, there are no soundness issues making `Carton`
sync either.

```rust
# struct Carton<T>(std::ptr::NonNull<T>);
// Safety: Since there exists a public way to go from a `&Carton<T>` to a `&T`
// in an unsynchronized fashion (such as `Deref`), then `Carton<T>` can't be
// `Sync` if `T` isn't.
// Conversely, `Carton` itself does not use any interior mutability whatsoever:
// all the mutations are performed through an exclusive reference (`&mut`). This
// means it suffices that `T` be `Sync` for `Carton<T>` to be `Sync`:
unsafe impl<T> Sync for Carton<T> where T: Sync  {}
```

When we assert our type is Send and Sync we usually need to enforce that every
contained type is Send and Sync. When writing custom types that behave like
standard library types we can assert that we have the same requirements.
For example, the following code asserts that a Carton is Send if the same
sort of Box would be Send, which in this case is the same as saying T is Send.

```rust
# struct Carton<T>(std::ptr::NonNull<T>);
unsafe impl<T> Send for Carton<T> where Box<T>: Send {}
```

Right now `Carton<T>` has a memory leak, as it never frees the memory it allocates.
Once we fix that we have a new requirement we have to ensure we meet to be Send:
we need to know `free` can be called on a pointer that was yielded by an
allocation done on another thread. We can check this is true in the docs for
[`libc::free`][libc-free-docs].

```rust
# struct Carton<T>(std::ptr::NonNull<T>);
# mod libc {
#     pub use ::std::os::raw::c_void;
#     unsafe extern "C" { pub fn free(p: *mut c_void); }
# }
impl<T> Drop for Carton<T> {
    fn drop(&mut self) {
        unsafe {
            libc::free(self.0.as_ptr().cast());
        }
    }
}
```

A nice example where this does not happen is with a MutexGuard: notice how
[it is not Send][mutex-guard-not-send-docs-rs]. The implementation of MutexGuard
[uses libraries][mutex-guard-not-send-comment] that require you to ensure you
don't try to free a lock that you acquired in a different thread. If you were
able to Send a MutexGuard to another thread the destructor would run in the
thread you sent it to, violating the requirement. MutexGuard can still be Sync
because all you can send to another thread is an `&MutexGuard` and dropping a
reference does nothing.

TODO: better explain what can or can't be Send or Sync. Sufficient to appeal
only to data races?

[unsafe traits]: safe-unsafe-meaning.html
[box-doc]: https://doc.rust-lang.org/std/boxed/struct.Box.html
[box-is-special]: https://manishearth.github.io/blog/2017/01/10/rust-tidbits-box-is-special/
[deref-doc]: https://doc.rust-lang.org/core/ops/trait.Deref.html
[deref-mut-doc]: https://doc.rust-lang.org/core/ops/trait.DerefMut.html
[mutex-guard-not-send-docs-rs]: https://doc.rust-lang.org/std/sync/struct.MutexGuard.html#impl-Send-for-MutexGuard%3C'_,+T%3E
[mutex-guard-not-send-comment]: https://github.com/rust-lang/rust/issues/23465#issuecomment-82730326
[libc-free-docs]: https://linux.die.net/man/3/free


---

# Atomics

Rust pretty blatantly just inherits the memory model for atomics from C++20. This is not
due to this model being particularly excellent or easy to understand. Indeed,
this model is quite complex and known to have [several flaws][C11-busted].
Rather, it is a pragmatic concession to the fact that *everyone* is pretty bad
at modeling atomics. At the very least, we can benefit from existing tooling and
research around the C/C++ memory model.
(You'll often see this model referred to as "C/C++11" or just "C11". C just copies
the C++ memory model; and C++11 was the first version of the model but it has
received some bugfixes since then.)

Trying to fully explain the model in this book is fairly hopeless. It's defined
in terms of madness-inducing causality graphs that require a full book to
properly understand in a practical way. If you want all the nitty-gritty
details, you should check out the [C++ specification][C++-model].
Still, we'll try to cover the basics and some of the problems Rust developers
face.

The C++ memory model is fundamentally about trying to bridge the gap between the
semantics we want, the optimizations compilers want, and the inconsistent chaos
our hardware wants. *We* would like to just write programs and have them do
exactly what we said but, you know, fast. Wouldn't that be great?

## Compiler Reordering

Compilers fundamentally want to be able to do all sorts of complicated
transformations to reduce data dependencies and eliminate dead code. In
particular, they may radically change the actual order of events, or make events
never occur! If we write something like:

<!-- ignore: simplified code -->
```rust,ignore
x = 1;
y = 3;
x = 2;
```

The compiler may conclude that it would be best if your program did:

<!-- ignore: simplified code -->
```rust,ignore
x = 2;
y = 3;
```

This has inverted the order of events and completely eliminated one event.
From a single-threaded perspective this is completely unobservable: after all
the statements have executed we are in exactly the same state. But if our
program is multi-threaded, we may have been relying on `x` to actually be
assigned to 1 before `y` was assigned. We would like the compiler to be
able to make these kinds of optimizations, because they can seriously improve
performance. On the other hand, we'd also like to be able to depend on our
program *doing the thing we said*.

## Hardware Reordering

On the other hand, even if the compiler totally understood what we wanted and
respected our wishes, our hardware might instead get us in trouble. Trouble
comes from CPUs in the form of memory hierarchies. There is indeed a global
shared memory space somewhere in your hardware, but from the perspective of each
CPU core it is *so very far away* and *so very slow*. Each CPU would rather work
with its local cache of the data and only go through all the anguish of
talking to shared memory only when it doesn't actually have that memory in
cache.

After all, that's the whole point of the cache, right? If every read from the
cache had to run back to shared memory to double check that it hadn't changed,
what would the point be? The end result is that the hardware doesn't guarantee
that events that occur in some order on *one* thread, occur in the same
order on *another* thread. To guarantee this, we must issue special instructions
to the CPU telling it to be a bit less smart.

For instance, say we convince the compiler to emit this logic:

```text
initial state: x = 0, y = 1

THREAD 1        THREAD 2
y = 3;          if x == 1 {
x = 1;              y *= 2;
                }
```

Ideally this program has 2 possible final states:

* `y = 3`: (thread 2 did the check before thread 1 completed)
* `y = 6`: (thread 2 did the check after thread 1 completed)

However there's a third potential state that the hardware enables:

* `y = 2`: (thread 2 saw `x = 1`, but not `y = 3`, and then overwrote `y = 3`)

It's worth noting that different kinds of CPU provide different guarantees. It
is common to separate hardware into two categories: strongly-ordered and weakly-ordered.
Most notably x86/64 provides strong ordering guarantees, while ARM
provides weak ordering guarantees. This has two consequences for concurrent
programming:

* Asking for stronger guarantees on strongly-ordered hardware may be cheap or
  even free because they already provide strong guarantees unconditionally.
  Weaker guarantees may only yield performance wins on weakly-ordered hardware.

* Asking for guarantees that are too weak on strongly-ordered hardware is
  more likely to *happen* to work, even though your program is strictly
  incorrect. If possible, concurrent algorithms should be tested on
  weakly-ordered hardware.

## Data Accesses

The C++ memory model attempts to bridge the gap by allowing us to talk about the
*causality* of our program. Generally, this is by establishing a *happens
before* relationship between parts of the program and the threads that are
running them. This gives the hardware and compiler room to optimize the program
more aggressively where a strict happens-before relationship isn't established,
but forces them to be more careful where one is established. The way we
communicate these relationships are through *data accesses* and *atomic
accesses*.

Data accesses are the bread-and-butter of the programming world. They are
fundamentally unsynchronized and compilers are free to aggressively optimize
them. In particular, data accesses are free to be reordered by the compiler on
the assumption that the program is single-threaded. The hardware is also free to
propagate the changes made in data accesses to other threads as lazily and
inconsistently as it wants. Most critically, data accesses are how data races
happen. Data accesses are very friendly to the hardware and compiler, but as
we've seen they offer *awful* semantics to try to write synchronized code with.
Actually, that's too weak.

**It is literally impossible to write correct synchronized code using only data
accesses.**

Atomic accesses are how we tell the hardware and compiler that our program is
multi-threaded. Each atomic access can be marked with an *ordering* that
specifies what kind of relationship it establishes with other accesses. In
practice, this boils down to telling the compiler and hardware certain things
they *can't* do. For the compiler, this largely revolves around re-ordering of
instructions. For the hardware, this largely revolves around how writes are
propagated to other threads. The set of orderings Rust exposes are:

* Sequentially Consistent (SeqCst)
* Release
* Acquire
* Relaxed

(Note: We explicitly do not expose the C++ *consume* ordering)

TODO: negative reasoning vs positive reasoning? TODO: "can't forget to
synchronize"

## Sequentially Consistent

Sequentially Consistent is the most powerful of all, implying the restrictions
of all other orderings. Intuitively, a sequentially consistent operation
cannot be reordered: all accesses on one thread that happen before and after a
SeqCst access stay before and after it. A data-race-free program that uses
only sequentially consistent atomics and data accesses has the very nice
property that there is a single global execution of the program's instructions
that all threads agree on. This execution is also particularly nice to reason
about: it's just an interleaving of each thread's individual executions. This
does not hold if you start using the weaker atomic orderings.

The relative developer-friendliness of sequential consistency doesn't come for
free. Even on strongly-ordered platforms sequential consistency involves
emitting memory fences.

In practice, sequential consistency is rarely necessary for program correctness.
However sequential consistency is definitely the right choice if you're not
confident about the other memory orders. Having your program run a bit slower
than it needs to is certainly better than it running incorrectly! It's also
mechanically trivial to downgrade atomic operations to have a weaker
consistency later on. Just change `SeqCst` to `Relaxed` and you're done! Of
course, proving that this transformation is *correct* is a whole other matter.

## Acquire-Release

Acquire and Release are largely intended to be paired. Their names hint at their
use case: they're perfectly suited for acquiring and releasing locks, and
ensuring that critical sections don't overlap.

Intuitively, an acquire access ensures that every access after it stays after
it. However operations that occur before an acquire are free to be reordered to
occur after it. Similarly, a release access ensures that every access before it
stays before it. However operations that occur after a release are free to be
reordered to occur before it.

When thread A releases a location in memory and then thread B subsequently
acquires *the same* location in memory, causality is established. Every write
(including non-atomic and relaxed atomic writes) that happened before A's
release will be observed by B after its acquisition. However no causality is
established with any other threads. Similarly, no causality is established
if A and B access *different* locations in memory.

Basic use of release-acquire is therefore simple: you acquire a location of
memory to begin the critical section, and then release that location to end it.
For instance, a simple spinlock might look like:

```rust
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, Ordering};
use std::thread;

fn main() {
    let lock = Arc::new(AtomicBool::new(false)); // value answers "am I locked?"

    // ... distribute lock to threads somehow ...

    // Try to acquire the lock by setting it to true
    while lock.compare_exchange(false, true, Ordering::Acquire, Ordering::Relaxed).is_err() { }
    // broke out of the loop, so we successfully acquired the lock!

    // ... scary data accesses ...

    // ok we're done, release the lock
    lock.store(false, Ordering::Release);
}
```

On strongly-ordered platforms most accesses have release or acquire semantics,
making release and acquire often totally free. This is not the case on
weakly-ordered platforms.

## Relaxed

Relaxed accesses are the absolute weakest. They can be freely re-ordered and
provide no happens-before relationship. Still, relaxed operations are still
atomic. That is, they don't count as data accesses and any read-modify-write
operations done to them occur atomically. Relaxed operations are appropriate for
things that you definitely want to happen, but don't particularly otherwise care
about. For instance, incrementing a counter can be safely done by multiple
threads using a relaxed `fetch_add` if you're not using the counter to
synchronize any other accesses.

There's rarely a benefit in making an operation relaxed on strongly-ordered
platforms, since they usually provide release-acquire semantics anyway. However
relaxed operations can be cheaper on weakly-ordered platforms.

[C11-busted]: http://plv.mpi-sws.org/c11comp/popl15.pdf
[C++-model]: https://en.cppreference.com/w/cpp/atomic/memory_order
