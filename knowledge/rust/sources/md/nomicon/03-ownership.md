# Ownership and Lifetimes

Ownership is the breakout feature of Rust. It allows Rust to be completely
memory-safe and efficient, while avoiding garbage collection. Before getting
into the ownership system in detail, we will consider the motivation of this
design.

We will assume that you accept that garbage collection (GC) is not always an
optimal solution, and that it is desirable to manually manage memory in some
contexts. If you do not accept this, might I interest you in a different
language?

Regardless of your feelings on GC, it is pretty clearly a *massive* boon to
making code safe. You never have to worry about things going away *too soon*
(although whether you still wanted to be pointing at that thing is a different
issue...). This is a pervasive problem that C and C++ programs need to deal
with. Consider this simple mistake that all of us who have used a non-GC'd
language have made at one point:

```rust,compile_fail
fn as_str(data: &u32) -> &str {
    // compute the string
    let s = format!("{}", data);

    // OH NO! We returned a reference to something that
    // exists only in this function!
    // Dangling pointer! Use after free! Alas!
    // (this does not compile in Rust)
    &s
}
```

This is exactly what Rust's ownership system was built to solve.
Rust knows the scope in which the `&s` lives, and as such can prevent it from
escaping. However this is a simple case that even a C compiler could plausibly
catch. Things get more complicated as code gets bigger and pointers get fed through
various functions. Eventually, a C compiler will fall down and won't be able to
perform sufficient escape analysis to prove your code unsound. It will consequently
be forced to accept your program on the assumption that it is correct.

This will never happen to Rust. It's up to the programmer to prove to the
compiler that everything is sound.

Of course, Rust's story around ownership is much more complicated than just
verifying that references don't escape the scope of their referent. That's
because ensuring pointers are always valid is much more complicated than this.
For instance in this code,

```rust,compile_fail
let mut data = vec![1, 2, 3];
// get an internal reference
let x = &data[0];

// OH NO! `push` causes the backing storage of `data` to be reallocated.
// Dangling pointer! Use after free! Alas!
// (this does not compile in Rust)
data.push(4);

println!("{}", x);
```

naive scope analysis would be insufficient to prevent this bug, because `data`
does in fact live as long as we needed. However it was *changed* while we had
a reference into it. This is why Rust requires any references to freeze the
referent and its owners.


---

# References

There are two kinds of references:

* Shared reference: `&`
* Mutable reference: `&mut`

Which obey the following rules:

* A reference cannot outlive its referent
* A mutable reference cannot be aliased

That's it. That's the whole model references follow.

Of course, we should probably define what *aliased* means.

```text
error[E0425]: cannot find value `aliased` in this scope
 --> <rust.rs>:2:20
  |
2 |     println!("{}", aliased);
  |                    ^^^^^^^ not found in this scope

error: aborting due to previous error
```

Unfortunately, Rust hasn't actually defined its aliasing model. 🙀

While we wait for the Rust devs to specify the semantics of their language,
let's use the next section to discuss what aliasing is in general, and why it
matters.


---

# Aliasing

First off, let's get some important caveats out of the way:

* We will be using the broadest possible definition of aliasing for the sake
of discussion. Rust's definition will probably be more restricted to factor
in mutations and liveness.

* We will be assuming a single-threaded, interrupt-free, execution. We will also
be ignoring things like memory-mapped hardware. Rust assumes these things
don't happen unless you tell it otherwise. For more details, see the
[Concurrency Chapter](concurrency.html).

With that said, here's our working definition: variables and pointers *alias*
if they refer to overlapping regions of memory.

## Why Aliasing Matters

So why should we care about aliasing?

Consider this simple function:

```rust
fn compute(input: &u32, output: &mut u32) {
    if *input > 10 {
        *output = 1;
    }
    if *input > 5 {
        *output *= 2;
    }
    // remember that `output` will be `2` if `input > 10`
}
```

We would *like* to be able to optimize it to the following function:

```rust
fn compute(input: &u32, output: &mut u32) {
    let cached_input = *input; // keep `*input` in a register
    if cached_input > 10 {
        // If the input is greater than 10, the previous code would set the output to 1 and then double it,
        // resulting in an output of 2 (because `>10` implies `>5`).
        // Here, we avoid the double assignment and just set it directly to 2.
        *output = 2;
    } else if cached_input > 5 {
        *output *= 2;
    }
}
```

In Rust, this optimization should be sound. For almost any other language, it
wouldn't be (barring global analysis). This is because the optimization relies
on knowing that aliasing doesn't occur, which most languages are fairly liberal
with. Specifically, we need to worry about function arguments that make `input`
and `output` overlap, such as `compute(&x, &mut x)`.

With that input, we could get this execution:

<!-- ignore: expanded code -->
```rust,ignore
                    //  input ==  output == 0xabad1dea
                    // *input == *output == 20
if *input > 10 {    // true  (*input == 20)
    *output = 1;    // also overwrites *input, because they are the same
}
if *input > 5 {     // false (*input == 1)
    *output *= 2;
}
                    // *input == *output == 1
```

Our optimized function would produce `*output == 2` for this input, so the
correctness of our optimization relies on this input being impossible.

In Rust we know this input should be impossible because `&mut` isn't allowed to be
aliased. So we can safely reject its possibility and perform this optimization.
In most other languages, this input would be entirely possible, and must be considered.

This is why alias analysis is important: it lets the compiler perform useful
optimizations! Some examples:

* keeping values in registers by proving no pointers access the value's memory
* eliminating reads by proving some memory hasn't been written to since last we read it
* eliminating writes by proving some memory is never read before the next write to it
* moving or reordering reads and writes by proving they don't depend on each other

These optimizations also tend to prove the soundness of bigger optimizations
such as loop vectorization, constant propagation, and dead code elimination.

In the previous example, we used the fact that `&mut u32` can't be aliased to prove
that writes to `*output` can't possibly affect `*input`. This lets us cache `*input`
in a register, eliminating a read.

By caching this read, we knew that the write in the `> 10` branch couldn't
affect whether we take the `> 5` branch, allowing us to also eliminate a
read-modify-write (doubling `*output`) when `*input > 10`.

The key thing to remember about alias analysis is that writes are the primary
hazard for optimizations. That is, the only thing that prevents us
from moving a read to any other part of the program is the possibility of us
re-ordering it with a write to the same location.

For instance, we have no concern for aliasing in the following modified version
of our function, because we've moved the only write to `*output` to the very
end of our function. This allows us to freely reorder the reads of `*input` that
occur before it:

```rust
fn compute(input: &u32, output: &mut u32) {
    let mut temp = *output;
    if *input > 10 {
        temp = 1;
    }
    if *input > 5 {
        temp *= 2;
    }
    *output = temp;
}
```

We're still relying on alias analysis to assume that `input` doesn't alias
`temp`, but the proof is much simpler: the value of a local variable can't be
aliased by things that existed before it was declared. This is an assumption
every language freely makes, and so this version of the function could be
optimized the way we want in any language.

This is why the definition of "alias" that Rust will use likely involves some
notion of liveness and mutation: we don't actually care if aliasing occurs if
there aren't any actual writes to memory happening.

Of course, a full aliasing model for Rust must also take into consideration things like
function calls (which may mutate things we don't see), raw pointers (which have
no aliasing requirements on their own), and UnsafeCell (which lets the referent
of an `&` be mutated).


---

# Lifetimes

Rust enforces these rules through *lifetimes*. Lifetimes are named
regions of code that a reference must be valid for. Those regions
may be fairly complex, as they correspond to paths of execution
in the program. There may even be holes in these paths of execution,
as it's possible to invalidate a reference as long as it's reinitialized
before it's used again. Types which contain references (or pretend to)
may also be tagged with lifetimes so that Rust can prevent them from
being invalidated as well.

In most of our examples, the lifetimes will coincide with scopes. This is
because our examples are simple. The more complex cases where they don't
coincide are described below.

Within a function body, Rust generally doesn't let you explicitly name the
lifetimes involved. This is because it's generally not really necessary
to talk about lifetimes in a local context; Rust has all the information and
can work out everything as optimally as possible. Many anonymous scopes and
temporaries that you would otherwise have to write are often introduced to
make your code Just Work.

However once you cross the function boundary, you need to start talking about
lifetimes. Lifetimes are denoted with an apostrophe: `'a`, `'static`. To dip
our toes with lifetimes, we're going to pretend that we're actually allowed
to label scopes with lifetimes, and desugar the examples from the start of
this chapter.

