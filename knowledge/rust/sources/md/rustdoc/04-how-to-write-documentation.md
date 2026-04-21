# How to write documentation

Good documentation is not natural.  There are opposing goals that make writing
good documentation difficult.  It requires expertise in the subject but also
writing to a novice perspective.  Documentation therefore often glazes over
implementation detail, or leaves readers with unanswered questions.

There are a few tenets to Rust documentation that can help guide anyone through
the process of documenting libraries so that everyone has an ample opportunity
to use the code.

This chapter covers not only how to write documentation but specifically
how to write **good** documentation.  It is important to be as clear
as you can, and as complete as possible.  As a rule of thumb: the more
documentation you write for your crate the better.  If an item is public
then it should be documented.

## Getting Started

Documenting a crate should begin with front-page documentation.  As an
example, the [`hashbrown`] crate level documentation summarizes the role of
the crate, provides links to explain technical details, and explains why you
would want to use the crate.

After introducing the crate, it is important that the front-page gives
an example of how to use the crate in a real world setting.  Stick to the
library's role in the example, but do so without shortcuts to benefit users who
may copy and paste the example to get started.

[`futures`] uses inline comments to explain line by line
the complexities of using a [`Future`], because a person's first exposure to
rust's [`Future`] may be this example.

The [`backtrace`] documentation walks through the whole process, explaining
changes made to the `Cargo.toml` file, passing command line arguments to the
compiler, and shows a quick example of backtrace in the wild.

Finally, the front-page can eventually become a comprehensive reference
how to use a crate, like [`regex`].  In this front page, all
requirements are outlined, the edge cases shown, and practical examples
provided.  The front page goes on to show how to use regular expressions
then concludes with crate features.

Don't worry about comparing your crate, which is just beginning, to other more
developed crates.  To get the documentation to something more polished, start
incrementally and put in an introduction, example, and features.  Rome was not
built in a day!

The first lines within the `lib.rs` will compose the front-page, and they
use a different convention than the rest of the rustdocs.  Lines should
start with `//!` which indicate module-level or crate-level documentation.
Here's a quick example of the difference:

```rust,no_run
//! Fast and easy queue abstraction.
//!
//! Provides an abstraction over a queue.  When the abstraction is used
//! there are these advantages:
//! - Fast
//! - [`Easy`]
//!
//! [`Easy`]: http://thatwaseasy.example.com

/// This module makes it easy.
pub mod easy {

    /// Use the abstraction function to do this specific thing.
    pub fn abstraction() {}

}
```

Ideally, this first line of documentation is a sentence without highly
technical details, but with a good description of where this crate fits
within the rust ecosystem.  Users should know whether this crate meets their use
case after reading this line.

## Documenting components

Whether it is modules, structs, functions, or macros: the public
API of all code should have documentation. Rarely does anyone
complain about too much documentation!

It is recommended that each item's documentation follows this basic structure:

```text
[short sentence explaining what it is]

[more detailed explanation]

[at least one code example that users can copy/paste to try it]

[even more advanced explanations if necessary]
```

This basic structure should be straightforward to follow when writing your
documentation; while you might think that a code example is trivial,
the examples are really important because they can help users understand
what an item is, how it is used, and for what purpose it exists.

Let's see an example coming from the [standard library] by taking a look at the
[`std::env::args()`][env::args] function:

``````markdown
Returns the arguments which this program was started with (normally passed
via the command line).

The first element is traditionally the path of the executable, but it can be
set to arbitrary text, and may not even exist. This means this property should
not be relied upon for security purposes.

On Unix systems shell usually expands unquoted arguments with glob patterns
(such as `*` and `?`). On Windows this is not done, and such arguments are
passed as-is.

# Panics

The returned iterator will panic during iteration if any argument to the
process is not valid unicode. If this is not desired,
use the [`args_os`] function instead.

# Examples

```
use std::env;

// Prints each argument on a separate line
for argument in env::args() {
    println!("{argument}");
}
```

[`args_os`]: ./fn.args_os.html
``````

Everything before the first empty line will be reused to describe the component
in searches and module overviews.  For example, the function `std::env::args()`
above will be shown on the [`std::env`] module documentation. It is good
practice to keep the summary to one line: concise writing is a goal of good
documentation.

Because the type system does a good job of defining what types a function
passes and returns, there is no benefit of explicitly writing it
into the documentation, especially since `rustdoc` adds hyper links to all types in the function signature.

In the example above, a 'Panics' section explains when the code might abruptly exit,
which can help the reader prevent reaching a panic.  A panic section is recommended
every time edge cases in your code can be reached if known.

As you can see, it follows the structure detailed above: it starts with a short
sentence explaining what the functions does, then it provides more information
and finally provides a code example.

## Markdown

`rustdoc` uses the [CommonMark Markdown specification]. You might be
interested in taking a look at their website to see what's possible:

 - [CommonMark quick reference]
 - [current spec]

In addition to the standard CommonMark syntax, `rustdoc` supports several
extensions:

### Strikethrough

Text may be rendered with a horizontal line through the center by wrapping the
text with one or two tilde characters on each side:

```text
An example of ~~strikethrough text~~. You can also use ~single tildes~.
```

This example will render as:

> An example of ~~strikethrough text~~. You can also use ~single tildes~.

This follows the [GitHub Strikethrough extension][strikethrough].

### Footnotes

A footnote generates a small numbered link in the text which when clicked
takes the reader to the footnote text at the bottom of the item. The footnote
label is written similarly to a link reference with a caret at the front. The
footnote text is written like a link reference definition, with the text
following the label. Example:

```text
This is an example of a footnote[^note].

[^note]: This text is the contents of the footnote, which will be rendered
    towards the bottom.
```

This example will render as:

> This is an example of a footnote[^note].
>
> [^note]: This text is the contents of the footnote, which will be rendered
>     towards the bottom.

The footnotes are automatically numbered based on the order the footnotes are
written.

### Tables

Tables can be written using pipes and dashes to draw the rows and columns of
the table. These will be translated to HTML table matching the shape. Example:

