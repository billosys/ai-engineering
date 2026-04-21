r[macro]
# Macros

r[macro.intro]
The functionality and syntax of Rust can be extended with custom definitions called macros. They are given names, and invoked through a consistent syntax: `some_extension!(...)`.

There are two ways to define new macros:

* [Macros by Example] define new syntax in a higher-level, declarative way.
* [Procedural Macros] define function-like macros, custom derives, and custom attributes using functions that operate on input tokens.

r[macro.invocation]
## Macro invocation

r[macro.invocation.syntax]
```grammar,macros
MacroInvocation ->
    SimplePath `!` DelimTokenTree

DelimTokenTree ->
      `(` TokenTree* `)`
    | `[` TokenTree* `]`
    | `{` TokenTree* `}`

TokenTree ->
    Token _except [delimiters][lex.token.delim]_ | DelimTokenTree

MacroInvocationSemi ->
      SimplePath `!` `(` TokenTree* `)` `;`
    | SimplePath `!` `[` TokenTree* `]` `;`
    | SimplePath `!` `{` TokenTree* `}`
```

r[macro.invocation.intro]
A macro invocation expands a macro at compile time and replaces the invocation with the result of the macro. Macros may be invoked in the following situations:

r[macro.invocation.expr]
* [Expressions] and [statements]

r[macro.invocation.pattern]
* [Patterns]

r[macro.invocation.type]
* [Types]

r[macro.invocation.item]
* [Items] including [associated items]

r[macro.invocation.nested]
* [`macro_rules`] transcribers

r[macro.invocation.extern]
* [External blocks]

r[macro.invocation.item-statement]
When used as an item or a statement, the [MacroInvocationSemi] form is used where a semicolon is required at the end when not using curly braces. [Visibility qualifiers] are never allowed before a macro invocation or [`macro_rules`] definition.

```rust
// Used as an expression.
let x = vec![1,2,3];

// Used as a statement.
println!("Hello!");

// Used in a pattern.
macro_rules! pat {
    ($i:ident) => (Some($i))
}

if let pat!(x) = Some(1) {
    assert_eq!(x, 1);
}

// Used in a type.
macro_rules! Tuple {
    { $A:ty, $B:ty } => { ($A, $B) };
}

type N2 = Tuple!(i32, i32);

// Used as an item.
# use std::cell::RefCell;
thread_local!(static FOO: RefCell<u32> = RefCell::new(1));

// Used as an associated item.
macro_rules! const_maker {
    ($t:ty, $v:tt) => { const CONST: $t = $v; };
}
trait T {
    const_maker!{i32, 7}
}

// Macro calls within macros.
macro_rules! example {
    () => { println!("Macro call in a macro!") };
}
// Outer macro `example` is expanded, then inner macro `println` is expanded.
example!();
```

r[macro.invocation.name-resolution]

Macros invocations can be resolved via two kinds of scopes:

- Textual Scope
  - [Textual scope `macro_rules`](macros-by-example.md#r-macro.decl.scope.textual)
- Path-based scope
  - [Path-based scope `macro_rules`](macros-by-example.md#r-macro.decl.scope.path-based)
  - [Procedural macros]

[External blocks]: items/external-blocks.md
[Macros by Example]: macros-by-example.md
[Procedural Macros]: procedural-macros.md
[`macro_rules`]: macros-by-example.md
[associated items]: items/associated-items.md
[delimiters]: tokens.md#delimiters
[expressions]: expressions.md
[items]: items.md
[patterns]: patterns.md
[statements]: statements.md
[types]: types.md
[visibility qualifiers]: visibility-and-privacy.md


---

r[macro.decl]
# Macros by example

r[macro.decl.syntax]
```grammar,macros
MacroRulesDefinition ->
    `macro_rules` `!` IDENTIFIER MacroRulesDef

MacroRulesDef ->
      `(` MacroRules `)` `;`
    | `[` MacroRules `]` `;`
    | `{` MacroRules `}`

MacroRules ->
    MacroRule ( `;` MacroRule )* `;`?

MacroRule ->
    MacroMatcher `=>` MacroTranscriber

MacroMatcher ->
      `(` MacroMatch* `)`
    | `[` MacroMatch* `]`
    | `{` MacroMatch* `}`

MacroMatch ->
      Token _except `$` and [delimiters][lex.token.delim]_
    | MacroMatcher
    | `$` ( IDENTIFIER_OR_KEYWORD _except `crate`_ | RAW_IDENTIFIER ) `:` MacroFragSpec
    | `$` `(` MacroMatch+ `)` MacroRepSep? MacroRepOp

MacroFragSpec ->
      `block` | `expr` | `expr_2021` | `ident` | `item` | `lifetime` | `literal`
    | `meta` | `pat` | `pat_param` | `path` | `stmt` | `tt` | `ty` | `vis`

MacroRepSep -> Token _except [delimiters][lex.token.delim] and [MacroRepOp]_

MacroRepOp -> `*` | `+` | `?`

MacroTranscriber -> DelimTokenTree
```

r[macro.decl.intro]
`macro_rules` allows users to define syntax extension in a declarative way.  We call such extensions "macros by example" or simply "macros".

Each macro by example has a name, and one or more _rules_. Each rule has two parts: a _matcher_, describing the syntax that it matches, and a _transcriber_, describing the syntax that will replace a successfully matched invocation. Both the matcher and the transcriber must be surrounded by delimiters. Macros can expand to expressions, statements, items (including traits, impls, and foreign items), types, or patterns.

r[macro.decl.transcription]
## Transcribing

r[macro.decl.transcription.intro]
When a macro is invoked, the macro expander looks up macro invocations by name, and tries each macro rule in turn. It transcribes the first successful match; if this results in an error, then future matches are not tried.

r[macro.decl.transcription.lookahead]
When matching, no lookahead is performed; if the compiler cannot unambiguously determine how to parse the macro invocation one token at a time, then it is an error. In the following example, the compiler does not look ahead past the identifier to see if the following token is a `)`, even though that would allow it to parse the invocation unambiguously:

```rust,compile_fail
macro_rules! ambiguity {
    ($($i:ident)* $j:ident) => { };
}

ambiguity!(error); // Error: local ambiguity
```

r[macro.decl.transcription.syntax]
In both the matcher and the transcriber, the `$` token is used to invoke special behaviours from the macro engine (described below in [Metavariables] and [Repetitions]). Tokens that aren't part of such an invocation are matched and transcribed literally, with one exception. The exception is that the outer delimiters for the matcher will match any pair of delimiters. Thus, for instance, the matcher `(())` will match `{()}` but not `{{}}`. The character `$` cannot be matched or transcribed literally.

r[macro.decl.transcription.fragment]
### Forwarding a matched fragment

When forwarding a matched fragment to another macro-by-example, matchers in the second macro will see an opaque AST of the fragment type. The second macro can't use literal tokens to match the fragments in the matcher, only a fragment specifier of the same type. The `ident`, `lifetime`, and `tt` fragment types are an exception, and *can* be matched by literal tokens. The following illustrates this restriction:

```rust,compile_fail
macro_rules! foo {
    ($l:expr) => { bar!($l); }
// ERROR:               ^^ no rules expected this token in macro call
}

macro_rules! bar {
    (3) => {}
}

foo!(3);
```

The following illustrates how tokens can be directly matched after matching a `tt` fragment:

```rust
// compiles OK
macro_rules! foo {
    ($l:tt) => { bar!($l); }
}

macro_rules! bar {
    (3) => {}
}

foo!(3);
```

r[macro.decl.meta]
## Metavariables

r[macro.decl.meta.intro]
In the matcher, `$` _name_ `:` _fragment-specifier_ matches a Rust syntax fragment of the kind specified and binds it to the metavariable `$`_name_.

r[macro.decl.meta.specifier]
Valid fragment specifiers are:

  * `block`: a [BlockExpression]
  * `expr`: an [Expression]
  * `expr_2021`: an [Expression] except [UnderscoreExpression] and [ConstBlockExpression] (see [macro.decl.meta.edition2024])
  * `ident`: an [IDENTIFIER_OR_KEYWORD] except `_`, [RAW_IDENTIFIER], or [`$crate`]
  * `item`: an [Item]
  * `lifetime`: a [LIFETIME_TOKEN]
  * `literal`: matches `-`<sup>?</sup>[LiteralExpression]
  * `meta`: an [Attr], the contents of an attribute
  * `pat`: a [Pattern] (see [macro.decl.meta.edition2021])
  * `pat_param`: a [PatternNoTopAlt]
  * `path`: a [TypePath] style path
  * `stmt`: a [Statement][grammar-Statement] without the trailing semicolon (except for item statements that require semicolons)
  * `tt`: a [TokenTree]&nbsp;(a single [token] or tokens in matching delimiters `()`, `[]`, or `{}`)
  * `ty`: a [Type][grammar-Type]
  * `vis`: a possibly empty [Visibility] qualifier

r[macro.decl.meta.transcription]
In the transcriber, metavariables are referred to simply by `$`_name_, since the fragment kind is specified in the matcher. Metavariables are replaced with the syntax element that matched them. Metavariables can be transcribed more than once or not at all.

r[macro.decl.meta.dollar-crate]
The keyword metavariable [`$crate`] can be used to refer to the current crate.

r[macro.decl.meta.edition2021]
> [!EDITION-2021]
> Starting with the 2021 edition, `pat` fragment-specifiers match top-level or-patterns (that is, they accept [Pattern]).
>
> Before the 2021 edition, they match exactly the same fragments as `pat_param` (that is, they accept [PatternNoTopAlt]).
>
> The relevant edition is the one in effect for the `macro_rules!` definition.

r[macro.decl.meta.edition2024]
> [!EDITION-2024]
> Before the 2024 edition, `expr` fragment specifiers do not match [UnderscoreExpression] or [ConstBlockExpression] at the top level. They are allowed within subexpressions.
>
> The `expr_2021` fragment specifier exists to maintain backwards compatibility with editions before 2024.

r[macro.decl.repetition]
## Repetitions

r[macro.decl.repetition.intro]
In both the matcher and transcriber, repetitions are indicated by placing the tokens to be repeated inside `$(`…`)`, followed by a repetition operator, optionally with a separator token between.

r[macro.decl.repetition.separator]
The separator token can be any token other than a delimiter or one of the repetition operators, but `;` and `,` are the most common. For instance, `$( $i:ident ),*` represents any number of identifiers separated by commas. Nested repetitions are permitted.

r[macro.decl.repetition.operators]
The repetition operators are:

- `*` --- indicates any number of repetitions.
- `+` --- indicates any number but at least one.
- `?` --- indicates an optional fragment with zero or one occurrence.

r[macro.decl.repetition.optional-restriction]
Since `?` represents at most one occurrence, it cannot be used with a separator.

r[macro.decl.repetition.fragment]
The repeated fragment both matches and transcribes to the specified number of the fragment, separated by the separator token. Metavariables are matched to every repetition of their corresponding fragment. For instance, the `$( $i:ident ),*` example above matches `$i` to all of the identifiers in the list.

During transcription, additional restrictions apply to repetitions so that the compiler knows how to expand them properly:

1.  A metavariable must appear in exactly the same number, kind, and nesting order of repetitions in the transcriber as it did in the matcher. So for the matcher `$( $i:ident ),*`, the transcribers `=> { $i }`, `=> { $( $( $i )* )* }`, and `=> { $( $i )+ }` are all illegal, but `=> { $( $i );* }` is correct and replaces a comma-separated list of identifiers with a semicolon-separated list.
2.  Each repetition in the transcriber must contain at least one metavariable to decide how many times to expand it. If multiple metavariables appear in the same repetition, they must be bound to the same number of fragments. For instance, `( $( $i:ident ),* ; $( $j:ident ),* ) => (( $( ($i,$j) ),* ))` must bind the same number of `$i` fragments as `$j` fragments. This means that invoking the macro with `(a, b, c; d, e, f)` is legal and expands to `((a,d), (b,e), (c,f))`, but `(a, b, c; d, e)` is illegal because it does not have the same number. This requirement applies to every layer of nested repetitions.

r[macro.decl.scope]
## Scoping, exporting, and importing

r[macro.decl.scope.intro]
For historical reasons, the scoping of macros by example does not work entirely like items. Macros have two forms of scope: textual scope, and path-based scope. Textual scope is based on the order that things appear in source files, or even across multiple files, and is the default scoping. It is explained further below. Path-based scope works exactly the same way that item scoping does. The scoping, exporting, and importing of macros is controlled largely by attributes.

r[macro.decl.scope.unqualified]
When a macro is invoked by an unqualified identifier (not part of a multi-part path), it is first looked up in textual scoping. If this does not yield any results, then it is looked up in path-based scoping. If the macro's name is qualified with a path, then it is only looked up in path-based scoping.

<!-- ignore: requires external crates -->
```rust,ignore
use lazy_static::lazy_static; // Path-based import.

macro_rules! lazy_static { // Textual definition.
    (lazy) => {};
}

lazy_static!{lazy} // Textual lookup finds our macro first.
self::lazy_static!{} // Path-based lookup ignores our macro, finds imported one.
```

r[macro.decl.scope.textual]
### Textual scope

r[macro.decl.scope.textual.intro]
Textual scope is based largely on the order that things appear in source files, and works similarly to the scope of local variables declared with `let` except it also applies at the module level. When `macro_rules!` is used to define a macro, the macro enters the scope after the definition (note that it can still be used recursively, since names are looked up from the invocation site), up until its surrounding scope, typically a module, is closed. This can enter child modules and even span across multiple files:

<!-- ignore: requires external modules -->
```rust,ignore
//// src/lib.rs
mod has_macro {
    // m!{} // Error: m is not in scope.

    macro_rules! m {
        () => {};
    }
    m!{} // OK: appears after declaration of m.

    mod uses_macro;
}

// m!{} // Error: m is not in scope.

//// src/has_macro/uses_macro.rs

m!{} // OK: appears after declaration of m in src/lib.rs
```

r[macro.decl.scope.textual.shadow]
It is not an error to define a macro multiple times; the most recent declaration will shadow the previous one unless it has gone out of scope.

```rust
macro_rules! m {
    (1) => {};
}

m!(1);

mod inner {
    m!(1);

    macro_rules! m {
        (2) => {};
    }
    // m!(1); // Error: no rule matches '1'
    m!(2);

    macro_rules! m {
        (3) => {};
    }
    m!(3);
}

m!(1);
```

Macros can be declared and used locally inside functions as well, and work similarly:

```rust
fn foo() {
    // m!(); // Error: m is not in scope.
    macro_rules! m {
        () => {};
    }
    m!();
}

// m!(); // Error: m is not in scope.
```

r[macro.decl.scope.textual.shadow.path-based]
Textual scope name bindings for macros shadow path-based scope bindings to macros.

```rust
macro_rules! m2 {
    () => {
        println!("m2");
    };
}

// Resolves to path-based candidate from use declaration below.
m!(); // prints "m2\n"

// Introduce second candidate for `m` with textual scope.
//
// This shadows path-based candidate from below for the rest of this
// example.
macro_rules! m {
    () => {
        println!("m");
    };
}

// Introduce `m2` macro as path-based candidate.
//
// This item is in scope for this entire example, not just below the
// use declaration.
use m2 as m;

// Resolves to the textual macro candidate from above the use
// declaration.
m!(); // prints "m\n"
```

> [!NOTE]
> For areas where shadowing is not allowed, see [name resolution ambiguities].

r[macro.decl.scope.path-based]
### Path-based scope

r[macro.decl.scope.path-based.intro]
By default, a macro has no path-based scope. Macros can gain path-based scope in two ways:

- [Use declaration re-export]
- [`macro_export`]

r[macro.decl.scope.path.reexport]
Macros can be re-exported to give them path-based scope from a module other than the crate root.

```rust
mac::m!(); // OK: Path-based lookup finds `m` in the mac module.

mod mac {
    // Introduce macro `m` with textual scope.
    macro_rules! m {
        () => {};
    }

    // Reexport with path-based scope from within `m`'s textual scope.
    pub(crate) use m;
}
```

r[macro.decl.scope.path-based.visibility]
Macros have an implicit visibility of `pub(crate)`. `#[macro_export]` changes the implicit visibility to `pub`.

```rust
// Implicit visibility is `pub(crate)`.
macro_rules! private_m {
    () => {};
}

// Implicit visibility is `pub`.
#[macro_export]
macro_rules! pub_m {
    () => {};
}

pub(crate) use private_m as private_macro; // OK.
pub use pub_m as pub_macro; // OK.
```

```rust,compile_fail,E0364
# // Implicit visibility is `pub(crate)`.
# macro_rules! private_m {
#     () => {};
# }
#
# // Implicit visibility is `pub`.
# #[macro_export]
# macro_rules! pub_m {
#     () => {};
# }
#
# pub(crate) use private_m as private_macro; // OK.
# pub use pub_m as pub_macro; // OK.
#
pub use private_m; // ERROR: `private_m` is only public within
                   // the crate and cannot be re-exported outside.
```

<!-- template:attributes -->
r[macro.decl.scope.macro_use]
### The `macro_use` attribute

r[macro.decl.scope.macro_use.intro]
The *`macro_use` [attribute][attributes]* has two purposes: it may be used on modules to extend the scope of macros defined within them, and it may be used on [`extern crate`][items.extern-crate] to import macros from another crate into the [`macro_use` prelude].

> [!EXAMPLE]
> ```rust
> #[macro_use]
> mod inner {
>     macro_rules! m {
>         () => {};
>     }
> }
> m!();
> ```
>
> ```rust,ignore
> #[macro_use]
> extern crate log;
> ```

r[macro.decl.scope.macro_use.syntax]
When used on modules, the `macro_use` attribute uses the [MetaWord] syntax.

When used on `extern crate`, it uses the [MetaWord] and [MetaListIdents] syntaxes. For more on how these syntaxes may be used, see [macro.decl.scope.macro_use.prelude].

r[macro.decl.scope.macro_use.allowed-positions]
The `macro_use` attribute may be applied to modules or `extern crate`.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[macro.decl.scope.macro_use.extern-crate-self]
The `macro_use` attribute may not be used on [`extern crate self`].

r[macro.decl.scope.macro_use.duplicates]
The `macro_use` attribute may be used any number of times on a form.

Multiple instances of `macro_use` in the [MetaListIdents] syntax may be specified. The union of all specified macros will be imported.

> [!NOTE]
> On modules, `rustc` lints against any [MetaWord] `macro_use` attributes following the first.
>
> On `extern crate`, `rustc` lints against any `macro_use` attributes that have no effect due to not importing any macros not already imported by another `macro_use` attribute. If two or more [MetaListIdents] `macro_use` attributes import the same macro, the first is linted against. If any [MetaWord] `macro_use` attributes are present, all [MetaListIdents] `macro_use` attributes are linted against. If two or more [MetaWord] `macro_use` attributes are present, the ones following the first are linted against.

r[macro.decl.scope.macro_use.mod-decl]
When `macro_use` is used on a module, the module's macro scope extends beyond the module's lexical scope.

> [!EXAMPLE]
> ```rust
> #[macro_use]
> mod inner {
>     macro_rules! m {
>         () => {};
>     }
> }
> m!(); // OK
> ```

r[macro.decl.scope.macro_use.prelude]
Specifying `macro_use` on an `extern crate` declaration in the crate root imports exported macros from that crate.

Macros imported this way are imported into the [`macro_use` prelude], not textually, which means that they can be shadowed by any other name. Macros imported by `macro_use` can be used before the import statement.

> [!NOTE]
> `rustc` currently prefers the last macro imported in case of conflict. Don't rely on this. This behavior is unusual, as imports in Rust are generally order-independent. This behavior of `macro_use` may change in the future.
>
> For details, see [Rust issue #148025](https://github.com/rust-lang/rust/issues/148025).

When using the [MetaWord] syntax, all exported macros are imported. When using the [MetaListIdents] syntax, only the specified macros are imported.

> [!EXAMPLE]
> <!-- ignore: requires external crates -->
> ```rust,ignore
> #[macro_use(lazy_static)] // Or `#[macro_use]` to import all macros.
> extern crate lazy_static;
>
> lazy_static!{}
> // self::lazy_static!{} // ERROR: lazy_static is not defined in `self`.
> ```

r[macro.decl.scope.macro_use.export]
Macros to be imported with `macro_use` must be exported with [`macro_export`][macro.decl.scope.macro_export].

<!-- template:attributes -->
r[macro.decl.scope.macro_export]
### The `macro_export` attribute

r[macro.decl.scope.macro_export.intro]
The *`macro_export` [attribute][attributes]* exports the macro from the crate and makes it available in the root of the crate for path-based resolution.

> [!EXAMPLE]
> ```rust
> self::m!();
> //  ^^^^ OK: Path-based lookup finds `m` in the current module.
> m!(); // As above.
>
> mod inner {
>     super::m!();
>     crate::m!();
> }
>
> mod mac {
>     #[macro_export]
>     macro_rules! m {
>         () => {};
>     }
> }
> ```

r[macro.decl.scope.macro_export.syntax]
The `macro_export` attribute uses the [MetaWord] and [MetaListIdents] syntaxes. With the [MetaListIdents] syntax, it accepts a single [`local_inner_macros`][macro.decl.scope.macro_export.local_inner_macros] value.

r[macro.decl.scope.macro_export.allowed-positions]
The `macro_export` attribute may be applied to `macro_rules` definitions.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[macro.decl.scope.macro_export.duplicates]
Only the first use of `macro_export` on a macro has effect.

> [!NOTE]
> `rustc` lints against any use following the first.

r[macro.decl.scope.macro_export.path-based]
By default, macros only have [textual scope][macro.decl.scope.textual] and cannot be resolved by path. When the `macro_export` attribute is used, the macro is made available in the crate root and can be referred to by its path.

> [!EXAMPLE]
> Without `macro_export`, macros only have textual scope, so path-based resolution of the macro fails.
>
> ```rust,compile_fail,E0433
> macro_rules! m {
>     () => {};
> }
> self::m!(); // ERROR
> crate::m!(); // ERROR
> # fn main() {}
> ```
>
> With `macro_export`, path-based resolution works.
>
> ```rust
> #[macro_export]
> macro_rules! m {
>     () => {};
> }
> self::m!(); // OK
> crate::m!(); // OK
> # fn main() {}
> ```

r[macro.decl.scope.macro_export.export]
The `macro_export` attribute causes a macro to be exported from the crate root so that it can be referred to in other crates by path.

> [!EXAMPLE]
> Given the following in a `log` crate:
>
> ```rust
> #[macro_export]
> macro_rules! warn {
>     ($message:expr) => { eprintln!("WARN: {}", $message) };
> }
> ```
>
> From another crate, you can refer to the macro by path:
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> fn main() {
>     log::warn!("example warning");
> }
> ```

r[macro.decl.scope.macro_export.macro_use]
`macro_export` allows the use of [`macro_use`][macro.decl.scope.macro_use] on an `extern crate` to import the macro into the [`macro_use` prelude].

> [!EXAMPLE]
> Given the following in a `log` crate:
>
> ```rust
> #[macro_export]
> macro_rules! warn {
>     ($message:expr) => { eprintln!("WARN: {}", $message) };
> }
> ```
>
> Using `macro_use` in a dependent crate allows you to use the macro from the prelude:
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> #[macro_use]
> extern crate log;
>
> pub mod util {
>     pub fn do_thing() {
>         // Resolved via macro prelude.
>         warn!("example warning");
>     }
> }
> ```

r[macro.decl.scope.macro_export.local_inner_macros]
Adding `local_inner_macros` to the `macro_export` attribute causes all single-segment macro invocations in the macro definition to have an implicit `$crate::` prefix.

> [!NOTE]
> This is intended primarily as a tool to migrate code written before [`$crate`] was added to the language to work with Rust 2018's path-based imports of macros. Its use is discouraged in new code.

> [!EXAMPLE]
> ```rust
> #[macro_export(local_inner_macros)]
> macro_rules! helped {
>     () => { helper!() } // Automatically converted to $crate::helper!().
> }
>
> #[macro_export]
> macro_rules! helper {
>     () => { () }
> }
> ```

r[macro.decl.hygiene]
## Hygiene

r[macro.decl.hygiene.intro]
Macros by example have _mixed-site hygiene_. This means that [loop labels], [block labels], and local variables are looked up at the macro definition site while other symbols are looked up at the macro invocation site. For example:

```rust
let x = 1;
fn func() {
    unreachable!("this is never called")
}

macro_rules! check {
    () => {
        assert_eq!(x, 1); // Uses `x` from the definition site.
        func();           // Uses `func` from the invocation site.
    };
}

{
    let x = 2;
    fn func() { /* does not panic */ }
    check!();
}
```

Labels and local variables defined in macro expansion are not shared between invocations, so this code doesn’t compile:

```rust,compile_fail,E0425
macro_rules! m {
    (define) => {
        let x = 1;
    };
    (refer) => {
        dbg!(x);
    };
}

m!(define);
m!(refer);
```

r[macro.decl.hygiene.crate]
A special case is the `$crate` metavariable. It refers to the crate defining the macro, and can be used at the start of the path to look up items or macros which are not in scope at the invocation site.

<!-- ignore: requires external crates -->
```rust,ignore
//// Definitions in the `helper_macro` crate.
#[macro_export]
macro_rules! helped {
    // () => { helper!() } // This might lead to an error due to 'helper' not being in scope.
    () => { $crate::helper!() }
}

#[macro_export]
macro_rules! helper {
    () => { () }
}

//// Usage in another crate.
// Note that `helper_macro::helper` is not imported!
use helper_macro::helped;

fn unit() {
    helped!();
}
```

Note that, because `$crate` refers to the current crate, it must be used with a fully qualified module path when referring to non-macro items:

```rust
pub mod inner {
    #[macro_export]
    macro_rules! call_foo {
        () => { $crate::inner::foo() };
    }

    pub fn foo() {}
}
```

r[macro.decl.hygiene.vis]
Additionally, even though `$crate` allows a macro to refer to items within its own crate when expanding, its use has no effect on visibility. An item or macro referred to must still be visible from the invocation site. In the following example, any attempt to invoke `call_foo!()` from outside its crate will fail because `foo()` is not public.

```rust
#[macro_export]
macro_rules! call_foo {
    () => { $crate::foo() };
}

fn foo() {}
```

> [!NOTE]
> Prior to Rust 1.30, `$crate` and [`local_inner_macros`][macro.decl.scope.macro_export.local_inner_macros] were unsupported. They were added alongside [path-based imports of macros][macro.decl.scope.macro_export], to ensure that helper macros did not need to be manually imported by users of a macro-exporting crate. Crates written for earlier versions of Rust that use helper macros need to be modified to use `$crate` or `local_inner_macros` to work well with path-based imports.

r[macro.decl.follow-set]
## Follow-set ambiguity restrictions

r[macro.decl.follow-set.intro]
The parser used by the macro system is reasonably powerful, but it is limited in order to prevent ambiguity in current or future versions of the language.

r[macro.decl.follow-set.token-restriction]
In particular, in addition to the rule about ambiguous expansions, a nonterminal matched by a metavariable must be followed by a token which has been decided can be safely used after that kind of match.

As an example, a macro matcher like `$i:expr [ , ]` could in theory be accepted in Rust today, since `[,]` cannot be part of a legal expression and therefore the parse would always be unambiguous. However, because `[` can start trailing expressions, `[` is not a character which can safely be ruled out as coming after an expression. If `[,]` were accepted in a later version of Rust, this matcher would become ambiguous or would misparse, breaking working code. Matchers like `$i:expr,` or `$i:expr;` would be legal, however, because `,` and `;` are legal expression separators. The specific rules are:

r[macro.decl.follow-set.token-expr-stmt]
  * `expr` and `stmt` may only be followed by one of: `=>`, `,`, or `;`.

r[macro.decl.follow-set.token-pat_param]
  * `pat_param` may only be followed by one of: `=>`, `,`, `=`, `|`, `if`, or `in`.

r[macro.decl.follow-set.token-pat]
  * `pat` may only be followed by one of: `=>`, `,`, `=`, `if`, or `in`.

r[macro.decl.follow-set.token-path-ty]
  * `path` and `ty` may only be followed by one of: `=>`, `,`, `=`, `|`, `;`, `:`, `>`, `>>`, `[`, `{`, `as`, `where`, or a macro variable of `block` fragment specifier.

r[macro.decl.follow-set.token-vis]
  * `vis` may only be followed by one of: `,`, an identifier other than a non-raw `priv`, any token that can begin a type, or a metavariable with a `ident`, `ty`, or `path` fragment specifier.

r[macro.decl.follow-set.token-other]
  * All other fragment specifiers have no restrictions.

r[macro.decl.follow-set.edition2021]
> [!EDITION-2021]
> Before the 2021 edition, `pat` may also be followed by `|`.

r[macro.decl.follow-set.repetition]
When repetitions are involved, then the rules apply to every possible number of expansions, taking separators into account. This means:

  * If the repetition includes a separator, that separator must be able to follow the contents of the repetition.
  * If the repetition can repeat multiple times (`*` or `+`), then the contents must be able to follow themselves.
  * The contents of the repetition must be able to follow whatever comes before, and whatever comes after must be able to follow the contents of the repetition.
  * If the repetition can match zero times (`*` or `?`), then whatever comes after must be able to follow whatever comes before.

For more detail, see the [formal specification].

[Metavariables]: #metavariables
[Repetitions]: #repetitions
[`macro_export`]: #the-macro_export-attribute
[`$crate`]: macro.decl.hygiene.crate
[`extern crate self`]: items.extern-crate.self
[`macro_use` prelude]: names/preludes.md#macro_use-prelude
[block labels]: expr.loop.block-labels
[delimiters]: tokens.md#delimiters
[formal specification]: macro-ambiguity.md
[loop labels]: expressions/loop-expr.md#loop-labels
[name resolution ambiguities]: names/name-resolution.md#r-names.resolution.expansion.imports.ambiguity
[token]: tokens.md
[use declaration re-export]: items/use-declarations.md#use-visibility


---

r[macro.proc]
# Procedural macros

r[macro.proc.intro]
*Procedural macros* allow creating syntax extensions as execution of a function. Procedural macros come in one of three flavors:

* [Function-like macros] - `custom!(...)`
* [Derive macros] - `#[derive(CustomDerive)]`
* [Attribute macros] - `#[CustomAttribute]`

Procedural macros allow you to run code at compile time that operates over Rust syntax, both consuming and producing Rust syntax. You can sort of think of procedural macros as functions from an AST to another AST.

r[macro.proc.def]
Procedural macros must be defined in the root of a crate with the [crate type] of `proc-macro`. The macros may not be used from the crate where they are defined, and can only be used when imported in another crate.

> [!NOTE]
> When using Cargo, Procedural macro crates are defined with the `proc-macro` key in your manifest:
>
> ```toml
> [lib]
> proc-macro = true
> ```

r[macro.proc.result]
As functions, they must either return syntax, panic, or loop endlessly. Returned syntax either replaces or adds the syntax depending on the kind of procedural macro. Panics are caught by the compiler and are turned into a compiler error. Endless loops are not caught by the compiler which hangs the compiler.

Procedural macros run during compilation, and thus have the same resources that the compiler has. For example, standard input, error, and output are the same that the compiler has access to. Similarly, file access is the same. Because of this, procedural macros have the same security concerns that [Cargo's build scripts] have.

r[macro.proc.error]
Procedural macros have two ways of reporting errors. The first is to panic. The second is to emit a [`compile_error`] macro invocation.

r[macro.proc.proc_macro-crate]
## The `proc_macro` crate

r[macro.proc.proc_macro-crate.intro]
Procedural macro crates almost always will link to the compiler-provided [`proc_macro` crate]. The `proc_macro` crate provides types required for writing procedural macros and facilities to make it easier.

r[macro.proc.proc_macro-crate.token-stream]
This crate primarily contains a [`TokenStream`] type. Procedural macros operate over *token streams* instead of AST nodes, which is a far more stable interface over time for both the compiler and for procedural macros to target. A *token stream* is roughly equivalent to `Vec<TokenTree>` where a `TokenTree` can roughly be thought of as lexical token. For example `foo` is an `Ident` token, `.` is a `Punct` token, and `1.2` is a `Literal` token. The `TokenStream` type, unlike `Vec<TokenTree>`, is cheap to clone.

r[macro.proc.proc_macro-crate.span]
All tokens have an associated `Span`. A `Span` is an opaque value that cannot be modified but can be manufactured. `Span`s represent an extent of source code within a program and are primarily used for error reporting. While you cannot modify a `Span` itself, you can always change the `Span` *associated* with any token, such as through getting a `Span` from another token.

r[macro.proc.hygiene]
## Procedural macro hygiene

Procedural macros are *unhygienic*. This means they behave as if the output token stream was simply written inline to the code it's next to. This means that it's affected by external items and also affects external imports.

Macro authors need to be careful to ensure their macros work in as many contexts as possible given this limitation. This often includes using absolute paths to items in libraries (for example, `::std::option::Option` instead of `Option`) or by ensuring that generated functions have names that are unlikely to clash with other functions (like `__internal_foo` instead of `foo`).

<!-- TODO: rule name needs improvement -->
<!-- template:attributes -->
r[macro.proc.proc_macro]
## The `proc_macro` attribute

r[macro.proc.proc_macro.intro]
The *`proc_macro` [attribute][attributes]* defines a [function-like][macro.invocation] procedural macro.

> [!EXAMPLE]
> This macro definition ignores its input and emits a function `answer` into its scope.
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> # #![crate_type = "proc-macro"]
> extern crate proc_macro;
> use proc_macro::TokenStream;
>
> #[proc_macro]
> pub fn make_answer(_item: TokenStream) -> TokenStream {
>     "fn answer() -> u32 { 42 }".parse().unwrap()
> }
> ```
>
> We can use it in a binary crate to print "42" to standard output.
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> extern crate proc_macro_examples;
> use proc_macro_examples::make_answer;
>
> make_answer!();
>
> fn main() {
>     println!("{}", answer());
> }
> ```

r[macro.proc.proc_macro.syntax]
The `proc_macro` attribute uses the [MetaWord] syntax.

r[macro.proc.proc_macro.allowed-positions]
The `proc_macro` attribute may only be applied to a `pub` function of type `fn(TokenStream) -> TokenStream` where [`TokenStream`] comes from the [`proc_macro` crate]. It must have the ["Rust" ABI][items.fn.extern]. No other function qualifiers are allowed. It must be located in the root of the crate.

r[macro.proc.proc_macro.duplicates]
The `proc_macro` attribute may only be specified once on a function.

r[macro.proc.proc_macro.namespace]
The `proc_macro` attribute publicly defines the macro in the [macro namespace] in the root of the crate with the same name as the function.

r[macro.proc.proc_macro.behavior]
A function-like macro invocation of a function-like procedural macro will pass what is inside the delimiters of the macro invocation as the input [`TokenStream`] argument and replace the entire macro invocation with the output [`TokenStream`] of the function.

r[macro.proc.proc_macro.invocation]
Function-like procedural macros may be invoked in any macro invocation position, which includes:

- [Statements]
- [Expressions]
- [Patterns]
- [Type expressions]
- [Item] positions, including items in [`extern` blocks]
- Inherent and trait [implementations]
- [Trait definitions]

<!-- template:attributes -->
r[macro.proc.derive]
## The `proc_macro_derive` attribute

r[macro.proc.derive.intro]
Applying the *`proc_macro_derive` [attribute]* to a function defines a *derive macro* that can be invoked by the [`derive` attribute]. These macros are given the token stream of a [struct], [enum], or [union] definition and can emit new [items] after it. They can also declare and use [derive macro helper attributes].

> [!EXAMPLE]
> This derive macro ignores its input and appends tokens that define a function.
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> # #![crate_type = "proc-macro"]
> extern crate proc_macro;
> use proc_macro::TokenStream;
>
> #[proc_macro_derive(AnswerFn)]
> pub fn derive_answer_fn(_item: TokenStream) -> TokenStream {
>     "fn answer() -> u32 { 42 }".parse().unwrap()
> }
> ```
>
> To use it, we might write:
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> extern crate proc_macro_examples;
> use proc_macro_examples::AnswerFn;
>
> #[derive(AnswerFn)]
> struct Struct;
>
> fn main() {
>     assert_eq!(42, answer());
> }
> ```

r[macro.proc.derive.syntax]
The syntax for the `proc_macro_derive` attribute is:

```grammar,attributes
@root ProcMacroDeriveAttribute ->
    `proc_macro_derive` `(` DeriveMacroName ( `,` DeriveMacroAttributes )? `,`? `)`

DeriveMacroName -> IDENTIFIER

DeriveMacroAttributes ->
    `attributes` `(` ( IDENTIFIER (`,` IDENTIFIER)* `,`?)? `)`
```

The name of the derive macro is given by [DeriveMacroName]. The optional `attributes` argument is described in [macro.proc.derive.attributes].

r[macro.proc.derive.allowed-positions]
The `proc_macro_derive` attribute may only be applied to a `pub` function with the [Rust ABI][items.fn.extern] defined in the root of the crate with a type of `fn(TokenStream) -> TokenStream`  where [`TokenStream`] comes from the [`proc_macro` crate]. The function may be `const` and may use `extern` to explicitly specify the Rust ABI, but it may not use any other [qualifiers][FunctionQualifiers] (e.g. it may not be `async` or `unsafe`).

r[macro.proc.derive.duplicates]
The `proc_macro_derive` attribute may be used only once on a function.

r[macro.proc.derive.namespace]
The `proc_macro_derive` attribute publicly defines the derive macro in the [macro namespace] in the root of the crate.

r[macro.proc.derive.output]
The input [`TokenStream`] is the token stream of the item to which the `derive` attribute is applied. The output [`TokenStream`] must be a (possibly empty) set of items. These items are appended following the input item within the same [module] or [block].

r[macro.proc.derive.attributes]
### Derive macro helper attributes

r[macro.proc.derive.attributes.intro]
Derive macros can declare *derive macro helper attributes* to be used within the scope of the [item] to which the derive macro is applied. These [attributes] are [inert]. While their purpose is to be used by the macro that declared them, they can be seen by any macro.

r[macro.proc.derive.attributes.decl]
A helper attribute for a derive macro is declared by adding its identifier to the `attributes` list in the `proc_macro_derive` attribute.

> [!EXAMPLE]
> This declares a helper attribute and then ignores it.
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> # #![crate_type="proc-macro"]
> # extern crate proc_macro;
> # use proc_macro::TokenStream;
> #
> #[proc_macro_derive(WithHelperAttr, attributes(helper))]
> pub fn derive_with_helper_attr(_item: TokenStream) -> TokenStream {
>     TokenStream::new()
> }
> ```
>
> To use it, we might write:
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> #[derive(WithHelperAttr)]
> struct Struct {
>     #[helper] field: (),
> }
> ```

r[macro.proc.derive.attributes.scope]
When a derive macro invocation is applied to an item, the helper attributes introduced by that derive macro become in scope 1) for attributes that are applied to that item and are applied lexically after the derive macro invocation and 2) for attributes that are applied to fields and variants inside of the item.

> [!NOTE]
> rustc currently allows derive helpers to be used before the macro that introduces them. Such derive helpers used out of order may not shadow other attribute macros. This behavior is deprecated and slated for removal.
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> #[helper] // Deprecated, hard error in the future.
> #[derive(WithHelperAttr)]
> struct Struct {
>     field: (),
> }
> ```
>
> For more details, see [Rust issue #79202](https://github.com/rust-lang/rust/issues/79202).


<!-- template:attributes -->
r[macro.proc.attribute]
## The `proc_macro_attribute` attribute

r[macro.proc.attribute.intro]
The *`proc_macro_attribute` [attribute][attributes]* defines an *attribute macro* which can be used as an [outer attribute][attributes].

> [!EXAMPLE]
> This attribute macro takes the input stream and emits it as-is, effectively being a no-op attribute.
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> # #![crate_type = "proc-macro"]
> # extern crate proc_macro;
> # use proc_macro::TokenStream;
>
> #[proc_macro_attribute]
> pub fn return_as_is(_attr: TokenStream, item: TokenStream) -> TokenStream {
>     item
> }
> ```

> [!EXAMPLE]
> This shows, in the output of the compiler, the stringified [`TokenStream`s] that attribute macros see.
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> // my-macro/src/lib.rs
> # extern crate proc_macro;
> # use proc_macro::TokenStream;
> #[proc_macro_attribute]
> pub fn show_streams(attr: TokenStream, item: TokenStream) -> TokenStream {
>     println!("attr: \"{attr}\"");
>     println!("item: \"{item}\"");
>     item
> }
> ```
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> // src/lib.rs
> extern crate my_macro;
>
> use my_macro::show_streams;
>
> // Example: Basic function.
> #[show_streams]
> fn invoke1() {}
> // out: attr: ""
> // out: item: "fn invoke1() {}"
>
> // Example: Attribute with input.
> #[show_streams(bar)]
> fn invoke2() {}
> // out: attr: "bar"
> // out: item: "fn invoke2() {}"
>
> // Example: Multiple tokens in the input.
> #[show_streams(multiple => tokens)]
> fn invoke3() {}
> // out: attr: "multiple => tokens"
> // out: item: "fn invoke3() {}"
>
> // Example: Delimiters in the input.
> #[show_streams { delimiters }]
> fn invoke4() {}
> // out: attr: "delimiters"
> // out: item: "fn invoke4() {}"
> ```

r[macro.proc.attribute.syntax]
The `proc_macro_attribute` attribute uses the [MetaWord] syntax.

r[macro.proc.attribute.allowed-positions]
The `proc_macro_attribute` attribute may only be applied to a `pub` function of type `fn(TokenStream, TokenStream) -> TokenStream` where [`TokenStream`] comes from the [`proc_macro` crate]. It must have the ["Rust" ABI][items.fn.extern]. No other function qualifiers are allowed. It must be located in the root of the crate.

r[macro.proc.attribute.duplicates]
The `proc_macro_attribute` attribute may only be specified once on a function.

r[macro.proc.attribute.namespace]
The `proc_macro_attribute` attribute defines the attribute in the [macro namespace] in the root of the crate with the same name as the function.

r[macro.proc.attribute.use-positions]
Attribute macros can only be used on:

- [Items]
- Items in [`extern` blocks]
- Inherent and trait [implementations]
- [Trait definitions]

r[macro.proc.attribute.behavior]
The first [`TokenStream`] parameter is the delimited token tree following the attribute's name but not including the outer delimiters. If the applied attribute contains only the attribute name or the attribute name followed by empty delimiters, the [`TokenStream`] is empty.

The second [`TokenStream`] is the rest of the [item], including other [attributes] on the [item].

The item to which the attribute is applied is replaced by the zero or more items in the returned [`TokenStream`].

r[macro.proc.token]
## Declarative macro tokens and procedural macro tokens

r[macro.proc.token.intro]
Declarative `macro_rules` macros and procedural macros use similar, but different definitions for tokens (or rather [`TokenTree`s].)

r[macro.proc.token.macro_rules]
Token trees in `macro_rules` (corresponding to `tt` matchers) are defined as
- Delimited groups (`(...)`, `{...}`, etc)
- All operators supported by the language, both single-character and multi-character ones (`+`, `+=`).
    - Note that this set doesn't include the single quote `'`.
- Literals (`"string"`, `1`, etc)
    - Note that negation (e.g. `-1`) is never a part of such literal tokens, but a separate operator token.
- Identifiers, including keywords (`ident`, `r#ident`, `fn`)
- Lifetimes (`'ident`)
- Metavariable substitutions in `macro_rules` (e.g. `$my_expr` in `macro_rules! mac { ($my_expr: expr) => { $my_expr } }` after the `mac`'s expansion, which will be considered a single token tree regardless of the passed expression)

r[macro.proc.token.tree]
Token trees in procedural macros are defined as
- Delimited groups (`(...)`, `{...}`, etc)
- All punctuation characters used in operators supported by the language (`+`, but not `+=`), and also the single quote `'` character (typically used in lifetimes, see below for lifetime splitting and joining behavior)
- Literals (`"string"`, `1`, etc)
    - Negation (e.g. `-1`) is supported as a part of integer and floating point literals.
- Identifiers, including keywords (`ident`, `r#ident`, `fn`)

r[macro.proc.token.conversion.intro]
Mismatches between these two definitions are accounted for when token streams are passed to and from procedural macros. Note that the conversions below may happen lazily, so they might not happen if the tokens are not actually inspected.

r[macro.proc.token.conversion.to-proc_macro]
When passed to a proc-macro
- All multi-character operators are broken into single characters.
- Lifetimes are broken into a `'` character and an identifier.
- The keyword metavariable [`$crate`] is passed as a single identifier.
- All other metavariable substitutions are represented as their underlying token streams.
    - Such token streams may be wrapped into delimited groups ([`Group`]) with implicit delimiters ([`Delimiter::None`]) when it's necessary for preserving parsing priorities.
    - `tt` and `ident` substitutions are never wrapped into such groups and always represented as their underlying token trees.

r[macro.proc.token.conversion.from-proc_macro]
When emitted from a proc macro
- Punctuation characters are glued into multi-character operators when applicable.
- Single quotes `'` joined with identifiers are glued into lifetimes.
- Negative literals are converted into two tokens (the `-` and the literal) possibly wrapped into a delimited group ([`Group`]) with implicit delimiters ([`Delimiter::None`]) when it's necessary for preserving parsing priorities.

r[macro.proc.token.doc-comment]
Note that neither declarative nor procedural macros support doc comment tokens (e.g. `/// Doc`), so they are always converted to token streams representing their equivalent `#[doc = r"str"]` attributes when passed to macros.

[Attribute macros]: #the-proc_macro_attribute-attribute
[Cargo's build scripts]: ../cargo/reference/build-scripts.html
[Derive macros]: macro.proc.derive
[Function-like macros]: #the-proc_macro-attribute
[`$crate`]: macro.decl.hygiene.crate
[`Delimiter::None`]: proc_macro::Delimiter::None
[`Group`]: proc_macro::Group
[`TokenStream`]: proc_macro::TokenStream
[`TokenStream`s]: proc_macro::TokenStream
[`TokenTree`s]: proc_macro::TokenTree
[`derive` attribute]: attributes/derive.md
[`extern` blocks]: items/external-blocks.md
[`macro_rules`]: macros-by-example.md
[`proc_macro` crate]: proc_macro
[attribute]: attributes.md
[attributes]: attributes.md
[block]: expressions/block-expr.md
[crate type]: linkage.md
[derive macro helper attributes]: #derive-macro-helper-attributes
[enum]: items/enumerations.md
[expressions]: expressions.md
[function]: items/functions.md
[implementations]: items/implementations.md
[inert]: attributes.md#active-and-inert-attributes
[item]: items.md
[items]: items.md
[macro namespace]: names/namespaces.md
[module]: items/modules.md
[patterns]: patterns.md
[public]: visibility-and-privacy.md
[statements]: statements.md
[struct]: items/structs.md
[trait definitions]: items/traits.md
[type expressions]: types.md#type-expressions
[type]: types.md
[union]: items/unions.md