Originally, our examples made use of *aggressive* sugar -- high fructose corn
syrup even -- around scopes and lifetimes, because writing everything out
explicitly is *extremely noisy*. All Rust code relies on aggressive inference
and elision of "obvious" things.

One particularly interesting piece of sugar is that each `let` statement
implicitly introduces a scope. For the most part, this doesn't really matter.
However it does matter for variables that refer to each other. As a simple
example, let's completely desugar this simple piece of Rust code:

```rust
let x = 0;
let y = &x;
let z = &y;
```

The borrow checker always tries to minimize the extent of a lifetime, so it will
likely desugar to the following:

<!-- ignore: desugared code -->
```rust,ignore
// NOTE: `'a: {` and `&'b x` is not valid syntax!
'a: {
    let x: i32 = 0;
    'b: {
        // lifetime used is 'b because that's good enough.
        let y: &'b i32 = &'b x;
        'c: {
            // ditto on 'c
            let z: &'c &'b i32 = &'c y; // "a reference to a reference to an i32" (with lifetimes annotated)
        }
    }
}
```

Wow. That's... awful. Let's all take a moment to thank Rust for making this easier.

Actually passing references to outer scopes will cause Rust to infer
a larger lifetime:

```rust
let x = 0;
let z;
let y = &x;
z = y;
```

<!-- ignore: desugared code -->
```rust,ignore
'a: {
    let x: i32 = 0;
    'b: {
        let z: &'b i32;
        'c: {
            // Must use 'b here because the reference to x is
            // being passed to the scope 'b.
            let y: &'b i32 = &'b x;
            z = y;
        }
    }
}
```

## Example: references that outlive referents

Alright, let's look at some of those examples from before:

```rust,compile_fail
fn as_str(data: &u32) -> &str {
    let s = format!("{}", data);
    &s
}
```

desugars to:

<!-- ignore: desugared code -->
```rust,ignore
fn as_str<'a>(data: &'a u32) -> &'a str {
    'b: {
        let s = format!("{}", data);
        return &'a s;
    }
}
```

This signature of `as_str` takes a reference to a u32 with *some* lifetime, and
promises that it can produce a reference to a str that can live *just as long*.
Already we can see why this signature might be trouble. That basically implies
that we're going to find a str somewhere in the scope the reference
to the u32 originated in, or somewhere *even earlier*. That's a bit of a tall
order.

We then proceed to compute the string `s`, and return a reference to it. Since
the contract of our function says the reference must outlive `'a`, that's the
lifetime we infer for the reference. Unfortunately, `s` was defined in the
scope `'b`, so the only way this is sound is if `'b` contains `'a` -- which is
clearly false since `'a` must contain the function call itself. We have therefore
created a reference whose lifetime outlives its referent, which is *literally*
the first thing we said that references can't do. The compiler rightfully blows
up in our face.

To make this more clear, we can expand the example:

<!-- ignore: desugared code -->
```rust,ignore
fn as_str<'a>(data: &'a u32) -> &'a str {
    'b: {
        let s = format!("{}", data);
        return &'a s
    }
}

fn main() {
    'c: {
        let x: u32 = 0;
        'd: {
            // An anonymous scope is introduced because the borrow does not
            // need to last for the whole scope x is valid for. The return
            // of as_str must find a str somewhere before this function
            // call. Obviously not happening.
            println!("{}", as_str::<'d>(&'d x));
        }
    }
}
```

Shoot!

Of course, the right way to write this function is as follows:

```rust
fn to_string(data: &u32) -> String {
    format!("{}", data)
}
```

We must produce an owned value inside the function to return it! The only way
we could have returned an `&'a str` would have been if it was in a field of the
`&'a u32`, which is obviously not the case.

(Actually we could have also just returned a string literal, which as a global
can be considered to reside at the bottom of the stack; though this limits
our implementation *just a bit*.)

## Example: aliasing a mutable reference

How about the other example:

```rust,compile_fail
let mut data = vec![1, 2, 3];
let x = &data[0];
data.push(4);
println!("{}", x);
```

<!-- ignore: desugared code -->
```rust,ignore
'a: {
    let mut data: Vec<i32> = vec![1, 2, 3];
    'b: {
        // 'b is as big as we need this borrow to be
        // (just need to get to `println!`)
        let x: &'b i32 = Index::index::<'b>(&'b data, 0);
        'c: {
            // Temporary scope because we don't need the
            // &mut to last any longer.
            Vec::push(&'c mut data, 4);
        }
        println!("{}", x);
    }
}
```

The problem here is a bit more subtle and interesting. We want Rust to
reject this program for the following reason: We have a live shared reference `x`
to a descendant of `data` when we try to take a mutable reference to `data`
to `push`. This would create an aliased mutable reference, which would
violate the *second* rule of references.

However this is *not at all* how Rust reasons that this program is bad. Rust
doesn't understand that `x` is a reference to a subpath of `data`. It doesn't
understand `Vec` at all. What it *does* see is that `x` has to live for `'b` in
order to be printed. The signature of `Index::index` subsequently demands that
the reference we take to `data` has to survive for `'b`. When we try to call
`push`, it then sees us try to make an `&'c mut data`. Rust knows that `'c` is
contained within `'b`, and rejects our program because the `&'b data` must still
be alive!

Here we see that the lifetime system is much more coarse than the reference
semantics we're actually interested in preserving. For the most part, *that's
totally ok*, because it keeps us from spending all day explaining our program
to the compiler. However it does mean that several programs that are totally
correct with respect to Rust's *true* semantics are rejected because lifetimes
are too dumb.

## The area covered by a lifetime

A reference (sometimes called a *borrow*) is *alive* from the place it is
created to its last use. The borrowed value needs to outlive only borrows that
are alive. This looks simple, but there are a few subtleties.

The following snippet compiles, because after printing `x`, it is no longer
needed, so it doesn't matter if it is dangling or aliased (even though the
variable `x` *technically* exists to the very end of the scope).

```rust
let mut data = vec![1, 2, 3];
let x = &data[0];
println!("{}", x);
// This is OK, x is no longer needed
data.push(4);
```

However, if the value has a destructor, the destructor is run at the end of the
scope. And running the destructor is considered a use ‒ obviously the last one.
So, this will *not* compile.

```rust,compile_fail
#[derive(Debug)]
struct X<'a>(&'a i32);

impl Drop for X<'_> {
    fn drop(&mut self) {}
}

let mut data = vec![1, 2, 3];
let x = X(&data[0]);
println!("{:?}", x);
data.push(4);
// Here, the destructor is run and therefore this'll fail to compile.
```

One way to convince the compiler that `x` is no longer valid is by using `drop(x)` before `data.push(4)`.

Furthermore, there might be multiple possible last uses of the borrow, for
example in each branch of a condition.

```rust
# fn some_condition() -> bool { true }
let mut data = vec![1, 2, 3];
let x = &data[0];

if some_condition() {
    println!("{}", x); // This is the last use of `x` in this branch
    data.push(4);      // So we can push here
} else {
    // There's no use of `x` in here, so effectively the last use is the
    // creation of x at the top of the example.
    data.push(5);
}
```

And a lifetime can have a pause in it. Or you might look at it as two distinct
borrows just being tied to the same local variable. This often happens around
loops (writing a new value of a variable at the end of the loop and using it for
the last time at the top of the next iteration).

```rust
let mut data = vec![1, 2, 3];
// This mut allows us to change where the reference points to
let mut x = &data[0];

println!("{}", x); // Last use of this borrow
data.push(4);
x = &data[3]; // We start a new borrow here
println!("{}", x);
```

Historically, Rust kept the borrow alive until the end of scope, so these
examples might fail to compile with older compilers. Also, there are still some
corner cases where Rust fails to properly shorten the live part of the borrow
and fails to compile even when it looks like it should. These'll be solved over
time.


---

# Limits of Lifetimes

Given the following code:

```rust,compile_fail
#[derive(Debug)]
struct Foo;

impl Foo {
    fn mutate_and_share(&mut self) -> &Self { &*self }
    fn share(&self) {}
}

fn main() {
    let mut foo = Foo;
    let loan = foo.mutate_and_share();
    foo.share();
    println!("{:?}", loan);
}
```

One might expect it to compile. We call `mutate_and_share`, which mutably
borrows `foo` temporarily, but then returns only a shared reference. Therefore
we would expect `foo.share()` to succeed as `foo` shouldn't be mutably borrowed.

However when we try to compile it:

```text
error[E0502]: cannot borrow `foo` as immutable because it is also borrowed as mutable
  --> src/main.rs:12:5
   |
11 |     let loan = foo.mutate_and_share();
   |                --- mutable borrow occurs here
12 |     foo.share();
   |     ^^^ immutable borrow occurs here
13 |     println!("{:?}", loan);
```

What happened? Well, we got the exact same reasoning as we did for
[Example 2 in the previous section][ex2]. We desugar the program and we get
the following:

<!-- ignore: desugared code -->
```rust,ignore
struct Foo;

impl Foo {
    fn mutate_and_share<'a>(&'a mut self) -> &'a Self { &'a *self }
    fn share<'a>(&'a self) {}
}

fn main() {
    'b: {
        let mut foo: Foo = Foo;
        'c: {
            let loan: &'c Foo = Foo::mutate_and_share::<'c>(&'c mut foo);
            'd: {
                Foo::share::<'d>(&'d foo);
            }
            println!("{:?}", loan);
        }
    }
}
```

The lifetime system is forced to extend the `&mut foo` to have lifetime `'c`,
due to the lifetime of `loan` and `mutate_and_share`'s signature. Then when we
try to call `share`, it sees we're trying to alias that `&'c mut foo` and
blows up in our face!

This program is clearly correct according to the reference semantics we actually
care about, but the lifetime system is too coarse-grained to handle that.

## Improperly reduced borrows

The following code fails to compile, because Rust sees that a variable, `map`,
is borrowed twice, and can not infer that the first borrow ceases to be needed
before the second one occurs. This is caused by Rust conservatively falling back
to using a whole scope for the first borrow. This will eventually get fixed.

```rust,compile_fail
# use std::collections::HashMap;
# use std::hash::Hash;
fn get_default<'m, K, V>(map: &'m mut HashMap<K, V>, key: K) -> &'m mut V
where
    K: Clone + Eq + Hash,
    V: Default,
{
    match map.get_mut(&key) {
        Some(value) => value,
        None => {
            map.insert(key.clone(), V::default());
            map.get_mut(&key).unwrap()
        }
    }
}
```

Because of the lifetime restrictions imposed, `&mut map`'s lifetime
overlaps other mutable borrows, resulting in a compile error:

```text
error[E0499]: cannot borrow `*map` as mutable more than once at a time
  --> src/main.rs:12:13
   |
4  |   fn get_default<'m, K, V>(map: &'m mut HashMap<K, V>, key: K) -> &'m mut V
   |                  -- lifetime `'m` defined here
...
9  |       match map.get_mut(&key) {
   |       -     --- first mutable borrow occurs here
   |  _____|
   | |
10 | |         Some(value) => value,
11 | |         None => {
12 | |             map.insert(key.clone(), V::default());
   | |             ^^^ second mutable borrow occurs here
13 | |             map.get_mut(&key).unwrap()
14 | |         }
15 | |     }
   | |_____- returning this value requires that `*map` is borrowed for `'m`
```

[ex2]: lifetimes.html#example-aliasing-a-mutable-reference


---

# Lifetime Elision

In order to make common patterns more ergonomic, Rust allows lifetimes to be
*elided* in function signatures.

A *lifetime position* is anywhere you can write a lifetime in a type:

<!-- ignore: simplified code -->
```rust,ignore
&'a T
&'a mut T
T<'a>
```

Lifetime positions can appear as either "input" or "output":

* For `fn` definitions, `fn` types, and the traits `Fn`, `FnMut`, and `FnOnce`,
  input refers to the types of the formal arguments, while output refers to
  result types. So `fn foo(s: &str) -> (&str, &str)` has elided one lifetime in
  input position and two lifetimes in output position. Note that the input
  positions of a `fn` method definition do not include the lifetimes that occur
  in the method's `impl` header (nor lifetimes that occur in the trait header,
  for a default method).

* For `impl` headers, all types are input. So `impl Trait<&T> for Struct<&T>`
  has elided two lifetimes in input position, while `impl Struct<&T>` has elided
  one.

Elision rules are as follows:

* Each elided lifetime in input position becomes a distinct lifetime
  parameter.

* If there is exactly one input lifetime position (elided or not), that lifetime
  is assigned to *all* elided output lifetimes.

* If there are multiple input lifetime positions, but one of them is `&self` or
  `&mut self`, the lifetime of `self` is assigned to *all* elided output lifetimes.

* Otherwise, it is an error to elide an output lifetime.

Examples:

<!-- ignore: simplified code -->
```rust,ignore
fn print(s: &str);                                      // elided
fn print<'a>(s: &'a str);                               // expanded

fn debug(lvl: usize, s: &str);                          // elided
fn debug<'a>(lvl: usize, s: &'a str);                   // expanded

fn substr(s: &str, until: usize) -> &str;               // elided
fn substr<'a>(s: &'a str, until: usize) -> &'a str;     // expanded

fn get_str() -> &str;                                   // ILLEGAL

fn frob(s: &str, t: &str) -> &str;                      // ILLEGAL

fn get_mut(&mut self) -> &mut T;                        // elided
fn get_mut<'a>(&'a mut self) -> &'a mut T;              // expanded

fn args<T: ToCStr>(&mut self, args: &[T]) -> &mut Command                  // elided
fn args<'a, 'b, T: ToCStr>(&'a mut self, args: &'b [T]) -> &'a mut Command // expanded

fn new(buf: &mut [u8]) -> BufWriter;                    // elided
fn new(buf: &mut [u8]) -> BufWriter<'_>;                // elided (with `rust_2018_idioms`)
fn new<'a>(buf: &'a mut [u8]) -> BufWriter<'a>          // expanded
```


---

# Unbounded Lifetimes

Unsafe code can often end up producing references or lifetimes out of thin air.
Such lifetimes come into the world as *unbounded*. The most common source of
this is taking a reference to a dereferenced raw pointer, which produces a
reference with an unbounded lifetime. Such a lifetime becomes as big as context
demands. This is in fact more powerful than simply becoming `'static`, because
for instance `&'static &'a T` will fail to typecheck, but the unbound lifetime
will perfectly mold into `&'a &'a T` as needed. However for most intents and
purposes, such an unbounded lifetime can be regarded as `'static`.

Almost no reference is `'static`, so this is probably wrong. `transmute` and
`transmute_copy` are the two other primary offenders. One should endeavor to
bound an unbounded lifetime as quickly as possible, especially across function
boundaries.

Given a function, any output lifetimes that don't derive from inputs are
unbounded. For instance:

<!-- no_run: This example exhibits undefined behavior. -->
```rust,no_run
fn get_str<'a>(s: *const String) -> &'a str {
    unsafe { &*s }
}

fn main() {
    let soon_dropped = String::from("hello");
    let dangling = get_str(&soon_dropped);
    drop(soon_dropped);
    println!("Invalid str: {}", dangling); // Invalid str: gӚ_`
}
```

The easiest way to avoid unbounded lifetimes is to use lifetime elision at the
function boundary. If an output lifetime is elided, then it *must* be bounded by
an input lifetime. Of course it might be bounded by the *wrong* lifetime, but
this will usually just cause a compiler error, rather than allow memory safety
to be trivially violated.

Within a function, bounding lifetimes is more error-prone. The safest and easiest
way to bound a lifetime is to return it from a function with a bound lifetime.
However if this is unacceptable, the reference can be placed in a location with
a specific lifetime. Unfortunately it's impossible to name all lifetimes involved
in a function.


---

# Higher-Rank Trait Bounds (HRTBs)

Rust's `Fn` traits are a little bit magic. For instance, we can write the
following code:

```rust
struct Closure<F> {
    data: (u8, u16),
    func: F,
}

impl<F> Closure<F>
    where F: Fn(&(u8, u16)) -> &u8,
{
    fn call(&self) -> &u8 {
        (self.func)(&self.data)
    }
}

fn do_it(data: &(u8, u16)) -> &u8 { &data.0 }

fn main() {
    let clo = Closure { data: (0, 1), func: do_it };
    println!("{}", clo.call());
}
```

If we try to naively desugar this code in the same way that we did in the
[lifetimes section][lt], we run into some trouble:

<!-- ignore: desugared code -->
```rust,ignore
// NOTE: `&'b data.0` and `'x: {` is not valid syntax!
struct Closure<F> {
    data: (u8, u16),
    func: F,
}

impl<F> Closure<F>
    // where F: Fn(&'??? (u8, u16)) -> &'??? u8,
{
    fn call<'a>(&'a self) -> &'a u8 {
        (self.func)(&self.data)
    }
}

fn do_it<'b>(data: &'b (u8, u16)) -> &'b u8 { &'b data.0 }

