<!-- Old headings. Do not remove or links may break. -->

<a id="managing-growing-projects-with-packages-crates-and-modules"></a>

# Packages, Crates, and Modules

As you write large programs, organizing your code will become increasingly
important. By grouping related functionality and separating code with distinct
features, you’ll clarify where to find code that implements a particular
feature and where to go to change how a feature works.

The programs we’ve written so far have been in one module in one file. As a
project grows, you should organize code by splitting it into multiple modules
and then multiple files. A package can contain multiple binary crates and
optionally one library crate. As a package grows, you can extract parts into
separate crates that become external dependencies. This chapter covers all
these techniques. For very large projects comprising a set of interrelated
packages that evolve together, Cargo provides workspaces, which we’ll cover in
[“Cargo Workspaces”][workspaces]<!-- ignore --> in Chapter 14.

We’ll also discuss encapsulating implementation details, which lets you reuse
code at a higher level: Once you’ve implemented an operation, other code can
call your code via its public interface without having to know how the
implementation works. The way you write code defines which parts are public for
other code to use and which parts are private implementation details that you
reserve the right to change. This is another way to limit the amount of detail
you have to keep in your head.

A related concept is scope: The nested context in which code is written has a
set of names that are defined as “in scope.” When reading, writing, and
compiling code, programmers and compilers need to know whether a particular
name at a particular spot refers to a variable, function, struct, enum, module,
constant, or other item and what that item means. You can create scopes and
change which names are in or out of scope. You can’t have two items with the
same name in the same scope; tools are available to resolve name conflicts.

Rust has a number of features that allow you to manage your code’s
organization, including which details are exposed, which details are private,
and what names are in each scope in your programs. These features, sometimes
collectively referred to as the _module system_, include:

* **Packages**: A Cargo feature that lets you build, test, and share crates
* **Crates**: A tree of modules that produces a library or executable
* **Modules and use**: Let you control the organization, scope, and privacy of
paths
* **Paths**: A way of naming an item, such as a struct, function, or module

In this chapter, we’ll cover all these features, discuss how they interact, and
explain how to use them to manage scope. By the end, you should have a solid
understanding of the module system and be able to work with scopes like a pro!

[workspaces]: ch14-03-cargo-workspaces.html


---

## Packages and Crates

The first parts of the module system we’ll cover are packages and crates.

A _crate_ is the smallest amount of code that the Rust compiler considers at a
time. Even if you run `rustc` rather than `cargo` and pass a single source code
file (as we did all the way back in [“Rust Program Basics”][basics]<!-- ignore
--> in Chapter 1), the compiler considers that file to be a crate. Crates can
contain modules, and the modules may be defined in other files that get
compiled with the crate, as we’ll see in the coming sections.

A crate can come in one of two forms: a binary crate or a library crate.
_Binary crates_ are programs you can compile to an executable that you can run,
such as a command line program or a server. Each must have a function called
`main` that defines what happens when the executable runs. All the crates we’ve
created so far have been binary crates.

_Library crates_ don’t have a `main` function, and they don’t compile to an
executable. Instead, they define functionality intended to be shared with
multiple projects. For example, the `rand` crate we used in [Chapter
2][rand]<!-- ignore --> provides functionality that generates random numbers.
Most of the time when Rustaceans say “crate,” they mean library crate, and they
use “crate” interchangeably with the general programming concept of a “library.”

The _crate root_ is a source file that the Rust compiler starts from and makes
up the root module of your crate (we’ll explain modules in depth in [“Control
Scope and Privacy with Modules”][modules]<!-- ignore -->).

A _package_ is a bundle of one or more crates that provides a set of
functionality. A package contains a _Cargo.toml_ file that describes how to
build those crates. Cargo is actually a package that contains the binary crate
for the command line tool you’ve been using to build your code. The Cargo
package also contains a library crate that the binary crate depends on. Other
projects can depend on the Cargo library crate to use the same logic the Cargo
command line tool uses.

A package can contain as many binary crates as you like, but at most only one
library crate. A package must contain at least one crate, whether that’s a
library or binary crate.

Let’s walk through what happens when we create a package. First, we enter the
command `cargo new my-project`:

```console
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

After we run `cargo new my-project`, we use `ls` to see what Cargo creates. In
the _my-project_ directory, there’s a _Cargo.toml_ file, giving us a package.
There’s also a _src_ directory that contains _main.rs_. Open _Cargo.toml_ in
your text editor and note that there’s no mention of _src/main.rs_. Cargo
follows a convention that _src/main.rs_ is the crate root of a binary crate
with the same name as the package. Likewise, Cargo knows that if the package
directory contains _src/lib.rs_, the package contains a library crate with the
same name as the package, and _src/lib.rs_ is its crate root. Cargo passes the
crate root files to `rustc` to build the library or binary.

Here, we have a package that only contains _src/main.rs_, meaning it only
contains a binary crate named `my-project`. If a package contains _src/main.rs_
and _src/lib.rs_, it has two crates: a binary and a library, both with the same
name as the package. A package can have multiple binary crates by placing files
in the _src/bin_ directory: Each file will be a separate binary crate.

[basics]: ch01-02-hello-world.html#rust-program-basics
[modules]: ch07-02-defining-modules-to-control-scope-and-privacy.html
[rand]: ch02-00-guessing-game-tutorial.html#generating-a-random-number


---

<!-- Old headings. Do not remove or links may break. -->

<a id="defining-modules-to-control-scope-and-privacy"></a>

## Control Scope and Privacy with Modules

In this section, we’ll talk about modules and other parts of the module system,
namely _paths_, which allow you to name items; the `use` keyword that brings a
path into scope; and the `pub` keyword to make items public. We’ll also discuss
the `as` keyword, external packages, and the glob operator.

### Modules Cheat Sheet

Before we get to the details of modules and paths, here we provide a quick
reference on how modules, paths, the `use` keyword, and the `pub` keyword work
in the compiler, and how most developers organize their code. We’ll be going
through examples of each of these rules throughout this chapter, but this is a
great place to refer to as a reminder of how modules work.

- **Start from the crate root**: When compiling a crate, the compiler first
  looks in the crate root file (usually _src/lib.rs_ for a library crate and
  _src/main.rs_ for a binary crate) for code to compile.
- **Declaring modules**: In the crate root file, you can declare new modules;
  say you declare a “garden” module with `mod garden;`. The compiler will look
  for the module’s code in these places:
  - Inline, within curly brackets that replace the semicolon following `mod
    garden`
  - In the file _src/garden.rs_
  - In the file _src/garden/mod.rs_
- **Declaring submodules**: In any file other than the crate root, you can
  declare submodules. For example, you might declare `mod vegetables;` in
  _src/garden.rs_. The compiler will look for the submodule’s code within the
  directory named for the parent module in these places:
  - Inline, directly following `mod vegetables`, within curly brackets instead
    of the semicolon
  - In the file _src/garden/vegetables.rs_
  - In the file _src/garden/vegetables/mod.rs_
- **Paths to code in modules**: Once a module is part of your crate, you can
  refer to code in that module from anywhere else in that same crate, as long
  as the privacy rules allow, using the path to the code. For example, an
  `Asparagus` type in the garden vegetables module would be found at
  `crate::garden::vegetables::Asparagus`.
- **Private vs. public**: Code within a module is private from its parent
  modules by default. To make a module public, declare it with `pub mod`
  instead of `mod`. To make items within a public module public as well, use
  `pub` before their declarations.
- **The `use` keyword**: Within a scope, the `use` keyword creates shortcuts to
  items to reduce repetition of long paths. In any scope that can refer to
  `crate::garden::vegetables::Asparagus`, you can create a shortcut with `use
  crate::garden::vegetables::Asparagus;`, and from then on you only need to
  write `Asparagus` to make use of that type in the scope.

Here, we create a binary crate named `backyard` that illustrates these rules.
The crate’s directory, also named _backyard_, contains these files and
directories:

```text
backyard
├── Cargo.lock
├── Cargo.toml
└── src
    ├── garden
    │   └── vegetables.rs
    ├── garden.rs
    └── main.rs
```

The crate root file in this case is _src/main.rs_, and it contains:

<Listing file-name="src/main.rs">

```rust,noplayground,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/quick-reference-example/src/main.rs}}
```

</Listing>

The `pub mod garden;` line tells the compiler to include the code it finds in
_src/garden.rs_, which is:

<Listing file-name="src/garden.rs">

```rust,noplayground,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/quick-reference-example/src/garden.rs}}
```

</Listing>

Here, `pub mod vegetables;` means the code in _src/garden/vegetables.rs_ is
included too. That code is:

```rust,noplayground,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/quick-reference-example/src/garden/vegetables.rs}}
```

Now let’s get into the details of these rules and demonstrate them in action!

### Grouping Related Code in Modules

_Modules_ let us organize code within a crate for readability and easy reuse.
Modules also allow us to control the _privacy_ of items because code within a
module is private by default. Private items are internal implementation details
not available for outside use. We can choose to make modules and the items
within them public, which exposes them to allow external code to use and depend
on them.

As an example, let’s write a library crate that provides the functionality of a
restaurant. We’ll define the signatures of functions but leave their bodies
empty to concentrate on the organization of the code rather than the
implementation of a restaurant.

In the restaurant industry, some parts of a restaurant are referred to as front
of house and others as back of house. _Front of house_ is where customers are;
this encompasses where the hosts seat customers, servers take orders and
payment, and bartenders make drinks. _Back of house_ is where the chefs and
cooks work in the kitchen, dishwashers clean up, and managers do administrative
work.

To structure our crate in this way, we can organize its functions into nested
modules. Create a new library named `restaurant` by running `cargo new
restaurant --lib`. Then, enter the code in Listing 7-1 into _src/lib.rs_ to
define some modules and function signatures; this code is the front of house
section.

<Listing number="7-1" file-name="src/lib.rs" caption="A `front_of_house` module containing other modules that then contain functions">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-01/src/lib.rs}}
```

</Listing>