```text
| Header1 | Header2 |
|---------|---------|
| abc     | def     |
```

This example will render similarly to this:

> | Header1 | Header2 |
> |---------|---------|
> | abc     | def     |

See the specification for the [GitHub Tables extension][tables] for more
details on the exact syntax supported.

### Task lists

Task lists can be used as a checklist of items that have been completed.
Example:

```md
- [x] Complete task
- [ ] Incomplete task
```

This will render as:

> - [x] Complete task
> - [ ] Incomplete task

See the specification for the [task list extension] for more details.

### Smart punctuation

Some ASCII punctuation sequences will be automatically turned into fancy Unicode
characters:

| ASCII sequence | Unicode |
|----------------|---------|
| `--`           | –       |
| `---`          | —       |
| `...`          | …       |
| `"`            | “ or ”, depending on context |
| `'`            | ‘ or ’, depending on context |

So, no need to manually enter those Unicode characters!

### Adding a warning block

If you want to make a warning or similar note stand out in the documentation,
you can wrap it like this:

```md
/// documentation
///
/// <div class="warning">A big warning!</div>
///
/// more documentation
```

Please note that if you want to put markdown in the HTML tag and for it to
be interpreted as such, you need to have an empty line between the HTML tags
and your markdown content. For example if you want to use a link:

```md
/// documentation
///
/// <div class="warning">
///
/// Go to [this link](https://rust-lang.org)!
///
/// </div>
///
/// more documentation
```

[`backtrace`]: https://docs.rs/backtrace/0.3.50/backtrace/
[commonmark markdown specification]: https://commonmark.org/
[commonmark quick reference]: https://commonmark.org/help/
[env::args]: https://doc.rust-lang.org/stable/std/env/fn.args.html
[`Future`]: https://doc.rust-lang.org/std/future/trait.Future.html
[`futures`]: https://docs.rs/futures/0.3.5/futures/
[`hashbrown`]: https://docs.rs/hashbrown/0.8.2/hashbrown/
[`regex`]: https://docs.rs/regex/1.3.9/regex/
[standard library]: https://doc.rust-lang.org/stable/std/index.html
[current spec]: https://spec.commonmark.org/current/
[`std::env`]: https://doc.rust-lang.org/stable/std/env/index.html#functions
[strikethrough]: https://github.github.com/gfm/#strikethrough-extension-
[tables]: https://github.github.com/gfm/#tables-extension-
[task list extension]: https://github.github.com/gfm/#task-list-items-extension-


---

# What to include (and exclude)

It is easy to say everything must be documented in a project and often times
that is correct, but how can we get there, and are there things that don't
belong?

At the top of the `src/lib.rs` or `main.rs` file in your binary project, include
the following attribute:

```rust
#![warn(missing_docs)]
```

Now run `cargo doc` and examine the output.  Here's a sample:

```text
 Documenting docdemo v0.1.0 (/Users/username/docdemo)
warning: missing documentation for the crate
 --> src/main.rs:1:1
  |
1 | / #![warn(missing_docs)]
2 | |
3 | | fn main() {
4 | |     println!("Hello, world!");
5 | | }
  | |_^
  |
note: the lint level is defined here
 --> src/main.rs:1:9
  |
1 | #![warn(missing_docs)]
  |         ^^^^^^^^^^^^

warning: 1 warning emitted

    Finished dev [unoptimized + debuginfo] target(s) in 2.96s
```

As a library author, adding the lint `#![deny(missing_docs)]` is a great way to
ensure the project does not drift away from being documented well, and
`#![warn(missing_docs)]` is a good way to move towards comprehensive
documentation.

There are more lints in the upcoming chapter [Lints][rustdoc-lints].

## Examples

Of course this is contrived to be simple, but part of the power of documentation
is showing code that is easy to follow, rather than being realistic.  Docs often
take shortcuts with error handling because examples can become complicated to
follow with all the necessary set up required for a simple example.

`Async` is a good example of this.  In order to execute an `async` example, an
executor needs to be available.  Examples will often shortcut this, and leave
users to figure out how to put the `async` code into their own runtime.

It is preferred that `unwrap()` not be used inside an example, and some of the
error handling components be hidden if they make the example too difficult to
follow.

``````text
/// Example
/// ```rust
/// let fourtytwo = "42".parse::<u32>()?;
/// println!("{} + 10 = {}", fourtytwo, fourtytwo+10);
/// ```
``````

When rustdoc wraps that in a main function, it will fail to compile because the
`ParseIntError` trait is not implemented.  In order to help both your audience
and your test suite, this example needs some additional code:

``````text
/// Example
/// ```rust
/// # fn main() -> Result<(), std::num::ParseIntError> {
/// let fortytwo = "42".parse::<u32>()?;
/// println!("{} + 10 = {}", fortytwo, fortytwo+10);
/// #     Ok(())
/// # }
/// ```
``````

The example is the same on the doc page, but has that extra information
available to anyone trying to use your crate.  More about tests in the
upcoming [Documentation tests] chapter.

## What to Exclude

Certain parts of your public interface may be included by default in the output
of rustdoc.  The attribute `#[doc(hidden)]` can hide implementation details
to encourage idiomatic use of the crate.

For example, an internal `macro!` that makes the crate easier to implement can
become a footgun for users when it appears in the public documentation.  An
internal `Error` type may exist, and `impl` details should be hidden, as
detailed in the [API Guidelines].

## Customizing the output

It is possible to pass a custom css file to `rustdoc` and style the
documentation.

```bash
rustdoc --extend-css custom.css src/lib.rs
```

A good example of using this feature to create a dark theme is documented [on
this blog].  Just remember, dark theme is already included in the rustdoc output
by clicking on the gear icon in the upper right. Adding additional options to the
themes are as easy as creating a custom theme `.css` file and using the following
syntax:

```bash
rustdoc --theme awesome.css src/lib.rs
```

Here is an example of a new theme, [Ayu].