fn main() {
    'x: {
        let clo = Closure { data: (0, 1), func: do_it };
        println!("{}", clo.call());
    }
}
```

How on earth are we supposed to express the lifetimes on `F`'s trait bound? We
need to provide some lifetime there, but the lifetime we care about can't be
named until we enter the body of `call`! Also, that isn't some fixed lifetime;
`call` works with *any* lifetime `&self` happens to have at that point.

This job requires The Magic of Higher-Rank Trait Bounds (HRTBs). The way we
desugar this is as follows:

<!-- ignore: simplified code -->
```rust,ignore
where for<'a> F: Fn(&'a (u8, u16)) -> &'a u8,
```

Alternatively:

<!-- ignore: simplified code -->
```rust,ignore
where F: for<'a> Fn(&'a (u8, u16)) -> &'a u8,
```

(Where `Fn(a, b, c) -> d` is itself just sugar for the unstable *real* `Fn`
trait)

`for<'a>` can be read as "for all choices of `'a`", and basically produces an
*infinite list* of trait bounds that F must satisfy. Intense. There aren't many
places outside of the `Fn` traits where we encounter HRTBs, and even for
those we have a nice magic sugar for the common cases.

In summary, we can rewrite the original code more explicitly as:

```rust
struct Closure<F> {
    data: (u8, u16),
    func: F,
}

impl<F> Closure<F>
    where for<'a> F: Fn(&'a (u8, u16)) -> &'a u8,
{
    fn call(&self) -> &u8 {
        (self.func)(&self.data)
    }
}

fn do_it(data: &(u8, u16)) -> &u8 { &data.0 }

fn main() {
    let clo = Closure { data: (0, 1), func: do_it };
    println!("{}", clo.call());
}
```

[lt]: lifetimes.html


---

# Subtyping and Variance

Rust uses lifetimes to track the relationships between borrows and ownership.
However, a naive implementation of lifetimes would be either too restrictive,
or permit undefined behavior.

In order to allow flexible usage of lifetimes
while also preventing their misuse, Rust uses **subtyping** and **variance**.

Let's start with an example.

```rust
// Note: debug expects two parameters with the *same* lifetime
fn debug<'a>(a: &'a str, b: &'a str) {
    println!("a = {a:?} b = {b:?}");
}

fn main() {
    let hello: &'static str = "hello";
    {
        let world = String::from("world");
        let world = &world; // 'world has a shorter lifetime than 'static
        debug(hello, world);
    }
}
```

In a conservative implementation of lifetimes, since `hello` and `world` have different lifetimes,
we might see the following error:

```text
error[E0308]: mismatched types
 --> src/main.rs:10:16
   |
10 |         debug(hello, world);
   |                      ^
   |                      |
   |                      expected `&'static str`, found struct `&'world str`
```

This would be rather unfortunate. In this case,
what we want is to accept any type that lives *at least as long* as `'world`.
Let's try using subtyping with our lifetimes.

## Subtyping

Subtyping is the idea that one type can be used in place of another.

Let's define that `Sub` is a subtype of `Super` (we'll be using the notation `Sub <: Super` throughout this chapter).

What this is suggesting to us is that the set of *requirements* that `Super` defines
are completely satisfied by `Sub`. `Sub` may then have more requirements.

Now, in order to use subtyping with lifetimes, we need to define the requirement of a lifetime:

> `'a` defines a region of code.

Now that we have a defined set of requirements for lifetimes, we can define how they relate to each other:

> `'long <: 'short` if and only if `'long` defines a region of code that **completely contains** `'short`.

`'long` may define a region larger than `'short`, but that still fits our definition.

> As we will see throughout the rest of this chapter,
subtyping is a lot more complicated and subtle than this,
but this simple rule is a very good 99% intuition.
And unless you write unsafe code, the compiler will automatically handle all the corner cases for you.

> But this is the Rustonomicon. We're writing unsafe code,
so we need to understand how this stuff really works, and how we can mess it up.

