# Type Conversions

At the end of the day, everything is just a pile of bits somewhere, and type
systems are just there to help us use those bits right. There are two common
problems with typing bits: needing to reinterpret those exact bits as a
different type, and needing to change the bits to have equivalent meaning for
a different type. Because Rust encourages encoding important properties in the
type system, these problems are incredibly pervasive. As such, Rust
consequently gives you several ways to solve them.

First we'll look at the ways that Safe Rust gives you to reinterpret values.
The most trivial way to do this is to just destructure a value into its
constituent parts and then build a new type out of them. e.g.

```rust
struct Foo {
    x: u32,
    y: u16,
}

struct Bar {
    a: u32,
    b: u16,
}

fn reinterpret(foo: Foo) -> Bar {
    let Foo { x, y } = foo;
    Bar { a: x, b: y }
}
```

But this is, at best, annoying. For common conversions, Rust provides
more ergonomic alternatives.


---

# Coercions

Types can implicitly be coerced to change in certain contexts.
These changes are generally just *weakening* of types, largely focused around pointers and lifetimes.
They mostly exist to make Rust "just work" in more cases, and are largely harmless.

For an exhaustive list of all the types of coercions, see the [Coercion types] section on the reference.

Note that we do not perform coercions when matching traits (except for receivers, see the [next page][dot-operator]).
If there is an `impl` for some type `U` and `T` coerces to `U`, that does not constitute an implementation for `T`.
For example, the following will not type check, even though it is OK to coerce `t` to `&T` and there is an `impl` for `&T`:

```rust,compile_fail
trait Trait {}

fn foo<X: Trait>(t: X) {}

impl<'a> Trait for &'a i32 {}

fn main() {
    let t: &mut i32 = &mut 0;
    foo(t);
}
```

which fails like as follows:

```text
error[E0277]: the trait bound `&mut i32: Trait` is not satisfied
 --> src/main.rs:9:9
  |
3 | fn foo<X: Trait>(t: X) {}
  |           ----- required by this bound in `foo`
...
9 |     foo(t);
  |         ^ the trait `Trait` is not implemented for `&mut i32`
  |
  = help: the following implementations were found:
            <&'a i32 as Trait>
  = note: `Trait` is implemented for `&i32`, but not for `&mut i32`
```

[Coercion types]: ../reference/type-coercions.html#coercion-types
[dot-operator]: ./dot-operator.html


---

# The Dot Operator

The dot operator will perform a lot of magic to convert types.
It will perform auto-referencing, auto-dereferencing, and coercion until types
match.
The detailed mechanics of method lookup are defined [here][method_lookup],
but here is a brief overview that outlines the main steps.

Suppose we have a function `foo` that has a receiver (a `self`, `&self` or
`&mut self` parameter).
If we call `value.foo()`, the compiler needs to determine what type `Self` is before
it can call the correct implementation of the function.
For this example, we will say that `value` has type `T`.

We will use [fully-qualified syntax][fqs] to be more clear about exactly which
type we are calling a function on.

- First, the compiler checks if it can call `T::foo(value)` directly.
This is called a "by value" method call.
- If it can't call this function (for example, if the function has the wrong type
or a trait isn't implemented for `Self`), then the compiler tries to add in an
automatic reference.
This means that the compiler tries `<&T>::foo(value)` and `<&mut T>::foo(value)`.
This is called an "autoref" method call.
- If none of these candidates worked, it dereferences `T` and tries again.
This uses the `Deref` trait - if `T: Deref<Target = U>` then it tries again with
type `U` instead of `T`.
If it can't dereference `T`, it can also try _unsizing_ `T`.
This just means that if `T` has a size parameter known at compile time, it "forgets"
it for the purpose of resolving methods.
For instance, this unsizing step can convert `[i32; 2]` into `[i32]` by "forgetting"
the size of the array.

Here is an example of the method lookup algorithm:

```rust,ignore
let array: Rc<Box<[T; 3]>> = ...;
let first_entry = array[0];
```