[Ayu]: https://github.com/rust-lang/rust/blob/HEAD/src/librustdoc/html/static/css/rustdoc.css#L2384-L2574
[API Guidelines]: https://rust-lang.github.io/api-guidelines/documentation.html#rustdoc-does-not-show-unhelpful-implementation-details-c-hidden
[Documentation tests]: documentation-tests.md
[on this blog]: https://blog.guillaume-gomez.fr/articles/2016-09-16+Generating+doc+with+rustdoc+and+a+custom+theme
[rustdoc-lints]: ../lints.md


---

# The `#[doc]` attribute

The `#[doc]` attribute lets you control various aspects of how `rustdoc` does
its job.

The most basic function of `#[doc]` is to handle the actual documentation
text. That is, `///` is syntax sugar for `#[doc]` (as is `//!` for `#![doc]`).
This means that these two are the same:

```rust,no_run
/// This is a doc comment.
#[doc = r" This is a doc comment."]
# fn f() {}
```

(Note the leading space and the raw string literal in the attribute version.)

In most cases, `///` is easier to use than `#[doc]`. One case where the latter is easier is
when generating documentation in macros; the `collapse-docs` pass will combine multiple
`#[doc]` attributes into a single doc comment, letting you generate code like this:

```rust,no_run
#[doc = "This is"]
#[doc = " a "]
#[doc = "doc comment"]
# fn f() {}
```

Which can feel more flexible. Note that this would generate this:

```rust,no_run
#[doc = "This is\n a \ndoc comment"]
# fn f() {}
```

but given that docs are rendered via Markdown, it will remove these newlines.

Another use case is for including external files as documentation:

```rust,no_run
#[doc = include_str!("../../README.md")]
# fn f() {}
```

The `doc` attribute has more options though! These don't involve the text of
the output, but instead, various aspects of the presentation of the output.
We've split them into two kinds below: attributes that are useful at the
crate level, and ones that are useful at the item level.

## At the crate level

These options control how the docs look at a crate level.

### `html_favicon_url`

This form of the `doc` attribute lets you control the favicon of your docs.

```rust,no_run
#![doc(html_favicon_url = "https://example.com/favicon.ico")]
```

This will put `<link rel="icon" href="{}">` into your docs, where
the string for the attribute goes into the `{}`.

If you don't use this attribute, a default favicon will be used.

### `html_logo_url`

This form of the `doc` attribute lets you control the logo in the upper
left hand side of the docs.

```rust,no_run
#![doc(html_logo_url = "https://example.com/logo.jpg")]
```

This will put `<a href='../index.html'><img src='{}' alt='logo' width='100'></a>` into
your docs, where the string for the attribute goes into the `{}`.

If you don't use this attribute, there will be no logo.

### `html_playground_url`

This form of the `doc` attribute lets you control where the "run" buttons
on your documentation examples make requests to.

```rust,no_run
#![doc(html_playground_url = "https://playground.example.com/")]
```

Now, when you press "run", the button will make a request to this domain. The request
URL will contain 3 query parameters:
1. `code` for the code in the documentation
2. `version` for the Rust channel, e.g. nightly, which is decided by whether `code` contain unstable features
3. `edition` for the Rust edition, e.g. 2024

If you don't use this attribute, there will be no run buttons.

### `issue_tracker_base_url`

This form of the `doc` attribute is mostly only useful for the standard library;
When a feature is unstable, an issue number for tracking the feature must be
given. `rustdoc` uses this number, plus the base URL given here, to link to
the tracking issue.

```rust,no_run
#![doc(issue_tracker_base_url = "https://github.com/rust-lang/rust/issues/")]
```

### `html_root_url`

The `#[doc(html_root_url = "…")]` attribute value indicates the URL for
generating links to external crates. When rustdoc needs to generate a link to
an item in an external crate, it will first check if the extern crate has been
documented locally on-disk, and if so link directly to it. Failing that, it
will use the URL given by the `--extern-html-root-url` command-line flag if
available. If that is not available, then it will use the `html_root_url`
value in the extern crate if it is available. If that is not available, then
the extern items will not be linked.

```rust,no_run
#![doc(html_root_url = "https://docs.rs/serde/1.0")]
```

### `html_no_source`

By default, `rustdoc` will include the source code of your program, with links
to it in the docs. But if you include this:

```rust,no_run
#![doc(html_no_source)]
```

it will not.

### `test(no_crate_inject)`

By default, `rustdoc` will automatically add a line with `extern crate my_crate;` into each doctest.
But if you include this:

```rust,no_run
#![doc(test(no_crate_inject))]
```

it will not.

## At the item level

These forms of the `#[doc]` attribute are used on individual items, to control how
they are documented.

### `inline` and `no_inline`

<span id="docno_inlinedocinline"></span>

These attributes are used on `use` statements, and control where the documentation shows
up. For example, consider this Rust code:

```rust,no_run
pub use bar::Bar;

/// bar docs
pub mod bar {
    /// the docs for Bar
    pub struct Bar;
}
# fn main() {}
```

The documentation will generate a "Re-exports" section, and say `pub use bar::Bar;`, where
`Bar` is a link to its page.

If we change the `use` line like this:

```rust,no_run
#[doc(inline)]
pub use bar::Bar;
# pub mod bar { pub struct Bar; }
# fn main() {}
```

Instead, `Bar` will appear in a `Structs` section, just like `Bar` was defined at the
top level, rather than `pub use`'d.

Let's change our original example, by making `bar` private:

```rust,no_run
pub use bar::Bar;

/// bar docs
mod bar {
    /// the docs for Bar
    pub struct Bar;
}
# fn main() {}
```

Here, because `bar` is not public, `bar` wouldn't have its own page, so there's nowhere
to link to. `rustdoc` will inline these definitions, and so we end up in the same case
as the `#[doc(inline)]` above; `Bar` is in a `Structs` section, as if it were defined at
the top level. If we add the `no_inline` form of the attribute:

```rust,no_run
#[doc(no_inline)]
pub use bar::Bar;

/// bar docs
mod bar {
    /// the docs for Bar
    pub struct Bar;
}
# fn main() {}
```