Going back to our example above, we can say that `'static <: 'world`.
For now, let's also accept the idea that subtypes of lifetimes can be passed through references
(more on this in [Variance](#variance)),
_e.g._ `&'static str` is a subtype of `&'world str`, then we can "downgrade" `&'static str` into a `&'world str`.
With that, the example above will compile:

```rust
fn debug<'a>(a: &'a str, b: &'a str) {
    println!("a = {a:?} b = {b:?}");
}

fn main() {
    let hello: &'static str = "hello";
    {
        let world = String::from("world");
        let world = &world; // 'world has a shorter lifetime than 'static
        debug(hello, world); // hello silently downgrades from `&'static str` into `&'world str`
    }
}
```

## Variance

Above, we glossed over the fact that `'static <: 'b` implied that `&'static T <: &'b T`. This uses a property known as _variance_.
It's not always as simple as this example, though. To understand that, let's try to extend this example a bit:

```rust,compile_fail,E0597
fn assign<T>(input: &mut T, val: T) {
    *input = val;
}

fn main() {
    let mut hello: &'static str = "hello";
    {
        let world = String::from("world");
        assign(&mut hello, &world);
    }
    println!("{hello}"); // use after free 😿
}
```

In `assign`, we are setting the `hello` reference to point to `world`.
But then `world` goes out of scope, before the later use of `hello` in the println!

This is a classic use-after-free bug!

Our first instinct might be to blame the `assign` impl, but there's really nothing wrong here.
It shouldn't be surprising that we might want to assign a `T` into a `T`.

The problem is that we cannot assume `&'static str` can still be downgraded into `&'world str` to satisfy `T`, once it's behind a `&mut` reference.
This means that `&mut &'static str` **cannot** be a *subtype* of `&mut &'world str`,
even if `'static` is a subtype of `'world`.

Variance is the concept that Rust borrows to define relationships about subtypes through their generic parameters.

> NOTE: For convenience we will define a generic type `F<T>` so
> that we can easily talk about `T`. Hopefully this is clear in context.

The type `F`'s *variance* is how the subtyping of its inputs affects the
subtyping of its outputs. There are three kinds of variance in Rust. Given two
types `Sub` and `Super`, where `Sub` is a subtype of `Super`:

* `F` is **covariant** if `F<Sub>` is a subtype of `F<Super>` (the subtype property is passed through)
* `F` is **contravariant** if `F<Super>` is a subtype of `F<Sub>` (the subtype property is "inverted")
* `F` is **invariant** otherwise (no subtyping relationship exists)

If we remember from the above examples,
it was ok for us to treat `&'a T` as a subtype of `&'b T` if `'a <: 'b`,
therefore we can say that `&'a T` is *covariant* over `'a`.

Also, we saw that it was not ok for us to treat `&mut &'a T` as a subtype of `&mut &'b T`,
therefore we can say that `&mut T` is *invariant* over `T`

Here is a table of some other generic types and their variances:

|                 |     'a    |         T         |     U     |
|-----------------|:---------:|:-----------------:|:---------:|
| `&'a T `        | covariant | covariant         |           |
| `&'a mut T`     | covariant | invariant         |           |
| `Box<T>`        |           | covariant         |           |
| `Vec<T>`        |           | covariant         |           |
| `UnsafeCell<T>` |           | invariant         |           |
| `Cell<T>`       |           | invariant         |           |
| `fn(T) -> U`    |           | **contra**variant | covariant |
| `*const T`      |           | covariant         |           |
| `*mut T`        |           | invariant         |           |

Some of these can be explained simply in relation to the others:

* `Vec<T>` and all other owning pointers and collections follow the same logic as `Box<T>`
* `Cell<T>` and all other interior mutability types follow the same logic as `UnsafeCell<T>`
* `UnsafeCell<T>` having interior mutability gives it the same variance properties as `&mut T`
* `*const T` follows the logic of `&T`
* `*mut T` follows the logic of `&mut T` (or `UnsafeCell<T>`)

For more types, see the ["Variance" section][variance-table] on the reference.

[variance-table]: ../reference/subtyping.html#variance

> NOTE: the *only* source of contravariance in the language is the arguments to
> a function, which is why it really doesn't come up much in practice. Invoking
> contravariance involves higher-order programming with function pointers that
> take references with specific lifetimes (as opposed to the usual "any lifetime",
> which gets into higher rank lifetimes, which work independently of subtyping).

Now that we have some more formal understanding of variance,
let's go through some more examples in more detail.

```rust,compile_fail,E0597
fn assign<T>(input: &mut T, val: T) {
    *input = val;
}

fn main() {
    let mut hello: &'static str = "hello";
    {
        let world = String::from("world");
        assign(&mut hello, &world);
    }
    println!("{hello}");
}
```

And what do we get when we run this?

```text
error[E0597]: `world` does not live long enough
  --> src/main.rs:9:28
   |
6  |     let mut hello: &'static str = "hello";
   |                    ------------ type annotation requires that `world` is borrowed for `'static`
...
9  |         assign(&mut hello, &world);
   |                            ^^^^^^ borrowed value does not live long enough
10 |     }
   |     - `world` dropped here while still borrowed
```

Good, it doesn't compile! Let's break down what's happening here in detail.

First let's look at the `assign` function:

```rust
fn assign<T>(input: &mut T, val: T) {
    *input = val;
}
```

All it does is take a mutable reference and a value and overwrite the referent with it.
What's important about this function is that it creates a type equality constraint. It
clearly says in its signature the referent and the value must be the *exact same* type.

Meanwhile, in the caller we pass in `&mut &'static str` and `&'world str`.

Because `&mut T` is invariant over `T`, the compiler concludes it can't apply any subtyping
to the first argument, and so `T` must be exactly `&'static str`.

This is counter to the `&T` case:

```rust
fn debug<T: std::fmt::Debug>(a: T, b: T) {
    println!("a = {a:?} b = {b:?}");
}
```

where similarly `a` and `b` must have the same type `T`.
But since `&'a T` *is* covariant over `'a`, we are allowed to perform subtyping.
So the compiler decides that `&'static str` can become `&'b str` if and only if
`&'static str` is a subtype of `&'b str`, which will hold if `'static <: 'b`.
This is true, so the compiler is happy to continue compiling this code.

As it turns out, the argument for why it's ok for Box (and Vec, HashMap, etc.) to be covariant is pretty similar to the argument for why it's ok for lifetimes to be covariant: as soon as you try to stuff them in something like a mutable reference, they inherit invariance and you're prevented from doing anything bad.

However Box makes it easier to focus on the by-value aspect of references that we partially glossed over.

Unlike a lot of languages which allow values to be freely aliased at all times, Rust has a very strict rule: if you're allowed to mutate or move a value, you are guaranteed to be the only one with access to it.

Consider the following code:

```rust,ignore
let hello: Box<&'static str> = Box::new("hello");

let mut world: Box<&'b str>;
world = hello;
```

There is no problem at all with the fact that we have forgotten that `hello` was alive for `'static`,
because as soon as we moved `hello` to a variable that only knew it was alive for `'b`,
**we destroyed the only thing in the universe that remembered it lived for longer**!

Only one thing left to explain: function pointers.

To see why `fn(T) -> U` should be covariant over `U`, consider the following signature:

<!-- ignore: simplified code -->
```rust,ignore
fn get_str() -> &'a str;
```

This function claims to produce a `str` bound by some lifetime `'a`. As such, it is perfectly valid to
provide a function with the following signature instead:

<!-- ignore: simplified code -->
```rust,ignore
fn get_static() -> &'static str;
```

So when the function is called, all its caller is expecting is a `&str` which lives at least the lifetime of `'a`,
it doesn't matter if the value actually lives longer.

However, the same logic does not apply to *arguments*. Consider trying to satisfy:

<!-- ignore: simplified code -->
```rust,ignore
fn store_ref(&'a str);
```

with:

<!-- ignore: simplified code -->
```rust,ignore
fn store_static(&'static str);
```

The first function can accept any string reference as long as it lives at least for `'a`,
but the second cannot accept a string reference that lives for any duration less than `'static`,
which would cause a conflict.
Covariance doesn't work here. But if we flip it around, it actually *does*
work! If we need a function that can handle `&'static str`, a function that can handle *any* reference lifetime
will surely work fine.

Let's see this in practice

```rust,compile_fail
# use std::cell::RefCell;
thread_local! {
    pub static StaticVecs: RefCell<Vec<&'static str>> = RefCell::new(Vec::new());
}

/// saves the input given into a thread local `Vec<&'static str>`
fn store(input: &'static str) {
    StaticVecs.with_borrow_mut(|v| v.push(input));
}

/// Calls the function with it's input (must have the same lifetime!)
fn demo<'a>(input: &'a str, f: fn(&'a str)) {
    f(input);
}

fn main() {
    demo("hello", store); // "hello" is 'static. Can call `store` fine

    {
        let smuggle = String::from("smuggle");

        // `&smuggle` is not static. If we were to call `store` with `&smuggle`,
        // we would have pushed an invalid lifetime into the `StaticVecs`.
        // Therefore, `fn(&'static str)` cannot be a subtype of `fn(&'a str)`
        demo(&smuggle, store);
    }

    // use after free 😿
    StaticVecs.with_borrow(|v| println!("{v:?}"));
}
```

And that's why function types, unlike anything else in the language, are
**contra**variant over their arguments.

Now, this is all well and good for the types the standard library provides, but
how is variance determined for types that *you* define? A struct, informally
speaking, inherits the variance of its fields. If a struct `MyType`
has a generic argument `A` that is used in a field `a`, then MyType's variance
over `A` is exactly `a`'s variance over `A`.

However if `A` is used in multiple fields:

* If all uses of `A` are covariant, then MyType is covariant over `A`
* If all uses of `A` are contravariant, then MyType is contravariant over `A`
* Otherwise, MyType is invariant over `A`

```rust
use std::cell::Cell;

struct MyType<'a, 'b, A: 'a, B: 'b, C, D, E, F, G, H, In, Out, Mixed> {
    a: &'a A,     // covariant over 'a and A
    b: &'b mut B, // covariant over 'b and invariant over B

    c: *const C,  // covariant over C
    d: *mut D,    // invariant over D

    e: E,         // covariant over E
    f: Vec<F>,    // covariant over F
    g: Cell<G>,   // invariant over G

    h1: H,        // would also be covariant over H except...
    h2: Cell<H>,  // invariant over H, because invariance wins all conflicts

    i: fn(In) -> Out,       // contravariant over In, covariant over Out

    k1: fn(Mixed) -> usize, // would be contravariant over Mixed except..
    k2: Mixed,              // invariant over Mixed, because invariance wins all conflicts
}
```


---

# Drop Check

We have seen how lifetimes provide us some fairly simple rules for ensuring
that we never read dangling references. However up to this point we have only ever
interacted with the _outlives_ relationship in an inclusive manner. That is,
when we talked about `'a: 'b`, it was ok for `'a` to live _exactly_ as long as
`'b`. At first glance, this seems to be a meaningless distinction. Nothing ever
gets dropped at the same time as another, right? This is why we used the
following desugaring of `let` statements:

<!-- ignore: simplified code -->
```rust,ignore
let x;
let y;
```

desugaring to:

<!-- ignore: desugared code -->
```rust,ignore
{
    let x;
    {
        let y;
    }
}
```

There are some more complex situations which are not possible to desugar using
scopes, but the order is still defined ‒ variables are dropped in the reverse
order of their definition, fields of structs and tuples in order of their
definition. There are some more details about order of drop in [RFC 1857][rfc1857].

Let's do this:

<!-- ignore: simplified code -->
```rust,ignore
let tuple = (vec![], vec![]);
```

The left vector is dropped first. But does it mean the right one strictly
outlives it in the eyes of the borrow checker? The answer to this question is
_no_. The borrow checker could track fields of tuples separately, but it would
still be unable to decide what outlives what in case of vector elements, which
are dropped manually via pure-library code the borrow checker doesn't
understand.

So why do we care? We care because if the type system isn't careful, it could
accidentally make dangling pointers. Consider the following simple program:

```rust
struct Inspector<'a>(&'a u8);

struct World<'a> {
    inspector: Option<Inspector<'a>>,
    days: Box<u8>,
}

fn main() {
    let mut world = World {
        inspector: None,
        days: Box::new(1),
    };
    world.inspector = Some(Inspector(&world.days));
}
```

This program is totally sound and compiles today. The fact that `days` does not
strictly outlive `inspector` doesn't matter. As long as the `inspector` is
alive, so is `days`.

However if we add a destructor, the program will no longer compile!

```rust,compile_fail
struct Inspector<'a>(&'a u8);

impl<'a> Drop for Inspector<'a> {
    fn drop(&mut self) {
        println!("I was only {} days from retirement!", self.0);
    }
}

struct World<'a> {
    inspector: Option<Inspector<'a>>,
    days: Box<u8>,
}

fn main() {
    let mut world = World {
        inspector: None,
        days: Box::new(1),
    };
    world.inspector = Some(Inspector(&world.days));
    // Let's say `days` happens to get dropped first.
    // Then when Inspector is dropped, it will try to read free'd memory!
}
```

```text
error[E0597]: `world.days` does not live long enough
  --> src/main.rs:19:38
   |
19 |     world.inspector = Some(Inspector(&world.days));
   |                                      ^^^^^^^^^^^ borrowed value does not live long enough
...
22 | }
   | -
   | |
   | `world.days` dropped here while still borrowed
   | borrow might be used here, when `world` is dropped and runs the destructor for type `World<'_>`
```

You can try changing the order of fields or use a tuple instead of the struct,
it'll still not compile.

Implementing `Drop` lets the `Inspector` execute some arbitrary code during its
death. This means it can potentially observe that types that are supposed to
live as long as it does actually were destroyed first.

Interestingly, only generic types need to worry about this. If they aren't
generic, then the only lifetimes they can harbor are `'static`, which will truly
live _forever_. This is why this problem is referred to as _sound generic drop_.
Sound generic drop is enforced by the _drop checker_. As of this writing, some
of the finer details of how the drop checker (also called dropck) validates
types is totally up in the air. However The Big Rule is the subtlety that we
have focused on this whole section:

**For a generic type to soundly implement drop, its generics arguments must
strictly outlive it.**

Obeying this rule is (usually) necessary to satisfy the borrow
checker; obeying it is sufficient but not necessary to be
sound. That is, if your type obeys this rule then it's definitely
sound to drop.

The reason that it is not always necessary to satisfy the above rule
is that some Drop implementations will not access borrowed data even
though their type gives them the capability for such access, or because we know
the specific drop order and the borrowed data is still fine even if the borrow
checker doesn't know that.

For example, this variant of the above `Inspector` example will never
access borrowed data:

```rust,compile_fail
struct Inspector<'a>(&'a u8, &'static str);

impl<'a> Drop for Inspector<'a> {
    fn drop(&mut self) {
        println!("Inspector(_, {}) knows when *not* to inspect.", self.1);
    }
}

struct World<'a> {
    inspector: Option<Inspector<'a>>,
    days: Box<u8>,
}

fn main() {
    let mut world = World {
        inspector: None,
        days: Box::new(1),
    };
    world.inspector = Some(Inspector(&world.days, "gadget"));
    // Let's say `days` happens to get dropped first.
    // Even when Inspector is dropped, its destructor will not access the
    // borrowed `days`.
}
```

Likewise, this variant will also never access borrowed data:

```rust,compile_fail
struct Inspector<T>(T, &'static str);

impl<T> Drop for Inspector<T> {
    fn drop(&mut self) {
        println!("Inspector(_, {}) knows when *not* to inspect.", self.1);
    }
}

struct World<T> {
    inspector: Option<Inspector<T>>,
    days: Box<u8>,
}

fn main() {
    let mut world = World {
        inspector: None,
        days: Box::new(1),
    };
    world.inspector = Some(Inspector(&world.days, "gadget"));
    // Let's say `days` happens to get dropped first.
    // Even when Inspector is dropped, its destructor will not access the
    // borrowed `days`.
}
```

However, _both_ of the above variants are rejected by the borrow
checker during the analysis of `fn main`, saying that `days` does not
live long enough.

The reason is that the borrow checking analysis of `main` does not
know about the internals of each `Inspector`'s `Drop` implementation. As
far as the borrow checker knows while it is analyzing `main`, the body
of an inspector's destructor might access that borrowed data.

Therefore, the drop checker forces all borrowed data in a value to
strictly outlive that value.

## An Escape Hatch

The precise rules that govern drop checking may be less restrictive in
the future.

The current analysis is deliberately conservative; it forces all
borrowed data in a value to outlive that value, which is certainly sound.

Future versions of the language may make the analysis more precise, to
reduce the number of cases where sound code is rejected as unsafe.
This would help address cases such as the two `Inspector`s above that
know not to inspect during destruction.

In the meantime, there is an unstable attribute that one can use to
assert (unsafely) that a generic type's destructor is _guaranteed_ to
not access any expired data, even if its type gives it the capability
to do so.

That attribute is called `may_dangle` and was introduced in [RFC 1327][rfc1327].
To deploy it on the `Inspector` from above, we would write:

```rust
#![feature(dropck_eyepatch)]

struct Inspector<'a>(&'a u8, &'static str);

unsafe impl<#[may_dangle] 'a> Drop for Inspector<'a> {
    fn drop(&mut self) {
        println!("Inspector(_, {}) knows when *not* to inspect.", self.1);
    }
}

struct World<'a> {
    days: Box<u8>,
    inspector: Option<Inspector<'a>>,
}

fn main() {
    let mut world = World {
        inspector: None,
        days: Box::new(1),
    };
    world.inspector = Some(Inspector(&world.days, "gadget"));
}
```

Use of this attribute requires the `Drop` impl to be marked `unsafe` because the
compiler is not checking the implicit assertion that no potentially expired data
(e.g. `self.0` above) is accessed.

The attribute can be applied to any number of lifetime and type parameters. In
the following example, we assert that we access no data behind a reference of
lifetime `'b` and that the only uses of `T` will be moves or drops, but omit
the attribute from `'a` and `U`, because we do access data with that lifetime
and that type:

```rust
#![feature(dropck_eyepatch)]
use std::fmt::Display;

struct Inspector<'a, 'b, T, U: Display>(&'a u8, &'b u8, T, U);

unsafe impl<'a, #[may_dangle] 'b, #[may_dangle] T, U: Display> Drop for Inspector<'a, 'b, T, U> {
    fn drop(&mut self) {
        println!("Inspector({}, _, _, {})", self.0, self.3);
    }
}
```

It is sometimes obvious that no such access can occur, like the case above.
However, when dealing with a generic type parameter, such access can
occur indirectly. Examples of such indirect access are:

- invoking a callback,
- via a trait method call.

(Future changes to the language, such as impl specialization, may add
other avenues for such indirect access.)

Here is an example of invoking a callback:

```rust
struct Inspector<T>(T, &'static str, Box<for <'r> fn(&'r T) -> String>);

impl<T> Drop for Inspector<T> {
    fn drop(&mut self) {
        // The `self.2` call could access a borrow e.g. if `T` is `&'a _`.
        println!("Inspector({}, {}) unwittingly inspects expired data.",
                 (self.2)(&self.0), self.1);
    }
}
```

Here is an example of a trait method call:

```rust
use std::fmt;