We define a module with the `mod` keyword followed by the name of the module
(in this case, `front_of_house`). The body of the module then goes inside curly
brackets. Inside modules, we can place other modules, as in this case with the
modules `hosting` and `serving`. Modules can also hold definitions for other
items, such as structs, enums, constants, traits, and as in Listing 7-1,
functions.

By using modules, we can group related definitions together and name why
they’re related. Programmers using this code can navigate the code based on the
groups rather than having to read through all the definitions, making it easier
to find the definitions relevant to them. Programmers adding new functionality
to this code would know where to place the code to keep the program organized.

Earlier, we mentioned that _src/main.rs_ and _src/lib.rs_ are called _crate
roots_. The reason for their name is that the contents of either of these two
files form a module named `crate` at the root of the crate’s module structure,
known as the _module tree_.

Listing 7-2 shows the module tree for the structure in Listing 7-1.

<Listing number="7-2" caption="The module tree for the code in Listing 7-1">

```text
crate
 └── front_of_house
     ├── hosting
     │   ├── add_to_waitlist
     │   └── seat_at_table
     └── serving
         ├── take_order
         ├── serve_order
         └── take_payment
```

</Listing>

This tree shows how some of the modules nest inside other modules; for example,
`hosting` nests inside `front_of_house`. The tree also shows that some modules
are _siblings_, meaning they’re defined in the same module; `hosting` and
`serving` are siblings defined within `front_of_house`. If module A is
contained inside module B, we say that module A is the _child_ of module B and
that module B is the _parent_ of module A. Notice that the entire module tree
is rooted under the implicit module named `crate`.

The module tree might remind you of the filesystem’s directory tree on your
computer; this is a very apt comparison! Just like directories in a filesystem,
you use modules to organize your code. And just like files in a directory, we
need a way to find our modules.


---

## Paths for Referring to an Item in the Module Tree

To show Rust where to find an item in a module tree, we use a path in the same
way we use a path when navigating a filesystem. To call a function, we need to
know its path.

A path can take two forms:

- An _absolute path_ is the full path starting from a crate root; for code
  from an external crate, the absolute path begins with the crate name, and for
  code from the current crate, it starts with the literal `crate`.
- A _relative path_ starts from the current module and uses `self`, `super`, or
  an identifier in the current module.

Both absolute and relative paths are followed by one or more identifiers
separated by double colons (`::`).

Returning to Listing 7-1, say we want to call the `add_to_waitlist` function.
This is the same as asking: What’s the path of the `add_to_waitlist` function?
Listing 7-3 contains Listing 7-1 with some of the modules and functions removed.

We’ll show two ways to call the `add_to_waitlist` function from a new function,
`eat_at_restaurant`, defined in the crate root. These paths are correct, but
there’s another problem remaining that will prevent this example from compiling
as is. We’ll explain why in a bit.

The `eat_at_restaurant` function is part of our library crate’s public API, so
we mark it with the `pub` keyword. In the [“Exposing Paths with the `pub`
Keyword”][pub]<!-- ignore --> section, we’ll go into more detail about `pub`.

