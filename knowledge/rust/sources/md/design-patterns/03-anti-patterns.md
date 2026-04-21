# Anti-patterns

An [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) is a solution to a
"recurring problem that is usually ineffective and risks being highly
counterproductive". Just as valuable as knowing how to solve a problem, is
knowing how *not* to solve it. Anti-patterns give us great counter-examples to
consider relative to design patterns. Anti-patterns are not confined to code.
For example, a process can be an anti-pattern, too.


---

# Clone to satisfy the borrow checker

## Description

The borrow checker prevents Rust users from developing otherwise unsafe code by
ensuring that either: only one mutable reference exists, or potentially many but
all immutable references exist. If the code written does not hold true to these
conditions, this anti-pattern arises when the developer resolves the compiler
error by cloning the variable.

## Example

```rust
// define any variable
let mut x = 5;

// Borrow `x` -- but clone it first
let y = &mut (x.clone());

// without the x.clone() two lines prior, this line would fail on compile as
// x has been borrowed
// thanks to x.clone(), x was never borrowed, and this line will run.
println!("{x}");

// perform some action on the borrow to prevent rust from optimizing this
//out of existence
*y += 1;
```

## Motivation

It is tempting, particularly for beginners, to use this pattern to resolve
confusing issues with the borrow checker. However, there are serious
consequences. Using `.clone()` causes a copy of the data to be made. Any changes
between the two are not synchronized -- as if two completely separate variables
exist.

There are special cases -- `Rc<T>` is designed to handle clones intelligently.
It internally manages exactly one copy of the data. Invoking `.clone()` on `Rc`
produces a new `Rc` instance, which points to the same data as the source `Rc`,
while increasing a reference count. The same applies to `Arc`, the thread-safe
counterpart of `Rc`.

In general, clones should be deliberate, with full understanding of the
consequences. If a clone is used to make a borrow checker error disappear,
that's a good indication this anti-pattern may be in use.

Even though `.clone()` is an indication of a bad pattern, sometimes **it is fine
to write inefficient code**, in cases such as when:

- the developer is still new to ownership
- the code doesn't have great speed or memory constraints (like hackathon
  projects or prototypes)
- satisfying the borrow checker is really complicated, and you prefer to
  optimize readability over performance