struct Inspector<T: fmt::Display>(T, &'static str);

impl<T: fmt::Display> Drop for Inspector<T> {
    fn drop(&mut self) {
        // There is a hidden call to `<T as Display>::fmt` below, which
        // could access a borrow e.g. if `T` is `&'a _`
        println!("Inspector({}, {}) unwittingly inspects expired data.",
                 self.0, self.1);
    }
}
```

And of course, all of these accesses could be further hidden within
some other method invoked by the destructor, rather than being written
directly within it.

In all of the above cases where the `&'a u8` is accessed in the
destructor, adding the `#[may_dangle]`
attribute makes the type vulnerable to misuse that the borrow
checker will not catch, inviting havoc. It is better to avoid adding
the attribute.

## A related side note about drop order

While the drop order of fields inside a struct is defined, relying on it is
fragile and subtle. When the order matters, it is better to use the
[`ManuallyDrop`] wrapper.

## Is that all about drop checker?

It turns out that when writing unsafe code, we generally don't need to
worry at all about doing the right thing for the drop checker. However there
is one special case that you need to worry about, which we will look at in
the next section.

[rfc1327]: https://github.com/rust-lang/rfcs/blob/master/text/1327-dropck-param-eyepatch.md
[rfc1857]: https://github.com/rust-lang/rfcs/blob/master/text/1857-stabilize-drop-order.md
[`manuallydrop`]: ../std/mem/struct.ManuallyDrop.html


---

# PhantomData

When working with unsafe code, we can often end up in a situation where
types or lifetimes are logically associated with a struct, but not actually
part of a field. This most commonly occurs with lifetimes. For instance, the
`Iter` for `&'a [T]` is (approximately) defined as follows:

```rust,compile_fail
struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
}
```

However because `'a` is unused within the struct's body, it's *unbounded*.
[Because of the troubles this has historically caused][unused-param],
unbounded lifetimes and types are *forbidden* in struct definitions.
Therefore we must somehow refer to these types in the body.
Correctly doing this is necessary to have correct variance and drop checking.

[unused-param]: https://rust-lang.github.io/rfcs/0738-variance.html#the-corner-case-unused-parameters-and-parameters-that-are-only-used-unsafely

We do this using `PhantomData`, which is a special marker type. `PhantomData`
consumes no space, but simulates a field of the given type for the purpose of
static analysis. This was deemed to be less error-prone than explicitly telling
the type-system the kind of variance that you want, while also providing other
useful things such as auto traits and the information needed by drop check.

Iter logically contains a bunch of `&'a T`s, so this is exactly what we tell
the `PhantomData` to simulate:

```rust
use std::marker;

struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
    _marker: marker::PhantomData<&'a T>,
}
```

and that's it. The lifetime will be bounded, and your iterator will be covariant
over `'a` and `T`. Everything Just Works.

## Generic parameters and drop-checking

In the past, there used to be another thing to take into consideration.

This very documentation used to say:

> Another important example is Vec, which is (approximately) defined as follows:
>
> ```rust
> struct Vec<T> {
>     data: *const T, // *const for variance!
>     len: usize,
>     cap: usize,
> }
> ```
>
> Unlike the previous example, it *appears* that everything is exactly as we
> want. Every generic argument to Vec shows up in at least one field.
> Good to go!
>
> Nope.
>
> The drop checker will generously determine that `Vec<T>` does not own any values
> of type T. This will in turn make it conclude that it doesn't need to worry
> about Vec dropping any T's in its destructor for determining drop check
> soundness. This will in turn allow people to create unsoundness using
> Vec's destructor.
>
> In order to tell the drop checker that we *do* own values of type T, and
> therefore may drop some T's when *we* drop, we must add an extra `PhantomData`
> saying exactly that:
>
> ```rust
> use std::marker;
>
> struct Vec<T> {
>     data: *const T, // *const for variance!
>     len: usize,
>     cap: usize,
>     _owns_T: marker::PhantomData<T>,
> }
> ```

But ever since [RFC 1238](https://rust-lang.github.io/rfcs/1238-nonparametric-dropck.html),
**this is no longer true nor necessary**.

If you were to write:

```rust
struct Vec<T> {
    data: *const T, // `*const` for variance!
    len: usize,
    cap: usize,
}

# #[cfg(any())]
impl<T> Drop for Vec<T> { /* … */ }
```

then the existence of that `impl<T> Drop for Vec<T>` makes it so Rust will consider
that that `Vec<T>` _owns_ values of type `T` (more precisely: may use values of type `T`
in its `Drop` implementation), and Rust will thus not allow them to _dangle_ should a
`Vec<T>` be dropped.

When a type already has a `Drop impl`, **adding an extra `_owns_T: PhantomData<T>` field
is thus _superfluous_ and accomplishes nothing**, dropck-wise (it still affects variance
and auto-traits).

  - (advanced edge case: if the type containing the `PhantomData` has no `Drop` impl at all,
    but still has drop glue (by having _another_ field with drop glue), then the
    dropck/`#[may_dangle]` considerations mentioned herein do apply as well: a `PhantomData<T>`
    field will then require `T` to be droppable whenever the containing type goes out of scope).

___

But this situation can sometimes lead to overly restrictive code. That's why the
standard library uses an unstable and `unsafe` attribute to opt back into the old
"unchecked" drop-checking behavior, that this very documentation warned about: the
`#[may_dangle]` attribute.

### An exception: the special case of the standard library and its unstable `#[may_dangle]`

This section can be skipped if you are only writing your own library code; but if you are
curious about what the standard library does with the actual `Vec` definition, you'll notice
that it still needs to use a `_owns_T: PhantomData<T>` field for soundness.

<details><summary>Click here to see why</summary>

Consider the following example:

```rust
fn main() {
    let mut v: Vec<&str> = Vec::new();
    let s: String = "Short-lived".into();
    v.push(&s);
    drop(s);
} // <- `v` is dropped here
```

with a classical `impl<T> Drop for Vec<T> {` definition, the above [is denied].

[is denied]: https://rust.godbolt.org/z/ans15Kqz3

Indeed, in this case we have a `Vec</* T = */ &'s str>` vector of `'s`-lived references
to `str`ings, but in the case of `let s: String`, it is dropped before the `Vec` is, and
thus `'s` **is expired** by the time the `Vec` is dropped, and the
`impl<'s> Drop for Vec<&'s str> {` is used.

This means that if such `Drop` were to be used, it would be dealing with an _expired_, or
_dangling_ lifetime `'s`. But this is contrary to Rust principles, where by default all
Rust references involved in a function signature are non-dangling and valid to dereference.

Hence why Rust has to conservatively deny this snippet.

And yet, in the case of the real `Vec`, the `Drop` impl does not care about `&'s str`,
_since it has no drop glue of its own_: it only wants to deallocate the backing buffer.

In other words, it would be nice if the above snippet was somehow accepted, by special
casing `Vec`, or by relying on some special property of `Vec`: `Vec` could try to
_promise not to use the `&'s str`s it holds when being dropped_.

This is the kind of `unsafe` promise that can be expressed with `#[may_dangle]`:

```rust ,ignore
unsafe impl<#[may_dangle] 's> Drop for Vec<&'s str> { /* … */ }
```

or, more generally:

```rust ,ignore
unsafe impl<#[may_dangle] T> Drop for Vec<T> { /* … */ }
```

is the `unsafe` way to opt out of this conservative assumption that Rust's drop
checker makes about type parameters of a dropped instance not being allowed to dangle.

And when this is done, such as in the standard library, we need to be careful in the
case where `T` has drop glue of its own. In this instance, imagine replacing the
`&'s str`s with a `struct PrintOnDrop<'s> /* = */ (&'s str);` which would have a
`Drop` impl wherein the inner `&'s str` would be dereferenced and printed to the screen.

Indeed, `Drop for Vec<T> {`, before deallocating the backing buffer, does have to transitively
drop each `T` item when it has drop glue; in the case of `PrintOnDrop<'s>`, it means that
`Drop for Vec<PrintOnDrop<'s>>` has to transitively drop the `PrintOnDrop<'s>`s elements before
deallocating the backing buffer.

So when we said that `'s` `#[may_dangle]`, it was an excessively loose statement. We'd rather want
to say: "`'s` may dangle provided it not be involved in some transitive drop glue". Or, more generally,
"`T` may dangle provided it not be involved in some transitive drop glue". This "exception to the
exception" is a pervasive situation whenever **we own a `T`**. That's why Rust's `#[may_dangle]` is
smart enough to know of this opt-out, and will thus be disabled _when the generic parameter is held
in an owned fashion_ by the fields of the struct.

Hence why the standard library ends up with:

```rust
# #[cfg(any())]
// we pinky-swear not to use `T` when dropping a `Vec`…
unsafe impl<#[may_dangle] T> Drop for Vec<T> {
    fn drop(&mut self) {
        unsafe {
            if mem::needs_drop::<T>() {
                /* … except here, that is, … */
                ptr::drop_in_place::<[T]>(/* … */);
            }
            // …
            dealloc(/* … */)
            // …
        }
    }
}

struct Vec<T> {
    // … except for the fact that a `Vec` owns `T` items and
    // may thus be dropping `T` items on drop!
    _owns_T: core::marker::PhantomData<T>,

    ptr: *const T, // `*const` for variance (but this does not express ownership of a `T` *per se*)
    len: usize,
    cap: usize,
}
```

</details>

___

Raw pointers that own an allocation is such a pervasive pattern that the
standard library made a utility for itself called `Unique<T>` which:

* wraps a `*const T` for variance
* includes a `PhantomData<T>`
* auto-derives `Send`/`Sync` as if T was contained
* marks the pointer as `NonZero` for the null-pointer optimization

## Table of `PhantomData` patterns

Here’s a table of all the wonderful ways `PhantomData` could be used:

| Phantom type                | variance of `'a` | variance of `T`   | `Send`/`Sync`<br/>(or lack thereof)       | dangling `'a` or `T` in drop glue<br/>(_e.g._, `#[may_dangle] Drop`) |
|-----------------------------|:----------------:|:-----------------:|:-----------------------------------------:|:------------------------------------------------:|
| `PhantomData<T>`            | -                | **cov**ariant     | inherited                                 | disallowed ("owns `T`")                          |
| `PhantomData<&'a T>`        | **cov**ariant    | **cov**ariant     | `Send + Sync`<br/>requires<br/>`T : Sync` | allowed                                          |
| `PhantomData<&'a mut T>`    | **cov**ariant    | **inv**ariant     | inherited                                 | allowed                                          |
| `PhantomData<*const T>`     | -                | **cov**ariant     | `!Send + !Sync`                           | allowed                                          |
| `PhantomData<*mut T>`       | -                | **inv**ariant     | `!Send + !Sync`                           | allowed                                          |
| `PhantomData<fn(T)>`        | -                | **contra**variant | `Send + Sync`                             | allowed                                          |
| `PhantomData<fn() -> T>`    | -                | **cov**ariant     | `Send + Sync`                             | allowed                                          |
| `PhantomData<fn(T) -> T>`   | -                | **inv**ariant     | `Send + Sync`                             | allowed                                          |
| `PhantomData<Cell<&'a ()>>` | **inv**ariant    | -                 | `Send + !Sync`                            | allowed                                          |

  - Note: opting out of the `Unpin` auto-trait requires the dedicated [`PhantomPinned`] type instead.

[`PhantomPinned`]: ../core/marker/struct.PhantomPinned.html


---

# Splitting Borrows

The mutual exclusion property of mutable references can be very limiting when
working with a composite structure. The borrow checker (a.k.a. borrowck)
understands some basic stuff, but will fall over pretty easily. It does
understand structs sufficiently to know that it's possible to borrow disjoint
fields of a struct simultaneously. So this works today:

```rust
struct Foo {
    a: i32,
    b: i32,
    c: i32,
}

let mut x = Foo {a: 0, b: 0, c: 0};
let a = &mut x.a;
let b = &mut x.b;
let c = &x.c;
*b += 1;
let c2 = &x.c;
*a += 10;
println!("{} {} {} {}", a, b, c, c2);
```

However borrowck doesn't understand arrays or slices in any way, so this doesn't
work:

```rust,compile_fail
let mut x = [1, 2, 3];
let a = &mut x[0];
let b = &mut x[1];
println!("{} {}", a, b);
```

```text
error[E0499]: cannot borrow `x[..]` as mutable more than once at a time
 --> src/lib.rs:4:18
  |
3 |     let a = &mut x[0];
  |                  ---- first mutable borrow occurs here
4 |     let b = &mut x[1];
  |                  ^^^^ second mutable borrow occurs here
5 |     println!("{} {}", a, b);
6 | }
  | - first borrow ends here

error: aborting due to previous error
```

While it was plausible that borrowck could understand this simple case, it's
pretty clearly hopeless for borrowck to understand disjointness in general
container types like a tree, especially if distinct keys actually *do* map
to the same value.

In order to "teach" borrowck that what we're doing is ok, we need to drop down
to unsafe code. For instance, mutable slices expose a `split_at_mut` function
that consumes the slice and returns two mutable slices. One for everything to
the left of the index, and one for everything to the right. Intuitively we know
this is safe because the slices don't overlap, and therefore alias. However
the implementation requires some unsafety:

```rust
# use std::slice::from_raw_parts_mut;
# struct FakeSlice<T>(T);
# impl<T> FakeSlice<T> {
# fn len(&self) -> usize { unimplemented!() }
# fn as_mut_ptr(&mut self) -> *mut T { unimplemented!() }
pub fn split_at_mut(&mut self, mid: usize) -> (&mut [T], &mut [T]) {
    let len = self.len();
    let ptr = self.as_mut_ptr();

    unsafe {
        assert!(mid <= len);

        (from_raw_parts_mut(ptr, mid),
         from_raw_parts_mut(ptr.add(mid), len - mid))
    }
}
# }
```

This is actually a bit subtle. So as to avoid ever making two `&mut`'s to the
same value, we explicitly construct brand-new slices through raw pointers.

However more subtle is how iterators that yield mutable references work.
The iterator trait is defined as follows:

```rust
trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Given this definition, Self::Item has *no* connection to `self`. This means that
we can call `next` several times in a row, and hold onto all the results
*concurrently*. This is perfectly fine for by-value iterators, which have
exactly these semantics. It's also actually fine for shared references, as they
admit arbitrarily many references to the same thing (although the iterator needs
to be a separate object from the thing being shared).

But mutable references make this a mess. At first glance, they might seem
completely incompatible with this API, as it would produce multiple mutable
references to the same object!

However it actually *does* work, exactly because iterators are one-shot objects.
Everything an IterMut yields will be yielded at most once, so we don't
actually ever yield multiple mutable references to the same piece of data.

Perhaps surprisingly, mutable iterators don't require unsafe code to be
implemented for many types!

For instance here's a singly linked list:

```rust
# fn main() {}
type Link<T> = Option<Box<Node<T>>>;

struct Node<T> {
    elem: T,
    next: Link<T>,
}

pub struct LinkedList<T> {
    head: Link<T>,
}

pub struct IterMut<'a, T: 'a>(Option<&'a mut Node<T>>);

impl<T> LinkedList<T> {
    fn iter_mut(&mut self) -> IterMut<T> {
        IterMut(self.head.as_mut().map(|node| &mut **node))
    }
}

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;

    fn next(&mut self) -> Option<Self::Item> {
        self.0.take().map(|node| {
            self.0 = node.next.as_mut().map(|node| &mut **node);
            &mut node.elem
        })
    }
}
```

Here's a mutable slice:

```rust
# fn main() {}
use std::mem;

pub struct IterMut<'a, T: 'a>(&'a mut[T]);

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;

    fn next(&mut self) -> Option<Self::Item> {
        let slice = mem::take(&mut self.0);
        if slice.is_empty() { return None; }

        let (l, r) = slice.split_at_mut(1);
        self.0 = r;
        l.get_mut(0)
    }
}

impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        let slice = mem::take(&mut self.0);
        if slice.is_empty() { return None; }

        let new_len = slice.len() - 1;
        let (l, r) = slice.split_at_mut(new_len);
        self.0 = l;
        r.get_mut(0)
    }
}
```

And here's a binary tree:

```rust
# fn main() {}
use std::collections::VecDeque;