<Listing number="7-3" file-name="src/lib.rs" caption="Calling the `add_to_waitlist` function using absolute and relative paths">

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-03/src/lib.rs}}
```

</Listing>

The first time we call the `add_to_waitlist` function in `eat_at_restaurant`,
we use an absolute path. The `add_to_waitlist` function is defined in the same
crate as `eat_at_restaurant`, which means we can use the `crate` keyword to
start an absolute path. We then include each of the successive modules until we
make our way to `add_to_waitlist`. You can imagine a filesystem with the same
structure: We’d specify the path `/front_of_house/hosting/add_to_waitlist` to
run the `add_to_waitlist` program; using the `crate` name to start from the
crate root is like using `/` to start from the filesystem root in your shell.

The second time we call `add_to_waitlist` in `eat_at_restaurant`, we use a
relative path. The path starts with `front_of_house`, the name of the module
defined at the same level of the module tree as `eat_at_restaurant`. Here the
filesystem equivalent would be using the path
`front_of_house/hosting/add_to_waitlist`. Starting with a module name means
that the path is relative.

Choosing whether to use a relative or absolute path is a decision you’ll make
based on your project, and it depends on whether you’re more likely to move
item definition code separately from or together with the code that uses the
item. For example, if we moved the `front_of_house` module and the
`eat_at_restaurant` function into a module named `customer_experience`, we’d
need to update the absolute path to `add_to_waitlist`, but the relative path
would still be valid. However, if we moved the `eat_at_restaurant` function
separately into a module named `dining`, the absolute path to the
`add_to_waitlist` call would stay the same, but the relative path would need to
be updated. Our preference in general is to specify absolute paths because it’s
more likely we’ll want to move code definitions and item calls independently of
each other.

Let’s try to compile Listing 7-3 and find out why it won’t compile yet! The
errors we get are shown in Listing 7-4.

<Listing number="7-4" caption="Compiler errors from building the code in Listing 7-3">

```console
{{#include ../listings/ch07-managing-growing-projects/listing-07-03/output.txt}}
```

</Listing>

The error messages say that module `hosting` is private. In other words, we
have the correct paths for the `hosting` module and the `add_to_waitlist`
function, but Rust won’t let us use them because it doesn’t have access to the
private sections. In Rust, all items (functions, methods, structs, enums,
modules, and constants) are private to parent modules by default. If you want
to make an item like a function or struct private, you put it in a module.

Items in a parent module can’t use the private items inside child modules, but
items in child modules can use the items in their ancestor modules. This is
because child modules wrap and hide their implementation details, but the child
modules can see the context in which they’re defined. To continue with our
metaphor, think of the privacy rules as being like the back office of a
restaurant: What goes on in there is private to restaurant customers, but
office managers can see and do everything in the restaurant they operate.

Rust chose to have the module system function this way so that hiding inner
implementation details is the default. That way, you know which parts of the
inner code you can change without breaking the outer code. However, Rust does
give you the option to expose inner parts of child modules’ code to outer
ancestor modules by using the `pub` keyword to make an item public.

### Exposing Paths with the `pub` Keyword

Let’s return to the error in Listing 7-4 that told us the `hosting` module is
private. We want the `eat_at_restaurant` function in the parent module to have
access to the `add_to_waitlist` function in the child module, so we mark the
`hosting` module with the `pub` keyword, as shown in Listing 7-5.

<Listing number="7-5" file-name="src/lib.rs" caption="Declaring the `hosting` module as `pub` to use it from `eat_at_restaurant`">

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-05/src/lib.rs:here}}
```

</Listing>

Unfortunately, the code in Listing 7-5 still results in compiler errors, as
shown in Listing 7-6.

<Listing number="7-6" caption="Compiler errors from building the code in Listing 7-5">

```console
{{#include ../listings/ch07-managing-growing-projects/listing-07-05/output.txt}}
```

</Listing>

What happened? Adding the `pub` keyword in front of `mod hosting` makes the
module public. With this change, if we can access `front_of_house`, we can
access `hosting`. But the _contents_ of `hosting` are still private; making the
module public doesn’t make its contents public. The `pub` keyword on a module
only lets code in its ancestor modules refer to it, not access its inner code.
Because modules are containers, there’s not much we can do by only making the
module public; we need to go further and choose to make one or more of the
items within the module public as well.

The errors in Listing 7-6 say that the `add_to_waitlist` function is private.
The privacy rules apply to structs, enums, functions, and methods as well as
modules.

Let’s also make the `add_to_waitlist` function public by adding the `pub`
keyword before its definition, as in Listing 7-7.

<Listing number="7-7" file-name="src/lib.rs" caption="Adding the `pub` keyword to `mod hosting` and `fn add_to_waitlist` lets us call the function from `eat_at_restaurant`.">

```rust,noplayground,test_harness
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-07/src/lib.rs:here}}
```

</Listing>

Now the code will compile! To see why adding the `pub` keyword lets us use
these paths in `eat_at_restaurant` with respect to the privacy rules, let’s
look at the absolute and the relative paths.

In the absolute path, we start with `crate`, the root of our crate’s module
tree. The `front_of_house` module is defined in the crate root. While
`front_of_house` isn’t public, because the `eat_at_restaurant` function is
defined in the same module as `front_of_house` (that is, `eat_at_restaurant`
and `front_of_house` are siblings), we can refer to `front_of_house` from
`eat_at_restaurant`. Next is the `hosting` module marked with `pub`. We can
access the parent module of `hosting`, so we can access `hosting`. Finally, the
`add_to_waitlist` function is marked with `pub`, and we can access its parent
module, so this function call works!

In the relative path, the logic is the same as the absolute path except for the
first step: Rather than starting from the crate root, the path starts from
`front_of_house`. The `front_of_house` module is defined within the same module
as `eat_at_restaurant`, so the relative path starting from the module in which
`eat_at_restaurant` is defined works. Then, because `hosting` and
`add_to_waitlist` are marked with `pub`, the rest of the path works, and this
function call is valid!

If you plan to share your library crate so that other projects can use your
code, your public API is your contract with users of your crate that determines
how they can interact with your code. There are many considerations around
managing changes to your public API to make it easier for people to depend on
your crate. These considerations are beyond the scope of this book; if you’re
interested in this topic, see [the Rust API Guidelines][api-guidelines].

> #### Best Practices for Packages with a Binary and a Library
>
> We mentioned that a package can contain both a _src/main.rs_ binary crate
> root as well as a _src/lib.rs_ library crate root, and both crates will have
> the package name by default. Typically, packages with this pattern of
> containing both a library and a binary crate will have just enough code in the
> binary crate to start an executable that calls code defined in the library
> crate. This lets other projects benefit from the most functionality that the
> package provides because the library crate’s code can be shared.
>
> The module tree should be defined in _src/lib.rs_. Then, any public items can
> be used in the binary crate by starting paths with the name of the package.
> The binary crate becomes a user of the library crate just like a completely
> external crate would use the library crate: It can only use the public API.
> This helps you design a good API; not only are you the author, but you’re
> also a client!
>
> In [Chapter 12][ch12]<!-- ignore -->, we’ll demonstrate this organizational
> practice with a command line program that will contain both a binary crate
> and a library crate.

### Starting Relative Paths with `super`

We can construct relative paths that begin in the parent module, rather than
the current module or the crate root, by using `super` at the start of the
path. This is like starting a filesystem path with the `..` syntax that means
to go to the parent directory. Using `super` allows us to reference an item
that we know is in the parent module, which can make rearranging the module
tree easier when the module is closely related to the parent but the parent
might be moved elsewhere in the module tree someday.

Consider the code in Listing 7-8 that models the situation in which a chef
fixes an incorrect order and personally brings it out to the customer. The
function `fix_incorrect_order` defined in the `back_of_house` module calls the
function `deliver_order` defined in the parent module by specifying the path to
`deliver_order`, starting with `super`.

<Listing number="7-8" file-name="src/lib.rs" caption="Calling a function using a relative path starting with `super`">

```rust,noplayground,test_harness
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-08/src/lib.rs}}
```

</Listing>

The `fix_incorrect_order` function is in the `back_of_house` module, so we can
use `super` to go to the parent module of `back_of_house`, which in this case
is `crate`, the root. From there, we look for `deliver_order` and find it.
Success! We think the `back_of_house` module and the `deliver_order` function
are likely to stay in the same relationship to each other and get moved
together should we decide to reorganize the crate’s module tree. Therefore, we
used `super` so that we’ll have fewer places to update code in the future if
this code gets moved to a different module.

### Making Structs and Enums Public

We can also use `pub` to designate structs and enums as public, but there are a
few extra details to the usage of `pub` with structs and enums. If we use `pub`
before a struct definition, we make the struct public, but the struct’s fields
will still be private. We can make each field public or not on a case-by-case
basis. In Listing 7-9, we’ve defined a public `back_of_house::Breakfast` struct
with a public `toast` field but a private `seasonal_fruit` field. This models
the case in a restaurant where the customer can pick the type of bread that
comes with a meal, but the chef decides which fruit accompanies the meal based
on what’s in season and in stock. The available fruit changes quickly, so
customers can’t choose the fruit or even see which fruit they’ll get.

<Listing number="7-9" file-name="src/lib.rs" caption="A struct with some public fields and some private fields">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-09/src/lib.rs}}
```

</Listing>

Because the `toast` field in the `back_of_house::Breakfast` struct is public,
in `eat_at_restaurant` we can write and read to the `toast` field using dot
notation. Notice that we can’t use the `seasonal_fruit` field in
`eat_at_restaurant`, because `seasonal_fruit` is private. Try uncommenting the
line modifying the `seasonal_fruit` field value to see what error you get!

Also, note that because `back_of_house::Breakfast` has a private field, the
struct needs to provide a public associated function that constructs an
instance of `Breakfast` (we’ve named it `summer` here). If `Breakfast` didn’t
have such a function, we couldn’t create an instance of `Breakfast` in
`eat_at_restaurant`, because we couldn’t set the value of the private
`seasonal_fruit` field in `eat_at_restaurant`.

In contrast, if we make an enum public, all of its variants are then public. We
only need the `pub` before the `enum` keyword, as shown in Listing 7-10.

<Listing number="7-10" file-name="src/lib.rs" caption="Designating an enum as public makes all its variants public.">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-10/src/lib.rs}}
```