How does the compiler actually compute `array[0]` when the array is behind so
many indirections?
First, `array[0]` is really just syntax sugar for the [`Index`][index] trait -
the compiler will convert `array[0]` into `array.index(0)`.
Now, the compiler checks to see if `array` implements `Index`, so that it can call
the function.

Then, the compiler checks if `Rc<Box<[T; 3]>>` implements `Index`, but it
does not, and neither do `&Rc<Box<[T; 3]>>` or `&mut Rc<Box<[T; 3]>>`.
Since none of these worked, the compiler dereferences the `Rc<Box<[T; 3]>>` into
`Box<[T; 3]>` and tries again.
`Box<[T; 3]>`, `&Box<[T; 3]>`, and `&mut Box<[T; 3]>` do not implement `Index`,
so it dereferences again.
`[T; 3]` and its autorefs also do not implement `Index`.
It can't dereference `[T; 3]`, so the compiler unsizes it, giving `[T]`.
Finally, `[T]` implements `Index`, so it can now call the actual `index` function.

Consider the following more complicated example of the dot operator at work:

```rust
fn do_stuff<T: Clone>(value: &T) {
    let cloned = value.clone();
}
```

What type is `cloned`?
First, the compiler checks if it can call by value.
The type of `value` is `&T`, and so the `clone` function has signature
`fn clone(&T) -> T`.
It knows that `T: Clone`, so the compiler finds that `cloned: T`.

What would happen if the `T: Clone` restriction was removed? It would not be able
to call by value, since there is no implementation of `Clone` for `T`.
So the compiler tries to call by autoref.
In this case, the function has the signature `fn clone(&&T) -> &T` since
`Self = &T`.
The compiler sees that `&T: Clone`, and then deduces that `cloned: &T`.

Here is another example where the autoref behavior is used to create some subtle
effects:

```rust
# use std::sync::Arc;
#
#[derive(Clone)]
struct Container<T>(Arc<T>);

fn clone_containers<T>(foo: &Container<i32>, bar: &Container<T>) {
    let foo_cloned = foo.clone();
    let bar_cloned = bar.clone();
}
```

What types are `foo_cloned` and `bar_cloned`?
We know that `Container<i32>: Clone`, so the compiler calls `clone` by value to give
`foo_cloned: Container<i32>`.
However, `bar_cloned` actually has type `&Container<T>`.
Surely this doesn't make sense - we added `#[derive(Clone)]` to `Container`, so it
must implement `Clone`!
Looking closer, the code generated by the `derive` macro is (roughly):

```rust,ignore
impl<T> Clone for Container<T> where T: Clone {
    fn clone(&self) -> Self {
        Self(Arc::clone(&self.0))
    }
}
```

The derived `Clone` implementation is [only defined where `T: Clone`][clone],
so there is no implementation for `Container<T>: Clone` for a generic `T`.
The compiler then looks to see if `&Container<T>` implements `Clone`, which it does.
So it deduces that `clone` is called by autoref, and so `bar_cloned` has type
`&Container<T>`.

We can fix this by implementing `Clone` manually without requiring `T: Clone`:

```rust,ignore
impl<T> Clone for Container<T> {
    fn clone(&self) -> Self {
        Self(Arc::clone(&self.0))
    }
}
```

Now, the type checker deduces that `bar_cloned: Container<T>`.

[fqs]: ../book/ch19-03-advanced-traits.html#fully-qualified-syntax-for-disambiguation-calling-methods-with-the-same-name
[method_lookup]: https://rustc-dev-guide.rust-lang.org/hir-typeck/method-lookup.html
[index]: ../std/ops/trait.Index.html
[clone]: ../std/clone/trait.Clone.html#derivable


---

# Casts

Casts are a superset of coercions: every coercion can be explicitly invoked via a cast.
However some conversions require a cast.
While coercions are pervasive and largely harmless, these "true casts" are rare and potentially dangerous.
As such, casts must be explicitly invoked using the `as` keyword: `expr as Type`.