type Link<T> = Option<Box<Node<T>>>;

struct Node<T> {
    elem: T,
    left: Link<T>,
    right: Link<T>,
}

pub struct Tree<T> {
    root: Link<T>,
}

struct NodeIterMut<'a, T: 'a> {
    elem: Option<&'a mut T>,
    left: Option<&'a mut Node<T>>,
    right: Option<&'a mut Node<T>>,
}

enum State<'a, T: 'a> {
    Elem(&'a mut T),
    Node(&'a mut Node<T>),
}

pub struct IterMut<'a, T: 'a>(VecDeque<NodeIterMut<'a, T>>);

impl<T> Tree<T> {
    pub fn iter_mut(&mut self) -> IterMut<T> {
        let mut deque = VecDeque::new();
        if let Some(root) = self.root.as_mut() {
            deque.push_front(root.iter_mut());
        }
        IterMut(deque)
    }
}

impl<T> Node<T> {
    pub fn iter_mut(&mut self) -> NodeIterMut<T> {
        NodeIterMut {
            elem: Some(&mut self.elem),
            left: self.left.as_deref_mut(),
            right: self.right.as_deref_mut(),
        }
    }
}

impl<'a, T> Iterator for NodeIterMut<'a, T> {
    type Item = State<'a, T>;

    fn next(&mut self) -> Option<Self::Item> {
        self.left.take().map(State::Node).or_else(|| {
            self.elem
                .take()
                .map(State::Elem)
                .or_else(|| self.right.take().map(State::Node))
        })
    }
}

impl<'a, T> DoubleEndedIterator for NodeIterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        self.right.take().map(State::Node).or_else(|| {
            self.elem
                .take()
                .map(State::Elem)
                .or_else(|| self.left.take().map(State::Node))
        })
    }
}

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;
    fn next(&mut self) -> Option<Self::Item> {
        loop {
            match self.0.front_mut().and_then(Iterator::next) {
                Some(State::Elem(elem)) => return Some(elem),
                Some(State::Node(node)) => self.0.push_front(node.iter_mut()),
                None => {
                    self.0.pop_front()?;
                }
            }
        }
    }
}

impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        loop {
            match self.0.back_mut().and_then(DoubleEndedIterator::next_back) {
                Some(State::Elem(elem)) => return Some(elem),
                Some(State::Node(node)) => self.0.push_back(node.iter_mut()),
                None => {
                    self.0.pop_back()?;
                }
            }
        }
    }
}
```

All of these are completely safe and work on stable Rust! This ultimately
falls out of the simple struct case we saw before: Rust understands that you
can safely split a mutable reference into subfields. We can then encode
permanently consuming a reference via Options (or in the case of slices,
replacing with an empty slice).