</Listing>

Because we made the `Appetizer` enum public, we can use the `Soup` and `Salad`
variants in `eat_at_restaurant`.

Enums aren’t very useful unless their variants are public; it would be annoying
to have to annotate all enum variants with `pub` in every case, so the default
for enum variants is to be public. Structs are often useful without their
fields being public, so struct fields follow the general rule of everything
being private by default unless annotated with `pub`.

There’s one more situation involving `pub` that we haven’t covered, and that is
our last module system feature: the `use` keyword. We’ll cover `use` by itself
first, and then we’ll show how to combine `pub` and `use`.

[pub]: ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html#exposing-paths-with-the-pub-keyword
[api-guidelines]: https://rust-lang.github.io/api-guidelines/
[ch12]: ch12-00-an-io-project.html


---

## Bringing Paths into Scope with the `use` Keyword

Having to write out the paths to call functions can feel inconvenient and
repetitive. In Listing 7-7, whether we chose the absolute or relative path to
the `add_to_waitlist` function, every time we wanted to call `add_to_waitlist`
we had to specify `front_of_house` and `hosting` too. Fortunately, there’s a
way to simplify this process: We can create a shortcut to a path with the `use`
keyword once and then use the shorter name everywhere else in the scope.

In Listing 7-11, we bring the `crate::front_of_house::hosting` module into the
scope of the `eat_at_restaurant` function so that we only have to specify
`hosting::add_to_waitlist` to call the `add_to_waitlist` function in
`eat_at_restaurant`.

<Listing number="7-11" file-name="src/lib.rs" caption="Bringing a module into scope with `use`">

```rust,noplayground,test_harness
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-11/src/lib.rs}}
```

</Listing>

Adding `use` and a path in a scope is similar to creating a symbolic link in
the filesystem. By adding `use crate::front_of_house::hosting` in the crate
root, `hosting` is now a valid name in that scope, just as though the `hosting`
module had been defined in the crate root. Paths brought into scope with `use`
also check privacy, like any other paths.