You can find an exhaustive list of [all the true casts][cast list] and [casting semantics][semantics list] on the reference.

## Safety of casting

True casts generally revolve around raw pointers and the primitive numeric types.
Even though they're dangerous, these casts are infallible at runtime.
If a cast triggers some subtle corner case no indication will be given that this occurred.
The cast will simply succeed.
That said, casts must be valid at the type level, or else they will be prevented statically.
For instance, `7u8 as bool` will not compile.

That said, casts aren't `unsafe` because they generally can't violate memory safety *on their own*.
For instance, converting an integer to a raw pointer can very easily lead to terrible things.
However the act of creating the pointer itself is safe, because actually using a raw pointer is already marked as `unsafe`.

## Some notes about casting

### Lengths when casting raw slices

Note that lengths are not adjusted when casting raw slices; `*const [u16] as *const [u8]` creates a slice that only includes half of the original memory.

### Transitivity

Casting is not transitive, that is, even if `e as U1 as U2` is a valid expression, `e as U2` is not necessarily so.

[cast list]: ../reference/expressions/operator-expr.html#type-cast-expressions
[semantics list]: ../reference/expressions/operator-expr.html#semantics


---

# Transmutes

Get out of our way type system! We're going to reinterpret these bits or die
trying! Even though this book is all about doing things that are unsafe, I
really can't emphasize enough that you should deeply think about finding Another Way
than the operations covered in this section. This is really, truly, the most
horribly unsafe thing you can do in Rust. The guardrails here are dental floss.

[`mem::transmute<T, U>`][transmute] takes a value of type `T` and reinterprets
it to have type `U`. The only restriction is that the `T` and `U` are verified
to have the same size. The ways to cause Undefined Behavior with this are mind
boggling.

* First and foremost, creating an instance of *any* type with an invalid state
  is going to cause arbitrary chaos that can't really be predicted. Do not
  transmute `3` to `bool`. Even if you never *do* anything with the `bool`. Just
  don't.

* Transmute has an overloaded return type. If you do not specify the return type
  it may produce a surprising type to satisfy inference.

* Transmuting an `&` to `&mut` is Undefined Behavior. While certain usages may
  *appear* safe, note that the Rust optimizer is free to assume that a shared
  reference won't change through its lifetime and thus such transmutation will
  run afoul of those assumptions. So:
  * Transmuting an `&` to `&mut` is *always* Undefined Behavior.
  * No you can't do it.
  * No you're not special.

* Transmuting to a reference without an explicitly provided lifetime
  produces an [unbounded lifetime].

* When transmuting between different compound types, you have to make sure they
  are laid out the same way! If layouts differ, the wrong fields are going to
  get filled with the wrong data, which will make you unhappy and can also be
  Undefined Behavior (see above).

  So how do you know if the layouts are the same? For `repr(C)` types and
  `repr(transparent)` types, layout is precisely defined. But for your
  run-of-the-mill `repr(Rust)`, it is not. Even different instances of the same
  generic type can have wildly different layout. `Vec<i32>` and `Vec<u32>`
  *might* have their fields in the same order, or they might not. The details of
  what exactly is and is not guaranteed for data layout are still being worked
  out over [at the UCG WG][ucg-layout].

[`mem::transmute_copy<T, U>`][transmute_copy] somehow manages to be *even more*
wildly unsafe than this. It copies `size_of<U>` bytes out of an `&T` and
interprets them as a `U`.  The size check that `mem::transmute` has is gone (as
it may be valid to copy out a prefix), though it is Undefined Behavior for `U`
to be larger than `T`.

Also of course you can get all of the functionality of these functions using raw
pointer casts or `union`s, but without any of the lints or other basic sanity
checks. Raw pointer casts and `union`s do not magically avoid the above rules.

[unbounded lifetime]: ./unbounded-lifetimes.md
[transmute]: ../std/mem/fn.transmute.html
[transmute_copy]: ../std/mem/fn.transmute_copy.html
[ucg-layout]: https://rust-lang.github.io/unsafe-code-guidelines/layout.html