If an unnecessary clone is suspected, The
[Rust Book's chapter on Ownership](https://doc.rust-lang.org/book/ownership.html)
should be understood fully before assessing whether the clone is required or
not.

Also be sure to always run `cargo clippy` in your project, which will detect
some cases in which `.clone()` is not necessary.

## See also

- [`mem::{take(_), replace(_)}` to keep owned values in changed enums](../idioms/mem-replace.md)
- [`Rc<T>` documentation, which handles .clone() intelligently](http://doc.rust-lang.org/std/rc/)
- [`Arc<T>` documentation, a thread-safe reference-counting pointer](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [Tricks with ownership in Rust](https://web.archive.org/web/20210120233744/https://xion.io/post/code/rust-borrowchk-tricks.html)


---

# `#![deny(warnings)]`

## Description

A well-intentioned crate author wants to ensure their code builds without
warnings. So they annotate their crate root with the following:

## Example

```rust
#![deny(warnings)]

// All is well.
```

## Advantages

It is short and will stop the build if anything is amiss.

## Drawbacks

By disallowing the compiler to build with warnings, a crate author opts out of
Rust's famed stability. Sometimes new features or old misfeatures need a change
in how things are done, thus lints are written that `warn` for a certain grace
period before being turned to `deny`.

For example, it was discovered that a type could have two `impl`s with the same
method. This was deemed a bad idea, but in order to make the transition smooth,
the `overlapping-inherent-impls` lint was introduced to give a warning to those
stumbling on this fact, before it becomes a hard error in a future release.

Also sometimes APIs get deprecated, so their use will emit a warning where
before there was none.

All this conspires to potentially break the build whenever something changes.

Furthermore, crates that supply additional lints (e.g. [rust-clippy]) can no
longer be used unless the annotation is removed. This is mitigated with
[--cap-lints]. The `--cap-lints=warn` command line argument, turns all `deny`
lint errors into warnings.

## Alternatives

There are two ways of tackling this problem: First, we can decouple the build
setting from the code, and second, we can name the lints we want to deny
explicitly.

The following command line will build with all warnings set to `deny`:

`RUSTFLAGS="-D warnings" cargo build`

This can be done by any individual developer (or be set in a CI tool like
Travis, but remember that this may break the build when something changes)
without requiring a change to the code.

Alternatively, we can specify the lints that we want to `deny` in the code. Here
is a list of warning lints that is (hopefully) safe to deny (as of rustc
1.48.0):

```rust,ignore
#![deny(
    bad_style,
    const_err,
    dead_code,
    improper_ctypes,
    non_shorthand_field_patterns,
    no_mangle_generic_items,
    overflowing_literals,
    path_statements,
    patterns_in_fns_without_body,
    private_in_public,
    unconditional_recursion,
    unused,
    unused_allocation,
    unused_comparisons,
    unused_parens,
    while_true
)]
```

In addition, the following `allow`ed lints may be a good idea to `deny`:

```rust,ignore
#![deny(
    missing_debug_implementations,
    missing_docs,
    trivial_casts,
    trivial_numeric_casts,
    unused_extern_crates,
    unused_import_braces,
    unused_qualifications,
    unused_results
)]
```

Some may also want to add `missing-copy-implementations` to their list.

Note that we explicitly did not add the `deprecated` lint, as it is fairly
certain that there will be more deprecated APIs in the future.

## See also

- [A collection of all clippy lints](https://rust-lang.github.io/rust-clippy/master)
- [deprecate attribute] documentation
- Type `rustc -W help` for a list of lints on your system. Also type
  `rustc --help` for a general list of options
- [rust-clippy] is a collection of lints for better Rust code

[rust-clippy]: https://github.com/rust-lang/rust-clippy
[deprecate attribute]: https://doc.rust-lang.org/reference/attributes.html#deprecation
[--cap-lints]: https://doc.rust-lang.org/rustc/lints/levels.html#capping-lints


---

# `Deref` polymorphism

## Description

Misuse the `Deref` trait to emulate inheritance between structs, and thus reuse
methods.

## Example

Sometimes we want to emulate the following common pattern from OO languages such
as Java:

```java
class Foo {
    void m() { ... }
}

class Bar extends Foo {}

public static void main(String[] args) {
    Bar b = new Bar();
    b.m();
}
```

We can use the deref polymorphism anti-pattern to do so:

```rust
use std::ops::Deref;

struct Foo {}

impl Foo {
    fn m(&self) {
        //..
    }
}

struct Bar {
    f: Foo,
}

impl Deref for Bar {
    type Target = Foo;
    fn deref(&self) -> &Foo {
        &self.f
    }
}

fn main() {
    let b = Bar { f: Foo {} };
    b.m();
}
```

There is no struct inheritance in Rust. Instead we use composition and include
an instance of `Foo` in `Bar` (since the field is a value, it is stored inline,
so if there were fields, they would have the same layout in memory as the Java
version (probably, you should use `#[repr(C)]` if you want to be sure)).

In order to make the method call work we implement `Deref` for `Bar` with `Foo`
as the target (returning the embedded `Foo` field). That means that when we
dereference a `Bar` (for example, using `*`) then we will get a `Foo`. That is
pretty weird. Dereferencing usually gives a `T` from a reference to `T`, here we
have two unrelated types. However, since the dot operator does implicit
dereferencing, it means that the method call will search for methods on `Foo` as
well as `Bar`.

## Advantages

You save a little boilerplate, e.g.,

```rust,ignore
impl Bar {
    fn m(&self) {
        self.f.m()
    }
}
```

## Disadvantages

Most importantly this is a surprising idiom - future programmers reading this in
code will not expect this to happen. That's because we are misusing the `Deref`
trait rather than using it as intended (and documented, etc.). It's also because
the mechanism here is completely implicit.

This pattern does not introduce subtyping between `Foo` and `Bar` like
inheritance in Java or C++ does. Furthermore, traits implemented by `Foo` are
not automatically implemented for `Bar`, so this pattern interacts badly with
bounds checking and thus generic programming.

Using this pattern gives subtly different semantics from most OO languages with
regards to `self`. Usually it remains a reference to the sub-class, with this
pattern it will be the 'class' where the method is defined.

Finally, this pattern only supports single inheritance, and has no notion of
interfaces, class-based privacy, or other inheritance-related features. So, it
gives an experience that will be subtly surprising to programmers used to Java
inheritance, etc.

## Discussion

There is no one good alternative. Depending on the exact circumstances it might
be better to re-implement using traits or to write out the facade methods to
dispatch to `Foo` manually. We do intend to add a mechanism for inheritance
similar to this to Rust, but it is likely to be some time before it reaches
stable Rust. See these [blog](http://aturon.github.io/blog/2015/09/18/reuse/)
[posts](http://smallcultfollowing.com/babysteps/blog/2015/10/08/virtual-structs-part-4-extended-enums-and-thin-traits/)
and this [RFC issue](https://github.com/rust-lang/rfcs/issues/349) for more
details.

The `Deref` trait is designed for the implementation of custom pointer types.
The intention is that it will take a pointer-to-`T` to a `T`, not convert
between different types. It is a shame that this isn't (probably cannot be)
enforced by the trait definition.

Rust tries to strike a careful balance between explicit and implicit mechanisms,
favouring explicit conversions between types. Automatic dereferencing in the dot
operator is a case where the ergonomics strongly favour an implicit mechanism,
but the intention is that this is limited to degrees of indirection, not
conversion between arbitrary types.

## See also

- [Collections are smart pointers idiom](../idioms/deref.md).
- Delegation crates for less boilerplate like
  [delegate](https://crates.io/crates/delegate) or
  [ambassador](https://crates.io/crates/ambassador)
- [Documentation for `Deref` trait](https://doc.rust-lang.org/std/ops/trait.Deref.html).