Note that `use` only creates the shortcut for the particular scope in which the
`use` occurs. Listing 7-12 moves the `eat_at_restaurant` function into a new
child module named `customer`, which is then a different scope than the `use`
statement, so the function body won’t compile.

<Listing number="7-12" file-name="src/lib.rs" caption="A `use` statement only applies in the scope it’s in.">

```rust,noplayground,test_harness,does_not_compile,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-12/src/lib.rs}}
```

</Listing>

The compiler error shows that the shortcut no longer applies within the
`customer` module:

```console
{{#include ../listings/ch07-managing-growing-projects/listing-07-12/output.txt}}
```

Notice there’s also a warning that the `use` is no longer used in its scope! To
fix this problem, move the `use` within the `customer` module too, or reference
the shortcut in the parent module with `super::hosting` within the child
`customer` module.

### Creating Idiomatic `use` Paths

In Listing 7-11, you might have wondered why we specified `use
crate::front_of_house::hosting` and then called `hosting::add_to_waitlist` in
`eat_at_restaurant`, rather than specifying the `use` path all the way out to
the `add_to_waitlist` function to achieve the same result, as in Listing 7-13.

<Listing number="7-13" file-name="src/lib.rs" caption="Bringing the `add_to_waitlist` function into scope with `use`, which is unidiomatic">

```rust,noplayground,test_harness
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-13/src/lib.rs}}
```

</Listing>

Although both Listing 7-11 and Listing 7-13 accomplish the same task, Listing
7-11 is the idiomatic way to bring a function into scope with `use`. Bringing
the function’s parent module into scope with `use` means we have to specify the
parent module when calling the function. Specifying the parent module when
calling the function makes it clear that the function isn’t locally defined
while still minimizing repetition of the full path. The code in Listing 7-13 is
unclear as to where `add_to_waitlist` is defined.

On the other hand, when bringing in structs, enums, and other items with `use`,
it’s idiomatic to specify the full path. Listing 7-14 shows the idiomatic way
to bring the standard library’s `HashMap` struct into the scope of a binary
crate.

<Listing number="7-14" file-name="src/main.rs" caption="Bringing `HashMap` into scope in an idiomatic way">

```rust
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-14/src/main.rs}}
```

</Listing>

There’s no strong reason behind this idiom: It’s just the convention that has
emerged, and folks have gotten used to reading and writing Rust code this way.

The exception to this idiom is if we’re bringing two items with the same name
into scope with `use` statements, because Rust doesn’t allow that. Listing 7-15
shows how to bring two `Result` types into scope that have the same name but
different parent modules, and how to refer to them.

<Listing number="7-15" file-name="src/lib.rs" caption="Bringing two types with the same name into the same scope requires using their parent modules.">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-15/src/lib.rs:here}}
```

</Listing>

As you can see, using the parent modules distinguishes the two `Result` types.
If instead we specified `use std::fmt::Result` and `use std::io::Result`, we’d
have two `Result` types in the same scope, and Rust wouldn’t know which one we
meant when we used `Result`.

### Providing New Names with the `as` Keyword

There’s another solution to the problem of bringing two types of the same name
into the same scope with `use`: After the path, we can specify `as` and a new
local name, or _alias_, for the type. Listing 7-16 shows another way to write
the code in Listing 7-15 by renaming one of the two `Result` types using `as`.

<Listing number="7-16" file-name="src/lib.rs" caption="Renaming a type when it’s brought into scope with the `as` keyword">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-16/src/lib.rs:here}}
```

</Listing>

In the second `use` statement, we chose the new name `IoResult` for the
`std::io::Result` type, which won’t conflict with the `Result` from `std::fmt`
that we’ve also brought into scope. Listing 7-15 and Listing 7-16 are
considered idiomatic, so the choice is up to you!

### Re-exporting Names with `pub use`

When we bring a name into scope with the `use` keyword, the name is private to
the scope into which we imported it. To enable code outside that scope to refer
to that name as if it had been defined in that scope, we can combine `pub` and
`use`. This technique is called _re-exporting_ because we’re bringing an item
into scope but also making that item available for others to bring into their
scope.

Listing 7-17 shows the code in Listing 7-11 with `use` in the root module
changed to `pub use`.

<Listing number="7-17" file-name="src/lib.rs" caption="Making a name available for any code to use from a new scope with `pub use`">

```rust,noplayground,test_harness
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-17/src/lib.rs}}
```

</Listing>

Before this change, external code would have to call the `add_to_waitlist`
function by using the path
`restaurant::front_of_house::hosting::add_to_waitlist()`, which also would have
required the `front_of_house` module to be marked as `pub`. Now that this `pub
use` has re-exported the `hosting` module from the root module, external code
can use the path `restaurant::hosting::add_to_waitlist()` instead.

