# Design Patterns

[Design patterns](https://en.wikipedia.org/wiki/Software_design_pattern) are
"general reusable solutions to a commonly occurring problem within a given
context in software design". Design patterns are a great way to describe the
culture of a programming language. Design patterns are very language-specific -
what is a pattern in one language may be unnecessary in another due to a
language feature, or impossible to express due to a missing feature.

If overused, design patterns can add unnecessary complexity to programs.
However, they are a great way to share intermediate and advanced level knowledge
about a programming language.

## Design patterns in Rust

Rust has many unique features. These features give us great benefit by removing
whole classes of problems. Some of them are also patterns that are *unique* to
Rust.

## YAGNI

YAGNI is an acronym that stands for `You Aren't Going to Need It`. It's a vital
software design principle to apply as you write code.

> The best code I ever wrote was code I never wrote.

If we apply YAGNI to design patterns, we see that the features of Rust allow us
to throw out many patterns. For instance, there is no need for the
[strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern) in Rust
because we can just use [traits](https://doc.rust-lang.org/book/traits.html).


---

# Behavioural Patterns

From [Wikipedia](https://en.wikipedia.org/wiki/Behavioral_pattern):

> Design patterns that identify common communication patterns among objects. By
> doing so, these patterns increase flexibility in carrying out communication.


---

# Command

## Description

The basic idea of the Command pattern is to separate out actions into its own
objects and pass them as parameters.

## Motivation

Suppose we have a sequence of actions or transactions encapsulated as objects.
We want these actions or commands to be executed or invoked in some order later
at different time. These commands may also be triggered as a result of some
event. For example, when a user pushes a button, or on arrival of a data packet.
In addition, these commands might be undoable. This may come in useful for
operations of an editor. We might want to store logs of executed commands so
that we could reapply the changes later if the system crashes.

## Example

Define two database operations `create table` and `add field`. Each of these
operations is a command which knows how to undo the command, e.g., `drop table`
and `remove field`. When a user invokes a database migration operation then each
command is executed in the defined order, and when the user invokes the rollback
operation then the whole set of commands is invoked in reverse order.

## Approach: Using trait objects

We define a common trait which encapsulates our command with two operations
`execute` and `rollback`. All command `structs` must implement this trait.

```rust
pub trait Migration {
    fn execute(&self) -> &str;
    fn rollback(&self) -> &str;
}

pub struct CreateTable;
impl Migration for CreateTable {
    fn execute(&self) -> &str {
        "create table"
    }
    fn rollback(&self) -> &str {
        "drop table"
    }
}

pub struct AddField;
impl Migration for AddField {
    fn execute(&self) -> &str {
        "add field"
    }
    fn rollback(&self) -> &str {
        "remove field"
    }
}

struct Schema {
    commands: Vec<Box<dyn Migration>>,
}

impl Schema {
    fn new() -> Self {
        Self { commands: vec![] }
    }

    fn add_migration(&mut self, cmd: Box<dyn Migration>) {
        self.commands.push(cmd);
    }

    fn execute(&self) -> Vec<&str> {
        self.commands.iter().map(|cmd| cmd.execute()).collect()
    }
    fn rollback(&self) -> Vec<&str> {
        self.commands
            .iter()
            .rev() // reverse iterator's direction
            .map(|cmd| cmd.rollback())
            .collect()
    }
}

fn main() {
    let mut schema = Schema::new();

    let cmd = Box::new(CreateTable);
    schema.add_migration(cmd);
    let cmd = Box::new(AddField);
    schema.add_migration(cmd);

    assert_eq!(vec!["create table", "add field"], schema.execute());
    assert_eq!(vec!["remove field", "drop table"], schema.rollback());
}
```

## Approach: Using function pointers

We could follow another approach by creating each individual command as a
different function and store function pointers to invoke these functions later
at a different time. Since function pointers implement all three traits `Fn`,
`FnMut`, and `FnOnce` we could as well pass and store closures instead of
function pointers.

```rust
type FnPtr = fn() -> String;
struct Command {
    execute: FnPtr,
    rollback: FnPtr,
}

struct Schema {
    commands: Vec<Command>,
}

impl Schema {
    fn new() -> Self {
        Self { commands: vec![] }
    }
    fn add_migration(&mut self, execute: FnPtr, rollback: FnPtr) {
        self.commands.push(Command { execute, rollback });
    }
    fn execute(&self) -> Vec<String> {
        self.commands.iter().map(|cmd| (cmd.execute)()).collect()
    }
    fn rollback(&self) -> Vec<String> {
        self.commands
            .iter()
            .rev()
            .map(|cmd| (cmd.rollback)())
            .collect()
    }
}

fn add_field() -> String {
    "add field".to_string()
}

fn remove_field() -> String {
    "remove field".to_string()
}

fn main() {
    let mut schema = Schema::new();
    schema.add_migration(|| "create table".to_string(), || "drop table".to_string());
    schema.add_migration(add_field, remove_field);
    assert_eq!(vec!["create table", "add field"], schema.execute());
    assert_eq!(vec!["remove field", "drop table"], schema.rollback());
}
```

## Approach: Using `Fn` trait objects

Finally, instead of defining a common command trait we could store each command
implementing the `Fn` trait separately in vectors.

```rust
type Migration<'a> = Box<dyn Fn() -> &'a str>;

struct Schema<'a> {
    executes: Vec<Migration<'a>>,
    rollbacks: Vec<Migration<'a>>,
}

impl<'a> Schema<'a> {
    fn new() -> Self {
        Self {
            executes: vec![],
            rollbacks: vec![],
        }
    }
    fn add_migration<E, R>(&mut self, execute: E, rollback: R)
    where
        E: Fn() -> &'a str + 'static,
        R: Fn() -> &'a str + 'static,
    {
        self.executes.push(Box::new(execute));
        self.rollbacks.push(Box::new(rollback));
    }
    fn execute(&self) -> Vec<&str> {
        self.executes.iter().map(|cmd| cmd()).collect()
    }
    fn rollback(&self) -> Vec<&str> {
        self.rollbacks.iter().rev().map(|cmd| cmd()).collect()
    }
}

fn add_field() -> &'static str {
    "add field"
}

fn remove_field() -> &'static str {
    "remove field"
}

fn main() {
    let mut schema = Schema::new();
    schema.add_migration(|| "create table", || "drop table");
    schema.add_migration(add_field, remove_field);
    assert_eq!(vec!["create table", "add field"], schema.execute());
    assert_eq!(vec!["remove field", "drop table"], schema.rollback());
}
```

## Discussion

If our commands are small and may be defined as functions or passed as a closure
then using function pointers might be preferable since it does not exploit
dynamic dispatch. But if our command is a whole struct with a bunch of functions
and variables defined as separated module then using trait objects would be more
suitable. A case of application can be found in [`actix`](https://actix.rs/),
which uses trait objects when it registers a handler function for routes. In
case of using `Fn` trait objects we can create and use commands in the same way
as we used in case of function pointers.

As performance, there is always a trade-off between performance and code
simplicity and organisation. Static dispatch gives faster performance, while
dynamic dispatch provides flexibility when we structure our application.

## See also

- [Command pattern](https://en.wikipedia.org/wiki/Command_pattern)

- [Another example for the `command` pattern](https://web.archive.org/web/20210223131236/https://chercher.tech/rust/command-design-pattern-rust)


---

# Interpreter

## Description

If a problem occurs very often and requires long and repetitive steps to solve
it, then the problem instances might be expressed in a simple language and an
interpreter object could solve it by interpreting the sentences written in this
simple language.

Basically, for any kind of problems we define:

- A
  [domain specific language](https://en.wikipedia.org/wiki/Domain-specific_language),
- A grammar for this language,
- An interpreter that solves the problem instances.

## Motivation

Our goal is to translate simple mathematical expressions into postfix
expressions (or
[Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation))
For simplicity, our expressions consist of ten digits `0`, ..., `9` and two
operations `+`, `-`. For example, the expression `2 + 4` is translated into
`2 4 +`.

## Context Free Grammar for our problem

Our task is translating infix expressions into postfix ones. Let's define a
context free grammar for a set of infix expressions over `0`, ..., `9`, `+`, and
`-`, where:

- Terminal symbols: `0`, `...`, `9`, `+`, `-`
- Non-terminal symbols: `exp`, `term`
- Start symbol is `exp`
- And the following are production rules

```ignore
exp -> exp + term
exp -> exp - term
exp -> term
term -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

**NOTE:** This grammar should be further transformed depending on what we are
going to do with it. For example, we might need to remove left recursion. For
more details please see
[Compilers: Principles,Techniques, and Tools](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools)
(aka Dragon Book).

## Solution

We simply implement a recursive descent parser. For simplicity's sake, the code
panics when an expression is syntactically wrong (for example `2-34` or `2+5-`
are wrong according to the grammar definition).

```rust
pub struct Interpreter<'a> {
    it: std::str::Chars<'a>,
}

impl<'a> Interpreter<'a> {
    pub fn new(infix: &'a str) -> Self {
        Self { it: infix.chars() }
    }

    fn next_char(&mut self) -> Option<char> {
        self.it.next()
    }

    pub fn interpret(&mut self, out: &mut String) {
        self.term(out);

        while let Some(op) = self.next_char() {
            if op == '+' || op == '-' {
                self.term(out);
                out.push(op);
            } else {
                panic!("Unexpected symbol '{op}'");
            }
        }
    }

    fn term(&mut self, out: &mut String) {
        match self.next_char() {
            Some(ch) if ch.is_digit(10) => out.push(ch),
            Some(ch) => panic!("Unexpected symbol '{ch}'"),
            None => panic!("Unexpected end of string"),
        }
    }
}

pub fn main() {
    let mut intr = Interpreter::new("2+3");
    let mut postfix = String::new();
    intr.interpret(&mut postfix);
    assert_eq!(postfix, "23+");

    intr = Interpreter::new("1-2+3-4");
    postfix.clear();
    intr.interpret(&mut postfix);
    assert_eq!(postfix, "12-3+4-");
}
```

## Discussion

There may be a wrong perception that the Interpreter design pattern is about
design grammars for formal languages and implementation of parsers for these
grammars. In fact, this pattern is about expressing problem instances in a more
specific way and implementing functions/classes/structs that solve these problem
instances. Rust language has `macro_rules!` that allow us to define special
syntax and rules on how to expand this syntax into source code.

In the following example we create a simple `macro_rules!` that computes
[Euclidean length](https://en.wikipedia.org/wiki/Euclidean_distance) of `n`
dimensional vectors. Writing `norm!(x,1,2)` might be easier to express and more
efficient than packing `x,1,2` into a `Vec` and calling a function computing the
length.

```rust
macro_rules! norm {
    ($($element:expr),*) => {
        {
            let mut n = 0.0;
            $(
                n += ($element as f64)*($element as f64);
            )*
            n.sqrt()
        }
    };
}

fn main() {
    let x = -3f64;
    let y = 4f64;

    assert_eq!(3f64, norm!(x));
    assert_eq!(5f64, norm!(x, y));
    assert_eq!(0f64, norm!(0, 0, 0));
    assert_eq!(1f64, norm!(0.5, -0.5, 0.5, -0.5));
}
```

## See also

- [Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)
- [Context free grammar](https://en.wikipedia.org/wiki/Context-free_grammar)
- [macro_rules!](https://doc.rust-lang.org/rust-by-example/macros.html)


---

# Newtype

What if in some cases we want a type to behave similar to another type or
enforce some behaviour at compile time when using only type aliases would not be
enough?

For example, if we want to create a custom `Display` implementation for `String`
due to security considerations (e.g. passwords).

For such cases we could use the `Newtype` pattern to provide **type safety** and
**encapsulation**.

## Description

Use a tuple struct with a single field to make an opaque wrapper for a type.
This creates a new type, rather than an alias to a type (`type` items).

## Example

```rust
use std::fmt::Display;

// Create Newtype Password to override the Display trait for String
struct Password(String);

impl Display for Password {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "****************")
    }
}

fn main() {
    let unsecured_password: String = "ThisIsMyPassword".to_string();
    let secured_password: Password = Password(unsecured_password.clone());
    println!("unsecured_password: {unsecured_password}");
    println!("secured_password: {secured_password}");
}
```

```shell
unsecured_password: ThisIsMyPassword
secured_password: ****************
```

## Motivation

The primary motivation for newtypes is abstraction. It allows you to share
implementation details between types while precisely controlling the interface.
By using a newtype rather than exposing the implementation type as part of an
API, it allows you to change implementation backwards compatibly.

Newtypes can be used for distinguishing units, e.g., wrapping `f64` to give
distinguishable `Miles` and `Kilometres`.

## Advantages

The wrapped and wrapper types are not type compatible (as opposed to using
`type`), so users of the newtype will never 'confuse' the wrapped and wrapper
types.

Newtypes are a zero-cost abstraction - there is no runtime overhead.

The privacy system ensures that users cannot access the wrapped type (if the
field is private, which it is by default).

## Disadvantages

The downside of newtypes (especially compared with type aliases), is that there
is no special language support. This means there can be *a lot* of boilerplate.
You need a 'pass through' method for every method you want to expose on the
wrapped type, and an impl for every trait you want to also be implemented for
the wrapper type.

## Discussion

Newtypes are very common in Rust code. Abstraction or representing units are the
most common uses, but they can be used for other reasons:

- restricting functionality (reduce the functions exposed or traits
  implemented),
- making a type with copy semantics have move semantics,
- abstraction by providing a more concrete type and thus hiding internal types,
  e.g.,

```rust,ignore
pub struct Foo(Bar<T1, T2>);
```

Here, `Bar` might be some public, generic type and `T1` and `T2` are some
internal types. Users of our module shouldn't know that we implement `Foo` by
using a `Bar`, but what we're really hiding here is the types `T1` and `T2`, and
how they are used with `Bar`.

## See also

- [Advanced Types in the book](https://doc.rust-lang.org/book/ch19-04-advanced-types.html?highlight=newtype#using-the-newtype-pattern-for-type-safety-and-abstraction)
- [Newtypes in Haskell](https://wiki.haskell.org/Newtype)
- [Type aliases](https://doc.rust-lang.org/stable/book/ch19-04-advanced-types.html#creating-type-synonyms-with-type-aliases)
- [derive_more](https://crates.io/crates/derive_more), a crate for deriving many
  builtin traits on newtypes.
- [The Newtype Pattern In Rust](https://web.archive.org/web/20230519162111/https://www.worthe-it.co.za/blog/2020-10-31-newtype-pattern-in-rust.html)


---

# RAII with guards

## Description

[RAII][wikipedia] stands for "Resource Acquisition is Initialisation" which is a
terrible name. The essence of the pattern is that resource initialisation is
done in the constructor of an object and finalisation in the destructor. This
pattern is extended in Rust by using a RAII object as a guard of some resource
and relying on the type system to ensure that access is always mediated by the
guard object.

## Example

Mutex guards are the classic example of this pattern from the std library (this
is a simplified version of the real implementation):

```rust,ignore
use std::ops::Deref;

struct Foo {}

struct Mutex<T> {
    // We keep a reference to our data: T here.
    //..
}

struct MutexGuard<'a, T: 'a> {
    data: &'a T,
    //..
}

// Locking the mutex is explicit.
impl<T> Mutex<T> {
    fn lock(&self) -> MutexGuard<T> {
        // Lock the underlying OS mutex.
        //..

        // MutexGuard keeps a reference to self
        MutexGuard {
            data: self,
            //..
        }
    }
}

// Destructor for unlocking the mutex.
impl<'a, T> Drop for MutexGuard<'a, T> {
    fn drop(&mut self) {
        // Unlock the underlying OS mutex.
        //..
    }
}

// Implementing Deref means we can treat MutexGuard like a pointer to T.
impl<'a, T> Deref for MutexGuard<'a, T> {
    type Target = T;

    fn deref(&self) -> &T {
        self.data
    }
}

fn baz(x: Mutex<Foo>) {
    let xx = x.lock();
    xx.foo(); // foo is a method on Foo.
              // The borrow checker ensures we can't store a reference to the underlying
              // Foo which will outlive the guard xx.

    // x is unlocked when we exit this function and xx's destructor is executed.
}
```

## Motivation

Where a resource must be finalised after use, RAII can be used to do this
finalisation. If it is an error to access that resource after finalisation, then
this pattern can be used to prevent such errors.

## Advantages

Prevents errors where a resource is not finalised and where a resource is used
after finalisation.

## Discussion

RAII is a useful pattern for ensuring resources are properly deallocated or
finalised. We can make use of the borrow checker in Rust to statically prevent
errors stemming from using resources after finalisation takes place.

The core aim of the borrow checker is to ensure that references to data do not
outlive that data. The RAII guard pattern works because the guard object
contains a reference to the underlying resource and only exposes such
references. Rust ensures that the guard cannot outlive the underlying resource
and that references to the resource mediated by the guard cannot outlive the
guard. To see how this works it is helpful to examine the signature of `deref`
without lifetime elision:

```rust,ignore
fn deref<'a>(&'a self) -> &'a T {
    //..
}
```

The returned reference to the resource has the same lifetime as `self` (`'a`).
The borrow checker therefore ensures that the lifetime of the reference to `T`
is shorter than the lifetime of `self`.

Note that implementing `Deref` is not a core part of this pattern, it only makes
using the guard object more ergonomic. Implementing a `get` method on the guard
works just as well.

## See also

[Finalisation in destructors idiom](../../idioms/dtor-finally.md)

RAII is a common pattern in C++:
[cppreference.com](http://en.cppreference.com/w/cpp/language/raii),
[wikipedia][wikipedia].

[wikipedia]: https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization

[Style guide entry](https://doc.rust-lang.org/1.0.0/style/ownership/raii.html)
(currently just a placeholder).


---

# Strategy (aka Policy)

## Description

The [Strategy design pattern](https://en.wikipedia.org/wiki/Strategy_pattern) is
a technique that enables separation of concerns. It also allows to decouple
software modules through
[Dependency Inversion](https://en.wikipedia.org/wiki/Dependency_inversion_principle).

The basic idea behind the Strategy pattern is that, given an algorithm solving a
particular problem, we define only the skeleton of the algorithm at an abstract
level, and we separate the specific algorithm’s implementation into different
parts.

In this way, a client using the algorithm may choose a specific implementation,
while the general algorithm workflow remains the same. In other words, the
abstract specification of the class does not depend on the specific
implementation of the derived class, but specific implementation must adhere to
the abstract specification. This is why we call it "Dependency Inversion".

## Motivation

Imagine we are working on a project that generates reports every month. We need
the reports to be generated in different formats (strategies), e.g., in `JSON`
or `Plain Text` formats. But things vary over time, and we don't know what kind
of requirement we may get in the future. For example, we may need to generate
our report in a completely new format, or just modify one of the existing
formats.

## Example

In this example our invariants (or abstractions) are `Formatter` and `Report`,
while `Text` and `Json` are our strategy structs. These strategies have to
implement the `Formatter` trait.

```rust
use std::collections::HashMap;

type Data = HashMap<String, u32>;

trait Formatter {
    fn format(&self, data: &Data, buf: &mut String);
}

struct Report;

impl Report {
    // Write should be used but we kept it as String to ignore error handling
    fn generate<T: Formatter>(g: T, s: &mut String) {
        // backend operations...
        let mut data = HashMap::new();
        data.insert("one".to_string(), 1);
        data.insert("two".to_string(), 2);
        // generate report
        g.format(&data, s);
    }
}

struct Text;
impl Formatter for Text {
    fn format(&self, data: &Data, buf: &mut String) {
        for (k, v) in data {
            let entry = format!("{k} {v}\n");
            buf.push_str(&entry);
        }
    }
}

struct Json;
impl Formatter for Json {
    fn format(&self, data: &Data, buf: &mut String) {
        buf.push('[');
        for (k, v) in data.into_iter() {
            let entry = format!(r#"{{"{}":"{}"}}"#, k, v);
            buf.push_str(&entry);
            buf.push(',');
        }
        if !data.is_empty() {
            buf.pop(); // remove extra , at the end
        }
        buf.push(']');
    }
}

fn main() {
    let mut s = String::from("");
    Report::generate(Text, &mut s);
    assert!(s.contains("one 1"));
    assert!(s.contains("two 2"));

    s.clear(); // reuse the same buffer
    Report::generate(Json, &mut s);
    assert!(s.contains(r#"{"one":"1"}"#));
    assert!(s.contains(r#"{"two":"2"}"#));
}
```

## Advantages

The main advantage is separation of concerns. For example, in this case `Report`
does not know anything about specific implementations of `Json` and `Text`,
whereas the output implementations does not care about how data is preprocessed,
stored, and fetched. The only thing they have to know is a specific trait to
implement and its method defining the concrete algorithm implementation
processing the result, i.e., `Formatter` and `format(...)`.

## Disadvantages

For each strategy there must be implemented at least one module, so number of
modules increases with number of strategies. If there are many strategies to
choose from then users have to know how strategies differ from one another.

## Discussion

In the previous example all strategies are implemented in a single file. Ways of
providing different strategies includes:

- All in one file (as shown in this example, similar to being separated as
  modules)
- Separated as modules, E.g. `formatter::json` module, `formatter::text` module
- Use compiler feature flags, E.g. `json` feature, `text` feature
- Separated as crates, E.g. `json` crate, `text` crate

Serde crate is a good example of the `Strategy` pattern in action. Serde allows
[full customization](https://serde.rs/custom-serialization.html) of the
serialization behavior by manually implementing `Serialize` and `Deserialize`
traits for our type. For example, we could easily swap `serde_json` with
`serde_cbor` since they expose similar methods. Having this makes the helper
crate `serde_transcode` much more useful and ergonomic.

However, we don't need to use traits in order to design this pattern in Rust.

The following toy example demonstrates the idea of the Strategy pattern using
Rust `closures`:

```rust
struct Adder;
impl Adder {
    pub fn add<F>(x: u8, y: u8, f: F) -> u8
    where
        F: Fn(u8, u8) -> u8,
    {
        f(x, y)
    }
}

fn main() {
    let arith_adder = |x, y| x + y;
    let bool_adder = |x, y| {
        if x == 1 || y == 1 {
            1
        } else {
            0
        }
    };
    let custom_adder = |x, y| 2 * x + y;

    assert_eq!(9, Adder::add(4, 5, arith_adder));
    assert_eq!(0, Adder::add(0, 0, bool_adder));
    assert_eq!(5, Adder::add(1, 3, custom_adder));
}
```

In fact, Rust already uses this idea for `Options`'s `map` method:

```rust
fn main() {
    let val = Some("Rust");

    let len_strategy = |s: &str| s.len();
    assert_eq!(4, val.map(len_strategy).unwrap());

    let first_byte_strategy = |s: &str| s.bytes().next().unwrap();
    assert_eq!(82, val.map(first_byte_strategy).unwrap());
}
```

## See also

- [Strategy Pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Policy Based Design](https://en.wikipedia.org/wiki/Modern_C++_Design#Policy-based_design)
- [Implementing a TCP server for Space Applications in Rust using the Strategy Pattern](https://web.archive.org/web/20231003171500/https://robamu.github.io/posts/rust-strategy-pattern/)


---

# Visitor

## Description

A visitor encapsulates an algorithm that operates over a heterogeneous
collection of objects. It allows multiple different algorithms to be written
over the same data without having to modify the data (or their primary
behaviour).

Furthermore, the visitor pattern allows separating the traversal of a collection
of objects from the operations performed on each object.

## Example

```rust,ignore
// The data we will visit
mod ast {
    pub enum Stmt {
        Expr(Expr),
        Let(Name, Expr),
    }

    pub struct Name {
        value: String,
    }

    pub enum Expr {
        IntLit(i64),
        Add(Box<Expr>, Box<Expr>),
        Sub(Box<Expr>, Box<Expr>),
    }
}

// The abstract visitor
mod visit {
    use ast::*;

    pub trait Visitor<T> {
        fn visit_name(&mut self, n: &Name) -> T;
        fn visit_stmt(&mut self, s: &Stmt) -> T;
        fn visit_expr(&mut self, e: &Expr) -> T;
    }
}

use ast::*;
use visit::*;

// An example concrete implementation - walks the AST interpreting it as code.
struct Interpreter;
impl Visitor<i64> for Interpreter {
    fn visit_name(&mut self, n: &Name) -> i64 {
        panic!()
    }
    fn visit_stmt(&mut self, s: &Stmt) -> i64 {
        match *s {
            Stmt::Expr(ref e) => self.visit_expr(e),
            Stmt::Let(..) => unimplemented!(),
        }
    }

    fn visit_expr(&mut self, e: &Expr) -> i64 {
        match *e {
            Expr::IntLit(n) => n,
            Expr::Add(ref lhs, ref rhs) => self.visit_expr(lhs) + self.visit_expr(rhs),
            Expr::Sub(ref lhs, ref rhs) => self.visit_expr(lhs) - self.visit_expr(rhs),
        }
    }
}
```

One could implement further visitors, for example a type checker, without having
to modify the AST data.

## Motivation

The visitor pattern is useful anywhere that you want to apply an algorithm to
heterogeneous data. If data is homogeneous, you can use an iterator-like
pattern. Using a visitor object (rather than a functional approach) allows the
visitor to be stateful and thus communicate information between nodes.

## Discussion

It is common for the `visit_*` methods to return void (as opposed to in the
example). In that case it is possible to factor out the traversal code and share
it between algorithms (and also to provide noop default methods). In Rust, the
common way to do this is to provide `walk_*` functions for each datum. For
example,

```rust,ignore
pub fn walk_expr(visitor: &mut Visitor, e: &Expr) {
    match *e {
        Expr::IntLit(_) => {}
        Expr::Add(ref lhs, ref rhs) => {
            visitor.visit_expr(lhs);
            visitor.visit_expr(rhs);
        }
        Expr::Sub(ref lhs, ref rhs) => {
            visitor.visit_expr(lhs);
            visitor.visit_expr(rhs);
        }
    }
}
```

In other languages (e.g., Java) it is common for data to have an `accept` method
which performs the same duty.

## See also

The visitor pattern is a common pattern in most OO languages.

[Wikipedia article](https://en.wikipedia.org/wiki/Visitor_pattern)

The [fold](../creational/fold.md) pattern is similar to visitor but produces a
new version of the visited data structure.


---

# Creational Patterns

From [Wikipedia](https://en.wikipedia.org/wiki/Creational_pattern):

> Design patterns that deal with object creation mechanisms, trying to create
> objects in a manner suitable to the situation. The basic form of object
> creation could result in design problems or in added complexity to the design.
> Creational design patterns solve this problem by somehow controlling this
> object creation.


---

# Builder

## Description

Construct an object with calls to a builder helper.

## Example

```rust
#[derive(Debug, PartialEq)]
pub struct Foo {
    // Lots of complicated fields.
    bar: String,
}

impl Foo {
    // This method will help users to discover the builder
    pub fn builder() -> FooBuilder {
        FooBuilder::default()
    }
}

#[derive(Default)]
pub struct FooBuilder {
    // Probably lots of optional fields.
    bar: String,
}

impl FooBuilder {
    pub fn new(/* ... */) -> FooBuilder {
        // Set the minimally required fields of Foo.
        FooBuilder {
            bar: String::from("X"),
        }
    }

    pub fn name(mut self, bar: String) -> FooBuilder {
        // Set the name on the builder itself, and return the builder by value.
        self.bar = bar;
        self
    }

    // If we can get away with not consuming the Builder here, that is an
    // advantage. It means we can use the FooBuilder as a template for constructing
    // many Foos.
    pub fn build(self) -> Foo {
        // Create a Foo from the FooBuilder, applying all settings in FooBuilder
        // to Foo.
        Foo { bar: self.bar }
    }
}

#[test]
fn builder_test() {
    let foo = Foo {
        bar: String::from("Y"),
    };
    let foo_from_builder: Foo = FooBuilder::new().name(String::from("Y")).build();
    assert_eq!(foo, foo_from_builder);
}
```

## Motivation

Useful when you would otherwise require many constructors or where construction
has side effects.

## Advantages

Separates methods for building from other methods.

Prevents proliferation of constructors.

Can be used for one-liner initialisation as well as more complex construction.

When you add new fields to the target struct, you can update the builder to
leave client code backwards compatible.

## Disadvantages

More complex than creating a struct object directly, or a simple constructor
function.

## Discussion

This pattern is seen more frequently in Rust (and for simpler objects) than in
many other languages because Rust lacks overloading and default values for
function parameters. Since you can only have a single method with a given name,
having multiple constructors is less nice in Rust than in C++, Java, or others.

This pattern is often used where the builder object is useful in its own right,
rather than being just a builder. For example, see
[`std::process::Command`](https://doc.rust-lang.org/std/process/struct.Command.html)
is a builder for
[`Child`](https://doc.rust-lang.org/std/process/struct.Child.html) (a process).
In these cases, the `T` and `TBuilder` naming pattern is not used.

The example takes and returns the builder by value. It is often more ergonomic
(and more efficient) to take and return the builder as a mutable reference. The
borrow checker makes this work naturally. This approach has the advantage that
one can write code like

```rust,ignore
let mut fb = FooBuilder::new();
fb.a();
fb.b();
let f = fb.build();
```

as well as the `FooBuilder::new().a().b().build()` style.

## See also

- [Description in the style guide](https://web.archive.org/web/20210104103100/https://doc.rust-lang.org/1.12.0/style/ownership/builders.html)
- [derive_builder](https://crates.io/crates/derive_builder), a crate for
  automatically implementing this pattern while avoiding the boilerplate.
- [Constructor pattern](../../idioms/ctor.md) for when construction is simpler.
- [Builder pattern (wikipedia)](https://en.wikipedia.org/wiki/Builder_pattern)
- [Construction of complex values](https://web.archive.org/web/20210104103000/https://rust-lang.github.io/api-guidelines/type-safety.html#c-builder)


---

# Fold

## Description

Run an algorithm over each item in a collection of data to create a new item,
thus creating a whole new collection.

The etymology here is unclear to me. The terms 'fold' and 'folder' are used in
the Rust compiler, although it appears to me to be more like a map than a fold
in the usual sense. See the discussion below for more details.

## Example

```rust,ignore
// The data we will fold, a simple AST.
mod ast {
    pub enum Stmt {
        Expr(Box<Expr>),
        Let(Box<Name>, Box<Expr>),
    }

    pub struct Name {
        value: String,
    }

    pub enum Expr {
        IntLit(i64),
        Add(Box<Expr>, Box<Expr>),
        Sub(Box<Expr>, Box<Expr>),
    }
}

// The abstract folder
mod fold {
    use ast::*;

    pub trait Folder {
        // A leaf node just returns the node itself. In some cases, we can do this
        // to inner nodes too.
        fn fold_name(&mut self, n: Box<Name>) -> Box<Name> { n }
        // Create a new inner node by folding its children.
        fn fold_stmt(&mut self, s: Box<Stmt>) -> Box<Stmt> {
            match *s {
                Stmt::Expr(e) => Box::new(Stmt::Expr(self.fold_expr(e))),
                Stmt::Let(n, e) => Box::new(Stmt::Let(self.fold_name(n), self.fold_expr(e))),
            }
        }
        fn fold_expr(&mut self, e: Box<Expr>) -> Box<Expr> { ... }
    }
}

use fold::*;
use ast::*;

// An example concrete implementation - renames every name to 'foo'.
struct Renamer;
impl Folder for Renamer {
    fn fold_name(&mut self, n: Box<Name>) -> Box<Name> {
        Box::new(Name { value: "foo".to_owned() })
    }
    // Use the default methods for the other nodes.
}
```

The result of running the `Renamer` on an AST is a new AST identical to the old
one, but with every name changed to `foo`. A real life folder might have some
state preserved between nodes in the struct itself.

A folder can also be defined to map one data structure to a different (but
usually similar) data structure. For example, we could fold an AST into a HIR
tree (HIR stands for high-level intermediate representation).

## Motivation

It is common to want to map a data structure by performing some operation on
each node in the structure. For simple operations on simple data structures,
this can be done using `Iterator::map`. For more complex operations, perhaps
where earlier nodes can affect the operation on later nodes, or where iteration
over the data structure is non-trivial, using the fold pattern is more
appropriate.

Like the visitor pattern, the fold pattern allows us to separate traversal of a
data structure from the operations performed to each node.

## Discussion

Mapping data structures in this fashion is common in functional languages. In OO
languages, it would be more common to mutate the data structure in place. The
'functional' approach is common in Rust, mostly due to the preference for
immutability. Using fresh data structures, rather than mutating old ones, makes
reasoning about the code easier in most circumstances.

The trade-off between efficiency and reusability can be tweaked by changing how
nodes are accepted by the `fold_*` methods.

In the above example we operate on `Box` pointers. Since these own their data
exclusively, the original copy of the data structure cannot be re-used. On the
other hand if a node is not changed, reusing it is very efficient.

If we were to operate on borrowed references, the original data structure can be
reused; however, a node must be cloned even if unchanged, which can be
expensive.

Using a reference counted pointer gives the best of both worlds - we can reuse
the original data structure, and we don't need to clone unchanged nodes.
However, they are less ergonomic to use and mean that the data structures cannot
be mutable.

## See also

Iterators have a `fold` method, however this folds a data structure into a
value, rather than into a new data structure. An iterator's `map` is more like
this fold pattern.

In other languages, fold is usually used in the sense of Rust's iterators,
rather than this pattern. Some functional languages have powerful constructs for
performing flexible maps over data structures.

The [visitor](../behavioural/visitor.md) pattern is closely related to fold.
They share the concept of walking a data structure performing an operation on
each node. However, the visitor does not create a new data structure nor consume
the old one.


---

# Structural Patterns

From [Wikipedia](https://en.wikipedia.org/wiki/Structural_pattern):

> Design patterns that ease the design by identifying a simple way to realize
> relationships among entities.


---

# Struct decomposition for independent borrowing

## Description

Sometimes a large struct will cause issues with the borrow checker - although
fields can be borrowed independently, sometimes the whole struct ends up being
used at once, preventing other uses. A solution might be to decompose the struct
into several smaller structs. Then compose these together into the original
struct. Then each struct can be borrowed separately and have more flexible
behaviour.

This will often lead to a better design in other ways: applying this design
pattern often reveals smaller units of functionality.

## Example

Here is a contrived example of where the borrow checker foils us in our plan to
use a struct:

```rust,ignore
struct Database {
    connection_string: String,
    timeout: u32,
    pool_size: u32,
}

fn print_database(database: &Database) {
    println!("Connection string: {}", database.connection_string);
    println!("Timeout: {}", database.timeout);
    println!("Pool size: {}", database.pool_size);
}

fn main() {
    let mut db = Database {
        connection_string: "initial string".to_string(),
        timeout: 30,
        pool_size: 100,
    };

    let connection_string = &mut db.connection_string;
    print_database(&db);
    *connection_string = "new string".to_string();
}
```

The compiler throws following errors:

```ignore
let connection_string = &mut db.connection_string;
                        ------------------------- mutable borrow occurs here
print_database(&db);
               ^^^ immutable borrow occurs here
*connection_string = "new string".to_string();
------------------ mutable borrow later used here
```

We can apply this design pattern and refactor `Database` into three smaller
structs, thus solving the borrow checking issue:

```rust
// Database is now composed of three structs - ConnectionString, Timeout and PoolSize.
// Let's decompose it into smaller structs
#[derive(Debug, Clone)]
struct ConnectionString(String);

#[derive(Debug, Clone, Copy)]
struct Timeout(u32);

#[derive(Debug, Clone, Copy)]
struct PoolSize(u32);

// We then compose these smaller structs back into `Database`
struct Database {
    connection_string: ConnectionString,
    timeout: Timeout,
    pool_size: PoolSize,
}

// print_database can then take ConnectionString, Timeout and Poolsize struct instead
fn print_database(connection_str: ConnectionString, timeout: Timeout, pool_size: PoolSize) {
    println!("Connection string: {connection_str:?}");
    println!("Timeout: {timeout:?}");
    println!("Pool size: {pool_size:?}");
}

fn main() {
    // Initialize the Database with the three structs
    let mut db = Database {
        connection_string: ConnectionString("localhost".to_string()),
        timeout: Timeout(30),
        pool_size: PoolSize(100),
    };

    let connection_string = &mut db.connection_string;
    print_database(connection_string.clone(), db.timeout, db.pool_size);
    *connection_string = ConnectionString("new string".to_string());
}
```

## Motivation

This pattern is most useful, when you have a struct that ended up with a lot of
fields that you want to borrow independently. Thus having a more flexible
behaviour in the end.

## Advantages

Decomposition of structs lets you work around limitations in the borrow checker.
And it often produces a better design.

## Disadvantages

It can lead to more verbose code. And sometimes, the smaller structs are not
good abstractions, and so we end up with a worse design. That is probably a
'code smell', indicating that the program should be refactored in some way.

## Discussion

This pattern is not required in languages that don't have a borrow checker, so
in that sense is unique to Rust. However, making smaller units of functionality
often leads to cleaner code: a widely acknowledged principle of software
engineering, independent of the language.

This pattern relies on Rust's borrow checker to be able to borrow fields
independently of each other. In the example, the borrow checker knows that `a.b`
and `a.c` are distinct and can be borrowed independently, it does not try to
borrow all of `a`, which would make this pattern useless.


---

# Prefer small crates

## Description

Prefer small crates that do one thing well.

Cargo and crates.io make it easy to add third-party libraries, much more so than
in say C or C++. Moreover, since packages on crates.io cannot be edited or
removed after publication, any build that works now should continue to work in
the future. We should take advantage of this tooling, and use smaller, more
fine-grained dependencies.

## Advantages

- Small crates are easier to understand, and encourage more modular code.
- Crates allow for re-using code between projects. For example, the `url` crate
  was developed as part of the Servo browser engine, but has since found wide
  use outside the project.
- Since the compilation unit of Rust is the crate, splitting a project into
  multiple crates can allow more of the code to be built in parallel.

## Disadvantages

- This can lead to "dependency hell", when a project depends on multiple
  conflicting versions of a crate at the same time. For example, the `url` crate
  has both versions 1.0 and 0.5. Since the `Url` from `url:1.0` and the `Url`
  from `url:0.5` are different types, an HTTP client that uses `url:0.5` would
  not accept `Url` values from a web scraper that uses `url:1.0`.
- Packages on crates.io are not curated. A crate may be poorly written, have
  unhelpful documentation, or be outright malicious.
- Two small crates may be less optimized than one large one, since the compiler
  does not perform link-time optimization (LTO) by default.

## Examples

The [`url`](https://crates.io/crates/url) crate provides tools for working with
URLs.

The [`num_cpus`](https://crates.io/crates/num_cpus) crate provides a function to
query the number of CPUs on a machine.

The [`ref_slice`](https://crates.io/crates/ref_slice) crate provides functions
for converting `&T` to `&[T]`. (Historical example)

## See also

- [crates.io: The Rust community crate host](https://crates.io/)


---

# Contain unsafety in small modules

## Description

If you have `unsafe` code, create the smallest possible module that can uphold
the needed invariants to build a minimal safe interface upon the unsafety. Embed
this into a larger module that contains only safe code and presents an ergonomic
interface. Note that the outer module can contain unsafe functions and methods
that call directly into the unsafe code. Users may use this to gain speed
benefits.

## Advantages

- This restricts the unsafe code that must be audited
- Writing the outer module is much easier, since you can count on the guarantees
  of the inner module

## Disadvantages

- Sometimes, it may be hard to find a suitable interface.
- The abstraction may introduce inefficiencies.

## Examples

- The [`toolshed`](https://docs.rs/toolshed) crate contains its unsafe
  operations in submodules, presenting a safe interface to users.
- `std`'s `String` class is a wrapper over `Vec<u8>` with the added invariant
  that the contents must be valid UTF-8. The operations on `String` ensure this
  behavior. However, users have the option of using an `unsafe` method to create
  a `String`, in which case the onus is on them to guarantee the validity of the
  contents.

## See also

- [Ralf Jung's Blog about invariants in unsafe code](https://www.ralfj.de/blog/2018/08/22/two-kinds-of-invariants.html)


---

# Use custom traits to avoid complex type bounds

## Description

Trait bounds can become somewhat unwieldy, especially if one of the `Fn` traits[^fn-traits]
is involved and there are specific requirements on the output type. In such
cases the introduction of a new trait may help reduce verbosity, eliminate some
type parameters and thus increase expressiveness. Such a trait can be
accompanied with a generic `impl` for all types satisfying the original bound.

## Example

Let's imagine some sort of monitoring or information gathering system. The
system retrieves values of various types from diverse sources. It may derive
from them some sort of status indicating issues. For example, the total amount
of free memory should be above a certain theshold, and the user with the id `0`
should always be named "root".

For management reasons, we probably want type erasure on the top level. However,
we also need to provide specific (user configurable) assesments for specific
types of data sources (e.g. thresholds and ranges for numerical types). And
since sources for these values are diverse, we may choose to supply data sources
as closures that return a value when called. Because we are probably getting
those values from the operating system, we are likely confronted with operations
that may fail.

We thus may have settled on the following types and traits for handling specific
values:

```rust
use std::fmt::Display;

struct Value<G: FnMut() -> Result<T, Error>, S: Fn(&T) -> Status, T: Display> {
    value: Option<T>,
    getter: G,
    status: S,
}

impl<G: FnMut() -> Result<T, Error>, S: Fn(&T) -> Status, T: Display> Value<G, S, T> {
    pub fn update(&mut self) -> Result<(), Error> {
        (self.getter)().map(|v| self.value = Some(v))
    }

    pub fn value(&self) -> Option<&T> {
        self.value.as_ref()
    }

    pub fn status(&self) -> Option<Status> {
        self.value().map(&self.status)
    }
}

// ...

enum Status {
    // ...
}

struct Error {
    // ...
}
```

With these types, we will need to repeat the trait bounds for `G` in at least a
few places. Readability suffers, partially due the the fact that the getter
returns a `Result`. Introducing a bound for "getters" allows a more expressive
bound and eliminate one of the type parameters:

```rust
# use std::fmt::Display;
trait Getter {
    type Output: Display;

    fn get_value(&mut self) -> Result<Self::Output, Error>;
}

impl<F: FnMut() -> Result<T, Error>, T: Display> Getter for F {
    type Output = T;

    fn get_value(&mut self) -> Result<Self::Output, Error> {
        self()
    }
}

struct Value<G: Getter, S: Fn(&G::Output) -> Status> {
    value: Option<G::Output>,
    getter: G,
    status: S,
}

// ...
# enum Status {}
# struct Error;
```

## Advantages

Introducing a new trait can help simplify type bounds, particularly via the
elimination of type parameters. A good name for the new trait will also make the
bound more expressive. The new trait, an abstraction, also offers opportunities
in itself, including:

- additional, specialized types implementing the new trait (e.g. representing an
  idendity of some sort) as well as other useful traits such as `Default` and
- additional methods, as long as they can be implemented for all relevant types.

## Disadvantages

Introducing new items such as the trait means we need to find an appropriate
name and place for it. It also means one more item users of the original
functionality need to investigate[^read-docs]. Depending on presentation, it may
not be obvious right away that a simple closure may be used as a `Getter` in the
example above.

[^fn-traits]: i.e. `Fn`, `FnOnce` and `FnMut`

[^read-docs]: meaning they may need to read more documentation


---

# FFI Patterns

Writing FFI code is an entire course in itself. However, there are several
idioms here that can act as pointers, and avoid traps for inexperienced users of
unsafe Rust.

This section contains design patterns that may be useful when doing FFI.

1. [Object-Based API](./export.md) design that has good memory safety
   characteristics, and a clean boundary of what is safe and what is unsafe

2. [Type Consolidation into Wrappers](./wrappers.md) - group multiple Rust types
   together into an opaque "object"


---

# Object-Based APIs

## Description

When designing APIs in Rust which are exposed to other languages, there are some
important design principles which are contrary to normal Rust API design:

1. All Encapsulated types should be *owned* by Rust, *managed* by the user, and
   *opaque*.
2. All Transactional data types should be *owned* by the user, and
   *transparent*.
3. All library behavior should be functions acting upon Encapsulated types.
4. All library behavior should be encapsulated into types not based on
   structure, but *provenance/lifetime*.

## Motivation

Rust has built-in FFI support to other languages. It does this by providing a
way for crate authors to provide C-compatible APIs through different ABIs
(though that is unimportant to this practice).

Well-designed Rust FFI follows C API design principles, while compromising the
design in Rust as little as possible. There are three goals with any foreign
API:

1. Make it easy to use in the target language.
2. Avoid the API dictating internal unsafety on the Rust side as much as
   possible.
3. Keep the potential for memory unsafety and Rust `undefined behaviour` as
   small as possible.

Rust code must trust the memory safety of the foreign language beyond a certain
point. However, every bit of `unsafe` code on the Rust side is an opportunity
for bugs, or to exacerbate `undefined behaviour`.

For example, if a pointer provenance is wrong, that may be a segfault due to
invalid memory access. But if it is manipulated by unsafe code, it could become
full-blown heap corruption.

The Object-Based API design allows for writing shims that have good memory
safety characteristics, and a clean boundary of what is safe and what is
`unsafe`.

## Code Example

The POSIX standard defines the API to access an on-file database, known as
[DBM](https://web.archive.org/web/20210105035602/https://www.mankier.com/0p/ndbm.h).
It is an excellent example of an "object-based" API.

Here is the definition in C, which hopefully should be easy to read for those
involved in FFI. The commentary below should help explain it for those who miss
the subtleties.

```C
struct DBM;
typedef struct { void *dptr, size_t dsize } datum;

int     dbm_clearerr(DBM *);
void    dbm_close(DBM *);
int     dbm_delete(DBM *, datum);
int     dbm_error(DBM *);
datum   dbm_fetch(DBM *, datum);
datum   dbm_firstkey(DBM *);
datum   dbm_nextkey(DBM *);
DBM    *dbm_open(const char *, int, mode_t);
int     dbm_store(DBM *, datum, datum, int);
```

This API defines two types: `DBM` and `datum`.

The `DBM` type was called an "encapsulated" type above. It is designed to
contain internal state, and acts as an entry point for the library's behavior.

It is completely opaque to the user, who cannot create a `DBM` themselves since
they don't know its size or layout. Instead, they must call `dbm_open`, and that
only gives them *a pointer to one*.

This means all `DBM`s are "owned" by the library in a Rust sense. The internal
state of unknown size is kept in memory controlled by the library, not the user.
The user can only manage its life cycle with `open` and `close`, and perform
operations on it with the other functions.

The `datum` type was called a "transactional" type above. It is designed to
facilitate the exchange of information between the library and its user.

The database is designed to store "unstructured data", with no pre-defined
length or meaning. As a result, the `datum` is the C equivalent of a Rust slice:
a bunch of bytes, and a count of how many there are. The main difference is that
there is no type information, which is what `void` indicates.

Keep in mind that this header is written from the library's point of view. The
user likely has some type they are using, which has a known size. But the
library does not care, and by the rules of C casting, any type behind a pointer
can be cast to `void`.

As noted earlier, this type is *transparent* to the user. But also, this type is
*owned* by the user. This has subtle ramifications, due to that pointer inside
it. The question is, who owns the memory that pointer points to?

The answer for best memory safety is, "the user". But in cases such as
retrieving a value, the user does not know how to allocate it correctly (since
they don't know how long the value is). In this case, the library code is
expected to use the heap that the user has access to -- such as the C library
`malloc` and `free` -- and then *transfer ownership* in the Rust sense.

This may all seem speculative, but this is what a pointer means in C. It means
the same thing as Rust: "user defined lifetime." The user of the library needs
to read the documentation in order to use it correctly. That said, there are
some decisions that have fewer or greater consequences if users do it wrong.
Minimizing those are what this best practice is about, and the key is to
*transfer ownership of everything that is transparent*.

## Advantages

This minimizes the number of memory safety guarantees the user must uphold to a
relatively small number:

1. Do not call any function with a pointer not returned by `dbm_open` (invalid
   access or corruption).
2. Do not call any function on a pointer after close (use after free).
3. The `dptr` on any `datum` must be `NULL`, or point to a valid slice of memory
   at the advertised length.

In addition, it avoids a lot of pointer provenance issues. To understand why,
let us consider an alternative in some depth: key iteration.

Rust is well known for its iterators. When implementing one, the programmer
makes a separate type with a bounded lifetime to its owner, and implements the
`Iterator` trait.

Here is how iteration would be done in Rust for `DBM`:

```rust,ignore
struct Dbm { ... }

impl Dbm {
    /* ... */
    pub fn keys<'it>(&'it self) -> DbmKeysIter<'it> { ... }
    /* ... */
}

struct DbmKeysIter<'it> {
    owner: &'it Dbm,
}

impl<'it> Iterator for DbmKeysIter<'it> { ... }
```

This is clean, idiomatic, and safe. thanks to Rust's guarantees. However,
consider what a straightforward API translation would look like:

```rust,ignore
#[no_mangle]
pub extern "C" fn dbm_iter_new(owner: *const Dbm) -> *mut DbmKeysIter {
    // THIS API IS A BAD IDEA! For real applications, use object-based design instead.
}
#[no_mangle]
pub extern "C" fn dbm_iter_next(
    iter: *mut DbmKeysIter,
    key_out: *const datum
) -> libc::c_int {
    // THIS API IS A BAD IDEA! For real applications, use object-based design instead.
}
#[no_mangle]
pub extern "C" fn dbm_iter_del(*mut DbmKeysIter) {
    // THIS API IS A BAD IDEA! For real applications, use object-based design instead.
}
```

This API loses a key piece of information: the lifetime of the iterator must not
exceed the lifetime of the `Dbm` object that owns it. A user of the library
could use it in a way which causes the iterator to outlive the data it is
iterating on, resulting in reading uninitialized memory.

This example written in C contains a bug that will be explained afterwards:

```C
int count_key_sizes(DBM *db) {
    // DO NOT USE THIS FUNCTION. IT HAS A SUBTLE BUT SERIOUS BUG!
    datum key;
    int len = 0;

    if (!dbm_iter_new(db)) {
        dbm_close(db);
        return -1;
    }

    int l;
    while ((l = dbm_iter_next(owner, &key)) >= 0) { // an error is indicated by -1
        free(key.dptr);
        len += key.dsize;
        if (l == 0) { // end of the iterator
            dbm_close(owner);
        }
    }
    if l >= 0 {
        return -1;
    } else {
        return len;
    }
}
```

This bug is a classic. Here's what happens when the iterator returns the
end-of-iteration marker:

1. The loop condition sets `l` to zero, and enters the loop because `0 >= 0`.
2. The length is incremented, in this case by zero.
3. The if statement is true, so the database is closed. There should be a break
   statement here.
4. The loop condition executes again, causing a `next` call on the closed
   object.

The worst part about this bug? If the Rust implementation was careful, this code
will work most of the time! If the memory for the `Dbm` object is not
immediately reused, an internal check will almost certainly fail, resulting in
the iterator returning a `-1` indicating an error. But occasionally, it will
cause a segmentation fault, or even worse, nonsensical memory corruption!

None of this can be avoided by Rust. From its perspective, it put those objects
on its heap, returned pointers to them, and gave up control of their lifetimes.
The C code simply must "play nice".

The programmer must read and understand the API documentation. While some
consider that par for the course in C, a good API design can mitigate this risk.
The POSIX API for `DBM` did this by *consolidating the ownership* of the
iterator with its parent:

```C
datum   dbm_firstkey(DBM *);
datum   dbm_nextkey(DBM *);
```

Thus, all the lifetimes were bound together, and such unsafety was prevented.

## Disadvantages

However, this design choice also has a number of drawbacks, which should be
considered as well.

First, the API itself becomes less expressive. With POSIX DBM, there is only one
iterator per object, and every call changes its state. This is much more
restrictive than iterators in almost any language, even though it is safe.
Perhaps with other related objects, whose lifetimes are less hierarchical, this
limitation is more of a cost than the safety.

Second, depending on the relationships of the API's parts, significant design
effort may be involved. Many of the easier design points have other patterns
associated with them:

- [Wrapper Type Consolidation](./wrappers.md) groups multiple Rust types
  together into an opaque "object"

- [FFI Error Passing](../../idioms/ffi/errors.md) explains error handling with
  integer codes and sentinel return values (such as `NULL` pointers)

- [Accepting Foreign Strings](../../idioms/ffi/accepting-strings.md) allows
  accepting strings with minimal unsafe code, and is easier to get right than
  [Passing Strings to FFI](../../idioms/ffi/passing-strings.md)

However, not every API can be done this way. It is up to the best judgement of
the programmer as to who their audience is.


---

# Type Consolidation into Wrappers

## Description

This pattern is designed to allow gracefully handling multiple related types,
while minimizing the surface area for memory unsafety.

One of the cornerstones of Rust's aliasing rules is lifetimes. This ensures that
many patterns of access between types can be memory safe, data race safety
included.

However, when Rust types are exported to other languages, they are usually
transformed into pointers. In Rust, a pointer means "the user manages the
lifetime of the pointee." It is their responsibility to avoid memory unsafety.

Some level of trust in the user code is thus required, notably around
use-after-free which Rust can do nothing about. However, some API designs place
higher burdens than others on the code written in the other language.

The lowest risk API is the "consolidated wrapper", where all possible
interactions with an object are folded into a "wrapper type", while keeping the
Rust API clean.

## Code Example

To understand this, let us look at a classic example of an API to export:
iteration through a collection.

That API looks like this:

1. The iterator is initialized with `first_key`.
2. Each call to `next_key` will advance the iterator.
3. Calls to `next_key` if the iterator is at the end will do nothing.
4. As noted above, the iterator is "wrapped into" the collection (unlike the
   native Rust API).

If the iterator implements `nth()` efficiently, then it is possible to make it
ephemeral to each function call:

```rust,ignore
struct MySetWrapper {
    myset: MySet,
    iter_next: usize,
}

impl MySetWrapper {
    pub fn first_key(&mut self) -> Option<&Key> {
        self.iter_next = 0;
        self.next_key()
    }
    pub fn next_key(&mut self) -> Option<&Key> {
        if let Some(next) = self.myset.keys().nth(self.iter_next) {
            self.iter_next += 1;
            Some(next)
        } else {
            None
        }
    }
}
```

As a result, the wrapper is simple and contains no `unsafe` code.

## Advantages

This makes APIs safer to use, avoiding issues with lifetimes between types. See
[Object-Based APIs](./export.md) for more on the advantages and pitfalls this
avoids.

## Disadvantages

Often, wrapping types is quite difficult, and sometimes a Rust API compromise
would make things easier.

As an example, consider an iterator which does not efficiently implement
`nth()`. It would definitely be worth putting in special logic to make the
object handle iteration internally, or to support a different access pattern
efficiently that only the Foreign Function API will use.

### Trying to Wrap Iterators (and Failing)

To wrap any type of iterator into the API correctly, the wrapper would need to
do what a C version of the code would do: erase the lifetime of the iterator,
and manage it manually.

Suffice it to say, this is *incredibly* difficult.

Here is an illustration of just *one* pitfall.

A first version of `MySetWrapper` would look like this:

```rust,ignore
struct MySetWrapper {
    myset: MySet,
    iter_next: usize,
    // created from a transmuted Box<KeysIter + 'self>
    iterator: Option<NonNull<KeysIter<'static>>>,
}
```

With `transmute` being used to extend a lifetime, and a pointer to hide it, it's
ugly already. But it gets even worse: *any other operation can cause Rust
`undefined behaviour`*.

Consider that the `MySet` in the wrapper could be manipulated by other functions
during iteration, such as storing a new value to the key it was iterating over.
The API doesn't discourage this, and in fact some similar C libraries expect it.

A simple implementation of `myset_store` would be:

```rust,ignore
pub mod unsafe_module {

    // other module content

    pub fn myset_store(myset: *mut MySetWrapper, key: datum, value: datum) -> libc::c_int {
        // DO NOT USE THIS CODE. IT IS UNSAFE TO DEMONSTRATE A PROBLEM.

        let myset: &mut MySet = unsafe {
            // SAFETY: whoops, UB occurs in here!
            &mut (*myset).myset
        };

        /* ...check and cast key and value data... */

        match myset.store(casted_key, casted_value) {
            Ok(_) => 0,
            Err(e) => e.into(),
        }
    }
}
```

If the iterator exists when this function is called, we have violated one of
Rust's aliasing rules. According to Rust, the mutable reference in this block
must have *exclusive* access to the object. If the iterator simply exists, it's
not exclusive, so we have `undefined behaviour`! [^1]

To avoid this, we must have a way of ensuring that mutable reference really is
exclusive. That basically means clearing out the iterator's shared reference
while it exists, and then reconstructing it. In most cases, that will still be
less efficient than the C version.

Some may ask: how can C do this more efficiently? The answer is, it cheats.
Rust's aliasing rules are the problem, and C simply ignores them for its
pointers. In exchange, it is common to see code that is declared in the manual
as "not thread safe" under some or all circumstances. In fact, the
[GNU C library](https://manpages.debian.org/buster/manpages/attributes.7.en.html)
has an entire lexicon dedicated to concurrent behavior!

Rust would rather make everything memory safe all the time, for both safety and
optimizations that C code cannot attain. Being denied access to certain
shortcuts is the price Rust programmers need to pay.

[^1]: For the C programmers out there scratching their heads, the iterator need
    not be read *during* this code to cause the UB. The exclusivity rule also
    enables compiler optimizations which may cause inconsistent observations by
    the iterator's shared reference (e.g. stack spills or reordering
    instructions for efficiency). These observations may happen *any time after*
    the mutable reference is created.