Now we'll have a `Re-exports` line, and `Bar` will not link to anywhere.

One special case: In Rust 2018 and later, if you `pub use` one of your dependencies, `rustdoc` will
not eagerly inline it as a module unless you add `#[doc(inline)]`.

If you want to know more about inlining rules, take a look at the
[`re-exports` chapter](./re-exports.md).

### `hidden`

<span id="dochidden"></span>

Any item annotated with `#[doc(hidden)]` will not appear in the documentation,
unless the [`--document-hidden-items`](../unstable-features.md#document-hidden-items) flag is used.

You can find more information in the [`re-exports` chapter](./re-exports.md).

### `alias`

This attribute adds an alias in the search index.

Let's take an example:

```rust,no_run
#[doc(alias = "TheAlias")]
pub struct SomeType;
```

So now, if you enter "TheAlias" in the search, it'll display `SomeType`.
Of course, if you enter `SomeType` it'll return `SomeType` as expected!

#### FFI example

This doc attribute is especially useful when writing bindings for a C library.
For example, let's say we have a C function that looks like this:

```c
int lib_name_do_something(Obj *obj);
```

It takes a pointer to an `Obj` type and returns an integer. In Rust, it might
be written like this:

```ignore (using non-existing ffi types)
pub struct Obj {
    inner: *mut ffi::Obj,
}

impl Obj {
    pub fn do_something(&mut self) -> i32 {
        unsafe { ffi::lib_name_do_something(self.inner) }
    }
}
```

The function has been turned into a method to make it more convenient to use.
However, if you want to look for the Rust equivalent of `lib_name_do_something`,
you have no way to do so.

To get around this limitation, we just add `#[doc(alias = "lib_name_do_something")]`
on the `do_something` method and then it's all good!
Users can now look for `lib_name_do_something` in our crate directly and find
`Obj::do_something`.

### `test(attr(...))`

This form of the `doc` attribute allows you to add arbitrary attributes to all your doctests. For
example, if you want your doctests to fail if they have dead code, you could add this:

```rust,no_run
#![doc(test(attr(deny(dead_code))))]

mod my_mod {
    #![doc(test(attr(allow(dead_code))))] // but allow `dead_code` for this module
}
```

`test(attr(..))` attributes are appended to the parent module's, they do not replace the current
list of attributes. In the previous example, both attributes would be present:

```rust,no_run
// For every doctest in `my_mod`

#![deny(dead_code)] // from the crate-root
#![allow(dead_code)] // from `my_mod`
```


---

# Re-exports

Let's start by explaining what are re-exports. To do so, we will use an example where we are
writing a library (named `lib`) with some types dispatched in sub-modules:

```rust
pub mod sub_module1 {
    pub struct Foo;
}
pub mod sub_module2 {
    pub struct AnotherFoo;
}
```

Users can import them like this:

```rust,ignore (inline)
use lib::sub_module1::Foo;
use lib::sub_module2::AnotherFoo;
```

But what if you want the types to be available directly at the crate root or if we don't want the
modules to be visible for users? That's where re-exports come in:

```rust,ignore (inline)
// `sub_module1` and `sub_module2` are not visible outside.
mod sub_module1 {
    pub struct Foo;
}
mod sub_module2 {
    pub struct AnotherFoo;
}
// We re-export both types:
pub use crate::sub_module1::Foo;
pub use crate::sub_module2::AnotherFoo;
```

And now users will be able to do:

```rust,ignore (inline)
use lib::{Foo, AnotherFoo};
```

And since both `sub_module1` and `sub_module2` are private, users won't be able to import them.

Now what's interesting is that the generated documentation for this crate will show both `Foo` and
`AnotherFoo` directly at the crate root, meaning they have been inlined. There are a few rules to
know whether or not a re-exported item will be inlined.

## Inlining rules

If a public item comes from a private module, it will be inlined:

```rust,ignore (inline)
mod private_module {
    pub struct Public;
}
pub mod public_mod {
    // `Public` will inlined here since `private_module` is private.
    pub use super::private_module::Public;
}
// `Public` will not be inlined here since `public_mod` is public.
pub use self::public_mod::Public;
```

Likewise, if an item inherits `#[doc(hidden)]` from any of its ancestors, it will be inlined:

```rust,ignore (inline)
#[doc(hidden)]
pub mod public_mod {
    pub struct Public;
}
// `Public` be inlined since its parent (`public_mod`) has `#[doc(hidden)]`.
pub use self::public_mod::Public;
```

If an item has `#[doc(hidden)]`, it won't be inlined (nor visible in the generated documentation):

```rust,ignore (inline)
// This struct won't be visible.
#[doc(hidden)]
pub struct Hidden;

// This re-export won't be visible.
pub use self::Hidden as InlinedHidden;
```

However, if you still want the re-export itself to be visible, you can add the `#[doc(inline)]`
attribute on it:

```rust,ignore (inline)
// This struct won't be visible.
#[doc(hidden)]
pub struct Hidden;

#[doc(inline)]
pub use self::Hidden as InlinedHidden;
```

In this case, you will have `pub use self::Hidden as InlinedHidden;` in the generated documentation
but no link to the `Hidden` item.

So back to `#[doc(hidden)]`: if you have multiple re-exports and some of them have
`#[doc(hidden)]`, then these ones (and only these) won't appear in the documentation:

```rust,ignore (inline)
mod private_mod {
    /// First
    pub struct InPrivate;
}

/// Second
#[doc(hidden)]
pub use self::private_mod::InPrivate as Hidden;
/// Third
pub use self::Hidden as Visible;
```

In this case, `InPrivate` will be inlined as `Visible`. However, its documentation will be
`First Third` and not `First Second Third` because the re-export with `Second` as documentation has
`#[doc(hidden)]`, therefore, all its attributes are ignored.

## Inlining with `#[doc(inline)]`

You can use the `#[doc(inline)]` attribute if you want to force an item to be inlined:

```rust,ignore (inline)
pub mod public_mod {
    pub struct Public;
}
#[doc(inline)]
pub use self::public_mod::Public;
```

With this code, even though `public_mod::Public` is public and present in the documentation, the
`Public` type will be present both at the crate root and in the `public_mod` module.

## Preventing inlining with `#[doc(no_inline)]`

On the opposite of the `#[doc(inline)]` attribute, if you want to prevent an item from being
inlined, you can use `#[doc(no_inline)]`:

```rust,ignore (inline)
mod private_mod {
    pub struct Public;
}
#[doc(no_inline)]
pub use self::private_mod::Public;
```

In the generated documentation, you will see a re-export at the crate root and not the type
directly.

## Attributes

When an item is inlined, its doc comments and most of its attributes will be inlined along with it:

```rust,ignore (inline)
mod private_mod {
    /// First
    #[cfg(a)]
    pub struct InPrivate;
    /// Second
    #[cfg(b)]
    pub use self::InPrivate as Second;
}

/// Third
#[doc(inline)]
#[cfg(c)]
pub use self::private_mod::Second as Visible;
```

In this case, `Visible` will have as documentation `First Second Third` and will also have as `cfg`:
`#[cfg(a, b, c)]`.

[Intra-doc links](./linking-to-items-by-name.md) are resolved relative to where the doc comment is
defined.

There are a few attributes which are not inlined though:
 * `#[doc(alias="")]`
 * `#[doc(inline)]`
 * `#[doc(no_inline)]`
 * `#[doc(hidden)]` (because the re-export itself and its attributes are ignored).

All other attributes are inherited when inlined, so that the documentation matches the behavior if
the inlined item was directly defined at the spot where it's shown.

These rules also apply if the item is inlined with a glob re-export:

```rust,ignore (inline)
mod private_mod {
    /// First
    #[cfg(a)]
    pub struct InPrivate;
}

#[cfg(c)]
pub use self::private_mod::*;
```

Otherwise, the attributes displayed will be from the re-exported item and the attributes on the
re-export itself will be ignored:

```rust,ignore (inline)
mod private_mod {
    /// First
    #[cfg(a)]
    pub struct InPrivate;
}

#[cfg(c)]
pub use self::private_mod::InPrivate;
```

In the above case, `cfg(c)` will not be displayed in the docs.


---

# Linking to items by name

Rustdoc is capable of directly linking to other rustdoc pages using the path of
the item as a link. This is referred to as an 'intra-doc link'.

For example, in the following code all of the links will link to the rustdoc page for `Bar`:

```rust
/// This struct is not [Bar]
pub struct Foo1;

/// This struct is also not [bar](Bar)
pub struct Foo2;

/// This struct is also not [bar][b]
///
/// [b]: Bar
pub struct Foo3;

/// This struct is also not [`Bar`]
pub struct Foo4;

/// This struct *is* [`Bar`]!
pub struct Bar;
```

Unlike normal Markdown, `[bar][Bar]` syntax is also supported without needing a
`[Bar]: ...` reference link.

Backticks around the link will be stripped, so ``[`Option`]`` will correctly
link to `Option`.

## Valid links

You can refer to anything in scope, and use paths, including `Self`, `self`, `super`, and
`crate`. Associated items (functions, types, and constants) are supported, but [not for blanket
trait implementations][#79682]. Rustdoc also supports linking to all primitives listed in
[the standard library documentation](../../std/index.html#primitives).

[#79682]: https://github.com/rust-lang/rust/pull/79682

You can also refer to items with generic parameters like `Vec<T>`. The link will
resolve as if you had written ``[`Vec<T>`](Vec)``. Fully-qualified syntax (for example,
`<Vec as IntoIterator>::into_iter()`) is [not yet supported][fqs-issue], however.

[fqs-issue]: https://github.com/rust-lang/rust/issues/74563

```rust,edition2018
use std::sync::mpsc::Receiver;

/// This is a version of [`Receiver<T>`] with support for [`std::future`].
///
/// You can obtain a [`std::future::Future`] by calling [`Self::recv()`].
pub struct AsyncReceiver<T> {
    sender: Receiver<T>
}

impl<T> AsyncReceiver<T> {
    pub async fn recv() -> T {
        unimplemented!()
    }
}
```

Rustdoc allows using URL fragment specifiers, just like a normal link:

```rust
/// This is a special implementation of [positional parameters].
///
/// [positional parameters]: std::fmt#formatting-parameters
struct MySpecialFormatter;
```

## Namespaces and Disambiguators

Paths in Rust have three namespaces: type, value, and macro. Item names must be unique within
their namespace, but can overlap with items in other namespaces. In case of ambiguity,
rustdoc will warn about the ambiguity and suggest a disambiguator.

```rust
/// See also: [`Foo`](struct@Foo)
struct Bar;

/// This is different from [`Foo`](fn@Foo)
struct Foo {}

fn Foo() {}
```

These prefixes will be stripped when displayed in the documentation, so `[struct@Foo]` will be
rendered as `Foo`. The following prefixes are available: `struct`, `enum`, `trait`, `union`,
`mod`, `module`, `const`, `constant`, `fn`, `function`, `field`, `variant`, `method`, `derive`,
`type`, `value`, `macro`, `tyalias`, `typealias`, `prim` or `primitive`.

You can also disambiguate for functions by adding `()` after the function name,
or for macros by adding `!` after the macro name. The macro `!` can be followed by `()`, `{}`,
or `[]`. Example:

```rust
/// This is different from [`foo!()`].
fn foo() {}

/// This is different from [`foo()`]
macro_rules! foo {
  () => {}
}
```

There is one case where the disambiguation will be performed automatically: if an intra doc
link is resolved at the same time as a trait and as a derive proc-macro. In this case, it'll
always generate a link to the trait and not emit a "missing disambiguation" warning. A good
example of this case is when you link to the `Clone` trait: there is also a `Clone`
proc-macro but it ignores it in this case. If you want to link to the proc-macro, you can
use the `macro@` disambiguator.

## Warnings, re-exports, and scoping

Links are resolved in the scope of the module where the item is defined, even
when the item is re-exported. If a link from another crate fails to resolve, no
warning is given.

```rust,edition2018
mod inner {
    /// Link to [f()]
    pub struct S;
    pub fn f() {}
}
pub use inner::S; // the link to `f` will still resolve correctly
```

When re-exporting an item, rustdoc allows adding additional documentation to it.
That additional documentation will be resolved in the scope of the re-export, not
the original, allowing you to link to items in the new crate. The new links
will still give a warning if they fail to resolve.

```rust
/// See also [foo()]
pub use std::process::Command;

pub fn foo() {}
```

This is especially useful for proc-macros, which must always be defined in their own dedicated crate.

Note: Because of how `macro_rules!` macros are scoped in Rust, the intra-doc links of a
`macro_rules!` macro will be resolved [relative to the crate root][#72243], as opposed to the
module it is defined in.

If links do not look 'sufficiently like' an intra-doc link, they will be ignored and no warning
will be given, even if the link fails to resolve. For example, any link containing `/` or `[]`
characters will be ignored.

[#72243]: https://github.com/rust-lang/rust/issues/72243

## What happens in case an intra-doc link cannot be generated

In some cases (items behind a `cfg` for example), an intra-doc link cannot be generated to item.
There are different ways to create a link in markdown, and depending on the one you use, it will
render differently in this case:

```md
1. [a]
2. [b][c]
3. [d](e)
4. [f]

[f]: g
```

`1.` and `2.` will be displayed as is in the rendered documentation (ie, `[a]` and `[b][c]`)
whereas `3.` and `4.` will be replaced by a link targeting `e` for `[d](e)` and `g` for `[f]`.


---

# Documentation tests

`rustdoc` supports executing your documentation examples as tests. This makes sure
that examples within your documentation are up to date and working.

The basic idea is this:

```rust,no_run
/// # Examples
///
/// ```
/// let x = 5;
/// ```
# fn f() {}
```

The triple backticks start and end code blocks. If this were in a file named `foo.rs`,
running `rustdoc --test foo.rs` will extract this example, and then run it as a test.

Please note that by default, if no language is set for the block code, rustdoc
assumes it is Rust code. So the following:

``````markdown
```rust
let x = 5;
```
``````

is strictly equivalent to:

``````markdown
```
let x = 5;
```
``````

There's some subtlety though! Read on for more details.

## Passing or failing a doctest

Like regular unit tests, regular doctests are considered to "pass"
if they compile and run without panicking.
So if you want to demonstrate that some computation gives a certain result,
the `assert!` family of macros works the same as other Rust code:

```rust
let foo = "foo";
assert_eq!(foo, "foo");
```

This way, if the computation ever returns something different,
the code panics and the doctest fails.

## Pre-processing examples

In the example above, you'll note something strange: there's no `main`
function! Forcing you to write `main` for every example, no matter how small,
adds friction and clutters the output. So `rustdoc` processes your examples
slightly before running them. Here's the full algorithm `rustdoc` uses to
preprocess examples:

1. Some common `allow` attributes are inserted, including
   `unused_variables`, `unused_assignments`, `unused_mut`,
   `unused_attributes`, and `dead_code`. Small examples often trigger
   these lints.
2. Any attributes specified with `#![doc(test(attr(...)))]` are added.
3. Any leading `#![foo]` attributes are left intact as crate attributes.
4. If the example does not contain `extern crate`, and
   `#![doc(test(no_crate_inject))]` was not specified, then `extern crate
   <mycrate>;` is inserted (note the lack of `#[macro_use]`).
5. Finally, if the example does not contain `fn main`, the remainder of the
   text is wrapped in `fn main() { your_code }`.

For more about that caveat in rule 4, see "Documenting Macros" below.

## Hiding portions of the example

Sometimes, you need some setup code, or other things that would distract
from your example, but are important to make the tests work. Consider
an example block that looks like this:

```rust,no_run
/// ```
/// /// Some documentation.
/// # fn foo() {} // this function will be hidden
/// println!("Hello, World!");
/// ```
# fn f() {}
```

It will render like this:

```rust
/// Some documentation.
# fn foo() {}
println!("Hello, World!");
```

Yes, that's right: you can add lines that start with `# `, and they will
be hidden from the output, but will be used when compiling your code. You
can use this to your advantage. In this case, documentation comments need
to apply to some kind of function, so if I want to show you just a
documentation comment, I need to add a little function definition below
it. At the same time, it's only there to satisfy the compiler, so hiding
it makes the example more clear. You can use this technique to explain
longer examples in detail, while still preserving the testability of your
documentation.

For example, imagine that we wanted to document this code:

```rust
let x = 5;
let y = 6;
println!("{}", x + y);
```

We might want the documentation to end up looking like this:

> First, we set `x` to five:
>
> ```rust
> let x = 5;
> # let y = 6;
> # println!("{}", x + y);
> ```
>
> Next, we set `y` to six:
>
> ```rust
> # let x = 5;
> let y = 6;
> # println!("{}", x + y);
> ```
>
> Finally, we print the sum of `x` and `y`:
>
> ```rust
> # let x = 5;
> # let y = 6;
> println!("{}", x + y);
> ```

To keep each code block testable, we want the whole program in each block, but
we don't want the reader to see every line every time.  Here's what we put in
our source code:

``````markdown
First, we set `x` to five:

```
let x = 5;
# let y = 6;
# println!("{}", x + y);
```

Next, we set `y` to six:

```
# let x = 5;
let y = 6;
# println!("{}", x + y);
```

Finally, we print the sum of `x` and `y`:

```
# let x = 5;
# let y = 6;
println!("{}", x + y);
```
``````

By repeating all parts of the example, you can ensure that your example still
compiles, while only showing the parts that are relevant to that part of your
explanation.

The `#`-hiding of lines can be prevented by using two consecutive hashes
`##`. This only needs to be done with the first `#` which would've
otherwise caused hiding. If we have a string literal like the following,
which has a line that starts with a `#`:

```rust
let s = "foo
## bar # baz";
```

We can document it by escaping the initial `#`:

```text
/// let s = "foo
/// ## bar # baz";
```

Here is an example with a macro rule which matches on tokens starting with `#`:

`````rust,no_run
/// ```
/// macro_rules! ignore { (##tag) => {}; }
/// ignore! {
///     ###tag
/// }
/// ```
# fn f() {}
`````

As you can see, the rule is expecting two `#`, so when calling it, we need to add an extra `#`
because the first one is used as escape.

## Using `?` in doc tests

When writing an example, it is rarely useful to include a complete error
handling, as it would add significant amounts of boilerplate code. Instead, you
may want the following:

```rust,no_run
/// ```
/// use std::io;
/// let mut input = String::new();
/// io::stdin().read_line(&mut input)?;
/// ```
# fn f() {}
```

The problem is that `?` returns a `Result<T, E>` and test functions don't
return anything, so this will give a mismatched types error.

You can get around this limitation by manually adding a `main` that returns
`Result<T, E>`, because `Result<T, E>` implements the `Termination` trait:

```rust,no_run
/// A doc test using ?
///
/// ```
/// use std::io;
///
/// fn main() -> io::Result<()> {
///     let mut input = String::new();
///     io::stdin().read_line(&mut input)?;
///     Ok(())
/// }
/// ```
# fn f() {}
```

Together with the `# ` from the section above, you arrive at a solution that
appears to the reader as the initial idea but works with doc tests:

```rust,no_run
/// ```
/// use std::io;
/// # fn main() -> io::Result<()> {
/// let mut input = String::new();
/// io::stdin().read_line(&mut input)?;
/// # Ok(())
/// # }
/// ```
# fn f() {}
```

As of version 1.34.0, one can also omit the `fn main()`, but you will have to
disambiguate the error type:

```rust,no_run
/// ```
/// use std::io;
/// let mut input = String::new();
/// io::stdin().read_line(&mut input)?;
/// # Ok::<(), io::Error>(())
/// ```
# fn f() {}
```

This is an unfortunate consequence of the `?` operator adding an implicit
conversion, so type inference fails because the type is not unique. Please note
that you must write the `(())` in one sequence without intermediate whitespace
so that `rustdoc` understands you want an implicit `Result`-returning function.

## Showing warnings in doctests

You can show warnings in doctests by running `rustdoc --test --test-args=--show-output`
(or, if you're using cargo, `cargo test --doc -- --show-output`).
By default, this will still hide `unused` warnings, since so many examples use private functions;
you can add `#![warn(unused)]` to the top of your example if you want to see unused variables or dead code warnings.
You can also use [`#![doc(test(attr(warn(unused))))]`][test-attr] in the crate root to enable warnings globally.

[test-attr]: the-doc-attribute.md#testattr

## Documenting macros

Here’s an example of documenting a macro:

```rust
/// Panic with a given message unless an expression evaluates to true.
///
/// # Examples
///
/// ```
/// # #[macro_use] extern crate foo;
/// # fn main() {
/// panic_unless!(1 + 1 == 2, “Math is broken.”);
/// # }
/// ```
///
/// ```should_panic
/// # #[macro_use] extern crate foo;
/// # fn main() {
/// panic_unless!(true == false, “I’m broken.”);
/// # }
/// ```
#[macro_export]
macro_rules! panic_unless {
    ($condition:expr, $($rest:expr),+) => ({ if ! $condition { panic!($($rest),+); } });
}
# fn main() {}
```

You’ll note three things: we need to add our own `extern crate` line, so that
we can add the `#[macro_use]` attribute. Second, we’ll need to add our own
`main()` as well (for reasons discussed above). Finally, a judicious use of
`#` to comment out those two things, so they don’t show up in the output.

## Attributes

Code blocks can be annotated with attributes that help `rustdoc` do the right
thing when testing your code:

The `ignore` attribute tells Rust to ignore your code. This is almost never
what you want as it's the most generic. Instead, consider annotating it
with `text` if it's not code or using `#`s to get a working example that
only shows the part you care about.

```rust
/// ```ignore
/// fn foo() {
/// ```
# fn foo() {}
```

`should_panic` tells `rustdoc` that the code should compile correctly but
panic during execution. If the code doesn't panic, the test will fail.

```rust
/// ```should_panic
/// assert!(false);
/// ```
# fn foo() {}
```

The `no_run` attribute will compile your code but not run it. This is
important for examples such as "Here's how to retrieve a web page,"
which you would want to ensure compiles, but might be run in a test
environment that has no network access. This attribute can also be
used to demonstrate code snippets that can cause Undefined Behavior.

```rust
/// ```no_run
/// loop {
///     println!("Hello, world");
/// }
/// ```
# fn foo() {}
```

`compile_fail` tells `rustdoc` that the compilation should fail. If it
compiles, then the test will fail. However, please note that code failing
with the current Rust release may work in a future release, as new features
are added.

```rust
/// ```compile_fail
/// let x = 5;
/// x += 2; // shouldn't compile!
/// ```
# fn foo() {}
```

`edition2015`, `edition2018`, `edition2021`, and `edition2024` tell `rustdoc`
that the code sample should be compiled using the respective edition of Rust.

```rust
/// Only runs on the 2018 edition.
///
/// ```edition2018
/// let result: Result<i32, ParseIntError> = try {
///     "1".parse::<i32>()?
///         + "2".parse::<i32>()?
///         + "3".parse::<i32>()?
/// };
/// ```
# fn foo() {}
```

Starting in the 2024 edition[^edition-note], compatible doctests are merged as one before being
run. We combine doctests for performance reasons: the slowest part of doctests is to compile them.
Merging all of them into one file and compiling this new file, then running the doctests is much
faster. Whether doctests are merged or not, they are run in their own process.

An example of time spent when running doctests:

[sysinfo crate](https://crates.io/crates/sysinfo):

```text
wall-time duration: 4.59s
total compile time: 27.067s
total runtime: 3.969s
```

Rust core library:

```text
wall-time duration: 102s
total compile time: 775.204s
total runtime: 15.487s
```

[^edition-note]: This is based on the edition of the whole crate, not the edition of the individual
test case that may be specified in its code attribute.

In some cases, doctests cannot be merged. For example, if you have:

```rust
//! ```
//! let location = std::panic::Location::caller();
//! assert_eq!(location.line(), 4);
//! ```
```

The problem with this code is that, if you change any other doctests, it'll likely break when
running `rustdoc --test`, making it tricky to maintain.

This is where the `standalone_crate` attribute comes in: it tells `rustdoc` that a doctest
should not be merged with the others. So the previous code should use it:

```rust
//! ```standalone_crate
//! let location = std::panic::Location::caller();
//! assert_eq!(location.line(), 4);
//! ```
```

In this case, it means that the line information will not change if you add/remove other
doctests.

### Ignoring targets

Attributes starting with `ignore-` can be used to ignore doctests for specific
targets. For example, `ignore-x86_64` will avoid building doctests when the
target name contains `x86_64`.

```rust
/// ```ignore-x86_64
/// assert!(2 == 2);
/// ```
struct Foo;
```

This doctest will not be built for targets such as `x86_64-unknown-linux-gnu`.

Multiple ignore attributes can be specified to ignore multiple targets:

```rust
/// ```ignore-x86_64,ignore-windows
/// assert!(2 == 2);
/// ```
struct Foo;
```

If you want to preserve backwards compatibility for older versions of rustdoc,
you can specify both `ignore` and `ignore-`, such as:

```rust
/// ```ignore,ignore-x86_64
/// assert!(2 == 2);
/// ```
struct Foo;
```

In older versions, this will be ignored on all targets, but starting with
version 1.88.0, `ignore-x86_64` will override `ignore`.

### Custom CSS classes for code blocks

```rust
/// ```custom,{class=language-c}
/// int main(void) { return 0; }
/// ```
pub struct Bar;
```

The text `int main(void) { return 0; }` is rendered without highlighting in a code block
with the class `language-c`. This can be used to highlight other languages through JavaScript
libraries for example.

Without the `custom` attribute, it would be generated as a Rust code example with an additional
`language-C` CSS class. Therefore, if you specifically don't want it to be a Rust code example,
don't forget to add the `custom` attribute.

To be noted that you can replace `class=` with `.` to achieve the same result:

```rust
/// ```custom,{.language-c}
/// int main(void) { return 0; }
/// ```
pub struct Bar;
```

To be noted, `rust` and `.rust`/`class=rust` have different effects: `rust` indicates that this is
a Rust code block whereas the two others add a "rust" CSS class on the code block.

You can also use double quotes:

```rust
/// ```"not rust" {."hello everyone"}
/// int main(void) { return 0; }
/// ```
pub struct Bar;
```

## Syntax reference

The *exact* syntax for code blocks, including the edge cases, can be found
in the [Fenced Code Blocks](https://spec.commonmark.org/0.29/#fenced-code-blocks)
section of the CommonMark specification.

Rustdoc also accepts *indented* code blocks as an alternative to fenced
code blocks: instead of surrounding your code with three backticks, you
can indent each line by four or more spaces.

``````markdown
    let foo = "foo";
    assert_eq!(foo, "foo");
``````

These, too, are documented in the CommonMark specification, in the
[Indented Code Blocks](https://spec.commonmark.org/0.29/#indented-code-blocks)
section.

However, it's preferable to use fenced code blocks over indented code blocks.
Not only are fenced code blocks considered more idiomatic for Rust code,
but there is no way to use attributes such as `ignore` or `should_panic` with
indented code blocks.

### Include items only when collecting doctests

Rustdoc's documentation tests can do some things that regular unit tests can't, so it can
sometimes be useful to extend your doctests with samples that wouldn't otherwise need to be in
documentation. To this end, Rustdoc allows you to have certain items only appear when it's
collecting doctests, so you can utilize doctest functionality without forcing the test to appear in
docs, or to find an arbitrary private item to include it on.

When compiling a crate for use in doctests (with `--test` option), `rustdoc` will set `#[cfg(doctest)]`.
Note that they will still link against only the public items of your crate; if you need to test
private items, you need to write a unit test.

In this example, we're adding doctests that we know won't compile, to verify that our struct can
only take in valid data:

```rust
/// We have a struct here. Remember it doesn't accept negative numbers!
pub struct MyStruct(pub usize);

/// ```compile_fail
/// let x = my_crate::MyStruct(-5);
/// ```
#[cfg(doctest)]
pub struct MyStructOnlyTakesUsize;
```

Note that the struct `MyStructOnlyTakesUsize` here isn't actually part of your public crate
API. The use of `#[cfg(doctest)]` makes sure that this struct only exists while `rustdoc` is
collecting doctests. This means that its doctest is executed when `--test` is passed to rustdoc,
but is hidden from the public documentation.

Another possible use of `#[cfg(doctest)]` is to test doctests that are included in your README file
without including it in your main documentation. For example, you could write this into your
`lib.rs` to test your README as part of your doctests:

```rust,no_run
#[doc = include_str!("../README.md")]
#[cfg(doctest)]
pub struct ReadmeDoctests;
```

This will include your README as documentation on the hidden struct `ReadmeDoctests`, which will
then be tested alongside the rest of your doctests.

## Controlling the compilation and run directories

By default, `rustdoc --test` will compile and run documentation test examples
from the same working directory.
The compilation directory is being used for compiler diagnostics, the `file!()` macro and
the output of `rustdoc` test runner itself, whereas the run directory has an influence on file-system
operations within documentation test examples, such as `std::fs::read_to_string`.

The `--test-run-directory` flag allows controlling the run directory separately from the compilation directory.
This is particularly useful in workspaces, where compiler invocations and thus diagnostics should be
relative to the workspace directory, but documentation test examples should run relative to the crate directory.