Re-exporting is useful when the internal structure of your code is different
from how programmers calling your code would think about the domain. For
example, in this restaurant metaphor, the people running the restaurant think
about “front of house” and “back of house.” But customers visiting a restaurant
probably won’t think about the parts of the restaurant in those terms. With `pub
use`, we can write our code with one structure but expose a different structure.
Doing so makes our library well organized for programmers working on the library
and programmers calling the library. We’ll look at another example of `pub use`
and how it affects your crate’s documentation in [“Exporting a Convenient Public
API”][ch14-pub-use]<!-- ignore --> in Chapter 14.

### Using External Packages

In Chapter 2, we programmed a guessing game project that used an external
package called `rand` to get random numbers. To use `rand` in our project, we
added this line to _Cargo.toml_:

<!-- When updating the version of `rand` used, also update the version of
`rand` used in these files so they all match:
* ch02-00-guessing-game-tutorial.md
* ch14-03-cargo-workspaces.md
-->

<Listing file-name="Cargo.toml">

```toml
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-02/Cargo.toml:9:}}
```

</Listing>

Adding `rand` as a dependency in _Cargo.toml_ tells Cargo to download the
`rand` package and any dependencies from [crates.io](https://crates.io/) and
make `rand` available to our project.

Then, to bring `rand` definitions into the scope of our package, we added a
`use` line starting with the name of the crate, `rand`, and listed the items we
wanted to bring into scope. Recall that in [“Generating a Random
Number”][rand]<!-- ignore --> in Chapter 2, we brought the `Rng` trait into
scope and called the `rand::thread_rng` function:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-03/src/main.rs:ch07-04}}
```

Members of the Rust community have made many packages available at
[crates.io](https://crates.io/), and pulling any of them into your package
involves these same steps: listing them in your package’s _Cargo.toml_ file and
using `use` to bring items from their crates into scope.

Note that the standard `std` library is also a crate that’s external to our
package. Because the standard library is shipped with the Rust language, we
don’t need to change _Cargo.toml_ to include `std`. But we do need to refer to
it with `use` to bring items from there into our package’s scope. For example,
with `HashMap` we would use this line:

```rust
use std::collections::HashMap;
```

This is an absolute path starting with `std`, the name of the standard library
crate.

<!-- Old headings. Do not remove or links may break. -->

<a id="using-nested-paths-to-clean-up-large-use-lists"></a>

### Using Nested Paths to Clean Up `use` Lists

If we’re using multiple items defined in the same crate or same module, listing
each item on its own line can take up a lot of vertical space in our files. For
example, these two `use` statements we had in the guessing game in Listing 2-4
bring items from `std` into scope:

<Listing file-name="src/main.rs">

```rust,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/no-listing-01-use-std-unnested/src/main.rs:here}}
```

</Listing>

Instead, we can use nested paths to bring the same items into scope in one
line. We do this by specifying the common part of the path, followed by two
colons, and then curly brackets around a list of the parts of the paths that
differ, as shown in Listing 7-18.

<Listing number="7-18" file-name="src/main.rs" caption="Specifying a nested path to bring multiple items with the same prefix into scope">

```rust,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-18/src/main.rs:here}}
```

</Listing>

In bigger programs, bringing many items into scope from the same crate or
module using nested paths can reduce the number of separate `use` statements
needed by a lot!

We can use a nested path at any level in a path, which is useful when combining
two `use` statements that share a subpath. For example, Listing 7-19 shows two
`use` statements: one that brings `std::io` into scope and one that brings
`std::io::Write` into scope.

<Listing number="7-19" file-name="src/lib.rs" caption="Two `use` statements where one is a subpath of the other">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-19/src/lib.rs}}
```

</Listing>

The common part of these two paths is `std::io`, and that’s the complete first
path. To merge these two paths into one `use` statement, we can use `self` in
the nested path, as shown in Listing 7-20.

<Listing number="7-20" file-name="src/lib.rs" caption="Combining the paths in Listing 7-19 into one `use` statement">

```rust,noplayground
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-20/src/lib.rs}}
```

</Listing>

This line brings `std::io` and `std::io::Write` into scope.

<!-- Old headings. Do not remove or links may break. -->

<a id="the-glob-operator"></a>

### Importing Items with the Glob Operator

If we want to bring _all_ public items defined in a path into scope, we can
specify that path followed by the `*` glob operator:

```rust
use std::collections::*;
```

This `use` statement brings all public items defined in `std::collections` into
the current scope. Be careful when using the glob operator! Glob can make it
harder to tell what names are in scope and where a name used in your program
was defined. Additionally, if the dependency changes its definitions, what
you’ve imported changes as well, which may lead to compiler errors when you
upgrade the dependency if the dependency adds a definition with the same name
as a definition of yours in the same scope, for example.

The glob operator is often used when testing to bring everything under test into
the `tests` module; we’ll talk about that in [“How to Write
Tests”][writing-tests]<!-- ignore --> in Chapter 11. The glob operator is also
sometimes used as part of the prelude pattern: See [the standard library
documentation](../std/prelude/index.html#other-preludes)<!-- ignore --> for more
information on that pattern.

[ch14-pub-use]: ch14-02-publishing-to-crates-io.html#exporting-a-convenient-public-api
[rand]: ch02-00-guessing-game-tutorial.html#generating-a-random-number
[writing-tests]: ch11-01-writing-tests.html#how-to-write-tests


---

## Separating Modules into Different Files

So far, all the examples in this chapter defined multiple modules in one file.
When modules get large, you might want to move their definitions to a separate
file to make the code easier to navigate.

For example, let’s start from the code in Listing 7-17 that had multiple
restaurant modules. We’ll extract modules into files instead of having all the
modules defined in the crate root file. In this case, the crate root file is
_src/lib.rs_, but this procedure also works with binary crates whose crate root
file is _src/main.rs_.

First, we’ll extract the `front_of_house` module to its own file. Remove the
code inside the curly brackets for the `front_of_house` module, leaving only
the `mod front_of_house;` declaration, so that _src/lib.rs_ contains the code
shown in Listing 7-21. Note that this won’t compile until we create the
_src/front_of_house.rs_ file in Listing 7-22.

<Listing number="7-21" file-name="src/lib.rs" caption="Declaring the `front_of_house` module whose body will be in *src/front_of_house.rs*">

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-21-and-22/src/lib.rs}}
```

</Listing>

Next, place the code that was in the curly brackets into a new file named
_src/front_of_house.rs_, as shown in Listing 7-22. The compiler knows to look
in this file because it came across the module declaration in the crate root
with the name `front_of_house`.

<Listing number="7-22" file-name="src/front_of_house.rs" caption="Definitions inside the `front_of_house` module in *src/front_of_house.rs*">

```rust,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/listing-07-21-and-22/src/front_of_house.rs}}
```

</Listing>

Note that you only need to load a file using a `mod` declaration _once_ in your
module tree. Once the compiler knows the file is part of the project (and knows
where in the module tree the code resides because of where you’ve put the `mod`
statement), other files in your project should refer to the loaded file’s code
using a path to where it was declared, as covered in the [“Paths for Referring
to an Item in the Module Tree”][paths]<!-- ignore --> section. In other words,
`mod` is _not_ an “include” operation that you may have seen in other
programming languages.

Next, we’ll extract the `hosting` module to its own file. The process is a bit
different because `hosting` is a child module of `front_of_house`, not of the
root module. We’ll place the file for `hosting` in a new directory that will be
named for its ancestors in the module tree, in this case _src/front_of_house_.

To start moving `hosting`, we change _src/front_of_house.rs_ to contain only
the declaration of the `hosting` module:

<Listing file-name="src/front_of_house.rs">

```rust,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/no-listing-02-extracting-hosting/src/front_of_house.rs}}
```

</Listing>

Then, we create a _src/front_of_house_ directory and a _hosting.rs_ file to
contain the definitions made in the `hosting` module:

<Listing file-name="src/front_of_house/hosting.rs">

```rust,ignore
{{#rustdoc_include ../listings/ch07-managing-growing-projects/no-listing-02-extracting-hosting/src/front_of_house/hosting.rs}}
```

</Listing>

If we instead put _hosting.rs_ in the _src_ directory, the compiler would
expect the _hosting.rs_ code to be in a `hosting` module declared in the crate
root and not declared as a child of the `front_of_house` module. The
compiler’s rules for which files to check for which modules’ code mean the
directories and files more closely match the module tree.

> ### Alternate File Paths
>
> So far we’ve covered the most idiomatic file paths the Rust compiler uses,
> but Rust also supports an older style of file path. For a module named
> `front_of_house` declared in the crate root, the compiler will look for the
> module’s code in:
>
> - _src/front_of_house.rs_ (what we covered)
> - _src/front_of_house/mod.rs_ (older style, still supported path)
>
> For a module named `hosting` that is a submodule of `front_of_house`, the
> compiler will look for the module’s code in:
>
> - _src/front_of_house/hosting.rs_ (what we covered)
> - _src/front_of_house/hosting/mod.rs_ (older style, still supported path)
>
> If you use both styles for the same module, you’ll get a compiler error.
> Using a mix of both styles for different modules in the same project is
> allowed but might be confusing for people navigating your project.
>
> The main downside to the style that uses files named _mod.rs_ is that your
> project can end up with many files named _mod.rs_, which can get confusing
> when you have them open in your editor at the same time.

We’ve moved each module’s code to a separate file, and the module tree remains
the same. The function calls in `eat_at_restaurant` will work without any
modification, even though the definitions live in different files. This
technique lets you move modules to new files as they grow in size.

Note that the `pub use crate::front_of_house::hosting` statement in
_src/lib.rs_ also hasn’t changed, nor does `use` have any impact on what files
are compiled as part of the crate. The `mod` keyword declares modules, and Rust
looks in a file with the same name as the module for the code that goes into
that module.

## Summary

Rust lets you split a package into multiple crates and a crate into modules so
that you can refer to items defined in one module from another module. You can
do this by specifying absolute or relative paths. These paths can be brought
into scope with a `use` statement so that you can use a shorter path for
multiple uses of the item in that scope. Module code is private by default, but
you can make definitions public by adding the `pub` keyword.

In the next chapter, we’ll look at some collection data structures in the
standard library that you can use in your neatly organized code.

[paths]: ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html
